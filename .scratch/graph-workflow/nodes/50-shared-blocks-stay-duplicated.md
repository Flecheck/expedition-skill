# Whether the five contracts' shared blocks stay duplicated

Type: grilling
Status: resolved

Blocked by: 54

## Question

216 lines and 2,800 words — **17% of the shipped corpus by word** — are four redundant copies of two
byte-identical sections; the vocabulary has seven homes for 17 terms. The standard names this a failure mode
with a named remedy; `map.md`'s standing preference and flags `22.5` and `35.3` name it a deliberate purchase of
exact agreement, and a code-review skill's finding was already suppressed against it once. **Neither side is
wrong**, which is why this is the human's and not a worker's.

Measured by [Review every shipped file against `/writing-great-skills`](47-review-shipped-skills.md)'s worker,
verified by hash over both section ranges: `## When you raise a flag` (21 lines, 276 words) and `## When a node
you report is an implementation node` (33 lines, 424 words) are byte-identical across all five worker contracts
— 54 lines and 700 words per contract, 53 non-blank lines appearing in all five. Corpus: 8 files, 1,786 lines,
16,869 words.

**The record's own case for keeping it**, all of it real: `map.md`'s *"completeness for an agent beats brevity
for a human, and the density of these files is correct rather than a failure of editing"*; flag `35.3`, whose
worker wrote them byte-identical *"to buy exact agreement across the five"* while naming the cost as *"a
five-way edit… in a set of files nothing checks for divergence"*; flag `22.5`; node 22's report that a
code-review skill's smell baseline **already flagged this duplication and suppressed it** against condition 9;
and node 31's record of a checker discarding a related finding because *"the map endorses completeness for an
agent reader over brevity"*.

**Three things the human has that nobody else does.** `map.md:49` asks for *"a worker contract that stands alone
as a file rather than depending on skill invocation"*, while node 22's condition 9 hardened that to *"everything
binding on the worker is in the file, so a runner with no skill-invocation mechanism gets the same instructions
by reading it."* **A plain-file pointer is not skill invocation, and a skill-less runner can follow one** — that
gap is where a remedy would fit if it fits anywhere, and closing or keeping it is the human's call. Second,
[Write the cascade worker's contract](44-cascade-worker-contract.md) will make this a **seven-way** edit.
Third, open nodes 32, 40, 41 and 48 each edit the same five files.

Sizing, for whether this is sprawl or density: `expedition-checker/SKILL.md` at 318 lines / 3,253 words is 2.3×
the plugin's longest `SKILL.md` by line and 1.6× by word; `graph-conventions.md` at 384 lines / 3,529 words
exceeds the plugin's largest disclosed reference.

**Options as that worker framed them:** keep it and record the standard as consciously declined; relax condition
9's one-file reading to permit a plain-file pointer inside the skill tree; or keep it and let [What keeps the
shipped files consistent when a decision changes a term](29-shipped-file-consistency.md) supply the divergence
check the record says nothing performs.

## Why this is blocked, and it is the manager's wiring rather than the reporting worker's

*The manager's note.* That worker reported this with **no blockers**, correctly on what it knew. It is blocked
here because the standard its whole argument is phrased in was superseded upstream the same day, and the change
lands on this question harder than on any other:

- The old charge was **Duplication**, remedied by **External Reference**. The new text keeps duplication but
  adds **sprawl** as a distinct failure mode — *"a document simply too long, even when every line is live and
  unique"* — which is a **different** charge, and the one the sizing figures above actually support.
- One new sentence contradicts the framing directly: progressive disclosure is *"Not primarily a token
  optimisation: it is how the hierarchy is protected."*
- And the new mechanics file supplies **an option the old standard did not offer**: *"A model-invoked skill whose
  content is all reference is also one home for shared reference: another skill can invoke it, so reference
  needed by several skills lives in one place."* That is a fourth option — make the shared reference a
  model-invoked skill the five contracts can reach — and it bears on the fact that
  `.claude/skills/expedition/graph-conventions.md` is reached by no pointer from anywhere today.

Grilling the human on this in the superseded vocabulary would spend the scarce resource on an argument that has
moved. Blocked by [Re-review the shipped files against
`/writing-for-agents`](54-review-against-writing-for-agents.md), which re-sites it.

## Annotation: both figures in the question above have moved, and a token price now exists

*Filed by the manager from two research nodes that resolved while this was blocked.* Do not re-derive these.

**Corpus figures, re-measured by [Re-review the shipped files against
`/writing-for-agents`](54-review-against-writing-for-agents.md)** — the two sections are still byte-identical
across all five contracts by md5, at 21 lines / 276 words and 33 lines / 424 words, so 216 lines and 2,800 words
in four redundant copies stands. **The corpus is now 8 files, 1,804 lines, 17,067 words**, so the share is
**12.0% by line and 16.4% by word**, where the question above says 1,786 / 16,869 / 17%.

**The charge has changed, and it was always available.** The right charge is **sprawl**, not duplication —
*"a document simply too long, even when every line is live and unique. Attention thins across the excess"* —
and node 54 established that this was a named, distinct failure mode in the **old** standard too, so node 47
could have raised it and did not. Sizing against the current standard: `expedition-checker/SKILL.md` is 3.9× its
`SKILL.md` by line and 1.8× by word; `graph-conventions.md` is **5.0× and 2.1×**.

**The two homes the standard names are both old, and one of them already exists.** A model-invoked all-reference
skill another skill invokes (verbatim in the old glossary; costs one always-loaded description), or a plain file
outside the skill system any document points at. Node 54's worker: *"`graph-conventions.md` is already the second
shape and is missing only the pointer, so that route costs one line per contract and no context load."* And
`map.md:51`'s insurance is against **skill invocation**, which a plain-file pointer is not.

**The token price, from [How an agent workflow and its skills reduce their own token
cost](52-token-cost-of-a-workflow.md), and it argues against acting on tokens alone.** The 700 duplicated words
are ~4,060 chars ≈ **~1,015 tokens per worker spawn**, paid once at full uncached rate and then cached inside
that worker. Against the **~19,840 tokens of `map.md`** that same worker reads cold, **the duplication is ~5% of
one worker's opening read.** That worker's inference, reported rather than decided: *"on token cost alone the
duplication does not clear the bar for a remedy that costs exact agreement, and the argument for changing it has
to stand on maintenance rather than on tokens."*

**And a counterweight whoever grills this must hold.** The compression literature's penalty falls on
**format-bearing** text, not semantic content — *"compression rates exceeding 30% led to failure on all tasks"*
in one measured agent scenario. The two duplicated sections are **exactly** that class: a five-part handover
with named parts and a flag form. So the safe target is prose that explains why, and the unsafe target is the
shapes.

## Annotation: a ninth file joined the corpus, and the human ruled on that one file alone

*Filed by the manager at [Write the first version of the manager's skill](76-write-the-manager-skill.md)'s third
correction round. **Not an answer to this node**, which stays open and still owns the question for the corpus.*

**New measurement, from a blind checker holding only the two files.** The manager's contract, shipped at node 76,
shares **82 eight-grams with `graph-conventions.md`**, clustering into **nine passages** restated near word-for-word
with *the manager* swapped for *you*: three against that document's `### The human's words, in either log`, three
against `### Raise a flag` and `### Settle a flag`, one against its acceptance-condition section from the new file's
`## The checker`, and two more against the same from its `## Acceptance conditions`. The enumerator is on node 76's
`## Review` under run 1.

**This is a different shape from the 216 lines this node was written about**, and worth separating. Those are
byte-identical blocks across five sibling contracts, written that way deliberately to buy exact agreement between
files that say the same thing to different readers. These nine are one document restating another document's
operative content across a stated division of labour — the new file's own sentence being *"This contract says what
you do; that document says what the files look like when you have done it."* **A ninth file makes it a nine-way
edit, and this instance also crosses the division rather than sitting inside it.**

**The human directed the repair on that one file.** Their word, `verbatim`: *"send it to the worker"*, against the
manager's recommendation that it be left to this node. Recorded as a divergence on node 76. **What that settles is
node 76's file and nothing else** — the five worker contracts go on duplicating, so the corpus is now deliberately
inconsistent until this node answers, and that inconsistency is itself new evidence rather than a defect to fix
here.

**The constraint that governed the repair, unchanged from this node's own finding.** Clause 3 of node 76's condition
requires the file to stand alone, so a rule may not simply become a pointer wherever one exists. What made any
remedy possible is the gap **this node identified first**: a plain-file pointer is not skill invocation, and a
skill-less runner can follow one.

## Interview

### Attempt 1

*The attempt's routing key does not survive the manager's session, so it is not recorded here.*

*Banked at hand-back: this question queued behind [node 144](144-make-the-rules-file-stand-alone.md)'s gate, [node
165](165-measure-whether-a-fed-file-earns-its-place.md)'s question, and [node
171](171-carry-the-record-node-reading-rule-into-the-rules-file.md)'s gate. Relayed once all three cleared.*

**The worker's question, pasted as it wrote it.**

> I have what I need. Node 54 (my blocker) is resolved, and I've re-measured the corpus — several of my node file's figures have moved.
>
> NODE:          Whether the five contracts' shared blocks stay duplicated
>
> ABOUT:         Two sections — `## When you raise a flag` and `## When a node you report is an implementation node` — are byte-for-byte identical in five of the six worker contract files. This node decides whether they stay that way or move to one file the five point at. It's being decided now because a large part of the open implementation backlog edits exactly those files, and several edit exactly those blocks, so the answer changes how that backlog is worked.
>
> SO FAR:        I read the node, the map, the decisions index, node 54's re-review (my blocker), and I re-measured the shipped files today rather than trusting the node's stored numbers. Four things I found:
>
> **1. The duplication is real and unchanged, but the node's arithmetic is stale.** Both sections are still md5-identical across grilling, implementation, precondition, prototype and research — 54 lines / 700 words per contract, so 216 lines / 2,800 words are redundant copies. But the corpus has grown from 8 files / 17,067 words to **9 files / 2,665 lines / 27,104 words** since that was measured. So the duplication's share has **fallen from 16.4% to 10.3% by word** (8.1% by line). It didn't grow; everything around it did.
>
> **2. The sprawl charge doesn't actually land on it.** No worker ever reads more than one contract — each reads its own 54 lines once. The 216-line figure is a corpus statistic no reader experiences. And the file that *is* oversized — the checker contract, 405 lines, the one node 54 priced at 5× the standard's own skill — shares **zero** duplicated lines with the other five. Deduplication would not shorten it by one line.
>
> **3. Two things I found that the node file doesn't know.** First, there is **more** duplication than the 216 lines: another ~165 line-instances / ~1,700 words of shared boilerplate (the glossary block, `## What you read`, the resume template, the handback template). In the grilling and prototype contracts, **93 of 225 lines — 41% — sit in some block shared with 3+ siblings.** Second, the node says `graph-conventions.md` is "reached by no pointer from anywhere" — that is **no longer true**: the manager's contract, shipped since, points at it five times, including *"beside this file. Read it before you touch an effort's files."*
>
> **4. The constraint the node treats as the blocker has already been relaxed, by you.** Node 22's condition 9 said everything binding on a worker must be *in* its file. But node 143 landed four commits ago and sends an implementation worker to `map-implementation-rules.md` for the standards it is held against. So a contract already points out of itself for binding material. Ground rule 2 as the map states it today only forbids depending on *a skill being invocable* — a plain-file pointer isn't that. **The remedy is available; the question is whether it's worth taking.**
>
> Settled on my own authority (returning as assumptions): the checker contract is out of scope here, since it shares no duplicated line; and I read the corpus-share percentage as a maintenance statistic rather than a cost any reader pays.
>
> The measured token price stands from node 52: ~1,015 tokens per worker spawn, about **5% of that worker's opening read** against `map.md`'s ~19,840.
>
> ASK:           Do the five worker contracts keep their shared blocks duplicated, or do those blocks move into one file that all five point at?
>
> RECOMMENDED:   **Keep them duplicated — and pay for that with a mechanical divergence check** (a tenth check in `graph-conventions.md`: the two sections' hashes match across the five contracts).
>
> What this rests on, in order of weight:
>
> - **The map's own rule points here.** It prioritises token-use work but explicitly refuses "prioritising one whose size has not been measured." This one *is* measured, and it's 5% of one worker's opening read. It doesn't clear the bar.
> - **The charge against it fails on measurement.** Sprawl is about attention, and no reader's attention is spent on the duplication — each reads one copy. The share is falling on its own as the corpus grows.
> - **These blocks are duties performed at handover time, not reference.** A worker reads `## When a node you report is an implementation node` at the moment it writes a condition. A pointer inserted there is a coin-flip on whether it gets followed — and badly-written conditions are a defect this graph has already had to open nodes to repair (148, 163). The contract's own line is *"what you write loosely here is paid for there."*
> - **The one cost genuinely being paid is silent divergence** — five files, nothing checking they agree. Node 109's acceptance condition is literally written as a five-way edit with a "correct the count in all five" rider, and it's blocked because "claiming this before both land would put three workers in one file." A hash check answers that directly, costs no worker any context, and touches no ground rule.
>
> The strongest argument *against* my recommendation, which I'll state rather than hide: a check catches divergence but does not reduce the labour, and nine-plus open nodes still each have to make the same edit five times — soon seven, once the cascade worker's contract exists.
>
> ALTERNATIVES:
>
> - **Move both blocks to one new plain shipped file the five contracts point at.** Cuts grilling and prototype by ~24% each, and the extra boilerplate would take them to ~45%. Costs one line per contract, no always-loaded context, and now has precedent (node 143). Against it: the material is no longer in front of its reader at the point of use, and `graph-conventions.md` would then hold a third statement of the same rules in a third voice — the division node 76 just drew.
> - **Move them into a model-invoked all-reference skill the contracts invoke.** Same benefit, plus ~80 bytes of always-loaded description, but reachable only by invocation — which is precisely what the map's insurance for a future non-Claude harness was written against. I set this aside as strictly worse than the plain file for this effort.
> - **Keep it with no check at all, and record the standard as consciously declined.** Cheapest possible answer; leaves the one real cost silent, which is the cost that is actually being paid.
> - **Deduplicate the wider boilerplate too** (the glossary block, `## What you read`, the templates) rather than just the two named sections. Larger saving, larger blast radius; I'd treat it as a separate decision if you want the first one.

**The human's reply, `verbatim`.**

> keep them duplicated

**The option it takes**, quoted from the worker's own `RECOMMENDED` and attributed to the worker:

> **Keep them duplicated — and pay for that with a mechanical divergence check** (a tenth check in
> `graph-conventions.md`: the two sections' hashes match across the five contracts).

***The manager's note.*** **Not a divergence**: the reply takes the `RECOMMENDED` and none of the four alternatives.
**What it does not say either way is the second half of that recommendation** — the divergence check — which the
worker offered as the price of keeping the duplication rather than as a separate option. The manager has not read the
reply as settling it and has not decided it; it is the worker's to put back or to treat as carried, and the manager
has said so in resuming it.

## Answer

*Pasted as the worker wrote it.*

> ## The blocks stay duplicated, and nothing ships
>
> The human's words, `verbatim`: *"keep them duplicated"*. Taking the worker's `RECOMMENDED` and none of the four alternatives; not a divergence.
>
> **No shipped file changes, and no node is minted to change one.** The record of the standard being consciously declined is this node. A reader asking what this decision altered in the tree is answered: nothing.
>
> ### What the decision was taken on, re-measured rather than inherited
>
> The figures this node carried were stale, and its annotation's *"Do not re-derive these"* would have carried them into this answer. Measured on disk at resolution:
>
> - The shipped corpus is **9 files, 2,726 lines, 27,735 words**, where this node said 8 files, 1,804 lines, 17,067 words.
> - The two sections are **identical in content across five contracts**, verified by md5 over both ranges. **54 lines and 684 words per contract; 216 lines and 2,736 words in four redundant copies.** The claim of byte-identity stands.
> - **The share has fallen, not grown: 7.9% by line and 9.9% by word**, against the 12.0% and 16.4% this node recorded. The duplication did not move; the corpus grew about 62% by word around it.
> - **The checker contract carries neither block.** This is a five-file matter, not six.
>
> ### The three grounds
>
> **The token price is measured and does not clear the bar.** ~1,015 tokens per worker spawn, about 5% of that worker's opening read against `map.md`'s ~19,840. `map.md`'s own rule refuses *"prioritising one whose size has not been measured"*; this one is measured, and it is small.
>
> **The sprawl charge does not land on the duplication.** No worker reads more than one contract, so the 216-line figure is a corpus statistic no reader experiences. And the file that is genuinely oversized, the checker contract at 405 lines, shares neither block: deduplication would not shorten it by a line.
>
> **The blocks are duties performed at handover time, not reference.** A worker reads the implementation-node section at the moment it writes a condition. A pointer inserted there is a variance lever on exactly the artifact this graph has already opened nodes to repair. The contract's own sentence is *"what you write loosely here is paid for there."*
>
> ### Why no divergence check was added, which was the other half of the recommendation
>
> **Its proposed home was wrong.** All ten mechanical checks in `graph-conventions.md` are checks on **an effort's graph**. A check that the workflow's own shipped source files agree with each other is not a graph check. It is live on this dogfood effort and dead on every other, and shipping it puts a permanently inapplicable check into every effort, against ground rule 1.
>
> **And the human has already refused it.** Node 29's part 3, assented to `verbatim` as *"ok for 29"*, is *"nothing is added to the mechanical checks, and nothing to any acceptance condition."*
>
> **The protection it was meant to buy already exists.** Node 94's extent rule requires every condition addressing a defect with instances to carry an enumerator or a bounding set. Applied to any edit of these blocks, that rule *is* the divergence check: an author who must enumerate the instances cannot silently miss four of five.
>
> ### One caution, from running the proposed check
>
> The worker ran the hash comparison it had recommended. **Its first run reported a divergence in the research contract that was not there** — an artifact of that section being last in the file, so the extraction captured no trailing blank line. The content is identical. Recorded because it is evidence about the remedy that was declined: **even the exact, decidable version of this check has an edge case, and its first run produced a false positive.**

**What the worker reported its work invalidates, pasted as it wrote it.**

> **Node 54's finding A is now substantially false, and node 54 is resolved.** It found that *"a quarter of the shipped corpus is read by nobody"* — **454 lines and 4,057 words** — resting on the verified fact that *"`.claude/skills/expedition/` holds no `SKILL.md` at all."*
>
> Node 76 shipped `.claude/skills/expedition/SKILL.md`. Verified today: it points at `graph-conventions.md` **five times**. So the whole set node 54 priced as unreachable is now reachable from a model-invoked skill by a two-hop chain.
>
> **What survives, narrowed:** no *worker contract* points at any of the three. The reachability runs through the manager's skill alone, so the files are reachable by the manager and unreachable by every worker. That is a real and much smaller finding than the one on record, and it bears on node 61, whose case rests on `scribe` living in the file nothing points at.
>
> **Also stale, in this node's own text:** its statement that `graph-conventions.md` *"is reached by no pointer from anywhere today"*, and both corpus figures under its second annotation, which the annotation instructs its reader not to re-derive.

## Flags

*All three are the worker's own text, pasted. The ids and links are the manager's bookkeeping and nothing else.*

`50.1` `ASSUMPTION` **· settled** — **Dropped the divergence check rather than putting it back to the human as a second question.** The worker offered the check as the price of keeping the duplication; the human's *"keep them duplicated"* reaches it either way. It judged the half unsettled, then found two facts that settle it without spending the human: the proposed home is a per-effort graph-check list, so a check over the workflow's own source would be dead on every effort but this one and would breach ground rule 1; and node 29's part 3, assented to as *"ok for 29"*, already says nothing is added to the mechanical checks. It also found that node 94's extent rule supplies the same protection node-by-node. Its contract says to find facts rather than ask for them, so it dropped the check and recorded this instead of relaying.

`50.2` `ASSUMPTION` **· settled** — **Scoped the checker contract out of the decision.** The node and its annotations discuss "the five contracts" while the shipped set has six worker contracts. The worker measured rather than assumed: the checker contract contains neither duplicated section. So the decision governs five files and the checker's size, which is the corpus's real outlier at 405 lines, is untouched by it.

`50.3` `ASSUMPTION` **· settled** — **Read the corpus-share percentage as a maintenance statistic rather than a cost any reader pays.** This is the analytical move the recommendation rested on: because no worker reads more than one contract, the 216 redundant lines are never in one reader's context, so the duplication cannot be charged with sprawl, whose whole content is spent attention. The human assented to the recommendation this produced rather than to the reasoning itself.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
