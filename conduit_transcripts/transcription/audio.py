"""Audio download utilities."""

import pathlib
import tempfile

import httpx


def download_audio_file(url: str) -> pathlib.Path:
    """Download an audio file from a URL to a temporary file."""
    with tempfile.NamedTemporaryFile(mode="+wb", suffix=".mp3", delete=False) as f:
        print(f"Downloading audio file from {url}")

        with httpx.stream("GET", url, follow_redirects=True) as response:
            print(f"Saving audio file to {f.name}")
            for chunk in response.iter_bytes():
                f.write(chunk)

        return pathlib.Path(f.name)
