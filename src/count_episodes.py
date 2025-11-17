"""
Count unique episodes in OpenSearch index.
This script provides a workaround if title.keyword doesn't exist yet.
"""

import os
from dotenv import load_dotenv
from opensearchpy import OpenSearch

load_dotenv()

connection_string = os.getenv("OPENSEARCH_SERVICE_URI")
index_name = os.getenv("INDEX_NAME", "embedded_vp_transcripts")
client = OpenSearch(connection_string, use_ssl=True, timeout=100)

# Try with title.keyword first
query = {
    "size": 0,
    "query": {
        "match_all": {}
    },
    "aggs": {
        "unique_episodes": {
            "terms": {
                "field": "title.keyword",
                "size": 10000
            }
        }
    }
}

print(f"Querying index: {index_name}")
try:
    response = client.search(index=index_name, body=query)
    buckets = response.get("aggregations", {}).get("unique_episodes", {}).get("buckets", [])
    
    if buckets:
        print(f"✅ Found {len(buckets)} unique episodes")
        print("\nFirst 10 episodes:")
        for bucket in buckets[:10]:
            print(f"  - {bucket['key']}: {bucket['doc_count']} chunks")
    else:
        print("⚠️  No results found. Trying alternative approach...")
        # Alternative: get all unique titles using a different method
        # This requires fetching documents and deduplicating
        scroll_query = {
            "size": 1000,
            "_source": ["title"],
            "query": {"match_all": {}}
        }
        
        titles = set()
        response = client.search(index=index_name, body=scroll_query, scroll="2m")
        scroll_id = response.get("_scroll_id")
        
        while True:
            hits = response.get("hits", {}).get("hits", [])
            if not hits:
                break
            
            for hit in hits:
                title = hit.get("_source", {}).get("title")
                if title:
                    titles.add(title)
            
            if not scroll_id:
                break
                
            response = client.scroll(scroll_id=scroll_id, scroll="2m")
            scroll_id = response.get("_scroll_id")
        
        print(f"✅ Found {len(titles)} unique episodes (using workaround method)")
        
except Exception as e:
    print(f"❌ Error: {e}")
    raise

