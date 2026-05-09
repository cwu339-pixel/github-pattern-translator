#!/usr/bin/env python3
"""Check whether HANDOFF.md has the required recovery sections populated."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = (
    "Current Paths",
    "Completed",
    "Not Completed",
    "Commands Run",
    "Artifacts Produced",
    "Current Pass/Fail",
    "Known Risks",
    "Next Open Loops",
)

PLACEHOLDER_PATTERNS = (
    r"^- \[ \] Item:\s*$",
    r"^- Path:\s*$",
    r"^- Workflow:\s*$",
    r"^- Task files:\s*$",
    r"^- Evidence/output:\s*$",
    r"^- Status:\s*$",
    r"^- Reason:\s*$",
    r"^- Evidence:\s*$",
    r"^- Risk:\s*$",
    r"^\d+\.\s*$",
    r"^# command\s*$",
    r"^# output summary\s*$",
)


def parse_sections(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            current = match.group(1)
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def meaningful_lines(body: str) -> list[str]:
    lines = []
    in_fence = False
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not line:
            continue
        if any(re.match(pattern, line) for pattern in PLACEHOLDER_PATTERNS):
            continue
        lines.append(line)
    return lines


def resolve_handoff(path: Path) -> Path:
    if path.is_dir():
        return path / "HANDOFF.md"
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a workflow HANDOFF.md for required recovery sections and placeholders."
    )
    parser.add_argument("path", help="Workflow folder path or HANDOFF.md path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    handoff = resolve_handoff(Path(args.path).expanduser().resolve())
    if not handoff.is_file():
        print(f"error: HANDOFF.md not found: {handoff}", file=sys.stderr)
        return 2

    text = handoff.read_text(encoding="utf-8")
    sections = parse_sections(text)
    failures: list[str] = []

    for section in REQUIRED_SECTIONS:
        body = sections.get(section)
        if body is None:
            failures.append(f"missing section: {section}")
            continue
        if not meaningful_lines(body):
            failures.append(f"empty or placeholder-only section: {section}")

    if failures:
        print(f"handoff incomplete: {handoff}")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"handoff complete: {handoff}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
