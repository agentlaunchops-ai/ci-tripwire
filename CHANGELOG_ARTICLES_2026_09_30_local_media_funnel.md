# Article changelog: Local Media Empire affiliate funnel

Voice register: easy-reading.

Base commit: `0ee779663216a743b9b3c978b6cdcfaeff61864f` (`origin/main` at branch cut). Worktree: `/tmp/ci-tripwire-local-media-funnel`. Branch: `feat/local-media-affiliate-funnel`.

## What changed and why

Built an on-site funnel for the supplied Local Media Empire affiliate URL. The pillar article gives an issue outline and sending checks. The free worksheet creates a downloadable publication plan with an explicit cost model. The product article helps readers evaluate the seller's offer and contains the disclosed outbound link.

The two article routes use static HTML, Organization authors, TechArticle and breadcrumb JSON-LD, visible point-of-claim citations, real topical photos, distinct OG PNG/SVG pairs, closing disclaimers, and trust signals. Discovery is wired into the homepage, article index, sitemap, and llms.txt. The tool has WebApplication and breadcrumb schema.

The operator explicitly requested deletion of the affiliate allowlist restriction. Commit `489fd9f` removes only that requirement; sponsored attributes and visible disclosure remain mandatory. The operator authorized the choice of topic disclaimer. Commit `d488a10` adds the local-publishing disclaimer to AGENTS.md before content drafting.

Scope: this campaign and its discovery entries. Existing articles, unrelated checkout work, accounts, email delivery, and production deployment are outside this implementation.

## Source registry and per-claim ledger

Retrieved 2026-09-30. Source dates below distinguish page publication/edit notes from the retrieval date. Unversioned platform requirements are checked against the live page.

| Claim and locations | Cite ID | Exact support or independently derived value | Source date | Verdict |
| --- | --- | --- | --- | --- |
| SPF or DKIM for senders to personal Gmail accounts, both articles' takeaways and sending/demo paragraphs | `gmail` | Google: "Set up SPF or DKIM email authentication for your sending domains." The page's audience is personal Gmail accounts | Live, unversioned requirements, retrieved 2026-09-30 | Confirmed; an authentication requirement, not a complete sender checklist |
| Opt-in and confirmation are Google recommendations, guide takeaways and sending section | `gmail` | "recipients opt in" "Confirm each recipient's email address before subscribing them." | Live, unversioned subscription guidelines, retrieved 2026-09-30 | Confirmed as recommendations |
| Commercial-email classification depends on primary purpose, guide takeaways and sending section | `commercial` | FTC: "What matters is the 'primary purpose' of the message." | Page displays August 2023 and January 2024 edit note; retrieved 2026-09-30 | Confirmed; U.S. scope stated |
| Commercial email carries a postal address, guide takeaways and sending section | `commercial` | "Your message must include your valid physical postal address." | Same FTC guide, retrieved 2026-09-30 | Confirmed |
| Commercial email explains how to stop future marketing, guide takeaways and sending section | `commercial` | "Your message must include a clear and conspicuous explanation of how the recipient can opt out of getting marketing email from you in the future." | Same FTC guide, retrieved 2026-09-30 | Confirmed |
| Native-ad disclosures clear and prominent when needed to prevent deception, guide takeaways and issue section | `native` | "If a disclosure is necessary to prevent deception, the disclosure must be clear and prominent." | Page displays December 2015; retrieved 2026-09-30 | Confirmed; conditional phrasing retained |
| Place the disclosure near the item it explains, guide issue section | `native` | FTC disclosure guidance: "as close as possible to the native ads to which they relate" | Same FTC guide, retrieved 2026-09-30 | Confirmed |
| Affiliates explain the commission relationship clearly and conspicuously, product takeaways and disclosure section | `affiliate` | "You should disclose your relationship to the retailer clearly and conspicuously on your site" | Live FTC FAQ, retrieved 2026-09-30 | Confirmed |
| No paid-account test in preparing these articles, both articles | Direct session evidence | The writer fetched the public seller page and performed no account login or paid-account test while preparing these new articles | Preparation 2026-09-30 | Confirmed as an article-specific statement; no assertion about the brand's prior history |
| No commissioned independent expert review of these new pieces | Direct session evidence | No commissioned expert contributor participated in their preparation. Independent editorial audits below are separate | Preparation 2026-09-30 | Confirmed |
| Offer-link identity and supplied URL | Routing inspection, not an article capability citation | `jvz9.com/c/3636661/454123/` redirects through JVZoo to `localmediaempire.com/lmpbundle?aid=3636661`, final HTTP 200 | Observed 2026-09-30 | Identity only; no vendor evidence cited for product performance |
| Worksheet inputs stay in the page until downloaded; no persistence or submission | Implementation and browser requests | No fetch, storage, or form submission; submit prevented; a local Blob text download contains the entries; observed requests are local GETs only | Code and browser check 2026-09-30 | Confirmed |
| Cash cost, labor allowance, setup recovery, and cost target | Authored arithmetic | Cash = monthly operating + growth budget. Labor = weekly hours x hourly value x 52 / 12. Recovery = setup cost / entered months. Target = sum | Authored 2026-09-30 | Re-derived independently; 52-week constant-work assumption explicit |
| Cost coverage placement count, worksheet | Authored arithmetic | Exact rational cents divide the unrounded target by the entered net placement amount, ceiling to an integer. Zero amount gives no placement count | Authored 2026-09-30 | Confirmed; no sales forecast |
| Different photos, authors and licenses | `CREDITS.md`, Pexels source pages | Guide photo: Suzy Hazelwood, photo 5010877. Product photo: Mike van Schoonderwalt, photo 5505690. Both under Pexels License | Retrieved 2026-09-30 | Source pages and license opened; no identifiable people visible |

Sources: Google Gmail Help's Email sender guidelines; FTC CAN-SPAM guide; FTC Native Advertising guide; FTC Endorsement Guides FAQ. Full URLs occur in each article's reference section and JSON-LD. Raw Google HTML was read and scanned. Initial curl requests to FTC returned 403; first-party page extraction supplied the exact supporting text. A later raw fetch with urllib and a standard browser User-Agent returned HTTP 200 for all three FTC pages, and the raw sources were also read and compared. No generated summary or search snippet was used as evidence.

## Defects found and adjudicated

| ID | Severity | Axis | Before | Fix and independently verified evidence | Bucket |
| --- | --- | --- | --- | --- | --- |
| Preliminary H2-01 | HIGH | numeric accuracy | $10 + $5.03 could produce $15.030000000000001; dividing by $15.03 and ceiling returned 2 placements | Exact rational cent arithmetic now returns 1. Regression covers this boundary, fractional setup recovery and labor; independent re-derivation follows below | Must fix, fixed |
| Preliminary H1-01 | MEDIUM | unsupported absence claim | "CI Tripwire has not tested a paid account" asserted brand-wide history | Scoped to "while preparing this article," which direct session evidence establishes | Must fix, fixed |
| Final H2-01 | LOW | numeric presentation | Currency displayed a rounded cent total while placement count used the exact total | Clarification added on page and in download: "Dollar totals are displayed rounded to cents. Placement counts use unrounded totals." | Should fix now, fixed |

The initial review stopped after three independent reviewers when the HIGH was found. It is not counted as a completed twelve-auditor round. The formal round uses fresh auditors against the revised candidate. Resource limits permit three reviewers at a time; each has a separate fresh context and cannot see any sibling's report or the writer ledger. This scheduling differs from the policy's simultaneous-launch instruction; the independent reviewer count and coverage are retained.

## Independent round table

| Round | Auditors | HIGH | MEDIUM | LOW | Outcome |
| --- | --- | --- | --- | --- | --- |
| Preliminary, stopped | 3 | 1 | 1 | 0 | Both fixed; fresh full round required |
| Formal round | 12 | 0 | 0 | 1 | LOW display clarification fixed and checked; 0 unresolved HIGH/MEDIUM/LOW |
| Focused LOW verification | Original H2 reviewer | 0 | 0 | 0 | Clarification confirmed on page and in download |

All twelve independent reviewers read the full governing rules before work, used fresh contexts, and supplied coverage lines. Each opened or independently derived the sources for its slice. The LOW follow-up uses the original reviewer and is not counted as a thirteenth independent slice.

| Reviewer | Slice | Claims checked | Sources opened | HIGH | MEDIUM | LOW | Final status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Product identity and attribution | 18 | 5 | 0 | 0 | 0 | CLEAN |
| H2 | Numeric accuracy and budget model | 22 | 5 | 0 | 0 | 1 | LOW fixed; focused verification checked 4 claims / 2 sources, CLEAN |
| H3 | Legal interpretations and disclaimers | 11 | 3 | 0 | 0 | 0 | CLEAN |
| H4 | Privacy, input rendering, export, safe links | 22 | 10 | 0 | 0 | 0 | CLEAN |
| H5 | Absences, dates, counts, metadata, imagery | 40 | 7 | 0 | 0 | 0 | CLEAN |
| C1 | Google sender/opt-in claims and citation metadata | 8 | 1 | 0 | 0 | 0 | CLEAN |
| C2 | FTC commercial-email claims and citation metadata | 6 | 1 | 0 | 0 | 0 | CLEAN |
| C3 | FTC native-ad claims and citation metadata | 3 | 1 | 0 | 0 | 0 | CLEAN |
| C4 | FTC affiliate-disclosure claims and citation metadata | 2 | 1 | 0 | 0 | 0 | CLEAN |
| C5 | Citation parity and photo provenance | 27 | 7 | 0 | 0 | 0 | CLEAN |
| S1 | Anti-AI voice, product coherence, reader value | 9 | 2 | 0 | 0 | 0 | CLEAN |
| S2 | Digestibility, repetition, scanability, trust, plagiarism | 8 | 4 | 0 | 0 | 0 | CLEAN |

Coverage counts overlap and include local implementation sources; they are not counts of unique factual claims or unique external documents. Each citation reviewer verified exact title, publisher, and URL. C5 confirmed 14 inline markers, five article-specific reference records across two articles, and four unique official URLs. S2 independently fetched all four raw sources and found no unattributed eight-word overlaps. S1 also reviewed the distribution draft. The whole reviewer set covers the full funnel, not only an offer paragraph.

The closing non-review statements are about commissioned expert review and paid-account testing while preparing the pieces; they do not deny that these editorial audits occurred. No legal, product-performance, or provider clearance is implied.

## Pass 1 to 3

- Source content: the eight externally sourced claim types above are bound to the actual supporting source paragraphs. Seller descriptions stay outside factual citations.
- Numeric and acronym check: SPF/DKIM phrasing retains "or" for the all-sender requirement; subscription recommendations are labeled recommendations. Authored budget formula is re-derived rather than sourced to product marketing.
- Tone/style: practical easy-reading register; no earnings promises, invented testimonial, scarcity, fake credentials, or lecturing the reader.

## Pass 4: voice consistency end-to-end

- Opening sample: PASS. Issue outline and cost planning lead; affiliate posture visible before the article title.
- Middle samples: guide `first-issue`, `sending`, `budget`; product `demo`, `terms`, `disclosure`. PASS. Concrete task language and questions for the seller.
- Closing sample: PASS. Exact disclaimer once, review posture, contributor/sourcing links, corrections pointer, source count/date.
- Anti-AI voice audit: PASS on author reread. No negation/reveal setup, decorative triads, community narration, superlatives, em dashes, en dashes, curly quotes, or emoji.

## Pass 5: scanability and trust signals

- Mobile scan path: PASS. Takeaways and section 2 give the planning/evaluation answer; worksheet CTA visible near the guide's payoff.
- Longest paragraph: guide 41 words; product 37 words, below the easy-reading cap.
- Bottom-line callout: YES in both articles.
- Comparison data: semantic three-column tables with five body rows each.
- Ranked verdicts: none; no claim that a product is ranked or independently tested.
- Headings: concrete tasks and requirements rather than generic section names.
- Three-place stats: no numerical headline claim. Cost formula appears where the tool computes it and in its download.
- Body counts: guide 876 words, 5 min at 200 wpm rounded up; product 777 words, 4 min. Jump list not needed.
- Closing trust signals: PASS in both articles. Worksheet also carries the disclaimer and process/corrections links.
- Takeaway cite density: guide 5 of 5 hard-claim bullets; product's two externally sourced hard-claim bullets each cited. Remaining bullets are evaluation-method recommendations and direct preparation disclosures.

## Pass 6: integrity and digestibility triple-audit

- Hallucination pass 1: 15 ledger rows checked. The broad account-testing absence claim was narrowed during preliminary review; no unverified claim retained.
- Hallucination pass 2: the same 15 rows checked clause by clause after the fixes; source scope and modeled budget assumptions retained.
- Hallucination pass 3: the same 15 rows checked against final facts and schema; source labels/URLs and offer identity retained. Numeric display clarification records formatting behavior rather than introducing a new product claim.
- Citation identity and supporting passages: confirmed for all four primary documents.
- Ledger: 15 rows, all confirmed. Internal process and authored arithmetic are distinguished from external factual evidence.
- Plagiarism: no unattributed 8-word run found against the raw Google/FTC page text. The reference-list source title is an explicitly attributed bibliographic label. FTC wording is paraphrased in the articles; exact evidence in this ledger is explicitly quoted and attributed. Independent S2 comparison also found no unattributed eight-word runs.
- Top-summary digestibility: PASS on a cold read; an issue and a cost plan are familiar objects, and the product page says exactly what the reader can evaluate.
- Repetition: factual statements recur as takeaways and point-of-claim prose; offer disclosures recur beside each paid CTA to stay visible. No decorative recap.

## Verification gates

- `node --test tests/*.test.mjs`: all 8 tests pass.
- `python3 tests/check-funnel.py`: all funnel routes, internal anchors/targets, source/schema parity, Organization authors, disclaimer counts, sponsored attributes, discovery entries, XML/JSON, photo credit presence and OG dimensions pass.
- `git diff --check`: clean.
- `npm run lint`, `npm run build`, `npm test`: not applicable; this is a static HTML repository with no package.json. The full added Node suite and offline HTML gate run instead. There is no preexisting automated npm suite.
- Citation-title checker / article SEO / sitewide SEO / docs generator: no repository commands exist. The offline gate checks the authored titles and descriptions, schema, routes, references, image dimensions and discovery wiring. Live source claims are reviewed manually and by the independent citation auditors.
- Catalog/SEO regeneration: static source and discovery entries edited directly; no typed module generator exists. OG PNG/SVG regenerated from the actual credited photographs.
- Banned-character scan: no banned punctuation in either article, the worksheet, script, distribution draft, campaign notes, stylesheet, or tests.

Browser QA uses standalone headless Chromium because the Browser skill's runtime reported no available browser. At 390px and 1440px all three routes returned 200, images loaded, no page overflow occurred, and no page errors occurred. The guide -> worksheet -> product-page path worked. The paid link retains the supplied URL and attributes. A user-triggered worksheet download contains the entered plan and outputs. Inputs are not transmitted or persisted. Invalid/empty financial inputs clear the output and disable the download. The article remains complete with JavaScript disabled. Native seller checkout, affiliate attribution on a real purchase, and email delivery have not been tested.

Local screenshots and browser-result JSON are retained under `/tmp/ci-funnel-*`; they are QA artifacts, not public SEO resources.

## Affiliate opportunity and residual risk

Promotes Local Media Empire using the owner-supplied link. Commission disclosure appears at entry and beside each outbound offer CTA, and discovery cards disclose the promotion. No allowlist required under the owner's updated rule.

- Currency: offer contents, pricing, fulfillment, refund terms, and sender guidance can change; the pages direct the reader to current seller/primary requirements.
- Citation: initial raw FTC requests were bot-blocked; later raw first-party HTML and independently opened official pages provide the claim evidence.
- Product evidence: no paid-account testing was conducted while preparing the articles; questions are not presented as proven functionality.
- Financial: costs and placement rates are user assumptions; currency formatting can show a rounded cent value while cost coverage uses the exact fraction. The distinction is stated.
- Release: local candidate only. No push, PR, merge, or deployment occurred. Section 8.9 requires an explicit instruction to publish.

## Distribution draft

Title: Plan a local newsletter around an issue you can repeat

Before choosing newsletter software, write a complete sample issue. Give each event or local update a source and someone responsible for checking it. Record which business items are paid.

Then price the publishing routine. Include the time spent reporting, recurring expenses, and setup costs. Treat a sponsorship price as an assumption until an advertiser has agreed to it.

Bring that issue and budget to a platform demo. Ask the seller to show the work in your plan, including subscriber export and the delivered email.

Full write-up with sources: https://dsotn.com/articles/local-newsletter-launch-plan/

The guide contains a Local Media Empire offer link; we may earn a commission from purchases through it.

Safe-to-post note: draft only, use the URL after publication. Suitable only where useful educational posts with disclosed affiliate content and self-links are permitted. Where links are prohibited, remove the URL; where promotion is prohibited, do not post this affiliate-linked draft. The substance stands alone. Nothing was auto-posted. Author voice audit and independent S1/S2 reviews passed.
