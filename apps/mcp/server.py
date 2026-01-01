"""MCP server implementation for transcript search and RAG."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp.server import FastMCP

from conduit_transcripts.search import actions

# Configure logging
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Conduit Transcript MCP Server",
    description="MCP server for searching and summarizing podcast transcripts",
    version="1.0.0",
)

# Create MCP Server
mcp = FastMCP("Conduit Transcripts")


@mcp.tool()
def search_transcripts(
    query: str, limit: int = 10, similarity_threshold: float = 0.0
) -> str:
    """
    Search transcripts using vector similarity.
    Returns formatted results suitable for LLM context.
    """
    results = actions.vector_search(query, limit, similarity_threshold)

    if not results:
        return "No matching transcripts found."

    output = [f"Found {len(results)} results for '{query}':\n"]
    for r in results:
        output.append(f"Episode {r.episode_number}: {r.title}")
        output.append(f"URL: {r.url}")
        output.append(f"Content: {r.content_snippet}")
        output.append(f"Similarity: {r.similarity_score}")
        output.append("---")

    return "\n".join(output)


@mcp.tool()
def search_titles(query: str) -> str:
    """
    Search transcripts by title.
    Returns formatted results suitable for LLM context.
    """
    results = actions.title_search(query)

    if not results:
        return f"No transcripts found with title matching '{query}'."

    output = [f"Found {len(results)} results for title '{query}':\n"]
    for r in results:
        output.append(f"Episode {r.episode_number}: {r.title}")
        output.append(f"URL: {r.url}")
        output.append(f"Description: {r.description}")
        output.append("---")

    return "\n".join(output)


@mcp.tool()
def get_episode_transcript(episode_number: int, podcast: str = "Conduit") -> str:
    """Get full transcript for a specific episode."""
    result = actions.get_episode_details(episode_number, podcast)
    if not result:
        return f"Episode {episode_number} not found."

    metadata = result["metadata"]
    return (
        f"Title: {metadata.get('title')}\n"
        f"Date: {metadata.get('pub_date')}\n"
        f"URL: {metadata.get('url')}\n"
        f"Content:\n{result['content']}"
    )


# Mount MCP SSE app
try:
    app.mount("/mcp", mcp.sse_app())
except Exception as e:
    logger.error(f"Failed to mount MCP app: {e}")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "mcp"}
