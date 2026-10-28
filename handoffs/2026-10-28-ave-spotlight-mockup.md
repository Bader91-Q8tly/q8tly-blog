# Handoff: 28 Oct 2026, AVE (Salhiya) spotlight, mock-up stage

**Brief:** Advisor, 28 Oct: a venue spotlight built on the owner's own review. Mock-up → full EN+AR → WPML-twinned drafts
on «window clear» → publish on the owner's word. **State: MOCK-UP for the owner. Nothing on q8tly.com.**

- Mock-up: `drafts/ave_MOCKUP_EN-AR_2026-10-28.md` (titles, meta, 6 sections + FAQ, 2 samples, hero options, photo plan).
- Listing read (public REST, 28 Oct): EN 2666 / AR 2754, title "AVE" in both, 5G Salhiya St, Kuwait City, Fine Dining,
  **business_hours null**, booking_url = Eat page (not pasted in the text).
- Photos: owner's folder `~/Desktop/new listing /Bader pending /Ave` (the path he gave, not `~/Downloads/Ave`): 29 JPEG/PNG,
  **all portrait, 721–1320 px wide** → no owner photo makes a ≥1520 landscape hero. Hero A = listing gallery `ave-02.jpg`
  (1920×2560, 16:9 crop passes); hero C = native-scale collage (D-180 override). Previews were in the session scratchpad only.
- **`reinject_en.py` fixed:** keeps the post's current status by default; `--status publish|draft` to change it; the cache
  touch uses the same status; render check skipped for non-published posts. Tested offline with mocked SSH (draft stays draft).
  README §6 updated. Sibling note: `populate_ar_twin.py` still defaults to publish unless `--draft` is passed.

## Open (owner)
Arabic name (stored "AVE" / sign «اڤي» / keyword «افي»); hero A or C; portrait body set under the override or hero only;
#02 blurred or swapped; confirm the Clean Up marker = people removal only.

## Route via Advisor
Listing has no hours; "Calm & Quiet" tag vs "sometimes loud"; the listing About carries facts not in the owner's review.

## Update 28 Oct, after 23:40: approved → full articles written (READY TO POST, nothing on q8tly.com)
Owner's choices: hero C (collage, D-180 override as for Bar Frès), portrait body set under the same override, #02 → #13,
«افي» + AVE in titles and «اڤي» once in the text, Clean Up = people removed only, no listing extras, no hours.
- EN → `guide-kit/guides/ave-restaurant-kuwait/article.md` (459 words) · AR → `drafts/ave-restaurant-kuwait_AR_2026-10-28.md`
  (341 words, the owner's own words; D-145 sign-off = his read of the draft). Both `status: draft`, 6 sections + FAQ.
- Images built in `guide-kit/guides/ave-restaurant-kuwait/images/` (hero 2336×1314 collage + inline-1…6), metadata-free, sRGB;
  hashes and sources in that folder's `POSTING.md`, which is also the runbook (lock → kit → AR twin without "+" with
  `--draft` → owner preview → publish on his word). Ramadan §5 refresh due mid-Jan 2027.
- Checked offline with the kit's own parser: required keys, images on disk, alt text, place card, no chrome, no
  lyrics/song titles, no estate wording, no listing extras, no hours. All six links 200.
- Mock-up + `reinject_en.py` fix committed on branch `blog/ave-spotlight` (b49f065, 9ec9901).
