import os
import json
import logging
import uuid
from datetime import datetime
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
) -> str:
    """
    Enqueue a transcription job.
    Returns the job ID.
    """
    client = get_valkey_client()
    job_id = str(uuid.uuid4())

    # Create job status record
    job_status = {
        "id": job_id,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "podcast_id": podcast_id,
        "episode_number": episode_number,
        "audio_url": audio_url,
    }

    # Store job status
    try:
        client.set(f"job:{job_id}", json.dumps(job_status))
    except Exception as e:
        logger.error(f"Failed to create job status record: {e}")
        # Continue to enqueue even if status tracking fails?
        # Ideally we should probably fail, but let's try to proceed.
        # Actually, if we can't write to valkey, lpush will likely fail too.
        pass

    job_data = {
        "job_id": job_id,
        "podcast_id": podcast_id,
        "episode_number": episode_number,
        "audio_url": audio_url,
    }
    payload = json.dumps(job_data)
    try:
        client.lpush(QUEUE_NAME, payload)
        logger.info(f"Enqueued job {job_id} for episode {episode_number}")
        return job_id
    except Exception as e:
        logger.error(f"Failed to enqueue job: {e}")
        raise


def update_job_status(
    job_id: str,
    status: str,
    result: Optional[Dict[str, Any]] = None,
    ttl: Optional[int] = None,
) -> None:
    """
    Update the status of a job.
    """
    client = get_valkey_client()
    key = f"job:{job_id}"

    try:
        # Get existing job data to preserve other fields
        existing_data = client.get(key)
        if existing_data:
            job_data = json.loads(existing_data)
        else:
            job_data = {"id": job_id, "created_at": datetime.now().isoformat()}

        job_data["status"] = status
        job_data["updated_at"] = datetime.now().isoformat()
        if result:
            job_data["result"] = result

        client.set(key, json.dumps(job_data))

        if ttl:
            client.expire(key, ttl)

        logger.info(f"Updated job {job_id} status to {status}")
    except Exception as e:
        logger.error(f"Failed to update job status for {job_id}: {e}")


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
