"""Text processing utilities."""

import re
from typing import List


def extract_episode_number(title: str) -> str:
    """Extract episode number from title."""
    match = re.match(r"^\d+", title)
    if match:
        return match.group()
    raise ValueError(f"Could not extract episode number from title: {title}")


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 20) -> List[str]:
    """Simple text chunking utility."""
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        if end >= len(text):
            chunks.append(text[start:])
            break

        # Try to break at sentence boundary
        for sep in [".", "!", "?", "\n"]:
            last_sep = text.rfind(sep, start, end)
            if last_sep != -1:
                end = last_sep + 1
                break

        chunks.append(text[start:end].strip())
        start = end - overlap if end > overlap else 0

    return [chunk for chunk in chunks if chunk]
