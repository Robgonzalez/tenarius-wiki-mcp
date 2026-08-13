"""MCP server comunitario (no oficial) para consultar la wiki pública de Tenarius RO."""

from __future__ import annotations

import httpx
from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP

BASE_API_URL = "https://tenarius-ro.com/wiki/api.php"
WIKI_BASE_URL = "https://tenarius-ro.com/wiki/index.php"
MAX_WIKITEXT_CHARS = 24_000
USER_AGENT = "TenariusWikiMCP/1.0 (community; unofficial; +https://github.com/Robgonzalez/tenarius-wiki-mcp)"

INSTRUCTIONS = """
Servidor MCP comunitario (NO OFICIAL) que consulta la wiki pública de Tenarius RO.
No está afiliado a Tenarius RO, Gravity Co., Ltd. ni Ragnarok Online.

Reglas para el agente:
1. Deja claro al usuario que este MCP es una herramienta comunitaria, no un producto oficial.
2. Usa estas herramientas para contenido de Tenarius: Oficios, Sets de Equipamiento,
   Tenarius Coin, quests custom, hats, pets, Battle Royale, rankings, materiales custom, etc.
3. NO mezcles datos de wikis genéricas de RO (iRO, kRO, Divine Pride) para sistemas custom
   de Tenarius. Si no encuentras algo aquí, dilo explícitamente.
4. La información puede estar desactualizada; recomienda verificar en el juego si es crítico.
5. Flujo recomendado: search_wiki → get_wiki_summary (lectura rápida) → get_wiki_page (detalle).
6. Los títulos de página suelen estar en español (ej. "Fisherman (Pescador)", "Set de Equipamiento").
""".strip()

mcp = FastMCP(
    "TenariusRO Wiki (unofficial)",
    instructions=INSTRUCTIONS,
)


def _api_get(params: dict) -> dict:
    with httpx.Client(
        timeout=30.0,
        headers={"User-Agent": USER_AGENT},
    ) as client:
        response = client.get(BASE_API_URL, params=params)
        response.raise_for_status()
        return response.json()


def _strip_html(html: str) -> str:
    return BeautifulSoup(html, "html.parser").get_text(" ", strip=True)


@mcp.tool()
def search_wiki(query: str, limit: int = 8) -> str:
    """Busca artículos en la Wiki de Tenarius RO.

    Args:
        query: Términos de búsqueda (ej. "fighting set", "fisherman", "oficios").
        limit: Cantidad máxima de resultados (1-20).
    """
    limit = max(1, min(limit, 20))
    try:
        data = _api_get(
            {
                "action": "query",
                "list": "search",
                "srsearch": query,
                "srlimit": limit,
                "utf8": "",
                "format": "json",
            }
        )
        search_results = data.get("query", {}).get("search", [])

        if not search_results:
            return f"No se encontraron resultados para '{query}'."

        lines = [f"Resultados para '{query}' ({len(search_results)}):"]
        for item in search_results:
            title = item["title"]
            snippet = _strip_html(item.get("snippet", ""))
            url = f"{WIKI_BASE_URL}/{title.replace(' ', '_')}"
            lines.append(f"- **{title}** — {snippet}\n  URL: {url}")

        lines.append("\nUsa get_wiki_summary o get_wiki_page con el título exacto.")
        return "\n".join(lines)
    except Exception as exc:
        return f"Error al buscar en la wiki: {exc}"


@mcp.tool()
def get_wiki_summary(title: str) -> str:
    """Obtiene un resumen legible de una página de la Wiki de Tenarius RO.

    Ideal para respuestas rápidas. Para tablas, wikitext completo o detalles finos,
    usa get_wiki_page.

    Args:
        title: Título exacto del artículo (ej. "Set de Equipamiento").
    """
    try:
        data = _api_get(
            {
                "action": "query",
                "titles": title,
                "prop": "extracts|info",
                "explaintext": "1",
                "exsectionformat": "plain",
                "inprop": "url",
                "format": "json",
            }
        )

        pages = data.get("query", {}).get("pages", {})
        if not pages:
            return f"Página no encontrada: '{title}'. Prueba search_wiki primero."

        page = next(iter(pages.values()))
        if page.get("missing"):
            return f"Página no encontrada: '{title}'. Prueba search_wiki primero."

        extract = page.get("extract", "").strip()
        page_title = page.get("title", title)
        url = page.get("fullurl", f"{WIKI_BASE_URL}/{title.replace(' ', '_')}")

        if not extract:
            return (
                f"Página '{page_title}' existe pero no tiene extracto de texto.\n"
                f"URL: {url}\n"
                "Usa get_wiki_page para el wikitext completo."
            )

        return f"# {page_title}\n\nURL: {url}\n\n{extract}"
    except Exception as exc:
        return f"Error al obtener resumen: {exc}"


@mcp.tool()
def get_wiki_page(title: str) -> str:
    """Obtiene el wikitext completo de una página de la Wiki de Tenarius RO.

    Útil para tablas de stats, recetas, listas de items y contenido detallado.

    Args:
        title: Título exacto del artículo.
    """
    try:
        data = _api_get(
            {
                "action": "parse",
                "page": title,
                "prop": "wikitext|displaytitle",
                "format": "json",
            }
        )

        if "error" in data:
            info = data["error"].get("info", "Página no encontrada")
            return f"Error al obtener la página '{title}': {info}"

        parsed = data.get("parse", {})
        wikitext = parsed.get("wikitext", {}).get("*", "")
        display_title = parsed.get("displaytitle", title)
        url = f"{WIKI_BASE_URL}/{title.replace(' ', '_')}"

        if not wikitext:
            return f"La página '{display_title}' no tiene contenido.\nURL: {url}"

        truncated = False
        if len(wikitext) > MAX_WIKITEXT_CHARS:
            wikitext = wikitext[:MAX_WIKITEXT_CHARS]
            truncated = True

        header = f"# {display_title}\n\nURL: {url}\n\n"
        footer = "\n\n[Contenido truncado por límite de tamaño]" if truncated else ""
        return header + wikitext + footer
    except Exception as exc:
        return f"Error al obtener contenido: {exc}"


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
