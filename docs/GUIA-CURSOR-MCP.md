# Guía: Cursor gratis + MCP Tenarius (agente de consultas)

Publicación interna del proyecto **tenarius-wiki-mcp** para jugadores que hoy usan IA en el navegador y quieren el **MCP completo** (búsqueda en wiki, referencias RO Pre-Renewal, perfil local).

> **Gratis:** Cursor tiene plan free — solo necesitas **correo electrónico**.  
> **Open source:** este MCP es comunitario, sin fines comerciales, no oficial de Tenarius ni Gravity.

---

## ¿Por qué Cursor?

| IA web (ChatGPT, Claude.ai) | Cursor + MCP Tenarius |
|-----------------------------|------------------------|
| Prompt manual, sin tools | Agente con tools estructuradas |
| Puede mezclar fuentes | Metadatos servidor/era/Tenarius |
| Sin perfil integrado | Perfil local opcional (100% en tu PC) |

---

## Requisitos

- PC con **Windows, macOS o Linux**
- **Correo electrónico** (registro Cursor)
- **Internet** (clonar repo, consultar wikis)
- **Git** recomendado ([git-scm.com](https://git-scm.com/))
- **Python 3.10+** (el script de setup instala dependencias; [uv](https://docs.astral.sh/uv/) es opcional pero recomendado)

---

## Paso 1 — Instalar Cursor (gratis)

1. Entra a **[cursor.com](https://cursor.com)** y pulsa **Download**.
2. Instala la app como cualquier programa.
3. Al abrir, **Sign up** / **Registrarse** con tu **correo** (Google/GitHub también sirven).
4. El plan **Hobby / Free** basta para usar el agente y MCP.

Documentación oficial: [cursor.com/docs](https://cursor.com/docs)

---

## Paso 2 — Crear tu carpeta de proyecto

Elige **una** de estas opciones:

### A) Solo consultas Tenarius (recomendado para empezar)

Crea una carpeta y clona el MCP ahí:

```bash
mkdir -p ~/TenariusRO
cd ~/TenariusRO
git clone https://github.com/Robgonzalez/tenarius-wiki-mcp.git
cd tenarius-wiki-mcp
```

### B) Carpeta de jugador Tenarius (wiki + notas propias)

Si además guardas guías o configs del juego:

```bash
mkdir -p ~/Documentos/TenariusRO
cd ~/Documentos/TenariusRO
git clone https://github.com/Robgonzalez/tenarius-wiki-mcp.git
```

Puedes añadir subcarpetas `notas/`, `builds/` — lo que quieras; el MCP no sube nada a la nube.

---

## Paso 3 — Abrir la carpeta en Cursor

1. Abre **Cursor**.
2. Menú **File → Open Folder…** (Archivo → Abrir carpeta).
3. Selecciona la carpeta **`tenarius-wiki-mcp`** que clonaste.
4. Cursor abrirá el proyecto; verás archivos como `README.md`, `scripts/`, etc.

> El archivo [`.cursor/mcp.json`](../.cursor/mcp.json) ya viene en el repo — registra el servidor MCP para esta carpeta.

---

## Paso 4 — Instalar el MCP

Abre la **terminal integrada** en Cursor: **Terminal → New Terminal** (o `` Ctrl+` ``).

```bash
./scripts/setup.sh
```

El script:

- Instala dependencias Python
- **Opcional:** te pregunta si quieres configurar tu **perfil de aventurero** (100% local, ver [PERFIL-AVENTURERO.md](./PERFIL-AVENTURERO.md))

Si `uv` no está instalado, el script usa `pip` automáticamente.

---

## Paso 5 — Activar el MCP en Cursor

1. **Reinicia Cursor** (cierra y abre) o recarga ventana.
2. Ve a **Settings** (⚙) → **Tools & MCP** (o **Cursor Settings → MCP**).
3. Busca **`tenarius-wiki`** — debe aparecer con estado **activo** (punto verde).
4. Si no aparece, comprueba que abriste la carpeta **`tenarius-wiki-mcp`** como proyecto.

### Usar el MCP desde otra carpeta (avanzado)

Si quieres consultar Tenarius mientras trabajas en **otra** carpeta, copia el bloque de [`examples/cursor-global-mcp.json`](../examples/cursor-global-mcp.json) a:

- **Linux/macOS:** `~/.cursor/mcp.json`
- **Windows:** `C:\Users\TU_USUARIO\.cursor\mcp.json`

Ajusta la ruta absoluta al clone de `tenarius-wiki-mcp`.

---

## Paso 6 — Usar el agente de consultas

1. Abre el chat del agente: **Ctrl+L** o panel **Chat / Agent**.
2. Modo **Agent** (no solo Ask) para que pueda llamar tools MCP.
3. Escribe preguntas naturales, por ejemplo:

```
¿Qué bonos da el Fighting Set para Professor en Tenarius?
```

```
Busca skills de Professor Pre-Renewal y dime si aplican a Tenarius.
```

```
Lee mi perfil de aventurero y recomiéndame farming para mi nivel.
```

El agente usará tools como `search_wiki`, `search_ro_reference`, `get_adventurer_profile`, etc.

### Perfil de aventurero (opcional)

```bash
./scripts/configure-profile.sh
```

Datos **solo en tu PC:** `~/.config/tenarius-wiki-mcp/adventurer-profile.json`

---

## Paso 7 — Verificar que funciona

Pregunta al agente:

> Lista las herramientas MCP de tenarius-wiki disponibles y busca "Set de Equipamiento" en la wiki de Tenarius.

Deberías ver resultados con **URL**, **servidor** y si **aplica a Tenarius**.

---

## Solución de problemas

| Problema | Qué hacer |
|----------|-----------|
| MCP no aparece | Reiniciar Cursor; abrir carpeta `tenarius-wiki-mcp`; ejecutar `./scripts/setup.sh` de nuevo |
| Error `uv` / Python | Instalar Python 3.10+; o `pip install -r requirements.txt` en el repo |
| Tools no se usan | Usar modo **Agent**, no solo chat sin tools |
| Perfil no se lee | Ejecutar `./scripts/configure-profile.sh`; recargar MCP |
| Wiki Tenarius falla | Comprobar internet; reintentar en unos minutos |

---

## Privacidad

- **Perfil de aventurero:** 100% local — [PERFIL-AVENTURERO.md](./PERFIL-AVENTURERO.md)
- **Consultas wiki:** el MCP lee wikis públicas desde tu PC; no vendemos datos
- **Cursor:** revisa su política de privacidad en [cursor.com](https://cursor.com) para el chat con modelos de IA

---

## Alternativa sin instalar Cursor

Si prefieres seguir en el navegador sin MCP: [USO-IA-WEB.md](./USO-IA-WEB.md) y [PROMPT-IA-WEB.txt](./PROMPT-IA-WEB.txt).

---

## Enlaces del proyecto

- Repo: https://github.com/Robgonzalez/tenarius-wiki-mcp
- Wiki Tenarius: https://tenarius-ro.com/wiki/
- Fuentes y eras RO: [FUENTES-RO.md](./FUENTES-RO.md)
