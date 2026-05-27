# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Conduit Transcripts is a podcast transcript management system for the [Conduit Podcast](https://relay.fm/conduit). It provides automated transcription using NVIDIA Parakeet (NeMo), vector search with pgvector, and multiple interfaces (CLI, REST API, MCP Server).

## Development Commands

Tools and tasks are managed by [mise](https://mise.jdx.dev/) (`mise.toml`). Run `mise tasks` to list every task.

```bash
# Setup
mise install                     # Install pinned python/uv/ruff
mise run setup                   # uv sync

# Testing
mise run test                    # uv run pytest -v

# Linting and formatting
mise run fmt                     # Format with ruff
mise run lint                    # Lint with ruff
mise run check                   # Run all quality checks

# CLI commands (local)
mise run transcribe <episode>    # Transcribe episode(s)
mise run search "query"          # Text search
mise run search-vector "query"   # Semantic search
mise run list                    # List episodes
mise run ingest                  # Ingest transcripts to DB

# Docker (preferred for full stack)
mise run docker-up               # Start all services
docker compose run --rm app python -m cli.main [command]
mise run docker-logs             # View logs
```

## Architecture

The project is a uv workspace with two packages:

### Root Package (`conduit-transcription`)

- **app/**: FastAPI web application
  - `main.py`: FastAPI app with web UI routes, mounts MCP server at `/mcp`
  - `api/routes.py`: REST API endpoints under `/api/v1`
  - `mcp/server.py`: MCP server with `search_transcripts`, `get_episode`, `list_episodes` tools
- **cli/**: Click-based CLI (`conduit` command)
  - Commands: `search`, `transcribe`, `transcribe-file`, `ingest`, `list`, `status`, `download`
  - Episode arguments support: single number, ranges (`100-105`), `latest`, `all`, comma-separated

### Workspace Member (`podcast-transcription-core`)

Located in `podcast_transcription/podcast_transcription_core/`:

- **config/**: Settings from environment variables (Pydantic-style class)
- **database/postgres.py**: `VectorDatabase` class - SQLAlchemy + pgvector operations, chunking, embeddings
- **models/**: SQLAlchemy models (`Podcast`, `Transcript`, `VectorChunk`)
- **transcription/**: NVIDIA Parakeet transcriber (`ParakeetTranscriber`)
- **utils/**: RSS feed parsing, Valkey queue operations, text utilities
- **chat/rag.py**: RAG-based chat with episodes

### Background Worker

`podcast_transcription/worker.py`: Valkey queue consumer for async transcription jobs

## Key Patterns

**Database Access**: Always use `VectorDatabase` from `podcast_transcription_core.database.postgres`:

```python
from podcast_transcription_core.database.postgres import VectorDatabase
db = VectorDatabase()
session = db.Session()
# ... use session ...
session.close()
```

**Embeddings**: Configurable via `EMBEDDING_PROVIDER` env var (`ollama` or `huggingface`)

**Transcription Jobs**: Enqueued to Valkey via `enqueue_transcription_job()`, processed by worker

## Environment Variables

Key settings (see `podcast_transcription_core/config/__init__.py`):

- `POSTGRES_*`: Database connection
- `VALKEY_HOST`, `VALKEY_PORT`: Queue connection
- `EMBEDDING_PROVIDER`: `ollama` (default) or `huggingface`
- `EMBEDDING_MODEL`: Model name (default: `nomic-embed-text`)
- `OLLAMA_BASE_URL`: Ollama API URL
- `TRANSCRIPTION_MODEL`: Parakeet model (default: `nvidia/parakeet-rnnt-1.1b`)

Env vars load automatically from `.env` via `mise` when you enter the project directory. Copy `.env.docker.example` to `.env` and fill in secrets.

## Docker Services

- **postgres**: PostgreSQL 16 with pgvector extension
- **valkey**: Redis-compatible queue for transcription jobs
- **app**: FastAPI server (port 8000, includes MCP at `/mcp`)
- **worker**: Background transcription processor

## Issue Tracking

For all of the things that you want to do, there should be an issue. This project uses tea so use the tea command tea issue to create a new issue for the problem. This can be used in conjunction with your internal task system.

## Development Strategy

Create a test to verify issues as they occur. Your tests should pass before the item is completed

## PR

You should NEVER apply fixes to main. Create a new worktree as a subfolder in the project under ./worktrees (which should be .gitignored). Submit a PR when a task is complete. PRs should solve simple and clear issues.
