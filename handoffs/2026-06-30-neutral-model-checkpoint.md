# Handoff — Blog checkpoint: NEUTRAL guide model proven on MizuMesa (2026-06-30, PM)

**Blog is at:** the guide content model changed (launch feedback) → guides are now
**SHORT + NEUTRAL**. MizuMesa is re-authored to it end-to-end (EN 2362 + AR 2618),
Bader-passed (9/10). The flow + tooling are proven; the other 5 guides are next.

## The neutral model (D-168) — final shape
**About → captioned photos → key-facts TABLE → `[q8tly_place]` listing card.**
- Neutral tone, no persuasion. **No FAQ. No 9-row data dump.** Key facts = a clean
  ~5-row table (cuisine / hours / price / location / reservations).
- **Facts presentation = a TABLE** (the old "before you go" look Bader's sister liked).
  Investigated: there is **no facts-card CSS component**; the old one was just a
  markdown table → so reproduce as a 2-col table = **content-only, no Builder.**
- **Photos stay**, each with a **short neutral caption** ("name what it is, no praise"):
  e.g. beef → "A beef dish" (NOT "the standout beef"). Captions approved
  **picture-by-picture** by Bader (give 2–3 options per photo, EN + AR; his pick = the
  D-145 sign-off on the AR label).

## Content flow (unchanged rails)
Content Writer → **approved EN + AR MD** (Bader-reviewed; AR = human Kuwaiti, D-145) +
photos → Blog **injects faithfully** (no edits/regeneration). MDs may arrive as one
combined `*-EN-AR.md` (split the `## EN` / `## AR` sections; ignore any
`## Listing data` block — that's Pipeline's gd_place data, not guide body).

## Re-inject mechanics for an EXISTING guide (all 6 already have AR twins)
- **AR twin** already exists → `guide-kit/populate_ar_twin.py --en-id <EN> --media … --execute`
  (updates the twin, **no new "+"**, fences noindex).
- **EN body** → `guide-kit/reinject_en.py <md> <EN_id> --media … --execute` (NEW kit tool,
  EN counterpart; handles inline media + hero/captions; **NO fence** — EN indexable).
- Both take `--media inline-1=ID,inline-2=ID,inline-3=ID,hero=ID` and **reuse existing
  media** (no re-upload; repo is text-only). MizuMesa media: hero 2358, inline 2359/2360/2361.
- **Timeout heads-up:** the AR run's DB backup (~2.4 MB gz) is slow; AR+EN back-to-back
  can exceed a 2-min shell timeout — the writes still land server-side, just **verify +
  flush after** (`wp post update <id>` + `rocket_clean_domain`).
- **Deck:** the template always renders a deck (`deck` meta else excerpt). For neutral,
  set `deck: ""` AND clear the old `post_excerpt` so it auto-derives from the new about
  (else the OLD persuasive excerpt leaks). reinject_en.py clears the excerpt.

## OPEN — route to Builder via Advisor (do at batch start, fixes all guides at once)
- **Tall inline photos:** body images render at natural aspect (portrait shots look
  stretched-tall; the roll photo on MizuMesa). Fix = a cap in **guide.css** (q8tly-core,
  Builder's), e.g. `.q8tly-guide-single__body .wp-block-image img { max-height:…; object-fit:cover }`
  or an `aspect-ratio` cap. One CSS rule → every guide. **Bader deferred to the batch.**

## Per-guide flags (low priority, not blockers)
- SEO meta (`rank_math_title`/`_description`) still old persuasive — the body inject
  doesn't touch it; pages noindex anyway. Neutralize separately if wanted.
- AR listing-card slug numeric → `/ar/places/شرق/2405/` (the gd_place AR twin's slug) —
  Pipeline listing-data, not the guide.

## Remaining work
Re-author the other **5 guides to neutral** when their MDs land: anosha (2189/2600),
naranj (2251/2612), south-avenue (2339/2619), keif (2132/2630), vibes (2131/2634).
They currently hold the OLD persuasive bodies; same flow re-injects neutral versions.

## State
Repo clean + pushed: `origin/main` = **7fbff98**. Sync model: q8tly-core = shared canon
(read-only for Blog); cross-lane → Advisor → Builder. Drafts: `drafts/mizumesa-sharq_{EN,AR}_2026-06-30.md`.
