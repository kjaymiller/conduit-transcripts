import frontmatter
import json
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
from bs4 import BeautifulSoup

load_dotenv()

INDEX_NAME = os.getenv("INDEX_NAME")
INDEX_NAME_WITH_TIMESTAMPS = os.getenv("INDEX_NAME_WITH_TIMESTAMPS", f"{INDEX_NAME}_timestamps" if INDEX_NAME else "transcripts_timestamps")
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


def parse_youtube_url(description: str) -> typing.Optional[str]:
    """Extract YouTube URL from HTML description field.
    
    Looks for patterns like youtube.com/watch?v=VIDEO_ID or youtu.be/VIDEO_ID
    Returns the full URL or None if not found.
    """
    if not description:
        return None
    
    # Parse HTML description
    soup = BeautifulSoup(description, 'html.parser')
    
    # Look for YouTube links in anchor tags
    for link in soup.find_all('a', href=True):
        href = link.get('href', '')
        if 'youtube.com/watch' in href or 'youtu.be/' in href:
            # Extract the URL, handling both full URLs and relative paths
            if href.startswith('http'):
                return href
            elif href.startswith('//'):
                return 'https:' + href
            elif href.startswith('/'):
                return 'https://www.youtube.com' + href
    
    # Also check for YouTube URLs in plain text
    youtube_pattern = r'(https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[\w-]+)'
    matches = re.findall(youtube_pattern, description)
    if matches:
        return matches[0]
    
    return None


def extract_youtube_video_id(youtube_url: str) -> typing.Optional[str]:
    """Extract video ID from YouTube URL.
    
    Handles both formats:
    - youtube.com/watch?v=VIDEO_ID
    - youtu.be/VIDEO_ID
    
    Returns just the video ID or None if not found.
    """
    if not youtube_url:
        return None
    
    # Pattern for youtube.com/watch?v=VIDEO_ID
    match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]+)', youtube_url)
    if match:
        return match.group(1)
    
    return None


def map_chunk_to_segment_timestamp(chunk_text: str, whisper_segments: typing.List[dict]) -> typing.Optional[float]:
    """Map a chunk to its corresponding Whisper segment and return the start timestamp.
    
    Args:
        chunk_text: The text content of the chunk
        whisper_segments: List of Whisper segments, each with 'start', 'end', and 'text' keys
    
    Returns:
        The start timestamp (in seconds) of the first matching segment, or None if no match
    """
    if not whisper_segments or not chunk_text:
        return None
    
    # Normalize text for comparison (lowercase, strip whitespace)
    chunk_text_normalized = chunk_text.lower().strip()
    
    # Try to find segment that contains the chunk text
    for segment in whisper_segments:
        segment_text = segment.get('text', '').lower().strip()
        if not segment_text:
            continue
        
        # Check if chunk text is contained in segment text or vice versa
        # We use a threshold to handle partial matches
        if chunk_text_normalized in segment_text or segment_text in chunk_text_normalized:
            return segment.get('start')
        
        # Also check for significant overlap (at least 50% of shorter string)
        shorter_len = min(len(chunk_text_normalized), len(segment_text))
        if shorter_len > 0:
            # Simple overlap check: count common words
            chunk_words = set(chunk_text_normalized.split())
            segment_words = set(segment_text.split())
            if chunk_words and segment_words:
                overlap_ratio = len(chunk_words & segment_words) / min(len(chunk_words), len(segment_words))
                if overlap_ratio > 0.5:
                    return segment.get('start')
    
    # If no exact match, try to find the segment that starts closest to where the chunk would be
    # This is a fallback for chunks that don't match exactly
    # We'll use the first segment as a last resort (not ideal, but better than None)
    if whisper_segments:
        return whisper_segments[0].get('start')
    
    return None


def os_load_data_from_file(file: pathlib.Path, use_timestamps: bool = False):
    """Chunk data, create embeddings, and index in OpenSearch.
    
    Args:
        file: Path to the transcript file
        use_timestamps: If True, extract YouTube URLs and map chunks to Whisper segments for timestamps
    """
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
    
    # Extract YouTube URL and video ID if using timestamps
    whisper_segments = None
    if use_timestamps:
        description = frontmatter_post.get("description", "")
        youtube_url = parse_youtube_url(description)
        youtube_video_id = extract_youtube_video_id(youtube_url) if youtube_url else None
        
        base_data["youtube_url"] = youtube_url
        base_data["youtube_video_id"] = youtube_video_id
        
        # Load Whisper segments from frontmatter
        whisper_segments_str = frontmatter_post.get("whisper_segments")
        if whisper_segments_str:
            try:
                whisper_segments = json.loads(whisper_segments_str)
            except (json.JSONDecodeError, TypeError):
                whisper_segments = None

    post_chunks = splitter.create_documents([frontmatter_post.content])
    
    # Determine which index to use
    target_index = INDEX_NAME_WITH_TIMESTAMPS if use_timestamps else INDEX_NAME
    
    for chunk_index, post_chunk in enumerate(post_chunks):
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
        
        # Add timestamp fields if using timestamps
        if use_timestamps:
            doc["chunk_index"] = chunk_index
            # Map chunk to Whisper segment to get timestamp
            timestamp = map_chunk_to_segment_timestamp(post_chunk.page_content, whisper_segments) if whisper_segments else None
            doc["timestamp"] = int(timestamp) if timestamp is not None else None
        
        docs.append(doc)
    
    response = helpers.bulk(client, docs, index=target_index)
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
    with_timestamps: typing_extensions.Annotated[
        bool,
        typer.Option("--with-timestamps", help="Use timestamp-enabled index and extract YouTube URLs/timestamps"),
    ] = False,
):
    """
    Ingest transcript files into OpenSearch.
    
    Can process a specific episode, all episodes in a show, or all episodes.
    Use --with-timestamps to ingest into the timestamp-enabled index and read from transcripts_with_timestamps/ folder.
    """
    # Use different folder based on with_timestamps flag
    transcripts_dir = pathlib.Path("transcripts_with_timestamps" if with_timestamps else "transcripts")
    
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
        index_type = "timestamp-enabled" if with_timestamps else "standard"
        typer.echo(f"Using {index_type} index")
        for file in files:
            typer.echo(f"Processing: {file}")
            try:
                os_load_data_from_file(file, use_timestamps=with_timestamps)
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
        index_type = "timestamp-enabled" if with_timestamps else "standard"
        typer.echo(f"Using {index_type} index")
        try:
            os_load_data_from_file(file_path, use_timestamps=with_timestamps)
            typer.echo(f"✓ Successfully ingested {file_path.name}")
        except Exception as e:
            typer.echo(f"✗ Error processing {file_path.name}: {e}", err=True)
            raise typer.Exit(1)
    
    else:
        typer.echo("Error: Must specify either --episode or --all", err=True)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
