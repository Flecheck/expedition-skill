# Node 250's finished work is committed to a branch that nothing will land

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [node 264](264-no-status-for-a-node-whose-work-no-longer-needs-a-node.md)'s worker, and pasted as it
wrote it.*

> Node 250's work is finished, passed its checker and is committed to `worktree-250-worker-reaches-its-worktree`,
> which is not on `master`. Node 265 replaced the route that work documents and node 268 is writing the replacement
> text now, so nothing will ever merge that branch. The node itself is superseded under node 264. What happens to
> the branch and its worktree — deleted outright, or read by node 268's worker first for anything worth carrying
> across?
>
> **It also sets a precedent the record has no slot for.** `SKILL.md`'s reject taxonomy sends a rejected node to
> exactly one of three places — beyond the destination, asked the wrong question, or something upstream is wrong —
> and node 250 is none of the three. **The work was right when it was written and the world changed under it before
> it landed.** What this decides is what happens the next time that occurs, which on a long-running effort it will.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**One half of the question has been overtaken since it was written, and the manager is saying so rather than letting
a worker discover it.** Node 268's worker has **finished**. It did not read node 250's branch — its spawn told it to
work from `master` and ignore that branch entirely, which was the manager's instruction and is the reason the
*"read it first for anything worth carrying across"* option was never taken. So that option is now *re-read it
retrospectively and carry anything missed into a follow-up*, which is a different and more expensive thing than the
question assumes.

**What the branch actually holds**, so nobody has to go and look to decide: commit `bd93fb8`, a single file
`map-manager-only.md`, 45 insertions and 0 deletions, adding a section `How the worker reaches it` stating the
worker's half of the `EnterWorktree` route. **Two blind checkers passed its bar and failed it on its acceptance
condition**, the condition having been measured false in three of its six clauses; the manager later amended those
clauses under node 252's rule, so the text and its condition now agree. **None of that changes that the route it
documents no longer exists.**

**The part the manager thinks outlasts the branch** is not the text but two measurements inside it, which are cited
as evidence in node 265's resolved answer and survive whatever happens here: that permission to write a worktree
precedes the `EnterWorktree` call, and that a worker's writable region holds every live worktree rather than its
own. **Those are safe in node 265 and in node 250's own file under never-delete.** What is at risk is only the
branch.

**The precedent half is the larger question and the manager holds no position on it.** It has now happened once,
visibly, within a single day. Whether that makes it worth a rule or is the sort of thing a long effort simply eats
is exactly what this node decides.
