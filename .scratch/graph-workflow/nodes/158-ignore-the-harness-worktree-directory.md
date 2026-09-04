# Ignore the harness's worktree directory

Type: implementation
Status: claimed

Blocked by: none

## Question

*Surfaced by [Which harness route creates an implementation node's
worktree](150-which-harness-route-creates-a-worktree.md)'s worker, and pasted as it wrote it.*

> The repository's `.gitignore` ignores `.worktrees/`, the path the landing policy used when the manager created
> worktrees by hand. The harness creates them at `.claude/worktrees/` instead, which no rule covers, so a live
> worktree appears as untracked in the main tree's `git status`, is traversed by repo-wide searches, and has been
> observed duplicating this workflow's own skill files into the manager's context.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 150's worker. Pasted as it wrote it, and not the manager's.*

> After the work, the file `.gitignore` at the repository root contains an entry that causes git to ignore the
> directory `.claude/worktrees/`, immediately preceded by a comment stating that this directory holds the git
> worktrees the agent harness creates for implementation workers, and that it is ignored so those worktrees are never
> committed. The file's existing entry ignoring `.worktrees/` is still present, and the existing comment lines above
> it are still present and unaltered. Running `git status --porcelain` from the repository root produces no line
> whose path begins with `.claude/worktrees`. No file other than `.gitignore` is changed anywhere in the repository.
> The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The pollution is confirmed in the manager's own context**, not only in `git status`: the harness surfaced all seven
`expedition*` skills a second time, scoped to `.claude/worktrees/agent-ac549d7fb8ff2bf22/`, in the manager's skill
list. Every agent spawned while a worktree is live pays for that.

**The manager did not make this one-line change itself**, though it could have and was tempted to. Having already
acted once today on its own authority in breach of its contract — flag `140.8` — it minted the node instead.

**Flag `68.2` bears on it and stays open**: it recorded that an ignore rule could not be assumed for a repository the
workflow does not own. This node's condition is scoped to this repository only and asserts nothing about any other.
