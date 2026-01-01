"""Web service for searching and viewing transcripts."""

import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import text

from conduit_transcripts.config import settings
from conduit_transcripts.database.postgres import VectorDatabase
from conduit_transcripts.models import Transcript, VectorChunk
from conduit_transcripts.models.search import (
    SearchResponse,
    HealthResponse,
)
from conduit_transcripts.search import actions
from conduit_transcripts.chat import rag

# Configure logging
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Conduit Transcripts Web",
    description="Web service for searching and viewing podcast transcripts",
    version="1.0.0",
)

# Setup templates
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Serve the search UI."""
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/stats", response_class=HTMLResponse)
async def stats_page(request: Request):
    """Serve the statistics page."""
    return templates.TemplateResponse(request=request, name="stats.html")


@app.get("/api/stats")
async def get_stats():
    """Get statistics about the transcripts."""
    try:
        vector_db = VectorDatabase()
        session = vector_db.Session()

        try:
            total_episodes = session.query(Transcript).count()
            total_chunks = session.query(VectorChunk).count()

            return {
                "total_episodes": total_episodes,
                "total_chunks": total_chunks,
            }
        finally:
            session.close()
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get stats: {str(e)}")


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    try:
        # Test database connection
        vector_db = VectorDatabase()
        with vector_db.engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        return HealthResponse(
            status="healthy",
            database="connected",
            embedding_model=settings.EMBEDDING_MODEL,
        )
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail=f"Service unhealthy: {str(e)}")


@app.get("/search/vector", response_model=SearchResponse)
async def vector_search(
    query: str = Query(..., description="Search query text"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results"),
    similarity_threshold: float = Query(
        0.0, ge=0.0, le=1.0, description="Minimum similarity score"
    ),
):
    """
    Search transcripts using vector similarity.
    """
    try:
        results = actions.vector_search(query, limit, similarity_threshold)
        return SearchResponse(
            query=query,
            results=results,
            total_results=len(results),
            search_type="vector_similarity",
        )
    except Exception as e:
        logger.error(f"Vector search error: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/search/text", response_model=SearchResponse)
async def text_search(
    query: str = Query(..., description="Search query text"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results"),
):
    """
    Search transcripts using text matching.
    """
    try:
        results = actions.text_search(query, limit)
        return SearchResponse(
            query=query,
            results=results,
            total_results=len(results),
            search_type="text_match",
        )
    except Exception as e:
        logger.error(f"Text search error: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/search/title", response_model=SearchResponse)
async def title_search(
    query: str = Query(..., description="Search query text"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results"),
):
    """
    Search transcripts by title.
    """
    try:
        results = actions.title_search(query, limit)
        return SearchResponse(
            query=query,
            results=results,
            total_results=len(results),
            search_type="title_match",
        )
    except Exception as e:
        logger.error(f"Title search error: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/episode/{episode_number}", response_class=HTMLResponse)
async def episode_page(
    request: Request,
    episode_number: int,
    podcast_id: int = Query(1, alias="podcast", description="Podcast ID"),
):
    """Serve the episode detail page."""
    try:
        result = actions.get_episode_details(episode_number, podcast_id)
        if not result:
            raise HTTPException(
                status_code=404, detail=f"Episode {episode_number} not found"
            )

        return templates.TemplateResponse(
            request=request,
            name="episode.html",
            context={
                "episode": result,
                "llm_model": settings.LLM_MODEL,
            },
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting episode page: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get episode: {str(e)}")


class ChatRequest(BaseModel):
    query: str


@app.post("/api/chat/{episode_number}")
async def chat_episode(
    episode_number: int,
    request: ChatRequest,
):
    """Chat with a specific episode."""
    return StreamingResponse(
        rag.generate_episode_response(request.query, episode_number),
        media_type="text/plain",
    )


@app.get("/api/episode/{episode_number}", response_model=dict)
async def get_episode(
    episode_number: int,
    podcast_id: int = Query(1, alias="podcast", description="Podcast ID"),
):
    """Get full transcript for a specific episode."""
    try:
        # For now, we only support integer IDs.
        # If the user passes "Conduit" via query param, FastAPI validation will fail
        # unless we handle it. But let's assume the frontend sends IDs or defaults.
        # To support legacy URLs, we might need more logic, but let's stick to int for now.

        result = actions.get_episode_details(episode_number, podcast_id)
        if not result:
            raise HTTPException(
                status_code=404, detail=f"Episode {episode_number} not found"
            )
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting episode: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get episode: {str(e)}")


@app.get("/episodes", response_model=dict)
async def list_episodes(
    podcast_id: int = Query(1, alias="podcast", description="Podcast ID"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of episodes"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
):
    """List all available episodes."""
    try:
        logger.info(
            f"Listing episodes for podcast {podcast_id} (limit={limit}, offset={offset})"
        )

        vector_db = VectorDatabase()
        session = vector_db.Session()

        try:
            # Get total count
            total = (
                session.query(Transcript)
                .filter(Transcript.podcast == podcast_id)
                .count()
            )

            # Get episodes
            transcripts = (
                session.query(Transcript)
                .filter(Transcript.podcast == podcast_id)
                .order_by(Transcript.episode_number.desc())
                .limit(limit)
                .offset(offset)
                .all()
            )

            episodes = []
            for transcript in transcripts:
                meta = transcript.meta
                episodes.append(
                    {
                        "episode_number": transcript.episode_number,
                        "title": meta.get("title"),
                        "description": meta.get("description"),
                        "url": meta.get("url"),
                        "pub_date": meta.get("pub_date"),
                    }
                )

            return {
                "podcast": str(podcast_id),
                "total_episodes": total,
                "episodes": episodes,
                "limit": limit,
                "offset": offset,
            }

        finally:
            session.close()

    except Exception as e:
        logger.error(f"Error listing episodes: {e}")
        raise HTTPException(
            status_code=500, detail=f"Failed to list episodes: {str(e)}"
        )
