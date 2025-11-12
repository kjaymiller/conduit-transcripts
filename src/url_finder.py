import urllib.parse as parser
import typer
import httpx
from bs4 import BeautifulSoup

URL_BASE = "https://www.relay.fm/conduit/"


def _get_url_soup(url: str) -> BeautifulSoup:
    """Gets a soup object from the web"""
    response = httpx.get(url)
    response.raise_for_status()
    html = response.text
    return BeautifulSoup(html)


def get_audio_url_from_episode_number(
    episode_number: int,
) -> tuple[dict[str, str], str] | None:
    """Get the audio URL and metadata for a given episode number."""
    typer.echo(f"Getting audio URL for episode {episode_number}")
    url = f"{URL_BASE}{episode_number}"
    soup = _get_url_soup(url)
    audio_url = soup.find("audio")

    if not (audio_url_attrs := getattr(audio_url, "attrs")):
        typer.echo("Unabled to fetch url.", err=True)
        typer.Exit(1)
        return None

    audio_file_url = audio_url_attrs.get("src", None)
    typer.echo(f"{url=} found")

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
    typer.echo(metadata)
    return (metadata, audio_file_url)


def fetch_latest_episode_number() -> int:
    """Gets the latests episode number"""
    typer.echo("Getting latest episode_number")
    soup = _get_url_soup(URL_BASE)
    episode_list_section = soup.find("div", attrs={"class": "episode-wrap"})

    error_message = "Error Fetching values"
    if not episode_list_section:
        raise ValueError(error_message)

    episode_url = episode_list_section.find("a")

    if not episode_url:
        raise ValueError(error_message)

    typer.echo(f"{episode_url=} found!")
    episode_number = parser.urlsplit(episode_url.get("href")).path.split("/")[-1]

    typer.echo(f"episode {episode_number=} found!")
    return int(episode_number)
