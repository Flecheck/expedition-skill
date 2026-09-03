# What can actually stop a running worker

Type: research
Status: claimed

Blocked by: none

## Question

*Surfaced by [Whether a dead attempt is resumed from its transcript rather than
replaced](119-dead-attempt-respawned-rather-than-resumed.md)'s worker, and pasted as it wrote it.*

> The manager may need to abandon a running worker — a node the human has redirected, a worker gone off-contract, a
> runaway loop, or a replacement made redundant by resuming the dead attempt instead. A message is not an interrupt:
> it is queued for delivery at the worker's next tool round, measured at 120 rounds in one case. `TaskStop` refused
> on ownership grounds when attempted from the spawning agent, but was never tried from a manager thread. Establish
> what the manager can and cannot stop, and at what latency; surface a grilling node if what it finds changes what
> the manager may promise the human.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The untested case is the manager's own thread**, so this node's central fact can only be established by the manager
attempting a stop or by a worker that the manager stops on request. A worker on this node cannot produce the case
from inside itself, which is the same wall node 119's worker hit on whether a human-stopped agent can be resumed.
How that is arranged is left to whoever spawns it.
