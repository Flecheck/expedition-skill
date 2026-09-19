# Three statements name a different "first act" for a worker

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 250](250-state-how-an-implementation-worker-reaches-its-worktree.md)'s worker, and pasted as it
wrote it. **Noticed first by that node's checker**, which met the collision while blind to the record and handed it
back as a question alongside its outcome.*

> `map-manager-only.md` now says "The worker's first act is to call `EnterWorktree`"; its fog item says "a worker's
> first act is to read its own node"; and the implementation spawn says the `EnterWorktree` call is the first act
> while the contract has the worker read its node and its contract first. Node 250's own worker read before it
> called, so it matched none of the three. What is each statement first relative to?

**Blockers, in the worker's words:** *"none. Must not hold `map-manager-only.md` while another worker holds it."*

## Acceptance condition

*Written by node 250's worker. Pasted as it wrote it, and not the manager's.*

> Done when no two statements in `.scratch/graph-workflow/map-manager-only.md` claim a worker's "first act" without
> saying what each is first relative to. There are two today: the binding rule under `How the worker reaches it`,
> *"The worker's first act is to call `EnterWorktree` with the worktree's absolute path"*, and the fog item under
> `## Not yet specified` headed *"What never-delete costs the reader of a node file"*, whose premise reads *"a
> worker's first act is to read its own node"*. Each states its scope — for instance the first being first before
> the worker writes anything, the second being the first thing it reads — or one stops using the phrase. The fog
> item's argument about what never-delete costs a node file's reader is preserved; only the phrase naming a first
> act changes. No other statement in the file is altered, `.scratch/graph-workflow/map.md` is not edited, and no
> file under `.claude/skills/` is changed. The bar applies.

## The manager's note at filing

*Not a change to anything above.*

**This node cannot be claimed until node 250 lands.** Its first target sentence does not exist yet: it is in node
250's uncommitted work, in `.claude/worktrees/250-worker-reaches-its-worktree`. That is sequencing the manager
holds, not a `Blocked by` edge, and it is the same sequencing [node
261](261-a-worker-can-land-at-the-repository-root-where-enterworktree-is-refused.md) is under.

**The condition covers two of the three statements the question names, and the manager did not widen it.** The
question also names the **implementation spawn** and the **shipped worker contract** as disagreeing about the first
act; the condition reaches neither, both being outside the one file. That gap is the author's and stands as written
— but it is the half that reaches every future worker on every effort, where this file reaches only this one. **It
is named here for whoever claims the node, and for the human if they want the node widened**, which is theirs and
not the manager's.

**The evidence the question rests on is the strongest kind this effort collects**: node 250's own worker read its
node before it called `EnterWorktree`, so it followed none of the three statements and nothing reported that it had
not.
