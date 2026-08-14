# When an AFK worker cannot proceed

Type: grilling
Status: open

## Question

How does an AFK worker — an implementer or a checker — tell the human that the node's premise is broken,
and what happens to the node while it waits?

Raised by the human as steering, verbatim: *"One think that would be good is if the implementor or the
checker can also raise when the plan can not be followed, some asumption was wrong or if the
implementation is more complex than expected, some important suposition is wrong, ... They shouldn't be
able to close the node by themself but can raise the issue to the user."*

**The second sentence is already guaranteed and needs nothing.** A worker writes no graph file
([Subagent context contract](12-subagent-context-contract.md)), the manager is the graph's only writer,
and resolving is the manager's act on a handover. No worker can end its own node today.

### Four named cases, three existing destinations

The human's list is not one thing. Each case already has somewhere to land; what none of them has is a
way to *get there from inside a running worker*.

| what the worker hit | where the graph already sends it |
| --- | --- |
| the plan cannot be followed | the node's own premise is wrong — supersession, or the early form of [Human review of landed code](20-human-code-review.md)'s `reject` |
| an assumption was wrong | an **upstream decision** is wrong — a revision, and a cascade ([Revision semantics](06-revision-semantics.md)) |
| an important supposition was wrong | same, and whether it is distinct from the previous row is this node's to decide |
| more complex than expected | the node is too coarse — the escalation [Node type taxonomy](07-node-type-taxonomy.md) already owns |

What unifies them is not the remedy but the worker's position: **it cannot act on any of them, and it
cannot honestly continue without an answer.** That is the property a single channel is for, and it is why
this is one node rather than three.

### Most of the mechanism exists; what is missing is permission and a threshold

[Relay protocol](08-relay-protocol.md) built the channel and [Subagent context
contract](12-subagent-context-contract.md) fixed its payload: the **question** variant, carrying the
node, `ABOUT`, `SO FAR`, `ASK`, `RECOMMENDED` and `ALTERNATIVES`, with the human's answer returning
verbatim, the four redirects supported, lazy death detection, and **park** as an outlet. That node then
closed it off in three words — *"HITL types only"*. Lifting that clause is most of what the human asked
for.

So the open work is not the channel. It is:

- **The threshold.** [Node type taxonomy](07-node-type-taxonomy.md) fixed that implementation *"never
  asks live: small ambiguities are decided and flagged, genuine forks become grilling nodes."* The flag
  and the new node are both **deferrals** — a flag costs nothing until the effort closes, and a new node
  joins the frontier. Neither reaches the human now. This node has to say where the line falls, and the
  failure mode is not caution but noise: a worker that raises on every mild surprise destroys the AFK
  property the taxonomy exists to protect, and floods the queue of the resource the whole map calls
  scarce. The cheap instrument is probably the same one the relay already uses — the worker must state
  `RECOMMENDED`, so a raise it can answer itself is a flag by construction.
- **The code slot.** An implementation worker holds the **exclusive** code slot. If it can now block on
  the human mid-node, the slot has a *second* way to sit idle waiting on attention — and [Git and
  code-landing policy](11-git-and-code-landing.md) already named the gate as *"the only claimant that
  holds a lock while it waits"*, which would stop being true. Park exists and returns a node to `open`
  with its answers banked, which frees the slot; whether an implementer that parks discards its
  half-written code, or leaves it and blocks everything, is the sharpest question here.
- **The checker has no variant at all.** [Subagent context
  contract](12-subagent-context-contract.md) gives it exactly `PASS` or `FAIL`, and nothing else. Yet it
  is the **only** party that ever reads an acceptance condition cold, with none of the reasoning behind
  it — so it is uniquely placed to notice a condition that is incoherent, unmeasurable, or contradicts
  itself, and it currently has no way to say so. Adding a third return is a genuine addition to that
  node's answer, recorded there as an annotation once decided.
- **What the human's answer is allowed to do.** *"Carry on, the assumption is fine"* is cheap. But the
  interesting answers reach further than the node: rewriting an acceptance condition that a **spawning
  node** wrote and its worker may not touch; revising an upstream resolved node, which spends a
  supersession and a cascade; splitting the node; or killing it, which is `reject` before there is a diff
  to reject. Which of those the human can do from inside a raise, versus which drop the worker and become
  ordinary graph work, is undecided.
- **Where it is recorded.** `## Interview` holds relayed questions and `## Review` holds everything after
  the code lands. A raise from a mid-flight implementer is neither, or both.

### Evidence already on the record

- **The checker case has happened.** [Write the graph conventions
  document](21-conventions-document.md)'s checker found *"two ambiguities, both real"* in the shipped
  document and reported them — but only because that run was improvised under a hand-written four-phase
  protocol that invited it. Under the contract as it stands it would have had `PASS` or `FAIL` and no
  words.
- **The implementer case has happened too, and took the deferral.** That same node raised
  `CONDITION-WRONG` against acceptance condition 4 — the condition was **false**, not merely awkward —
  and shipped anyway with a flag, because a flag was the only outlet it had. Whether that was the right
  outcome is a good test of whatever threshold this node writes: it plausibly was, which means the
  answer is not simply *raise more*.
- **The gate's `reject` is this same discovery arriving later.** [Human review of landed
  code](20-human-code-review.md) fixed it as *the act of implementing surfaced something meaning the code
  should not exist*. A worker that spots that at hour one instead of at the gate saves the whole
  implementation — so this node is, in part, about moving a known outcome earlier, and the two must not
  end up with different names for the same finding.

### What this node must not quietly change

- **The worker still never resolves, and never decides.** The human's own constraint.
- **Implementation is still AFK.** If the answer makes an implementer routinely interactive, it has
  superseded [Node type taxonomy](07-node-type-taxonomy.md) rather than qualified it, and should say so
  in those terms rather than by drift.
- **The manager still answers nothing on the human's behalf.** A raise it can absorb from context it
  already holds is a **manager note** on a question, not an answer to it.

### Consequences already known

- **[Write the worker contract skills](22-worker-contract-skills.md) is blocked on this.** The
  implementation and checker contracts must both state every return variant their worker may use
  (condition 2) and may introduce no rule no node decided (condition 3), so those two of the six cannot
  be written until this resolves. It costs a second commit against a resolved node otherwise, which the
  landing policy forbids.
- Related, and deliberately distinct: [Human-initiated steering](16-human-steering.md) is the same
  channel in the opposite direction, and [Off-contract subagent output](17-off-contract-output.md) is
  about a worker that fails its contract rather than one correctly using a channel that does not exist
  yet.
