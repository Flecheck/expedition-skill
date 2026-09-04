# `graph-conventions.md`'s rules for the map now resolve to more than one `## Notes`

Type: implementation
Status: open

Blocked by: none — [node 139](139-move-the-managers-material-out-of-the-map.md) landed as `4e38c11`

## Question

*Surfaced by [Where the rules a checker is held to live](138-where-the-rules-a-checker-is-held-to-live.md)'s worker,
and pasted as it wrote it. Found independently and first by [node
139](139-move-the-managers-material-out-of-the-map.md)'s checker.*

> `map-manager-only.md` declares itself part of the map and carries its own `## Notes` at line 7, so the 500-byte
> target and the mechanical check that reports a breach of it, both written against *the map's `## Notes`*, now name
> two sections. Found by node 139's checker; the staleness it also found about that file naming five map sections is
> reported as already owned elsewhere.

## Acceptance condition

*Written by node 138's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`. Done means: every
> rule in that file written against *the map's `## Notes`* states which file's `## Notes` it governs, given that the
> effort's map is more than one file and more than one of them carries a section by that name; in particular the
> 500-byte size target for a map item and the numbered mechanical check that reports a breach of it each name the
> file they apply to. Nothing else in the file changes, and no file outside it is modified. The working tree meets
> the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is a defect in text [node 139](139-move-the-managers-material-out-of-the-map.md) itself shipped**, rather than
one it left alone — its clauses 9 and 10 mandated the wording *"the map's `## Notes`"* while its clause 2 created a
second file that declares itself part of the map. **Its checker and node 138's worker found it independently and
blind to each other.**

**It is distinct from [node 142](142-bring-graph-conventions-map-shape-into-line.md)**, which owns the same file's
stale section list and two procedure steps, and which waits on node 140. This one waits on nothing. **The manager has
not merged them** and records that they touch one file and would serialise on the code slot anyway.
