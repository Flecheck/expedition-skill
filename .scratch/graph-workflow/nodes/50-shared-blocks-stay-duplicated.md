# Whether the five contracts' shared blocks stay duplicated

Type: grilling
Status: open

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
