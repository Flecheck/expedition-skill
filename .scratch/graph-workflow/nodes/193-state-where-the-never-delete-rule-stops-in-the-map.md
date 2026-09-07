# State where the never-delete rule stops, in this effort's map

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [Where the never-delete rule stops](189-where-the-never-delete-rule-stops.md)'s worker, and pasted as
it wrote it.*

> `map.md`'s standing preference beginning *"An in-place update never deletes"* says *"when any file in the graph is
> edited — a node or this map —"*, which has twice been read as an exhaustive list, and it says nothing about the
> rule stopping at a rule statement. Both boundaries are now settled and neither is written anywhere a worker meets
> them. Write them into the map, and into the rules file that node 144 made stand alone for a reader who does not
> read `map.md`.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 189's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-implementation-rules.md`, plus
> `.scratch/graph-workflow/map-history.md` where clause 2 requires text to be moved into it. No other file may be
> edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
>
> 1. `map.md`'s standing preference beginning `**An in-place update never deletes.**` states all four of the
>    following in its own text:
>    a. the rule governs the effort's own record files — `map.md` and its siblings, `decisions.md`, `flags.md`, and
>       the files under `nodes/` — and reaches no file the workflow ships and no product code the effort changes;
>    b. within those files it reaches text whose job is to record what happened — a node's `## Answer`, a line in
>       `decisions.md`, an entry in `flags.md` — which is marked superseded in place and never removed;
>    c. text whose job is to state a rule that currently binds is **not** struck in place: when it is superseded it
>       is **replaced** by its current form, and its existing text is appended **verbatim** to `map-history.md`
>       under the heading mirroring the section it came from, struck-through text staying struck through;
>    d. the ground for (c), quoting the human `verbatim`: *"I don't think there should a be a never delete rule on
>       the rules. They can change."*
> 2. The full text that standing preference carried before this work is appended verbatim to `map-history.md`, under
>    the heading mirroring the `map.md` section it came from.
> 3. `map-implementation-rules.md` states in its own text that a superseded rule in that file is replaced by its
>    current form and its superseded text appended verbatim to `map-history.md`, so a reader of that file who has
>    not read `map.md` can edit it correctly.
> 4. No numbered rule in `map-implementation-rules.md`'s two blocks — the five ground rules, and the four standing
>    rules for writing — is reworded, renumbered or reordered.
> 5. No text already present in `map-history.md` is altered or removed.
> 6. Every markdown link in the two edited files resolves to a path that exists.
> 7. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**Its author split this from its sibling deliberately**, in its words: *"The map statement and the shipped statement
are separate because they have different readers, different files and different blockers — the shipped one cannot
start yet and the map one should not wait for it."* The shipped half is [node
194](194-ship-where-the-never-delete-rule-stops.md).

**This node's own condition is the first written under the rule it states.** Clause 1 replaces a standing
preference rather than striking it, and clause 2 sends the old text to `map-history.md` — which is the procedure
`map.md` has always used and which node 189 established was never carried into its siblings.

## Flags

*Both are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`193.1` `ASSUMPTION` — **The rewritten preference is 1865 bytes against `## Notes`' 500-byte soft target, and I did
not add the sentence `graph-conventions.md` asks an over-target item for.** Its `## Writing the map` says *"An item
that needs more exceeds it and says why"*; my clause 1 required four distinct statements plus a verbatim quotation
of the human in one item, so it cannot reach 500 and I judged a self-referential sentence about its own size to be
exactly the narrative the human objected to in `map-implementation-rules.md` an hour before this node was filed. I
compressed the *why* twice instead, per standing rule 1, and left every shape. What I rested on: mechanical check 10
*"reports and never fails"*, and no item in `map.md` today carries a size justification — the four other
over-target items measured at node 136 (349-445 bytes) carry none.

`193.2` `ASSUMPTION` — **I stated the rule's first boundary as a test of a file's job rather than as the list of
files my condition enumerated, which widens it to files that do not exist yet.** Clause 1(a) gave four names; I
wrote the test and then the four names marked as illustrative. Ground: the wording being replaced was read as
exhaustive twice, which is the defect this node exists to close, so reproducing a bare list would reproduce it on
the next sibling. The cost is that two directories beside `map.md` — `prototypes/` and `recovered/` — are neither
included nor excluded by the test as written, where a bare list excluded them by silence.

## Review

***The manager's note before the check.*** **Its checker died mid-response on a lost connection**, near the end of
its run, and was **resumed** rather than replaced. The resume told it to keep whatever it could still see and to
redo rather than reconstruct whatever it could not — *"a clause you believe you checked but cannot point at the
evidence for is an unchecked clause"* — and to prefer an honest `NOT COVERED` over a `PASS` resting on work it
could no longer see. It returned evidence for all seven clauses and no `NOT COVERED`.

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, ordered under its own headings; every sentence is the checker's.*

> **Settled first — did the work move a standard?** No. I established this myself rather than taking it. The
> standards are named in `map-implementation-rules.md`'s `## What the work is held against`… That section also
> explicitly states **`map.md`'s standing preferences are not among the standards**, so this work's rewrite of the
> never-delete preference does not touch the standard set. `git diff --numstat` on `map-implementation-rules.md` is
> `11 0` — eleven insertions, zero deletions. I confirmed byte-identity of the whole file outside the inserted
> paragraph… The five ground rules and the four standing rules for writing are element-for-element identical.
> **Which state I used:** the post-change state of `## What the work is held against`. It is byte-identical to the
> pre-change state, so the choice is immaterial — which is exactly what leaves a check possible.
>
> **Clause 1** — a–d all stated in the preference's own text. (d) the human's quote checked byte-exact by string
> containment, **including the `should a be` word order**: `True`. **Clause 2 — verbatim, byte-exact.** I extracted
> the bullet from `git show HEAD:.scratch/graph-workflow/map.md`, stripped the `- ` list marker, extracted the `> `
> quote line from the new `map-history.md`, and compared: `BYTE EQUAL: True`, 348 bytes on both sides. The heading
> matches the file's established idiom — three sibling headings already read `## Notes — …`. **Clause 3** — the new
> paragraph states the rule in its own words and says why it is there: *"stated here because this file is read by
> workers who do not read `map.md`"*. It stands alone without `map.md`, and it forecloses the obvious misreading:
> *"The struck rule statements below predate this and are not licence to add another."* **Clause 4** — both blocks
> re-extracted and compared element-wise: ground rules `IDENTICAL: True` (5/5), writing rules `IDENTICAL: True`
> (4/4). **Clause 5** — `git diff --word-diff=porcelain` on `map-history.md` yields **no** removed-word lines. Pure
> append at end of file. **Clause 6** — all markdown links resolved programmatically: `map.md` 68 links / 38
> unique, `map-implementation-rules.md` 43 / 26, `map-history.md` 207 / 63 — **BROKEN: none**. **Clause 7** —
> exactly the three given paths; `--untracked-files=all` returns nothing.
>
> **The bar** — verified from the tree, not taken. No `.github/`, and a `find` for `package.json`, `Cargo.toml`,
> `pyproject.toml`, `Makefile`, `justfile`, `go.mod`, `*.cfg` returns nothing. So the command half is empty and I
> ran nothing. Ground rule 4: the boundary is stated as prose with `**That list illustrates and does not bound**`,
> so a later sibling needs no edit — a change-later shape rather than machinery. Rule 4 met: a regex for `line \d+`,
> `:\d+`, `L\d+` over the added text returns none. **`CONTEXT.md` `_Avoid_` lines** — scanned the added text (3832
> bytes) against every refused word; three hits, all false positives, one of them `where`, which
> `map-implementation-rules.md` itself already records as not refused by any `_Avoid_` line. **`/writing-for-agents`**
> — read and applied. **Negation is paired with the positive target every time.**
>
> **Reported, not a defect.** The rewritten bullet is **1864 bytes** against 354 before. `map.md`'s `## Notes`
> carries a soft 500-byte-per-item target, and `graph-conventions.md`'s mechanical check 10 **reports and never
> fails**, so this is a number to look at rather than a finding.

*No `NOT COVERED`. In its words: "I can point at the evidence for all seven clauses."*

**The question it raised alongside its outcome, pasted as it wrote it.**

> The condition's clause 3 requires `map-implementation-rules.md` to state that a superseded **rule** in that file
> is *replaced* and its text moved verbatim to `map-history.md`, and the work states exactly that… The shipped
> `graph-conventions.md` — a standard this work is held against, and which the condition forbade editing — states
> the opposite scope in two places… So after this work the effort's record files and the shipped conventions
> disagree about whether `map-implementation-rules.md` is a move-file. **Two things soften it and neither removes
> it:** the divergence **predates this work** — `map-history.md` already carried `## Superseded from
> map-implementation-rules.md — the code-slot count at one` before this branch — so the work writes down a practice
> that was already running; and the work anticipates the mixed state with *"The struck rule statements below
> predate this and are not licence to add another."* … Does `graph-conventions.md` now need to follow — dropping
> *"the one file"* and widening `Change the map`'s scope to the map's rule-bearing siblings — and if so, on which
> node?

***The manager's note.*** **The answer to its closing question already exists and the checker could not have known
it**: [node 194](194-ship-where-the-never-delete-rule-stops.md)'s clause 3 demands exactly that, in exactly those
terms, and was written by node 189's worker before this check ran. **This is the fifth independent arrival at that
one defect** — node 189's worker as an invalidation of node 64, node 142's worker as its surfaced node 195, node
142's checker from behind the blindfold, node 191's worker in its retrospective, and now this checker. The manager
settles nothing on it and records that the carrier was already minted.

***The manager's second note.*** **The checker independently established the thing that made this check possible at
all** — that `## What the work is held against` is byte-identical before and after — and said so in the one sentence
that matters: *"the choice is immaterial, which is exactly what leaves a check possible."* Had this node's work
touched that section, no blind check of it could have been run.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*One checker run, `PASS`. No correction round. Both flags are settled by the approval. The checker's one question
was put to the human with the rest of the payload, and the manager's note that node 194 already answers it went
with it.*

## Answer

*Pasted as the worker wrote it.*

> `map.md`'s standing preference `**An in-place update never deletes.**` is replaced by a current statement carrying
> both boundaries [node 189](189-where-the-never-delete-rule-stops.md) settled, and `map-implementation-rules.md`
> states the second boundary in its own text for a reader who never opens `map.md`. The old preference is banked
> verbatim in [map-history.md](../map-history.md) under `## Notes — the standing preference on never-delete, before
> its two boundaries were written into it`. **The edit is the rule applied to itself**: the preference was replaced,
> not struck, and its prior text moved under the `### Change the map` procedure.
>
> **Four calls a later reader would otherwise re-derive.**
>
> **1. The first boundary is written as a membership test, not as a list of today's files.** The preference names
> what makes a file one of the record's — *"the files whose job is to hold what this effort decided and why"* — and
> then gives the enumeration the condition asked for explicitly marked *"illustrates and does not bound"*. Ground:
> the record has gained three sibling files in the last forty nodes, and the wording this replaces was misread twice
> precisely because its illustration `— a node or this map —` looked exhaustive. A list of today's files would be
> false again on the next split; a test is not. The cost is that files in the same directory whose job is arguable —
> `prototypes/`, `recovered/` — are left unadjudicated rather than silently included, which is flag `193.2`.
>
> **2. `map-history.md`'s own immunity is stated in `map.md` though no clause asked for it.** One clause: *"That
> history file is itself never replaced, holding superseded text only."* It carries node 189's flag `189.3` rather
> than any judgement of this node's, and it is there because a worker reading *"text that states a rule is
> replaced"* could start replacing rule text inside the destination the same sentence sends text to. What may leave
> that file at all stays [node 70](70-pruning-a-long-running-map.md)'s.
>
> **3. The rules file's new paragraph sits above `**Nothing below was reworded on the way here**`, not below it.**
> That sentence is a standing claim about everything after it, and a new paragraph appended into the header region
> below it would make it false — a new paragraph was written here, not moved from `map.md`. Placing it between that
> sentence and the file's opening paragraph keeps the claim true without rewording it, which nodes 144 and 152 hold
> conditions quoting.
>
> **4. Nothing was struck in either edited file.** `map-implementation-rules.md` takes 11 inserted lines and no
> deletion, so its two numbered blocks are untouched by construction; `map-history.md` takes 9 appended lines and no
> deletion; `map.md` is one line replaced by one line. The banked text was diffed byte-for-byte against `HEAD`'s and
> is identical. The struck rule statements already standing in the rules file were left where they are — they
> predate the rule and moving them is [node 190](190-the-rules-file-states-one-list-twice.md)'s clause 3, which the
> manager amended to do exactly that. The new paragraph says so in as many words, so a worker does not read those
> strikes as the file's live idiom.

**What the worker reported its work invalidates:** [node 80](80-map-items-nodes-64-and-68-left-stale.md), in
substance discharged and in form falsified. Its full text is annotated onto that node rather than restated here,
with the manager's note that node 80's clauses 2 and 3 have been unworkable since node 139 for a reason predating
this work. **It found node 80 by running a `grep` nothing told it to run**, three nodes having passed the same
preference without noticing an open condition quoted it.
