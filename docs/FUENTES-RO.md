# Fuentes de información y atribución

Cómo el MCP clasifica la información y qué implica para **Tenarius RO**.

## Referencia de época Tenarius

| Campo | Valor |
|-------|-------|
| **Era objetivo** | Pre-Renewal |
| **Episodio máximo de referencia** | 13.2 |
| **Servidor** | Tenarius RO (privado) |

Si una fuente es **Renewal** o **posterior al Ep. 13.2**, el MCP lo marca con advertencias.
Eso **no garantiza** que no aplique parcialmente, pero **sí obliga** al agente a avisar al jugador.

---

## Fuentes disponibles

| ID | Nombre | Tipo de servidor | ¿Aplica a Tenarius? |
|----|--------|------------------|---------------------|
| `tenarius` | Wiki Tenarius RO | Privado (Tenarius) | **Sí** — fuente primaria |
| `irowiki` | iRO Wiki | Oficial (Gravity / iRO) | **Verificar** — vanilla oficial |
| `fandom` | Ragnarok Fandom | Comunitaria (no oficial) | **Verificar** — puede mezclar eras |
| Web (Brave) | Búsqueda web | Variable | **Verificar / desconocido** |

---

## Herramientas MCP

### Tenarius (contenido del servidor)

| Tool | Uso |
|------|-----|
| `search_wiki` | Buscar en wiki Tenarius |
| `get_wiki_summary` | Resumen artículo Tenarius |
| `get_wiki_page` | Wikitext completo Tenarius |

### RO vanilla / referencia (Pre-Renewal)

| Tool | Uso |
|------|-----|
| `search_ro_reference` | iRO Wiki + Fandom con sesgo Pre-Renewal |
| `get_ro_reference_summary` | Resumen (`source_id`: `irowiki` o `fandom`) |
| `get_ro_reference_page` | Wikitext completo de referencia |
| `search_ro_web` | Referencias + web Brave (opcional `BRAVE_API_KEY`) |

---

## Metadatos en cada respuesta

Toda respuesta incluye un bloque como:

```
---
## Metadatos de fuente
- **Origen:** iRO Wiki
- **Servidor:** iRO — servidor oficial internacional (Gravity)
- **Era detectada / referencia:** Renewal o posterior — puede NO aplicar a Tenarius
- **Referencia Tenarius (Pre-Renewal, ~Ep. 13.2):** Verificar — confirmar en wiki/juego Tenarius
- **URL:** ...
- ⚠️ Posible contenido Renewal...
---
```

---

## Reglas para el agente (resumen)

1. **Custom Tenarius** → wiki Tenarius primero.
2. **RO vanilla** → `search_ro_reference` / `get_ro_reference_*`.
3. **Siempre decir:** servidor, era (Pre-Renewal / Renewal / mixto / desconocido).
4. **Si no estás seguro** si aplica a Tenarius → dilo explícitamente.
5. **Renewal o Ep. > 13.2** → destacar que puede no existir en Tenarius.

---

## Búsqueda web amplia (opcional)

Configura `BRAVE_API_KEY` para activar resultados extra en `search_ro_web`:

```bash
export BRAVE_API_KEY="tu-token-brave"
```

Sin clave, `search_ro_web` sigue funcionando con iRO Wiki y Fandom.

API Brave: https://brave.com/search/api/

---

## Usuarios de IA web (sin MCP)

Si no usan el MCP, deben pedir manualmente al chat que cite **servidor y era**.
Ver [USO-IA-WEB.md](./USO-IA-WEB.md) y el prompt actualizado en [PROMPT-IA-WEB.txt](./PROMPT-IA-WEB.txt).
