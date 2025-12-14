"""
MCP Server for Conduit Transcript Search and Summarization

This server provides MCP-compliant endpoints for searching podcast transcripts
using vector similarity search and text search capabilities.
"""

import os
import logging
from typing import List, Optional, Dict, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, text, select, or_
from sqlalchemy.orm import sessionmaker, Session
from pgvector.sqlalchemy import Vector

from langchain_huggingface import HuggingFaceEmbeddings

# Import models from pg_ingest
from pg_ingest import Transcript, VectorChunk, Base

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Database configuration
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "transcripts")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")

# For local development, fallback to AIVEN_POSTGRES_SERVICE_URI if available
if os.getenv("AIVEN_POSTGRES_SERVICE_URI"):
    DB_URI = os.getenv("AIVEN_POSTGRES_SERVICE_URI")
else:
    DB_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

logger.info(f"Connecting to database at {POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")

# Global variables for database and embeddings
engine = None
SessionLocal = None
embedding_model = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown"""
    global engine, SessionLocal, embedding_model

    # Startup
    logger.info("Initializing MCP server...")

    try:
        engine = create_engine(DB_URI, pool_pre_ping=True)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        # Test database connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            logger.info("Database connection successful")

        # Initialize embedding model
        logger.info("Loading embedding model...")
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": False},
        )
        logger.info("Embedding model loaded successfully")
        logger.info("MCP server initialized successfully")

    except Exception as e:
        logger.error(f"Failed to initialize server: {e}")
        raise

    yield

    # Shutdown
    logger.info("Shutting down MCP server...")
    if engine:
        engine.dispose()
    logger.info("MCP server shutdown complete")


# Create FastAPI app with lifespan
app = FastAPI(
    title="Conduit Transcript MCP Server",
    description="MCP server for searching and summarizing podcast transcripts",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for API
class SearchResult(BaseModel):
    """Single search result"""
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
    """Search response with results"""
    query: str
    results: List[SearchResult]
    total_results: int
    search_type: str


class SummaryRequest(BaseModel):
    """Request for summarizing search results"""
    query: str
    max_results: int = Field(default=10, ge=1, le=100)


class SummaryResponse(BaseModel):
    """Summary response"""
    query: str
    summary: str
    sources: List[Dict[str, Any]]


class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    database: str
    embedding_model: str


def get_db() -> Session:
    """Get database session"""
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint"""
    return {
        "message": "Conduit Transcript MCP Server",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "vector_search": "/search/vector",
            "text_search": "/search/text",
            "episode": "/episode/{episode_number}",
            "list_episodes": "/episodes"
        }
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    try:
        # Test database connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        return HealthResponse(
            status="healthy",
            database="connected",
            embedding_model="sentence-transformers/all-mpnet-base-v2"
        )
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail=f"Service unhealthy: {str(e)}")


@app.get("/search/vector", response_model=SearchResponse)
async def vector_search(
    query: str = Query(..., description="Search query text"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results"),
    similarity_threshold: float = Query(0.0, ge=0.0, le=1.0, description="Minimum similarity score")
):
    """
    Search transcripts using vector similarity

    This endpoint converts the query to an embedding and finds the most similar
    transcript chunks using cosine similarity.
    """
    try:
        logger.info(f"Vector search query: '{query}' (limit={limit})")

        # Generate embedding for query
        query_embedding = embedding_model.embed_query(query)

        # Create database session
        db = get_db()

        try:
            # Perform vector similarity search using L2 distance
            # Note: We use order_by with l2_distance for similarity ranking
            results = db.execute(
                select(
                    VectorChunk,
                    VectorChunk.embedding.l2_distance(query_embedding).label("distance")
                )
                .order_by(VectorChunk.embedding.l2_distance(query_embedding))
                .limit(limit)
            ).all()

            # Convert results to SearchResult objects
            search_results = []
            for chunk, distance in results:
                # Get transcript metadata
                transcript = db.query(Transcript).filter(
                    Transcript.podcast == chunk.podcast,
                    Transcript.episode_number == chunk.episode_number
                ).first()

                meta = transcript.meta if transcript else {}

                # Convert L2 distance to similarity score (inverse relationship)
                # Lower distance = higher similarity
                similarity_score = 1.0 / (1.0 + distance) if distance is not None else 0.0

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
                            chunk_id=chunk.id
                        )
                    )

            logger.info(f"Found {len(search_results)} results")

            return SearchResponse(
                query=query,
                results=search_results,
                total_results=len(search_results),
                search_type="vector_similarity"
            )

        finally:
            db.close()

    except Exception as e:
        logger.error(f"Vector search error: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/search/text", response_model=SearchResponse)
async def text_search(
    query: str = Query(..., description="Search query text"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results")
):
    """
    Search transcripts using text matching

    This endpoint performs case-insensitive text search across transcript content.
    """
    try:
        logger.info(f"Text search query: '{query}' (limit={limit})")

        db = get_db()

        try:
            # Perform text search using ILIKE for case-insensitive matching
            results = db.query(VectorChunk).filter(
                VectorChunk.content.ilike(f"%{query}%")
            ).limit(limit).all()

            # Convert results to SearchResult objects
            search_results = []
            for chunk in results:
                # Get transcript metadata
                transcript = db.query(Transcript).filter(
                    Transcript.podcast == chunk.podcast,
                    Transcript.episode_number == chunk.episode_number
                ).first()

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
                        chunk_id=chunk.id
                    )
                )

            logger.info(f"Found {len(search_results)} results")

            return SearchResponse(
                query=query,
                results=search_results,
                total_results=len(search_results),
                search_type="text_match"
            )

        finally:
            db.close()

    except Exception as e:
        logger.error(f"Text search error: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@app.get("/episode/{episode_number}", response_model=Dict[str, Any])
async def get_episode(
    episode_number: int,
    podcast: str = Query("Conduit", description="Podcast name")
):
    """
    Get full transcript for a specific episode
    """
    try:
        logger.info(f"Getting episode {episode_number} from {podcast}")

        db = get_db()

        try:
            # Get transcript
            transcript = db.query(Transcript).filter(
                Transcript.podcast == podcast,
                Transcript.episode_number == episode_number
            ).first()

            if not transcript:
                raise HTTPException(
                    status_code=404,
                    detail=f"Episode {episode_number} not found"
                )

            # Get all chunks for this episode
            chunks = db.query(VectorChunk).filter(
                VectorChunk.podcast == podcast,
                VectorChunk.episode_number == episode_number
            ).order_by(VectorChunk.id).all()

            return {
                "episode_number": episode_number,
                "podcast": podcast,
                "metadata": transcript.meta,
                "content": transcript.meta.get("content", ""),
                "chunks_count": len(chunks)
            }

        finally:
            db.close()

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting episode: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get episode: {str(e)}")


@app.get("/episodes", response_model=Dict[str, Any])
async def list_episodes(
    podcast: str = Query("Conduit", description="Podcast name"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of episodes"),
    offset: int = Query(0, ge=0, description="Offset for pagination")
):
    """
    List all available episodes
    """
    try:
        logger.info(f"Listing episodes for {podcast} (limit={limit}, offset={offset})")

        db = get_db()

        try:
            # Get total count
            total = db.query(Transcript).filter(
                Transcript.podcast == podcast
            ).count()

            # Get episodes
            transcripts = db.query(Transcript).filter(
                Transcript.podcast == podcast
            ).order_by(Transcript.episode_number.desc()).limit(limit).offset(offset).all()

            episodes = []
            for transcript in transcripts:
                meta = transcript.meta
                episodes.append({
                    "episode_number": transcript.episode_number,
                    "title": meta.get("title"),
                    "description": meta.get("description"),
                    "url": meta.get("url"),
                    "pub_date": meta.get("pub_date")
                })

            return {
                "podcast": podcast,
                "total_episodes": total,
                "episodes": episodes,
                "limit": limit,
                "offset": offset
            }

        finally:
            db.close()

    except Exception as e:
        logger.error(f"Error listing episodes: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to list episodes: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
