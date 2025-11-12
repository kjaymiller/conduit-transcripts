import typer
import tempfile
import httpx


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
