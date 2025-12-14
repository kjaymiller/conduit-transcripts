# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Note**: This project uses [bd (beads)](https://github.com/steveyegge/beads) for issue tracking. Use `bd` commands instead of markdown TODOs. See AGENTS.md for workflow details.

## Project Overview

This is a podcast transcript management system for the Conduit Podcast. It automates the process of:
1. Fetching episode metadata from the Conduit website
2. Downloading audio files
3. Transcribing audio using OpenAI Whisper
4. Processing and chunking transcripts
5. Generating embeddings for vector search
6. Storing data in PostgreSQL and OpenSearch for RAG applications

## Technology Stack

- **Language**: Python 3.12+ (specified in `.python-version`)
- **Package Manager**: uv (see `pyproject.toml` for dependencies)
- **Task Runner**: just (see `justfile` for recipes)
- **Audio Processing**: MLX Whisper (Apple Silicon optimized) with OpenAI Whisper fallback
- **Text Processing**: LangChain text splitters and HuggingFace embeddings
- **Databases**: PostgreSQL with pgvector extension, OpenSearch
- **Web Scraping**: BeautifulSoup, httpx
- **CLI Framework**: Typer with Rich for progress and output
- **ORM**: SQLAlchemy with pgvector support
- **Environment Management**: python-dotenv, direnv (`.envrc`)
- **Code Quality**: Ruff (formatting and linting), pytest (testing)

## Directory Structure

- `src/` - Main application code
  - `transcribe.py` - Main CLI for episode transcription workflow
  - `transcriber.py` - Transcription backend abstraction (MLX/Whisper with fallback logic)
  - `url_finder.py` - Web scraping for Conduit website (episode metadata, audio URLs)
  - `quick_upload.py` - Unified data loading script for both OpenSearch and PostgreSQL
  - `pg_ingest.py` - PostgreSQL data processing with embeddings and vector storage
  - `os_ingest.py` - OpenSearch data ingestion (incomplete/skeleton)
  - `os_index.py` - OpenSearch index creation and setup
  - `download_audio_file.py` - Audio file download utility
- `transcripts/` - Generated markdown files with frontmatter metadata and transcribed content
- `infra/` - Infrastructure configuration files
- `justfile` - Task runner recipes for common commands
- `pyproject.toml` - Project metadata and dependencies
- `uv.lock` - Locked dependency versions for reproducible builds

## Setup

### Installation with uv

This project uses `uv` for fast, reliable Python package management. To get started:

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies and create virtual environment
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

### Environment Variables

Load the environment configuration:
```bash
# Using direnv (recommended)
direnv allow

# Or manually source the .envrc file
source .envrc
```

## Key Architecture Patterns

### Transcription Backend Strategy Pattern
The `transcriber.py` module implements a hybrid transcription strategy:
- **HybridTranscriber**: Tries MLX Whisper first (Apple Silicon optimized), falls back to OpenAI Whisper
- **MLXTranscriber**: Uses `mlx-whisper` for fast, hardware-accelerated transcription on Apple Silicon
- **WhisperTranscriber**: Uses standard `openai-whisper` for CPU/GPU transcription
- Configurable via `prefer_mlx` flag (default: True)
- Both backends support model sizes: tiny, base, small, medium, large

### Frontmatter Posts
Transcripts are stored as markdown files with YAML frontmatter containing metadata:
```yaml
---
title: <episode_number> <episode_title>
description: <episode_description>
url: <episode_url>
pub_date: <publication_date>
---
<transcribed_content>
```

### Text Processing Pipeline
All modules use consistent text splitting configuration:
- Chunk size: 300 characters
- Separators: `[".", "!", "?", "\n"]`
- Overlap: 20 characters (varies: 0 in transcribe.py, 20 in others)
- Keep separators at end

### Vector Embeddings
- Model: `sentence-transformers/all-mpnet-base-v2` (768-dimensional vectors)
- Device: CPU (configurable in embedding initialization)
- Used for semantic search in both PostgreSQL and OpenSearch

### Database Models

**PostgreSQL** (via SQLAlchemy):
- `Transcript` table: episode metadata and content (composite PK: podcast, episode_number)
- `VectorChunk` table: chunked text with embeddings (FK to Transcript)
- Extension: pgvector for vector storage and operations

**OpenSearch**:
- KNN vector index with HNSW algorithm, L2 space, FAISS engine
- Fields: title, episode_number, description, url, content, content_vector, pub_date

## Common Commands

**Note**: All commands below use `uv run` to ensure proper environment isolation. If you've activated the virtual environment with `source .venv/bin/activate`, you can omit `uv run`.

### Running the Transcription Pipeline
```bash
# Transcribe latest episode
uv run python src/transcribe.py ep

# Transcribe specific episodes
uv run python src/transcribe.py ep 100 101 102

# Transcribe a range
uv run python src/transcribe.py ep --range 100-105

# Transcribe all episodes (with confirmation)
uv run python src/transcribe.py ep --all

# Transcribe a local audio file
uv run python src/transcribe.py file path/to/audio.mp3 --output path/to/output.txt
```

### Ingesting Data into Databases
```bash
# Load transcripts into both PostgreSQL and OpenSearch
uv run python src/quick_upload.py files

# Load specific files
uv run python src/quick_upload.py files --file transcripts/episode1.md --file transcripts/episode2.md

# Load with reindexing (recreate OpenSearch index)
uv run python src/quick_upload.py files --reindex

# Load only to PostgreSQL
uv run python src/quick_upload.py files --pg-only

# Load only to OpenSearch
uv run python src/quick_upload.py files --os-only
```

### Index Management
```bash
# Create/recreate OpenSearch index (destructive)
uv run python src/os_index.py
```

### Code Quality and Formatting
The project uses **ruff** for both code formatting and linting:

```bash
# Format code with ruff
uv tool run ruff format .

# Check code for linting issues
uv tool run ruff check .

# Fix linting issues automatically
uv tool run ruff check . --fix
```

**Using just recipes** (recommended):
```bash
just fmt        # Format code with ruff
just lint       # Check code with ruff
just lint-fix   # Fix linting issues automatically
just check      # Run all quality checks
```

### Testing
```bash
# Run all tests
just test

# Run tests with coverage report
just test-coverage

# Run pytest directly
uv run pytest -v
```

### Utility Commands (just recipes)
```bash
# Setup and installation
just setup              # Install dependencies and show next steps

# Transcription shortcuts
just transcribe-latest          # Transcribe the latest episode
just transcribe-range 100 105   # Transcribe episodes 100-105

# Data management
just upload             # Upload all transcripts to both databases
just upload-reindex     # Upload with OpenSearch reindexing
just upload-pg-only     # Upload only to PostgreSQL
just upload-os-only     # Upload only to OpenSearch
just index-recreate     # Recreate OpenSearch index (destructive)

# Maintenance
just clean              # Remove Python cache and build artifacts
just update-deps        # Update and sync dependencies
just py-version         # Show Python version
just uv-version         # Show uv version
```

## Environment Configuration

Required environment variables (configured via `.envrc` or manual setup):
- `AIVEN_POSTGRES_SERVICE_URI` - Aiven PostgreSQL connection string
- `OPENSEARCH_SERVICE_URI` - Aiven OpenSearch connection string
- `POSTGRES_DB_NAME` - Database name for transcripts (default: "transcripts")
- `POSTGRES_VECTOR_DB_NAME` - Table name for vector chunks
- `INDEX_NAME` - OpenSearch index name

Load environment with `direnv allow` or `source .envrc` manually.

**Note**: The `.envrc` file is not tracked in git (contains sensitive credentials). Copy from `.envrc.example` if available or set these variables in your shell.

## Development Notes

- **Transcription Backend Selection**: The system automatically prefers MLX Whisper on Apple Silicon for performance, falling back to OpenAI Whisper. First run downloads the model (~140MB for "base" model).
- **Web Scraping**: The `url_finder.py` module is tightly coupled to the Conduit website structure (CSS selectors for `.episode-wrap`, `<title>`, `<audio>` tags). Changes to the website layout will require updates here.
- **Episode Number Extraction**: Uses regex pattern `^\d+` to extract episode numbers from titles and markdown filenames.
- **Date Parsing**: Uses Arrow with custom format `r"MMMM[\s+]D[\w+,\s+]YYYY"` for publication dates.
- **Embedding Storage**: VectorChunk records store embeddings as 768-dimensional vectors; ensure pgvector extension is installed and enabled in PostgreSQL.
- **Error Handling**: `pg_ingest.py` uses logging (WARNING level by default); check logs for detailed error information during data processing.
- **Contributing**: See `CONTRIBUTING.md` for PR requirements. PRs require an issue first, use format `[TYPE] <Issue Number> - Description`, and must pass `just check` quality checks.

## Common Issues

- **Virtual Environment**: Run `uv sync` to install dependencies and create the virtual environment. If you encounter import errors, ensure you're running commands with `uv run` or have activated the venv with `source .venv/bin/activate`
- **Missing Environment Variables**: Ensure `.envrc` is loaded (via `direnv allow` or `source .envrc`) before running scripts. The variable name is `AIVEN_POSTGRES_SERVICE_URI` (not `POSTGRES_SERVICE_URI`).
- **MLX vs Whisper**: MLX Whisper requires Apple Silicon (M1/M2/M3). On other platforms, the system automatically falls back to OpenAI Whisper.
- **Model Downloads**: First run downloads the transcription model (~140MB for "base") - network access required
- **Database Connection**: Services are hosted on Aiven; ensure network access and valid credentials in environment variables
- **Destructive Operations**: `pg_ingest.py` and `quick_upload.py` can drop tables; `--reindex` flag recreates OpenSearch index - use with caution
- **Lock File**: The `uv.lock` file should be committed to version control for reproducible installs across environments
- **Missing Imports in quick_upload.py**: Note that `quick_upload.py` has missing imports (`psycopg` and `os`) - these need to be added if running the script directly
