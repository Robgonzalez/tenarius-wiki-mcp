#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Tenarius Wiki MCP — setup (proyecto comunitario, no oficial)"

if command -v uv >/dev/null 2>&1; then
  echo "    Instalando con uv..."
  uv sync
  RUN_CMD='uv run tenarius-wiki-mcp'
  PROFILE_CMD=(uv run python "$ROOT/scripts/configure-profile.py")
else
  echo "    uv no encontrado; usando pip..."
  python3 -m venv .venv
  # shellcheck disable=SC1091
  source .venv/bin/activate
  pip install -U pip
  pip install -e .
  RUN_CMD='.venv/bin/tenarius-wiki-mcp'
  PROFILE_CMD=(python3 "$ROOT/scripts/configure-profile.py")
fi

chmod +x "$ROOT/scripts/configure-profile.sh" 2>/dev/null || true

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Perfil de aventurero (OPCIONAL — 100% local en tu PC)"
echo " Open source · sin fines comerciales · nadie más ve tus datos"
echo " Guardado en: ~/.config/tenarius-wiki-mcp/adventurer-profile.json"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
read -r -p "¿Configurar perfil de aventurero ahora? [S/n]: " SETUP_PROFILE || true
SETUP_PROFILE=${SETUP_PROFILE:-S}
if [[ "${SETUP_PROFILE,,}" != "n" && "${SETUP_PROFILE,,}" != "no" ]]; then
  "${PROFILE_CMD[@]}" || true
else
  echo "    Omitido. Luego: ./scripts/configure-profile.sh"
fi

echo ""
echo "Setup listo. Para probar el servidor:"
echo "  cd $ROOT && $RUN_CMD"
echo ""
echo "Cursor: abre esta carpeta como workspace — .cursor/mcp.json ya está configurado."
echo "Global: copia examples/cursor-global-mcp.json a ~/.cursor/mcp.json (ajusta la ruta)."
echo "Perfil: ./scripts/configure-profile.sh  |  docs/PERFIL-AVENTURERO.md"
echo "Ver DISCLAIMER.md — este MCP no es oficial de Tenarius ni de Gravity/RO."
echo ""
echo "Reinicia Cursor después de cambiar la config MCP."
