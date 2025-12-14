# GitHub Copilot Instructions for Conduit Transcripts

## Project Overview

**conduit-transcripts** is a podcast transcript management system for the Conduit Podcast. It automates fetching, downloading, transcribing, and storing podcast episode data for RAG applications.

**Key Features:**
- Automated episode metadata extraction from Conduit website
- MLX Whisper transcription (Apple Silicon optimized) with OpenAI Whisper fallback
- Vector embeddings and semantic search
- PostgreSQL + pgvector and OpenSearch storage
- LangChain text processing and chunking

## Tech Stack

- **Language**: Python 3.12+
- **Package Manager**: uv
- **Task Runner**: just
- **Audio Processing**: MLX Whisper, OpenAI Whisper
- **Text Processing**: LangChain, HuggingFace embeddings
- **Databases**: PostgreSQL (pgvector), OpenSearch
- **CLI Framework**: Typer with Rich
- **ORM**: SQLAlchemy

## Coding Guidelines

### Testing
- Run tests with `just test` or `uv run pytest -v`
- Use `just test-coverage` for coverage reports
- Always test transcription changes with sample audio

### Code Style
- Format with `just fmt` (uses ruff)
- Lint with `just lint` (uses ruff)
- Run `just check` before committing
- Follow existing patterns in `src/` directory

### Git Workflow
- Always commit `.beads/issues.jsonl` with code changes
- Run `bd sync` at end of work sessions
- Install git hooks: `bd hooks install`

## Issue Tracking with bd

**CRITICAL**: This project uses **bd** for ALL task tracking. Do NOT create markdown TODO lists.

### Essential Commands

```bash
# Find work
bd ready --json                    # Unblocked issues
bd stale --days 30 --json          # Forgotten issues

# Create and manage
bd create "Title" -t bug|feature|task -p 0-4 --json
bd create "Subtask" --parent <epic-id> --json  # Hierarchical subtask
bd update <id> --status in_progress --json
bd close <id> --reason "Done" --json

# Search
bd list --status open --priority 1 --json
bd show <id> --json

# Sync (CRITICAL at end of session!)
bd sync  # Force immediate export/commit/push
```

### Workflow

1. **Check ready work**: `bd ready --json`
2. **Claim task**: `bd update <id> --status in_progress`
3. **Work on it**: Implement, test, document
4. **Discover new work?** `bd create "Found bug" -p 1 --deps discovered-from:<parent-id> --json`
5. **Complete**: `bd close <id> --reason "Done" --json`
6. **Sync**: `bd sync` (flushes changes to git immediately)

### Priorities

- `0` - Critical (security, data loss, broken builds)
- `1` - High (major features, important bugs)
- `2` - Medium (default, nice-to-have)
- `3` - Low (polish, optimization)
- `4` - Backlog (future ideas)

## Project Structure

```
conduit-transcripts/
├── src/                 # Main application code
│   ├── transcribe.py    # Main CLI for transcription workflow
│   ├── transcriber.py   # Transcription backend (MLX/Whisper)
│   ├── url_finder.py    # Web scraping for Conduit website
│   ├── quick_upload.py  # Unified data loading (PostgreSQL + OpenSearch)
│   ├── pg_ingest.py     # PostgreSQL ingestion with embeddings
│   ├── os_ingest.py     # OpenSearch ingestion
│   └── os_index.py      # OpenSearch index setup
├── transcripts/         # Generated markdown with frontmatter
├── infra/               # Infrastructure config
├── justfile             # Task runner recipes
└── .beads/
    ├── beads.db         # SQLite database (DO NOT COMMIT)
    └── issues.jsonl     # Git-synced issue storage
```

## Available Resources

### Common Commands (via just)

```bash
# Transcription
just transcribe-latest              # Transcribe latest episode
just transcribe-range 100 105       # Transcribe episodes 100-105

# Data ingestion
just upload                         # Upload to both databases
just upload-pg-only                 # PostgreSQL only
just upload-os-only                 # OpenSearch only
just upload-reindex                 # Recreate OpenSearch index

# Code quality
just fmt                            # Format with ruff
just lint                           # Lint with ruff
just check                          # Run all checks
just test                           # Run tests
```

### MCP Server (Recommended)
Use the beads MCP server for native function calls:
- Install: `pip install beads-mcp`
- Functions: `mcp__beads__ready()`, `mcp__beads__create()`, etc.

### Key Documentation
- **AGENTS.md** - AI agent workflow guide
- **CLAUDE.md** - Project instructions for Claude Code
- **CONTRIBUTING.md** - PR requirements and guidelines
- **README.md** - User-facing documentation

## Environment Setup

Required environment variables (see `.envrc`):
- `AIVEN_POSTGRES_SERVICE_URI` - PostgreSQL connection
- `OPENSEARCH_SERVICE_URI` - OpenSearch connection
- `POSTGRES_DB_NAME` - Database name
- `INDEX_NAME` - OpenSearch index name

Load with `direnv allow` or `source .envrc`.

## CLI Help

Run `bd <command> --help` to see all available flags for any command.
For example: `bd create --help` shows `--parent`, `--deps`, `--assignee`, etc.

## Important Rules

- ✅ Use bd for ALL task tracking
- ✅ Always use `--json` flag for programmatic use
- ✅ Run `bd sync` at end of sessions
- ✅ Use `just` commands when available
- ✅ Run `bd <cmd> --help` to discover available flags
- ✅ Test with sample audio files before processing all episodes
- ❌ Do NOT create markdown TODO lists
- ❌ Do NOT commit `.beads/beads.db` (JSONL only)
- ❌ Do NOT commit `.envrc` (contains secrets)

---

**For detailed workflows and advanced features, see [AGENTS.md](../AGENTS.md)**
