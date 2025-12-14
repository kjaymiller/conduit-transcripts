"""PostgreSQL vector database operations."""

import logging
import re
from typing import Optional

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from conduit_transcripts.models import Transcript, VectorChunk, Base
from conduit_transcripts.config import settings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import frontmatter


class VectorDatabase:
    """Handler for vector database operations using SQLAlchemy."""

    def __init__(self, recreate_tables: bool = False):
        """Initialize the database handler."""
        self.engine = create_engine(settings.postgres_uri)

        # Create tables
        if recreate_tables:
            Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)

        # Create pgvector extension
        with self.engine.connect() as conn:
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            conn.commit()

        # Create session factory
        self.Session = sessionmaker(bind=self.engine)

        # Initialize text processing tools
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=20,
            separators=[".", "!", "?", "\n"],
            keep_separator="end",
        )

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={"device": settings.EMBEDDING_DEVICE},
            encode_kwargs={"normalize_embeddings": False},
        )

    def process_frontmatter_post(self, post: frontmatter.Post) -> bool:
        """Process a frontmatter post and save to database."""
        # Convert frontmatter post to dictionary
        metadata = post.metadata.copy()
        podcast = "Conduit"

        # Store content in metadata
        metadata["content"] = post.content

        if "episode_number" not in metadata:
            episode_number = re.match(r"^\d+", metadata["title"]).group()
        else:
            episode_number = metadata["episode_number"]

        logging.warning(episode_number)

        # Start session
        session = self.Session()

        try:
            transcript = Transcript(
                episode_number=episode_number, podcast=podcast, meta=metadata
            )
            session.add(transcript)

            # Create chunks and embeddings
            chunks = self.text_splitter.create_documents([metadata["content"]])
            texts = [chunk.page_content for chunk in chunks]
            embeddings = self.embedding_model.embed_documents(texts)

            # Create vector chunks
            for text, embedding in zip(texts, embeddings):
                chunk = VectorChunk(
                    episode_number=episode_number,
                    podcast=podcast,
                    content=text,
                    embedding=embedding,
                )
                session.add(chunk)

            # Commit changes
            session.commit()
            logging.info(
                f"Processed transcript {episode_number} with {len(chunks)} chunks"
            )
            return True

        except Exception as e:
            session.rollback()
            logging.error(f"Error processing transcript: {e}")
            return False

        finally:
            session.close()
