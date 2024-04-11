import pathlib

from slugify import slugify

def slugify_file(file:pathlib.Path) -> pathlib.Path:
    """Rename a file to a slugified version of its name."""
    new_name = slugify(file.stem) + file.suffix
    return file.rename(file.with_name(new_name))

def slugify_paths(directory:pathlib.Path):
    """Slugify all files in a directory."""
    for file in list(directory.iterdir()):
        if file.is_file():
            slugify_file(file)
        elif file.is_dir():
            slugify_paths(file)