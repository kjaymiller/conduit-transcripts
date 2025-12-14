"""Main entry point for transcribe app."""

import uvicorn
from conduit_transcripts.config import settings
from apps.transcribe.api import app

if __name__ == "__main__":
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)
