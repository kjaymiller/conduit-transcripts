"""SQLAlchemy models for transcript data."""

from pgvector.sqlalchemy import Vector
from sqlalchemy import (
    Column,
    ForeignKeyConstraint,
    Integer,
    Text,
    UniqueConstraint,
    DateTime,
    Index,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, mapped_column, relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.sql import func

from conduit_transcripts.config import settings

Base = declarative_base()


class Transcript(Base):
    """Model for transcript data."""

    __tablename__ = settings.POSTGRES_TABLE_TRANSCRIPTS

    podcast = Column(Text, primary_key=True)
    episode_number = Column(Integer, primary_key=True)
    meta = Column(JSONB)
    title = Column(Text)
    description = Column(Text)
    published_date = Column(DateTime)
    url = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

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

    __tablename__ = settings.POSTGRES_TABLE_VECTORS

    id = Column(Integer, primary_key=True)
    episode_number = Column(Integer)
    podcast = Column(Text)
    content = Column(Text)
    embedding = mapped_column(Vector(768))
    created_at = Column(DateTime, server_default=func.now())

    # Define relationship to transcript
    transcript = relationship("Transcript", back_populates="chunks")

    __table_args__ = (
        ForeignKeyConstraint(
            ["podcast", "episode_number"],
            [
                f"{settings.POSTGRES_TABLE_TRANSCRIPTS}.podcast",
                f"{settings.POSTGRES_TABLE_TRANSCRIPTS}.episode_number",
            ],
            ondelete="CASCADE",
        ),
        UniqueConstraint(
            "id",
            "podcast",
            "episode_number",
            name="uq_search_id_podcast_episode",
        ),
        Index("search_episode_idx", "podcast", "episode_number"),
        Index(
            "search_embedding_idx",
            "embedding",
            postgresql_using="ivfflat",
            postgresql_with={"lists": 100},
            postgresql_ops={"embedding": "vector_l2_ops"},
        ),
    )

    def __repr__(self):
        return f"<VectorChunk(id={self.id}, episode_number={self.episode_number})>"
