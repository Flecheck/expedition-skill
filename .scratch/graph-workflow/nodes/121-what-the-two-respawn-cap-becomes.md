# What the two-respawn cap becomes now its reason is falsified

Type: grilling
Status: superseded
Superseded by: 119

Blocked by: none

## Question

*Superseded 2026-09-29: this question no longer needs doing here. See `## Superseded, 2026-09-29` below.*

*Surfaced by [Whether a dead attempt is resumed from its transcript rather than
replaced](119-dead-attempt-respawned-rather-than-resumed.md)'s worker, and pasted as it wrote it.*

> Node 08 capped respawns at two because *"replay re-inflates exactly the context that killed the previous
> attempt."* No death on this effort was caused by an agent's own context — all of them died on a shared session or
> weekly usage quota — and replay is no longer the primary recovery. Does the cap survive, and on what ground? Does a
> resume count against it, given that it adds no attempt block? And what is the node-too-coarse signal now, given
> that a quota death says nothing about a node's size?

**Blockers, in the worker's words:** *"node 119 resolved."* Node 119 is resolved, so this node is unblocked at
filing.

## Superseded, 2026-09-29

*The manager's note:* superseded by [node 119](119-dead-attempt-respawned-rather-than-resumed.md), under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q1 (`verbatim`: *"ok"*, recorded on node 366). Node 366's worker's reason: no respawn cap exists any more, and a dead attempt is resumed wherever it can be (node 119).
