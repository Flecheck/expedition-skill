# Cascade pass mechanics

Type: grilling
Status: resolved
Blocked by: 07

## Question

The cascade is now a named mechanism with settled goals and no design. How does it actually run?

Settled by [Revision semantics](06-revision-semantics.md): it is aggressive, AFK and agent-driven; its scope is agent judgement over both blocking edges and the code itself; its output is queued graph edits — supersede resolved nodes, update open nodes in place, create intermediate nodes — and never a human interrupt. What is not settled:

- **When does it run?** Immediately when a revision lands, or as a step the manager takes before choosing the next node? Running late risks the manager scheduling work against a graph it already knows is stale; running immediately puts a pass between every revision and the next thing.
- **How many agents is it?** One agent per revision surveying the whole graph, or one per candidate node? The first is cheap and holds the whole picture but must fit the graph in one context; the second parallelises as AFK work and scales, at the cost of no agent seeing the pattern across nodes.
- **Who writes the edits** — does the cascade agent modify the graph files directly, or return a proposed edit list that the manager applies? The manager applying them keeps a single writer on the graph; the agent applying them saves a round trip and a large amount of relayed context.
- **Does it need the code-writing lock?** It reads the repo, and reading is safe under the single-writer rule — but if a cascade can ever be triggered while an implementation subagent is mid-edit, it is judging a tree that is in flux.
- **What does it report to the human, if anything?** Its whole design is to avoid interrupting, but a pass that supersedes eleven nodes silently is a surprise the next time the human looks at the graph.

Now unblocked by [Node type taxonomy](07-node-type-taxonomy.md), which also adds to the last two bullets:

- The pass creates and edits nodes drawn from five types, and the ones it will reach for when an implementation must change are `grilling` and `research` — both cheap, neither touching code.
- **On the code lock:** an implementation node now holds the exclusive slot from first edit through review and rework, which widens the window in which a cascade could be judging a tree in flux.
- Its queued output can also include **sharpening an unstarted node's acceptance condition**, since those are written by the spawner and updated in place.

Added by [Done-ness and termination](10-done-ness.md), which gives this pass a **second mode** rather than a new mechanism — and it answers two of the bullets above while sharpening a third:

- **The sweep** is this same agent with the bound taken off: whole graph as its scope, no triggering revision, run when the frontier empties. Termination depends on it, since done requires a sweep that produces nothing new.
- **It must collect flags** — every outstanding assumption flag, flagged acceptance condition and delegated answer — and produce the findings section of the completion report.
- **"What does it report to the human" is answered for the sweep and unchanged for the rest.** The sweep reports, because the completion report is a required condition of the done test. The revision-triggered cascade still reports nothing and only queues edits.
- **"Does it need the code lock" is answered for the sweep too, for free:** the sweep only runs when the frontier is empty, so no implementation node holds the slot and no tree is in flux. The question survives only for the triggered cascade.
- **"How many agents" gets harder, not easier.** The sweep's scope is unbounded by construction, so the one-agent-surveys-everything option would have to fit ~130 nodes *plus* the repo into a single context, which it will not. The sweep therefore has to fan out — which turns the choice for the triggered cascade from a free one into a question about whether both modes should share a shape.

Added by [Graph file format](13-graph-file-format.md), which gives the pass concrete file duties and splits its work cleanly in two:

- **Two bookkeeping duties fall on the cascade because it already visits every affected node:** striking through a superseded node's line in `decisions.md` and adding the replacement's, and appending a flag's line to `flags.md`. Neither is new work — it is the price of the indexes being separate files, and it is paid by the only agent already at the right place.
- **Flag collection got cheap, which does not help the fan-out problem.** Flags now live in `flags.md` with their state, so the sweep gathers them in a single-file read rather than a 179-file scan. But the pressure to fan out was never about flags — it is about holding the whole graph *and* the repo in one context — so that bullet above stands unchanged.
- **The pass's work is now provably two kinds**, which is the strongest input this node has for the *how many agents* question. [Graph file format](13-graph-file-format.md) lists **eight invariants decidable with no judgement at all** (dangling edges, missing back-edges, reused numbers, undeclared labels, index/flag consistency, missing acceptance conditions, attempt-block count). Everything else the pass does — is this resolved node actually affected, does this code still match — is irreducibly judgement. A design that runs the mechanical half as a script and fans out agents only over the judgement half is a different shape from one agent doing both, and this node should choose deliberately rather than inherit.
- **`out-of-scope` joins `superseded` in edge repointing.** [Revision semantics](06-revision-semantics.md) made the cascade repoint inbound edges off superseded nodes; the new fifth status behaves identically — a `Blocked by:` onto it is an error — so a node ruled out of scope leaves the same dangling edges behind and needs the same treatment.

- **The judgement half now has a cheap first pass**, added by [Git and code-landing policy](11-git-and-code-landing.md). Code lands as one commit per implementation node carrying that node's id in the subject, so `git log -- <path>` names the nodes that touched a file and `git log --grep` finds a node's landed code. [Revision semantics](06-revision-semantics.md) told this pass to find code coupling *by reading the repo* after rejecting a hand-maintained `Touches:` field for failing silently — the git history is that index, maintained by the act of landing rather than by anyone remembering. It does not replace reading the code, but it turns "which resolved nodes might be affected?" from a search into a query, and it is the only part of the pass's judgement half with a mechanical starting point.
- **One limitation, and it lands on the dogfood.** The join key only exists going forward: nothing that landed in Lang before the migration names a node, so the first-pass query returns nothing for the existing tree and the pass falls back to reading code — which is precisely the case where the graph is largest.

Blocked on the taxonomy because the pass creates and edits nodes by type, and cannot be specified before the types are.

### What the record now holds, gathered by the manager before this node was claimed

*The manager's own note, not a decision.* Everything below is measured from the files rather than argued, so
the worker spends no question establishing it. This node's question was last annotated by
[Naming](14-naming.md) at fourteen nodes. Twenty-eight more have resolved since, and the pass this node
designs has run zero times in all of them.

**Fact 1 — the cascade has never run, and neither status it needs has ever been used.** No node records a
pass. No node carries `Status: superseded` or `Status: out-of-scope`, and the only `Superseded by:` string
anywhere in the graph is inside [Graph file format](13-graph-file-format.md)'s own fenced template — one of
the known false positives. So the pass's headline output, as [Revision semantics](06-revision-semantics.md)
specified it — supersede a resolved node, repoint the inbound edges off it, rule one out of scope — has fired
**zero** times across 42 nodes. This node is designing a mechanism with no operating experience of the thing
it is named for.

**Fact 2 — what ran instead: 28 in-place annotations, every one written by the manager, by hand.** Every
propagation this effort has actually performed arrived as a **section appended to an existing node by a later
node**, marked with the node that added it and left in place forever under the never-delete rule.
Twenty-eight of them across seventeen nodes: four on [Done-ness and termination](10-done-ness.md), three on
[Node type taxonomy](07-node-type-taxonomy.md), two each on 08, 11, 12, 16, 20 and 22, and one each on 04,
13, **15 — this node**, 18, 19, 21, 23, 24 and 28. The map's fog items take the same shape and are not
counted here. Two of the question's five bullets therefore have de facto answers that were never chosen.
*Who writes the edits*: the manager, as scribe, pasting the resolving worker's own words under a marked
heading. *How many agents*: one, and it was never an agent. Nothing decided this — the pass was never built,
so the manager did the work — which means this node is choosing whether to keep or replace a practice with
twenty-eight instances behind it rather than filling a blank.

**Fact 3 — `INVALIDATIONS` has fired exactly twice, both from one worker.** [Workflow self-improvement during
use](19-workflow-self-improvement.md)'s worker reported two, and they became the `### Narrowed by` section on
[Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md) and the
`## Annotation: which graph a promoted flag's node lands on` on
[Done-ness and termination](10-done-ness.md). Every other handover in the effort reported `none`. So the
worker-side channel exists, works, and fires rarely — and the other twenty-six annotations came from the
**manager's own reading** of what an answer touched, which is unbudgeted work that no contract describes and
nothing checks.

**Correction to Fact 3, by the manager, after the first question on this node had already been asked.** The
figures above are wrong and the shape of the fact changes with them. ~~`INVALIDATIONS` has fired exactly
twice, both from one worker~~ — it has fired **three** times, from **two** workers: [Whether flags.md
survives the settle-at-close practice](27-does-flags-file-survive.md)'s worker reported one onto
[Done-ness and termination](10-done-ness.md), recorded there as *"Reported as an invalidation by"*, which the
first count missed. So twenty-**five** of the twenty-eight came from the manager's own reading, not
twenty-six.

The correction also brings a split the first count did not draw, and it bears on what this node decides.
Taking each annotation's target and asking whether that target was **already resolved** when the annotation
landed: **eighteen** landed on resolved nodes and **ten** on open ones. Of the eighteen, three came through
`INVALIDATIONS` and fifteen came from the manager. The eighteen are reachable from `decisions.md`, which
every worker already reads; the ten are not reachable from any index, an open node's one-line summary being
its title.

One thing the manager observed while counting, offered as an observation and not as a fact of the record:
almost none of the eighteen is a **contradiction**. They are renames, extensions, narrowings and
refinements — *"the write lock is called the code slot"*, *"`done` is gone as a word"*, *"the raise reaches
`precondition` too"*. All five contracts word the channel as *"which resolved node your work **contradicts**,
and how"*, so on that reading the three firings may be the channel used correctly rather than a channel
underused, with its word covering about a sixth of the traffic it would have to carry.

**Fact 4 — the mechanical half is a real script, and it now survives sessions.** The eight invariants run as
one ~9k perl script, invoked once per node, printing the state counts, the eight checks and the broken-link
count; at this node's claim it reported `open=13 resolved=29 | total 42`, all eight passing, 0 broken links.
It survived a session boundary for the first time at [What the checker contract
owes to having been run](31-checker-contract-owes.md), for the single reason that it had been written to the
session's own job directory rather than to `$TMPDIR` — so *a throwaway checker that dies with the temp
directory* is a storage-location cost with a free remedy and is not evidence for anything. Twelve false
results have been measured across the effort's sessions, every one of them from a rule the format either
states elsewhere or fails to state at all; [map.md](../map.md)'s *extraction of a graph tool* fog item lists
all twelve.

**Fact 5 — two open nodes have drawn their boundary against this one explicitly, and one of them is now
stale.** [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md) lists *the cascade already owns this* as one of its four candidate
mechanisms, and cannot judge it without knowing what the pass does: *"If a cascade scans code for decisions
that have moved, a shipped prose file is code."* [Nothing tells a worker to hold its work against the
record](37-invalidations-is-not-a-check.md) puts itself on the other side of the same line — the cascade
*"owns the pass that propagates a known revision outward"*, and node 37 owns **finding** one. Both are open
and unclaimed, so this node's answer sets the scope of two others. The stale part: node 29's question states
that `INVALIDATIONS` is *"defined over resolved nodes, not over product files, and no worker has ever
reported one"* — true when written, false since Fact 3.

**Fact 6 — this node is one of the two blockers left on the manager's own skill**, the last and largest
product file; the other is [Human-initiated steering](16-human-steering.md). What that skill has accumulated
is not written in this node's question: [map.md](../map.md)'s first fog item now carries nine requirements and
two whole mechanisms, every one learned by *running* the workflow rather than by reasoning about it. The ninth
is the closest to this node's subject — a statement of what changed must cover the commits and the files left
in the older form, not only the working tree — and it is the same duty this pass would discharge if it
existed.

### Standing instructions for this node's worker

- The facts above are the **manager's**, not the human's. None of them has been put to the human. Where your
  answer turns on one, ask rather than treat it as settled.
- The human reads your questions and nothing else. They do not open this file. Write `ABOUT` and `SO FAR` for
  someone who has read none of it, every time.
- Five bullets are open in the question above and the annotations added more. You are not required to settle
  all of them, and not in the order written. Where one turns out to belong to another node, say so on
  `NEW NODES` rather than deciding it thinly.
- **One implementation node is running concurrently with yours**, and it holds the code slot: [The checker's
  spawn carries the effort's ground rules](42-checker-spawn-carries-ground-rules.md), editing
  `.claude/skills/expedition-checker/SKILL.md`. Nothing you decide may assume that file's current text. This
  is the first time this effort has run two nodes at once.

## Annotation

Added by [Naming](14-naming.md).

- **The cascade and the sweep are now separated by purpose, not by scope.** A cascade propagates a revision it knows about; a sweep looks for revisions nobody propagated. This node owns the first and [Done-ness](10-done-ness.md) the second, and they are the same machinery run in opposite directions — which is an argument for specifying both here rather than leaving the sweep to be re-derived at termination.
- **The code-coupling query is `git log --grep '^Node: <effort>/<NN>$'`**, not a bare id. The join key carries the effort name because `NN` restarts at `01` per effort, so the cheap first pass this node inherited is exact rather than approximately right.

## Answer

**The cascade is not one agent. It is three parties, split by what the change lands on, and only the
third is a spawned pass.** The split is by target rather than by frequency, and the measured traffic is
what forced it: of twenty-eight propagations this effort actually performed, eighteen landed on
already-resolved nodes and ten on open ones, and none at all on landed code — which is the case the pass
would have handled if it had existed.

### 1. Resolved-node targets ride the resolving worker's handover, and the word widens

A worker already reads `decisions.md`, one capped line per resolved node, so it can reach every candidate
with no change to what a spawn carries. What changes is the word: the channel asks today for *which
resolved node your work contradicts*, and it now asks for any resolved node whose answer this work
**changes what it says** — a rename, an extension, a narrowing, or a contradiction.

The reason is a count. Of the eighteen, three came through `INVALIDATIONS` and fifteen through the
manager's own reading — and almost none of the eighteen is a contradiction. They are renames,
extensions and narrowings: *the write lock is called the code slot*, *`done` is gone as a word*, *the
raise reaches `precondition` too*. On that reading the three firings are the channel used correctly
rather than a channel underused, with its word covering about a sixth of the traffic it has to carry.

This costs one reworded line in five worker contracts and one sentence in `graph-conventions.md`. The
node for it is reported below.

### 2. Open-node targets are not settled, and stay where they are

The human's words: *"I am not too sure about 2 for now, but we can see later."* Until then the manager
keeps reading its own answers and appending the marked note by hand, as it has ten times. What was
offered and not taken was pulling at claim time instead of pushing at resolution, on the ground that no
index reaches an open node — an open node's one-line summary is its title. **Nothing in this answer
depends on that half resolving either way**, and one duty waits with it: sharpening an unstarted node's
acceptance condition, which [Node type taxonomy](07-node-type-taxonomy.md) gave this pass, is an
open-node edit and therefore stays with the manager for now.

### 3. Landed code is the spawned pass, and it is two agents

**It never edits product code.** Its only output is a minted node — an `implementation` node with its
acceptance condition where what the fix must be is determined, a `grilling` or `research` node where it
is not. This is forced rather than chosen: product code reaches the repo only through an implementation
node's acceptance condition, its independent checker and the human's gate, and the landing policy allows
exactly one commit per node, so a pass that edited code would bypass all four. It is also what has been
happening — the real instances of a decision reaching already-shipped files were ordinary implementation
nodes, at [26](26-carry-deltas-into-shipped-files.md), [31](31-checker-contract-owes.md) and
[35](35-handover-mints-no-condition.md).

This follows [Revision semantics](06-revision-semantics.md), which qualifies the cheap types with *"when
it is not yet clear into what"*, rather than the unqualified reading in this node's own question that the
pass reaches only for `grilling` and `research`.

**Triage, at every resolution.** The manager spawns one cheap agent whose whole input is the answer that
just resolved, plus the landed-code inventory: one line per node that ever landed code — its number, its
name, and the paths its commit touched — from `git log --grep '^Node: <effort>/'`. It goes and looks
rather than waiting to be told. Its output is the landed nodes worth a real look, and the empty result is
the ordinary one. It reads no product code.

**One agent per candidate, not one survey.** Each survivor gets its own agent, handed that node's answer,
its commits from `git log --grep '^Node: <effort>/<NN>$'`, and its files. The anchors are load-bearing: a
bare id is not unique, and unanchored, `Node: <effort>/4` matches 4, 40–49 and 400 upward.

**What makes this affordable is that the candidate set is the landed code and not the graph.** Only
implementation nodes land, and they are a minority — eight commits against forty-two nodes here — so the
triage input is about a page and stays about a page as the graph grows. That is the whole difference from
the option set aside earlier in this node's interview, *spawn a cascade agent after every resolution*,
whose price was named there as re-reading what the resolving worker already had in hand: the input is
bounded by commits rather than by node count. The two positions are not in conflict, and the later one
holds.

**It is built now, not deferred to a first firing.** The human's words: *"One of the reason that the
cascade agent hasn't run yet is because we haven't create it yet."* Zero firings of a mechanism that does
not exist measures nothing, so the zero count is no argument for a placeholder.

**Fan-out is also the only shape the sweep can use.** [Done-ness and termination](10-done-ness.md) made
the sweep this same machinery with no starting point, and the whole graph plus the repo will not fit one
context at the dogfood's scale. Under this answer the sweep is triage with every resolved answer as its
input rather than one, fanning out identically — plus the flag collection that node owes the closing
report, which is a single read of `flags.md`.

### What this pass does not reach, stated plainly

**This class of work has three origins and triage reaches one.** *Decision-driven* — a decision resolved
and shipped files stopped matching, which is nodes 26 and 35. *Use-driven* — friction found by using the
thing, which [Workflow self-improvement during use](19-workflow-self-improvement.md) already routes
through a `FRICTION` flag. And *the human noticing at a gate* — node 31 was created at node 26's gate
from the human's own question on reading the payload, with no decision having resolved and nothing stale;
a per-resolution triage agent would never have found it. Two of the three origins already have channels
and need nothing added. What this answer adds covers the first.

**The only mechanism that has ever caught this class of miss is being set aside.** [What keeps the shipped
files consistent when a decision changes a term](29-shipped-file-consistency.md) records that the failure
was found by a **blind checker** tracing an acceptance condition — the party with the least context.
Extending the checker's remit was set aside because a checker runs only on implementation nodes, so it
covers nothing across a run of decision nodes, and a *something-else-is-now-stale* finding has no home in
a `PASS`/`FAIL` verdict. That coverage argument stands, and the honest statement of it is that a mechanism
with catches to its name is being set aside for one with none.

**Neither half of the finding is checked.** Part 1 depends on a worker reporting, and [Nothing tells a
worker to hold its work against the record](37-invalidations-is-not-a-check.md) records that nothing tells
a worker to go and look. Triage does go and look, and nothing checks triage. This answer moves the
exposure; it does not close it. Consistent with [Done-ness and termination](10-done-ness.md), which ruled
out an audit agent over the cascade and named the residual risk instead.

### Who writes, and who reads

**No agent in this pass writes a graph file.** Both roles return text and the manager pastes it, which is
what keeps the manager the graph's only writer. Two consequences.

The bookkeeping [Graph file format](13-graph-file-format.md) assigned to the cascade — striking a
superseded node's `decisions.md` line and adding the replacement's, appending a flag's line to `flags.md`
— and the inbound-edge repointing [Revision semantics](06-revision-semantics.md) assigned to it are **the
manager's procedural steps, not the pass's writes**. They already read that way in the shipped
`graph-conventions.md`, under `Supersede` and `Raise a flag`. Nothing about the duties changes; only who
performs them.

And the acceptance condition on an implementation node this pass mints is written by **the per-candidate
agent, in its own return**, with the manager pasting it. [A worker's handover carries no acceptance
condition for the node it mints](35-handover-mints-no-condition.md)'s rule therefore applies unchanged,
and such a node is **not** manager-minted. [What writes the acceptance condition for a node the manager
mints](39-condition-for-a-manager-minted-node.md) stays open and is not narrowed by this: its subject is
a condition the manager authors, and here the manager authors nothing.

### The code slot

The pass modifies no product code, so it never holds the slot. But the per-candidate agent **reads** code,
and a tree whose slot is occupied is in flux, so that agent does not run while it is occupied — occupancy
being discovered from the working tree, as it already is. Waiting costs nothing: the pass is AFK and its
output is a queued node rather than an edit. Triage reads no product code and never waits. That settles
the code-slot question for the triggered pass; [Done-ness and termination](10-done-ness.md) had already
settled it for the sweep, which runs only on an empty frontier.

### What it reports

Nothing as an interrupt — unchanged from [Revision semantics](06-revision-semantics.md), and the sweep
still reports through the closing report. What is added is one line rather than a channel: a minted node
lands on the frontier where it is visible anyway, and the manager names in its ordinary narration at
resolution what the pass minted, or that it found nothing. That is what stops a pass which supersedes
eleven nodes from being a surprise at the next human read, and it costs nothing that is not already being
said.

**The pass raises no flag of its own.** Its entire output is a judgement, so a flag per judgement would
put one line of noise in `flags.md` per resolution. Where it cannot judge — a tree in flux, a file it
cannot read — it says so in its return and mints nothing.

### The mechanical half is the tool's, not an agent's

[Graph file format](13-graph-file-format.md)'s eight invariants are decidable without judgement and
already run as a script. Neither role in this pass re-derives them and neither is asked to check them.
The pass's work is the judgement half only.

### Consequences

- **Two new nodes**, both implementation: the widened channel in six shipped files, and the pass's own
  worker contract. Reported with this handover.
- **The manager's own skill** gains the manager-side half of all three parties — when triage is spawned,
  what it is handed, what gets pasted where, and the one narration line. With this node resolved that
  file is down to one blocker, [Human-initiated steering](16-human-steering.md).
- **[What keeps the shipped files consistent when a decision changes a
  term](29-shipped-file-consistency.md) is largely absorbed and should be updated in place**, it being
  open and unclaimed. Of its four candidate mechanisms, *the cascade already owns this* is now answered:
  a shipped prose file is code for this pass, and the finding mechanism is triage plus the widened
  handover. What triage cannot reach is what is left of that node — the glossary not travelling to another
  repository, and a term shipped with no `CONTEXT.md` entry at all, which the manager has hit twice while
  filing acceptance conditions at nodes 41 and 42. Neither is a decision that moved, so neither is
  reachable from a resolved answer.
- **[Nothing tells a worker to hold its work against the record](37-invalidations-is-not-a-check.md) keeps
  its whole question and gains a reason it matters more**: part 1 now carries eighteen twenty-eighths of
  this effort's propagation traffic on a channel nothing tells a worker to go and look at.
- **[Done-ness and termination](10-done-ness.md)'s sweep is specified** — triage over every resolved
  answer, the same fan-out, plus the single-file flag read.

## Flags

`15.1` **· settled** `ASSUMPTION` — the code slot. I settled the pass's relation to the code slot myself rather than
asking, the human's attention being spent on the three larger calls. The pass holds the slot never, since
it modifies no product code; the per-candidate agent does not *run* while the slot is occupied, because
reading a tree in flux makes its judgement unreliable and an AFK pass whose output is a queued node loses
nothing by waiting; triage reads no product code and never waits.

`15.2` **· settled** `ASSUMPTION` — the one narration line. Settled by me, not asked. The design reports nothing as an
interrupt, which leaves a pass that supersedes eleven nodes invisible until the next human read, and the
manager is already narrating each resolution — so naming what the pass minted, or that it found nothing,
is one line inside a message that already exists rather than a new channel.

`15.3` **· settled** `ASSUMPTION` — who performs the bookkeeping. Settled by me from the single-writer rule rather than
asked, and it contradicts the letter of two resolved nodes, which is why it is worth revisiting. The
`decisions.md` strike-through, the `flags.md` append and the inbound-edge repointing are the manager's
procedural steps, as the shipped `graph-conventions.md` already has them, and not writes the pass performs.

`15.4` **· settled** `ASSUMPTION` — who authors a minted node's acceptance condition. Settled by me, on the manager's
explicit request that this answer say plainly what it assumes. The per-candidate agent writes the condition
in its own return and the manager pastes it, so the reporting-worker rule applies unchanged and such a node
is not manager-minted. If that reading is wrong, every implementation node this pass ever mints falls to
node 39 instead.

`15.5` **· settled** `ASSUMPTION` — the pass raises no flag. Settled by me, not asked. The pass's entire output is a
judgement, so a flag per judgement would add one line of noise to `flags.md` per resolution; what it finds
becomes a node, which is the visible artifact, and its misses surface through the sweep and the closing
report, consistent with node 10 having ruled out any audit over the cascade.

## Interview

### Attempt 1 — routing key `graph-workflow/15/a1`

**Q1, from the worker.** Should the frequent, cheap propagation move onto the **resolving worker's handover**
— a new part where the worker names the nodes its own answer changes and writes the note for each, which the
manager then pastes — leaving a separately spawned cascade agent only for the rare, expensive case where an
answer makes an already-resolved node or landed code wrong?

The worker's own recommendation was **yes**, resting on the standing preference that most of the context
lives in the workers rather than the manager, and on the measured ~200k of manager context per node. It named
one honest cost: a worker sees the resolved decisions index but not the open nodes, so it can only name open
nodes it was pointed at, and the fix is one line per open node in the spawn. Set aside: keep it as the
manager's own reading; spawn a cascade agent after every resolution; leave it lazy and check at claim time.

**The manager's counter-proposal, put to the human alongside the worker's question and recorded here as the
manager's own, not the worker's and not the human's.** Split by what the target is, not by how often it
happens:

1. **Resolved-node targets → the resolving worker's handover, and widen the word** from *contradicts* to
   *changes what it says*, covering renames, extensions, narrowings and contradictions alike. The worker
   already reads `decisions.md`, one capped line per resolved node, so it can reach every candidate with no
   spawn change at all. Eighteen of the twenty-eight measured edits.
2. **Open-node targets → pull at claim time rather than push at resolution.** A worker cannot judge an open
   node from an index, an open node's one-line summary being its title. The pull already exists as unnamed
   practice — this node's own `### What the record now holds` gathering and node 42's claim-time audit, both
   run the same day — and it is paid by the node about to be worked rather than by every resolution. Ten of
   the twenty-eight.
3. **Landed code → the spawned cascade agent, thin, and not built until it fires.** Zero instances in
   42 nodes.

**A1**, the human's words, `verbatim`:

> ok for recommandation, I am not too sure about 2 for now, but we can see later. One of the reason that the
> cascade agent hasn't run yet is because we haven't create it yet.

**What that endorses, quoted beside it, and attributed.** The endorsed option is the **manager's** three-part
counter-proposal above, not the worker's recommendation — so the worker's recommendation lost on the split it
drew. Parts **1** and **3** are taken as offered. Part **2** is explicitly **not settled**: *"I am not too
sure about 2 for now, but we can see later"*, so the open-node half stays with the manager as it is today and
the question of moving it is deferred rather than decided either way.

**The correction in the second sentence, and what it reaches.** It falsifies the reasoning inside part 3 —
*not built until it fires* — because a mechanism that does not exist cannot fire, so zero firings is no
evidence of rarity. It reaches further back than part 3: the manager's own **Fact 1** above frames the zero
count as a measurement, and for the *agent* it is a tautology. What survives as a real measurement is the
graph-side half of Fact 1 — nothing has ever been superseded and `out-of-scope` has never been used — which
is a fact about the graph rather than about the missing agent.

**The manager's note on the same correction, recorded as the manager's.** The landed-code case has in fact
arisen repeatedly and was handled by **minting an implementation node** each time rather than by any pass:
[Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md) carried nine
deltas into shipped files, [What the checker contract owes to having been run](31-checker-contract-owes.md)
rewrote a contract, [A worker's handover carries no acceptance condition for the node it
mints](35-handover-mints-no-condition.md) changed five, and [What keeps the shipped files consistent when a
decision changes a term](29-shipped-file-consistency.md) exists because that class of miss has failed three
times. So the substance fired four or more times and the mechanism zero, which is the concrete form of what
the human said.

**One thing about this round rather than its content.** It is the first time in this effort that the human has
endorsed a manager's proposal **in place of** the worker's recommendation, as against node 19's note 6, which
was endorsed as an addition to what its worker had already recommended.

**Q2, from the worker.** For the landed-code half, is this the shape? (1) It never edits product code — its
only output is a **minted node**: an implementation node with its acceptance condition written where the fix
is determined, a grilling or research node where it is not. (2) **One agent per candidate rather than one
survey**, triggered by part 1's own report: where a worker names a resolved node whose answer changed and
`git log --grep` shows that node landed code, one agent is spawned on that one node with its commits and files
as its whole input. (3) It is **built now** rather than deferred to its first firing.

The worker recommended **yes to all three**. On (1): forced rather than chosen, since product code reaches the
repo only through an implementation node's condition, its blind checker, the gate and one commit, and all
three real instances were implementation nodes. On (2): git makes the candidate list exact, and fan-out is the
only shape the sweep can use at all, so one-survey-per-revision would stop the two modes being one mechanism.
On (3): the argument for deferring was the zero count, and the human removed it. Its named cost on (2): the
join key exists only going forward, so in the dogfood target the query returns nothing for anything that
landed before migration. Set aside: always mint a grilling node and never an implementation node; one agent
surveying the whole graph per revision; defer as originally offered.

**The manager's four notes, put to the human alongside Q2 and recorded here as the manager's own.**

1. **The join key was verified on this repository rather than trusted.** Eight code commits exist and all
   eight carry the trailer; `git log --grep '^Node: graph-workflow/42$'` returns exactly one commit, and the
   reverse direction names all four nodes that ever touched the checker contract. One precision fix: the
   worker wrote the query unanchored, and [Naming](14-naming.md) already fixed the anchored form
   `git log --grep '^Node: <effort>/<NN>$'` because a bare id is not unique — unanchored,
   `Node: graph-workflow/4` will match 4, 40–49 and 400+ at the dogfood's scale.
2. **The proposed trigger inherits part 1's blind spot in full.** The landed-code agent fires only where a
   resolving worker reported a changed resolved node, and nothing tells a worker to go and look — [Nothing
   tells a worker to hold its work against the record](37-invalidations-is-not-a-check.md), still open.
   Against that, [What keeps the shipped files consistent when a decision changes a
   term](29-shipped-file-consistency.md) records that this exact class of miss escaped **three times running**
   and was caught by a blind checker tracing a condition, not by any resolving worker. So (2)'s exactness buys
   precision on candidates the trigger never surfaces.
3. **The sweep cannot be the safety net on the effort that matters most.** The natural answer to note 2 is
   that the sweep catches what part 1 misses, it being the pass that looks for revisions nobody propagated —
   but the sweep runs only when the frontier empties, and [map.md](../map.md) records that Lang's effort
   **will not terminate**. On the dogfood target the safety net never fires.
4. **(1) collides with an open node.** A pass minting an implementation node has to write its acceptance
   condition. [A worker's handover carries no acceptance condition for the node it
   mints](35-handover-mints-no-condition.md) settled that the reporting worker writes it, but this pass
   returns text the manager pastes, which makes such a node arguably manager-minted — and that is [What
   writes the acceptance condition for a node the manager
   mints](39-condition-for-a-manager-minted-node.md), open and unclaimed.

The manager's read, offered after those four: (1) and (3) right and takeable as offered; on (2),
one-agent-per-candidate accepted and **the trigger not accepted**, with note 3 closing the sweep as a
fallback — so if the trigger stands as proposed, something else has to find the case.

**A2**, the human's words, `verbatim`:

> for the question, ok for the manager proposition

**What that endorses, quoted beside it, and attributed.** The **manager's** read immediately above, not the
worker's recommendation. So: **(1) settled** — the pass never edits product code and its only output is a
minted node. **(3) settled** — it is built now. **(2) settled in half** — one agent per candidate rather than
one survey, and its **trigger is refused**, leaving open what finds the case instead. That open part is this
node's to answer and is not a licence to fall back on the sweep, note 3 having ruled that out for the effort
the design is aimed at.

**Two things about this round rather than its content.** It is the second manager proposition this node's
human has endorsed in place of the worker's recommendation, so the pattern is no longer a single instance.
And it is the first time a manager note **refused a part** of a worker's own recommendation and the human
took the refusal — as against node 19, where every endorsed manager note added something rather than
subtracting it. The human also named which pending thing they were answering — *"for the question"* — which
is the queue discipline they had stated one message earlier being applied to their own reply.

**Q3, from the worker.** Is this what finds the case? At every resolution the manager spawns one cheap
**triage** agent whose entire input is the answer that just resolved plus the **landed-code inventory** — one
line per node that ever landed code, with its number, its name and the paths its commit touched, from
`git log --grep '^Node: <effort>/'`. It goes and looks rather than waiting to be told, and its output is the
list of landed nodes worth a real look, usually empty. Each survivor gets the per-candidate agent already
settled at Q2.

The worker recommended **yes**: it is not the refused trigger, since nothing has to have been reported by
anyone and *going to look* is the act nothing in the workflow performs today; it does not route through the
sweep, so the non-terminating case is covered; and it is affordable because the candidate list is bounded by
**commits rather than node count** — eight code commits against forty-two nodes here, a few dozen against
179 at the dogfood target — which keeps the triage input at about a page and makes it the cheapest agent in
the design and the first worth putting on a cheap model. Set aside: extending the blind checker's remit,
which runs only on implementation nodes and so covers nothing across a run of decision nodes; skipping
triage and spawning a per-candidate agent for every landed node at every resolution; running it periodically,
which leaves each run with no anchor; and folding it into claim time beside the parked open-node half, which
is tidier but would let landed code stay stale until something happened to be claimed near it.

**The manager's four notes, put to the human alongside Q3 and recorded here as the manager's own.**

1. **The worker's evidence is two of three, and the third is the instructive one.** It claimed all three real
   instances fit this shape. [Carry the recorded deltas into the shipped skill
   files](26-carry-deltas-into-shipped-files.md) does — nine deltas from resolved decisions against a file
   node 21 had landed. [A worker's handover carries no acceptance condition for the node it
   mints](35-handover-mints-no-condition.md) does — node 33's resolution made five contracts stale.
   [What the checker contract owes to having been run](31-checker-contract-owes.md) does **not**: it was
   created at node 26's *gate*, from the human's own question on reading the payload — *"do you also want to
   do something also with the 'What the checker did that I'd want kept'"*. No decision had resolved that made
   anything stale. A per-resolution triage agent would never have found it. So this class of work has **three
   distinct origins** — decision-driven, use-driven, and the human noticing at a gate — and triage reaches
   only the first. The second already has a channel, [Workflow self-improvement during
   use](19-workflow-self-improvement.md)'s `FRICTION` flag; the third is the human reading a diff, which is
   itself a mechanism and needs no other.
2. **The worker reversed its own Q1 position, on a reasoned ground.** At Q1 it set aside *spawn a cascade
   agent after every resolution* on the price of *"179 extra agent spawns each re-reading what the resolving
   worker already had in hand"*. Q3 is the same shape. What changed is the input: bounded to about a page by
   commits, so the triage agent re-reads nothing. Deliberate rather than forgotten, and put to the human as
   such.
3. **It replaces the only mechanism that has ever caught this with one that has never run.** [What keeps the
   shipped files consistent when a decision changes a term](29-shipped-file-consistency.md) records that the
   miss was found by a **blind checker** tracing a condition — the party with the least context. Setting that
   aside on coverage grounds is fair, and the record should still say plainly that the empirical catcher is
   being sidelined for something untested.
4. **This probably absorbs most of node 29**, which holds four candidate mechanisms and gets one of them
   answered properly here. What would be left of it is the part triage cannot reach: the glossary not
   travelling to another repository, and terms shipped with no `CONTEXT.md` entry — which the manager has now
   hit twice while filing acceptance conditions, at nodes 41 and 42.

**A3**, the human's words, `verbatim`:

> ok for recommanded

**What that endorses, quoted beside it, and attributed.** The **worker's** own `RECOMMENDED` block above —
yes to the triage agent as described. The manager's read offered under the four notes carried two riders with
it, that coverage be stated honestly rather than overclaimed and that the node 29 overlap be reported, and
**neither rider was separately endorsed**. They travel to the worker as manager notes, not as the human's
word: note 1 because a false statement is not the worker's to write whatever anyone endorses, and note 4
because `INVALIDATIONS` is already the worker's own duty to report.

**One finding about attribution, which is this node's third round in a row to produce one.** Across three
answers this human has used *"ok for the manager proposition"* for the manager's text and *"ok for
recommanded"* for the worker's `RECOMMENDED` block, naming the source by its label each time. So attribution
here was mechanical rather than a judgement — which is exactly what [What is recorded when the human takes an
option as offered](25-recording-an-option-taken.md) asks for, arriving as the human's own habit rather than as
a rule the workflow imposed. Set against the one reply earlier in the same session that named nothing and had
to be placed by content, the difference is that a reply naming a **label** is placeable and a reply naming
only assent is not.
