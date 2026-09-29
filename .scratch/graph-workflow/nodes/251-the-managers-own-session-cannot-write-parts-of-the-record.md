# The manager's own session cannot write parts of the record or land code without disabling the sandbox

Type: precondition
Status: out-of-scope

Blocked by: none

## Question

*Surfaced by [node 243](243-a-worker-cannot-enter-its-worktree-by-the-route-the-spawn-names.md)'s worker, and pasted
as it wrote it.*

> Two of the manager's core duties currently require the sandbox to be switched off, and nothing has established
> whether they must. Landing node 235 needed it off for the commit, the merge and the worktree removal; and
> appending to `flags.md` and `decisions.md` needs it off while writing a node file in the same directory does not.
> The second has a measured cause — the writable mount is `.scratch/graph-workflow/nodes` and not its parent, so the
> two index files sit just outside the region — and the first has none yet. Establish, by measurement, what the
> manager's landing and record-keeping actually write that falls outside its region, and whether anything short of
> disabling the sandbox brings them inside.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above, and one half of it is already answered.*

**The record-keeping half was settled by the human stopping the manager mid-write.** They asked *"Why unsandboxed"*,
and two calls established it: the shell still cannot append to `.scratch/graph-workflow/decisions.md` or
`flags.md` — `Read-only file system`, sandbox on — but **the harness's file-editing tool writes both of them with
the sandbox on**. Both appends landed that way. So the manager's record-keeping needs no exception at all; what it
needed was a second route, and the manager had stopped looking after one failure. That is flag `243.4`.

**What is left for this node is the landing half**, which is git rather than file writes and which the manager has
not retested: the path-limited commit inside the worktree, the `git merge --ff-only` into the main tree, and
`git reset --hard` on a worktree whose base is stale. Those were run with the sandbox off and are the only remaining
claimants to an exception.

**This node is a `precondition` and decides nothing.** Its worker establishes by measurement what is actually
refused and what route succeeds; what the manager should then do about it is a decision that node does not make.

## Ruled out of scope, 2026-09-29

*The manager's note:* under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q2 (`verbatim`: *"ok"*). Its line in `map-manager-only.md`'s `## Out of scope` is node 366's worker's text.
