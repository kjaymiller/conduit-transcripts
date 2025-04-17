import pathlib
import re

from typing import Annotated, List, Optional

import arrow
import frontmatter
import typer

from os_ingest import os_load_data_from_file
from os_index import create_index
from pg_ingest import pg_load_data_from_file, drop_table


ARROW_FMT = r"MMMM[\s+]D[\w+,\s+]YYYY"


def process_frontmatter(file: pathlib.Path)
    frontmatter_post = frontmatter.loads(
        file.read_text()
    )  # loads the metadata from the file
    return {
        "title": frontmatter_post["title"],
        "episode_number": int(re.match(r"^\d+", frontmatter_post["title"]).group()),
        "show": "Conduit",
        "description": frontmatter_post["description"],
        "url": frontmatter_post["url"],
        "pub_date": arrow.get(frontmatter_post["pub_date"], ARROW_FMT).date().isoformat(),
        "content": frontmatter_post.content
    }


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
    if not os_only:
        _CONNECTION_STRING = os.getenv("AIVEN_POSTGRES_SERVICE_URI")
        conn = psycopg.connect(_CONNECTION_STRING)

        if not reindex:
            drop_table()

    if reindex and not pg_only:
        create_index()

    if not files:
        files = target_dir.iterdir()

    for file in files:
        if file.parent.name != target_dir.name:
            raise ValueError("File must be in the transcripts directory.")

        post = process_frontmatter(file)

        if not pg_only:
            os_load_data_from_file(post)

        if not os_only:
            pg_load_data_from_file(post)


if __name__ == "__main__":
    typer.run(load_data_from_file)
