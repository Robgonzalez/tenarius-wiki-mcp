# Roadmap — tenarius-wiki-mcp

Plan de evolución del proyecto. Actualizar al completar tareas.

**Estrategia actual:** usuarios de IA web usan [USO-IA-WEB.md](./USO-IA-WEB.md) (workaround sin MCP).
**Meta a futuro:** MCP hosteado con funcionalidad completa para Claude web y otros clientes remotos.

---

## Fase 1 — Disponible hoy ✅

- [x] Servidor MCP local (stdio) para Cursor / Claude Desktop
- [x] Herramientas Tenarius: `search_wiki`, `get_wiki_summary`, `get_wiki_page`
- [x] Herramientas RO referencia Pre-Renewal: `search_ro_reference`, `get_ro_reference_*`, `search_ro_web`
- [x] Metadatos de fuente (servidor, era, aplicabilidad Tenarius) en cada respuesta
- [x] Perfil de aventurero local opcional (`configure-profile.sh`, `get_adventurer_profile`)
- [x] Repo open source en GitHub
- [x] Disclaimer: proyecto comunitario, no oficial
- [x] Guía IA web sin MCP → [USO-IA-WEB.md](./USO-IA-WEB.md)

---

## Fase 2 — IA web (workaround) 🔄 En uso

Documentación y difusión del método sin instalación.

- [x] Crear guía `docs/USO-IA-WEB.md`
- [x] Prompts reusables para Claude / ChatGPT / Gemini
- [x] Tabla Tenarius custom vs RO original
- [x] Guía Cursor gratis + MCP: `docs/GUIA-CURSOR-MCP.md` (README Opción D)
- [ ] Añadir enlace en descripción del repo de GitHub
- [ ] Compartir prompt reusable en Discord/comunidad Tenarius (cuando aplique)
- [ ] Recopilar feedback: ¿qué preguntas fallan más sin MCP?

---

## Fase 3 — MCP remoto (objetivo ideal) 📋 Pendiente

Hostear el MCP para que usuarios web tengan **todas** las características funcionales.

### 3.1 Código

- [ ] Añadir flag CLI `--transport streamable-http` (FastMCP)
- [ ] Variables de entorno: `HOST`, `PORT`, `MCP_PATH` (default `/mcp`)
- [ ] Health check endpoint (`/health`) para el hosting
- [ ] Rate limiting básico (por IP o API key)
- [ ] Logging de requests (sin datos sensibles)

### 3.2 Seguridad y operación

- [ ] Evaluar auth opcional vía header `x-api-key` (abuse prevention)
- [ ] Documentar límites de uso comunitario
- [ ] Monitoreo de uptime (UptimeRobot o similar)
- [ ] Política de costos: Fly.io / Railway / Render / Cloudflare

### 3.3 Deploy

- [ ] Elegir plataforma de hosting (recomendación: Fly.io o Railway)
- [ ] Crear `docs/DEPLOY.md` con pasos reproducibles
- [ ] Dockerfile o config de deploy
- [ ] CI: deploy automático desde `main` (opcional)
- [ ] URL pública estable (ej. `https://tenarius-wiki-mcp.fly.dev/mcp`)

### 3.4 Integración Claude web

- [ ] Probar conector en Claude: Customize → Connectors → Custom → Web
- [ ] Documentar paso a paso con capturas o GIF
- [ ] Verificar que Anthropic alcanza la URL (IPs públicas, HTTPS)
- [ ] Publicar URL comunitaria en README cuando esté estable

### 3.5 Otros clientes web

- [ ] Documentar config Cursor con `streamable-http` remoto
- [ ] Evaluar ChatGPT / Gemini si soportan MCP remoto en el futuro

---

## Fase 4 — Mejoras opcionales 💡 Ideas

- [ ] Caché de respuestas frecuentes (reducir carga a la wiki)
- [ ] Tool extra: listar categorías principales de la wiki
- [ ] README en inglés
- [ ] Issue templates en GitHub (bug / idea / pregunta wiki)
- [ ] Badge "Community MCP" en README

---

## Comparativa de fases

| Capacidad | Fase 2 (IA web) | Fase 3 (MCP hosteado) |
|-----------|-----------------|------------------------|
| Sin instalar nada | ✅ | ✅ (solo pegar URL) |
| Búsqueda wiki fiable | ⚠️ | ✅ |
| Resumen estructurado | ⚠️ | ✅ |
| Wikitext completo | ⚠️ | ✅ |
| Reglas Tenarius embebidas | Manual (prompt) | ✅ en el servidor |
| Claude.ai web | ✅ workaround | ✅ conector nativo |

---

## Notas

- **Prioridad inmediata:** Fase 2 (difundir workaround mientras no hay host).
- **Prioridad media:** Fase 3 cuando haya tiempo/recursos para mantener un servicio público.
- El workaround de Fase 2 **no se depreca**: sigue siendo útil para quien no quiera conectores.

Última actualización: 2026-08-13
