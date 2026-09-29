# A worker has no permitted way to bank its work when the manager orders a replay

Type: grilling
Status: superseded
Superseded by: 265

Blocked by: none

## Question

*Superseded 2026-09-29: this question no longer needs doing here. See `## Superseded, 2026-09-29` below.*

*Minted by the manager as the permanent fix its own contract requires after a licence. The question below is the
manager's own.*

A worker contract's hard rule 3 states that a worker **never commits, never branches, never rewrites history**. That
rule is right for the ordinary case: the manager owns the landing, and a worker that commits pre-empts the gate.

**It has no exception for the case that actually arose.** [Node
140](140-move-the-implementers-and-checkers-material-out-of-the-map.md)'s worker finished a verified piece of work in
a worktree cut from a stale base. The work could not rebase. The only ways forward were to **discard verified work**
or to **bank it in a commit first** — and banking it is forbidden by hard rule 3. The manager instructed the breach
rather than raising it, which is its own failure and is flagged at `140.8`; but the hole the breach stepped through is
real and outlives that failure.

**What this decides:** whether hard rule 3 gains an exception for work a worker is ordered to replay, what form
banking takes if so, and who may order it. Adjacent but not the same: whether the manager may ever instruct a
departure at all, which its contract already answers — it may not, it raises instead.

## The manager's note at filing

*Not a change to anything above.*

**This node exists because the manager's contract requires it.** Its rule is that a licence to depart from a contract
produces two things, always both: a flag on the node, and a node for the permanent fix. The flag is `140.8`. This is
the node. **The licence itself was never granted** — the manager acted without asking — so this node is filed late
and against a breach rather than against a licence.

## Superseded, 2026-09-29

*The manager's note:* superseded by [node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md), under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q1 (`verbatim`: *"ok"*, recorded on node 366). Node 366's worker's reason: under node 265's landing route the manager banks the work, so a worker never needs to commit.
