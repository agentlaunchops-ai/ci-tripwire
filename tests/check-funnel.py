"""Offline content, linking, imagery, and discovery checks for this static funnel."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
SLUGS = ['local-newsletter-launch-plan', 'local-media-empire-publishing-checklist']
ROUTES = [f'/articles/{slug}/' for slug in SLUGS] + ['/tools/local-publication-planner/']
AFFILIATE = 'https://jvz9.com/c/3636661/454123/'
DISCLAIMER = 'This article is informational and is not a substitute for a legal, tax, or business review of your own publication.'

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.meta = {}
        self.json_ld = []
        self.script_type = None
        self.script_data = ''
        self.feed(source)

    def handle_starttag(self, tag, items):
        attr = dict(items)
        if 'id' in attr:
            self.ids.append(attr['id'])
        if tag == 'a':
            self.links.append(attr)
        if tag == 'img':
            self.images.append(attr)
        if tag == 'meta':
            self.meta[attr.get('name') or attr.get('property')] = attr.get('content')
        if tag == 'script':
            self.script_type = attr.get('type')
            self.script_data = ''

    def handle_data(self, data):
        if self.script_type == 'application/ld+json':
            self.script_data += data

    def handle_endtag(self, tag):
        if tag == 'script':
            if self.script_type == 'application/ld+json':
                self.json_ld.append(json.loads(self.script_data))
            self.script_type = None

def file_for_route(route):
    path = ROOT / unquote(route).lstrip('/')
    return path / 'index.html' if route.endswith('/') else path

for route in ROUTES:
    path = file_for_route(route)
    source = path.read_text()
    page = Page(source)
    assert not re.search('[\u2013\u2014\u2018\u2019\u201c\u201d]', source), path
    assert source.count(DISCLAIMER) == 1, path
    assert not [key for key, value in Counter(page.ids).items() if value > 1], path
    assert page.meta['robots'] == 'index,follow', path
    assert any(item['@type'] == 'BreadcrumbList' for item in page.json_ld), path
    for link in page.links:
        url = urlsplit(link.get('href', ''))
        if url.scheme:
            assert url.scheme == 'https', link
            assert link.get('target') == '_blank', link
            required = {'sponsored', 'noopener', 'noreferrer'} if link['href'] == AFFILIATE else {'nofollow', 'noopener', 'noreferrer'}
            assert required <= set(link.get('rel', '').split()), link
            if url.netloc in {'jvz9.com', 'www.jvzoo.com'}:
                assert link['href'] == AFFILIATE, link
        else:
            assert not link.get('target') and not link.get('rel'), link
            target = path if not url.path else file_for_route(url.path)
            assert target.exists(), (path, link)
            if url.fragment:
                assert url.fragment in Page(target.read_text()).ids, (path, link)
    for image in page.images:
        assert image.get('alt') and file_for_route(image['src']).exists(), image
    if route.startswith('/articles/'):
        title = re.search('<title>(.*?)</title>', source).group(1)
        assert 50 <= len(title) <= 60, title
        assert 50 <= len(page.meta['description']) <= 155, page.meta['description']
        article = next(item for item in page.json_ld if item['@type'] == 'TechArticle')
        assert article['author']['@type'] == 'Organization'
        assert article['datePublished'] == article['dateModified'] == '2026-09-30'
        assert article['image']['width'] == 1600 and article['image']['height'] == 900
        assert all(cite['@type'] == 'CreativeWork' for cite in article['citation'])
        visible_refs = source[source.index('<section id="references"'):]
        assert all(cite['url'].replace('&', '&amp;') in visible_refs for cite in article['citation'])
        assert re.search('<section id="key-takeaways"', source)
        assert re.search('<section id="article-summary"', source)
        assert '<script async' not in source and 'plausible.io' not in source
        assert AFFILIATE in source and 'We may earn a commission if you purchase through this paid link.' in source
    print('PASS', route)

tree = ET.parse(ROOT / 'sitemap.xml')
ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
locations = [item.text for item in tree.findall('s:url/s:loc', ns)]
assert len(locations) == len(set(locations))
for route in ROUTES:
    assert 'https://dsotn.com' + route in locations, route
for name in ['index.html', 'articles/index.html']:
    source = (ROOT / name).read_text()
    page = Page(source)
    listing = next(item for item in page.json_ld if item['@type'] == 'ItemList')
    assert [item['position'] for item in listing['itemListElement']] == list(range(1, len(listing['itemListElement']) + 1))
    for slug in SLUGS:
        assert any(item['url'] == f'https://dsotn.com/articles/{slug}/' for item in listing['itemListElement'])
        assert f'href="/articles/{slug}/"' in source
for slug in SLUGS:
    assert f'https://dsotn.com/articles/{slug}/' in (ROOT / 'llms.txt').read_text()
    assert (ROOT / 'og/articles' / f'{slug}.png').exists()
    ET.parse(ROOT / 'og/articles' / f'{slug}.svg')
    assert slug in (ROOT / 'CREDITS.md').read_text()
    # PNG IHDR dimensions, no optional image dependency required.
    png = (ROOT / 'og/articles' / f'{slug}.png').read_bytes()
    assert png[:8] == b'\x89PNG\r\n\x1a\n'
    assert int.from_bytes(png[16:20], 'big') == 1200
    assert int.from_bytes(png[20:24], 'big') == 630
print('PASS discovery, schema, credits, image dimensions, and internal links')
