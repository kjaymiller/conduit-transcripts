"""Episode metadata extraction utilities."""

import logging
import urllib.parse as parser
from typing import Dict, Optional, Tuple, cast

import httpx
from bs4 import BeautifulSoup, Tag

logger = logging.getLogger(__name__)

URL_BASE = "https://www.relay.fm/conduit/"


def _get_url_soup(url: str) -> BeautifulSoup:
    """Gets a soup object from the web."""
    response = httpx.get(url)
    response.raise_for_status()
    html = response.text
    return BeautifulSoup(html, "html.parser")


def get_audio_url_from_episode_number(
    episode_number: int,
) -> Optional[Tuple[Dict[str, str], str]]:
    """Get the audio URL and metadata for a given episode number."""
    logger.info(f"Getting audio URL for episode {episode_number}")
    url = f"{URL_BASE}{episode_number}"
    
    try:
        soup = _get_url_soup(url)
    except httpx.HTTPStatusError as e:
        logger.error(f"Failed to fetch episode page: {e}")
        return None

    audio_url_tag = soup.find("audio")
    if not audio_url_tag or not isinstance(audio_url_tag, Tag):
        logger.error(f"No audio tag found for {url}")
        return None

    if not (audio_url_attrs := audio_url_tag.attrs):
        logger.error("Unable to fetch url attributes.")
        return None

    audio_file_url = cast(str, audio_url_attrs.get("src"))
    if not audio_file_url:
        logger.error("No src attribute in audio tag.")
        return None
        
    logger.info(f"{url=} found")

    title_tag = soup.find("title")
    title = (
        title_tag.get_text().split(" - ")[0].removeprefix("Conduit #")
        if title_tag
        else f"Episode {episode_number}"
    )

    desc_meta = soup.find("meta", attrs={"property": "og:description"})
    description = (
        cast(str, desc_meta.attrs["content"]) 
        if desc_meta and isinstance(desc_meta, Tag) and "content" in desc_meta.attrs 
        else ""
    )
    
    pub_date_p = soup.find("p", attrs={"class": "pubdate"})
    pub_date = (
        pub_date_p.get_text().split("\n·\n")[0] 
        if pub_date_p 
        else ""
    )
    
    metadata = {
        "title": title,
        "url": url,
        "description": description,
        "pub_date": pub_date,
    }
    logger.info(metadata)
    return (metadata, audio_file_url)


def fetch_latest_episode_number() -> int:
    """Gets the latest episode number."""
    logger.info("Getting latest episode_number")
    soup = _get_url_soup(URL_BASE)
    episode_list_section = soup.find("div", attrs={"class": "episode-wrap"})

    error_message = "Error Fetching values"
    if not episode_list_section or not isinstance(episode_list_section, Tag):
        raise ValueError(error_message)

    episode_url = episode_list_section.find("a")

    if not episode_url or not isinstance(episode_url, Tag):
        raise ValueError(error_message)

    logger.info(f"{episode_url=} found!")
    href = cast(str, episode_url.get("href"))
    episode_number = parser.urlsplit(href).path.split("/")[-1]

    logger.info(f"episode {episode_number=} found!")
    return int(episode_number)
