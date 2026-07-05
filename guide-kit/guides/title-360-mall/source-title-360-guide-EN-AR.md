# Title (360 Mall) — تايتل
*Neutral guide/listing content, EN + AR (AR hand-written by Bader, D-145). Project Brief v2.4 (D-168). Category: Restaurants — Food & Drink. Venue: 360 Mall.*

> ## ROUTING
> - **"About" paragraph → Pipeline lane → branch listing About** at `/places/{district}/title-360/` *(360 Mall district: South Surra / Al-Zahra — confirm slug, same as B+F)*. AR: `/ar/places/...`.
> - Guide card if used → Blog lane. Photos: blog / photography lane.
> - **Chain handling — DEFERRED:** "360 BR" implies branches. Branch-scoped now; ⚠ revisit at 5+ (set `chain_parent: Title`).
> - **Mall-amenity rule applied (B+F precedent — also 360 Mall):** parking + prayer room are the mall's → prose, not tags. (Indoor + family section are the venue's own — tagged.)
>
> ## NEEDS BADER / PIPELINE
> - **⚠ PRICE `$$$` — PENDING PIPELINE (joins Select).** Founder call; fights the data (form ticked `$$`/mid + 15 KD, and 15 KD = `$$` for Odachi/B+F). Now the SECOND 15-KD-pushed-to-`$$$` (with Select). One pipeline ruling reconciles all: Odachi + B+F ($$) vs Select + Title ($$$), all ~15 KD. Shipped `$$$` provisionally.
> - **`American` cuisine — founder addition.** Intake said "Italian food" only; Bader added American from menu knowledge. Both shipped; noted it's founder-sourced, not intake.
> - **Hours** — 12:00 PM – 11:00 PM stated, no sign photographed (Anosha-F1 class).
> - **Coordinates / Maps** — not provided.

---

## EN — guide

**About** *(this paragraph is also the listing About — LOCKED by Bader; updated to Italian + American, price line removed):*

A restaurant at 360 Mall serving Italian and American dishes, with a wide menu for lunch and dinner. One nice detail is the complimentary welcome drink on arrival. Seating is indoors, with a family section.

**Key facts**

- Cuisine: Italian · American
- Nice detail: complimentary welcome drink on arrival *(kept from the visit)*
- Hours: 12:00 PM – 11:00 PM, daily *(stated; no sign photographed)*
- Price: $$$ ⚠ pending pipeline · around 15 KD per person
- Location: 360 Mall
- Seating: indoor · family section · kid-friendly · good for groups (6+)
- Delivery: available

**Photos:** blog / photography lane.

**› See the full listing:** `[/places/{district}/title-360/]`

---

## AR — الدليل

**نبذة** *(تصلح أيضًا كنبذة "عن المكان" في صفحة المكان — بقلم بدر):*

مطعم في 360 مول، يقدم أطباق إيطالية وأمريكية مع منيو واسع للغداء والعشاء. من التفاصيل الحلوة عندهم إنهم يقدمون مشروب ترحيبي عند الوصول. القعدة داخلية، وفيه قسم للعائلات.

**معلومات أساسية**

- المطابخ: إيطالي · أمريكي
- تفصيلة حلوة: مشروب ترحيبي عند الوصول
- ساعات العمل: يوميًا، من 12:00 ظهرًا إلى 11:00 مساءً *(حسب الإفادة؛ ما فيه لوحة مصوّرة)*
- الأسعار: $$$ ⚠ بانتظار البايبلاين · حوالي 15 د.ك للشخص
- الموقع: 360 مول
- الجلوس: داخلي · قسم عائلي · مناسب للأطفال · مناسب للمجموعات (6+)
- التوصيل: متوفر

**› لعرض صفحة المكان كاملةً:** `[/ar/places/{district}/title-360/]`

---

## Listing data — NOT guide prose

**Contact / status**
| Field | Value |
|---|---|
| Phone | +965 9666 9201 |
| Menu | https://qr.finedinemenu.com/title360?... *(QR-service link — reasonably stable, watch for rot)* |
| Instagram | @titlekw — https://www.instagram.com/titlekw |
| Hours | Daily 12:00 PM – 11:00 PM ⚠ stated, no sign |
| Status | Open / operating normally |
| Delivery | Available |
| Coordinates / Maps | ⚠ missing |

**Taxonomy / structured fields**
- Category (primary): `Restaurants — Food & Drink`
- `chain_parent`: — deferred (see routing)
- Venue (displayed): `360 Mall` ⚠ mall composer treatment to confirm (same open item as B+F)
- `price_range`: `$$$` ⚠ **PENDING PIPELINE** (see flag — 15 KD vs $$ precedent; joins Select)
- `indoor__outdoor`: `indoor`
- `payment_methods`: `KNET,Visa/Mastercard,Cash`

**Cuisine (GD field 59, multiselect — stored labels exact per ruled 33-value list)**
| EN (stored) | AR (stored, WPML ST) | Status |
|---|---|---|
| `Italian` | إيطالي | ✓ stated |
| `American` | أمريكي | ⚠ founder addition (intake said Italian only) — shipped on Bader's menu knowledge |

**Tags** *(from Bader, 2026-07-04)*
| EN (stored) | AR (display) | Status |
|---|---|---|
| `Date-Night` | أجواء رومانسية | ⚠ **Founder call.** Intake reads family/groups ("bring your friends," family section, kid-friendly), not romantic — not intake-derived. Shipped on Bader's read (same class as AVE's founder-call tags). |

*(Bader's `Italian`/`American` "tags" re-filed to cuisine multiselect above. `Family` NOT tagged — it's a venue amenity below; forward-rule, no double-tag.)*

**Amenities — venue-true, tag these**
- Indoor seating
- Strong AC
- Family section
- Kid-friendly
- Good for groups (6+)
- Delivery

**Mall-provided — do NOT tag (prose only)**
- Parking *(360 Mall)* · Prayer room *(360 Mall)*

**Not available — do not tag**
- Outdoor seating · Valet · Customer WiFi · Shisha · Women-only section/hours · Good for studying/laptop

---

### Voice note (audit trail)

About locked by Bader with hand-written AR, 2026-07-04; updated from the original Italian-only draft to Italian + American per Bader, price line removed (Chef Pillai precedent — price stays in data, out of prose). Cut per D-168: "if you love Italian you'll enjoy," "something for everyone," "everything was delicious," "really nice touch," "warm and lively," "worth it," "I'd definitely recommend," and the bring-your-friends blockquote. Kept as fact: complimentary welcome drink (Naranj free-dessert / Chef Pillai sulemani-tea class), wide menu. `American` cuisine + `Date-Night` tag both flagged as founder-sourced (not intake). `$$$` PENDING PIPELINE — Title joins Select as the second 15-KD-→-$$$ escalation; one ruling reconciles the four 15-KD venues. `Family` kept as amenity, not double-tagged.
