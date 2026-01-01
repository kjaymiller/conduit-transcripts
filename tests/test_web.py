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


@patch("apps.web.main.actions.get_episode_details")
def test_episode_page(mock_get_details):
    # Setup
    mock_get_details.return_value = {
        "episode_number": 100,
        "podcast": "1",
        "metadata": {
            "title": "Test Episode",
            "description": "A test description",
            "url": "http://example.com",
            "pub_date": "2023-01-01",
        },
        "content": "# Markdown Content",
        "chunks_count": 10,
    }

    # Run
    response = client.get("/episode/100")

    # Verify
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "Test Episode" in response.text
    # Check if markdown was converted to HTML
    assert "<h1>Markdown Content</h1>" in response.text


@patch("apps.web.main.rag.generate_episode_response")
def test_chat_episode(mock_generate):
    # Setup
    def fake_generator(query, episode_number):
        yield "Hello "
        yield "World"

    mock_generate.side_effect = fake_generator

    # Run
    response = client.post("/api/chat/100", json={"query": "hello"})

    # Verify
    assert response.status_code == 200
    # TestClient reads the full streaming response
    assert response.text == "Hello World"

    mock_generate.assert_called_once_with("hello", 100)
