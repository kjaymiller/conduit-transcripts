import pytest
from unittest.mock import Mock, patch, MagicMock
from conduit_transcripts.search.actions import title_search
from conduit_transcripts.models import Transcript


@patch("conduit_transcripts.search.actions.VectorDatabase")
def test_title_search(MockVectorDatabase):
    # Setup mock session and results
    session = Mock()
    MockVectorDatabase.return_value.Session.return_value = session

    mock_transcript = Mock(spec=Transcript)
    mock_transcript.episode_number = 1
    mock_transcript.podcast = 1
    mock_transcript.title = "Test Episode"
    mock_transcript.description = "A test description"
    mock_transcript.url = "http://example.com"
    mock_transcript.published_date = None

    # Configure query return
    # session.query(Transcript).filter(...).limit(...).all()
    query_mock = session.query.return_value
    filter_mock = query_mock.filter.return_value
    limit_mock = filter_mock.limit.return_value
    limit_mock.all.return_value = [mock_transcript]

    # Execute search
    results = title_search("Test")

    # Verify
    assert len(results) == 1
    assert results[0].title == "Test Episode"
    assert results[0].episode_number == 1
    assert results[0].content_snippet == "A test description"

    # Verify query
    session.query.assert_called_with(Transcript)
