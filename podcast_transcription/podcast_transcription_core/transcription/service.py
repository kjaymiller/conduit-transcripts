import os
import logging
from podcast_transcription_core.database.postgres import VectorDatabase
from podcast_transcription_core.transcription.audio import download_audio_file
from podcast_transcription_core.transcription.core import ParakeetTranscriber

logger = logging.getLogger(__name__)


def process_new_episode_transcription(
    podcast_id: int, episode_number: int, audio_url: str
):
    """Background task to download, transcribe, and index a new episode."""
    db = VectorDatabase()

    try:
        logger.info(f"Starting processing for episode {episode_number}")
        logger.info(f"Audio URL: {audio_url}")

        # 1. Download audio
        if not audio_url:
            raise ValueError("No audio URL provided")

        logger.info(f"Downloading audio file for episode {episode_number}...")
        audio_path = download_audio_file(audio_url)
        logger.info(f"Audio downloaded to: {audio_path}")

        # 2. Transcribe
        logger.info(f"Initializing transcriber for episode {episode_number}...")
        transcriber = ParakeetTranscriber()
        logger.info(f"Starting transcription for episode {episode_number}...")
        transcript_text = transcriber.transcribe(audio_path)
        logger.info(
            f"Transcription completed for episode {episode_number}. Length: {len(transcript_text)}"
        )

        # 3. Cleanup audio file
        if audio_path.exists():
            logger.info(f"Cleaning up audio file: {audio_path}")
            os.unlink(audio_path)

        # 4. Update DB with content (this also chunks it and sets status to completed)
        logger.info(f"Updating database for episode {episode_number}...")
        success = db.update_transcript_content(
            podcast_id, episode_number, transcript_text
        )

        if not success:
            raise RuntimeError(
                f"Failed to update database for episode {episode_number}"
            )

        logger.info(f"Database update complete for episode {episode_number}")

    except Exception as e:
        logger.error(
            f"Error processing new episode {episode_number}: {e}", exc_info=True
        )
        db.set_transcript_status(podcast_id, episode_number, "error")


def run_transcript_update(episode_number: int, content: str):
    """Background task to update transcript content."""
    db = VectorDatabase()
    # Assume podcast ID 1 for Conduit
    db.update_transcript_content(1, episode_number, content)
