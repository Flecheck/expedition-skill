# Carry the worktree lifecycle into the shipped files

Type: implementation
Status: open

## Question

The implementation worker contract and this map's landing-policy paragraph are both written for a workflow that
works in place, never branches and holds an exclusive code slot. **Both have to say what an implementation node's
lifecycle now is**, as settled by [Run an implementation node's work in a worktree](68-implementation-in-a-worktree.md).

Reported by node 68's worker, which wrote the acceptance condition below. **Blockers: none.**

## Acceptance condition

*Written by node 68's worker.*

Two files are edited, and nothing else is.

**1. `.claude/skills/expedition-implementation/SKILL.md`.** The sentence *"You hold the **code slot** for the whole
of this node — from your first edit until the human has approved your work. No other implementation worker is
running while you do."* is replaced by text stating: the worker holds **a** code slot for the whole of the node,
from its first edit until the human has approved the work; the number of code slots is set by the effort and may be
more than one; and the tree named in the worker's spawn is the worker's alone for the whole of the node, and the
worker does not edit files outside it. The `code slot` entry under *Words used exactly* is updated to match — it
currently reads *"the right to modify product code, held by one worker at a time"* and must stop asserting one. The
file's existing hard rule 3 — never commit, never branch, never switch branches, never push, never rewrite history
— is left exactly as it stands, wording included.

**2. `.scratch/graph-workflow/map.md`.** The paragraph beginning *"**Landing policy, now settled and binding on
this map too**"* is edited under this effort's standing never-delete rule: superseded text is marked as superseded
and left in place, and new text is added around it. The new text states, in this order: an implementation node's
worker works in a git worktree the manager creates for that node with `git worktree add` off the current `HEAD`, on
a branch whose name carries the node's id, placed outside the repository's working tree; the changes stay
uncommitted through the checker and through the human's gate; on approval the manager makes one path-limited commit
of that node's paths, rebases the branch onto the branch the manager thread is on, re-runs the bar's commands on the
rebased result, merges with `git merge --ff-only`, then removes the worktree and deletes the branch; a rebase
conflict is resolved by nobody in the moment — the manager runs `git rebase --abort` and the node takes a correction
round with the worker respawned; a post-rebase bar failure likewise takes a correction round and the work does not
land; on reject the worktree is removed and its branch deleted, and where the human asks for the work to be kept the
manager commits it onto that branch before removing the directory; nothing is ever pushed. It further states that
the number of concurrent implementation workers is a setting of the effort, that it is **one**, and that occupancy of
a code slot is discovered by counting the live worktrees rather than by inspecting the working tree for uncommitted
changes.

The map's existing sentence *"No branch is ever created or switched, nothing is ever pushed, and history is never
rewritten"* is marked as superseded on its first two counts, with the never-pushed clause stated as still standing.

Both files continue to state properties rather than assuming any particular repository, machine, or toolchain beyond
git, which the landing policy already assumes throughout. **Neither file gains a claim that worktrees are reused
between nodes.**

The standing bar applies: the working tree builds, warns about nothing, is formatted, and passes the tests relevant
to the change. This repository has no build, no tests and no formatter, which is a complete bar on its remaining
half and not a deficient one — so what remains is the project's own criteria, this map's standing preferences, and
the `_Avoid_` lines of the glossary the shipped files declare authoritative.

### The manager's note at filing, not a change to the condition

**Two facts in clause 1 were verified rather than trusted**, in the contract as it stands: the code-slot sentence is
present verbatim as quoted, and the *Words used exactly* entry reads exactly *"the right to modify product code,
held by one worker at a time."* Both hold.

**This node writes `map.md`, which the implementation contract's hard rule 1 forbids** — *"You write product code.
You write no graph file."* That is the same collision [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md) met, and it was answered there by the human's ruling that the ban stops a worker
doing the manager's **progress bookkeeping** and does not reach work whose **subject** is a graph file. **Here the
map is the subject of clause 2.** The permanent fix is [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md), still open — so whoever claims this node needs the human's licence
carried into the spawn in their own words again, exactly as node 59 did. **The manager may not grant it.**
