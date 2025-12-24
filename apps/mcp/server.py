"""MCP server implementation for transcript search and RAG."""

import logging
from typing import List

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from conduit_transcripts.config import settings
from conduit_transcripts.database.postgres import VectorDatabase
from conduit_transcripts.models import Transcript, VectorChunk
from apps.mcp.models import (
    SearchResponse,
    HealthResponse,
)
from apps.mcp import actions

# Import FastMCP
from mcp.server import FastMCP

# Configure logging
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Conduit Transcript MCP Server",
    description="MCP server for searching and summarizing podcast transcripts",
    version="1.0.0",
)

# Create MCP Server
# Dependencies: "mcp" package
mcp = FastMCP("Conduit Transcripts")


@mcp.tool()
def search_transcripts(
    query: str, limit: int = 10, similarity_threshold: float = 0.0
) -> str:
    """
    Search transcripts using vector similarity.
    Returns formatted results suitable for LLM context.
    """
    results = actions.vector_search(query, limit, similarity_threshold)
    
    if not results:
        return "No matching transcripts found."
        
    output = [f"Found {len(results)} results for '{query}':\n"]
    for r in results:
        output.append(f"Episode {r.episode_number}: {r.title}")
        output.append(f"URL: {r.url}")
        output.append(f"Content: {r.content_snippet}")
        output.append(f"Similarity: {r.similarity_score}")
        output.append("---")
    
    return "\n".join(output)


@mcp.tool()
def get_episode_transcript(episode_number: int, podcast: str = "Conduit") -> str:
    """Get full transcript for a specific episode."""
    result = actions.get_episode_details(episode_number, podcast)
    if not result:
        return f"Episode {episode_number} not found."
    
    metadata = result['metadata']
    return (
        f"Title: {metadata.get('title')}\n"
        f"Date: {metadata.get('pub_date')}\n"
        f"URL: {metadata.get('url')}\n"
        f"Content:\n{result['content']}"
    )


# Mount MCP SSE app
# The MCP SSE transport will be available at /mcp/sse and /mcp/messages
try:
    app.mount("/mcp", mcp.sse_app())
except Exception as e:
    logger.error(f"Failed to mount MCP app: {e}")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=dict)
async def root():
    """Root endpoint."""
    return {
        "message": "Conduit Transcript MCP Server",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "vector_search": "/search/vector",
            "text_search": "/search/text",
            "episode": "/episode/{episode_number}",
            "list_episodes": "/episodes",
            "mcp_sse": "/mcp/sse",
        },
    }


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


@app.get("/episode/{episode_number}", response_model=dict)
async def get_episode(
    episode_number: int, podcast: str = Query("Conduit", description="Podcast name")
):
    """Get full transcript for a specific episode."""
    try:
        result = actions.get_episode_details(episode_number, podcast)
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
    podcast: str = Query("Conduit", description="Podcast name"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of episodes"),
    offset: int = Query(0, ge=0, description="Offset for pagination"),
):
    """List all available episodes."""
    try:
        logger.info(f"Listing episodes for {podcast} (limit={limit}, offset={offset})")

        vector_db = VectorDatabase()
        session = vector_db.Session()

        try:
            # Get total count
            total = (
                session.query(Transcript).filter(Transcript.podcast == podcast).count()
            )

            # Get episodes
            transcripts = (
                session.query(Transcript)
                .filter(Transcript.podcast == podcast)
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
                "podcast": podcast,
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
