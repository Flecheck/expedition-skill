# Repoint the `.worktrees/` comment at the file that now holds the landing policy

Type: implementation
Status: superseded
Superseded by: 249

Blocked by: 158

## Question

*Superseded 2026-09-29: this question no longer needs doing here. See `## Superseded, 2026-09-29` below.*

*Surfaced by [Ignore the harness's worktree directory](158-ignore-the-harness-worktree-directory.md)'s worker, and
pasted as it wrote it.*

> The first comment block in `.gitignore` ends "See `.scratch/graph-workflow/map.md`, the landing policy". Node 140
> moved the landing policy out of `map.md` into `map-implementation-rules.md`, leaving `map.md` holding only a
> forwarding line to it. The pointer still resolves in one hop and is not broken, so this is a tidy rather than a
> defect — but node 158 could not fix it, its acceptance condition requiring those comment lines to stay unaltered.

**Blockers, in the worker's words:** *"none. Node 158's work must have landed first, or the two changes conflict in
the same file."* **The manager has made that an edge** rather than leaving it a sequencing note, both nodes editing
one small file.

## Acceptance condition

*Written by node 158's worker. Pasted as it wrote it, and not the manager's.*

> After the work, the first comment block in the file `.gitignore` at the repository root points at
> `.scratch/graph-workflow/map-implementation-rules.md` in place of `.scratch/graph-workflow/map.md`, and no longer
> names `map.md` at all. The rest of that comment block's wording is unchanged, and the entry `.worktrees/`
> immediately below it is unchanged. The second comment block and the entry `.claude/worktrees/` below it are
> unchanged. No file other than `.gitignore` is changed anywhere in the repository. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its author declined to raise this and said why**, at flag `158.2`: the pointer still resolves in one hop, and a
raise would have spent the human's single live question on it. The manager records that it agrees, and that the
judgement is the worker's rather than the manager's.

## Superseded, 2026-09-29

*The manager's note:* superseded by [node 249](249-gitignores-two-comments-point-at-files-that-moved.md), under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q1 (`verbatim`: *"ok"*, recorded on node 366). Node 366's worker's reason: the `.gitignore` comment already points at `map-manager-only.md`, "Landing an implementation node's work" (node 249).
