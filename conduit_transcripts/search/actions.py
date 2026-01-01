"""Core actions for MCP server."""

import logging
from typing import List, Optional, Dict, Any

from sqlalchemy import select, or_
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings

from conduit_transcripts.config import settings
from conduit_transcripts.database.postgres import VectorDatabase
from conduit_transcripts.models import Transcript, VectorChunk
from conduit_transcripts.models.search import SearchResult

logger = logging.getLogger(__name__)

# Global for caching model
_embedding_model = None


def get_embedding_model():
    """Get embedding model."""
    global _embedding_model
    if _embedding_model is None:
        if settings.EMBEDDING_PROVIDER == "ollama":
            _embedding_model = OllamaEmbeddings(
                model=settings.EMBEDDING_MODEL,
                base_url=settings.OLLAMA_BASE_URL,
            )
        else:
            _embedding_model = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL,
                model_kwargs={"device": settings.EMBEDDING_DEVICE},
                encode_kwargs={"normalize_embeddings": False},
            )
    return _embedding_model


def vector_search(
    query: str, limit: int = 10, similarity_threshold: float = 0.0
) -> List[SearchResult]:
    """Search transcripts using vector similarity."""
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
                            podcast=str(chunk.podcast),
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
            return search_results

        finally:
            session.close()

    except Exception as e:
        logger.error(f"Vector search error: {e}")
        raise


def text_search(query: str, limit: int = 10) -> List[SearchResult]:
    """Search transcripts using text matching."""
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
                        podcast=str(chunk.podcast),
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
            return search_results

        finally:
            session.close()

    except Exception as e:
        logger.error(f"Text search error: {e}")
        raise


def title_search(query: str, limit: int = 10) -> List[SearchResult]:
    """Search transcripts by title."""
    try:
        logger.info(f"Title search query: '{query}' (limit={limit})")

        vector_db = VectorDatabase()
        session = vector_db.Session()

        try:
            # Perform title search using ILIKE for case-insensitive matching
            results = (
                session.query(Transcript)
                .filter(
                    or_(
                        Transcript.title.ilike(f"%{query}%"),
                        Transcript.description.ilike(f"%{query}%"),
                    )
                )
                .limit(limit)
                .all()
            )

            # Convert results to SearchResult objects
            search_results = []
            for transcript in results:
                # Use description as content snippet since we don't have a chunk
                content_snippet = transcript.description or ""
                if len(content_snippet) > 500:
                    content_snippet = content_snippet[:500] + "..."

                search_results.append(
                    SearchResult(
                        episode_number=transcript.episode_number,
                        podcast=str(transcript.podcast),
                        title=transcript.title,
                        description=transcript.description,
                        url=transcript.url,
                        pub_date=str(transcript.published_date)
                        if transcript.published_date
                        else None,
                        content_snippet=content_snippet,
                        similarity_score=None,
                        chunk_id=None,
                    )
                )

            logger.info(f"Found {len(search_results)} results")
            return search_results

        finally:
            session.close()

    except Exception as e:
        logger.error(f"Title search error: {e}")
        raise


def get_episode_details(episode_number: int, podcast: str) -> Optional[Dict[str, Any]]:
    """Get full transcript for a specific episode."""
    try:
        # TODO: Handle podcast lookup by name/slug if string provided
        # For now, assume "Conduit" -> 1 if not int
        podcast_id = 1
        if isinstance(podcast, int):
            podcast_id = podcast
        elif podcast == "Conduit":
            podcast_id = 1

        logger.info(f"Getting episode {episode_number} from podcast {podcast_id}")

        vector_db = VectorDatabase()
        session = vector_db.Session()

        try:
            # Get transcript
            transcript = (
                session.query(Transcript)
                .filter(
                    Transcript.podcast == podcast_id,
                    Transcript.episode_number == episode_number,
                )
                .first()
            )

            if not transcript:
                return None

            # Get all chunks for this episode
            chunks = (
                session.query(VectorChunk)
                .filter(
                    VectorChunk.podcast == podcast_id,
                    VectorChunk.episode_number == episode_number,
                )
                .order_by(VectorChunk.id)
                .all()
            )

            return {
                "episode_number": episode_number,
                "podcast": str(podcast_id),
                "metadata": transcript.meta,
                "content": transcript.meta.get("content", ""),
                "chunks_count": len(chunks),
            }

        finally:
            session.close()

    except Exception as e:
        logger.error(f"Error getting episode: {e}")
        raise
