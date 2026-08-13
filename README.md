# Tenarius Wiki MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-community-green.svg)](./CONTRIBUTING.md)

Servidor [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) **open source** para consultar la wiki pública de [Tenarius RO](https://tenarius-ro.com/wiki/) desde agentes de IA (Cursor, Claude Desktop, OpenCode, etc.).

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

## Instalación rápida

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

## Herramientas MCP

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
