# Done-ness and termination

Type: grilling
Status: open
Blocked by: 06, 07

## Question

How does the manager know the graph is exhausted and the code is in its final, correct state?

The stated goal is that when the workflow finishes, "the state of the code is perfect". That has to become something checkable.

- Must the repo be **green after every implementation node** — tests passing, builds clean — or may it be transiently broken mid-graph, with correctness only required at the end?
- Is there a **final verification pass**, or is done-ness the simple absence of open nodes?
- Since implementations are revisable, "no open nodes" is not obviously stable: resolving the last node can create new ones. What makes termination converge rather than oscillate? (Wayfinder's fog graduates monotonically toward the destination; a revision loop does not obviously do the same.)
- Who declares done — the manager, or the human?
- Is "perfect" measured against the destination, against the code's own quality standards, or both?
- **Does anything verify that the cascade did not miss a node?** [Revision semantics](06-revision-semantics.md) made the cascade's scope a matter of agent judgement, deliberately accepting that an agent can miss things. If nothing ever checks, "the state of the code is perfect" rests on every cascade having been right.

- **Does an unresolved flagged assumption block done-ness?** [Node type taxonomy](07-node-type-taxonomy.md) lets an implementer land code on its best judgement and flag the assumption for the human. Those flags accumulate, and if none of them blocks, the graph can be exhausted while the code rests on guesses nobody ever confirmed.

Added by [Node type taxonomy](07-node-type-taxonomy.md), narrowing this node's job: per-node verification is settled and is **not** this node's business. Every implementation node already carries a spawner-written acceptance condition and is checked by an independent reviewer before resolving. What remains here is whether anything checks *across* nodes — the final pass, the cascade's misses, and the flagged assumptions above.

- **Do parked nodes and delegated answers block done-ness?** [Relay protocol](08-relay-protocol.md) adds two more things that accumulate quietly. A **parked** node is back to `open` with banked human answers, so it counts as an open node and the frontier is not exhausted while any exists — but nothing yet says the human must ever return to it, and "ask me later" was explicitly a prioritization act rather than a promise. A **delegated** answer is recorded as a flag and explicitly does *not* gate done-ness, which is an input that node accepted on agent judgement; if that is wrong, this is where it gets overturned. Both join the flagged assumptions above as ways the graph can empty while resting on things the human never actually decided.

Added by [Revision semantics](06-revision-semantics.md): it supplies a partial answer to the oscillation question — the supersession chain makes churn visible, chains only lengthen through completed attempts, and a session revising an already-revised lineage escalates instead. What it does not settle is whether an exhausted frontier is a *stable* state, which is this node's business.

Blocked on revision semantics because whether termination can oscillate depends entirely on how revision is modelled, and on the taxonomy because a verification node type would change the shape of the answer.
