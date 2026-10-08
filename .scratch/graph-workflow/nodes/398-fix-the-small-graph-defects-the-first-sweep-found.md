# Fix the small graph defects the first sweep found

Type: implementation
Status: claimed
Blocked by: none

## Question

This work leaves the graph's edges, back-edges and indexes consistent, so the second sweep, and anyone reading the graph, meets no broken link the first sweep already reported. The first sweep ([node 396](396-sweep-round-1.md)) found them under checks 1, 2, 5 and 6.

*Minted by the manager from the human's `verbatim` "ok", 2026-10-08, to part 2 of the manager's proposal recorded on node 396.*

## Acceptance condition

*Written by the manager, who minted the node.*

> The work is files in `.scratch/graph-workflow/`: the node files named below, `decisions.md` and `flags.md`. No other file may be edited, and no node's `Status:` line changes. The changes to `decisions.md` and `flags.md` are the node's work.
>
> Scope: the instances are the ones the first sweep listed, in node 396's pasted report under checks 1, 2, 5 and 6c. That report's list is the scope. An instance found outside it is reported and not edited.
>
> Done when all of the following hold.
>
> 1. In `nodes/164-what-a-standards-path-may-hold.md`, `Blocked by:` names node 334 in place of node 151.
> 2. Each of these replacement nodes carries the superseded node's number in its `Supersedes:` field, which is added where it is absent: node 76 carries 61; node 143 carries 72; node 332 carries 81 beside the numbers it already holds; node 100 carries 192; node 311 carries 279.
> 3. In `decisions.md`, node 131 has exactly one line that is not struck, so one of its two identical lines is struck through in place.
> 4. In `decisions.md`, nodes 218 and 243 each have exactly one line that is not struck. Each added line uses the node's current answer as the node file states it. Where the node file states no answer from which a line can be taken, the worker reports that and adds no line for that node.
> 5. `flags.md` has one line for each of flags 265.2, 265.3, 265.4 and 283.1, in the form the file's other lines take, taking each flag's index sentence from its entry on its node. Where an entry gives no index sentence, the line uses the entry's own one-line summary, and the worker says so.
> 6. Nothing is deleted from any file. Struck text stays in place.
> 7. The working tree meets the bar.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-08.*

`````
HANDOVER:      Fix the small graph defects the first sweep found

ANSWER:        The defects that node 396's sweep report listed under checks 1, 2, 5 (the `decisions.md` counts) and 6c are repaired in the record. Nothing was deleted, and no `Status:` line changed.
- Check 1: in node 164, `Blocked by: 143, 151` now reads `Blocked by: 143, ~~151~~ 334`. Number 151 is struck in place rather than overwritten, because the condition's clause 6 forbids deletion. Under the reading rule in `graph-conventions.md`, a struck number yields nothing, so the field gives 143 and 334.
- Check 2: these `Supersedes:` fields were added: node 76 `Supersedes: 61`, node 143 `Supersedes: 72`, node 100 `Supersedes: 192` and node 311 `Supersedes: 279`. Node 332's field now reads `Supersedes: 90, 92, 134, 247, 81`. Each new field goes after `Blocked by:` where the node has one (76, 143) and after `Status:` where it has none (100, 311), which follows the field order in `graph-conventions.md`.
- Check 5, `decisions.md`, node 131: the second of the two identical lines is struck in place. It carries the note "Struck as an identical copy of the line above, by node 398".
- Check 5, node 218: the node has no `## Answer`. A current line was appended anyway, taken from the node's `### Gate — approve` "What it decided" paragraph and its two later annotations. The line says that `.claude/rules/expedition-triggers.md` landed holding the trigger-duties, that the harness loads it through its `paths:` frontmatter, and that the human has since narrowed the glob and changed two of its four triggers.
- Check 5, node 243: a current line was appended, taken from its `## Answer` as the node's own second annotation corrects it. The route stands. The worker starts in a directory that is neither the repository root nor the worktree. It then calls `EnterWorktree` by absolute path, which is sufficient for write access but not necessary.
- Check 6c: `flags.md` gains four `- [x]` lines, for 265.2, 265.3 and 265.4 (`ASSUMPTION`) and for 283.1 (`MANAGER-WRONG`). They are marked `[x]` because each node carries a manager's note dated 2026-09-29 saying its outstanding flags were settled in the batch the human approved at node 366's Q4.
- Re-run after the edits: checks 1 and 2 pass over the whole graph. Nodes 131, 218 and 243 each have exactly one unstruck and one struck line in `decisions.md`, and each of the four flag ids has exactly one line in `flags.md`.

INDEX LINE:    The first sweep's small defects are repaired: node 164's stale blocker, five missing `Supersedes:` back-edges, the `decisions.md` lines for nodes 131, 218 and 243, and four missing `flags.md` lines.

FLAGS:
- ASSUMPTION. Prose: Clause 1 asks that node 164's `Blocked by:` name 334 "in place of" 151, and step 4 of `### Supersede` says "replace". Clause 6 forbids deleting anything. I struck 151 in place and added 334 after it (`143, ~~151~~ 334`). Under the `Blocked by:` reading rule this yields exactly 143 and 334, so both clauses hold. Index: Node 398's worker struck node 164's stale blocker 151 in place and added 334, rather than overwriting it, to keep the condition's no-deletion clause.
- ASSUMPTION. Prose: Node 218 has no `## Answer` section. Clause 4 allows adding no line where the node file states no answer a line can be taken from. I judged that a line can be taken. The `### Gate — approve` paragraph states what landed, and the two later annotations state what has since changed (the human narrowed the glob, and two of the four triggers changed). The line was written from those three passages. Index: Node 398's worker wrote node 218's current `decisions.md` line from its gate approval and annotations, since the node has no `## Answer` section.
- ASSUMPTION. Prose: For node 243, the struck `decisions.md` line already carries a manager-written "Replacement line" saying the inherited sandbox region is what permits the write. The node file's own second annotation (2026-09-19, from node 265) says instead that the `EnterWorktree` call is sufficient but not necessary. Clause 4 asks for the answer as the node file states it, so I used the node file's form. Index: Node 398's worker wrote node 243's current line from the node file's second annotation, not from the differing replacement text on its struck `decisions.md` line.
- ASSUMPTION. Prose: The four new flag lines are `- [x]`, because the manager's notes of 2026-09-29 on nodes 265 and 283 record those flags as settled by the human at node 366's Q4. `flags.md` wins on state. The four entries on the nodes still carry no `**· settled**` marker, so check 6 will now report these four as state mismatches (the sweep's group g pattern) instead of missing lines. I did not edit the entries: they are outside the files this condition lets me edit, and the human chose to leave old flag drift alone. Index: Node 398's worker filed flags 265.2–265.4 and 283.1 as settled, per the 2026-09-29 notes, leaving their node entries without the settled marker.
- ASSUMPTION. Prose: None of the four entries gives an index sentence. For 265.2, 265.3 and 265.4 I used each entry's bolded opening sentence, which is its one-line summary, with "I" recast as "Node 265's worker" to match the file's other lines and keep the referent clear. Entry 283.1 has no summary sentence, so I used its sentence "The manager counted filings and reported them as landings, which overstates the cost of the very thing the human was questioning" word for word. Index: Node 398's worker built the four flag lines from each entry's opening or key sentence, since none of the entries gives an index sentence.
- FRICTION. Prose: The implementation contract says "Leave `flags.md` unread. It is not yours." This node's acceptance condition makes `flags.md` its work and requires lines "in the form the file's other lines take". I read the file's lines as the work under edit, which the rules file's paragraph on record files as work allows. The contract has no exception for a node whose work is `flags.md`. Index: The implementation contract's "leave `flags.md` unread" has no exception for a node whose acceptance condition makes `flags.md` the work.

NEW NODES:     none

INVALIDATIONS: none. Every edit brings the record in line with what nodes already state, and no resolved node's answer changes. An observation that was not edited: node 243's new `decisions.md` line states a route (`EnterWorktree`) that node 265 later replaced with plain git. Node 243 stays `resolved` with no `Superseded by:`, as before.

CONDITIONS:    The only open or claimed nodes are 397 (claimed) and 398. I searched node 397's file for `131`, `218`, `243`, `265.`, `283.1`, `164` and `Supersedes`, with no match. No replacement clause, and no question changed.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none received yet.
Paths touched, all under /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/398-graph-fixes/.scratch/graph-workflow/:
- decisions.md
- flags.md
- nodes/164-what-a-standards-path-may-hold.md
- nodes/76-write-the-manager-skill.md
- nodes/143-rules-arrive-by-the-spawn-never-by-a-search.md
- nodes/332-repair-the-glossarys-code-slot-reject-kinds-grilling-and-closed-text.md
- nodes/100-the-manager-starts-the-next-node-rather-than-proposing-it.md
- nodes/311-may-the-human-amend-a-held-nodes-condition-of-their-own-accord.md

The bar: the repo's root `CLAUDE.md` `## Commands` says there is no build, no tests, no formatter and no CI. That agrees with the copy in `map-implementation-rules.md`. `git diff --check` is clean. The changes are additions and in-place strikes only: three lines changed and ten added (`decisions.md` 1 changed + 2 added; `flags.md` 4 added; node 164's and node 332's header lines changed in place; nodes 76, 143, 100 and 311 gain one header line each).

Files other nodes are written against: none moved, and no files are left in an older form.

Proposed commit message:
```
Graph state: repair the first sweep's small defects

Node 164's stale blocker, five Supersedes back-edges, the decisions.md
lines for nodes 131, 218 and 243, and flags.md lines for 265.2-265.4
and 283.1.

Node: graph-workflow/398
```

RETROSPECTIVE
1. What I had to hunt for:
- `settled-state-only-in-a-trailing-note`: what state the four flag lines should carry. The condition is silent on it, and the sweep report says "None of these is marked settled". The answer was in a manager's note dated 2026-09-29 at the very bottom of nodes 265 and 283. I looked first at their `## Flags` entries. New name, carried by no earlier retrospective.
- `contract-forbids-a-file-the-node-edits`: the contract's "Leave `flags.md` unread" against a node whose work is `flags.md`. I settled it from the record-files paragraph in `map-implementation-rules.md`. New name.
2. What arrived in my context that this node did not need:
- `map-read-whole-for-a-few-items`: almost none of `map.md` bore on this node, only the never-delete preference. Carried by 22 earlier retrospectives: nodes 135, 178, 185, 205, 214, 220, 284, 317, 382, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 397, 40, 41.
- `rules-file-read-whole-for-one-section`: only the paragraph on record files as work applied. Count 18; files 178, 185, 214, 220, 317, 382, 386, 387, 388, 390, 391, 392, 393, 395, 397, 40, 41.
- The implementation contract's sections on writing NEW NODES conditions were also not needed for a record-only node.
3. What would have made this node easier:
- `condition-silent-on-flag-state`: the condition should have stated the checkbox state for the four flag lines, and whether a gate approval counts as an "answer" for node 218. New name.
4. What I read that was stale, wrong or contradicted something else:
- `stale-number-in-the-record`: the sweep report's `flags.md` line count (815, now 858) and its `decisions.md` line numbers. Count 11; files 178, 185, 212, 220, 382, 385, 386, 388, 391, 392.
- `index-line-contradicts-node-file`: node 243's struck `decisions.md` line carries replacement text that differs from the node file's second annotation. Also, the sweep's "none of these is marked settled" contradicts the 2026-09-29 notes on nodes 265 and 283. New name.
`````

## Flags

`398.1` `ASSUMPTION` — Node 164's stale blocker was struck in place and 334 added. *(The worker's full text is under its handover's `FLAGS`.)*

`398.2` `ASSUMPTION` — Node 218's line was written from its gate approval and annotations. *(The worker's full text is under its handover's `FLAGS`.)*

`398.3` `ASSUMPTION` — Node 243's line follows the node file's annotation, not the struck line's replacement text. *(The worker's full text is under its handover's `FLAGS`.)*

`398.4` `ASSUMPTION` — The four flag lines were filed as settled, per the 2026-09-29 notes. *(The worker's full text is under its handover's `FLAGS`.)*

`398.5` `ASSUMPTION` — The four flag lines were built from each entry's opening or key sentence. *(The worker's full text is under its handover's `FLAGS`.)*

`398.6` `FRICTION` — The implementation contract's "leave flags.md unread" has no exception for a node whose work is flags.md. *(The worker's full text is under its handover's `FLAGS`.)*
