# Handoff: 30 Oct 2026, Things to Do in Kuwait (tourism pillar, EN + AR, PUBLISHED on q8tly.com)

**Brief:** owner, 30 Oct ("Things to Do in Kuwait", our main tourism page): 12–15 attractions, each confirmed open on its
official site/account; "Eat nearby" from our listings for every attraction; Commons photos only (CC0/PD/CC BY/CC BY-SA,
unmodified, ≥1200 px, credited); drafts in both languages, don't publish until the owner has reviewed.

- **Drafts:** EN **7891** · AR **7893** (trid 7241, made without the "+"), hero 7882 + 8 body photos 7883–7890.
  Preview (logged in): `https://q8tly.com/?post_type=guide_article&p=7891&preview=true` ·
  `https://q8tly.com/ar/?post_type=guide_article&p=7893&preview=true`. Lock 06:58:52Z–07:09:21Z; 3 backups in BACKUP_LOG.
- **12 attractions kept** (official evidence for each in POSTING): Kuwait Towers, Grand Mosque tours, Al Sadu House,
  Al Salam Palace Museum, Tareq Rajab Museum, Arabian Gulf Street, Al Shaheed Park, Scientific Center, ASCC, The Avenues,
  Marina Crescent, JACC.
- **Dropped:** Kuwait National Museum (NCCAL: closed for maintenance 22 Oct), Bait Al Othman (closed for maintenance since
  ~2024), Green Island (redevelopment), Souq Sharq (closed Jan 2026). **Flagged, left out (owner's call):** Souq Al Mubarakiya
  (no official account confirms it; text parked in POSTING), Al Khiran (no official mall channel), Failaka (ferry confirmed
  for Nov; nothing official on what's open on the island).
- **Free box:** no official source says general entry is free for any of the 12 → box shows only the children's free entry the
  sources state (TRM under-6, ASCC under-2). Owner's call if he wants more (needs a confirmation).
- **Eat nearby:** 27 listings checked for closure/recent activity; Hoffee, EQ, Toby's Jabriya taken out (weak). Listing flags
  (Fish Market Towers wrong Instagram, Melt missing @try.melt, Untold/EDO area labels, Mais Alghanim "Souk Sharq") → POSTING.
- **Map:** the theme can't map coordinates without a template change → `map-attractions.csv` + `map-eat-nearby.csv` for My Maps.
- **Kit:** `publish_guide.py` `md_inline()` now protects link URLs from the emphasis rules (Commons URLs have underscores);
  regression 46/48 identical, the 2 diffs are fixes to old Anosha drafts (live Anosha pages unaffected).
- **Not done on purpose:** burger guide → this page link (would 404 while this is a draft; exact text ready in POSTING, add at
  publish); seasonal paragraphs unlinked (camping / New Year's Eve guides don't exist yet).

**Next:** owner reviews the previews → decides souq / Khiran / Failaka, the free box, the inline-7 (ASCC, GPS-identified) photo,
the H1 exact-match question → publish on his word, then add the burger backlink. Blogger shot list in POSTING.


## Update 30 Oct ~10:35: PUBLISHED (EN 7891 + AR 7893) on the owner's word
- Decisions applied: free box = "no entry ticket" (Gulf Road seafront, Marina Crescent promenade, The Avenues) + the two sourced
  child entries; H1 kept; GPS-only ASCC photo removed; **Souq Al Mubarakiya restored** (owner confirmed open; photo 7897; 13 places);
  Al Khiran and Failaka stay out. Dalaq Assail (souq) dropped as weak; souq eat-nearby = Al Shemam, Bab Al Yemen, Assk Kahve.
- Live proofs passed (200, title/description/schema, canonical, index, hreflang, og:image, sitemaps, toggle, 70 served links per page).
- Burger guide (7869/7871) now links here in both languages.
- Listing flags sent to the owner as a separate list for the listings team (also in POSTING).
- Committed and pushed on the owner's instruction after a credentials scan (none found).
