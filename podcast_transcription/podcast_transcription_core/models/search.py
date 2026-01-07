"""MCP server models."""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    """Single search result."""

    episode_number: int
    podcast: str
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    pub_date: Optional[str] = None
    content_snippet: str
    similarity_score: Optional[float] = None
    chunk_id: Optional[int] = None


class SearchResponse(BaseModel):
    """Search response with results."""

    query: str
    results: List[SearchResult]
    total_results: int
    search_type: str


class SummaryRequest(BaseModel):
    """Request for summarizing search results."""

    query: str
    max_results: int = Field(default=10, ge=1, le=100)


class SummaryResponse(BaseModel):
    """Summary response."""

    query: str
    summary: str
    sources: List[Dict[str, Any]]


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    database: str
    embedding_model: str
