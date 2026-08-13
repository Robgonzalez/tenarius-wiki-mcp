# AGENTS.md — Tenarius Wiki MCP

## ⚠️ No oficial

Proyecto **open source comunitario**. No es oficial de Tenarius RO, Gravity ni Ragnarok Online.

**Tenarius:** Pre-Renewal, referencia hasta **Episodio 13.2**.

Al responder, **siempre** indica: servidor, era (Pre-Renewal/Renewal), y si aplica a Tenarius.

Ver [DISCLAIMER.md](./DISCLAIMER.md) · [docs/FUENTES-RO.md](./docs/FUENTES-RO.md)

## Usuarios de IA web (sin MCP)

→ [`docs/USO-IA-WEB.md`](./docs/USO-IA-WEB.md) · [`docs/PROMPT-IA-WEB.txt`](./docs/PROMPT-IA-WEB.txt)

## Herramientas MCP

### Tenarius (custom del servidor)

| Tool | Cuándo |
|------|--------|
| `search_wiki` | Oficios, Sets, Tenarius Coin, quests custom |
| `get_wiki_summary` | Respuesta rápida Tenarius |
| `get_wiki_page` | Tablas, recetas, stats Tenarius |

### RO vanilla (Pre-Renewal)

| Tool | Cuándo |
|------|--------|
| `search_ro_reference` | Clases, skills, items, MVPs vanilla RO |
| `get_ro_reference_summary` | Resumen (`source_id`: `irowiki` o `fandom`) |
| `get_ro_reference_page` | Detalle wikitext referencia |
| `search_ro_web` | Búsqueda amplia (+ Brave si `BRAVE_API_KEY`) |

## Reglas de consulta

| Tipo | Fuente | Aplica Tenarius |
|------|--------|-----------------|
| Custom Tenarius | Wiki Tenarius | **Sí** |
| RO vanilla Pre-Renewal | irowiki / fandom | **Verificar** |
| Renewal / Ep. > 13.2 | Cualquiera | **Advertir** — puede no aplicar |
| Servidor privado desconocido | Web | **Decir que no se sabe** |

**No mezclar** wikis genéricas con sistemas exclusivos de Tenarius.

## Instalación rápida

1. Clonar repo · `uv sync` o `pip install -r requirements.txt`
2. Registrar MCP (`.cursor/mcp.json` o global)
3. Reiniciar editor
4. Verificar tools listadas arriba

## Flujos

- Tenarius: `search_wiki` → `get_wiki_summary` → `get_wiki_page`
- RO vanilla: `search_ro_reference` → `get_ro_reference_summary` → `get_ro_reference_page`
