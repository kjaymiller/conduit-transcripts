"""Transcribe app models."""

from typing import Optional
from pydantic import BaseModel, Field


class TranscribeRequest(BaseModel):
    """Request for transcription."""

    episode_number: Optional[int] = None
    audio_url: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "episode_number": 100,
            }
        }


class TranscribeResponse(BaseModel):
    """Response for transcription."""

    status: str
    message: str
    episode_number: Optional[int] = None


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    database: str
    message: str


class StatusResponse(BaseModel):
    """Status check response."""

    episode_number: int
    ingested: bool
    chunks_count: Optional[int] = None


class IngestResponse(BaseModel):
    """File ingestion response."""

    status: str
    message: str
    episode_number: int
