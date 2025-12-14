"""MCP server implementation for transcript search and RAG."""

import logging
from typing import List

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from conduit_transcripts.config import settings
from conduit_transcripts.database.postgres import VectorDatabase
from conduit_transcripts.models import Transcript, VectorChunk
from apps.mcp.models import (
    SearchResult,
    SearchResponse,
    SummaryRequest,
    SummaryResponse,
    HealthResponse,
)

# Configure logging
logger = logging.getLogger(__name__)

# Global variables for database and embeddings
db = None
embedding_model = None


def get_db() -> Session:
    """Get database session."""
    global db
    if db is None:
        db = VectorDatabase()
    session = db.Session()
    try:
        return session
    finally:
        session.close()


def get_embedding_model():
    """Get embedding model."""
    global embedding_model
    if embedding_model is None:
        from langchain_huggingface import HuggingFaceEmbeddings

        embedding_model = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={"device": settings.EMBEDDING_DEVICE},
            encode_kwargs={"normalize_embeddings": False},
        )
    return embedding_model


# Create FastAPI app
app = FastAPI(
    title="Conduit Transcript MCP Server",
    description="MCP server for searching and summarizing podcast transcripts",
    version="1.0.0",
)

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

    This endpoint converts the query to an embedding and finds the most similar
    transcript chunks using cosine similarity.
    """
    try:
        logger.info(f"Vector search query: '{query}' (limit={limit})")

        # Generate embedding for query
        embedding_model = get_embedding_model()
        query_embedding = embedding_model.embed_query(query)

        # Create database session
        vector_db = VectorDatabase()
        session = vector_db.Session()

        try:
            # Perform vector similarity search using L2 distance
            results = session.execute(
                select(
                    VectorChunk,
                    VectorChunk.embedding.l2_distance(query_embedding).label(
                        "distance"
                    ),
                )
                .order_by(VectorChunk.embedding.l2_distance(query_embedding))
                .limit(limit)
            ).all()

            # Convert results to SearchResult objects
            search_results = []
            for chunk, distance in results:
                # Get transcript metadata
                transcript = (
                    session.query(Transcript)
                    .filter(
                        Transcript.podcast == chunk.podcast,
                        Transcript.episode_number == chunk.episode_number,
                    )
                    .first()
                )

                meta = transcript.meta if transcript else {}

                # Convert L2 distance to similarity score (inverse relationship)
                similarity_score = (
                    1.0 / (1.0 + distance) if distance is not None else 0.0
                )

                if similarity_score >= similarity_threshold:
                    search_results.append(
                        SearchResult(
                            episode_number=chunk.episode_number,
                            podcast=chunk.podcast,
                            title=meta.get("title"),
                            description=meta.get("description"),
                            url=meta.get("url"),
                            pub_date=meta.get("pub_date"),
                            content_snippet=chunk.content[:500],  # Limit snippet size
                            similarity_score=round(similarity_score, 4),
                            chunk_id=chunk.id,
                        )
                    )

            logger.info(f"Found {len(search_results)} results")

            return SearchResponse(
                query=query,
                results=search_results,
                total_results=len(search_results),
                search_type="vector_similarity",
            )

        finally:
            session.close()

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

    This endpoint performs case-insensitive text search across transcript content.
    """
    try:
        logger.info(f"Text search query: '{query}' (limit={limit})")

        vector_db = VectorDatabase()
        session = vector_db.Session()

        try:
            # Perform text search using ILIKE for case-insensitive matching
            results = (
                session.query(VectorChunk)
                .filter(VectorChunk.content.ilike(f"%{query}%"))
                .limit(limit)
                .all()
            )

            # Convert results to SearchResult objects
            search_results = []
            for chunk in results:
                # Get transcript metadata
                transcript = (
                    session.query(Transcript)
                    .filter(
                        Transcript.podcast == chunk.podcast,
                        Transcript.episode_number == chunk.episode_number,
                    )
                    .first()
                )

                meta = transcript.meta if transcript else {}

                search_results.append(
                    SearchResult(
                        episode_number=chunk.episode_number,
                        podcast=chunk.podcast,
                        title=meta.get("title"),
                        description=meta.get("description"),
                        url=meta.get("url"),
                        pub_date=meta.get("pub_date"),
                        content_snippet=chunk.content[:500],
                        similarity_score=None,
                        chunk_id=chunk.id,
                    )
                )

            logger.info(f"Found {len(search_results)} results")

            return SearchResponse(
                query=query,
                results=search_results,
                total_results=len(search_results),
                search_type="text_match",
            )

        finally:
            session.close()

    except Exception as e:
        logger.error(f"Text search error: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/episode/{episode_number}", response_model=dict)
async def get_episode(
    episode_number: int, podcast: str = Query("Conduit", description="Podcast name")
):
    """Get full transcript for a specific episode."""
    try:
        logger.info(f"Getting episode {episode_number} from {podcast}")

        vector_db = VectorDatabase()
        session = vector_db.Session()

        try:
            # Get transcript
            transcript = (
                session.query(Transcript)
                .filter(
                    Transcript.podcast == podcast,
                    Transcript.episode_number == episode_number,
                )
                .first()
            )

            if not transcript:
                raise HTTPException(
                    status_code=404, detail=f"Episode {episode_number} not found"
                )

            # Get all chunks for this episode
            chunks = (
                session.query(VectorChunk)
                .filter(
                    VectorChunk.podcast == podcast,
                    VectorChunk.episode_number == episode_number,
                )
                .order_by(VectorChunk.id)
                .all()
            )

            return {
                "episode_number": episode_number,
                "podcast": podcast,
                "metadata": transcript.meta,
                "content": transcript.meta.get("content", ""),
                "chunks_count": len(chunks),
            }

        finally:
            session.close()

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
