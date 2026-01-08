"""PostgreSQL vector database operations."""

import logging
import re
from typing import Optional

import frontmatter
from dateutil import parser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from ..config import settings
from ..models import Base, Podcast, Transcript, VectorChunk

logger = logging.getLogger(__name__)


class VectorDatabase:
    """Handler for vector database operations using SQLAlchemy."""

    def __init__(self, recreate_tables: bool = False):
        """Initialize the database handler.

        Args:
            recreate_tables: If True, drop and recreate tables.
        """
        self.engine = create_engine(settings.postgres_uri)

        # Create pgvector extension
        with self.engine.connect() as conn:
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            conn.commit()

        # Create tables
        if recreate_tables:
            Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

        # Create session factory
        self.Session = sessionmaker(bind=self.engine)

        # Initialize text processing tools
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            separators=[".", "!", "?", "\n", " ", ""],
            keep_separator="end",
        )

        if settings.EMBEDDING_PROVIDER == "ollama":
            self.embedding_model = OllamaEmbeddings(
                model=settings.EMBEDDING_MODEL,
                base_url=settings.OLLAMA_BASE_URL,
            )
        else:
            self.embedding_model = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL,
                model_kwargs={"device": settings.EMBEDDING_DEVICE},
                encode_kwargs={"normalize_embeddings": False},
            )

    def set_transcript_status(
        self, podcast_id: int, episode_number: int, status: str
    ) -> bool:
        """Set the processing status of a transcript.

        Args:
            podcast_id: The ID of the podcast.
            episode_number: The episode number.
            status: The status to set (e.g., 'processing', 'completed', 'error').

        Returns:
            True if successful, False otherwise.
        """
        session = self.Session()
        try:
            transcript = session.query(Transcript).get((podcast_id, episode_number))
            if not transcript:
                return False

            transcript.processing_status = status
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            logger.error(f"Error setting transcript status: {e}")
            return False
        finally:
            session.close()

    def update_transcript_content(
        self, podcast_id: int, episode_number: int, new_content: str
    ) -> bool:
        """Update transcript content and regenerate chunks.

        Args:
            podcast_id: The ID of the podcast.
            episode_number: The episode number.
            new_content: The new transcript content.

        Returns:
            True if successful, False otherwise.
        """
        session = self.Session()
        try:
            # Update transcript
            transcript = session.query(Transcript).get((podcast_id, episode_number))
            if not transcript:
                logger.error(f"Transcript not found: {podcast_id}, {episode_number}")
                return False

            # Update content in metadata
            new_meta = transcript.meta.copy()
            new_meta["content"] = new_content
            transcript.meta = new_meta

            # Clear existing chunks
            session.query(VectorChunk).filter_by(
                episode_number=episode_number, podcast=podcast_id
            ).delete()

            # Create new chunks
            texts = self.text_splitter.split_text(new_content)
            if texts:
                embeddings = self.embedding_model.embed_documents(texts)
                for text_content, embedding in zip(texts, embeddings):
                    chunk = VectorChunk(
                        episode_number=episode_number,
                        podcast=podcast_id,
                        content=text_content,
                        embedding=embedding,
                    )
                    session.add(chunk)

            # Set status to completed
            transcript.processing_status = "completed"

            session.commit()
            logger.info(f"Updated transcript {episode_number} with {len(texts)} chunks")
            return True
        except Exception as e:
            session.rollback()
            logger.error(f"Error updating transcript: {e}")
            # Try to set status to error in a new transaction if possible, or just log it
            try:
                transcript.processing_status = "error"
                session.commit()
            except:
                pass
            return False
        finally:
            session.close()

    def get_podcast(self, podcast_id: int) -> Optional[Podcast]:
        """Get a podcast by ID.

        Args:
            podcast_id: The ID of the podcast.

        Returns:
            The Podcast object if found, None otherwise.
        """
        session = self.Session()
        try:
            return session.query(Podcast).get(podcast_id)
        finally:
            session.close()

    def update_podcast_feed_url(self, podcast_id: int, feed_url: str) -> bool:
        """Update the RSS feed URL for a podcast.

        Args:
            podcast_id: The ID of the podcast.
            feed_url: The new RSS feed URL.

        Returns:
            True if successful, False otherwise.
        """
        session = self.Session()
        try:
            podcast = session.query(Podcast).get(podcast_id)
            if not podcast:
                # Create if not exists (assuming ID 1 for Conduit mostly)
                if podcast_id == 1:
                    podcast = Podcast(
                        id=podcast_id,
                        slug="conduit",
                        title="Conduit",
                        feed_url=feed_url,
                    )
                    session.add(podcast)
                else:
                    return False
            else:
                podcast.feed_url = feed_url

            session.commit()
            return True
        except Exception as e:
            session.rollback()
            logger.error(f"Error updating podcast feed URL: {e}")
            return False
        finally:
            session.close()

    def process_frontmatter_post(self, post: frontmatter.Post) -> bool:
        """Process a frontmatter post and save to database.

        Args:
            post: The frontmatter post object.

        Returns:
            True if successful, False otherwise.
        """
        # Convert frontmatter post to dictionary
        metadata = post.metadata.copy()
        podcast_name = "Conduit"
        podcast_id = 1

        # Store content in metadata
        metadata["content"] = post.content

        if "episode_number" not in metadata:
            match = re.match(r"^\d+", metadata["title"])
            if match:
                episode_number = int(match.group())
            else:
                logger.error(
                    f"Could not extract episode number from title: {metadata['title']}"
                )
                return False
        else:
            episode_number = int(metadata["episode_number"])

        logger.debug(f"Processing episode {episode_number}")

        # Extract normalized fields
        title = metadata.get("title")
        description = metadata.get("description")
        url = metadata.get("url")
        published_date = None
        if "pub_date" in metadata and metadata["pub_date"]:
            try:
                published_date = parser.parse(str(metadata["pub_date"]))
            except Exception:
                logger.warning(f"Could not parse pub_date: {metadata['pub_date']}")

        # Start session
        session = self.Session()

        try:
            # Ensure podcast exists
            podcast_obj = session.query(Podcast).get(podcast_id)
            if not podcast_obj:
                podcast_obj = Podcast(
                    id=podcast_id, slug=podcast_name, title=podcast_name
                )
                session.add(podcast_obj)
                session.flush()

            # Check if exists and update or insert
            transcript = session.query(Transcript).get((podcast_id, episode_number))
            if not transcript:
                transcript = Transcript(
                    episode_number=episode_number,
                    podcast=podcast_id,
                    meta=metadata,
                    title=title,
                    description=description,
                    url=url,
                    published_date=published_date,
                )
                session.add(transcript)
            else:
                transcript.meta = metadata
                transcript.title = title
                transcript.description = description
                transcript.url = url
                transcript.published_date = published_date

            # Clear existing chunks for this episode to avoid duplicates
            session.query(VectorChunk).filter_by(
                episode_number=episode_number, podcast=podcast_id
            ).delete()

            # Create chunks and embeddings using text splitter
            texts = self.text_splitter.split_text(metadata["content"])

            if not texts:
                logger.warning(f"No content to chunk for episode {episode_number}")

            if texts:
                embeddings = self.embedding_model.embed_documents(texts)

                # Create vector chunks
                for text_content, embedding in zip(texts, embeddings):
                    chunk = VectorChunk(
                        episode_number=episode_number,
                        podcast=podcast_id,
                        content=text_content,
                        embedding=embedding,
                    )
                    session.add(chunk)

            # Commit changes
            session.commit()
            logger.info(
                f"Processed transcript {episode_number} with {len(texts)} chunks"
            )
            return True

        except Exception as e:
            session.rollback()
            logger.error(f"Error processing transcript: {e}")
            return False

        finally:
            session.close()
