"""Cliente genérico MediaWiki."""

from __future__ import annotations

import httpx
from bs4 import BeautifulSoup

from tenarius_wiki_mcp.sources import WikiSource

USER_AGENT = (
    "TenariusWikiMCP/1.0 (community; unofficial; "
    "+https://github.com/Robgonzalez/tenarius-wiki-mcp)"
)
MAX_WIKITEXT_CHARS = 24_000


def strip_html(html: str) -> str:
    return BeautifulSoup(html, "html.parser").get_text(" ", strip=True)


def page_url(source: WikiSource, title: str) -> str:
    return f"{source.page_base_url}{title.replace(' ', '_')}"


def api_get(source: WikiSource, params: dict) -> dict:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    }
    with httpx.Client(timeout=30.0, headers=headers) as client:
        response = client.get(source.api_url, params=params)
        response.raise_for_status()
        return response.json()


def search(source: WikiSource, query: str, limit: int = 8) -> list[dict]:
    data = api_get(
        source,
        {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srlimit": limit,
            "utf8": "",
            "format": "json",
        },
    )
    return data.get("query", {}).get("search", [])


def get_summary(source: WikiSource, title: str) -> tuple[str, str, str]:
    """Returns (page_title, url, extract)."""
    data = api_get(
        source,
        {
            "action": "query",
            "titles": title,
            "prop": "extracts|info",
            "explaintext": "1",
            "exsectionformat": "plain",
            "inprop": "url",
            "format": "json",
        },
    )
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        raise LookupError(f"Página no encontrada: '{title}'")

    page = next(iter(pages.values()))
    if page.get("missing"):
        raise LookupError(f"Página no encontrada: '{title}'")

    page_title = page.get("title", title)
    url = page.get("fullurl", page_url(source, title))
    extract = page.get("extract", "").strip()
    return page_title, url, extract


def get_wikitext(source: WikiSource, title: str) -> tuple[str, str, str]:
    """Returns (display_title, url, wikitext)."""
    data = api_get(
        source,
        {
            "action": "parse",
            "page": title,
            "prop": "wikitext|displaytitle",
            "format": "json",
        },
    )
    if "error" in data:
        info = data["error"].get("info", "Página no encontrada")
        raise LookupError(f"Error al obtener '{title}': {info}")

    parsed = data.get("parse", {})
    wikitext = parsed.get("wikitext", {}).get("*", "")
    display_title = parsed.get("displaytitle", title)
    url = page_url(source, title)
    return display_title, url, wikitext
