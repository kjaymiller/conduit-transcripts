"""Transcription abstraction layer with MLX support and Whisper fallback."""

import pathlib
import typing
import warnings

import typer


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
            typer.echo(f"✓ MLX Whisper initialized with model: {model}")
        except ImportError:
            raise ImportError(
                "mlx-whisper not installed. Install with: pip install mlx-whisper"
            )

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe using MLX."""
        try:
            typer.echo(f"Transcribing with MLX ({self.model} model)...")
            result = self.mlx_whisper.transcribe(
                str(audio_path), model=self.model, verbose=False
            )
            return result["text"]
        except Exception as e:
            typer.echo(f"MLX transcription failed: {e}", err=True)
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
            typer.echo(f"✓ OpenAI Whisper initialized with model: {model}")
        except ImportError:
            raise ImportError(
                "openai-whisper not installed. Install with: pip install openai-whisper"
            )

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe using OpenAI Whisper."""
        try:
            typer.echo("Transcribing with OpenAI Whisper...")
            audio = self.whisper.load_audio(str(audio_path))
            result = self.model.transcribe(audio=audio, verbose=False)
            return result["text"]
        except Exception as e:
            typer.echo(f"Whisper transcription failed: {e}", err=True)
            raise


class HybridTranscriber:
    """Transcriber that tries MLX first, falls back to Whisper."""

    def __init__(self, model: str = "base", prefer_mlx: bool = True):
        """Initialize hybrid transcriber.

        Args:
            model: Model size (tiny, base, small, medium, large)
            prefer_mlx: If True, try MLX first; if False, use Whisper directly
        """
        self.model = model
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
            except ImportError as e:
                typer.echo(f"Warning: MLX not available ({e})", err=True)
                self._primary_transcriber = None

            # Whisper as fallback
            try:
                self._fallback_transcriber = WhisperTranscriber(self.model)
            except ImportError as e:
                typer.echo(f"Warning: Whisper not available ({e})", err=True)
                self._fallback_transcriber = None
        else:
            # Use Whisper directly
            try:
                self._primary_transcriber = WhisperTranscriber(self.model)
            except ImportError as e:
                typer.echo(f"Warning: Whisper not available ({e})", err=True)
                self._primary_transcriber = None

            # MLX as fallback
            try:
                self._fallback_transcriber = MLXTranscriber(self.model)
            except ImportError as e:
                typer.echo(f"Warning: MLX not available ({e})", err=True)
                self._fallback_transcriber = None

        if not self._primary_transcriber and not self._fallback_transcriber:
            raise RuntimeError(
                "No transcription backends available. Install mlx-whisper or openai-whisper."
            )

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe using primary backend, falling back if needed.

        Args:
            audio_path: Path to the audio file

        Returns:
            Transcribed text

        Raises:
            RuntimeError: If all transcription backends fail
        """
        if self._primary_transcriber:
            try:
                return self._primary_transcriber.transcribe(audio_path)
            except Exception as e:
                if self._fallback_transcriber:
                    typer.echo(
                        f"Primary transcriber failed, trying fallback...", err=True
                    )
                    try:
                        return self._fallback_transcriber.transcribe(audio_path)
                    except Exception as fallback_error:
                        raise RuntimeError(
                            f"All transcription backends failed. Primary: {e}, Fallback: {fallback_error}"
                        )
                else:
                    raise RuntimeError(
                        f"Transcription failed and no fallback available: {e}"
                    )
        elif self._fallback_transcriber:
            return self._fallback_transcriber.transcribe(audio_path)
        else:
            raise RuntimeError("No transcription backends available")
