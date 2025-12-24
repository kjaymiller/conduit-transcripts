"""Transcribe API endpoints."""

import logging
import pathlib
import shutil
import tempfile
import re
import uuid
from typing import Optional, List, Dict, Any
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

import arrow
import frontmatter
from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks, Form
from fastapi.responses import JSONResponse, HTMLResponse
from sqlalchemy import text, or_
from sqlalchemy.types import String
from sqlalchemy.sql.expression import cast

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
)
from conduit_transcripts.utils.tracker import tracker, TaskStatus

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

# Thread pool for parallel ingestion
# Using threads since embedding calls (to Ollama/OpenAI) are I/O bound
# or handled by external libraries that might release GIL
_executor = ThreadPoolExecutor(max_workers=4)

ARROW_FMT = r"MMMM[\s+]D[\w+,\s+]YYYY"


def get_transcriber():
    """Lazy load transcriber to avoid model loading on startup."""
    global _transcriber
    if _transcriber is None:
        _transcriber = HybridTranscriber(
            model=settings.TRANSCRIPTION_MODEL,
            prefer_mlx=settings.TRANSCRIBE_PREFER_MLX,
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


def process_single_file(job_id: str, file_path: Path, filename: str):
    """Process a single file in a background thread."""
    try:
        tracker.update_file_status(job_id, filename, TaskStatus.PROCESSING)

        # Read content
        content = file_path.read_text(encoding="utf-8")

        # Parse frontmatter
        post = frontmatter.loads(content)

        # Extract episode number
        if "episode_number" not in post.metadata:
            episode_match = re.match(r"^\d+", str(post.metadata.get("title", "")))
            if not episode_match:
                raise ValueError("Could not extract episode number from title")
            episode_number = int(episode_match.group())
        else:
            episode_number = int(str(post.metadata["episode_number"]))

        tracker.update_file_status(
            job_id, filename, TaskStatus.PROCESSING, episode_number=episode_number
        )

        # Process with VectorDatabase
        db = VectorDatabase()
        success = db.process_frontmatter_post(post)

        if success:
            tracker.update_file_status(job_id, filename, TaskStatus.COMPLETED)
        else:
            tracker.update_file_status(
                job_id, filename, TaskStatus.FAILED, error="Database processing failed"
            )

    except Exception as e:
        logger.error(f"Error processing file {filename}: {e}")
        tracker.update_file_status(job_id, filename, TaskStatus.FAILED, error=str(e))
    finally:
        # Clean up temp file
        if file_path.exists():
            try:
                file_path.unlink()
            except Exception as e:
                logger.warning(f"Failed to delete temp file {file_path}: {e}")


@app.post("/ingest/files")
async def ingest_files(
    background_tasks: BackgroundTasks, files: list[UploadFile] = File(...)
):
    """
    Ingest multiple transcript markdown files in parallel.
    Returns a job ID to track progress.
    """
    filenames = [f.filename or f"unknown_{uuid.uuid4()}.md" for f in files]
    job_id = tracker.create_job(filenames)

    # Save files to disk first so threads can access them
    temp_dir = Path(tempfile.gettempdir()) / "conduit_ingest" / job_id
    temp_dir.mkdir(parents=True, exist_ok=True)

    for i, file in enumerate(files):
        filename = filenames[i]
        file_path = temp_dir / filename
        try:
            with file_path.open("wb") as f:
                shutil.copyfileobj(file.file, f)

            # Submit to thread pool
            background_tasks.add_task(process_single_file, job_id, file_path, filename)
        except Exception as e:
            tracker.update_file_status(
                job_id, filename, TaskStatus.FAILED, error=f"Upload failed: {str(e)}"
            )

    return JSONResponse(
        status_code=202,
        content={
            "job_id": job_id,
            "message": f"Started ingestion for {len(files)} files",
            "status_url": f"/ingest/status/{job_id}",
        },
    )


@app.get("/ingest/status/{job_id}")
async def get_ingest_status(job_id: str):
    """Get status of an ingestion job."""
    job = tracker.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job.dict()


@app.post("/ingest/file")
async def ingest_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    """Legacy endpoint for single file ingestion - redirects to multi-file handler."""
    return await ingest_files(background_tasks, [file])


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


async def transcribe_file_background(episode_number: int, file_path: Path):
    """Background task to transcribe an uploaded file."""
    try:
        logger.info(
            f"Starting transcription for uploaded file, episode {episode_number}"
        )

        # Transcribe
        transcriber = get_transcriber()
        transcription = transcriber.transcribe(file_path)

        # Create frontmatter post
        post = frontmatter.Post(content=transcription)
        post.metadata["title"] = f"{episode_number} - Uploaded Episode"
        post.metadata["episode_number"] = episode_number
        post.metadata["description"] = (
            f"Transcription of uploaded episode {episode_number}"
        )
        post.metadata["url"] = "uploaded-file"
        post.metadata["pub_date"] = arrow.now().format(ARROW_FMT)

        # Process with VectorDatabase
        db = VectorDatabase()
        success = db.process_frontmatter_post(post)

        # Clean up temp file
        file_path.unlink()

        if success:
            logger.info(
                f"Successfully transcribed and ingested uploaded episode {episode_number}"
            )
        else:
            logger.error(
                f"Failed to ingest transcription for uploaded episode {episode_number}"
            )

    except Exception as e:
        logger.error(f"Error in background file transcription: {e}")
        # Ensure cleanup even on error
        if file_path.exists():
            file_path.unlink()


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
        if episode_number and audio_url:
            background_tasks.add_task(
                transcribe_episode_background, episode_number, audio_url
            )
        elif audio_url and not episode_number:
            # Case where only URL is provided - user should ideally provide episode number
            # but we can try to extract or fail gracefully or handle it.
            # For now, let's require episode number if using internal logic, or just fail if not found.
            # Actually, the logic above sets episode_number to None if not provided.
            # If we have audio_url but no episode_number, transcribe_episode_background expects int.
            # We might need to generate one or update existing logic.
            # For simplicity, if episode_number is missing, we can't ingest properly with current DB model.
            # We could parse URL for number.
            raise HTTPException(
                status_code=400, detail="Episode number is required for ingestion."
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


@app.post("/transcribe/file", response_model=TranscribeResponse)
async def transcribe_uploaded_file(
    background_tasks: BackgroundTasks,
    episode_number: int = Form(...),
    file: UploadFile = File(...),
):
    """Upload and transcribe an audio file."""
    try:
        # Save uploaded file to temp file
        # We need to preserve the extension for some transcribers/ffmpeg to hint format
        filename = file.filename or "upload.mp3"
        suffix = Path(filename).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = Path(tmp.name)

        background_tasks.add_task(transcribe_file_background, episode_number, tmp_path)

        return TranscribeResponse(
            status="accepted",
            message="File uploaded and transcription started in background",
            episode_number=episode_number,
        )

    except Exception as e:
        logger.error(f"Error handling file upload: {e}")
        raise HTTPException(
            status_code=500, detail=f"Error handling file upload: {str(e)}"
        )


@app.get("/transcripts")
async def list_transcripts(limit: int = 100, offset: int = 0, q: Optional[str] = None):
    """List all ingested transcripts."""
    try:
        db = VectorDatabase()
        session = db.Session()

        query = session.query(Transcript).filter(Transcript.podcast == "Conduit")

        if q:
            # Search in title or content within the JSONB meta field
            search_term = f"%{q}%"
            query = query.filter(
                or_(
                    cast(Transcript.meta["title"], String).ilike(search_term),
                    cast(Transcript.meta["content"], String).ilike(search_term),
                    cast(Transcript.episode_number, String).ilike(search_term),
                )
            )

        # Query transcripts sorted by episode number descending
        transcripts = (
            query.order_by(Transcript.episode_number.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )

        result = []
        for t in transcripts:
            chunks_count = len(t.chunks)
            title = t.meta.get("title", f"Episode {t.episode_number}")
            pub_date = t.meta.get("pub_date", "")

            result.append(
                {
                    "episode_number": t.episode_number,
                    "title": title,
                    "pub_date": pub_date,
                    "chunks_count": chunks_count,
                    "created_at": t.created_at.isoformat() if t.created_at else None,
                }
            )

        session.close()
        return {"transcripts": result, "count": len(result)}

    except Exception as e:
        logger.error(f"Error listing transcripts: {e}")
        raise HTTPException(
            status_code=500, detail=f"Error listing transcripts: {str(e)}"
        )


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the ingestion UI."""
    template_path = Path(__file__).parent / "templates" / "index.html"
    if not template_path.exists():
        return HTMLResponse(
            content="<h1>Error: Template not found</h1>", status_code=500
        )

    return HTMLResponse(content=template_path.read_text(encoding="utf-8"))
