# Revision semantics

Type: grilling
Status: resolved

## Question

When work on a later issue reveals that an already-finished issue was wrong, how is that represented and driven?

This is the crux of the whole workflow — the thing that distinguishes it from wayfinder, where a resolved ticket stays resolved. Candidate models to put under pressure:

- **Reopen** the original node — its status goes back to open, its answer is replaced. History is mutated; the graph stays small but loses the record of what was believed before and why it changed.
- **Supersede** — a new node is created that supersedes the old one via an edge. History is append-only and the reasoning trail survives, at the cost of a growing graph and a "which node is current?" question on every read.
- **Fix in place** — the discovering node simply changes the code and records what it changed. Cheapest; no graph surgery. But an invalidated *decision* then has no visible correction, and anything else that depended on it is not re-examined.

Questions the answer must settle:

- Does invalidating a node force re-examination of everything downstream of it, or only the code?
- Can a decision node be invalidated, or only an implementation node?
- What stops revision from cycling forever — is there a budget, a depth limit, or does the human arbitrate?
- Is a revision distinguishable from ordinary new work when the manager picks the next node?

Why this is heavy design rather than a quick call: the graph is a core data structure and this decision is expensive to reverse once tickets and prose depend on it. Per the project's coding principles, that earns real design effort up front.

Blocks: [Done-ness](10-done-ness.md), [Git and code-landing policy](11-git-and-code-landing.md), [Graph file format](13-graph-file-format.md)

## Answer

Two mechanisms, and which applies is decided by one test: **is there work in this node to preserve?**

- **Not yet started** — open, unclaimed, no answer, no landed code → **update in place.** The question is rewritten to reflect what was learned. No replacement node, no chain. Supersession exists to preserve work; where there is none, a replacement node is pure noise.
- **Started or resolved** — it holds an answer, or code has landed → **supersede.** Replacement node(s) are created; the old node gets `Status: superseded` and a forward pointer `Superseded by: NN, NN`.

Added by [Node type taxonomy](07-node-type-taxonomy.md): this test governs revision arriving from **outside** the node. A node that is still claimed and under its own reviewer's scrutiny has landed code but is not being revised — a rejected review keeps the node's number, identity and file, with no chain and no replacement. Without that scoping the test would fire on every review round, manufacturing a supersession chain per rejection.

Reopen was rejected, and the deciding reason is stronger than the loss-of-trail argument in the question above: **reopen silently assumes the replacement has the same shape as the original.** That is exactly false in the case that matters most, where the lesson is "that node was too coarse" — one implementation node may need to become a fresh grilling round plus three implementation nodes. Supersede is the only model in which the replacement's shape is free. Fix-in-place was rejected because it leaves the graph asserting something false.

The forward pointer is mandatory and lives on the **old** node, so a stale answer can never be read as current and a reader always finds the replacement without going looking for it. The replacement also carries `Supersedes: NN`; that back-edge is what makes "is this node a revision?" a local read, which the priority rule below depends on.

### Editing discipline

**An in-place update never deletes.** Superseded text is marked as superseded and left where it is; new text is added around it. Information leaves a file only when it is clearly wrong or the human asks for it gone. This is a standing preference for the whole effort rather than a revision-only rule — it also binds the manager when it edits the map, which is where quiet deletion would be most damaging and least visible. Promoted to the map's Notes.

### The cascade

Revision fans out through an **aggressive, AFK, agent-driven pass**. Aggressive because the destination forbids silently stale code; AFK because the human is the scarce resource and most of what a cascade visits turns out to be fine.

**Scope is agent judgement, not declared bookkeeping.** The cascade agent walks blocking-edge descendants *and* reads the repo to find resolved nodes that touch the same code without depending on the revised decision — coupling the graph never knew about, because the graph's edges record decision dependencies, not code dependencies. Rejected: a `Touches:` field on implementation nodes. It is a second edge kind maintained by hand, and it fails silently the moment one entry is forgotten. Since an agent is doing the pass anyway, it can read the actual code instead of trusting a declaration.

**Its output is queued graph edits, never a human interrupt.** Discovery is not resolution.

- A resolved node genuinely affected → superseded, with replacement node(s).
- An open node affected → updated in place, so whoever works it later is prompted with the new consideration.
- A big decision surfaced → written into the node, to be raised with the human *when that node is worked*, not now.
- New intermediate nodes — grilling, research — may be created when an implementation has to change and it is not yet clear into what.

The accepted risk is judgement: an agent can miss things. That is why the pass is aggressive rather than minimal, and it is why [Done-ness](10-done-ness.md) has to say whether anything ever checks the cascade's work.

### Edges follow supersession

A `Blocked by` pointing at a superseded node is an **error, not a satisfied edge** — `superseded` does not count as `resolved` when computing the frontier. The cascade repoints inbound edges from the superseded node onto its replacement(s); where one node is superseded by several, the dependent inherits all of them, because the replacement set collectively does what the old node did. This costs nothing extra, since the cascade already visits every affected node, and it buys a property worth having: a dangling edge becomes mechanically detectable — precisely what the read-only `check` command in [Graph state mechanism](05-graph-state-mechanism.md) would be extracted to catch.

Node identity is stable and numbers are never reused. A superseded node keeps its number forever.

### The four sub-questions

**Does invalidation force re-examination downstream, or only the code?** Downstream, aggressively — but re-examination means *an agent visits and judges*, not *the human re-decides*. Only genuine conflicts reach a human, and they arrive queued on a node rather than as an interrupt.

**Can decision nodes be invalidated, or only implementation nodes?** Both. Implementation feeding back into decisions is the entire thesis of this workflow; a version where only code could be revised would be wayfinder with extra steps.

**What stops revision cycling forever?** No budget and no depth counter. Two properties carry it, plus one rule:

- The supersession chain makes friction **visible** — it shows where the graph keeps rubbing.
- Because unstarted nodes are updated in place, a chain only lengthens through *completed* attempts. A lineage three deep means three finished attempts at one question, which is signal rather than noise.
- **Adopted on the agent's judgement rather than asked, and so the most revisable part of this answer:** a session about to supersede a node that is itself a replacement escalates to the human as a decision instead of revising again. It is the smallest thing that gives the bad case a signal, and it adds no fields.

**Is a revision distinguishable when the manager picks the next node?** Yes, via `Supersedes:` — and it changes the ordering, but only for code:

- **Code revisions take the exclusive code-writing slot ahead of new code work.** A superseded implementation means the repo holds code known to be wrong right now, and anything built on top of it compounds the problem.
- **Decision revisions queue normally** in the ~2 HITL slots. A stale decision harms nothing while it waits, since whatever depended on it is blocked anyway.

This adds no scheduling machinery: it falls out of [the concurrency model](04-concurrency-model.md), where the code slot is already exclusive.

### Consequences

- Surfaced [Cascade pass mechanics](15-cascade-pass-mechanics.md) — this answer fixes what the cascade must achieve, but not when it runs, how many agents it is, or who applies its edits.
- [Git and code-landing policy](11-git-and-code-landing.md) is now unblocked, with its revision input settled: a revision is a distinct replacement node, not an edit to the original.
- [Graph file format](13-graph-file-format.md) inherits its revision fields — the `superseded` status, both edge directions, stable identity — and no `Touches:` field.
- [Done-ness](10-done-ness.md) gains a sub-question: whether anything verifies that the cascade did not miss a node.
