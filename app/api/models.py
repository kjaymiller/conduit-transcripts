from pydantic import BaseModel, Field
from typing import Optional, List


class SearchResult(BaseModel):
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
    query: str
    results: List[SearchResult]
    total_results: int
    search_type: str


class EpisodeMetadata(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    pub_date: Optional[str] = None


class EpisodeResponse(BaseModel):
    episode_number: int
    podcast: str
    metadata: EpisodeMetadata
    content: str
    chunks_count: int


class EpisodeListItem(BaseModel):
    episode_number: int
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    pub_date: Optional[str] = None


class EpisodesResponse(BaseModel):
    podcast: str
    total_episodes: int
    episodes: List[EpisodeListItem]
    limit: int
    offset: int


class HealthResponse(BaseModel):
    status: str
    database: str
