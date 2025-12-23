# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Note**: This project uses [bd (beads)](https://github.com/steveyegge/beads) for issue tracking. Use `bd` commands instead of markdown TODOs. See AGENTS.md for workflow details.

## Project Overview

This is a podcast transcript management system for the Conduit Podcast. It automates:
1. Fetching episode metadata from RSS feed (relay.fm/conduit/feed)
2. Downloading and transcribing audio using MLX Whisper (Apple Silicon) or OpenAI Whisper
3. Processing transcripts with LangChain text splitters
4. Generating embeddings and storing in PostgreSQL + OpenSearch
5. Providing MCP server for semantic search and RAG applications

## Technology Stack

- **Language**: Python 3.13 (specified in `.python-version`)
- **Package Manager**: uv (see `pyproject.toml`)
- **Task Runner**: just (see `justfile`)
- **Transcription**: MLX Whisper (Apple Silicon optimized) with OpenAI Whisper fallback
- **Text Processing**: LangChain, HuggingFace embeddings (`sentence-transformers/all-mpnet-base-v2`)
- **Databases**: PostgreSQL with pgvector, OpenSearch
- **Web**: FastAPI (MCP server), feedparser (RSS parsing)
- **CLI**: Typer with Rich
- **Code Quality**: Ruff, pytest

## Key Architecture Patterns

### RSS Feed Strategy
The codebase uses `feedparser` to extract episode metadata from the Conduit RSS feed (`https://www.relay.fm/conduit/feed`), eliminating fragile web scraping. See `src/rss_feed.py`:
- `fetch_latest_episode_number()` - Get latest episode number
- `fetch_episode_by_number(n)` - Get specific episode metadata
- Episode numbers are extracted from titles using pattern: `"114: Title" -> 114`

### Hybrid Transcription Backend
`src/transcriber.py` implements a strategy pattern:
- **HybridTranscriber**: Tries MLX Whisper first (fast on Apple Silicon), falls back to OpenAI Whisper
- **MLXTranscriber**: Uses `mlx-whisper` for hardware-accelerated transcription
- **WhisperTranscriber**: Uses standard `openai-whisper` for CPU/GPU
- Configurable via `prefer_mlx` flag (default: True)
- Supported models: tiny, base, small, medium, large

### Transcript Storage Format
Transcripts are markdown files with YAML frontmatter:
```yaml
---
title: <episode_number> <episode_title>
description: <episode_description>
url: <episode_url>
pub_date: <publication_date>
---
<chunked_transcribed_content>
```

### Text Processing Pipeline
Consistent chunking configuration across all modules:
- Chunk size: 300 characters
- Separators: `[".", "!", "?", "\n"]`
- Keep separators at end
- Overlap: 0 in `transcribe.py`, 20 in `pg_ingest.py`

### Vector Database Architecture
**PostgreSQL** (`src/pg_ingest.py`):
- `Transcript` table: Composite PK `(podcast, episode_number)`, JSONB metadata
- `VectorChunk` table: Chunked text with 768-dimensional embeddings, FK to Transcript
- Uses SQLAlchemy ORM with pgvector extension

**OpenSearch** (`src/os_index.py`, `src/os_ingest.py`):
- KNN index with HNSW algorithm, L2 space, FAISS engine
- Fields: title, episode_number, description, url, content, content_vector, pub_date

### MCP Server
FastAPI-based server (`src/mcp_server.py`) provides:
- Vector similarity search (semantic)
- Text search (keyword)
- Episode retrieval and listing
- Integration with Claude for RAG
See `MCP_SERVER.md` for full API documentation.

## Environment Setup

### Installation
```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies and create venv
uv sync

# Load environment (choose one)
direnv allow              # If using direnv
source .envrc             # Manual load
```

### Required Environment Variables
- `POSTGRES_SERVICE_URI` - PostgreSQL connection string
- `OPENSEARCH_SERVICE_URI` - OpenSearch connection string
- `POSTGRES_DB_NAME` - Database name (default: "transcripts")
- `POSTGRES_VECTOR_DB_NAME` - Vector table name
- `INDEX_NAME` - OpenSearch index name

**Note**: `quick_upload.py` uses `AIVEN_POSTGRES_SERVICE_URI` (not `POSTGRES_SERVICE_URI`)

## Common Commands

All commands use `uv run` for isolation. Omit if venv is activated via `source .venv/bin/activate`.

### Transcription
```bash
# Latest episode
uv run python src/transcribe.py ep

# Specific episodes
uv run python src/transcribe.py ep 100 101 102

# Range
uv run python src/transcribe.py ep --range 100-105

# All episodes (with confirmation)
uv run python src/transcribe.py ep --all

# Local audio file
uv run python src/transcribe.py file audio.mp3 --output output.txt
```

### Data Ingestion
```bash
# Load all transcripts to both databases
uv run python src/quick_upload.py files

# Load specific files
uv run python src/quick_upload.py files --file transcripts/ep1.md

# Reindex OpenSearch (destructive)
uv run python src/quick_upload.py files --reindex

# Database-specific loading
uv run python src/quick_upload.py files --pg-only
uv run python src/quick_upload.py files --os-only
```

### MCP Server
```bash
# Start server
uv run python src/mcp_server.py

# Start with auto-reload (development)
uv run uvicorn src.mcp_server:app --host 0.0.0.0 --port 8000 --reload

# Or use just recipes
just mcp-server          # Start server
just mcp-server-dev      # Auto-reload mode
just mcp-health          # Test health endpoint
```

Interactive docs: http://localhost:8000/docs

### Docker Deployment
```bash
# Setup
cp .env.docker.example .env.docker
# Edit .env.docker with passwords

# Start all services (PostgreSQL, ingestion, MCP server)
just docker-up

# View logs
just docker-logs

# Stop services
just docker-down
```

See `infra/README.md` for complete Docker documentation.

### Code Quality
```bash
# Format with ruff
just fmt

# Check linting
just lint

# Fix linting issues
just lint-fix

# Run tests
just test
```

### Just Recipes
The `justfile` provides shortcuts for common tasks:
```bash
just --list              # Show all commands
just setup               # Install dependencies
just transcribe-latest   # Transcribe latest episode
just upload              # Load all transcripts
just upload-reindex      # Load with reindex
just clean               # Remove cache artifacts
```

## Development Notes

### Episode Caching
`src/episode_cache.py` provides caching to avoid repeated RSS fetches:
- Cache stored in `.episode_cache/` (gitignored)
- Reduces load on RSS feed during development

### Important Gotchas
- **MLX Requirement**: MLX Whisper requires Apple Silicon (M1/M2/M3). On other platforms, system falls back to OpenAI Whisper.
- **First Run**: Downloads transcription model (~140MB for "base") - requires network access.
- **Destructive Operations**:
  - `pg_ingest.py` and `quick_upload.py` can drop tables
  - `--reindex` flag recreates OpenSearch index
  - Use with caution in production
- **Missing Imports**: `quick_upload.py` has missing imports (`psycopg`, `os`) at top - these need to be added if errors occur.
- **Variable Names**: `quick_upload.py` uses `AIVEN_POSTGRES_SERVICE_URI`, other scripts use `POSTGRES_SERVICE_URI`.

### Issue Tracking with bd
This project uses **bd (beads)** for all issue tracking. Do NOT create markdown TODOs. See AGENTS.md for complete workflow:
```bash
bd list                  # List all issues
bd ready                 # Show unblocked work
bd create "Title" -p 1   # Create issue
bd update <id> --status in_progress
bd close <id> --reason "Completed"
```

Always use `--json` flag for programmatic use.

## Project Structure

```
src/
  ├── transcribe.py          # Main transcription CLI
  ├── transcriber.py         # Hybrid MLX/Whisper backend
  ├── rss_feed.py           # RSS feed parsing (replaces web scraping)
  ├── episode_cache.py      # Episode metadata caching
  ├── quick_upload.py       # Unified data loader (PostgreSQL + OpenSearch)
  ├── pg_ingest.py          # PostgreSQL ingestion with embeddings
  ├── os_ingest.py          # OpenSearch ingestion
  ├── os_index.py           # OpenSearch index management
  ├── mcp_server.py         # MCP server for search/RAG
  └── download_audio_file.py # Audio download utility

transcripts/              # Generated markdown with frontmatter
infra/                    # Docker infrastructure
  ├── README.md           # Docker documentation
  └── init-db.sql         # PostgreSQL initialization

docker-compose.yml        # Multi-service Docker setup
Dockerfile.ingestion      # Ingestion container
Dockerfile.mcp            # MCP server container
justfile                  # Task runner recipes
pyproject.toml            # Dependencies and config
```

## Related Documentation

- `MCP_SERVER.md` - Complete MCP server API documentation
- `AGENTS.md` - AI agent instructions for bd issue tracking
- `infra/README.md` - Docker deployment guide
- `README.md` - User-facing project documentation
