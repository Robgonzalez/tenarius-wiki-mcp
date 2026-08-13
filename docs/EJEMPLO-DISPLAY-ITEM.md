# Ejemplo de display — Fighting Set (Tenarius)

Datos extraídos de la wiki vía MCP (`get_wiki_page("Set de Equipamiento")`).
El agente debe producir fichas **con este formato** al hablar de un ítem concreto.

---

## 🎒 Fighting Set (Set de Batalla)

| Campo | Valor |
|-------|-------|
| **Servidor** | Tenarius RO |
| **Origen del contenido** | Exclusivo Tenarius (custom) |
| **Era** | Pre-Renewal |
| **¿Aplica a Tenarius?** | Sí — contenido del servidor / confirmado Tenarius |
| **Tipo** | Set de Equipamiento (especial — batalla) |
| **Piezas del set** | Armor + Garment + Shoes (c/u con [1] slot) |
| **Bonus combo (set completo)** | Max HP +10%, Flee +20, Atk +20 |
| **Bonos por job/clase** | **Priest:** Str+3, Agi+3 (+ skills). **Sage/Professor:** Int+3, Agi+3 (+ Auto Spell, Free Cast, Soul Strike, Dispell…) |
| **Obtención / craft** | Oficios Armorsmith (armor) + Tailor (garment/shoes); posible encantamiento con runas |
| **Advertencias** | En **PvP** el usuario recibe **triple de daño** estando equipado |
| **Fuente** | https://tenarius-ro.com/wiki/index.php/Set_de_Equipamiento#fighting |

**Notas:** Set especial, distinto de los sets por árbol de clase (Arkana, Violent Gale, etc.).

_Stats exactos pueden diferir en el juego. Verifica in-game si la decisión es crítica._

---

## 🎒 Fighting Set — Armor

| Campo | Valor |
|-------|-------|
| **Servidor** | Tenarius RO |
| **Origen del contenido** | Exclusivo Tenarius (custom) |
| **Era** | Pre-Renewal |
| **¿Aplica a Tenarius?** | Sí |
| **Tipo** | Armor |
| **Slot** | Armor [1] |
| **Set** | Fighting (Set de Batalla) |
| **Stats (pieza)** | Def +5, Flee +4 |
| **Fuente** | https://tenarius-ro.com/wiki/index.php/Set_de_Equipamiento#fighting |

---

## Regla para el agente

Cuando la respuesta **nombre un ítem** (equipo, material, consumible, pieza de set):

1. Consultar fuente (`search_wiki` / `get_wiki_page` o `search_ro_reference`).
2. Llamar tool **`format_item_info`** con los campos conocidos **o** replicar esta ficha en markdown.
3. No dar solo el nombre en prosa — incluir al menos: servidor, origen, era, si aplica a Tenarius, stats/bonos relevantes, URL.

Tool MCP: `format_item_info` · Set completo: `format_set_info`
