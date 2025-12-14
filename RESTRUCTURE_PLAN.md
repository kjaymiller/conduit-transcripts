# Project Structure Design

## Current Analysis

Based on the codebase analysis, I've identified the following structure:

### Apps (2 services)
1. **transcribe** - Audio transcription and ingestion API
2. **mcp** - Search and RAG API server  

### CLI (1 tool)
1. **cli** - Local operations tool

### Shared Components
1. **Database models** - SQLAlchemy models for PostgreSQL/OpenSearch
2. **Transcription utilities** - Core transcription classes and audio processing
3. **Configuration** - Environment and database configuration
4. **Utilities** - Common helpers for text, files, logging

## Directory Structure

```
conduit-transcripts/
├── apps/
│   ├── transcribe/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI app entry point
│   │   ├── api.py            # API endpoints (from ingestion_api.py)
│   │   └── models.py         # Request/response models
│   └── mcp/
│       ├── __init__.py
│       ├── main.py           # FastAPI app entry point  
│       ├── server.py         # MCP server logic (from mcp_server.py)
│       └── models.py         # Request/response models
├── cli/
│   ├── __init__.py
│   └── main.py               # CLI entry point using Typer
├── conduit_transcripts/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py       # Environment configuration
│   ├── models/
│   │   ├── __init__.py
│   │   ├── transcript.py     # SQLAlchemy models (from pg_ingest.py)
│   │   └── api.py           # Pydantic models
│   ├── database/
│   │   ├── __init__.py
│   │   ├── postgres.py      # PostgreSQL operations (from pg_ingest.py)
│   │   └── opensearch.py    # OpenSearch operations (from os_ingest.py)
│   ├── transcription/
│   │   ├── __init__.py
│   │   ├── core.py          # Transcriber classes (from transcriber.py)
│   │   ├── audio.py         # Audio download utilities
│   │   └── metadata.py      # URL finding (from url_finder.py)
│   ├── search/
│   │   ├── __init__.py
│   │   ├── embeddings.py    # Embedding utilities
│   │   └── queries.py       # Search query builders
│   └── utils/
│       ├── __init__.py
│       ├── text.py          # Text processing
│       ├── logging.py       # Logging setup
│       └── files.py         # File utilities
├── tests/
├── transcripts/
└── pyproject.toml
```

## Benefits
- **Separation of Concerns**: Each app has a single responsibility
- **Reusability**: Shared module prevents code duplication  
- **Independent Deployment**: Apps can be deployed separately
- **Maintainability**: Clear structure makes code easier to understand
- **Testability**: Smaller modules are easier to test