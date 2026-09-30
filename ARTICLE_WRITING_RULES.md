# Content Agent Rules (portable)

One file covering everything an agent needs to research, write, structure,
optimize, audit, and ship editorial content in a repo where content is typed
data. Consolidated from a live YMYL health-content catalog (110+ long-form
articles, 220+ structured reference entries) and the defect history that
produced each rule.

Copy this file into a repo, fill in section 0, and treat it as the canonical
contract. Every rule below exists because something shipped broken without it.

---

## 0. Adapt before you use

Fill these in once per repo. The rest of the document refers to them.

| Placeholder | Meaning | Example |
| --- | --- | --- |
| `<SITE>` | Public origin | `https://example.com` |
| `<BRAND>` | Publisher name used in bylines and JSON-LD | `Example Editorial` |
| `<ARTICLE_DIR>` | Typed article modules | `src/data/articles/posts/` |
| `<ARTICLE_INDEX>` | Hand-edited catalog registry | `src/data/articles/index.ts` |
| `<SCHEMA>` | Article type definitions | `src/data/articles/types.ts` |
| `<REF_DIR>` | Structured reference entries | `src/data/entries/` |
| `<IMAGES>` | Hero photos + credits ledger | `public/images/articles/`, `CREDITS.md` |
| `<CHANGELOG_DIR>` | Per-day changelogs | `docs/changelog/` |
| `<DISCLAIMER>` | The exact compliance sentence, if the domain needs one | see 1.1 |
| `<TOPIC_EXCLUSIONS>` | Subject matter the owner has excluded | (list them) |

**Precedence.** When two rules conflict, the stricter one wins. When this file
conflicts with a repo-specific guardrail, surface the conflict to the owner and
fix the doc in its own commit before writing content.

**What this file replaces.** Fixed word counts, readability-score targets,
mandatory FAQ blocks, keyword checklists, and topic-discovery ceremony. None of
those are here on purpose. What is here is accuracy machinery, structure that
survives a phone screen, and a voice that does not read like a machine.

---

## 1. Non-negotiables

These never relax. A lighter register, a shorter piece, a rush, or a "quick
fix" buys no exemption.

### 1.1 Compliance line

If the domain is regulated or advice-adjacent, every piece carries the exact
disclaimer string **exactly once**, in the closing section, verbatim:

```
<DISCLAIMER>
```

Example from the source catalog: `For research and educational purposes only.
Not medical advice.`

Not in the key-takeaways bullets. Not twice. Page chrome that renders a
standing disclaimer panel is independent of the in-body occurrence and does not
substitute for it.

### 1.2 Nothing invented, ever

No invented study, identifier (PMID, NCT, DOI, setid), author, date, statistic,
price, product, shortage, statute, quote, anecdote, or credential. If a claim
cannot be verified against a real source that actually states it, cut it,
soften it to plainly-flagged uncertainty, or re-source it.

### 1.3 Byline integrity

Authorship is `<BRAND>` at the organization level. Never invent an expert, a
reviewer, a medical director, a degree, or an affiliation the brand does not
own. JSON-LD `author` stays an Organization until real contributor identities
exist. Do not emit `Person` schema for fabricated or anonymous individuals.

### 1.4 Banned characters

- **No em dashes (U+2014).** Anywhere: titles, headings, summaries, body,
  callouts, captions, table cells, alt text, commit messages, distribution
  drafts. Use commas, parentheses, periods, or hyphens.
- No en dash standing in for an em dash. No comma-spliced antithesis that
  smuggles the em-dash reveal back in ("it is a plan, not a bridge").
- No curly quotes (U+2018, U+2019, U+201C, U+201D). Straight quotes only.
- No emoji in body, headings, or titles.

These are almost never enforced by a test suite. Grep before every commit:

```
rg -n '[\x{2014}\x{2013}\x{2018}\x{2019}\x{201C}\x{201D}]' <ARTICLE_DIR><file>
```

`grep -P` does not work on macOS BSD grep. Use `rg`.

### 1.5 Claim hygiene

- No marketing superlatives (revolutionary, miracle, best-ever, game-changer,
  cutting-edge, must-know).
- No claim that anything diagnoses, treats, cures, or prevents disease.
- No second-person prescription ("you should", "you must") on regulated topics.
  It reads as advice, not education.
- `<TOPIC_EXCLUSIONS>` stay out of the catalog entirely.

### 1.6 Preserve other people's work

Never reset, revert, stash, or clean uncommitted changes you did not create.
Shared checkouts are normal; an uncommitted diff you did not write is someone
else's in-progress work.

---

## 2. Audience posture: who you are writing for

This is the rule whose absence produced the worst public feedback the source
catalog ever got ("fearmongering", "hypocritical", "what is the point, none of
this is news"). Read it before picking a stance on anything.

### 2.1 Product coherence

Know what the product actually helps people do, and write in service of that.
If the tools exist to help readers do a thing competently, the editorial stance
toward that thing is **competent harm reduction, not abstinence and not a
sermon.** Assume the reader is going to do it. Your job is to make them better
and safer at it.

- **Be skeptical of the right targets.** Blunt skepticism points at hype,
  vendors, marketing claims, junk studies, and bad numbers. It never points at
  the reader's own decision. An article skeptical of *the reader* instead of
  *the claim* reads as the brand lecturing the people it is built for.
- **State a real risk once, plainly, with the cite, then pivot to how to handle
  it.** Risk information serves doing the thing safely, not scaring the reader
  off. The sentence after the risk is the mitigation, not "so maybe do not do
  this."
- **Banned framings:** "no evidence it works, so do not", "the version worth
  having is a conversation with a professional, not the thing itself", "just
  see your doctor", or any framing whose implicit conclusion is that the reader
  should not be a user of this product. If the honest take really is "this is
  dangerous enough that the move is to not do it", that is a rare load-bearing
  call: state it once, cite it hard, do not pad it into a recurring moral.
- **Hold one standard.** Do not fearmonger about one route while the product
  enables a riskier one. Readers see the incoherence instantly.
- None of this softens real safety content. It aims the honesty at helping the
  reader succeed, which is also the safest posture: a reader who feels judged
  stops reading and fails on the details anyway.

### 2.2 Reader value: say something the label does not

- Before drafting, name in one sentence the specific thing the reader walks
  away with that they could not have found in ten seconds. If the honest answer
  is "the official guidance says start low, so ask a professional", that is the
  label plus a shrug, not an article. Kill it or find the angle that delivers.
- The value is almost always the operational detail the official source omits:
  the actual math, how to vet a supplier, what real aggregated experience
  reports (labeled as such), the tradeoffs between options, what the failure
  modes look like.
- "None of this is news" is a failure result, not a neutral one. Fresh framing
  of a known fact still has to be more useful, more honest, or more specific
  than what the reader already has.

### 2.3 Do not be preachy

Inform, do not lecture. The reader is a curious adult making their own calls.

- State a risk once, then move on. Do not circle back in a sterner voice.
- Replace the lecture with the fact. Not "never buy from unverified sources",
  but "here is what people who got burned actually ran into, and how it showed
  up." The facts do the persuading.
- Delete boilerplate: "always consult a professional", "it cannot be stressed
  enough", "remember to", "it is important to prioritize your health."
- Not preachy is not the same as not honest. When a thing is genuinely
  dangerous, say so plainly and once. That is the cite doing its job.

### 2.4 Make it relatable

Anchor the piece in the reader's lived moment, not a definition. Open with the
question they actually typed. Name the feeling in plain words. Use real
reported experience, cited, and **never invent a quote, a person, or a forum
post.**

### 2.5 Never narrate the reader's community (hard ban)

An article states facts to one reader. It never comments on Reddit, forums,
"the sub", "the threads", "the community", or any platform where the reader
hangs out, and it never narrates what that crowd thinks, asks, fears, or wants.

Banned in every form:

- Naming the venue: "the plateau that fills Reddit threads", "every forum post
  asks this", "as everyone knows."
- Narrating the crowd's psychology: "the answer nobody wants to hear", "the
  question nobody wants to admit", "what everyone is really asking."
- Any knowing, meta, we-both-know-the-community wink.

Write the fact plainly. "The plateau is built into the drug" is the sentence.
"The plateau that fills Reddit threads is built into the drug" is banned.
Knowing who the audience is shapes what you explain; it never gets narrated
back at them. (A separate, actual community post deliverable is exempt: it is
an actual post on that platform.)

### 2.6 Do not sanitize the audience's vocabulary

Community terms are the correct, common terms. Never rename, scare-quote,
clinicalize, or add construct-validity hedging to vocabulary the audience
already uses. Audit the facts, not the words.

---

## 3. Voice

### 3.1 Pick a register per piece, then hold it

Two registers, same facts, same rigor, different delivery. State the chosen
register in one line before drafting and record it in the changelog so a future
audit grades against the right rule.

**Research register.** Evidence maps, "what the data actually shows",
regulatory posture, comparisons that turn on trial numbers, mechanism
deep-dives. Voice: blunt, skeptical, owner-led, opinionated, direct. The reader
wants the honest verdict and the evidence behind it. Profanity and strong
judgment are allowed when they fit.

**Easy-reading register.** Timelines, digests, living reference guides,
beginner on-ramps, "what you actually need to know" explainers. Voice: a sharp,
funny, well-read friend who knows the field and wants you to get it. Warm,
plain, direct, a little playful, occasionally wry. Never smug, never
breathless.

Worked contrast:

- Research (do not use in easy-reading): "Adverse-event profiles associated
  with the class are predominantly gastrointestinal in nature and typically
  attenuate over the titration period."
- Easy-reading: "Most side effects are gut stuff: nausea, constipation nobody
  warns you about, the occasional rough morning. For a lot of people it eases
  off as the dose ramps slowly. For some it does not. Both are normal."

Only the delivery changed. The facts and the cite on each claim did not.

Pick the register at the title and TL;DR and hold it through the closing. The
most common failure is a punchy opener and a policy-brief body.

### 3.2 The policy-brief failure mode

Avoid passive constructions stacking up, nominalization-heavy clauses ("the
comparator structure tended to flag", "the regulatory environment tightens"),
and abstractions where a concrete noun would do.

- Avoid: "The trap with a contamination story is the binary read. Treating
  two-thirds-over-threshold as either a panic or a shrug loses the structure of
  what is actually known."
- Use: "The trap here is reading this as either total panic or a shrug. Neither
  is right. The lead is real, it adds up, and the spread between brands is big
  enough that which tub you buy matters more than whether you use powder at
  all."

### 3.3 Do not write like an AI (the denylist)

This is the canonical, catalog-wide anti-AI-voice rule. It binds every piece in
every register and every distribution draft.

Why it is not a nitpick: a live article got publicly mocked with "give my
regards to Claude for writing it up." That is a brand-credibility failure. A
technical, skeptical audience smells machine-written copy in one paragraph and
stops reading before the facts land, however correct the facts are.

The rule has two halves and **both bind**: a hard denylist, and a catch-all.
The list is illustrative. **The catch-all is the law: if a phrase is one an AI
would produce by reflex, it is banned here even if it is not printed below.**

**The negation-and-reveal reflex (loudest tell, kill on sight).**
Defining a thing by what it is not, then revealing what it really is:
"It's not X, it's Y." "It's not just X, it's Y." "This isn't about X, it's
about Y." "X isn't the problem, Y is." "Not X, but Y." "It's less about X and
more about Y." Also the general setup-and-pivot: a sentence that exists only to
knock down a strawman so the next clause sounds profound.
State what the thing IS. "Staying on it is the maintenance plan" is a real
sentence. "It's not a bridge to getting off the drug, it's the plan itself" is
the AI rewrite of the same idea.

**The rule-of-three drumbeat.** Three adjectives, three parallel clauses,
three-item payoffs ("safer, cheaper, and more consistent"). Vary it: sometimes
one word, sometimes five real items. Never a reflexive tricolon whose third
element exists only for rhythm. A real ranked list or table of data is fine;
the tell is the decorative triad inside a sentence.

**The performative-casual flourish (subtlest and most dangerous).** When told
to "sound human", an AI reaches into a small bag of writerly tricks instead of
saying the specific thing plainly. All banned:

- Rhetorical reversal / chiasmus: "the question people ask last and should ask
  first", "we don't stop to rest, we rest to keep going."
- Writerly setup devices: "if you only read one thing, read this", "here is the
  part that matters." Make the point; do not announce it or rank your own
  sentences for the reader.
- Cutesy sensory or anthropomorphic metaphor: "food gets less loud", "the drug
  presses its buttons", "the schedule never rushes." Say the literal thing.
  (An established community term is fine; the ban is on decorative rephrasings
  of plain facts.)
- Folksy idiom as costume: "without white-knuckling it", "the whole nine
  yards", "easier said than done", "your mileage may vary", "at the end of the
  day."
- Ironic understatement as a wit move: "the reliable way to feel awful", "that
  went about as well as you'd expect."
- The reflexive punchy fragment. One deliberate fragment can be real voice; a
  drop-to-a-fragment after every claim is the tell.
- "The X thing" as filler: "the single-versus-dual thing." Name the actual
  thing.
- Imperative nudges: "but notice the timeline", "watch what happens here", "sit
  with that for a second."
- Framing lead-ins that rank the next sentence: "a fair way to read that:",
  "the honest truth is", "here is the part people miss", "if we're being real."

The test: if the personality in a sentence is a device rather than a real
thought, cut the device and keep the thought.

**Throat-clearing and transition filler.** "Here's the thing." "Here's the
deal." "But here's the kicker." "The thing is." "The reality is." "The truth
is." "Let's be honest/clear." "Let's face it." "Make no mistake." "Look," /
"Honestly," / "Frankly," / "Now," / "So," as a sentence-opening throat-clear.
"That said." "That being said." "At the end of the day." "When it comes to."
"It's worth noting/mentioning." "It's important to note/remember/understand."
"Needless to say." "It's no secret that."

**Tour-guide and essay scaffolding.** "Let's dive in." "Let's unpack this."
"Let's break it down." "Let's take a closer look." "A deep dive." "In this
article, we'll..." "By the end of this, you'll..." "In the sections that
follow..." A "First... Second... Finally" scaffold when the ideas do not
actually need numbering.

**LLM-vocabulary tells.** Use the plain word or cut the sentence:
delve; navigate / landscape / realm / sphere / arena / "the world of X" as
metaphor; tapestry; "a testament to"; beacon; cornerstone; bedrock; ecosystem
as metaphor; leverage; utilize (use "use"); harness; unlock; unleash; empower;
elevate; streamline; foster; facilitate; spearhead; boasts; showcase;
underscore; highlight (meaning emphasize); robust; seamless; holistic; nuanced;
multifaceted; intricate; myriad; plethora; "a wealth of"; "a treasure trove
of"; "a wide array of"; "a vast array"; crucial; pivotal; vital; paramount;
essential; "key" as adjective spam; notable; compelling; significant (when it
means nothing); "ever-evolving"; "rapidly changing"; "fast-paced"; "in today's
world"; "in an era of"; game-changer; revolutionary; cutting-edge;
state-of-the-art; groundbreaking; transformative; next-level.

None are forbidden English. They are forbidden because AI over-produces them
and readers pattern-match them instantly.

**The both-sides sandwich and the tidy uplifting closer.** "Ultimately, the
choice is yours." "The decision comes down to you." "Only you can decide."
"Whether you're X or Y, [tidy takeaway]." "One thing is clear:" "In
conclusion," "To sum up," "All in all." A closing paragraph that restates what
was already said. "...empowering you to make an informed decision." The empty
universal caveat: "Everyone is different." "Results may vary." "What works for
one person may not work for another." (Give the actual variance with a number,
or cut it.)
End on the most useful specific, or a real opinion with a spine, or nothing.
Not a bow. This does not touch the structured Bottom-line callout or the
closing trust block; those are load-bearing and named.

**Rhetorical-question filler and curiosity gaps.** "So what does this mean for
you?" "But why does this matter?" "You might be wondering..." "Ever
wondered...?" "The million-dollar question is..."
Plus the full curiosity-gap denylist, banned in titles, headings, summaries,
and body: "the crazy part", "the wild part", "the surprising part", "what most
people miss", "what nobody tells you", "what they don't tell you", "what they
don't want you to know", "the part nobody talks about", "the real reason", "the
truth about", "you won't believe", "here's the kicker", "plot twist", "and that
changes everything", "the one thing", "this is huge", "let that sink in", "the
secret to", "and the results may surprise you."
The rule underneath: **never tease a payoff you are about to give. State it.**
"Most of the food-noise data is on drug A, not drug B" beats "the food-noise
detail nobody mentions."

**Structural and formatting tics.** The reflexive bold-label-colon bullet on
every point ("**Dosing:** start low"). Over-listing prose that should breathe.
Perfectly even rhythm (AI writes similar-length sentences in similar shapes;
put a five-word sentence next to a twenty-five-word one). Colon-spray.
Exclamation spray. Hedge-stacking: "may potentially possibly help support",
"arguably", "relatively", "somewhat", "fairly", "quite", "generally speaking",
"for the most part", "by and large" as reflex softeners. Commit or cut.

### 3.4 How to sound human instead

Start in the middle, at the useful part, not with context-setting. Use concrete
nouns and real numbers instead of abstractions. Have an opinion and commit to
it; hedge only where the evidence is genuinely thin, and then say exactly how
thin ("two small trials and a lot of forum confidence"). Let the rhythm be
uneven. Contractions are good. Define a term in half a sentence the first time,
then move on. Write the whole piece as if one specific person who knows the
field typed it in one sitting and did not go back to sand it smooth. If a
paragraph reads back smooth and content-free, it is slop; rewrite until a real
person is in it.

**Anti-AI voice audit is a mandatory pre-commit pass.** Reread the finished
draft against 3.3 adversarially, in the voice of the skeptical commenter who
will publicly credit an AI for writing it. For every sentence ask: would a
person who actually knows this field type this? Fix every hit and record the
pass in the changelog next to the voice verdict.

---

## 4. Structure and the content model

### 4.1 Length follows the evidence

There is no word count. Write exactly what the topic's real, verifiable
information supports. A thin topic yields a short, tight piece; a rich topic
yields a long one. Padding to look thorough and truncating to look tidy are
both failures. No forced readability score, grade level, fixed outline, fixed
heading count, or fixed number of related links.

### 4.2 The typed article module

Content is typed data, not markdown prose files. One module per piece in
`<ARTICLE_DIR>`, registered in `<ARTICLE_INDEX>`, satisfying `<SCHEMA>`.

Reference shape (adapt names, keep the roles):

```ts
type Article = {
  slug: string;              // kebab-case, unique, matches the filename
  title: string;             // 50-60 chars, never over 60
  summary: string;           // 2-4 sentences, under ~320 chars
  tldr?: string;             // 1-2 sentence answer, front-loaded
  metaDescription?: string;  // 50-155 chars, search snippet override
  category: ArticleCategory; // a literal from the closed set
  tags: readonly string[];
  readingTimeMinutes: number;// words / ~200, honest
  publishedAt: string;       // YYYY-MM-DD
  updatedAt: string;         // == publishedAt on first ship
  heroId: string;
  sections: readonly ArticleSection[];
  citations: readonly ArticleCitation[]; // {id, label, publisher, url}
  relatedCompoundIds: readonly string[];
  relatedArticleSlugs: readonly string[];
  faq?: readonly { question: string; answer: string }[];
};
```

Block types inside a section: `paragraph`, `list`, `callout`
(`tone: info | caution | evidence`), `chart` (self-authored horizontal bar),
`table` (real semantic table). Treat the schema file as truth on block shapes;
rule docs go stale on them.

Field rules that matter:

- **`title`**: 50-60 characters. Search truncates around 60 and a truncated
  title loses the hook in front of the click decision. Longer editorial framing
  goes in `summary`, never in `title`.
- **`tldr`**: the answer-shaped bottom line, not a restatement of the takeaways
  and not "this article covers...". Front-load it: some surfaces truncate at
  145 characters, so the payoff must land in the first clause. Practical test:
  a reader who only reads the TL;DR knows the bottom line; a reader who only
  reads the bullets knows the load-bearing numbers; a reader who reads both
  does not feel they read the same thing twice.
- **`readingTimeMinutes`**: hand-set and honest. Recompute at ~200 wpm.
- **`relatedArticleSlugs` / `relatedCompoundIds`**: only ids that exist today.
  Skip rather than invent. Once the catalog passes ~30 pieces, require 3+
  related slugs, chosen by tag overlap and category match, preferring the
  strongest matches over the most recent, and including at least one
  cross-category match when a plausible one exists.
- **`chart` / `table`**: authored from the piece's own cited numbers, so they
  are original by construction. Never lift a copyrighted figure or screenshot a
  journal chart. Set `max` explicitly (for example 100 for percentages) so bars
  stay honest. Every table row has exactly `columns.length` cells.
- **`faq`**: when present, the visible FAQ section and the FAQPage JSON-LD ship
  together. JSON-LD FAQ with no visible counterpart is a structured-data policy
  violation. Answers are plain text restating facts already established and
  cited in the body. Never introduce a new claim through FAQ schema.

### 4.3 Section order

1. **`key-takeaways` (first section, always).** A single `list` of 4-6
   specific, numeric, extractable bullets. Every bullet carrying a hard claim
   (a number, a regulatory status, a trial outcome, a named-entity verdict)
   lands its inline citation marker **inside that bullet**. This section feeds
   speakable JSON-LD; an uncited number reads as opinion at the extraction
   layer. Opinion and rhetorical-summary bullets are exempt.
2. **Reader-payoff section (second, always).** The concrete answer the reader
   came for: the tested-clean brand list, the side-by-side comparison, the step
   list, the explicit "should I keep doing this" answer. Bury the analysis
   behind the answer, not in front of it. If the topic genuinely has no single
   concrete payoff (a mechanism piece, a regulatory explainer with no
   consumer-facing decision), the strongest evidence section takes this slot.
3. **Body sections.** Each heading carries its load-bearing claim.
4. **Closing section.** The recap, the single disclaimer, and the trust block.
   Never the first surfacing of the answer.

### 4.4 Scanability (mobile-first, and this is a voice rule)

Traffic skews mobile. A piece that reads cleanly on a laptop and renders as a
six-screen wall on a phone is broken even if every sentence is correct.
Scanability is how "blunt, direct, useful" expresses itself as layout.

- **Bottom line up front.** When the piece makes a recommendation, the
  reader-payoff section opens with a `callout` `tone: "info"` titled "Bottom
  line", carrying the one-or-two-sentence answer. Supporting data renders under
  it, never before it.
- **Comparison data is a list or a table, never prose.** Use a real `table` for
  genuine grids of 3+ columns. Use a `list` with parallel-structure rows
  (`Item, verdict, load-bearing number, citation`) for two-field rows that read
  better as one mobile column. Parallel structure across rows is what makes it
  scannable at 375px.
- **Ranked verdicts are callouts.** `tone: "evidence"` for the best / clean /
  recommended verdict, `tone: "caution"` for the worst / avoid verdict. The
  title is the verdict itself ("Tested clean: six brands under threshold"), not
  a hedge ("Notable findings").
- **Headings carry the claim.** "Plant-based ran nine times the dairy average"
  beats "Discussion". No one-word headings (Background, Methodology, Results,
  Conclusion); they are scan-dead. No curiosity-gap headings that hide the
  answer.
- **Three-place rule.** Every number the headline rests on appears in the
  key-takeaways bullet, in the reader-payoff section, and again at the point of
  claim in body prose. Identical wording and identical rounding in all three.
- **Paragraph cap.** A single paragraph over ~120 words is a wall (~80 words in
  the easy-reading register). Break it or move the claim into a list or
  callout. Ship at least one non-paragraph block per ~300 words of prose; a
  600-word wall of pure paragraphs fails.
- **Jump list at 1,400+ words.** Append a one-line `paragraph` reading "Skip
  to:" plus a `list` of the remaining section headings to the key-takeaways
  section. Mobile scan affordance only; the sidebar table of contents handles
  deep linking on large screens. Under 1,400 words, skip it.

### 4.5 Trust signals in the closing section (YMYL block)

Advice-adjacent content is YMYL under search-quality guidelines. The closing
section carries four signals **beyond** the single disclaimer, in this order,
roughly four lines on mobile:

1. A one-sentence honesty line about the review posture: "`<BRAND>` has not
   commissioned independent clinical review of this article." Do not invent a
   reviewer or credential the brand does not own.
2. A `paragraph` with two inline internal links: editorial process /
   contributor disclosure, and sourcing posture.
3. A one-line corrections pointer, so the corrections process is visible inside
   the piece.
4. A one-line citation-density footer: "Sources: N entries, all primary canon,
   last reviewed YYYY-MM-DD." Substitute "primary canon plus reputable
   secondary sources, with inline acknowledgment" when applicable.

### 4.6 Hero imagery

- A real, topical photograph is **required on first ship**. No SVG-only first
  ship. Generated hero art is an OG fallback only.
- **Unique per piece.** Grep the credits ledger for the source URL before
  downloading. If it is already there, pick a different photo.
- Permitted pools, in order of preference: public-domain government works,
  Wikimedia Commons CC0/PD, Pexels, Unsplash.
- Off-limits: Getty, Shutterstock, Adobe Stock, Alamy, any rights-managed or
  per-use-licensed pool, AI-generated raster imagery, any identifiable
  individual without a clear model release on the source page.
- No image that implies a clinical claim (before/after body comparisons,
  someone weighing themselves). Educational context photos are fine.
- Prefer landscape, crop to 1600x900 or similar.
- Register the photo with descriptive alt text and append a credits row: slug,
  source URL, author, license, retrieval date. The credits ledger is the single
  source of truth for both attribution and the no-reuse rule.
- Regenerate the OG image pair whenever the hero or the title changes.

### 4.7 Inline links

- Internal links use an absolute path and render as a client-side link. No
  `rel`, no `target`.
- External non-affiliate links use a full https URL and render with
  `rel="nofollow noopener noreferrer"` and `target="_blank"`.
- Affiliate links render with `rel="sponsored noopener noreferrer"` and a
  visible inline disclosure marker.
- `javascript:`, `data:`, and mailto URLs are rejected as a security gate.
- Do not put citation markers inside link labels; the bracket collision breaks
  the parse. Put the cite after the link.

---

## 5. Citations and factual standard

### 5.1 What must be cited

Every nontrivial factual claim: regulatory or approval status, meeting and
approval dates, label claims, trial outcomes, human-study findings, safety
findings, adverse-event prevalence, mechanism, dose ranges, anti-doping status,
prices, counts, and every number the headline rests on.

Pharmacology constants (half-lives, Tmax, PK curves) must trace to published
human data. Something with no published human PK gets an honest "no data"
statement, **never** an invented number or a fabricated curve.

If a claim cannot be verified, rewrite it as opinion or plainly-flagged
uncertainty, or remove it.

### 5.2 Sourcing posture

**Preferred primary canon** (regulators, peer-reviewed journals, federal public
health bodies, trial registries). For the health domain that is: PubMed, PMC,
PubChem, ClinicalTrials.gov, DailyMed, FDA / accessdata.fda.gov, Federal
Register, WADA / USADA, CDC, NIH / ODS, Cochrane, WHO, court dockets. Adapt the
canon list to your domain.

**Reputable secondary sources are allowed** when they add value the canon does
not cover (independent journalism, professional-society guidance, manufacturer
prescribing information not on the primary mirror, international regulator
pages, university press releases). When one is doing load-bearing work, the
body must acknowledge it inline. Do not hide the caveat:

- "Per a 2025 press summary from manufacturer X (industry-funded, full trial
  data not yet published)..."
- "A community-aggregated report database (self-reported, not peer-reviewed)
  shows..."
- "Per a non-peer-reviewed preprint that has not been replicated..."

**Off-limits as citations:** vendor pages, retail and affiliate pages,
telehealth or other marketing pages, sourcing forums, discussion-forum threads,
AI-generated summary pages. They are sales surfaces or unverifiable.

Reuse URLs from a shared source registry where one exists, so articles and
reference entries stay consistent.

### 5.3 The Citation Correctness Standard

"I added a citation" is not the bar. **"This source contains this exact fact"
is.** A catalog-wide audit found 53 citation-integrity defects across 35
articles, every one of which passed the test suite. Read this as a hard
procedure, not advice.

- **What the tests do NOT check.** Typical data-invariant tests check only that
  each URL is https and parses and that every citation marker resolves. They do
  NOT check that the URL is live, that the source supports the claim, that
  author / year / identifier are accurate, or that a number matches its source.
  Those four are the most common real defects and are entirely the agent's job.
  **A green test run is not evidence of citation correctness.**
- **Claim-to-source binding.** A citation backs only the specific clause it
  touches. Every load-bearing claim carries its own citation at the point of
  claim, and that source must contain that exact fact, not merely the topic. A
  cite at the end of a paragraph does not retroactively support an earlier
  load-bearing claim in the same block. When one sentence asserts two
  independent facts, split the citation.
- **Open and quote before you cite.** Find the exact supporting sentence, table
  cell, or labeled value. If you cannot quote it, the claim is unsupported:
  cut, soften to what the source does support, or re-source. Never cite from
  memory, a search-result snippet, or a generated summary.
- **Metadata must match the record.** Author list, year, journal or publisher,
  and the identifier (PMID / NCT / DOI / setid) in the label must match the
  actual record. A wrong author or a transposed identifier is a hallucinated
  citation even when the URL resolves.
- **Number fidelity.** State every figure exactly as the source states it.
  Round to nearest, never inflate or widen (45.2% is "about 45 percent", never
  "about 50 percent"). The same figure reads identically in all three
  placements; the three-place rule is reinforcement, not license for drift.
- **Citation labels are reader-visible.** In many renderers the `label` field
  becomes the visible reference link text. Audit labels as prose. An incomplete
  instruction truncated into a label has shipped live. Never put raw quotes in
  a label.
- **Corroboration is not verification.** A sibling article or a prior
  "correction" agreeing with the claim is the least independent check there is.
  Fetch the primary document. If it makes no claim either way, delete the
  assertion rather than reversing it, then grep the whole catalog for every
  copy of it.
- **No commercial pages for load-bearing claims.** If a figure exists only on a
  market-research, vendor, or marketing page, soften the claim so it no longer
  asserts false precision, or drop it.

### 5.4 Named failure modes (hunt for each)

- A citation that supports the adjacent sentence but not the load-bearing claim
  it is attached to.
- A compound sentence where the cite supports only one of two facts.
- A study-design, rationale, or protocol paper cited for trial results it does
  not report.
- A registry record or review cited for outcomes it never states.
- A cite pointing at a different study, dose, population, or estimand than the
  claim states.
- A primary trial paper cited for a substudy figure that lives only in a
  separate analysis.
- An identifier resolving to an unrelated paper.
- A number rounded up or widened beyond the source.
- A load-bearing claim carrying no citation at all.
- A bot-blocked or commercial URL standing in for an available
  fetch-verifiable primary.
- Stale regulatory status after a label revision, approval, or readout.

### 5.5 Two traps that hide from every automated check

**Search URLs.** A keyword-search URL (`pubmed.../?term=...`,
`clinicaltrials.gov/search?term=...`) is the one citation form a title-verify
net cannot see: no identifier to check, and the search page returns HTTP 200.
A fabricated "Author (year) found X" parked on one ships invisibly. This is
exactly how a fabricated trial reached production. **A search URL is allowed
ONLY as an explicitly-labeled breadth pointer whose label contains the word
"search"** ("PubMed search: ..."). For any specific claim, cite the actual
record. Enforce this as a hard offline invariant in CI.

**Publisher bot-blocks.** Large publishers (NEJM, Nature, Lancet, JAMA, many
society journals, and several government pages) return 403 or 404 to automated
fetchers while loading fine in a browser. A link checker that GETs every URL
will fail on them.

- Cite the PMC / PubMed / DailyMed / FDA / NIDDK mirror of the same record
  instead.
- A 403 is **not** proof a source is fabricated. Confirm through the mirror or
  a domain-restricted search before calling anything fake. This is a standing
  false positive in audits.

### 5.6 Verify with raw sources, not a summarizing fetcher

A summarizing web-fetch tool has invented a detail and dropped a qualifier on
an audited source, nearly producing a false high-severity finding. For audit
work, read the raw source: `curl`, `pdftotext`, the registry's own API. Also:
brand-name queries against a drug-label API can return a narrower label
variant, so verify against the cited setid, and check section numbers literally
because they differ between an injection label and a tablet label of the same
drug.

---

## 6. SEO and answer-engine optimization

Structure earns the ranking here, not keyword density. No keyword stuffing, no
formulaic FAQ padding, no fixed SEO checklist. What follows is what actually
ships.

### 6.1 Per-piece on-page

- Canonical URL of the form `<SITE>/articles/<slug>`.
- `<title>` 50-60 characters, specific, no clickbait, sentence case.
- Meta description 50-160 characters (cap the authored field at ~155 to leave
  headroom for HTML escaping, since the same string is reused for `og:` and
  `twitter:` descriptions). Precedence: `metaDescription`, then `tldr`, then
  `summary`.
- OpenGraph title / description / URL / type / site name / image, plus
  `article:published_time`, `article:modified_time`, `article:author`,
  `article:section`, `article:tag`.
- Twitter card `summary_large_image` when a 1200x630 hero PNG exists.
- Per-piece OG image pair (PNG primary, SVG fallback), regenerated whenever
  hero or title changes.
- Robots metadata that indexes public routes and noindexes private, fallback,
  and unknown routes.

### 6.2 Structured data

- `Article` JSON-LD with `author` (Organization), `publisher`, `datePublished`,
  `dateModified`, `articleSection`, `keywords`, `wordCount`, `timeRequired`
  (ISO 8601 duration), `mainEntityOfPage`, an `articleBody` snippet with cite
  markers stripped, `image` as an ImageObject with width and height.
- `speakable` targeting the key-takeaways, summary, and editorial-summary
  anchors.
- `citation` as an array of `CreativeWork` entries with `name` and `publisher`,
  not bare URLs.
- `BreadcrumbList` on every detail route, emitted in **both** the SPA head and
  the static crawler HTML (parity matters; a gap here is a real defect).
- `ItemList` on index routes.
- `MedicalWebPage` (or the domain equivalent) rather than generic `Article` for
  structured reference entries, with `lastReviewed`, `reviewedBy`,
  `medicalAudience`, and a `MedicalEntity` `mainEntity`.
- `FAQPage` only alongside a visible FAQ section, only where question-shaped
  traffic is real. Do not add FAQ or HowTo markup purely for rich-result
  eligibility; those surfaces have narrowed. Never author a novel claim through
  schema.
- `HowTo` only when each step reflects a real interaction the UI implements.
- Do not use structured data to imply diagnosis, treatment, or advice.

### 6.3 Crawler and AI-engine assets

- **Static route HTML** for public routes with a no-JavaScript body snapshot,
  so crawlers and AI engines see the full content without executing the SPA.
  The static generator must mirror the SPA's own link and block parsing so the
  two outputs agree.
- **`robots.txt`** explicitly allow-listing AI crawler user agents (GPTBot,
  ChatGPT-User, OAI-SearchBot, ClaudeBot, anthropic-ai, Claude-Web,
  PerplexityBot, Perplexity-User, Google-Extended, GoogleOther,
  Applebot-Extended, Bytespider, Amazonbot, CCBot, Diffbot, FacebookBot,
  Meta-ExternalAgent, Meta-ExternalFetcher, FriendlyCrawler, cohere-ai, YouBot,
  DuckAssistBot) with the same private-route exclusions as the wildcard rule.
- **`ai.txt`** declaring training / search / citation posture.
- **`llms.txt`** per the llmstxt.org spec: H1, blockquote summary, top-level
  navigation, content by category with counts, optional auxiliary resources.
  Never include private routes, user ids, internal identifiers, or secrets.
- **`sitemap.xml`** with per-route `<lastmod>` sourced from `updatedAt`, the
  `xmlns:image` namespace, and `<image:image>` blocks for hero images.
- Charts render as accessible DOM in the app and as a semantic definition list
  in the crawler HTML, so engines get the numbers rather than a picture. Tables
  render as real `<table>` in both.

### 6.4 Internal linking and clusters

- Follow a committed cluster map (pillar and spoke) rather than ad-hoc
  interlinking. Descriptive anchors, never "click here".
- Inline mid-paragraph internal links are encouraged where context makes them
  natural, in addition to the related-content rail.
- Deliberately avoid cannibalization: when a hub piece and a deep dive cover
  the same query, the hub answers concisely and links out rather than
  re-explaining.

### 6.5 Security and compliance in SEO assets

Never expose user-scoped data, private notes, logs, inventory, messages, or
auth state in any SEO asset. Do not add analytics pixels, ad-network code, or
consent-sensitive tracking as part of SEO work. Keep the disclaimer visible on
public educational surfaces.

---

## 7. The writer's self-audit stack (Passes 1 to 6)

Mandatory on every piece, recorded in the per-day changelog using the templates
below. This is necessary and **not sufficient**: a writer grading their own
draft is the weakest possible reviewer of it. Section 8 is the real gate.

**Pass 1 to 3: source content, numeric and acronym, tone and style.** Grade the
tone pass against the chosen register and the section 3.3 denylist, not against
a generic style guide.

**Pass 4: voice consistency end to end.** Read the opening (title, TL;DR,
key takeaways, first paragraph), three random middle paragraphs, and the
closing. Does one person write all of it, or does the register drift? Rewrite
every drift before commit.

```
#### Pass 4: voice consistency end-to-end

- Opening sample (title / TL;DR / first paragraph): <PASS|FAIL plus rewrites>
- Middle samples (three paragraphs, by section id): <PASS|FAIL plus rewrites>
- Closing sample: <PASS|FAIL plus rewrites>
- Anti-AI voice audit (section 3.3 denylist): <PASS|FAIL plus what was cut>
```

**Pass 5: scanability and trust signals.** Could a mobile reader scrolling fast
extract the answer in under 30 seconds, and does the closing make the editorial
process visible?

```
#### Pass 5: scanability and trust signals

- Mobile scan path (takeaways + section 2 answer the headline): <PASS|FAIL>
- Longest paragraph word count: <N> (cap ~120, ~80 easy-reading)
- Bottom-line callout in reader-payoff section: <YES|NO|carve-out: reason>
- Comparison data as list/table rows: <YES|NO|not comparison-shaped>
- Ranked verdicts in evidence/caution callouts: <YES|NO|none>
- Self-describing headings (no one-word generics): <PASS|FAIL plus rewrites>
- Three-place coverage for load-bearing stats: <PASS|FAIL>
- Body word count: <N>; jump list at 1,400+: <PRESENT|NOT NEEDED>
- Closing trust signals (disclaimer x1, honesty line, two-link paragraph,
  corrections pointer, citation density line): <PASS|FAIL plus what was missing>
- Key-takeaways cite-density (load-bearing bullets carrying a marker): <N of M>
```

**Pass 6: integrity and digestibility triple-audit. MANDATORY, NO EXCEPTIONS,
NO CARVE-OUTS.** The last gate before commit. Four checks; the first runs three
times.

- **Hallucination triple-check, three genuinely independent passes.** Each pass
  is a fresh read, not a skim. Walk every load-bearing claim (every number,
  percentage, dose, date, trial name, identifier, statute, regulatory status,
  named entity, approval claim, count, and reported effect) and confirm it
  traces to a real cited source that actually says it. Open or re-derive the
  source wherever there is doubt. A body claim in no cited source is a
  hallucination: cut or correct. A citation whose URL, identifier, author,
  year, or finding you cannot independently confirm is a hallucination: remove
  it. If pass two or three surfaces a single unverified claim, fix it and
  **re-run all three from the top.**
- **The per-citation ledger is how this check is satisfied, not re-reading.**
  Build a table in the changelog, one row per load-bearing claim:
  `claim -> cite id -> exact supporting quote or named table cell -> verdict`,
  plus a **source-date column** so staleness is visible per claim. Every row
  confirmed before commit. A row you cannot fill is a defect, not a pass.
- **Plagiarism.** No run of roughly 8+ consecutive words lifted verbatim
  without explicit quotation and attribution. Abstracts, prescribing
  information, and press releases get paraphrased, never pasted. Headings and
  the TL;DR must not echo a source headline.
- **Top-summary digestibility.** Read the TL;DR and the first takeaway cold, as
  a first-time mobile reader who knows nothing. It must deliver the bottom line
  in plain language in under 15 seconds: no jargon wall, no nominalization
  stack, no sentence that needs a second read.
- **Quality-degrading repetition.** No stat restated beyond its sanctioned
  three placements, no aphorism reused near-verbatim across sections, no
  closing sentence duplicating the opening, no two list items making the same
  point. The three-place rule is the only sanctioned repetition.

```
#### Pass 6: integrity and digestibility triple-audit (mandatory)

- Hallucination pass 1: <N claims checked, M failed and fixed>
- Hallucination pass 2: <N checked, M failed and fixed>
- Hallucination pass 3: <N checked, M failed and fixed>
- Citations independently confirmed (URL/id/author/year/finding): <PASS|FAIL>
- Per-citation ledger: <N rows, all confirmed | defects found and fixed>
- Plagiarism (no unattributed runs >= ~8 words): <PASS|FAIL plus rewrites>
- Top-summary digestibility (<15s, plain): <PASS|FAIL plus rewrites>
- Quality-degrading repetition: <PASS|FAIL plus what was cut>
```

---

## 8. The independent adversarial audit (the real gate)

Passes 1 to 6 are the writer's self-audit, and self-reported clean is exactly
what an independent skeptic exists to distrust. Before anything ships, run the
**12-auditor adversarial stack**, executed by someone other than the writer.

Three axes are in scope, and no CI check can see any of them: **currency**
(true at publication, wrong today), **citation correctness and hallucination**
(does the cited source contain this exact fact), and **voice** (does it read
like an AI wrote it).

### 8.1 The three rules that define it

1. **Twelve independent auditors per round.** Fresh context each, disjoint
   slices, no sight of each other's findings, no sight of the writer's own
   ledger, refute-unless-proven posture. Twelve is the floor. The proven shape
   adds two standing extras for fourteen, and those two have repeatedly found
   what the sliced dozen missed.
2. **Any HIGH fixed means a full re-run from the top.** Fresh auditors, all
   twelve, whole piece, not a spot-check of the patched paragraph. The
   documented failure mode is that **the fix introduces the next defect**: on
   one article the round-1 fix introduced a false "no results paper published"
   claim, and the round-2 fix introduced a false "the trials are completed"
   claim. Five rounds and 60 auditors to reach clean.
3. **Clean means 12 of 12 with 0 HIGH and 0 MEDIUM.** Green gates prove nothing
   about truth. Every gate was green on that same article while 13
   HIGH-severity defects were live in it.

### 8.2 The slice table

| Auditor | Slice (disjoint by construction) |
| --- | --- |
| H1 | Identity, chemistry, mechanism, constants (half-life, Tmax, receptor targets, MW, CID) |
| H2 | Human trial claims: design, n, arms, endpoints, estimand, effect sizes, p values, CIs |
| H3 | Regulatory and legal: approval status, indications, label sections, scheduling, enforcement, anti-doping |
| H4 | Safety: adverse events, contraindications, warnings, interactions, and all dose and unit math |
| H5 | Absence claims, superlatives, counts, dates, chart/table values, three-place consistency |
| C1-C5 | One disjoint block of `citations[]` each; open every assigned URL live |
| S1 | Anti-AI denylist, community-narration ban, banned characters, product coherence, reader-value bar |
| S2 | Voice consistency, digestibility, repetition, scanability, trust block, 8-gram plagiarism scan |
| X1 | Breadth and currency sweep: what changed since publication, and what the piece omits |
| X2 | Whole-draft adversarial verifier: reads it cold and tries to break the thesis |

Launch all of them in a single message so they run concurrently, with tools
that can actually fetch and search.

### 8.3 Hard constraints, restated in every auditor prompt

```
You are an independent adversarial auditor. Your posture is
refute-unless-proven: assume every claim is wrong until a source you opened
yourself proves otherwise. Finding nothing is a valid result, but "looks fine"
without having opened the sources is a failed audit.

- READ-ONLY. Report findings; never edit. The orchestrator is the only writer.
- Open every source you rely on and quote the exact supporting sentence, table
  cell, or labeled value, with the retrieval date. Never rely on memory, a
  search snippet, the citation label's own wording, or any changelog or ledger
  already in the repo. Those are the artifacts you are auditing, not evidence.
- A 403 or 404 from a large publisher is a bot-block, not proof the source is
  fake. Confirm through a mirror or a domain-restricted search before calling
  anything fabricated.
- Do not soften a finding to be agreeable, and do not inflate one to look
  productive. Apply the severity rubric literally.
- Report using the finding schema exactly. End with the coverage line.
```

### 8.4 Severity rubric

- **HIGH.** A reader could act on it and be harmed, or the piece asserts
  something false about the world. Fabricated or non-existent source; a
  citation pointing at a different paper, product, dose, population, or
  estimand; an inverted or reversed finding; a wrong dose or unit-math error; a
  regulatory status that is out of date or overstated; a safety claim the
  primary source contradicts; community narration (a hard ban).
- **MEDIUM.** The claim is defensible but the support is not: a cite backing
  the adjacent sentence and not the load-bearing one; a number rounded up,
  widened, or inconsistent between its three placements; wrong author, year, or
  identifier in a label; a review or registry record cited for results it does
  not report; a load-bearing claim with no citation; a denylist voice tell; an
  unattributed verbatim run of 8+ words.
- **LOW.** Style, precision, or polish that does not change what the reader
  believes.

### 8.5 Finding schema and coverage line

```
### <ID> | <HIGH|MEDIUM|LOW> | <axis>

- Location: <section id, and the exact quoted sentence>
- Claim as written: "<verbatim>"
- Why it fails: <one or two sentences>
- Evidence: <URL> retrieved <date>, which states: "<exact quote or cell>"
- Minimal fix: <the smallest edit that makes the claim true>
- Confidence: <high|medium|low, and what would settle it if not high>
```

```
COVERAGE: <n> claims checked / <n> sources opened / <n> findings (H:<n> M:<n> L:<n>)
VERDICT: CLEAN | FINDINGS
```

A report without the coverage line is incomplete. Re-run that auditor.

### 8.6 Consolidate into one adjudicated ledger

Fourteen reports are not a result. One ledger is.

1. **Merge** every finding into one table with stable ids (`H2-03`, `C4-01`,
   `S1-07`) so every row traces back to the agent that raised it.
2. **Dedupe.** Multiple auditors hitting one claim raises confidence, not
   severity. Keep the best-evidenced wording, list the corroborators.
3. **Adjudicate.** Auditors are wrong in both directions. Before a finding
   changes a fact, verify it against the live source yourself. "The label does
   not say this" with no quote is a lead, not a finding. Two standing false
   positives: a publisher 403 read as a fabricated source, and a real citation
   marked wrong because the auditor read a different revision of a label.
4. **Classify** into exactly one bucket, with the reason recorded:
   **Must fix before final** (every HIGH, plus MEDIUMs that change what a
   reader believes), **Should fix now** (low-risk, same edit pass),
   **Follow-up** (real but out of scope; goes to changelog known limitations),
   **Invalid** (rejected, with the evidence that rejects it). A silently
   dropped finding is indistinguishable from a missed one next round.
5. **Residual risk**, one line per axis: what the audit could not settle.

```
| ID | Sev | Axis | Location | Finding | Corroborated by | Verified by me | Bucket |
|---|---|---|---|---|---|---|---|
| H3-01 | HIGH | currency | regulatory para 2 | Indication predates the 2026-03-19 revision | X1, C2 | primary record, retrieved <TODAY> | Must fix |
| C1-03 | - | citation | closing | Auditor called the URL dead | none | 403 is a bot-block; mirror confirms | Invalid |
```

### 8.7 Fix in lanes, by file, serially

The generic "no two prompts touch the same file" rule cannot be satisfied by
slicing findings, because on a single-piece audit nearly every fix lands in one
module. **Slice by file, not by finding.**

| Lane | Write scope | Order |
| --- | --- | --- |
| A | the content module (all HIGH, then MEDIUM/LOW, then voice) | first, serial |
| B | the shared source registry | after A if A re-sourced anything |
| C | regenerated artifacts, sitemap, llms.txt, OG images | after A |
| D | the dated changelog and ledger | after A, parallel with C |
| E | guardrail docs, only if the doc audit found a defect | independent |

The lane that actually parallelizes is **across pieces** in a sweep wave: one
worktree and one pack per slug, disjoint write scopes.

**Fix-agent constraints, pasted into every lane prompt:**

- Stay inside the scope boundaries. Do not touch an unlisted file.
- **Fix minimally.** Make the smallest edit that makes the claim true. Every
  new defect this catalog has seen lived in **added** material. Rewriting a
  section to fix one number is how round 2 earns its own HIGH.
- Never invent a replacement fact. If the source does not support the claim,
  cut it, soften it to what the source does support, or re-source it and quote
  the new source in the ledger.
- When a load-bearing number changes, update all three placements plus any
  chart or table row.
- Every factual edit is backed by a source you opened yourself, quoted in your
  report with its retrieval date. Never edit from the finding's own wording.
- If a finding looks wrong, do not fix it. Return it with your evidence.
- Bump `updatedAt`. Be aware this may opt the piece into stricter invariants
  that grandfathered older content. Adjust reading time and add the jump list
  if the body crossed 1,400 words.
- Voice rewrites go last, so they operate on final facts.

### 8.8 Re-audit until clean

Re-run the full twelve with fresh agents against the edited piece. Do not tell
them what an earlier round found, what was fixed, or ask them to confirm a fix.
Add four review lenses on the re-run:

1. **Accuracy re-audit** (the twelve, unchanged).
2. **Compliance and policy**: disclaimer exactly once, no disease claims, no
   invented credentials, trust block intact, sourcing posture held, excluded
   topics absent.
3. **Editorial and product**: does the piece still clear the reader-value bar
   after the cuts, and does the harm-reduction stance survive the safety edits?
   A fix that adds risk language can quietly turn the piece into the
   fearmongering the rules ban.
4. **Docs and pack fidelity**: does the changelog ledger match what shipped,
   does the prompt pack match what was actually done, are follow-ups recorded.

Track the trajectory as a table (round, HIGH, MEDIUM, LOW, outcome). It is the
evidence the standard was met. Treat "no findings" as unproven, not as proof.

```
| Round | HIGH | MEDIUM | LOW | Outcome |
|---|---|---|---|---|
```

### 8.9 Do not merge on your own audit

Self-reported clean is exactly what an independent skeptic exists to distrust.
Push and open a PR only if asked, and hold before merge unless the owner
explicitly says to ship. Do not describe a piece as verified or ready unless
the round table ends at 0 HIGH and 0 MEDIUM, the gates are green, and manual QA
actually ran. State plainly which of those three is missing when one is.

---

## 9. Structured reference entries (the compound-library pattern)

Content that is one record per subject rather than long-form prose. Same
integrity machine, different schema.

### 9.1 Per-entry schema requirements

- `id`: kebab-case, unique, stable. It appears in URLs, security-rule
  allowlists, and every generated artifact. **A rename is a breaking change.**
- `name`, `aliases`: aliases carry brand names, manufacturer codes, and common
  community names. Search indexes them.
- `categories`: from a closed set. Do not add a category to hold one entry;
  wait for 2+.
- `regulatoryStatus`: the real status, substantive length. Never claim
  "available" when it is not approved. Research-only entries must literally
  state that no approved product exists.
- `evidenceSummary`: state directly when human evidence is thin, animal-only,
  failed in trials, or non-US.
- `evidenceTier`: pick the **lower** tier when in doubt.
- `evidenceFlag`: required whenever evidence is thin, shaky, failed,
  animal-only, non-US, or the subject carries a serious risk class. Short and
  concrete: "Mostly animal data", "Human trials did not support approval",
  "Severe hypoglycemia risk: fatal if mis-dosed".
- Schedule-reference fields (dose, frequency, route, cycle, storage): reflect
  commonly cited conventions **from the cited sources**. Do not invent numbers.
  Say "research dose", never "recommended dose". Enforce a formatting
  convention (terminal punctuation, canonical unit casing) with a test.
- `notes`: reaffirms "not a treatment" / "not approved" where applicable and
  carries the anti-doping, scheduling, topical-only, and enforcement posture.
- Public-facing "what people report using it for" copy: required, substantive,
  and **free of prescriptive patterns and dose numbers** (enforce with regex
  denylists in tests).
- A plain-language card (what it is, what people use it for, what the science
  shows, the catch) at an eighth-grade reading level, subject to the same
  denylists.
- `contentReview`: `status`, `checkedAt`, `summary`, `sources[]`.

### 9.2 Content-status enum

- `approved_label_reference`: approved-label reference while a compounded or
  derived product is explicitly disclaimed as not approved.
- `label_verified`: approved or manufacturer reference content drives the
  fields; must attach an official label or prescribing-information source.
- `investigational_verified`: trial context only; never presented as approved
  or available.
- `research_reference`: no approved label exists; fields summarize commonly
  cited research conventions as educational reference. Empty sources tolerated
  only when no public source exists, and `evidenceSummary` must say so.
- `research_review_required`: needs editorial review before the fields are
  presentable.

### 9.3 Public-copy denylists

Enforced by tests against the serialized public JSON:

- No sourcing, purchase, or vendor language ("where to buy", "legal to buy",
  "source exchange", "vendor", "per vendor").
- No post-cycle / PCT planning language.
- No prescriptive patterns ("always follow", "never cold turkey", "take with
  food", "once daily") and no dose numbers in the community-use or
  plain-language fields.
- No em dashes anywhere in entry copy.
- Class-specific risk framing never softens on edit relative to the existing
  entry.

### 9.4 Generated artifacts and allowlists

- Regenerate every derived artifact after any entry, config, or schema edit,
  and commit the regenerated JSON in the same change. Never hand-edit a
  generated file.
- Feature subsets (pickers, loggers, previews, templates) are **explicit
  allowlists**, not derivable from a `type` or `categories` field. High-risk
  entries stay excluded even when their schema type would admit them.
- Any decoupled frozen snapshot of the catalog needs a manual re-sync in the
  same change, or its parity test goes red. Know which fields it mirrors.
- Security-rule id helpers must match the generated ids exactly; enforce with a
  parity test.
- Guard the index bundle against accidentally importing the full-detail
  artifact. Index surfaces read the lightweight index; detail routes load the
  full record for that route only.

### 9.5 Per-entry pre-merge checklist

1. `contentReview.status` matches the real regulatory state.
2. At least one real source when a public primary exists; empty only when none
   applies, and `evidenceSummary` says so.
3. `regulatoryStatus` states the real status with the required literal wording
   for research-only entries.
4. `evidenceTier` is conservative.
5. `evidenceFlag` populated wherever evidence is thin or risk is serious.
6. Schedule fields reflect cited conventions; no invented numbers.
7. `notes` carries the risk, scheduling, and enforcement posture.
8. Community-use copy exists, is substantive, and is free of prescriptive
   patterns and dose numbers.
9. No em dashes anywhere in entry copy.
10. No sourcing, purchase, or PCT language in serialized public copy.
11. Side-effect content framed as user accounts, never as guidance.
12. Subset allowlists reflect intent.
13. Security-rule id helper updated.
14. Every generated artifact regenerated and committed in the same change.
15. Every source URL verified to resolve to a live page that supports the
    claim. None assembled from a search-result slug or a guessed filename.
16. The triple audit ran three separate independent times.
17. A per-claim ledger was produced and every row confirmed, per the Citation
    Correctness Standard, with a freshness row recording that status and
    evidence fields were verified current as of today (or old value to new
    value).

### 9.6 Auditing an entry

The section 8 machine applies, with these substitutions: slice the five
hallucination auditors over **fields** (identity and chemistry; the
plain-language card; regulatory status and evidence; risk, flags, and notes;
community uses, reviews, and schedule fields). C1-C5 split the entry's sources.
S1 and S2 check the public-copy denylists. The freshness ledger row is
mandatory. Lane C becomes the artifact-regeneration lane.

---

## 10. Beginner guides and on-ramp content

A bounded program of free, plain-language "start here" guides, one per popular
subject. It is a content type, not a new surface.

- Ships as a normal typed article on the easy-reading register, tagged both
  `easy-reading` and `beginner-guide`.
- Cross-linked both directions: the guide links the subject's reference entry
  and the anchor deep-dive article; the reference page links back via a slim
  generated map (compound id to `{slug, title}`) so the detail chunk never
  pulls article prose.
- Free to everyone, always. No paywall, no sign-in wall. The only optional gate
  is an email capture on a downloadable PDF, and the on-page guide is complete
  without it.

**Fixed skeleton** (so the set reads as one series):

1. TL;DR: what it is and what people use it for, front-loaded.
2. Key takeaways: 4-6 bullets, hard-fact bullets carry their citation.
3. "What it is, in plain English": define in half a sentence, then the class
   and how it is taken. No mechanism lecture.
4. "What people use it for": the honest community-use picture, matching the
   reference entry. State plainly where human evidence is thin.
5. "What the science actually shows": the evidence tier in plain language with
   real numbers cited at the point of claim.
6. "The catch" (a caution callout): **derive this from the live reference
   entry, never from memory.** Open the record, read its risk flags and notes,
   and carry EVERY acute or serious risk it names. The citation and
   hallucination passes verify what you wrote, not what you omitted, so a
   dropped risk will not be caught automatically. Matching the live entry is
   the only guard. If the guide correctly asserts a posture the entry omits,
   cite the primary source for it and log the catalog gap as a follow-up rather
   than letting the two surfaces disagree.
7. "How people take it": practical basics in service of doing it safely. Point
   at the calculator and the reference schedule block rather than hardcoding
   numbers that then drift.
8. "Where to go deeper": explicit links to the reference entry and the anchor
   article. This is the hand-off.
9. Closing section with the disclaimer and the full trust block.

**Downloadable eligibility.** Only stable pieces. Never mark an investigational
or regulatory-moving guide downloadable: a frozen PDF of a moving fact goes
stale silently.

---

## 11. Freshness and living content

- **Living formats** (status trackers, shortage lists, periodic digests,
  legality tables) state an as-of date plainly in the prose, set `updatedAt`
  honestly, and carry a one-line caution callout linking the authoritative
  tracker: "this changes; check the primary source before you act." Never
  present a moving target as permanent fact.
- **Timelines**: every dated row carries a cite. Do not smooth over gaps with
  invented connective events.
- **Reference tables** (side effects, legality by jurisdiction): every row is a
  discrete factual claim needing its own cite or a clearly cited shared source.
  Get every cell right or leave it explicitly "unclear, see source". Never
  guess a cell.
- **Digests**: short items, each with a cite and a one-line "why it matters".
  Date-stamp it. Five real items beat ten with filler.
- **Currency is an audit axis.** A piece that was true at publication and is
  wrong today is a HIGH finding, not a nitpick. Auditor H3 pulls the current
  record as of today; X1 sweeps for what changed since publication.
- **Flag, do not silently fix, link rot** in published pieces. Report the dead
  citation with the proposed replacement; do not quietly rewrite a published
  claim.
- A freshness agent proposes, never publishes. The pull request is the publish
  gate.

---

## 12. Workflow and gates

### 12.1 Required reading before writing

The repo's operating guide and agent workflow; the content-library guardrail
(voice posture, Citation Correctness Standard, imagery, JSON-LD); the workflow
contract with the audit-pass templates; the register rules for the chosen
voice; the schema file; then skim 2-3 recent pieces for live conventions and
the newest changelog.

Then inspect repo state: current branch, `git status --short`,
`git log --oneline -5`. Identify uncommitted work. **It is not yours.**

Restate scope before implementing: what changes, what does not, assumptions,
risks.

### 12.2 Branch and worktree isolation

Never push the default branch from a shared root checkout. Other agents share
the tree and rebase it mid-task; a stray rebase clobbers committed work. Do
non-trivial work in an isolated worktree cut from fresh remote main:

```
git fetch origin
git worktree add -b <type>/<slug> /tmp/<repo>-<slug> origin/main
ln -s <repo-root>/node_modules /tmp/<repo>-<slug>/node_modules
```

Record the base commit hash in the changelog. Local main is chronically stale;
fetch and reason about `origin/main`. Use `git rev-list --cherry-pick
--right-only` (not hash ancestry) to tell genuinely-unmerged work from
squash-superseded work.

### 12.3 Gates, in this order, all green

```
<regenerate catalog index>        # summaries + lazy body loaders; parity test fails on drift
<regenerate SEO assets>           # required if the title changed
npm run lint
npm run build                     # the real type gate; a bare typecheck can skip a referenced project
npm test                          # the FULL suite, never a scoped run
<citation checker> --verify-titles
<article SEO lint>
<sitewide SEO check>
<docs check>
<OG image regeneration>           # only if title or hero changed
rg -n '[\x{2014}\x{2013}\x{2018}\x{2019}\x{201C}\x{201D}]' <file>   # must return nothing
```

Scoped test runs miss cross-file assertions and have already cost a red main.
If a command cannot be run, document the command, why, and the residual risk.
Never bypass hooks, skip tests, or weaken a data invariant to get green.

**Manual QA on the rendered page:** the detail route loads, key takeaways and
the reader-payoff section answer the headline, every inline link resolves, the
disclaimer appears once in the body, charts and tables render with their
values, and a 390px viewport has no horizontal scroll.

### 12.4 Changelog

Per-day changelog at `<CHANGELOG_DIR>/CHANGELOG_ARTICLES_YYYY_MM_DD[_<slug>].md`
with the required doc-role banner as line 1 if the repo uses one. It carries:

- What changed and why, headline defects first: one subsection per HIGH with
  before, after, and the live source quote that settles it.
- The register line ("Voice register: easy-reading") so a future audit grades
  against the right rule.
- The full per-citation ledger with source dates.
- The consolidated findings ledger including rejected findings and follow-ups.
- The adversarial round table and auditor-by-auditor verdicts.
- The Pass 4 / 5 / 6 blocks.
- Gate output, manual QA results, known limitations, residual risk.
- Affiliate opportunities flagged, or an explicit "none", so a future audit
  knows the question was considered.

Add a one-line index entry to the rolling changelog. On a multi-piece sweep,
skip the per-piece index line (it conflicts on every PR) and batch them at the
end of the wave.

If the work moves a tracked feature status, edit the structured status source
and run the sync script. Never hand-edit generated state docs.

### 12.5 Commit and ship

- One coherent conventional commit per piece: `feat(articles): add <slug>
  article`, or `fix(articles): currency, citation and voice audit of <slug>`.
  Do not bundle unrelated changes.
- Push the branch, open a PR. If merging is the deploy, say so explicitly in
  the hand-off.
- Verify live: fetch `<SITE>/articles/<slug>` and confirm HTTP 200 with the
  title in the HTML. Allow a few minutes of deploy lag before treating a miss
  as a failure.
- Record the shipped commit hash and live URL in the changelog.
- Know the repo's commit-identity requirement (some deploy pipelines block
  certain author emails). Set it per-repo before the first commit.

---

## 13. Distribution drafts (community posts)

Where the operator distributes a piece by hand, the deliverable is a
ready-to-post draft. Nothing is auto-posted.

- **Lead with the substance, in full.** The post stands on its own and is
  useful even if nobody clicks. Open with the answer or the most useful
  specific, then the scannable points. Every claim is supported by the article,
  so by a cited source. Invent nothing; never fabricate an anecdote or a quote.
- **The link is never the payload.** Place the live URL once, near the end,
  framed plainly ("full write-up with sources: <url>"). No "click here for
  more" scaffolding. The body must deliver enough that a reader who ignores the
  link loses nothing essential.
- **No marketing scaffolding.** No brand pitch, no "check out <BRAND>", no
  verbatim legal-disclaimer footer, no promo-trailer cadence ("X is all over
  the place right now", "here's where the evidence sits"). That shape is the
  exact signature of automated marketing, and a real post in that shape got
  called spam ("be gone bot", "looking for clicks").
- **Run the anti-AI voice audit on the draft, not just the article.** The full
  section 3.3 denylist plus a one-human-voice read.
- **Honest title.** The question the reader is actually asking, or the one-line
  truth the piece lands. Sentence case, no clickbait, no em dashes.
- Same content rules as the article: no em dashes, no curly quotes, no
  superlatives, no disease claims, and the product-coherence stance (a peer
  sharing what works, never the brand lecturing the community it serves).
- **Flag the posting reality every time.** Many communities ban promotion and
  external self-links outright, and posting from an obvious brand account makes
  it worse. Say plainly which kind of community the draft is safe for, and note
  that where link rules forbid it the operator should strip the URL and post
  the substance alone. The draft is written so it survives that cut. Where the
  piece just restates the label, say there is no honest post and skip it.

Record the draft in the changelog with the live URL and the safe-to-post note,
and deliver it in the hand-off message, not only in the changelog.

---

## 14. Pre-commit checklist

- [ ] Reads like one specific person who knows the field wrote it, top to
      bottom.
- [ ] Anti-AI denylist swept (section 3.3), including the catch-all reread.
- [ ] No em dashes (`rg` returns nothing), no curly quotes, no emoji.
- [ ] Disclaimer present exactly once, in the closing section.
- [ ] All four trust signals plus the citation-density footer present.
- [ ] Every load-bearing claim cited at the point of claim; every cited source
      opened and quoted; metadata matches the record; numbers stated exactly.
- [ ] No search URL carrying a specific claim.
- [ ] Key-takeaways bullets with hard claims carry inline cites.
- [ ] Three-place coverage for every load-bearing number, identical everywhere.
- [ ] Paragraphs under the register cap; payoff leads; visual blocks used.
- [ ] Headings carry the claim; no one-word or curiosity-gap headings.
- [ ] Jump list present at 1,400+ words, correctly absent below.
- [ ] Hero photo real, topical, unique, credited; OG regenerated if needed.
- [ ] Register tagged and recorded in the changelog.
- [ ] Living content carries an as-of date and a check-the-source caution.
- [ ] Full self-audit stack (Passes 1-6) run and recorded, including the
      three-pass hallucination check with counts and the per-citation ledger.
- [ ] Independent 12-auditor stack run to 0 HIGH and 0 MEDIUM, round table
      recorded.
- [ ] All gates green, full test suite (not scoped), manual QA at 390px done.
- [ ] Changelog written; index line added; status source updated if a milestone
      moved.
- [ ] Distribution draft written, slop-audited, with the safe-to-post note.

---

## 15. Appendix: what has actually gone wrong

Hand these to auditors as leads. Every one is a real, shipped defect.

**Accuracy**

- An inverted body-composition claim that cited one half of a paired figure and
  dropped the other, reversing the meaning.
- An estimand mismatch: a treatment-policy figure compared against an efficacy
  figure as if like-for-like.
- A headline percentage lifted from a 62-person sub-arm of a 338-person trial,
  with the base rate hidden.
- Cross-trial arithmetic: adding results from separate trials with different
  populations and calling the sum meaningful.
- A figure attached to product A when it was product B's contribution in a
  trial A was never in.
- Dosing advice generalized past its tested scope.
- A fabricated author name and two papers with their identifiers swapped.
- A fabricated trial parked on a search URL, which returns HTTP 200 and so
  passed every automated check.
- Fictional registry records: eight look-real "recruiting" entries from one
  sponsor, two of them cloning a real company's trials. Verify registry records
  against the registry API, and never assert a named sponsor is faking.
- A guessed label-PDF filename that shipped a live 404.
- A citation label that truncated a clinical instruction, and shipped that
  truncated instruction as visible link text for two audit rounds.

**Process**

- **Every new defect lived in ADDED material.** On dense pieces, fix minimally.
- **Self-reported ledgers are not evidence.** The changelog ledger is the
  artifact under audit, not proof.
- **Green gates prove nothing.** 13 HIGH-severity defects were live while every
  gate passed.
- **The fix is where the next defect comes from.** Two consecutive rounds each
  introduced a brand-new false claim while fixing a real one.
- **A three-agent audit gate found a defect every single round** it was run.
- **Corroboration is not verification.** A sibling article agreeing with a
  claim is the least independent check available.
- **A summarizing fetch tool invented a detail** and dropped a qualifier on an
  audited source, nearly producing a false HIGH. Read raw sources.
- **Bumping `updatedAt` can turn on stricter invariants** that grandfathered
  older content. Invariants that assert in a loop report only the first failing
  item, so the first reported slug is not the failure set.
- A title change requires regenerating the index, the SEO assets, and the OG
  cards; OG cards keep baking the old title until regenerated.
- Value-importing a content barrel into client code dragged ~345KB gzip of
  prose into the bundle. Summary surfaces import summaries; detail pages load
  one body chunk on demand. Type-only imports are fine.
