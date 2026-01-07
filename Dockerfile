FROM python:3.13-slim

WORKDIR /app

# Install only essential system deps
RUN apt-get update && apt-get install -y \
  libpq5 \
  build-essential \
  curl \
  && rm -rf /var/lib/apt/lists/*

# Copy conduit_transcripts module first
COPY conduit_transcripts/ /app/conduit_transcripts/
COPY conduit_transcripts/pyproject.toml /app/conduit_transcripts/

# Install uv
RUN pip install uv

# Install conduit_transcripts in editable mode
RUN cd /app/conduit_transcripts && pip install -e .

# Copy app code
COPY app/ /app/app/
COPY cli/ /app/cli/
COPY pyproject.toml ./
COPY README.md ./

# Set PROJECT_ROOT for local dependency reference
ENV PROJECT_ROOT=/app

# Install app dependencies
RUN uv sync

# Create non-root user
RUN useradd -m -u 1000 appuser
RUN chown -R appuser:appuser /app
USER appuser

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
