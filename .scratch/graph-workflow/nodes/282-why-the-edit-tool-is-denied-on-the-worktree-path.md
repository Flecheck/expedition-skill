# Why the `Edit` tool is denied on the worktree path, and what the route must say

Type: research
Status: open

Blocked by: none

## Question

*Surfaced by [node 274](274-carry-the-widened-supersession-into-the-shipped-files.md)'s worker, and pasted as it
wrote it.*

> An implementation worker on node 274, told to write its worktree by absolute path, had every `Edit` call on files
> under `.scratch/graph-workflow/worktrees/274-widened-supersession/` refused by the permission system, while a
> `Bash` write to the same directory succeeded. The path was added to `.gitignore` at commit `7aa89cb` by node 269.
> **What decides this — whether it is the ignore entry, the write allowlist, or something else — is unmeasured**,
> and the route settled at [node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md) says which path a
> worker writes and not which tool it may use. **Every future implementation worker meets this.** What this settles:
> the cause, whether it reaches the two older worktree paths, and whether the shipped route or `map-manager-only.md`
> must name a writing route.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**This is the manager's defect to have not known.** It has now told six implementation workers which *harness* tools
not to call and has never told one that an *ordinary* tool would be refused. Node 274's worker lost a round of
denied calls and a probe establishing it, and did not raise because a route existed — **so the cost is paid quietly
by every worker rather than once by the manager.**

**One correlation the manager holds and offers as material rather than as a finding**: node 269 added
`.scratch/graph-workflow/worktrees/` to `.gitignore` at `7aa89cb`, and the manager's own sandbox policy carries a
deny list nested inside its write allowlist. **Whether either is the cause is untested**, and this effort has twice
had a mechanism asserted from a plausible correlation and refuted by measurement — flags `263.4` and `277.2`. **A
worker on this node should measure before it explains.**

**Two cheap discriminators the manager can name without having run them**, offered so the node does not start from
nothing: the two older worktree paths — `.claude/worktrees/` and `.worktrees/` — are ignored by the same file and
would separate *ignored* from *this particular path*; and a file under `.scratch/graph-workflow/` but **outside**
`worktrees/` is not ignored and is written by `Edit` routinely, which is the control for the ignore hypothesis.

**What the answer has to reach**, beyond the cause: **where the route is stated.** Node 265's answer and
`map-manager-only.md`'s `How the worktree is made` both say a worker writes its tree by absolute path and neither
says with what. If a worker must use `Bash`, that belongs in the record and in every implementation spawn — and
ground rule 1 bites, since naming a tool is closer to declaring a command than to discovering a property.
