# Things to Do in Kuwait (tourism pillar): posting record

Brief: owner, 30 Oct 2026 ("Things to Do in Kuwait" EN + AR, our main tourism page). **Save as DRAFT in both languages;
don't publish until the owner has reviewed it.** New guide posts are allowed during the app 1.3 freeze (owner, 30 Oct);
code, theme and template changes stay frozen, so no map and no "Featured in" block (both need a template change).

> **Owner's decisions (30 Oct 2026, approval: "Approved. Publish both versions."):**
> 1. Free box = only what's true: add the public places with **no entry ticket** (Arabian Gulf Street's public seafront, the
>    Marina Crescent promenade, The Avenues mall entry), worded "no entry ticket", not "free"; keep the two sourced free entries
>    for young children; nothing else.
> 2. H1 stays as it is (the exact phrase is in the first sentence, three H2s and the FAQ).
> 3. The GPS-only photo (inline-7, "Trees at Scientific center", captioned as ASCC) is **removed**: we don't caption a photo with a
>    place we can't confirm. Attachment 7889 stays in the media library, unused. ASCC exterior = shot list #5.
> 4. **Souq Al Mubarakiya restored: the owner personally confirmed it's open** (no official account exists). 13 places.
> 5. Al Khiran and Failaka stay out.
> 6. After publishing: burger guide → this page link, live checks (200, hreflang, canonical, sitemap, index), live URLs.
> 7. Commit and push guide files, records and the `publish_guide.py` fix, after a credentials check.
> 8. Listing data problems as a separate list for the listings team.

## Files
- EN: `guide-kit/guides/things-to-do-in-kuwait/article.md`
- AR: `drafts/things-to-do-in-kuwait_AR_2026-10-30.md` (written natively in Kuwaiti dialect, Western digits)
- Images: `guide-kit/guides/things-to-do-in-kuwait/images/` (gitignored, local only; original Commons files, byte-identical)
- Map: `map-attractions.csv` (12 attractions) and `map-eat-nearby.csv` (every linked listing), columns `name,lat,lng`, for a
  Google My Maps embed. The theme can't draw a map from coordinates: `[q8tly_map]` only takes listing IDs and renders a
  numbered list with Directions links, so a real map needs a template change (after the freeze, via the Advisor).

## Attractions: open checks (30 Oct 2026)
Rule: on the page only if the attraction's OFFICIAL website or OFFICIAL social account shows it open now. News alone = not
enough. The regional situation is never mentioned on the page.

### Kept (12)
| # | Attraction | Official evidence (30 Oct) | Hours / fees on the page (official source) |
|---|---|---|---|
| 1 | Kuwait Towers | TEC page (operator; © 2026, no closure notice) + @kuwait.towers posts to 19 Oct 2026 | 8 AM–11 PM (may vary on holidays); viewing sphere 2–11 PM. Fees: not on official source, not stated |
| 2 | Grand Mosque (tours) | @thegrandmosque (Ministry of Awqaf) X post 29 Oct 2026: visits 25–29 Oct; tour-times graphic 31 Aug 2026; Awqaf visit form live 30 Oct | Sun–Thu 9 AM–1 PM and 3:30–7 PM (subject to prayer times); Fri/Sat by appointment; 45–90 min; AR/EN/FR. Fee: not stated |
| 3 | Al Sadu House | @saduhouse posts 10 Sep (exhibition opening 14 Sep) and 21 Oct 2026 (children's programme to 14 Nov) | alsadu.org.kw/museum: 8 AM–1 PM and 4–8 PM, closed first two days of Eid (page from 2022, no days named). Fee: not stated |
| 4 | Tareq Rajab Museum | @trmkuwait post 20 Oct 2026 (visit); trmkt.org hours/fees | Sat–Thu 9 AM–1 PM and 4:30–8:30 PM; Fri 9 AM–1 PM; KD 3 adults, KD 1.5 under 18, free under 6; one ticket for both museums |
| 5 | Arabian Gulf Street | Public road; TEC waterfront page is the official reference | No hours/fees given (TEC's 8–11 on that page are for its facilities, not quoted) |
| 6 | Al Shaheed Park | alshaheedpark.kw (new official site, © 2026) + @alshaheedpark posts 20–28 Oct 2026 | Park 5 AM–midnight; museums Sat–Thu. Fees: not stated. Old domain alshaheedpark.com is broken, not linked |
| 7 | The Scientific Center | tsck.org.kw IMAX schedule shows 30 Oct 2026 screenings; @scicenterkw posts 22–29 Oct | 9 AM–10 PM; FAQ says Fri from 2 PM (the site's own pages conflict, both stated). Fees: not on any readable official page |
| 8 | Sheikh Abdullah Al Salem Cultural Centre | booking.ascckw.com: 30 Oct–2 Nov open days, tickets sold for 30 Oct; @ascckw posts 14–29 Oct | Mon–Thu + Sat 9 AM–10 PM, Fri 2–10 PM, last entry 9 PM; KD 3 / 2 (under 18) / 1.5 (60+), under-2s free; planetarium KD 2 |
| 9 | Marina Crescent | marinaworld.com.kw (opening hours) + @themarinamall posts 13–28 Oct 2026 (whole complex) | Shops 10 AM–10 PM weekdays, to 11 PM weekends; restaurants inside 9 AM–11 PM. The "Crescent side 07:00 am – 12:00 pm" line looks like a typo, not quoted |
| 10 | Sheikh Jaber Al-Ahmad Cultural Centre | jacc-kw.com What's On lists 30 Oct 2026 8:30 PM and later dates; 2026–27 season PDF; @jacc_kw posts 21–29 Oct | Building hours/tours: not on official source (no tours promised). Tickets only via JACC app/website; dress code from the season PDF |
| 11 | Al Salam Palace Museum | aspm.com.kw booking shows Standard Tour slots 1–12 Nov 2026; @aspm.kw 9 May 2026 "reopens to the public" | Morning tours Sun–Thu 9 AM–2 PM; evening Sat/Mon/Wed 5–8 PM; arrive 15 min early; standard tour 2 h, AR/EN, KD 8; online only, ≥24 h ahead; no children under 12 |
| 12 | The Avenues | the-avenues.com live status 30 Oct ("10 AM – 11 PM"); operator Mabanee @mabaneeco post 10 Oct 2026 | Hours NOT printed: the site's live status says 10 AM–11 PM, its footer says 8 AM–10 PM (template text). Facts from the official about/services pages (12 districts, 1,100+ stores, respectful clothing, pet-free) |

### Dropped or flagged (not on the page)
- **Kuwait National Museum: DROPPED.** NCCAL (@kw_nccal, X, 22 Oct 2026): «إغلاق متحف الكويت الوطني لحين الانتهاء من أعمال الصيانة»
  (closed until maintenance is finished; no reopening date).
- **Bait Al Othman: DROPPED.** Closed for maintenance since ~Oct 2024 (Al-Rai, news); its own account silent since Nov 2024;
  NCCAL's 26 Sep 2026 post is a poster with no "open" statement. A call to 22653323 could change this.
- **Green Island: DROPPED.** No official site/account; TEC is redeveloping it (Jan 2026 launch, demolition reported Jun–Jul 2026).
- **Souq Al Mubarakiya: RESTORED 30 Oct on the owner's personal confirmation (decision 4).** Was flagged: It's a public market with no operator account that posts; only news shows it
  operating (stall lottery 12 Oct 2026, smoking-fine campaign Sep 2026). The fire-damaged block is being rebuilt (KFH contract,
  2024). **Owner's call:** restore it if you're happy with "open public market" as the evidence. Parked text below.
- **Al Khiran / Sabah Al Ahmad Sea City: FLAGGED, left out.** No mall-run official channel (developer page undated; only IKEA's
  own hours). Khiran Resort (TEC) has an official 4 Dec 2026 event but no hours/fees. Boat activities: nothing official.
- **Souq Sharq: not used.** Checked as a possible addition: closed since 31 Jan 2026 (Ministry of Finance eviction; being redeveloped).
- **Failaka Island: FLAGGED, left out.** The ferry is officially confirmed: Joan Al Kuwait Marine (@joanalkuwait) posted the
  November 2026 Ras Al Ard ⇄ Failaka timetable on 26 Oct (no Friday sailings; some days one-way only; fares not official).
  Nothing official confirms the heritage village or visitor access to the archaeological sites, so there's nothing to send
  people to once they land. Restore if you want a ferry-only entry.

## "Free things to do" box (owner's decision 1, 30 Oct)
Only what's true. Rows: Arabian Gulf Street (public seafront), the Marina Crescent promenade and The Avenues (mall entry), worded
"no entry ticket" (not "free"); plus the two sourced free entries for young children (Tareq Rajab under-6, ASCC under-2).
Nothing else. FAQ 2 says the same. (No official source says general entry is free for any attraction on the page.)

## Eat nearby (our listings): open checks (30 Oct)
Facts from each listing (live GeoDirectory API, EN + AR). Every one checked for a closure/move notice and recent activity
(Instagram post dates, venue sites, delivery-app listings; Google Maps not used). No closure notices anywhere.
- **Taken out (weak evidence):** Hoffee (no posts since 29 Jun 2026), EQ (no posts since 19 Feb 2026; a directory shows
  "Closed"), Toby's Estate Jabriya (branch and drive-thru not confirmed anywhere current), Dalaq Assail (souq; own posts
  stop 12 Feb 2026, nothing from 2026 places it in the souq; checked 30 Oct before restoring the souq).
- **Souq restaurants (checked 30 Oct):** Al Shemam OK (Mubarakiya branch named in an 18 Jul 2026 collab; posts geotagged in the
  souq Apr–May 2026); Bab Al Yemen and Assk Kahve OK (first check).
- **Quiet but no warning signs (kept):** Novikov Brasserie (last post 21 Sep), Below Zero (14 Sep), Jumparoo (8 Sep).
- **Distances:** straight-line from the attraction; everything is in the same building or within about 1 km, except the Tareq
  Rajab Museum (Jabriya has few listings: Fish Market Salmiya ~2 km, EDO ~2.5 km, stated on the page).

| Attraction | Eat nearby (EN listing → AR listing) |
|---|---|
| Kuwait Towers | Amimoto 3125, Fish Market 6743, Mais Alghanim 1861 |
| Grand Mosque | The Grove 7690, TAP BAKERY 5260, Title 4802 |
| Souq Al Mubarakiya | Al Shemam 4710, Bab Al Yemen 3267, Assk Kahve 1911 («عشق») — all inside the souq |
| Al Sadu House | Piatti 7408, Slider Station 6142 (~300 m) |
| Tareq Rajab Museum | Fish Market Salmiya 7018 («مطعم فيش ماركت»), EDO 6996 («إدو») |
| Arabian Gulf Street | Slider Station 6142, Babel 1837 (+ link to the burger guide) |
| Al Shaheed Park | Fired 6639, Odachi 2432, Neighbors Matcha 4561 |
| Scientific Center | Naranj 2239, Toby's Estate Salmiyah 1833 |
| ASCC | Untold 7620, OKAN 7712, EDO 6996 |
| Marina Crescent | Melt 7708, Espresso Lab 4107, Jihan 3669 (+ Marina Mall listing 2346) |
| JACC | Novikov Brasserie 5368, White Robata 3914 (both at the centre) |
| Al Salam Palace Museum | Novikov Brasserie 5368, White Robata 3914 (~700 m, at JACC) |
| The Avenues | Em Sherif Café 5350, Said Dal 1923 3019, Wooden Bakery Avenues 2947 (+ The Avenues listing 2344, VOX 6529) |
| Indoor activities | Below Zero Marina Mall 5829, Jumparoo 4507 («جمباروو»), Wonderkin 4742, VOX Cinemas 6529, Fun City 3992 |

No restaurant photos on this page: the brief's rule for them is "bloggers' photos only", and the attraction photos already
carry the page (the listing pages have the bloggers' photos). Easy to add per venue if wanted.

## Photo log (Wikimedia Commons; original files, unmodified, SHA-1 matches Commons)
All CC BY or CC BY-SA (no NC, no ND), all ≥1200 px wide. No identifiable faces (checked at full size), no AI images, nothing
from Google Maps or Instagram, no government, military or security buildings. Credit line under each photo:
"Photo: [author] / Wikimedia Commons / [licence]" (AR «الصورة: … / ويكيميديا كومنز / …»), author linked to the file page and
the licence linked to its deed. The hero credit is the hero caption (plain text: the template escapes links in `hero_caption`)
and is repeated with links in the last line of the page.

| Stem | Used for | File (source URL) | Author | Licence | Size | Taken | sha256 (= file served on q8tly.com) |
|---|---|---|---|---|---|---|---|
| hero | Kuwait Towers (hero) | https://commons.wikimedia.org/wiki/File:Kuwait_(31420655062).jpg | Jaafar Alnasser (via Flickr) | CC BY 2.0 | 4856×2374, 3.8 MB | 16 May 2016 | 5658de11cb8e25e11551d5814aae0c0e6add500fdd865e78abbf9169d42d502a |
| inline-1 | Kuwait Towers | https://commons.wikimedia.org/wiki/File:Kuwait_tower_at_dusk.jpg | Samarstha45 | CC BY-SA 4.0 | 4032×3024, 2.9 MB | 7 May 2023 | 31d9e4effdb91873cd23f35de42be76bb0725ba0aa9550f4c255b09a806f33c6 |
| inline-2 | Grand Mosque | https://commons.wikimedia.org/wiki/File:Kuwait_City_Grand_Mosque_Exterior_South_Facade_1.jpg | Zairon | CC BY 4.0 | 4529×2811, 5.4 MB | 3 Dec 2022 | e28743196986b0d159ef565fd5ed0ce73d456bd334c9fd0c6bf334f660a6eea4 |
| inline-3 | Tareq Rajab Museum | https://commons.wikimedia.org/wiki/File:TRM_Gold_Room.jpg | Tnrajab | CC BY-SA 4.0 | 6075×4160, 3.4 MB | 15 Oct 2023 | 7a070f24da44c61a0121d07d89d1b94386fb79f6017771654223df369423a5e6 |
| inline-4 | Arabian Gulf Street | https://commons.wikimedia.org/wiki/File:Kuwait_City_Kuwait_Towers_View_to_the_Arabian_Gulf_Street_1.jpg | Zairon | CC BY 4.0 | 4574×3094, 1.6 MB | 3 Dec 2022 | 90cc44588bd284a76215b12ee7f263b3ccbb2954e6d944d034570b357de3178e |
| inline-5 | Al Shaheed Park | https://commons.wikimedia.org/wiki/File:A_pathway_with_modern_streetlights_and_trees_in_Al_Shaheed_Park,_Kuwait.jpg | Coretto958 | CC BY-SA 4.0 | 3888×2592, 0.6 MB | 22 Mar 2025 | b155e883278e26181c7a1b23dd159abee9314f4f283a3804a7b1b328b39058c5 |
| inline-6 | Scientific Center (aquarium) | https://commons.wikimedia.org/wiki/File:View_from_kuwait_scientific_centre_in_salmiya_(20).jpg | irvin calicut | CC BY-SA 3.0 | 2592×1944, 0.8 MB | 25 Aug 2011 | 397ad65c2d06830ed753c49163fc7a90e88fb29914bcdbe8683ccdb66e595468 |
| inline-8 | The Avenues | https://commons.wikimedia.org/wiki/File:Prestige_the_avenues_mall_of_Kuwait.jpg | Jassem1992 | CC BY-SA 4.0 | 4284×5712 (portrait), 9.1 MB | 27 Feb 2024 | cd54b25a1e1ab92b503db87cb1a56fe55bff6d68409156a65e4d90ae27e6e54f |
| ~~inline-7~~ (REMOVED 30 Oct, owner) | ASCC | https://commons.wikimedia.org/wiki/File:Trees_at_Scientific_center,_Kuwait.jpg | Kishore R Sudarsan | CC BY-SA 4.0 | 4624×3472, 5.1 MB | 5 Nov 2022 | 56a3a25b50a22a4bce646167d5aa03023329142e17a2ed25167f9e2c9b8ec6ea |
| inline-9 | Souq Al Mubarakiya (restored 30 Oct) | https://commons.wikimedia.org/wiki/File:Kuwait_City_Souq_al-Mubarakeya_3.jpg | Zairon | CC BY 4.0 | 4536×2988, 5.0 MB | 3 Dec 2022 | f945c2486a24b4fa1113733589b2420f0fa9bdd95eeeaa6383e99151a253927c |

Notes:
- **inline-7 REMOVED from both pages (owner, 30 Oct): "we don't caption a photo with a place we can't confirm"; attachment 7889 stays unused in the library.** It was captioned as ASCC although its Commons title says "Scientific center". Its GPS tag (29.343452, 48.040928) is the
  Sheikh Abdullah Al Salem Cultural Centre (which has a Science Museum), 4.7 km from the Scientific Center in Salmiya, and the
  pale stone walls match ASCC. Owner: confirm, or swap for a blogger shot.
- **Hero crop:** the file is uploaded unmodified, but the theme displays the hero as a 16:9 crop (q8-hero). This photo is
  about 2:1, so the display trims about 6.5% from each side; both towers stay in frame.
- **Rejected:** Al Shaheed Park fountains (Zs.84): the gold twin towers behind are the Central Bank of Kuwait (government).
  "Kuwait City's popular landmarks Liberty Tower & Kuwait Towers": Liberation Tower (Ministry of Communications).
  Souq photos with people near the camera; the souq interior with portraits of the Emirs; the Scientific Center IMAX photo
  (audience faces); the only JACC file on Commons (CC0, shows a person, not the building); Marina Crescent's only usable
  file (2006, 20 years old); Green Island (2016, date stamp burned in; and the island is dropped).
- **Souq photo (inline-9, attachment 7897):** Zairon, CC BY 4.0, daytime, flags, only distant figures (checked at full size).

## Blogger shot list ("tourism day")
Landscape, ≥1600 px wide (hero: exact 16:9 ≥1600), no identifiable faces, no government/military/security buildings in frame
(watch for: Seif Palace beside the Grand Mosque, the Central Bank twin towers by Al Shaheed Park, the National Assembly and
Liberation Tower).
1. **Al Salam Palace Museum:** exterior (nothing on Commons). Tours are booked online; ask before photographing inside.
1. **Sheikh Jaber Al-Ahmad Cultural Centre:** exterior of the buildings and fountains, day and blue hour. (Nothing usable on Commons.)
2. **Al Sadu House:** the façade on Gulf Road, the courtyard, a loom or Sadu weaving detail. (Nothing on Commons.)
3. **Marina Crescent:** the seafront walk and the glass bridge at dusk. (Only a 2006 photo exists.)
4. **Sheikh Abdullah Al Salem Cultural Centre:** an exterior that's clearly ASCC (the page has no ASCC photo since inline-7 was removed).
5. **The Scientific Center:** the building on the Salmiya seafront (we only have a 2011 aquarium shot).
6. **Kuwait Towers by day:** a 16:9 hero option from Gulf Road (current hero is a 2016 night shot).
7. **Al Shaheed Park by day:** lawns and lakes, wide (keep the Central Bank towers out of frame).
8. Optional: **Souq Al Mubarakiya** by day (the page uses a 2022 Commons photo). Failaka and Al Khiran stay out (owner, 30 Oct).
9. The restaurants in "Eat nearby" already have the bloggers' listing photos; none needed unless we add venue photos here.

## SEO fields
| | EN | AR |
|---|---|---|
| URL | `/guide/things-to-do-in-kuwait/` | `/ar/guide/things-to-do-in-kuwait/` (WPML twin, same slug) |
| H1 (post title) | Things to Do in Kuwait: Best Places to Visit | اماكن سياحية في الكويت: وين تروح ووين تاكل |
| SEO title | Things to Do in Kuwait: Best Places to Visit \| Q8tly | اماكن سياحية في الكويت: وين تروح ووين تاكل \| Q8tly |
| Meta description (= excerpt = schema) | Things to do in Kuwait: 10 places to visit, from Kuwait Towers to museums and the waterfront, with official hours and Q8tly restaurants nearby. | اماكن سياحية في الكويت: 10 اماكن من أبراج الكويت لين المتاحف والواجهة البحرية، مع المواعيد الرسمية ومطاعم Q8tly القريبة من كل مكان. |
| Focus keyword | things to do in kuwait | اماكن سياحية في الكويت |
| topic | culture-heritage | culture-heritage |

### Where each target keyword appears
**EN**
- "things to do in kuwait": SEO title (first words), H1 (first words), slug, meta description (first words), first sentence,
  H2 "Things to do in Kuwait by area", focus keyword. FAQ 2 has "free things to do in Kuwait".
- "places to visit in kuwait": first sentence ("10 places to visit in Kuwait"), deck, H2s "Places to visit in Kuwait with family",
  "…at night", "…for free", FAQ 1 (H3 + answer). **The H1 has "Best Places to Visit" but not the exact phrase "places to visit
  in Kuwait"** (the H1 is the title you gave). Say if you want "Things to Do in Kuwait: Best Places to Visit in Kuwait" (repetitive) instead.
- "places to visit in kuwait with family": H2 + FAQ 3 (H3).
- "activities in kuwait": H3 "Indoor activities in Kuwait" + the line under it.
- "places to visit in kuwait for free": H2 (the free box) + FAQ 2 ("free things to do in Kuwait").
- "fun places to go in kuwait": first line under the family H2.
- "indoor activities in kuwait": H3 + the line under it.
- "places to visit in kuwait at night": H2 + FAQ 4 (H3).
**AR**
- «اماكن سياحية في الكويت»: SEO title, H1, meta description (all first words), first sentence, H2 «…حسب المنطقة», FAQ 1 (H3; answer has «الاماكن السياحية في الكويت»), focus keyword.
- «اماكن ترفيهية في الكويت»: first line under the family H2.
- «اماكن عائلية في الكويت»: H2 + FAQ 3 (H3 «شنو أفضل اماكن عائلية في الكويت؟»).
- «اماكن ترفيهية للاطفال»: H3 (the indoor list).

## Links
- **Internal:** 37 listings ("Eat nearby" + 5 indoor activities + Marina Mall + The Avenues + the souq), 6 area hubs (EN `/en/areas/…`:
  Kuwait City, Sharq, Qibla, Salmiya, Jabriya, Rai; AR `/ar/areas/…`), the burger guide (`/guide/best-burger-in-kuwait/`, AR
  `/ar/guide/best-burger-in-kuwait/`). All checked 200 on 30 Oct; every listing link is the listing's real URL in the page's language.
- **External:** each attraction's official site or account (TEC pages are Arabic-only and say so on the EN page), plus the
  Commons file pages and licence deeds in the credits. All 200 on 30 Oct.
- **Burger guide → this page: ADDED 30 Oct at publish (EN 7869 + AR 7871, verified live).** Text used: the burger guide is live and this page is a draft, so a link
  now would 404 for readers. At publish, add to the end of "Burger spots by area" in both languages:
  - EN: `Visiting Kuwait? See our guide to [things to do in Kuwait](/guide/things-to-do-in-kuwait/).`
  - AR: `زاير الكويت؟ شوف دليلنا [اماكن سياحية في الكويت](/ar/guide/things-to-do-in-kuwait/).`
  and push with `reinject_en.py … 7869 --status keep` / `populate_ar_twin.py … --en-id 7869` (AR stays published).
- **Seasonal paragraphs:** no links yet (the camping and New Year's Eve guides don't exist). Link them when they do.
- No "book on Q8tly" anywhere; the listings' own buttons handle bookings.

## Listing flags (route via the Advisor → Pipeline; not Blog's to change)
- **Fish Market, Kuwait Towers (6743):** stored Instagram `@fishmarket_` is the Salmiya/Abu Halifa business; the Towers branch is
  `@fishmarket_kwt_towers` (posting 29 Oct). It isn't on restaurants.kuwaittowers.com, so "next to" the towers (as the listing
  says), not "inside".
- **Melt (7708):** no Instagram stored; it's `@try.melt` (bio: Marina Crescent).
- **Untold (7620):** city "Kuwait City"; its bio says Shaab.
- **EDO (6996):** listed in Salmiya; its bio says Al Khaled Complex, Maidan Hawally.
- **Mais Alghanim (1861):** located_in "Souk Sharq"; its bio says Arabian Gulf St, opposite Kuwait Towers.
- **Fish Market Salmiya (7018):** "Old Souk" in the About; no current source confirms it (directories: Salem Al-Mubarak St).
- **Dalaq Assail (3291):** no own posts since 12 Feb 2026 and nothing from 2026 placing it in the souq; a Talabat "tmp" branch
  sits at souq coordinates. Phone 22432224 would settle it. (Not to be confused with Dalak Suhail, a separate restaurant opposite the souq.)
- **Al Shemam (4710):** the brand writes its Arabic name «الشمم» (not «الشمام»); our AR title is Latin, so only relevant if it's translated.
- **Mais Alghanim (1861):** located_in "Souk Sharq" is stale as well as wrong: the Souq Sharq mall closed on 31 Jan 2026.
- **Hoffee (7344), EQ (1945):** possibly closed (silent since Jun / Feb 2026; EQ shows "Closed" in a directory). Worth a Pipeline check.
- **Toby's Estate Jabriya (1849):** branch and drive-thru not confirmed by any current source.
- **Fun City (3992):** stored Instagram is the regional account; the Kuwait branch is on funcityarabia.com/en-kw.

## Kit change (this session)
`publish_guide.py` `md_inline()` now sets links aside before emphasis, so underscores/asterisks inside a URL can't become `<em>`
(Commons file URLs are full of underscores). Shared by all three tools. Regression: 46 of 48 existing drafts/articles render
byte-identical; the 2 that change are the old June Anosha drafts, where the fix repairs a broken link
(`instagram.com/anosha</em>salon/`). The live Anosha pages don't carry that link (checked 30 Oct).

## Souq Al Mubarakiya: restored 30 Oct (owner's decision 4)
The owner personally confirmed it's open (there's no official account). Restored under "Landmarks and culture" after Kuwait
Towers with photo inline-9 (7897), counts 12 → 13 (intro, deck, meta, excerpt), Qibla line in "by area", FAQ 1. The two
unsourced sentences in the parked draft ("no ticket", "busiest in the evening") were cut; best time = "late afternoon or
evening, when it's cooler". Not in the free box (decision 1: nothing else). No official site to link: the name links our listing.

## Order of operations (drafts)
1. Check and take `/tmp/q8tly-publish.lock`. Prod dry-run (done 30 Oct: slug free, place id resolves).
2. `publish_guide.py guides/things-to-do-in-kuwait --execute` with `GUIDEKIT_SSH_HOST` / `GUIDEKIT_SITE_URL` (prod): backs up
   prod, uploads hero + inline-1…8, creates EN as a **draft** (frontmatter `status: draft`).
3. AR twin without the "+": backup → `wp_insert_post` draft, slug `things-to-do-in-kuwait` →
   `$sitepress->set_element_language_details(A,'post_guide_article',<trid of E>,'ar','en')` →
   `populate_ar_twin.py drafts/things-to-do-in-kuwait_AR_2026-10-30.md --en-id E --media hero=H,inline-1=…,inline-8=… --draft`.
4. Prove the WPML pair; focus keywords; touch (status stays draft); flush; check stored links (WPML rewrites AR links on save);
   release the lock.
5. Owner previews. **Publish only on the owner's word.** At publish: lock, backup, EN then AR, flush, anonymous proofs, then
   add the burger guide → this page link (above).

## ✅ POSTED AS DRAFTS: 30 Oct 2026, ~09:59–10:09 Kuwait (brief: "Save as DRAFT in both languages"; under /tmp/q8tly-publish.lock 06:58:52Z → 07:09:21Z)
- Lock was free. Prod dry-run clean (slug free, place id 3125 resolves). All 68 unique links per language checked 200 beforehand.
- EN **7891** (draft) · AR **7893** (draft) · trid **7241** · hero **7882** (shared) · inline-1 **7883**, inline-2 **7884**, inline-3 **7885**,
  inline-4 **7886**, inline-5 **7887**, inline-6 **7888**, inline-7 **7889**, inline-8 **7890** (shared).
- Media stored at full original size; served files byte-identical to the Commons originals (sha256 checked on hero, inline-3, inline-8).
- WPML pair proven (7891 → ar 7893, src en). Twin made without the "+"; zero raw `icl_*` writes.
- Stored content, both: 79 links / 68 unique, all 200 (35 listings, 6 area hubs, the burger guide, 13 official, 13 Commons/CC);
  AR all `/ar/places/` and `/ar/areas/` (WPML made the burger link absolute `https://q8tly.com/ar/guide/best-burger-in-kuwait/`);
  8 inline photos each; no raw `[[`; no `<em>` inside any href. SEO title, description and excerpt match on both;
  `rank_math_robots` empty; focus keywords `things to do in kuwait` / «اماكن سياحية في الكويت»; topic culture-heritage (1717).
- Both touched with status kept as draft; WP Rocket flushed. Anonymous: both public URLs and both `?p=` URLs 404.
- Backups: `prod-20261030-065911-guide-things-to-do-in-kuwait`, `prod-20261030-070407-pre-ar-shell-things-to-do-in-kuwait`,
  `prod-20261030-070633-ar-twin-things-to-do-in-kuwait` (BACKUP_LOG).
- Owner preview (logged in): EN https://q8tly.com/?post_type=guide_article&p=7891&preview=true · AR https://q8tly.com/ar/?post_type=guide_article&p=7893&preview=true
- **Publish only on the owner's word.** At publish: lock, backup, EN (`reinject_en.py … 7891 --status publish`) then AR
  (`populate_ar_twin.py … --en-id 7891`, publish, unfenced), flush, anonymous proofs (200, title, description, canonical,
  hreflang, og:image, index, sitemap), served links on both pages, then the burger guide → this page link (see Links).

## ✅ PUBLISHED: 30 Oct 2026, ~10:22–10:35 Kuwait (owner's word: "Approved. Publish both versions."; lock 07:22:44Z → 07:35:51Z)
- Backups: `prod-20261030-072248-pre-publish-things-to-do-in-kuwait` + the tools' own (`…-072519-en-guide-…`, `…-072705-ar-twin-…`,
  `…-072932-en-guide-best-burger-in-kuwait`, `…-073130-ar-twin-best-burger-in-kuwait`) (BACKUP_LOG).
- Souq photo uploaded: inline-9 = attachment **7897** (parent 7891). inline-7 (7889) no longer in either page.
- EN 7891 published with `reinject_en.py --status publish`; AR 7893 with `populate_ar_twin.py` (publish, unfenced). WPML pair unchanged
  (trid 7241). Burger backlink pushed: EN 7869 (`reinject_en.py`, status kept; diff vs live = the one paragraph) and AR 7871
  (`populate_ar_twin.py`, publish).
- **Live proofs (anonymous, 30 Oct):**
  - `https://q8tly.com/guide/things-to-do-in-kuwait/` **200** · `https://q8tly.com/ar/guide/things-to-do-in-kuwait/` **200**.
  - Title = SEO title, meta description = og:description = Article schema description (13 places) on both. Canonical = self on both.
    Robots `index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large`; no X-Robots-Tag.
  - hreflang on both: ar → AR, en → EN, x-default → EN. og:image = hero 7882 on both. `<html lang>` en-US / ar.
  - EN/AR switch: the header toggle (`button.q8tly-header__lang-toggle`) clicked in headless Chromium: EN → AR URL (H1 «اماكن سياحية
    في الكويت: وين تروح ووين تاكل», lang ar) and AR → EN URL (H1 "Things to Do in Kuwait: Best Places to Visit", lang en-US).
  - Sitemap: both URLs in `/guide_article-sitemap.xml`; the AR URL also in `/ar/guide_article-sitemap.xml`.
  - Served body links: 70 unique per page, all 200; AR: every listing and area link on `/ar/` (43 listing links), none wrong-language.
  - 8 body photos (7883–7888, 7890, 7897) + hero; 9 Commons credit links; no raw `[[`/`[q8tly_`; no mojibake.
  - Burger guide: EN 200 with the link to `/guide/things-to-do-in-kuwait/`; AR 200 with the link to `/ar/guide/things-to-do-in-kuwait/`.
