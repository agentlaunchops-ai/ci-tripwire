# Article evidence: GitHub Actions job summary security

## Scope

- Route: `/articles/github-actions-job-summary-security/`
- Base commit: `02fd9becc0866ebf4ffd518727c443ed7003c3b9`
- Draft date: 2026-08-11
- Voice register: research
- Reader value: a copy-ready pattern that publishes validated counts only, plus the exact cleanup path before and after a summary uploads.
- Excluded from the public article: editorial production mechanics and unrelated implementation details.

## Topic research

The repository has no formal backlog or enabled GitHub Issues queue. The retained image-credit ledger contained an unpublished job-summary-security slug, so the topic was validated against current search results before drafting.

Searches run on 2026-08-11:

- `GitHub Actions job summary security secrets GITHUB_STEP_SUMMARY`
- `GITHUB_STEP_SUMMARY secret leak delete workflow run`
- `GitHub Actions job summary Markdown injection security`
- `GitHub Actions job summary best practices test report`

The result set was led by GitHub's general workflow-command and security references, followed by action and tool pages. No strong result combined summary-specific masking, the warning that redaction is not guaranteed, safe handling of untrusted context values, the 1 MiB and 20-summary limits, and the before-or-after-upload cleanup split. No keyword-volume or Search Console data was available, so the opportunity is directional rather than a traffic forecast.

## What changed

- Added a question-shaped article that answers whether GitHub Actions job summaries can expose CI secrets.
- Added a fixed-field Bash example that accepts only one-to-nine-digit counts and can report after a failed test step.
- Added homepage, article-index, sitemap, and `llms.txt` discovery entries.
- Added a unique 1600 by 900 Unsplash hero and a 1200 by 630 OG image pair.
- Added mobile-safe code-block styling.
- Replaced the unused retained image credit with a neutral dashboard photograph whose source page and license were opened before use.

## Source ledger

| Claim | Source | Exact support or source location | Source date | Verdict |
| --- | --- | --- | --- | --- |
| Job summaries render custom Markdown on the workflow-run summary page | 1 | `Adding a job summary`, first three paragraphs | Retrieved 2026-08-11 | Confirmed |
| `GITHUB_STEP_SUMMARY` is unique for each step | 1 | `Adding a job summary`, paragraph beginning `Job summaries support` | Retrieved 2026-08-11 | Confirmed |
| Step summaries are grouped by job and multiple job summaries use completion order | 1 | `Adding a job summary`, paragraph beginning `When a job finishes` | Retrieved 2026-08-11 | Confirmed |
| Current-step summary content can be overwritten | 1 | `Overwriting job summaries` | Retrieved 2026-08-11 | Confirmed |
| The current step's summary file can be deleted before upload | 1 | `Removing job summaries` | Retrieved 2026-08-11 | Confirmed |
| Later steps cannot modify an uploaded summary | 1 | `Removing job summaries`, paragraph after the examples | Retrieved 2026-08-11 | Confirmed |
| Deleting the workflow run removes uploaded job summaries | 1 | `Removing job summaries`, paragraph after the examples | Retrieved 2026-08-11 | Confirmed |
| Summaries mask accidentally added secrets | 1 | Exact phrase: `Summaries automatically mask any secrets that might have been added accidentally.` | Retrieved 2026-08-11 | Confirmed |
| Each step has a 1 MiB summary limit | 1 | `Step isolation and limits` | Retrieved 2026-08-11 | Confirmed |
| A summary upload failure does not fail the step or job | 1 | `Step isolation and limits` | Retrieved 2026-08-11 | Confirmed |
| No more than 20 step summaries are displayed per job | 1 | `Step isolation and limits` | Retrieved 2026-08-11 | Confirmed |
| Automatic secret redaction is not guaranteed | 2 | Exact phrase: `automatic redaction is not guaranteed` | Retrieved 2026-08-11 | Confirmed |
| Generated and transformed sensitive values need their own mask registration | 2 | `Use secrets for sensitive information`, masking and registration bullets | Retrieved 2026-08-11 | Confirmed |
| Inline scripts should receive untrusted expressions through an environment variable | 2 | Heading: `Use an intermediate environment variable` | Retrieved 2026-08-11 | Confirmed |
| Titles, bodies, branch names, labels, and related context values can be untrusted | 3 | Exact phrase: `should be treated as potentially untrusted input` | Retrieved 2026-08-11 | Confirmed |
| Direct expression substitution can rewrite the temporary shell script | 3 | `Example of a script injection attack`, explanation after the YAML | Retrieved 2026-08-11 | Confirmed |
| Repository read access is required to open workflow-run history and its summary | 4 | `Viewing recent workflow runs`, access note and step 4 | Retrieved 2026-08-11 | Confirmed |
| Workflow-run information requires a signed-in GitHub account, including for public repositories | 5 | Opening access paragraph | Retrieved 2026-08-11 | Confirmed |
| A step uses the default `success()` status check unless a status function is present | 6 | `Status check functions`, opening paragraph | Retrieved 2026-08-11 | Confirmed |
| `!cancelled()` is the recommended condition for a step that should run after success or failure | 6 | `always`, warning and recommended alternative | Retrieved 2026-08-11 | Confirmed |
| Workflow-run deletion requires completion or an age over two weeks and repository write access | 7 | Opening eligibility and access notes | Retrieved 2026-08-11 | Confirmed |
| An in-progress workflow run can be canceled by someone with repository write access | 8 | Opening statement and access note | Retrieved 2026-08-11 | Confirmed |

Source ids:

1. GitHub Docs, `Workflow commands for GitHub Actions`, retrieved 2026-08-11.
2. GitHub Docs, `Secure use reference`, retrieved 2026-08-11.
3. GitHub Docs, `Script injections`, retrieved 2026-08-11.
4. GitHub Docs, `Viewing workflow run history`, retrieved 2026-08-11.
5. GitHub Docs, `Using workflow run logs`, retrieved 2026-08-11.
6. GitHub Docs, `Evaluate expressions in workflows and actions`, retrieved 2026-08-11.
7. GitHub Docs, `Deleting a workflow run`, retrieved 2026-08-11.
8. GitHub Docs, `Canceling a workflow run`, retrieved 2026-08-11.

## Consolidated findings ledger

| ID | Sev | Axis | Location | Finding | Corroborated by | Verified by me | Bucket |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SELF-01 | MEDIUM | image provenance | retained credit | The retained photo was legally reusable but contextually unsuitable for this topic | none | Opened the Wikimedia source and licensing record | Must fix, fixed with a neutral Unsplash photo |
| SELF-02 | MEDIUM | metadata | article and homepage cards | Initial word count and read time were estimates | none | Recounted rendered article text | Must fix, fixed to 1,202 words and 6 minutes after the round-5 edit |
| SELF-03 | LOW | mobile layout | code example | The shared stylesheet had no bounded code-block rule | none | Inspected `styles.css` and measured the rendered block | Should fix now, fixed |
| SELF-04 | LOW | mobile QA | initial 390px screenshot | The first screenshot made the article column appear clipped beside the code example | none | Added explicit mobile width constraints, then measured document and element widths through Chrome | Should fix now, fixed |
| SELF-05 | MEDIUM | deployment rendering | workflow expressions | Raw double braces could be interpreted by the GitHub Pages build before the HTML reached a reader | none | Compared existing static examples with the Pages publishing path and reran the parsed YAML example | Must fix, fixed with HTML-encoded braces that render as literal workflow syntax |
| H2-01 | MEDIUM | workflow behavior | `#safe-pattern` | The reporting step inherited `success()` and could skip failed-test reporting | X1-03 | GitHub expressions reference, retrieved 2026-08-11 | Must fix, fixed with `!cancelled()` and an output prerequisite |
| H2-02 | MEDIUM | validation | `#safe-pattern` and result table | Digit-only input had no actual length bound despite the bounded-data claim | H5-01, C5-05 | Source 1 limit plus direct code execution | Must fix, fixed with a one-to-nine-digit regular expression |
| H3-01 | MEDIUM | recovery | `#recovery` | Deletion eligibility and write-access requirements were omitted | X1-02 | Deletion and cancellation docs, retrieved 2026-08-11 | Must fix, fixed with rotate-first, cancel-active, then delete-after-completion guidance |
| H5-02 | LOW | metadata | description tags | Meta, OpenGraph, and Twitter descriptions used different strings | none | Compared all three literal values against section 6.1 | Should fix now, fixed with one 140-character description |
| C3-01 | MEDIUM | citation correctness | publishing-contract table | The cited Script injections page names labels, not comments | none | Source 3 live text, retrieved 2026-08-11 | Must fix, fixed by using `labels` |
| C3-02 | MEDIUM | citation density | `#review` | The repeated environment-variable and action-input rule lacked an at-point citation | C5-03 | Source 2 live text, retrieved 2026-08-11 | Must fix, fixed with source 2 at the checklist item |
| S1-01 | MEDIUM | voice | article and discovery descriptions | The `Learn X, Y, and Z` copy used a denied three-part payoff pattern | none | Section 3.3 policy reread | Must fix, fixed with direct declarative copy on every surface |
| S2-01 | LOW | repetition | summary and key takeaways | The redaction caveat was repeated in both top blocks | none | Read both blocks together against section 4.2 | Should fix now, fixed by removing the duplicate takeaway |
| C5-01 | MEDIUM | citation placement | `#article-summary` | The platform-definition claim relied on a citation after the next sentence | none | Source 1 live text, retrieved 2026-08-11 | Must fix, fixed with an immediate source 1 marker |
| C5-02 | MEDIUM | citation directness | `#masking` and `#review` | Mask timing needed the direct source 1 marker and narrower checklist wording | none | Source 1 live text, retrieved 2026-08-11 | Must fix, fixed at both placements |
| C5-04 | MEDIUM | citation density | `#review` | The repeated summary-size failure behavior lacked an at-point citation | none | Source 1 live text, retrieved 2026-08-11 | Must fix, fixed with source 1 at the checklist item |
| X1-01 | MEDIUM | access scope | `#article-summary` | The exposure answer omitted who can view workflow-run summaries | none | Sources 4 and 5, retrieved 2026-08-11 | Must fix, fixed with private-read and public-visibility scope |
| R2-C3-01 | MEDIUM | citation density | `#two-boundaries` | The derived shell-boundary and Markdown-boundary sentences needed their own citations | none | Sources 1, 2, and 3, retrieved 2026-08-11 | Must fix, fixed with at-point markers on both sentences |
| R2-S1-01 | LOW | voice and polish | `#masking` | `criteria` was used for a singular approval test | none | Direct grammar review | Should fix now, fixed to `a weak approval criterion` |
| R3-C1-01 | MEDIUM | citation density | recovery and review lists | Two repeated pending-summary deletion instructions lacked at-point source markers | C5-08 | Source 1, retrieved 2026-08-11 | Must fix, fixed at both list items |
| R3-C5-01 | MEDIUM | citation placement | editorial summary | Masking and redaction clauses pooled two source markers | none | Sources 1 and 2, retrieved 2026-08-11 | Must fix, fixed with one sentence and marker per claim |
| R3-C5-02 | MEDIUM | citation placement | key takeaways | Grouping and completion-order mechanics pooled a marker | none | Source 1, retrieved 2026-08-11 | Must fix, split and cited per sentence |
| R3-C5-03 | MEDIUM | citation placement | key takeaways | Immutability relied on a marker after the separate deletion sentence | none | Source 1, retrieved 2026-08-11 | Must fix, cited both sentences separately |
| R3-C5-04 | MEDIUM | citation placement | key takeaways | Size, display count, and status behavior pooled one marker | none | Source 1, retrieved 2026-08-11 | Must fix, split and cited each fact |
| R3-C5-05 | MEDIUM | citation placement | `#article-summary` | Read access and public visibility pooled different sources | none | Sources 4 and prior 5, retrieved 2026-08-11 | Must fix, split; source 5 was replaced after the X2 finding |
| R3-C5-06 | MEDIUM | citation placement | `#masking` | Transformation and runner-access conditions pooled one marker | none | Source 2, retrieved 2026-08-11 | Must fix, split and cited each fact |
| R3-C5-07 | MEDIUM | citation placement | `#recovery` | Upload immutability relied on the later deletion marker | none | Source 1, retrieved 2026-08-11 | Must fix, cited each recovery fact at point |
| R3-X2-01 | HIGH | accuracy | `#article-summary` | `visible to everyone` omitted GitHub's account sign-in requirement for public workflow information | none | Source 5 replacement, retrieved 2026-08-11 | Must fix, replaced the claim and incomplete source |
| R4-H2-01 | MEDIUM | validation portability | `#safe-pattern` | `[0-9]` is a locale-sensitive POSIX range and did not prove an ASCII-only contract | none | Bash and POSIX pattern references, retrieved 2026-08-11 | Must fix, fixed with explicit `[0123456789]` characters |
| R4-C1-01 | MEDIUM | citation correctness | `#two-boundaries` | Source 1 proved Markdown rendering, not the editorial inference attached to it | C5-01 | Source 1, retrieved 2026-08-11 | Must fix, replaced with a directly sourced rendering fact |
| R4-C1-02 | MEDIUM | citation placement | recovery list | Source 1 appeared to support a compound editorial stop/delete/fail instruction | C5-02 | Source 1, retrieved 2026-08-11 | Must fix, split documented deletion from editorial failure policy |
| R5-S2-01 | MEDIUM | plagiarism and scope | `#article-summary` | The public-repository sign-in sentence copied ten source words and omitted its web-UI scope | X1-01, X2-01 | Source 5 plus REST reference, retrieved 2026-08-11 | Must fix, replaced with a scoped independent paraphrase |

## Writer self-audit

### Pass 1: source and content

- Primary-source posture: PASS. All eight citations are current GitHub documentation.
- Claim-to-source binding: PASS. Twenty-two load-bearing rows are mapped above.
- Search URLs: PASS. None cited.
- Reader payoff: PASS. The answer and the safe pattern appear before supporting analysis.

### Pass 2: numeric and acronym

- Limits: PASS. 1 MiB per step and 20 displayed step summaries per job match source 1.
- Count method: PASS. Body text is 1,202 words from `#editorial-summary` and all article sections before `#references`.
- Reading time: PASS. Six minutes at approximately 200 words per minute.
- Terms: PASS. `GITHUB_STEP_SUMMARY`, CI, YAML, and Markdown are used consistently.

### Pass 3: tone and style

- Research register: PASS.
- Voice-denylist sweep: PASS.
- Banned characters: PASS.
- Public article scope: PASS. The page discusses the GitHub question only.

#### Pass 4: voice consistency end to end

- Opening sample: PASS. The question receives a direct answer in the first word.
- Middle samples (`safe-pattern`, `two-boundaries`, `masking`): PASS. The same direct engineering register holds.
- Closing sample: PASS. It ends with a review checklist and related implementation guides.
- Rule 3.3 voice audit: PASS. No denylist phrase remained.

#### Pass 5: scanability and trust signals

- Mobile scan path: PASS. Key takeaways and the second section answer the headline.
- Longest paragraph word count: 67, below the research-register cap.
- Bottom-line callout: YES.
- Comparison data: YES, one semantic three-column table.
- Self-describing headings: PASS.
- Three-place headline statistic: not applicable; the headline contains no statistic.
- Body word count: 1,202; jump list: NOT NEEDED.
- Closing trust signals: PASS. Disclaimer once, review-posture line, two internal trust links, corrections pointer, and source-density footer.
- Key-takeaway citation density: 4 of 4 factual bullets cited.

#### Pass 6: integrity and digestibility triple-audit

- Hallucination pass 1: 22 claims checked from article to source, 0 failed.
- Hallucination pass 2: 22 claims checked from source sections back to article, 0 failed.
- Hallucination pass 3: 22 claims checked with live URL, title, and metadata verification, 0 failed.
- Citations independently confirmed: PASS. All eight official URLs returned HTTP 200 on 2026-08-11 and their titles matched the visible labels.
- Per-citation ledger: 22 rows, all confirmed.
- Plagiarism: PASS. No shared run of 8 consecutive normalized words was found against the eight source files.
- Top-summary digestibility: PASS.
- Quality-degrading repetition: PASS. The repeated masking takeaway was removed; remaining long runs are required title, URL, JSON-LD, and metadata parity.

## Independent adversarial audit

| Round | HIGH | MEDIUM | LOW | Outcome |
| --- | --- | --- | --- | --- |
| 1 | 0 | 12 | 5 | Corrected; full fresh round required before release |
| 2 | 0 | 1 | 1 | Corrected; full fresh round required before release |
| 3 | 1 | 10 | 0 | Corrected; HIGH requires full fresh rerun |
| 4 | 0 | 5 | 0 | Corrected; full fresh round required before release |
| 5 | 0 | 2 | 1 | Corrected; full fresh round required before release |
| 6 | 0 | 0 | 0 | Clean release round |

Round 1 used fourteen isolated, read-only roles with no access to the writer ledger or one another's reports. Raw findings are counted before deduplication. Every finding is represented in the consolidated ledger; repeated findings are listed as corroborators.

### Round 1 role verdicts

| Role | Coverage | HIGH | MEDIUM | LOW | Verdict |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | 28 claims, 3 sources | 0 | 0 | 0 | CLEAN |
| H2 | 31 claims, 5 sources | 0 | 1 | 1 | FINDINGS |
| H3 | 17 claims, 5 sources | 0 | 0 | 1 | FINDINGS |
| H4 | 39 claims, 3 sources | 0 | 0 | 0 | CLEAN |
| H5 | 48 claims, 3 sources | 0 | 1 | 1 | FINDINGS |
| C1 | 29 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C2 | 14 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C3 | 11 claims, 2 sources | 0 | 2 | 0 | FINDINGS |
| C4 | 52 claims, 3 sources | 0 | 0 | 0 | CLEAN |
| C5 | 34 claims, 3 sources | 0 | 4 | 1 | FINDINGS |
| S1 | 197 public text and metadata units, 1 policy source | 0 | 1 | 0 | FINDINGS |
| S2 | 61 claims, 3 sources | 0 | 0 | 1 | FINDINGS |
| X1 | 27 claims, 14 sources | 0 | 3 | 0 | FINDINGS |
| X2 | 35 claims, 5 sources | 0 | 0 | 0 | CLEAN |

### Round 2 role verdicts

Round 2 used fourteen new read-only roles against one frozen corrected revision. Its two findings were fixed together after every report completed.

| Role | Coverage | HIGH | MEDIUM | LOW | Verdict |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | 46 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H2 | 30 claims, 9 sources | 0 | 0 | 0 | CLEAN |
| H3 | 21 claims, 17 sources | 0 | 0 | 0 | CLEAN |
| H4 | 47 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H5 | 71 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C1 | 32 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C2 | 12 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C3 | 12 claims, 2 sources | 0 | 1 | 0 | FINDINGS |
| C4 | 31 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C5 | 70 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| S1 | 82 claims, 1 source | 0 | 0 | 1 | FINDINGS |
| S2 | 37 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| X1 | 48 claims, 12 sources | 0 | 0 | 0 | CLEAN |
| X2 | 43 claims, 10 sources | 0 | 0 | 0 | CLEAN |

### Round 3 role verdicts

Round 3 used fourteen new read-only roles against article SHA-256 `6b9a8d3655d42d899668fa73d006e2c5518d605bddc2134947da98812e37d553`. Source-slice findings are counted separately before deduplication. The HIGH audience-scope finding and all citation-placement findings were fixed only after the round completed.

| Role | Coverage | HIGH | MEDIUM | LOW | Verdict |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | 49 claims, 9 sources | 0 | 0 | 0 | CLEAN |
| H2 | 29 claims, 9 sources | 0 | 0 | 0 | CLEAN |
| H3 | 17 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H4 | 49 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H5 | 54 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C1 | 33 claims, 1 source | 0 | 2 | 0 | FINDINGS |
| C2 | 9 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C3 | 11 claims, 3 sources | 0 | 0 | 0 | CLEAN |
| C4 | 34 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C5 | 48 claims, 8 sources | 0 | 8 | 0 | FINDINGS |
| S1 | 90 claims | 0 | 0 | 0 | CLEAN |
| S2 | 43 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| X1 | 34 claims, 21 sources | 0 | 0 | 0 | CLEAN |
| X2 | 55 claims, 10 sources | 1 | 0 | 0 | FINDINGS |

### Round 4 role verdicts

Round 4 used fourteen new read-only roles against article SHA-256 `db91ce6377cb00c5a26de641b331bd3c80332356fea7568a40ff7eeac895fe94`. Its duplicated citation findings were consolidated but remain counted separately below.

| Role | Coverage | HIGH | MEDIUM | LOW | Verdict |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | 70 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H2 | 31 claims, 10 sources | 0 | 1 | 0 | FINDINGS |
| H3 | 17 claims, 56 source variants | 0 | 0 | 0 | CLEAN |
| H4 | 56 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H5 | 37 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C1 | 30 claims, 1 source | 0 | 2 | 0 | FINDINGS |
| C2 | 11 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C3 | 5 claims, 3 sources | 0 | 0 | 0 | CLEAN |
| C4 | 83 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C5 | 51 claims, 8 sources | 0 | 2 | 0 | FINDINGS |
| S1 | 95 claims | 0 | 0 | 0 | CLEAN |
| S2 | 61 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| X1 | 28 claims, 26 sources | 0 | 0 | 0 | CLEAN |
| X2 | 47 claims, 9 sources | 0 | 0 | 0 | CLEAN |

### Round 5 role verdicts

Round 5 used fourteen new read-only roles against article SHA-256 `61525de67980c13fc5517be860bf1946ed3d5288f280e4b73d1543176d296ed2`. The S2 and X2 plagiarism findings identified the same phrase; X1 added the web-UI qualifier.

| Role | Coverage | HIGH | MEDIUM | LOW | Verdict |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | 78 claims, 9 sources | 0 | 0 | 0 | CLEAN |
| H2 | 20 claims, 6 sources | 0 | 0 | 0 | CLEAN |
| H3 | 20 claims, 12 sources | 0 | 0 | 0 | CLEAN |
| H4 | 63 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H5 | 37 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C1 | 30 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C2 | 11 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C3 | 7 claims, 3 sources | 0 | 0 | 0 | CLEAN |
| C4 | 51 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C5 | 83 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| S1 | 69 claims | 0 | 0 | 0 | CLEAN |
| S2 | 59 claims, 8 sources | 0 | 1 | 0 | FINDINGS |
| X1 | 38 claims, 16 sources | 0 | 0 | 1 | FINDINGS |
| X2 | 49 claims, 9 sources | 0 | 1 | 0 | FINDINGS |

### Round 6 role verdicts

Round 6 used fourteen new read-only roles against article SHA-256 `130713525123e705ddae2d39fee6cfdeaf8c6006764c3a181d0a77d809a4ef79`. Every role returned CLEAN with zero HIGH, MEDIUM, or LOW findings.

| Role | Coverage | HIGH | MEDIUM | LOW | Verdict |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | 43 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H2 | 30 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H3 | 14 claims, 13 sources | 0 | 0 | 0 | CLEAN |
| H4 | 52 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| H5 | 61 claims, 10 sources | 0 | 0 | 0 | CLEAN |
| C1 | 30 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C2 | 11 claims, 1 source | 0 | 0 | 0 | CLEAN |
| C3 | 9 claims, 2 sources | 0 | 0 | 0 | CLEAN |
| C4 | 51 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| C5 | 73 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| S1 | 90 public text and metadata units | 0 | 0 | 0 | CLEAN |
| S2 | 60 claims, 8 sources | 0 | 0 | 0 | CLEAN |
| X1 | 52 claims, 16 sources | 0 | 0 | 0 | CLEAN |
| X2 | 75 claims, 9 sources | 0 | 0 | 0 | CLEAN |

## Gates and manual QA

- `git diff --check`: PASS.
- Sitewide JSON-LD, XML, internal-target, and discovery parity: PASS across 23 HTML files and 19 article routes.
- Visible and JSON-LD citation URL parity: PASS for all 8 sources.
- All 8 official GitHub source URLs and the Unsplash source page: HTTP 200 on 2026-08-11.
- Title length: PASS at 51 characters. Meta description: PASS at 140 characters.
- Body and schema count: PASS at 1,202 words. Reading-time parity: PASS at 6 minutes and `PT6M`.
- Banned-character scan: PASS with no em dash, en dash, or curly quote.
- Hero: PASS at 1600 by 900. OG PNG: PASS at 1200 by 630. SVG fallback title parity: PASS.
- YAML example syntax: PASS. Behavior check: the fixed template accepted the exact expected numeric output across 288 installed locales. Eight empty, oversized, non-ASCII, signed, padded, alphabetic, and injection-shaped inputs failed and removed the pending summary file.
- Local HTTP route, hero, and OG asset: PASS at HTTP 200 with the exact title in route HTML.
- Mobile Chrome QA at 390 by 844: PASS. Document and body `scrollWidth` both equaled 390; the title and table were 350 pixels wide inside the viewport; the code block stayed contained and scrolled internally at 348 client pixels and 504 content pixels; desktop TOC was hidden.
- Desktop Chrome QA at 1440 by 1000: PASS. Document and body `scrollWidth` both equaled 1440; article content was 740 pixels wide; the hero loaded at its natural 1600 by 900 dimensions; TOC was visible.
- Package-manager gates: not applicable. This static repository has no `package.json`, lint script, build script, or test script.
- Full independent audit: PASS. Round 6 returned 0 HIGH, 0 MEDIUM, and 0 LOW findings across all 14 required roles.

## Distribution draft

### Can GitHub Actions job summaries expose CI secrets?

Yes. A job summary is Markdown published on a workflow-run page, so dumping logs, contexts, stack traces, or API responses can expose data that never belonged there. GitHub masks secrets in summaries, but its secure-use guidance says redaction is not guaranteed for transformed values.

A safer pattern is narrow. Move untrusted expressions into environment variables, validate both shape and length, then render only approved fields through a fixed template. Never deliberately publish credentials. If sensitive content is still pending in the current summary step, delete `GITHUB_STEP_SUMMARY` before the step ends. After upload, rotate any exposed credential immediately. Someone with repository write access can cancel an active run and permanently delete it after completion.

Full write-up with sources: https://dsotn.com/articles/github-actions-job-summary-security/

Safe-to-post note: suitable for engineering communities that allow source-linked technical answers. If a community prohibits external self-links, remove the final URL and post the complete answer above. The draft was checked against the article's sources and voice denylist.

## Affiliate opportunities

None. This is a platform-security implementation guide.

## Known limitations and residual risk

- Search evidence is directional and has no query-volume or Search Console support.
- GitHub can revise summary handling and redaction behavior after the 2026-08-11 source snapshot.
- No live GitHub Actions workflow was dispatched. The workflow expression and lifecycle behavior were checked against current GitHub documentation, and the Bash body was executed locally across 288 installed locales.
- All citations were reachable and directly supportive on the review date; future documentation or platform changes remain a currency risk.
- The public article and distribution draft contain only the GitHub question and answer. Internal production methods are excluded.
- The existing site does not declare a favicon, so Chrome's implicit `/favicon.ico` request returned 404 during local QA. The article's declared route and assets returned 200.
