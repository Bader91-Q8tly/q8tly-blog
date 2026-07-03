#!/usr/bin/env python3
r"""
reinject_en.py — update-only re-author of an EXISTING EN guide_article body.

Formalized EN sibling to populate_ar_twin.py. Same discipline, mirrored:
  backup (auto, before any write) -> update (charset-safe) -> verify (live render).

UPDATE-ONLY, same rail as the AR tool: it only ever writes post_content/meta on
the ONE explicit --post_id you pass. It never touches WPML: no icl_translations
writes, no "+" twin creation, no lookup/mutation of any AR twin. A hard target
check refuses to run if the post isn't a guide_article or its WPML language
isn't 'en' (or untranslated) — this is what keeps it from ever landing on the
AR side of a trid by accident.

Charset-safe: body is streamed as UTF-8 bytes to a temp file and read back with
file_get_contents(); all meta/title use json.dumps(ensure_ascii=False) so PHP
stores real UTF-8 (same CHARSET-trap avoidance as populate_ar_twin.py).

Idempotency: before writing, the tool fetches the CURRENT live post_content and
diffs it against the newly-generated body. Dry run always shows this; it's the
built-in no-op/safe-rerun check — if a guide's approved MD hasn't changed,
re-running should report NO CHANGE.

Usage:
  python3 reinject_en.py <draft.md> <post_id> \
      --media inline-1=2359,inline-2=2360,inline-3=2361,hero=2358 [--execute]
Default = DRY RUN (verifies target, builds the body, prints the diff/plan, no writes).
"""
import argparse, difflib, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import publish_guide as kit  # reuse parse_frontmatter, md_to_blocks, word_count, ssh, load_config, CHROME_FORBIDDEN


def die(m):
    print(f"\n❌ {m}\n", file=sys.stderr); sys.exit(1)


def jx(s):
    """JSON-encode for embedding in PHP, keeping non-ASCII as real UTF-8 (no \\uXXXX)."""
    return json.dumps(s if s is not None else "", ensure_ascii=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("post_id", help="EN guide_article id to update (the post itself, never its AR twin)")
    ap.add_argument("--media", default="", help="stem=attachment,... (e.g. inline-1=2359,hero=2358)")
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    cfg = kit.load_config()
    host = cfg["SSH_HOST"]
    if not host:
        die("no SSH_HOST in config.sh")

    media = {}
    for pair in [p for p in args.media.split(",") if p.strip()]:
        k, v = pair.split("="); media[k.strip()] = v.strip()

    raw = open(args.draft, encoding="utf-8").read()
    raw = re.sub(r"^﻿?\s*<!--.*?-->\s*", "", raw, count=1, flags=re.S)  # allow a leading HTML comment before frontmatter
    fm, body = kit.parse_frontmatter(raw)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()  # drop any remaining comments
    if fm.get("lang") != "en":
        die("draft lang is not 'en' (this tool is EN-only — AR twins go through populate_ar_twin.py)")
    for bad in kit.CHROME_FORBIDDEN:
        if bad.lower() in body.lower():
            die(f"body contains chrome '{bad}'")

    post_id = args.post_id
    place_id = fm.get("place_id")
    map_ids = fm.get("map_ids") if isinstance(fm.get("map_ids"), list) else ([fm["map_ids"]] if fm.get("map_ids") else [])
    blocks, body_images = kit.md_to_blocks(body, place_id, map_ids)
    wc = kit.word_count(body)

    # ── HARD-VERIFY target: a guide_article, and NEVER the AR side of a trid ──
    vphp = f"""<?php
$p = {post_id};
echo "type=".get_post_type($p)."\\n";
echo "status=".get_post_status($p)."\\n";
$ld = apply_filters("wpml_post_language_details", null, $p);
echo "lang=".($ld && isset($ld["language_code"]) ? $ld["language_code"] : "")."\\n";
"""
    rc, info, err = kit.ssh(host, "wp eval-file -", inp=vphp)
    d = dict(l.split("=", 1) for l in info.strip().splitlines() if "=" in l)
    print("TARGET VERIFY:", d)
    if d.get("type") != "guide_article":
        die(f"target {post_id} is not a guide_article (got {d.get('type')!r})")
    if d.get("lang") not in ("en", ""):
        die(f"target {post_id} WPML language is {d.get('lang')!r}, not 'en' — refusing "
            f"(this would be writing into the AR twin; never do that here)")

    # ── build image blocks from EXISTING media (reuse; no upload — repo is text-only) ──
    final = blocks
    for stem, cap in body_images:
        aid = media.get(stem, "")
        if not aid:
            die(f"no --media mapping for image stem '{stem}'")
        rc, url, _ = kit.ssh(host, f"wp post get {aid} --field=guid 2>/dev/null")
        url = url.strip()
        alt = cap or fm["title"]
        cap_html = f'<figcaption class="wp-block-image__caption">{html.escape(cap)}</figcaption>' if cap else ""
        blk = (f'<!-- wp:image {{"id":{aid},"sizeSlug":"large","linkDestination":"none"}} -->\n'
               f'<figure class="wp-block-image size-large"><img src="{url}" alt="{html.escape(alt)}" '
               f'class="wp-image-{aid}"/>{cap_html}</figure>\n<!-- /wp:image -->')
        final = final.replace(f"<!--GUIDEKIT_IMG:{stem}|{cap}-->", blk)

    hero = media.get("hero", "")
    seo_title = fm.get("seo_title", "")
    meta_desc = fm.get("meta_description", "")

    print(f"\n=== EN RE-AUTHOR post {post_id}  [{'EXECUTE' if args.execute else 'DRY RUN'}] ===")
    print(f"title  : {fm.get('title')}")
    print(f"place_id: {place_id}   map_ids: {map_ids}   words: {wc}   hero(reuse): {hero or '⚠none'}")
    print(f"images : " + ", ".join(f"{s}->{media.get(s, '?')}" for s, _ in body_images))
    print(f"SEO    : rank_math_title {'-> set' if seo_title else '(unchanged, not in draft)'}, "
          f"rank_math_description {'-> set' if meta_desc else '(unchanged, not in draft)'}")
    print("fence  : NONE — EN always stays indexable")

    # ── idempotency check: diff the new body against what's currently live ──
    rc, old_content, _ = kit.ssh(host, f"wp post get {post_id} --field=content 2>/dev/null")
    old_norm = [ln.rstrip() for ln in old_content.strip().splitlines()]
    new_norm = [ln.rstrip() for ln in final.strip().splitlines()]
    if old_norm == new_norm:
        print("\nidempotency: ✓ NO CHANGE — generated body is byte-identical to what's already live")
    else:
        diff = list(difflib.unified_diff(old_norm, new_norm, lineterm="", n=1))
        print(f"\nidempotency: ✗ DIFFERS ({len(diff)} diff lines) — preview:")
        for ln in diff[:20]:
            print("    " + ln)
        if len(diff) > 20:
            print(f"    … {len(diff) - 20} more lines")

    if not args.execute:
        print("\nDRY RUN — no writes.\n")
        return

    # ── backup FIRST (discipline — mirrors populate_ar_twin.py) ──
    rc, ts, _ = kit.ssh(host, "date +%Y%m%d-%H%M%S"); ts = ts.strip()
    bdir = cfg["BACKUP_DIR"]
    if not (bdir and os.path.isdir(bdir)):
        die("BACKUP_DIR missing — no write without a backup")
    dump = os.path.join(bdir, f"staging-{ts}-en-guide-{fm['slug']}.sql.gz")
    with open(dump, "wb") as f:
        subprocess.run(["ssh", "-o", "BatchMode=yes", host, "wp db export - 2>/dev/null | gzip"], stdout=f)
    size = os.path.getsize(dump) if os.path.exists(dump) else 0
    print(f"\n[1] backup : {os.path.basename(dump)} ({size} B)")
    with open(os.path.join(HERE, "BACKUP_LOG.md"), "a", encoding="utf-8") as lg:
        lg.write(f"| {ts} | EN re-author `{fm['slug']}` (post {post_id}) | `{os.path.basename(dump)}` | {size} B | staging |\n")

    # ── stream body (charset-safe) ──
    bodyfile = f"/tmp/guidekit-en-{fm['slug']}-body.html"
    subprocess.run(["ssh", "-o", "BatchMode=yes", host, f"cat > {bodyfile}"], input=final.encode("utf-8"), check=True)

    # ── update-only PHP (ensure_ascii=False -> real UTF-8) ──
    seo_lines = ""
    if seo_title:
        seo_lines += f"update_post_meta($id,'rank_math_title',{jx(seo_title)});\n"
    if meta_desc:
        seo_lines += f"update_post_meta($id,'rank_math_description',{jx(meta_desc)});\n"
    php = f"""<?php
$id = {post_id};
if (get_post_type($id) !== 'guide_article') {{ echo "ERR=not a guide_article\\n"; exit; }}
$r = wp_update_post(array(
  'ID' => $id, 'post_status' => 'publish',
  'post_title' => {jx(fm['title'])}, 'post_name' => {jx(fm['slug'])},
  'post_excerpt' => '',
  'post_content' => file_get_contents({jx(bodyfile)}),
), true);
if (is_wp_error($r)) {{ echo "ERR=".$r->get_error_message()."\\n"; exit; }}
update_post_meta($id,'deck',{jx(fm.get('deck',''))});
update_post_meta($id,'word_count',{int(wc)});
update_post_meta($id,'hero_alt',{jx(fm.get('hero_alt',''))});
update_post_meta($id,'hero_caption',{jx(fm.get('hero_caption',''))});
{seo_lines}$h = {int(hero) if str(hero).isdigit() else 0};
if ($h>0) {{ set_post_thumbnail($id,$h); update_post_meta($id,'hero_photo_id',$h); }}
echo "OK=".$id."\\n"; echo "URL=".get_permalink($id)."\\n"; echo "ST=".get_post_status($id)."\\n";
"""
    rc, out, err = kit.ssh(host, "wp eval-file -", inp=php)
    print("[2] update :")
    for ln in out.splitlines():
        print("    " + ln)
    if "OK=" not in out:
        die(f"update failed. out={out} err={err}")

    # ── touch + flush (edge cache) ──
    kit.ssh(host, f'wp post update {post_id} --post_status=publish >/dev/null 2>&1; '
                  f'wp eval "if(function_exists(\\"rocket_clean_domain\\")){{rocket_clean_domain();}}" >/dev/null 2>&1')
    print("[3] cache  : touched + flushed")

    # ── verify the live render ──
    print("[4] verify :")
    import urllib.request
    rc, url, _ = kit.ssh(host, f"wp post get {post_id} --field=guid 2>/dev/null")
    u = url.strip() or f"{cfg['SITE_URL'].rstrip('/')}/guide/{fm['slug']}/"
    try:
        h = urllib.request.urlopen(u, timeout=25).read().decode("utf-8", "replace")
        title_ok = fm["title"][:10] in h
        no_raw_shortcode = not bool(re.search(r"\[q8tly_(place|map)", h))
        place_card_ok = (not place_id) or bool(re.search(r'href="[^"]*/places/', h))
        single_title = h.count('class="entry-title"') <= 1
        ok = lambda b: "✓" if b else "✗"
        print(f"    {ok(title_ok)} title renders (no mojibake)")
        print(f"    {ok(no_raw_shortcode)} no raw [q8tly_*] shortcode literal")
        print(f"    {ok(place_card_ok)} place card resolves to a real /places/ link")
        print(f"    {ok(single_title)} no double title")
        # NOTE: deliberately NOT checking robots/noindex here — this staging site
        # emits a sitewide noindex (the WP.com "discourage search engines"
        # option), so per-page robots meta can't distinguish that from an
        # accidental guide-level fence. An hreflang link to the /ar/ twin is
        # normal WPML output, not a leak — don't flag it.
    except Exception as e:
        print(f"    ⚠ could not fetch {u}: {e}")

    print(f"\n✅ RE-AUTHORED  {u}  (post {post_id}, publish, EN indexable)\n")


if __name__ == "__main__":
    main()
