from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DAYS = range(27, 55)

PLACEHOLDERS = (
    "TODO",
    "Trainer guidance",
    "Part of the example; explain its role",
    "paste the rest",
    "insert code here",
)

def fail(message):
    print(f"FAIL: {message}")
    return False

def check_fences(path, text):
    ok = True
    for fence in ("~~~", "```"):
        count = sum(
            1 for line in text.splitlines()
            if line.lstrip().startswith(fence)
        )
        if count % 2:
            ok = fail(f"{path}: unbalanced {fence} code fence") and ok
    return ok

def main():
    failures = []
    note_total = 0
    guide_total = 0

    for day in DAYS:
        note_path = ROOT / f"day_{day:02d}_notes.md"
        guide_path = ROOT / f"day_{day:02d}_interview.md"

        if not note_path.exists():
            failures.append(fail(f"Missing {note_path.name}"))
            continue
        if not guide_path.exists():
            failures.append(fail(f"Missing {guide_path.name}"))
            continue

        notes = note_path.read_text(encoding="utf-8")
        guide = guide_path.read_text(encoding="utf-8")
        note_lines = len(notes.splitlines())
        guide_lines = len(guide.splitlines())
        note_total += note_lines
        guide_total += guide_lines

        if not re.match(rf"^# Day {day:02d}:", notes.lstrip()):
            failures.append(fail(f"{note_path.name}: incorrect/missing day title"))
        if not re.match(rf"^# Day {day:02d}:", guide.lstrip()):
            failures.append(fail(f"{guide_path.name}: incorrect/missing day title"))
        if note_lines < 300:
            failures.append(fail(f"{note_path.name}: only {note_lines} lines (minimum 300)"))
        if guide_lines < 50:
            failures.append(fail(f"{guide_path.name}: only {guide_lines} lines (minimum 50)"))

        lower_notes = notes.lower()
        for phrase in ("mini-project", "checklist"):
            if phrase not in lower_notes:
                failures.append(fail(f"{note_path.name}: missing {phrase} section"))
        if not any(p in lower_notes for p in ("troubleshooting", "common errors", "common beginner mistakes", "debugging")):
            failures.append(fail(f"{note_path.name}: missing troubleshooting coverage"))
        if not any(p in lower_notes for p in ("interview preparation", "interview questions", "interview guide")):
            failures.append(fail(f"{note_path.name}: missing interview preparation"))
        if not any(p in lower_notes for p in ("mcq", "self-assessment", "self assessment", "check your understanding")):
            failures.append(fail(f"{note_path.name}: missing knowledge check"))

        lower_guide = guide.lower()
        if not any(p in lower_guide for p in ("model answer", "**answer:**", "answer:")):
            failures.append(fail(f"{guide_path.name}: missing explanatory answers"))
        if not any(p in lower_guide for p in ("scenario", "debugging", "practical")):
            failures.append(fail(f"{guide_path.name}: missing scenario/practical questions"))

        for placeholder in PLACEHOLDERS:
            if placeholder.lower() in lower_notes:
                failures.append(fail(f"{note_path.name}: contains placeholder '{placeholder}'"))
            if placeholder.lower() in lower_guide:
                failures.append(fail(f"{guide_path.name}: contains placeholder '{placeholder}'"))

        if not check_fences(note_path.name, notes):
            failures.append(False)
        if not check_fences(guide_path.name, guide):
            failures.append(False)

        print(
            f"PASS {day:02d}: notes={note_lines} lines, "
            f"interview={guide_lines} lines"
        )

    print(f"\nTotal class-note lines: {note_total}")
    print(f"Total interview-guide lines: {guide_total}")
    print(f"Days audited: {len(list(DAYS))}")
    if failures:
        print(f"\n{len(failures)} quality check(s) failed.")
        return 1
    print("\nAll Django documentation static checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
