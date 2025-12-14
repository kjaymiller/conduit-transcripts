"""Main entry points for apps."""


def transcribe_main():
    """Entry point for transcribe app."""
    from apps.transcribe.main import main

    main()


def mcp_main():
    """Entry point for MCP app."""
    from apps.mcp.main import main

    main()
