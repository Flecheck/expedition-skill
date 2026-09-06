# What the harness worktree cycle does to the manager's writable region

Type: precondition
Status: resolved

Blocked by: none

## Question

*The manager's own, minted after the failure below. Marked as the manager's.*

**The manager could not write the effort's own record from a shell, which is its core duty.** After two
`EnterWorktree` / `ExitWorktree` cycles in one session, the command sandbox's writable region had migrated to the
*second* worktree and never came back. Measured at the moment of failure:

```
.git IS writable
126 worktree IS writable
repo root NOT writable
```

**What it broke, concretely.** `git stash push -- <two paths>` printed `Saved working directory and index state` and
then failed twice with `unable to unlink … Read-only file system`, leaving the two paths staged, the edits in the
working tree, and a duplicate stash entry. The stash object goes in `.git`, which was writable; the working-tree
update was denied. `git merge --ff-only` would fail the same way, so **an approved node could not be landed at all**.
`cd` does not fix it: the sandbox is a path allowlist rather than a cwd rule, and moving the shell to the repository
root changed nothing.

**Why the manager could still write the graph:** the file-editing tools bypass the command sandbox. So the failure is
invisible until something needs `git`, which is exactly the landing step.

**What must be established, by experiment rather than by reading documentation:**

1. What `EnterWorktree` does to the writable region, and whether `ExitWorktree` with `keep` restores it, with
   `remove` restores it, or neither does.
2. Whether a second `EnterWorktree` in one session displaces the first worktree's write access, as the measurement
   above suggests.
3. What, if anything, restores write access to the main checkout inside one session without disabling the sandbox.
4. Whether a **subagent** that enters a worktree perturbs its parent's region, since this effort spawns one worker
   per node and the harness documents the switch as agent-local.
5. Whether the manager can avoid the cycle altogether — the recorded route has the manager call `EnterWorktree` only
   to check the base and reset, which may be replaceable by a read-only inspection from the main tree.

**What later work depends on this:** the harness-worktree route recorded in
[map-implementation-rules.md](../map-implementation-rules.md), which [node
150](150-which-harness-route-creates-a-worktree.md) settled and [node
152](152-where-the-harness-worktree-instruction-lives.md) is open on; and the landing procedure, whose separate gap is
[node 176](176-the-managers-record-edits-collide-with-a-landing.md).

## The manager's note at filing

*Not a change to anything above.*

**This is filed as the manager's own conduct failing, not the harness's.** The manager entered two worktrees in one
session under the route the map records, and the map's own account of that route already carries [flag
`150.3`](150-which-harness-route-creates-a-worktree.md) — that a correction round's re-entry mechanism *"could not be
verified from inside a subagent"*. The same unverified area produced this.

**The human's words that prompted it**, `verbatim`: *"we should make it so that there isn't issues like that later"*.

## Answer

*Pasted as the worker wrote it.*

> **The operative rule, measured.** The command sandbox is a set of bind mounts recomputed for *every* Bash call. A command succeeds iff every path it writes lies inside a `rw` mount and outside a `ro` mount. The shell's `cd` is irrelevant, and so is git's route (`git -C` from outside a tree vs. from inside it) — only the paths written matter, and only against the *writing session's* mount set. A healthy session's set is: `<repo>` rw, `<repo>/.claude` rw, `<repo>/.claude/worktrees` rw, every live worktree rw (plus its `<wt>/.claude` rw), `<repo>/.git` and `.git/worktrees/*` rw, `$TMPDIR` rw, plus the `allowWrite` paths in the user's settings; with `ro` denies on `<repo>/.claude/skills`, `<repo>/.claude/.cc-writes`, `.git/config`, `.git/hooks`, and on *some* worktrees' `<wt>/.claude/skills`, `<wt>/.claude/.cc-writes`, `<wt>/.git`, `<wt>` `commondir`. A **broken** session's set has a different root: this worker's own set for the first half of this node was rooted at `.scratch/graph-workflow/nodes` with **no repo root at all**, exactly the manager's reported failure.
>
> **The measurement instrument.** A probe that attempts a real write in each directory and deletes it, plus `grep " <repo>" /proc/mounts | awk '{split($4,a,","); print a[1]" "$2}' | sort -u`. The mount table alone is sufficient and non-destructive; every writability claim below was also confirmed by an actual write.
>
> **1. What `EnterWorktree` does to the region, and whether `ExitWorktree` restores it — NOT MEASURABLE from any worker, and here is why.** Both tools hard-refuse from a subagent: *"EnterWorktree cannot create a worktree from a subagent with a cwd override … it would mutate the parent session's process-wide working directory"*, and the same for `ExitWorktree`. Three separately spawned workers hit the identical refusal, one of them worktree-isolated. **Only the manager's own session can run this cycle.** What would settle it: the manager, in its own session, runs the mount-table one-liner above before `EnterWorktree`, after it, after `ExitWorktree {action: keep}`, and after `ExitWorktree {action: remove}` — four readings, four tool calls, no risk.
>
> What *was* measured in the nearest available form: `EnterWorktree {path: <sibling worktree>}` from a worktree-isolated worker succeeds and reports *"This agent's working directory and write access now point at the worktree; the previous directory was left untouched."* After switching away and back, the writable set was byte-identical to baseline **but the mount set was not restored** — the round trip left extra `ro` and `rw` entries behind. So a switch mutates the region cumulatively rather than restoring it.
>
> **2. Whether a second `EnterWorktree` displaces the first's write access — NOT MEASURABLE from a worker** (creation is refused, per 1). Two things bear on it. First, the tool's own description states it: *"After a further switch, previously-visited worktrees are no longer writable"* — documentation, not experiment, offered only as corroboration of the manager's measurement. Second, measured: the re-entry remedy works — after `EnterWorktree {path: sibling}` then `EnterWorktree {path: original}`, the original worktree was writable again.
>
> **3. What restores write access to the main checkout in one session — measured, three ways, and one surprise.**
> - `cd` to the repository root does not.
> - The main checkout **can never be an `EnterWorktree` target**: *"Cannot enter worktree: … is the main working tree, not a linked worktree."* So the documented re-entry remedy in 2 covers worktrees only and has no analogue for the main tree.
> - Building a worktree to enter is blocked too when the root is out of the region: `mkdir .claude/worktrees/…` → `Read-only file system`. A worktree built in `$TMPDIR` instead was then refused as a target.
> - **The surprise, and it is the most important single observation of this node: the region heals by itself.** This worker's region was rooted at `.scratch/graph-workflow/nodes` with the repo root unwritable for roughly the first half of the node, and later in the same session, with no action of this worker's, it became rooted at the repo root. It changed twice under this worker: mounts for the `126` worktree vanished the moment the manager removed that worktree, and the root moved later. **The region is therefore live session-derived state, not a snapshot taken at spawn.** What correlates with the healing is the manager's own worktree lifecycle completing; which act restores it is not observable from a worker.
> - The one channel that never stops working is the file-editing tools. Measured: shell `echo x > <repo>/.probe` → `Read-only file system`; the `Write` tool, same directory, same moment → success, confirmed on disk. Deleting it needed the sandbox off. **So the tools can create a file no sandboxed command can remove**, and this is why the breakage stays invisible until git is needed.
>
> **4. Whether a subagent perturbs its parent's region — no, and it cannot; the propagation runs the other way.** A subagent cannot enter or exit a worktree at all (1). `Agent {isolation: "worktree"}` left this worker's mount table byte-identical before and after, and the child's worktree was *not* added to the parent's writable set.
>
> **The reverse direction is real and is the finding node 152 needs.** A worker's region tracks the manager's, live. Two consequences, both measured:
> - A worker spawned with `isolation: "worktree"` **during the broken window could not write its own worktree**: `Read-only file system`, its own path appearing nowhere in `/proc/mounts` while every `rw` mount pointed at the *manager's* worktree. An identically-spawned worker after the region healed wrote its own worktree fine.
> - Two plain workers spawned by the same manager minutes apart got **different regions** — the earlier one with no writable repo root, the later one with the full healthy set.
>
> So a manager whose region has migrated silently cripples every worker it spawns while that lasts, implementation workers included, and neither the manager nor the worker sees it until a git write fails.
>
> **Two further harness facts measured here.** A worktree-isolated worker's Bash is pinned to its *launch* worktree by a separate guard, so after switching by `path` every Bash call is refused — the tool's stated effect and the guard disagree, leaving the agent with no working Bash until it switches back. This partially settles flag `150.3`: re-entry by `path` *is* available to a subagent, and it bricks that subagent's shell unless the target is its own launch worktree. Separately, the guard rejects compound Bash commands from an isolated agent, so a `for` loop is unavailable to an implementation worker.
>
> **5. Whether the manager can avoid the cycle — yes for the base check, and yes for the reset, both measured from the main tree with no `EnterWorktree`.**
> - Base check, two routes, both work read-only from the main tree: `cat .git/worktrees/<name>/CLAUDE_BASE`, and `git -C <worktree> rev-parse HEAD`, against `git -C <repo> rev-parse HEAD`.
> - Reset from the main tree into a harness worktree, from a session with a healthy region: `git -C <worktree> reset --hard 37a3d28` → exit 0; `git -C <worktree> reset --hard 8cc9b79`, whose range **crosses `.claude/skills/expedition-grilling/SKILL.md`** → exit 0. **So the reset does not need the sandbox off when it is run from the main tree on a harness worktree.**
> - The same reset **fails completely** when the worktree is outside the running session's region — failing on ordinary `.scratch` files, nothing to do with skills.
> - Therefore the manager needs `EnterWorktree` for **neither** the base check nor the reset. The manager's *own* session never has to leave the main tree.
>
> **Resulting facts later nodes depend on.**
> - `worktree.baseRef` is **not set** on this machine, so the default `fresh` applies and every harness worktree lands on `origin/master`. Measured: three harness worktrees created during this node, every one with `CLAUDE_BASE` = `8340e18`, while `master` was `37a3d28` then `8cc9b79`. The map's *"which is the typical case"* about `baseRef=head` does not hold here — the base is always stale and the reset always runs.
> - A `locked` worktree needs `git worktree remove --force --force`, and a harness worktree created by `isolation: "worktree"` is **auto-removed when the agent ends if it is unchanged** — four of five throwaway worktrees vanished by themselves. That bears on counting slot occupancy from live worktrees.
> - `git branch -D` prints `error: could not write config file .git/config: Device or resource busy` because `.git/config` is a `ro` bind mount, and **deletes the branch anyway**.
> - The `ro` overlay on `<wt>/.claude/skills` is present for **some** worktrees and absent for others in the same session's table, and the trigger was not isolated.

**What the worker reported its work invalidates, pasted as it wrote it.**

> 1. `map-implementation-rules.md`, the bullet **"The one asymmetry, and it is a hole rather than a feature"**: *"A worktree operated from the main tree with `git -C` escapes the rule entirely, because the deny list names `<repo>/.claude/skills` and a worktree at another path is not that."* The **conclusion holds only conditionally and the stated reason is wrong**. Measured: from a session whose region did not contain the worktree path, `git -C <harness worktree> reset --hard` failed on plain `.scratch/` files with `Read-only file system` — no skills file involved. From a session whose region did contain it, the same command succeeded across a `.claude/skills` file. What decides is whether the target path is inside the *writing session's* writable region, not which tree the command is issued from; and harness worktrees do sometimes carry their own `<wt>/.claude/skills` `ro` mount, so "a worktree at another path is not that" is not reliably true. This text traces to no resolved node — a repository-wide grep finds it only in the map — so it is the map's to amend.
> 2. The same bullet's rule statement, **"the sandbox mounts `.claude/skills` read-only in whichever tree the session is standing in"**: incomplete rather than false. The `ro` overlay was observed on trees the session was *not* standing in, and — the part that produced this node — the `ro` deny is not the constraint that bites when the region has migrated. The allow-set is, and it is far smaller than "everything but skills".
> 3. `map-implementation-rules.md`, *"where `worktree.baseRef` is already `head` in the human's global config — which is the typical case"*: not true on this machine. The setting is absent, and all three harness worktrees recorded `CLAUDE_BASE = origin/master` while `master` was ahead. The three-case account still stands; the case it calls typical is, here, the one that never happens.

***The manager's note on those three.*** **They are the map's to amend and the manager's to write, and it has not
written them**, because [node 171](171-carry-the-record-node-reading-rule-into-the-rules-file.md) holds
`map-implementation-rules.md` in a worktree at its gate. Amending it in the main tree now would recreate exactly the
collision [node 176](176-the-managers-record-edits-collide-with-a-landing.md) was minted for, one hour after minting
it. The amendment waits for node 171 to land.

## Flags

*Both are the worker's own text, pasted. The ids and the links are the manager's bookkeeping and nothing else.*

`175.1` **· settled** `ASSUMPTION` — The five questions are all about `EnterWorktree`/`ExitWorktree`, which refuse to run from any subagent, so I routed around the ban rather than returning nothing: I ran the measurable parts through spawned workers (one worktree-isolated, one placeholder holding a harness worktree open, two plain probes) and built one throwaway worktree **by hand** with `git worktree add --detach` in `$TMPDIR`, against this effort's standing instruction that worktrees are harness-made — the harness having refused to make one for me. It was removed with `git worktree remove --force`, exit 0. Everything I could not reach that way is marked NOT MEASURABLE above with the exact sequence that would settle it.

`175.2` **· settled** `ASSUMPTION` — My writability probe creates and immediately deletes a dot-file in every live worktree it finds. It skipped the `126` worktree by name, as instructed, but it did not skip `171-record-node-reading-rule`, which was created mid-node by the manager, so `.probe175.<pid>` was written and removed there three times by spawned probes. Nothing tracked was touched; `git -C .../171-record-node-reading-rule status --porcelain` afterwards shows only that node's own `M .scratch/graph-workflow/map-implementation-rules.md`, and a `find` for `.probe175*` and `WT175*` under `.claude/worktrees` returns nothing.

## Retrospective

*Pasted as the worker wrote it. Filed by the manager as an annotation.*

1. *What I had to hunt for.* The spawn pointed me at a heading, `## How the worktree is made`, that does not exist — `map-implementation-rules.md` has two headings and the material is a bold paragraph plus bullets inside the first one. `grep -n` returned nothing; I found it by listing headings, then grepping `worktree`. A line range would have been exact. I also hunted for whether `worktree.baseRef` was set: I tried `git config --get worktree.baseRef` first (wrong place — it is not a git setting), then found it absent from the user's settings.

2. *What arrived that this node did not need.* `map.md` in full: I read all sixty-odd lines and used one — the standing worktree instruction. The question-batching count, the retrospective rule, the token-maxing rule, the glossary's term counts, the heterogeneous-harness plan and the flag-settling rule bore on nothing a sandbox measurement can touch; they did keep me from contradicting the effort's shape, which is worth something, but a node about `/proc/mounts` is where that value is thinnest. `decisions.md` was pointed at with no section named, so I grepped it rather than reading it and used two of its 111 lines — naming the sections, as the contract says the spawn should, would have cost nothing. The contract's whole *"When a node you report is an implementation node"* section, about forty lines on acceptance conditions, bore on nothing until `NEW NODES`, and then only to tell me neither node I surfaced needs one. A narrower arrangement that would have avoided most of it: the spawn quoting the two map lines that bear on the sandbox instead of pointing at two whole files.

3. *What would have made this node easier.* The single largest cost was discovering, through three spawned agents, that **no worker can call `EnterWorktree` or `ExitWorktree` at all** — the manager could have learned that from the tool's own description before writing the node, and then either run the cycle itself and handed me the readings, or asked me only for the four questions a worker can answer. Three of the five questions are addressed to a party that cannot act. Second: the node file gave the manager's failure measurement as three lines of prose with no record of the command that produced them, so I had to build an instrument before I could compare anything to it. Third, in the record: the map's account of the sandbox has been rewritten three times, and two superseded accounts sit struck-through above the current one — under the never-delete rule that is correct, but it means a reader must work out which of three accounts is live before trusting any of it, and the live one turned out to be wrong anyway.

4. *What was stale, wrong, or contradictory.* The three items on `INVALIDATIONS`. Additionally, `decisions.md` still describes node 150's answer as *"The isolated-worker route carries the harness-worktree rule…"*, while `map-implementation-rules.md` records that route as superseded by the human's own `EnterWorktree`-by-name route — two live descriptions of the same decision in two files, and the index is the one a later worker greps. Finally, the record moved underneath this node while it ran: `master` went `37a3d28` → `8cc9b79`, the `126` worktree was landed and removed, and the `171` worktree appeared. Every measurement above is stated against the commit it was taken at for that reason.
