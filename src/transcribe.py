"""Use Whisper to transcribe audio files to text."""

from os import name
import json
import pathlib
import re
import tempfile
import typing
import typing_extensions

import frontmatter
import httpx
import slugify
import typer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich.progress import track
from rich.prompt import Confirm
from url_finder import fetch_latest_episode_number, get_audio_url_from_episode_number
from rss_parser import (
    parse_rss_feed,
    get_episode_by_number,
    get_latest_episode,
    get_audio_url_from_rss_episode,
)

# Lazy import and loading of Whisper model
_whisper_model = None
_whisper_module = None


def _get_whisper_model():
    """Lazily load the Whisper model only when needed."""
    global _whisper_model, _whisper_module
    
    if _whisper_model is not None:
        return _whisper_model
    
    try:
        import whisper
        _whisper_module = whisper
    except ImportError:
        typer.echo(
            "Error: Whisper not found. Please install it with: pip install openai-whisper",
            err=True,
        )
        raise typer.Exit(1)
    
    try:
        _whisper_model = whisper.load_model("base")
        return _whisper_model
    except AttributeError as e:
        typer.echo(
            f"Error: Whisper module doesn't have expected API. "
            f"Please ensure you have 'openai-whisper' installed: pip install openai-whisper",
            err=True,
        )
        typer.echo(f"Details: {e}", err=True)
        raise typer.Exit(1)


app = typer.Typer()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    separators=[".", "!", "?", "\n"],
    keep_separator="end",
    chunk_overlap=0,
)


def download_audio_file(url: str) -> str:
    """
    Stream Download an audio file from a URL. Save the audio file to a temporary file.

    Args:
        url: The URL of the audio file.

    Returns:
        The path to the downloaded audio file.
    """
    # Use browser-like headers to avoid getting ad-injected versions
    # Some CDNs (like RSS.com) serve different content based on User-Agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "audio/mpeg, audio/*, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://rss.com/",
    }

    with tempfile.NamedTemporaryFile(mode="+wb", suffix=".mp3", delete=False) as f:
        typer.echo(f"Downloading audio file from {url}")

        with httpx.stream("GET", url, headers=headers, follow_redirects=True) as response:
            # Log the final URL after redirects for debugging
            final_url = str(response.url)
            if final_url != url:
                typer.echo(f"Redirected to: {final_url}")
            
            typer.echo(f"Saving audio file to {f.name}")
            for chunk in response.iter_bytes():
                f.write(chunk)

        return f.name


def transcribe_audio_file(audio_file: pathlib.Path) -> dict:
    """Transcribe an audio file and return full Whisper result with text and segments"""
    model = _get_whisper_model()
    # _whisper_module is guaranteed to be set if _get_whisper_model() succeeded
    whisper = _whisper_module
    
    audio = whisper.load_audio(str(audio_file))
    transcription = model.transcribe(audio=audio, verbose=False)

    return transcription


def transcribe_audio_file_text_only(audio_file: pathlib.Path) -> str:
    """Transcribe an audio file to text (backward compatibility)"""
    transcription = transcribe_audio_file(audio_file)
    return transcription["text"]


@app.command(name="file")
def transcribe_file(
    input_file: typing_extensions.Annotated[
        pathlib.Path,
        typer.Argument(exists=True, file_okay=True, dir_okay=False),
    ],
    output_file: typing_extensions.Annotated[
        typing.Optional[pathlib.Path],
        typer.Option("--output", exists=True, file_okay=True, dir_okay=False),
    ] = None,
):

    transcription = transcribe_audio_file(audio_file=input_file)
    if not output_file:
        output_file = input_file.absolute().with_suffix(".txt")

    return output_file.write_text(transcription["text"])


def transcribe_from_audio_url(audio_url: str) -> dict:
    """Transcribe audio from URL and return full Whisper result with text and segments"""
    typer.echo(f"Transcribing audio from {audio_url}")
    audio_file_path = download_audio_file(audio_url)
    transcription = transcribe_audio_file(pathlib.Path(audio_file_path))
    # Clean up temporary file
    pathlib.Path(audio_file_path).unlink()
    return transcription


def get_output_file_path(metadata: dict, show: typing.Optional[str] = None, with_timestamps: bool = False) -> pathlib.Path:
    """Get the output file path for a transcript based on metadata and show name.
    
    Args:
        metadata: Episode metadata dictionary
        show: Optional show name (subdirectory)
        with_timestamps: If True, save to transcripts_with_timestamps/ folder
    """
    base_dir = "transcripts_with_timestamps" if with_timestamps else "transcripts"
    if show:
        return pathlib.Path(
            f"{base_dir}/{slugify.slugify(show)}/{slugify.slugify(metadata['title'])}.md"
        )
    else:
        return pathlib.Path(
            f"{base_dir}/{slugify.slugify(metadata['title'])}.md"
        )


@app.command(name="ep")
def transcribe_from_episode_number(
    episode_numbers: typing.Optional[typing.List[int]] = None,
    all: typing_extensions.Annotated[
        bool, typer.Option("-a", "--all", help="redownload_all_files")
    ] = False,
    _range: typing_extensions.Annotated[
        typing.Optional[str],
        typer.Option(
            "-r", "--range", help="two numbers separated by a dash ('-'). Example: 1-10"
        ),
    ] = None,
    show: typing_extensions.Annotated[
        typing.Optional[str],
        typer.Option("--show", help="Show name to use as subdirectory in transcripts/ folder"),
    ] = None,
    skip_if_exists: typing_extensions.Annotated[
        bool,
        typer.Option("--skip-if-exists", help="Skip episodes for which transcriptions already exist"),
    ] = False,
    with_timestamps: typing_extensions.Annotated[
        bool,
        typer.Option("--with-timestamps", help="Extract and store Whisper segments with timestamps (slower, saves to transcripts_with_timestamps/)"),
    ] = False,
):
    """
    Transcribe an episode from an episode number

    Metadata is pulled from the webpage contents.

    Audio is downloaded from the extracted audio_url.
    """

    if all:
        if Confirm.ask(
            "This Process will re-download and overwrite all transcriptions. Continue?",
            show_choices=True,
            default=False,
        ):
            episode_numbers = range(1, fetch_latest_episode_number())

    elif _range:
        start, stop = _range.split("-")
        episode_numbers = range(int(start), int(stop) + 1)

    elif not episode_numbers:
        typer.echo("Fetching Latest Episode Number")
        episode_numbers = [fetch_latest_episode_number()]

    for episode_number in track(episode_numbers):
        metadata, audio_url = get_audio_url_from_episode_number(episode_number)
        output_file = get_output_file_path(metadata, show, with_timestamps=with_timestamps)
        
        if skip_if_exists and output_file.exists():
            typer.echo(f"Skipping episode {episode_number}: {output_file} already exists")
            continue
        
        transcription_result = transcribe_from_audio_url(audio_url)
        transcription_text = transcription_result["text"]
        
        # Only extract and store segments if with_timestamps is enabled
        if with_timestamps:
            whisper_segments = transcription_result.get("segments", [])
            metadata["whisper_segments"] = json.dumps(whisper_segments) if whisper_segments else None
        else:
            metadata["whisper_segments"] = None
        
        post = frontmatter.Post(
            "\n".join(splitter.split_text(transcription_text)), **metadata
        )
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(frontmatter.dumps(post))


@app.command(name="rss")
def transcribe_from_rss(
    rss_url: typing_extensions.Annotated[
        str,
        typer.Option("--url", help="RSS feed URL"),
    ] = "https://media.rss.com/vector-podcast/feed.xml",
    episode_numbers: typing.Optional[typing.List[int]] = None,
    latest: typing_extensions.Annotated[
        bool, typer.Option("-l", "--latest", help="Transcribe latest episode only")
    ] = False,
    all: typing_extensions.Annotated[
        bool, typer.Option("-a", "--all", help="Transcribe all episodes")
    ] = False,
    _range: typing_extensions.Annotated[
        typing.Optional[str],
        typer.Option(
            "-r", "--range", help="two numbers separated by a dash ('-'). Example: 1-10"
        ),
    ] = None,
    show: typing_extensions.Annotated[
        typing.Optional[str],
        typer.Option("--show", help="Show name to use as subdirectory in transcripts/ folder"),
    ] = None,
    skip_if_exists: typing_extensions.Annotated[
        bool,
        typer.Option("--skip-if-exists", help="Skip episodes for which transcriptions already exist"),
    ] = False,
    with_timestamps: typing_extensions.Annotated[
        bool,
        typer.Option("--with-timestamps", help="Extract and store Whisper segments with timestamps (slower, saves to transcripts_with_timestamps/)"),
    ] = False,
):
    """
    Transcribe episodes from an RSS feed (e.g., Vector Podcast)
    
    Metadata is pulled from the RSS feed.
    Audio is downloaded from the enclosure URL in the feed.
    """
    # Auto-detect show name from RSS URL if not provided
    if show is None:
        # Try to extract show name from URL pattern like "rss.com/vector-podcast/feed.xml"
        match = re.search(r'/([^/]+)/feed\.xml', rss_url)
        if match:
            show = match.group(1)
        else:
            # Fallback: try to extract from any path segment before feed.xml
            match = re.search(r'/([^/]+)/[^/]*feed', rss_url)
            if match:
                show = match.group(1)
    
    if latest:
        episode = get_latest_episode(rss_url)
        if not episode:
            typer.echo("No episodes found in RSS feed", err=True)
            raise typer.Exit(1)
        
        metadata, audio_url = get_audio_url_from_rss_episode(episode)
        output_file = get_output_file_path(metadata, show, with_timestamps=with_timestamps)
        
        if skip_if_exists and output_file.exists():
            typer.echo(f"Skipping latest episode: {output_file} already exists")
            return
        
        transcription_result = transcribe_from_audio_url(audio_url)
        transcription_text = transcription_result["text"]
        
        # Only extract and store segments if with_timestamps is enabled
        if with_timestamps:
            whisper_segments = transcription_result.get("segments", [])
            metadata["whisper_segments"] = json.dumps(whisper_segments) if whisper_segments else None
        else:
            metadata["whisper_segments"] = None
        
        post = frontmatter.Post(
            "\n".join(splitter.split_text(transcription_text)), **metadata
        )
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(frontmatter.dumps(post))
        return
    
    if all:
        if Confirm.ask(
            "This Process will download and transcribe all episodes. Continue?",
            show_choices=True,
            default=False,
        ):
            episodes = parse_rss_feed(rss_url)
            for episode in track(episodes):
                metadata, audio_url = get_audio_url_from_rss_episode(episode)
                output_file = get_output_file_path(metadata, show, with_timestamps=with_timestamps)
                
                if skip_if_exists and output_file.exists():
                    typer.echo(f"Skipping episode: {output_file} already exists")
                    continue
                
                transcription_result = transcribe_from_audio_url(audio_url)
                transcription_text = transcription_result["text"]
                
                # Only extract and store segments if with_timestamps is enabled
                if with_timestamps:
                    whisper_segments = transcription_result.get("segments", [])
                    metadata["whisper_segments"] = json.dumps(whisper_segments) if whisper_segments else None
                else:
                    metadata["whisper_segments"] = None
                
                post = frontmatter.Post(
                    "\n".join(splitter.split_text(transcription_text)), **metadata
                )
                output_file.parent.mkdir(parents=True, exist_ok=True)
                output_file.write_text(frontmatter.dumps(post))
            return
    
    if _range:
        start, stop = _range.split("-")
        episode_numbers = list(range(int(start), int(stop) + 1))
    
    if not episode_numbers:
        # Default to latest episode
        episode = get_latest_episode(rss_url)
        if not episode:
            typer.echo("No episodes found in RSS feed", err=True)
            raise typer.Exit(1)
        episodes_to_process = [episode]
    else:
        episodes_to_process = []
        for ep_num in episode_numbers:
            episode = get_episode_by_number(rss_url, ep_num)
            if episode:
                episodes_to_process.append(episode)
            else:
                typer.echo(f"Episode {ep_num} not found in RSS feed", err=True)
    
    for episode in track(episodes_to_process):
        metadata, audio_url = get_audio_url_from_rss_episode(episode)
        output_file = get_output_file_path(metadata, show, with_timestamps=with_timestamps)
        
        if skip_if_exists and output_file.exists():
            typer.echo(f"Skipping episode: {output_file} already exists")
            continue
        
        transcription_result = transcribe_from_audio_url(audio_url)
        transcription_text = transcription_result["text"]
        
        # Only extract and store segments if with_timestamps is enabled
        if with_timestamps:
            whisper_segments = transcription_result.get("segments", [])
            metadata["whisper_segments"] = json.dumps(whisper_segments) if whisper_segments else None
        else:
            metadata["whisper_segments"] = None
        
        post = frontmatter.Post(
            "\n".join(splitter.split_text(transcription_text)), **metadata
        )
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(frontmatter.dumps(post))


if __name__ == "__main__":
    app()
