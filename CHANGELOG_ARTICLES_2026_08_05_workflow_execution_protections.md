# Article changelog: workflow execution protections

## Scope and rationale

- Article: `articles/github-actions-workflow-execution-protections/index.html`
- Voice register: research
- Fresh remote base: `5be5872` from `origin/main`
- Carried local baseline: GA4 commit `a09ab84`, cherry-picked as `caef224`
- Reader value: a repository-first rollout for one allow list with actor and event rules, with evaluate-mode checks before activation
- SEO rationale: GitHub announced the exact-match feature on 2026-06-18, the current CI Tripwire catalog had no article for the feature, and the query fits the existing GitHub Actions security cluster without duplicating the `pull_request_target` or token-permissions guides
- SEO confidence: directional. No Google Search Console query data or paid keyword-volume dataset was available for this pass.

The change adds one static article route, a licensed and unique hero photo, PNG and SVG social assets, homepage and article-index cards, sitemap discovery, `llms.txt` discovery, image credit, and a mobile table overflow fix. It also corrects the stale `llms.txt` GitHub Actions count from 52 to the actual 13.

On 2026-08-06, the owner explicitly requested a commit and feature-branch push after the outstanding final fresh-context audit gate was disclosed. On 2026-08-07, after that limitation was repeated, the owner explicitly requested that the branch be pushed and made live. That instruction authorizes the merge and GitHub Pages deployment recorded in the delivery evidence.

## Citation ledger

All sources were opened directly on 2026-08-05. The final register contains 22 official GitHub primary-source entries across 21 underlying documents. GitHub Docs source files and rendered pages were checked where product versioning or interface wording mattered.

| Claim | Cite | Exact support or named source section | Source date | Verdict |
| --- | --- | --- | --- | --- |
| GitHub announced the feature in public preview on 2026-06-18 | 1 | Page date 2026-06-18; phrase: "now in public preview" | Published 2026-06-18; modified 2026-06-23 | Confirmed |
| The feature uses one allow list with actor and event rules | 2 | `About workflow execution protections`; phrase: "define an allow list" | Retrieved 2026-08-05 | Confirmed |
| Actor and event are the first two rule types | 2 | `Available rules`; phrase: "Event and actor" | Retrieved 2026-08-05 | Confirmed |
| GitHub plans more rule types | 2 | `Available rules`; phrase: "add more rules over time" | Retrieved 2026-08-05 | Confirmed |
| Evaluate mode shows blocked outcomes without enforcement | 2 | `Backed by rulesets`; phrase: "without enforcing them" | Retrieved 2026-08-05 | Confirmed |
| Would-be blocked runs surface in policy insights | 5 | `Safe rollout: evaluate mode`; phrase: "surfaced in policy insights" | Updated 2026-03-30 | Confirmed |
| Policies exist at repository, organization, and enterprise levels | 3 | `About Actions policies`; phrase: "enterprise, organization, and repository levels" | Retrieved 2026-08-05 | Confirmed |
| Actions policies currently contain one policy type | 3 | `About Actions policies`; phrase: "one type of policy" | Retrieved 2026-08-05 | Confirmed |
| Workflow execution protections use the rulesets framework | 3 | `About workflow execution protections`; named rulesets paragraph | Retrieved 2026-08-05 | Confirmed |
| The current feature page covers GitHub.com and Enterprise Cloud, not GHES | 9 | Frontmatter lists `fpt` and `ghec`; no `ghes` key | Retrieved 2026-08-05 | Confirmed |
| Actor rules cover users, roles, Apps, Copilot, and Dependabot | 2 | `Available rules`; actor-rule bullet | Retrieved 2026-08-05 | Confirmed |
| Event-rule examples include push, pull request, pull_request_target, and workflow_dispatch | 2 | `Available rules`; event-rule bullet | Retrieved 2026-08-05 | Confirmed |
| Users with write access can trigger workflows by default | 2 | `Available rules`; default-access paragraph | Retrieved 2026-08-05 | Confirmed |
| A compromised allowed identity can still satisfy an identity-based actor rule | 2, 6 | Actor rules control who can trigger; hold announcement names compromised credentials | Retrieved 2026-08-05 | Confirmed inference, labeled in prose |
| Other approval and security gates can hold an actor/event-eligible run | 6, 7 | "holds certain workflow runs"; automation PR runs can enter an "approval-required state" | Published 2026-07-28; retrieved 2026-08-05 | Confirmed |
| GitHub's automatic malicious-workflow hold is limited to public repositories on GitHub.com and excludes GHES | 6 | Scope note states public GitHub.com only and no GHES support | Published 2026-07-28 | Confirmed |
| Job token permissions, environment approvals, and workflow-file review are separate controls | 4 | `GITHUB_TOKEN`, environment reviewers, and CODEOWNERS sections | Retrieved 2026-08-05 | Confirmed |
| Third-party actions should use verified full-length commit SHAs | 4 | Phrase: "full-length commit SHA" | Retrieved 2026-08-05 | Confirmed |
| Untrusted self-hosted work needs isolated, non-reused compute without internal-resource access | 13 | `Self-hosted runners`; named isolation paragraph | Retrieved 2026-08-05 | Confirmed |
| Privileged workflows are at risk when they fetch and execute untrusted code or artifacts | 4 | `Mitigating the risks of untrusted code checkout` and artifact guidance | Retrieved 2026-08-05 | Confirmed |
| GitHub scheduled safer checkout backport enforcement for 2026-07-20; v1 and pinned SHA, minor, and patch references are excluded | 8 | Editor note and `What's changing`; phrase: "aren't affected by the backport" | Updated 2026-07-15 | Confirmed as schedule, not completion |
| `allow-unsafe-pr-checkout: true` opts out of the safer checkout guard | 8, 13 | `Opting out of this protection`; named input | Updated 2026-07-15; retrieved 2026-08-05 | Confirmed |
| Repository setup is under Settings, Actions, Policies | 2 | `Configuring workflow execution protections`; numbered steps | Retrieved 2026-08-05 | Confirmed |
| Central rules can block events without editing each workflow file first | 2 | `About workflow execution protections`; phrase: "each workflow file individually" | Retrieved 2026-08-05 | Confirmed |
| Repository custom properties can target protection scope | 3 | `About workflow execution protections`; custom-property paragraph | Retrieved 2026-08-05 | Confirmed |
| GitHub documents simultaneous aggregation for branch or tag rulesets | 10 | `About rule layering`; branch/tag scope stated in the source | Retrieved 2026-08-05 | Confirmed; not extrapolated to Actions policies |
| Organization audit logs expose Actions-policy violation events and fields | 11 | `workflows.actions_policy_violation`; fields `allowed`, `event_name`, `ruleset_ids`, `violations` | Retrieved 2026-08-05 | Confirmed |
| Organization audit logs can be opened from organization settings | 16 | `Accessing the audit log`; numbered navigation | Retrieved 2026-08-05 | Confirmed |
| Authorized repository users and Apps can update custom-property values when enabled | 12 | `Managing custom properties`; named repository-actor paragraph | Retrieved 2026-08-05 | Confirmed |
| Environment approvals gate jobs that reference that environment | 14 | `Required reviewers`; protected-environment job scope | Retrieved 2026-08-05 | Confirmed |
| CODEOWNERS approval protects pull-request merges when enforcement is configured | 15 | `CODEOWNERS and branch protection`; merge-approval scope | Retrieved 2026-08-05 | Confirmed |
| Direct untrusted expressions in scripts should move through action inputs or intermediate environment variables | 4 | `Use an action instead of an inline script` and intermediate-variable guidance | Retrieved 2026-08-05 | Confirmed |
| Rulesets can be saved active or in evaluate mode | 2 | `Configuring workflow execution protections`; final numbered step | Retrieved 2026-08-05 | Confirmed |
| Repository and organization policy setup is under Actions, Policies | 2, 17 | Both configuration sections; numbered navigation | Retrieved 2026-08-05 | Confirmed |
| Only organization owners can access the organization audit log | 16 | `Accessing the audit log`; access note | Retrieved 2026-08-05 | Confirmed |
| Policy-violation audit entries lack a workflow-run ID and must be correlated by available fields | 11 | Complete `workflows.actions_policy_violation` field list | Retrieved 2026-08-05 | Confirmed |
| Checkout alone is not execution and untrusted data can arrive outside actions/checkout | 13 | `The risks` and `Opting out`; exact boundary and non-checkout examples | Retrieved 2026-08-05 | Confirmed |
| Custom-property changes have organization or GitHub App webhook coverage and an organization-scoped paginated REST endpoint | 18, 19 | Event availability lists repositories, organizations, and GitHub Apps; `GET /orgs/{org}/properties/values`; `per_page` maximum 100 and default 30 | Retrieved 2026-08-05 | Confirmed |
| Actor and event canaries must isolate the configured rule dimensions and denied organization-owned canaries need a matching audit event | 2, 11 | Actor and event are independent rules; `workflows.actions_policy_violation` fields identify repository, actor, event, and ruleset | Retrieved 2026-08-05 | Confirmed operational inference |
| The feature is still public preview and subject to change | 3 | Page note; phrase: "subject to change" | Retrieved 2026-08-05 | Confirmed |
| Scheduled-workflow actors change after default-branch changes and after a write user reactivates a deactivated cron schedule; EMU deprovisioning can stop a schedule | 20 | `actor for scheduled workflows`; qualified default-branch, reactivation, and deprovisioned-actor paragraphs | Retrieved 2026-08-05 | Confirmed |
| Enterprise configuration is under Policies, Actions, Policies | 21 | `Configuring workflow execution protections`; ordered navigation steps | Retrieved 2026-08-05 | Confirmed |
| Enterprise audit logs aggregate actions from organizations owned by the enterprise | 22 | `About the audit log for your enterprise`; aggregation sentence | Retrieved 2026-08-05 | Confirmed |

## Consolidated findings ledger

| ID | Sev | Axis | Location | Finding | Corroborated by | Verified by orchestrator | Bucket |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SELF-01 | LOW | mobile layout | shared `styles.css` mobile rules | A four-column table widened the mobile grid beyond the article viewport | rendered 390px QA | CDP measured the initial overflow and the fixed page at `scrollWidth=390`, `innerWidth=390` | Should fix now, fixed |
| R1-01 | HIGH | enforcement boundary | summary and distribution copy | Draft treated execution protections as the sole decision before a run starts | H4, X1 | Confirmed against GitHub's 2026-07-28 hold and trigger-approval docs | Must fix, fixed |
| R1-02 | MEDIUM | feature model | summary, takeaways, rollout | Draft alternated between two allow lists and an Actions-wide ruleset implementation | H1, C3, C5, X2 | GitHub documents one allow list, two rule types, and ruleset backing for workflow execution protections | Must fix, fixed |
| R1-03 | MEDIUM | citation binding | summary, table, event and actor sections | Several load-bearing product and security claims lacked at-point citations | H1, H2, C1, C4, C5, X2 | Confirmed by claim-to-source remap | Must fix, fixed |
| R1-04 | MEDIUM | threat boundaries | event and actor sections | Draft omitted compromised allowed identities, runner isolation, and non-checkout untrusted inputs | H4 | Confirmed against current GitHub security guidance | Must fix, fixed |
| R1-05 | MEDIUM | evaluate operations | evaluate-mode section | Draft did not name policy insights or disclose the missing documented navigation path | H2, X1 | Confirmed against GitHub's roadmap and setup page | Must fix, fixed |
| R1-06 | MEDIUM | currency and availability | key takeaways and event section | Draft omitted GHES scope and the July checkout backport behavior | X1 | Confirmed against GitHub Docs frontmatter and changelog | Must fix, fixed |
| R1-07 | MEDIUM | ruleset overlap | rollout | Draft promoted scope without reconciling rulesets that can apply together | X1 | Confirmed against GitHub ruleset layering docs | Must fix, fixed |
| R1-08 | MEDIUM | metadata | JSON-LD, byline, homepage | Word count and read time were not based on a reproducible rendered-text count | H5, C5, S2, X2 | Recounted with `xmllint` over visible `<article>` text | Must fix, fixed |
| R1-09 | MEDIUM | voice and title | title, summary, rollout | Headline case and two abstract or anthropomorphic phrases violated the register | S1, S2 | Confirmed against the style rules | Must fix, fixed |
| R1-10 | MEDIUM | accessibility and discovery | shared CSS and articles index | Light-surface eyebrow contrast failed and `/articles/` lacked ItemList data | X2 | Contrast and index markup checked locally | Must fix, fixed |
| R1-11 | LOW | navigation and semantics | table and `llms.txt` | Table lacked a name and `llms.txt` omitted the article index | X2 | Confirmed in local markup | Should fix now, fixed |
| R2-01 | MEDIUM | operations | evaluate and activation sections | Policy-insights review lacked the documented organization audit-log fallback and post-activation rollback checks | H2 | Confirmed against audit-log and protection docs | Must fix, fixed |
| R2-02 | MEDIUM | dynamic scope | rollout and activation | Custom-property targeting lacked ownership, mutability, and scope-drift controls | H2 | Confirmed against custom-property docs | Must fix, fixed |
| R2-03 | MEDIUM | unsupported extrapolation | rollout | Branch/tag ruleset aggregation was applied to undocumented Actions-policy overlap behavior | H1, C5, X1 | Source scope confirmed; extrapolation removed | Must fix, fixed |
| R2-04 | MEDIUM | citation precision | summary, actor rules, checkout note | Draft asserted gate ordering, a negative actor-rule boundary, and completed backport deployment without direct proof | C2, C5 | Claims narrowed to documented positive behavior or schedule | Must fix, fixed |
| R2-05 | MEDIUM | security boundaries | event, actor, and activation sections | Draft under-specified CODEOWNERS, environment, runner, unsafe-checkout, and script-interpolation limits | H3, H4 | Confirmed against five current GitHub security sources | Must fix, fixed |
| R2-06 | MEDIUM | plagiarism and labels | rollout and trust block | One exact eight-word source run and two misleading source/byline labels remained | S2, X1 | Phrase paraphrased; labels corrected | Must fix, fixed |
| R2-07 | MEDIUM | mobile and count method | shared mobile CSS and Pass 5 | Desktop TOC preceded the mobile H1; count scope and jump-list evidence were inconsistent | H5, S1, X2 | Mobile TOC hidden; body count method documented; jump list added after body expansion | Must fix, fixed |
| R2-08 | LOW | asset parity | SVG fallback | SVG title and visible text retained headline case | H5, X2 | Matched to canonical sentence-case title | Should fix now, fixed |
| R3-01 | HIGH | rollback oracle | activation review | An already allowed canary could not prove that enforcement was removed | H1, H4 | Test outcome was identical before and after rollback | Must fix, fixed |
| R3-02 | MEDIUM | audit-log access | evaluate mode | Audit fallback omitted owner-only access, repository filtering, and run-correlation limits | H2, X1, X2 | Confirmed against access and event-field docs | Must fix, fixed |
| R3-03 | MEDIUM | activation coverage | activation review | One blocked canary did not independently test actor and event rules | H2 | Confirmed against two independent rule dimensions | Must fix, fixed |
| R3-04 | MEDIUM | citation binding | evaluate, event, actor, rollout | Four claims used adjacent sources or negative phrasing beyond what the cited page established | C2, C5, X2 | Claims re-bound, narrowed, or removed | Must fix, fixed |
| R3-05 | MEDIUM | checkout currency | event rules | An expired schedule did not give a current, verified rollout state | X1 | Article now states what the changelog proves and requires exact-ref inspection | Must fix, fixed |
| R3-06 | MEDIUM | scope-drift operations | rollout | Custom-property monitoring lacked a change signal and reconciliation method | X1 | Added official webhook and REST endpoint | Must fix, fixed |
| R3-07 | LOW | image metadata | PNG social asset | Embedded XMP height said 640 while IHDR and decoders said 630 | H5 | Re-encoded PNG; XMP and IHDR now both say 630 | Should fix now, fixed |
| R4-01 | MEDIUM | observability claim | activation review | Draft promised that each violation names the expected rule without a source defining that output | H1, H4, C2 | GitHub documents denied execution, not a human-readable named-rule result | Must fix, fixed |
| R4-02 | MEDIUM | citation binding | summary, event rules, actor rules | Supported security controls and checkout facts used trailing or pooled citation markers | C4, C5 | Reopened sources 4, 8, 13, and 14; markers now bind each independent clause | Must fix, fixed |
| R4-03 | MEDIUM | citation binding | evaluate mode and rollout | Audit-log and custom-property claims used paragraph-end citation clusters | C5 | Reopened sources 11, 12, 16, 18, and 19; markers now bind their exact clauses | Must fix, fixed |
| R4-04 | MEDIUM | operational completeness | actor rules | Rollout omitted scheduled-workflow actor changes and EMU deprovisioning behavior | X1 | Confirmed against current events-that-trigger-workflows documentation | Must fix, fixed |
| R4-05 | MEDIUM | scope reconciliation | rollout | REST reconciliation omitted pagination and could inspect only the default first 30 results | X2 | Current endpoint documents default 30 and maximum 100 results per page | Must fix, fixed |
| R4-06 | LOW | enterprise navigation | rollout | Enterprise promotion lacked its documented settings path | X1 | Added Policies, Actions, Policies with source 21 | Should fix now, fixed |
| R4-07 | LOW | crawler contract | `robots.txt` | FriendlyCrawler was allowed by wildcard but absent from the explicit required list | X2 | Added explicit allow block | Should fix now, fixed |
| R5-01 | MEDIUM | canary correctness | activation review | Denied canaries did not isolate actor and event dimensions or require positive policy evidence | H2, C2, X1 | Reworked tests to vary one rule dimension and require a matching organization audit event | Must fix, fixed |
| R5-02 | MEDIUM | enterprise scope monitoring | rollout | One organization webhook and REST enumeration could not cover an enterprise policy | H2, X1 | Source availability is organization/App scoped; instructions now cover every targeted organization separately | Must fix, fixed |
| R5-03 | LOW | rollback precision | activation review | Rollback path did not name the operator action or resulting ruleset state | H2 | Current setup docs support saving the ruleset in evaluate mode; owner and state change are explicit | Should fix now, fixed |
| R5-04 | MEDIUM | crawler exclusions | `robots.txt` | Named crawler groups did not repeat the wildcard `/.git/` exclusion | H5, X2 | RFC group matching and the repository contract require the exclusion in each named group | Must fix, fixed |
| R5-05 | MEDIUM | scheduled actor scope | actor rules | Cron-based actor reassignment was generalized beyond deactivated-schedule reactivation | C3, C5, X1, X2 | Current GitHub source states the narrower write-user reactivation condition | Must fix, fixed |
| R5-06 | MEDIUM | source precision | actor rules | Runner guidance added the unsupported adjective "clean" | C4 | Source supports restricted, non-reused isolation; unsupported adjective removed | Must fix, fixed |
| R5-07 | MEDIUM | citation binding | article summary | Two product-mechanics sentences lacked point-of-claim source 2 markers | C5 | Markers now touch both independent clauses | Must fix, fixed |
| R5-08 | LOW | scanability | bottom-line callout | Supporting control distinctions expanded the callout to six sentences | S2 | Callout restored to two sentences; supporting facts moved below | Should fix now, fixed |
| R5-09 | MEDIUM | platform scope | article summary | Automatic malicious-workflow hold omitted public GitHub.com-only and GHES-excluded scope | X1 | Current hold announcement states both boundaries | Must fix, fixed |
| R5-10 | LOW | enterprise auditability | evaluate mode | Enterprise promotion lacked its corresponding aggregate audit-log path | X1 | Added enterprise audit-log path with source 22 | Should fix now, fixed |

## Writer self-audit

### Pass 1: source and content

- Primary-source posture: PASS. All 22 entries are GitHub-owned docs, docs source, blog, or changelog pages and represent 21 underlying documents.
- Claim-to-source binding: PASS after Round 5 corrections. Forty-three load-bearing claim rows appear in the ledger.
- Search URLs: PASS. None used.
- Product coherence: PASS. The article gives a bounded rollout and preserves workflow-level review controls.

### Pass 2: numeric and acronym

- Dates: PASS. The 2026-06-18 announcement date matches the official changelog record.
- Counts: PASS. One allow list, two current rule types, 22 reference entries across 21 documents, 13 GitHub Actions articles, and 18 total article routes were re-counted.
- Acronyms and code terms: PASS. GitHub Actions, CI, JSON-LD, GA4, and event names are used consistently.

### Pass 3: tone and style

- Research register held: PASS.
- Anti-AI denylist: PASS after an exact phrase sweep and line-by-line read.
- Banned characters: PASS. No em dash, en dash, or curly quote in the article or distribution draft.
- Community narration: PASS. None.

#### Pass 4: voice consistency end-to-end

- Opening sample (title, summary, first paragraph): PASS. Sentence-case feature identity and direct rollout payoff.
- Middle samples (`two-rules`, `event-rules`, `actor-rules`): PASS. Same research register and concrete nouns.
- Closing sample (`activation-review`): PASS. Ends on current preview status and related implementation reviews.
- Anti-AI voice audit (section 3.3 denylist): PASS. No denylist hit remained.

#### Pass 5: scanability and trust signals

- Mobile scan path: PASS. Key takeaways and the second section answer the headline.
- Longest paragraph word count: 82 from rendered `innerText`.
- Bottom-line callout in reader-payoff section: YES.
- Comparison data as list or table rows: YES, one semantic four-column table.
- Ranked verdicts in evidence or caution callouts: not comparison-shaped.
- Self-describing headings: PASS.
- Three-place coverage for headline statistics: not applicable; the headline carries no statistic.
- Body word count: 1,769 from rendered `innerText` for `#editorial-summary` plus content sections before `#references`; reading time: 9 minutes at approximately 200 wpm; jump list: PRESENT.
- Closing trust signals: PASS. Disclaimer once, honesty line, contributor and sourcing links, corrections pointer, citation-density line.
- Key-takeaways cite density: 6 of 6 factual bullets cited.

#### Pass 6: integrity and digestibility triple-audit

- Hallucination pass 1: 43 ledger rows checked after corrections, 0 failed.
- Hallucination pass 2: 43 rows checked from the source sections, 0 failed.
- Hallucination pass 3: 43 rows and citation metadata rechecked, 0 failed.
- Citations independently confirmed (URL, title, publisher, date, finding): PASS.
- Per-citation ledger: 43 rows, all confirmed or explicitly scoped as inference or schedule.
- Plagiarism (no unattributed runs of roughly 8 words): PASS.
- Top-summary digestibility: PASS.
- Quality-degrading repetition: PASS.

## Independent adversarial audit

Each round used a frozen draft. Counts below are raw auditor findings and therefore include corroborating duplicates. Round 1 and Round 3 HIGH fixes require complete fresh-context reruns. Round 2 had no HIGH finding, but its MEDIUM fixes touched several sections, so the complete stack also reran after that round. Round 5 completed all 14 roles, but an agent-thread cap forced reuse of isolated read-only auditor threads for C4 through X2. Because the fixes after Round 5 did not receive a complete fresh-context round, this candidate is not release-ready under the repository contract.

| Round | HIGH | MEDIUM | LOW | Outcome |
| --- | --- | --- | --- | --- |
| 1 | 2 | 28 | 13 | Failed; findings deduplicated, adjudicated, and fixed |
| 2 | 0 | 16 | 11 | Failed; findings deduplicated, adjudicated, and fixed |
| 3 | 1 | 13 | 1 | Failed; findings deduplicated, adjudicated, and fixed |
| 4 | 0 | 13 | 2 | Failed; findings deduplicated, adjudicated, and fixed |
| 5 | 0 | 15 | 3 | Failed; findings deduplicated, adjudicated, and fixed |

### Round 1 auditor verdicts

| Auditor | Coverage | Verdict |
| --- | --- | --- |
| H1 feature mechanics | 31 claims, 3 sources, 3 findings | FINDINGS, H0 M2 L1 |
| H2 configuration and rollout | 43 claims, 10 sources, 2 findings | FINDINGS, H0 M1 L1 |
| H3 currency | 25 claims, 4 sources, 0 findings | CLEAN |
| H4 security risks and mitigations | 36 claims, 12 sources, 5 findings | FINDINGS, H1 M3 L1 |
| H5 dates, counts, and three-place consistency | 42 claims, 4 sources, 1 finding | FINDINGS, H0 M1 L0 |
| C1 announcement source | 5 claims, 1 source, 1 finding | FINDINGS, H0 M1 L0 |
| C2 protection docs | 24 claims, 1 source, 0 findings | CLEAN |
| C3 Actions policy docs | 8 claims, 1 source, 2 findings | FINDINGS, H0 M2 L0 |
| C4 secure-use source | 9 claims, 2 sources, 2 findings | FINDINGS, H0 M2 L0 |
| C5 citation set | 39 claims, 5 sources, 7 findings | FINDINGS, H0 M6 L1 |
| S1 anti-AI voice and product value | 9 sections, 12 rule groups, 3 findings | FINDINGS, H0 M2 L1 |
| S2 voice, trust, and plagiarism | 9 sections, 4 sources, 4 findings | FINDINGS, H0 M0 L4 |
| X1 breadth and currency | 27 areas, 17 sources, 5 findings | FINDINGS, H1 M4 L0 |
| X2 whole deliverable | 16 files, 9 sources, 8 findings | FINDINGS, H0 M4 L4 |

### Round 2 auditor verdicts

| Auditor | Coverage | Verdict |
| --- | --- | --- |
| H1 feature mechanics | 43 claims, 17 sources, 1 finding | FINDINGS, H0 M1 L0 |
| H2 configuration and rollout | 36 claims, 18 sources, 3 findings | FINDINGS, H0 M3 L0 |
| H3 currency | 41 claims, 12 sources, 1 finding | FINDINGS, H0 M0 L1 |
| H4 security risks and mitigations | 47 claims, 21 sources, 5 findings | FINDINGS, H0 M4 L1 |
| H5 dates, counts, and three-place consistency | 61 claims, 10 sources, 3 findings | FINDINGS, H0 M0 L3 |
| C1 announcement source | 11 claims, 1 source, 0 findings | CLEAN |
| C2 protection docs | 15 claims, 1 source, 1 finding | FINDINGS, H0 M1 L0 |
| C3 Actions policy docs | 8 claims, 1 source, 0 findings | CLEAN |
| C4 secure-use source | 25 claims, 8 sources, 0 findings | CLEAN |
| C5 citation set | 54 claims, 10 sources, 4 findings | FINDINGS, H0 M3 L1 |
| S1 anti-AI voice and product value | 10 sections, 13 rule groups, 1 finding | FINDINGS, H0 M0 L1 |
| S2 voice, trust, and plagiarism | 9 sections, 10 sources, 3 findings | FINDINGS, H0 M1 L2 |
| X1 breadth and currency | 40 areas, 20 sources, 2 findings | FINDINGS, H0 M1 L1 |
| X2 whole deliverable | 12 files, 10 sources, 3 findings | FINDINGS, H0 M2 L1 |

### Round 3 auditor verdicts

| Auditor | Coverage | Verdict |
| --- | --- | --- |
| H1 feature mechanics | 40 claims, 16 sources, 1 finding | FINDINGS, H1 M0 L0 |
| H2 configuration and rollout | 36 claims, 20 sources, 2 findings | FINDINGS, H0 M2 L0 |
| H3 currency | 29 claims, 23 sources, 0 findings | CLEAN |
| H4 security risks and mitigations | 46 claims, 12 sources, 1 finding | FINDINGS, H0 M1 L0 |
| H5 dates, counts, and three-place consistency | 61 claims, 11 sources, 1 finding | FINDINGS, H0 M0 L1 |
| C1 announcement source | 6 claims, 1 source, 0 findings | CLEAN |
| C2 protection docs | 16 claims, 4 sources, 1 finding | FINDINGS, H0 M1 L0 |
| C3 Actions policy, version, and ruleset docs | 13 claims across 6 uses, 3 sources, 0 findings | CLEAN |
| C4 security source set | 8 claims, 4 sources, 0 findings | CLEAN |
| C5 citation set | 54 claims, 17 sources, 4 findings | FINDINGS, H0 M4 L0 |
| S1 anti-AI voice and product value | 111 units, 0 findings | CLEAN |
| S2 voice, trust, and plagiarism | 80 claims, 16 sources, 0 findings | CLEAN |
| X1 breadth and currency | 41 areas, 14 sources, 3 findings | FINDINGS, H0 M3 L0 |
| X2 whole deliverable | 36 claims, 17 sources, 2 findings | FINDINGS, H0 M2 L0 |

### Round 4 auditor verdicts

| Auditor | Coverage | Verdict |
| --- | --- | --- |
| H1 feature mechanics | 31 claims, 9 sources, 1 finding | FINDINGS, H0 M1 L0 |
| H2 configuration and rollout | 46 claims, 13 sources, 0 findings | CLEAN |
| H3 currency | 18 claims, 10 sources, 0 findings | CLEAN |
| H4 security risks and mitigations | 28 claims, 9 sources, 1 finding | FINDINGS, H0 M1 L0 |
| H5 dates, counts, and three-place consistency | 61 claims, 11 sources, 0 findings | CLEAN |
| C1 announcement source | 2 claims, 1 source, 0 findings | CLEAN |
| C2 protection docs | 36 claims, 2 sources, 1 finding | FINDINGS, H0 M1 L0 |
| C3 Actions policy, version, and ruleset docs | 16 claims, 3 sources, 0 findings | CLEAN |
| C4 security source set | 26 claims, 4 sources, 4 findings | FINDINGS, H0 M4 L0 |
| C5 citation set | 43 claims, 19 sources, 4 findings | FINDINGS, H0 M4 L0 |
| S1 anti-AI voice and product value | 111 units, 0 findings | CLEAN |
| S2 voice, trust, and plagiarism | 82 claims, 19 sources, 0 findings | CLEAN |
| X1 breadth and currency | 51 claims, 16 sources, 2 findings | FINDINGS, H0 M1 L1 |
| X2 whole deliverable | 41 claims, 19 sources, 2 findings | FINDINGS, H0 M1 L1 |

### Round 5 auditor verdicts

| Auditor | Coverage | Verdict |
| --- | --- | --- |
| H1 feature mechanics | 36 claims, 8 sources, 0 findings | CLEAN |
| H2 configuration and rollout | 29 claims, 12 sources, 3 findings | FINDINGS, H0 M2 L1 |
| H3 currency | 32 claims, 20 sources, 0 findings | CLEAN |
| H4 security risks and mitigations | 28 claims, 9 sources, 0 findings | CLEAN |
| H5 dates, counts, and three-place consistency | 41 claims, 11 sources, 1 finding | FINDINGS, H0 M1 L0 |
| C1 announcement source | 2 claims, 1 source, 0 findings | CLEAN |
| C2 protection docs | 28 claims, 2 sources, 1 finding | FINDINGS, H0 M1 L0 |
| C3 policy, ruleset, schedule, and enterprise docs | 15 claims, 5 sources, 1 finding | FINDINGS, H0 M1 L0 |
| C4 security source set | 15 claims, 5 sources, 1 finding | FINDINGS, H0 M1 L0 |
| C5 citation set | 49 claims, 21 sources, 3 findings | FINDINGS, H0 M3 L0 |
| S1 anti-AI voice and product value | 182 units, 0 findings | CLEAN |
| S2 voice, trust, and plagiarism | 83 claims, 21 sources, 1 finding | FINDINGS, H0 M0 L1 |
| X1 breadth and currency | 43 claims, 24 sources, 5 findings | FINDINGS, H0 M4 L1 |
| X2 whole deliverable | 74 claims, 22 sources, 2 findings | FINDINGS, H0 M2 L0 |

## Gates and manual QA

- `git diff --check`: PASS.
- JSON-LD parse, two blocks: PASS.
- `sitemap.xml` and SVG XML parse: PASS.
- Canonical, title, robots, OpenGraph, Twitter, and article metadata checks: PASS.
- All 22 visible source URLs: HTTP 200 on 2026-08-05; all 22 marker targets resolve and are used.
- Named AI-crawler parity: 22 required groups, each with `Allow: /` and `Disallow: /.git/`.
- Article route, hero image, and PNG social image through local HTTP server: HTTP 200.
- Article discovery parity: 18 article routes, 18 article-index cards, 18 homepage ItemList entries, 18 homepage cards, 18 sitemap article URLs, 13 GitHub Actions links plus 5 Stripe links in `llms.txt`.
- Hero dimensions: 1600 by 900 JPEG. PNG social image: 1200 by 630.
- Desktop render at 1440px: PASS with `scrollWidth=1440`, `innerWidth=1440`, and the table of contents visible.
- Mobile render at 390px: PASS after the shared table overflow fix and removal of the desktop TOC from the mobile flow. CDP measured `scrollWidth=390`, `innerWidth=390`, the H1 beginning at 434px, and a two-sentence Bottom line callout.
- Full test, lint, and build commands: not available. This repository is static HTML with no package manifest or test runner.

## Delivery evidence

- Feature branch: `feat/workflow-execution-protections-article`, pushed at `60b784a547c08af9a79ff6e5e0d3dbfae14e3fec`.
- Pull request: `https://github.com/agentlaunchops-ai/ci-tripwire/pull/1`, merged 2026-08-07.
- Initial `main` merge commit: `ac3d465fa6dafb192991204b43b48d4265cc13e9`.
- GitHub Pages build: `built` for the initial merge commit at 2026-08-07T13:32:30Z.
- Live URL: `https://dsotn.com/articles/github-actions-workflow-execution-protections/`, HTTP 200 with the committed title, canonical URL, 22 visible sources, 22 JSON-LD citation entries, GA4, and Plausible.
- Live asset checks: hero JPEG, social PNG, and social SVG each returned HTTP 200.

## Known limitations and residual risk

- Workflow execution protections remain in public preview and can change after this review date.
- Search opportunity is based on catalog gap, recency, exact-match result shape, and source readiness. It is not backed by Search Console impressions or a paid volume estimate.
- The Pexels source page returned HTTP 403 to `curl`; it loaded in browser-based research, identified Ibrahim Boran and the Pexels License, and its direct image asset downloaded successfully.
- Local rendering proves the static candidate, not production deployment or indexing.
- A complete fresh-context adversarial round after the Round 5 fixes remains unrun because the session reached its auditor-thread limit. The article must not be described as verified or release-ready until that round reaches 0 HIGH and 0 MEDIUM.
- Owner-directed exception: commit and push the feature branch on 2026-08-06, then merge and deploy it on 2026-08-07 while preserving the release-readiness limitation above.
- Affiliate opportunity: none.

## Distribution draft

**Safe-to-post note:** suitable for developer or DevOps communities that allow sourced educational self-links. Remove the URL where external links or brand accounts are restricted; the post still carries the full practical point.

### GitHub Actions can now block disallowed workflow triggers

GitHub put workflow execution protections into public preview. The policy adds one allow list with two rule types:

- Actor rules cover users, repository roles, GitHub Apps, Copilot, and Dependabot.
- Event rules cover trigger types such as `push`, `pull_request`, `pull_request_target`, and `workflow_dispatch`.

Start with one repository in evaluate mode. Review would-be blocked runs in policy insights, then exercise pull requests, releases, dependency automation, and manual maintenance before activation. A human-only actor rule can break bot and App workflows, while a broad event rule leaves the risky trigger surface unchanged.

The policy decides whether an actor and event pass this gate. On public repositories at GitHub.com, separate GitHub features also hold certain runs before execution; that automatic hold is not available on GitHub Enterprise Server. Keep least-privilege `GITHUB_TOKEN` settings, approvals for jobs that reference protected environments, full-SHA action pinning, workflow-file review, and runner isolation in place.

Full write-up with sources: https://dsotn.com/articles/github-actions-workflow-execution-protections/
