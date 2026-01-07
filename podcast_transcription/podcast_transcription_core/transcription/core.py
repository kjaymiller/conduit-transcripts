"""Transcription abstraction layer with MLX support and Whisper fallback."""

import logging
import os
import pathlib
import typing
import warnings

logger = logging.getLogger(__name__)


class TranscriptionBackend:
    """Abstract base for transcription backends."""

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe an audio file to text."""
        raise NotImplementedError


class MLXTranscriber(TranscriptionBackend):
    """MLX-based transcriber (Apple Silicon optimized)."""

    def __init__(self, model: str = "base"):
        """Initialize MLX transcriber.

        Args:
            model: Model size (tiny, base, small, medium, large)
        """
        try:
            import mlx_whisper

            self.mlx_whisper = mlx_whisper
            self.model = model
            logger.info(f"MLX Whisper initialized with model: {model}")
        except ImportError:
            raise ImportError(
                "mlx-whisper not installed. Install with: pip install mlx-whisper"
            )

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe using MLX."""
        try:
            logger.info(f"Transcribing with MLX ({self.model} model)...")
            result = self.mlx_whisper.transcribe(
                str(audio_path), model=self.model, verbose=False
            )
            return result["text"]
        except Exception as e:
            logger.error(f"MLX transcription failed: {e}")
            raise


class WhisperTranscriber(TranscriptionBackend):
    """OpenAI Whisper transcriber (CPU/GPU based)."""

    def __init__(self, model: str = "base"):
        """Initialize Whisper transcriber.

        Args:
            model: Model size (tiny, base, small, medium, large)
        """
        try:
            import whisper

            self.whisper = whisper
            self.model = whisper.load_model(model)
            logger.info(f"OpenAI Whisper initialized with model: {model}")
        except ImportError:
            raise ImportError(
                "openai-whisper not installed. Install with: pip install openai-whisper"
            )

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe using OpenAI Whisper."""
        try:
            logger.info("Transcribing with OpenAI Whisper...")
            audio = self.whisper.load_audio(str(audio_path))
            result = self.model.transcribe(audio=audio, verbose=False)
            return result["text"]
        except Exception as e:
            logger.error(f"Whisper transcription failed: {e}")
            raise


class HybridTranscriber:
    """Transcriber that tries MLX first, falls back to Whisper."""

    def __init__(
        self, model: str = "base", prefer_mlx: typing.Optional[bool] = None
    ):
        """Initialize hybrid transcriber.

        Args:
            model: Model size (tiny, base, small, medium, large)
            prefer_mlx: If True, try MLX first; if False, use Whisper directly.
                        If None, defaults to TRANSCRIBE_PREFER_MLX env var (default: False).
        """
        self.model = model

        if prefer_mlx is None:
            prefer_mlx = (
                os.environ.get("TRANSCRIBE_PREFER_MLX", "false").lower() == "true"
            )

        self.prefer_mlx = prefer_mlx
        self._primary_transcriber: typing.Optional[TranscriptionBackend] = None
        self._fallback_transcriber: typing.Optional[TranscriptionBackend] = None

        self._initialize_transcribers()

    def _initialize_transcribers(self) -> None:
        """Initialize primary and fallback transcribers."""
        if self.prefer_mlx:
            # Try MLX first
            try:
                self._primary_transcriber = MLXTranscriber(self.model)
            except ImportError:
                logger.warning("MLX not available, falling back to Whisper")
                self._primary_transcriber = WhisperTranscriber(self.model)

            # Set fallback to Whisper
            if not isinstance(self._primary_transcriber, WhisperTranscriber):
                try:
                    self._fallback_transcriber = WhisperTranscriber(self.model)
                except ImportError:
                    logger.warning("Whisper not available as fallback")
        else:
            # Use Whisper directly
            try:
                self._primary_transcriber = WhisperTranscriber(self.model)
            except ImportError:
                raise ImportError("Neither MLX nor Whisper is available")

            # Set fallback to MLX
            if not isinstance(self._primary_transcriber, MLXTranscriber):
                try:
                    self._fallback_transcriber = MLXTranscriber(self.model)
                except ImportError:
                    logger.warning("MLX not available as fallback")

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe audio file with fallback support."""
        if not self._primary_transcriber:
            raise RuntimeError("No transcriber initialized")

        try:
            return self._primary_transcriber.transcribe(audio_path)
        except Exception as e:
            if self._fallback_transcriber:
                logger.warning(f"Primary transcriber failed: {e}. Trying fallback...")
                return self._fallback_transcriber.transcribe(audio_path)
            else:
                raise
