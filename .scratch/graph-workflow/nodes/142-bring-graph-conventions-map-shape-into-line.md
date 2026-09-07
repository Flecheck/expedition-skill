# Bring `graph-conventions.md`'s map shape into line with the split map

Type: implementation
Status: resolved

Blocked by: 140

## Question

*Surfaced by [Move the manager's material out of the map](139-move-the-managers-material-out-of-the-map.md)'s worker,
and pasted as it wrote it.*

> `graph-conventions.md` now lists six graph files including `map-manager-only.md`, but three of its statements still
> place the fog and out-of-scope inside `map.md`: the sentence *"`map.md` has five sections, in this order:"* with its
> bullets for `## Not yet specified` and `## Out of scope`, the `Resolve` procedure's step 5 (*"`map.md`: remove that
> item from `## Not yet specified`"*), and the `Rule out of scope` procedure's step 2 (*"`map.md`: append one line to
> `## Out of scope`"*). Node 139's clause 11 forbade touching them. It waits on node 140 because node 140's own
> condition reuses node 139's clauses 1 to 8 and 12 to 13 only — so nothing raises the file count from six to seven
> when the second sibling lands either, and the shape should be corrected once rather than twice.

## Acceptance condition

*Written by node 139's worker. Pasted as it wrote it, and not the manager's.*

> The work is the file `.claude/skills/expedition/graph-conventions.md`. It is
> written against whatever `.scratch/graph-workflow/` holds at claim time, because
> which sections have moved out of `map.md` is not fixed until node 140 lands. Done means every one of the following
> is true of the finished tree.
>
> 1. The sentence in `graph-conventions.md` beginning `` `map.md` has ``, and the bulleted list under it, name every
>    `##` heading that `.scratch/graph-workflow/map.md` actually holds, and name no
>    heading it does not hold. The count stated in that sentence equals the number of bullets under it.
> 2. Every `##` heading that has moved out of `map.md` into another file in that directory is described in
>    `graph-conventions.md` under that other file rather than under `map.md`, and its one-line description says the
>    same thing it said before the move.
> 3. The `### Resolve` procedure's step that removes a resolved fog item names the file that actually holds `## Not
>    yet specified`.
> 4. The `### Rule out of scope` procedure's step that appends the out-of-scope line names the file that actually
>    holds `## Out of scope`.
> 5. The heading that opens the graph's file list states the number of entries the list holds, and the list holds one
>    entry for each file present in `.scratch/graph-workflow/` plus one entry
>    standing for the per-node files under `nodes/`.
> 6. No file under `.scratch/graph-workflow/` is modified, and no file under any of
>    `.claude/skills/expedition-checker/`, `.../expedition-grilling/`,
>    `.../expedition-implementation/`, `.../expedition-precondition/`, `.../expedition-prototype/`,
>    `.../expedition-research/` is modified.
> 7. `graph-conventions.md` changes in no respect other than clauses 1 to 5.

## The manager's note at filing

*Not a change to anything above.*

**This node exists because a condition fenced its own worker out of a defect that condition created**, which is flag
`139.1`. Node 139's clause 11 required `graph-conventions.md` to name the correct file count while forbidding any
other change, and raising the count is exactly what made three other passages of the same file false. Its worker read
the fence as binding, said so, and reported this node rather than reading the fence generously. **The manager takes
no view on which reading was right and records that both were available.**

**Its condition is the first on this graph written entirely against the tree at claim time rather than against any
state its author could see.** Every clause reads a fact off `.scratch/graph-workflow/` when the work runs, because
node 140 has not landed and the shape is not yet fixed. Under [node 94](94-condition-scope-as-a-predicate.md)'s
rungs it is a predicate with a domain and no recorded return, which is legitimate and which its checker cannot
compare against anything — there is nothing to re-run.

**Why it is blocked on [node 140](140-move-the-implementers-and-checkers-material-out-of-the-map.md) rather than
merely sequenced after it.** Node 140 adds a seventh file and moves more sections out of `map.md`. Doing this node
first would correct the shape to a state node 140 immediately invalidates, which is the double work its author named.

## Review

***The manager's note before the check.*** **Its first checker attempt died two lines in on an API session limit**,
having established nothing, and was **resumed** rather than replaced under the human's standing instruction. The
resume carried one fact the manager already held and told it to verify rather than take: that `master` had moved two
commits past the worktree's base while the work sat, and that neither commit touches the path under check.

### Checker run 1 — `PASS`

*Pasted as the checker wrote it, ordered under its own headings; every sentence is the checker's.*

> **Settled first: a standard the work moved.** `map-implementation-rules.md` names `graph-conventions.md` as a
> standard — in the review route's *"standards to hold work against"*, and, since commit `25bcefa` (node 184), in
> the bar's non-command half too. It is also the path under check, so `### Where the work moved one of them` applies
> and I settled it before checking anything else. Operative content **did** move: Resolve step 5 and
> Rule-out-of-scope step 2 now require a different file. But every element that moved governs the manager's writes
> to an effort's **graph files**, and this work touches no graph file. So no moved element bears on this work in
> either form; the element that could have (`## No edit deletes`) is unmoved. The contract's ground for raising —
> *"nothing unmoved left to hold the rest of the work against"* — is not met, so I issue an outcome rather than
> raising.
>
> **Baseline verified rather than taken:** worktree `HEAD` and `CLAUDE_BASE` are both `31ad6fa`; `master` is
> `25bcefa`, two commits ahead; `git diff --name-only 31ad6fa..HEAD -- .claude/skills/` is empty, and the file's
> base blob `598eb65` equals `master:`'s. The diff is against current content.
>
> **Clause 1** — `` `map.md` has three sections, in this order: `` over three bullets. Live `map.md` holds exactly
> those three, and `grep -c '^```' map.md` = 0, so no heading hides in a fence. Stated count 3 = bullet count 3.
> **Clause 2** — the headings that moved out are `## Not yet specified` and `## Out of scope`, both now in
> `map-manager-only.md`, both described under that file and no longer under `map.md`; the word diff shows the
> removed and added bullets as identical words. `## Notes` did **not** move out, so the clause does not reach
> `map-manager-only.md`'s own `## Notes`. **Clause 3** and **Clause 4** — steps 5 and 2 each name
> `map-manager-only.md`, which holds the heading; `map-history.md` also carries both headings, but as the mirror the
> same procedure appends to. **Clause 5** — `## The seven files` over 7 entries; `find -maxdepth 1 -type f` gives
> exactly 6, and 6 + 1 for the per-node files = 7. Reading *"file present in"* as non-recursive is forced by the
> clause's own *"plus one entry standing for the per-node files"*. **Clause 6** — one path in `git status
> --porcelain -uall`; scoped to `.scratch` and to all six named sibling skill dirs, empty. **Clause 7** — five
> hunks, +10/−9, each attributable to clauses 1-4; the only other movement is a rewrap forced by the longer
> filename, its words unchanged.
>
> **The bar** — command half empty, verified from the tree: no manifest, task runner, formatter config, test
> directory or `.github`. Non-command half: `CONTEXT.md`'s 40 `_Avoid_` lines checked **by hand** per the rules
> file's own warning that the list greps false. Ground rules 1, 3 and 4 bore and hold; writing rules 1 and 4 bore
> and hold, 2 and 3 did not reach a shipped file. `/writing-for-agents` read by path located by name per ground rule
> 5, and **read by me rather than delegated, so nothing ran in an agent handed less than I was.**

*No `NOT COVERED`. No findings, so no extent owed.*

**Its two questions, pasted as it wrote them.**

> The checker contract says a raise is owed where the work moves the operative content of a standard the bar
> carries, and `map-implementation-rules.md` names `graph-conventions.md` as one. **Read strictly, every node whose
> work IS `graph-conventions.md` forces a raise and the file becomes unmaintainable.** I read it against its own
> stated ground instead and issued an outcome. Whether the wording should be narrowed to the elements that bear on
> the work is the human's.

> Pre-existing and outside clauses 1-5, so not a finding against this work: **`graph-conventions.md` contradicts
> itself on where the bar's commands live.** Its `## Notes` bullet says `map.md`'s `## Notes` holds *"the bar's
> commands once they have been discovered for this repo"* and its *"ground rules"*, while three paragraphs earlier
> the same file says `map-implementation-rules.md` holds *"the bar's commands and the standards work is held
> against"*. Likewise `## Labels` says *"A node may only use a label declared in the map's `## Notes`"* where this
> effort's vocabulary is now in `map-manager-only.md`. Neither is a `##` heading, so clauses 1-5 miss both and
> clause 7 forbade touching them. **The worker was right to leave them.**

***The manager's note.*** **Its second question is [node 153](153-graph-conventions-notes-bullet-is-false.md)'s
subject, reached from behind the blindfold**, and it adds one thing node 153 does not hold: the `## Labels` sentence.
**Its `## Notes`-bullet half is the fourth independent arrival at that defect.** The manager settles nothing on it.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*One checker run, `PASS`. No correction round. All three flags are settled by the approval, and both of the
checker's questions were put to the human with the rest of the payload.*

## Answer

*Pasted as the worker wrote it.*

> `.claude/skills/expedition/graph-conventions.md` now describes the map as the split left it. Four changes, and
> nothing else:
>
> - The sentence `` `map.md` has five sections, in this order: `` becomes `` `map.md` has three sections ``, and the
>   bullets for `## Not yet specified` and `## Out of scope` leave that list. The three bullets that remain —
>   `## Destination`, `## Notes`, `## Decisions so far` — are unchanged in wording, so the count and the list agree
>   at three.
> - Those two bullets move, word for word, under the `map-manager-only.md` paragraph, which now ends `does. Two of
>   the map's sections are among what it holds:` and carries them.
> - `### Resolve` step 5 names `map-manager-only.md` rather than `map.md`. Its second sentence rewrapped; no word of
>   it changed.
> - `### Rule out of scope` step 2 names `map-manager-only.md` rather than `map.md`. Rewrapped; no word changed.
>
> `## The seven files` needed no change and got none: it already stated seven and already held seven entries.
>
> **What the tree held when I read it**, on 2026-09-06 around 23:05, in the manager's main checkout. Every clause of
> the condition reads a fact off this state, and there is nothing for a checker to compare a result against, so this
> is the reading the work was written to:
>
> - `map.md` holds exactly three `##` headings — `## Destination`, `## Notes`, `## Decisions so far`. It contains no
>   fenced block at all, so no heading is hidden in one, and the strings `Not yet specified` and `Out of scope` do
>   not occur in it.
> - `map-manager-only.md` holds `## Notes`, `## Not yet specified`, `## Out of scope`.
> - `map-implementation-rules.md` holds `## Landing an implementation node's work` and `## What the work is held
>   against`.
> - `map-history.md` holds many `##` headings, all of them history sections.
> - The directory holds six regular files and four subdirectories: `nodes/`, `prototypes/`, `recovered/`,
>   `.claude/`.
>
> **Three calls a later reader would otherwise re-derive.**
>
> 1. **Six files plus the `nodes/` entry is seven, so clause 5 was already met.** I read "each file present in
>    `.scratch/graph-workflow/`" as the regular files at the directory's top level, not its subdirectories: the
>    clause names `nodes/` separately and asks for one entry standing for the files under it, which is what a
>    directory gets. Read the other way the heading would have had to say nine or ten.
> 2. **Only two `##` headings have moved out of `map.md`, so clause 2 reaches only those two.** `## Notes` is in
>    both `map.md` and `map-manager-only.md`; it did not move, part of its contents did.
>    `map-implementation-rules.md`'s two headings were minted at node 140 out of `## Notes` items and were never
>    `##` headings in `map.md`.
> 3. **The lead-in to the moved bullets is deliberately non-exhaustive** — *"Two of the map's sections are among
>    what it holds"* rather than *"holds two sections"* — because `map-manager-only.md` also holds `## Notes`, and
>    clause 7 barred me from describing it. An exhaustive-sounding lead-in would have shipped a new false statement
>    while removing an old one.
>
> **Two false statements about the fog are still in the file and clause 7 fenced me out of them**, both still
> placing fog items in `map.md`. They are reported as a new node.

**What the worker reported its work invalidates:** `none`. In its words: *"No resolved node's answer is
contradicted. Nodes 139 and 140 shipped the text I corrected, but each did so under a clause that fenced its own
worker out of these passages, and node 142 exists to close exactly that."* It also reported that neither open node
on the file is made false or trivial, naming what each still owns, and added: *"Whoever works either of them should
read this diff first."*

## Flags

*All three are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`142.1` **· settled** `ASSUMPTION` — Clause 5 asks for one list entry per "file present in
`.scratch/graph-workflow/`". The directory holds six regular files and four subdirectories (`nodes/`,
`prototypes/`, `recovered/`, `.claude/`). I read "file" as the regular files only, on the ground that the clause
names `nodes/` separately and asks for one entry standing for what is under it — which is the treatment a directory
gets. Six plus that entry is seven, the heading already said seven and the list already held seven, so I changed
neither. Read the other way the heading would need to say nine or ten and three entries would have to be added.

`142.2` **· settled** `ASSUMPTION` — Clause 2 covers every `##` heading that moved out of `map.md`. I took that to
be exactly `## Not yet specified` and `## Out of scope`. `## Notes` still stands in `map.md` and so did not move,
even though `map-manager-only.md` carries a section by that name; and `map-implementation-rules.md`'s `## Landing an
implementation node's work` and `## What the work is held against` were minted at node 140 out of `## Notes` items
rather than being `##` headings `map.md` ever held. So nothing was written under `map-implementation-rules.md`.

`142.3` **· settled** `ASSUMPTION` — The two moved bullets are introduced as *"Two of the map's sections are among
what it holds"*. `map-manager-only.md` also holds a `## Notes`, which clause 7 forbade me to describe, so an
exhaustive lead-in would have replaced one false statement with another. The wording lists what clause 2 requires
without claiming the list is complete.

***The manager's note on `142.1`.*** **Its checker reached the same reading independently and found it forced rather
than chosen**, the clause's own *"plus one entry standing for the per-node files"* contradicting a recursive count.
So the flag records a judgement that turned out to have only one available answer.

***The manager's note, and it is against the manager.*** **The checker also reported a defect of the manager's own,
outside the tree it was checking**: an untracked `decisions.md` at the **repository root**, holding node 189's index
line. The manager had created it by running a `cat >>` from the wrong working directory after a worktree was removed
under it. Verified before removal: the file held exactly one line, byte-identical to the line already correctly
present in `.scratch/graph-workflow/decisions.md`, which holds it once — so nothing was lost. **The failure mode is
worth stating: in a chained shell command the failing links reported themselves loudly and the one that succeeded
against the wrong path said nothing.**
