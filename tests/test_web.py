import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from apps.web.main import app
from conduit_transcripts.models import Transcript

client = TestClient(app)


@patch("conduit_transcripts.search.actions.VectorDatabase")
def test_web_title_search(MockVectorDatabase):
    # Setup mock
    session = Mock()
    MockVectorDatabase.return_value.Session.return_value = session

    mock_transcript = Mock(spec=Transcript)
    mock_transcript.episode_number = 100
    mock_transcript.title = "Test Episode 100"
    mock_transcript.description = "Description 100"
    mock_transcript.podcast = 1
    mock_transcript.url = "http://example.com"
    mock_transcript.published_date = None

    query_mock = session.query.return_value
    filter_mock = query_mock.filter.return_value
    limit_mock = filter_mock.limit.return_value
    limit_mock.all.return_value = [mock_transcript]

    # Run request
    response = client.get("/search/title?query=Test")

    # Verify
    assert response.status_code == 200
    data = response.json()
    assert data["query"] == "Test"
    assert data["search_type"] == "title_match"
    assert len(data["results"]) == 1
    assert data["results"][0]["title"] == "Test Episode 100"

    # Verify query
    session.query.assert_called_with(Transcript)
