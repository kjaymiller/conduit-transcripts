"""Episode metadata extraction utilities."""

import urllib.parse as parser
from typing import Optional, Tuple, Dict

import httpx
from bs4 import BeautifulSoup

URL_BASE = "https://www.relay.fm/conduit/"


def _get_url_soup(url: str) -> BeautifulSoup:
    """Gets a soup object from the web."""
    response = httpx.get(url)
    response.raise_for_status()
    html = response.text
    return BeautifulSoup(html)


def get_audio_url_from_episode_number(
    episode_number: int,
) -> Optional[Tuple[Dict[str, str], str]]:
    """Get the audio URL and metadata for a given episode number."""
    print(f"Getting audio URL for episode {episode_number}")
    url = f"{URL_BASE}{episode_number}"
    soup = _get_url_soup(url)
    audio_url = soup.find("audio")

    if not (audio_url_attrs := getattr(audio_url, "attrs")):
        print("Unable to fetch url.", err=True)
        return None

    audio_file_url = audio_url_attrs.get("src", None)
    print(f"{url=} found")

    title = (
        getattr(soup.find("title"), "text").split(" - ")[0].removeprefix("Conduit #")
    )
    description = getattr(
        soup.find("meta", attrs={"property": "og:description"}), "attrs"
    )["content"]
    pub_date = soup.find("p", attrs={"class": "pubdate"}).text.split("\n·\n")[0]
    metadata = {
        "title": title,
        "url": url,
        "description": description,
        "pub_date": pub_date,
    }
    print(metadata)
    return (metadata, audio_file_url)


def fetch_latest_episode_number() -> int:
    """Gets the latest episode number."""
    print("Getting latest episode_number")
    soup = _get_url_soup(URL_BASE)
    episode_list_section = soup.find("div", attrs={"class": "episode-wrap"})

    error_message = "Error Fetching values"
    if not episode_list_section:
        raise ValueError(error_message)

    episode_url = episode_list_section.find("a")

    if not episode_url:
        raise ValueError(error_message)

    print(f"{episode_url=} found!")
    episode_number = parser.urlsplit(episode_url.get("href")).path.split("/")[-1]

    print(f"episode {episode_number=} found!")
    return int(episode_number)
