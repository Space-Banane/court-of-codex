# AGENTS.md

## Purpose

This repository packages the `idea-evaluator` skill for multiple agent ecosystems.
Treat the root files as the canonical project guidance:

- `Intent.md` is the behavior spec for the skill.
- `README.md` explains the repo layout at a high level.
- `cspell.json` defines the spellcheck vocabulary used by CI.

## Working Rules

- Read `Intent.md` and `README.md` before making repo-wide changes.
- Keep the three package folders aligned when a shared description changes.
- Keep prose concise and consistent across `codex/`, `claude/`, and `openclaw/`.
- When adding new markdown wording or project terms, update `cspell.json` if CI should accept them.
- Preserve intentional misspellings only when they are part of a test or a deliberate example.
- Prefer `apply_patch` for edits and keep changes minimal.

## Validation

- Markdown files are checked in CI with `cspell`.
- Make sure new or edited `.md` files pass spellcheck before you consider the work done.
