# Dogfood target

Type: grilling
Status: resolved

## Question

Which real effort is the workflow first run on, end to end?

The destination requires at least one dogfood run, so this needs an answer — and picking it early shapes the design, because the workflow should be built for the effort it will actually face first.

Candidates to weigh:

- **Itself** — use the workflow to finish the workflow. Maximally recursive and a genuine test of the revision loop, but a broken workflow cannot repair itself, and a failure is hard to attribute.
- **A separate real project** of the user's, chosen for having genuine fog and real code to write.
- **A deliberately small throwaway effort** built only to exercise the machinery. Fastest signal, weakest evidence that it works at real scale.

The answer should also state what would count as the run **succeeding** — otherwise "dogfooded once" is not checkable, and the destination has no test.

Independent of the other open issues: answerable now, and its answer constrains how much the rest can cost.

## Answer

**[Lang](/home/mathieu/projects/Lang) — and not a fresh effort inside it. Lang's existing `.scratch/spec-completion/` effort migrates onto the workflow.**

The human's framing, which is the reason this is not a greenfield run: *"I started thinking about this workflow when working on lang, idealy the current workflow should be migrated to use the new one"*. Lang is the origin of the idea, so it is the effort the workflow was implicitly designed for all along. Migrating an in-flight effort is also a **harder and more honest test** than starting clean: it has to absorb decisions already made, questions already labelled, and a resuming point already written by hand.

### Why Lang, on the facts

Lang was not chosen for convenience. It is the only candidate where the workflow's own thesis is already the project's working practice:

- **Its agenda is already a graph written in prose.** `inventory.md` holds ~130 labelled gaps (`CLASS-1`, `LIN-3`, `EFF-1`, `X-14`, plus `PRIN-*`/`REPR-*`/`REFL-*`/`TOOL-*` families), with explicit blocks-lists per gap, an ordering by fan-out, and a `Status: open / claimed / resolved` legend. The edges exist; they just are not machine-readable yet.
- **`decisions.md` is 2028 lines** of settled decisions with the author's reasoning, numbered to `D47` — so the migration imports history, not just questions.
- **Implementation is explicitly disposable.** The README: the compiler *"currently implements only a lexer and parser, and may be rebuilt from scratch as the design settles"* (5 files, 528 lines). A codebase whose owner already expects to throw it away is the ideal place to test that implementing something does not mean it is done.
- **Its ground rules restate this effort's principles.** *"Docs win over code"*; *"the implementation may be discarded and rebuilt"*; *"facts are the agent's job to look up; decisions are the author's"*; *"no invented semantics — an unanswered question stays open rather than getting a plausible answer."* That last one is [grilling discipline](../map.md) as a repo rule.
- **The conventions are already there.** `docs/agents/issue-tracker.md` defines the local-markdown wayfinding operations this graph runs on — map, child ticket, `Blocked by:`, frontier, claim, resolve. `CONTEXT.md` is a live glossary. `docs/superseded/` is supersession already practised on docs. `handoff.md` is a hand-written resuming point.
- **It supplies the first genuine research node.** `CLASS-1` — "the box" — is specified as *"stores the scope and dependencies" + a pointer to Effekt's paper*. That is an external fact to go and read, which retires the premise of the map's fog item claiming no research node was warranted because every open question was a design decision.

Rejected: **the workflow itself** (cannot be first — it must exist before it can be run on anything; and its prose deliverable rarely discovers that an upstream decision was wrong); **gw2-craft** (~1100 lines, actively committed, zero TODOs — real but thin fog, so it would likely succeed without exercising anything risky); **a throwaway** (proves the mechanics run, not that they survive a real codebase).

### What counts as the run succeeding: coverage, not completion

The human's answer, verbatim: *"I would say migrate and then try a bit of everything. The workflow is bound to evolve and improve anyway as I find new things by using it"*.

**This diverges from the recommendation and the recommendation was wrong.** The proposal was one vertical slice — a single construct from open gap to landed compiler code, with at least one earlier decision forced to change. The human chose breadth instead, and it is the better test for two reasons. The purpose of a dogfood run is to find the unknown unknowns, which breadth does and depth does not. And a *forced* revision cannot be scheduled without becoming theatre: a cascade that only fires because the test required it proves nothing about a cascade that fires on its own.

So "dogfooded once" is not "Lang is finished" — Lang's graph will not empty for a long time. It is **every mechanism this map has decided has been run at least once on a real effort.** That splits in two, and the split is the load-bearing part.

**Must be exercised — the manager can schedule these, and the run is not done until each has happened:**

1. **The migration itself** — Lang's decisions and gaps imported, per [Adopting an in-flight effort](18-adopting-in-flight-effort.md).
2. **All five node types**, at least once each. Lang guarantees material for every one: *research* (`CLASS-1`'s Effekt paper), *prototype* (syntax to react to — `REG-2` has two competing surface forms in the docs already), *grilling* (~130 gaps), *task* (the migration), *implementation* (compiler code for a settled construct).
3. **The relay** — a subagent pauses mid-interview, its question reaches the human carrying `ABOUT` and `SO FAR`, the answer returns verbatim, the subagent resumes. Per [Relay protocol](08-relay-protocol.md).
4. **At least one of the four human redirects**, used because the human genuinely wanted it, not to tick the box.
5. **Concurrency** — two HITL interviews live at once, and the exclusive code slot respected while an implementation node holds it. Per [Concurrency model](04-concurrency-model.md).
6. **An implementation node with a spawner-written acceptance condition, checked by an independent reviewer** before it resolves. Per [Node type taxonomy](07-node-type-taxonomy.md).
7. **Code actually landing in Lang's repo**, under whatever [Git and code-landing policy](11-git-and-code-landing.md) settles.

**Must not be faked — recorded when observed, and recorded as *not yet observed* when not:**

8. **Supersession of a node that already holds work.**
9. **A cascade pass** repointing edges after a decision changed underneath them.
10. **A death-and-respawn recovery** from the node's relay log.
11. **Termination.** Lang's graph will not reach an empty frontier during the run, so an exhausted frontier is only testable if a bounded sub-effort is scoped inside it.

    **Updated by [Done-ness and termination](10-done-ness.md): this stops being a Lang problem.** The human will also run the workflow on *"some other projects (not on this machine, for my work), which will finish"* — so termination, the final sweep, the completion report and a human closing an effort all get observed on a genuinely bounded effort, without manufacturing one. Two alternatives were considered and rejected: scoping an artificial sub-effort inside Lang, and narrowing Lang's own destination until it terminates — the second being exactly the theatre this criterion exists to prevent. What it adds instead is a coverage requirement nobody had written down: **the workflow must survive a repository this machine has never seen**, on a stack it cannot assume.

Items 8–11 are where the design is least proven, and the honest position is that the dogfood run may end without evidence on some of them. **Recording "not yet observed" is a result, not a failure** — it says exactly which parts of the design are still only reasoned about. Faking any of them would destroy the only signal the run produces.

### The run's second output

Because the workflow *"is bound to evolve and improve anyway"*, the run produces two things: changes to Lang, and **a record of the friction found while using it**. Without somewhere to put the second, the most valuable output of the dogfood is the one that evaporates. That mechanism is [Workflow self-improvement during use](19-workflow-self-improvement.md).

### Consequences

- **Two new nodes:** [Adopting an in-flight effort](18-adopting-in-flight-effort.md), which the dogfood cannot start without, and [Workflow self-improvement during use](19-workflow-self-improvement.md).
- **Scale is now a known number, not a guess.** ~130 nodes with ~40 plausibly unblocked at once, against a graph that has so far only been reasoned about at 17. **Corrected by [Graph file format](13-graph-file-format.md), which counted instead of estimating: 179 distinct gap labels across 188 inventory rows in 13 families, 43 settled decisions (not ~47), and 48 further rows in `consistency.md` that may or may not become nodes.** The "~130" here was an estimate that three later nodes then reasoned against; the corpus is a third larger, and every scale argument on this map holds *more* strongly rather than less. The `PRIN-*`/`REPR-*`/`REFL-*`/`TOOL-*` families named above do not appear in `inventory.md`'s own tables, so they live elsewhere in the effort and the migration will have to find them. This lands hardest on [Human-initiated steering](16-human-steering.md): wayfinder's inherited "first by number wins" is defensible at 17 and indefensible at 130 — and Lang's inventory already orders by **fan-out**, which is evidence about what the right policy is.
- **Correction to the map's Notes:** the `git init` prerequisite is already satisfied. `graph-agent` is a git repository with all graph files tracked under commit `cf7e549 start`. Separately, the code that lands during the dogfood lands in **Lang's** repository (56 commits), not this one — which is the repo [Git and code-landing policy](11-git-and-code-landing.md) actually has to work in.
- **The migration is not a pure copy.** `inventory.md` audited `docs/` at 538 lines; `docs/` has since been restructured into `docs/spec/` and `docs/superseded/`, and decisions have reached `D47`. Some gaps are already answered, so the import has to reconcile rather than transcribe — which is [Adopting an in-flight effort](18-adopting-in-flight-effort.md)'s hardest part.
