# `graph-conventions.md` still puts the fog in `map.md` outside the two procedure steps node 142 corrected

Type: implementation
Status: superseded
Superseded by: 338

Blocked by: 142

## Question

*Surfaced by [Bring `graph-conventions.md`'s map shape into line with the split map](142-bring-graph-conventions-map-shape-into-line.md)'s worker, and pasted as it wrote it.*

> Two passages of `.claude/skills/expedition/graph-conventions.md` still place fog items in `map.md`, where the fog
> left `map.md` for `map-manager-only.md` at node 139. `## Writing the map` opens *"Every note, standing preference
> and fog item in `map.md` is a **current statement**"*, and the `### Change the map` procedure opens *"Use when a
> note, a standing preference or a fog item in `map.md` no longer says what holds. A new item is written straight
> into `map.md`"*, its step 2 writing the replacement into `map.md` too. Node 142's clauses 3 and 4 reached only the
> `### Resolve` and `### Rule out of scope` steps and its clause 7 barred everything else, so these two were left
> standing. A third passage is doubtful rather than plainly false and is the reason this node is not purely
> mechanical: the file's opening says *"`map.md` is the one file whose superseded text is also *moved* rather than
> left in place"*, while `map-manager-only.md` is part of the map, holds the fog, has its own superseded fog moved
> verbatim into `map-history.md` under a heading `## Not yet specified — superseded at the close of the session that
> ran nodes 129-163`, and at the same time keeps a superseded sentence of its own standing in place at its lines 7
> to 9. So the record's practice on the sibling files points two ways at once.

**Blockers, in the worker's words:** *"none — node 139 landed as `4e38c11`, node 140 as `ba91cf8`."* **The manager
has added the edge to 142**, whose work is on the same file and whose clause 7 fenced these passages off; the two
cannot run in parallel worktrees.

## Acceptance condition

*Written by node 142's worker. Pasted as it wrote it, and not the manager's.*

> The work is the file `.claude/skills/expedition/graph-conventions.md`. It is written against whatever
> `.scratch/graph-workflow/` holds at claim time, because which sections sit in which file of the map is a fact of
> that directory rather than of this condition. Done means every one of the following is true of the finished tree.
>
> 1. The sentence under `## Writing the map` beginning `Every note, standing preference and fog item` names, for
>    each kind of item it lists, the file in `.scratch/graph-workflow/` that actually holds that kind. Where two
>    kinds live in different files, the sentence says so rather than naming one file for all of them.
> 2. The `### Change the map` procedure's opening sentence, and each of its numbered steps that names a file to
>    write to, names the file that actually holds the kind of item being changed. Where that depends on the kind, the
>    procedure says so rather than naming one file for every kind.
> 3. The sentence beginning `No edit deletes` and ending `see `## Writing the map` below.` states, truly of
>    `.scratch/graph-workflow/` at claim time, which files of the map move their superseded text out to another file
>    and which mark it in place.
> 4. No file under `.scratch/graph-workflow/` is modified, and no file outside
>    `.claude/skills/expedition/graph-conventions.md` is modified.
> 5. `graph-conventions.md` changes in no respect other than clauses 1 to 3.

**What its author could not write into that condition, stated plainly and pasted as it wrote it:**

> clause 3 asks the worker to state a truth it may find the record does not hold consistently —
> `map-manager-only.md` both sends superseded fog to `map-history.md` and keeps a superseded sentence in place.
> Whether the never-delete rule's *move* applies to every file of the map or to `map.md` alone is a design point
> nobody has settled, and it was not mine to settle from inside node 142. **A worker that finds clause 3 turns on
> that point should raise rather than pick.**

## The manager's note at filing

*Not a change to anything above.*

**The design point clause 3 turns on has been settled since this condition was written, and by the human.** [Node
189](189-where-the-never-delete-rule-stops.md) resolved that the cut follows **what a piece of text is** rather than
which file it sits in: a superseded **rule statement** is replaced and its old text banked verbatim to
`map-history.md`, while text that records what happened is struck in place. So `map-manager-only.md` pointing two
ways at once is not an inconsistency to adjudicate — it is one file holding both kinds of text. **The manager
states this beside the condition rather than editing it**, and the condition's author's instruction to raise rather
than pick stands: a worker that reads clause 3 differently should still raise.

**This file is congested.** [Node 146](146-graph-conventions-map-rules-name-two-notes-sections.md), [node
153](153-graph-conventions-notes-bullet-is-false.md) and [node
194](194-ship-where-the-never-delete-rule-stops.md) are all open on it, and node 142's checker reported two further
defects in it from behind the blindfold — the `## Notes` bullet's claim about where the bar's commands live, and the
`## Labels` sentence pointing at the map's `## Notes` for the label vocabulary. The manager sequences these rather
than running them together.

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Clause 3.** Replace "The sentence beginning `No edit deletes` and ending `see `## Writing the map` below.`" with "The two paragraphs running from the one beginning `No edit deletes` to the sentence `` `## Writing the map` below describes how. ``". The rest is unchanged. Clause 1's "Every note, standing preference and fog item" still opens its sentence.

## Flags

`195.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 338](338-say-in-graph-conventions-md-which-file-of-the-map.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
