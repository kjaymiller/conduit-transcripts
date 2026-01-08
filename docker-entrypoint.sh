#!/bin/bash

set -e

# Start FastAPI app on port 8000 in background
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 &
MAIN_APP_PID=$!

# Start MCP server on port 8001 in background
uv run python -m app.mcp.server &
MCP_SERVER_PID=$!

# Function to handle shutdown
shutdown() {
    echo "Shutting down servers..."
    kill $MAIN_APP_PID 2>/dev/null || true
    kill $MCP_SERVER_PID 2>/dev/null || true
    wait $MAIN_APP_PID 2>/dev/null || true
    wait $MCP_SERVER_PID 2>/dev/null || true
    exit 0
}

# Trap signals
trap shutdown SIGTERM SIGINT

# Wait for both processes
wait
