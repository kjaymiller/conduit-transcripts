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

# Install uv and conduit_transcripts dependencies
RUN pip install uv
RUN cd /app/conduit_transcripts && uv sync

# Copy app code
COPY app/ /app/app/
COPY pyproject.toml ./
COPY README.md ./

# Install app dependencies (including conduit_transcripts)
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
