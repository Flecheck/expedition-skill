## Landing an implementation node's work

The landing policy in `map-manager-only.md`, as it stood before the human declared deliverables on 2026-11-12:

The landing policy is the one the root `CLAUDE.md` states under `## The worktree of an implementation
node`: a worktree made with plain `git worktree add` at
`.scratch/manager-own-choices/worktrees/<NN>-<name>`, on a branch `worktree-<NN>-<name>`, created from
the repository root with `git -C <repo root>`. On approval the manager makes one path-limited code
commit on that branch carrying the node trailer, fast-forwards the main checkout's `master` to it, and
removes the worktree and the branch. The merge and the removal run with the sandbox off. On a reject or
a supersession before landing, the graph is edited first and the worktree and branch are removed after.
Where integrating conflicts, the manager starts a correction round naming the conflicted paths. The
effort declares no deliverables. Nothing is pushed without the human's word.
