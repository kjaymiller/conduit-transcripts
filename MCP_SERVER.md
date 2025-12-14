# Conduit Transcript MCP Server

A FastAPI-based MCP (Model Context Protocol) server for searching and retrieving Conduit podcast transcripts using semantic vector search and text matching.

## Features

- **Vector Similarity Search**: Semantic search using 768-dimensional embeddings from `sentence-transformers/all-mpnet-base-v2`
- **Text Search**: Case-insensitive keyword matching across transcript content
- **Episode Retrieval**: Get full transcripts and metadata for specific episodes
- **Episode Listing**: Browse all available episodes with pagination
- **Health Checks**: Monitor server and database connectivity
- **RESTful API**: Clean, documented endpoints with Pydantic validation

## API Endpoints

### Root
**GET /** - Server information and available endpoints

### Health Check
**GET /health** - Check server health and database connectivity

**Response:**
```json
{
  "status": "healthy",
  "database": "connected",
  "embedding_model": "sentence-transformers/all-mpnet-base-v2"
}
```

### Vector Search
**GET /search/vector** - Semantic search using vector embeddings

**Parameters:**
- `query` (required): Search query text
- `limit` (optional, default=10): Maximum results (1-100)
- `similarity_threshold` (optional, default=0.0): Minimum similarity score (0.0-1.0)

**Example:**
```bash
curl "http://localhost:8000/search/vector?query=python%20testing&limit=5"
```

**Response:**
```json
{
  "query": "python testing",
  "results": [
    {
      "episode_number": 42,
      "podcast": "Conduit",
      "title": "42 Testing Best Practices",
      "description": "Discussion about testing in Python",
      "url": "https://conduit.fm/episodes/42",
      "pub_date": "2024-01-15",
      "content_snippet": "When it comes to testing in Python...",
      "similarity_score": 0.8523,
      "chunk_id": 1234
    }
  ],
  "total_results": 5,
  "search_type": "vector_similarity"
}
```

### Text Search
**GET /search/text** - Keyword-based text search

**Parameters:**
- `query` (required): Search query text
- `limit` (optional, default=10): Maximum results (1-100)

**Example:**
```bash
curl "http://localhost:8000/search/text?query=machine%20learning&limit=10"
```

**Response:**
```json
{
  "query": "machine learning",
  "results": [
    {
      "episode_number": 38,
      "podcast": "Conduit",
      "title": "38 Intro to Machine Learning",
      "description": "Getting started with ML",
      "url": "https://conduit.fm/episodes/38",
      "pub_date": "2024-01-10",
      "content_snippet": "Machine learning is a subset of...",
      "similarity_score": null,
      "chunk_id": 1180
    }
  ],
  "total_results": 10,
  "search_type": "text_match"
}
```

### Get Episode
**GET /episode/{episode_number}** - Get full transcript for a specific episode

**Parameters:**
- `episode_number` (path parameter): Episode number
- `podcast` (optional, default="Conduit"): Podcast name

**Example:**
```bash
curl "http://localhost:8000/episode/42"
```

**Response:**
```json
{
  "episode_number": 42,
  "podcast": "Conduit",
  "metadata": {
    "title": "42 Testing Best Practices",
    "description": "Discussion about testing",
    "url": "https://conduit.fm/episodes/42",
    "pub_date": "2024-01-15",
    "content": "Full transcript text..."
  },
  "content": "Full transcript text...",
  "chunks_count": 45
}
```

### List Episodes
**GET /episodes** - List all available episodes

**Parameters:**
- `podcast` (optional, default="Conduit"): Podcast name
- `limit` (optional, default=100): Maximum episodes (1-1000)
- `offset` (optional, default=0): Pagination offset

**Example:**
```bash
curl "http://localhost:8000/episodes?limit=20&offset=0"
```

**Response:**
```json
{
  "podcast": "Conduit",
  "total_episodes": 150,
  "episodes": [
    {
      "episode_number": 150,
      "title": "150 Latest Episode",
      "description": "The newest episode",
      "url": "https://conduit.fm/episodes/150",
      "pub_date": "2024-03-01"
    }
  ],
  "limit": 20,
  "offset": 0
}
```

## Running the Server

### Local Development

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Set up environment variables:**
   ```bash
   export POSTGRES_HOST=localhost
   export POSTGRES_PORT=5432
   export POSTGRES_DB=transcripts
   export POSTGRES_USER=postgres
   export POSTGRES_PASSWORD=your_password
   ```

   Or use your existing Aiven connection:
   ```bash
   source .envrc  # Loads AIVEN_POSTGRES_SERVICE_URI
   ```

3. **Run the server:**
   ```bash
   uv run python src/mcp_server.py
   ```

   Or with uvicorn directly:
   ```bash
   uv run uvicorn src.mcp_server:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Access the API:**
   - Interactive docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc
   - OpenAPI spec: http://localhost:8000/openapi.json

### Docker Deployment

Using the Docker Compose setup:

```bash
# Start all services (database, ingestion, MCP server)
just docker-up

# View logs
just docker-logs

# Access the server
curl http://localhost:8000/health
```

## Environment Variables

The server supports flexible configuration for different deployment scenarios:

### Docker Environment
- `POSTGRES_HOST` - Database host (default: "localhost")
- `POSTGRES_PORT` - Database port (default: "5432")
- `POSTGRES_DB` - Database name (default: "transcripts")
- `POSTGRES_USER` - Database user (default: "postgres")
- `POSTGRES_PASSWORD` - Database password (default: "postgres")

### Local Development
- `AIVEN_POSTGRES_SERVICE_URI` - Full Aiven connection string (overrides individual settings)

## Search Strategies

### When to Use Vector Search
- **Semantic queries**: Find conceptually similar content even if keywords don't match
- **Natural language**: Search using phrases like "how to deploy applications"
- **Topic discovery**: Find all episodes discussing a broad topic
- **Best for**: Exploratory search, understanding context, finding related concepts

### When to Use Text Search
- **Exact terms**: Find specific keywords or phrases
- **Names and titles**: Search for person names, product names, etc.
- **Code snippets**: Find exact function names or code patterns
- **Best for**: Precise matching, known keywords, specific references

## Integration with Claude

This server is designed to be used as an MCP server for Claude Code and other Claude integrations:

1. **Semantic Search**: Claude can query transcripts using natural language
2. **Context Retrieval**: Fetch relevant transcript chunks for RAG applications
3. **Episode Discovery**: Browse and explore podcast content programmatically
4. **Summarization**: Combine search results with Claude's summarization capabilities

### Example Claude Workflow

```python
# 1. Search for relevant content
response = requests.get(
    "http://localhost:8000/search/vector",
    params={"query": "python type hints", "limit": 5}
)
results = response.json()

# 2. Extract context for Claude
context = "\n\n".join([
    f"Episode {r['episode_number']}: {r['content_snippet']}"
    for r in results['results']
])

# 3. Use with Claude for summarization or analysis
# (Pass context to Claude API)
```

## Performance Considerations

- **Embedding Generation**: First query may be slower as the model loads (~2-3 seconds)
- **Vector Search**: Fast with IVFFlat index on 768-dimensional vectors
- **Connection Pooling**: SQLAlchemy manages connection pool automatically
- **Caching**: Consider adding Redis for frequently accessed episodes
- **Scaling**: Can be deployed as multiple instances behind a load balancer

## Monitoring

The server logs all queries and errors:

```bash
# View logs in Docker
just docker-logs-service mcp-server

# Local development logs show:
# - Query text and parameters
# - Number of results found
# - Database connection status
# - Errors and stack traces
```

## Error Handling

The API returns standard HTTP status codes:

- **200 OK**: Success
- **404 Not Found**: Episode doesn't exist
- **422 Unprocessable Entity**: Invalid parameters
- **500 Internal Server Error**: Database or server error
- **503 Service Unavailable**: Health check failed

## Development

### Running Tests

```bash
# Run all tests
just test

# Test specific endpoint
curl http://localhost:8000/health
```

### Adding New Endpoints

1. Define Pydantic models for request/response
2. Create endpoint with type hints
3. Add database query logic
4. Update documentation in this file

### Code Quality

```bash
# Format code
just fmt

# Check linting
just lint

# Fix linting issues
just lint-fix
```

## Related Issues

- **MCP Server Implementation**: conduit-transcripts-ikr
- **Database Setup**: conduit-transcripts-h6e
- **Ingestion Pipeline**: conduit-transcripts-0mt
- **Docker Infrastructure**: conduit-transcripts-1h3

## License

MIT
