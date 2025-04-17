"""
Creates the index for opensearch

Should be ran before sending information to a new database
"""

import os

from dotenv import load_dotenv
from opensearchpy import OpenSearch

load_dotenv()

connection_string = os.getenv("OPENSEARCH_SERVICE_URI")
client = OpenSearch(connection_string, use_ssl=True, timeout=100)
client.info()

index_settings = {
    "settings": {
        "index": {"knn": True},
    },
    "mappings": {
        "properties": {
            "title": {"type": "text"},
            "episode_number": {"type": "int"},
            "description": {"type": "text"},
            "url": {"type": "keyword"},
            "content": {"type": "text"},
            "content_vector": {
                "type": "knn_vector",
                "dimension": 768,
                "method": {
                    "name": "hnsw",
                    "space_type": "l2",
                    "engine": "faiss",
                },
            },
            "pub_date": {"type": "date"},
        }
    },
}

index_name = os.getenv("INDEX_NAME", "transcripts")


def create_index(index_name: str = index_name, index_settings=index_settings):
    """Checks for existing index and deletes it and recreates it if it exists"""
    if client.indices.exists(index=index_name):
        client.indices.delete(index=index_name)

    client.indices.create(index=index_name, body=index_settings, ignore=400)
