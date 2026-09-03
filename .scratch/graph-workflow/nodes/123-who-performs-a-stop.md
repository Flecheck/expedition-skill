# Who performs a stop, and what the human's own stop destroys

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [What can actually stop a running worker](122-what-can-stop-a-running-worker.md)'s worker, and pasted as
it wrote it.*

> Two stops exist and they differ in one consequence. A stop the manager issues with `TaskStop` leaves the agent
> resumable from its transcript. A stop the human issues from the task UI sets a persisted `stoppedByUser` flag that
> refuses every agent-initiated resume for ever, so for that agent the map's standing rule — *"Whenever it can be
> resumed, resume I think"* — is dead, and only the human typing to the agent can revive it. Two agents on this
> project are already in that state, one of them a checker holding 65 records and 483,376 bytes of work, and nothing
> in the graph records either as human-stopped. So: when a worker must be abandoned, who should perform the stop?
> Should the human's own stop be reserved for work that is genuinely to be discarded, with a redirection or a runaway
> routed to the manager instead? Does the manager owe the human a line, at the moment it reports a worker as running,
> saying which of the two they are choosing between? And is there a case where the human wants a worker gone
> permanently and unrevivably, which is the one thing the manager's stop cannot give them?

**Blockers, in the worker's words:** *"Node 122 resolved. **Sharper if the manager has run node 122's Test 1
first**, since the human's answer is worth less if the manager's stop turns out not to work at all."*

## The manager's note at filing

*Not a change to anything above.*

**Both of this node's preconditions are met.** Node 122 is resolved, and **the manager has run Test 1 and Test 2 and
both passed** — the manager's stop works and leaves the agent resumable, recorded on node 122 under `## The manager
ran Tests 1 and 2, and both pass`. So the worker's *"worth less"* case does not arise: the two stops really do
differ in exactly the consequence this node asks about.
