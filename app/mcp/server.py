from mcp.server.fastmcp import FastMCP
from sqlalchemy import select

from podcast_transcription_core.database.postgres import VectorDatabase
from podcast_transcription_core.config import settings
from podcast_transcription_core.models import VectorChunk, Transcript

# Initialize FastMCP with 0.0.0.0 host to disable DNS rebinding protection
# This allows access via external domains like conduit.kjaymiller.dev
mcp = FastMCP("Conduit Transcripts Server", host="0.0.0.0")


@mcp.tool()
def search_transcripts(query: str, limit: int = 10, use_vector: bool = True) -> str:
    """Search through Conduit podcast transcripts.

    Args:
        query: Search query text
        limit: Maximum number of results (1-100)
        use_vector: If True, use semantic vector search; if False, use keyword text search

    Returns:
        JSON string with search results
    """
    try:
        db = VectorDatabase()
        session = db.Session()

        results = []
        if use_vector:
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
            search_results = session.execute(
                select(
                    VectorChunk,
                    VectorChunk.embedding.l2_distance(query_embedding).label(
                        "distance"
                    ),
                )
                .order_by(VectorChunk.embedding.l2_distance(query_embedding))
                .limit(limit)
            ).all()

            for chunk, distance in results:
                similarity_score = (
                    1.0 / (1.0 + distance) if distance is not None else 0.0
                )
                results.append(
                    {
                        "episode_number": chunk.episode_number,
                        "podcast": "Conduit",
                        "content_snippet": chunk.content[:200] + "..."
                        if len(chunk.content) > 200
                        else chunk.content,
                        "similarity_score": round(similarity_score, 4),
                    }
                )
        else:
            search_results = (
                session.query(VectorChunk)
                .filter(VectorChunk.content.ilike(f"%{query}%"))
                .limit(limit)
                .all()
            )

            for chunk in search_results:
                results.append(
                    {
                        "episode_number": chunk.episode_number,
                        "podcast": "Conduit",
                        "content_snippet": chunk.content[:200] + "..."
                        if len(chunk.content) > 200
                        else chunk.content,
                    }
                )

        session.close()
        return f"Found {len(results)} results for '{query}': {results}"

    except Exception as e:
        return f"Error searching transcripts: {str(e)}"


@mcp.tool()
def get_episode(episode_number: int) -> str:
    """Get full transcript for a specific episode.

    Args:
        episode_number: Episode number

    Returns:
        JSON string with episode metadata and content
    """
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
            return f"Episode {episode_number} not found"

        result = {
            "episode_number": transcript.episode_number,
            "title": transcript.title,
            "description": transcript.description,
            "url": transcript.url,
            "published_date": str(transcript.published_date)
            if transcript.published_date
            else None,
            "content": transcript.content,
            "chunks_count": len(transcript.chunks),
        }

        session.close()
        return f"Episode {episode_number}: {result}"

    except Exception as e:
        return f"Error retrieving episode: {str(e)}"


@mcp.tool()
def list_episodes(limit: int = 20) -> str:
    """List all available Conduit episodes.

    Args:
        limit: Maximum number of episodes to return (1-100)

    Returns:
        JSON string with list of episodes
    """
    try:
        db = VectorDatabase()
        session = db.Session()

        transcripts = (
            session.query(Transcript)
            .filter(Transcript.podcast == "Conduit")
            .order_by(Transcript.episode_number.desc())
            .limit(limit)
            .all()
        )

        episodes = []
        for transcript in transcripts:
            episodes.append(
                {
                    "episode_number": transcript.episode_number,
                    "title": transcript.title,
                    "description": transcript.description,
                    "url": transcript.url,
                    "published_date": str(transcript.published_date)
                    if transcript.published_date
                    else None,
                }
            )

        session.close()
        return f"Found {len(episodes)} episodes: {episodes}"

    except Exception as e:
        return f"Error listing episodes: {str(e)}"


if __name__ == "__main__":
    import os

    port = int(os.getenv("MCP_PORT", "8001"))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
