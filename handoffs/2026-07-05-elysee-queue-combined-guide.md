# Session handoff — Elysee Beauty Lounge + Queue Café COMBINED guide (2026-07-05)

## What shipped
**EN guide LIVE: `guide_article` 3115** at `/guide/elysee-queue-cafe-mahboula/` (staging).
**First COMBINED guide** (owner-directed: "make both into one, mix them") and **first use of
the D-180 Canva-interim PASS path**. Kit run clean (backup `20260705-205507`); verify green
(200, house chrome, hero, no double title). Two women-only venues on the 24th-floor rooftop
of the Park Inn by Radisson, Mahboula, framed as a salon-visit-plus-coffee day out.

## Photo gate: strong PASS (the anti-B+F)
The intake's **22 originals were 4284–5712px** (mostly native landscape) — 2.8–3.7× the 1520
bar. Ran the D-180 Step-0 gate (measure width first): PASS. Fitted 5 to **7:5 1520×1086**
(one ratio, all ≥1520px), auto-rotating the sideways shots (no EXIF flag → ROTATE_270):
hero **3110** (rooftop lounge, sea view) + inline **3111** (Elysee gold sign) / **3112**
(salon styling chairs + sea view) / **3113** (Queue Café metal sign) / **3114** (café interior).
Narrative: rooftop hero → Elysee sign → salon w/ view → Queue sign → café.

## Two place cards — the mechanism (reusable)
A combined guide needs a card for **each** venue. The kit's `[[place]]` only emits the single
frontmatter `place_id`, so: `place_id: 3067` (Queue) → `[[place]]`; **Elysee 3066** via a raw
**unquoted** `[q8tly_place id=3066]` on its own line. Unquoted matters — the kit's `md_inline`
HTML-escapes quotes (`"`→`&quot;`), which breaks a quoted shortcode; unquoted survives, and
WP `shortcode_unautop` strips the wrapping `<p>` so it renders as a clean card. **Verified
live: 2 `q8tly-place` cards, both `/places/mahboula/…` links, 0 shortcode literal leak.**
(Pattern for any future multi-venue guide.)

## Voice / no-fabrication
Neutral (D-168): the owner's "fancy / breathtaking view" rendered as **facts** — rooftop, 24th
floor, floor-to-ceiling windows, sea views over the coast. **No fabrication:** Elysee's salon
services/hours/price are unknown (the intake was ~90% café), so the salon is described only by
confirmed facts (women-only, on the floor, valet, the café pairing). Queue uses its locked
facts (coffee/light bites, ~10 KD, 10–8, indoor/outdoor, women-only, groups, laptop).

## AR twin — staged, PENDING (needs Bader's "+" and D-145 pass)
`drafts/elysee-queue-cafe-mahboula_AR_2026-07-06.md`. Because a combined guide is a NEW
artifact, the AR is **assembled from Bader's verbatim AR sentences** in the two source MDs; the
**combined arrangement + section headers + captions are Blog-staged and need his D-145 pass**
(he may prefer to author the combined AR himself). Then: WPML "+" on 3115 → `populate_ar_twin.py`
`--en-id 3115 --media hero=3110,inline-1=3111,inline-2=3112,inline-3=3113,inline-4=3114` → fence.
The Elysee raw-shortcode card is in the AR draft too (unquoted).

## Open items (content/listing lane — NOT photos)
- **Queue Café listing 3067:** missing **phone** + **coordinates** (Maps pin).
- **Elysee listing 3066:** thin — no salon **services / hours / price / phone** (needs its own
  Quick Visit Pack). The guide runs on shared-premises facts; a fuller listing needs the salon intake.
- **AR:** Bader's D-145 pass on the combined Arabic + the "+".
- Route the two listing gaps to **Pipeline** (via Advisor) — they're `gd_place` data, not Blog's.

## Repo
`guide-kit/guides/elysee-queue-cafe-mahboula/` (article.md + 2 source MDs; images gitignored),
`guide-kit/runs/elysee-queue-cafe-mahboula.md`, `drafts/…_AR_2026-07-06.md`, calendar updated
(rotation + Published entry). Committed.
