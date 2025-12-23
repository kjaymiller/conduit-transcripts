"""
Tests for the RSS feed module with episode caching.

Tests cover:
- Episode fetching with caching
- Single episode lookup
- Latest episode retrieval
- Environment variable support
- Integration with the episode cache
"""

import os
from unittest.mock import patch

import pytest

from src.rss_feed import (
    CONDUIT_RSS_FEED,
    fetch_episodes,
    fetch_episode_by_number,
    fetch_latest_episode,
    fetch_latest_episode_number,
)


@pytest.fixture
def mock_cache(mocker):
    """Mock the episode cache to avoid network requests."""
    return mocker.patch("src.rss_feed._cache")


class TestFetchEpisodes:
    """Tests for fetch_episodes function."""

    def test_fetch_episodes_returns_list(self, mock_cache):
        """fetch_episodes should return a list of episodes."""
        mock_episodes = [
            {
                "episode_number": 1,
                "title": "Episode 1",
                "description": "Test episode",
                "pub_date": "January 01, 2021",
                "url": "https://example.com",
                "audio_url": "https://example.com/audio.mp3",
            }
        ]
        mock_cache.get_episodes_with_numbers.return_value = mock_episodes

        episodes = fetch_episodes()

        assert isinstance(episodes, list)
        assert len(episodes) == 1
        assert episodes[0]["episode_number"] == 1

    def test_fetch_episodes_uses_cache(self, mock_cache):
        """fetch_episodes should use the cache."""
        mock_cache.get_episodes_with_numbers.return_value = []

        fetch_episodes()

        mock_cache.get_episodes_with_numbers.assert_called_once()

    def test_fetch_episodes_with_custom_feed_url(self, mock_cache):
        """fetch_episodes should accept custom feed URL."""
        custom_url = "https://custom-podcast.com/feed"
        mock_cache.get_episodes_with_numbers.return_value = []

        fetch_episodes(feed_url=custom_url)

        mock_cache.get_episodes_with_numbers.assert_called_once_with(custom_url)

    def test_fetch_episodes_uses_default_feed_url(self, mock_cache):
        """fetch_episodes should use PODCAST_FEED_URL if not specified."""
        mock_cache.get_episodes_with_numbers.return_value = []

        fetch_episodes()

        # Should be called with CONDUIT_RSS_FEED or PODCAST_FEED_URL
        mock_cache.get_episodes_with_numbers.assert_called_once()


class TestFetchEpisodeByNumber:
    """Tests for fetch_episode_by_number function."""

    def test_fetch_episode_by_number_found(self, mock_cache):
        """Should return episode when found."""
        mock_episode = {
            "episode_number": 42,
            "title": "Episode 42",
            "description": "Test",
            "pub_date": "June 01, 2023",
            "url": "https://example.com",
            "audio_url": "https://example.com/audio.mp3",
        }
        mock_cache.get_episode_by_number.return_value = mock_episode

        episode = fetch_episode_by_number(42)

        assert episode is not None
        assert episode["episode_number"] == 42
        assert episode["title"] == "Episode 42"

    def test_fetch_episode_by_number_not_found(self, mock_cache):
        """Should return None when episode not found."""
        mock_cache.get_episode_by_number.return_value = None

        episode = fetch_episode_by_number(999999)

        assert episode is None

    def test_fetch_episode_by_number_uses_cache(self, mock_cache):
        """fetch_episode_by_number should use the cache."""
        mock_cache.get_episode_by_number.return_value = None

        fetch_episode_by_number(1)

        mock_cache.get_episode_by_number.assert_called_once()

    def test_fetch_episode_by_number_with_custom_feed(self, mock_cache):
        """fetch_episode_by_number should accept custom feed URL."""
        custom_url = "https://custom-podcast.com/feed"
        mock_cache.get_episode_by_number.return_value = None

        fetch_episode_by_number(1, feed_url=custom_url)

        mock_cache.get_episode_by_number.assert_called_once_with(1, custom_url)


class TestFetchLatestEpisode:
    """Tests for fetch_latest_episode function."""

    def test_fetch_latest_episode_returns_dict(self, mock_cache):
        """fetch_latest_episode should return a dictionary."""
        mock_latest = {
            "episode_number": 100,
            "title": "Latest Episode",
            "description": "The newest episode",
            "pub_date": "December 15, 2024",
            "url": "https://example.com",
            "audio_url": "https://example.com/audio.mp3",
        }
        mock_cache.get_episodes_with_numbers.return_value = [mock_latest]

        episode = fetch_latest_episode()

        assert isinstance(episode, dict)
        assert episode["episode_number"] == 100

    def test_fetch_latest_episode_uses_max_episode_number(self, mock_cache):
        """fetch_latest_episode should find episode with highest number."""
        mock_episodes = [
            {"episode_number": 1, "title": "Old"},
            {"episode_number": 50, "title": "Middle"},
            {"episode_number": 100, "title": "Latest"},
        ]
        mock_cache.get_episodes_with_numbers.return_value = mock_episodes

        episode = fetch_latest_episode()

        assert episode["episode_number"] == 100
        assert episode["title"] == "Latest"

    def test_fetch_latest_episode_with_custom_feed(self, mock_cache):
        """fetch_latest_episode should accept custom feed URL."""
        custom_url = "https://custom-podcast.com/feed"
        mock_cache.get_episodes_with_numbers.return_value = [
            {"episode_number": 1, "title": "Test"}
        ]

        fetch_latest_episode(feed_url=custom_url)

        mock_cache.get_episodes_with_numbers.assert_called_once_with(custom_url)


class TestFetchLatestEpisodeNumber:
    """Tests for fetch_latest_episode_number function."""

    def test_fetch_latest_episode_number_returns_int(self, mock_cache):
        """fetch_latest_episode_number should return an integer."""
        mock_cache.get_episodes_with_numbers.return_value = [
            {"episode_number": 100, "title": "Latest"}
        ]

        latest_num = fetch_latest_episode_number()

        assert isinstance(latest_num, int)
        assert latest_num == 100

    def test_fetch_latest_episode_number_with_custom_feed(self, mock_cache):
        """fetch_latest_episode_number should accept custom feed URL."""
        custom_url = "https://custom-podcast.com/feed"
        mock_cache.get_episodes_with_numbers.return_value = [
            {"episode_number": 50, "title": "Test"}
        ]

        fetch_latest_episode_number(feed_url=custom_url)

        mock_cache.get_episodes_with_numbers.assert_called_once_with(custom_url)


class TestEnvironmentVariableSupport:
    """Tests for PODCAST_FEED_URL environment variable support."""

    def test_podcast_feed_url_env_var(self, mock_cache):
        """Module should read PODCAST_FEED_URL from environment."""
        # This test verifies the import-time behavior
        # The PODCAST_FEED_URL is set when the module is imported
        from src.rss_feed import PODCAST_FEED_URL

        assert PODCAST_FEED_URL is not None
        # Should be either the env var or default to Conduit
        assert isinstance(PODCAST_FEED_URL, str)
        assert PODCAST_FEED_URL.startswith("https://")

    def test_default_to_conduit_feed(self):
        """Should default to Conduit feed if env var not set."""
        with patch.dict(os.environ, {}, clear=False):
            # Remove PODCAST_FEED_URL if it exists
            if "PODCAST_FEED_URL" in os.environ:
                del os.environ["PODCAST_FEED_URL"]

            # Re-import to get fresh value
            import importlib
            import src.rss_feed

            importlib.reload(src.rss_feed)
            assert src.rss_feed.PODCAST_FEED_URL == CONDUIT_RSS_FEED
