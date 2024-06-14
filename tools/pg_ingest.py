import pathlib
import os

import arrow
import frontmatter
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from typing import Optional
from sqlalchemy import String, select
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
)
from sqlalchemy.types import Date

load_dotenv()

class Base(DeclarativeBase):
    pass
    

class Episode(Base):
    __tablename__ = 'conduit_transcripts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[str]
    date: Mapped[Optional[Date]] = mapped_column(Date)
    description: Mapped[str]
    url: Mapped[str] = mapped_column(String(240))
    

engine = create_engine(os.getenv("POSTGRES_SERVICE_URI"))
Base.metadata.create_all(engine)

fmt = r"MMMM[\s+]D[\w+,\s+]YYYY"

def episode_from_file(file_path:pathlib.Path) -> Episode:
    """Create an Episode object from a file."""
    post = frontmatter.loads(file_path.read_text())
    episode = Episode(
        title=post["title"],
        content=post.content,
        date=arrow.get(post["pub_date"], fmt).date(),
        description=post["description"],
        url=post["url"]
    )
    return episode

def pg_load_episode(episode: Episode) -> None:
    """Load an Episode object into the database."""
    with Session(engine) as session:
        session.add(episode)
        session.commit()


def pg_update_episode(episode: Episode) -> None:
    with Session(engine) as session:
        query = select(Episode).where(Episode.title == episode.title)
        old_episode = session.scalars(query).one()
        session.delete(old_episode)
        session.add(episode)
        session.commit()


def pg_load_from_file(file_path:pathlib.Path) -> Episode:
    """
    Update the database with the contents of a file.
    If the file is not in the database, add it.
    """
    
    episode = episode_from_file(file_path)

    with Session(engine) as session:
        query = select(Episode).where(Episode.title == episode.title)
        old_episode = session.scalars(query).one_or_none()
    
        if old_episode is None:
            session.add(episode)
    
        else:
            session.delete(old_episode)
            session.add(episode)
        session.commit()