# Villa Shams Beach Club — فيلا شمس
*Neutral guide/listing content, EN + AR (AR hand-written by Bader, D-145). Project Brief v2.4 (D-168). **Dual-category** (pipeline-ratified 2026-07-04). Area: Messilah.*

> ## ROUTING
> - **"About" paragraph → Pipeline lane → listing About** at `/places/messilah/villa-shams/` *(slug to confirm)*. AR: `/ar/places/...`.
> - Guide card if used → Blog lane. Photos: blog / photography lane.
> - **Dual-category — pipeline-ratified (commit cedece7, 2026-07-04):** singular-category rule is stale in the current build (listing URL never contains the category; dual-category live-proven on Keke + South Avenue, URL/SEO-safe). Villa Shams is a genuine two-nature venue → ships dual. Blue + Wooden Bakery stay Shape 1 (not two-nature).
>
> ## NEEDS BADER
> - **"First women's beach club in Kuwait" — NOT asserted.** The intake claims it ("first fully equipped beach club for women in Kuwait"); withheld pending Bader's confirm — a "first" claim shouldn't ship on the visitor's word. Say the word to assert.
> - **EN About = Option 1** (fullest, mirrors the AR). Flag if you want Option 2 or 3.
> - **Seasonal status** — "only in summer." ⚠ Needs a real seasonal/status treatment: the listing must NOT read "Open" off-season. Confirm whether the build has a seasonal-status field or this is prose + a manual open/close. Flagged for pipeline.
> - **Payment / entry model** — no KNET/cards/cash at a counter; entry is **online reservation only** (villashams.com). Price is a **day-pass**, not per-plate. Store accordingly.
> - **Coordinates / Maps** — not provided. Needed for pin / Directions.

---

## EN — guide

**About** *(this paragraph is also the listing About — Option 1, mirrors the AR; "first" claim withheld):*

Villa Shams is a women-only beach club in Messilah, open in the summer season. It has an open swimming beach, a large and a small pool, changing rooms, and rotating pop-up kiosks, along with an Italian restaurant on site. Entry is by online reservation — around 32 KD on weekdays and 38 KD on weekends, the weekend rate including a DJ. Valet parking and a prayer room are available.

**Key facts**

- Type: women-only beach club *(defining feature)*
- Season: summer only ⚠ seasonal — see status flag
- Facilities: swimming beach · large + small pool · changing rooms · rotating pop-up kiosks · on-site Italian restaurant · tanning area
- Entry: online reservation only *(no walk-in)*
- Price: $$$ · day-pass ~32 KD weekday / ~38 KD weekend (DJ included) — *day-pass, not a per-meal price*
- Hours: 9:00 AM – 6:00 PM *(stated; no sign photographed)*
- Location: Messilah
- Valet parking · prayer room *(venue's own — not a mall)*

**Photos:** blog / photography lane.

**› See the full listing:** `[/places/messilah/villa-shams/]`

---

## AR — الدليل

**نبذة** *(تصلح أيضًا كنبذة "عن المكان" في صفحة المكان — بقلم بدر):*

نادي شاطئي نسائي في المسيلة، يفتح خلال موسم الصيف. المكان فيه شاطئ مفتوح للسباحة، مسبح كبير ومسبح صغير، غرف تبديل، وكشكات مؤقتة تتغير بين فترة وفترة، بالإضافة إلى مطعم إيطالي داخل المكان. الدخول يكون بالحجز أونلاين، والسعر تقريبًا 32 د.ك في أيام الأسبوع و38 د.ك في الويكند، وسعر الويكند يشمل DJ. وتتوفر خدمة صف السيارات ومصلى.

**معلومات أساسية**

- النوع: نادي شاطئي نسائي *(ميزة أساسية)*
- الموسم: الصيف فقط ⚠ موسمي
- المرافق: شاطئ للسباحة · مسبح كبير وصغير · غرف تبديل · كشكات مؤقتة متغيّرة · مطعم إيطالي داخل المكان · منطقة تسمير
- الدخول: بالحجز أونلاين فقط *(لا يوجد دخول مباشر)*
- الأسعار: $$$ · تذكرة يوم ~32 د.ك في الأسبوع / ~38 د.ك في الويكند (يشمل DJ)
- ساعات العمل: 9:00 صباحًا – 6:00 مساءً *(حسب الإفادة؛ ما فيه لوحة مصوّرة)*
- الموقع: المسيلة
- صف سيارات · مصلّى *(من المكان نفسه)*

**› لعرض صفحة المكان كاملةً:** `[/ar/places/messilah/villa-shams/]`

---

## Listing data — NOT guide prose

**Contact / status**
| Field | Value |
|---|---|
| Phone | +965 6363 1725 |
| Reservations | Online only — https://www.villashams.com/villa-shams *(tracking params stripped)* |
| Menu | https://menu.matix.one/m/villashams/... |
| Instagram | @villashams.beachclub |
| Hours | 9:00 AM – 6:00 PM ⚠ stated, no sign |
| Season | Summer only ⚠ seasonal-status treatment needed |
| Status | Open in season / operating normally |
| Delivery | None |
| Coordinates / Maps | ⚠ missing |

**Taxonomy / structured fields — DUAL-CATEGORY**
- **Category (primary): `Pools & Swim Clubs`** (term 1582, مسابح ونوادي سباحة) — `default_category=1582`; owns breadcrumb + card label
- **Category (secondary): `Beaches`** (term 1524, شواطئ) — listing renders in both archives; both AR-ready per the category tree
- Area (displayed): `Messilah` *(D-140: non-mall → Area only)*
- `price_range`: `$$$` *(day-pass model, not per-plate — noted)*
- `indoor__outdoor`: `outdoor` *(beach/pool venue)*
- `payment_methods`: — **online reservation only**; no counter KNET/cards/cash. Store per pipeline convention for reservation-only venues.

**Tags** *(approved by Bader, 2026-07-04)*
| EN (stored) | AR (display) | Status |
|---|---|---|
| `Women-Only` | نساء فقط | ✓ defining fact — same stored label as Queue Café / Elysee |
| `Seasonal` | موسمي | ✓ approved ⚠ new vocab — register; pairs with the seasonal-status field question |
| `Valet Parking` | خدمة صف السيارات | ✓ venue's own (not a mall) |

*(Held OFF, per discussion: `Italian` — the on-site restaurant is Italian, but tagging the *club* Italian mis-signals to cuisine filters; if the restaurant gets its own split listing later, it carries `Italian` then. `Beach` tag — redundant with the `Beaches` category. `Groups 6+` — amenity, not double-tagged.)*

**Amenities — venue-true**
- Valet parking
- Easy self parking
- Prayer room *(venue's own)*
- Women-only
- Swimming beach · large pool · small pool · changing rooms · tanning area

**Not available — do not tag**
- Indoor seating · Outdoor seating *(table-seating sense)* · Strong AC · Delivery · Customer WiFi · Shisha · Family section · Good for studying/laptop · Kid-friendly

---

### Register flags (for the Advisor pass, per pipeline note)
1. **"Beach Clubs" taxonomy gap** — Villa Shams needed two cross-pillar categories because no single "Beach Clubs" category exists. Candidate for the register.
2. **Dual-category criterion** — codify in the Brief when dual-category is warranted (genuine two-nature venue) vs Shape 1 (category + tag), so the singular-rule text is updated to match the ratified build behavior.
3. **`Seasonal` vocab + status field** — new tag + the open/closed-by-season handling.

### Voice note (audit trail)
About = Option 1 (default; Bader didn't pick — flagged), mirrors the AR. Cut per D-168: "perfect for girls," "fun and relaxing," "everything you need," "loved hearing," "so fun and lively," "really good food," "tan comfortably," "definitely worth visiting," and the spend-the-whole-day blockquote. Kept as fact: pools/beach/changing rooms/kiosks/tanning/on-site Italian restaurant, music-through-the-day (folded into DJ/weekend fact), reservation model, day-pass pricing. "First women's beach club" withheld pending confirm. Dual-category applied per pipeline ratification (commit cedece7). AR typo fixed at packaging: "متوفر بعد خدمة صف السيارات ومصلى" → "وتتوفر خدمة صف السيارات ومصلى".
