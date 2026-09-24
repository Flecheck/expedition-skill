# `graph-conventions.md`'s `## Labels` section still names `map.md`'s `## Notes` as where a label vocabulary is declared

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [Which statement of the bar's commands wins where a recorded copy and the repo's own
instructions disagree](174-which-statement-of-the-bars-commands-wins.md)'s worker, and pasted as it wrote it.*

> That section's first bullet reads *"A node may only use a label declared in the map's
> `## Notes`"*, and the declared label vocabulary left `map.md` for `map-manager-only.md` at node 139.
> It is the same defect class as the `## Notes` bullet
> [node 153](153-graph-conventions-notes-bullet-is-false.md) owns, at a second site that node's
> condition does not plainly reach — its clauses are framed on the bullet describing `## Notes`, and it
> also forbids the file to change in any other respect. Found independently by node 142's checker from
> behind the blindfold, in a file it was not asked to audit. Not this node's subject; reported because
> nothing owns it.

**Blockers, in the worker's words:**

> none in the graph, but the manager sequences rather than parallelises on this file —
> node 197 is claimed and running on it, and nodes 146, 153, 195 and 201 are open on it. The file's line
> numbers moved between two reads taken minutes apart during this node's work, so whoever claims this
> should read the landed diffs of whatever ran before it. Its demand is deliberately not folded into any
> of those conditions.

## Acceptance condition

*Written by node 174's worker. Pasted as it wrote it, and not the manager's.*

> The work is the file `.claude/skills/expedition/graph-conventions.md`, relative to the repository
> root. The worker may edit that file and no other, and may not write any file under `.scratch/`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. No sentence in the section headed `## Labels` states or implies that the labels a node may use
>    are declared in `map.md`'s `## Notes` section, or in any section of `map.md`.
> 2. That section instead names `map-manager-only.md` — the sibling of the effort's `map.md` holding
>    the part of the map only the manager acts on — as where a declared label vocabulary lives. The
>    file already names that file elsewhere, so no new filename is introduced.
> 3. The rule that section states is kept in force and not weakened: a node may use only a label that
>    has been declared.
> 4. That section's other statements are unchanged — that labels are optional and multi-valued, that
>    they name the family or part a node belongs to, that they are a filter and never structure, that
>    no order may be inferred from one and a label is never a node's identity, and that they are
>    absent by default so an effort declaring no vocabulary has labels on no node.
> 5. No section of the file other than `## Labels` is modified.
> 6. No file other than the one named above is modified, and no file under `.scratch/` is modified.
> 7. The finished file names no plugin, requires no skill to be invocable, and assumes no particular
>    repository, machine or toolchain.
> 8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Nobody was asked to find this.** It was found by [node 142](142-bring-graph-conventions-map-shape-into-line.md)'s checker from behind the blindfold, in a file it was not asked to audit, and node 174's worker carried it here because nothing owned it.

**It is the same defect class as [node 153](153-graph-conventions-notes-bullet-is-false.md)'s at a second site**, and its author deliberately did not fold it into node 153's condition — that condition is framed on the bullet describing `## Notes` and also forbids the file to change in any other respect, so folding would have widened a condition its own author never weighed. That is the failure [node 191](191-the-rules-file-carries-accounts-rather-than-rules.md) named.

**Five nodes are queued on `graph-conventions.md` ahead of or beside it** — 146, 153, 195, 201 and this — and the manager sequences rather than parallelising worktrees over one file. Its author recorded that the file's line numbers moved between two of its own reads minutes apart, and asks whoever claims it to read the landed diffs of whatever ran before it.

## Amendment, 2026-09-24 (from node 300)

*Written by [node 300](300-rewrite-graph-conventions-part-2.md)'s worker and filed by the manager, after that node's work landed as commit `527596c`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. Node 300's worker's search is on node 300 under `#### Re-pointing search`.*

- **Clause 4.** Replace "That section's other statements are unchanged — that labels are optional and multi-valued, that they name the family or part a node belongs to, that they are a filter and never structure, that no order may be inferred from one and a label is never a node's identity, and that they are absent by default so an effort declaring no vocabulary has labels on no node." with: "That section's other statements are unchanged: *"A label names the family or part a node belongs to, for example `CLASS` rather than `CLASS-1`. Labels are optional, and a node may carry several."*, *"A label is only a filter. Order comes from `Blocked by:` edges and never from a label."*, *"A node's identity is its `NN` and never a label."*, and *"An effort that declares no vocabulary has no labels on any node."*"

## Flags

`206.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from node 300's re-pointing list, on the ground that every word of the replacement is fixed by commit `527596c`.
