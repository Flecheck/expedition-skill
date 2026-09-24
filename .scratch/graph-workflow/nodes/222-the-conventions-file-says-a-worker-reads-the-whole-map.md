# `graph-conventions.md` says every worker reads the whole map, and contradicts its own file table

Type: implementation
Status: superseded

Blocked by: 215
Superseded by: 299

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

## Annotation: a second stale statement in the same section, from node 224's checker

*Filed by the manager from [node 224](224-the-glossary-says-the-map-is-read-once-per-session.md)'s checker, in its
own words. Nothing above is changed, and **this node's condition is not amended.** Node 224 has passed its check and
is at its gate; this arrived as that checker's question and lands here because this node already holds
`graph-conventions.md`'s account of how the map is read.*

> A file beside the one the condition names still carries the wording the condition removed, and the worker could
> not touch it: `.claude/skills/expedition/graph-conventions.md`, under `## The seven files`, describes `map.md` as
> *"The whole effort at low resolution. Read once per session."* — the glossary's superseded phrasing, in a shipped
> standard whose own opening says *"Terms are used exactly as the glossary (`CONTEXT.md`) defines them."* It is not
> false of `map.md`, but the two documents now differ in vocabulary for the same read (`per session` there, `per
> node` in the revised entry and in the implementation-rules file's *"read whole, cold, once per node by every
> worker"*), and `session` is a word `CONTEXT.md` refuses on both its **Effort** and **Attempt** entries. Condition
> 8 confined the work to `CONTEXT.md`, so this was the condition's own scope and not the worker's to depart from;
> whether the shipped conventions document should follow is for the human.

**So this node now has two statements in one section rather than one**: the whole-map read its own question names,
and *"Read once per session"* on the `map.md` line. Both are in `## The seven files`, and the second is refused
vocabulary rather than merely imprecise. **Whoever claims this node should establish whether its condition reaches
the second**; the manager has not widened it.

## Superseded, 2026-09-24

*The manager's note.* Made unnecessary by [node 299](299-rewrite-graph-conventions-part-1.md)'s landing as `0d406b7`: the rewrite cut the sentence this node's question is about, "every worker reads the whole map cold, so an item's size is paid once per node", as an explanation. What stays is "Every worker reads all of `map.md` once per node", which this node itself says needs nothing. Proposed by node 299's worker (its flag `299.5`), which the human approved with the node.
