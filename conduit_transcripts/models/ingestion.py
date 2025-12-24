"""SQLAlchemy models for ingestion tracking."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
import enum

from conduit_transcripts.models.transcript import Base


class TaskStatus(str, enum.Enum):
    """Status of an ingestion task."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class IngestionJob(Base):
    """Model for an ingestion job."""
    
    __tablename__ = "ingestion_jobs"

    job_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    status = Column(SqlEnum(TaskStatus), default=TaskStatus.PENDING)
    created_at = Column(DateTime, default=datetime.now)
    completed_at = Column(DateTime, nullable=True)

    # Relationship to files
    files = relationship("IngestionFile", back_populates="job", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<IngestionJob(job_id={self.job_id}, status={self.status})>"


class IngestionFile(Base):
    """Model for a file in an ingestion job."""
    
    __tablename__ = "ingestion_files"

    id = Column(Integer, primary_key=True)
    job_id = Column(String, ForeignKey("ingestion_jobs.job_id"))
    filename = Column(String, nullable=False)
    status = Column(SqlEnum(TaskStatus), default=TaskStatus.PENDING)
    episode_number = Column(Integer, nullable=True)
    chunks_processed = Column(Integer, default=0)
    total_chunks = Column(Integer, nullable=True)
    error = Column(String, nullable=True)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    # Relationship to job
    job = relationship("IngestionJob", back_populates="files")

    def __repr__(self):
        return f"<IngestionFile(filename={self.filename}, status={self.status})>"
