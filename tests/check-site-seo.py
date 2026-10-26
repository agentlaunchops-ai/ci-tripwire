"""Comprehensive offline SEO, HTML, schema, link, disclaimer, and image gate across all dsotn.com routes."""
from collections import Counter, defaultdict
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://dsotn.com"
AFFILIATE = "https://jvz9.com/c/3636661/454123/"

DISCLAIMERS = {
    "ci": "This article is informational and is not a substitute for a security review of your own workflows, repositories, or cloud accounts.",
    "stripe": "This article is informational and is not a substitute for a security, billing, tax, or legal review of your own product.",
    "local": "This article is informational and is not a substitute for a legal, tax, or business review of your own publication.",
}

FUNNEL_SLUGS = {"local-newsletter-launch-plan", "local-media-empire-publishing-checklist"}
BANNED_CHARS_RE = re.compile(r"[\u2013\u2014\u2018\u2019\u201c\u201d]")
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")


class PageParser(HTMLParser):
    def __init__(self, source: str):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.meta = {}
        self.canonical = None
        self.h1s = []
        self.title = ""
        self.json_ld = []
        self._in_title = False
        self._in_h1 = False
        self._h1_buf = []
        self._script_type = None
        self._script_buf = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if "id" in attr:
            self.ids.append(attr["id"])
        if tag == "a":
            self.links.append(attr)
        elif tag == "img":
            self.images.append(attr)
        elif tag == "meta":
            key = attr.get("name") or attr.get("property")
            if key:
                self.meta[key] = attr.get("content", "")
        elif tag == "link" and attr.get("rel") == "canonical":
            self.canonical = attr.get("href")
        elif tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
            self._h1_buf = []
        elif tag == "script":
            self._script_type = attr.get("type")
            self._script_buf = []

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1:
            self._h1_buf.append(data)
        if self._script_type == "application/ld+json":
            self._script_buf.append(data)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
            self.h1s.append("".join(self._h1_buf).strip())
        elif tag == "script":
            if self._script_type == "application/ld+json":
                self.json_ld.append(json.loads("".join(self._script_buf)))
            self._script_type = None


def file_for_route(route: str) -> Path:
    clean = unquote(route).lstrip("/")
    if not clean:
        return ROOT / "index.html"
    p = ROOT / clean
    return p / "index.html" if route.endswith("/") else p


def jpeg_dimensions(data: bytes) -> tuple[int, int]:
    assert data[:2] == b"\xff\xd8", "Not a JPEG"
    i = 2
    while i < len(data):
        while i < len(data) and data[i] != 0xFF:
            i += 1
        while i < len(data) and data[i] == 0xFF:
            i += 1
        marker = data[i]
        i += 1
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            continue
        seg_len = int.from_bytes(data[i : i + 2], "big")
        if marker in (0xC0, 0xC1, 0xC2):
            h = int.from_bytes(data[i + 3 : i + 5], "big")
            w = int.from_bytes(data[i + 5 : i + 7], "big")
            return w, h
        i += seg_len
    raise AssertionError("No SOF marker found in JPEG")


def png_dimensions(data: bytes) -> tuple[int, int]:
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "Not a PNG"
    w = int.from_bytes(data[16:20], "big")
    h = int.from_bytes(data[20:24], "big")
    return w, h


def discover_routes() -> list[str]:
    routes = [
        "/",
        "/about/",
        "/articles/",
        "/categories/github-actions/",
        "/categories/stripe-billing/",
        "/tools/local-publication-planner/",
    ]
    for p in sorted((ROOT / "articles").glob("*/index.html")):
        routes.append(f"/articles/{p.parent.name}/")
    return routes


def main():
    # 1. Check governance & discovery markdown files for banned chars/emoji
    for doc_name in [
        "AGENTS.md",
        "BRAND_VOICE.md",
        "ARTICLE_WRITING_RULES.md",
        "llms.txt",
        "CHANGELOG.md",
        "CHANGELOG_ARTICLES_2026_10_26_brand_voice_seo_overhaul.md",
    ]:
        doc_path = ROOT / doc_name
        assert doc_path.exists(), f"Missing {doc_name}"
        txt = doc_path.read_text()
        assert not BANNED_CHARS_RE.search(txt), f"Banned typography in {doc_name}"
        assert not EMOJI_RE.search(txt), f"Emoji found in {doc_name}"

    routes = discover_routes()
    assert len(routes) == 29, f"Expected 29 routes, found {len(routes)}"

    parsed_pages: dict[str, tuple[Path, str, PageParser]] = {}
    for route in routes:
        path = file_for_route(route)
        assert path.exists(), f"Missing route file {path}"
        source = path.read_text()
        parsed_pages[route] = (path, source, PageParser(source))

    outbound_article_links: dict[str, set[str]] = defaultdict(set)
    inbound_article_links: dict[str, set[str]] = defaultdict(set)

    # 2. Validate every HTML route
    for route, (path, source, page) in parsed_pages.items():
        assert not BANNED_CHARS_RE.search(source), f"Banned quote/dash in {route}"
        assert not EMOJI_RE.search(source), f"Emoji in {route}"

        # Raw backticks outside script/style/pre/code
        stripped = re.sub(r"<(script|style|pre|code)\b[^>]*>.*?</\1>", "", source, flags=re.S)
        raw_bts = re.findall(r"`[^`\n]+`", stripped)
        assert not raw_bts, f"Raw Markdown backticks in {route}: {raw_bts[:5]}"

        # Unique DOM IDs & single H1
        dup_ids = [k for k, v in Counter(page.ids).items() if v > 1]
        assert not dup_ids, f"Duplicate IDs in {route}: {dup_ids}"
        assert len(page.h1s) == 1 and page.h1s[0], f"Expected 1 non-empty H1 in {route}, got {page.h1s}"

        # Title, description, canonical, OG, Twitter
        title = unescape(page.title.strip())
        desc = unescape(page.meta.get("description", "").strip())
        assert 50 <= len(desc) <= 155, f"Description length {len(desc)} out of [50,155] on {route}: {desc}"
        expected_url = SITE + route
        assert page.canonical == expected_url, f"Canonical mismatch on {route}: {page.canonical}"
        assert page.meta.get("og:url") == expected_url, f"og:url mismatch on {route}: {page.meta.get('og:url')}"
        assert page.meta.get("twitter:card") == "summary_large_image", f"Missing summary_large_image on {route}"

        # OG image PNG + SVG pair validation
        og_img_url = page.meta.get("og:image", "")
        assert og_img_url.startswith(SITE + "/og/") and og_img_url.endswith(".png"), f"Bad og:image on {route}: {og_img_url}"
        og_png_path = file_for_route(og_img_url.removeprefix(SITE))
        og_svg_path = og_png_path.with_suffix(".svg")
        assert og_png_path.exists() and og_svg_path.exists(), f"Missing OG PNG/SVG pair for {route}: {og_png_path}"
        assert og_png_path.stat().st_size <= 960 * 1024, f"OG PNG > 960 KB: {og_png_path}"
        assert png_dimensions(og_png_path.read_bytes()) == (1200, 630), f"OG PNG not 1200x630: {og_png_path}"
        ET.parse(og_svg_path)

        # Robots & analytics privacy rules
        is_funnel_route = route == "/tools/local-publication-planner/" or any(
            route == f"/articles/{slug}/" for slug in FUNNEL_SLUGS
        )
        if is_funnel_route:
            assert page.meta.get("robots") == "index,follow", f"Funnel robots mismatch on {route}"
            assert "plausible.io" not in source and "<script async" not in source, f"Analytics forbidden on funnel {route}"
        else:
            assert page.meta.get("robots") == "index,follow,max-image-preview:large", f"Missing max-image-preview:large on {route}"
            if route == "/categories/github-actions/":
                assert "plausible.io" not in source and "<script async" not in source, "Do not add analytics to new routes"

        # JSON-LD validation (no top-level @graph without @type)
        assert page.json_ld, f"Missing JSON-LD on {route}"
        for ld in page.json_ld:
            assert "@type" in ld, f"JSON-LD block missing top-level @type on {route}"
        if route != "/":
            assert any(ld["@type"] == "BreadcrumbList" for ld in page.json_ld), f"Missing BreadcrumbList on {route}"

        # Images validation
        for img in page.images:
            assert img.get("alt", "").strip(), f"Empty alt on {route}: {img}"
            assert img.get("width", "").isdigit() and img.get("height", "").isdigit(), f"Missing width/height on {route}: {img}"
            img_file = file_for_route(img["src"])
            assert img_file.exists(), f"Missing image {img['src']} referenced in {route}"

        # Links validation
        for link in page.links:
            href = link.get("href", "")
            assert href, f"Empty href on {route}: {link}"
            sp = urlsplit(href)
            if sp.scheme:
                assert sp.scheme == "https", f"Non-https link on {route}: {href}"
                assert link.get("target") == "_blank", f"External link missing target=_blank on {route}: {href}"
                rels = set(link.get("rel", "").split())
                req_rels = {"sponsored", "noopener", "noreferrer"} if href == AFFILIATE else {"nofollow", "noopener", "noreferrer"}
                assert req_rels <= rels, f"External link rel mismatch on {route}: {link}"
            else:
                assert not link.get("target") and not link.get("rel"), f"Internal link has target/rel on {route}: {link}"
                target_route = route if not sp.path else sp.path
                if target_route in parsed_pages:
                    target_ids = parsed_pages[target_route][2].ids
                else:
                    tf = file_for_route(target_route)
                    assert tf.exists(), f"Broken internal link {href} on {route}"
                    target_ids = PageParser(tf.read_text()).ids if tf.suffix == ".html" else []
                if sp.fragment:
                    assert sp.fragment in target_ids, f"Broken fragment #{sp.fragment} -> {target_route} from {route}"
                if (
                    route.startswith("/articles/")
                    and route != "/articles/"
                    and target_route.startswith("/articles/")
                    and target_route != "/articles/"
                    and target_route != route
                ):
                    src_slug = route.strip("/").split("/")[1]
                    dst_slug = target_route.strip("/").split("/")[1]
                    outbound_article_links[src_slug].add(dst_slug)
                    inbound_article_links[dst_slug].add(src_slug)

        # Article-specific checks
        if route.startswith("/articles/") and route != "/articles/":
            slug = route.strip("/").split("/")[1]
            if slug in FUNNEL_SLUGS:
                assert 50 <= len(title) <= 60, f"Funnel title len {len(title)}: {title}"
                expected_disc = DISCLAIMERS["local"]
            elif slug.startswith("stripe-"):
                assert 45 <= len(title) <= 60, f"Stripe title len {len(title)}: {title}"
                expected_disc = DISCLAIMERS["stripe"]
            else:
                assert 45 <= len(title) <= 60, f"Article title len {len(title)}: {title}"
                expected_disc = DISCLAIMERS["ci"]

            assert title == page.h1s[0], f"Title != H1 on {route}: {title!r} vs {page.h1s[0]!r}"
            assert source.count(expected_disc) == 1, f"Expected 1 disclaimer on {route}, found {source.count(expected_disc)}"
            for kind, disc_text in DISCLAIMERS.items():
                if disc_text != expected_disc:
                    assert disc_text not in source, f"Wrong topic disclaimer ({kind}) on {route}"

            # Hero image dimensions & weight
            hero_path = ROOT / "public/images/articles" / f"{slug}.jpg"
            assert hero_path.exists(), f"Missing hero JPEG for {slug}"
            hero_bytes = hero_path.read_bytes()
            assert len(hero_bytes) <= 350 * 1024, f"Hero > 350 KiB ({len(hero_bytes)} B) for {slug}"
            assert jpeg_dimensions(hero_bytes) == (1600, 900), f"Hero not 1600x900 for {slug}: {jpeg_dimensions(hero_bytes)}"

            # TechArticle JSON-LD & citations
            tech = next((ld for ld in page.json_ld if ld["@type"] == "TechArticle"), None)
            assert tech is not None, f"Missing TechArticle on {route}"
            assert tech["headline"] == title, f"TechArticle.headline != title on {route}"
            assert tech["author"]["@type"] == "Organization" and tech["author"]["name"] == "CI Tripwire Editorial"
            assert "<section id=\"key-takeaways\"" in source and "<section id=\"article-summary\"" in source
            assert "<section id=\"references\"" in source
            refs_section = source[source.index('<section id="references"') :]
            assert tech.get("citation"), f"Empty citations on {route}"
            for cite in tech["citation"]:
                c_url = cite["url"]
                if any(tok in c_url for tok in ("/search?", "?q=", "google.com/search")):
                    assert "search" in cite.get("name", "").lower(), f"Unlabeled search URL in citation on {route}: {c_url}"
                assert c_url.replace("&", "&amp;") in refs_section, f"Citation URL missing from #references on {route}: {c_url}"
        else:
            assert 35 <= len(title) <= 65, f"Hub/page title len {len(title)} on {route}: {title}"

    # 3. Verify hub card Updated YYYY-MM-DD parity with each article's canonical TechArticle.dateModified
    article_mod_dates = {}
    for route, (_, _, page) in parsed_pages.items():
        if route.startswith("/articles/") and route != "/articles/":
            slug = route.strip("/").split("/")[1]
            tech = next(ld for ld in page.json_ld if ld["@type"] == "TechArticle")
            article_mod_dates[slug] = tech["dateModified"][:10]

    for hub_route in ["/", "/articles/", "/categories/github-actions/", "/categories/stripe-billing/"]:
        hub_src = parsed_pages[hub_route][1]
        for card_block in re.findall(r'<article class="card">.*?</article>', hub_src, flags=re.S):
            m_slug = re.search(r'<h[23]><a href="/articles/([a-z0-9-]+)/">', card_block)
            m_date = re.search(r'Updated (\d{4}-\d{2}-\d{2})', card_block)
            if m_slug and m_date:
                slug, card_date = m_slug.group(1), m_date.group(1)
                assert card_date == article_mod_dates[slug], (
                    f"Hub card date mismatch on {hub_route} for {slug}: {card_date} vs {article_mod_dates[slug]}"
                )

    # 4. Verify bidirectional cluster linking on all 21 non-funnel technical articles
    for route in routes:
        if route.startswith("/articles/") and route != "/articles/":
            slug = route.strip("/").split("/")[1]
            if slug in FUNNEL_SLUGS:
                assert len(outbound_article_links[slug]) >= 1, f"Funnel {slug} has no sibling link"
            else:
                assert len(outbound_article_links[slug]) >= 4, (
                    f"Article {slug} has only {len(outbound_article_links[slug])} outbound article links"
                )
                assert len(inbound_article_links[slug]) >= 1, f"Orphan technical article {slug} has 0 inbound article links"

    # 4. Verify sitemap.xml and llms.txt discovery coverage
    tree = ET.parse(ROOT / "sitemap.xml")
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_locs = [el.text for el in tree.findall("s:url/s:loc", ns)]
    assert len(sitemap_locs) == len(set(sitemap_locs)) == len(routes), (
        f"Sitemap count mismatch: {len(sitemap_locs)} vs {len(routes)} routes"
    )
    for route in routes:
        assert SITE + route in sitemap_locs, f"Route missing from sitemap.xml: {route}"

    llms_txt = (ROOT / "llms.txt").read_text()
    for route in routes:
        if route != "/about/":
            assert SITE + route in llms_txt, f"Route missing from llms.txt: {route}"
    assert SITE + "/about/" in llms_txt

    print(f"PASS check-site-seo.py: all {len(routes)} routes, JSON-LD, citations, links, disclaimers, OG cards, and 1600x900 heroes verified")


if __name__ == "__main__":
    main()
