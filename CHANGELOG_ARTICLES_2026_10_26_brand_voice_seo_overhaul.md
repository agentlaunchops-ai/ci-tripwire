# Editorial, Brand Voice, and SEO Overhaul Changelog (2026-10-26)

Base commit: `a78b29ebb9d48d04a1e8f9e4a1243fb583b4c57b` (`origin/main` at worktree cut).
Branch: `feat/brand-voice-seo-overhaul` in isolated worktree `/tmp/ci-tripwire-brand-seo-overhaul`.

## What changed and why

1. **Canonical editorial & brand voice governance (`BRAND_VOICE.md`, `AGENTS.md`, `ARTICLE_WRITING_RULES.md`):**
   - Established `BRAND_VOICE.md` as the canonical positioning, voice, UX writing, conversion copywriting, eight-concept homepage hero evaluation, surface-by-surface standards, and seven-lens editorial quality gate for `https://dsotn.com`.
   - Updated `AGENTS.md` and `ARTICLE_WRITING_RULES.md` (sections 1.5, 3.3, 3.4, 4.2, 6.1, 12.1) to retire arbitrary blanket prohibitions on single everyday words, two-part headlines, slogans, and conversational questions in favor of contextual editorial judgment, while preserving 100% of factual accuracy, primary-source citation, compliance disclaimer, affiliate disclosure, privacy, accessibility, and ASCII typography safeguards.
2. **Sitewide brand positioning, category hubs, catalog, about page, and UX polish:**
   - Overhauled `/` (`index.html`) with the selected problem-solution hero (`"Production breaks in the edge cases. Catch them before merge."`), clear track navigation, November 2 `pull_request_target` enforcement notice, core engineering tracks ahead of affiliate resources, `Organization` + `WebSite` + `ItemList` JSON-LD, `og/site.png`, and `loading="lazy"` on all 23 catalog cards.
   - Created `/categories/github-actions/` (`categories/github-actions/index.html`, zero analytics scripts per section 6.5) organizing all 15 GitHub Actions security guides into three maintainer workflows.
   - Overhauled `/categories/stripe-billing/` (`categories/stripe-billing/index.html`), `/articles/` (`articles/index.html`), `/about/` (`about/index.html`, with explicit independence from GitHub, Stripe, and Fortra Tripwire to resolve entity bleed in search queries), and `/tools/local-publication-planner/` (`index.html` + `public/js/local-publication-planner.mjs` concrete field examples and download confirmation copy, preserving `calculateBudget` math and all affiliate disclosures).
3. **Technical & CTR remediation across 23 articles + primary-sourced `GITHUB_TOKEN` expansion:**
   - Cropped and compressed all 17 oversized/portrait June hero JPEGs in `public/images/articles/` to `1600x900` landscape (`< 350 KB` each), reducing total hero image weight from `51.59 MB` to `4.54 MB` (`91.2%` reduction).
   - Generated `1200x630` PNG + valid SVG Open Graph card pairs for `og/site.{png,svg}` and all 17 June legacy articles in `og/articles/`.
   - Fixed 127 raw unparsed Markdown backtick spans across 4 core GitHub Actions articles (`pull-request-target-security`, `github-token-permissions`, `github-actions-security-risks`, `pin-github-actions-sha`), 10 curly apostrophes across 2 articles, 17 duplicate disclaimers (`count == 1` across all 23 articles), missing `rel="nofollow noopener noreferrer" target="_blank"` on external `https://` links, broken `/articles/github-actions-security-risks/` header nav link, and 160-char description overflow on `pin-github-actions-sha`.
   - Expanded `articles/github-token-permissions/index.html` with `<section id="repo-org-settings">` covering personal vs. organization default `GITHUB_TOKEN` permissions (`contents` and `packages` read access vs. permissive read/write), inherited restricted organization/enterprise settings disabling permissive UI controls, YAML `permissions` overrides, and `Allow GitHub Actions to create and approve pull requests` under `Settings > Actions > General > Workflow permissions` (targeting the #1 Search Console query cluster).
   - Added `#related-guides` internal cluster linking across all 21 non-funnel technical articles so 0 articles are orphaned or dead-ends.
   - Updated `sitemap.xml` (all 29 routes), `llms.txt`, and `styles.css`, and added `tests/check-site-seo.py`.

## Per-citation ledger (`articles/github-token-permissions/index.html` expansion)

Retrieved and verified via live HTTP 200 fetch on `2026-10-26`:

| Claim | Cite | Supporting quote / primary text | Source date | Verdict |
| --- | --- | --- | --- | --- |
| Two workflow permission modes under `Settings > Actions > General > Workflow permissions`: read/write for all permissions (permissive) vs read for `contents` and `packages` (restricted) | [5], [6] | `Under "Workflow permissions", choose whether you want the GITHUB_TOKEN to have read and write access for all permissions (the permissive setting), or just read access for the contents and packages permissions (the restricted setting).` | Live GitHub Docs retrieved 2026-10-26 | Confirmed |
| Default `GITHUB_TOKEN` permissions for new personal repositories and newly created organizations (`contents` and `packages` read access only), and org inheritance for new org repos | [5], [6] | Repo docs [5]: `By default, when you create a new repository in your personal account, GITHUB_TOKEN only has read access for the contents and packages scopes. If you create a new repository in an organization, the setting is inherited from what is configured in the organization settings.` Org docs [6]: `By default, when you create a new organization, GITHUB_TOKEN only has read access for the contents and packages scopes.` | Live GitHub Docs retrieved 2026-10-26 | Confirmed |
| Organization restrictive default disables permissive option in repository settings; Enterprise restrictive default prevents selecting permissive default in org settings | [5], [6] | Repo docs [5]: `If your repository belongs to an organization and a more restrictive default has been selected in the organization settings, the same option is selected in your repository settings and the permissive option is disabled.` Org docs [6]: `If your organization belongs to a GitHub Enterprise account and a more restrictive default has been selected in the enterprise settings, you won't be able to select the more permissive default in your organization settings.` | Live GitHub Docs retrieved 2026-10-26 | Confirmed |
| Users with write access to a repository can modify `GITHUB_TOKEN` permissions via the `permissions` key in the workflow file | [5], [6] | `Anyone with write access to a repository can modify the permissions granted to the GITHUB_TOKEN, adding or removing access as required, by editing the permissions key in the workflow file.` | Live GitHub Docs retrieved 2026-10-26 | Confirmed |
| Default pull-request creation/approval block and `Allow GitHub Actions to create and approve pull requests` toggle | [5], [6] | Repo docs [5]: `By default, when you create a new repository in your personal account, workflows are not allowed to create or approve pull requests.` Org docs [6]: `By default, when you create a new organization, workflows are not allowed to create or approve pull requests.` Both [5], [6]: `Under "Workflow permissions", use the Allow GitHub Actions to create and approve pull requests setting to configure whether GITHUB_TOKEN can create and approve pull requests.` | Live GitHub Docs retrieved 2026-10-26 | Confirmed |

## Independent subagent audit & adjudication

An independent read-only auditor subagent (`053354cd-d50f-4136-940e-1bfd1cbd0f96`) read `BRAND_VOICE.md` and `ARTICLE_WRITING_RULES.md` in full, executed all three validation suites, opened all 6 primary URLs on `articles/github-token-permissions/index.html` live (`HTTP 200`), and audited governance, brand voice, citations, compliance/privacy/WCAG contrast, and SEO discovery across all 29 routes:

| Round | HIGH | MEDIUM | LOW | Adjudication & Fixes |
| --- | --- | --- | --- | --- |
| 1 | 0 | 3 | 5 | Fixed all 3 MEDIUMs and all 5 LOWs: (`M-01`) aligned hub-card `Updated` dates on the 3 August 2026 articles (`2026-08-05`, `2026-08-11`, `2026-08-13`) and added programmatic hub-card date parity assertion in `tests/check-site-seo.py`; (`M-02`) added split citation `[2]` on `id-token: write` beside `[3]` in `github-token-permissions`; (`M-03`) rewrote `#repo-org-settings` prose and quoted the exact checkbox label `"Allow GitHub Actions to create and approve pull requests"` (verified `0` unquoted 8-gram overlaps against live `[5]` and `[6]`); (`L-01`) renamed `All Engineering Guides (23)` to `All Guides (23)` across all 29 routes and `articles/index.html` title; (`L-02`) promoted `.about-card` headings on `/about/` from `h3` to `h2`; (`L-03`) replaced residual `denylist`/`superlatives` checklist phrasing in `ARTICLE_WRITING_RULES.md`, added `AboutPage` to `AGENTS.md`, and tightened hero check to `<= 350 KiB`; (`L-04`) added explicit `:focus-visible` outlines in `styles.css`; (`L-05`) replaced `Clean verdict:` / `Avoid verdict:` meta-labels in `stripe-webhook-idempotency-node`. |
| 2 | 0 | 0 | 0 | Independent Round 2 re-verification confirmed all 8 findings resolved with `0 HIGH`, `0 MEDIUM`, `0 LOW` across Governance, Brand Voice, Citations/Accuracy, Compliance/Privacy, and SEO/Discovery. |

## Pass 4, Pass 5, and Pass 6 verification (`github-token-permissions` & remediated catalog)

- **Pass 4 (Voice & Seven-Lens Quality Gate):** PASS. Opening `#editorial-summary`, new `#repo-org-settings` section, hub introductions, homepage hero, and card summaries read naturally aloud, name concrete mechanisms (`GITHUB_TOKEN`, `Settings > Actions > General`, `proration_behavior`, `cancel_at_period_end`, `event.id`), and contain zero banned typographic characters (`U+2013`, `U+2014`, `U+2018`-`U+201D`) or raw Markdown backticks.
- **Pass 5 (Mobile scanability & trust signals):** PASS. `#key-takeaways` + `#article-summary` answer the headline on mobile (`390px`); every article carries its exact topic disclaimer once (`count == 1`), organization honesty line, `/about/#contributors`, `/about/#sourcing`, `/about/#corrections`, and source count/review date.
- **Pass 6 (Integrity & digestibility triple-audit):** PASS across 3 hallucination passes against live GitHub Docs `[1]`-`[6]`, zero unquoted verbatim 8-gram runs against live `[5]` and `[6]`, all 29 routes covered by `tests/check-site-seo.py`.

## Automated & visual gates

- `python3 tests/check-funnel.py`: PASS
- `python3 tests/check-site-seo.py`: PASS (all 29 routes, JSON-LD, citations, links, disclaimers, `1200x630` OG PNG/SVG pairs, and `1600x900` `<= 350 KiB` heroes)
- `node --test tests/local-publication-planner.test.mjs`: PASS (`8/8` tests)
- Live HTTP 200 + headless Chrome Blink layout verification at `390px` mobile and `1440px` desktop across `/`, `/categories/github-actions/`, `/categories/stripe-billing/`, `/articles/`, `/about/`, `/tools/local-publication-planner/`, `/articles/github-token-permissions/`, `/articles/pull-request-target-november-2/`, and `/articles/stripe-webhook-idempotency-node/`: PASS (`scrollWidth <= innerWidth` on every route at both `390px` and `1440px`).
