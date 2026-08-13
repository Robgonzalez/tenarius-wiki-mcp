# Contribuir

¡Gracias por interesarte en **tenarius-wiki-mcp**! Este es un proyecto **open source** (MIT)
creado por jugadores, para jugadores.

## Antes de contribuir

Lee [DISCLAIMER.md](./DISCLAIMER.md): este proyecto **no es oficial** de Tenarius RO ni de Gravity /
Ragnarok Online. Contribuyes bajo esa premisa.

## Cómo puedes ayudar

- **Issues:** reportar bugs, mejoras de documentación o ideas de herramientas MCP
- **Pull requests:** correcciones de código, tests, traducciones, ejemplos de config para más editores
- **Documentación:** aclarar Tenarius custom vs RO original, casos de uso, guías de instalación

## Desarrollo local

```bash
git clone <url-del-repo>
cd tenarius-wiki-mcp
./scripts/setup.sh
uv run tenarius-wiki-mcp
```

## Estilo

- Python 3.10+, tipado cuando aporte claridad
- Cambios mínimos y enfocados (no mezclar refactors grandes con fixes pequeños)
- README y comentarios en español (idioma principal del proyecto y de la wiki)

## Pull requests

1. Describe el **por qué** del cambio
2. Si tocas comportamiento del MCP, indica cómo probarlo
3. No incluyas credenciales ni rutas personales en configs de ejemplo
