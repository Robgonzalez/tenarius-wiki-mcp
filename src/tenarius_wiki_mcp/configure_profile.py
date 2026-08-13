"""CLI para configurar el perfil de aventurero (100% local)."""

from __future__ import annotations

import argparse

from tenarius_wiki_mcp.profile import (
    PRIVACY_NOTICE,
    AdventurerProfile,
    load_profile,
    profile_path,
    save_profile,
)


def _prompt(label: str, default: str = "", required: bool = False) -> str:
    hint = f" [{default}]" if default else ""
    while True:
        value = input(f"{label}{hint}: ").strip()
        if not value and default:
            return default
        if value or not required:
            return value
        print("  (requerido — Enter para omitir si no es obligatorio)")


def _prompt_int(label: str, default: int | None = None) -> int | None:
    default_str = str(default) if default is not None else ""
    hint = f" [{default_str}]" if default_str else " [Enter=omitir]"
    while True:
        raw = input(f"{label}{hint}: ").strip()
        if not raw:
            return default
        try:
            return int(raw)
        except ValueError:
            print("  Introduce un número entero o Enter para omitir.")


def run_interactive(*, edit: bool = False) -> int:
    print(PRIVACY_NOTICE)
    print()

    existing = load_profile()
    if existing and not edit:
        print(f"Ya existe un perfil en: {profile_path()}")
        print(f"  Personaje: {existing.character_name} | Clase: {existing.class_name}")
        answer = input("¿Reconfigurar? [s/N]: ").strip().lower()
        if answer not in ("s", "si", "sí", "y", "yes"):
            print("Perfil sin cambios.")
            return 0
        base = existing
    elif existing:
        base = existing
        print(f"Editando perfil en: {profile_path()}\n")
    else:
        base = AdventurerProfile()
        print("Configuración opcional — Enter deja campos vacíos.\n")

    profile = AdventurerProfile(
        character_name=_prompt("Nombre del personaje", base.character_name),
        class_name=_prompt("Clase (ej. Professor, Lord Knight)", base.class_name),
        base_level=_prompt_int("Base level", base.base_level),
        job_level=_prompt_int("Job level", base.job_level),
        server=_prompt("Servidor", base.server or "Tenarius RO"),
        notable_gear=_prompt("Equipo notable (ej. Fighting Set, Snake Head)", base.notable_gear),
        play_style=_prompt("Estilo (ej. PvM solo, MVP, farming)", base.play_style),
        goals_short=_prompt("Objetivo corto plazo", base.goals_short),
        goals_medium=_prompt("Objetivo mediano plazo", base.goals_medium),
        language=_prompt("Idioma preferido (es/en)", base.language or "es"),
        notes=_prompt("Notas extra para el agente", base.notes),
    )

    if not profile.is_configured():
        print("\nNo ingresaste nombre ni clase — perfil no guardado.")
        print("Puedes ejecutar este script de nuevo cuando quieras.")
        return 0

    path = save_profile(profile)
    print(f"\n✓ Perfil guardado localmente en:\n  {path}")
    print("  Solo tu usuario en esta PC puede leerlo (permisos 600).")
    print("  Reinicia o recarga el MCP en Cursor para aplicar cambios.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Configura tu perfil de aventurero (100% local, open source)."
    )
    parser.add_argument("--edit", action="store_true", help="Editar perfil existente")
    parser.add_argument("--show-path", action="store_true", help="Mostrar ruta del perfil")
    args = parser.parse_args()

    if args.show_path:
        print(profile_path())
        raise SystemExit(0)

    raise SystemExit(run_interactive(edit=args.edit))
