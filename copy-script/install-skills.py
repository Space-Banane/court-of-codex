from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ECOSYSTEMS = {
    "codex": ("codex", ".codex"),
    "claude": ("claude", ".claude"),
    "openclaw": ("openclaw", ".openclaw"),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Copy the idea-evaluator skill packages into local skills directories."
    )
    parser.add_argument(
        "--ecosystems",
        nargs="+",
        choices=sorted(ECOSYSTEMS),
        help="One or more ecosystems to install into. Omit for interactive mode.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Install into all supported ecosystems.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Path to the repository root. Defaults to the parent of copy-script/.",
    )
    parser.add_argument(
        "--home",
        type=Path,
        default=Path.home(),
        help="Home directory that contains the target skills folders.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be copied without writing anything.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing installations without prompting.",
    )
    return parser


def prompt_ecosystems() -> list[str]:
    options = list(ECOSYSTEMS)
    print("Select ecosystems to install:")
    for index, name in enumerate(options, start=1):
        print(f"  {index}. {name}")
    print("  a. all")

    choice = input("Enter numbers or names separated by commas [a]: ").strip().lower()
    if not choice or choice == "a" or choice == "all":
        return options

    selected: list[str] = []
    for raw_item in choice.split(","):
        item = raw_item.strip()
        if not item:
            continue
        if item.isdigit():
            index = int(item) - 1
            if index < 0 or index >= len(options):
                raise SystemExit(f"Invalid ecosystem number: {item}")
            selected.append(options[index])
            continue
        if item not in ECOSYSTEMS:
            raise SystemExit(f"Unknown ecosystem: {item}")
        selected.append(item)

    if not selected:
        raise SystemExit("No ecosystems selected.")

    return list(dict.fromkeys(selected))


def prompt_confirmation(message: str) -> bool:
    choice = input(f"{message} [y/N]: ").strip().lower()
    return choice in {"y", "yes"}


def resolve_targets(args: argparse.Namespace) -> list[str]:
    if args.all:
        return list(ECOSYSTEMS)

    if args.ecosystems:
        return list(dict.fromkeys(args.ecosystems))

    if sys.stdin.isatty():
        return prompt_ecosystems()

    raise SystemExit("Specify --all or --ecosystems when running non-interactively.")


def install_skill(source: Path, destination_root: Path, dry_run: bool) -> Path:
    destination = destination_root / source.name
    if dry_run:
        print(f"Would copy {source} -> {destination}")
        return destination

    destination_root.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        if destination.is_dir():
            shutil.rmtree(destination)
        else:
            destination.unlink()

    shutil.copytree(source, destination)
    print(f"Copied {source} -> {destination}")
    return destination


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    home = args.home.expanduser().resolve()
    selected = resolve_targets(args)

    jobs = []
    for ecosystem in selected:
        source_dirname, destination_dirname = ECOSYSTEMS[ecosystem]
        source = repo_root / source_dirname / "idea-evaluator"
        destination_root = home / destination_dirname / "skills"
        jobs.append((ecosystem, source, destination_root))

    if not args.force and not args.dry_run:
        destinations = [destination_root / "idea-evaluator" for _, _, destination_root in jobs]
        existing = [path for path in destinations if path.exists()]
        if existing:
            print("Existing installations found:")
            for path in existing:
                print(f"  {path}")
            if not sys.stdin.isatty() or not prompt_confirmation("Overwrite them"):
                raise SystemExit("Cancelled.")

    for _, source, destination_root in jobs:
        install_skill(source, destination_root, args.dry_run)


if __name__ == "__main__":
    main()
