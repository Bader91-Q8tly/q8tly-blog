# Guide ingestion — charset / mojibake (the latin1-connection trap)

**Read this before publishing.** Q8tly's WP.com Atomic platform forces the DB
**connection** charset to **latin1** (`/scripts/env.php` runs before `wp-config`,
so a `wp-config` `DB_CHARSET` can't override it). The content columns are
**utf8mb4**. If you write multibyte text (em-dash `—`, curly quotes `'' ""`,
ellipsis `…`, accents `é`, **all Arabic**) while the connection is latin1, MySQL
re-encodes every byte and you get **double-encoded mojibake** — e.g. a clean
em-dash `E2 80 94` is stored as `C3A2 E282AC E2809D` and renders as `â€"`.

This bit guides **Keif (2132)** and **Vibes (2131)** — published 2026-06-19,
~9h *before* the charset bridge existed (repaired under **BIR-079**). **Anosha
(2189)**, published after the bridge via this same kit, came out clean.

## What makes a write safe
The bridge is the mu-plugin **`q8charset.php`** (sets `$wpdb` charset/collate +
`SET NAMES utf8mb4` on the live connection). Any write that goes through WordPress
*after* the bridge loads is clean. This kit already does that:

- **Body** — written to a UTF-8 temp file, read with `file_get_contents`, inserted
  via `wp_insert_post`. **Correct, keep as-is.**
- All work runs through `wp eval-file` / `wp` (WP context → `q8charset` active).

So the kit is correct **on staging today**. Two standing rules:

1. **Prod gate.** `q8charset.php` rides the Method-A push, but its presence on
   prod is gated at **cutover runbook Step 13** + a `wp cache flush`. **Do not
   publish any guide (or any AR content) on prod until Step 13 is confirmed** — a
   latin1 write there re-corrupts. This matters *doubly for Arabic*: every AR
   character is multibyte, so a latin1 write mojibakes the entire article.

2. **Latent meta fragility (harden when convenient).** `build_create_php()` embeds
   meta via `json.dumps(...)` (default `ensure_ascii=True`) **inside a PHP
   double-quoted string**. PHP only decodes `\u{XXXX}` *with* braces — a bare
   `—` is stored literally. Decks today are clean, but a non-ASCII deck/
   `hero_alt`/`hero_caption`/`meta_description` could store literal `—`.
   **Fix:** write the meta map to a UTF-8 JSON file (like the body) and
   `json_decode(file_get_contents($f), true)` in the PHP — never interpolate
   non-ASCII into PHP source.

## If you ever need to repair existing mojibake
Reverse the double-encoding through WordPress (so `q8charset` applies), never via
raw `wp db query` over the latin1 connection. Guard it so it only writes when the
reversal is lossless:

```php
$wpdb->query("SET NAMES utf8mb4");            // belt-and-suspenders
$fixed = @iconv('UTF-8','CP1252',$value);     // â€" -> E2 80 94 (the real em-dash)
$back  = @iconv('CP1252','UTF-8',$fixed);
if ($fixed !== false && $back === $value) {   // only if it round-trips exactly
    // $wpdb->update(...) with $fixed
}
```

HEX-verify after (em-dash must be `E28094`, é `C3A9`) and check the **live**
front-end — never trust a CLI read alone (latin1-connection display artifacts can
make clean utf8mb4 *look* broken in `wp db query`; always confirm via `HEX()`).
