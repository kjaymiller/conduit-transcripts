"""Progress tracking for ingestion tasks."""

import logging
import uuid
from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field

from conduit_transcripts.database.postgres import VectorDatabase
from conduit_transcripts.models.ingestion import IngestionJob, IngestionFile, TaskStatus

logger = logging.getLogger(__name__)


class FileProgressSchema(BaseModel):
    """Progress of a single file ingestion (Pydantic model for API)."""
    filename: str
    status: TaskStatus = TaskStatus.PENDING
    episode_number: Optional[int] = None
    chunks_processed: int = 0
    total_chunks: Optional[int] = None
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class IngestionJobSchema(BaseModel):
    """A job containing multiple file ingestions (Pydantic model for API)."""
    job_id: str
    status: TaskStatus = TaskStatus.PENDING
    files: Dict[str, FileProgressSchema] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None

    @property
    def progress(self) -> float:
        """Calculate overall progress percentage."""
        if not self.files:
            return 0.0
        completed = sum(1 for f in self.files.values() if f.status in (TaskStatus.COMPLETED, TaskStatus.FAILED))
        return (completed / len(self.files)) * 100


class IngestionTracker:
    """Tracker for ingestion jobs using database persistence."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IngestionTracker, cls).__new__(cls)
        return cls._instance

    def create_job(self, filenames: List[str]) -> str:
        """Create a new ingestion job in the database."""
        db = VectorDatabase()
        session = db.Session()
        
        try:
            job_id = str(uuid.uuid4())
            job = IngestionJob(job_id=job_id, status=TaskStatus.PENDING)
            session.add(job)
            
            for filename in filenames:
                file_record = IngestionFile(
                    job_id=job_id,
                    filename=filename,
                    status=TaskStatus.PENDING
                )
                session.add(file_record)
            
            session.commit()
            return job_id
        except Exception as e:
            session.rollback()
            logger.error(f"Error creating ingestion job: {e}")
            raise
        finally:
            session.close()

    def get_job(self, job_id: str) -> Optional[IngestionJobSchema]:
        """Get job details from database."""
        db = VectorDatabase()
        session = db.Session()
        
        try:
            job = session.query(IngestionJob).filter_by(job_id=job_id).first()
            if not job:
                return None
            
            # Convert SQLAlchemy model to Pydantic schema
            files_dict = {}
            for f in job.files:
                files_dict[f.filename] = FileProgressSchema(
                    filename=f.filename,
                    status=f.status,
                    episode_number=f.episode_number,
                    chunks_processed=f.chunks_processed,
                    total_chunks=f.total_chunks,
                    error=f.error,
                    started_at=f.started_at,
                    completed_at=f.completed_at
                )
                
            return IngestionJobSchema(
                job_id=job.job_id,
                status=job.status,
                files=files_dict,
                created_at=job.created_at,
                completed_at=job.completed_at
            )
        finally:
            session.close()

    def update_file_status(
        self, 
        job_id: str, 
        filename: str, 
        status: TaskStatus, 
        error: Optional[str] = None,
        episode_number: Optional[int] = None,
        chunks_count: Optional[int] = None
    ):
        """Update status of a specific file in database."""
        db = VectorDatabase()
        session = db.Session()
        
        try:
            # Find the file record
            # Joining with job to ensure job_id matches
            file_record = (
                session.query(IngestionFile)
                .join(IngestionJob)
                .filter(IngestionJob.job_id == job_id, IngestionFile.filename == filename)
                .first()
            )
            
            if not file_record:
                logger.warning(f"File record not found for job {job_id}, file {filename}")
                return
            
            file_record.status = status
            
            if error:
                file_record.error = error
                
            if episode_number:
                file_record.episode_number = episode_number
                
            if chunks_count is not None:
                file_record.total_chunks = chunks_count
                file_record.chunks_processed = chunks_count
                
            if status == TaskStatus.PROCESSING and not file_record.started_at:
                file_record.started_at = datetime.now()
                
            if status in (TaskStatus.COMPLETED, TaskStatus.FAILED):
                file_record.completed_at = datetime.now()
                
            # Update job status logic
            # Need to query all files for this job to update aggregate status
            job = session.query(IngestionJob).get(job_id)
            if job:
                all_files = job.files # This uses the relationship, might need refresh if not in session? 
                # Since we are in the same session and just updated file_record which is in job.files, it should be reflected?
                # SQLAlchemy relationships can be tricky with uncommitted changes.
                # Let's flush first.
                session.flush()
                
                # Check statuses
                statuses = [f.status for f in job.files]
                
                if all(s == TaskStatus.PENDING for s in statuses):
                    job.status = TaskStatus.PENDING
                elif all(s in (TaskStatus.COMPLETED, TaskStatus.FAILED) for s in statuses):
                    job.status = TaskStatus.COMPLETED
                    if not job.completed_at:
                        job.completed_at = datetime.now()
                else:
                    job.status = TaskStatus.PROCESSING
            
            session.commit()
            
        except Exception as e:
            session.rollback()
            logger.error(f"Error updating file status: {e}")
        finally:
            session.close()

tracker = IngestionTracker()

