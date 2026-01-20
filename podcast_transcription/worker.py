import os
import logging
import signal
import sys
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("worker")

from podcast_transcription_core.utils.queue import dequeue_job
from podcast_transcription_core.transcription.service import (
    process_new_episode_transcription,
)

running = True


def handle_sigterm(signum, frame):
    global running
    logger.info("Received SIGTERM. Shutting down worker...")
    running = False


def run_worker():
    logger.info("Starting transcription worker...")

    # Register signal handlers
    signal.signal(signal.SIGTERM, handle_sigterm)
    signal.signal(signal.SIGINT, handle_sigterm)

    while running:
        try:
            # Blocking pop with timeout allows checking 'running' flag periodically
            job = dequeue_job(timeout=2)

            if job:
                logger.info(f"Received job: {job}")

                podcast_id = job.get("podcast_id")
                episode_number = job.get("episode_number")
                audio_url = job.get("audio_url")

                if podcast_id and episode_number and audio_url:
                    process_new_episode_transcription(
                        podcast_id, episode_number, audio_url
                    )
                else:
                    logger.error("Invalid job data: missing required fields")

            # If no job, loop continues immediately (after timeout)

        except Exception as e:
            logger.error(f"Worker loop error: {e}", exc_info=True)
            time.sleep(1)  # Prevent tight loop on error

    logger.info("Worker stopped.")


if __name__ == "__main__":
    run_worker()
