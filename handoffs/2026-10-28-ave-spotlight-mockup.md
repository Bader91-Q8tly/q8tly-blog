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
