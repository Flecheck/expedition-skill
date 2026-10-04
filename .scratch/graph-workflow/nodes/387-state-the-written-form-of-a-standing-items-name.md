# State in the retrospective bullet the form a standing item's name is written in

Type: implementation
Status: claimed
Blocked by: 220

## Question

map-manager-only.md's retrospective bullet has the worker name each standing item it reports, but fixes no written form. Entry (j) of derivations.md finds names in exactly one form, as the human settled at node 220's raise 1 on 2026-10-04. A name written in any other form is invisible to it, and so to the next worker looking for a name to reuse.

*Reported by [node 220](220-derive-how-many-times-each-standing-item-was-reported.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "220 (the entry the bullet points at must have landed)". On joining: "node 284 also edits `map-manager-only.md`, but only its *How the worktree is made* Create bullet, which is a different concern."*

## Acceptance condition

*Authored by node 220's worker and filed by the manager.*

> The work is an edit to one file, `.scratch/graph-workflow/map-manager-only.md`. Nothing else changes.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `.scratch/graph-workflow/map-manager-only.md`, the bullet beginning **"Every worker returns a retrospective as the last handover part, on this effort only"** states that the worker writes each standing item's name as a numbered or bulleted list item of its retrospective, whose text opens with the name in a code span. The name is two or more words of lowercase letters and digits joined by hyphens. The name is followed in that list item by the count of earlier retrospectives carrying it and their node ids.
> 2. That bullet states that the existing names, with their counts and node files, are obtained by running the entry headed `## (j) Item names carried by the retrospectives` in `.scratch/graph-workflow/derivations.md`, and that a name written in any other form is not found by that entry.
> 3. No statement already in that bullet is changed or removed. In particular, the human's quoted instruction beginning *"Could you, for this effort only, ask subagents"* and the four questions numbered (1) to (4) are unchanged character for character.
> 4. No file under `.claude/` is modified, and no file in `.scratch/graph-workflow/` other than `map-manager-only.md` is modified.
> 5. The tree meets the bar.
>
> The scope came from no search: the named bullet is the work, not an instance of a defect.

## Amendment, 2026-10-04 (from node 220, correction round 1)

*Written by [node 220](220-derive-how-many-times-each-standing-item-was-reported.md)'s worker, the author of this node's condition, in its correction-round handover, and filed by the manager before this node is claimed. The worker's words, pasted:*

- "In its clause 1, after "joined by hyphens", add: "The list item may sit inside a blockquote." This keeps it matched to entry (j)."

