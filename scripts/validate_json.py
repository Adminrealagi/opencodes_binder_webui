#!/usr/bin/env python3

from pathlib import Path
import json
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", ".venv", "node_modules"}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def main() -> int:
    json_files = [
        path
        for path in REPO_ROOT.rglob("*.json")
        if path.is_file() and not should_skip(path)
    ]

    if not json_files:
        print("No JSON files found.")
        return 0

    failures: list[tuple[str, str]] = []
    for path in sorted(json_files):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            rel = str(path.relative_to(REPO_ROOT))
            failures.append((rel, str(exc)))

    print(f"Checked {len(json_files)} JSON files.")

    if not failures:
        print("PASS: all JSON files are valid.")
        return 0

    print("FAIL: invalid JSON files found:")
    for rel, err in failures:
        print(f"- {rel}: {err}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
