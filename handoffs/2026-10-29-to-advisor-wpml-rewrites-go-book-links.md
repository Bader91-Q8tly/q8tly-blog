# To Advisor (→ Builder): WPML rewrites `/go/book/` links inside AR guide content · blocks publishing the romantic-restaurants AR

**Found 29 Oct 2026, ~19:00 Kuwait, creating the romantic-restaurants drafts (EN 7850 / AR 7852, prod).**

## What happens
The AR article's 7 booking links were written as `https://q8tly.com/go/book/<slug>?from=web&lang=ar` (rel="nofollow").
After saving the AR twin, all 7 point to the AR **listing** instead, e.g.
`https://q8tly.com/ar/places/مدينة-الكويت/noya/?from=web&lang=ar`. The EN original keeps its `/go/book/` links.
Readers would land on the listing, not the booking page, and the booking-click counter never sees the click.

## Cause (read on prod; nothing changed)
- WPML `AdjustLinks` → `WPML_Pro_Translation::fix_links_to_translated_content()` runs on **every save of a translation** and
  re-points internal links to their translated targets.
- `/go/(book|call)/<slug>` has no rewrite rule: q8tly-core `includes/go-counter.php` answers it at `do_parse_request`
  (v1.14.551). So WPML treats `go/book/noya` as an ordinary path, resolves `noya` to the gd_place, and writes its AR permalink.
- WPML leaves alone any request listed in the `wpml_sl_blacklist_requests` filter (`WPML_Absolute_Links_Blacklist`; regex entries
  are strings that start and end with `/`, matched against the lower-cased, language-stripped path, e.g. `go/book/noya`).

## Proposed fix (Builder's call; untested)
In q8tly-core, next to the `/go/` route:
```php
// WPML "adjust links" must not turn a /go/ hop into the listing it names.
add_filter( 'wpml_sl_blacklist_requests', static function ( $requests ) {
	$requests[] = '/^go\/(book|call)\//';
	return $requests;
} );
```
Proof to run after deploy: save any AR post whose content has a `/go/book/` link and check the stored href is unchanged.

## Why Blog can't work around it
A direct DB patch of 7852 would be undone by the next save (the publish itself is a save). No other link form fits the brief.

## Status / ask
- Both drafts exist (EN 7850 correct; AR 7852 correct except the 7 booking links). **AR publish is blocked on this fix.**
- After the fix: Blog re-runs `populate_ar_twin.py` on 7852 (draft), verifies 7 `/go/book/` links, then publishes on the owner's word.
- Scope: this is the first guide with `/go/` links in its body; no other live content is affected as far as Blog knows.

## Update 29 Oct 19:15: published under the 19:10 ruling; the EN page is affected too
- Both guides are live (EN 7850, AR 7852). Per the ruling, booking links stay as WPML renders them until 1.14.552.
- **New finding:** the EN page shows the same listing URLs. Its stored content keeps the 7 `/go/book/` links, but WPML converts
  them again on front-end requests (WP-CLI `the_content` keeps them; the served HTML doesn't). The same blacklist should cover
  both, since both paths go through `AbsoluteLinks`, but **the 1.14.552 proof must check the served EN HTML too**, not only an AR save.
- **AR after 1.14.552:** a plain re-save of 7852 won't bring the links back (its stored content no longer holds `/go/book/`).
  Blog will re-run `populate_ar_twin.py` (live post, no `--draft`) and verify stored + served HTML. Steps in
  `guide-kit/guides/romantic-restaurants-kuwait/POSTING.md`.
