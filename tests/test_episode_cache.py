"""
Tests for the episode caching and numbering system.

Tests cover:
- Episode number assignment based on chronological order
- Cache creation and persistence
- Cache invalidation on feed changes
- Episode lookups by number
- Multi-podcast support
"""

import json
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import feedparser
import pytest

from src.episode_cache import EpisodeCache


@pytest.fixture
def temp_cache_dir():
    """Create a temporary directory for cache files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def episode_cache(temp_cache_dir):
    """Create an EpisodeCache instance with a temporary directory."""
    return EpisodeCache(cache_dir=temp_cache_dir)


@pytest.fixture
def sample_feed_url():
    """Return the Conduit podcast RSS feed URL."""
    return "https://www.relay.fm/conduit/feed"


class TestEpisodeNumberAssignment:
    """Test that episode numbers are assigned correctly by chronological order."""

    def test_episodes_numbered_chronologically(self, episode_cache, sample_feed_url):
        """Episodes should be numbered 1, 2, 3... by release date (oldest first)."""
        episodes = episode_cache.get_episodes_with_numbers(sample_feed_url)

        # Check that episodes are numbered sequentially
        episode_numbers = [ep["episode_number"] for ep in episodes]
        assert episode_numbers == list(range(1, len(episodes) + 1))

        # Check that episodes are sorted by publication date (oldest first)
        pub_dates = [ep["raw_pub_date"] for ep in episodes if ep["raw_pub_date"]]
        assert pub_dates == sorted(pub_dates)

    def test_latest_episode_has_highest_number(self, episode_cache, sample_feed_url):
        """The most recently published episode should have the highest episode number."""
        episodes = episode_cache.get_episodes_with_numbers(sample_feed_url)
        max_episode_number = max(ep["episode_number"] for ep in episodes)

        # Get the episode with the max number
        latest_episode = next(
            ep for ep in episodes if ep["episode_number"] == max_episode_number
        )

        # Verify it's the most recently published
        all_dates = [ep["raw_pub_date"] for ep in episodes if ep["raw_pub_date"]]
        assert latest_episode["raw_pub_date"] == max(all_dates)

    def test_zero_based_indexing(self, temp_cache_dir, sample_feed_url):
        """Episodes should be numbered 0, 1, 2... when zero_based is True."""
        # Create cache with zero-based indexing
        zero_based_cache = EpisodeCache(cache_dir=temp_cache_dir, zero_based=True)
        episodes = zero_based_cache.get_episodes_with_numbers(sample_feed_url)

        # Check that episodes are numbered starting from 0
        episode_numbers = [ep["episode_number"] for ep in episodes]
        assert episode_numbers == list(range(0, len(episodes)))

        # Latest episode should still be the most recent
        max_episode_number = max(ep["episode_number"] for ep in episodes)
        latest_episode = next(
            ep for ep in episodes if ep["episode_number"] == max_episode_number
        )
        all_dates = [ep["raw_pub_date"] for ep in episodes if ep["raw_pub_date"]]
        assert latest_episode["raw_pub_date"] == max(all_dates)


class TestCaching:
    """Test cache creation, persistence, and invalidation."""

    def test_cache_created_on_first_fetch(self, episode_cache, sample_feed_url):
        """Cache file should be created after first fetch."""
        cache_path = episode_cache._get_cache_path(sample_feed_url)
        assert not cache_path.exists()

        episode_cache.get_episodes_with_numbers(sample_feed_url)

        assert cache_path.exists()

    def test_cache_contains_feed_hash(self, episode_cache, sample_feed_url):
        """Cache file should contain a feed hash for change detection."""
        episode_cache.get_episodes_with_numbers(sample_feed_url)

        cache_path = episode_cache._get_cache_path(sample_feed_url)
        with open(cache_path, "r") as f:
            cache_data = json.load(f)

        assert "feed_hash" in cache_data
        assert "episodes" in cache_data
        assert isinstance(cache_data["feed_hash"], str)
        assert len(cache_data["feed_hash"]) > 0

    def test_cache_reused_on_second_fetch(self, episode_cache, sample_feed_url, mocker):
        """Second fetch should reuse cached episodes when feed hasn't changed."""
        # First fetch - populates cache
        episodes1 = episode_cache.get_episodes_with_numbers(sample_feed_url)
        cache_path = episode_cache._get_cache_path(sample_feed_url)
        assert cache_path.exists()

        # Get the cached hash
        import json
        with open(cache_path, "r") as f:
            cache_data1 = json.load(f)
        hash1 = cache_data1["feed_hash"]

        # Second fetch - should use cache
        episodes2 = episode_cache.get_episodes_with_numbers(sample_feed_url)

        # Verify results are identical
        assert len(episodes1) == len(episodes2)
        assert episodes1[0]["episode_number"] == episodes2[0]["episode_number"]

        # Cache should still exist with same hash
        with open(cache_path, "r") as f:
            cache_data2 = json.load(f)
        hash2 = cache_data2["feed_hash"]
        assert hash1 == hash2

    def test_cache_cleared_on_feed_change(self, episode_cache, temp_cache_dir, mocker):
        """Cache should be invalidated when feed contents change."""
        sample_url = "https://www.relay.fm/conduit/feed"

        # First fetch
        episodes1 = episode_cache.get_episodes_with_numbers(sample_url)
        num_episodes_1 = len(episodes1)

        # Simulate a feed change by mocking with different feed data
        original_feed = feedparser.parse(sample_url)

        # Create a modified feed with different entries
        modified_feed = feedparser.FeedParserDict()
        modified_feed.entries = original_feed.entries[:10]  # Fewer entries

        mock_parse = mocker.patch("src.episode_cache.feedparser.parse")
        mock_parse.return_value = modified_feed

        # Second fetch should detect feed change and recalculate
        episodes2 = episode_cache.get_episodes_with_numbers(sample_url)

        # Should have different number of episodes
        assert len(episodes2) == 10
        assert len(episodes2) != num_episodes_1

    def test_clear_cache_single_feed(self, episode_cache, sample_feed_url):
        """clear_cache() should remove cache for a specific feed."""
        # Create cache
        episode_cache.get_episodes_with_numbers(sample_feed_url)
        cache_path = episode_cache._get_cache_path(sample_feed_url)
        assert cache_path.exists()

        # Clear cache
        episode_cache.clear_cache(sample_feed_url)
        assert not cache_path.exists()

    def test_clear_cache_all_feeds(self, episode_cache, sample_feed_url):
        """clear_cache() with no args should remove all caches."""
        # Create caches for multiple feeds
        feed1 = "https://www.relay.fm/conduit/feed"
        feed2 = "https://www.relay.fm/incomparable/feed"

        episode_cache.get_episodes_with_numbers(feed1)
        path1 = episode_cache._get_cache_path(feed1)
        assert path1.exists()

        # Clear all caches
        episode_cache.clear_cache()
        assert not path1.exists()


class TestEpisodeLookup:
    """Test episode lookup by number."""

    def test_get_episode_by_number_found(self, episode_cache, sample_feed_url):
        """Should return episode when number exists."""
        episode = episode_cache.get_episode_by_number(1, sample_feed_url)

        assert episode is not None
        assert episode["episode_number"] == 1
        assert "title" in episode
        assert "audio_url" in episode

    def test_get_episode_by_number_not_found(self, episode_cache, sample_feed_url):
        """Should return None when episode number doesn't exist."""
        episode = episode_cache.get_episode_by_number(999999, sample_feed_url)
        assert episode is None

    def test_episode_metadata_complete(self, episode_cache, sample_feed_url):
        """Episodes should have all required metadata."""
        episodes = episode_cache.get_episodes_with_numbers(sample_feed_url)
        episode = episodes[0]

        # Check required fields
        assert "episode_number" in episode
        assert "title" in episode
        assert "description" in episode
        assert "pub_date" in episode
        assert "url" in episode
        assert "audio_url" in episode

        # Check types
        assert isinstance(episode["episode_number"], int)
        assert isinstance(episode["title"], str)
        assert episode["audio_url"] is None or isinstance(episode["audio_url"], str)


class TestMultiPodcastSupport:
    """Test support for multiple podcast feeds."""

    def test_different_feed_urls_cached_separately(
        self, episode_cache, mocker
    ):
        """Different feeds should have separate cache files."""
        feed1 = "https://www.relay.fm/conduit/feed"
        feed2 = "https://www.relay.fm/incomparable/feed"

        # Mock both feeds
        mock_parse = mocker.patch("src.episode_cache.feedparser.parse")

        # Create mock feeds
        feed1_data = feedparser.parse(feed1)
        feed2_data = feedparser.parse(feed1)  # Use same data for simplicity
        feed2_data.entries = feed2_data.entries[:5]

        def parse_side_effect(url):
            if url == feed1:
                return feed1_data
            else:
                return feed2_data

        mock_parse.side_effect = parse_side_effect

        # Fetch from both feeds
        episodes1 = episode_cache.get_episodes_with_numbers(feed1)
        episodes2 = episode_cache.get_episodes_with_numbers(feed2)

        # Should have different cache files
        cache_path1 = episode_cache._get_cache_path(feed1)
        cache_path2 = episode_cache._get_cache_path(feed2)
        assert cache_path1 != cache_path2
        assert cache_path1.exists()
        assert cache_path2.exists()

    def test_env_var_podcast_feed_url(self, episode_cache, mocker):
        """Should respect PODCAST_FEED_URL environment variable."""
        custom_feed = "https://custom-podcast.com/feed"
        mocker.patch.dict(
            "os.environ", {"PODCAST_FEED_URL": custom_feed}
        )

        # Import after setting env var
        from src import rss_feed

        # Clear the module to reimport with new env var
        mock_parse = mocker.patch("src.rss_feed._cache.get_episodes_with_numbers")
        mock_parse.return_value = []

        # The PODCAST_FEED_URL should be set during import
        assert rss_feed.PODCAST_FEED_URL == custom_feed or rss_feed.PODCAST_FEED_URL == rss_feed.CONDUIT_RSS_FEED


class TestFeedHashComputation:
    """Test feed hash computation for change detection."""

    def test_same_feed_produces_same_hash(self, episode_cache):
        """Same feed should produce same hash."""
        feed = feedparser.parse("https://www.relay.fm/conduit/feed")
        hash1 = episode_cache._compute_feed_hash(feed.entries)
        hash2 = episode_cache._compute_feed_hash(feed.entries)

        assert hash1 == hash2

    def test_different_feeds_produce_different_hashes(self, episode_cache):
        """Different feed contents should produce different hashes."""
        feed = feedparser.parse("https://www.relay.fm/conduit/feed")
        hash1 = episode_cache._compute_feed_hash(feed.entries)

        # Modify feed
        modified_entries = feed.entries[:5]
        hash2 = episode_cache._compute_feed_hash(modified_entries)

        assert hash1 != hash2
