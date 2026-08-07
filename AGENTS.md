# Repository Agent Instructions

## Mandatory article-writing rules

Any agent or subagent that researches, plans, drafts, revises, audits, optimizes,
or prepares publication or distribution material for an article in this
repository MUST read `ARTICLE_WRITING_RULES.md` in full before beginning that
work.

The agent MUST adhere to every applicable rule in that document. This is a
required gate, not optional guidance. An agent must not delegate article work
without passing this requirement to every delegated agent.

If `ARTICLE_WRITING_RULES.md` conflicts with another repository instruction,
the agent must stop article work, identify the conflict to the owner, and wait
for the governing instruction to be clarified. It must not silently choose or
weaken a rule.

## CI Tripwire repository mapping

Use these values when applying section 0 of `ARTICLE_WRITING_RULES.md`:

| Placeholder | CI Tripwire value |
| --- | --- |
| `<SITE>` | `https://dsotn.com` |
| `<BRAND>` | `CI Tripwire Editorial` for the organization byline; `CI Tripwire` for the publisher |
| `<ARTICLE_DIR>` | `articles/<slug>/index.html` |
| `<ARTICLE_INDEX>` | `articles/index.html`, plus the relevant listings in `index.html`, `sitemap.xml`, and `llms.txt` |
| `<SCHEMA>` | The established article HTML structure and its `TechArticle` and breadcrumb JSON-LD |
| `<REF_DIR>` | The article's inline citations and closing `#references` section |
| `<IMAGES>` | `public/images/articles/`, `og/articles/`, and `CREDITS.md` |
| `<CHANGELOG_DIR>` | The repository root for dated article changelogs; `CHANGELOG.md` is the rolling index |
| `<DISCLAIMER>` | CI/security: `This article is informational and is not a substitute for a security review of your own workflows, repositories, or cloud accounts.` Stripe/billing: `This article is informational and is not a substitute for a security, billing, tax, or legal review of your own product.` |
| `<TOPIC_EXCLUSIONS>` | None documented; ask the owner before assuming an exclusion |

This is a static HTML repository, not a typed-data content repository. Map the
portable document's typed-module requirements to the existing static HTML and
JSON-LD structure. That representation difference does not relax its research,
accuracy, citation, voice, imagery, audit, or release requirements.
