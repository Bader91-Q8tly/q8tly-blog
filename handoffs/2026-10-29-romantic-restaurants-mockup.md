# Handoff: 29 Oct 2026, 7 romantic restaurants in Kuwait (MOCK-UP, waiting for the owner; nothing on q8tly.com)

**Brief:** Advisor, 29 Oct (the owner's 7: Roka, Piatti, Nōya, Solange Maison, Amimoto, AVE, MizuMesa). AR is the lead article
(«مطعم رومانسي الكويت» / «مطاعم رومانسية في الكويت»), EN on "romantic restaurants in Kuwait".

- Mock-up → `drafts/romantic-restaurants_MOCKUP_AR-EN_2026-10-29.md` (titles/meta with counts, occasion-grouped outline, per-listing
  fact table, booking checks, interlinks, AR + EN sample blocks, photos, 5 open points, listing flags).
- All 7 listings read live (EN + AR). All 14 `/go/book/` links 302 to the right venue (Amimoto = the shared Kuwait Towers page).
- Date Night tag + Fine Dining category (EN + AR) are already index, follow, hreflang-paired and in their sitemaps.
- **Photos:** the owner asked mid-session to use the folders in `~/Desktop/new listing /` (better quality than the galleries).
  Hero options all pass: Solange `IMG_4010` (recommended, 1600 wide WebP), Piatti `IMG_5564` (3667 wide), Amimoto `IMG_2286`.
  Nōya and Roka venue shots top out at 941/1034 px, so body photos for them need the D-180 override. MizuMesa has no folder
  in `new listing`; its June photo in `guide-kit/guides/mizumesa-sharq/images/` is used.
- **Kit change needed at the article stage:** `rel="nofollow"` on `/go/book/` links (one line in `publish_guide.py` `md_inline()`).
- AVE AR meta tweak proposed (leading with «مطعم افي»), not written.

**Next:** owner's answers → full EN + AR markdown → drafts on the Advisor's «window clear», under the lock → publish on his word.
Add "refresh by 7 Feb 2027" to the calendar when the guide is posted.

## Update 29 Oct, after 18:40: mock-up APPROVED → EN + AR READY TO POST (drafts only, nothing on q8tly.com)
- Decisions: hero Solange `IMG_4010`; one photo per restaurant (D-180 override for Nōya + Roka); AVE = listing line + pointer to
  the AVE guide; AR headings = stored AR titles (all Latin); grouped by occasion; AVE AR meta swap at publish.
- EN → `guide-kit/guides/romantic-restaurants-kuwait/article.md` (884 words) · AR → `drafts/romantic-restaurants-kuwait_AR_2026-10-29.md`.
  Hero + inline-1…7 exported metadata-free into the guide's `images/` (gitignored).
- **Kit:** `publish_guide.py` now writes `rel="nofollow"` on `/go/book/` links (`md_link()`, shared by the AR/EN re-inject tools);
  README §1 notes it. Offline dry-run clean; both files parse with 7 nofollow booking links, 7 photos with alt, no chrome.
- All 60 links checked (20 unique per article): pages 200, booking 302 to the right venue.
- Runbook, sha256s, AVE meta step and listing flags: `guide-kit/guides/romantic-restaurants-kuwait/POSTING.md`.
  Calendar: pipeline row + "refresh by 7 Feb 2027".

## Update 29 Oct ~19:00: DRAFTS ON PROD (not published); AR booking links blocked on a Builder fix
- Committed + pushed `46d6ba2`. Window clear → lock 15:50:11Z–16:04:52Z → EN **7850** + AR **7852** drafts (trid 7216), hero 7842,
  photos 7843–7849; WPML pair proven; focus keywords set; flushed; both public URLs 404. Backups in BACKUP_LOG.
- ⚠ WPML's "adjust links" rewrote the AR's 7 `/go/book/` links into AR listing links on save (EN fine). Every save re-runs it, so
  no Blog-side patch lasts. Fix = q8tly-core `wpml_sl_blacklist_requests` (Builder) → `handoffs/2026-10-29-to-advisor-wpml-rewrites-go-book-links.md`.
- Next: owner previews; after the Builder fix → re-populate 7852 (draft) → verify → publish on the owner's word → AVE AR meta swap.

## Update 29 Oct 19:15: PUBLISHED (EN 7850 + AR 7852) + AVE AR meta swapped · «publish complete»
- Ruling 19:10: publish both; booking links stay as WPML renders them (code freeze). Lock 16:08:58Z–16:15:48Z; backup; EN → AR
  published; all live proofs pass (see POSTING). EN page also shows listing URLs (WPML converts at display); recorded for 1.14.552.
- AVE 7778: meta description **and** excerpt (schema reads it) now lead with «مطعم افي»; old phrase gone from the page; content unchanged.
- Open: after q8tly-core 1.14.552 → EN served check + AR re-populate (no `--draft`) + verify + record.
