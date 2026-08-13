"""Etiquetado de fuente, era y aplicabilidad a Tenarius."""

from __future__ import annotations

import re

from tenarius_wiki_mcp.sources import (
    TARGET_EPISODE_MAX,
    TARGET_ERA,
    TenariusApplicability,
    WikiSource,
)

_RENEWAL_MARKERS = (
    "renewal",
    "3rd class",
    "third class",
    "4th class",
    "fourth class",
    "expanded class",
    "rebellion",
    "kagerou",
    "oboro",
    "summoner",
    "star emperor",
    "soul reaper",
    "hyper novice",
    "dragon knight",
    "imperial guard",
    "episode 14",
    "episode 15",
    "episode 16",
    "episode 17",
    "episode 18",
    "episode 19",
    "episode 20",
)

_PRE_RENEWAL_MARKERS = (
    "pre-renewal",
    "pre renewal",
    "classic",
    "episode 13",
    "ep 13",
    "ep13",
    "transcendent",
    "transcendent class",
    "high priest",
    "professor",
    "stalker",
    "champion",
)

_POST_13_EPISODE = re.compile(r"episode\s*(1[4-9]|[2-9]\d)", re.I)
_EPISODE_13_2 = re.compile(r"episode\s*13\.2|ep\s*13\.2|13\.2", re.I)


def detect_era(text: str) -> str:
    lower = text.lower()
    has_pre = any(m in lower for m in _PRE_RENEWAL_MARKERS)
    has_renewal = any(m in lower for m in _RENEWAL_MARKERS)

    if has_pre and has_renewal:
        return "Mixto / ambiguo — revisar artículo"
    if has_renewal:
        return "Renewal o posterior — puede NO aplicar a Tenarius"
    if has_pre:
        return "Pre-Renewal (referencia alineada con Tenarius)"
    return "Era no determinada — verificar en fuente y en juego"


def detect_episode_warnings(text: str) -> list[str]:
    warnings: list[str] = []
    lower = text.lower()

    if _POST_13_EPISODE.search(lower):
        warnings.append(
            f"⚠️ Menciona contenido posterior al Episodio {TARGET_EPISODE_MAX} "
            f"(referencia Tenarius: hasta ~{TARGET_EPISODE_MAX})."
        )
    elif _EPISODE_13_2.search(lower):
        warnings.append(
            f"ℹ️ Contenido alineado con Episodio {TARGET_EPISODE_MAX} (rango de referencia Tenarius)."
        )

    if any(m in lower for m in _RENEWAL_MARKERS):
        warnings.append(
            "⚠️ Posible contenido **Renewal** o post-Pre-Renewal. "
            "Destácalo al usuario; puede no existir o diferir en Tenarius."
        )

    return warnings


def tenarius_applicability_label(value: TenariusApplicability) -> str:
    return {
        TenariusApplicability.YES: "Sí — fuente del servidor Tenarius",
        TenariusApplicability.VERIFY: "Verificar — referencia RO; confirmar en wiki/juego Tenarius",
        TenariusApplicability.NO: "No aplica directamente a Tenarius",
        TenariusApplicability.UNKNOWN: "Desconocido — no se puede afirmar si aplica a Tenarius",
    }[value]


def format_source_block(
    source: WikiSource,
    *,
    url: str | None = None,
    content_hint: str = "",
) -> str:
    era = detect_era(content_hint) if content_hint else source.era_default
    warnings = detect_episode_warnings(content_hint) if content_hint else []

    lines = [
        "---",
        "## Metadatos de fuente",
        f"- **Origen:** {source.name}",
        f"- **Servidor:** {source.server_label} ({source.server_kind.value})",
        f"- **Era detectada / referencia:** {era}",
        f"- **Referencia Tenarius ({TARGET_ERA}, ~Ep. {TARGET_EPISODE_MAX}):** "
        f"{tenarius_applicability_label(source.tenarius)}",
        f"- **Notas:** {source.notes}",
    ]
    if url:
        lines.append(f"- **URL:** {url}")
    for warning in warnings:
        lines.append(f"- {warning}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)
