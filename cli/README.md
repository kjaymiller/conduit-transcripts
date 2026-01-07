# CLI Access for Conduit Transcripts

The CLI is built with Click and can be accessed directly through the unified Docker container.

## Quick Start

```bash
# Start the services
docker compose up -d

# Run CLI commands
docker compose run --rm app python -m cli.main [command] [options]

# Examples:
docker compose run --rm app python -m cli.main --help
docker compose run --rm app python -m cli.main list
docker compose run --rm app python -m cli.main search "query"
docker compose run --rm app python -m cli.main search "query" --vector
docker compose run --rm app python -m cli.main status 123
docker compose run --rm app python -m cli.main ingest
docker compose run --rm app python -m cli.main transcribe 123
```

## CLI Commands

- `search` - Search transcripts
  - `--vector` - Use vector search
  - `--title` - Search by title  
  - `--limit` - Maximum results

- `list` - List episodes
  - `--limit` - Maximum episodes to show

- `status` - Check episode status
  - Requires episode number

- `ingest` - Ingest transcript files
  - `--dir` - Directory to ingest (default: transcripts)
  - `--reindex` - Recreate tables

- `transcribe` - Transcribe an episode
  - Supports ranges: `100`, `100-105`, `latest`, `all`
  - `--model` - Model size
  - `--ingest/--no-ingest` - Ingest after transcription

- `transcribe-file` - Transcribe local audio file
  - `--output` - Output file path

## Environment Variables

The CLI inherits all environment variables from the app service:
- `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`
- `OLLAMA_BASE_URL`, `LLM_MODEL`, `EMBEDDING_MODEL`

## Unified Architecture

The CLI, API, Web UI, and MCP all use the same:
- Codebase and dependencies
- Database connections  
- Business logic through shared functions
- Container environment

This ensures consistent behavior across all interfaces.