# Subagent context contract

Type: grilling
Status: open
Blocked by: 07, 08

## Question

Exactly what does an issue subagent receive when spawned, and what must it return?

A subagent starts with fresh context and cannot see the manager's conversation, so everything it needs must be handed to it deliberately. Both halves of the contract are open.

Inbound:

- The node's own question, obviously. What else — the whole graph, or just its ancestors' answers?
- How are ancestor answers passed: inlined, or as file pointers it reads on demand? (Wayfinder's "zoom as needed" pattern suggests pointers.)
- Does it get the destination and the standing notes for the effort?
- Which skills is it told to invoke — `/grilling`, `/domain-modeling`, `/naming`, `/prototype`?
- For implementation nodes: what code orientation, and what acceptance condition?

Outbound:

- The answer, in what shape? Free prose, or something structured enough for the manager to act on without re-reading?
- Whether it surfaced new nodes, and whether it invalidated an existing one — the manager cannot spot a needed revision if subagents do not report it.
- A pause-with-question, per [Relay protocol](08-relay-protocol.md), which is a different return shape from a finished answer. The contract has to cover both.

Settled by [Node type taxonomy](07-node-type-taxonomy.md), which confirms the contract does differ per type and fixes several entries:

- There are five types to write contracts for, and one extra worker that is not a type: the **independent reviewer**, which gets the node's acceptance condition and the landed code, and returns a pass or a rejection with reasons.
- An **implementation** subagent receives its acceptance condition, written by the spawning node, and may not rewrite it — but may flag it as wrong, which is part of its return shape.
- An implementation subagent **never pauses to ask**. Its outbound contract therefore needs two things a grilling contract does not: flagged assumptions it decided itself, and a request to create a grilling node when it met a genuine fork.
- **Prototype** is HITL and so does use the relay; its return links a throwaway artifact rather than reporting landed code.

**Now unblocked.** [Relay protocol](08-relay-protocol.md) was prototyped live and hands over a working first draft of both halves rather than an open question — see its [prototype asset](../prototypes/08-relay-protocol/run-1.md), which records the exact contract two real subagents were run under. What it settles:

- **Inbound context is file pointers, not inlined text.** Tested and confirmed: both subagents oriented themselves correctly from pointers to the map and the relevant resolved nodes. Wayfinder's zoom-as-needed pattern is the answer for this node.
- **The outbound question shape** — node name, the question verbatim, a recommendation, the alternatives — and the inbound answer shape, which carries the human's **verbatim** words, a **divergence** marker when the answer contradicts the subagent's recommendation, and manager notes kept separate from the human's words.
- **A third return variant: parked-with-progress.** A subagent told to stand down returns its progress as a dump, including the questions already answered and the human's words verbatim, which the manager writes onto the node. Subagents stay off the graph; the manager remains the single writer.
- **Delegated-answer marking**, for when the human said "you decide" and the subagent answered instead.
- A subagent must **report** its own new nodes and invalidations, because the manager cannot read a running subagent's transcript and so has no other way to learn of them.
- The run's `CONTEXT-PROOF` field was instrumentation and is **not** part of the shipped contract; what replaces it is a provenance marker on recorded answers.

What remains genuinely open for this node: whether a subagent gets the destination and standing notes (the run gave it the whole map, which worked but may be more than needed), which skills each type is told to invoke, and the contracts for the types the prototype did not exercise — research, task, implementation, and the independent reviewer.

Blocked on the taxonomy because the contract likely differs per node type, and on the relay because pausing is one of the things a subagent can return.
