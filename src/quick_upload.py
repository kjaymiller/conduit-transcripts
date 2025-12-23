import pathlib
from typing import Annotated, List, Optional

import arrow
import frontmatter
import typer

from conduit_transcripts.database.opensearch import OpenSearchDatabase
from conduit_transcripts.database.postgres import VectorDatabase

ARROW_FMT = r"MMMM[\s+]D[\w+,\s+]YYYY"

app = typer.Typer()


@app.command("files")
def load_data_from_file(
    target_dir: Annotated[
        pathlib.Path, typer.Option("--dir", dir_okay=True, file_okay=False)
    ] = pathlib.Path("transcripts"),
    files: Optional[
        List[
            Annotated[
                pathlib.Path,
                typer.Option(
                    "--file",
                    help="The file to load.",
                    file_okay=True,
                    dir_okay=False,
                    exists=True,
                    readable=True,
                    resolve_path=True,
                ),
            ]
        ]
    ] = None,
    reindex: bool = False,
    os_only: bool = False,
    pg_only: bool = False,
):
    """Load data from a file into OpenSearch and PostgreSQL."""
    pg_db = None
    os_db = None

    if not os_only:
        pg_db = VectorDatabase(recreate_tables=reindex and not os_only)

    if not pg_only:
        try:
            os_db = OpenSearchDatabase()
            if reindex:
                os_db.create_index()
        except ImportError:
            typer.echo("OpenSearch support not available. Skipping OpenSearch indexing.", err=True)
            if not pg_db:
                typer.echo("No databases available to write to. Exiting.", err=True)
                raise typer.Exit(code=1)

    if not files:
        files = list(target_dir.iterdir())

    for file in files:
        if file.parent.name != target_dir.name and file.parent.name != "transcripts":
             # loose check, relying on file existence
             pass

        # Load frontmatter
        try:
            post = frontmatter.load(str(file))
        except Exception as e:
            typer.echo(f"Error loading {file}: {e}", err=True)
            continue

        if not pg_only and os_db:
            typer.echo(f"Indexing {file.name} to OpenSearch...")
            os_db.process_frontmatter_post(post)

        if not os_only and pg_db:
            typer.echo(f"Indexing {file.name} to PostgreSQL...")
            pg_db.process_frontmatter_post(post)


if __name__ == "__main__":
    app()
