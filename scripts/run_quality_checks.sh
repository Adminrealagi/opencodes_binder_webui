#!/usr/bin/env bash
set -euo pipefail

python3 scripts/check_max_lines.py
python3 scripts/validate_json.py

ruff check tests scripts
yamllint -c .yamllint.yml .github/workflows docker-compose.yml

if command -v hadolint >/dev/null 2>&1; then
  hadolint docker/electerm-hoster.Dockerfile docker/opencode-hoster.Dockerfile
else
  echo "hadolint is not installed; Dockerfile lint is enforced in CI workflow." >&2
fi

python3 -m unittest discover -s tests/bdd -p "test_*.py"
