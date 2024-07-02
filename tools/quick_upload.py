import pathlib
from typing import Annotated

import typer

from os_ingest import os_load_data_from_file
from pg_ingest import pg_load_from_file


def load_data_from_file(
        file: Annotated[
            pathlib.Path, 
            typer.Argument(
                ...,
                help="The file to load.",
                file_okay=True,
                dir_okay=False,
                exists=True,
                readable=True,
                resolve_path=True,
                )]):
    """Load data from a file into OpenSearch and PostgreSQL."""

    if file.parent.name != "transcripts":
        raise ValueError("File must be in the transcripts directory.")
    
    os_load_data_from_file(file)
    pg_load_from_file(file)
    

if __name__ == "__main__":
    typer.run(load_data_from_file)