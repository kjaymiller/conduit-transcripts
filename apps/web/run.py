"""Entry point for web app."""

import uvicorn
from conduit_transcripts.config import settings


def main():
    """Run the web app."""
    uvicorn.run("apps.web.main:app", host=settings.API_HOST, port=settings.API_PORT, reload=True)


if __name__ == "__main__":
    main()
