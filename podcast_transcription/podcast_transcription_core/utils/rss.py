"""
RSS feed parser for podcast episode metadata.

This module uses feedparser to extract episode information from the Conduit
podcast RSS feed, eliminating the need for web scraping and making the
codebase more resilient to website layout changes.
"""

import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

import feedparser

# Configure logging
logger = logging.getLogger(__name__)

# Conduit podcast RSS feed URL
CONDUIT_RSS_FEED = "https://www.relay.fm/conduit/feed"


def _parse_episode_entry(entry: Any) -> Dict:
    """
    Parse a single RSS feed entry into our episode format.

    Args:
        entry: A feedparser entry object (dict-like)

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
    # feedparser entries use attribute access or dict access.
    # attributes are safer with getattr for optional fields if using objects,
    # but here entry is likely a struct.
    if hasattr(entry, "enclosures") and entry.enclosures:
        audio_url = entry.enclosures[0].href
    elif "enclosures" in entry and entry["enclosures"]:
        audio_url = entry["enclosures"][0]["href"]

    # Parse publication date
    pub_date = None
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        pub_date = datetime(*entry.published_parsed[:6]).strftime("%B %d, %Y")
    elif "published_parsed" in entry and entry["published_parsed"]:
        pub_date = datetime(*entry["published_parsed"][:6]).strftime("%B %d, %Y")

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


def fetch_episodes(feed_url: str = CONDUIT_RSS_FEED) -> List[Dict]:
    """
    Fetch all episodes from a podcast RSS feed.

    Args:
        feed_url: URL of the RSS feed (defaults to Conduit feed)

    Returns:
        List of episode dictionaries with metadata
    """
    logger.info(f"Fetching episodes from {feed_url}")
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        raise ValueError("No episodes found in feed")

    episodes = []
    for entry in feed.entries:
        episode = _parse_episode_entry(entry)
        episodes.append(episode)

    logger.info(f"Found {len(episodes)} episodes")
    return episodes


def fetch_episode_by_number(
    episode_number: int, feed_url: str = CONDUIT_RSS_FEED
) -> Optional[Dict]:
    """
    Fetch a specific episode by episode number.

    Args:
        episode_number: The episode number to fetch
        feed_url: URL of the RSS feed (defaults to Conduit feed)

    Returns:
        Episode dictionary with metadata, or None if not found
    """
    logger.info(f"Fetching episode {episode_number} from {feed_url}")
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        episode = _parse_episode_entry(entry)
        if episode["episode_number"] == episode_number:
            logger.info(f"Found episode {episode_number}")
            return episode

    logger.warning(f"Episode {episode_number} not found")
    return None


def fetch_latest_episode(feed_url: str = CONDUIT_RSS_FEED) -> Dict:
    """
    Fetch the latest episode from the feed.

    Args:
        feed_url: URL of the RSS feed (defaults to Conduit feed)

    Returns:
        Latest episode dictionary with metadata
    """
    logger.info(f"Fetching latest episode from {feed_url}")
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        raise ValueError("No episodes found in feed")

    # First entry is the latest
    latest_entry = feed.entries[0]
    episode = _parse_episode_entry(latest_entry)

    logger.info(f"Latest episode: {episode['episode_number']}")
    return episode


def fetch_latest_episode_details(feed_url: str = CONDUIT_RSS_FEED) -> Dict:
    """
    Fetch the latest episode from the feed with full details.

    Args:
        feed_url: URL of the RSS feed

    Returns:
        Latest episode dictionary with metadata
    """
    return fetch_latest_episode(feed_url)
