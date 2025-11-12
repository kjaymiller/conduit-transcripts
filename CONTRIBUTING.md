# Contributing to this project

Here are the steps to contributing changes in the project

1. File an issue
2. Get the green light (:rocket: or 👍 reaction or a written confirmation to that work would be accepted). Do this
**BEFORE** submitting a PR
3. Submit a PR

## Filing an Issue

Select an appropriate template for your issue type.

### Types of issues

* :memo: Add an episode
* 💫 Add a Feature
* 🐛 Report a Bug

Fill out as much information as possible and submit.

> [!NOTE]
>
> PRs will not be approved without an issue_

## Submitting a PR

When submitting a PR please use the following syntax for your PR.

`[PR TYPE] <Issue Numer> - Short Summarization of Changes`

PR Type should be [ADD, FIX, REMOVE, UPDATE]

Your summary should combine with the PR Type to create a short summary of what is being done.

Examples:

- `ADD ## - Episode ## Episode Title`
- `FIX ## - Lints Contributing.md`
- `Updates ## - Adds 'Kathy' to corrections.json`

## Code Quality Requirements

Before submitting a PR, ensure your code passes quality checks:

### Formatting

Code must be formatted with ruff:

```bash
just fmt  # Format code
```

Or manually:

```bash
uv tool run ruff format .
```

### Linting

Code must pass ruff linting checks:

```bash
just lint  # Check for linting issues
```

Or manually:

```bash
uv tool run ruff check .
```

To automatically fix common issues:

```bash
just lint-fix
```

Or manually:

```bash
uv tool run ruff check . --fix
```

### Running All Quality Checks

```bash
just check  # Runs linting
```

> [!NOTE]
>
> PRs will not be merged if they fail code quality checks. Please run these checks locally before submitting.