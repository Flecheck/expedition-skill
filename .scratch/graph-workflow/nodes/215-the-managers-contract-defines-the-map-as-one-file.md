# The manager's contract defines the map as one file, where the workflow ships four map files

Type: implementation
Status: open

Blocked by: 204

## Question

*Surfaced by [Demote the recorded bar commands to a copy confirmed against the
repo](204-demote-the-recorded-bar-commands-to-a-copy.md)'s worker, and pasted as it wrote it.*

> `.claude/skills/expedition/SKILL.md`'s glossary entry for **map** says the map is "the
>            effort's whole shape at low resolution, in the one file every worker reads cold once per
>            node", equating the map with a single file. The rest of the shipped set does not:
>            `graph-conventions.md`, beside it, lists `map.md`, `map-history.md`, `map-manager-only.md`
>            and `map-implementation-rules.md` as an effort's map files; the implementation contract
>            calls the rules file "the sibling of the effort's map"; the checker's contract names its
>            path; and `CONTEXT.md`, the glossary this effort declares authoritative, defines Map with
>            no filename and no one-file claim at all. So the manager's contract is the single outlier,
>            the same shape node 174 found for the implementer's contract. This node's own work
>            sharpened it: the entry now also says the map "holds a record of the bar's commands", and
>            on this effort that record sits in a sibling rather than in the file a worker reads cold.

**Blockers, in the worker's words:** node 204, whose work puts the wording clause 2 below requires kept into that entry.

## Acceptance condition

*Written by node 204's worker. Pasted as it wrote it, and not the manager's.*

> The work is one file, relative to the repository root: `.claude/skills/expedition/SKILL.md`. The worker may edit that one and no other, and may not write any file under `.scratch/`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. That file's glossary entry for **map** no longer states that the effort's map is one file, and no longer states or implies that everything the map holds sits in the one file a worker reads cold once per node. Where the entry says what a worker reads cold once per node, it says that file is a part of the map rather than the whole of it.
> 2. That entry keeps its statement of what the map is — the effort's whole shape at low resolution, holding the destination, the standing preferences, the fog as in-scope work that can be told is coming but cannot yet be phrased as a question, and what is ruled out of scope — and keeps all four of its remaining statements: that the map indexes decisions and never restates one; that the manager owns it; that two things live there and nowhere else, those being the effort's ground rules and the standing steering the human has given; and that it holds a record of the bar's commands once discovered for this repo, which an agent confirms against the repo before using.
> 3. The entry names no particular filename. Where it says where the map's material sits, it says so by role and position only.
> 4. No sentence anywhere in the finished file states or implies that a worker reads the whole of the map, or that the map is a single file.
> 5. Any sentence in the finished file that introduces a list by stating how many items it holds states a count arithmetically correct for the items that list then holds.
> 6. No text outside the passages clauses 1 to 5 reach is deleted or reworded.
> 7. The finished file names no plugin, requires no skill to be invocable, and assumes no particular repository, machine or toolchain.
> 8. No file other than the one named above is modified, and no file under `.scratch/` is modified.
> 9. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its blocking edge is already satisfied.** Node 204 landed with the wording its clause 2 requires kept, so this
node is takeable now.

**It is the same shape as its own parent, one file over.** Node 174 found the implementer's contract to be the
outlier on where the bar's commands live; this is the manager's contract as the outlier on what the map is. **Its
author's own work sharpened the defect it reports** — node 204 added *"holds a record of the bar's commands"* to
that entry, and on this effort that record sits in a sibling rather than in the file a worker reads cold.

**Its clause 5 carries the arithmetic audit forward**, which on node 204 meant enumerating 49 counted lists across
two files to satisfy one clause. **Nothing indexes counted lists** — the item node 204's retrospective reports for
the fourth time.
