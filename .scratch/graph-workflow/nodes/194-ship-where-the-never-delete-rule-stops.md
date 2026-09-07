# Ship where the never-delete rule stops, in the conventions document

Type: implementation
Status: resolved

Blocked by: 142

## Question

*Surfaced by [Where the never-delete rule stops](189-where-the-never-delete-rule-stops.md)'s worker, and pasted as
it wrote it.*

> The shipped `graph-conventions.md` states *"No edit deletes"* for every effort and scopes it correctly to graph
> files, but says nothing about the rule stopping at a rule statement, and asserts that `map.md` is *"the one file
> whose superseded text is also moved rather than left in place"* — which its siblings that state current rules now
> contradict. Carry both boundaries into the shipped statement.

**Blockers, in the worker's words:** *"142."*

**Its sequencing note, in the same worker's words and marked by it as not part of the condition:**

> node 142 is claimed and running on this file under a condition forbidding changes beyond its own five clauses, and
> nodes 146 and 153 are also open on it. This node runs after 142 lands, and the manager sequences it against 146
> and 153 rather than running them in parallel worktrees over one file.

## Acceptance condition

*Written by node 189's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. The worker may not
> mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. This is a file the workflow ships, so
> it is edited plainly: superseded wording is removed rather than struck, and nothing is moved to any history file.
>
> Done means all of the following are true of the finished tree.
>
> 1. The paragraph beginning `**No edit deletes.**` states in its own text that the rule reaches the graph's own
>    files and nothing outside them — neither the product the effort changes nor any file the effort ships.
> 2. That paragraph, or one adjacent to it under the same heading, states that within the graph's files the rule
>    distinguishes two kinds of text: text that records what happened — a node's `## Answer`, a line in
>    `decisions.md`, an entry in `flags.md` — is marked superseded in place and never removed; and text whose job is
>    to state a rule that currently binds is instead replaced by its current form, its superseded text appended
>    verbatim to `map-history.md`.
> 3. The sentence `**map.md** is the one file whose superseded text is also *moved* rather than left in place` no
>    longer claims `map.md` is the only such file, and the `## Writing the map` section and the `### Change the map`
>    procedure both apply to `map.md` and to those of its siblings that state current rules, rather than to `map.md`
>    alone.
> 4. No procedure in the file other than `### Change the map` is reworded, and the numbered list under
>    `## Mechanical checks` is unchanged in content, count and order.
> 5. Every markdown link in the file resolves to a path that exists.
> 6. No file outside `.claude/skills/expedition/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**This is the node that carries the human's `Q3` answer**, given at node 189's interview against that node's
worker's own recommendation and against `map.md`'s standing default that a rule reaches a shipped file only where
they say so. Their word, `verbatim`: *"Q1 ok Q2 ok Q3 ok"*.

**Its clause 3 repairs what node 189 reported as an invalidation** of [node
64](64-conventions-say-how-the-map-is-written.md) — the shipped claim that `map.md` is the one file whose superseded
text moves, true when the graph had five files and false since node 140 created two siblings that hold rules.

**The manager has added the `Blocked by: 142` edge**, which the worker named in its own text as a blocker and as a
sequencing note. Nodes 146 and 153 are also open on that file and hold no edge to this one; the manager sequences
them rather than running them together.

## Flags

*Both are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`194.1` `ASSUMPTION` — **I read clause 5's *"every markdown link resolves to a path that exists"* as a demand on
prose links, and left the one link in the file untouched.** The file holds exactly one `[...](...)`:
`[<node name>](nodes/NN-<name>.md)`, inside the fenced block showing `flags.md`'s line form. It is a placeholder
with `NN` and `<name>` unfilled, it is relative to `.scratch/<effort>/` rather than to the shipped file's own
directory, and the file's own scanning rule two lines from it says to skip fenced code blocks. It predates this
node, no clause reaches it, and repairing it would be inventing a demand. I added no link, so the clause holds on
everything this work wrote.

`194.2` `ASSUMPTION` — **I wrote the sibling scope as a test and left the fog-item enumerations pointing at
`map.md`.** The condition asks that `## Writing the map` and `### Change the map` apply to `map.md` *and to those
of its siblings that state current rules*. Written as a list of today's siblings that is false the next time the
map splits, so all three passages say *"every sibling of it that states rules that currently bind"*. The narrower
call: both passages also enumerate *"a note, a standing preference or a fog item in `map.md`"*, and the fog no
longer lives in `map.md`. Generalising the file reference there would have swallowed a defect that is another open
node's whole subject, so I widened the scope alongside the enumeration and left the enumeration itself untouched.

***The manager's note on `194.2`.*** **The defect it declined to swallow is [node
195](195-graph-conventions-still-puts-the-fog-in-the-map.md)'s**, minted from node 142's handover before this node
was claimed. The worker reached the same boundary without being told where it was.

## Review

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, ordered under its own headings; every sentence is the checker's.*

> **Settled first — the standard under check.** `graph-conventions.md` is named as a standard by
> `map-implementation-rules.md` (twice: in the bar's non-command half and in the review route's standards list) and
> is also the path under check. I split it into operative content and rationale and compared the sets. The
> paragraphs the work moved state rules governing **the graph's own files** — the seven under `.scratch/<effort>/`.
> On the pre-change side the rule opened *"When any graph file changes"*, and `graph-conventions.md` at
> `.claude/skills/expedition/` is not among the seven files that section enumerates. On the post-change side it is
> excluded explicitly. So **the set of things this standard requires or refuses of the work under check is identical
> on both sides**: on neither side does it reach a file the workflow ships, and neither side was ever what I would
> hold this work against. An unmoved statement survives, no circularity arises, and a check is possible. I did
> **not** raise.
>
> **Clause 1. Met.** *"**The rule reaches the graph's own files — those listed below — and nothing outside them.**
> The product the effort changes, and every file the effort ships, are edited plainly."* Both exclusions named.
> **Clause 2. Met.** The immediately adjacent paragraph states the two-kinds cut and names all three record examples
> as marked-in-place-and-never-removed, and rule-stating text as **replaced** with its superseded text *"appended
> verbatim to `map-history.md`"*. **Clause 3. Met.** The uniqueness sentence is gone, replaced by *"`map.md` is
> written this way, and so is every sibling of it that states rules that currently bind"*. *(Note: the condition
> quotes the old sentence with `map.md` in bold where the file had it in code ticks — the sentence was unmistakable
> and I matched it on its text.)* **Clause 4. Met**, by word-level diff and an unwrapped per-procedure diff. All 8
> procedures present in the same order; exactly one body differs, `### Change the map`. `## Mechanical checks` diffs
> **identical** unwrapped, 10 items both sides, same order. **Clause 5. Met, vacuously and correctly.** The file
> contains exactly one `](` occurrence and it sits **inside a fenced code block** (fences verified balanced). There
> are zero markdown links in the file's prose, and the change adds and removes none. **Clause 6. Met.** Both `git
> status --porcelain -uall` and `git diff --name-only a240eed` return exactly one path.
>
> **The bar** — command half empty, verified from the tree rather than taken on trust: the repo tracks 213 files,
> 212 `.md` plus `.gitignore`. No manifest, task runner, formatter config or `.github` of any kind. **Ground rule 1**
> — the added text names no effort, no node number, no machine, no toolchain, and no path outside
> `.scratch/<effort>/`. **`CONTEXT.md` `_Avoid_` lines** — scanned word-boundary-wise against every distinctive
> refusal; three hits, all clear, one of them text carried over verbatim by the rewrap rather than new.
>
> **Internal consistency I checked and found sound:** the new by-text-kind formulation leaves `map-manager-only.md`
> and `map-implementation-rules.md` in the covered set and `map-history.md` outside it, which is what `### Resolve`
> steps 4-5 and `### Rule out of scope` step 2 already do — the change introduces no contradiction with any
> unreworded procedure.

*No `NOT COVERED`. No questions raised.*

***The manager's note.*** **The first check this session to hand back nothing at all** — no question, no uncovered
clause, no finding. It is also the first to verify the *set* of a standard's demands rather than its text, which is
what let it clear the circularity in one step: the standard's requirements on this work were identical before and
after, so which state it read was immaterial.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*One checker run, `PASS`, with no questions and nothing uncovered. No correction round. Both flags are settled by
the approval.*

## Answer

*Pasted as the worker wrote it.*

> The shipped `graph-conventions.md` now carries both boundaries of the never-delete rule and no longer claims
> `map.md` is the only file whose superseded text moves. Three passages changed and nothing else.
>
> **The `**No edit deletes.**` paragraph gained the location boundary.** After the existing strike-in-place sentence
> it now says the rule reaches the graph's own files — *those listed below*, pointing at `## The seven files` rather
> than at a count that decays — and nothing outside them, and that the product the effort changes and every file the
> effort ships are edited plainly, superseded wording removed and nothing moved to a history file. It is phrased as
> the positive act on the outside files rather than as a bare prohibition, so a reader learns what to *do* to a
> shipped file.
>
> **An adjacent paragraph, in the same preamble, carries the text boundary.** It states that inside the graph's
> files the rule cuts by what a piece of text is and not by which file holds it: text that records what happened — a
> node's `## Answer`, a line in `decisions.md`, an entry in `flags.md` — is marked superseded in place and never
> removed; text whose job is to state a rule that currently binds is replaced by its current form, its superseded
> text appended verbatim to `map-history.md`. It closes by naming `map.md` **and every sibling of it that states
> rules that currently bind** as written that way, which is where the old *"one file"* claim stood.
>
> **`map-history.md` is protected inside that same sentence** — *"which holds superseded text only and is itself
> never rewritten"*. Without it a worker reading *"text that states a rule is replaced"* can start replacing rule
> text inside the destination the rule sends text to. It sits in the sentence that names the destination rather than
> in its own paragraph, so the protection travels with the instruction that creates the hazard.
>
> **The sibling scope is written as a test, never as a list.** *"Every sibling of it that states rules that
> currently bind"* stays true the day the map splits again; an enumeration of today's siblings would be false on the
> next split. The same phrase is used in all three passages so the reader meets one concept rather than three
> wordings.
>
> **`## Writing the map` opens with its own scope.** A new first paragraph says the section covers `map.md` and
> every sibling that states rules that currently bind, so a file the map later splits into is covered the day it is
> written, and names the files written the other way — `decisions.md`, `flags.md`, the node files, and
> `map-history.md` — as recording what happened, with their superseded text staying where it is. Two sentences
> inside the section were made precise rather than generalised: *"So **a map file** is rewritten as it changes"*, and
> *"Every worker reads **`map.md`** whole and cold"* — the second because the sibling holding the manager's material
> is read by no worker at all, so a widened *"the whole map"* would have been false.
>
> **`### Change the map` now has two triggers.** A note, standing preference or fog item in `map.md` that no longer
> says what holds, **or** a rule in a sibling that states rules that currently bind and no longer holds. Step 2's
> target became *"`map.md`, or the sibling the item came from"*, keeping the procedure's promise that each step names
> the file that changes, and the two closing sentences shifted from *"the map"* to *"the item"* and *"a map file"*.
>
> **Two things were deliberately left alone.** The enumerations *"a note, a standing preference or a fog item in
> `map.md`"* keep placing fog items in `map.md`, which stopped being true when the fog moved to the manager's
> sibling — that is a separate open node's defect, it predates this work, and widening the file scope around it
> without touching it leaves it exactly as live as it was. And the `500-byte` paragraph keeps its `map.md`-only
> scope and its *"the whole map"*, both correct there and both referenced by a mechanical check.

**What the worker reported its work invalidates:** `none`. In its words: *"it **lands** the invalidation node 189
already reported against node 64, whose `## Writing the map` produced the *"one file whose superseded text is also
moved"* claim. The rest of node 64 stands and this work builds on it."*
