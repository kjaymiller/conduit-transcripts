"""CLI tool for Conduit Transcripts."""

import pathlib
import typing

import typer
from rich.console import Console
from rich.table import Table

from conduit_transcripts.config import settings
from conduit_transcripts.database.postgres import VectorDatabase
from conduit_transcripts.models import Transcript, VectorChunk
from conduit_transcripts.transcription import HybridTranscriber
from conduit_transcripts.transcription.metadata import get_audio_url_from_episode_number

app = typer.Typer(help="Conduit Transcripts CLI")
console = Console()


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    vector: bool = typer.Option(False, "--vector", "-v", help="Use vector search"),
    limit: int = typer.Option(10, "--limit", "-l", help="Maximum results"),
):
    """Search transcripts."""
    try:
        db = VectorDatabase()
        session = db.Session()

        if vector:
            # Vector search
            from langchain_huggingface import HuggingFaceEmbeddings

            embedding_model = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL,
                model_kwargs={"device": settings.EMBEDDING_DEVICE},
                encode_kwargs={"normalize_embeddings": False},
            )
            query_embedding = embedding_model.embed_query(query)

            results = session.execute(
                select(
                    VectorChunk,
                    VectorChunk.embedding.l2_distance(query_embedding).label(
                        "distance"
                    ),
                )
                .order_by(VectorChunk.embedding.l2_distance(query_embedding))
                .limit(limit)
            ).all()

            table = Table(title="Vector Search Results")
            table.add_column("Episode", style="cyan")
            table.add_column("Score", style="green")
            table.add_column("Content", style="white")

            for chunk, distance in results:
                similarity_score = (
                    1.0 / (1.0 + distance) if distance is not None else 0.0
                )
                table.add_row(
                    str(chunk.episode_number),
                    f"{similarity_score:.3f}",
                    chunk.content[:100] + "..."
                    if len(chunk.content) > 100
                    else chunk.content,
                )
        else:
            # Text search
            results = (
                session.query(VectorChunk)
                .filter(VectorChunk.content.ilike(f"%{query}%"))
                .limit(limit)
                .all()
            )

            table = Table(title="Text Search Results")
            table.add_column("Episode", style="cyan")
            table.add_column("Content", style="white")

            for chunk in results:
                table.add_row(
                    str(chunk.episode_number),
                    chunk.content[:100] + "..."
                    if len(chunk.content) > 100
                    else chunk.content,
                )

        console.print(table)
        session.close()

    except Exception as e:
        console.print(f"[red]Error searching: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def status(
    episode_number: int = typer.Argument(..., help="Episode number"),
):
    """Check episode status."""
    try:
        db = VectorDatabase()
        session = db.Session()

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
            console.print(f"[green]✓ Episode {episode_number} is ingested[/green]")
            console.print(f"[blue]Chunks: {chunks_count}[/blue]")

            meta = transcript.meta
            if meta.get("title"):
                console.print(f"[white]Title: {meta['title']}[/white]")
            if meta.get("description"):
                console.print(
                    f"[white]Description: {meta['description'][:100]}...[/white]"
                )
        else:
            console.print(f"[red]✗ Episode {episode_number} not found[/red]")

        session.close()

    except Exception as e:
        console.print(f"[red]Error checking status: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def transcribe(
    episode_number: int = typer.Argument(..., help="Episode number to transcribe"),
    model: str = typer.Option("base", "--model", "-m", help="Model size"),
    prefer_mlx: bool = typer.Option(True, "--prefer-mlx/--no-mlx", help="Prefer MLX"),
):
    """Transcribe an episode."""
    try:
        console.print(
            f"[blue]Fetching audio URL for episode {episode_number}...[/blue]"
        )
        result = get_audio_url_from_episode_number(episode_number)

        if result is None:
            console.print("[red]Could not fetch episode metadata[/red]")
            raise typer.Exit(1)

        metadata, audio_url = result
        console.print(f"[green]Found audio URL: {audio_url}[/green]")

        # Download audio
        from conduit_transcripts.transcription.audio import download_audio_file

        audio_file = download_audio_file(audio_url)
        console.print(f"[green]Downloaded audio to: {audio_file}[/green]")

        # Transcribe
        console.print(f"[blue]Transcribing with {model} model...[/blue]")
        transcriber = HybridTranscriber(model=model, prefer_mlx=prefer_mlx)
        transcription = transcriber.transcribe(audio_file)

        # Save transcription
        output_file = pathlib.Path(f"episode_{episode_number}_transcript.md")
        with output_file.open("w") as f:
            f.write(f"# {metadata['title']}\n\n")
            f.write(f"**Episode:** {episode_number}\n")
            f.write(f"**Description:** {metadata['description']}\n")
            f.write(f"**URL:** {metadata['url']}\n")
            f.write(f"**Published:** {metadata['pub_date']}\n\n")
            f.write("---\n\n")
            f.write(transcription)

        console.print(f"[green]Transcription saved to: {output_file}[/green]")

        # Cleanup
        audio_file.unlink()

    except Exception as e:
        console.print(f"[red]Error transcribing: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def ingest(
    file_path: pathlib.Path = typer.Argument(..., help="Markdown file to ingest"),
):
    """Ingest a transcript file."""
    try:
        import frontmatter

        console.print(f"[blue]Ingesting {file_path}...[/blue]")

        # Load frontmatter
        with file_path.open("r") as f:
            post = frontmatter.load(f)

        # Process with database
        db = VectorDatabase()
        success = db.process_frontmatter_post(post)

        if success:
            console.print(f"[green]✓ Successfully ingested {file_path}[/green]")
        else:
            console.print(f"[red]✗ Failed to ingest {file_path}[/red]")
            raise typer.Exit(1)

    except Exception as e:
        console.print(f"[red]Error ingesting: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def list(
    limit: int = typer.Option(20, "--limit", "-l", help="Maximum episodes to show"),
):
    """List episodes."""
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

        table = Table(title="Episodes")
        table.add_column("Episode", style="cyan")
        table.add_column("Title", style="white")
        table.add_column("Published", style="green")

        for transcript in transcripts:
            meta = transcript.meta
            table.add_row(
                str(transcript.episode_number),
                meta.get("title", "No title"),
                meta.get("pub_date", "Unknown"),
            )

        console.print(table)
        session.close()

    except Exception as e:
        console.print(f"[red]Error listing episodes: {e}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
