from fastapi import APIRouter, Query, HTTPException, BackgroundTasks, status
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
    TranscriptUpdate,
)

router = APIRouter()


@router.post(
    "/episodes/check-latest",
    response_model=EpisodeResponse,
    status_code=status.HTTP_200_OK,
)
async def check_latest_episode(
    background_tasks: BackgroundTasks,
    podcast_id: int = Query(1, description="Podcast ID"),
    feed_url: Optional[str] = Query(None, description="Override RSS feed URL"),
):
    """
    Check for the latest episode in the RSS feed.
    If it's new (not in DB), start transcription in background.
    """
    from podcast_transcription_core.utils.rss import (
        fetch_latest_episode_details,
        CONDUIT_RSS_FEED,
    )
    from podcast_transcription_core.transcription.audio import download_audio_file
    from podcast_transcription_core.transcription.core import HybridTranscriber
    import frontmatter
    import os

    db = VectorDatabase()

    # Update feed URL if provided
    if feed_url:
        db.update_podcast_feed_url(podcast_id, feed_url)

    # Get current feed URL from DB
    podcast = db.get_podcast(podcast_id)
    current_feed_url = (
        podcast.feed_url if podcast and podcast.feed_url else CONDUIT_RSS_FEED
    )

    # Fetch latest episode from RSS
    try:
        latest_ep_data = fetch_latest_episode_details(current_feed_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching RSS feed: {e}")

    episode_number = latest_ep_data["episode_number"]

    # Check if exists in DB
    session = db.Session()
    existing_transcript = (
        session.query(Transcript)
        .filter(
            Transcript.episode_number == episode_number,
            Transcript.podcast == podcast_id,
        )
        .first()
    )
    session.close()

    if existing_transcript:
        return await get_episode(episode_number, "Conduit")

    # It's new! Start background task
    # First, create a placeholder transcript record

    # Create basic frontmatter post to initialize record
    post = frontmatter.Post(content="")
    post.metadata = {
        "title": latest_ep_data["title"],
        "episode_number": episode_number,
        "description": latest_ep_data["description"],
        "url": latest_ep_data["url"],
        "pub_date": latest_ep_data["pub_date"],
        "audio_url": latest_ep_data["audio_url"],
    }

    # This will create the record with empty content
    db.process_frontmatter_post(post)

    # Set status to processing
    db.set_transcript_status(podcast_id, episode_number, "processing")

    # Add background task for transcription
    background_tasks.add_task(
        process_new_episode_transcription,
        podcast_id,
        episode_number,
        latest_ep_data["audio_url"],
    )

    # Return placeholder
    return EpisodeResponse(
        episode_number=episode_number,
        podcast="Conduit",
        metadata=EpisodeMetadata(
            title=latest_ep_data["title"],
            description=latest_ep_data["description"],
            url=latest_ep_data["url"],
            pub_date=str(latest_ep_data["pub_date"]),
        ),
        content="",
        chunks_count=0,
        processing_status="processing",
    )


def process_new_episode_transcription(
    podcast_id: int, episode_number: int, audio_url: str
):
    """Background task to download, transcribe, and index a new episode."""
    from podcast_transcription_core.transcription.audio import download_audio_file
    from podcast_transcription_core.transcription.core import HybridTranscriber
    import os

    db = VectorDatabase()

    try:
        # 1. Download audio
        if not audio_url:
            raise ValueError("No audio URL provided")

        audio_path = download_audio_file(audio_url)

        # 2. Transcribe
        transcriber = HybridTranscriber(model="base")
        transcript_text = transcriber.transcribe(audio_path)

        # 3. Cleanup audio file
        if audio_path.exists():
            os.unlink(audio_path)

        # 4. Update DB with content (this also chunks it and sets status to completed)
        db.update_transcript_content(podcast_id, episode_number, transcript_text)

    except Exception as e:
        print(f"Error processing new episode {episode_number}: {e}")
        db.set_transcript_status(podcast_id, episode_number, "error")


def run_transcript_update(episode_number: int, content: str):
    """Background task to update transcript content."""
    db = VectorDatabase()
    # Assume podcast ID 1 for Conduit
    db.update_transcript_content(1, episode_number, content)


@router.put(
    "/episode/{episode_number}/transcript",
    response_model=EpisodeResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_episode_transcript(
    episode_number: int,
    update: TranscriptUpdate,
    background_tasks: BackgroundTasks,
    podcast: str = Query("Conduit", description="Podcast name"),
):
    """Update transcript content for a specific episode."""
    try:
        db = VectorDatabase()

        # Set status to processing immediately
        success = db.set_transcript_status(1, episode_number, "processing")

        if not success:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to initiate update for episode {episode_number}",
            )

        # Add background task
        background_tasks.add_task(run_transcript_update, episode_number, update.content)

        # Return the episode with processing status
        # We need to get the episode again to return the response
        return await get_episode(episode_number, podcast)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error updating transcript: {str(e)}"
        )

        # Return the updated episode
        return await get_episode(episode_number, podcast)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error updating transcript: {str(e)}"
        )


@router.post(
    "/episodes/{episode_number}/transcribe",
    response_model=EpisodeResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
async def transcribe_episode(
    episode_number: int,
    background_tasks: BackgroundTasks,
    podcast_id: int = Query(1, description="Podcast ID"),
    feed_url: Optional[str] = Query(None, description="Override RSS feed URL"),
):
    """
    Trigger transcription for a specific episode.
    """
    from podcast_transcription_core.utils.rss import (
        fetch_episode_by_number,
        CONDUIT_RSS_FEED,
    )
    from podcast_transcription_core.models import Transcript
    import frontmatter

    db = VectorDatabase()

    # Update feed URL if provided
    if feed_url:
        db.update_podcast_feed_url(podcast_id, feed_url)

    # Get current feed URL from DB
    podcast = db.get_podcast(podcast_id)
    current_feed_url = (
        podcast.feed_url if podcast and podcast.feed_url else CONDUIT_RSS_FEED
    )

    # Check if exists and completed
    session = db.Session()
    existing_transcript = (
        session.query(Transcript)
        .filter(
            Transcript.episode_number == episode_number,
            Transcript.podcast == podcast_id,
        )
        .first()
    )
    session.close()

    if existing_transcript and existing_transcript.processing_status == "completed":
        # Return existing
        return await get_episode(episode_number, "Conduit")

    # Fetch episode details
    episode_data = fetch_episode_by_number(episode_number, current_feed_url)
    if not episode_data:
        raise HTTPException(
            status_code=404, detail=f"Episode {episode_number} not found in RSS feed"
        )

    # If it exists but failed or is new, we proceed

    if not existing_transcript:
        # Create placeholder
        post = frontmatter.Post(content="")
        post.metadata = {
            "title": episode_data["title"],
            "episode_number": episode_number,
            "description": episode_data["description"],
            "url": episode_data["url"],
            "pub_date": episode_data["pub_date"],
            "audio_url": episode_data["audio_url"],
        }
        db.process_frontmatter_post(post)

    # Set status
    db.set_transcript_status(podcast_id, episode_number, "processing")

    # Add background task
    background_tasks.add_task(
        process_new_episode_transcription,
        podcast_id,
        episode_number,
        episode_data["audio_url"],
    )

    # Return placeholder/status
    return EpisodeResponse(
        episode_number=episode_number,
        podcast="Conduit",
        metadata=EpisodeMetadata(
            title=episode_data["title"],
            description=episode_data["description"],
            url=episode_data["url"],
            pub_date=str(episode_data["pub_date"]),
        ),
        content="",
        chunks_count=0,
        processing_status="processing",
    )


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

        content = ""
        if transcript.meta and "content" in transcript.meta:
            content = transcript.meta["content"]
        elif transcript.chunks:
            # Fallback to joining chunks if no full content in meta
            chunks = sorted(transcript.chunks, key=lambda x: x.created_at)
            content = " ".join(chunk.content for chunk in chunks)

        session.close()

        return EpisodeResponse(
            episode_number=episode_number,
            podcast=podcast,
            metadata=metadata,
            content=content,
            chunks_count=chunks_count,
            processing_status=transcript.processing_status or "completed",
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
