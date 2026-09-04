# How much of the integration-conflict rule reaches the shipped files

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [Two writers edit the map at once](115-two-writers-edit-the-map-at-once.md)'s worker, and pasted as it
wrote it.*

> Node 115 settled that integration conflicts are resolved rather than prevented, and produced two rules whose scope
> the human's words leave open. The first is the pick heuristic — *"favor paralellization on nodes that have little
> chance of conflicting with one another"* — which node 115's worker scoped to this effort's map, because only the
> other half of that sentence says *"the framework should"*. The second is the resolver split: the manager unions
> never-delete prose, the branch's worker resolves code, and a contradiction aborts. Neither is in any shipped file
> today, and the shipped implementation contract already tells a worker that *"another implementation worker may be
> running alongside you"* without saying what happens when the two pieces of work meet. Does either reach the shipped
> files, and if the resolver does, does the implementation contract's definition of a correction round widen to cover
> a round the integration triggers rather than the human?

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**Its subject is flag `115.2`**, which is that worker's own record of having read one sentence of the human's as
scoping only its second half. This node exists so the reading is settled rather than left standing on a flag.
