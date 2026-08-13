"""Búsqueda web opcional (Brave Search API)."""

from __future__ import annotations

import os

import httpx

from tenarius_wiki_mcp.attribution import detect_episode_warnings, detect_era
from tenarius_wiki_mcp.mediawiki import USER_AGENT

BRAVE_API_URL = "https://api.search.brave.com/res/v1/web/search"


def brave_search(query: str, limit: int = 5) -> list[dict]:
    api_key = os.environ.get("BRAVE_API_KEY", "").strip()
    if not api_key:
        return []

    ro_query = f"{query} ragnarok online pre-renewal"
    with httpx.Client(timeout=20.0, headers={"User-Agent": USER_AGENT}) as client:
        response = client.get(
            BRAVE_API_URL,
            params={"q": ro_query, "count": limit},
            headers={"Accept": "application/json", "X-Subscription-Token": api_key},
        )
        response.raise_for_status()
        data = response.json()

    results = []
    for item in data.get("web", {}).get("results", []):
        title = item.get("title", "")
        url = item.get("url", "")
        snippet = item.get("description", "")
        hint = f"{title} {snippet} {url}"
        results.append(
            {
                "title": title,
                "url": url,
                "snippet": snippet,
                "era": detect_era(hint),
                "warnings": detect_episode_warnings(hint),
                "server_label": _guess_server_from_url(url),
                "tenarius_note": _tenarius_note_for_url(url),
            }
        )
    return results


def _guess_server_from_url(url: str) -> str:
    lower = url.lower()
    if "tenarius-ro.com" in lower:
        return "Tenarius RO (privado)"
    if "irowiki.org" in lower:
        return "iRO — oficial (Gravity)"
    if "fandom.com" in lower:
        return "Fandom — wiki comunitaria"
    if "ratemyserver.net" in lower:
        return "RateMyServer — referencia comunitaria (Pre-Renewal)"
    if "playragnarok.com" in lower or "ragnarokonline.com" in lower:
        return "Gravity / RO oficial"
    return "Origen web — servidor no identificado con certeza"


def _tenarius_note_for_url(url: str) -> str:
    lower = url.lower()
    if "tenarius-ro.com" in lower:
        return "Aplica a Tenarius (fuente del servidor)"
    return "Verificar si aplica a Tenarius (referencia externa)"
