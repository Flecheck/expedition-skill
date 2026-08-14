# Cascade pass mechanics

Type: grilling
Status: open
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

## Annotation

Added by [Naming](14-naming.md).

- **The cascade and the sweep are now separated by purpose, not by scope.** A cascade propagates a revision it knows about; a sweep looks for revisions nobody propagated. This node owns the first and [Done-ness](10-done-ness.md) the second, and they are the same machinery run in opposite directions — which is an argument for specifying both here rather than leaving the sweep to be re-derived at termination.
- **The code-coupling query is `git log --grep '^Node: <effort>/<NN>$'`**, not a bare id. The join key carries the effort name because `NN` restarts at `01` per effort, so the cheap first pass this node inherited is exact rather than approximately right.
