# Off-contract subagent output

Type: grilling
Status: open
Blocked by: 12

## Question

What happens when a subagent is alive but returns garbage — output that does not satisfy its return contract?

Split out from the map's *Failure handling* fog by [Relay protocol](08-relay-protocol.md), which answered the other half: a subagent that **dies** mid-question. The two are genuinely different failures and share no remedy.

- A dead subagent leaves nothing to salvage, so the answer is replay into a fresh agent.
- An off-contract subagent is **alive and resumable**, so the remedy is rejection and a re-prompt against the contract — no respawn, no replay, and the node's claim never in question.

Open:

- What counts as off-contract? A missing required field is mechanical; a well-shaped answer that is merely **thin** is a judgement call, and the manager is the only one positioned to make it.
- How many re-prompts before the manager gives up, and what does giving up mean — respawn, escalate as a node-too-coarse decision (the route [Relay protocol](08-relay-protocol.md) took for repeated death), or hand it to the human?
- Does a rejected return get **recorded** on the node? [Revision semantics](06-revision-semantics.md) says nothing is deleted, but a log of rejected garbage may be noise rather than history.
- Does the same rule cover an **implementation** subagent whose code fails its acceptance condition? [Node type taxonomy](07-node-type-taxonomy.md) already routes that through the independent reviewer, so these may be one mechanism or two.
- The dangerous case: output that satisfies the contract's *shape* while inventing content — a subagent that answers its own HITL question and formats it as though the human had. Nothing currently detects this, and it is the exact failure [Relay protocol](08-relay-protocol.md) exists to prevent.

Blocked on [Subagent context contract](12-subagent-context-contract.md), because "garbage" is only definable against a fixed return shape.
