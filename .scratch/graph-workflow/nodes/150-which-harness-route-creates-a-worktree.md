# Which harness route creates an implementation node's worktree

Type: grilling
Status: claimed

Blocked by: none

## Question

*Minted by the manager on the human's standing instruction. The question below is the manager's own.*

The human has directed that a worktree be created by the harness rather than by hand. **The instruction is settled and
is in the map**; what it does not settle is which harness route carries it, and the two are not interchangeable.

**Their words**, `verbatim`:

> when you use worktrees, you should use the EnterWorktree skill instead of creating worktrees by hand - that way you
> don't have all these worktree management issues afterwards

**Why a route still has to be chosen.** `EnterWorktree` switches **the calling session** into the worktree. The
manager is the one party that must stay in the main tree: it owns the graph, and every node file, `decisions.md` and
`flags.md` write it makes is to the main checkout. The parties that need to be *in* the worktree are the **worker**
that writes the code and then the **checker** that reads it — two different agents, across a span that outlives
both, because the tree must survive until the human's gate.

**What each route costs, as far as the manager can state it without deciding:**

- **The manager enters the worktree** — matches the instruction's named tool literally, and puts the manager where
  the diff is. Against it: the manager would be writing the graph from inside a worktree, and the graph is the main
  tree's.
- **The worker is spawned with harness worktree isolation** — puts the harness-managed tree around the party that
  actually writes, and the checker is pointed at the path afterwards. Against it: it is not the tool the human named,
  and the manager has not established that such a tree survives the worker's exit in the way the gate needs.

**What this node decides:** which route the effort uses, and consequently what the map's landing policy says the
manager does when an implementation node starts.

## The manager's note at filing

*Not a change to anything above.*

**The instruction itself is not in question and is already in force**, written into `map.md` beside the landing policy
under [Rules added to one effort's map, and what makes them legitimate](93-effort-scoped-custom-rules.md). This node
is the fit, not the direction.

**What produced it**, recorded because it is the evidence either route has to beat: the manager created node 147's
worktree with `git worktree add` and then could not remove it. The sandbox bind-mounts `.git/config` read-only and
makes `.git/worktrees/<name>` its own mountpoint, so both `git worktree remove` and `git worktree prune` returned
`EBUSY`. The entry stayed in `git worktree list` as `prunable`, and **this effort discovers a code slot's occupancy
by counting live worktrees**, so a stale entry reads as an occupied slot. It was cleared only by re-running the prune
outside the sandbox.

## Interview

### Attempt 1

*The attempt's routing key is held in the manager's session and does not survive it. Banked at hand-back, before
being relayed.*

**The worker's question, pasted as it wrote it.**

> **ASK:** Do we take the isolated-worker route — the harness makes the worktree when the manager spawns the worker,
> and the manager points the checker and every later correction round at that same path — and will you set
> `worktree.baseRef` to `head` so it is cut from where the manager actually is?
>
> **RECOMMENDED:** Yes to both. Everything the gate needs is measured to work on this route: the tree outlives its
> worker, a second agent can read it, the harness hands the manager the path and branch automatically when the worker
> finishes, and the manager can remove it at the end. It is also the only route that costs you nothing per node — the
> manager sets nothing up and cleans nothing up in the ordinary case.
>
> The setting is not optional and not a matter of taste. Without it every implementation node on this effort starts
> from a snapshot that gets staler with every commit the manager makes, which is one node's work already lost. It is
> the same setting whichever route wins, so it is not me smuggling a second decision in — it is the condition that
> makes any of them work. If you would rather scope it to this repo than to your whole machine, that is a project
> settings file rather than your global one, and either is fine by me.
>
> What this route costs, named rather than hidden: the worktree is named after the agent, not after the node, so `git
> worktree list` will show you `agent-ac549d7fb8ff2bf22` instead of something readable. The manager gets the path
> handed to it mechanically and the gate always names it, so nothing breaks — it is just uglier to look at than the
> current `.worktrees/140-move-the-map/`.
>
> **ALTERNATIVES:**
> - The manager creates the worktree with `EnterWorktree`, steps straight back out keeping it, and points the worker
>   at it. This is the tool you actually named, and it keeps the node's number in the path and the branch name. I did
>   not recommend it because I could not test any of it — subagents are barred from that tool, so I have no evidence
>   it works, and it needs the same setting anyway.
> - The manager enters the worktree and works from inside it. Ruled out above.
> - The worker calls `EnterWorktree` itself. Measured and impossible.

**The six measurements it rests on**, pasted as the worker wrote them:

> 1. A worker spawned with harness worktree isolation gets a real git worktree at `.claude/worktrees/agent-<id>` on a
>    branch `worktree-agent-<id>`.
> 2. **The tree survives the worker's exit.** This was the manager's stated unknown and it is now settled twice over:
>    my probe agent wrote a file, exited, and its tree was still there; and I — a different agent entirely — just read
>    the running node's tree from the main checkout and got back exactly its five changed paths, uncommitted. The
>    worktree also unlocks itself when its worker exits, so the manager can remove it afterwards. A worker that
>    changed nothing has its tree swept away automatically, which is the one thing the harness route does better than
>    doing it by hand.
> 3. `git worktree remove` on it worked fine from inside the manager's sandbox.
> 4. **And so did doing it by hand.** I created a hand-rolled worktree the old way and removed it in the same breath —
>    no error. So the removal failure that prompted your instruction does not reproduce today, on either route. Your
>    instruction still stands; I am only reporting that the specific breakage is not what separates the two routes.
> 5. **The base is wrong, and this is the real problem.** Every harness worktree is cut from `origin/master` — the
>    last thing pushed — not from where the manager is standing. This effort never pushes, so that point is frozen
>    forever while the manager's own branch runs ahead of it; it was fifteen commits ahead when I measured. The
>    running node was cut from a `map.md` 1.5 KB out of date and is being redone. This is a single harness setting,
>    `worktree.baseRef`, which has exactly two values, `fresh` (today's default) and `head`. It is in your settings,
>    and I have deliberately not touched it.
> 6. **The route where the worker calls the tool itself is not available** — I tried it and the harness refuses
>    outright: a subagent cannot create a worktree. That removes one option before you have to think about it.

**Two things it settled itself**, in its words, coming back as flags at resolution:

> that the manager entering the worktree is out (it would be writing the graph from inside a branch that is not
> master, and it can only be inside one at a time, which would freeze the number of parallel implementation nodes at
> one permanently); and that the harness worktree directory needs a line in `.gitignore`, which it currently lacks —
> it shows up as untracked clutter and makes every repo-wide search return two copies of every file.

***The manager's note.*** **Measurement 4 contradicts what the manager recorded on this node**, and both stand. The
manager's own attempt to remove a hand-rolled worktree failed with `EBUSY` on `.git/worktrees/147-absolute-paths` and
on `.git/config`, and `/proc/mounts` showed both as sandbox bind mounts, `.git/config` read-only; it succeeded only
outside the sandbox. The worker reports the failure not reproducing today on either route. The manager has not
reconciled the two and neither is withdrawn.

**Measurement 5's *fifteen commits* is the worker's count at its own measuring time** and is not the manager's; the
manager measured six at the point node 140's tree was cut. Both are counts of the same gap taken at different
moments.

**The `.gitignore` gap is confirmed by the manager**: `git check-ignore` reports `.claude/worktrees/` not ignored, and
`git status` shows the running node's tree as untracked. The manager has changed nothing, that being a tracked file
outside the graph and this node's subject.

**A later message from the same attempt, pasted**, which the manager records because it partly reconciles the
contradiction noted above:

> No human answer has arrived — that was a background command of mine completing. It added nothing that changes the
> question (only a minor detail: the harness maintains `extensions.worktreeConfig` in `.git/config`, which the
> sandbox mounts read-only, producing a harmless warning on branch deletion; every operation I ran still succeeded).

***The manager's note.*** **This corroborates the mechanism the manager measured and not its severity.** Both agree
the sandbox mounts `.git/config` read-only; they differ on whether the resulting failure is fatal. The manager's
attempt could not remove the worktree at all until it ran outside the sandbox; this worker's produced a warning and
succeeded. Neither observation is withdrawn.

**The human's answer**, `verbatim`:

> 150 -> yes to what you said except this: I don't understand the point of "and will you set worktree.baseRef to
> head" -> doesn't it do that by default when creating a worktree, taking whereever the tree already is?

**The option the first half takes, in the worker's own words** — quoted because the reply is unreadable without it:

> **the isolated-worker route** — the harness makes the worktree when the manager spawns the worker, and the manager
> points the checker and every later correction round at that same path.

***The manager's note.*** **The reply is half an answer and half a question about the second half's premise.** The
route is settled: the isolated-worker route, accepted. **The `worktree.baseRef` half is not settled and was not
treated as settled** — the human questions whether the setting is needed at all, believing the default already cuts
from where the tree stands. Under the rule that the worker holds the interview and the manager holds the channel, the
premise question was **put back to the worker** rather than answered by the manager, and the manager separately
reported to the human the measurement it already holds, which is evidence rather than an answer:

- Node 140's harness worktree was cut at `c3d50bf`. `git rev-parse origin/master` is also `c3d50bf`. Local `master`
  was six commits ahead at that moment.
- The consequence was measured on the file itself: node 140's `map.md` was 31,481 bytes where the live one was
  33,007 — 1,526 bytes stale — and its work did not rebase.
- Independently, the harness's own documentation of the worktree tool states that the base ref is governed by
  `worktree.baseRef`, *"`fresh` (default) branches from `origin/<default-branch>`; `head` branches from your current
  local HEAD."*

Measurement and documentation agree, and both say the default is **not** where the tree already is.
