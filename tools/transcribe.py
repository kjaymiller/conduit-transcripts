"""Use Whisper to transcribe audio files to text."""

import pathlib
import typer
import tempfile

import slugify
import frontmatter
import httpx
import whisper
from langchain_text_splitters import RecursiveCharacterTextSplitter

from url_finder import get_audio_url_from_episode_number

app = typer.Typer()

model = whisper.load_model("base")    


splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=20,
    separators=[".", "!", "?", "\n"],
)


def check_first_character(segment: str) -> bool:
    """Check if a segment needs to have the first character removed"""
    return segment[0] in (".", "!", "?")


def split_text(text: str) -> list[str]:
    """
    Split a block of text into paragraphs.
    
    Text is written in a single string and split using the RecursiveCharacterTextSplitter.

    This corrects for text leading with punctuation will grab the punctuation from the next segment.
    """
    text_segments = splitter.split_text(text)
    new_text_segments = []
    
    for i, segment in enumerate(text_segments):
        if check_first_character(segment):
            modified_new_text_segment = segment[1:].lstrip()
        else:
            modified_new_text_segment = segment

        if segment != text_segments[-1]:
            if check_first_character(text_segments[i+1]):
                modified_new_text_segment += text_segments[i + 1][1:]
        
        new_text_segments.append(modified_new_text_segment)

    return new_text_segments

def download_audio_file(url: str) -> str:
    """
    Stream Download an audio file from a URL.
    
    Save the audio file to a temporary file.

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
    """Transcribe an audio file to text"""

    transcription = model.transcribe(audio=audio_file, verbose=False)
    return "\n".join(split_text(transcription["text"]))


def transcribe_from_audio_url(audio_url: str) -> int:
    typer.echo(f"Transcribing audio from {audio_url}")
    audio_file = download_audio_file(audio_url)
    return transcribe_audio_file(audio_file)


def transcribe_from_episode_number(episode_number: int):
    """
    Transcribe an episode from an episode number

    Metadata is pulled from the webpage contents.

    Audio is downloaded from the extracted audio_url.
    """
    metadata, audio_url = get_audio_url_from_episode_number(episode_number)
    transcription = transcribe_from_audio_url(audio_url)
    post = frontmatter.Post(transcription, **metadata)
    output_file = pathlib.Path(f"transcripts/{slugify.slugify(metadata['title'])}.md")
    output_file.write_text(frontmatter.dumps(post))



if __name__ == "__main__":
    typer.run(transcribe_from_episode_number)