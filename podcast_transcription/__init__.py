"""Conduit Transcripts - Modular podcast transcript management system."""

__version__ = "0.1.0"

# Import and expose submodules using relative imports
from .podcast_transcription_core import chat, config, database, models, search, transcription, utils

# Re-export submodule contents
from .podcast_transcription_core.chat import *  # noqa: F401
from .podcast_transcription_core.config import *  # noqa: F401
from .podcast_transcription_core.database import *  # noqa: F401
from .podcast_transcription_core.models import *  # noqa: F401
from .podcast_transcription_core.search import *  # noqa: F401
from .podcast_transcription_core.transcription import *  # noqa: F401
from .podcast_transcription_core.utils import *  # noqa: F401

__all__ = ['chat', 'config', 'database', 'models', 'search', 'transcription', 'utils']
