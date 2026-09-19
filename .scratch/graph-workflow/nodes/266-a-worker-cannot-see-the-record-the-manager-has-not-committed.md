# A worker's worktree cannot see the record the manager has not committed

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [node 260](260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md)'s worker, and pasted as it
wrote it.*

> An implementation node whose work *is* a change to the effort's record is handed a worktree reset to committed
> `master`, while the record it must edit lives partly uncommitted in the manager's main tree. Node 260 hit this
> exactly: its condition named a `map.md` paragraph that existed only in the manager's working copy, and the node
> file it had to link to was untracked. The worker could produce the right end state, but landing has to reconcile
> two divergent copies of `map.md` by hand, and a worker with less context would have silently written against a
> stale map or reported the condition broken. Which fix does the human want — the manager commits the record before
> resetting a worktree for any node that touches it; record-file nodes are worked in the main tree rather than a
> worktree; or the manager states the discrepancy in the spawn and owns the reconciliation as it does today? Each
> has a different cost and one of them changes the landing policy in `map-manager-only.md`.

**Blockers, in the worker's words:** *"none"*

## The manager's note at filing

*Not a change to anything above.*

**This is a defect in the manager's landing policy and the manager found none of it.** The policy resets every
worktree to the manager's committed `HEAD`, and says nothing about the manager's own **working tree**, which on this
effort is never clean: the graph's record is written continuously and committed in batches.

**The concrete cost, measured on node 260 rather than argued**: ~8k tokens and two minutes of a worker's context
establishing that a paragraph its condition quoted was not in its tree, and a landing that now cannot fast-forward
without a hand reconciliation of `map.md`.

**One consequence the question does not name, and it reaches every record node, not only this one.** A node file
minted during the session is **untracked** in every worktree cut before the commit that adds it. So any link a
worker writes to a node it must cite — which the effort's second standing writing rule requires — dangles in the
tree the checker reads, and resolves only after landing. Node 260's worker took that trade knowingly. **A checker
is blind and will read it as a broken link**, so the cost is paid again at every check.

**The manager offers no position between the three options**, having caused the problem, and notes only that the
first and second both change `map-manager-only.md`'s landing policy while the third leaves it as it is and makes
the manager's spawn carry the discrepancy every time.
