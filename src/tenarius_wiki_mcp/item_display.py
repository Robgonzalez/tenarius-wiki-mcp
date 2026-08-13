"""Formato estándar para mostrar información de un ítem específico."""

from __future__ import annotations

from typing import Literal

TenariusApplicability = Literal["yes", "verify", "no", "unknown"]
ContentOrigin = Literal["tenarius_custom", "ro_vanilla", "mixed", "unknown"]


def format_item_card(
    *,
    name: str,
    item_type: str = "",
    server: str = "Tenarius RO",
    content_origin: ContentOrigin = "unknown",
    era: str = "Pre-Renewal",
    tenarius_applies: TenariusApplicability = "verify",
    slot: str = "",
    stats: str = "",
    set_name: str = "",
    set_pieces: str = "",
    set_combo: str = "",
    job_bonuses: str = "",
    requirements: str = "",
    obtain: str = "",
    warnings: str = "",
    source_url: str = "",
    notes: str = "",
) -> str:
    """Genera ficha markdown uniforme para un ítem concreto.

    El agente debe usar esta tool (o replicar el mismo formato) cada vez que
    mencione un ítem específico por nombre en la respuesta al jugador.
    """
    applies_label = {
        "yes": "Sí — contenido del servidor / confirmado Tenarius",
        "verify": "Verificar — confirmar en wiki o in-game",
        "no": "No aplica directamente a Tenarius",
        "unknown": "Desconocido — no afirmar sin fuente",
    }[tenarius_applies]

    origin_label = {
        "tenarius_custom": "Exclusivo Tenarius (custom)",
        "ro_vanilla": "RO original (vanilla)",
        "mixed": "Mixto / revisar fuente",
        "unknown": "Origen no determinado",
    }[content_origin]

    lines = [
        f"## 🎒 {name}",
        "",
        "| Campo | Valor |",
        "|-------|-------|",
        f"| **Servidor** | {server} |",
        f"| **Origen del contenido** | {origin_label} |",
        f"| **Era** | {era} |",
        f"| **¿Aplica a Tenarius?** | {applies_label} |",
    ]

    if item_type:
        lines.append(f"| **Tipo** | {item_type} |")
    if slot:
        lines.append(f"| **Slot** | {slot} |")
    if set_name:
        lines.append(f"| **Set** | {set_name} |")
    if set_pieces:
        lines.append(f"| **Piezas del set** | {set_pieces} |")
    if stats:
        lines.append(f"| **Stats (pieza)** | {stats} |")
    if set_combo:
        lines.append(f"| **Bonus combo (set completo)** | {set_combo} |")
    if job_bonuses:
        lines.append(f"| **Bonos por job/clase** | {job_bonuses} |")
    if requirements:
        lines.append(f"| **Requisitos** | {requirements} |")
    if obtain:
        lines.append(f"| **Obtención / craft** | {obtain} |")
    if warnings:
        lines.append(f"| **Advertencias** | {warnings} |")
    if source_url:
        lines.append(f"| **Fuente** | {source_url} |")

    lines.append("")
    if notes:
        lines.append(f"**Notas:** {notes}")
        lines.append("")

    lines.append(
        "_Stats exactos pueden diferir en el juego. Verifica in-game si la decisión es crítica._"
    )
    return "\n".join(lines)


def format_set_piece_cards(
    set_name: str,
    pieces: list[dict[str, str]],
    *,
    server: str = "Tenarius RO",
    content_origin: ContentOrigin = "tenarius_custom",
    era: str = "Pre-Renewal",
    tenarius_applies: TenariusApplicability = "yes",
    set_combo: str = "",
    job_bonuses: str = "",
    obtain: str = "",
    warnings: str = "",
    source_url: str = "",
) -> str:
    """Varias piezas de un mismo set en fichas encadenadas."""
    blocks = [
        f"# Set: {set_name}",
        "",
        format_item_card(
            name=set_name,
            item_type="Set de Equipamiento (combo)",
            server=server,
            content_origin=content_origin,
            era=era,
            tenarius_applies=tenarius_applies,
            set_pieces=", ".join(p.get("name", "?") for p in pieces),
            set_combo=set_combo,
            job_bonuses=job_bonuses,
            obtain=obtain,
            warnings=warnings,
            source_url=source_url,
        ),
    ]
    for piece in pieces:
        blocks.append("")
        blocks.append(
            format_item_card(
                name=piece.get("name", "Pieza"),
                item_type=piece.get("type", "Pieza de set"),
                server=server,
                content_origin=content_origin,
                era=era,
                tenarius_applies=tenarius_applies,
                slot=piece.get("slot", ""),
                stats=piece.get("stats", ""),
                set_name=set_name,
                source_url=source_url,
            )
        )
    return "\n".join(blocks)
