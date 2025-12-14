"""Database models for Conduit Transcripts."""

from sqlalchemy import Column, Integer, Text, ForeignKeyConstraint, JSONB
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.schema import PrimaryKeyConstraint, UniqueConstraint
from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Transcript(Base):
    """Model for transcript data."""

    __tablename__ = "transcripts"

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
    """Model for vector chunks."""

    __tablename__ = "transcript_vector"

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
            ["transcripts.podcast", "transcripts.episode_number"],
        ),
        UniqueConstraint(
            "id", "podcast", "episode_number", name="uq_vector_chunk_id_podcast_episode"
        ),
    )

    def __repr__(self):
        return f"<VectorChunk(id={self.id}, episode_number={self.episode_number})>"
