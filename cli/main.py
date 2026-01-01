"""CLI tool for Conduit Transcripts."""

import logging
import pathlib
import typing

import typer
from rich.console import Console
from rich.table import Table
from sqlalchemy import select

# Imports moved to functions for lazy loading


# Silence noisy loggers
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

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
        from conduit_transcripts.config import settings
        from conduit_transcripts.database.postgres import VectorDatabase
        from conduit_transcripts.models import VectorChunk

        db = VectorDatabase()
        session = db.Session()

        if vector:
            # Vector search using PostgreSQL
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
        from conduit_transcripts.database.postgres import VectorDatabase
        from conduit_transcripts.models import Transcript

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

            if transcript.title:
                console.print(f"[white]Title: {transcript.title}[/white]")
            if transcript.description:
                console.print(
                    f"[white]Description: {transcript.description[:100]}...[/white]"
                )
        else:
            console.print(f"[red]✗ Episode {episode_number} not found[/red]")

        session.close()

    except Exception as e:
        console.print(f"[red]Error checking status: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def transcribe(
    episodes: typing.List[str] = typer.Argument(
        ..., help="Episode number(s) to transcribe (e.g. 100, 100-105, 'latest')"
    ),
    model: str = typer.Option("base", "--model", "-m", help="Model size"),
    prefer_mlx: bool = typer.Option(
        False,
        "--prefer-mlx/--no-mlx",
        help="Prefer MLX",
        envvar="TRANSCRIBE_PREFER_MLX",
    ),
    ingest: bool = typer.Option(
        True, "--ingest/--no-ingest", help="Ingest after transcription"
    ),
):
    """Transcribe an episode."""
    try:
        from conduit_transcripts.transcription.metadata import (
            get_audio_url_from_episode_number,
            fetch_latest_episode_number,
        )

        episode_list = []
        for ep_str in episodes:
            if ep_str.lower() == "latest":
                episode_list.append(fetch_latest_episode_number())
            elif ep_str.lower() == "all":
                latest = fetch_latest_episode_number()
                episode_list.extend(range(1, latest + 1))
            elif "-" in ep_str:
                start, end = map(int, ep_str.split("-"))
                episode_list.extend(range(start, end + 1))
            elif "," in ep_str:
                episode_list.extend(map(int, ep_str.split(",")))
            else:
                episode_list.append(int(ep_str))

        for episode_number in episode_list:
            console.print(
                f"[blue]Fetching audio URL for episode {episode_number}...[/blue]"
            )
            result = get_audio_url_from_episode_number(episode_number)

            if result is None:
                console.print(
                    f"[red]Could not fetch metadata for episode {episode_number}[/red]"
                )
                continue

            metadata, audio_url = result
            console.print(f"[green]Found audio URL: {audio_url}[/green]")

            # Download audio
            from conduit_transcripts.transcription.audio import download_audio_file

            audio_file = download_audio_file(audio_url)
            console.print(f"[green]Downloaded audio to: {audio_file}[/green]")

            # Transcribe
            console.print(f"[blue]Transcribing with {model} model...[/blue]")
            from conduit_transcripts.transcription import HybridTranscriber

            transcriber = HybridTranscriber(model=model, prefer_mlx=prefer_mlx)
            transcription = transcriber.transcribe(audio_file)

            # Save transcription
            import slugify

            slug = slugify.slugify(metadata["title"])
            output_file = pathlib.Path(f"transcripts/{slug}.md")
            output_file.parent.mkdir(exist_ok=True)

            import frontmatter

            post = frontmatter.Post(content=transcription, **metadata)
            # Ensure episode number is in metadata
            post.metadata["episode_number"] = episode_number

            with output_file.open("w") as f:
                f.write(frontmatter.dumps(post))

            console.print(f"[green]Transcription saved to: {output_file}[/green]")

            # Cleanup
            audio_file.unlink()

            if ingest:
                console.print(f"[blue]Ingesting {output_file}...[/blue]")
                from conduit_transcripts.database.postgres import VectorDatabase

                db = VectorDatabase()
                success = db.process_frontmatter_post(post)
                if success:
                    console.print(
                        f"[green]✓ Successfully ingested to PostgreSQL[/green]"
                    )
                else:
                    console.print(f"[red]✗ Failed to ingest to PostgreSQL[/red]")

                # Try OpenSearch
                try:
                    from conduit_transcripts.database.opensearch import (
                        OpenSearchDatabase,
                    )

                    os_db = OpenSearchDatabase()
                    os_success = os_db.process_frontmatter_post(post)
                    if os_success:
                        console.print(
                            f"[green]✓ Successfully ingested to OpenSearch[/green]"
                        )
                    else:
                        console.print(f"[red]✗ Failed to ingest to OpenSearch[/red]")
                except ImportError:
                    console.print("[yellow]OpenSearch support not available[/yellow]")
                except Exception as e:
                    console.print(f"[red]Error indexing to OpenSearch: {e}[/red]")

    except Exception as e:
        console.print(f"[red]Error transcribing: {e}[/red]")
        raise typer.Exit(1)


@app.command(name="transcribe-file")
def transcribe_file(
    file_path: pathlib.Path = typer.Argument(
        ..., help="Path to audio file", exists=True
    ),
    model: str = typer.Option("base", "--model", "-m", help="Model size"),
    prefer_mlx: bool = typer.Option(
        False,
        "--prefer-mlx/--no-mlx",
        help="Prefer MLX",
        envvar="TRANSCRIBE_PREFER_MLX",
    ),
    output: pathlib.Path = typer.Option(
        None, "--output", "-o", help="Output file path"
    ),
):
    """Transcribe a local audio file."""
    try:
        console.print(f"[blue]Transcribing {file_path} with {model} model...[/blue]")
        from conduit_transcripts.transcription import HybridTranscriber

        transcriber = HybridTranscriber(model=model, prefer_mlx=prefer_mlx)
        transcription = transcriber.transcribe(file_path)

        if output:
            output_file = output
        else:
            output_file = file_path.with_suffix(".txt")

        output_file.write_text(transcription)
        console.print(f"[green]Transcription saved to: {output_file}[/green]")

    except Exception as e:
        console.print(f"[red]Error transcribing file: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def ingest(
    files: typing.Optional[typing.List[pathlib.Path]] = typer.Argument(
        None, help="Specific file(s) to ingest"
    ),
    directory: pathlib.Path = typer.Option(
        pathlib.Path("transcripts"), "--dir", help="Directory to ingest"
    ),
    reindex: bool = typer.Option(False, "--reindex", help="Recreate tables/indexes"),
    pg_only: bool = typer.Option(False, "--pg-only", help="Ingest only to PostgreSQL"),
    os_only: bool = typer.Option(False, "--os-only", help="Ingest only to OpenSearch"),
):
    """Ingest transcript files."""
    try:
        import frontmatter

        # Gather files
        files_to_process = []
        if files:
            files_to_process.extend(files)
        else:
            if directory.exists():
                files_to_process.extend(directory.glob("*.md"))

        if not files_to_process:
            console.print("[yellow]No files found to ingest[/yellow]")
            raise typer.Exit(0)

        pg_db = None
        os_db = None

        if not os_only:
            console.print("[blue]Initializing PostgreSQL database...[/blue]")
            from conduit_transcripts.database.postgres import VectorDatabase

            pg_db = VectorDatabase(recreate_tables=reindex)

        if not pg_only:
            try:
                from conduit_transcripts.database.opensearch import OpenSearchDatabase

                os_db = OpenSearchDatabase()
                if reindex:
                    console.print("[blue]Recreating OpenSearch index...[/blue]")
                    os_db.create_index()
            except ImportError:
                console.print(
                    "[yellow]OpenSearch support not available. Skipping OpenSearch indexing.[/yellow]"
                )
                if not pg_db:
                    console.print(
                        "[red]No databases available to write to. Exiting.[/red]"
                    )
                    raise typer.Exit(1)

        with console.status(
            f"[bold green]Ingesting {len(files_to_process)} files..."
        ) as status:
            success_count = 0
            fail_count = 0

            for file_path in files_to_process:
                status.update(f"Processing {file_path.name}...")
                try:
                    # Load frontmatter
                    with file_path.open("r") as f:
                        post = frontmatter.load(f)

                    file_success = True

                    if pg_db:
                        if not pg_db.process_frontmatter_post(post):
                            file_success = False
                            console.print(
                                f"[red]Failed to ingest {file_path.name} to PostgreSQL[/red]"
                            )

                    if os_db:
                        if not os_db.process_frontmatter_post(post):
                            # Don't mark as full failure if only OS fails, unless OS-only
                            if os_only:
                                file_success = False
                            console.print(
                                f"[red]Failed to ingest {file_path.name} to OpenSearch[/red]"
                            )

                    if file_success:
                        success_count += 1
                    else:
                        fail_count += 1

                except Exception as e:
                    fail_count += 1
                    console.print(f"[red]Error processing {file_path.name}: {e}[/red]")

        console.print(f"\n[bold]Ingestion complete![/bold]")
        console.print(f"[green]Successful: {success_count}[/green]")
        if fail_count > 0:
            console.print(f"[red]Failed: {fail_count}[/red]")

    except Exception as e:
        console.print(f"[red]Error during ingestion: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def list(
    limit: int = typer.Option(20, "--limit", "-l", help="Maximum episodes to show"),
):
    """List episodes."""
    try:
        from conduit_transcripts.database.postgres import VectorDatabase
        from conduit_transcripts.models import Transcript

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
            table.add_row(
                str(transcript.episode_number),
                transcript.title or "No title",
                str(transcript.published_date)
                if transcript.published_date
                else "Unknown",
            )

        console.print(table)
        session.close()

    except Exception as e:
        console.print(f"[red]Error listing episodes: {e}[/red]")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
