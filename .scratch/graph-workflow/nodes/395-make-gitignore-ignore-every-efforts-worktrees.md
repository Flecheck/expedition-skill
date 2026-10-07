# Make `.gitignore` ignore every effort's worktrees directory

Type: implementation
Status: claimed
Blocked by: 394

## Question

This lets a later effort in this repository cut implementation worktrees without first editing `.gitignore`, as the root `CLAUDE.md` describes. Today `.gitignore` ignores only `.scratch/graph-workflow/worktrees/`. Should it ignore `.scratch/*/worktrees/` instead?

*Reported by [node 394](394-a-repo-claude-md-so-the-next-effort-does-not-start-cold.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none". The manager added node 394 as a blocker, because this condition edits the `CLAUDE.md` that node 394 creates.*

## Acceptance condition

*Authored by node 394's worker and filed by the manager.*

> The work edits `.gitignore` and `CLAUDE.md` only. Scope came from no search: the named places are the work.
> 1. `.gitignore` ignores `.scratch/*/worktrees/`, and `git check-ignore .scratch/anyname/worktrees/x` prints that path.
> 2. `.gitignore` still ignores `.scratch/graph-workflow/worktrees/`.
> 3. The sentence in `CLAUDE.md`'s `## The worktree of an implementation node` that tells an effort to check `.gitignore` before its first worktree, and to add an entry where none covers it, is removed. The bullet still states that `.gitignore` ignores that path.
> 4. `CLAUDE.md` is at most 900 words by `wc -w CLAUDE.md`.
> 5. The working tree meets the bar.
