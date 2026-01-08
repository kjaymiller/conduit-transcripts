import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from app.main import app
from podcast_transcription_core.models import Transcript, VectorChunk

client = TestClient(app)


@patch("podcast_transcription_core.database.postgres.VectorDatabase")
@patch("app.main.settings")
def test_search_no_results(mock_settings, MockVectorDatabase):
    # Setup mocks
    session = Mock()
    MockVectorDatabase.return_value.Session.return_value = session

    # Mock settings
    mock_settings.EMBEDDING_PROVIDER = "ollama"
    mock_settings.EMBEDDING_MODEL = "nomic-embed-text"
    mock_settings.OLLAMA_BASE_URL = "http://localhost:11434"

    # Mock empty results for vector search
    # Vector search uses session.execute().all()
    session.execute.return_value.all.return_value = []

    # Run request
    response = client.get("/search?query=NonExistentTerm&search_type=vector")

    # Verify
    assert response.status_code == 200
    assert "No Results Found" in response.text
    assert (
        'We couldn\'t find any transcripts matching "NonExistentTerm"' in response.text
    )


@patch("podcast_transcription_core.database.postgres.VectorDatabase")
@patch("app.main.settings")
def test_search_with_results(mock_settings, MockVectorDatabase):
    # Setup mocks
    session = Mock()
    MockVectorDatabase.return_value.Session.return_value = session

    mock_settings.EMBEDDING_PROVIDER = "ollama"

    # Mock results
    mock_chunk = Mock(spec=VectorChunk)
    mock_chunk.episode_number = 100
    mock_chunk.content = "Found content"

    session.execute.return_value.all.return_value = [(mock_chunk, 0.1)]

    # Run request
    response = client.get("/search?query=Found&search_type=vector")

    # Verify
    assert response.status_code == 200
    assert "1 Results Found" in response.text
    assert "Episode 100" in response.text
    assert "Found content" in response.text
