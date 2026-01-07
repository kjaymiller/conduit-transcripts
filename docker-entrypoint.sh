#!/bin/bash
set -e

MODE=${CONDUIT_MODE:-api}

case $MODE in
  api)
    echo "Starting API server..."
    exec uvicorn app.main:app --host 0.0.0.0 --port ${API_PORT:-8000}
    ;;
  mcp)
    echo "Starting MCP server..."
    exec python -m app.mcp.server
    ;;
  cli)
    echo "Running CLI command: $@"
    exec "$@"
    ;;
  *)
    echo "Error: Unknown mode '$MODE'. Valid modes: api, mcp, cli"
    exit 1
    ;;
esac
