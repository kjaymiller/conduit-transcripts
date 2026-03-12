"""Transcription abstraction layer with Parakeet and MLX Whisper support."""

import logging
import pathlib
import platform
import sys
import typing

logger = logging.getLogger(__name__)


class TranscriptionBackend:
    """Abstract base for transcription backends."""

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe an audio file to text."""
        raise NotImplementedError


class ParakeetTranscriber(TranscriptionBackend):
    """NVIDIA Parakeet transcriber using NeMo toolkit."""

    def __init__(self, model: str = "nvidia/parakeet-rnnt-1.1b"):
        """Initialize Parakeet transcriber.

        Args:
            model: NeMo model name (default: nvidia/parakeet-rnnt-1.1b)
                   If "base", "small", etc. are passed (Whisper legacy),
                   it defaults to the standard Parakeet model.
        """
        # Handle legacy Whisper model names
        if model in [
            "tiny",
            "base",
            "small",
            "medium",
            "large",
            "large-v2",
            "large-v3",
        ]:
            logger.warning(
                f"Legacy Whisper model '{model}' requested. Using default Parakeet model."
            )
            model = "nvidia/parakeet-rnnt-1.1b"

        self.model_name = model

        try:
            import nemo.collections.asr as nemo_asr
            import torch
        except ImportError:
            raise ImportError(
                "nemo_toolkit[asr] not installed. Install with: pip install nemo_toolkit[asr]"
            )

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Parakeet initialized on device: {self.device}")

        try:
            logger.info(f"Loading Parakeet model: {self.model_name}")
            # NeMo's ASRModel.from_pretrained() handles auto-resolution of model class
            self.model = nemo_asr.models.ASRModel.from_pretrained(
                model_name=self.model_name
            )

            self.model.freeze()
            self.model.to(self.device)
        except Exception as e:
            logger.error(f"Failed to load Parakeet model {self.model_name}: {e}")
            raise

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe using Parakeet."""
        try:
            logger.info(
                f"Transcribing {audio_path} with Parakeet ({self.model_name})..."
            )

            # NeMo expects list of paths
            files = [str(audio_path)]

            # transcribe() method signature depends on model type (CTC vs RNNT)
            # Most NeMo ASR models support transcribe(paths2audio_files=...)
            transcriptions = self.model.transcribe(
                paths2audio_files=files, batch_size=1
            )

            if isinstance(transcriptions, list) and len(transcriptions) > 0:
                result = transcriptions[0]

                # RNNT models often return Hypothesis objects
                if hasattr(result, "text"):
                    return result.text

                # CTC models usually return plain strings
                if isinstance(result, str):
                    return result

                # Fallback for other return types (e.g. tuples)
                if isinstance(result, tuple):
                    return result[0]

                return str(result)

            return ""

        except Exception as e:
            logger.error(f"Parakeet transcription failed: {e}")
            raise


class MLXWhisperTranscriber(TranscriptionBackend):
    """MLX Whisper transcriber for Apple Silicon Macs."""

    # Map short names to HuggingFace model IDs
    MODEL_MAP = {
        "tiny": "mlx-community/whisper-tiny-mlx",
        "base": "mlx-community/whisper-base-mlx-q4",
        "small": "mlx-community/whisper-small-mlx",
        "medium": "mlx-community/whisper-medium-mlx",
        "large": "mlx-community/whisper-large-v3-mlx",
        "large-v2": "mlx-community/whisper-large-v2-mlx",
        "large-v3": "mlx-community/whisper-large-v3-mlx",
    }

    def __init__(self, model: str = "mlx-community/whisper-large-v3-mlx"):
        # Map short names to full model IDs
        if model in self.MODEL_MAP:
            model = self.MODEL_MAP[model]
        elif model.startswith("nvidia/"):
            logger.warning(
                f"NeMo model '{model}' not supported on MLX. Using default MLX Whisper model."
            )
            model = "mlx-community/whisper-large-v3-mlx"

        self.model_name = model

        try:
            import mlx_whisper  # noqa: F401
        except ImportError:
            raise ImportError(
                "mlx-whisper not installed. Install with: uv add mlx-whisper"
            )

        logger.info(f"MLX Whisper initialized with model: {self.model_name}")

    def transcribe(self, audio_path: pathlib.Path) -> str:
        """Transcribe using MLX Whisper."""
        try:
            import mlx_whisper

            logger.info(
                f"Transcribing {audio_path} with MLX Whisper ({self.model_name})..."
            )

            result = mlx_whisper.transcribe(
                str(audio_path),
                path_or_hf_repo=self.model_name,
            )

            text = result.get("text", "")
            logger.info(f"MLX Whisper transcription completed. Length: {len(text)}")
            return text

        except Exception as e:
            logger.error(f"MLX Whisper transcription failed: {e}")
            raise


def get_transcriber(model: str | None = None) -> TranscriptionBackend:
    """Factory that returns the appropriate transcriber for the current platform.

    On macOS ARM64, returns MLXWhisperTranscriber.
    On Linux (or when TRANSCRIBE_PREFER_MLX is explicitly False), returns ParakeetTranscriber.
    """
    from podcast_transcription_core.config import settings

    if model is None:
        model = settings.TRANSCRIPTION_MODEL

    use_mlx = (
        sys.platform == "darwin"
        and platform.machine() == "arm64"
    ) or settings.TRANSCRIBE_PREFER_MLX

    if use_mlx:
        return MLXWhisperTranscriber(model=model)
    else:
        return ParakeetTranscriber(model=model)
