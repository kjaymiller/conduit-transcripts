# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a podcast transcript management system for the Conduit Podcast. It automates the process of:
1. Fetching episode metadata from the Conduit website
2. Downloading audio files
3. Transcribing audio using OpenAI Whisper
4. Processing and chunking transcripts
5. Generating embeddings for vector search
6. Storing data in PostgreSQL and OpenSearch for RAG applications

## Technology Stack

- **Language**: Python 3.12.5 (specified in `.python-version`)
- **Package Manager**: uv (see `pyproject.toml` for dependencies)
- **Audio Processing**: OpenAI Whisper (for transcription)
- **Text Processing**: LangChain text splitters and HuggingFace embeddings
- **Databases**: PostgreSQL with pgvector extension, OpenSearch
- **Web Scraping**: BeautifulSoup, httpx
- **CLI Framework**: Typer
- **ORM**: SQLAlchemy with pgvector support
- **Environment Management**: python-dotenv, direnv (`.envrc`)
- **Code Quality**: Ruff (formatting and linting), pytest (testing)

## Directory Structure

- `src/` - Main application code
  - `transcribe.py` - Main script for Whisper transcription and episode processing
  - `url_finder.py` - Web scraping for Conduit website (episode metadata, audio URLs)
  - `os_ingest.py` - OpenSearch data ingestion (incomplete/skeleton)
  - `os_index.py` - OpenSearch index creation and setup
  - `pg_ingest.py` - PostgreSQL data processing with embeddings and vector storage
  - `quick_upload.py` - Unified data loading script for both OpenSearch and PostgreSQL
  - `download_audio_file.py` - Audio file download utility
- `transcripts/` - Generated markdown files with frontmatter metadata and transcribed content
- `infra/` - Infrastructure configuration files
- `.envrc` - Direnv environment variables (contains sensitive connection strings)
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

## Environment Configuration

The `.envrc` file contains:
- `OPENSEARCH_SERVICE_URI` - Aiven OpenSearch connection
- `POSTGRES_SERVICE_URI` - Aiven PostgreSQL connection
- `POSTGRES_DB_NAME` - Database name for transcripts (default: "transcripts")
- `POSTGRES_VECTOR_DB_NAME` - Table name for vector chunks
- `INDEX_NAME` - OpenSearch index name

Load environment with `direnv allow` or source `.envrc` manually.

## Development Notes

- **Web Scraping**: The `url_finder.py` module is tightly coupled to the Conduit website structure (CSS selectors for `.episode-wrap`, `<title>`, `<audio>` tags). Changes to the website layout will require updates here.
- **Episode Number Extraction**: Uses regex pattern `^\d+` to extract episode numbers from titles and markdown filenames.
- **Date Parsing**: Uses Arrow with custom format `r"MMMM[\s+]D[\w+,\s+]YYYY"` for publication dates.
- **Embedding Storage**: VectorChunk records store embeddings as 768-dimensional vectors; ensure pgvector extension is installed and enabled in PostgreSQL.
- **Error Handling**: `pg_ingest.py` uses logging (WARNING level by default); check logs for detailed error information during data processing.

## Common Issues

- **Virtual Environment**: Run `uv sync` to install dependencies and create the virtual environment. If you encounter import errors, ensure you're running commands with `uv run` or have activated the venv
- **Missing Environment Variables**: Ensure `.envrc` is loaded (via `direnv allow` or `source .envrc`) before running scripts
- **Whisper Model Loading**: First run downloads the "base" model (~140MB) - network access required
- **Database Connection**: Services are hosted on Aiven; ensure network access and credentials are valid
- **Table Recreation**: `pg_ingest.py` and `quick_upload.py` can drop tables; use `--reindex` flag carefully
- **Lock File**: The `uv.lock` file should be committed to version control for reproducible installs across environments
