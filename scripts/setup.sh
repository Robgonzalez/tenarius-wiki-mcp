#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

echo "==> Tenarius Wiki MCP — setup (proyecto comunitario, no oficial)"

if command -v uv >/dev/null 2>&1; then
  echo "    Instalando con uv..."
  uv sync
  RUN_CMD='uv run tenarius-wiki-mcp'
else
  echo "    uv no encontrado; usando pip..."
  python3 -m venv .venv
  # shellcheck disable=SC1091
  source .venv/bin/activate
  pip install -U pip
  pip install -e .
  RUN_CMD='.venv/bin/tenarius-wiki-mcp'
fi

echo ""
echo "Setup listo. Para probar el servidor:"
echo "  cd $ROOT && $RUN_CMD"
echo ""
echo "Cursor: abre esta carpeta como workspace — .cursor/mcp.json ya está configurado."
echo "Global: copia examples/cursor-global-mcp.json a ~/.cursor/mcp.json (ajusta la ruta)."
echo "Ver DISCLAIMER.md — este MCP no es oficial de Tenarius ni de Gravity/RO."
echo ""
echo "Reinicia Cursor después de cambiar la config MCP."
