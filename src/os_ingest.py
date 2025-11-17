import frontmatter
import os
import pathlib
import re
import typing
import uuid
import typing_extensions

import arrow
import slugify
import typer
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from opensearchpy import OpenSearch, helpers

load_dotenv()

INDEX_NAME = os.getenv("INDEX_NAME")
CONNECTION_STRING = os.getenv("OPENSEARCH_SERVICE_URI")
client = OpenSearch(CONNECTION_STRING, use_ssl=True, timeout=100)

fmt = r"MMMM[\s+]D[\w+,\s+]YYYY"

# define splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=20,
    separators=[".", "!", "?", "\n"],
)

# define embeddings. These options are all the defaults and not explicitly needed.
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False},
)


def os_load_data_from_file(file: pathlib.Path):
    """Chunk data, create embeddings, and index in OpenSearch."""
    docs = []

    # Load frontmatter and extract metadata
    frontmatter_post = frontmatter.loads(file.read_text())
    
    # Extract episode_number from title (e.g., "1 - Title" -> 1)
    episode_number_match = re.match(r"^\d+", frontmatter_post["title"])
    episode_number = int(episode_number_match.group()) if episode_number_match else None
    
    # Parse pub_date - try multiple formats
    pub_date_str = frontmatter_post["pub_date"]
    pub_date = None
    
    # Try the defined format first
    try:
        pub_date = arrow.get(pub_date_str, fmt).date().isoformat()
    except (arrow.parser.ParserError, arrow.parser.ParserMatchError, ValueError):
        # Try RFC 2822 format (e.g., "Fri, 07 Nov 2025 05:58:00 GMT")
        try:
            pub_date = arrow.get(pub_date_str, "ddd, DD MMM YYYY HH:mm:ss ZZZ").date().isoformat()
        except (arrow.parser.ParserError, arrow.parser.ParserMatchError, ValueError):
            # Try RFC 2822 without timezone
            try:
                pub_date = arrow.get(pub_date_str, "ddd, DD MMM YYYY HH:mm:ss").date().isoformat()
            except (arrow.parser.ParserError, arrow.parser.ParserMatchError, ValueError):
                # Last resort: try to parse with dateutil (more flexible)
                from dateutil import parser as dateutil_parser
                pub_date = dateutil_parser.parse(pub_date_str).date().isoformat()
    
    if pub_date is None:
        raise ValueError(f"Could not parse pub_date: {pub_date_str}")
    
    # Build base_data with metadata fields
    base_data = {
        "title": frontmatter_post["title"],
        "episode_number": episode_number,
        "description": frontmatter_post.get("description", ""),
        "url": frontmatter_post.get("url", ""),
        "image_url": frontmatter_post.get("image_url", ""),
        "pub_date": pub_date,
    }

    post_chunks = splitter.create_documents([frontmatter_post.content])
    for post_chunk in post_chunks:
        doc = {
            **base_data,
            **{
                "_id": str(uuid.uuid4()),
                "content": post_chunk.page_content,
                "content_vector": embeddings.embed_documents([post_chunk.page_content])[
                    0
                ],
            },
        }
        docs.append(doc)
    response = helpers.bulk(client, docs, index=INDEX_NAME)
    return response


app = typer.Typer()


@app.command()
def ingest(
    episode: typing_extensions.Annotated[
        typing.Optional[str],
        typer.Option("--episode", "-e", help="Episode name (slugified filename without .md extension)"),
    ] = None,
    show: typing_extensions.Annotated[
        typing.Optional[str],
        typer.Option("--show", "-s", help="Show name (subdirectory in transcripts/ folder)"),
    ] = None,
    all: typing_extensions.Annotated[
        bool,
        typer.Option("--all", "-a", help="Process all transcript files"),
    ] = False,
):
    """
    Ingest transcript files into OpenSearch.
    
    Can process a specific episode, all episodes in a show, or all episodes.
    """
    transcripts_dir = pathlib.Path("transcripts")
    
    if all:
        # Process all files in transcripts directory (including subdirectories)
        if show:
            # Process all files in the show subdirectory
            show_dir = transcripts_dir / slugify.slugify(show)
            if not show_dir.exists():
                typer.echo(f"Show directory not found: {show_dir}", err=True)
                raise typer.Exit(1)
            files = list(show_dir.glob("*.md"))
        else:
            # Process all files in transcripts and all subdirectories
            files = list(transcripts_dir.rglob("*.md"))
        
        if not files:
            typer.echo("No transcript files found", err=True)
            raise typer.Exit(1)
        
        typer.echo(f"Processing {len(files)} transcript file(s)...")
        for file in files:
            typer.echo(f"Processing: {file}")
            try:
                os_load_data_from_file(file)
                typer.echo(f"✓ Successfully ingested {file.name}")
            except Exception as e:
                typer.echo(f"✗ Error processing {file.name}: {e}", err=True)
    
    elif episode:
        # Process a specific episode
        if show:
            # Look in the show subdirectory
            file_path = transcripts_dir / slugify.slugify(show) / f"{slugify.slugify(episode)}.md"
        else:
            # Look in transcripts root or try to find it recursively
            file_path = transcripts_dir / f"{slugify.slugify(episode)}.md"
            if not file_path.exists():
                # Try to find it in subdirectories
                found_files = list(transcripts_dir.rglob(f"{slugify.slugify(episode)}.md"))
                if found_files:
                    file_path = found_files[0]
        
        if not file_path.exists():
            typer.echo(f"Episode file not found: {file_path}", err=True)
            raise typer.Exit(1)
        
        typer.echo(f"Processing: {file_path}")
        try:
            os_load_data_from_file(file_path)
            typer.echo(f"✓ Successfully ingested {file_path.name}")
        except Exception as e:
            typer.echo(f"✗ Error processing {file_path.name}: {e}", err=True)
            raise typer.Exit(1)
    
    else:
        typer.echo("Error: Must specify either --episode or --all", err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
