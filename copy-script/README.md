# Copy Script

This folder contains the Python installer for the `idea-evaluator` skill packages.

## What It Does

The script copies each ecosystem package into the matching skills directory in your home folder:

- `codex/idea-evaluator` -> `~/.codex/skills/idea-evaluator`
- `claude/idea-evaluator` -> `~/.claude/skills/idea-evaluator`
- `openclaw/idea-evaluator` -> `~/.openclaw/skills/idea-evaluator`

## Interactive Mode

Run the script with no flags in a terminal to pick ecosystems interactively.

It will:

- show the available ecosystems,
- let you choose one or more,
- and ask before overwriting existing installs.

## CLI Mode

Use flags when you want a non-interactive run.

Examples:

```bash
python copy-script/install-skills.py --all
python copy-script/install-skills.py --ecosystems codex openclaw
python copy-script/install-skills.py --all --dry-run
python copy-script/install-skills.py --all --force
```

## Options

- `--all`: install into every supported ecosystem
- `--ecosystems`: install into selected ecosystems only
- `--repo-root`: point the script at a different repository root
- `--home`: point the script at a different home directory
- `--dry-run`: print actions without copying files
- `--force`: skip overwrite confirmation
