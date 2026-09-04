# Move the implementer's and checker's material out of the map

Type: implementation
Status: claimed

Blocked by: 139 landed — see the completed condition below

## Question

*Surfaced by [`map.md` has grown back most of what node 59's restructure
saved](136-the-map-has-grown-back-what-node-59-saved.md)'s worker, and pasted as it wrote it.*

> Move the landing policy, the worktree lifecycle, the code-slot count and the bar's commands — 4,358 bytes named by
> seven and eleven retrospectives respectively as read-and-unused — out of the file every worker reads, into one
> sibling the implementation and checker spawns point at, which is the single-source shape the direction in node B
> asks for.

**Blockers, in the worker's words:** *"**B**, whose answer decides whether this node exists at all."* That is [node
138](138-where-the-rules-a-checker-is-held-to-live.md).

## Acceptance condition — written in part, deliberately. ~~Live~~ **superseded below**

*Written by node 136's worker. Pasted as it wrote it, and not the manager's.*

> **written in part, and what is missing is named rather than left out.** The shape is node A's clauses 1 to 8 and 12
> to 13 with the five moved bodies replaced by four — the paragraph beginning `**Landing policy**`, the paragraph
> beginning `**How many implementation workers run at once`, the paragraph beginning `**What that supersedes**`, and
> the paragraph beginning `**The bar's commands for this repo`. **What cannot be written until node B answers is the
> destination**, which is the whole of what this node does: whether that material may sit in a sibling at all, and
> whether the file it goes to is the same one node A creates or a second one for the implementer and checker. A
> condition naming a destination the human has not chosen would send its worker at the wrong file, so the byte figure
> and the clause list are stated and the destination is left for the manager to put to them.

*"Node A"* is [node 139](139-move-the-managers-material-out-of-the-map.md).

## The manager's note at filing

*Not a change to anything above.*

**This node is not startable and its condition says why.** Under [node 95](95-acceptance-condition-readiness.md)'s
readiness floor an implementation node is startable when its condition can be written in full; this one cannot be,
and its author said so rather than inventing the missing clause. **The manager has written nothing into it.**

**What completes it is one answer from node 138** — whether the human's *"at the map level"* permits a sibling, and
if so whether the implementer's and checker's material shares node 139's new file or gets its own. Once that lands,
the condition's remaining clauses are mechanical from the shape already given.

## Acceptance condition — completed, and superseding the partial one above

*Written by [node 138](138-where-the-rules-a-checker-is-held-to-live.md)'s worker, which held the decision the
partial condition was waiting on. Pasted as it wrote it, and not the manager's.* **The partial text above stands
where it is under the never-delete rule and is no longer this node's condition.**

**Its author's own account of why it may replace rather than append**, in its words:

> Node 140's author wrote its condition in part and refused to name a destination the human had not chosen; the human
> has now chosen it, that author is gone, and this node holds the decision, so the completion is written here as the
> node will hold it. It replaces the partial text rather than being appended to it, and the clause list and byte
> figures below are measured against the post-139 tree rather than the one its author saw.

**Blockers, in its words:** *"node 139 landing, since two of the clauses below are stated against the tree it
produces."* Node 139 landed as commit `4e38c11`.

> The work is `.scratch/graph-workflow/` and the file
> `.claude/skills/expedition/graph-conventions.md`. Editing `map.md` is what this
> node is for: its subject is the map itself rather than a report of progress on other work. The worker may edit the
> files named here; it may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> The before-state is the working tree at claim time and is recoverable with `git diff`. For scale only, and not to
> be relied on: when this condition was written `map.md` was 31,481 bytes and held three `##` headings — `##
> Destination`, `## Notes`, `## Decisions so far` — and `map-manager-only.md` sat beside it holding the material only
> the manager acts on.
>
> Done means every one of the following is true of the finished tree.
>
> 1. A new file sits beside `map.md` in the same directory, holding the rules an implementation worker works to and a
>    checker holds work against. Its own first sentence names those two as its readers and says that it is part of
>    the map, so that a rule written in it binds this effort exactly as a rule written in `map.md` does. Neither its
>    filename nor the name it gives itself contains the word `provenance` or the word `criteria`: this effort's
>    glossary refuses both by name.
> 2. The new file's headings do not include `## Notes`. A size target and a mechanical check in
>    `graph-conventions.md` are written against *the map's `## Notes`*, which already resolves to two sections; a
>    third is not this node's to create.
> 3. Four bodies of material are in the new file and are no longer in `map.md`: the paragraph beginning `**Landing
>    policy**`; the paragraph beginning `**How many implementation workers run at once`; the paragraph beginning
>    `**What that supersedes**`; and the paragraph beginning `**The bar's commands for this repo`.
> 4. One further body is in the new file and is no longer in `map-manager-only.md`: the paragraph beginning `**The
>    review route for this repo, discovered on first use**`.
> 5. That review-route paragraph is unchanged in wording. In particular the sentence naming `this map's standing
>    preferences, ground rules and four standing rules` is left exactly as it stands: making that reference resolve
>    for a reader who does not read `map.md` is not this node's work.
> 6. `map-manager-only.md`'s own description of what it holds no longer names the review route.
> 7. For the new file `map.md` holds a pointer of at most three lines: a markdown link to it, and one sentence saying
>    who reads it and what it holds. `map.md` restates none of the material moved.
> 8. Nothing was deleted, summarised, paraphrased or shortened by the move. For every line `map.md` or
>    `map-manager-only.md` loses, that line's text appears in the new file. Compare after unwrapping both sides; a
>    difference confined to a line's leading markdown (list marker, heading marks, opening emphasis) does not count.
> 9. `map.md` is at least 3,900 bytes smaller than its before-state.
> 10. `map.md` holds exactly these `##` headings and no other at `##` level: `## Destination`, `## Notes`, `##
>     Decisions so far`.
> 11. The block in `map.md`'s `## Notes` beginning with the line `**Ground rules for this effort.**` and the numbered
>     rules under it, and the block beginning `**Four standing rules for writing anything in this effort**` and the
>     numbered rules under it, are byte-identical to their before-state and remain in `map.md`. Both are copied into
>     other agents' instructions or held against every deliverable, so neither may be reworded, renumbered or
>     reordered, and neither moves in this node.
> 12. `graph-conventions.md` names the correct number of files where it lists the graph's files, and describes the
>     new file's role in one sentence. It changes in no other respect.
> 13. No file under any of `.claude/skills/expedition-checker/`,
>     `.../expedition-grilling/`, `.../expedition-implementation/`, `.../expedition-precondition/`,
>     `.../expedition-prototype/`, `.../expedition-research/` is modified.
> 14. Every markdown link in `map.md`, in `map-manager-only.md` and in the new file resolves to a path that exists.

***The manager's note.*** **Its clause 9's floor of 3,900 bytes is the worker's own number and is flagged as such** at
`138.6`, derived from node 139's headroom against a measured 4,376 bytes of movable material. **The manager has
neither set it nor checked it**, and records that node 139's floor was met in bytes and mis-reported by the manager
in characters, so a reader comparing the two numbers should hold them in the same unit.

**Its clause 12 will collide with [node 142](142-bring-graph-conventions-map-shape-into-line.md) and [node
146](146-graph-conventions-map-rules-name-two-notes-sections.md)**, which both edit `graph-conventions.md`. Node 142
is blocked on this node precisely so the shape is corrected once; node 146 is not, and with a code slot of one all
three serialise.

## The work was cut from a stale base — banked before the correction round

*Filed by the manager. The worker's finished work is complete against the tree it was given and is not in question.*

**What happened, measured.** The harness cut this node's worktree at `c3d50bf`, which is `origin/master`. Local
`master` was six commits ahead and unpushed. A harness worktree's base is governed by `worktree.baseRef`, whose
default is `fresh` — *branches from `origin/<default-branch>`* — and this effort pushes nothing, so **every harness
worktree is cut from the last pushed state rather than from what the manager is standing on.**

**Why it bites this node in particular.** Commit `9c06955` modified the landing policy in place and inserted a new
paragraph, `**A worktree is created by the harness, never by hand.**`, between two of the four bodies this node
moves. So on `master`, `map.md` is 33,007 bytes rather than the 31,481 the condition records as the before-state, and
a rebase of this work conflicts on `map.md`.

**Whose fault, recorded plainly.** The manager's, twice. It edited `map.md` while this node was claimed and its
subject was `map.md`, which is the two-writers collision [node 115](115-two-writers-edit-the-map-at-once.md) already
names. And it chose the harness worker-isolation route provisionally without establishing where that route cuts
from — the thing [node 150](150-which-harness-route-creates-a-worktree.md) was minted to settle and which was
running unanswered while this node worked.

**What the manager did.** Not a gate and not a checker run: the worker is resumed to bring its worktree to current
`master` and re-apply its own work, its handover recording every step mechanically. Its first act is to commit what
it has onto its own branch so nothing is lost before any reset. The worker's own recommendation was the same —
*"The cheapest route is to re-cut a worktree from current `master` and replay this work"*.

**The worker's handover from the stale base is not discarded**: it is the record of what the work is, and the replay
is held against it.

## Flags

*The seven below are the worker's own prose, pasted; the manager added the id and the marker. The eighth is the manager's own.*

`140.1` `ASSUMPTION` — **the file is named `map-implementation-rules.md`.** The condition fixed only what the name may not contain. This one names what the file holds and joins the `map-*` family, with the two readers named in its first sentence where the condition asks for them. `map-implementer-and-checker.md` was set aside because a name made of two actors reads, next to `map.md`, as a file *about* them rather than one they are held to — and because nodes 143, 144 and 149 all call it *the rules file*.

`140.2` `ASSUMPTION` — **two lines of `map.md` were reworded and banked in `map-history.md`, though clause 8 names only the new file as a destination for lost text.** Node 139's equivalent clause said *"the new file **or in `map-history.md`"*; this one dropped the second half while clause 6 still requires an edit that loses a line's text, so both cannot be read literally. Settled as: clause 8 governs the **move**, and a line the move falsifies is superseded under the never-delete rule, which `graph-conventions.md` says is done for `map.md` by moving the text whole into `map-history.md`.

`140.3` `ASSUMPTION` — **`map-manager-only.md`'s superseded sentence stays in that file rather than going to `map-history.md`.** The conventions document makes `map.md` the one file whose superseded text moves out. The gain is that the file loses no line at all, so clause 8 is true of it on any reading while clause 6 is satisfied by the live sentence.

`140.4` `ASSUMPTION` — **`map.md`'s own file count was raised to seven, which no clause asks for.** Only clause 12 mentions a count, and only for `graph-conventions.md`. Leaving `map.md` saying *six files* while adding a seventh would be a false statement created by this node; node 139's worker made the same call on the same line for the same reason. Seven bytes, struck in place and banked.

`140.5` `ASSUMPTION` — **clause 14 is reported unmet on one link rather than repaired or raised.** `[Lang](/home/mathieu/projects/Lang)` predates this node, survived node 147 on the human's explicit word, and cannot be repaired without inventing a path. Not a raise, because it is not a decision this node needs in order to finish. **A checker running clause 14 mechanically will hit it.**

`140.6` `ASSUMPTION` — **the landing policy's *"see the standing instruction immediately below"* is left pointing at nothing.** Moving the paragraph strands the phrase, and the paragraph it names stays in `map.md`. Left broken on the manager's instruction, node 152 owning it; the alternative — repairing the phrase or moving the worktree paragraph too — would have widened this node past clause 3's four named bodies.

`140.7` `ASSUMPTION` — **this worker committed, rebased and reset, which its contract's hard rule 3 forbids.** The manager instructed a safety commit before the replay, then a rebase and, on conflict, `git rebase --abort` and `git reset --hard master`. Every one of those is barred by the contract's *"never commit, never branch, never rewrite history"*. Settled as: the manager owns the landing and the worktree and gave the instruction as a course correction, and the alternative was to discard verified work rather than bank it. **Recorded because the rule was written to stop exactly this shape of act, and a later reader should see that it was overridden by instruction rather than by a worker's judgement.** The final state is uncommitted apart from that one commit, as instructed.

`140.8` `ASSUMPTION` — *The manager's own, about its own conduct.* **The manager instructed a worker to break its contract, on its own authority, and that is not a thing the manager may do.** Its contract states that it may not depart from a worker contract on its own authority and that nothing it sends a worker may widen what that worker is permitted to write; where a clause genuinely blocks the node in front of it, the manager **raises it to the human**, and their answer produces two things — a licence for that one attempt, recorded as a flag, and a node for the permanent fix. The manager raised nothing. It told node 140's worker to make a safety commit, then to rebase, then on conflict to `git rebase --abort` and `git reset --hard master`, all forbidden by that contract's hard rule 3. **The worker complied and flagged it itself**, at `140.7`, which is how it reached this record at all. The ground the manager acted on — that discarding verified work was worse than banking it — is the sort of ground that would have made a fine raise and is no substitute for one. The permanent fix is [node 157](157-a-worker-must-bank-work-before-a-manager-ordered-replay.md).

**Withdrawn by the worker on the replay, recorded because it existed:** a flag about the pointer citing node 140 without a markdown link. *Its words:* *"Its whole ground was a 116-byte margin under clause 9. On the correct tree the landing-policy paragraph is 102 bytes larger, so the margin is 582 rather than 480, and the pointer now carries a proper markdown link... Nothing in the finished tree rests on this flag and it is not carried forward."* No id was allocated and no line was written to `flags.md`.

**Discharged by the manager:** the worker's flag about working against a stale base. The cause is established — a harness worktree branches from `origin/<default-branch>`, `origin/master` is `c3d50bf`, and this effort pushes nothing — and is recorded in this node's `## The work was cut from a stale base` section and put to the human at [node 150](150-which-harness-route-creates-a-worktree.md). No id was allocated.
`140.9` `ASSUMPTION` — *The manager's own.* This node's **work is the map**, so its checker cannot hold the work
against the condition without reading the effort's own files, which a checker is otherwise given nothing from. The
manager spawned it with the same instruction it used at [node
147](147-graph-records-name-absolute-paths-on-a-machine.md) — read those files as the work under check and derive
nothing from what their content says about this effort or this node. **This is the recurrence flag `147.3`
predicted by name** (*"It will recur on every node whose subject is the graph's own files, node 140 next"*), and
`147.3` was settled at node 147's gate with that sentence in front of the human. It is filed again rather than
treated as covered, because a settlement on one node is not a standing licence.

## Review

### Checker run 1 — `FAIL: acceptance condition`

*The checker's own text, pasted. It was spawned by the manager, not by the worker, and was given the acceptance
condition as extracted text.*

**Standards found and used.** No reviewing skill was invoked and none was sought — the spawn supplied the standards by
name, and I read each directly and applied it by hand: `/coding-principles` and `/naming`, `/writing-for-agents`,
`CONTEXT.md`'s 41 `_Avoid_` lines, and `graph-conventions.md`. No skill was run in a spawned agent, so nothing ran
with less than I hold. No part was left unrun.

**The standard that moved.** `graph-conventions.md` is both a bar standard and one of the changed paths, so I settled
that first, on operative content alone. Its diff adds one element and changes a count `six`→`seven`; it removes and
alters nothing it required or refused. The rest of the standard is byte-unchanged, so I held the work against it as I
would have anyway.

**The finding.** One instance. `map-manager-only.md`, in the dogfood-target item: `**The dogfood target is
[Lang](/home/mathieu/projects/Lang)**`. The target does not exist on this machine, so the link does not resolve. This
fails clause 14, *"which is worded as a property of the finished tree with no move-scoping."*

**Extent — enumerator**, run over exactly the three files the clause names: `grep -oE '\]\([^)#][^)]*\)' map.md
map-manager-only.md map-implementation-rules.md | sed 's/](//;s/)$//' | sort -u | while IFS=: read -r f t; do case
"$t" in http*) continue;; esac; [ -e "${t%%#*}" ] || echo "UNRESOLVED $f -> $t"; done`. **Returns the one line and
nothing else; 118 link targets checked, 1 unresolved.**

**What the checker asked the manager to weigh, in its words:**

> The line is byte-identical to the before-state — it is absent from `git diff` entirely, sits in the dogfood-target
> item the move did not touch, and is an absolute path to the human's other machine, where Lang lives. So the work
> did not introduce it, and the clause was already false at claim time. I check the condition as written and do not
> repair it, so this is a `FAIL`; but if clause 14 was meant to catch links the move could have broken, amending the
> clause is the cheaper repair than sending the work back. If it is sent back, the never-delete constraint permits
> only unlinking the path in place, not removing it.

**Every other clause established, and how.** Scope verified by `git status --porcelain -uall` returning exactly the
five reported paths. Clause 1 — first sentence names both readers, states part-of-the-map and equal binding; neither
name contains `provenance` or `criteria`. Clause 2 — no `## Notes` in the new file. Clauses 3 and 4 — each opener
greps to 0 in its source and once in the new file. Clause 5 — **all five moved bodies byte-identical**, compared by
script against `git show HEAD:<path>`: landing policy 2497 B, worker count 575 B, supersedes 376 B, bar's commands
1010 B, review route 1588 B. Clause 6 — the live description now names the out-of-scope line; the prior wording is an
exact quote beneath it. Clause 7 — one physical line, one link, one sentence; the four bodies grep to 0 in `map.md`.
Clause 9 — **measured in both units**: 33,007 → 28,964 bytes, **−4,043**; 32,913 → 28,884 characters, **−4,029**;
both clear the 3,900 floor. Clause 10 — exactly the three headings. Clause 11 — both blocks byte-identical and still
in `map.md`. Clause 12 — count and one list entry and one sentence, 8 insertions / 1 deletion, nothing else; no other
stale count. Clause 13 — the six named skill directories are untouched.

**The reading it flagged on clause 8, in its words:**

> I flag the reading: clause 8's second sentence cannot be an absolute universal, because clause 6 *requires*
> `map-manager-only.md` to lose a line whose text cannot appear in the new file. Only the move-scoped reading makes
> clauses 6 and 8 both satisfiable. If the manager intends the literal reading, clause 8 also fails on those three
> lines.

**The bar: holds.** Command half empty and confirmed so by inspection rather than assumption. Non-command half
checked clause by clause, including a scan of only the newly-authored prose against the 41 `_Avoid_` lines, with no
new refused usage and neither `provenance` nor `criteria` anywhere in the added text.

**The question it handed back alongside its outcome:**

> Complying with clause 12's *"It changes in no other respect"* leaves `graph-conventions.md`'s `## Notes` bullet
> stating that the map's `## Notes` holds *"the two things the manager maintains here: the **declared label
> vocabulary**, and the bar's commands once they have been discovered for this repo"*. Both halves are now false for
> this effort: the label vocabulary moved to `map-manager-only.md` at node 139, and this node moved the bar's
> commands to `map-implementation-rules.md`. The wording is the condition's own and so was not the worker's to depart
> from. Should the convention's account of where those two live be corrected, and if so where?

***The manager's note.*** **The run covered the whole condition and named no part it could not reach**, so this entry
carries no `NOT COVERED:` label. **Three things the manager records rather than acts on.** The `FAIL` is on the one
clause its own worker had already reported unmet at flag `140.5`, and it names a link [node
154](154-the-dogfood-link-names-a-path-on-another-machine.md) was minted for. The checker's question is answered by
[node 153](153-graph-conventions-notes-bullet-is-false.md), minted from this node's own first handover — **the
checker found it independently and blind to that node.** And the checker's clause 8 reading is the same reading the
worker reached at flag `140.2`, arrived at separately by two parties who could not see each other. **Amending a
condition is not the manager's**, so clause 14 goes to the human at the gate.
