"""Use Whisper to transcribe audio files to text."""

import pathlib
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
from transcriber import HybridTranscriber
from url_finder import fetch_latest_episode_number, get_audio_url_from_episode_number

app = typer.Typer()
transcriber = HybridTranscriber(model="base", prefer_mlx=True)
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

    with tempfile.NamedTemporaryFile(mode="+wb", suffix=".mp3", delete=False) as f:
        typer.echo(f"Downloading audio file from {url}")

        with httpx.stream("GET", url, follow_redirects=True) as response:
            typer.echo(f"Saving audio file to {f.name}")
            for chunk in response.iter_bytes():
                f.write(chunk)

        return f.name


def transcribe_audio_file(audio_file: pathlib.Path) -> str:
    """Transcribe an audio file to text using MLX or Whisper"""

    return transcriber.transcribe(audio_file)


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

    return output_file.write_text(transcription)


def transcribe_from_audio_url(audio_url: str) -> int:
    typer.echo(f"Transcribing audio from {audio_url}")
    audio_file = download_audio_file(audio_url)
    return transcribe_audio_file(audio_file)


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
        transcription = transcribe_from_audio_url(audio_url)
        post = frontmatter.Post(
            "\n".join(splitter.split_text(transcription)), **metadata
        )
        output_file = pathlib.Path(
            f"transcripts/{slugify.slugify(metadata['title'])}.md"
        )
        output_file.write_text(frontmatter.dumps(post))


if __name__ == "__main__":
    app()
