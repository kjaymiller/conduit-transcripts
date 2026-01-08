from mcp.server.fastmcp import FastMCP
from sqlalchemy import select

from podcast_transcription_core.database.postgres import VectorDatabase
from podcast_transcription_core.config import settings
from podcast_transcription_core.models import VectorChunk, Transcript

# Initialize FastMCP with 0.0.0.0 host to disable DNS rebinding protection
# This allows access via external domains like conduit.kjaymiller.dev
mcp = FastMCP("Conduit Transcripts Server", host="0.0.0.0")


@mcp.tool()
def search_transcripts(
    query: str,
    limit: int = 10,
    use_vector: bool = True,
    episode_number: int | None = None,
) -> str:
    """Search through Conduit podcast transcripts.

    Args:
        query: Search query text
        limit: Maximum number of results (1-100)
        use_vector: If True, use semantic vector search; if False, use keyword text search
        episode_number: Optional episode number to filter results

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

            stmt = select(
                VectorChunk,
                VectorChunk.embedding.l2_distance(query_embedding).label("distance"),
            )

            if episode_number is not None:
                stmt = stmt.filter(VectorChunk.episode_number == episode_number)

            search_results = session.execute(
                stmt.order_by(VectorChunk.embedding.l2_distance(query_embedding)).limit(
                    limit
                )
            ).all()

            for chunk, distance in search_results:
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
            stmt = session.query(VectorChunk).filter(
                VectorChunk.content.ilike(f"%{query}%")
            )

            if episode_number is not None:
                stmt = stmt.filter(VectorChunk.episode_number == episode_number)

            search_results = stmt.limit(limit).all()

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
def list_episodes(
    limit: int = 20, start_date: str | None = None, end_date: str | None = None
) -> str:
    """List all available Conduit episodes.

    Args:
        limit: Maximum number of episodes to return (1-100)
        start_date: Filter episodes published on or after this date (ISO format YYYY-MM-DD)
        end_date: Filter episodes published on or before this date (ISO format YYYY-MM-DD)

    Returns:
        JSON string with list of episodes
    """
    try:
        from datetime import datetime

        db = VectorDatabase()
        session = db.Session()

        query = session.query(Transcript).filter(Transcript.podcast == "Conduit")

        if start_date:
            try:
                start_dt = datetime.fromisoformat(start_date)
                query = query.filter(Transcript.published_date >= start_dt)
            except ValueError:
                return f"Error: Invalid start_date format '{start_date}'. Use ISO format YYYY-MM-DD."

        if end_date:
            try:
                end_dt = datetime.fromisoformat(end_date)
                query = query.filter(Transcript.published_date <= end_dt)
            except ValueError:
                return f"Error: Invalid end_date format '{end_date}'. Use ISO format YYYY-MM-DD."

        transcripts = (
            query.order_by(Transcript.episode_number.desc()).limit(limit).all()
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
