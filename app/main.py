from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select

app = FastAPI(
    title="Conduit Transcripts API",
    description="API for searching and managing podcast transcripts",
    version="0.1.0",
)

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/episodes", response_class=HTMLResponse)
async def episodes_list(request: Request, limit: int = 100):
    from podcast_transcription_core.database.postgres import VectorDatabase
    from podcast_transcription_core.models import Transcript

    db = VectorDatabase()
    session = db.Session()

    transcripts = (
        session.query(Transcript)
        .order_by(Transcript.episode_number.desc())
        .limit(limit)
        .all()
    )

    session.close()

    return templates.TemplateResponse(
        "episodes.html", {"request": request, "episodes": transcripts}
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
    if transcript and transcript.chunks:
        chunks = sorted(transcript.chunks, key=lambda x: x.chunk_number or 0)
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
):
    from podcast_transcription_core.database.postgres import VectorDatabase
    from podcast_transcription_core.models import Transcript, VectorChunk
    from podcast_transcription_core.config import settings

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

        vector_results = session.execute(
            select(
                VectorChunk,
                VectorChunk.embedding.l2_distance(query_embedding).label("distance"),
            )
            .order_by(VectorChunk.embedding.l2_distance(query_embedding))
            .limit(limit)
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
        transcripts = (
            session.query(Transcript)
            .filter(Transcript.title.ilike(f"%{query}%"))
            .limit(limit)
            .all()
        )

        results = [
            {
                "episode_number": t.episode_number,
                "title": t.title,
                "description": t.description,
            }
            for t in transcripts
        ]

    else:
        chunks = (
            session.query(VectorChunk)
            .filter(VectorChunk.content.ilike(f"%{query}%"))
            .limit(limit)
            .all()
        )

        results = [
            {
                "episode_number": chunk.episode_number,
                "content": chunk.content,
            }
            for chunk in chunks
        ]

    session.close()

    return templates.TemplateResponse(
        "index.html", {"request": request, "results": results}
    )


@app.get("/health")
async def health_check():
    try:
        from podcast_transcription_core.database.postgres import VectorDatabase

        db = VectorDatabase()
        session = db.Session()
        session.execute("SELECT 1")
        session.close()

        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": f"error: {str(e)}"}


from app.api.routes import router

app.include_router(router, prefix="/api/v1")
