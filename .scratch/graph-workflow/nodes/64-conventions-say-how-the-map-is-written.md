# Say in the conventions document how the map and its history are written

Type: implementation
Status: resolved

## Question

`graph-conventions.md` now lists five files, but it still describes the map as though every append lands in it, so
nothing states the practice that keeps the map at the size [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md) just brought it to — **the next account filed in place starts the growth again.**

Two defects, one file: the writing procedure is absent, and the document's list of the map's sections names four
where a map carries a fifth pointing at `decisions.md`. The second is pre-existing, and clause 10 of node 59's
condition forbade touching it. No mechanical check reads either, so nothing catches the drift.

Reported by node 59's worker, which wrote the acceptance condition below.

**Why this is token work rather than tidying.** Node 59 cut every worker's map read from ~23,000 tokens to ~6,700
by moving the append history out. Nothing in the shipped files says to keep doing that. The saving is a one-off
until the practice is written down, and the file it belongs in is the one every node's work is measured against.

**Blockers: none.** It touches only `.claude/skills/expedition/graph-conventions.md`, so it contends for the code
slot with any other node editing that file.

## Acceptance condition

*Written by node 59's worker.*

The file being changed is `.claude/skills/expedition/graph-conventions.md`, and
it is the only file this node modifies. Before this change it holds a section headed `## The five files` listing
five paths with a one-line description of each; a sentence reading ``map.md` has four sections, in this order:`
followed by a four-item bulleted list; and a paragraph headed `**No edit deletes.**`. Done means every one of the
following.

1. The document states, in prose of its own, the procedure for writing the map: an account of how a note, a
   standing preference or a fog item reached its current form goes into `map-history.md`, while the map keeps that
   item's **current statement**, which cites the nodes that shaped it by markdown link and does not restate what
   those nodes hold. It states this where a reader looking for how the map is changed will meet it — under the
   never-delete paragraph, in the five-files section, or in a section of its own.
2. It states that this procedure deletes nothing: text moved to `map-history.md` is moved verbatim rather than
   summarised, paraphrased or shortened, and text already struck through moves struck through.
3. Its list of the map's sections carries an entry for a section that points at `decisions.md`, and says that
   section holds a pointer rather than any decision, and the sentence introducing that list names the same number
   of sections as the list has entries.
4. The document cites no place inside any file by line number, and every markdown link in it resolves to a path
   that exists.
5. No file under any of `.claude/skills/expedition-checker/`, `.../expedition-grilling/`,
   `.../expedition-implementation/`, `.../expedition-precondition/`, `.../expedition-prototype/`,
   `.../expedition-research/` is modified.
6. The bar.

### What the minting worker could not settle, in its own words

> Whether that fifth map section is a convention every effort's map carries or an artifact of this effort's own
> history. I wrote clause 3 the way the never-delete rule implies — the pointer exists, so the document should
> describe it — but the opposite fix (the document stands and this effort's map is nonconforming) is a live
> option, and taking it would change clause 3 and nothing else in the condition.

Whoever claims this node should know the question is live rather than settled, and that clause 3 is one of the two
answers rather than the neutral statement of the problem.

## Annotation: a third defect in the same file, found by node 59's blind checker

*Filed by the manager. The condition above was written before this was known, so it is **not** covered by any of
its six clauses.*

The checker on [Restructure `map.md` to what every worker needs](59-restructure-the-map.md) reported it in its
`QUESTIONS`, alongside the two the condition already covers:

> `## Procedures`, whose own rule is *"Each lists every file that changes, in order"*, never mentions
> `map-history.md`, so the graph now has a fifth file that no procedure writes or maintains.

**This is the sharper of the three**, and it is not a stale number. The other two are a heading and a count that
disagree with the file they describe; this one is a **file with no writer**. The section's own rule promises that
every procedure lists every file it changes, and the procedure that would file an account into `map-history.md`
does not exist — so the practice clause 1 demands has nowhere to be performed from, and the never-delete rule
carries on pointing every append back into `map.md`.

**Whoever claims this node should treat it as a seventh clause they are owed under the bar rather than as
optional**, on the ground [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md) settled: *a shipped file may require only what travels with it, or what the
effort is obliged to declare in the form the requirement needs.* The declaration here is `## Procedures`' own
stated rule, which the file makes false about itself the moment a fifth file exists. **The manager did not add it
to the condition**, that text being the minting worker's, and records it here so the audit at claim time meets it.

### Audit at claim time, by the manager

*The manager's own note, not a change to the condition above.* Read against [An acceptance condition is
self-contained text](33-condition-is-self-contained.md) and [The clause that says no resolved node changes
cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md).

**All six clauses pass.** Clause 5 quantifies over the **tree**, which node 36 permits. Clause 6 is the bar, the
one exemption. Nothing points at material the checker will not be given: clauses 1 and 2 state the procedure as
text rather than sending anyone to read node 59, and clause 3 states the count rule rather than naming the count.

**The three before-state facts were verified rather than trusted**, in the file as it stands at commit `8a39024`:
`## The five files` is present exactly once; the sentence ``map.md` has four sections, in this order:` is there
followed by a four-item list; and `**No edit deletes.**` opens a paragraph. All three hold.

**The `## Procedures` defect is deliberately left outside the condition, and this is the second run of [What keeps
the shipped files consistent when a decision changes a term](29-shipped-file-consistency.md)'s mechanism.** The
minting worker said plainly that *"clauses 1 to 3 as I wrote them do not reach `## Procedures`"*, and supplying
what a condition omits would make the manager the author of the standard — which node 33 forbids for the reason it
gives. So the condition stands unamended and **the defect is owed under the bar**: `## Procedures` states its own
rule, *"Each lists every file that changes, in order"*, and a fifth graph file that no procedure writes makes that
sentence false about the document itself. Verified present at that section. If the worker does not deliver it, the
blind checker should fault the work under the bar rather than under any clause. **Either outcome is informative**,
which is the same reason [Ship the FRICTION flag and the self-edit disclosure duty](41-ship-the-friction-flag.md)
was held back for the mechanism's first run.

**One risk worth naming.** Clause 3 takes a side on a question the minting worker could not settle — whether the
map's fifth section is a convention or an artifact of this effort. The worker said so itself. The worker on this
node inherits that choice rather than making it, and should not reopen it.

## Answer

The practice [Restructure `map.md` to what every worker needs](59-restructure-the-map.md) performed by hand is now
written into `.claude/skills/expedition/graph-conventions.md`, the only file this node touched.

**`## Writing the map`** — a new top-level section between `## The five files` and `## Adding a node`. Every note,
standing preference and fog item in `map.md` is a **current statement**: what holds now, citing by markdown link the
nodes that shaped it and never restating what those nodes hold. The **account** behind it belongs in
`map-history.md`, under a heading mirroring the map section it came from. **So the map is rewritten as it changes
rather than grown by appending, and every worker reads it cold, so its size is a cost paid once per node.** Its
second paragraph, `**This deletes nothing.**`, states that moved text moves **verbatim** — never summarised,
paraphrased or shortened — that struck-through text moves struck through, and that the never-delete rule is
*satisfied* by the move rather than exempted from it.

**`### Change the map`** — a new procedure, last in `## Procedures`, **which is what makes that section's own rule
(*"Each lists every file that changes, in order"*) true again now the graph has a fifth file**: `map-history.md`
first, `map.md` second, the account written before the map changes so a run that dies leaves it banked. *"Without it
the practice above had nowhere to be performed from."*

**The map's section list names five**, with `## Decisions so far` described as a pointer to `decisions.md` holding
no decision. **`### Resolve` step 4 split into 4 and 5**, its old single step having changed two files while naming
one — *"reinstating the exact `## Procedures` defect this node exists to fix at a different step."*

**And the `## The five files` paragraph describing `map-history.md` was removed**, at correction round 1. It said the
map *"appended in place"*, which `## Writing the map` denies. **The only text this node deletes.**

Two calls a later reader would otherwise re-derive: **no markdown link was added anywhere**, the graph files living
in `.scratch/<effort>/` while this file ships in `.claude/skills/expedition/`, so no relative link resolves — paths
are backticked and cross-references are by heading, which is the effort's standing rule 4. And **no mechanical check
was added**, confirmed correct on review: whether text moved *verbatim* needs the prior version, so it is not
decidable by reading the files, which is `## Mechanical checks`' own stated bar.

**The `## Procedures` defect owed under the bar was delivered.** It was deliberately kept out of the condition — the
second live run of [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md)'s mechanism — and the worker met it without any clause saying so, **and then
found a second instance of the same defect in `### Resolve` that nobody had reported.**

## Flags

`64.1` **· settled** `ASSUMPTION` — **Clause 4's link rule was read as not reaching the one placeholder markdown link inside a
fenced code block**, on the document's own *"Skip fenced code blocks."* **The checker reached the same reading
independently** and added an argument the worker did not have: the wider reading would have made clause 4
unsatisfiable at `HEAD` too, which is evidence against it.

`64.2` **· settled** `ASSUMPTION` — **`### Resolve` was edited, a procedure the acceptance condition does not name.** It was the
only other procedure that writes the map, and once a fog item's text moves to `map-history.md` that step changed two
files while naming one. **The checker did not fault the edit.**

`64.3` **· settled** `ASSUMPTION` — **The stale paragraph was removed rather than reworded, and its one live clause folded into
`## Writing the map`.** In the worker's words: *"Removal was my call, not the correction's: it deletes prose node 59
wrote, and a reworded version would have been a third copy of what the fenced inventory line and the new section
already say. Never-delete governs the graph's files and not the shipped ones, so this needed no exception, but it is
the only deletion in this node's diff and the human sees it as one."*

## Review

**Checker, run 1 — `FAIL: the bar`.** All five substantive clauses met; **one breach**, and it was in text the
change did not touch: `## The five files` asserted the map *"appended in place"* while the new `## Writing the map`
denies it. **The checker handed back a finding in three parts** — the instances, the form as a predicate, and the
**extent**, enumerated and complete: 15 sentences in the file mentioning either map file, all 15 read, exactly one
inconsistent. That is [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md)'s proposal,
run by the agent that proposed it, one node after proposing it.

It also **re-derived the delegated reviewing agent's findings rather than relaying them, and two of four did not
survive** — a refused-vocabulary charge against `run`, disposed of by the document's own established usage at
`HEAD`, and a missing-mechanical-check charge, disposed of on the section's own stated bar. **Relaying which
findings were considered and rejected was itself reported as worth its tokens** by the implementer, which is a
practice the manager will keep.

**Correction round 1.** Both items repaired: the stale paragraph removed with its live clause folded into the
practice it motivates, and `### Resolve` step 5 reworded so only the cross-reference reading survives. **The
implementer verified the checker's enumeration before acting on it** rather than taking it — 13 prose sentences plus
2 fenced lines, matching the count.

**Checker, run 2 — `PASS`**, over the whole condition, **run by resuming the same checker rather than spawning a
third**, so it re-established nothing and re-ran only what the round reached. It confirmed the enumeration
independently — 15 before, **14 now, a drop of exactly one**, none asserting append-in-place — and it **hunted the
one candidate that could have falsified the claim**: `### Rule out of scope`'s *"append one line to `## Out of
scope`"*. Not a contradiction, because `## Writing the map` scopes itself to *superseded* items and a new
out-of-scope line is a new item.

**It traced all four claims of the deleted paragraph to where they now live** — *verbatim* into the clause-2
paragraph and stronger there as an operative rule; the read-cold rationale into `## Writing the map`;
account-to-history into its first paragraph; and the append-in-place mechanism *"was the false claim, correctly
gone."* And it settled the deletion question **from the text it holds alone**: the never-delete rule's antecedent is
*"When any **graph file** changes"*, and `graph-conventions.md` is not among the five. *"I did not go near node 59,
and I assert nothing about what it wrote."*

**It also declined to re-spawn the Standards axis** and did the pass by hand — three small edits, every round-1
finding already re-derived — and reported the choice as strengthening its own earlier proposal: a delegated agent's
findings are evidence to re-derive, **and on a re-check with a small diff the hand pass is ordinarily the better
spend.**

**Gate: awaiting the human.**

**Gate: `approve`.** The human's word, `verbatim`: *"Approve."*

**All three flags settled by that approval** under the standing instruction at [Whether flags.md survives the
settle-at-close practice](27-does-flags-file-survive.md) — *"when I approve the end of the node, the flags should be
considered ok."*

### The manager failed the payload's own rule at this gate, and the human caught it

*The manager's own note.* Their words, `verbatim`: *"you forgot to describe the flags."*

**The payload named three flags and described one.** `64.3` was set out in full; `64.1` and `64.2` were named and
left at that. The instruction that governs is recorded on [Nothing checks that a part a checker left uncovered was
ever established](45-nothing-checks-an-uncovered-part.md), in the manager's own words at that gate: *"approval
discharges them, so a payload that omits one settles it silently."* **The manager wrote that sentence and then did
the thing it warns against.**

**Both were settled by an approval given without their content.** What they said, recorded here so the record is not
merely a checkbox: `64.1` read clause 4's link rule as not reaching a placeholder link inside a fenced code block,
on the document's own *"Skip fenced code blocks"* rule — **the checker reached the same reading independently and
supplied an argument the worker lacked**, that the wider reading would have made clause 4 unsatisfiable at `HEAD`
too. `64.2` edited `### Resolve`, a procedure the condition does not name, because it was the only other procedure
writing the map and its single step changed two files while naming one — **the checker examined the edit and did not
fault it**. Neither is a judgement the human would likely have disturbed, which is what makes the omission a process
failure rather than a lost decision, and the manager records it as the former.

**Why it happened, since the pattern is more useful than the instance.** The payload was assembled around the
*checker's* findings, which is what the gate is mostly about, and the flags were appended as a list of ids at the
end. **A flag is not a line item on the payload; it is a decision the approval consumes.** The two that were
dropped were the two the checker had already blessed — which is precisely why they read as bookkeeping and precisely
why that reading is wrong.

## Annotation: one sentence this node landed is now false

*Filed by the manager from [node 189](189-where-the-never-delete-rule-stops.md)'s handover, and pasted as that
worker wrote it. This node is resolved; the annotation records the finding here rather than editing its answer.*

> **Node 64** — one sentence of what it landed is now false. Its `## Writing the map` section produced the shipped
> claim that `map.md` *"is the one file whose superseded text is also moved rather than left in place"*, written
> when the graph had five files and `map.md` had no sibling holding rules. It now has two, and their superseded rule
> statements move the same way. **The rest of node 64 stands** — the current-statement/account split, the
> verbatim-move property, and the `### Change the map` procedure are all what this answer builds on rather than
> displaces.

***The manager's note.*** **The repair is [node 194](194-ship-where-the-never-delete-rule-stops.md)'s clause 3**, so
this annotation carries no work of its own. Whether an annotation onto an already-resolved node has a home in the
graph's format is one of the manager contract's own declared unsettled questions, and this is the second time this
session it has been needed.
