#!/usr/bin/env python3
"""Create a workflow folder from the built-in template."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = ROOT / "workflows" / "_template"
DEFAULT_OUTPUT_DIR = ROOT / "workflows"
WORKFLOW_FILES = ("WORKFLOW.md", "TASK_CARD.md", "EXECUTION_PROMPT.md", "HANDOFF.md")


def slug_is_safe(name: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9][a-z0-9_-]*", name))


def title_from_slug(name: str) -> str:
    return " ".join(part.capitalize() for part in re.split(r"[-_]+", name) if part)


def rewrite_placeholders(target: Path, title: str) -> None:
    replacements = {
        "<Name>": title,
        "<Task Name>": title,
    }
    for filename in WORKFLOW_FILES:
        path = target / filename
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a workflow folder from workflows/_template."
    )
    parser.add_argument(
        "name",
        help="Workflow folder name, e.g. auto-research-breakdown.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory that will contain the new workflow folder. Defaults to workflows/.",
    )
    parser.add_argument(
        "--template",
        default=str(DEFAULT_TEMPLATE),
        help="Template directory. Defaults to workflows/_template.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing workflow folder.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not slug_is_safe(args.name):
        print(
            "error: workflow name must use lowercase letters, digits, hyphen, or underscore",
            file=sys.stderr,
        )
        return 2

    template = Path(args.template).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    target = output_dir / args.name

    if not template.is_dir():
        print(f"error: template directory not found: {template}", file=sys.stderr)
        return 2

    missing = [name for name in WORKFLOW_FILES if not (template / name).is_file()]
    if missing:
        print(f"error: template missing required files: {', '.join(missing)}", file=sys.stderr)
        return 2

    if target.exists():
        if not args.force:
            print(f"error: workflow already exists: {target}", file=sys.stderr)
            print("hint: use --force to overwrite", file=sys.stderr)
            return 1
        shutil.rmtree(target)

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template, target)
    rewrite_placeholders(target, title_from_slug(args.name))

    print(f"created workflow: {target}")
    print("next: edit TASK_CARD.md, then render a worker prompt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
