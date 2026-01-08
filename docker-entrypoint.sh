#!/bin/bash

set -e

# Start FastAPI app on port 8000
# This includes the mounted MCP server at /mcp
exec uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
