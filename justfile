# conduit-transcripts justfile
# Common commands for the podcast transcript management system

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

# Transcription Commands

# Transcribe the latest episode
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

# Format code with black
fmt:
    uv run black .

# Check code with ruff
lint:
    uv run ruff check .

# Fix linting issues with ruff
lint-fix:
    uv run ruff check . --fix

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

# Help Commands

# Show help for transcribe.py
@help-transcribe:
    uv run python src/transcribe.py --help

# Show help for quick_upload.py
@help-upload:
    uv run python src/quick_upload.py --help
