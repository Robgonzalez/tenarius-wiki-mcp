#!/usr/bin/env bash
# Configura perfil de aventurero (100% local). Wrapper sobre configure-profile.py
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if command -v uv >/dev/null 2>&1; then
  exec uv run python "$ROOT/scripts/configure-profile.py" "$@"
else
  exec python3 "$ROOT/scripts/configure-profile.py" "$@"
fi
