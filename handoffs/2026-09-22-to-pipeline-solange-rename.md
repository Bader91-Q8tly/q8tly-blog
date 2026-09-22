# → PIPELINE (via Advisor) — listing 4025/4040 renamed to "Solange Maison" by Blog (2026-09-22)

**Heads-up: Blog wrote listing (`gd_place`) data, which is Pipeline's lane.** Done on Bader's
explicit instruction, after the same rename had sat routed to Pipeline since 2026-08-13
(`handoffs/2026-08-13-to-advisor-solange-maison-and-open-rulings.md` §B1). **That routed item is
now CLOSED** — don't do it twice, and see the guard below.

## What changed
| | EN 4025 | AR 4040 |
|---|---|---|
| `post_title` | Solange → **Solange Maison** | Solange → **Solange Maison** |
| GD detail `post_title` | → Solange Maison | → Solange Maison |
| GD detail `_search_title` | → `solange maison` | → `solange maison` |
| `post_content` (name mention) | "Solange is an upscale…" → "**Solange Maison** is an upscale…" | «سولانج مطعم صيني…» → «**سولانج ميزون** مطعم صيني…» |
| `post_name` (slug) | **unchanged** (`solange`) | **unchanged** (`solange`) |

- **URLs did not move:** `/places/kuwait-city/solange/` and `/ar/places/مدينة-الكويت/solange/` both
  still return 200. No redirect needed, nothing to re-link.
- **Title stays Latin on the Arabic side**, per the house convention: **219 of 234** AR listings keep
  the Latin brand name; only 15 are Arabic-script (businesses with Arabic branding). Bader's standing
  rule is "business names stay in the business's own script", and Solange Maison brands in Latin
  (`solangemaison.com`). The **Arabic body** carries «سولانج ميزون» per his instruction.
  ⚠ Method note for anyone auditing: an earlier count of mine said 225/234 were Arabic-script. That was
  **wrong** — a MySQL `REGEXP '[؀-ۿ]'` that didn't match as intended. The PHP `\p{Arabic}`
  recount above is the correct one.

## Verified live (cache-busted, all 200)
`Solange Maison` now renders as the place card **and** map pin on both flagship guides (6307 / 6309),
as the place card on both Solange Maison spotlight guides (5430 / 5436), and as the H1 on both listing
pages. **Zero `>Solange<` left on any of the six pages.**

## Guard for Pipeline
If the listings pipeline re-syncs 4025/4040 from its source data, **the title will revert to "Solange"**
unless the source record is updated too. Please fix it at source. Also still open from the 2026-08-13
brief (Blog did NOT touch these): `amenities` is "Strong AC" only though the pack claims valet parking;
`price_kd_min`/`max` are both null though the pack says 15–19 KD; category is `Fine Dining` with no
`Restaurants` parent; `smoking`, `website`, `established_year` null; and the **AR listing body was
English until today** — this edit changed only the first name mention, the rest of that Arabic body is
Bader's own copy and reads fine, but the field-level AR gaps remain Pipeline's.

## Provenance
Backup `prod-20260922-234135.sql.gz` (canon, pre-write). Write done with `wp_update_post` +
a direct GD detail-table update, slug explicitly preserved, then a cache flush.
