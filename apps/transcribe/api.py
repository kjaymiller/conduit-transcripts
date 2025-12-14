"""Transcribe API endpoints."""

import logging
import pathlib
from typing import Optional

import arrow
import frontmatter
from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse

from conduit_transcripts.config import settings
from conduit_transcripts.database.postgres import VectorDatabase
from conduit_transcripts.models import Transcript
from conduit_transcripts.transcription import HybridTranscriber
from conduit_transcripts.transcription.metadata import get_audio_url_from_episode_number
from conduit_transcripts.transcription.audio import download_audio_file
from apps.transcribe.models import (
    TranscribeRequest,
    TranscribeResponse,
    HealthResponse,
    StatusResponse,
    IngestResponse,
)

# Configure logging
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Conduit Transcript Transcription API",
    description="API for transcribing audio and ingesting transcripts",
    version="1.0.0",
)

# Initialize transcriber (lazy loading)
_transcriber = None

ARROW_FMT = r"MMMM[\s+]D[\w+,\s+]YYYY"


def get_transcriber():
    """Lazy load transcriber to avoid model loading on startup."""
    global _transcriber
    if _transcriber is None:
        _transcriber = HybridTranscriber(
            model=settings.TRANSCRIPTION_MODEL, prefer_mlx=settings.PREFER_MLX
        )
    return _transcriber


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Check API and database health."""
    try:
        # Test database connection
        db = VectorDatabase()
        with db.engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        return HealthResponse(
            status="healthy",
            database="connected",
            message="API is running and database is accessible",
        )
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail=f"Service unavailable: {str(e)}")


@app.get("/status/{episode_number}", response_model=StatusResponse)
async def check_status(episode_number: int):
    """Check if an episode has been ingested."""
    try:
        db = VectorDatabase()
        session = db.Session()

        # Query for the transcript
        transcript = (
            session.query(Transcript)
            .filter(
                Transcript.episode_number == episode_number,
                Transcript.podcast == "Conduit",
            )
            .first()
        )

        if transcript:
            chunks_count = len(transcript.chunks)
            session.close()
            return StatusResponse(
                episode_number=episode_number, ingested=True, chunks_count=chunks_count
            )
        else:
            session.close()
            return StatusResponse(
                episode_number=episode_number, ingested=False, chunks_count=None
            )
    except Exception as e:
        logger.error(f"Error checking status: {e}")
        raise HTTPException(status_code=500, detail=f"Error checking status: {str(e)}")


@app.post("/ingest/file")
async def ingest_file(file: UploadFile = File(...)):
    """
    Ingest a transcript markdown file with frontmatter.

    Expected format:
    ---
    title: <episode_number> <episode_title>
    description: <episode_description>
    url: <episode_url>
    pub_date: <publication_date>
    ---
    <transcript_content>
    """
    try:
        # Read file content
        content = await file.read()

        # Parse frontmatter
        post = frontmatter.loads(content.decode("utf-8"))

        # Validate required fields
        required_fields = ["title", "description", "url", "pub_date"]
        for field in required_fields:
            if field not in post.metadata:
                raise HTTPException(
                    status_code=400,
                    detail=f"Missing required field in frontmatter: {field}",
                )

        # Extract episode number
        if "episode_number" not in post.metadata:
            import re

            episode_match = re.match(r"^\d+", post.metadata["title"])
            if not episode_match:
                raise HTTPException(
                    status_code=400,
                    detail="Could not extract episode number from title",
                )
            episode_number = int(episode_match.group())
        else:
            episode_number = int(post.metadata["episode_number"])

        # Process with VectorDatabase
        db = VectorDatabase()
        success = db.process_frontmatter_post(post)

        if success:
            return JSONResponse(
                status_code=200,
                content={
                    "status": "success",
                    "message": f"Ingested episode {episode_number}",
                    "episode_number": episode_number,
                },
            )
        else:
            raise HTTPException(status_code=500, detail="Failed to process transcript")

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error ingesting file: {e}")
        raise HTTPException(status_code=500, detail=f"Error ingesting file: {str(e)}")


async def transcribe_episode_background(episode_number: int, audio_url: str):
    """Background task to transcribe an episode."""
    try:
        logger.info(f"Starting transcription for episode {episode_number}")

        # Download audio file
        audio_file = download_audio_file(audio_url)

        # Transcribe
        transcriber = get_transcriber()
        transcription = transcriber.transcribe(audio_file)

        # Create frontmatter post
        post = frontmatter.Post(content=transcription)
        post.metadata["title"] = f"{episode_number} - Transcribed Episode"
        post.metadata["episode_number"] = episode_number
        post.metadata["description"] = f"Transcription of episode {episode_number}"
        post.metadata["url"] = audio_url
        post.metadata["pub_date"] = arrow.now().format(ARROW_FMT)

        # Process with VectorDatabase
        db = VectorDatabase()
        success = db.process_frontmatter_post(post)

        # Clean up temp file
        audio_file.unlink()

        if success:
            logger.info(
                f"Successfully transcribed and ingested episode {episode_number}"
            )
        else:
            logger.error(f"Failed to ingest transcription for episode {episode_number}")

    except Exception as e:
        logger.error(f"Error in background transcription: {e}")


@app.post("/transcribe", response_model=TranscribeResponse)
async def transcribe_episode(
    request: TranscribeRequest, background_tasks: BackgroundTasks
):
    """
    Trigger transcription of an episode.

    Provide either episode_number (to fetch from Conduit website) or audio_url.
    """
    try:
        # Validate input
        if not request.episode_number and not request.audio_url:
            raise HTTPException(
                status_code=400,
                detail="Must provide either episode_number or audio_url",
            )

        # Get audio URL
        if request.episode_number:
            episode_number = request.episode_number
            try:
                result = get_audio_url_from_episode_number(episode_number)
                if result is None:
                    raise Exception("Could not fetch episode metadata")
                metadata, audio_url = result
            except Exception as e:
                raise HTTPException(
                    status_code=404,
                    detail=f"Could not find episode {episode_number}: {str(e)}",
                )
        else:
            audio_url = request.audio_url
            episode_number = None

        # Start background transcription
        if episode_number:
            background_tasks.add_task(
                transcribe_episode_background, episode_number, audio_url
            )

        return TranscribeResponse(
            status="accepted",
            message="Transcription started in background",
            episode_number=episode_number,
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error starting transcription: {e}")
        raise HTTPException(
            status_code=500, detail=f"Error starting transcription: {str(e)}"
        )


@app.get("/")
async def root():
    """API root endpoint."""
    return {
        "service": "Conduit Transcript Transcription API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "status": "/status/{episode_number}",
            "ingest_file": "/ingest/file",
            "transcribe": "/transcribe",
        },
    }
