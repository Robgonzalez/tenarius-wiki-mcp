"""Perfil local del aventurero — solo en la máquina del usuario."""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

PROFILE_VERSION = 1
CONFIG_DIR = Path.home() / ".config" / "tenarius-wiki-mcp"
PROFILE_PATH = CONFIG_DIR / "adventurer-profile.json"

PRIVACY_NOTICE = """
╔══════════════════════════════════════════════════════════════════╗
║  Perfil de aventurero — 100% LOCAL                               ║
╠══════════════════════════════════════════════════════════════════╣
║  • Se guarda SOLO en tu PC: ~/.config/tenarius-wiki-mcp/         ║
║  • El MCP corre en tu máquina (stdio local); no envía datos      ║
║    a servidores del proyecto ni a terceros comerciales.          ║
║  • Proyecto open source (MIT), sin fines comerciales.            ║
║  • Puedes omitir, editar o borrar el archivo cuando quieras.     ║
╚══════════════════════════════════════════════════════════════════╝
"""


@dataclass
class AdventurerProfile:
    version: int = PROFILE_VERSION
    character_name: str = ""
    class_name: str = ""
    base_level: int | None = None
    job_level: int | None = None
    server: str = "Tenarius RO"
    notable_gear: str = ""
    goals_short: str = ""
    goals_medium: str = ""
    play_style: str = ""
    language: str = "es"
    notes: str = ""

    def is_configured(self) -> bool:
        return bool(self.character_name.strip() or self.class_name.strip())

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AdventurerProfile:
        known = {f.name for f in cls.__dataclass_fields__.values()}  # type: ignore[attr-defined]
        filtered = {k: v for k, v in data.items() if k in known}
        return cls(**filtered)


def profile_path() -> Path:
    return PROFILE_PATH


def load_profile() -> AdventurerProfile | None:
    path = profile_path()
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        profile = AdventurerProfile.from_dict(data)
        return profile if profile.is_configured() else None
    except (json.JSONDecodeError, OSError, TypeError):
        return None


def save_profile(profile: AdventurerProfile) -> Path:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    profile.version = PROFILE_VERSION
    path = profile_path()
    path.write_text(
        json.dumps(profile.to_dict(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass
    return path


def format_profile_for_agent(profile: AdventurerProfile) -> str:
    lines = [
        "## Perfil del aventurero (local, configurado por el jugador)",
        f"- **Personaje:** {profile.character_name or '(sin nombre)'}",
        f"- **Clase:** {profile.class_name or '(sin definir)'}",
    ]
    if profile.base_level is not None:
        lvl = str(profile.base_level)
        if profile.job_level is not None:
            lvl += f"/{profile.job_level}"
        lines.append(f"- **Nivel:** {lvl}")
    lines.append(f"- **Servidor:** {profile.server}")
    if profile.notable_gear:
        lines.append(f"- **Equipo notable:** {profile.notable_gear}")
    if profile.play_style:
        lines.append(f"- **Estilo de juego:** {profile.play_style}")
    if profile.goals_short:
        lines.append(f"- **Objetivos corto plazo:** {profile.goals_short}")
    if profile.goals_medium:
        lines.append(f"- **Objetivos mediano plazo:** {profile.goals_medium}")
    if profile.notes:
        lines.append(f"- **Notas:** {profile.notes}")
    lines.append(
        "- _Usa este contexto para personalizar builds, farming y recomendaciones._"
    )
    return "\n".join(lines)


def build_instructions_base() -> str:
    from tenarius_wiki_mcp.sources import TARGET_EPISODE_MAX, TARGET_ERA

    return f"""
Servidor MCP comunitario (NO OFICIAL). No afiliado a Tenarius RO, Gravity ni Ragnarok Online.

Contexto Tenarius: servidor privado **{TARGET_ERA}**, referencia hasta **Episodio {TARGET_EPISODE_MAX}**.

Reglas para el agente:
1. **Siempre** indica servidor, era (Pre-Renewal / Renewal / mixto) y si aplica a Tenarius.
2. Contenido **custom Tenarius** → `search_wiki`, `get_wiki_summary`, `get_wiki_page`.
3. Mecánicas **vanilla RO** → `search_ro_reference` / `get_ro_reference_*`.
4. Búsqueda web amplia → `search_ro_web` (opcional con BRAVE_API_KEY).
5. **Renewal** o posterior al Ep. {TARGET_EPISODE_MAX} → **destacar** que puede no aplicar a Tenarius.
6. Si no sabes el servidor o la era, dilo explícitamente.
7. Si existe perfil local → usa `get_adventurer_profile` para personalizar respuestas.
8. El perfil del jugador es **100% local**; no compartir ni inferir datos fuera de lo configurado.
""".strip()


def build_instructions() -> str:
    base = build_instructions_base()
    profile = load_profile()
    if profile:
        return f"{base}\n\n{format_profile_for_agent(profile)}"
    return (
        f"{base}\n\n"
        "_Perfil de aventurero no configurado. Sugiere al usuario ejecutar "
        "`./scripts/configure-profile.sh` para respuestas personalizadas (100% local)._"
    )
