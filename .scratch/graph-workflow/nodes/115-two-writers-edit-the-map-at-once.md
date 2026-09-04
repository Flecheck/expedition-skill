# Two writers edit the map at once when an implementation node's work is a map change

Type: grilling
Status: claimed

## Question

*Surfaced by [Carry the pick-report settling moment into the shipped files and the
map](103-carry-the-pick-report-settling-moment.md)'s worker, and pasted as it wrote it.*

> `.scratch/` is tracked, so an implementation node whose own work includes editing `map.md` edits the copy in its
> worktree — which is the last commit's — while the manager goes on editing the live copy in the main checkout,
> uncommitted. At node 103 the two had diverged in four places before the worker began. Two policy lines then pull
> against each other: the landing policy says the graph's files are *not* committed per node but periodically by the
> human, and it also says the manager makes one path-limited commit of that node's paths and merges `--ff-only` —
> which cannot run over a tracked path the main checkout has dirty. So what should happen: does such a node's map
> text travel back as text for the manager to apply, does the manager commit the graph before creating the worktree,
> is the map excluded from the worker's tree entirely, or something else?

**Blockers, in the worker's words:** *"none. Node 103's own map edit is affected and its gate is the first place the
collision bites."*

## The manager's note at filing

*Not a change to anything above.*

**The manager has already acted on this for node 103 alone, and that act is not an answer to this node.** It took the
worker's map and `map-history.md` text out of the worktree, applied it verbatim to the live copies in the main
checkout, and reverted the worktree's `.scratch/` — so node 103's commit carries its four shipped files only. Recorded
as flag `103.5`. **The route it took is the first of the four this question offers**, chosen because it was the only
one that needed no decision the manager is not entitled to make: the two files are the graph's own and the manager is
their only writer, so pasting a worker's text into them is scribe work. It is a one-node disposition and this node
decides the rule.

**One consequence the manager accepted and this node should weigh.** Under that route, **place 5 of node 103's
acceptance condition cannot be established in the tree its checker sees** — and the checker is blind to `.scratch/`
regardless, so it could never have established it. That is a second, sharper form of the collision: a condition may
name a place its own checker is forbidden to look at. Whether an acceptance condition may demand a change to the
effort's record at all is not something the four routes above settle.

## Interview

### Attempt 1

*The attempt's routing key is held in the manager's session and does not survive it. Banked at hand-back, before
being relayed: this question queues behind node 150's, which was live when it arrived.*

**The worker's question, pasted as it wrote it.**

> **ASK:** Do we prevent the collision instead of recovering from it, with one rule — **while an implementation node
> is claimed, the manager writes none of the files that node's acceptance condition names, banking any such write on
> the node that produced it and applying it after the work merges** — with the worker keeping its worktree and
> writing the map itself as it does today?
>
> **RECOMMENDED:** Yes. It is one sentence, it needs no new machinery, and it is decidable mechanically: the
> condition lists its paths and is written before the claim, so there is never a judgement call about whether the
> rule is on.
>
> It fits both incidents exactly. Node 140's loss was me writing `map.md` while node 140 held it. Node 129's fog
> items are you and I already doing this rule by hand, as a one-off — this makes the one-off the practice.
>
> It is nearly free, and that is measured rather than hoped: one deferral in thirty commits.
>
> Two things you should weigh before saying yes:
>
> - **It has a contingency on node 150, the question in front of you now.** Committing the graph before the worktree
>   is cut only makes the base current if the cut comes from where I am standing. If node 150 lands `fresh` —
>   cutting from the last pushed commit, which on this effort is frozen forever — the base is stale before the node
>   begins and no rule of mine repairs it. Parts of this answer stand either way; that part does not.
> - **It delays one thing by up to a node's duration:** a standing rule you state mid-node reaches the map only
>   after that node lands. I do not think that costs you anything, because the map already works this way in one
>   place — the rule from node 96 is written as "binding this effort from now whether or not that node has landed" —
>   and I would carry your words into any spawn as yours in the meantime. But it does sit against node 93's wording,
>   "a standing rule binds this effort only once it is written here," and I would be narrowing that.
>
> **ALTERNATIVES:**
> - **The worker hands its map text back and I paste it into the live copy** (what I did at node 103). Sets aside: it
>   makes me re-author the work, it reverses a carve-out already shipped in all eight contract files — that a worker
>   whose own work *is* a graph file makes that change itself — and every hand-application is a place a paraphrase
>   enters the record silently.
> - **Keep the record out of the worktree entirely**, via a sparse checkout that drops `.scratch/`. Sets aside: it
>   fixes the *ordinary* node, which was never the problem, and does nothing for a node whose work *is* the map,
>   which is this question. It has real side benefits though — it would end the duplicate-skills pollution I am
>   seeing right now — so I would rather it were its own node than folded in here.
> - **Stop tracking `.scratch/` in git.** One writer, problem gone. Sets aside: it destroys the record's history and
>   takes the graph out of the diff, and reviewing diffs is one of your two interfaces.
> - **Change nothing; the landing policy already covers it** — a rebase conflict aborts and the node takes a
>   correction round with the worker respawned. That rule did fire, and node 140 is what it costs: a whole node
>   replayed. It is a recovery, and it is the expensive one.

**The four things it measured rather than assumed**, pasted as it wrote them:

> - `git merge --ff-only` **refuses outright** over a tracked path dirty in the main checkout — reproduced in a
>   scratch repo: `error: Your local changes to the following files would be overwritten by merge: map.md`.
> - Across the manager's last 30 graph-state commits, the non-`nodes/` files touched are `flags.md` ×13,
>   `decisions.md` ×5, `map.md` **×1** — and that one is `9c06955`, the commit that cost node 140 its first pass.
> - The checker's contract, given 5: the ground rules are copied into its spawn because they live in "the effort's
>   map, **which every other worker reads and you do not**". Node 140 is at its checker right now with a 14-clause
>   condition made almost entirely of `map.md` facts.
> - `.gitignore` covers `.worktrees/` but not `.claude/worktrees/`; the live harness worktree is surfacing a
>   duplicate copy of all seven expedition skills into every agent's skill list.

> **The landing policy is stale on its own face.** It says the graph's files "are *not* committed per node; they are
> committed periodically by the human." My git log says otherwise: nearly every commit is a `Graph state:` commit of
> mine, several per node. That sentence should go, whatever you decide here.

***The manager's note.*** **The duplicate-skills finding is confirmed live and now reaches the manager's own
context**: the harness surfaced all seven `expedition*` skills a second time, scoped to
`.claude/worktrees/agent-ac549d7fb8ff2bf22/`, in the manager's own skill list. The manager has changed nothing —
`.gitignore` is a tracked file outside the graph, and having already acted once today on its own authority in breach
of its contract (flag `140.8`), it is not doing so again.

**The human's answer**, `verbatim`:

> 115 -> Don't prevent writes, resolving merge conflicts when integrating the implementor's worktree is fine. This
> ultimately allows parallelizing implementations as well, and that and resolving potential merge conflicts will
> still lead to faster implementations than what's basically a mutex. Ultimately to minimize merge conflicts we
> should limit implementation parallelization, and favor paralellization on nodes that have little chance of
> conflicting with one another - but the framework should allow user to tell the manager to increase
> parallelization, at the expanse of odds of having to resolve merge conflicts.

**`DIVERGENCE`.** The recommendation was to prevent the collision — *"while an implementation node is claimed, the
manager writes none of the files that node's acceptance condition names"*. The human refuses prevention and takes
recovery, on a ground the worker did not weigh: that the rule is **a mutex**, and that a mutex costs more throughput
than conflicts cost to resolve.

***The manager's note.*** **The answer reaches further than the question did, and the manager records what it reaches
rather than deciding any of it.** Three things follow that the worker must now carry:

1. **It reverses a landing-policy rule.** That policy says *"A rebase conflict is resolved by nobody in the moment:
   the manager runs `git rebase --abort` and the node takes a correction round with the worker respawned."* If
   resolving conflicts on integration is fine, that rule no longer holds and **somebody has to be named** as the
   party who resolves one.
2. **It makes the code-slot count a control the human turns**, rather than a fixed setting: *"the framework should
   allow user to tell the manager to increase parallelization, at the expanse of odds of having to resolve merge
   conflicts."* The count already is a per-effort setting; what is new is that raising it is offered to the human as
   a trade with a named cost.
3. **It puts a scheduling heuristic on the manager's pick** — *"favor paralellization on nodes that have little
   chance of conflicting with one another"* — which is a new consideration in choosing what to start, and one nothing
   in the workflow currently states.

**The manager has run the refused rule by hand twice**, holding node 129's fog items and node 150's landing-policy
edit behind node 140, and both landings rebased clean. That is evidence the rule works, not that it was the right
trade, and the human has now priced the trade differently.
