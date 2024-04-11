import gazpacho
import frontmatter
import pathlib

def append_frontmatter_to_file(filename:pathlib.Path) -> None:
    """Prepend frontmatter to a file."""
    episode_frontmatter = frontmatter.loads(filename.read_text())
    episode_frontmatter["title"] = episode_frontmatter["title"].removesuffix(" - Relay FM").removeprefix("Conduit #")
    filename.write_text(frontmatter.dumps(episode_frontmatter))

if __name__ == "__main__":
    for file in pathlib.Path("transcripts").iterdir():
        append_frontmatter_to_file(file)