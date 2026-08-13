"""MCP server comunitario (no oficial) — Tenarius wiki + referencias RO Pre-Renewal."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from tenarius_wiki_mcp.attribution import format_source_block
from tenarius_wiki_mcp.mediawiki import (
    MAX_WIKITEXT_CHARS,
    get_summary,
    get_wikitext,
    page_url,
    search,
    strip_html,
)
from tenarius_wiki_mcp.sources import (
    ALL_SOURCES,
    RO_REFERENCE_SOURCES,
    TARGET_EPISODE_MAX,
    TARGET_ERA,
    TENARIUS,
)
from tenarius_wiki_mcp.web_search import brave_search

INSTRUCTIONS = f"""
Servidor MCP comunitario (NO OFICIAL). No afiliado a Tenarius RO, Gravity ni Ragnarok Online.

Contexto Tenarius: servidor privado **{TARGET_ERA}**, referencia hasta **Episodio {TARGET_EPISODE_MAX}**.

Reglas para el agente:
1. **Siempre** indica servidor, era (Pre-Renewal / Renewal / mixto) y si aplica a Tenarius.
2. Contenido **custom Tenarius** (Oficios, Sets, Tenarius Coin, rankings, etc.):
   → tools `search_wiki`, `get_wiki_summary`, `get_wiki_page`.
3. Mecánicas **vanilla RO** (clases, skills, items clásicos, quests oficiales):
   → `search_ro_reference` / `get_ro_reference_*` (iRO Wiki, Fandom).
4. Búsqueda web amplia: `search_ro_web` (opcional Brave API si BRAVE_API_KEY está configurada).
5. Si la fuente es **Renewal** o posterior al Ep. {TARGET_EPISODE_MAX}, **destácalo** — puede no existir en Tenarius.
6. Si no sabes el servidor o la era, dilo explícitamente; no asumas que aplica a Tenarius.
7. Flujo Tenarius: search_wiki → get_wiki_summary → get_wiki_page.
8. Flujo RO vanilla: search_ro_reference → get_ro_reference_summary → get_ro_reference_page.
""".strip()

mcp = FastMCP(
    "TenariusRO Wiki (unofficial)",
    instructions=INSTRUCTIONS,
)


def _resolve_source(source_id: str):
    source = ALL_SOURCES.get(source_id.lower())
    if not source:
        ids = ", ".join(sorted(ALL_SOURCES))
        raise ValueError(f"Fuente desconocida '{source_id}'. Válidas: {ids}")
    return source


# --- Tenarius (servidor privado) ---


@mcp.tool()
def search_wiki(query: str, limit: int = 8) -> str:
    """Busca artículos en la Wiki de Tenarius RO (contenido del servidor privado).

    Usar para Oficios, Sets, Tenarius Coin, quests custom, rankings, etc.

    Args:
        query: Términos de búsqueda (ej. "fighting set", "fisherman").
        limit: Cantidad máxima de resultados (1-20).
    """
    limit = max(1, min(limit, 20))
    try:
        results = search(TENARIUS, query, limit)
        if not results:
            return (
                format_source_block(TENARIUS)
                + f"No se encontraron resultados en Tenarius para '{query}'."
            )

        lines = [format_source_block(TENARIUS), f"## Resultados Tenarius para '{query}'"]
        for item in results:
            title = item["title"]
            snippet = strip_html(item.get("snippet", ""))
            url = page_url(TENARIUS, title)
            era_hint = f"{title} {snippet}"
            lines.append(
                f"- **{title}** — {snippet}\n  URL: {url}\n  "
                f"_Era:_ Pre-Renewal Tenarius | _Aplica a Tenarius:_ Sí"
            )
        lines.append("\nSiguiente: get_wiki_summary o get_wiki_page con título exacto.")
        return "\n".join(lines)
    except Exception as exc:
        return f"Error al buscar en wiki Tenarius: {exc}"


@mcp.tool()
def get_wiki_summary(title: str) -> str:
    """Resumen legible de un artículo de la Wiki de Tenarius RO.

    Args:
        title: Título exacto (ej. "Set de Equipamiento").
    """
    try:
        page_title, url, extract = get_summary(TENARIUS, title)
        if not extract:
            return (
                format_source_block(TENARIUS, url=url, content_hint=page_title)
                + f"Página '{page_title}' sin extracto. Usa get_wiki_page.\nURL: {url}"
            )
        header = format_source_block(TENARIUS, url=url, content_hint=extract)
        return f"{header}# {page_title}\n\n{extract}"
    except LookupError as exc:
        return str(exc)
    except Exception as exc:
        return f"Error al obtener resumen Tenarius: {exc}"


@mcp.tool()
def get_wiki_page(title: str) -> str:
    """Wikitext completo de un artículo de la Wiki de Tenarius RO.

    Args:
        title: Título exacto del artículo.
    """
    try:
        display_title, url, wikitext = get_wikitext(TENARIUS, title)
        if not wikitext:
            return format_source_block(TENARIUS, url=url) + f"Sin contenido.\nURL: {url}"

        truncated = len(wikitext) > MAX_WIKITEXT_CHARS
        body = wikitext[:MAX_WIKITEXT_CHARS] if truncated else wikitext
        header = format_source_block(TENARIUS, url=url, content_hint=body)
        footer = "\n\n[Contenido truncado]" if truncated else ""
        return f"{header}# {display_title}\n\n{body}{footer}"
    except LookupError as exc:
        return str(exc)
    except Exception as exc:
        return f"Error al obtener página Tenarius: {exc}"


# --- RO vanilla / referencia web ---


def _pre_renewal_query(query: str) -> str:
    return f"{query} pre-renewal classic episode 13"


def _search_ro_reference_body(query: str, limit: int) -> str:
    biased_query = _pre_renewal_query(query)
    sections: list[str] = [
        f"# Búsqueda RO de referencia: `{query}`",
        f"_Sesgo de búsqueda:_ Pre-Renewal / Ep. ≤ {TARGET_EPISODE_MAX}",
        "",
    ]

    any_result = False
    for source in RO_REFERENCE_SOURCES.values():
        try:
            results = search(source, biased_query, limit)
            if not results:
                results = search(source, query, max(1, limit // 2))

            sections.append(format_source_block(source))
            sections.append(f"## {source.name}")

            if not results:
                sections.append(f"Sin resultados para '{query}'.\n")
                continue

            any_result = True
            for item in results:
                title = item["title"]
                snippet = strip_html(item.get("snippet", ""))
                url = page_url(source, title)
                sections.append(
                    f"- **{title}** — {snippet}\n"
                    f"  URL: {url}\n"
                    f"  _Fuente:_ {source.server_label}\n"
                    f"  _Era (estimada):_ ver metadatos arriba\n"
                    f"  _Tenarius:_ {source.tenarius.value} — verificar en wiki Tenarius"
                )
            sections.append("")
        except Exception as exc:
            sections.append(f"Error en {source.name}: {exc}\n")

    if not any_result:
        sections.append(
            "No hubo resultados en wikis de referencia. Prueba `search_ro_web` "
            "o reformula la consulta."
        )
    else:
        sections.append(
            "Siguiente: get_ro_reference_summary(source_id, title) con source_id "
            "`irowiki` o `fandom`."
        )

    return "\n".join(sections)


@mcp.tool()
def search_ro_reference(query: str, limit: int = 6) -> str:
    """Busca información de Ragnarok Online en wikis de referencia (iRO Wiki, Fandom).

    Prioriza contexto Pre-Renewal (~Episodio 13.2). Cada resultado incluye servidor,
    era estimada y si debe verificarse en Tenarius.

    Args:
        query: Tema RO vanilla (ej. "Professor skills", "Assassin Cross", "MVP Amon Ra").
        limit: Resultados por fuente (1-10).
    """
    limit = max(1, min(limit, 10))
    return _search_ro_reference_body(query, limit)


@mcp.tool()
def get_ro_reference_summary(source_id: str, title: str) -> str:
    """Resumen de un artículo RO desde iRO Wiki o Fandom (referencia vanilla).

    Args:
        source_id: `irowiki` o `fandom`.
        title: Título exacto del artículo.
    """
    try:
        source = _resolve_source(source_id)
        if source.id == TENARIUS.id:
            return "Para Tenarius usa get_wiki_summary en lugar de get_ro_reference_summary."

        page_title, url, extract = get_summary(source, title)
        if not extract:
            return (
                format_source_block(source, url=url, content_hint=page_title)
                + f"Sin extracto en '{page_title}'. Prueba get_ro_reference_page.\nURL: {url}"
            )
        header = format_source_block(source, url=url, content_hint=extract)
        return f"{header}# {page_title}\n\n{extract}"
    except ValueError as exc:
        return str(exc)
    except LookupError as exc:
        return str(exc)
    except Exception as exc:
        return f"Error al obtener resumen RO: {exc}"


@mcp.tool()
def get_ro_reference_page(source_id: str, title: str) -> str:
    """Wikitext completo de referencia RO (irowiki / fandom).

    Args:
        source_id: `irowiki` o `fandom`.
        title: Título exacto del artículo.
    """
    try:
        source = _resolve_source(source_id)
        if source.id == TENARIUS.id:
            return "Para Tenarius usa get_wiki_page."

        display_title, url, wikitext = get_wikitext(source, title)
        if not wikitext:
            return format_source_block(source, url=url) + f"Sin contenido.\nURL: {url}"

        truncated = len(wikitext) > MAX_WIKITEXT_CHARS
        body = wikitext[:MAX_WIKITEXT_CHARS] if truncated else wikitext
        header = format_source_block(source, url=url, content_hint=body)
        footer = "\n\n[Contenido truncado]" if truncated else ""
        return f"{header}# {display_title}\n\n{body}{footer}"
    except ValueError as exc:
        return str(exc)
    except LookupError as exc:
        return str(exc)
    except Exception as exc:
        return f"Error al obtener página RO: {exc}"


@mcp.tool()
def search_ro_web(query: str, limit: int = 5) -> str:
    """Búsqueda web amplia sobre Ragnarok Online (Pre-Renewal / Ep. ≤ 13.2).

    1) Consulta wikis de referencia (iRO Wiki, Fandom).
    2) Si existe BRAVE_API_KEY, añade resultados Brave Search.

    Cada resultado indica servidor estimado, era y si aplica a Tenarius.

    Args:
        query: Tema a investigar.
        limit: Límite para búsqueda web Brave (1-10).
    """
    limit = max(1, min(limit, 10))
    sections = [
        f"# Búsqueda web RO: `{query}`",
        f"_Referencia Tenarius:_ {TARGET_ERA}, Episodio ≤ {TARGET_EPISODE_MAX}",
        "",
        "## Wikis de referencia",
        _search_ro_reference_body(query, limit=min(limit, 6)),
    ]

    web_results = brave_search(query, limit)
    sections.append("\n## Web (Brave Search)")
    if not web_results:
        sections.append(
            "Sin resultados web adicionales. "
            "(Opcional: configura BRAVE_API_KEY para búsqueda web amplia.)"
        )
    else:
        for item in web_results:
            warn = "\n  ".join(f"- {w}" for w in item.get("warnings", []))
            sections.append(
                f"- **{item['title']}**\n"
                f"  URL: {item['url']}\n"
                f"  _Servidor (estimado):_ {item['server_label']}\n"
                f"  _Era (estimada):_ {item['era']}\n"
                f"  _Tenarius:_ {item['tenarius_note']}\n"
                f"  {item.get('snippet', '')}"
                + (f"\n  {warn}" if warn else "")
            )

    sections.append(
        "\n**Recuerda:** indica siempre si la info es oficial, de un privado concreto, "
        "Renewal/post-13.2, o si no estás seguro de que aplique a Tenarius."
    )
    return "\n".join(sections)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
