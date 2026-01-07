import pytest
from click.testing import CliRunner
from unittest.mock import Mock, patch
from cli.main import cli
from conduit_transcripts.models import Transcript

runner = CliRunner()


@patch("conduit_transcripts.database.postgres.VectorDatabase")
def test_cli_title_search(MockVectorDatabase):
    # Setup mock
    session = Mock()
    MockVectorDatabase.return_value.Session.return_value = session

    mock_transcript = Mock(spec=Transcript)
    mock_transcript.episode_number = 100
    mock_transcript.title = "Test Episode 100"
    mock_transcript.description = "Description 100"

    query_mock = session.query.return_value
    filter_mock = query_mock.filter.return_value
    limit_mock = filter_mock.limit.return_value
    limit_mock.all.return_value = [mock_transcript]

    # Run command
    result = runner.invoke(cli, ["search", "Test", "--title"])

    # Verify
    assert result.exit_code == 0
    assert "Title Search Results" in result.stdout
    assert "Test Episode 100" in result.stdout
    assert "100" in result.stdout

    # Verify query was called
    session.query.assert_called_with(Transcript)
