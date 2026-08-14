# Concurrency model

Type: grilling
Status: resolved

## Question

How many issue subagents are in flight at once, and what constrains that number?

## Answer

**Parallel, sized to saturate the human — with an exclusive lock on code modification.**

- Roughly **two HITL (grilling) subagents in flight at once**, so the human always has a question waiting and never idles.
- **Exactly one code-modifying subagent at a time.** This is what makes worktrees unnecessary in v1.
- AFK work (e.g. research) may fan out freely.

The governing principle, in the user's framing: **parallelism exists to saturate the human, not the machine.** The human is the scarce resource; concurrency is tuned to keep their question queue full, not to maximise machine throughput.

Later (not v1): subagents run in their own worktrees and, on finishing, land work on the manager's branch with `git merge --ff-only`.

Note on why that ordering is coherent: with a single writer, the manager's branch is always an ancestor of the subagent's, so the fast-forward cannot fail. `--ff-only` only becomes a real merge problem once the single-writer restriction is lifted — so the lock and the ff-only policy are two views of the same invariant.

Consequence to carry downstream: with two HITL subagents live, the manager is **multiplexing** a question channel. Attribution of questions to issues, and of answers back to the right subagent, is now a real problem — see [Relay protocol](08-relay-protocol.md).

Annotated by [Git and code-landing policy](11-git-and-code-landing.md), which changes the shape of the human's queue without changing either number here:

- **The code slot is no longer purely AFK.** An implementation node ends in a human gate — the manager raises the reviewed diff, the human approves or asks for corrections — so the slot's occupant is a **third claimant** on the human's attention alongside the ~2 interviews. The map's fog claimed the two budgets were disjoint; that claim is struck.
- **It is the only claimant that holds a lock while it waits.** An interview waiting on the human costs nothing but that interview; a gate waiting on the human blocks every other implementation node in the graph. This is the number the dogfood should watch, and it is the trigger for flipping landing to asynchronous.
- The `--ff-only` sequencing above gains a reason rather than a habit: **a per-node branch isolates work from nothing while there is a single writer**, so branches arrive exactly with the worktrees in this answer's later phase and not before. Until then the workflow creates no branches at all.

## Annotation: the write lock is called the code slot

Added by [Naming](14-naming.md).

- **`write lock` is refused as a name.** [Git and code-landing policy](11-git-and-code-landing.md) made occupancy a property *discovered* from the working tree, so no lock object exists anywhere in the design — a name promising one would send an agent looking for a file that is not there. The term is **code slot**, which this node's own prose had already drifted towards.
- The HITL budget's occupants are **workers** on **grilling**, **prototype** and HITL **precondition** nodes — `task` having been renamed. Nothing about the budget itself changes.
