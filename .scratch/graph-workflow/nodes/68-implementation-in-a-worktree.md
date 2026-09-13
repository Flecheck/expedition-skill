# Run an implementation node's work in a worktree

Type: grilling
Status: resolved

## Question

An implementation node's worker writes directly into the tree the manager and the human are working in. The
human's instruction is that it should work in a **git worktree** instead, and that the work reaches the main branch
by a named sequence rather than by a plain commit in place.

### The human's instruction, `verbatim`

> *"Add a node to run implementation tasks in a worktree. During the review, the changes are not commited but when
> they pass they are commited, rebased on the branch where the main thread is and then merged ff on it."*

So the lifecycle becomes: **work in a worktree → check and gate against uncommitted changes → on approval commit,
rebase onto the main thread's branch, fast-forward merge.**

### This reverses part of [Git and code-landing policy](11-git-and-code-landing.md), and that has to be said plainly

That node's answer states: **"The manager commits — one commit per implementation node, containing only that node's
code, and only after the human has approved it. The workflow never branches, never pushes, and never rewrites
history."**

The instruction keeps the first sentence — one commit per node, after approval — and **reverses the second on two of
its three counts**: it branches, and a rebase rewrites history. Only *never pushes* survives untouched.

**It is not a contradiction of the reasoning, which is why this is a node rather than a raise.** Node 11's
never-branch clause was decided in a session where the alternative on the table was a long-lived feature branch, and
its stated reasons were the human's own review habit and the exclusive code slot. A worktree that lives for one node
and merges fast-forward serves both of those better than working in place does, because it stops an
in-progress node's edits from appearing in the human's own tree. **The human has now seen the mechanism and chosen
it**, so what is open is the specification, not the direction.

## What this node has to settle

1. **What the checker sees, and where.** The changes are uncommitted during the check, so the checker must be
   pointed at the worktree rather than at the main tree — and its third given is *the work — the paths that
   changed*, which are now paths inside a worktree. Whether `git diff` in the worktree is the route, and what the
   checker's before-state is.
2. **What happens on reject.** Node 11's lifecycle had nothing to discard; a worktree is discardable, which is new
   leverage and a new decision. Whether a rejected node's worktree is removed, kept for the next round, or kept as
   a record.
3. **Where the gate sits relative to the merge.** The instruction says commit-then-rebase-then-merge happens *when
   they pass*, so the gate precedes all three. Whether the human reviews the diff from the worktree, and whether
   anything can still fail between approval and the fast-forward.
4. **Whether the rebase can conflict, and who resolves it.** A fast-forward merge is only possible after a clean
   rebase. If another node landed on the main branch meanwhile, the rebase may conflict — and the exclusive code
   slot is what currently makes that impossible. **If the code slot stays exclusive, this cannot happen and the
   rebase is a formality; if the worktree is what finally makes parallel implementation nodes safe, it is the
   central question of this node rather than a detail.** That is the decision with the most reach.
5. **Cleanup.** Who removes the worktree, and when.
6. **What the six shipped contracts have to say.** The implementation contract's paths, and the checker's third
   given, are both written for a single tree.

### One measured cost the human should have before deciding, from [What one node actually costs](52-token-cost-of-a-workflow.md)

That node found, from primary harness documentation, that **prompt-cache scope is per machine *and* per directory,
worktrees included** — so an agent working in a worktree **forfeits prefix sharing** with everything cached against
the main directory. Its own words: *"a cost this effort has never priced and the one item here that is actionable
today."*

**This is that item arriving.** The cost is real and its size is not yet measured. It is worth naming that this node
would be the first decision in the effort to knowingly **spend** tokens for a correctness property, every other
token finding so far having been a saving — which makes it a good test of whether the effort's priorities are
ordered or merely listed.

## Where it came from

The human's own instruction, unprompted, alongside two others filed as [Whether the workflow ships explicit
subagent definitions](69-explicit-subagent-definitions.md) and [Pruning a long-running effort's
map](70-pruning-a-long-running-map.md).

### Claimed by the manager

Picked as one of two grilling nodes, on the human's instruction to choose. **It carries the furthest**: its
question 4 asks whether the exclusive code slot survives, and if worktrees make parallel implementation nodes safe
that is the largest change to the design since it was charted. Its cost is measured and unpriced — worktrees
forfeit prefix cache sharing, which [What one node actually costs](52-token-cost-of-a-workflow.md) named as *"the
one item here that is actionable today."*

## Answer

**An implementation node's worker works in a git worktree the manager creates for that node alone. The changes stay
uncommitted through the check and the gate. On approval the manager commits, rebases onto the branch the manager
thread is on, re-runs the bar, fast-forward merges, and removes the worktree.** The code slot survives as a
**count**, and the count is **one** — a number, not a property.

```
manager creates the worktree off HEAD → worker implements in it (uncommitted)
    → checker checks the acceptance condition in the worktree
    → manager raises the gate, pointing at the worktree
        → approve → commit → rebase onto the manager thread's branch → re-run the bar
                    → merge --ff-only → remove the worktree, delete the branch → node resolves
        → correct → worker fixes in the worktree; bar re-checked; gate re-raised   (uncapped)
        → reject  → graph edit, then the worktree is removed and its branch deleted
```

### The code slot is a count, and the count is one

The human's answer, `verbatim`: *"for 68, for now there will be only one running at once, but it should be possible
to run multiple ones at once."* So *exclusive* stops being a property of the design and becomes **a number in this
map's Notes**, the same shape [Concurrency model](04-concurrency-model.md) already uses for *"~2 grilling subagents
in flight"*. Raising it later changes a number and no part of the lifecycle.

**Worktrees also make the slot countable rather than inferred.** [Git and code-landing
policy](11-git-and-code-landing.md) discovered occupancy as *no uncommitted changes outside the effort's own
directory* — a heuristic that reads the human's own hand-edits as a dead worker. It is replaced: **the live
worktrees are the occupied slots**, one per claimed implementation node; a worktree with no claimed node is the
death signature; and the human's tree no longer participates in the signal at all. *"This is the single largest
improvement the change buys, and it is what makes the count safe to move."*

### The merged state is checked, because the check is split across the rebase

Two worktrees can touch disjoint files, fast-forward cleanly, and leave a broken tree — each checker having passed a
state that never landed. **It closes by splitting what is checked, and the split is principled rather than
defensive.** The **acceptance condition is a statement about this node's own work**, so it is checked in the
worktree, exactly as today. The **bar is a property of a tree**, so it must hold of the tree that actually lands —
the rebased result. The manager re-runs the bar after the rebase and before the fast-forward.

Not new machinery: [Human review of landed code](20-human-code-review.md) already re-checks the bar on every
correction round, and running commands is assembling rather than authoring, inside the manager's scribe boundary.
At a count of one it is a no-op; in `graph-agent`, where the bar has no commands, a no-op twice over. **A
post-rebase bar failure takes a correction round** — no new status, no new gate outcome.

### A rebase conflict is nobody's to resolve silently

**Even at a count of one the main branch moves under an in-flight node**, because node 11 has the human committing
graph files by hand while work is in flight. **Absorbing the human's own periodic commits is the rebase's real
job**, and it is clean by path-disjointness. At a higher count a conflict is ordinary: the manager runs `git rebase
--abort`, which restores the worktree exactly, and the node takes a **correction round** with the worker respawned
on the new base. Three reasons — the manager does not author code; the worker holds the intent behind the lines in
conflict; and `--abort` is a total non-destructive undo, *"which is what a policy running on repositories this
machine has never seen can afford to rely on."*

**Consequence, named rather than hidden: the human's approval is no longer the last thing that can fail.** At a
count of one neither failure is reachable except through the human's own commits.

### The worktree is the manager's, not the harness's

[Whether the workflow ships explicit subagent definitions](69-explicit-subagent-definitions.md) closed the
declared-type route, and it is refused on its own merits besides: it is a **harness** assumption where `git worktree
add` is a git assumption the landing policy already makes; **its base ref is wrong**, defaulting to
`origin/<default-branch>` where this lifecycle must branch from current `HEAD` and a repository with no remote has
no such ref; and **the manager must own the path** to point the checker and the human at it and to run the commit,
rebase, merge and removal.

So `git worktree add -b <branch> <path> HEAD`, run by the manager before it spawns the worker. **It goes outside the
repository's working tree** — the property, whose default realisation is a sibling of the repository root, falling
back to a path under `git rev-parse --git-common-dir`. A worktree inside the tree shows up as untracked in the
human's `git status`, *"which is the exact thing this change exists to prevent, and no ignore rule can be assumed in
a repository the workflow does not own."* **The branch carries the node's id**, `expedition/<effort>/<NN>`, and is
deleted with the worktree. **It is never pushed** — the one clause of node 11's git policy that survives untouched.

### What the checker sees, and where

**The checker contract needs no change.** Its third given already reads *"the paths that changed, in the working
tree holding them"* — written tree-agnostically. Only the manager's spawn changes, naming the worktree.

**The before-state is exact, and better than what it replaces.** A worktree is empty at creation, so at check time
everything modified or untracked in it is this node's work and nothing else. **`git status` in the worktree *is* the
list of paths that changed** — discovered rather than declared, where in the main tree that list is polluted by the
human's own edits and bookkeeping.

**Nothing confines the worker to its worktree except the instruction to stay there.** Node 69 established that a
tool set cannot express a path and that Bash defeats every write rule the contracts state. *"It is isolation of the
human's tree from accidents, not a sandbox"* — stated so no later reader mistakes the worktree for enforcement.

### On reject, and what "keep it" now costs

Node 20's policy stands — discard by default, the discovery survives as prose, one line offering to keep. **Only the
mechanism changes, and it gets cheaper.** Discard is `git worktree remove --force` and a branch deletion, with no
path-limited cleaning of a tree that also holds the human's bookkeeping — *"which was the risky half of the old
procedure."* **Keep now costs nothing and pollutes nothing**: the manager commits onto the worktree's branch and
removes the directory, so the branch is the record and **a kept reject cannot be miscounted as an occupied slot.**

### The cost, priced, and one belief left standing as a belief

**[What one node actually costs](52-token-cost-of-a-workflow.md) named the wrong cost.** It flagged worktrees
forfeiting prompt-cache prefix sharing as *"the one item here that is actionable today."* **The same node's primary
source says a subagent never reads its parent's cache regardless**, and the directory-scoped sharing it warns about
requires several agents matching on model, effort, agent type, tools, output schema *and* directory. **Nothing in
this design matches**: a worker and its checker differ in tools, every other worker differs in type. **There is no
sharing for a worktree to forfeit.** It becomes real in exactly one future — a fan-out of same-type implementation
workers — which is the parallel case the count is kept open for.

**The real cost is the cold build.** A fresh worktree is a fresh checkout with an empty ignored-artifact directory,
so the bar's build runs from scratch in every implementation node in any repository whose build cache is keyed to
the working directory. **Lang is Rust with a `target/`, so the dogfood target pays it in full.** Wall-clock and
tokens both, a cold build's output being what the worker and the checker read. **This is the number the dogfood must
carry back.**

**The reuse belief is not written into this specification.** The human's words were *"i belive"*; the harness's own
wording is *"its own git worktree (auto-cleaned if unchanged)"*, which reads as per-agent creation, and it does not
govern this lifecycle either way. **What is true is that reuse is now a policy the manager could simply adopt**,
the manager owning creation — *"the cheapest available remedy if the measured number hurts."* Not adopted now: a
reused worktree persists between nodes, breaking the slot count's discovery and reintroducing the dead-worker
leftovers the old heuristic suffered from.

## Flags

`68.1` `ASSUMPTION` — **The checker contract needs no edit, and the worktree path travels in the spawn instead.**
Its third given was already written without assuming which tree. *"I settled this rather than asking, because it is
a fact the file states rather than a choice."*

`68.2` `ASSUMPTION` — **The worktree lives outside the repository's working tree, defaulting to a sibling of the
repository root**, with a fallback under `git rev-parse --git-common-dir`. Chosen as a property rather than a fixed
path, because no ignore rule may be assumed in a repository the workflow does not own.

`68.3` `ASSUMPTION` — **On reject, the manager commits the work onto the unmerged worktree branch when the human
asks to keep it, then removes the directory.** Node 20 settled the policy and only the mechanism was open; the
branch was taken over a surviving directory *"so a kept reject cannot be miscounted as an occupied code slot."*

`68.4` `ASSUMPTION` — **Worktree reuse is recorded as an unestablished belief and left out of the specification.**
The human offered it as *"i belive"*; the harness's wording reads as per-agent creation; and it is moot for a
manager-created worktree. Written as a remedy available against measurement rather than as a property.

## Annotation: two things the worktree lifecycle broke, found on its first two runs

*Filed by the manager at [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md)'s landing —
the second implementation node to use the lifecycle this node decided. Not a change to the answer above.*

### 1. The worktree moves inside the repository, and flag `68.2` stays open

**What broke.** The manager presented node 71's gate describing a diff. The human replied, `verbatim`: *"what are
the changes ? I don't see them in git ?"* — because `git diff` in the repository showed only the manager's graph
bookkeeping, the work being uncommitted in a checkout under `/tmp`. `map.md` records that one of the human's two
interfaces **is** the diff, so a gate that describes one and points at nothing has not been presented.

**The instruction**, `verbatim`: *"Also for the next times, add the worktrees in the project directory"*, and on
being told it costs an ignore rule: *"For the worktree, I think it might be needed as otherwise it is too anoying
for the review"*.

**What it costs, stated because this node decided the opposite.** Flag `68.2` reads: *an expedition places an
implementation node's worktree outside the repository's working tree, on the property that no ignore rule may be
assumed in a repository the workflow does not own.* That property is untouched and the reasoning still holds for
what the workflow **ships**. What changed is this effort's own practice, which owns its repository and can carry an
ignore rule: worktrees now live at `.worktrees/NN-<name>/`, and a `.gitignore` was added for them where none
existed. **Flag `68.2` is therefore still outstanding**, and the shipped answer for a repository the workflow does
not own is undecided.

**Nobody could have caught this from the record.** Three resolved nodes each hold a piece — this one moved the work
out of the repository, [Human review of landed code](20-human-code-review.md) settled that the human reviews a
diff, and `map.md` names the diff as an interface — and the hole is between them. That is recorded as a duty
missing from [Gather the manager's accumulated duties into one enumerated list](75-gather-the-managers-duties.md)'s
list, with the method's limit stated there.

### 2. The landing step cannot run in the manager's sandbox

**What broke.** `git merge --ff-only` failed with *"unable to unlink old
'.claude/skills/expedition-checker/SKILL.md': Read-only file system"*. The manager's sandbox allows the project
directory and carves specific paths back out inside it — `.claude/skills`, `.claude/hooks`, and the settings files
— which is the harness's guard against an agent rewriting its own instructions. Verified by test rather than
assumed: `touch` in the project root succeeds and `touch .claude/skills/…` does not, and this project ships no
settings files, so nothing here configured it.

**Why this lifecycle created it and the old one did not.** Before worktrees, a worker wrote the file in the main
checkout and the manager only committed it; `git commit` **reads** the file. A merge **writes** it. So the same
paths that were readable became unwritable, and the failure appears at the last step of the node rather than the
first.

**It is not fixed by moving the worktree inside the repository** — the merge writes the main checkout's
`.claude/skills` wherever the worktree lives. The human's word, `verbatim`: *"you can run it outside the sandbox"*,
and the merge, the prune and the branch delete were run with the sandbox off. **That is a per-node exception and
not a rule**: it recurs on every implementation node whose work is a shipped skill file, which on this effort is
most of them.

**A second artifact of the same guard.** `git worktree remove` and `git worktree prune` both failed with *"failed
to delete '.git/worktrees/wt-71': Device or resource busy"*. `/proc/mounts` shows the sandbox bind-mounts
`.git/worktrees` and each worktree's admin directory, so the directory cannot be unlinked from inside it. The
checkout itself was removed; only the admin directory persisted, and the prune succeeded with the sandbox off.

## Annotation: one clause of this answer is superseded

*Filed by the manager from [node 216](216-what-a-correction-round-after-a-rebase-conflict-owes.md)'s worker, in its
own words, on the human's answer to that node's `Q1.` **This node stays `resolved`.***

> **Node 68's** *"A post-rebase bar failure takes a correction round — no new status, **no new gate outcome**"* is
> superseded in its second clause only. A bar failure is fixed by somebody authoring something, and content that did
> not exist when the human approved is not covered by that approval. **"No new status" stands**: the node does not
> change state, and it is the same node throughout.

**What supersedes it** is node 216's single test, which the human took as written: after an approval, **did anybody
author content?** Nothing authored — the approval stands and the manager lands. Something authored — the work
returns to the checker, then to the human for another approval. A post-rebase bar failure is the authored branch.
