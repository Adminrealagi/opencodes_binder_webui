#!/usr/bin/env python3

from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
MAX_LINES = 300

SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "node_modules",
}

ALLOWED_EXTENSIONS = {
    ".py",
    ".sh",
    ".md",
    ".yml",
    ".yaml",
    ".json",
    ".csv",
    ".feature",
    ".txt",
}

ALLOWED_FILENAMES = {
    "Dockerfile",
    "docker-compose.yml",
}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def is_target_file(path: Path) -> bool:
    if path.name in ALLOWED_FILENAMES:
        return True
    if path.name.endswith(".Dockerfile"):
        return True
    return path.suffix.lower() in ALLOWED_EXTENSIONS


def line_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    return len(text.splitlines())


def main() -> int:
    violations: list[tuple[str, int]] = []
    checked = 0

    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or should_skip(path) or not is_target_file(path):
            continue

        checked += 1
        count = line_count(path)
        if count > MAX_LINES:
            violations.append((str(path.relative_to(REPO_ROOT)), count))

    print(f"Checked {checked} text/config files with max line limit {MAX_LINES}.")

    if not violations:
        print("PASS: all files are within line-count policy.")
        return 0

    print("FAIL: files exceeding the line-count policy were found:")
    for rel_path, count in sorted(violations):
        print(f"- {rel_path}: {count} lines")

    return 1


if __name__ == "__main__":
    sys.exit(main())
