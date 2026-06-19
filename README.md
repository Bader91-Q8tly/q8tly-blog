# Q8tly Blog — Editorial / Guide Workspace (Module 8)

Editorial workspace for **Q8tly**, a bilingual EN/AR curated Kuwait directory.
This repo holds the markdown drafts, editorial calendar, and session handoffs for
**Module 8 only** — best-of lists, area/district guides, and the rotating
"editorial of the week" content the homepage surfaces.

> Editorial is the cold-start trust substitute. Quality and SEO internal-linking
> are the priority.

## Structure

| Path         | Purpose |
|--------------|---------|
| `/role`      | The role brief — who Claude Blog is and the scope boundaries. |
| `/drafts`    | Markdown editorial drafts before they go into WordPress. |
| `/calendar`  | Editorial calendar + the "this week" rotation the homepage pulls from. |
| `/handoffs`  | Session handoff notes (write one at the end of every session). |
| `/reference` | Read-only: Project Brief, Module 8 spec, IA Strategy. Do not edit. |

## Ground rules

- **Publish under `/{lang}/guide/`** — never `/blog/`.
- **Bilingual:** every guide ships EN + AR; not launched until both exist.
  AR publishing is GATED on WPML being on production (S2-19). Until then: author
  EN, stage AR drafts, do not publish AR.
- **Staging only.** Production is frozen until cutover.
- **Internal-link** each guide into the relevant district + category money pages.
- **Out of scope:** the data model, listing template, combo/archive pages, and
  header/footer/homepage chrome (Modules 1–7), the homepage editorial widget, and
  the q8tly-core plugin. Stop and route those to the Advisor.
- **Audit trail is single-sourced:** handoffs live here; decisions go UP to the
  central BIR / Decision Log — no parallel decision log in this repo.

See [`role/role-brief.md`](role/role-brief.md) for the full brief.
