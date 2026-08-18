# Done-ness and termination

Type: grilling
Status: resolved
Blocked by: 06, 07

## Question

How does the manager know the graph is exhausted and the code is in its final, correct state?

The stated goal is that when the workflow finishes, "the state of the code is perfect". That has to become something checkable.

- Must the repo be **green after every implementation node** — tests passing, builds clean — or may it be transiently broken mid-graph, with correctness only required at the end?
- Is there a **final verification pass**, or is done-ness the simple absence of open nodes?
- Since implementations are revisable, "no open nodes" is not obviously stable: resolving the last node can create new ones. What makes termination converge rather than oscillate? (Wayfinder's fog graduates monotonically toward the destination; a revision loop does not obviously do the same.)
- Who declares done — the manager, or the human?
- Is "perfect" measured against the destination, against the code's own quality standards, or both?
- **Does anything verify that the cascade did not miss a node?** [Revision semantics](06-revision-semantics.md) made the cascade's scope a matter of agent judgement, deliberately accepting that an agent can miss things. If nothing ever checks, "the state of the code is perfect" rests on every cascade having been right.

- **Does an unresolved flagged assumption block done-ness?** [Node type taxonomy](07-node-type-taxonomy.md) lets an implementer land code on its best judgement and flag the assumption for the human. Those flags accumulate, and if none of them blocks, the graph can be exhausted while the code rests on guesses nobody ever confirmed.

Added by [Node type taxonomy](07-node-type-taxonomy.md), narrowing this node's job: per-node verification is settled and is **not** this node's business. Every implementation node already carries a spawner-written acceptance condition and is checked by an independent reviewer before resolving. What remains here is whether anything checks *across* nodes — the final pass, the cascade's misses, and the flagged assumptions above.

- **Do parked nodes and delegated answers block done-ness?** [Relay protocol](08-relay-protocol.md) adds two more things that accumulate quietly. A **parked** node is back to `open` with banked human answers, so it counts as an open node and the frontier is not exhausted while any exists — but nothing yet says the human must ever return to it, and "ask me later" was explicitly a prioritization act rather than a promise. A **delegated** answer is recorded as a flag and explicitly does *not* gate done-ness, which is an input that node accepted on agent judgement; if that is wrong, this is where it gets overturned. Both join the flagged assumptions above as ways the graph can empty while resting on things the human never actually decided.

Added by [Revision semantics](06-revision-semantics.md): it supplies a partial answer to the oscillation question — the supersession chain makes churn visible, chains only lengthen through completed attempts, and a session revising an already-revised lineage escalates instead. What it does not settle is whether an exhausted frontier is a *stable* state, which is this node's business.

Added by [Dogfood target](09-dogfood-target.md), which reveals that this node's central mechanism may go **untested by the first real run**:

- **Lang's graph will not reach an empty frontier during the dogfood.** ~130 open gaps, and the run's success criterion is coverage of the machinery rather than completion. So whatever this node decides about termination is only exercised if a **bounded sub-effort** is deliberately scoped inside Lang — otherwise "the manager knows the graph is exhausted" ships on reasoning alone.
- That is a legitimate outcome, recorded as *not yet observed*, but it is worth knowing in advance: of everything this map decides, termination is the piece most likely to reach the destination unverified.
- Separately, this map's **own** done-ness is now a checklist rather than an empty frontier — a distinction this node should be aware of, because it means the workflow's first user already needed two different notions of done.

Blocked on revision semantics because whether termination can oscillate depends entirely on how revision is modelled, and on the taxonomy because a verification node type would change the shape of the answer.

## Answer

**Done is a fixed point the human declares, not a milestone the manager reaches — and the fact that reframes this node is that most efforts will never be done at all.**

### Three kinds of effort, one mechanism

The human, unprompted, supplied the case this map had not accounted for: *"I will most likely test the workflow on some other projects also (not on this machine, for my work), which will finish."* So there are three shapes in play, and they differ only in whether the terminal state is ever reached:

- **Bounded delivery efforts** — the work projects. They empty, terminate, and get closed. This is where the machinery below is actually exercised.
- **Open-ended efforts** — Lang's spec completion, ~130 gaps. May never empty. **A never-emptying frontier is a legitimate steady state, not a stalled one**, and the workflow must not treat it as a defect. It follows that the workflow has to be useful *continuously* rather than only at the end, which is why the report below is a delta rather than a finale.
- **This map** — bounded, but its destination is a checklist (*skill files exist, dogfooded once*) rather than an empty frontier.

The rule underneath: **the destination decides whether an effort can terminate.** "The spec is complete" is not reachable on a schedule; "this feature ships" is. Nothing in the mechanism changes between them.

### The done test

Four conditions. Three mechanical, and the fourth deliberately not.

1. **The frontier is empty** — no open, unblocked, unclaimed node. Two consequences worth stating because they are easy to get wrong. Per [Revision semantics](06-revision-semantics.md), `superseded` does not count as `resolved`, so a dangling edge keeps the frontier non-empty instead of silently satisfying it. And a **parked** node is `open`, so **"ask me later" postpones *done*, not just the question** — which answers something [Relay protocol](08-relay-protocol.md) left hanging. The human's deferral is honoured indefinitely; the price is that the effort cannot close while it stands.

    **A third consequence, added by [Graph file format](13-graph-file-format.md):** there is now a fifth status, `out-of-scope`, and it does not satisfy a `Blocked by:` edge either — for the same reason `superseded` does not. So ruling a node out of scope **does not** close the effort by itself: anything blocked on it is left holding a dangling edge, which keeps the frontier non-empty until someone decides whether the dependent is also out of scope or was depending on the wrong thing. Scoping something out is a decision that propagates, not a way to make work disappear.
2. **The tree meets the standing bar** — below.
3. **A whole-graph sweep produces nothing new** — below.
4. **The human has read the completion report and closed the effort.**

**Only the human closes an effort. The manager never does.** Three reasons, and the first is new information: the human already reads the changes themselves, so they are not being asked to rubber-stamp something they have not seen. The destination is theirs. And the first real target's own ground rules say it outright — *"facts are the agent's job to look up; decisions are the author's."*

An **empty frontier is necessary but not sufficient**, which settles the node's second sub-question: there *is* a final pass, and done-ness is not the simple absence of open nodes.

### The standing bar — properties, not commands

The human's answer, verbatim: *"by default it should check if it builds, no warnings, formated, test passes (if relevant, if there are no test and no plan to make tests in the task, there are no tests to run). It should also follows the global and per project specific criterias if there are any. Acceptance condition should be met."* — with *"The user should be able to choose if he wants"*.

So the bar is a **default the workflow ships with**, not a line every effort must write:

- **It builds.**
- **No warnings.**
- **Formatted.**
- **Tests pass where tests are relevant.** The conditional is the human's and it is load-bearing: if the repo has no tests and the node does not plan to add any, there is nothing to run — not a failure, and not grounds for demanding a suite. If the node *does* plan to add tests, they are relevant and they must pass.
- **Global and project-specific criteria**, where any exist.
- **The node's acceptance condition is met.**

Overridable per effort when the human wants something else.

**Expressed as properties, because the commands are unknowable in advance.** This is the direct consequence of the workflow being run on work repositories this machine has never seen: a bar written as `cargo build && cargo clippy` would be correct for exactly one repo on earth. So the *properties* are fixed and shipped, the *commands* are discovered per repo on first use, and then **written once into the map's Notes** — so the next node does not re-derive them, and so the human can see and edit what is actually being run.

On the first target that discovery lands somewhere unusually thin, which is better known now than discovered mid-run: Lang has **no tests, no CI, and no test scripts** — its own `CLAUDE.md` states *"no tests exist"* and *"no custom build/test scripts exist"* — so the entire bar there is `cargo build` warning-free, `cargo clippy`, `cargo fmt`, plus its `CLAUDE.md` rules. Under the "if relevant" clause that is a **complete** bar, not a deficient one.

### Green after every node, not only at the end

The bar is checked by the **independent reviewer** at every implementation node, alongside the acceptance condition, before the node may resolve. The reasoning is stronger than a preference for tidiness:

- There is exactly **one code slot**, so the tree is never mid-edit by two agents. Leaving it broken between nodes buys nothing.
- A broken tree makes the **next** node's reviewer unable to attribute the breakage it is looking at.
- The human reads the changes **partially and continuously**. A tree that may not build at the moment they look wastes the scarcest review in the system.

Rejected: requiring a test suite to exist before any implementation node may run. On the first real target that means writing tests for a parser whose semantics are ~130 open questions from settled, in a tree whose README says it may be rebuilt from scratch — tests for code about to be deleted. The "if relevant" clause exists precisely so this does not happen.

### "Perfect" is measured against both, and there is no global oracle

The node asked whether "perfect" is measured against the destination or against the code's own quality standards. **Both, and by construction rather than by a top-level judgement.** The acceptance conditions carry the destination down to each node; the standing bar carries the quality standards. Their conjunction, plus a clean sweep, is everything "perfect" ever means. There is no global quality oracle at the top of the graph, and inventing one would be the failure mode — a single agent asked "is this codebase perfect?" produces an opinion, not a check.

### The completion report, and what a flag costs

Everything this design lets accumulate quietly converges on one artifact. The human's answer, verbatim: *"The human will review the changes, at least partially. So when the job is done, it is reported to the human so that it can look at it, give the flaged stuff. The human can decide to postpone it, then create a new node."*

So: **a report, a human read, and a node only for what gets postponed.**

The report carries:

- **What landed** — the code, and the supersession chains, which are the record of where the graph kept rubbing.
- **The bar's current state.**
- **Every outstanding flag** — assumptions an implementer decided for itself, acceptance conditions an implementer flagged as wrong, and **delegated answers** where the human said "you decide".
- **What the sweep found** — dangling edges, resolved nodes whose code no longer matches, coupling the graph never recorded.
- Scoped to **what the human has not already seen.** Because they review continuously, the report is a delta, not a replay. On an open-ended effort a report covering six months of changes would be unreadable, which is exactly the case the design has to survive.

The human's four moves on it: **accept**; **settle a flag on the spot**; **postpone → which creates a node**; or **reject what landed**, which is a revision and belongs to [Revision semantics](06-revision-semantics.md).

**A node is therefore the deferral device, not the confirmation device.** That is `park` from [Relay protocol](08-relay-protocol.md) applied to a flag rather than to a question, so it costs no new machinery. And it prices the human's attention the right way round: they are not marched through a mandatory per-flag confirmation round — they skim and pick — but anything they pick becomes an open node, and an open node keeps the frontier non-empty. **A postponed flag postpones done.**

Rejected on the human's instruction: a sweep that automatically batches every flag into a mandatory confirmation node. It forces a round the human may not want, and the deferral mechanism they described does the same job while leaving the choice with them.

This **narrows** [Relay protocol](08-relay-protocol.md)'s judgement call rather than reversing it. A delegated flag still does not gate the frontier — and it does appear in the report, so no delegated answer reaches a closed effort unseen.

### The final sweep, and why oscillation needs no counter

There is a final pass, and it is not new machinery: it is **the cascade agent run with the whole graph as its scope and no triggering revision.** [Revision semantics](06-revision-semantics.md) already built an agent that walks the graph and reads the repo looking for things that no longer agree; the sweep is that agent with the bound taken off. Its mechanics belong to [Cascade pass mechanics](15-cascade-pass-mechanics.md).

That gives termination a **fixed-point** shape rather than a finish line:

> frontier empties → sweep → sweep creates nodes → work them → sweep again → clean → report → human closes.

And it settles the oscillation question with no budget and no depth counter, matching [Revision semantics](06-revision-semantics.md)'s choice to make friction *visible* rather than capped: **every sweep round appears in the report.** A graph that keeps producing work at the sweep simply never gets closed, and the human can see precisely why, round by round. Because only the human closes, an oscillating effort cannot terminate by accident — so nothing needs a counter to stop it.

### Does anything check the cascade did not miss a node

[Revision semantics](06-revision-semantics.md) accepted that an agent can miss things and left this question here. The answer is **no audit agent** — a second agent judging the first is the same judgement risk restated, with no ground truth to appeal to. Three real backstops instead, in increasing order of what they can catch:

1. **The standing bar** catches every miss that breaks the build, warns, or fails a test.
2. **The mechanical check** catches dangling and superseded edges — precisely the read-only `check` command [Graph state mechanism](05-graph-state-mechanism.md) named as the first thing to extract.
3. **The human reading the changes** is the only one that can catch code coupling the graph never recorded. It exists as a backstop because the human said they do it, not because the design asked them to.

**The named residual risk:** a semantic miss, in code that builds cleanly, in a file the human did not happen to read. Nothing here catches that. So the honest reading of *"the state of the code is perfect"* is **nothing known-wrong is outstanding** — not *nothing is wrong*. That is the strongest claim this design can support, and claiming more would be the kind of invented certainty the first target's own ground rules forbid.

### Consequences

- **One new node:** [Human review of landed code](20-human-code-review.md). The human's own review turns out to be load-bearing — it is the done test's fourth condition and the only backstop for an undeclared-coupling miss — and nothing in this map said how they see what landed, at what granularity, or what happens when they reject it. Blocked by [Git and code-landing policy](11-git-and-code-landing.md), because how landed code can be shown depends on whether it lands as commits, a branch, or working-tree edits.
- **Termination will be observed after all**, off this machine, on bounded work efforts — so [Dogfood target](09-dogfood-target.md)'s coverage item 11 moves out of "may end unobserved". No bounded sub-effort needs manufacturing inside Lang, and narrowing Lang's destination to make it terminate was rejected as exactly the theatre that answer ruled out.
- **A portability constraint the map did not have:** the workflow will be run on repositories this machine has never seen. Promoted to the map's Notes. It is why the bar is properties-with-discovered-commands, and it means no part of the design may assume this repo, this machine, or a toolchain.
- [Cascade pass mechanics](15-cascade-pass-mechanics.md) inherits the sweep — same agent, unbounded scope, no trigger, and it must collect flags.
- [Graph file format](13-graph-file-format.md) must make flags **mechanically collectable**, since the sweep gathers them, and holds the discovered bar in the map's Notes.
- [Subagent context contract](12-subagent-context-contract.md) must carry the bar to implementers *and* to the reviewer, who now checks two things rather than one.
- [Relay protocol](08-relay-protocol.md)'s delegated-flag input is narrowed, not overturned.
- [Naming](14-naming.md) inherits four terms: the **completion report**, the **sweep**, the **bar**, and **postpone**.

## Annotation: "landed green" now has a mechanism, and the human's reading is no longer optional

Added by [Git and code-landing policy](11-git-and-code-landing.md):

- **Every commit the workflow makes has passed the reviewer and the human**, because the commit *is* the approval. So "landed green" stops being an intention and becomes a property of the history: `git bisect` over an effort stays meaningful, and the human is never asked to look at a tree that does not build.
- **The fourth done condition got stronger than this answer assumed.** *"The human will review the changes, at least partially"* was read here as partial coverage; with a per-node gate, coverage is structurally **complete at the node level** and only the *depth* of each reading is the human's discretion. The residual-risk argument survives — a skim still misses semantic coupling — but the risk is now depth-shaped rather than coverage-shaped.
- **A fifth thing can block an effort**, and it is not a decision: an implementation node awaiting approval holds the exclusive code slot. Done is unaffected in principle — the frontier is non-empty either way — but an effort can now be idle on the human in a place that looks like progress.
- **Not committing the graph is safe only because of the append-only rule.** The workflow commits code, not bookkeeping, so history holds no snapshot of the graph at landing time and "why was this written?" is answered by the node file as it stands. That is sound exactly because a node file never loses what was true earlier.

## Annotation: `done` is gone as a word

Added by [Naming](14-naming.md).

- **`done` was doing triple duty** — a node being answered, an effort being over, and this map's own checklist — so it is refused outright, with `finished` and `complete`. A **node resolves**; an **effort is closed**. Two objects, two words, and only the human closes one.
- **`completion report` → `closing report`**, following `closed`.
- **`postpone` → `promote`.** Turning a flag into a node is the same act as turning a note of friction into one, which is what [Workflow self-improvement](19-workflow-self-improvement.md) asked for; one verb now covers both.
- **`sweep` survives, re-derived.** It was distinguished from `cascade` only by scope, which this node itself called thin ground for two words. The honest distinction is purpose: a cascade propagates a change it knows about, a sweep looks for changes nobody propagated. Same machinery, opposite direction.
- **`the bar` keeps its bare form.** *Quality bar* is redundant, and *default checks* is actively wrong: this answer made the bar a set of **properties** whose commands are discovered per repo, so a name saying "checks" would invite hardcoding the commands it deliberately refused to hardcode.

## Annotation: when a flag is paid for

Reported as an invalidation by [Whether flags.md survives the settle-at-close
practice](27-does-flags-file-survive.md), and **caused** by [Write the worker contract
skills](22-worker-contract-skills.md)'s gate rather than by that node.

This node's *"flags cost nothing until the report"* no longer holds. The human's instruction at that gate
made the manager **settle a node's flags as it closes that node**, on the ground that while the node is
still open the work is still there, so acting on a flag is cheap. A flag is therefore paid for at its own
node's close, and eleven of eleven, then four of four, then four of four were settled that way.

What that leaves for the **closing report** is the exception rather than the rule: flags raised before the
practice existed — twenty of them, permanently unreachable at a close since their nodes are resolved — and
flags from the two node kinds that never end in front of the human, a `research` node and an AFK
`precondition` node. Everything else has been settled already.

**This node's four human moves on the report stand unchanged**, as does its definition of the report's
contents and its rule that a promoted flag postpones closure. Only the claim about *when* a flag is paid
for is contradicted.
