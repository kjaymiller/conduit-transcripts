# conduit-transcripts justfile
# Common commands for podcast transcript management system

set shell := ["bash", "-c"]

# Default recipe - show available commands
@default:
    just --list

# Setup and Installation
@setup:
    echo "Installing dependencies with uv..."
    uv sync
    echo "Setup complete! Next steps:"
    echo "  1. direnv allow  (or source .envrc)"
    echo "  2. See 'just --list' for available commands"

# Environment
@env-load:
    source .envrc

# CLI Commands (using new modular structure)

# Search transcripts
cli-search QUERY:
    uv run python -m cli.main search "{{QUERY}}"

# Vector search with CLI
cli-search-vector QUERY LIMIT="10":
    uv run python -m cli.main search "{{QUERY}}" --vector --limit {{LIMIT}}

# Check episode status
cli-status EPISODE:
    uv run python -m cli.main status {{EPISODE}}

# List episodes
cli-list LIMIT="20":
    uv run python -m cli.main list --limit {{LIMIT}}

# Transcribe episode via CLI
cli-transcribe EPISODE:
    uv run python -m cli.main transcribe {{EPISODE}}

# Ingest transcript file via CLI
cli-ingest FILE:
    uv run python -m cli.main ingest {{FILE}}

# Legacy Transcription Commands (using old src structure)

# Transcribe latest episode
transcribe-latest:
    uv run python src/transcribe.py ep

# Transcribe specific episodes (e.g., just transcribe-episodes 100 101 102)
transcribe-episodes EPISODES:
    uv run python src/transcribe.py ep {{EPISODES}}

# Transcribe episodes in a range (e.g., just transcribe-range 100 105)
transcribe-range START END:
    uv run python src/transcribe.py ep --range {{START}}-{{END}}

# Transcribe all episodes (with confirmation)
transcribe-all:
    uv run python src/transcribe.py ep --all

# Transcribe a local audio file
transcribe-file FILE OUTPUT:
    uv run python src/transcribe.py file {{FILE}} --output {{OUTPUT}}

# Data Ingestion Commands

# Load all transcript files into both PostgreSQL and OpenSearch
upload:
    uv run python src/quick_upload.py files

# Load specific transcript files
upload-files FILES:
    uv run python src/quick_upload.py files {{FILES}}

# Load transcripts with OpenSearch reindexing
upload-reindex:
    uv run python src/quick_upload.py files --reindex

# Load transcripts to PostgreSQL only
upload-pg-only:
    uv run python src/quick_upload.py files --pg-only

# Load transcripts to OpenSearch only
upload-os-only:
    uv run python src/quick_upload.py files --os-only

# Index Management

# Create or recreate OpenSearch index (destructive - use with caution)
index-recreate:
    uv run python src/os_index.py

# Code Quality Commands

# Format code with ruff
fmt:
    uv tool run ruff format .

# Check code with ruff
lint:
    uv tool run ruff check .

# Fix linting issues with ruff
lint-fix:
    uv tool run ruff check . --fix

# Run all quality checks
check: lint
    echo "✓ Linting passed"

# Testing Commands

# Run tests
test:
    uv run pytest -v

# Run tests with coverage
test-coverage:
    uv run pytest --cov=src --cov-report=html

# Utility Commands

# Show Python version
@py-version:
    python --version

# Show uv version
@uv-version:
    uv --version

# Update dependencies
update-deps:
    uv lock --upgrade
    uv sync

# Clean up Python cache and build artifacts
@clean:
    find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete
    find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
    find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    echo "✓ Cleaned up cache and build artifacts"

# Issue Tracking (bd/beads)

# List all issues
@bd-list:
    bd list

# Show ready work (unblocked issues)
@bd-ready:
    bd ready

# Show issue details (e.g., just bd-show conduit-transcripts-66x)
@bd-show ISSUE_ID:
    bd show {{ISSUE_ID}}

# Create a new issue (e.g., just bd-create "Fix bug" bug 1)
@bd-create TITLE TYPE PRIORITY:
    bd create "{{TITLE}}" -t {{TYPE}} -p {{PRIORITY}} --json

# Update issue status to in_progress (e.g., just bd-start conduit-transcripts-66x)
@bd-start ISSUE_ID:
    bd update {{ISSUE_ID}} --status in_progress --json

# Close an issue (e.g., just bd-close conduit-transcripts-66x "Completed")
@bd-close ISSUE_ID REASON:
    bd close {{ISSUE_ID}} --reason "{{REASON}}" --json

# MCP Server Commands

# Start MCP server locally
mcp-server:
    uv run python src/mcp_server.py

# Start MCP server with auto-reload (development mode)
mcp-server-dev:
    uv run uvicorn src.mcp_server:app --host 0.0.0.0 --port 8000 --reload

# Test MCP server health
mcp-health:
    curl http://localhost:8000/health

# Test vector search (requires server running)
mcp-search-vector QUERY:
    curl "http://localhost:8000/search/vector?query={{QUERY}}&limit=5"

# Test text search (requires server running)
mcp-search-text QUERY:
    curl "http://localhost:8000/search/text?query={{QUERY}}&limit=5"

# Docker Commands

# Build all Docker images
docker-build:
    docker-compose build

# Start all Docker services (database, ingestion, MCP server)
docker-up:
    docker-compose --env-file .env.docker up -d

# Start services and follow logs
docker-up-logs:
    docker-compose --env-file .env.docker up

# Stop all Docker services
docker-down:
    docker-compose down

# Stop services and remove volumes (destructive - deletes database data)
docker-down-volumes:
    docker-compose down -v

# View logs for all services
docker-logs:
    docker-compose logs -f

# View logs for specific service (e.g., just docker-logs-service postgres)
docker-logs-service SERVICE:
    docker-compose logs -f {{SERVICE}}

# Restart all services
docker-restart:
    docker-compose restart

# Run ingestion manually
docker-ingest:
    docker-compose run --rm ingestion uv run conduit ingest --pg-only

# Access PostgreSQL shell
docker-psql:
    docker-compose exec postgres psql -U postgres -d transcripts

# Show Docker service status
docker-status:
    docker-compose ps

# Rebuild and restart services (useful after code changes)
docker-rebuild: docker-down docker-build docker-up

# Help Commands

# Show help for transcribe.py
@help-transcribe:
    uv run python src/transcribe.py --help

# Show help for quick_upload.py
@help-upload:
    uv run python src/quick_upload.py --help

# Show help for bd
@help-bd:
    bd --help

# Show help for MCP server commands
@help-mcp:
    echo "MCP Server Commands:"
    echo "  mcp-server          - Start MCP server locally"
    echo "  mcp-server-dev      - Start server with auto-reload"
    echo "  mcp-health          - Test server health"
    echo "  mcp-search-vector   - Test vector search"
    echo "  mcp-search-text     - Test text search"

# Show help for Docker commands
@help-docker:
    echo "Docker Commands:"
    echo "  docker-build         - Build all Docker images"
    echo "  docker-up            - Start all services in background"
    echo "  docker-up-logs       - Start all services with logs"
    echo "  docker-down          - Stop all services"
    echo "  docker-down-volumes  - Stop services and delete data"
    echo "  docker-logs          - View logs for all services"
    echo "  docker-logs-service  - View logs for specific service"
    echo "  docker-restart       - Restart all services"
    echo "  docker-ingest        - Run ingestion manually"
    echo "  docker-psql          - Access PostgreSQL shell"
    echo "  docker-status        - Show service status"
    echo "  docker-rebuild       - Rebuild and restart all services"
