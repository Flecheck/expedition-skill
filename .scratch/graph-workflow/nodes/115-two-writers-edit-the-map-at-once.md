# Two writers edit the map at once when an implementation node's work is a map change

Type: grilling
Status: resolved

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

## Answer

*The worker's own text, pasted.*

**The collision is not prevented. It is resolved when the work is integrated.** The human's answer is a `DIVERGENCE`
against this node's worker's recommendation of prevention.

**The ground is throughput, and it prices the thing this node's worker did not weigh.** The rule that was
recommended — the manager holding its writes to any file a claimed node's condition names — is a mutex. Its measured
cost was one deferral in thirty commits, but that measures how often it *fires*, not what it *forecloses*, and what
it forecloses is parallel implementation. Conflicts are the cheaper of the two.

### 1. What the landing policy now does on a conflict

The sentence that falls is **"A rebase conflict is resolved by nobody in the moment: the manager runs `git rebase
--abort` and the node takes a correction round with the worker respawned."** It is not deleted — struck in place
under the never-delete rule and kept for the one case where it was right. What replaces it splits by **what
conflicted**:

- **Text under the never-delete rule** — `map.md`, its siblings, node files — is resolved by the **manager**, by
  keeping both sides. Neither side deleted anything, so the union *is* the correct resolution. This does not breach
  the manager's scribe rule: its own contract names *"ordering pasted pieces, laying runs end to end"* as scribe
  work, and a union of two appends is exactly that. The manager reports the resolution; the work does not return to
  the checker or the gate, nothing having been authored.
- **Everything else, product code included**, is resolved by the **worker whose branch is being rebased** — the one
  party holding that change's intent, the other side being on `master` and readable. The manager runs the rebase,
  stops at the conflict, and resumes that worker to edit the conflicted files in place. The worker runs no git
  command: its contract forbids it to rewrite history, and that rule is untouched. The resolution is new work, so it
  returns to the checker and to the gate.
- **Two sides that genuinely contradict** — where keeping both would make the file assert two incompatible things —
  is not a merge problem and no resolution settles it. `git rebase --abort`, and a correction round. This is the old
  rule, narrowed to the case it actually described.

### 2. The slot count is a dial the human turns, and its price is stated

The count was already a per-effort setting; what is new is that the trade is offered rather than buried. Raising it
buys parallel implementation at the price of integration conflicts. The manager does not raise it on its own
judgement, does not treat the effort's current value as a ceiling it must justify leaving, and states the price when
the human moves it. This half is scoped to the shipped files by the human's own words — *"the framework should allow
user to tell the manager to increase parallelization"*.

### 3. What the manager weighs when it picks, and it is decidable rather than intuitive

When more than one code slot is free, the manager prefers candidates whose **acceptance conditions name disjoint sets
of paths**. A condition is already required to list its paths, so conflict likelihood is readable before either node
starts, at no cost and with no prediction.

### 4. What this settles that was open

The manager's contract carries, under `## What nothing here settles`, the question **"What does a worker do when a
file it must read is being changed by whoever holds the code slot?"** **This node answers it, and the answer was
already shipped without anyone noticing:** every worker reads a consistent snapshot. An implementation worker reads
its own tree, which its contract already calls *"yours alone for the whole of the node"*; every other worker reads
the main checkout, which no implementation worker writes. No worker ever reads a file mid-change. Divergence between
the two snapshots is not a reading problem at all — it is the integration, settled by section 1.

### 5. Two mechanisms measured on this node, recorded so they are not re-derived

- **`git merge --ff-only` refuses outright over a tracked path that is dirty in the main checkout**, reproduced in a
  scratch repository: `error: Your local changes to the following files would be overwritten by merge: map.md`. This
  is a *second* failure mode independent of the rebase conflict: an uncommitted graph edit blocks the landing step
  even when the rebase is clean. It is why the manager's graph state must be committed before a worktree is cut.
- **The manager's routine bookkeeping barely touches the map.** Across its last thirty `Graph state:` commits the
  non-node files touched are `flags.md` ×13, `decisions.md` ×5, and `map.md` ×1 — and that single one is commit
  `9c06955`, the commit that cost node 140 its first pass. **Recorded because it is the number that made prevention
  look cheap, and it is exactly the number that does not measure what prevention costs.**

### 6. What this does not settle

Whether an acceptance condition may demand facts about files the checker is told it does not read. The checker's
contract hands it the ground rules as copied text precisely because they live in *"the effort's map, which every
other worker reads and you do not"* — yet node 140 went to its checker with fourteen clauses about `map.md`.


## Flags

*Each entry is the worker's own prose, pasted. The manager added the id and the marker and nothing else.*

`115.1` `ASSUMPTION` — **Who resolves a conflict, which the human's answer did not name.** The human settled that conflicts are resolved at integration and named no resolver. I derived the three-way split in section 1 from rules already fixed rather than inventing one: the implementation contract forbids a worker to rewrite history, so the git operation stays the manager's; the manager's own contract names assembling pasted text as scribe work, which is what a union under the never-delete rule is; and the manager is barred from reading code to produce a note, so it cannot be the party resolving a code conflict. The one case none of those reaches — two sides asserting incompatible things — I left with the existing abort-and-correction-round.

`115.2` `ASSUMPTION` — **The conflict-aware pick heuristic is scoped to this effort, not to the shipped files.** The human's sentence contrasts *"we should limit implementation parallelization, and favor paralellization on nodes that have little chance of conflicting"* against *"but **the framework** should allow user to tell the manager to increase parallelization"*. Only the second names the framework. Under node 93 — a rule reaches a shipped file only where the human says so — I scoped the count-as-a-dial to the shipped files and the pick heuristic to this effort's map. The reading is defensible but it is a reading, and the two halves plainly belong together.

`115.3` `ASSUMPTION` — **A union resolution is reported, and every other resolution returns to the gate.** A conflict is resolved after the human has already approved the work, so the resolution is content nobody reviewed. I split it: a union of two appends authored nothing new and is reported at the next report; a resolution the worker wrote is new work and returns to the checker and to the gate. The alternative — re-gating every resolution — makes the union case cost as much as the thing it was chosen to avoid, and the human bought this rule for throughput.

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
