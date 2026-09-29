# The landing merge runs with the sandbox off from the start

Type: implementation
Status: open
Blocked by: 234

## Question

Should the landing policy say that `git merge --ff-only` into the main tree always runs with the sandbox off? The sandbox mounts the main checkout's `.claude/skills` read-only, so a merge run inside it can fail after writing part of its result. Every landing merge on 2026-09-28 ran with the sandbox off from the start, and none partially wrote.

*Reported by [node 234](234-a-failed-merge-can-leave-the-tree-partially-updated.md)'s worker under its `NEW NODES`, and filed by the manager. Its words on blockers: "none. It edits `.scratch/graph-workflow/map-manager-only.md`, which node 234 also edits, so the two must not run in the same pair of code slots." The manager made the edge to node 234.*

## Acceptance condition

*Authored by node 234's worker and filed by the manager.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`. The worker may edit those two files and no other.
> Done means every one of the following is true of the finished tree.
> 1. In `map-manager-only.md`, under the heading `## Landing an implementation node's work`, the paragraph beginning `**Landing policy**` states that the manager runs `git merge --ff-only` with the sandbox off, and states the reason: the sandbox mounts `.claude/skills` in the main checkout read-only, so a merge run inside it can fail after writing some of the changed files.
> 2. Where a sentence stating a rule that currently binds is replaced to meet clause 1, its text before the change is appended, unaltered, to `map-history.md` under a heading naming `map-manager-only.md` and this node, with a subheading naming *Landing an implementation node's work*. It is appended rather than replacing anything.
> 3. The text in the same section that states the repair for a partially written merge (confirm that each dirty file is byte-identical to the branch's version, discard, then re-run the merge outside the sandbox, and stop without discarding where any file differs) is still present, and says it applies where a merge was run inside the sandbox.
> 4. Every markdown link in both files resolves to a path that exists, except a link to a path outside this repository.
> 5. No file outside `.scratch/graph-workflow/` is modified.
> Scope came from no search: the named places are the work.
