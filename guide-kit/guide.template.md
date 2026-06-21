---
# ── Q8tly guide drop — frontmatter contract ──
# Copy this file to guides/<slug>/article.md and fill it in.
# Everything the guide_article needs lives here. The BODY (below the second ---)
# is PLAIN editorial prose. Do NOT hand-build kicker / byline / hero / share /
# related / CTA — the guide template renders all of that. Hand-built chrome
# double-renders.

# ── REQUIRED ──
title: "Place Name, Area: The Hook"          # H1 + <title> base
slug: place-name-area                          # → /guide/<slug>/  (kebab-case, unique)
lang: en                                        # en | ar   (ar stays parked unless you set status: publish)
deck: "One-sentence subtitle the template shows under the title."
topic: neighborhoods                            # ONE of: food-drink | neighborhoods | culture-heritage | seasonal
article_type: guide                             # longread | guide | quick_take
place_id: 0                                      # the gd_place listing ID this guide is about (for [[place]])

# ── OPTIONAL ──
map_ids: [0]                                     # gd_place IDs for [[map]]; omit to skip the map
word_count: auto                                 # 'auto' counts the body, or put an integer
seo_title: ""                                    # Rank Math <title>; omit → uses title
meta_description: ""                             # Rank Math description; ≤ 155 chars
hero_alt: "Describe the hero image for accessibility + SEO."
hero_caption: "Caption shown under the hero."
replaces_page_slug: ""                           # if a stand-in Page exists at /<slug>/, put that slug → trash + 301
status: publish                                  # publish | draft
---

Open with the lede — no title, no byline (the template adds those). Just start
the story.

## A section heading

Normal Markdown prose. Paragraphs, **bold**, _italics_, [links](/places/...),
and lists work:

- A point
- Another point

> A pulled quote reads well between sections.

### A sub-section

Tables work too:

| Service | From |
|---|---|
| Example | 5 KD |

## Markers the publisher expands (place these where you want them)

[[place]]                         <!-- → [q8tly_place id=<place_id>] : the listing card -->

[[map]]                           <!-- → [q8tly_map ids=<map_ids>] : the map pin list (max 1) -->

[[image:inline-1|Caption text]]   <!-- → an inline photo from images/inline-1.* with this caption -->

## Frequently asked questions

### A question?

A plain answer.
