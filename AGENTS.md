# AGENTS.md — Tenarius Wiki MCP

## ⚠️ No oficial

Este repositorio es un proyecto **open source comunitario**. **No es oficial** de Tenarius RO,
Gravity Co., Ltd. ni Ragnarok Online. Solo facilita consultar la wiki pública de Tenarius.

Al responder al usuario, **no presentes este MCP como producto o servicio oficial** de Tenarius.
Si citas información, indica que proviene de la wiki de Tenarius y puede estar desactualizada.

Ver [DISCLAIMER.md](./DISCLAIMER.md).

## Instalación rápida

Si el usuario pide agregar este repo o consultar info de Tenarius:

1. **Clonar** el repositorio (o abrirlo como workspace).
2. **Instalar dependencias:** `uv sync` o `pip install -r requirements.txt`
3. **Registrar el MCP:**
   - **Cursor:** `.cursor/mcp.json` o bloque en `~/.cursor/mcp.json`
   - **OpenCode:** `examples/opencode.jsonc`
   - **Claude Desktop:** `examples/claude-desktop.json`
4. **Reiniciar** el editor / recargar MCP servers.
5. **Verificar** herramientas: `search_wiki`, `get_wiki_summary`, `get_wiki_page`.

### Config mínima Cursor (sin uv)

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

## Reglas de consulta (Tenarius vs RO original)

| Tipo de contenido | Fuente correcta |
|---|---|
| Oficios, Sets crafteados, Tenarius Coin, rankings, Battle Royale, materiales custom | **Wiki de Tenarius** (este MCP) |
| Clases/skills vanilla, headgears clásicos, mecánicas base de RO | RO original — **verificar stats/rates en Tenarius** |
| Builds meta, drops, fórmulas del servidor | **Wiki de Tenarius primero** |

No mezclar wikis genéricas (iRO, kRO, Divine Pride) con sistemas exclusivos de Tenarius.
Si la wiki no tiene la respuesta, dilo explícitamente.

## Flujo de herramientas

1. `search_wiki("término")`
2. `get_wiki_summary("Título exacto")`
3. `get_wiki_page("Título exacto")` — solo si necesitas tablas o detalle

## Prompt sugerido para el usuario

> Agrega el repo open source `tenarius-wiki-mcp` (no oficial de Tenarius), configura el MCP
> y consúltame sobre [tema] usando la wiki de Tenarius.
