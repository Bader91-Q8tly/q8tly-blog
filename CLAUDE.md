# Q8tly Blog — Claude working notes

This is the **Module 8 Editorial / Guide** workspace for Q8tly (bilingual EN/AR
curated Kuwait directory). You produce and publish **guides** — best-of lists,
area/district guides, and single-place spotlights.

## To publish a new guide: use the Guide Ingestion Kit

**Everything is automated through `guide-kit/`.** Don't hand-build it.

1. The new guide arrives as one folder: `guide-kit/guides/<slug>/` with
   `article.md` (frontmatter + PLAIN prose body) and an `images/` subfolder
   (`hero.*`, optional `og.*`, `inline-*.*`). See `guide-kit/guide.template.md`
   and the worked `guide-kit/guides/_example-anosha/`.
   - If Bader instead just gives content + photos + the listing it's about, build
     that folder yourself from the template, then run the kit.
2. Dry-run, then execute:
   ```bash
   python3 guide-kit/publish_guide.py guide-kit/guides/<slug>            # validate + preview
   python3 guide-kit/publish_guide.py guide-kit/guides/<slug> --execute  # publish
   ```
   The kit handles: validation, DB backup, image upload, `guide_article`
   creation, meta + topic, featured image, Page→guide 301, verify, and a per-run
   handoff in `guide-kit/runs/`.

Full contract + runbook + the publishing gotchas: **`guide-kit/README.md`**.

## Hard rules (the kit enforces these; you should too)

- **Guides are the `guide_article` CPT** at `/guide/{slug}/` (REST base
  `/wp/v2/guides`). **Never publish a guide as a Page**, never the dead
  `/wp/v2/guide_article` base.
- **Publish via WP-CLI over SSH** (`config.sh`) — the WordPress.com MCP can't
  create the CPT.
- **Body is plain prose + `[q8tly_place]` / `[q8tly_map]` only** — the template
  owns kicker/byline/hero/share/related (hand-built chrome double-renders).
- **`topic` (one of food-drink|neighborhoods|culture-heritage|seasonal), `deck`,
  and a hero image must be set**, or the template falls back.
- **Staging only; production (q8tly.com) is frozen.** **AR stays parked** until
  Bader says publish (same plain-body rule when it does).
- **Backup before any write** → log in `guide-kit/BACKUP_LOG.md`.
- **After wp-cli meta writes, touch the post** (`wp post update`) + flush, or the
  WordPress.com edge cache serves stale.

## Where things are

- `role/role-brief.md` — full scope + what to route to the Advisor.
- `guide-kit/` — the publishing kit (start here for any guide).
- `drafts/` — markdown drafts (EN + AR). `handoffs/` — session handoffs (write one
  each session). `calendar/editorial-calendar.md` — pipeline + weekly rotation.
- `assets/` — optimized guide images.

First guide shipped this way: Anosha Beauty Salon (`/guide/anosha-beauty-salon-sabah-al-salem/`, guide_article 2189). See `handoffs/2026-06-20-anosha-spotlight.md`.
