import frontmatter
import os
import pathlib
import uuid

import arrow
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from opensearchpy import OpenSearch, helpers

load_dotenv()

INDEX_NAME = os.getenv("INDEX_NAME")
CONNECTION_STRING = os.getenv("OPENSEARCH_SERVICE_URI")
client = OpenSearch(CONNECTION_STRING, use_ssl=True, timeout=100)

fmt = r"MMMM[\s+]D[\w+,\s+]YYYY"

# define splitter    
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=20,
    separators=[".", "!", "?", "\n"],
)

# define embeddings. These options are all the defaults and not explicitly needed.
embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-mpnet-base-v2",
    model_kwargs = {'device': 'cpu'},
    encode_kwargs = {'normalize_embeddings': False}
)

    
def os_load_data_from_file(file: pathlib.Path):
    """Chunk data, create embeddings, and index in OpenSearch."""
    frontmatter_post = frontmatter.loads(file.read_text()) # loads the metadata from the file
    base_data = {
            "_index": INDEX_NAME,
            "title": frontmatter_post["title"],
            "description": frontmatter_post["description"],
            "url": frontmatter_post["url"],
            "pub_date": arrow.get(frontmatter_post["pub_date"], fmt).date().isoformat(),
        }
    
    docs = []
    
    post_chunks = splitter.create_documents([frontmatter_post.content])
    for post_chunk in post_chunks:
        doc = {
            **base_data, 
            **{
                "_id": str(uuid.uuid4()),
                "content": post_chunk.page_content,
                "content_vector": embeddings.embed_documents([post_chunk.page_content])[0]
                }
            }
        docs.append(doc)      
    response = helpers.bulk(client, docs)
    return response