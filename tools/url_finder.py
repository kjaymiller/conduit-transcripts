import typer
import httpx
import gazpacho

URL_BASE = "https://www.relay.fm/conduit/"


def get_audio_url_from_episode_number(episode_number: int, base_url="URL_BASE") -> tuple[dict[str, str], str]:
    """Get the audio URL and metadata for a given episode number."""
    typer.echo(f"Getting audio URL for episode {episode_number}")
    url = f"{URL_BASE}{episode_number}"
    response = httpx.get(url)
    response.raise_for_status()
    html = response.text
    soup = gazpacho.Soup(html)
    audio_url = soup.find("audio").attrs["src"]
    typer.echo(audio_url)

    title = soup.find("title").text.split(" - ")[0].removeprefix("Conduit #")
    description = soup.find("meta", attrs={"property": "og:description"}).attrs["content"]
    pub_date = soup.find("p", attrs={"class": "pubdate"}).text.split("\n·\n")[0]
    metadata = {
        "title": title,
        "url": url,
        "description": description,
        "pub_date": pub_date,
    }
    typer.echo(metadata)
    return (metadata, audio_url)


if __name__ == "__main__":
    typer.run(get_audio_url_from_episode_number)
