"""Tests for transcript deletion functionality."""

import pytest
from click.testing import CliRunner
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch, MagicMock

from cli.main import cli
from app.main import app
from podcast_transcription_core.models import Transcript

runner = CliRunner()
client = TestClient(app)


class TestCLIDelete:
    """Tests for CLI delete command."""

    @patch("podcast_transcription_core.database.postgres.VectorDatabase")
    def test_delete_single_episode(self, MockVectorDatabase):
        """Test deleting a single episode."""
        session = Mock()
        MockVectorDatabase.return_value.Session.return_value = session

        mock_transcript = Mock(spec=Transcript)
        mock_transcript.episode_number = 100
        mock_transcript.podcast = 1

        query_mock = session.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.return_value = mock_transcript

        result = runner.invoke(cli, ["delete", "100", "--yes"])

        assert result.exit_code == 0
        assert "Deleted episode 100" in result.stdout
        assert "Deleted 1 transcript(s)" in result.stdout
        session.delete.assert_called_once_with(mock_transcript)
        session.commit.assert_called_once()

    @patch("podcast_transcription_core.database.postgres.VectorDatabase")
    def test_delete_episode_not_found(self, MockVectorDatabase):
        """Test deleting an episode that doesn't exist."""
        session = Mock()
        MockVectorDatabase.return_value.Session.return_value = session

        query_mock = session.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.return_value = None

        result = runner.invoke(cli, ["delete", "999", "--yes"])

        assert result.exit_code == 0
        assert "Episode 999 not found" in result.stdout
        assert "Deleted 0 transcript(s)" in result.stdout
        session.delete.assert_not_called()

    @patch("podcast_transcription_core.database.postgres.VectorDatabase")
    def test_delete_multiple_episodes(self, MockVectorDatabase):
        """Test deleting multiple episodes."""
        session = Mock()
        MockVectorDatabase.return_value.Session.return_value = session

        def mock_first():
            mock_transcript = Mock(spec=Transcript)
            mock_transcript.episode_number = 100
            mock_transcript.podcast = 1
            return mock_transcript

        query_mock = session.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.side_effect = [mock_first(), mock_first(), mock_first()]

        result = runner.invoke(cli, ["delete", "100-102", "--yes"])

        assert result.exit_code == 0
        assert "Deleted 3 transcript(s)" in result.stdout
        assert session.delete.call_count == 3

    @patch("podcast_transcription_core.database.postgres.VectorDatabase")
    def test_delete_requires_confirmation(self, MockVectorDatabase):
        """Test that delete requires confirmation without --yes flag."""
        result = runner.invoke(cli, ["delete", "100"], input="n\n")

        assert result.exit_code == 0
        assert "Cancelled" in result.stdout

    @patch("podcast_transcription_core.database.postgres.VectorDatabase")
    def test_delete_with_confirmation(self, MockVectorDatabase):
        """Test delete with user confirmation."""
        session = Mock()
        MockVectorDatabase.return_value.Session.return_value = session

        mock_transcript = Mock(spec=Transcript)
        query_mock = session.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.return_value = mock_transcript

        result = runner.invoke(cli, ["delete", "100"], input="y\n")

        assert result.exit_code == 0
        assert "Deleted episode 100" in result.stdout
        session.delete.assert_called_once()


class TestAPIDelete:
    """Tests for API delete endpoint."""

    @patch("app.api.routes.VectorDatabase")
    def test_delete_episode_success(self, MockVectorDatabase):
        """Test successful episode deletion via API."""
        session = Mock()
        MockVectorDatabase.return_value.Session.return_value = session

        mock_transcript = Mock(spec=Transcript)
        mock_transcript.episode_number = 100
        mock_transcript.podcast = 1

        query_mock = session.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.return_value = mock_transcript

        response = client.delete("/api/v1/episode/100")

        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert data["episode_number"] == 100
        assert "deleted successfully" in data["message"]
        session.delete.assert_called_once_with(mock_transcript)
        session.commit.assert_called_once()

    @patch("app.api.routes.VectorDatabase")
    def test_delete_episode_not_found(self, MockVectorDatabase):
        """Test deleting non-existent episode via API."""
        session = Mock()
        MockVectorDatabase.return_value.Session.return_value = session

        query_mock = session.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.return_value = None

        response = client.delete("/api/v1/episode/999")

        assert response.status_code == 404
        data = response.json()
        assert "not found" in data["detail"]
        session.delete.assert_not_called()

    @patch("app.api.routes.VectorDatabase")
    def test_delete_with_podcast_id(self, MockVectorDatabase):
        """Test deleting episode with specific podcast_id."""
        session = Mock()
        MockVectorDatabase.return_value.Session.return_value = session

        mock_transcript = Mock(spec=Transcript)
        query_mock = session.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.first.return_value = mock_transcript

        response = client.delete("/api/v1/episode/100?podcast_id=2")

        assert response.status_code == 200
        session.delete.assert_called_once()
