from fastapi import FastAPI

app = FastAPI(
    title="Conduit Transcripts API",
    description="API for searching and managing podcast transcripts",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "Conduit Transcripts API",
        "version": "0.1.0",
        "endpoints": {
            "health": "/health",
            "search_vector": "/api/v1/search/vector",
            "search_text": "/api/v1/search/text",
            "episodes": "/api/v1/episodes",
            "episode": "/api/v1/episode/{episode_number}",
        },
    }


@app.get("/health")
async def health_check():
    try:
        from conduit_transcripts.database.postgres import VectorDatabase

        db = VectorDatabase()
        session = db.Session()
        session.execute("SELECT 1")
        session.close()

        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": f"error: {str(e)}"}


from app.api.routes import router

app.include_router(router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    try:
        from conduit_transcripts.database.postgres import VectorDatabase

        db = VectorDatabase()
        session = db.Session()
        session.execute("SELECT 1")
        session.close()

        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": f"error: {str(e)}"}
