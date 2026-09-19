# A worker can land at the repository root, where `EnterWorktree` is refused

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 250](250-state-how-an-implementation-worker-reaches-its-worktree.md)'s worker, and pasted as it
wrote it.*

> The manager spawns every implementation worker with its working directory at `.scratch/graph-workflow/nodes`, and
> node 250's worker landed at the repository root anyway, where `EnterWorktree` is refused outright. It could still
> write, because the region was inherited; a worker that inherited no region would have been stuck with no route and
> no instruction. What does a worker do when the call is refused?

**Blockers, in the worker's words:** *"none. It must not edit `map-manager-only.md`'s `How the worktree is made`
section while another worker holds that file."*

## Acceptance condition

*Written by node 250's worker. Pasted as it wrote it, and not the manager's.*

> Done when the implementation worker's spawn, or the record the manager writes it from, states what a worker does
> when `EnterWorktree` returns a refusal naming its working directory — and that instruction is neither "disable the
> sandbox" nor "proceed and hope the region was inherited". It must state: that the worker probes its own writable
> region read-only with `grep " <repo>" /proc/mounts | awk '{split($4,a,","); print a[1]" "$2}' | sort -u`; that a
> worktree appearing `rw` there means the worker may proceed and must say in its handover that it proceeded without
> the call; and that a worktree absent from it is a raise. The bar applies.

## The manager's note at filing

*Not a change to anything above.*

**The blocker the worker named is live right now.** Node 250's own work is uncommitted in
`.claude/worktrees/250-worker-reaches-its-worktree`, editing exactly the section this node must not touch while that
holds. **This node is not claimable until node 250 lands**, and that is sequencing the manager holds rather than a
`Blocked by` edge on a decision.

**Why the manager did not simply fix its own conduct and close this.** It cannot. The working directory a worker
inherits is not a parameter the manager can pass, and **the harness resets the manager's own shell to the repository
root between its turns** — recorded at `250.1`. So there is no discipline that makes the refusal impossible, and the
worker's instruction for when it happens is the only repair that holds.

**The condition's `<repo>` is a placeholder the worker left literal**, being the repository's own path. Whoever
claims this writes the probe in a form that works without the placeholder being filled in by hand, or says why it
cannot be.
