"""
Basic tests for MCP server endpoints
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


@pytest.fixture
def mock_db_session():
    """Mock database session"""
    session = Mock()
    return session


@pytest.fixture
def mock_engine():
    """Mock SQLAlchemy engine"""
    engine = Mock()
    conn = Mock()
    conn.execute = Mock()
    engine.connect = Mock(return_value=conn)
    engine.__enter__ = Mock(return_value=conn)
    engine.__exit__ = Mock(return_value=False)
    conn.__enter__ = Mock(return_value=conn)
    conn.__exit__ = Mock(return_value=False)
    return engine


@pytest.fixture
def mock_embedding_model():
    """Mock embedding model"""
    model = Mock()
    model.embed_query = Mock(return_value=[0.1] * 768)
    model.embed_documents = Mock(return_value=[[0.1] * 768])
    return model


def test_root_endpoint(mock_engine, mock_embedding_model):
    """Test root endpoint returns server info"""
    # No need to patch db for root
    from apps.mcp.server import app

    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "endpoints" in data


def test_health_endpoint(mock_engine, mock_embedding_model):
    """Test health check endpoint"""
    # Patch VectorDatabase in server module (for health check)
    with patch("apps.mcp.server.VectorDatabase") as MockDB:
        MockDB.return_value.engine.connect.return_value.__enter__.return_value.execute.return_value = None
        from apps.mcp.server import app

        client = TestClient(app)
        response = client.get("/health")

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["database"] == "connected"
        assert "embedding_model" in data


def test_vector_search_validation(mock_engine, mock_embedding_model):
    """Test vector search requires query parameter"""
    from apps.mcp.server import app

    client = TestClient(app)

    # Missing query parameter
    response = client.get("/search/vector")
    assert response.status_code == 422  # Unprocessable Entity


def test_text_search_validation(mock_engine, mock_embedding_model):
    """Test text search requires query parameter"""
    from apps.mcp.server import app

    client = TestClient(app)

    # Missing query parameter
    response = client.get("/search/text")
    assert response.status_code == 422  # Unprocessable Entity


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
