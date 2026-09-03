# What the two-respawn cap becomes now its reason is falsified

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [Whether a dead attempt is resumed from its transcript rather than
replaced](119-dead-attempt-respawned-rather-than-resumed.md)'s worker, and pasted as it wrote it.*

> Node 08 capped respawns at two because *"replay re-inflates exactly the context that killed the previous
> attempt."* No death on this effort was caused by an agent's own context — all of them died on a shared session or
> weekly usage quota — and replay is no longer the primary recovery. Does the cap survive, and on what ground? Does a
> resume count against it, given that it adds no attempt block? And what is the node-too-coarse signal now, given
> that a quota death says nothing about a node's size?

**Blockers, in the worker's words:** *"node 119 resolved."* Node 119 is resolved, so this node is unblocked at
filing.
