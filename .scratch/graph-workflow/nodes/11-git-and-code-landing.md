# Git and code-landing policy

Type: grilling
Status: resolved
Blocked by: 06

## Question

How does code produced by an implementation subagent land, and how is that recorded in git?

Settled inputs: one code-modifying subagent at a time in v1 (no worktrees); later, worktrees plus `git merge --ff-only` onto the manager's branch. This issue works out the rest.

- Branch layout: one branch for the whole effort, or a branch per implementation node?
- Does an implementation subagent **commit its own work**, or hand a diff back to the manager to commit?
- How is the single-writer lock actually expressed, given the manager is the only thing that spawns subagents — is it an explicit recorded lock, or an emergent property of the manager's scheduling?
- How does a **revision** land against code that already shipped — a new commit forward, or a rewrite of the earlier one? (Depends directly on [Revision semantics](06-revision-semantics.md).)
- Does the effort's history stay legible as a record of the route walked, or is it squashed at the end?

Added by [Node type taxonomy](07-node-type-taxonomy.md), which now also depends on this node:

- **Prototype artifacts live outside the product tree**, so a prototype never contends for the exclusive code slot. This was adopted on agent judgement rather than asked, and this node owns where things land, so it is the place to confirm or overturn it. If prototypes *do* land in the tracked tree, the concurrency consequence is immediate: a HITL prototype and an AFK implementation could no longer run at the same time.
- **Landing includes a review step.** An implementation node is not resolved until an independent read-only agent has checked it, so "how code lands" is now implement → review → possibly rework → land, with the code slot held throughout.

~~Prerequisite noticed while charting: **this directory is not yet a git repository.** Whatever this issue decides, `git init` has to happen before any implementation node can run.~~ **Superseded — the prerequisite is satisfied.** `graph-agent` is a git repository and all 19 graph files are tracked under commit `cf7e549 start`.

Added by [Dogfood target](09-dogfood-target.md), which changes which repository this node is about:

- **The code lands in Lang's repository, not this one.** The dogfood target is Lang (56 commits, active history, its own conventions). So whatever branch layout, commit authorship and locking this node decides has to work in a repo the workflow does not own and did not set up — one where the human commits by hand between agent sessions.
- **Two repositories are in play at once during the run**, and they change for different reasons: Lang's tree holds the code and spec the graph is about, while `graph-agent` holds the workflow's own skill files, which [Workflow self-improvement during use](19-workflow-self-improvement.md) expects to be edited *during* the run. Whether that second stream of commits is this node's business or that node's needs deciding.
- Lang's tree contains `target/` and large generated JSON; a code-landing policy that stages broadly would pick those up.

Added by [Done-ness and termination](10-done-ness.md), which makes this node a blocker for a new one and couples landing to correctness:

- **This node now blocks [Human review of landed code](20-human-code-review.md).** What the human can be shown, and what "reject this" can even mean, both depend on whether code lands as per-node commits, one branch per effort, or uncommitted working-tree edits. That node cannot start until this one lands.
- **"Landed" now means "landed green".** The standing bar — builds, no warnings, formatted, tests pass where relevant, plus project criteria — is checked by the independent reviewer at *every* implementation node, so a node may not resolve leaving the tree failing it. Landing and correctness are no longer separable steps.
- **The human reads the changes partially and continuously**, which turns a question above from a matter of taste into a functional one: whether history stays legible or gets squashed decides whether their review is possible at all. Per-node commits can be skimmed and chosen between; one squashed effort commit cannot, and *choosing what to read* is the whole of "at least partially".
- **The policy has to work on repositories this machine has never seen.** The workflow will be run on work projects elsewhere, so it cannot assume Lang's conventions, or a particular branch layout, or that the repo is even shaped like these two.

Added by [Graph file format](13-graph-file-format.md), which makes this node the second blocker on the map's first implementation node:

- **This node now also blocks [Write the graph conventions document](21-conventions-document.md)**, and the dependency is not special to that node: **no implementation node can land before there is a policy for landing**, so this node gates the entire implementation phase rather than one member of it. That reprices it — it is no longer one grilling node among seven but the gate in front of everything the destination is measured by.
- **The graph files themselves are committed, in both repositories.** Confirmed by lookup rather than assumed: Lang ignores only `/target` and `/.direnv`, so its `.scratch/` is tracked exactly as `graph-agent`'s is. So an effort's own bookkeeping — `map.md`, `decisions.md`, `flags.md`, every node file — is part of the history this node designs, and it changes on almost every node. Whether graph edits share commits with code, or are a separate stream, is this node's call and nobody else's.
- **The third stream is now visible.** The bullet above already noted two repositories changing for different reasons; the graph's own files are a third kind of change inside each of them, and the human's continuous review is much easier if a code diff is not buried in bookkeeping.

## Answer

**The manager commits — one commit per implementation node, containing only that node's code, and only after the human has approved it. The workflow never branches, never pushes, and never rewrites history.**

The whole lifecycle, in order:

```
implement (AFK) → independent reviewer (AFK) → manager raises the diff → human reviews
    → subagent corrects until the human is happy → manager commits → node resolves
```

### The human's answer, and the divergence inside it

Verbatim: *"Right now I work more on a agent write -> I review -> I commit. for lang and this it's grilling and not implementation. I tend to not commit the issue tracker, but I still commited it periodicly for lang and here. Right now I would want that when an implementation task finishes, the manager raises it to me, I review, the implementation subagent will correct until I am happy and then I commit."*

**DIVERGENCE on authorship, agreement on granularity.** The recommendation was that the manager commit *every* node resolution as one commit each, decision nodes' bookkeeping included. The human kept the commit for themselves and split the two streams instead — code per approved node, tracker periodically. **The split is better than the recommendation** and is now policy: it is what stops a code diff from being buried in bookkeeping, which this node had already identified as a functional requirement of a review that is *partial and continuous* rather than exhaustive.

The authorship half then went the other way once its price was named. Asked who runs the commit after approval, the human chose **the manager, on approval** — because the alternative holds the exclusive code slot until a human types `git commit`, so a forgotten commit stalls every implementation node behind it. Approval remains the gate; nothing is ever committed unapproved.

That choice also **collapsed a state rather than adding one.** Under human-authored commits there would be an *approved but uncommitted* node: resolved in the graph, still holding the code slot, its diff waiting to be mixed with the next node's. Committing on approval makes resolution and landing the same instant, so slot occupancy stays a single fact with no third state to represent.

### Two streams, separated by path and nothing else

A code commit contains exactly the paths the node touched, taken from the diff that was just reviewed: `git add -- <files the node created>`, then `git commit -- <the node's paths>`. Never `git add -A`, never `git commit -a`.

This is not fastidiousness, it is required by the human's own habit: **the tracker is dirty by design.** Graph files change on every node and are committed periodically by the human, so at any moment the tree holds bookkeeping that belongs to no code commit. A path-limited commit is what lets the two habits coexist; it also leaves the human's own index untouched, which staging would not.

It retires one worry in this node's question generally rather than locally. Lang gitignores `/target` and `/.direnv`, so a broad `git add` would have been safe *there* — but the policy has to work on repositories this machine has never seen, and path-limited commits never need to know what a repo ignores.

**If the product tree holds uncommitted code the node did not write** — the human's own hand-edits, or a dead agent's leftovers — the manager stops and says so rather than committing someone else's work under a node's name. Silently sweeping it in would attribute a change to a decision that never made it.

### Not committing the tracker is safe, and the never-delete rule is why

The cost is real: history holds the code but not the graph state at the moment it landed, so "why was this written?" is answered by the node file *as it stands today*, not by a snapshot taken at landing time.

That is only safe because node files are **append-only**. The reasoning that was true when the code landed is still in the file, marked superseded if it has since changed. Under a tracker that rewrote answers in place, leaving the graph uncommitted would quietly destroy the justification for every commit — so the standing never-delete rule, adopted for readability, turns out to be what makes this split affordable.

### An implementation node is AFK while it works and HITL at the gate

[Node type taxonomy](07-node-type-taxonomy.md) has implementation as AFK with an independent AFK reviewer. The human's gate does not contradict *never asks live* — the subagent still decides small ambiguities and flags them rather than interrupting — but it does mean an implementation node **ends in a human exchange**, which the taxonomy did not anticipate.

**The AFK reviewer stays**, and its purpose sharpens rather than duplicating the human's: it spends machine time so the gate is spent on judgement instead of on build failures, and it guarantees the human never reviews a red tree. Dropping it because "the human reads the diff anyway" would trade the abundant resource for the scarce one, which is the exact inversion of this map's governing principle.

Two costs, named rather than hidden:

- **The human's queue has a third claimant.** ~2 grilling interviews plus one implementation gate. The gate is *short* — read a diff, approve or point at something — where an interview is long, so it likely does not need a full slot. But it is the only claimant that **holds a lock while it waits**, which is what makes it the first thing to watch during the dogfood.
- **Correction rounds are uncapped.** *"Until I am happy"* is the authority, and a cap on the human's own review would be absurd. What is bounded is the *agent*: death or context exhaustion mid-round falls to the existing machinery from [Relay protocol](08-relay-protocol.md) — lazy detection, replay, two respawns — with the node's `## Review` section as the replay log. Rounds that keep failing are the node-too-coarse signal that node already escalates on.

### The lock is a discovered property, not a field

The single-writer lock stays **emergent from the manager's scheduling** — it is the only thing that spawns subagents, so it cannot double-book the slot. No lock file, no `Locked by:` field.

What the landing policy adds is a way to *check* it: **no uncommitted changes outside the effort's own directory** means the code slot is free. A dirty product tree with no `claimed` implementation node means an agent died holding the slot — and `git diff` is then exactly the partial work that node 08's replay needs. This is a repo-level precondition rather than a graph invariant, so it is a different kind of check from the eight in [Graph file format](13-graph-file-format.md): it reads git, not markdown.

### The workflow's git usage is append-only

No amend, no rebase, no squash, no automatic revert, no force. **The graph never deletes and the history never rewrites — one rule, one reason:** the record of the route walked is part of what this workflow produces, and per-node commits are the join key everything else leans on.

- A **revision lands forward.** The replacement node makes a new commit; the superseded node's commit stays. The message names both its own node and the one it supersedes, so the log shows the friction the supersession chain shows.
- **Squashing is never the workflow's act.** Whatever the human does to their own history before pushing is theirs — a work repo that wants one commit per PR gets it at push time, without the graph losing its join key in the meantime.
- **Never-delete governs the graph's files, not the working tree.** Discarding an abandoned diff is not a violation of it: the tree is a workspace, not a record, and the record of a rejected attempt is the node's `## Review` prose. Whether a total rejection also offers to keep the diff belongs to [Human review of landed code](20-human-code-review.md).

### No branch policy, and no push

**The workflow never creates, switches or deletes a branch.** It commits onto whatever HEAD is. Three reasons, and the first is the decisive one:

- **Most efforts never terminate** ([Done-ness and termination](10-done-ness.md)), so an effort branch has no merge point. Lang's spec effort will run for months; a branch that never merges either forks the repo indefinitely or has to be merged back continuously, at which point it was never a branch.
- **The human owns branch choice.** Lang is developed on `main` with no local branches; a work repo that requires a branch gets one before the workflow starts.
- **A per-node branch isolates work from nothing** while there is a single writer. Per-node branches arrive exactly with worktrees in [Concurrency model](04-concurrency-model.md)'s later phase, where each worktree needs its own branch and `git merge --ff-only` lands it — the same sequencing that node already decided, now with a reason rather than a habit.

**Push is always the human's act.** This is their standing rule for every project, not a call this node makes: commit first, ask before pushing. Everything the workflow commits is therefore local and cheap to undo, which is what makes agent-authored commits low-stakes in the first place.

### The commit message carries the node's id

The subject names the node and includes its `NN` in a machine-findable form, so `git log --grep` and `git log -- <path>` answer *which nodes touched this code* — the question [Revision semantics](06-revision-semantics.md) told the cascade to answer by reading the repo, after rejecting a hand-maintained `Touches:` field for failing silently. Here the answer is maintained by the act of landing, so it cannot drift.

There is precedent in the target repo, invented by hand: `849ed64 spec: struct values, effect handlers, sums (D31-D47)` cites decision numbers in its subject. The exact token — `[34]`, `n34`, a trailer — is [Naming](14-naming.md)'s to fix; that the id must be there and be greppable is fixed here. The manager proposes the message; the human sees it before the commit happens.

### Prototypes: confirmed outside the product tree

[Node type taxonomy](07-node-type-taxonomy.md)'s provisional call stands, made precise: prototype artifacts land under the effort's own directory (`.scratch/<effort>/prototypes/…`), tracked but outside the product tree. So they never contend for the code slot, they ride the tracker's periodic commits, and they never pass through the code gate — the standing bar does not apply to something that is not the product.

Escape hatch, stated rather than built for: a prototype that can only exist *inside* the product tree (a stub component in a running app) takes the code slot and the gate like an implementation node.

### Green by construction

Every commit the workflow makes has passed the independent reviewer *and* the human. Two free properties fall out: `git bisect` over an effort's history stays meaningful, and the human is never asked to review a tree that does not build. "Landed green" from node 10 now has a mechanism rather than an intention.

### The async switch is one step, and it has a trigger

The human's closing question: *"I will maybe at some point want to work more in a asyncronous way with the agent commiting directly and me reviewing asyncronously ?"*

Yes — and nothing needs building for it now, because **the seam is a single step in the order above**: the manager commits *before* the gate instead of after. Granularity, path-limited commits, the id in the subject, the append-only history, the branch and push policy are all identical either way; the only thing that changes is whether the human's approval precedes the commit or follows it. Reviewing asynchronously then means reviewing commits, and rejecting one means a replacement node landing a forward fix — which is already how revision works.

**The trigger to flip it** is the gate becoming the bottleneck: the code slot sitting idle waiting on approvals while the human's queue is full of interviews. That is observable during the dogfood, and it is exactly the number the concurrency model wants. No setting, no flag, no abstraction over "who commits" — one sentence in the manager's procedure changes.

### Three kinds of change, two repositories

The question asked whether the second repository's commits are this node's business. They are not, beyond one rule: **an effort's graph lives in the repo the effort changes, and each repo's effort follows this same policy.** Skill-file edits made during the dogfood are a `graph-agent` effort under this map, committed here by this policy; Lang's code is a Lang effort committed there by the same one. Nothing cross-repo is coordinated, which is consistent with multi-repo already being out of scope. What [Workflow self-improvement during use](19-workflow-self-improvement.md) still owns is *when* the workflow may edit itself mid-run, not how those edits land.

### Consequences

- **[Human review of landed code](20-human-code-review.md) unblocks, and changes character.** It is no longer about *landed* code: the human's review is now a **pre-commit gate inside the node's lifecycle**, so its question becomes the gate's protocol — what the manager shows, what a correction round looks like, and what a total rejection does. Updated in place, since it holds no work.
- **[Write the graph conventions document](21-conventions-document.md) is down to one blocker**, [Naming](14-naming.md). The map's first implementation node is one node from takeable — and it will be the first thing to exercise this gate.
- **[Cascade pass mechanics](15-cascade-pass-mechanics.md) gains a cheap first pass.** `git log -- <path>` names the nodes that touched a file, so the cascade's code-coupling search starts from a fact instead of a search.
- **[Concurrency model](04-concurrency-model.md) needs a correction, not a supersession**: the map's fog asserted the HITL budget is disjoint from the code slot. It is not, now that landing ends in a human exchange.
- **[Subagent context contract](12-subagent-context-contract.md)** gains two duties: an implementation subagent must be resumable through correction rounds, and the manager needs the reviewed diff as part of what it raises.
- **[Naming](14-naming.md)** inherits the commit-id token, plus *gate*, *approval*, *correction round*, and the two stream names.
- **[Adopting an in-flight effort](18-adopting-in-flight-effort.md)** learns a limitation: adoption retro-fits no join key. Lang's existing commits do not name nodes, so the cascade's git-based first pass is empty for everything that landed before the migration.
- **No new node.** Everything this answer surfaced landed on nodes that already exist — which is the first session where that has been true, and a sign the map is converging rather than fanning out.

## Annotation: the id token is a trailer, and a bare `NN` was not unique

Added by [Naming](14-naming.md), which **corrects this answer rather than superseding it**: the requirement was named exactly right and the scope of the id was wrong.

- **`NN` restarts at `01` for every new effort a repo hosts.** So "the node id in the commit subject" is ambiguous across efforts: `git log --grep 21` in a repo with a finished effort behind it returns unrelated work. The cascade *acts* on that query — it repoints edges and judges code — so an ambiguous join key is a correctness problem, not a cosmetic one.
- **The token is `Node: <effort>/<NN>`, a trailer in the commit body.** A trailer has room for the effort name where a 50-character subject does not, it is git-native, and it greps exactly: `git log --grep '^Node: graph-workflow/21$'`.
- **The cost accepted:** the token is invisible in `git log --oneline`. Its reader is an agent rather than the human, and `git log -- <path>` prints full messages anyway.
- **The two streams are the `code commit` and the `graph commit`.** This answer noted the pair had no names and that the distinction was load-bearing; naming each side turned out to be enough, and the pair needs no collective noun.
- **The gate, approval and correction round** keep the names used here, and **review** now belongs to the human alone — the agent that goes first is the **checker**.

## Annotation: the gate is no longer the only claimant holding the code slot while it waits

Added by [When an AFK worker cannot proceed](23-worker-cannot-proceed.md). This answer's *"the only claimant
that holds a lock while it waits"* was true while the gate was the only way an implementation node could
reach the human. It now has a sibling: an AFK worker that hits a broken premise **blocks and keeps the code
slot**, its half-written code left in the tree.

- **Two claimants, and the new one is unscheduled.** The gate arrives at a predictable point in the
  lifecycle; a raise can arrive at any moment, including before a line of code is written.
- **The trigger this answer named for flipping landing asynchronous arrives sooner.** It was *the code slot
  idling on approvals*; there are now two ways for the slot to idle on human attention rather than one.
- **What bounds it is a priority rule rather than a cap.** The manager must get a blocking raise answered
  before it goes on filling the human's queue with grilling questions — recorded on [Human-initiated
  steering](16-human-steering.md), which owns the selection policy.
- **A stop cleans the tree, and something is saved first.** `reject` here says the working tree is cleaned;
  that node adds that a diff is saved to the effort's own directory before the cleaning, written by the
  manager without reading it and path-limited exactly as a code commit is.

## Annotation: branching and rebasing arrive, exactly where this node deferred them

*Filed by the manager at [Run an implementation node's work in a worktree](68-implementation-in-a-worktree.md)'s
resolution, in that worker's own words.*

> Its answer states *"The workflow never branches, never pushes, and never rewrites history"* and, under *No branch
> policy, and no push*, *"The workflow never creates, switches or deletes a branch. It commits onto whatever HEAD
> is."* Both are contradicted on two of three counts: the workflow now creates and deletes a per-node branch, and a
> rebase rewrites history. **Never-pushes stands.** That node's own reasoning is not contradicted — it deferred
> branches to *"exactly with the worktrees in Concurrency model's later phase"*, which is what has now arrived. Its
> clause *"no uncommitted changes outside the effort's own directory means the code slot is free"* is also
> replaced, by counting live worktrees.

**The manager adds one thing this node got right that is now load-bearing.** Its finding that the human commits the
graph files by hand, periodically, while work is in flight is what makes the rebase necessary **even at a count of
one** — the branch moves under an in-flight node, and `--ff-only` would refuse. Node 68 calls absorbing those
commits *"the rebase's real job"*.

## Annotation: the no-effort-branch conclusion stands on a different ground

*Filed by the manager from [The human rejects *most efforts never end*](86-most-efforts-never-end-rejected.md)'s
`INVALIDATIONS`, site 4. This corrects the stated reason and not the conclusion; the disposition is flag `86.1`. It
sits alongside this node's existing annotation recording that [node 68](68-implementation-in-a-worktree.md) replaced
this section's conclusion.*

`### No branch policy, and no push`'s first bullet reads *"**Most efforts never terminate** …, so an effort branch has
no merge point"*, and calls it *"the decisive one"*. **The conclusion is not contradicted. Its decisive ground is** —
the human rejected the frequency claim at node 86.

**The ground that survives is about the interval, not the existence, of the merge point.** Even for an effort known to
terminate, an effort branch's merge point sits at close while the human reviews partially and continuously and
hand-commits the graph files while work is in flight. So such a branch must be merged back continuously — and this
node's own next clause is the conclusion: *"at which point it was never a branch."* That clause never depended on
frequency.

**The second reason is untouched and sufficient alone**: *"The human owns branch choice. Lang is developed on `main`
with no local branches; a work repo that requires a branch gets one before the workflow starts."* The human's new
material at node 86 — *"If it is a very long running effort it will be talked about during the start of the effort I
expect"* — **strengthens** it: that discussion is exactly where a human decides whether to cut a branch, and it is
still not the workflow's act.

**The repair the human was shown is not the repair recorded here**, and that is flag `86.3`: they assented to *"the
workflow cannot name an effort branch's merge point at the time it would open one"*, which their own next sentence
falsified.

**What must not be lost:** only the **effort-wide** branch is refused. Per [node
68](68-implementation-in-a-worktree.md) the workflow does create and delete per-node branches and does rewrite
history by rebasing.
