# Which harness route creates an implementation node's worktree

Type: grilling
Status: resolved

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

## Answer

*The worker's own text, pasted.*

**An implementation node's worktree is created by the harness around the *worker*, at the moment the manager spawns
it — the worker is spawned with the harness's worktree isolation, and the manager stays in the main tree throughout.
The harness's base-ref setting `worktree.baseRef` is set to `head`, so the tree is cut from the manager's current
`HEAD` rather than from the last pushed commit.** The human's words settling the route, `verbatim`: *"150 -> yes to
what you said except this"*, against the recommendation named below; and settling the base ref, `verbatim`: *"150
alright good for baseRef to head then of course"*. No divergence on either.

### What the landing policy now does when an implementation node starts

The manager **spawns the worker with worktree isolation and creates nothing itself.** It does not choose the path and
does not choose the branch name; the harness picks both, and the manager learns them from the worker's completion
notification, which carries them mechanically. Everything downstream is unchanged from what [Run an implementation
node's work in a worktree](68-implementation-in-a-worktree.md) fixed: the changes stay uncommitted through the checker
and the gate, the gate payload names the worktree's path and the command that shows its diff, and on approval the
manager commits path-limited, rebases onto the branch the manager thread is on, re-runs the bar, `--ff-only` merges,
then removes the worktree and deletes the branch.

Three clauses of the old policy are replaced by what the harness does instead:

- **The path.** Was `.worktrees/NN-<name>/`. Is now `.claude/worktrees/agent-<agentId>/`, still inside the
  repository. It is **not** ignored today, which is the node surfaced below.
- **The branch.** Was a name carrying the node's id. Is now `worktree-agent-<agentId>`. **The join key is
  unaffected** — [Git and code-landing policy](11-git-and-code-landing.md)'s `Node: <effort>/<NN>` trailer is written
  by the manager into the commit, not by the branch name — so what is lost is only the legibility of `git worktree
  list` to a human reading it cold.
- **The base.** Was `git worktree add … HEAD`. Is now the harness's, governed by `worktree.baseRef`.

**Occupancy still counts.** One live worktree per claimed implementation node, exactly as before. What is no longer
discoverable from the path is *which* node a given worktree belongs to; the manager holds that from the spawn and
again from the completion notification.

### The base-ref setting, and the one thing left for the human

`worktree.baseRef` has exactly two values: `fresh`, the default, meaning `origin/<default-branch>`, and `head`,
meaning the current local `HEAD`. It is set to `head`. **Whether that is written into the human's user settings or
into this repository's `.claude/settings.json` is not settled and nothing here turns on it** — the answer holds under
either, and the human's later word fills it. The manager may not write the project file from inside its sandbox, so
the write itself is theirs or is made with the sandbox off.

**One cheap verification is owed, because the setting was not in force when this was measured.** On the first
implementation node spawned after the change, the manager reads `.git/worktrees/<name>/CLAUDE_BASE` — the harness
records its own chosen base there — or runs `git -C <worktree> rev-parse HEAD`, and confirms it equals the manager's
`HEAD`. One command, once.

### Correction rounds must not re-isolate

**A second spawn with worktree isolation creates a second, empty worktree at a fresh base and strands the first one's
work.** So a correction round **resumes** the worker, per this map's standing rule that an agent is resumed wherever
it can be resumed; a resumed worker returns to its own tree. Where resume is unavailable — the manager's session
having ended — the replacement is spawned with its working directory set to the surviving path rather than with
isolation. The harness names this route itself, in the refusal quoted below: *"To work in a different directory
(including a worktree), spawn an Agent with `cwd` set to it."* Flagged, being unverified.

### What was measured, and what it replaces

Everything below was measured on this tree today, with three throwaway probe agents and the live tree of node 140.
**None of it was taken from the record**, and two things the record asserted did not survive contact.

1. **A harness-isolated worker's tree survives its worker's exit.** Settled twice: a probe agent wrote a file,
   exited, and its tree remained; and, independently, node 140's own worktree was read *by this worker* — a different
   agent entirely — from the main checkout, returning exactly its five changed paths, uncommitted. **The span the
   gate needs is therefore real**: worker finishes → tree persists → a separate agent reads it → the human reviews
   it.
2. **The tree unlocks itself at its worker's exit.** While the worker runs, the worktree is `locked` with a reason
   naming the agent id and pid; afterwards the lock is gone, so nothing blocks the manager's removal.
3. **A worker that changed nothing has its tree removed automatically**, checkout and admin directory both, from
   inside the manager's sandbox. This is the one thing the harness route does that the hand route does not, and it is
   what makes a dead or no-op worker leave no stale slot.
4. **The completion notification carries the path and the branch** when a tree survives, and carries no such block
   when the harness swept one — so the manager learns a path exactly when there is a path to learn.
5. **The base was wrong under the default, and by a growing margin.** A probe spawned with isolation was cut at
   `c3d50bf`, which is `origin/master`; local `master` was `80260a3`, **22 commits ahead**. The gap was 15 an hour
   earlier. Since this effort never pushes — the one clause of node 11's git policy that has survived every revision
   — `origin/master` is frozen and the gap only grows. This is what stranded node 140, whose `map.md` was 1,526 bytes
   stale and whose work did not rebase.
6. **The difference is the harness's, not git's.** In the same minute, `git worktree add` with no ref given was cut
   at `80260a3` — the current `HEAD`, exactly as expected. The human's premise was right about git and wrong only
   about the harness, which is why the setting is a correction rather than an imposition.
7. **`git worktree remove --force` succeeds from inside the manager's sandbox**, on both a harness tree and a
   hand-rolled one. `git branch -D` succeeds with a warning that `.git/config` is read-only, the harness maintaining
   `extensions.worktreeConfig` there.
8. **The `EBUSY` failure that produced the human's instruction does not reproduce.** It is recorded as measured fact
   in two places — node 68's annotation section 2 and this node's own filing note — and today `/proc/mounts` shows
   `.git/worktrees` mounted but no per-worktree mountpoint, and both removals return 0. **The instruction stands on
   the human's word and not on this ground**; it is recorded here so no later reader rests an argument on a failure
   that is no longer observable.

### The three routes not taken

- **The manager enters the worktree.** Refused. It would write the graph — every node file, `decisions.md`,
  `flags.md` — from inside a branch that is not `master`, and a session can be in one worktree at a time, which would
  freeze the code-slot count at one permanently rather than leaving it the settable number node 68 made it. Settled
  by this worker; flagged.
- **The worker calls `EnterWorktree` itself.** Not available. Measured: the harness refuses a subagent outright —
  *"EnterWorktree cannot create a worktree from a subagent with a cwd override … it would mutate the parent session's
  process-wide working directory."*
- **The manager creates the tree with `EnterWorktree`, steps back out keeping it, and points the worker at it with
  `cwd`.** A real route, and the only one that would keep the node's id in the path and the branch. Set aside because
  none of it could be verified from inside a subagent, it needs the same base-ref setting anyway, and the one thing
  it buys — a readable `git worktree list` — is already served by the gate payload naming the path. **Recorded rather
  than closed**: it is the remedy available if the agent-id naming turns out to hurt.

### What this changes about what the workflow ships: nothing

No shipped file mentions a worktree at all — `grep -rn worktree .claude/skills/` returns nothing — and the lifecycle
lives only in `map.md`. Under [Rules added to one effort's map, and what makes them
legitimate](93-effort-scoped-custom-rules.md) the human declared no shipping scope for the harness-worktree
instruction, so **it binds this effort's map and no shipped file.**

**One consequence for an open node, stated because it is not obvious.** [Carry the worktree lifecycle into the
manager's contract](89-carry-worktree-lifecycle-into-managers-contract.md) is blocked on *"whether the lifecycle is a
rule of the workflow or a practice of one effort"*. This answer does not unblock it and makes it harder in a way
worth naming: the effort's practice is now **harness-specific**, and ground rule 1 forbids a shipped file assuming a
harness. So whatever that node ships cannot be what this effort now does, and the divergence is now a fact rather
than a risk.


## Flags

*Each entry is the worker's own prose, pasted. The manager added the id and the marker and nothing else.*

`150.1` `ASSUMPTION` — **The manager entering the worktree was eliminated by this worker rather than put to the human.** Both of its costs are facts rather than preferences: the manager writes the graph to the main tree, so it would be writing every node file, `decisions.md` and `flags.md` from inside a branch that is not `master`; and a session occupies one worktree at a time, so the route would cap the code-slot count at one permanently, undoing the settable count node 68 established. I judged these dispositive and spent the human's one question on the route that remained.

`150.2` `ASSUMPTION` — **`.claude/worktrees/` needs a `.gitignore` entry, and I settled that rather than asking.** Measured: `git status --short` in the main tree shows `?? .claude/worktrees/`, and a repo-wide search traverses it and returns a second copy of every graph file. The manager reports the same pollution reaching its own context — all seven `expedition*` skills surfaced a second time, scoped to the live worktree path. The landing policy already requires worktrees inside the repository to be ignored; the harness moved the directory and the ignore rule did not follow. I treated this as a defect to repair rather than a choice to offer.

`150.3` `ASSUMPTION` — **A correction round after an unresumable worker is spawned with its working directory set to the surviving worktree, not with worktree isolation.** Isolation demonstrably creates a fresh tree at a fresh base, which would strand the work; the harness's own refusal message names the `cwd` route as the alternative. **I could not verify it** — a subagent cannot set a child's working directory — so this rests on the harness's documentation of itself plus the measured behaviour of isolation, and the manager should confirm it the first time it is needed rather than at the moment it is needed.

`150.4` `ASSUMPTION` — **The `head` half of the base-ref setting is documented, not measured.** Every measurement in this answer was taken with the setting at its `fresh` default; I could not change the harness's configuration and did not try. That `head` cuts from local `HEAD` rests on the harness's own statement of the setting and on the two values it exposes. This is why the answer carries a one-command verification duty on the first implementation node spawned after the change.

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

**The worker's second question, pasted as it wrote it.** Same attempt; put after the human questioned the premise of
the first question's second half, and after the manager asked it to demonstrate rather than assert.

> **You are right, and it is right about `git`.** A plain `git worktree add` with no ref given does exactly what you
> describe — branches from wherever you are standing. I just ran it: it landed on `80260a3`, which is the tip of
> `master` this minute. That is almost certainly where the belief comes from, and it is correct.
>
> **The harness does not do that.** In the same minute, on the same tree, I spawned a throwaway probe agent with
> worktree isolation. It reported its own base as `c3d50bf` — `origin/master`, the last thing anyone pushed, **22
> commits behind** where the manager is standing. I saw the same thing from the main tree in `git worktree list`, and
> the harness writes its own choice into a file inside the worktree, which also says `c3d50bf`. So: three
> observations, one conclusion, all from today's tree rather than from the failed node's history.
>
> Two worktrees, same repo, same minute:
>
>     git worktree add  (by hand)  ->  80260a3   = local master, where you are
>     harness isolation (a worker) ->  c3d50bf   = origin/master, 22 behind
>
> **Why it doesn't self-correct.** This effort never pushes — that is the one git rule from the original landing
> policy that has survived every revision. So `origin/master` is frozen at whatever was last pushed, and the gap only
> ever grows: it was 15 commits when I first measured it an hour ago, and 22 now. Every implementation node would
> start further behind than the last.
>
> The harness documents this as a setting with exactly two values — `fresh`, the default, meaning
> `origin/<default-branch>`, and `head`, meaning where you actually are. The default is the odd one; the setting just
> asks the harness to behave the way plain `git` already does.
>
> **ASK:** Given that — plain `git` does branch from HEAD, but the harness measurably does not and is 22 commits
> behind today — will you set `worktree.baseRef` to `head`?
>
> **RECOMMENDED:** Yes. It is one line, and it makes the harness match the behaviour you already expected it to have.
> Without it the landing policy's rebase step is doing real work on every single node instead of absorbing your
> occasional graph commits, which is what it was designed for — and node 140 is what that looks like when it fails.
>
> Your global settings or this project's, whichever you prefer. Project-scoped keeps it off your other repos and
> travels with this one; I have not touched either.
>
> **ALTERNATIVES:**
> - Leave it at `fresh` and change the landing policy to say worktrees are cut from `origin/<default-branch>`.
>   Honest, but it makes every node's rebase a real merge across a gap that never stops growing, and I would not
>   recommend it.
> - Push `master` before each implementation node so `origin/master` keeps up. This works, but it breaks "nothing is
>   ever pushed", which you have held to since the beginning.

***The manager's note.*** **The worker withdrew nothing and was told it could.** The manager's resume offered it the
withdrawal explicitly — *"If your probe shows the default does cut from local `HEAD` on this machine today, say that
plainly and withdraw the request"* — and the probe went the other way. The human's belief is confirmed correct about
plain `git` and refuted about the harness, both in one observation on today's tree.

**The human's answer to the second question**, `verbatim`:

> 150 alright good for baseRef to head then of course

***The manager's note.*** **Not a divergence**: the answer takes the worker's recommendation, and it followed a probe
run at the manager's request that confirmed the human's belief about plain `git` and refuted it about the harness.
**The scope was offered and not named.** The worker put it as *"Your global settings or this project's, whichever you
prefer"*, and the reply chooses neither. The manager has **not** picked one and has **not** written the setting: the
project's `.claude/settings.json` is outside what the manager may write in its sandbox, and having already acted once
today on its own authority in breach of its contract (flag `140.8`), it is putting the scope and the write to the
human rather than deciding either.

## The worker reissued its handover, and this is what changed

*Filed by the manager. The answer above is **not** withdrawn and stands where it is under the never-delete rule; the
sections below supersede the parts they name. The reissue followed the manager relaying the human's question —
whether the base could be passed as an argument rather than being a setting — together with the fact, taken from the
two tool definitions, that it cannot. **The worker folded that in and it changed the shape of the base-ref half.**
Its own text, pasted.*

**The answer's opening gains a third sentence:**

> Because that base is a property of the environment and cannot be passed per call, the manager verifies it at every
> implementation node's spawn rather than trusting it.

### The base is a property of the environment, not of the spawn

> **It cannot be passed per call on either route.** `EnterWorktree` takes `name` or `path` and nothing else;
> `Agent`'s `isolation` is an enum of `worktree` and `remote` and carries no base. The only control is the setting
> `worktree.baseRef`, whose two values are `fresh` — the default, meaning `origin/<default-branch>` — and `head`.
> Three things follow, and each is a real cost rather than a technicality.
>
> **1. It cannot vary per node.** Every implementation node on this effort gets whatever the setting says. No node
> has a route to a different base, so a node that needed one — rebuilding on a rejected node's branch, say — cannot
> have it by this route at all; it would need a hand-made worktree and a worker pointed at it, which the standing
> instruction forbids. **No node needs that today**, and it is recorded as a known limit rather than a problem to
> solve now.
>
> **2. It does not travel, and under ground rule 1 it must not be relied on to.** The workflow is for repositories
> this machine has never seen, and *nothing shipped may assume this machine or a toolchain*. A value in a config file
> on one laptop is exactly that assumption. So **the shipped landing policy may not depend on `worktree.baseRef`
> being `head`.** The rule's own remedy is the answer: *prefer properties that are discovered over commands that are
> declared.* A line in the starting-an-effort procedure is the wrong instrument — a procedure step can be skipped,
> and this one would be skipped silently — where a check cannot be. So a fresh repository does not *learn* the
> setting; the manager **observes the base it actually got** and acts on what it sees.
>
> **3. Unset, it fails silently, and today that is exactly how it failed.** Nothing announces a stale base. It
> surfaced only when a node's work would not rebase, after the work was done. So the landing policy gains one
> standing step, and it is one observation:
>
> ```
> manager spawns the worker with worktree isolation
>     → manager immediately reads the base the harness chose:
>           cat .git/worktrees/<name>/CLAUDE_BASE     (the harness records it there)
>           — or —  git -C <worktree> rev-parse HEAD
>     → equal to the manager's HEAD at spawn  → proceed
>     → not equal                            → TaskStop the worker, remove the worktree,
>                                              and raise it to the human
> ```
>
> **The repair is to start over, not to fix the tree in place**, and that is the part worth being precise about.
> Resetting a stale worktree onto the right base moves the branch pointer and leaves the working tree holding the
> *old* content of every file the worker has not touched. That is not a near-miss: node 140 was moving text verbatim
> between files, so a late reset would have carried pre-repair text forward and silently undone [node
> 147](147-graph-records-name-absolute-paths-on-a-machine.md)'s landed work while every check passed. **A wrong base
> is cheap to discard in the first seconds and expensive to discover at the gate.** Stopping a worker is available to
> the manager and leaves it resumable, per [What can actually stop a running worker](122-what-can-stop-a-running-worker.md).
>
> Whether the setting lives in the human's user settings or in this repository's `.claude/settings.json` is not
> settled, and nothing here turns on it — no such file exists in this project yet, so it is a creation rather than an
> edit, and the human has not named a scope. The answer holds under either, **and the check above holds even if
> neither is written.**

**Its index line changed with it**, from *"and `worktree.baseRef` becomes `head`"* to:

> The isolated-worker route carries the harness-worktree rule: the harness cuts the tree at spawn, the manager owns
> the path from the completion notification, and verifies the base it got.

**Its map edit gains a fifth item**, in its words: *"(4) **the standing base check joins the lifecycle** as the first
step after the spawn, with its stop-and-restart repair and its reason"*, and the surfaced map-edit condition gains
*"that the manager observes the base the worktree actually got before the work proceeds and stops the worker rather
than repairing the tree when it is not the manager's `HEAD`"*.

**What it now gives node 115**, superseding the earlier sentence: *"It landed `head`, plus a check that the base
actually is `head`. So a worker's tree is a true snapshot of the manager's `HEAD` at the instant of spawn — and,
unlike a setting taken on trust, that is now observed rather than assumed."*

***The manager's note.*** **This is operative for the manager immediately, ahead of any map edit.** The next
implementation node spawned gets the base check as its first step after the spawn, and the manager records that here
rather than only in the map, the map edit being held behind node 140's landing under [node
115](115-two-writers-edit-the-map-at-once.md)'s not-yet-settled rule.

`150.5` `ASSUMPTION` — *The worker's own prose, pasted.* **The manager verifies the base at every spawn, and a wrong
base stops the worker rather than being repaired in place.** The human settled the setting, not the failure
procedure. I chose verification over trust because the setting cannot be passed per call, does not travel to another
machine, and announces nothing when absent; and I chose stop-and-restart over resetting the tree because a base
corrected after a worker has read the tree leaves it holding pre-repair content, which on node 140 would have
silently reverted node 147's landed work with every check passing.

## Revision: the human named a fourth route, and it is measured to work

*Filed by the manager after this node resolved. **The answer above is superseded on the route and stands on
everything else**, per the never-delete rule.*

~~**An implementation node's worktree is created by the harness around the *worker*, at the moment the manager spawns
it — the worker is spawned with the harness's worktree isolation**~~ — **superseded.** The human named the route this
node's worker had set aside as unverifiable, and gave it in two steps, `verbatim`:

> Here's what I expect from an agent that needs to start a worktree for an implementation:
> 1. It calls EnterWorktree specifying a name tied to the node and vaguely describing the node's title
> 2. If it didn't land on HEAD (but e.g. landed on origin/master because of the user's config) it does `git reset`
> itself to reach the proper base
>
> So I don't see why you're blkocked on worktree.baseRef: we just established we don't need it.?

**The manager tested it rather than reasoning about it, subagents being barred from `EnterWorktree`.** Three
measurements, on this tree:

1. `EnterWorktree` with a name landed the worktree at `c3d50bf` — `origin/master`, **32 commits behind** `master`.
   So it takes the same `worktree.baseRef` default as the isolation route, and step 2 is what the route turns on.
2. `git reset --hard master` **inside the manager's sandbox failed**: `fatal: Could not reset index file to revision
   'master'`. It applied partially — working-tree files updated, `HEAD` unmoved, `.claude/skills/expedition/graph-conventions.md`
   not written. Same class of restriction as the merge failure recorded on [node
   140](140-move-the-implementers-and-checkers-material-out-of-the-map.md).
3. **Outside the sandbox it succeeded**: `HEAD` at `master`, zero commits behind, working tree clean.

**Why this beats what this node landed.** It needs no setting, so it assumes no machine and satisfies ground rule 1
where the setting could not. It puts the node's id back in the path and the branch, which this node's answer had
given up. And **the reset happens before any worker reads the tree**, which is precisely the case this node's own
objection to resetting did not reach — that objection was about resetting *after* a worker has read it, and it still
stands in that form.

**What is still unverified, and the manager says so rather than assuming it.** Whether a worker spawned while the
manager is inside the worktree inherits that working directory. The manager observed, from inside, that its own
`Bash` refused a command targeting the shared checkout — *"a worktree-isolated session's git operations must target
its own worktree"* — which is evidence that the isolation is real, but is not the spawn test. **It is the first thing
the manager checks on the next implementation node**, and until it is checked, flag `150.3`'s status is unchanged.

**Flags `150.1`, `150.4` and `150.5` are reached.** `150.1`'s elimination of *the manager enters the worktree* was
about the manager **working** from one; entering transiently to create and reset, then leaving, is not that, and the
manager did exactly it here and returned. `150.4`'s and `150.5`'s subject — the `worktree.baseRef` setting — is no
longer load-bearing under this route; the base check survives, because a reset that does not happen is a stale base
either way. **None is withdrawn**: they were correct about the route this node answered on.
