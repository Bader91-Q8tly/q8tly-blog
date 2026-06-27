# Guide Ingestion Kit

Turnkey publishing for Module 8 guides. **Bader drops one folder; the kit
publishes a correct `guide_article` from it** — no avoidable manual steps.

This exists because a guide is a custom post type (`guide_article` at
`/guide/{slug}/`) with its own meta + taxonomy. The WordPress.com **MCP can't
create it** (only posts/pages), so publishing goes through **WP-CLI over SSH**
(the same `…@ssh.wp.com` access the listings pipeline uses). Get that wrong and
you ship a Page (wrong type, no template chrome) — which is exactly what happened
on the first Anosha attempt before this kit.

> **This README ships the English guide.** For the **Arabic twin** (how it's
> created through WPML, human translation, `/ar/` routing, the
> fenced→reviewed→unfenced lifecycle), see **`GUIDE_AR_WORKFLOW.md`** — read it
> first for any AR work.

---

## 1. The drop (input contract)

One folder per guide under `guides/`:

```
guides/
  my-place-area/
    article.md          # frontmatter + PLAIN body (see guide.template.md)
    images/
      hero.jpg          # → Featured image + hero_photo_id  (also OG if no og.*)
      og.jpg            # optional 1200×630 social card (sets OG; else hero is used)
      inline-1.jpg      # inline body photo, referenced by [[image:inline-1|caption]]
      inline-2.jpg      # …add as many as the body references
```

- **`article.md` frontmatter** carries everything the `guide_article` needs:
  `title, slug, lang, deck, topic, article_type, place_id` (required) and
  `map_ids, word_count, seo_title, meta_description, hero_alt, hero_caption,
  replaces_page_slug, status` (optional). Copy `guide.template.md` and fill it.
- **The body is PLAIN editorial prose.** No kicker / byline / hero / share /
  related / CTA — the template owns all of it; hand-built chrome double-renders.
- **Markers** the publisher expands in the body:
  - `[[place]]` → `[q8tly_place id=<place_id>]` (the listing card)
  - `[[map]]` → `[q8tly_map ids=<map_ids>]` (numbered map pins; max 1/article)
  - `[[image:STEM|Caption]]` → an inline photo from `images/STEM.*`
- **Image slots are declared by filename:** `hero.*`, `og.*` (optional),
  `inline-*.*`. The hero is the Featured image + `hero_photo_id`.

---

## 2. Photos — resolved honestly (this step IS automated)

The images are local files on Bader's Mac. The MCP API can't upload local
binaries, and server-side WP-CLI can't read his disk. **But the same SSH account
that runs WP-CLI is binary-safe**, so the kit streams each file up and imports it
server-side — no SFTP client, no app password, no drag-drop:

```
cat images/hero.jpg | ssh $SSH_HOST "cat > /tmp/guidekit-<slug>-hero.jpg"
ssh $SSH_HOST "wp media import /tmp/guidekit-<slug>-hero.jpg --post_id=<ID> --featured_image --porcelain"
```

This is proven (it's how the Anosha hero + 3 inline photos + the listing photo
were published). **Step 2 is automated — there is no manual drag-drop.** The only
thing that stays manual is whatever the *listing* (gd_place) needs, which is a
separate data-pass concern, not a guide.

> If SSH is ever unavailable, the kit falls back to a single documented
> drag-drop (upload `images/` in wp-admin, then re-run with `--media-ids`); it
> will say so loudly rather than leave it silently broken.

---

## 3. Publish runbook (what `publish_guide.py` does)

1. **Validate** — frontmatter present + required keys; `slug` doesn't collide
   with an existing `guide_article`; `place_id` resolves to a published
   `gd_place`; `topic` is one of the four locked slugs.
2. **Backup** — `wp db export` → gzip to `$BACKUP_DIR`, logged in
   `BACKUP_LOG.md` (staging is same write-class; discipline applies).
3. **Images** — stream each `images/*` up over SSH, `wp media import`, capture
   attachment IDs + URLs. Hero → Featured.
4. **Create** — `wp post create --post_type=guide_article` (the `/wp/v2/guides`
   REST equivalent; **never a Page**, never the dead `/wp/v2/guide_article`
   base). Body = plain blocks + `[q8tly_place]`/`[q8tly_map]` only. Set meta
   (`deck, hero_photo_id, primary_topic, article_type, word_count, hero_alt,
   hero_caption`) and assign the `topic` term in the same run.
5. **Featured image** → the hero attachment (`_thumbnail_id` + `hero_photo_id`).
6. **Replace a stand-in?** If `replaces_page_slug` is set: trash that Page and
   add a Rank Math **301** `/{old}/` → `/guide/{slug}/`.
7. **Verify + handoff** — confirm the single renders with house chrome (no
   double), appears in `/guide/` cards, permalink is `/guide/{slug}/`, images
   present, OG set. Writes a one-screen per-run handoff to `runs/<slug>.md`.

> **Edge-cache gotcha (baked into the runbook):** WP-CLI meta writes do NOT
> trigger the WordPress.com Atomic edge purge. The runbook always finishes with
> a `wp post update <id>` touch + `rocket_clean_domain()`; without the touch the
> page serves stale (this is why the hero "didn't show" until a re-save).

---

## 4. Guardrails (checks, not vibes)

The script enforces these and aborts if violated:

- **Endpoint** = `guide_article` CPT (REST base `guides`). Never a Page. Never
  `/wp/v2/guide_article` (404 since BIR-078).
- **Body is plain** — rejects a body containing kicker/byline/hero/share markup.
- **`topic`, `deck`, `hero` must be set** — or the template falls back (empty
  kicker, deck→excerpt, flat-plate hero). Missing `topic`/`deck` = hard fail;
  missing hero = warn (publishes flat-plate, flagged in the handoff).
- **AR stays parked** — `lang: ar` won't publish unless `status: publish` is
  explicit; same plain-body rule applies.

---

## 5. Usage

```bash
cd "guide-kit"
# Dry run — validates, resolves images, prints the body + every command. No writes.
python3 publish_guide.py guides/my-place-area

# Execute — takes the backup, uploads, creates, verifies, writes the handoff.
python3 publish_guide.py guides/my-place-area --execute
```

Config (SSH host + site URL) lives in `config.sh`; override with `--ssh-host` /
`--site-url` or env `GUIDEKIT_SSH_HOST` / `GUIDEKIT_SITE_URL`. **Always dry-run
first.** A worked reference drop is in `guides/_example-anosha/`.
