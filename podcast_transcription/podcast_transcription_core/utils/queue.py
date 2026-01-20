import os
import json
import logging
import valkey
from typing import Optional, Dict, Any, Generator

logger = logging.getLogger(__name__)

VALKEY_HOST = os.getenv("VALKEY_HOST", "valkey")
VALKEY_PORT = int(os.getenv("VALKEY_PORT", 6379))
QUEUE_NAME = "transcription_queue"

_client = None


def get_valkey_client() -> valkey.Valkey:
    global _client
    if _client is None:
        _client = valkey.Valkey(
            host=VALKEY_HOST, port=VALKEY_PORT, decode_responses=True
        )
    return _client


def enqueue_transcription_job(
    podcast_id: int, episode_number: int, audio_url: str
) -> None:
    """Enqueue a transcription job."""
    client = get_valkey_client()
    job_data = {
        "podcast_id": podcast_id,
        "episode_number": episode_number,
        "audio_url": audio_url,
    }
    payload = json.dumps(job_data)
    try:
        client.lpush(QUEUE_NAME, payload)
        logger.info(f"Enqueued job for episode {episode_number}")
    except Exception as e:
        logger.error(f"Failed to enqueue job: {e}")
        raise


def dequeue_job(timeout: int = 5) -> Optional[Dict[str, Any]]:
    """
    Blocking pop from the queue.
    Returns a job dictionary or None if timeout.
    """
    client = get_valkey_client()
    try:
        # brpop returns a tuple (queue_name, value) or None
        result = client.brpop(QUEUE_NAME, timeout=timeout)
        if result:
            queue, value = result
            return json.loads(value)
        return None
    except Exception as e:
        logger.error(f"Error dequeueing job: {e}")
        return None
