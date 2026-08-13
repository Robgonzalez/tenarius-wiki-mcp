# Uso con IA web (sin MCP)

Guía para jugadores que usan **Claude web**, **ChatGPT**, **Gemini** u otros chats en el navegador,
**sin instalar** el MCP ni clonar este repositorio.

> **Estado actual:** esta es la opción recomendada para IA web.
> Para funcionalidad completa (`search_wiki` → `get_wiki_summary` → `get_wiki_page`), ver
> [ROADMAP.md](./ROADMAP.md) — el MCP hosteado está planificado a futuro.

## Enfoque: wiki directa + reglas claras al agente

El chat debe usar **solo** la wiki pública de Tenarius como fuente para contenido del servidor:

**https://tenarius-ro.com/wiki/**

No mezclar con wikis genéricas de RO (iRO, kRO, Divine Pride) para sistemas exclusivos de Tenarius.

---

## Método A — Navegación web (recomendado)

Activa la búsqueda/navegación web del chat y pega un prompt como este:

```
Consulta SOLO la wiki de Tenarius RO: https://tenarius-ro.com/wiki/

Reglas:
- Para Oficios, Sets, Tenarius Coin, rankings, quests custom y mecánicas del servidor:
  usa únicamente tenarius-ro.com/wiki
- NO uses wikis genéricas de RO para contenido exclusivo de Tenarius
- Si no encuentras algo en la wiki, dilo explícitamente
- Indica la URL del artículo que usaste

Mi pregunta: [escribe aquí tu duda]
```

### Ejemplos de preguntas

- *¿Cómo funciona el Fighting Set y qué bonos da al Professor?*
- *¿Qué recompensa da el top 1 del ranking de Fisherman?*
- *¿Qué materiales necesito para craftear el Set Violent Gale?*

---

## Método B — Pegar el artículo en el chat

Si ya conoces la página o la encontraste en el navegador:

1. Abre el artículo en https://tenarius-ro.com/wiki/
2. Copia el contenido relevante (o toda la sección)
3. Pégalo en el chat con contexto:

```
Este texto viene de la wiki oficial de Tenarius RO (no es RO original genérico).
Respóndeme basándote SOLO en esto:

[pégalo aquí]

Mi pregunta: [...]
```

Útil cuando la IA no navega bien o el artículo es largo.

---

## Método C — Enlaces directos por tema

| Tema | Artículo wiki |
|------|----------------|
| Sets de equipamiento | [Set de Equipamiento](https://tenarius-ro.com/wiki/index.php/Set_de_Equipamiento) |
| Oficio pesca / ranking ASPD | [Fisherman (Pescador)](https://tenarius-ro.com/wiki/index.php/Fisherman_(Pescador)) |
| Oficios en general | Buscar "Oficios" en la wiki |
| Tenarius Coin / shop | Buscar en la wiki |

Prompt corto:

```
Lee este artículo de la wiki de Tenarius y explícame [tema]:
https://tenarius-ro.com/wiki/index.php/Nombre_del_artículo
```

---

## Qué distingue Tenarius vs RO original

En **cada respuesta**, el agente debe indicar:

| Campo | Valores |
|-------|---------|
| **Servidor** | Tenarius / iRO oficial / otro privado / desconocido |
| **Era** | Pre-Renewal / Renewal / mixto |
| **Episodio** | Tenarius ~13.2 — advertir si es posterior |
| **¿Aplica a Tenarius?** | sí / verificar / no / no sé |

| Tipo | Fuente |
|------|--------|
| Custom Tenarius (Oficios, Sets, Tenarius Coin, etc.) | **Wiki Tenarius** |
| RO vanilla Pre-Renewal | irowiki.org, ratemyserver.net |
| Renewal o Ep. > 13.2 | **Destacar** — puede no aplicar a Tenarius |

---

## Limitaciones vs MCP (por qué no es igual)

| | IA web (esta guía) | MCP hosteado (futuro) |
|---|---|---|
| Instalación | Ninguna | URL o conector en Claude |
| Búsqueda estructurada en wiki | Depende del chat | `search_wiki` garantizado |
| Resumen vs wikitext completo | Manual / inconsistente | `get_wiki_summary` / `get_wiki_page` |
| Mezcla de fuentes externas | Riesgo alto | Bajo (instrucciones en el servidor) |
| Tenarius custom vs RO original | Hay que recordárselo al agente | Reglas embebidas en el MCP |

---

## Prompt reusable (copiar y guardar)

Guarda este bloque en tus notas y reutilízalo:

Ver prompt completo en [`PROMPT-IA-WEB.txt`](./PROMPT-IA-WEB.txt).

```
Eres un asistente para jugadores de Tenarius RO (Pre-Renewal, ~Ep. 13.2).

FUENTES: wiki Tenarius + irowiki.org / ratemyserver.net para RO vanilla.

Indica SIEMPRE: servidor, era, si aplica a Tenarius, URLs.
Renewal o post-Ep.13.2 → DESTÁCALO.

Mi pregunta: [tu duda]
```

---

## Compatibilidad por plataforma

| Plataforma | Método A (web) | Método B (pegar) |
|------------|----------------|------------------|
| Claude.ai | ✅ con navegación | ✅ |
| ChatGPT | ✅ con browsing | ✅ |
| Gemini | ✅ según plan | ✅ |
| Copilot | ⚠️ variable | ✅ |

---

## Próximo paso del proyecto

Cuando el MCP esté **hosteado públicamente**, los usuarios web podrán conectarlo como
conector remoto en Claude (Customize → Connectors) y recuperar todas las herramientas.

Seguimiento: [ROADMAP.md](./ROADMAP.md)
