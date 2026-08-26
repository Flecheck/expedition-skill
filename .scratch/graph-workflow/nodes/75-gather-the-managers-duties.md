# Gather the manager's accumulated duties into one enumerated list

Type: precondition
Status: open

## Question

**The manager is the only actor in this workflow with no contract.** `.claude/skills/` holds six worker contracts
and `expedition/graph-conventions.md`; nothing describes what the manager does. Its duties have accumulated across
the effort as consequences of other nodes' answers, and they sit **on those nodes** rather than anywhere a manager
could read them.

### The human's instruction, `verbatim`

> *"I think the priority should be writing the first version of the manager skill as now you don't have any way to
> know what to follow as the information is split everywhere."*

### Measured, so the size is not guessed

**20 node files name a duty of the manager's.** The fog paragraph that tracked them, now in `map-history.md`, ran to
**17,497 characters** before it was compressed to a pointer. The requirements were deliberately left on their
producing nodes under this effort's own rule that an item cites rather than restates — **which is right for the map
and is exactly what makes the skill unwritable without this node.**

## Why this is its own node, and the alternative that was rejected

**The obvious move is one implementation node that writes the skill.** It fails on [An acceptance condition is
self-contained text](33-condition-is-self-contained.md): a condition saying *"state the duties the graph has
accumulated"* points at material the blind checker will not be given, and a condition that **enumerates** them can
only be written by someone who has first gathered them. So the gathering happens either way; the only question is
whether it happens inside a condition the manager writes, or as work with its own output.

**It is put here for three reasons.** The manager writing it would spend the effort's scarcest resource — [Friction
from running this map by hand](24-self-hosted-friction.md) found the manager's context is what has failed every
session, and this session's own gathering would be ~20 node files. [A worker's handover carries no acceptance
condition for the node it mints](35-handover-mints-no-condition.md) **measured** that every condition written by a
spawning node's worker passes the self-containment rule while nine of thirty-one others fail. And the manager is the
one party that cannot check its own account of its duties, having formed those duties by doing them.

**Its type is `precondition` rather than `research`**: nothing here is decided and nothing outside this repository is
consulted. It is work that must happen before the skill can be specified.

## Acceptance condition

*Written by the manager, which minted this node, under [A worker's handover carries no acceptance condition for the
node it mints](35-handover-mints-no-condition.md)'s permission and marked as the manager's own.*

The work is `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/`. Done means all of the following.

1. This node's `## Answer` holds **one enumerated list of every duty, rule and constraint the manager is under**,
   each item stating the duty in its own words and citing by markdown link the node that produced it. A duty that
   several nodes shaped carries several links.
2. The list is derived by reading the node files rather than the map: **every `resolved` node is opened**, and the
   answer states how many were read and how many produced a manager duty. Where a node was opened and produced
   none, it is not listed.
3. The list separates, under headings of the author's choosing, at least: what the manager **writes** and where;
   what it **may not** write or author; what travels in a **spawn**; what it does with a **handover**; what it does
   at a **gate**; what it does with a **flag**; how it **reports to the human**; and what it does when an agent
   **dies, stops or returns something it cannot file**.
4. Where two nodes' duties **conflict or overlap**, the answer says so and does not resolve it. Resolving one would
   be a decision, which this node's type does not permit.
5. The answer names every duty the manager is currently observing **that no node ever settled** — practice the
   manager adopted on its own authority — separately from the settled ones, so the human can see what has never been
   ruled on.
6. This node's `## Answer` ends with an **acceptance condition for the node that writes the skill**, written as
   self-contained text under node 33's rule: it demands only what the condition itself states, and a blind checker
   given that condition and the bar can establish every clause without being handed the graph.
7. No file outside `.scratch/graph-workflow/` is modified, and no shipped skill file is written by this node.
8. The bar.

### Audit at claim time, by the manager

*To be filled at claim.* **Two risks are already visible and named here so the audit meets them rather than finds
them.** Clause 2 quantifies over the record, which [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md) treats carefully — it is permitted here because
it demands an **action over the record** and reports a count, rather than asserting a property of it that a checker
must verify. And clause 5 asks a worker to identify practice **the manager invented**, which the manager is the
worst-placed party to have specified; if the worker cannot separate the two classes, that is a flag rather than a
guess.
