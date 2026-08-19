# A worker's handover carries no acceptance condition for the node it mints

Type: implementation
Status: open

## Question

All five worker contracts write the same handover part:

```
NEW NODES:     <name, kind, question, blockers — one block each>
```

Nothing there is an **acceptance condition**. Yet [Node type taxonomy](07-node-type-taxonomy.md) and
`CONTEXT.md` both fix that a condition is written by the node that spawned it, **before any work starts**,
and [`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s `### Claim` procedure
forbids claiming an implementation node without one:

> An `implementation` node may not be claimed until it has an `## Acceptance condition`.

So a worker that surfaces an implementation node returns no condition, and the manager writes one later.

### This is why three conditions in a row were manager-written

- [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md)'s — and
  [What the checker contract owes to having been run](31-checker-contract-owes.md) records that it **had to
  be amended twice**, once for naming a glossary entry that does not exist, once for a clause true only of
  implementation nodes.
- That same node's own condition 6, added by [Whether a spawn may override a shipped worker
  contract](28-spawn-overriding-a-contract.md), marked `Manager-written` in place with the warning attached.
- [An acceptance condition is self-contained text](33-condition-is-self-contained.md)'s, whose condition 6
  then **failed the very rule that node shipped** — it named four node files inside the record and put its
  deliverable in the node's `## Answer`, which a checker is never given. The blind checker declined to
  establish it rather than passing or failing it.

Three instances, one cause, and the warning has been carried forward by hand each time instead of fixed.

**The rule node 33 shipped binds whoever writes a condition. The handover gives them nowhere to write one.**

### What the fix probably is, and what it must not assume

A sixth element on the `NEW NODES` block, required for an implementation node and absent for every other
kind — plus the self-containment rule stated where the writer will actually read it, which is the worker
contract rather than `graph-conventions.md`.

One thing to decide rather than assume: a worker mints a node **at the end of its own work**, having never
read the node it is minting for. Whether it is in a position to write a condition at all, or whether the
honest answer is that the manager raises it to the human, is this node's to settle — and *"the manager writes
it"* is the option already known to cost two amendments.

Reported by [An acceptance condition is self-contained text](33-condition-is-self-contained.md)'s worker.

### The acceptance condition is owed

Written by whoever spawns this, and it may not be claimed without one — which is this node's own subject
arriving in its own paperwork.

**Sequencing, not a blocker.** It touches the five `expedition-<type>/SKILL.md` files, which are also the
live territory of [Checking a flag before the human sees it](30-checking-a-flag-before-the-human.md) and [Narrow the
flags.md clause in the worker contracts](32-narrow-flags-file-clause.md). The landing policy forbids a second
commit against one **node**, not against one **file**, so these may run in any order — but not concurrently,
the code slot being exclusive.
