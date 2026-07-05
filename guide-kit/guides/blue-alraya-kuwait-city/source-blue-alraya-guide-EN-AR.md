# Blue (Al Raya branch) — بلو
*Neutral guide/listing content, EN + AR (AR hand-written by Bader, D-145). Project Brief v2.4 (D-168). Category: Restaurants — Food & Drink. Venue: Al Raya, Kuwait City.*

> ## ROUTING
> - **"About" paragraph → Pipeline lane → listing About** at `/places/kuwait-city/blue-alraya/` *(slug to confirm at build)*. AR: `/ar/places/...`.
> - Guide card if used → Blog lane. Photos: blog / photography lane.
> - **Chain handling — DEFERRED (Aseer Time precedent):** "Alraya BR" + own domain = multi-branch chain. Branch-scoped now; ⚠ revisit flag — at 5+ listed branches, set `chain_parent: Blue` retroactively.
> - **Mall-amenity rule applied (B+F precedent):** Al Raya parking + prayer rooms are the complex's, not Blue's — prose only, not tagged.
>
> ## NEEDS BADER
> - **Cuisine ⚠ items** — `Burgers` (not in the raw pack) and `Grill & BBQ` (menu-strength call): one-line confirm from the menu (bluekw.co) or visit, then they ship. `Grab and Go` half-supported (ready meals yes, but sit-down venue) — confirm fits.
> - **Hours provenance** — 6 AM–2:30 AM stated, no sign photographed (Anosha-F1 class). Fine to ship; audit note.
> - **AR business name** — brand renders Latin "Blue"; بلو in title only. Confirm Latin-stays (Pick/B+F pattern).
> - **Coordinates / Maps** — not in the raw pack. Needed for stored pin / Directions.

---

## EN — guide

**About** *(this paragraph is also the listing About — LOCKED by Bader, amended for menu breadth):*

This is the Al Raya branch of Blue, a healthy restaurant in Kuwait City open 6 AM to 2:30 AM. The menu is wide — grilled dishes, platters, and take-home ready meals — with calorie counts on every meal, at around 7.5 KD per person. Seating is indoors, with a family section.

**Key facts**

- Menu: wide — grilled dishes · platters · take-home ready meals · calorie counts on every meal
- Hours: 6:00 AM – 2:30 AM, daily *(stated; no sign photographed)*
- Price: $$ · around 7.5 KD per person
- Location: Al Raya, Kuwait City
- Seating: indoor · family section · kid-friendly · good for groups (6+)
- Delivery: available
- Via Al Raya (not venue amenities): parking · prayer rooms

**Photos:** blog / photography lane.

**› See the full listing:** `[/places/kuwait-city/blue-alraya/]`

---

## AR — الدليل

**نبذة** *(تصلح أيضًا كنبذة "عن المكان" في صفحة المكان — بقلم بدر):*

هذا فرع Blue في الراية بمدينة الكويت، مطعم صحي يفتح من 6 الصبح إلى 2:30 الفجر. المنيو واسع وفيه مشاوي، بلاترز، ووجبات جاهزة تاخذها للبيت. كل وجبة موضّح عليها السعرات الحرارية، فالمكان مناسب للي يبي خيارات صحية وواضحة. السعر تقريبًا حول 7.5 د.ك للشخص الواحد، والقعدة داخلية مع قسم للعائلات.

**معلومات أساسية**

- القائمة: واسعة — مشاوي · بلاترز · وجبات جاهزة للبيت · السعرات موضّحة على كل وجبة
- ساعات العمل: يوميًا، من 6:00 صباحًا إلى 2:30 فجرًا *(حسب الإفادة؛ ما فيه لوحة مصوّرة)*
- الأسعار: $$ · حوالي 7.5 د.ك للشخص
- الموقع: الراية، مدينة الكويت
- الجلوس: داخلي · قسم عائلي · مناسب للأطفال · مناسب للمجموعات (6+)
- التوصيل: متوفر
- خدمات المجمع (مو من المطعم): مواقف · مصلّيات

**› لعرض صفحة المكان كاملةً:** `[/ar/places/kuwait-city/blue-alraya/]`

---

## Listing data — NOT guide prose

**Contact / status**
| Field | Value |
|---|---|
| Phone | 2299 7766 |
| Menu / Website | https://www.bluekw.co *(own domain — stable)* |
| Instagram | @blue__kwt — https://www.instagram.com/blue__kwt |
| Hours | Daily 6:00 AM – 2:30 AM ⚠ stated, no sign |
| Status | Open / operating normally |
| Delivery | Available *(platform unspecified in intake)* |
| Coordinates / Maps | ⚠ missing |

**Taxonomy / structured fields**
- Category (primary): `Cafes`? No — `Restaurants — Food & Drink` *(sit-down healthy restaurant; Pick's Cafes ruling doesn't transfer — Blue has full meals + family section)*
- `chain_parent`: — deferred (see routing)
- Venue (displayed): `Al Raya, Kuwait City` ⚠ D-140 composer treatment for complex/tower venues to confirm (same open item as B+F/360 Mall)
- `price_range`: `$$` — **ruling 2026-07-04**: form ticked `$` but 7.5 KD/person = `$$` on the batch scale (Pick 4 KD = $, Odachi/B+F 15 KD = $$); data over form-tick, Aseer Time precedent in reverse
- `indoor__outdoor`: `indoor`
- `payment_methods`: `KNET,Visa/Mastercard,Cash`

**Cuisine (GD field 59, multiselect — stored labels exact per the ruled 33-value list)**
| EN (stored) | AR (stored, WPML ST) | Status |
|---|---|---|
| `Multi-Cuisine` | مأكولات متنوعة | ✓ — the "wide variety" identity; International rejected (world-cuisine identity ≠ many-kinds-of-food) |
| `Burgers` | برجر | ⚠ NOT in raw pack — confirm from menu (bluekw.co) |
| `Grill & BBQ` | مشويات وباربكيو | ⚠ grilled chicken observed; menu-strength call — confirm |

**Tags**
| EN (stored) | AR (display) | Status |
|---|---|---|
| `Healthy Food` | أكل صحي | ✓ — matches Pick; shared filter label |
| `Grab and Go` | طلبات سريعة | ⚠ half-supported — ready meals yes, but sit-down venue; confirm fits |

**Amenities — venue-true, tag these**
- Indoor seating
- Strong AC
- Family section
- Kid-friendly
- Good for groups (6+)
- Delivery

**Complex-provided — do NOT tag (prose only, B+F rule)**
- Parking *(Al Raya)* · Prayer rooms *(Al Raya)*

**Not available — do not tag**
- Outdoor seating · Valet · Customer WiFi · Shisha · Women-only section/hours · Studying/laptop

---

### Voice note (audit trail)

About locked by Bader (EN Option 2 amended for menu breadth) with hand-written AR, 2026-07-04. Cut per D-168: "perfect if you're trying," "honestly I was surprised," "so fresh and juicy," "didn't feel like diet food," "really easy to stay on track," "really nice and cozy," "you'll definitely enjoy," and the memorable-detail closer. "Wide menu" kept as breadth-fact (B+F's "great variety" cut for the *great*, not the variety). Grilled-chicken smell → "grilled dishes" menu fact. AR adds the explanatory clause "فالمكان مناسب للي يبي خيارات صحية وواضحة" with no EN counterpart — Bader's established localization pattern (Pick precedent), kept. Cuisine set per the ruled list via multiselect; note for B+F retro-fix: its Burger/Steak-house tags map to registered cuisine values `Burgers`/`Steakhouse`.
