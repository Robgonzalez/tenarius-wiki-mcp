"""Fuentes de consulta: Tenarius, RO oficial y referencias web."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ServerKind(str, Enum):
    OFFICIAL = "official"
    PRIVATE = "private"
    COMMUNITY = "community"
    UNKNOWN = "unknown"


class TenariusApplicability(str, Enum):
    YES = "yes"
    VERIFY = "verify"
    NO = "no"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class WikiSource:
    id: str
    name: str
    api_url: str
    page_base_url: str
    server_kind: ServerKind
    server_label: str
    era_default: str
    tenarius: TenariusApplicability
    notes: str


TENARIUS = WikiSource(
    id="tenarius",
    name="Wiki Tenarius RO",
    api_url="https://tenarius-ro.com/wiki/api.php",
    page_base_url="https://tenarius-ro.com/wiki/index.php/",
    server_kind=ServerKind.PRIVATE,
    server_label="Tenarius RO (servidor privado)",
    era_default="Pre-Renewal (según época del servidor)",
    tenarius=TenariusApplicability.YES,
    notes="Fuente primaria para mecánicas y contenido custom de Tenarius.",
)

IRO_WIKI = WikiSource(
    id="irowiki",
    name="iRO Wiki",
    api_url="https://irowiki.org/w/api.php",
    page_base_url="https://irowiki.org/wiki/",
    server_kind=ServerKind.OFFICIAL,
    server_label="iRO — servidor oficial internacional (Gravity)",
    era_default="Mixto (contiene Pre-Renewal y Renewal)",
    tenarius=TenariusApplicability.VERIFY,
    notes=(
        "Referencia vanilla RO oficial. Verificar en wiki Tenarius antes de aplicar stats, "
        "drops o disponibilidad."
    ),
)

FANDOM_WIKI = WikiSource(
    id="fandom",
    name="Ragnarok Fandom Wiki",
    api_url="https://ragnarok.fandom.com/api.php",
    page_base_url="https://ragnarok.fandom.com/wiki/",
    server_kind=ServerKind.COMMUNITY,
    server_label="Fandom — wiki comunitaria (no oficial)",
    era_default="Mixto (a menudo Renewal o genérico)",
    tenarius=TenariusApplicability.VERIFY,
    notes="Wiki fan. Puede mezclar eras o servidores. Contrastar con Tenarius e iRO Wiki.",
)

RO_REFERENCE_SOURCES: dict[str, WikiSource] = {
    IRO_WIKI.id: IRO_WIKI,
    FANDOM_WIKI.id: FANDOM_WIKI,
}

ALL_SOURCES: dict[str, WikiSource] = {
    TENARIUS.id: TENARIUS,
    **RO_REFERENCE_SOURCES,
}

# Referencia de época para Tenarius (Pre-Renewal ~ hasta Episodio 13.2)
TARGET_ERA = "Pre-Renewal"
TARGET_EPISODE_MAX = "13.2"
