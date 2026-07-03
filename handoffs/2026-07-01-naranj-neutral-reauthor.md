# Handoff — Naranj (Salmiya) neutral re-author, EN + AR (2026-07-01)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## ✅ DONE — Naranj now matches the MizuMesa neutral model (D-168 / D-145)

Bader's request: bring `naranj-salmiya` in line with the neutral vibe proven on
MizuMesa, keeping the existing photos. Source content: his
`naranj-guide-EN-AR (1).md` intake drop (Project Brief v2.4), which already
had the neutral About paragraph + key facts, EN and AR, ready to inject.

- **EN — guide_article 2251** (`/guide/naranj-salmiya/`): body replaced via
  `reinject_en.py` — old spotlight structure (H2 sections "The room"/"The
  food"/service, pull-quote, "Know before you go" 7-row table, `[[map]]`, FAQ)
  fully removed. New body: neutral title ("Naranj"), one About paragraph, 3
  reused inline photos with short captions, a clean 6-row **Key facts** table,
  `[[place]]` only. `deck` cleared to `""`. `rank_math_description` replaced
  directly via SSH (script doesn't manage SEO meta — same as the MizuMesa
  precedent); `rank_math_title` left as-is (already factual).
- **AR — twin post 2612** (`/ar/guide/naranj-salmiya/`, linked via WPML trid
  4657 to EN 2251): repopulated via `populate_ar_twin.py` with the matching
  Arabic. **Stays `publish` + `noindex`** — content-only update, fence
  unchanged (D-145 quality gate, not a go-live; twin was already fenced from
  the 2026-06-29 build). First-twin-style proof re-ran clean: Arabic title
  renders, `[q8tly_place]` emits `/ar/places/…`, no bare `/places/` leak, no
  `/ar/en/` double-prefix, single H1, noindex present.
- **Photos: untouched, all 4 reused** (hero 2247, inline 2248/2249/2250) — no
  re-upload, no deletion. Only the captions were shortened to match the
  neutral vibe ("Outside Naranj", "Inside Naranj", "Mezze and meat arayes",
  "Dessert at the end of the meal" / AR equivalents).
- **Drafts:** `drafts/naranj-salmiya_EN_2026-07-01.md`,
  `drafts/naranj-salmiya_AR_2026-07-01.md`. (`guide-kit/guides/naranj-salmiya/
  article.md` intentionally left as the original-publish historical record —
  same pattern as `guides/mizumesa-sharq/article.md`, which is also stale.)
- **Verified live** (both `curl` + structural checks): EN 200, single H1
  "Naranj", all 4 new captions present, zero raw `[q8tly_*]` shortcode
  literals, no leftover persuasive copy ("standout"/"attentive"). AR 200,
  single H1 "نارنج", all 4 AR captions present, noindex meta present.

## ⚠ Process gap found + logged — not a Bader flag, my own catch
`reinject_en.py` has **no built-in pre-write DB backup** (unlike
`publish_guide.py` and `populate_ar_twin.py`, which both snapshot
automatically). The EN reinject above ran before I caught this — I took a
snapshot immediately **after** instead of before
(`staging-20260701-200653-guide-naranj-salmiya-en-reinject-post.sql.gz`),
logged honestly in `BACKUP_LOG.md` with the gap noted (same pattern as the
original Anosha logging gap). If a rollback of the EN reinject is ever
needed, the closest clean restore point is the prior snapshot
(`20260624-165707`, internal-link guides). **Worth closing:** add a backup
step to `reinject_en.py` mirroring the other two scripts, so this can't
recur on the next content-only EN re-author.

## Open items (out of Blog's lane — not touched here)
- **Listing About paragraph** at `/places/salmiya/naranj/` — the intake's
  routing note says the same About text also updates the Pipeline-lane
  listing About. That's Pipeline/Builder scope per the squad-sync model, not
  a `guide_article` change — **not done here**, flag to Advisor if not
  already in flight.
- **NEEDS BADER flags carried from the intake** (unrelated to the guide body,
  listing-data scope): AR business name confirmation (نارنج used as
  placeholder), phone vs WhatsApp split, map pin/coordinates, weekend hours,
  smoking-section field. None of these block the guide re-author done here.
