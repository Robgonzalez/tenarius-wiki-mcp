# Tenarius Wiki MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-community-green.svg)](./CONTRIBUTING.md)

Servidor [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) **open source** para consultar la wiki pública de [Tenarius RO](https://tenarius-ro.com/wiki/).

- **IA local** (Cursor, Claude Desktop): instala el MCP y consulta con herramientas estructuradas.
- **IA web** (Claude.ai, ChatGPT, Gemini): usa el [prompt sin instalar nada](#opción-c--ia-web-sin-mcp).

> **⚠️ Proyecto comunitario — no oficial**
>
> Este repositorio **no está afiliado ni respaldado** por Tenarius RO, Gravity Co., Ltd. ni Ragnarok Online.
> Es una herramienta independiente, hecha por jugadores, para **facilitar el acceso** a la documentación
> oficial publicada en la wiki de Tenarius y a información del juego RO.
>
> Ver [DISCLAIMER.md](./DISCLAIMER.md) para el aviso legal completo.

## Qué es y qué no es

| ✅ Sí es | ❌ No es |
|---|---|
| Proyecto open source (MIT) | Producto oficial de Tenarius |
| Cliente de lectura de la wiki pública | Wiki, sitio web ni servicio de Tenarius |
| Herramienta para jugadores y agentes de IA | Afiliado a Gravity / Ragnarok Online |
| Facilitador de consultas sobre RO y Tenarius | Garantía de exactitud del contenido de la wiki |

**Ragnarok Online** es marca registrada de Gravity Co., Ltd. **Tenarius RO** es un servidor privado;
sus marcas y contenidos son de sus respectivos titulares. Los nombres se usan aquí solo de forma descriptiva.

## Cómo empezar

Elige según cómo uses la IA:

| Perfil | Qué hacer |
|--------|-----------|
| **IA local** (Cursor, Claude Desktop, OpenCode) | Instalar el MCP → [Opción A/B abajo](#opción-ab--ia-local-mcp) |
| **IA web** (Claude.ai, ChatGPT, Gemini en navegador) | Sin instalar nada → [Opción C abajo](#opción-c--ia-web-sin-mcp) |

---

## Opción A/B — IA local (MCP)

Para quien usa agentes en el **escritorio** con soporte MCP.

### Opción A — Pedirle al agente

> Clona el repo `tenarius-wiki-mcp`, ejecuta `./scripts/setup.sh` y configura el MCP para consultar la wiki de Tenarius.

Instrucciones para agentes en [`AGENTS.md`](./AGENTS.md).

### Opción B — Manual

```bash
git clone https://github.com/Robgonzalez/tenarius-wiki-mcp.git
cd tenarius-wiki-mcp
./scripts/setup.sh
```

Abre la carpeta en **Cursor** — [`.cursor/mcp.json`](./.cursor/mcp.json) ya registra el servidor.

---

## Opción C — IA web (sin MCP)

**Alternativa para quien no usa IA local** — Claude web, ChatGPT, Gemini, etc.
No hace falta clonar este repo ni instalar Python.

### Pasos

1. Abre tu chat en el navegador (con **navegación web** activada, si la tiene).
2. Copia y pega el prompt de abajo.
3. Escribe tu pregunta al final, donde dice `Mi pregunta:`.

### Prompt (copiar y pegar)

```
Eres un asistente para jugadores de Tenarius RO (servidor privado de Ragnarok Online).

FUENTE OBLIGATORIA para contenido de Tenarius: https://tenarius-ro.com/wiki/
- Usa navegación web para consultar artículos de esa wiki.
- NO mezcles con iRO, kRO, Divine Pride ni wikis genéricas para sistemas custom de Tenarius
  (Oficios, Sets crafteados, Tenarius Coin, rankings, Battle Royale, materiales custom).
- Para mecánicas vanilla de RO, indica que pueden diferir en Tenarius y prioriza la wiki del servidor.
- Cita la URL del artículo que usaste.
- Si no encuentras la respuesta en la wiki, dilo explícitamente.

Este asistente es comunitario y NO es oficial de Tenarius RO ni de Gravity / Ragnarok Online.

Mi pregunta: [escribe aquí tu duda]
```

### Si no navega bien

Abre el artículo en https://tenarius-ro.com/wiki/, copia el texto y pégalo en el chat con:
*"Respóndeme basándote SOLO en este contenido de la wiki de Tenarius."*

### Limitaciones vs MCP local

| | IA web (esta opción) | MCP local (Opción A/B) |
|---|---|---|
| Instalación | Ninguna | Clonar repo + setup |
| Búsqueda en wiki | Depende del chat | `search_wiki` estructurado |
| Mezcla otras fuentes | Posible | Menor riesgo |

Guía ampliada: [`docs/USO-IA-WEB.md`](./docs/USO-IA-WEB.md) · Prompt en texto plano: [`docs/PROMPT-IA-WEB.txt`](./docs/PROMPT-IA-WEB.txt)

> **Futuro:** planeamos hostear el MCP para que usuarios web tengan funcionalidad completa vía conector en Claude.
> Seguimiento en [`docs/ROADMAP.md`](./docs/ROADMAP.md).

---

| Herramienta | Descripción |
|---|---|
| `search_wiki` | Busca artículos por palabra clave |
| `get_wiki_summary` | Resumen legible en texto plano |
| `get_wiki_page` | Wikitext completo (tablas, recetas, stats) |

Flujo recomendado: `search_wiki` → `get_wiki_summary` → `get_wiki_page` (si necesitas detalle).

## Configuración por editor

### Cursor (proyecto)

Abre este repo como workspace. Listo.

### Cursor (global — desde cualquier proyecto)

Copia [`examples/cursor-global-mcp.json`](./examples/cursor-global-mcp.json) a `~/.cursor/mcp.json` y ajusta la ruta absoluta.

### Sin uv (solo Python)

```json
{
  "mcpServers": {
    "tenarius-wiki": {
      "command": "python3",
      "args": ["-m", "tenarius_wiki_mcp.server"],
      "cwd": "/ruta/absoluta/a/tenarius-wiki-mcp/src"
    }
  }
}
```

Instala antes: `pip install -r requirements.txt`

### Otros clientes

- Claude Desktop: [`examples/claude-desktop.json`](./examples/claude-desktop.json)
- OpenCode: [`examples/opencode.jsonc`](./examples/opencode.jsonc)

## Tenarius vs RO original

Este MCP consulta la **wiki de Tenarius** para contenido del servidor (Oficios, Sets crafteados,
Tenarius Coin, rankings, etc.). Para mecánicas base de RO, la wiki puede no bastar — y Tenarius
puede tener rates o stats distintos al RO oficial. **Prioriza la wiki de Tenarius** para dudas del servidor.

## Contribuir

Las contribuciones son bienvenidas. Ver [CONTRIBUTING.md](./CONTRIBUTING.md).

## Estructura

```
tenarius-wiki-mcp/
├── .cursor/mcp.json
├── AGENTS.md              # Instrucciones para agentes de IA
├── DISCLAIMER.md          # Aviso legal — no oficial
├── docs/
│   ├── USO-IA-WEB.md      # Guía IA web sin MCP (workaround actual)
│   ├── PROMPT-IA-WEB.txt  # Prompt reusable
│   └── ROADMAP.md         # Tasklist / plan MCP hosteado
├── src/tenarius_wiki_mcp/
├── examples/
└── scripts/setup.sh
```

## Requisitos

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recomendado) o pip
- Conexión a internet (API pública de MediaWiki)

## Licencia

[MIT](./LICENSE) — software libre. El contenido de la wiki pertenece a sus respectivos autores en Tenarius RO.

## Fuentes de datos

- Wiki consultada: [tenarius-ro.com/wiki](https://tenarius-ro.com/wiki/)
- Protocolo: [Model Context Protocol](https://modelcontextprotocol.io/)
