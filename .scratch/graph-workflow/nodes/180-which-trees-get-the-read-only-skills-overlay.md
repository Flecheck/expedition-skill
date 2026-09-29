# Which trees get the read-only `.claude/skills` overlay

Type: research
Status: out-of-scope

Blocked by: none

## Question

*Surfaced by [What the harness worktree cycle does to the manager's writable region](175-what-the-worktree-cycle-does-to-the-sandbox.md)'s worker, and pasted as it wrote it.*

> The `ro` bind mount on `<tree>/.claude/skills` decides whether a merge or a reset crossing a shipped file needs the
> sandbox off, and it was observed present on some worktrees and absent on others within one session's mount table,
> with the trigger not isolated. What determines it — a session standing in that tree, the tree existing when the
> profile was built, or something else — and does the answer make the landing route's "needs the sandbox off" cases
> predictable in advance rather than discovered on failure?

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**Why it matters beyond tidiness.** The effort's landing policy tells the manager to expect a sandbox-off merge when
a node touched `.claude/skills/`. Node 175 measured a reset **crossing** such a file succeeding inside the sandbox
when run from the main tree on a harness worktree, and a reset touching **only** `.scratch/` failing when the
worktree was outside the session's region. So the rule as recorded predicts the wrong cases in both directions, and
this node is what would make the prediction sound.

**The sources are this machine's own mount table and the harness's behaviour**, both readable without the human.

## Ruled out of scope, 2026-09-29

*The manager's note:* under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q2 (`verbatim`: *"ok"*). Its line in `map-manager-only.md`'s `## Out of scope` is node 366's worker's text.
