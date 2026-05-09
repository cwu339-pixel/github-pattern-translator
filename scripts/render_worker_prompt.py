#!/usr/bin/env python3
"""Render a copy-paste worker prompt from a workflow folder."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FILES = ("WORKFLOW.md", "TASK_CARD.md", "EXECUTION_PROMPT.md", "HANDOFF.md")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a worker prompt from WORKFLOW.md, TASK_CARD.md, EXECUTION_PROMPT.md, and HANDOFF.md."
    )
    parser.add_argument("workflow", help="Workflow folder path.")
    parser.add_argument(
        "--no-context",
        action="store_true",
        help="Print only EXECUTION_PROMPT.md without embedding workflow context snapshots.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    workflow = Path(args.workflow).expanduser().resolve()
    if not workflow.is_dir():
        print(f"error: workflow folder not found: {workflow}", file=sys.stderr)
        return 2

    missing = [name for name in REQUIRED_FILES if not (workflow / name).is_file()]
    if missing:
        print(f"error: workflow missing required files: {', '.join(missing)}", file=sys.stderr)
        return 2

    execution_prompt = read(workflow / "EXECUTION_PROMPT.md")
    print("# Worker Prompt")
    print()
    print(execution_prompt)

    if args.no_context:
        return 0

    print()
    print("---")
    print()
    print("# Workflow Context Snapshots")
    print()
    for filename in ("WORKFLOW.md", "TASK_CARD.md", "HANDOFF.md"):
        print(f"## {filename}")
        print()
        print("```markdown")
        print(read(workflow / filename))
        print("```")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
