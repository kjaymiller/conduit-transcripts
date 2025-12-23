"""Progress tracking for ingestion tasks."""

import logging
import uuid
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class TaskStatus(str, Enum):
    """Status of an ingestion task."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class FileProgress(BaseModel):
    """Progress of a single file ingestion."""
    filename: str
    status: TaskStatus = TaskStatus.PENDING
    episode_number: Optional[int] = None
    chunks_processed: int = 0
    total_chunks: Optional[int] = None
    error: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class IngestionJob(BaseModel):
    """A job containing multiple file ingestions."""
    job_id: str
    status: TaskStatus = TaskStatus.PENDING
    files: Dict[str, FileProgress] = Field(default_factory=dict)
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
    """Singleton tracker for ingestion jobs."""
    _instance = None
    _jobs: Dict[str, IngestionJob] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IngestionTracker, cls).__new__(cls)
        return cls._instance

    def create_job(self, filenames: List[str]) -> str:
        """Create a new ingestion job."""
        job_id = str(uuid.uuid4())
        job = IngestionJob(job_id=job_id)
        
        for filename in filenames:
            job.files[filename] = FileProgress(filename=filename)
            
        self._jobs[job_id] = job
        return job_id

    def get_job(self, job_id: str) -> Optional[IngestionJob]:
        """Get job details."""
        return self._jobs.get(job_id)

    def update_file_status(
        self, 
        job_id: str, 
        filename: str, 
        status: TaskStatus, 
        error: Optional[str] = None,
        episode_number: Optional[int] = None,
        chunks_count: Optional[int] = None
    ):
        """Update status of a specific file."""
        if job_id not in self._jobs:
            return
            
        job = self._jobs[job_id]
        if filename not in job.files:
            return
            
        file_progress = job.files[filename]
        file_progress.status = status
        
        if error:
            file_progress.error = error
            
        if episode_number:
            file_progress.episode_number = episode_number
            
        if chunks_count is not None:
            file_progress.total_chunks = chunks_count
            file_progress.chunks_processed = chunks_count
            
        if status == TaskStatus.PROCESSING and not file_progress.started_at:
            file_progress.started_at = datetime.now()
            
        if status in (TaskStatus.COMPLETED, TaskStatus.FAILED):
            file_progress.completed_at = datetime.now()
            
        # Update job status
        self._update_job_status(job)

    def _update_job_status(self, job: IngestionJob):
        """Update parent job status based on children."""
        statuses = [f.status for f in job.files.values()]
        
        if all(s == TaskStatus.PENDING for s in statuses):
            job.status = TaskStatus.PENDING
        elif all(s in (TaskStatus.COMPLETED, TaskStatus.FAILED) for s in statuses):
            job.status = TaskStatus.COMPLETED
            job.completed_at = datetime.now()
        else:
            job.status = TaskStatus.PROCESSING

tracker = IngestionTracker()
