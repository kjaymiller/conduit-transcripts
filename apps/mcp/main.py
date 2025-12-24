"""Main entry point for MCP server app."""

import uvicorn
from conduit_transcripts.config import settings
from apps.mcp.server import app


def main():
    """Run the MCP server."""
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)


if __name__ == "__main__":
    main()
