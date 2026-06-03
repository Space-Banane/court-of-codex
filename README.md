# Court of Codex

This repository packages the same `idea-evaluator` concept for three different agent ecosystems.

## Contents

- `Intent.md`: the shared source of truth for the skill behavior
- `codex/idea-evaluator`: Codex-formatted package
- `claude/idea-evaluator`: Claude Code-formatted package
- `openclaw/idea-evaluator`: OpenClaw-formatted package
- `copy-script/`: Python installer and its README

## What It Does

`idea-evaluator` helps an agent judge whether a product idea, MVP, or startup concept is worth pursuing.

It is designed to:

- gather pro and con viewpoints,
- pressure-test the market and execution,
- and return a clear score, verdict, and next-step recommendation.

## Repo Layout

- `Intent.md` is the canonical brief for the skill
- Each package folder contains a `SKILL.md` plus a short README for that ecosystem
- `copy-script/README.md` explains the installer and its options

## Installation

Run the Python installer in `copy-script/` to copy the package folders into the matching skills directories under your home folder.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE).
