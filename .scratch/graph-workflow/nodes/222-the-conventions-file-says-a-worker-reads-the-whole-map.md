# `graph-conventions.md` says every worker reads the whole map, and contradicts its own file table

Type: implementation
Status: open

Blocked by: 215

## Question

*Raised by [node 215](215-the-managers-contract-defines-the-map-as-one-file.md)'s checker alongside its outcome,
and pasted as it wrote it. It wrote no acceptance condition and none is invented here.*

> The condition's clauses 1 to 4 are right for the file they name and leave the shipped file beside it saying the
> opposite, and clause 8 forbids the worker from touching it. `.claude/skills/expedition/graph-conventions.md`,
> under `## Writing the map`, states: "every worker reads the whole map cold, so an item's size is paid once per
> node". That sentence says exactly what clause 4 forbids the manager contract to say, and it contradicts that same
> file's own table entry for `map-manager-only.md` — "The part of the map only the manager acts on. No worker reads
> it." — so the inconsistency predates this work rather than being made by it. Its neighbour two paragraphs
> earlier, "Every worker reads `map.md` whole and cold", is consistent with the amended glossary and needs nothing.
> This is not a departure the worker made and not a defect in the wording the condition dictates; it is a second
> shipped file the same correction has not reached, and it needs a node rather than a correction round here.

## Acceptance condition

**None. Its author is a checker, which mints no node and wrote no condition, and the manager did not write one.**
The condition is owed by whoever the human sends at it, or by them.

## The manager's note at filing

*Not a change to anything above.*

**The edge to node 215 is real and not bookkeeping.** Node 215's own work is what makes this sentence read as a
contradiction rather than as one of two consistent statements, and node 215's outcome is unsettled — its checker
returned `FAIL` on a judgement its worker had flagged the other way, and the human is the referee. **What this node
must say depends on which reading survives that.**

**The distinction its author drew is the useful part.** Two sentences two paragraphs apart in the same file: *"Every
worker reads `map.md` whole and cold"* is correct and needs nothing, while *"every worker reads the whole map
cold"* is the false one. **The difference is one filename**, and it is exactly the difference node 215's entry now
draws between the map and a part of it.
