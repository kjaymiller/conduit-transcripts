"""Audio download utilities."""

import logging
import pathlib
import tempfile

import httpx

logger = logging.getLogger(__name__)


def download_audio_file(url: str) -> pathlib.Path:
    """Download an audio file from a URL to a temporary file.

    Args:
        url: The URL of the audio file to download.

    Returns:
        Path to the temporary file containing the downloaded audio.
    """
    with tempfile.NamedTemporaryFile(mode="+wb", suffix=".mp3", delete=False) as f:
        logger.info(f"Downloading audio file from {url}")

        with httpx.stream("GET", url, follow_redirects=True) as response:
            logger.info(f"Saving audio file to {f.name}")
            for chunk in response.iter_bytes():
                f.write(chunk)

        return pathlib.Path(f.name)


def download_audio_to_path(url: str, path: pathlib.Path) -> pathlib.Path:
    """Download an audio file from a URL to a specific path.

    Args:
        url: The URL of the audio file to download.
        path: The path to save the audio file to.

    Returns:
        The path to the saved file.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    logger.info(f"Downloading audio file from {url} to {path}")

    with httpx.stream("GET", url, follow_redirects=True) as response:
        with path.open("wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)

    return path
