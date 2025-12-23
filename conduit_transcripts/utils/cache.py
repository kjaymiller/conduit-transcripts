"""
Episode caching and numbering for multi-podcast support.

This module handles:
- Caching episodes from RSS feeds to minimize network requests
- Assigning sequential episode numbers based on chronological order
- Detecting feed changes and recalculating only when needed
- Supporting podcasts with or without explicit episode numbering
- Zero-based indexing support for podcasts with episode 0
"""

import hashlib
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import feedparser

logger = logging.getLogger(__name__)


class EpisodeCache:
    """Manages episode caching and numbering for RSS feeds."""

    def __init__(self, cache_dir: str = ".episode_cache", zero_based: bool = False):
        """
        Initialize the episode cache.

        Args:
            cache_dir: Directory to store cache files
            zero_based: If True, start numbering from 0 instead of 1
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.zero_based = zero_based

    def _get_cache_path(self, feed_url: str) -> Path:
        """Generate a cache file path for a feed URL."""
        # Create a safe filename from the feed URL using hash
        hash_name = hashlib.md5(feed_url.encode()).hexdigest()
        return self.cache_dir / f"{hash_name}.json"

    def _compute_feed_hash(self, entries: List) -> str:
        """
        Compute a hash of feed contents for change detection.

        Args:
            entries: List of feedparser entries

        Returns:
            MD5 hash of feed contents
        """
        # Hash based on entry titles and publication dates
        data = json.dumps(
            {
                "entries": [
                    {
                        "title": e.get("title", ""),
                        "published": e.get("published", ""),
                    }
                    for e in entries
                ]
            },
            sort_keys=True,
        )
        return hashlib.md5(data.encode()).hexdigest()

    def _parse_episode_entry(self, entry: Any, episode_number: int) -> Dict:
        """
        Parse a single RSS feed entry into our episode format.

        Args:
            entry: A feedparser entry object
            episode_number: The sequential episode number (from chronological position)

        Returns:
            Dictionary with episode metadata
        """
        # Get original title
        title = entry.get("title", "")

        # Get audio URL from enclosure
        audio_url = None
        if hasattr(entry, "enclosures") and entry.enclosures:
            audio_url = entry.enclosures[0].href
        elif "enclosures" in entry and entry["enclosures"]:
            audio_url = entry["enclosures"][0]["href"]

        # Parse publication date
        pub_date = None
        raw_pub_date = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            raw_pub_date = datetime(*entry.published_parsed[:6])
            pub_date = raw_pub_date.strftime("%B %d, %Y")
        elif "published_parsed" in entry and entry["published_parsed"]:
            raw_pub_date = datetime(*entry["published_parsed"][:6])
            pub_date = raw_pub_date.strftime("%B %d, %Y")

        # Get description/summary
        description = entry.get("summary", entry.get("subtitle", ""))

        # Get episode URL
        episode_url = entry.get("link", "")

        return {
            "episode_number": episode_number,
            "title": title,
            "description": description,
            "pub_date": pub_date,
            "raw_pub_date": raw_pub_date,  # Keep for sorting/comparison
            "url": episode_url,
            "audio_url": audio_url,
        }

    def _assign_episode_numbers(self, feed) -> List[Dict]:
        """
        Sort entries by publication date (oldest first) and assign sequential episode numbers.

        Args:
            feed: Parsed feedparser feed object

        Returns:
            List of episodes with assigned sequential numbers
        """
        # Collect entries with their publication dates
        entries_with_date: List[Tuple[datetime, Any]] = []
        for entry in feed.entries:
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                dt = datetime(*entry.published_parsed[:6])
                entries_with_date.append((dt, entry))
            elif "published_parsed" in entry and entry["published_parsed"]:
                dt = datetime(*entry["published_parsed"][:6])
                entries_with_date.append((dt, entry))
            else:
                # Entries without dates go to the end
                entries_with_date.append((datetime.max, entry))

        # Sort by date ascending (oldest first)
        entries_with_date.sort(key=lambda x: x[0])

        # Assign sequential episode numbers (0-indexed or 1-indexed based on config)
        episodes = []
        start_num = 0 if self.zero_based else 1
        for episode_num, (dt, entry) in enumerate(entries_with_date, start=start_num):
            episode = self._parse_episode_entry(entry, episode_num)
            episodes.append(episode)

        return episodes

    def get_episodes_with_numbers(self, feed_url: str) -> List[Dict]:
        """
        Get all episodes from a feed with assigned sequential numbers.

        Uses caching: only refetches the feed if contents have changed.

        Args:
            feed_url: URL of the RSS feed

        Returns:
            List of episode dictionaries with assigned episode numbers
        """
        logger.info(f"Fetching episodes from {feed_url}")

        # Check cache first to avoid unnecessary network requests
        cache_path = self._get_cache_path(feed_url)
        if cache_path.exists():
            try:
                with open(cache_path, "r") as f:
                    cache_data = json.load(f)
                    # Fetch feed to compute current hash
                    feed = feedparser.parse(feed_url)
                    if not feed.entries:
                        raise ValueError("No episodes found in feed")
                    current_hash = self._compute_feed_hash(feed.entries)

                    # Validate cache
                    if cache_data.get("feed_hash") == current_hash:
                        logger.info(
                            f"Using cached episodes ({len(cache_data['episodes'])} episodes)"
                        )
                        return cache_data["episodes"]
            except (json.JSONDecodeError, KeyError):
                # Cache corrupted, will recalculate
                pass

        # Cache miss or not yet created - fetch feed
        logger.info("Fetching feed to assign episode numbers")
        feed = feedparser.parse(feed_url)

        if not feed.entries:
            raise ValueError("No episodes found in feed")

        # Compute hash of current feed contents
        current_hash = self._compute_feed_hash(feed.entries)

        # Recalculate episode numbers
        logger.info("Recalculating episode numbers")
        episodes = self._assign_episode_numbers(feed)

        # Save to cache
        cache_data = {"feed_hash": current_hash, "episodes": episodes}
        with open(cache_path, "w") as f:
            json.dump(cache_data, f, default=str, indent=2)

        logger.info(f"Found and cached {len(episodes)} episodes")
        return episodes

    def get_episode_by_number(
        self, episode_number: int, feed_url: str
    ) -> Optional[Dict]:
        """
        Get a specific episode by its sequential number.

        Args:
            episode_number: The episode number to fetch
            feed_url: URL of the RSS feed

        Returns:
            Episode dictionary or None if not found
        """
        episodes = self.get_episodes_with_numbers(feed_url)
        for episode in episodes:
            if episode["episode_number"] == episode_number:
                logger.info(f"Found episode {episode_number}")
                return episode

        logger.warning(f"Episode {episode_number} not found")
        return None

    def clear_cache(self, feed_url: Optional[str] = None) -> None:
        """
        Clear cache for a specific feed or all feeds.

        Args:
            feed_url: URL of feed to clear, or None to clear all
        """
        if feed_url:
            cache_path = self._get_cache_path(feed_url)
            if cache_path.exists():
                cache_path.unlink()
                logger.info(f"Cleared cache for {feed_url}")
        else:
            for cache_file in self.cache_dir.glob("*.json"):
                cache_file.unlink()
            logger.info("Cleared all episode caches")
