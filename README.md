# Tenarius Wiki MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-community-green.svg)](./CONTRIBUTING.md)

Servidor [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) **open source** para consultar:

- **Wiki Tenarius RO** — contenido del servidor privado
- **Referencias RO Pre-Renewal** — iRO Wiki, Fandom y web (hasta ~Episodio 13.2)

Cada respuesta indica **servidor**, **era** (Pre-Renewal / Renewal) y **si aplica a Tenarius**.

- **IA local** (Cursor, Claude Desktop): instala el MCP y consulta con herramientas estructuradas.
- **IA web** (Claude.ai, ChatGPT, Gemini): [prompt rápido](#opción-c--ia-web-sin-mcp) o [instalar Cursor gratis](#opción-d--de-ia-web-a-cursor-gratis--mcp-completo) para MCP completo.

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
| **IA web** (Claude.ai, ChatGPT, Gemini) | Prompt rápido → [Opción C](#opción-c--ia-web-sin-mcp) |
| **IA web pero quieres MCP completo (gratis)** | Instalar **Cursor** + MCP → [Opción D](#opción-d--de-ia-web-a-cursor-gratis--mcp-completo) |

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

### Perfil de aventurero (opcional, 100% local)

Durante `./scripts/setup.sh` puedes configurar tu personaje. Mejora builds y recomendaciones **sin enviar datos a internet**:

- Guardado en `~/.config/tenarius-wiki-mcp/adventurer-profile.json`
- Open source, sin fines comerciales — solo tu PC lee el archivo
- Tool MCP: `get_adventurer_profile`

```bash
./scripts/configure-profile.sh      # configurar o reconfigurar
./scripts/configure-profile.sh --edit
```

Detalle: [`docs/PERFIL-AVENTURERO.md`](./docs/PERFIL-AVENTURERO.md)

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
Eres un asistente para jugadores de Tenarius RO (servidor privado Pre-Renewal, ~Ep. 13.2).

FUENTES:
1) Contenido Tenarius (Oficios, Sets, Tenarius Coin, custom): https://tenarius-ro.com/wiki/
2) RO vanilla Pre-Renewal: irowiki.org, ratemyserver.net (verificar era)

REGLAS:
- Indica SIEMPRE: servidor (Tenarius / iRO oficial / otro privado / desconocido), era (Pre-Renewal o Renewal), y si aplica a Tenarius.
- Si es Renewal o posterior al Ep. 13.2, DESTÁCALO — puede no existir en Tenarius.
- NO mezcles wikis genéricas para sistemas custom de Tenarius.
- Si no estás seguro del servidor o la era, dilo explícitamente.
- Cita URLs usadas.

No oficial de Tenarius ni Gravity.

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

Guía ampliada: [`docs/USO-IA-WEB.md`](./docs/USO-IA-WEB.md) · Prompt: [`docs/PROMPT-IA-WEB.txt`](./docs/PROMPT-IA-WEB.txt)

> **¿Quieres más que un prompt?** Instala **Cursor gratis** (solo correo) y el MCP completo: [Opción D](#opción-d--de-ia-web-a-cursor-gratis--mcp-completo).

> **Futuro:** MCP hosteado en la nube para conectar desde Claude web sin instalar nada.
> Seguimiento en [`docs/ROADMAP.md`](./docs/ROADMAP.md).

---

## Opción D — De IA web a Cursor (gratis) + MCP completo

**Para jugadores que usan ChatGPT/Claude en el navegador** y quieren un **agente de consultas** con wiki Tenarius, referencias RO y perfil local — sin pagar licencias de IDE.

### Resumen (5 minutos)

1. **Descargar Cursor** — [cursor.com](https://cursor.com) · registro **gratis con tu correo**
2. **Crear carpeta** y clonar este repo:
   ```bash
   mkdir -p ~/TenariusRO && cd ~/TenariusRO
   git clone https://github.com/Robgonzalez/tenarius-wiki-mcp.git
   ```
3. **Abrir en Cursor** — `File → Open Folder` → carpeta `tenarius-wiki-mcp`
4. **Instalar MCP** — terminal en Cursor: `./scripts/setup.sh`
5. **Reiniciar Cursor** → Settings → Tools & MCP → verificar `tenarius-wiki` activo
6. **Preguntar al agente** — ej.: *"¿Cómo funciona el Fighting Set en Tenarius?"*

### Guía paso a paso (publicación interna)

📖 **[`docs/GUIA-CURSOR-MCP.md`](./docs/GUIA-CURSOR-MCP.md)** — instalación de Cursor, carpeta de proyecto, MCP, perfil de aventurero y primeras consultas.

Incluye solución de problemas y notas de privacidad (perfil 100% local).

---

## Herramientas MCP

### Tenarius (servidor privado)

| Herramienta | Descripción |
|---|---|
| `search_wiki` | Busca en wiki Tenarius |
| `get_wiki_summary` | Resumen legible |
| `get_wiki_page` | Wikitext completo |

Flujo: `search_wiki` → `get_wiki_summary` → `get_wiki_page`

### RO vanilla / referencia (Pre-Renewal ~ Ep. 13.2)

| Herramienta | Descripción |
|---|---|
| `search_ro_reference` | iRO Wiki + Fandom (sesgo Pre-Renewal) |
| `get_ro_reference_summary` | Resumen (`source_id`: `irowiki` o `fandom`) |
| `get_ro_reference_page` | Wikitext de referencia |
| `search_ro_web` | Referencias + web (opcional `BRAVE_API_KEY`) |
| `get_adventurer_profile` | Perfil local del jugador (100% en tu PC) |

Todas las respuestas incluyen **metadatos de fuente** (servidor, era, aplicabilidad a Tenarius).

Detalle: [`docs/FUENTES-RO.md`](./docs/FUENTES-RO.md)

---

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

### Búsqueda web amplia (opcional)

```bash
export BRAVE_API_KEY="tu-token"   # activa resultados extra en search_ro_web
```

---

## Tenarius vs RO original

| Contenido | Fuente MCP |
|-----------|------------|
| Oficios, Sets, Tenarius Coin, custom | Wiki Tenarius |
| Clases/skills/items vanilla RO | `search_ro_reference` (Pre-Renewal) |
| ¿Aplica a Tenarius? | Siempre en metadatos — **verificar** si es referencia externa |

Tenarius es **Pre-Renewal (~Ep. 13.2)**. Info **Renewal** o de **otros privados** debe marcarse como tal.

## Contribuir

Las contribuciones son bienvenidas. Ver [CONTRIBUTING.md](./CONTRIBUTING.md).

## Estructura

```
tenarius-wiki-mcp/
├── .cursor/mcp.json
├── AGENTS.md              # Instrucciones para agentes de IA
├── DISCLAIMER.md          # Aviso legal — no oficial
├── docs/
│   ├── USO-IA-WEB.md      # Guía IA web sin MCP
│   ├── GUIA-CURSOR-MCP.md # Cursor gratis + MCP (desde IA web)
│   ├── PROMPT-IA-WEB.txt
│   ├── FUENTES-RO.md      # Servidores, eras, atribución
│   ├── PERFIL-AVENTURERO.md # Perfil local (privacidad)
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
