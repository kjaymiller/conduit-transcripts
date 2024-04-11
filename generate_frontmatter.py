import pathlib
import frontmatter
from gazpacho import get, Soup


def append_frontmatter_to_file(filename:pathlib.Path) -> None:
    """Prepend frontmatter to a file."""
    episode_number,_ = filename.stem.split("-", 1)
    web_soup = get(f"https://relay.fm/conduit/{episode_number}")
    soup = Soup(web_soup)
    description = soup.find("meta", {"name": "description"}, mode="first").attrs["content"]
    title = soup.find("title").text.split(" - ")[1]
    pub_date = soup.find("p", {"class": "pubdate"}).text.split("\n")[0]
    episode_frontmatter = frontmatter.Post(filename.read_text(), pub_date=pub_date, title=title, description=description)
    filename.write_text(frontmatter.dumps(episode_frontmatter))


def append_frontmatter_to_directory(directory:pathlib.Path) -> None:
    """Prepend frontmatter to all files in a directory."""
    for filepath in directory.iterdir():
        if filepath.is_file():
            try:
                append_frontmatter_to_file(filepath)
            except UnicodeDecodeError:
                print(f"Could not process {filepath} due to a decoding error")
                continue
        elif filepath.is_dir():
            append_frontmatter_to_directory(filepath)