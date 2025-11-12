"""
RSS feed parser for podcast episode metadata.

This module uses feedparser to extract episode information from the Conduit
podcast RSS feed, eliminating the need for web scraping and making the
codebase more resilient to website layout changes.
"""

import typer
import feedparser
from datetime import datetime

# Conduit podcast RSS feed URL
CONDUIT_RSS_FEED = "https://www.relay.fm/conduit/feed"


def fetch_episodes(feed_url: str = CONDUIT_RSS_FEED) -> list[dict]:
    """
    Fetch all episodes from a podcast RSS feed.

    Args:
        feed_url: URL of the RSS feed (defaults to Conduit feed)

    Returns:
        List of episode dictionaries with metadata
    """
    typer.echo(f"Fetching episodes from {feed_url}")
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        raise ValueError("No episodes found in feed")

    episodes = []
    for entry in feed.entries:
        episode = _parse_episode_entry(entry)
        episodes.append(episode)

    typer.echo(f"Found {len(episodes)} episodes")
    return episodes


def fetch_episode_by_number(
    episode_number: int, feed_url: str = CONDUIT_RSS_FEED
) -> dict | None:
    """
    Fetch a specific episode by episode number.

    Args:
        episode_number: The episode number to fetch
        feed_url: URL of the RSS feed (defaults to Conduit feed)

    Returns:
        Episode dictionary with metadata, or None if not found
    """
    typer.echo(f"Fetching episode {episode_number} from {feed_url}")
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        episode = _parse_episode_entry(entry)
        if episode["episode_number"] == episode_number:
            typer.echo(f"Found episode {episode_number}")
            return episode

    typer.echo(f"Episode {episode_number} not found", err=True)
    return None


def fetch_latest_episode(feed_url: str = CONDUIT_RSS_FEED) -> dict:
    """
    Fetch the latest episode from the feed.

    Args:
        feed_url: URL of the RSS feed (defaults to Conduit feed)

    Returns:
        Latest episode dictionary with metadata
    """
    typer.echo(f"Fetching latest episode from {feed_url}")
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        raise ValueError("No episodes found in feed")

    # First entry is the latest
    latest_entry = feed.entries[0]
    episode = _parse_episode_entry(latest_entry)

    typer.echo(f"Latest episode: {episode['episode_number']}")
    return episode


def fetch_latest_episode_number(feed_url: str = CONDUIT_RSS_FEED) -> int:
    """
    Get the latest episode number.

    Args:
        feed_url: URL of the RSS feed (defaults to Conduit feed)

    Returns:
        Latest episode number
    """
    episode = fetch_latest_episode(feed_url)
    return episode["episode_number"]


def _parse_episode_entry(entry: dict) -> dict:
    """
    Parse a single RSS feed entry into our episode format.

    Args:
        entry: A feedparser entry dictionary

    Returns:
        Dictionary with episode metadata
    """
    # Extract episode number from title (e.g., "114: Title" -> 114)
    title = entry.get("title", "")
    episode_number_str = title.split(":")[0].strip()
    try:
        episode_number = int(episode_number_str)
    except ValueError:
        episode_number = 0

    # Get audio URL from enclosure
    audio_url = None
    if "enclosures" in entry and entry.enclosures:
        audio_url = entry.enclosures[0].href

    # Parse publication date
    pub_date = None
    if "published_parsed" in entry and entry.published_parsed:
        pub_date = datetime(*entry.published_parsed[:6]).strftime("%B %d, %Y")

    # Get description/summary
    description = entry.get("summary", entry.get("subtitle", ""))

    # Get episode URL
    episode_url = entry.get("link", "")

    episode = {
        "episode_number": episode_number,
        "title": title,
        "description": description,
        "pub_date": pub_date,
        "url": episode_url,
        "audio_url": audio_url,
    }

    return episode
