# Briefing → Advisor — Neutral-model ledger update: Naranj + Anosha DONE, queue corrected to 3 (2026-07-02)

**From:** Claude Blog (Module 8 — Editorial / Guide). **To:** Advisor → update STATE.md.
**TL;DR:** Shared STATE.md's Content-Writer-lane line still says **"5 remaining guides"**
(written 2026-06-30, right after MizuMesa alone was done). That's stale — **Naranj and
Anosha are now also neutral-re-authored** (2026-07-01). **3 guides remain, not 5.** This
briefing states the exact dated draft filenames + post IDs for the ledger, and reports the
Blog-kit EN-update path (the other gate on that STATE.md line) as closed.

---

## 1. Two more guides moved to the neutral model (D-168), 2026-07-01

Same proven flow as MizuMesa (checkpoint: `handoffs/2026-06-30-neutral-model-checkpoint.md`).
Both Bader-approved MDs came in as combined `*-guide-EN-AR.md` intake drops; both full-read
by Bader before injection (the D-145 human-authorship gate).

| Guide | EN post | AR twin (fenced) | Dated draft files |
|---|---|---|---|
| Naranj — Salmiya | `guide_article` **2251** (`naranj-salmiya`) | **2612** | `drafts/naranj-salmiya_EN_2026-07-01.md`, `drafts/naranj-salmiya_AR_2026-07-01.md` |
| Anosha Beauty Salon | `guide_article` **2189** (`anosha-beauty-salon-sabah-al-salem`) | **2600** | `drafts/anosha-beauty-salon-sabah-al-salem_EN_2026-07-01.md`, `drafts/anosha-beauty-salon-sabah-al-salem_AR_2026-07-01.md` |

Both: neutral About paragraph, existing photos reused with short neutral captions (none
deleted, none re-uploaded), key-facts **table**, `[q8tly_place]` card only (no `[[map]]`,
matching the MizuMesa v2 shape). AR twins stay **publish + noindex** — content-only update,
fence untouched (D-145 quality gate, not a go-live). Full detail in
`handoffs/2026-07-01-naranj-neutral-reauthor.md` and `handoffs/2026-07-01-anosha-neutral-reauthor.md`.

One real content call surfaced and was routed to Bader rather than guessed: Anosha's price
tier was left open in the intake ("$$ or $$$ — did NOT pick, that's a call not data"). Bader
confirmed **keep $$**, matching what was already live.

## 2. Blog-kit EN-update path — CLOSED (the other gate on STATE.md's line 26)

`reinject_en.py` (the EN counterpart to `populate_ar_twin.py`) is formalized, same
backup → update → verify discipline as the AR tool:
- **Auto-backup** before every write, self-logged to `guide-kit/BACKUP_LOG.md` — no more
  manual pre-write snapshots (closes a gap this lane hit twice on the Naranj/Anosha runs).
- **Hard target guard**: refuses unless the post is a `guide_article` with WPML language
  `en`/untranslated — this is what makes "never touch the AR twin, never write
  `icl_translations`" a structural guarantee, not a convention.
- **Built-in idempotency check**: diffs the generated body against the post's live content
  on every run (dry or execute), reports `NO CHANGE` or a line-diff.
- **Conditional SEO-meta sync** (`rank_math_title`/`_description` from the draft's
  frontmatter, only when supplied — never blanks an existing value).

**No-op tested against MizuMesa** (post 2362, `drafts/mizumesa-sharq_EN_2026-06-30.md`):
idempotency check reported byte-identical body; every meta field already matched live; full
backup → update → verify pipeline ran clean; AR twin (2618) confirmed untouched afterward
(`post_modified` unchanged, still noindex, trid intact). Documented in `guide-kit/README.md`
§6. Full detail: `handoffs/2026-07-01-reinject-en-formalized.md`.

## 3. Corrected queue — 3 guides remain, not 5

`south-avenue-salon-sabah-al-salem` (2339/2619), `keif-restaurant-al-kout-mall` (2132/2630),
`vibes-coffee-roastery-al-kout-mall` (2131/2634) — verified still on the old persuasive body
(live `wp post list` check, 2026-07-02). Same flow, gated only on their approved MDs landing
from the Content Writer. No blockers on Blog's side — kit is fully hardened on both the EN
and AR paths.

## Ask of Advisor
Update STATE.md's Content-Writer-lane line (currently: *"Mezo guide re-authored neutral +
BLOG-PASS'd (the validated model); 5 remaining guides queued through the same flow, gated on
the image-height cap... + the Blog kit EN-update path"*) to reflect: **3 of 6 done
(mizumesa, naranj, anosha); 3 remain (south-avenue, keif, vibes); both named gates
(image-height cap v1.14.185, Blog kit EN-update path) are CLOSED** — nothing left blocking
the remaining 3 on Blog's or Builder's side; only the Content Writer's MDs are the pacing
item now.

## State
Blog repo: this handoff + the matching `calendar/editorial-calendar.md` update are the
local record. q8tly-core = shared canon (read-only for Blog, per the six-lane sync model);
this briefing routes **Advisor → STATE.md** (Blog does not write q8tly-core directly).
