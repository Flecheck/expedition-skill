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

### The same defect on a second handover part: `FLAGS` names one artifact where the graph needs two

Added in place by [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md) at its gate, this node being open and
unstarted. It is the **same shape** as the node's own subject — a handover part naming one artifact where
the graph needs two — so it belongs here rather than in a node of its own.

All five contracts write:

```
FLAGS:         <one line each, prefixed ASSUMPTION>
```

But a flag lands in **two** places under **two different caps**, fixed by
[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s `### Raise a flag`
procedure: free prose under the node's `## Flags`, and one capped sentence in [flags.md](../flags.md).
*"One line each"* names neither, and nothing in any contract says which of the two a worker is writing.

**What happens in practice, twice measured.** The worker writes the prose — the more useful half — and the
manager condenses each flag into its index line, authoring text that is neither the worker's nor the
human's. That is the scribe rule broken by omission rather than by choice: the manager is not re-authoring
what it was given, it is writing what it was not given at all.

- Flag `33.4` recorded it at [An acceptance condition is self-contained
  text](33-condition-is-self-contained.md), where the manager authored all four index lines. Settled at
  that node's gate, and **settled is not fixed**.
- It recurred immediately at [The clause that says no resolved node changes cannot be
  self-contained](36-resolved-node-clause-cannot-be-self-contained.md) — two flags, two index lines, both
  the manager's. No flag was filed the second time: a duplicate of a settled flag is noise, and what the
  recurrence establishes is that **nothing owned the fix**, which is what this annotation changes.

Whoever takes this node decides both parts together or says why they differ. One thing not to assume: the
answer may be that a worker writes only the prose and the *capped line is the manager's by design* — in
which case the contracts should say so, and `graph-conventions.md`'s *"written report-shaped at raise time
by whoever holds the context"* is the clause to hold that answer against.

### The acceptance condition is owed

Written by whoever spawns this, and it may not be claimed without one — which is this node's own subject
arriving in its own paperwork.

**Sequencing, not a blocker.** It touches the five `expedition-<type>/SKILL.md` files, which are also the
live territory of [Checking a flag before the human sees it](30-checking-a-flag-before-the-human.md) and [Narrow the
flags.md clause in the worker contracts](32-narrow-flags-file-clause.md). The landing policy forbids a second
commit against one **node**, not against one **file**, so these may run in any order — but not concurrently,
the code slot being exclusive.
