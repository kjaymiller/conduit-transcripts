"""
Creates the index for opensearch

Should be ran before sending information to a new database
"""

import copy
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
            "title": {
                "type": "text",
                "fields": {
                    "keyword": {"type": "keyword"}
                }
            },
            "episode_number": {"type": "integer"},
            "description": {"type": "text"},
            "url": {"type": "keyword"},
            "image_url": {"type": "keyword"},
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
index_name_with_timestamps = os.getenv("INDEX_NAME_WITH_TIMESTAMPS", f"{index_name}_timestamps")


def create_index_with_timestamps(index_name: str = index_name_with_timestamps):
    """Creates an index with timestamp fields for timecode support"""
    # Start with base index settings (deep copy to avoid modifying original)
    timestamps_index_settings = copy.deepcopy(index_settings)
    
    # Add timestamp-related fields to mappings
    timestamps_index_settings["mappings"]["properties"]["youtube_url"] = {"type": "keyword"}
    timestamps_index_settings["mappings"]["properties"]["youtube_video_id"] = {"type": "keyword"}
    timestamps_index_settings["mappings"]["properties"]["timestamp"] = {"type": "integer"}
    timestamps_index_settings["mappings"]["properties"]["chunk_index"] = {"type": "integer"}
    
    if client.indices.exists(index=index_name):
        print(f"Deleting existing index {index_name}")
        client.indices.delete(index=index_name)

    print(f"Creating index {index_name} with knn_vector mapping and timestamp fields")
    try:
        response = client.indices.create(
            index=index_name,
            body=timestamps_index_settings
        )
        print(f"✅ Index created successfully: {response}")
    except Exception as e:
        print(f"❌ Error creating index: {e}")
        raise
    
    # Verify the mapping was applied correctly
    print(f"\nVerifying index mapping...")
    mapping = client.indices.get_mapping(index=index_name)
    content_vector_type = mapping[index_name]["mappings"]["properties"].get("content_vector", {}).get("type")
    if content_vector_type == "knn_vector":
        print(f"✅ content_vector field is correctly set to knn_vector")
    else:
        print(f"⚠️  WARNING: content_vector field type is '{content_vector_type}', expected 'knn_vector'")
        print(f"   This may cause vector search to fail. Please recreate the index.")
    
    # Verify timestamp fields
    has_timestamp = "timestamp" in mapping[index_name]["mappings"]["properties"]
    has_youtube_url = "youtube_url" in mapping[index_name]["mappings"]["properties"]
    if has_timestamp and has_youtube_url:
        print(f"✅ Timestamp fields are correctly set")
    else:
        print(f"⚠️  WARNING: Some timestamp fields are missing")


def create_index(index_name: str = index_name, index_settings=index_settings, with_timestamps: bool = False):
    """Checks for existing index and deletes it and recreates it if it exists
    
    Args:
        index_name: Name of the index to create
        index_settings: Index settings to use (defaults to base settings)
        with_timestamps: If True, create index with timestamp fields
    """
    if with_timestamps:
        create_index_with_timestamps(index_name)
        return
    
    if client.indices.exists(index=index_name):
        print(f"Deleting existing index {index_name}")
        client.indices.delete(index=index_name)

    print(f"Creating index {index_name} with knn_vector mapping")
    try:
        response = client.indices.create(
            index=index_name,
            body=index_settings
        )
        print(f"✅ Index created successfully: {response}")
    except Exception as e:
        print(f"❌ Error creating index: {e}")
        raise
    
    # Verify the mapping was applied correctly
    print(f"\nVerifying index mapping...")
    mapping = client.indices.get_mapping(index=index_name)
    content_vector_type = mapping[index_name]["mappings"]["properties"].get("content_vector", {}).get("type")
    if content_vector_type == "knn_vector":
        print(f"✅ content_vector field is correctly set to knn_vector")
    else:
        print(f"⚠️  WARNING: content_vector field type is '{content_vector_type}', expected 'knn_vector'")
        print(f"   This may cause vector search to fail. Please recreate the index.")

if __name__ == "__main__":
    import sys
    with_timestamps = "--with-timestamps" in sys.argv
    if with_timestamps:
        create_index_with_timestamps()
    else:
        create_index()