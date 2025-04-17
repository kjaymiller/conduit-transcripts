"""
Vectorizes content and inserts it into a table using standard SQLAlchemy methods
"""

import logging
import os
import re
import pathlib

import frontmatter
from pgvector.sqlalchemy import Vector
from sqlalchemy import create_engine, Column, Integer, Text, ForeignKeyConstraint, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import mapped_column, sessionmaker, declarative_base, relationship
from sqlalchemy.schema import PrimaryKeyConstraint, UniqueConstraint

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Configure logging
logging.basicConfig(
    level=logging.WARN, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Database connection
DB_URI = os.getenv("POSTGRES_SERVICE_URI")
PG_DB_NAME = os.getenv("POSTGRES_DB_NAME", "transcripts")
PG_VECTOR_DB_NAME = os.getenv("POSTGRES_VECTOR_DB_NAME", "transcript_vector")

# Initialize SQLAlchemy
engine = create_engine(DB_URI)

# Create base
Base = declarative_base()


# Define SQLAlchemy models
class Transcript(Base):
    """Model for transcript data"""

    __tablename__ = PG_DB_NAME

    podcast = Column(Text, primary_key=True)
    episode_number = Column(Integer, primary_key=True)
    meta = Column(JSONB)

    # Define composite primary key
    __table_args__ = (PrimaryKeyConstraint("podcast", "episode_number"),)

    # Define relationship to vector chunks
    chunks = relationship(
        "VectorChunk", back_populates="transcript", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Transcript(episode_number={self.episode_number})>"


class VectorChunk(Base):
    """Model for vector chunks"""

    __tablename__ = PG_VECTOR_DB_NAME

    id = Column(Integer, primary_key=True)
    episode_number = Column(Integer)
    podcast = Column(Text)
    content = Column(Text)
    embedding = mapped_column(Vector(768))

    # Define relationship to transcript
    transcript = relationship("Transcript", back_populates="chunks")

    __table_args__ = (
        ForeignKeyConstraint(
            ["podcast", "episode_number"],
            [f"{PG_DB_NAME.lower()}.podcast", f"{PG_DB_NAME.lower()}.episode_number"],
        ),
        UniqueConstraint(
            "id", "podcast", "episode_number", name="uq_vector_chunk_id_podcast_episode"
        ),
    )

    def __repr__(self):
        return f"<VectorChunk(id={self.id}, episode_number={self.episode_number})>"


class VectorDatabase:
    """Handler for vector database operations using SQLAlchemy"""

    def __init__(self, recreate_tables=False):
        """Initialize the database handler"""
        self.engine = engine

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
            model_name="sentence-transformers/all-mpnet-base-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": False},
        )

    def process_frontmatter_post(self, post: frontmatter.Post) -> bool:
        """Process a frontmatter post and save to database"""
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


def process_files(dir_path: pathlib.Path, recreate_tables: bool = False) -> bool:
    """Process a frontmatter file"""
    try:
        db = VectorDatabase(recreate_tables=recreate_tables)

        for file in dir_path.iterdir():
            # Load frontmatter file
            with file.open("r") as f:
                post = frontmatter.load(f)

            # Process with database
            db.process_frontmatter_post(post)

    except Exception as e:
        ValueError(logging.error(f"Error processing file {dir_path}: {e}"))


if __name__ == "__main__":
    process_files(pathlib.Path("transcripts"), recreate_tables=True)
