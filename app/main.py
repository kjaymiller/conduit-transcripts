from typing import Optional
from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from contextlib import asynccontextmanager

from app.mcp.server import mcp


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Conduit Transcripts API",
    description="API for searching and managing podcast transcripts",
    version="0.1.0",
    lifespan=lifespan,
)

# Mount the MCP server
app.mount("/mcp", mcp.sse_app())

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/episodes", response_class=HTMLResponse)
async def episodes_list(
    request: Request,
    limit: int = 100,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    from podcast_transcription_core.database.postgres import VectorDatabase
    from podcast_transcription_core.models import Transcript
    from datetime import datetime

    db = VectorDatabase()
    session = db.Session()

    query = session.query(Transcript)

    if start_date:
        try:
            start_dt = datetime.fromisoformat(start_date)
            query = query.filter(Transcript.published_date >= start_dt)
        except ValueError:
            pass  # Ignore invalid dates for now or handle appropriately

    if end_date:
        try:
            end_dt = datetime.fromisoformat(end_date)
            query = query.filter(Transcript.published_date <= end_dt)
        except ValueError:
            pass

    transcripts = query.order_by(Transcript.episode_number.desc()).limit(limit).all()

    session.close()

    return templates.TemplateResponse(
        "episodes.html",
        {
            "request": request,
            "episodes": transcripts,
            "start_date": start_date,
            "end_date": end_date,
        },
    )


@app.get("/episode/{episode_number}", response_class=HTMLResponse)
async def episode_detail(request: Request, episode_number: int):
    from podcast_transcription_core.database.postgres import VectorDatabase
    from podcast_transcription_core.models import Transcript, VectorChunk

    db = VectorDatabase()
    session = db.Session()

    transcript = (
        session.query(Transcript)
        .filter(Transcript.episode_number == episode_number)
        .first()
    )

    transcript_text = None
    if transcript:
        if transcript.meta and "content" in transcript.meta:
            transcript_text = transcript.meta["content"]
        elif transcript.chunks:
            chunks = sorted(transcript.chunks, key=lambda x: x.created_at)
            transcript_text = " ".join(chunk.content for chunk in chunks)

    session.close()

    return templates.TemplateResponse(
        "episode.html",
        {
            "request": request,
            "episode": transcript,
            "transcript": transcript_text,
        },
    )


@app.get("/search", response_class=HTMLResponse)
async def search(
    request: Request,
    query: str,
    search_type: str = "text",
    limit: int = 20,
    episode_number: Optional[str] = None,
):
    from podcast_transcription_core.database.postgres import VectorDatabase
    from podcast_transcription_core.models import Transcript, VectorChunk
    from podcast_transcription_core.config import settings

    # Process episode_number: treat empty string as None, otherwise parse to int
    episode_num: Optional[int] = None
    if episode_number and episode_number.strip():
        try:
            episode_num = int(episode_number)
        except ValueError:
            # If invalid integer is passed (like "abc"), ignore it or treat as None
            # Could also raise HTTPException(422) if strict validation is desired
            pass

    db = VectorDatabase()
    session = db.Session()

    results = []

    if search_type == "vector":
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

        vector_results = session.execute(
            stmt.order_by(VectorChunk.embedding.l2_distance(query_embedding)).limit(
                limit
            )
        ).all()

        results = [
            {
                "episode_number": chunk.episode_number,
                "content": chunk.content,
                "score": 1.0 / (1.0 + distance) if distance is not None else 0.0,
            }
            for chunk, distance in vector_results
        ]

    elif search_type == "title":
        # Title search is on Transcript model, not VectorChunk
        # It handles episode_number differently (it's a property of Transcript)
        stmt = session.query(Transcript).filter(Transcript.title.ilike(f"%{query}%"))

        if episode_num is not None:
            stmt = stmt.filter(Transcript.episode_number == episode_num)

        transcripts = stmt.limit(limit).all()

        results = [
            {
                "episode_number": t.episode_number,
                "title": t.title,
                "description": t.description,
            }
            for t in transcripts
        ]

    else:
        # Text search
        stmt = session.query(VectorChunk).filter(
            VectorChunk.content.ilike(f"%{query}%")
        )

        if episode_num is not None:
            stmt = stmt.filter(VectorChunk.episode_number == episode_num)

        chunks = stmt.limit(limit).all()

        results = [
            {
                "episode_number": chunk.episode_number,
                "content": chunk.content,
            }
            for chunk in chunks
        ]

    session.close()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "results": results,
            "query": query,
            "episode_number": episode_num,
        },
    )


@app.get("/health")
async def health_check():
    try:
        from podcast_transcription_core.database.postgres import VectorDatabase
        from sqlalchemy import text

        db = VectorDatabase()
        session = db.Session()
        session.execute(text("SELECT 1"))
        session.close()

        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": f"error: {str(e)}"}


from app.api.routes import router

app.include_router(router, prefix="/api/v1")
