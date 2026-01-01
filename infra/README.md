# Docker Infrastructure for Conduit Transcripts

This directory contains infrastructure configuration for running the Conduit Transcript system in Docker.

## Services

The Docker Compose setup includes three services:

### 1. PostgreSQL Database (`postgres`)
- **Image**: `pgvector/pgvector:pg16`
- **Purpose**: Stores podcast transcripts and vector embeddings
- **Features**:
  - pgvector extension for semantic search
  - Persistent volume for data storage
  - Automatic schema initialization via `init-db.sql`
  - Health checks for service dependencies

### 2. Transcript Ingestion (`ingestion`)
- **Purpose**: Processes transcript markdown files and loads them into PostgreSQL
- **Features**:
  - Reads transcripts from `/transcripts` directory
  - Chunks text and generates embeddings
  - Stores data in `transcriptions` and `search` tables
  - Uses existing `quick_upload.py` script

### 3. MCP Server (`mcp-server`)
- **Purpose**: Provides API for transcript search and summarization
- **Features**:
  - Vector similarity search
  - MCP (Model Context Protocol) compliant endpoints
  - Integration with Claude for intelligent queries
  - REST API on port 8000 (configurable)

**Note**: The MCP server implementation is tracked in issue `conduit-transcripts-ikr`.

## Quick Start

1. **Copy environment configuration**:
   ```bash
   cp .env.docker.example .env.docker
   ```

2. **Edit `.env.docker`** and set secure passwords:
   ```bash
   POSTGRES_PASSWORD=your_secure_password_here
   ```

3. **Start all services**:
   ```bash
   docker-compose --env-file .env.docker up -d
   ```

4. **View logs**:
   ```bash
   docker-compose logs -f
   ```

5. **Stop services**:
   ```bash
   docker-compose down
   ```

## Database Schema

The PostgreSQL database includes three main tables:

### `podcasts`
- Primary key: `id` (text, e.g., "Conduit")
- Columns: `title`, `description`, `feed_url`, `created_at`, `updated_at`
- Stores podcast-level metadata

### `transcriptions`
- Primary key: `(podcast, episode_number)`
- Foreign key: `podcast` → `podcasts.id`
- Columns: `title`, `description`, `url`, `published_date`, `meta` (JSONB), `created_at`, `updated_at`
- Stores episode metadata

### `search`
- Primary key: `id` (serial)
- Foreign key: `(podcast, episode_number)` → `transcriptions`
- Columns: `content`, `embedding` (768-dim vector), `created_at`
- Stores chunked text with embeddings for vector similarity search
- Indexed using IVFFlat

## Volume Management

- **`postgres_data`**: Persistent storage for PostgreSQL data
- **`./transcripts`**: Read-only mount of transcript markdown files
- **`./src`**: Read-only mount of application source code

## Networking

All services communicate via the `conduit-network` bridge network:
- Services reference each other by container name (e.g., `postgres:5432`)
- Only the MCP server and PostgreSQL expose ports to the host

## Development Workflow

### Running ingestion manually:
```bash
docker-compose run --rm ingestion python src/quick_upload.py files
```

### Accessing the database:
```bash
docker-compose exec postgres psql -U postgres -d transcripts
```

### Rebuilding after code changes:
```bash
docker-compose build
docker-compose up -d
```

## Related Issues

- **Database Setup**: `conduit-transcripts-h6e`
- **Ingestion Pipeline**: `conduit-transcripts-0mt`
- **MCP Server**: `conduit-transcripts-ikr`
- **Docker Compose**: `conduit-transcripts-1h3`

## Production Considerations

For production deployment, consider:
- Using secrets management instead of environment variables
- Configuring PostgreSQL connection pooling
- Adding backup and restore procedures
- Implementing monitoring and logging
- Setting up SSL/TLS for database connections
- Using health checks for all services
