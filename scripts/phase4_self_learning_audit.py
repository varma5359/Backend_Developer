#!/usr/bin/env python3
"""Static quality gate for the Phase 4 self-learning lesson manuscripts.

This checks Markdown structure and required teaching elements only. It does
not execute Django code or certify beginner usability.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAYS = range(42, 46)
ERRORS: list[str] = []
WARNINGS: list[str] = []
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*(?:~~~|\x60\x60\x60)", re.MULTILINE)


def check_file(path: Path, required: tuple[str, ...]) -> str:
    if not path.is_file():
        ERRORS.append(f"Missing required file: {path.relative_to(ROOT)}")
        return ""
    content = path.read_text(encoding="utf-8")
    fences = FENCE_RE.findall(content)
    if len(fences) % 2:
        ERRORS.append(f"{path.name}: unbalanced code fences ({len(fences)})")

    for target in LINK_RE.findall(content):
        target = target.strip().split()[0].strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        local = target.split("#", 1)[0].split("?", 1)[0]
        if not local:
            continue
        resolved = (path.parent / local).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            ERRORS.append(f"{path.name}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            ERRORS.append(f"{path.name}: broken local link: {target}")

    lowered = content.lower()
    for phrase in required:
        if phrase.lower() not in lowered:
            WARNINGS.append(f"{path.name}: missing expected teaching element: {phrase}")

    if "trainer guidance" in lowered or "ask the trainer" in lowered:
        ERRORS.append(f"{path.name}: trainer-dependent wording remains")
    return content


def main() -> int:
    total_lines = 0
    for day in DAYS:
        prefix = f"day_{day:02d}"
        notes = check_file(
            ROOT / f"{prefix}_notes.md",
            (
                "learning outcomes",
                "common errors",
                "mini-project",
                "acceptance",
                "knowledge check",
                "completion checklist",
            ),
        )
        interview = check_file(
            ROOT / f"{prefix}_interview.md",
            (
                "model answer",
                "scenario",
                "project viva",
                "self-check", "self-assessment",
            ),
        )
        total_lines += len(notes.splitlines()) + len(interview.splitlines())

    audit_path = ROOT / "PHASE_4_SELF_LEARNING_AUDIT.md"
    if not audit_path.is_file():
        ERRORS.append("Missing PHASE_4_SELF_LEARNING_AUDIT.md")
    else:
        audit = audit_path.read_text(encoding="utf-8").lower()
        for phrase in ("day 43", "day 44", "day 45", "runtime validation pending"):
            if phrase not in audit:
                ERRORS.append(f"Phase 4 audit is missing: {phrase}")

    print("PHASE 4 DOCUMENTATION QUALITY GATE")
    print("==================================")
    print("Days checked: 42–45")
    print("Class notes: 4")
    print("Interview guides: 4")
    print(f"Total Markdown lines: {total_lines:,}")
    print(f"Errors: {len(ERRORS)}")
    for error in ERRORS:
        print(f"ERROR: {error}")
    print(f"Warnings: {len(WARNINGS)}")
    for warning in WARNINGS:
        print(f"WARNING: {warning}")
    print("\nLIMITATION: This is a static Markdown check only. It does not install")
    print("Django, run migrations, execute browser flows or prove beginner usability.")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
