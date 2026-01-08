from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy import select
from typing import Optional

from podcast_transcription_core.database.postgres import VectorDatabase
from podcast_transcription_core.config import settings
from podcast_transcription_core.models import VectorChunk, Transcript
from podcast_transcription_core.chat.rag import generate_episode_response

from .models import (
    SearchResponse,
    EpisodeResponse,
    EpisodesResponse,
    SearchResult,
    EpisodeListItem,
    EpisodeMetadata,
    ChatRequest,
)

router = APIRouter()


@router.get("/search/vector", response_model=SearchResponse)
async def vector_search(
    query: str = Query(..., description="Search query text"),
    limit: int = Query(10, ge=1, le=100, description="Maximum results"),
    similarity_threshold: float = Query(
        0.0, ge=0.0, le=1.0, description="Minimum similarity score"
    ),
    episode_number: Optional[str] = Query(None, description="Filter by episode number"),
):
    """Semantic search using vector embeddings."""
    try:
        # Parse episode_number
        episode_num: Optional[int] = None
        if episode_number and episode_number.strip():
            try:
                episode_num = int(episode_number)
            except ValueError:
                pass

        db = VectorDatabase()
        session = db.Session()

        if settings.EMBEDDING_PROVIDER == "ollama":
            from langchain_ollama import OllamaEmbeddings

            embedding_model = OllamaEmbeddings(
                model=settings.EMBEDDING_MODEL,
                base_url=settings.OLLAMA_BASE_URL,
            )
        else:
            from langchain_huggingface import HuggingFaceEmbeddings

            embedding_model = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL,
                model_kwargs={"device": settings.EMBEDDING_DEVICE},
                encode_kwargs={"normalize_embeddings": False},
            )

        query_embedding = embedding_model.embed_query(query)

        stmt = select(
            VectorChunk,
            VectorChunk.embedding.l2_distance(query_embedding).label("distance"),
        )

        if episode_num is not None:
            stmt = stmt.filter(VectorChunk.episode_number == episode_num)

        results = session.execute(
            stmt.order_by(VectorChunk.embedding.l2_distance(query_embedding)).limit(
                limit
            )
        ).all()

        search_results = []
        for chunk, distance in results:
            similarity_score = 1.0 / (1.0 + distance) if distance is not None else 0.0
            if similarity_score < similarity_threshold:
                continue

            search_results.append(
                SearchResult(
                    episode_number=chunk.episode_number,
                    podcast="Conduit",
                    title=None,
                    description=None,
                    url=None,
                    pub_date=None,
                    content_snippet=chunk.content[:200] + "..."
                    if len(chunk.content) > 200
                    else chunk.content,
                    similarity_score=round(similarity_score, 4),
                    chunk_id=chunk.id,
                )
            )

        session.close()

        return SearchResponse(
            query=query,
            results=search_results,
            total_results=len(search_results),
            search_type="vector_similarity",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Vector search error: {str(e)}")


@router.get("/search/text", response_model=SearchResponse)
async def text_search(
    query: str = Query(..., description="Search query text"),
    limit: int = Query(10, ge=1, le=100, description="Maximum results"),
    episode_number: Optional[str] = Query(None, description="Filter by episode number"),
):
    """Keyword-based text search."""
    try:
        # Parse episode_number
        episode_num: Optional[int] = None
        if episode_number and episode_number.strip():
            try:
                episode_num = int(episode_number)
            except ValueError:
                pass

        db = VectorDatabase()
        session = db.Session()

        stmt = session.query(VectorChunk).filter(
            VectorChunk.content.ilike(f"%{query}%")
        )

        if episode_num is not None:
            stmt = stmt.filter(VectorChunk.episode_number == episode_num)

        results = stmt.limit(limit).all()

        search_results = []
        for chunk in results:
            search_results.append(
                SearchResult(
                    episode_number=chunk.episode_number,
                    podcast="Conduit",
                    title=None,
                    description=None,
                    url=None,
                    pub_date=None,
                    content_snippet=chunk.content[:200] + "..."
                    if len(chunk.content) > 200
                    else chunk.content,
                    similarity_score=None,
                    chunk_id=chunk.id,
                )
            )

        session.close()

        return SearchResponse(
            query=query,
            results=search_results,
            total_results=len(search_results),
            search_type="text_match",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Text search error: {str(e)}")


@router.get("/episode/{episode_number}", response_model=EpisodeResponse)
async def get_episode(
    episode_number: int, podcast: str = Query("Conduit", description="Podcast name")
):
    """Get full transcript for a specific episode."""
    try:
        db = VectorDatabase()
        session = db.Session()

        transcript = (
            session.query(Transcript)
            .filter(
                Transcript.episode_number == episode_number, Transcript.podcast == 1
            )
            .first()
        )

        if not transcript:
            raise HTTPException(
                status_code=404, detail=f"Episode {episode_number} not found"
            )

        metadata = EpisodeMetadata(
            title=transcript.title,
            description=transcript.description,
            url=transcript.url,
            pub_date=str(transcript.published_date)
            if transcript.published_date
            else None,
        )

        chunks_count = len(transcript.chunks)

        session.close()

        return EpisodeResponse(
            episode_number=episode_number,
            podcast=podcast,
            metadata=metadata,
            content=transcript.content,
            chunks_count=chunks_count,
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error retrieving episode: {str(e)}"
        )


@router.get("/episodes", response_model=EpisodesResponse)
async def list_episodes(
    podcast: str = Query("Conduit", description="Podcast name"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum episodes"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
    start_date: Optional[str] = Query(
        None, description="Filter episodes published on or after this date (ISO format)"
    ),
    end_date: Optional[str] = Query(
        None,
        description="Filter episodes published on or before this date (ISO format)",
    ),
):
    """List all available episodes."""
    try:
        from datetime import datetime

        db = VectorDatabase()
        session = db.Session()

        query = session.query(Transcript).filter(Transcript.podcast == podcast)

        if start_date:
            try:
                start_dt = datetime.fromisoformat(start_date)
                query = query.filter(Transcript.published_date >= start_dt)
            except ValueError:
                raise HTTPException(
                    status_code=400, detail="Invalid start_date format. Use ISO format."
                )

        if end_date:
            try:
                end_dt = datetime.fromisoformat(end_date)
                query = query.filter(Transcript.published_date <= end_dt)
            except ValueError:
                raise HTTPException(
                    status_code=400, detail="Invalid end_date format. Use ISO format."
                )

        transcripts = (
            query.order_by(Transcript.episode_number.desc())
            .limit(limit)
            .offset(offset)
            .all()
        )

        episodes = []
        for transcript in transcripts:
            episodes.append(
                EpisodeListItem(
                    episode_number=transcript.episode_number,
                    title=transcript.title,
                    description=transcript.description,
                    url=transcript.url,
                    pub_date=str(transcript.published_date)
                    if transcript.published_date
                    else None,
                )
            )

        total_count = (
            session.query(Transcript).filter(Transcript.podcast == podcast).count()
        )
        session.close()

        return EpisodesResponse(
            podcast=podcast,
            total_episodes=total_count,
            episodes=episodes,
            limit=limit,
            offset=offset,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing episodes: {str(e)}")


@router.post("/chat/{episode_number}")
async def chat_episode(
    episode_number: int,
    request: ChatRequest,
):
    """Chat with a specific episode using RAG."""
    return StreamingResponse(
        generate_episode_response(request.query, episode_number),
        media_type="text/plain",
    )
