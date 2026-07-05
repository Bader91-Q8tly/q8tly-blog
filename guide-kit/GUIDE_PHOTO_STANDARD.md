# Guide-Photo Qualification Standard — D-180 candidate (DRAFT, pending ratification)

> **Owner ruling (2026-07-05):** *A listing only becomes a guide if its photo set
> fits the guide frame cleanly; otherwise the guide is **DEFERRED** (the listing
> stays live) and we move to the next guide-ready business.* This file is the
> checklist that ruling asks for. **Odachi = the reference pass; B+F = the
> rescue-by-crop test case.** Status: DRAFT for ratification (routes Advisor →
> Decision Log as D-180). Frame numbers below are Blog's **measured** working
> values — **Builder is supplying the authoritative numbers** (they pair with the
> featured-image crop-fix handoff, 2026-07-05); update this table when they land.

## 1. The frames a guide photo must survive
The **same** featured image is re-cropped in several places, each a different
ratio, all center-anchored (until Builder adds focal-point). A photo "fits" only
if its subject survives **every** frame it will appear in.

| Context | Desktop | Mobile | Source size |
|---|---|---|---|
| Blog-post header (hero) | 16:9 | 16:10 | `q8-hero` 1600×900 |
| Homepage **Featured** guide card | 16:10 | 3:2 | `q8-hero` |
| Homepage **Latest** guide card | 16:9 | 3:2 | `q8-latest` 800×450 |
| In-body inline photo | ~7:5 (1.4:1) | ~1:1 | wp `large` |

**Safe zone (the load-bearing idea):** because the hero is shown from 16:9 down to
~1:1, the subject (sign / logo / dish / face) must sit inside the region common to
**all** those crops — i.e. **centered, with ≥~15% margin on every side, and never
touching an edge (the top especially).** If the subject is jammed to an edge in the
source, no single crop saves every context → it fails.

## 2. Qualification checklist (run per guide, BEFORE it publishes)

**A. Hero / storefront**
- [ ] A storefront/sign shot exists and the business **name is fully legible** (Latin and/or Arabic).
- [ ] The name/sign stays fully inside the frame in a 16:9 **and** a 3:2 **and** a ~1:1 centre-crop — not touching any edge (esp. top).
- [ ] If no usable name-bearing storefront exists, a **food/setting hero is allowed only if clearly intentional**, landscape-friendly, and clean (Keif/Vibes precedent).

**B. The set as a whole**
- [ ] **Enough frame-fitting photos:** ≥1 clean hero + ≥3 body photos that survive the 7:5 / ~1:1 inline frames.
- [ ] **Consistent aspect ratios** — no jarring portrait ↔ landscape (or 3:4 ↔ 9:16) jumps within the body set; they should all crop to the same display ratio cleanly.
- [ ] **Subjects not near the crop edges** — centred with margin, so a tighter context-crop never clips them.

**C. Body / detail photos**
- [ ] Food/detail shots only where the subject is **intentionally in-frame** — the whole dish/plate reads after the 7:5 crop, not a sliced fragment.
- [ ] **No competing brand/logo** dominating the frame (e.g. a neighbouring store's sign).
- [ ] Exposure is workable — not so dark the subject is lost after WebP compression.

## 3. Outcome
- **All boxes tick → guide-ready.**
- **Portrait sources do NOT auto-fail.** If the subject sits safely inside the safe
  zone, a **pre-crop rescue** is valid: hero → 16:9, inline → 7:5, centred on the
  subject (Odachi / B+F precedent). **Note the crop in the ledger.**
- **Any hard box fails and no crop rescues it → DEFER.** The listing stays live; the
  guide is flagged *"deferred pending better photo."* Move to the next guide-ready
  business. For an **already-published** guide, retire/hold is the **owner's**
  per-case call, not Blog's.

## 4. Interaction with the template fix
This standard is the **content-side gate**; Builder's featured-image crop fix
(focal-point → `object-position`, consistent ratios) is the **template-side fix**.
Once Builder lands focal-point, criterion A relaxes (a subject slightly off-centre
can be nudged with `hero_focus` instead of deferred), and the guide-kit will set
`hero_focus` per guide. Until then, the safe-zone rule + pre-crop rescue stand.
