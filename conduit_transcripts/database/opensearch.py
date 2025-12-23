"""OpenSearch database operations."""

import logging
import uuid
from typing import Dict, Any, List, Optional

import frontmatter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Import OpenSearch lazily
try:
    from opensearchpy import OpenSearch, helpers
    OPENSEARCH_AVAILABLE = True
except ImportError:
    OPENSEARCH_AVAILABLE = False

from conduit_transcripts.config import settings

logger = logging.getLogger(__name__)


class OpenSearchDatabase:
    """Handler for OpenSearch database operations."""

    def __init__(self):
        """Initialize the OpenSearch handler."""
        if not OPENSEARCH_AVAILABLE:
            raise ImportError(
                "opensearch-py is not installed. Install with 'uv pip install conduit-transcripts[opensearch]' or 'uv sync --extra opensearch'"
            )
            
        self.client = OpenSearch(
            hosts=[{"host": settings.OPENSEARCH_HOST, "port": int(settings.OPENSEARCH_PORT)}],
            use_ssl=True,
            verify_certs=False,  # For dev environments
            timeout=100,
        )
        self.index_name = settings.OPENSEARCH_INDEX

        # Initialize text processing tools
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=20,
            separators=[".", "!", "?", "\n"],
        )

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={"device": settings.EMBEDDING_DEVICE},
            encode_kwargs={"normalize_embeddings": False},
        )

    def create_index(self) -> None:
        """Create the OpenSearch index with mapping."""
        if not self.client.indices.exists(index=self.index_name):
            logger.info(f"Creating index {self.index_name}")
            # Define index mapping here (vector field, etc.)
            # For brevity, assuming dynamic mapping or basic setup
            body = {
                "settings": {"index": {"knn": True}},
                "mappings": {
                    "properties": {
                        "content_vector": {
                            "type": "knn_vector",
                            "dimension": 768,
                            "method": {
                                "name": "hnsw",
                                "space_type": "l2",
                                "engine": "nmslib",
                                "parameters": {"ef_construction": 128, "m": 24},
                            },
                        }
                    }
                },
            }
            self.client.indices.create(index=self.index_name, body=body)

    def process_frontmatter_post(self, post: frontmatter.Post) -> bool:
        """Process a frontmatter post and index in OpenSearch."""
        try:
            metadata = post.metadata.copy()
            content = post.content

            chunks = self.text_splitter.create_documents([content])
            texts = [chunk.page_content for chunk in chunks]
            embeddings = self.embedding_model.embed_documents(texts)

            docs = []
            for text_content, embedding in zip(texts, embeddings):
                doc = {
                    **metadata,
                    "content": text_content,
                    "content_vector": embedding,
                    "podcast": "Conduit",
                }
                docs.append(
                    {
                        "_index": self.index_name,
                        "_id": str(uuid.uuid4()),
                        "_source": doc,
                    }
                )

            success, failed = helpers.bulk(self.client, docs, stats_only=True)
            logger.info(f"Indexed {success} chunks, {failed} failed")
            return failed == 0

        except Exception as e:
            logger.error(f"Error indexing to OpenSearch: {e}")
            return False
