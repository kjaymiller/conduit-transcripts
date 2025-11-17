"""
Add keyword subfield to title field in existing OpenSearch index.
This allows aggregations on the title field.
"""

import os
from dotenv import load_dotenv
from opensearchpy import OpenSearch

load_dotenv()

connection_string = os.getenv("OPENSEARCH_SERVICE_URI")
index_name = os.getenv("INDEX_NAME", "embedded_vp_transcripts")
client = OpenSearch(connection_string, use_ssl=True, timeout=100)

# Update mapping to add keyword subfield to title
mapping_update = {
    "properties": {
        "title": {
            "type": "text",
            "fields": {
                "keyword": {"type": "keyword"}
            }
        }
    }
}

print(f"Updating mapping for index: {index_name}")
try:
    response = client.indices.put_mapping(
        index=index_name,
        body=mapping_update
    )
    print(f"✅ Mapping updated successfully: {response}")
    print("\nNote: The keyword subfield will only be available for new documents.")
    print("To make it available for existing documents, you'll need to reindex.")
except Exception as e:
    print(f"❌ Error updating mapping: {e}")
    raise

