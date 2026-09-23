# Article changelog: pull-request-target-november-2

Voice register: research.

Base commit: `d0f1aef2bde6a645c9e5eb9fa52a2856fb5efd9c` (`origin/main` at branch cut).

## What changed and why

New article, `articles/pull-request-target-november-2/index.html`, published 2026-09-23.

The catalog already had a workflow execution protections setup guide (as of August 5, 2026, while the feature was in public preview) and separate guides for `pull_request_target` and SHA pinning. It did not have the September 17, 2026 general-availability note or the November 2, 2026 enforcement date for the default public-repository `pull_request_target` rule.

Reader payoff: enforcement on November 2, 2026 is for repositories that were using the default `pull_request_target` policy before general availability. The default is in evaluate mode until then, so runs still start. It is added on public repositories that do not yet have an applicable Actions event policy. Private and internal repositories are outside it. An applicable event policy already in place is not replaced. Full SHA pins, minor tags, and patch tags were outside the checkout backport. `actions/checkout` v1 is excluded. The July 20, 2026 backport date is the revised schedule. The changelog page retrieved September 23, 2026 has no later note that the backport finished.

## Follow-up, not fixed here

The August 5, 2026 workflow execution protections article still says Actions policies were in public preview as of that date. The September 17, 2026 changelog says they are generally available. That older sentence was true on August 5 and is stale now. Flagged, not rewritten in this change.

## Per-citation ledger

Retrieved 2026-09-23 unless noted.

| Claim | Cite | Supporting quote | Source date | Verdict |
| --- | --- | --- | --- | --- |
| Enforcement date and cohort | [1] | "On November 2, 2026, GitHub will enforce the default policy for affected repositories that were using the default pull_request_target policy before general availability." | Docs page live 2026-09-23 | Confirmed, quoted in the article |
| Default added on public repos with no applicable event policy; private and internal out; applicable policy not replaced; evaluate mode, runs continue | [1] | "For public repositories that do not already have an applicable Actions event policy, GitHub adds a default policy that blocks workflows triggered by pull_request_target." "Does not apply to private or internal repositories." "Does not replace an applicable event policy that you have already configured." "Currently runs in evaluate mode. In this mode, workflow runs continue" | Docs page live 2026-09-23 | Confirmed |
| Short public-repo line and November 2 date, with a link to the guide | [4] | "GitHub has added a default policy that will block the pull_request_target event in public repositories. This policy will be enforced on November 2, 2026. See Securely using pull_request_target." | Docs page live 2026-09-23 | Confirmed. Article says "will block," not that the block is already on |
| GA scope and the three additions | [2] | "now generally available for GitHub Enterprise, organizations, and repositories." Workflow file targeting, Insights, REST API create/read/update/delete including workflow path conditions | Changelog published 2026-09-17 | Confirmed, availability line quoted |
| Checkout date move, v1 exclusion, pin split, July 16 sentence still in the body | [3] | Editor's note July 15, 2026 moves enforcement from July 16, 2026 to Monday, July 20, 2026, and says v1 will not receive the change. Body still says "On July 16, 2026, we'll backport" and that a specific SHA, minor, or patch version is not affected | Post published 2026-06-18, modified 2026-07-15, retrieved 2026-09-23 | Confirmed. No later completion note on that page |
| Fork code not executed by default; checkout alone does not execute; later step does | [1] | "No code from the fork is executed by default." "The checkout step alone does not execute untrusted code." | Docs page live 2026-09-23 | Confirmed after round-2 and round-3 fixes |
| Default-branch cache access, and read-only unless a write-capable cache mode is declared | [3] and [1] | Checkout changelog: "default-branch cache access." Guide: read-only unless a write-capable cache mode is declared | Retrieved 2026-09-23 | Confirmed in the post-round-3 edit |
| Hero | CREDITS.md | Commons File:Rail_road_crossing_Yankton_2013.jpg, Peterupton99, CC0, "A railroad crossing in Yankton South Dakota in 2013" | Retrieved 2026-09-23 | Confirmed |

## Adjudicated findings

Round 1 (14 auditors) found a HIGH: a no-`ref` checkout was described as if it were the only way fork code runs. Fixed by naming a later executing step, a fork `repository` input, and a fetch outside `actions/checkout`.

Round 2 (14 auditors) found HIGHs in that fix: the colon treated checkout and fetch as the executing step, and "neither ref nor a fork repository" was too wide. Fixed by separating "checkout by itself does not run that code" from the later executing step.

Round 3 (12 auditors) found a HIGH: "Any other repository value checks out that other repository" is false, because a `repository` value that resolves to the fork is refused. Fixed by cutting that universal and keeping only the unrelated third-party case, which the June 18 changelog states is not blocked.

MEDIUMs fixed in the same passes included: "for the conditions" gloss, "second condition" weld, "stays blocked" while evaluate mode is still on, "pre-availability" shortened past "general," decision bullets that dropped "update the workflow," and an unquoted cohort clause in JSON-LD `articleBody`.

A full round after the round-3 HIGH fix has not been run. This piece is not at 0 HIGH and 0 MEDIUM on a post-fix round.

After that commit, the citation auditor (still running on the round-3 text) reported two MEDIUMs. Both were fixed in a follow-up commit:

- "only where a workflow still depends on this trigger" was rewritten to "if workflows still depend on this trigger," matching the changelog's choice condition rather than a product limit on which workflows an allow can cover.
- The SHA-pin sentences in the checkout section were cited to the checkout changelog [3]. The November 2 sentences in that paragraph stay on [1].
- The enforcement quote now includes the source word "affected."
- The default-branch checkout sentence no longer adds "and no repository," which the guide does not say. The third-party repository sentence is cited only to [3].

| Round | HIGH | MEDIUM | LOW | Outcome |
| --- | --- | --- | --- | --- |
| 1 | 1 | several | several | HIGH fixed, full re-run required |
| 2 | 2 | several | several | HIGH fixed, full re-run required |
| 3 | 1 | several | several | HIGH and the MEDIUMs above fixed after the round |
| 4 | not run | not run | not run | Outstanding |

## Pass 4: voice consistency end-to-end

- Opening sample (title / TL;DR / first paragraph): PASS. Research register, enforcement date in the first clause.
- Middle samples (`general-availability`, `who-is-covered`, `checkout-pins`): PASS after the cohort and checkout edits.
- Closing sample: PASS. Trust block, no bow.
- Anti-AI voice audit (section 3.3 denylist): PASS. No em dash, en dash, or curly quotes.

## Pass 5: scanability and trust signals

- Mobile scan path (takeaways + section 2 answer the headline): PASS
- Longest paragraph word count: under 120 after the last split
- Bottom-line callout in reader-payoff section: YES
- Comparison data as list/table rows: YES
- Ranked verdicts in evidence/caution callouts: YES
- Self-describing headings: PASS
- Three-place coverage for load-bearing stats: PASS for the November 2 quote, the September 17 quote, and the July 15/16/20 sentence
- Body word count: about 2070; jump list at 1,400+: PRESENT
- Closing trust signals: PASS. Disclaimer once. Honesty line. Contributors and sourcing links. Corrections link. "Sources: 4 entries, all primary GitHub documentation, last reviewed 2026-09-23."
- Key-takeaways cite-density: 6 of 6

## Pass 6: integrity and digestibility triple-audit (mandatory)

- Hallucination pass 1: load-bearing dates and cohort checked against the four GitHub pages, 0 left unfixed
- Hallucination pass 2: checkout refusal and evaluate mode rechecked, the "any other repository" universal failed and was cut
- Hallucination pass 3: decision list and cache read-only qualifier rechecked after the cut
- Citations independently confirmed: PASS for the four URLs (HTTP 200 on 2026-09-23)
- Per-citation ledger: rows above, confirmed
- Plagiarism: the visible cohort clause is quoted. JSON-LD `articleBody` was paraphrased after an unquoted 11-word run was found
- Top-summary digestibility: PASS
- Quality-degrading repetition: the identical November 2 sentence is in the takeaway, the bottom line, and the body. Table cells were shortened so they do not paste it a fourth time

## Gates

No `package.json`. `npm run lint`, `npm run build`, and `npm test` were not run because this repository has no npm project. Residual risk: no automated test suite covers this HTML.

Banned-character scan of the article file returned nothing.

Source URLs returned HTTP 200 on 2026-09-23.

Manual QA: anchors in the article resolve, the disclaimer string appears once, hero is 1600x900, OG card is 1200x630. A browser pass at 390px was not run. Tables use the existing overflow rule under 820px. That is the unverified part.

## Known limitations

- "Affected repositories" in GitHub's November 2 sentence is not defined beyond the quoted clause. The article does not invent a rule for a repository that was on the default before general availability and later added an applicable policy.
- The checkout backport page does not say the July 20, 2026 enforcement finished.

## Residual risk

- Currency: a changelog after 2026-09-23 can move November 2. The article says to recheck.
- Citation: the read-only cache sentence was added from the guide after round 3. It was not in a later full round.
- Voice: research register held in the audited rounds. Later edits were small and were not re-graded by a fresh voice panel.

## Affiliate opportunities

None.

## Distribution draft

Safe for an engineering community that allows a technical writeup. Many communities ban promotion and external links. If the rules forbid a link, post the substance and drop the URL. Do not post this from an obvious brand account into a community that treats that as spam.

---

On November 2, 2026, GitHub will enforce a default pull_request_target block for repositories that "were using the default pull_request_target policy before general availability."

Until then the default is in evaluate mode, so those runs still start. Policy insights show which runs enforcement would block.

Who gets the default:

- Public repository, no applicable Actions event policy yet: GitHub adds the default.
- Applicable event policy already in place: it is not replaced.
- Private or internal: this default does not apply.

Checkout pins are a separate control. A July 15, 2026 editor's note moved the actions/checkout backport from July 16, 2026 to July 20, 2026. Full SHA pins, minor tags, and patch tags are outside that backport. actions/checkout v1 is excluded. The page retrieved September 23, 2026 has no later note that the July 20 enforcement finished.

Fork code is not executed by default. Checkout by itself does not run it. The bug is a later step that executes what a checkout or a fetch brought in.

Full write-up with sources: https://dsotn.com/articles/pull-request-target-november-2/
