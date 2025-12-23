"""Configuration module for Conduit Transcripts."""

import os
from typing import Optional
from functools import lru_cache

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """Application settings."""

    # Database configuration
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "transcripts")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_TABLE_TRANSCRIPTS: str = os.getenv("POSTGRES_TABLE_TRANSCRIPTS", "transcripts")
    POSTGRES_TABLE_VECTORS: str = os.getenv("POSTGRES_TABLE_VECTORS", "transcript_vector")

    # OpenSearch configuration
    OPENSEARCH_HOST: str = os.getenv("OPENSEARCH_HOST", "localhost")
    OPENSEARCH_PORT: str = os.getenv("OPENSEARCH_PORT", "9200")
    OPENSEARCH_INDEX: str = os.getenv("OPENSEARCH_INDEX", "transcripts")

    # Service URIs
    POSTGRES_SERVICE_URI: Optional[str] = os.getenv("POSTGRES_SERVICE_URI")
    AIVEN_POSTGRES_SERVICE_URI: Optional[str] = os.getenv("AIVEN_POSTGRES_SERVICE_URI")

    # Transcription configuration
    TRANSCRIPTION_MODEL: str = os.getenv("TRANSCRIPTION_MODEL", "base")
    PREFER_MLX: bool = os.getenv("PREFER_MLX", "true").lower() == "true"

    # Embedding configuration
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL", "sentence-transformers/all-mpnet-base-v2"
    )
    EMBEDDING_DEVICE: str = os.getenv("EMBEDDING_DEVICE", "cpu")

    # API configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))

    # Logging configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @property
    def postgres_uri(self) -> str:
        """Get PostgreSQL connection URI."""
        if self.AIVEN_POSTGRES_SERVICE_URI:
            return self.AIVEN_POSTGRES_SERVICE_URI
        if self.POSTGRES_SERVICE_URI:
            return self.POSTGRES_SERVICE_URI
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def opensearch_uri(self) -> str:
        """Get OpenSearch connection URI."""
        return f"http://{self.OPENSEARCH_HOST}:{self.OPENSEARCH_PORT}"


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
