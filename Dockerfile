FROM python:3.13-slim

WORKDIR /app

# Install only essential system deps
RUN apt-get update && apt-get install -y \
  libpq5 \
  build-essential \
  curl \
  ffmpeg \
  && rm -rf /var/lib/apt/lists/*

# Copy podcast_transcription module first
COPY podcast_transcription/ /app/podcast_transcription/
COPY podcast_transcription/pyproject.toml /app/podcast_transcription/

# Install uv
RUN pip install uv


# Copy app code
COPY app/ /app/app/
COPY cli/ /app/cli/
COPY pyproject.toml ./
COPY README.md ./
COPY uv.lock .


# Set PROJECT_ROOT for local dependency reference
ENV PROJECT_ROOT=/app

# Install app and its dependencies using uv
# This will install both the main app and the podcast_transcription workspace member
RUN uv sync --frozen

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Copy entrypoint script
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

# Run entrypoint script that starts both FastAPI and MCP server
ENTRYPOINT ["/app/docker-entrypoint.sh"]
