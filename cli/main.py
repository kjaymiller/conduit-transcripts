"""CLI tool for Conduit Transcripts."""

import logging
import pathlib
import sys
import typing

import click
from rich.console import Console
from rich.table import Table
from sqlalchemy import select

# Imports moved to functions for lazy loading

# Silence noisy loggers
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

console = Console()


def _parse_episodes(episodes: typing.Tuple[str, ...]) -> typing.List[int]:
    """Parse episode arguments into a list of episode numbers."""
    from podcast_transcription_core.transcription.metadata import (
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

    # Note: Using sorted(set(...)) directly since `list` builtin is shadowed
    # by the CLI's list command in this module
    return sorted(set(episode_list))


@click.group(help="Conduit Transcripts CLI")
def cli():
    pass


@cli.command()
@click.argument("query")
@click.option("--vector", "-v", is_flag=True, help="Use vector search")
@click.option("--title", "-t", is_flag=True, help="Search by title")
@click.option("--limit", "-l", default=10, help="Maximum results")
def search(query: str, vector: bool, title: bool, limit: int):
    """Search transcripts."""
    try:
        from podcast_transcription_core.config import settings
        from podcast_transcription_core.database.postgres import VectorDatabase
        from podcast_transcription_core.models import VectorChunk, Transcript

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
        elif title:
            # Title search
            results = (
                session.query(Transcript)
                .filter(Transcript.title.ilike(f"%{query}%"))
                .limit(limit)
                .all()
            )

            table = Table(title="Title Search Results")
            table.add_column("Episode", style="cyan")
            table.add_column("Title", style="green")
            table.add_column("Description", style="white")

            for transcript in results:
                table.add_row(
                    str(transcript.episode_number),
                    transcript.title,
                    transcript.description[:100] + "..."
                    if transcript.description and len(transcript.description) > 100
                    else (transcript.description or ""),
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
        sys.exit(1)


@cli.command()
@click.argument("episode_number", type=int)
def status(episode_number: int):
    """Check episode status."""
    try:
        from podcast_transcription_core.database.postgres import VectorDatabase
        from podcast_transcription_core.models import Transcript

        db = VectorDatabase()
        session = db.Session()

        transcript = (
            session.query(Transcript)
            .filter(
                Transcript.episode_number == episode_number,
                Transcript.podcast == 1,
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
        sys.exit(1)


@cli.command()
@click.argument("episodes", nargs=-1, required=True)
@click.option("--output-dir", "-o", default="downloads", help="Output directory")
def download(episodes: typing.Tuple[str, ...], output_dir: str):
    """Download episode audio."""
    try:
        from podcast_transcription_core.transcription.audio import (
            download_audio_to_path,
        )
        from podcast_transcription_core.transcription.metadata import (
            get_audio_url_from_episode_number,
        )

        episode_list = _parse_episodes(episodes)
        out_path = pathlib.Path(output_dir)

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

            file_path = out_path / f"{episode_number}.mp3"
            download_audio_to_path(audio_url, file_path)
            console.print(f"[green]Downloaded audio to: {file_path}[/green]")

    except Exception as e:
        console.print(f"[red]Error downloading: {e}[/red]")
        sys.exit(1)


@cli.command()
@click.argument("episodes", nargs=-1, required=True)
@click.option(
    "--model",
    "-m",
    default="nvidia/parakeet-rnnt-1.1b",
    help="Model name",
    envvar="TRANSCRIPTION_MODEL",
)
@click.option("--ingest/--no-ingest", default=True, help="Ingest after transcription")
def transcribe(episodes: typing.Tuple[str, ...], model: str, ingest: bool):
    """Transcribe an episode."""
    try:
        from podcast_transcription_core.transcription.metadata import (
            get_audio_url_from_episode_number,
        )

        episode_list = _parse_episodes(episodes)

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
            from podcast_transcription_core.transcription.audio import (
                download_audio_file,
            )

            audio_file = download_audio_file(audio_url)
            console.print(f"[green]Downloaded audio to: {audio_file}[/green]")

            # Transcribe
            console.print(f"[blue]Transcribing with {model} model...[/blue]")
            from podcast_transcription_core.transcription import ParakeetTranscriber

            transcriber = ParakeetTranscriber(model=model)
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
                from podcast_transcription_core.database.postgres import VectorDatabase

                db = VectorDatabase()
                success = db.process_frontmatter_post(post)
                if success:
                    console.print(
                        f"[green]✓ Successfully ingested to PostgreSQL[/green]"
                    )
                else:
                    console.print(f"[red]✗ Failed to ingest to PostgreSQL[/red]")

    except Exception as e:
        console.print(f"[red]Error transcribing: {e}[/red]")
        sys.exit(1)


@cli.command(name="transcribe-file")
@click.argument("file_path", type=click.Path(exists=True))
@click.option(
    "--model",
    "-m",
    default="nvidia/parakeet-rnnt-1.1b",
    help="Model name",
    envvar="TRANSCRIPTION_MODEL",
)
@click.option("--output", "-o", type=click.Path(), help="Output file path")
def transcribe_file(file_path: str, model: str, output: typing.Optional[str]):
    """Transcribe a local audio file."""
    try:
        file_path_obj = pathlib.Path(file_path)
        console.print(f"[blue]Transcribing {file_path} with {model} model...[/blue]")
        from podcast_transcription_core.transcription import ParakeetTranscriber

        transcriber = ParakeetTranscriber(model=model)
        transcription = transcriber.transcribe(file_path_obj)

        if output:
            output_file = pathlib.Path(output)
        else:
            output_file = file_path_obj.with_suffix(".txt")

        output_file.write_text(transcription)
        console.print(f"[green]Transcription saved to: {output_file}[/green]")

    except Exception as e:
        console.print(f"[red]Error transcribing file: {e}[/red]")
        sys.exit(1)


@cli.command()
@click.argument("files", nargs=-1, type=click.Path())
@click.option(
    "--dir",
    "directory",
    default="transcripts",
    type=click.Path(),
    help="Directory to ingest",
)
@click.option("--reindex", is_flag=True, help="Recreate tables")
def ingest(files: typing.Tuple[str, ...], directory: str, reindex: bool):
    """Ingest transcript files."""
    try:
        import frontmatter

        # Gather files
        files_to_process = []
        if files:
            files_to_process.extend([pathlib.Path(f) for f in files])
        else:
            directory_path = pathlib.Path(directory)
            if directory_path.exists():
                files_to_process.extend(directory_path.glob("*.md"))

        if not files_to_process:
            console.print("[yellow]No files found to ingest[/yellow]")
            sys.exit(0)

        console.print("[blue]Initializing PostgreSQL database...[/blue]")
        from podcast_transcription_core.database.postgres import VectorDatabase

        pg_db = VectorDatabase(recreate_tables=reindex)

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

                    if not pg_db.process_frontmatter_post(post):
                        file_success = False
                        console.print(
                            f"[red]Failed to ingest {file_path.name} to PostgreSQL[/red]"
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
        sys.exit(1)


@cli.command()
@click.option("--limit", "-l", default=20, help="Maximum episodes to show")
def list(limit: int):
    """List episodes."""
    try:
        from podcast_transcription_core.database.postgres import VectorDatabase
        from podcast_transcription_core.models import Transcript

        db = VectorDatabase()
        session = db.Session()

        transcripts = (
            session.query(Transcript)
            .filter(Transcript.podcast == 1)
            .order_by(
                Transcript.published_date.desc().nulls_last(),
                Transcript.episode_number.desc(),
            )
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
        sys.exit(1)


@cli.command()
@click.argument("episodes", nargs=-1, required=True)
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation prompt")
def delete(episodes: typing.Tuple[str, ...], yes: bool):
    """Delete transcripts for episodes.

    EPISODES can be: single number (123), range (100-105), comma-separated (1,3,5),
    'latest', or 'all'.
    """
    try:
        from podcast_transcription_core.database.postgres import VectorDatabase
        from podcast_transcription_core.models import Transcript

        episode_list = _parse_episodes(episodes)

        if not episode_list:
            console.print("[yellow]No episodes specified[/yellow]")
            sys.exit(0)

        if not yes:
            console.print(
                f"[yellow]This will delete transcripts for {len(episode_list)} episode(s):[/yellow]"
            )
            console.print(", ".join(map(str, episode_list)))
            if not click.confirm("Continue?"):
                console.print("[red]Cancelled[/red]")
                sys.exit(0)

        db = VectorDatabase()
        session = db.Session()

        deleted_count = 0
        not_found_count = 0

        for episode_number in episode_list:
            try:
                transcript = (
                    session.query(Transcript)
                    .filter(
                        Transcript.episode_number == episode_number,
                        Transcript.podcast == 1,
                    )
                    .first()
                )

                if transcript:
                    session.delete(transcript)
                    session.commit()
                    deleted_count += 1
                    console.print(f"[green]✓ Deleted episode {episode_number}[/green]")
                else:
                    not_found_count += 1
                    console.print(
                        f"[yellow]✗ Episode {episode_number} not found[/yellow]"
                    )

            except Exception as e:
                session.rollback()
                console.print(
                    f"[red]Error deleting episode {episode_number}: {e}[/red]"
                )

        session.close()

        console.print(f"\n[bold]Deleted {deleted_count} transcript(s)[/bold]")
        if not_found_count > 0:
            console.print(f"[yellow]{not_found_count} episode(s) not found[/yellow]")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    cli()
