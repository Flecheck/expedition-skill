# The rules file's bar paragraph still names the map's standing preferences as project criteria

Type: implementation
Status: resolved

Blocked by: 144

## Question

*Surfaced by [Make the rules file stand alone for a reader that does not read `map.md`](144-make-the-rules-file-stand-alone.md)'s worker, and pasted as it wrote it.*

> `map-implementation-rules.md`'s `## What the work is held against` now holds both "the
> project criteria (the human's global coding principles and `/naming`), this map's own standing
> preferences, `CONTEXT.md`'s `_Avoid_` lines" in its bar paragraph and, two paragraphs below, the
> statement that the map's standing preferences are not among the standards as a whole. Node 144 could
> not repair the first, its condition forbidding any change to another paragraph of that file.

## Acceptance condition

*Written by node 144's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited.
> The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
> Done means all of the following are true of the finished tree.
> 1. The paragraph beginning `**The bar's commands for this repo, discovered on first use**` no longer
>    names the map's standing preferences among the bar's project criteria: the phrase `this map's own
>    standing preferences` is struck through, and what stands in its place either names the two blocks
>    that file holds — the ground rules and the four standing rules for writing — or states that the
>    map's standing preferences are not part of the bar.
> 2. Nothing is deleted: the superseded phrase remains in the file, marked struck.
> 3. No numbered rule in either of the two blocks that file holds is reworded, renumbered or reordered,
>    and no other paragraph of the file changes.
> 4. Every markdown link in the file resolves to a path that exists.
> 5. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**This node's own subject is [flag `144.3`](144-make-the-rules-file-stand-alone.md)**, which records the worker
leaving that paragraph intact because its condition's clause 5 forbade changing it. The flag and this node are the
two halves of one thing: the flag says the judgement was made, this node is where it gets undone.

**The blocker is the manager's bookkeeping**, taken from the `blockers: 144` its author wrote beside the node.

**The condition's clause 1 quotes a phrase the same file may hold more than once.** The worker's own retrospective
on node 144 reports meeting exactly that hazard — a quoted phrase occurring twice in this file, once in the sentence
its condition named and once in this paragraph. The manager records the risk and has not altered the condition.

## Flags

*The worker's own text, pasted. The id and the link are the manager's bookkeeping and nothing else.*

`169.1` **· settled** `ASSUMPTION` — Clause 1 offered two alternatives for what replaces the struck phrase — naming the two blocks, or stating that the map's standing preferences are not part of the bar — and I wrote both into one substitution rather than choosing between them, and added a citation to node 42 for the test that excludes the preferences. Neither the second branch nor the citation was demanded; I judged that naming the blocks without saying why the preferences left recreates, for the next reader, exactly the puzzle this node exists to remove, and that standing rule 2 for writing asks an item to cite the nodes that shaped it. Nothing outside the struck phrase's own replacement bracket changed.

## Review

***The manager's note before the first check.*** **The hazard this node was warned about did not materialise**, and the
worker checked rather than assuming: the condition's quoted phrase occurs exactly once in the file, verified by count,
and the two nearby occurrences are different strings. The manager records that the warning it carried was discharged
by measurement.

### Checker run 1 — `PASS`

*Attempt 1 of this check died mid-run on an API session limit, having established that the diff was one line. It was
**resumed rather than respawned**, under the human's standing instruction that an agent is resumed wherever it can be.
Pasted as the checker wrote it, ordered under its own headings; every sentence is the checker's.*

> **Settled first — the work moved a paragraph in the file my contract sends me to.** The single changed path is the implementation-rules file itself, so before checking anything I applied `### Where the work moved one of them` and split operative content from rationale on the operative content alone.
>
> The passages of that file that state standards are line 106 (the review route), the record-as-work rule, the five ground rules and the four standing rules for writing. **None of them changed.** The diff is `1 insertion(+), 1 deletion(-)`, hunk header `@@ -104 +104 @@` — line 104 only, which is the bar paragraph, and the bar reached me in the spawn as my contract's given #2 rather than from this file.
>
> Element by element, the set I hold work against is identical on both sides of the change, because the unmoved line 106 fixes it — and line 106 already states, unchanged, that "`map.md`'s standing preferences are not among the standards, as a whole." Line 104's before-state disagreed with that already-standing line 106; **the change removes the disagreement rather than moving anything.** So there is unmoved operative content to hold the work against, and no raise. Rationale moved, operative content did not.
>
> **Standards read, and which bore:** the four standing rules for writing (rules 2 and 4), `graph-conventions.md`'s "citing by markdown link the nodes that shaped it and never restating what those nodes hold", `CONTEXT.md`'s `_Avoid_` lines, and `/writing-for-agents`. `/coding-principles` and `/naming` did not bite — no code. Line 106 states **no reviewing skill is named for this repo**, so I ran none and went looking for none.
>
> **I read the changed path I was given as the work under lines 108-126 of that file**, which require me to say so. Nothing in it was read as a statement of intent; the acceptance condition stayed the only one. No node status line, no `decisions.md` and no `flags.md` appears among the work.
>
> **The condition, part by part:**
>
> 1. Met. `git diff --word-diff` on line 104 shows exactly two edits, both inside the target clause. The phrase is struck (`grep -oP … | cat -A` returns it exactly, byte for byte). What stands in its place satisfies **both** disjuncts, not just one.
> 2. Met. `1 insertion(+), 1 deletion(-)`; the superseded phrase is present and wrapped in `~~ ~~`. Nothing was deleted, only bracketed.
> 3. Met. The hunk header `@@ -104 +104 @@` is conclusive: every other line of the file is byte-identical to `HEAD`.
> 4. Met. Extracted all 26 markdown links, 17 unique targets, tested each: **all 17 resolve.** The one link the work added resolves.
> 5. Met. `git status --porcelain -uall` returns exactly one line.
>
> **The bar.** Its command half: **I re-discovered it rather than trusting the spawn.** No manifest or task runner at root, no `.github/workflows`, and `git ls-files` returns 185 `.md` files plus `.gitignore`, which invokes nothing. **Nothing to run, so nothing printed.** Under the *"if relevant"* clause that is a complete bar.
>
> Its non-command half holds. Against `CONTEXT.md`'s `_Avoid_` lines I checked the inserted clause **by hand rather than by grep**, per that file's own measured note that the list returns false positives. Standing rule 2 and `graph-conventions.md` are met — the clause cites node 42 by markdown link and defers with "as the review route below states" instead of restating what node 42 holds. Standing rule 4 is met: citations by link and by named paragraph, never by line number. Against `/writing-for-agents`: the clause leads with the positive and carries the exclusion second, so it does not steer by prohibition alone. Both of its uses of *below* are anchored inside this file, **which is the hazard the file's own line 5 warns about and which the work avoids.**

*No `NOT COVERED`. No questions raised.*

***The manager's note.*** **This run used [node 171](171-carry-the-record-node-reading-rule-into-the-rules-file.md)'s
rule, which landed an hour before it**, and said so in its outcome because that rule requires it: *"I read the changed
path I was given as the work under lines 108-126 of that file, which require me to say so."* **No licence was raised
and none was needed** — the third record-editing node in a row to need none, where node 144 needed one from the human.

**Two independence signals the manager records without weighing.** The checker **re-discovered the bar's command half
rather than trusting the spawn's statement of it**, and it **checked the `_Avoid_` lines by hand rather than by grep**,
citing the file's own measured warning that the list yields false positives.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*No correction round; run 1's `PASS` is the only run. Flag `169.1` is settled by the approval. **Landed as
`c8e2c69`**, rebased onto `b2c8e9b` and fast-forwarded; worktree removed, branch deleted.*

## Answer

*Pasted as the worker wrote it.*

> `map-implementation-rules.md`'s bar paragraph no longer names `map.md`'s standing preferences among the bar's project criteria. In the sentence *"So the bar here is entirely its non-command half"*, the phrase `this map's own standing preferences` is struck in place and followed by both branches clause 1 offered:
>
> > ~~this map's own standing preferences~~ **this effort's ground rules and its four standing rules for writing, the two blocks this file holds below — `map.md`'s standing preferences are not part of the bar, on [node 42](nodes/42-checker-spawn-carries-ground-rules.md)'s test as the review route below states**
>
> Three calls a later reader would otherwise re-derive.
>
> 1. **Both branches of clause 1 rather than one.** The condition allowed naming the two blocks *or* stating that the preferences are not part of the bar. Naming the blocks alone leaves the reader to infer why the preferences left; stating the exclusion alone leaves the bar's non-command half short of the two blocks that do bind. Together they say what stands and what does not, in one substitution.
> 2. **The replacement is worded to match the review-route paragraph two paragraphs below**, which already reads *"this effort's ground rules and its four standing rules for writing, both of which this file holds below"*. The bar paragraph and the standards paragraph now name the same two blocks in the same words, which is what makes the contradiction visibly gone rather than merely repaired on one side.
> 3. **The citation is to node 42, not to node 138 or 144.** Node 42 owns the *test* — a standing constraint true of any node's work may travel to a blind reader, an account of what happened may not — and that test is the reason the preferences are out.
>
> **The hazard the manager flagged did not materialise.** The condition's quoted phrase occurs exactly **once** in the file (verified by count). The nearby occurrences are different strings; neither was touched.

**What the worker reported its work invalidates:** `none`. In its words: *"The change removes a contradiction internal
to one file and contradicts no resolved node: node 42's test, node 138's finding and node 144's repair all say the
map's standing preferences are not among what work is held against, and this edit brings the last paragraph that said
otherwise into line with them."*

***The manager's note on the landing, filed because [node 179](179-the-manager-sees-its-own-writable-region.md) is
live and this is evidence for it.*** **The manager's writable region was in the broken state throughout this
landing** — the repository root not writable — **and the landing succeeded anyway.** Before starting it the manager
ran `test -w` on the five paths the landing writes: the root failed, and `.git`, `.scratch/graph-workflow`, the
target file and the worktree all passed. Only the worktree removal needed the sandbox off, for the `ro` mounts inside
it. **The manager reports this as an observation and takes no view on which of node 179's two arms it favours**, that
being the human's to settle.
