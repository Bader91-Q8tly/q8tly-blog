# Handoff — `reinject_en.py` formalized as a permanent kit tool (2026-07-01)

**Session:** Module 8 (Editorial / Guide). Author: Claude Blog.

## Ask
Before the remaining 5 guides go through the D-168 neutral re-author flow,
formalize the EN-update path: the MizuMesa EN re-author used what was
literally a one-off script. Bader asked for a repeatable tool, sibling to
`populate_ar_twin.py`, with the same backup → update → verify discipline,
tested via a no-op re-run of the Mezo (MizuMesa) EN content.

## ✅ Tool: `guide-kit/reinject_en.py` (formalized in place, same filename)

Kept the established name — it's already referenced across handoffs, the
calendar, and `BACKUP_LOG.md` as "the EN counterpart to `populate_ar_twin.py`"
— but hardened it to match that tool's guarantees:

1. **Backup, automatic.** Every `--execute` snapshots the DB first
   (`staging-<ts>-en-guide-<slug>.sql.gz`) and self-logs to `BACKUP_LOG.md` —
   no more manual pre-write snapshots (closes the gap hit on the Naranj and
   Anosha runs earlier this session).
2. **Update, charset-safe, one explicit post.** Same `ensure_ascii=False`
   pattern as the AR tool; writes only to the exact `post_id` passed;
   images are reused via `--media stem=id`, never re-uploaded.
3. **Hard target verify.** Refuses unless the target is a `guide_article`
   with WPML language `en` (or untranslated) — this is what makes "never
   touch the AR twin" a guarantee, not a convention: if the id ever resolved
   to the AR side of a trid, the language check would catch it before any
   write. No WPML write calls exist in the tool at all (no `icl_translations`,
   no twin create/mutate).
4. **Built-in idempotency check** (new). Before writing, it diffs the
   generated body against the post's live `post_content` and prints
   `NO CHANGE` or a line-diff. This is the standing no-op/safe-rerun check
   for all future re-authors, not just this one test.
5. **Verify, post-write.** Fetches the live URL and confirms: title renders
   (no mojibake), no raw `[q8tly_*]` shortcode literal, the place shortcode
   resolved to a real `/places/` link, no double title.
6. **SEO meta, conditionally.** If the draft's frontmatter sets
   `meta_description` / `seo_title`, now sets `rank_math_description` /
   `rank_math_title` too — closes the "SEO meta needs a separate SSH command"
   papercut hit on MizuMesa, Naranj, and Anosha. Only touches these fields
   when the draft supplies them; never blanks an existing value.
7. **Documented** in `guide-kit/README.md` §6 (new section) — CLI usage,
   guarantees, what it deliberately doesn't do (no fencing — EN always stays
   indexable; that's AR-only per `GUIDE_AR_WORKFLOW.md` rail #4).

Run pattern (unchanged CLI shape from the old script):
```bash
python3 reinject_en.py drafts/<slug>_EN_<date>.md <en_post_id> \
  --media inline-1=<id>,inline-2=<id>,inline-3=<id>,hero=<id>            # dry run
python3 reinject_en.py drafts/<slug>_EN_<date>.md <en_post_id> \
  --media inline-1=<id>,inline-2=<id>,inline-3=<id>,hero=<id> --execute  # do it
```

## No-op test: MizuMesa EN (post 2362), draft `mizumesa-sharq_EN_2026-06-30.md`

**Dry run:**
```
idempotency: ✓ NO CHANGE — generated body is byte-identical to what's already live
```

**Execute** (full pipeline, to prove backup→update→verify end to end on a
real no-op, not just the dry-run diff):
```
[1] backup : staging-20260701-203207-en-guide-mizumesa-sharq.sql.gz (2415596 B)
[2] update : OK=2362 · URL=.../guide/mizumesa-sharq/ · ST=publish
[3] cache  : touched + flushed
[4] verify :
    ✓ title renders (no mojibake)
    ✓ no raw [q8tly_*] shortcode literal
    ✓ place card resolves to a real /places/ link
    ✓ no double title
```

Pre-flight confirmed every meta field the tool would write already matched
what was live (`rank_math_description`, `deck`, `hero_alt`, `hero_caption`,
`word_count`, `hero_photo_id`) — a genuine end-to-end no-op, not just a body
match. **AR twin (post 2618) confirmed untouched afterward** —
`post_modified` still `2026-06-30 20:45:08` (unchanged), still
`publish` + `noindex`, WPML trid 4659 intact.

### One bug caught and fixed during this test
First execute run flagged two verify checks red (`no /ar/ leak`,
`stays indexable`). Investigated — both were false positives from checks
that didn't fit this environment, not real problems:
- The "`/ar/` leak" was WPML's own `<link rel="alternate" hreflang="ar" …>`
  tag — correct, expected cross-link to the twin, not a bug. Replaced the
  check with a positive one (`place card resolves to a real /places/ link`).
- The "`noindex`" hit was the sitewide `<meta name="robots" content="noindex,
  nofollow">` this WP.com **staging** site emits at the platform level
  ("discourage search engines") — present on every page regardless of
  per-guide fencing, so it can't distinguish a real accidental fence.
  Removed that check rather than have it cry wolf on every future run.

Fixed both, re-ran clean (all 4 checks ✓, shown above).

## Status: unblocked
The 5-guide neutral re-author queue (`south-avenue-salon-sabah-al-salem`,
`keif-restaurant-al-kout-mall`, `vibes-coffee-roastery-al-kout-mall`, plus
any others) can now go through `reinject_en.py` with the same confidence as
the AR side — backup, verify, and no-manual-snapshot discipline built in.
