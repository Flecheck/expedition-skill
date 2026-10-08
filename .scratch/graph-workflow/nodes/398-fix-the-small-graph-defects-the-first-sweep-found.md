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
