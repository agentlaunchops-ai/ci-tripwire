# Repository Agent Instructions

## Mandatory editorial, brand voice, and article rules

Any agent or subagent that researches, plans, drafts, revises, audits, optimizes,
or prepares marketing, UX, SEO, publication, or distribution material in this
repository MUST read both `BRAND_VOICE.md` and `ARTICLE_WRITING_RULES.md` in
full before beginning that work.

- **`BRAND_VOICE.md`** is the canonical brand positioning, voice, UX writing,
  conversion copywriting, homepage/hub copy, SEO snippet, and contextual
  language-judgment standard across `https://dsotn.com`.
- **`ARTICLE_WRITING_RULES.md`** is the canonical factual accuracy, primary
  citation, compliance disclaimer, mobile scanability, self-audit (Passes 1-6),
  and independent 12-auditor verification gate for editorial articles.

The agent MUST adhere to every applicable rule in both documents. This is a
required gate, not optional guidance. An agent must not delegate copy, SEO, or
article work without passing both requirements to every delegated agent.

If `BRAND_VOICE.md` or `ARTICLE_WRITING_RULES.md` conflicts with another
repository instruction, the agent must stop work, identify the conflict to the
owner, and wait for the governing instruction to be clarified. Never weaken
safeguards governing factual accuracy, primary citations, legal/commercial
disclosures, privacy, accessibility, or security.

## CI Tripwire repository mapping

Use these values when applying section 0 of `ARTICLE_WRITING_RULES.md`:

| Placeholder | CI Tripwire value |
| --- | --- |
| `<SITE>` | `https://dsotn.com` |
| `<BRAND>` | `CI Tripwire Editorial` for the organization byline; `CI Tripwire` for the publisher |
| `<ARTICLE_DIR>` | `articles/<slug>/index.html` |
| `<ARTICLE_INDEX>` | `articles/index.html`, plus the relevant listings in `index.html`, `categories/github-actions/index.html`, `categories/stripe-billing/index.html`, `sitemap.xml`, and `llms.txt` |
| `<SCHEMA>` | The established HTML structure (`TechArticle`, `BreadcrumbList`, `ItemList`, `WebSite`, `Organization`, `WebApplication`) |
| `<REF_DIR>` | The article's inline citations and closing `#references` section |
| `<IMAGES>` | `public/images/articles/` (`1600x900` landscape `<350 KB`), `og/` (`1200x630` PNG + SVG pairs), and `CREDITS.md` |
| `<CHANGELOG_DIR>` | The repository root for dated changelogs; `CHANGELOG.md` is the rolling index |
| `<DISCLAIMER>` | CI/security: `This article is informational and is not a substitute for a security review of your own workflows, repositories, or cloud accounts.` Stripe/billing: `This article is informational and is not a substitute for a security, billing, tax, or legal review of your own product.` Local publishing: `This article is informational and is not a substitute for a legal, tax, or business review of your own publication.` |
| `<TOPIC_EXCLUSIONS>` | None documented; ask the owner before assuming an exclusion |

This is a static HTML repository, not a typed-data content repository. Map the
portable document's typed-module requirements to the existing static HTML and
JSON-LD structure. That representation difference does not relax its research,
accuracy, citation, voice, imagery, audit, or release requirements.

## Mandatory validation gates

Before opening a pull request or shipping changes, run all applicable checks
from an isolated worktree cut from `origin/main`:

```bash
python3 tests/check-funnel.py
python3 tests/check-site-seo.py
node --test tests/local-publication-planner.test.mjs
```

Also inspect rendered mobile (`390px`) and desktop (`1440px`) viewports for
text wrapping, visual hierarchy, and zero horizontal scroll.
