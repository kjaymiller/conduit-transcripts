"""Apply rewrite rules to transcript files to correct common transcription errors."""

import json
import pathlib
import re
from typing import Dict

import frontmatter
import typer
import typing_extensions
from rich.progress import track

app = typer.Typer()


def load_rewrite_rules(rules_file: pathlib.Path) -> Dict[str, str]:
    """Load rewrite rules from a JSON file."""
    if not rules_file.exists():
        typer.echo(f"Error: Rules file not found: {rules_file}", err=True)
        raise typer.Exit(1)
    
    try:
        with open(rules_file, "r", encoding="utf-8") as f:
            rules = json.load(f)
        return rules
    except json.JSONDecodeError as e:
        typer.echo(f"Error: Invalid JSON in rules file: {e}", err=True)
        raise typer.Exit(1)


def apply_rewrite_rules(text: str, rules: Dict[str, str]) -> str:
    """
    Apply rewrite rules to text using case-insensitive matching with word boundaries.
    
    Args:
        text: The text to process
        rules: Dictionary mapping incorrect text to correct text
    
    Returns:
        Text with rewrite rules applied
    """
    result = text
    
    for incorrect, correct in rules.items():
        # Create a regex pattern with word boundaries for case-insensitive matching
        # For multi-word phrases, replace spaces with \s+ to allow flexible whitespace
        # and use word boundaries only at the start and end
        escaped = re.escape(incorrect)
        # Replace escaped spaces with \s+ pattern
        pattern = escaped.replace(r"\ ", r"\s+")
        # Add word boundaries at start and end
        pattern = r"\b" + pattern + r"\b"
        result = re.sub(pattern, correct, result, flags=re.IGNORECASE)
    
    return result


def process_transcript_file(
    input_file: pathlib.Path,
    output_file: pathlib.Path,
    rules: Dict[str, str],
) -> bool:
    """
    Process a single transcript file by applying rewrite rules.
    
    Args:
        input_file: Path to input transcript file
        output_file: Path to output transcript file
        rules: Dictionary of rewrite rules
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Read and parse the file with frontmatter
        content = input_file.read_text(encoding="utf-8")
        post = frontmatter.loads(content)
        
        # Apply rewrite rules to the content (not the frontmatter metadata)
        corrected_content = apply_rewrite_rules(post.content, rules)
        
        # Update the post with corrected content
        post.content = corrected_content
        
        # Ensure output directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the corrected file
        output_file.write_text(frontmatter.dumps(post), encoding="utf-8")
        
        return True
    except Exception as e:
        typer.echo(f"Error processing {input_file}: {e}", err=True)
        return False


@app.command()
def apply_rules(
    input_dir: typing_extensions.Annotated[
        pathlib.Path,
        typer.Option("--input-dir", "-i", help="Input directory containing transcript files"),
    ] = None,
    output_dir: typing_extensions.Annotated[
        pathlib.Path,
        typer.Option("--output-dir", "-o", help="Output directory for corrected transcript files"),
    ] = None,
    rules_file: typing_extensions.Annotated[
        pathlib.Path,
        typer.Option("--rules-file", "-r", help="Path to rewrite rules JSON file"),
    ] = pathlib.Path("rewrite_rules.json"),
    with_timestamps: typing_extensions.Annotated[
        bool,
        typer.Option("--with-timestamps", help="Process transcripts_with_timestamps/ directory instead of transcripts/"),
    ] = False,
    in_place: typing_extensions.Annotated[
        bool,
        typer.Option("--in-place", help="Overwrite input files instead of writing to output directory"),
    ] = False,
):
    """
    Apply rewrite rules to transcript files.
    
    Processes all .md files in the input directory recursively and writes
    corrected versions to the output directory, preserving directory structure.
    
    If --with-timestamps is used, defaults to transcripts_with_timestamps/ directory.
    If --in-place is used, files are overwritten in the input directory.
    """
    # Set default directories based on with_timestamps flag
    if input_dir is None:
        input_dir = pathlib.Path("transcripts_with_timestamps" if with_timestamps else "transcripts")
    
    if output_dir is None:
        if in_place:
            output_dir = input_dir
        else:
            # Default output: add _corrected suffix
            output_dir = pathlib.Path(f"{input_dir}_corrected")
    
    # Validate input directory
    if not input_dir.exists():
        typer.echo(f"Error: Input directory does not exist: {input_dir}", err=True)
        raise typer.Exit(1)
    
    if not input_dir.is_dir():
        typer.echo(f"Error: Input path is not a directory: {input_dir}", err=True)
        raise typer.Exit(1)
    
    # Load rewrite rules
    typer.echo(f"Loading rewrite rules from {rules_file}")
    rules = load_rewrite_rules(rules_file)
    typer.echo(f"Loaded {len(rules)} rewrite rules")
    
    # Find all markdown files recursively
    md_files = list(input_dir.rglob("*.md"))
    
    if not md_files:
        typer.echo(f"No .md files found in {input_dir}")
        return
    
    typer.echo(f"Found {len(md_files)} transcript files to process")
    
    # Process each file
    successful = 0
    failed = 0
    
    for input_file in track(md_files, description="Processing files"):
        # Calculate relative path from input directory
        relative_path = input_file.relative_to(input_dir)
        output_file = output_dir / relative_path
        
        if process_transcript_file(input_file, output_file, rules):
            successful += 1
        else:
            failed += 1
    
    typer.echo(f"\nProcessing complete:")
    typer.echo(f"  ✓ Successfully processed: {successful}")
    if failed > 0:
        typer.echo(f"  ✗ Failed: {failed}", err=True)


if __name__ == "__main__":
    app()

