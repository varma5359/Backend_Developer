#!/usr/bin/env python3
"""Static quality gate for the Phase 3 self-learning Markdown lessons.

This script validates the learning-document package. It does NOT execute Django
or certify that the application runs. Runtime validation must be performed
against a real project in a clean environment.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAYS = range(27, 42)
ERRORS: list[str] = []
WARNINGS: list[str] = []
SUMMARY: list[tuple[str, int, int]] = []

LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
FENCE_RE = re.compile(r"^\s*```", re.MULTILINE)
TRAINER_PHRASES = (
    "trainer-led",
    "trainer demonstrates",
    "trainer should",
    "ask the trainer",
    "wait for your trainer",
    "instructor will",
)


def read_required(path: Path) -> str:
    if not path.is_file():
        ERRORS.append(f"Missing required file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def check_links(path: Path, content: str) -> None:
    for target in LINK_RE.findall(content):
        target = target.strip().split()[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        target_path = target.split("#", 1)[0].split("?", 1)[0]
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            ERRORS.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not resolved.exists():
            ERRORS.append(f"{path.relative_to(ROOT)}: broken local link: {target}")


def main() -> int:
    for day in DAYS:
        prefix = f"day_{day:02d}"
        notes_path = ROOT / f"{prefix}_notes.md"
        interview_path = ROOT / f"{prefix}_interview.md"

        notes = read_required(notes_path)
        interview = read_required(interview_path)

        for path, content, kind in (
            (notes_path, notes, "class notes"),
            (interview_path, interview, "interview guide"),
        ):
            if not content:
                continue
            fence_count = len(FENCE_RE.findall(content))
            if fence_count % 2:
                ERRORS.append(f"{path.name}: unbalanced Markdown code fences ({fence_count})")
            check_links(path, content)
            lowered = content.lower()
            hits = [phrase for phrase in TRAINER_PHRASES if phrase in lowered]
            if hits:
                WARNINGS.append(f"{path.name}: review trainer-dependent wording: {', '.join(hits)}")

        if notes:
            lowered = notes.lower()
            required_groups = {
                "beginner explanation": ("learning objectives", "what you will learn", "what we will build", "business requirement"),
                "verification": ("verification checklist", "verify the application", "expected result", "expected output"),
                "debugging": ("troubleshooting", "common errors", "common mistakes"),
                "independent work": ("independent completion test", "independent challenge", "independent project"),
                "project work": ("mini-project", "mini project", "guided project"),
            }
            missing = [
                label for label, variants in required_groups.items()
                if not any(v in lowered for v in variants)
            ]
            if missing:
                WARNINGS.append(f"{notes_path.name}: consider strengthening {', '.join(missing)}")

        if interview:
            lowered = interview.lower()
            for label, phrase in (
                ("topic-specific model answers", "model answer"),
                ("scenario practice", "scenario"),
                ("project viva", "mini-project viva"),
                ("learner self-check", "self-check"),
            ):
                if phrase not in lowered:
                    WARNINGS.append(f"{interview_path.name}: missing {label}")

        SUMMARY.append((
            prefix,
            len(notes.splitlines()) if notes else 0,
            len(interview.splitlines()) if interview else 0,
        ))

    print("PHASE 3 DOCUMENTATION QUALITY GATE")
    print("==================================")
    print(f"Days checked: {len(SUMMARY)} (27–41)")
    print(f"Class notes checked: {sum(1 for d, _, _ in SUMMARY)}")
    print(f"Interview guides checked: {sum(1 for d, _, _ in SUMMARY)}")
    print(f"Total Markdown lines: {sum(n + i for _, n, i in SUMMARY):,}")
    print("\nPer-day line counts:")
    for day, notes_lines, interview_lines in SUMMARY:
        print(f"  {day}: notes={notes_lines:,}, interview={interview_lines:,}")

    print(f"\nErrors: {len(ERRORS)}")
    for item in ERRORS:
        print(f"ERROR: {item}")
    print(f"Warnings: {len(WARNINGS)}")
    for item in WARNINGS:
        print(f"WARNING: {item}")

    print("\nLIMITATION: This is a static Markdown check only. It does not install Django,")
    print("run manage.py, execute browser flows, or prove beginner usability.")

    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
