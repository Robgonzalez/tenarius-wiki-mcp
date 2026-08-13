# Perfil de aventurero (100% local)

Configura datos básicos de tu personaje para que el agente personalice builds, farming y recomendaciones.

## Privacidad

| | |
|---|---|
| **Dónde se guarda** | `~/.config/tenarius-wiki-mcp/adventurer-profile.json` |
| **Quién lo lee** | Solo el MCP en **tu PC** (proceso local stdio) |
| **Se sube a GitHub** | **No** — nunca está en el repo |
| **Fines comerciales** | **No** — proyecto open source MIT, comunitario |
| **Borrar** | `rm ~/.config/tenarius-wiki-mcp/adventurer-profile.json` |

El MCP **no envía** tu perfil a Tenarius, Gravity ni a los maintainers del repo.
Solo se inyecta en las instrucciones del agente **en tu máquina**.

## Configurar al instalar

Durante `./scripts/setup.sh` se ofrece configurar el perfil.
También puedes hacerlo en cualquier momento:

```bash
./scripts/configure-profile.sh
```

Editar perfil existente:

```bash
./scripts/configure-profile.sh --edit
```

## Campos

| Campo | Ejemplo |
|-------|---------|
| `character_name` | Danparojo |
| `class_name` | Professor |
| `base_level` / `job_level` | 99 / 70 |
| `server` | Tenarius RO |
| `notable_gear` | Fighting Set, Snake Head |
| `play_style` | PvM solo, MVP |
| `goals_short` | Top 1 Fisherman |
| `goals_medium` | Mejorar PC, promocionar servidor |
| `language` | es |
| `notes` | Cualquier contexto extra |

Ver plantilla: [`examples/adventurer-profile.example.json`](../examples/adventurer-profile.example.json)

## En el MCP

- Tool `get_adventurer_profile` — el agente lee tu perfil local
- Las instrucciones del servidor incluyen el perfil si está configurado

## Sin perfil

El MCP funciona igual; las respuestas serán genéricas hasta que configures el perfil.
