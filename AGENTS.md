# AI Agent Instructions

## Issue Tracking with bd (beads)

**IMPORTANT**: This project uses **bd (beads)** for ALL issue tracking. Do NOT use markdown TODOs, task lists, or other tracking methods.

**CRITICAL**: Before starting ANY task, ALWAYS check beads issues for context:
```bash
bd list --json           # See all issues
bd ready --json          # Check for unblocked issues
bd show <issue-id>       # Get details on specific issue
```
This ensures you understand what's already planned, discovered, or in progress related to the work.

### Why bd?

- Dependency-aware: Track blockers and relationships between issues
- Git-friendly: Auto-syncs to JSONL for version control
- Agent-optimized: JSON output, ready work detection, discovered-from links
- Single source of truth for task state (GitHub/Gitea for external visibility)
- Prevents duplicate tracking systems and confusion

### Quick Start

**Check for ready work:**
```bash
bd ready --json
```

**Create new issues:**
```bash
bd create "Issue title" -t bug|feature|task -p 0-4 --description "Detailed description" --json
bd create "Issue title" -p 1 --deps discovered-from:bd-123 --description "Why this exists and what needs to be done" --json
bd create "Subtask" --parent <epic-id> --description "Subtask details" --json  # Hierarchical subtask (gets ID like epic-id.1)
```

**Claim and update:**
```bash
bd update bd-42 --status in_progress --json
bd update bd-42 --priority 1 --json
```

**Complete work:**
```bash
bd close bd-42 --reason "Completed" --json
```

### Issue Types

- `bug` - Something broken
- `feature` - New functionality
- `task` - Work item (tests, docs, refactoring)
- `epic` - Large feature with subtasks
- `chore` - Maintenance (dependencies, tooling)

### Priorities

- `0` - Critical (security, data loss, broken builds)
- `1` - High (major features, important bugs)
- `2` - Medium (default, nice-to-have)
- `3` - Low (polish, optimization)
- `4` - Backlog (future ideas)

### Workflow for AI Agents

1. **Check beads for context**: Always run `bd list --json` to understand existing work, and `bd show <issue-id>` for relevant context before starting
2. **Check ready work**: `bd ready` shows unblocked issues
3. **Claim your task**: `bd update <id> --status in_progress`
4. **Work on it**: Implement, test, document
5. **Need to plan/design first?** Create planning issue:
   - `bd create "Design: Feature name" -t task -p 1 --description "Architecture, implementation steps, considerations" --json`
6. **Discover new work?** Create linked issue with description:
   - `bd create "Found bug" -p 1 --deps discovered-from:<parent-id> --description "Bug details and impact"`
7. **Complete**: `bd close <id> --reason "Done"`
8. **Commit together**: Always commit the `.beads/issues.jsonl` file together with the code changes so issue state stays in sync with code state

### Auto-Sync

bd automatically syncs with git:
- Exports to `.beads/issues.jsonl` after changes (5s debounce)
- Imports from JSONL when newer (e.g., after `git pull`)
- No manual export/import needed!

### GitHub Copilot Integration

If using GitHub Copilot, also create `.github/copilot-instructions.md` for automatic instruction loading.
Run `bd onboard` to get the content, or see step 2 of the onboard instructions.

### MCP Server (Recommended)

If using Claude or MCP-compatible clients, install the beads MCP server:

```bash
pip install beads-mcp
```

Add to MCP config (e.g., `~/.config/claude/config.json`):
```json
{
  "beads": {
    "command": "beads-mcp",
    "args": []
  }
}
```

Then use `mcp__beads__*` functions instead of CLI commands.

### Planning and Design Work

AI assistants often need to create planning and design documents during development:
- Architecture decisions, implementation plans, testing strategies
- Research findings, design documents, integration plans

**Best Practice: Use beads for ALL planning and design work**

**Recommended approach:**
- Create planning/design issues in beads with detailed descriptions
- Use `--description` to document the full plan, architecture, or research findings
- Link related issues with dependencies (e.g., `--deps discovered-from:bd-123`)
- Create epics for large features with multiple subtasks
- Store detailed design information in issue descriptions, not separate files

**Benefits:**
- ✅ Single source of truth for all work
- ✅ Dependency tracking ensures correct work order
- ✅ Planning stays in sync with code state
- ✅ Easy to track what's planned, in-progress, or completed
- ✅ Clean repository without planning clutter
- ✅ Git-friendly with automatic version control

**Example: Creating a design issue**
```bash
bd create "Design: User authentication flow" -t task -p 1 \
  --description "
# Overview
Design a secure authentication flow for the application

# Architecture
1. Use JWT tokens
2. Implement refresh token rotation
3. Add rate limiting

# Implementation Steps
- Add dependencies (PyJWT, bcrypt)
- Create auth endpoints (/login, /refresh, /logout)
- Implement middleware for protected routes
- Add unit tests for auth logic
" \
  --json
```

### GitHub/Gitea Integration

For external visibility and collaboration, create corresponding GitHub/Gitea issues that align with beads tasks.

**When to create GitHub/Gitea issues:**
- Work that requires external review or collaboration
- Features or bugs reported by contributors
- Epics that need project-level tracking
- Work that needs milestone or release planning

**Creating aligned issues:**
1. Create the beads issue first (source of truth)
2. Create a GitHub/Gitea issue that references the beads ID
3. Use consistent titles and descriptions
4. Link related issues appropriately

**Example workflow:**
```bash
# 1. Create beads issue (source of truth)
bd create "Add user authentication" -t feature -p 1 \
  --description "
Implement OAuth2 authentication with GitHub provider.

# Tasks
- Add OAuth2 dependencies
- Configure GitHub OAuth app
- Create login endpoint
- Add user session management
" \
  --json

# 2. Create GitHub issue with reference
gh issue create \
  --title "Add user authentication [bd-42]" \
  --body "
This issue tracks beads task bd-42

# Description
Implement OAuth2 authentication with GitHub provider.

## Tasks
- Add OAuth2 dependencies
- Configure GitHub OAuth app
- Create login endpoint
- Add user session management
"
```

**Using GitHub Projects:**
- Create projects for epics or milestones
- Use project boards to track progress visually
- Add beads ID to issue titles for cross-referencing
- Project status mirrors beads issue status

**Synchronization guidelines:**
- Beads is the source of truth for task state
- Update GitHub/Gitea issues when beads status changes
- Reference beads ID in external issue titles: `[bd-XX]`
- Create GitHub issues for high-priority or collaborative work
- Skip GitHub issues for small internal tasks

### CLI Help

Run `bd <command> --help` to see all available flags for any command.
For example: `bd create --help` shows `--parent`, `--deps`, `--assignee`, etc.

### Important Rules

- ✅ Use bd for ALL internal task tracking (source of truth)
- ✅ Always use `--json` flag for programmatic use
- ✅ **ALWAYS provide `--description` when creating issues** - provides context for future work
- ✅ Link discovered work with `discovered-from` dependencies
- ✅ Check `bd ready` before asking "what should I work on?"
- ✅ Use beads for ALL planning and design work (create issues with detailed descriptions)
- ✅ Create GitHub/Gitea issues aligned with beads for external visibility
- ✅ Reference beads ID in external issue titles: `[bd-XX]`
- ✅ Run `bd <cmd> --help` to discover available flags
- ❌ Do NOT create markdown TODO lists
- ❌ Do NOT create separate planning/design files in repo root
- ❌ Do NOT create GitHub/Gitea issues without corresponding beads issue
- ❌ Do NOT duplicate tracking systems (keep beads as source of truth)
- ❌ Do NOT create issues without descriptions

For more details, see README.md and QUICKSTART.md.
