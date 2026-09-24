# Write the adoption procedure

Type: implementation
Status: open

Blocked by: 18

## Question

*Surfaced by [Adopting an in-flight effort](18-adopting-in-flight-effort.md)'s worker, and pasted as it wrote it.*

> Write the file that tells a manager how to start an effort from a directory of work that already exists. This is
> the second of the two pieces the map's fog item *"The implementation nodes that write the actual skill files"*
> names, and the one it says waits on node 18.

**Blockers, in the worker's words:** *"58. Node 58 qualifies the graph-file ban so that a worker whose own node's
work is a change to a graph file makes that change itself. The procedure this node writes hands the bulk import to
workers, so if 58 does not land the procedure has no performer to name."*

**The manager's note at filing:** [node 58](58-qualify-the-graph-file-ban.md) has since been approved and landed as
commit `392e0ae`, so that blocker is discharged and is not carried in the header. What remains is `Blocked by: 18`,
this node's source, which is `resolved`.

## Acceptance condition

*Written by node 18's worker. Pasted as it wrote it, and not the manager's.*

> A file exists at `.claude/skills/expedition/adoption.md`. It is instructions to a manager starting an effort from a
> directory of work that already exists, and it states all of the following. Each is judged as a property of what the
> text says, never as particular wording.
>
> 1. That adoption is a mode of starting an effort rather than a kind of node, and that the manager performs it
>    before the graph exists.
> 2. That the manager's own act is bounded and ends by minting the bulk import as the graph's first nodes, whose kind
>    is `precondition` — rather than the manager writing the imported node files itself.
> 3. The steps of the manager's own act, in order: taking the effort's name from the directory that already exists;
>    resolving any of the reserved graph names (`map.md`, `map-history.md`, `decisions.md`, `flags.md`, `nodes/`)
>    that the directory is already using for something else; writing `map.md` with its destination, its notes, the
>    effort's ground rules and its standing over sources copied from what the effort already wrote rather than
>    invented; declaring the label vocabulary from the foreign label families; appending the expedition section to
>    the target repository's tracker doc where it has one; creating the remaining graph files empty; and minting the
>    import nodes.
> 4. The rule for a reserved name already in use: the existing file's content moves verbatim into the node files that
>    now hold it, and the reserved name is then rewritten to its expedition meaning. Nothing is summarised, shortened
>    or discarded on the way.
> 5. That the import transcribes the foreign corpus as it stands and reconciles nothing, and that a question the
>    foreign record has already answered is imported as an ordinary node and resolved afterwards by ordinary graph
>    work.
> 6. That the bulk import runs in two passes — one minting every node file, splittable and parallel; a second wiring
>    the blocking edges from the foreign prose, which is single because inverting an edge needs the whole
>    foreign-label-to-number mapping at once.
> 7. That a foreign identifier survives in the node's free-form filename and never as a field, and that foreign prose
>    moved into a node keeps its own words while newly written prose does not adopt them.
> 8. The rule for which foreign files import as nodes and which are linked from the map: a file holding questions or
>    decisions imports, a file holding research output is linked, and a file that is genuinely either gets a node of
>    its own rather than being decided by the import.
> 9. That a foreign status maps onto an expedition status, and that where the foreign record already names one thing
>    as superseding another, both directions of the supersession edge are written so the pair is complete.
> 10. That adoption changes nothing about the target repository's git history, and that no existing commit is
>     attributed to an imported node.
> 11. That citations inside imported material are repointed by a lookup table the manager builds once before the
>     import and the import applies mechanically, and that building the table is part of the manager's own act.
>
> The file is instructions and not an account: it narrates no particular effort's adoption, and it contains no
> passage that only makes sense to a reader who already knows the `Lang` repository.
>
> Nothing outside `.claude/skills/expedition/` changes. Within it, only the new file, plus optionally a pointer to it
> added to `SKILL.md` and to the closing section of `wayfinder-divergences.md`. No file under `.scratch/` changes.
>
> The work leaves the tree meeting the bar.

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Clause 3.** It says "the effort's ground rules and its standing over sources copied from …". Replace "its standing over sources" with "its declaration of which sources are authoritative, which are evidence only, and which hold statements known to be false".

## Flags

`97.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.
