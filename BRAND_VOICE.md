# CI Tripwire Brand Voice, Copywriting, and Editorial Governance

Canonical brand positioning, UX writing, conversion copywriting, and editorial
quality standard for **CI Tripwire** (`https://dsotn.com`), published by
**CI Tripwire Editorial**.

Every agent or contributor planning, drafting, editing, auditing, or optimizing
copy, metadata, navigation, tools, or articles in this repository must follow
this standard alongside `ARTICLE_WRITING_RULES.md`.

---

## 1. Brand, Product, and Audience Identity

### 1.1 Ecosystem and surfaces

- **CI Tripwire (`https://dsotn.com`):** Independent software engineering
  publication focused on GitHub Actions CI/CD security, Node.js Stripe billing
  reliability, and production AI release engineering. CI Tripwire is published
  by `CI Tripwire Editorial` and is unaffiliated with GitHub, Stripe, Fortra
  Tripwire, or any third-party enterprise security vendor.
- **`gha-guard` (`https://github.com/agentlaunchops-ai/gha-guard`):**
  Open-source companion workflow auditor referenced from CI/CD guides so
  maintainers can scan `.github/workflows` locally before merging changes.
- **Local Publication Planner (`/tools/local-publication-planner/`):** Free,
  zero-login browser worksheet and rational-cent cost calculator paired with a
  transparently disclosed affiliate evaluation funnel for Local Media Empire
  (`LOCAL_PUBLISHING_FUNNEL.md`). It keeps its own operator-focused vocabulary
  and explicit `Ad:` / affiliate labels so commercial promotion never blurs
  into core engineering guidance.

### 1.2 Audiences

- **Primary audience:** Software engineers, repository maintainers, platform
  and DevSecOps teams, and SaaS founders shipping GitHub Actions pipelines,
  Stripe subscription/webhook backends in Node.js, and AI-assisted software
  releases. High technical fluency, zero patience for filler or hand-waving.
- **Secondary audience:** Independent local newsletter and directory operators
  modeling publishing costs and evaluating publishing software before buying.

### 1.3 Positioning fundamentals

Every landing, hub, and product surface should answer six questions without
forcing visitors to decode buzzwords:

1. **What it is:** Primary-sourced engineering playbooks and audit checklists
   for CI/CD workflow security, Stripe billing reliability, and AI release
   gates.
2. **Who it serves:** Maintainers and product engineers whose YAML workflows,
   webhook handlers, and release pipelines hold production credentials or move
   customer money.
3. **Why it matters:** Small configuration mistakes (`pull_request_target`
   checkouts, implicit `GITHUB_TOKEN` write scopes, unpinned third-party
   actions, duplicate Stripe webhook deliveries, surprise seat prorations)
   quietly turn into secret leaks, broken builds, or double-billed customers.
4. **What makes it different:** Every non-trivial technical claim cites the
   exact official documentation, changelog, standard, or study inline, paired
   with copy-ready configuration patterns and concrete verification steps.
5. **Why trust it:** Organization-level authorship (`CI Tripwire Editorial`),
   verifiable inline citations, explicit review-posture and corrections links
   (`/about/#sourcing`, `/about/#corrections`), zero login walls, and upfront
   `Ad:` labeling on affiliate content.
6. **What to do next:** Open the relevant topic track (`GitHub Actions`,
   `Stripe & Billing`, or `All Guides`), copy and verify the control against
   your repo or handler, or run `gha-guard` / the free worksheet.

---

## 2. Brand Voice and Editorial Principles

### 2.1 Default personality

**Confident, clear, intelligent, approachable, direct, distinctive, and
compelling.**

Write like a sharp principal engineer and clear product writer speaking to
capable peers. Sound natural when read aloud.

Never write like:
- A generic SaaS template or agency slogan deck
- A dry internal compliance memo or bureaucratic policy brief
- An AI summary stalling before the point
- A brand lecturing or scolding the developers it exists to help
- A company afraid to state why its guides save real engineering pain

### 2.2 Twelve core editorial principles

1. **Clarity before cleverness:** Every headline, card summary, and section
   heading states something concrete and useful. Creative phrasing is welcome
   when it sharpens memory without hiding the subject.
2. **Benefits before feature inventories:** Explain what risk disappears or
   what workflow becomes predictable, not just which YAML keys or API fields
   exist.
3. **Specificity over abstraction:** Name exact triggers, scopes, API fields
   (`pull_request_target`, `GITHUB_TOKEN`, `proration_behavior`,
   `cancel_at_period_end`, `event.id`), dates, and verified numbers instead of
   vague abstractions.
4. **Confidence without exaggeration:** Recommend proven patterns directly
   without inventing metrics, guarantees, or superiority claims.
5. **Conversational professionalism:** Use clean, natural English, active
   verbs, and contractions where they fit. Preserve exact technical identifiers.
6. **Concision without sacrificing substance:** Cut throat-clearing and
   repeated caveats; keep every operational detail a maintainer needs to ship
   safely.
7. **Distinctiveness:** Write copy rooted in CI Tripwire's actual Primary-Cite
   + Failure-Mode approach rather than interchangeable DevSecOps cliches.
8. **Consistency without repetition:** Hold one recognizable voice from hero to
   footer without repeating the same tagline or caveat on every card.
9. **Persuasion through substance:** Earn clicks and trust by surfacing the
   real failure mode and the concrete fix right in the title, lede, and card.
10. **Audience awareness:** Match technical depth to the surface: exact YAML
    and Node.js semantics for engineers; plain-English arithmetic and demo
    questions on the local-publishing worksheet.
11. **Natural rhythm:** Mix crisp short sentences (including two-part
    headlines) with fuller explanatory sentences. Avoid monotonous machine
    cadence.
12. **Editorial judgment over rigid formulas:** Evaluate every line by whether
    it helps a real reader understand, trust, or act.

---

## 3. Contextual Judgment vs. Substantive Safeguards

### 3.1 Permitted stylistic tools (contextual judgment)

Blanket stylistic bans on individual everyday words or sentence shapes are
retired. Words such as `complete`, `comprehensive`, `powerful`, `confidence`,
`success`, `smarter`, `easier`, `better`, `transform`, `simplify`, `advanced`,
`professional`, `essential`, `key`, and `master` are **permitted** whenever
they are accurate, natural, and specific to what the reader achieves.

Likewise, writers may use:
- **Two-part headlines** (for example: `"Production breaks in the edge cases.
  Catch them before merge."` or `"Plan the issue. Price the work."`)
- **Short slogans and benefit-driven hooks**
- **Conversational questions** (`"Can GitHub Actions job summaries expose CI
  secrets?"`)
- **Direct, confident positioning** on homepages, category hubs, cards, and
  CTAs

Reject a word or construction when it is vague, robotic, repetitive, or
untrue, not because it matched a static word list. Continue to cut genuine AI
cliches (`delve`, `tapestry`, `"in today's ever-evolving landscape"`, empty
negation-and-reveal filler like `"It's not X, it's Y"` when it stalls instead
of stating the point, and deceptive curiosity-gap clickbait that hides the
topic).

### 3.2 Non-negotiable substantive safeguards

Editorial flexibility **never** relaxes accuracy, safety, compliance, privacy,
accessibility, or engineering integrity:

1. **Zero fabrication:** Never invent a study, benchmark, CVE, incident, quote,
   testimonial, customer count, statistic, price, trial term, or source URL.
2. **Primary-source Citation Correctness (`ARTICLE_WRITING_RULES.md` section
   5):** Every load-bearing factual claim in an article binds inline to a live,
   verified primary source (or explicitly labeled reputable secondary source)
   opened and confirmed by the author/auditor. No search URLs for specific
   claims.
3. **Compliance disclaimers (`AGENTS.md`):** Every article carries its exact
   topic disclaimer **once**, verbatim, in the closing section (never duplicated
   at the top of the body), followed by the four closing trust signals.
4. **Byline integrity:** Organization authorship (`CI Tripwire Editorial`)
   only; never fabricate individual reviewers, credentials, or certifications.
5. **Commercial and affiliate transparency:** Affiliate content must carry
   explicit upfront disclosure (`Includes affiliate promotion`, `Ad:` prefix on
   product-evaluation spokes), exact `rel="sponsored noopener noreferrer"` and
   `target="_blank"` on paid links, and zero earnings promises or false
   scarcity (`LOCAL_PUBLISHING_FUNNEL.md`).
6. **ASCII typography hygiene:** Straight quotes and standard ASCII hyphens,
   commas, colons, or periods only. No em dashes (`U+2014`), en dashes
   (`U+2013`), curly quotes (`U+2018`-`U+201D`), emoji, or unparsed Markdown
   backticks in rendered HTML.
7. **Privacy and security (`ARTICLE_WRITING_RULES.md` section 6.5):** Never add
   new ad-network pixels or consent-sensitive tracking scripts as part of copy
   or SEO work. External non-affiliate links must carry
   `rel="nofollow noopener noreferrer"` and `target="_blank"`; internal links
   use root-relative paths with no `rel` or `target`.

---

## 4. Homepage Positioning & Eight-Concept Hero Protocol

Whenever creating or overhauling a primary homepage hero, explore at least
**eight distinct creative directions** (Relatable, Direct, Product-focused,
Minimal, Benefit-driven, Differentiated, Aspirational, Problem-solution) and
select the strongest on immediate comprehension, audience relevance,
differentiation, memorability, credibility, visual fit, and conversion clarity.

### Recorded hero evaluation for `dsotn.com` (`/`)

| Direction | Candidate headline | Evaluation |
| --- | --- | --- |
| 1. Relatable | `One YAML line can hand a fork write access. Catch it before merge.` | Vivid GitHub Actions hook, but narrows the brand to YAML and omits Stripe billing and AI release gates. |
| 2. Direct | `Primary-sourced security and billing guides for software teams.` | Clear and accurate, but reads like a catalog label rather than a memorable point of view. |
| 3. Product-focused | `CI Tripwire: verified playbooks for safer pipelines and cleaner billing.` | Explains the catalog well, though leading with the brand name duplicates the header bar. |
| 4. Minimal | `Harden the pipeline. Trust the ledger.` | Punchy and rhythmic, but slightly abstract for a first-time visitor arriving from search. |
| 5. Benefit-driven | `Ship CI workflows and Stripe billing you never have to debug in production.` | Appealing promise, but "never" overpromises against our no-exaggeration standard. |
| 6. Differentiated | `Every claim cited to the spec. Every fix ready for code review.` | Captures the citation differentiator well; works best as supporting proof right beneath the headline. |
| 7. Aspirational | `Run CI/CD and billing paths worthy of a high-trust engineering team.` | Good posture, but softer than naming the operational problem directly. |
| **8. Problem-solution (Selected)** | **`Production breaks in the edge cases. Catch them before merge.`** | **Selected.** Immediately names why engineers visit (subtle edge-case failures across CI, billing, and AI releases), states the outcome (`Catch them before merge`), fits the 2-column hero cleanly on mobile (`390px`) and desktop (`1440px`), and pairs naturally with a specific lede and direct topic CTAs. |

---

## 5. Surface-by-Surface Copy & UX Writing Standards

### 5.1 Homepage (`/`)
- Establish what CI Tripwire is, who it serves, what makes it trustworthy
  (inline primary citations + open-source `gha-guard`), and clear paths into
  each core engineering track above the fold.
- Group guides by engineering job-to-be-done (`GitHub Actions & CI/CD Security`,
  `Stripe & Node.js Billing`, `AI Release Engineering`) ahead of secondary
  `Local Publishing` affiliate resources so developer visitors immediately see
  core technical depth.

### 5.2 Category hubs (`/categories/github-actions/`, `/categories/stripe-billing/`) and `/articles/`
- Open with a clear 1-2 sentence explanation of how the guides in that track
  fit together architecturally (for example: webhook signature verification ->
  durable event ledger -> seat proration -> usage meters -> cancel-save flows).
- Provide fast jump links on multi-category index pages so mobile visitors reach
  their stack in one tap.
- Every card summary must state the specific operational payoff rather than
  repeating the card title in different words.

### 5.3 About page (`/about/`)
- State CI Tripwire's mission, technical scope, organization authorship
  (`CI Tripwire Editorial`), independence from third-party vendors, primary
  sourcing hierarchy (`#sourcing`), contributor & commercial disclosure
  (`#contributors`), and public issue-based corrections workflow
  (`#corrections`).

### 5.4 Interactive tools & UX copy (`/tools/local-publication-planner/`)
- **CTA labels** must describe the exact action or destination (`Browse all 23
  guides`, `Download my worksheet (.txt)`, `Evaluate Local Media Empire
  (affiliate promotion)`). Never disguise commercial or external jumps.
- **Form labels, empty states, errors, and confirmations** must tell the user
  what input is expected, keep all entries local in the browser as promised,
  and state plainly how calculations work without implying guaranteed revenue.

### 5.5 SEO metadata, snippets, and internal linking
- **Article `<title>`:** 45-60 characters (`50-60` preferred; `50-60` required
  on funnel routes tested by `tests/check-funnel.py`), natural sentence case
  preserving exact technical casing (`GITHUB_TOKEN`, `OIDC`, `SHA`, `Stripe`,
  `Node.js`, `MRR`, `CI/CD`), naming the exact token/mechanism developers query.
- **Meta description:** 50-155 characters, front-loading the concrete solution
  or key API/workflow terms (`proration_behavior`, `cancel_at_period_end`,
  `allow-unsafe-pr-checkout`, `evaluate mode`) to earn clicks on Google and
  Bing SERPs.
- **Images & OG cards:** Landscape `1600x900` hero JPEGs compressed under
  `350 KB` (`fetchpriority="high"` on detail routes, `loading="lazy"` and
  `decoding="async"` on listing cards), paired with `1200x630` PNG + SVG cards
  in `og/` and `<meta name="robots" content="index,follow,max-image-preview:large">`
  on non-funnel editorial routes.
- **Cluster interlinking:** Every article links contextually or via a closing
  `#related-guides` block to at least 3 relevant sibling guides plus its
  category hub, avoiding query cannibalization between hub overviews and
  feature-specific deep dives.

---

## 6. Seven-Lens Editorial Quality Gate & Validation

Before committing any copy, metadata, UX, or article change, review every
modified surface through all seven lenses:

1. **Human test:** Would a sharp engineer or editor say this aloud without
   wincing?
2. **Differentiation test:** Could a generic DevSecOps blog paste this sentence
   unchanged? If yes, replace with the concrete mechanism, scope, or number.
3. **Usefulness test:** Does this help the reader understand the failure mode,
   verify the source, or choose the next step?
4. **Repetition test:** Did the headline, lede, takeaway, or adjacent card
   already say this? Cut duplicate phrasing.
5. **Accuracy test:** Is every factual claim backed by a verified primary
   source or real repository behavior?
6. **Conversion test:** Is the next action (`Read guide`, `Explore track`,
   `Download worksheet`, `gha-guard`) obvious, honest, and friction-free?
7. **Brand test:** Does the page read unmistakably like CI Tripwire?

### Mandatory automated & visual validation before shipping

Run all repository validation suites from the active worktree:

```bash
python3 tests/check-funnel.py
python3 tests/check-site-seo.py
node --test tests/local-publication-planner.test.mjs
```

And inspect rendered mobile (`390px`) and desktop (`1440px`) viewports to
confirm zero horizontal overflow, clean text wrapping, intact disclosures, and
accessible contrast and focus states.
