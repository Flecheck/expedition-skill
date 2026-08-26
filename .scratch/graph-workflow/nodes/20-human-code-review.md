# Human review of landed code

Type: grilling
Status: resolved
Blocked by: 11

## Question

How does the human see the code that landed, and what happens when they don't accept it?

Surfaced by [Done-ness and termination](10-done-ness.md), from a premise the human stated in passing while answering it: *"The human will review the changes, at least partially."* Nothing in this map had accounted for that. The **independent reviewer** from [Node type taxonomy](07-node-type-taxonomy.md) is an *agent*, checking an acceptance condition and the standing bar; the human's own reading of the code is a different act with different powers, and it now carries real weight:

- it is the fourth condition of the done test — an effort cannot close until the human has looked;
- it is the **only** backstop that can catch code coupling the graph never recorded, which [Done-ness and termination](10-done-ness.md) named as the design's accepted residual risk.

So the design depends on it and does not specify it.

The load-bearing word is **partially**. The human chooses what to look at, which means something has to make that choice possible — a wall of diff supports no choosing at all.

- **Cadence and granularity.** Per implementation node, per batch, on demand, or only when the completion report arrives? On an open-ended effort like Lang the last option is unusable, since the report would cover months.
- **Does it block?** An implementation node currently resolves the moment the agent reviewer passes. If it instead waits for the human, the exclusive code slot is held while nobody is looking — the serialization disaster [Concurrency model](04-concurrency-model.md) exists to avoid. If it does not wait, the human reviews code that later nodes are already built on top of.
- **What is actually shown** — a diff, a written summary, the acceptance condition beside the reviewer's verdict, or just a pointer? A cheap option worth taking seriously: the manager only ever *points*, and the human reads it in their own editor and git, where they are already fluent. That costs nothing to build and may be strictly better than anything the manager could render.
- **Rejection is a different animal from the agent reviewer's rejection.** [Node type taxonomy](07-node-type-taxonomy.md) settled that a reviewer rejection is *not* supersession, because the node is still `claimed` and keeps its identity. Human rejection arrives *after* the node resolved, which makes it revision-from-outside — and [Revision semantics](06-revision-semantics.md) says that means **supersession**, with replacement nodes of any shape. Worth confirming rather than inheriting by accident, because it means a human saying "this isn't right" spends a supersession chain.
- **Which budget does it come out of?** [Concurrency model](04-concurrency-model.md) sized ~2 HITL slots over grilling, prototype and HITL tasks. Reading code is a demand on the same scarce human but is not an interview, so either it is a third kind of claim on their attention or it competes with the interviews for the same two slots.
- **What if they don't?** "At least partially" is honest about coverage. If the human reads a tenth of what landed, the residual risk is nine tenths of it — so does the workflow record *what was reviewed*, or is review an unmeasured act?

~~Blocked on [Git and code-landing policy](11-git-and-code-landing.md): what can be shown, and what "reject this" can even mean, both depend on whether code lands as per-node commits, one branch per effort, or uncommitted working-tree edits.~~

**Now unblocked — and this node is no longer about *landed* code.** Updated in place by [Git and code-landing policy](11-git-and-code-landing.md), which moved the human's review from *after* landing to *before* it, on the human's own instruction: *"when an implementation task finishes, the manager raises it to me, I review, the implementation subagent will correct until I am happy and then I commit."* The review is now a **pre-commit gate inside the node's lifecycle**, and the manager commits on approval. Four of the bullets above are answered by that, one is now wrong, and what is left is a protocol rather than a policy.

Answered, and no longer this node's to decide:

- **Cadence and granularity** — per implementation node, at the gate, every time. Coverage is therefore structurally complete at the node level; *depth* is still the human's choice, which is what "at least partially" now means.
- **Does it block?** — Yes, and knowingly: the exclusive code slot is held while the human looks. The serialization the question feared is real but bounded, because the gate is short (read a diff, approve or point) where an interview is long, and because approval and the commit are the same instant, so no *approved but uncommitted* state exists to prolong it.
- **Which budget?** — A third claimant on the human's attention alongside the ~2 interviews, and the only one that holds a lock while it waits. The map's fog claim that the HITL budget was disjoint from the code slot was corrected there.
- **What is actually shown** — partially answered: the manager raises the reviewed diff. Whether it *renders* anything beyond a pointer is still open below.

~~**Rejection is a different animal from the agent reviewer's rejection.** … Human rejection arrives *after* the node resolved, which makes it revision-from-outside — and [Revision semantics](06-revision-semantics.md) says that means **supersession**, with replacement nodes of any shape.~~ **This premise is now false, and it is the most useful thing the landing policy changed here.** The human's rejection arrives *before* the node resolves, so an ordinary correction round costs no supersession at all — the node keeps its identity, exactly as [Node type taxonomy](07-node-type-taxonomy.md) already settled for the agent reviewer. Supersession is spent only when the rejection is not a correction but a verdict that the node's whole approach was wrong, or when a change of mind arrives after the commit. Distinguishing those two is this node's work.

What remains open:

- **The payload.** What the manager raises: a pointer to the working tree, the diff itself, the acceptance condition beside the reviewer's verdict, the flags the implementer left. [Relay protocol](08-relay-protocol.md) fixed the shape of a *question* travelling from subagent to human; this is the opposite direction and a different kind of thing — a work product raised by the manager — so it needs its own shape.
- **What a correction round looks like.** The subagent stays alive and corrects, so the human's instruction has to reach it; rounds are uncapped and their record lives in the node's `## Review`. Whether a round is relayed verbatim like an answer, and whether the AFK reviewer re-runs after each one, is undecided.
- **The abandoned diff.** A total rejection leaves uncommitted work that will never land. The landing policy states that the never-delete rule governs the graph's files and not the working tree, so discarding it is permitted — whether the manager should nevertheless offer to keep it under the effort directory is this node's call.
- **Is review recorded?** Unchanged from the original question, and sharper now that the gate is mandatory: the human approving is an event the workflow could record per node, or a fact it simply assumes.

Related, and deliberately distinct: [Human-initiated steering](16-human-steering.md) is the control side of the human's attention and the map's *how the human sees graph progress* fog is the graph-state view. This node is the third face of the same problem — the **code** view — and it is the one with a decision attached, because rejecting code changes the graph.

## Annotation

Added by [Naming](14-naming.md).

- **The word `review` is the human's.** The AFK agent that goes first is the **checker**: it checks a landed implementation against a stated acceptance condition and the bar, which [Node type taxonomy](07-node-type-taxonomy.md) already required of it. The human **reviews** and **approves**. Two review-shaped steps end one node, and the names now tell them apart without a qualifier.
- **The vocabulary this node needs is settled**: the **gate** is the step, **approval** the outcome, a **correction round** one cycle — and a correction round is emphatically not a **revision**, which means supersession here. Its four open questions are untouched: the payload, what a round looks like, the abandoned diff, and whether the review is recorded.
- **`## Review` is where it is recorded if it is recorded** — that section holds everything after the code lands, from the checker or from the human.

### Added by [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md): the gate payload's flags

The payload this node fixed says the manager assembles it from others' text and never renders the diff. It
did not say **how a flag travels in it**, and the manager read the silence as permission to relay a flag's
one-line index entry. The human's instruction at that node's gate, `verbatim`:

> Also for flags, when asking the user, please explain in more detail what was done and why and the context.
> Idealy I don't have to go into the files to find out what happened and how to respond

**A flag reaches the human as what was done, why, and the context it needs to be answered — and answering it
never requires opening a file.** Neither of a flag's two existing forms is a payload: its
[flags.md](../flags.md) line is capped at one sentence by [Graph file format](13-graph-file-format.md), and
its node entry is written for a reader who already has the node open. The manager writes a third form for
the gate, and this is the same scribe-versus-render boundary this node already drew for the diff, arriving
on the one part of the payload that is not somebody else's text to lay end to end.

## Answer

**The gate has three outcomes — approve, correct, reject — and the manager *assembles* what it raises
rather than writing it.** The whole lifecycle, with this node's contribution in the middle three lines:

```
implement (AFK) → checker → [FAIL → worker corrects → checker again] → manager raises the gate
    → approve → manager commits → node resolves
    → correct → worker fixes → bar re-checked → manager re-raises        (uncapped)
    → reject  → graph edit, then the tree is cleaned; the node does not resolve
```

### What the manager raises

The human's own list, and it is shorter than any of the four options they were offered:

- **a chronology of the checker** — what it checked, what it found, and what the implementer did about
  each finding;
- **the flags the worker raised**, because those are *"things to be looked at"*;
- the node, the paths actually touched, and the proposed commit message with its `Node:` trailer;
- **a pointer to the tree. The diff is never rendered into the conversation.**

The last line is inferred rather than instructed, and the inference is that a chronology of the checker
only earns its place if the human is reading the code somewhere else. Two things make it the right
reading anyway. The human reads code in their own editor and git, where they are fluent and the manager
is not; and a rendered diff is spent from the **manager's** context, which is the one context in the
design that has to survive the whole graph. Flagged, because it is their daily experience and they did
not say it.

**No acceptance condition in the payload.** It was one of the offered options and the human dropped it,
correctly: the condition's reader is the checker, whose whole job is to hold the code against it, and a
human who has to check the condition themselves is doing the checker's work at the gate.

### The chronology is assembled, not summarized, and that is what keeps the manager a scribe

*"A summary of what happened with the checker"* is the one phrase in the human's answer that pulls
against [Subagent context contract](12-subagent-context-contract.md)'s rule that the manager pastes and
never re-authors. It is resolved by noticing that **every piece of the chronology is already text
somebody else wrote** — the checker's verdict, the worker's account of what it changed in response. The
manager lays them end to end, oldest first, and adds only separately-marked notes of its own. Ordering
pasted pieces is scribe work; rewriting them into a gloss is not.

What the human gets is therefore what happened rather than the manager's account of it — and a
chronology long enough to want shortening is a **signal, not a formatting problem**: it means the node
took many rounds, which is the node-too-coarse escalation [Node type taxonomy](07-node-type-taxonomy.md)
already owns.

### Flags are read at the gate, and that is the last moment they are cheap

The human's phrase makes the gate a flag's real audience, which nothing in this map had noticed. A flag
is a worker's judgement the human may want to revisit, and at the gate the worker is **still alive and
still holding the code slot**:

- the human may **settle a flag at the gate** — `[x]` in [flags.md](../flags.md), the flag's text
  staying where it is, exactly as the settle procedure already works;
- settling it by agreeing with the worker costs nothing further;
- settling it by disagreeing **is** a correction round, and is recorded as one.

[Done-ness and termination](10-done-ness.md) had flags settled at the closing report or promoted into a
node. The gate is a third place and a much cheaper one: overturning a judgement here costs a correction
round, where overturning the same judgement after the node resolves costs a supersession *and* a second
commit, which the landing policy forbids. So the gate is not merely *a* place flags can be settled — it
is the only place where acting on one is free.

### The three outcomes

The human's definition, verbatim: *"approve = ok, correct = change something, reject = doing the
implementation made something pop up that mean that the code will not be kept."*

**`reject` is not "this approach was wrong, try again".** That was the recommendation and the
recommendation was wrong. Correction rounds are uncapped, so *try again, differently* is a correction —
last session's split of one document into two was exactly that, and it cost no supersession. Reject is
the narrower and far more interesting case: **implementing the node taught the graph something that
means this code should not exist.** It is a discovery, not a verdict on quality.

That also retires this node's own framing of the question. It asked how to tell a correction from a
rejection and assumed the line ran through *how wrong the code is*. It does not. It runs through
**whether the code should exist at all**, which the human can answer without grading anything.

### Reject routes to a status the graph already has

A rejected node cannot stay `claimed` — a claimed node with no live worker is the death signature
[Git and code-landing policy](11-git-and-code-landing.md) reads off the tree. Nor can it return to
`open` unchanged, which would re-offer work already known to be unwanted. **What popped up decides**, and
the three cases are exhaustive over the statuses that already exist:

| what the implementation surfaced | the node becomes | machinery |
| --- | --- | --- |
| this work sits past the destination | `out-of-scope` | the map's ruling procedure |
| the node asked the wrong question | `superseded` by a replacement | [Revision semantics](06-revision-semantics.md) |
| something upstream is wrong | `open` with a new `Blocked by:` edge on the fix | ordinary blocking, so it leaves the frontier |

The enumeration is the manager's, not the human's. The third row is what earns the outcome its place: it
is the only path by which *writing code* revises a decision, which is the premise
[How much of the lifecycle the workflow owns](03-lifecycle-scope.md) exists to defend. Under a workflow
where implementation sat downstream of the plan, reject would have nowhere to route.

**The graph edit is made before the tree is cleaned**, per the standing rule that the graph is written
the moment the human speaks.

### The abandoned diff: discarded by default, with one line offering to keep it

The tree must be cleaned — the code slot is discovered from the working tree, so leaving a rejected diff
in place would read as a dead worker forever. What survives is the **discovery**, which is prose in
`## Review` and which the never-delete rule already protects.

The code itself is discarded, and the manager says so in one line as it does it: *"discarding
`<paths>` — say so now if you want the diff kept."* No round trip, no standing directory of dead work.
The reasoning is the human's own definition: under *"the code will not be kept"* the valuable artifact is
what was learned, not what was typed, and there may be no replacement node to hand it to. Under the
recommendation's weaker reading of reject — try again — saving it would have been obviously right, which
is why this is flagged rather than simply decided.

### The checker is started by the manager, and its verdicts are renamed

The human's parenthesis: *"(I guess the implementor could be the one to start the checker ? I am not
sure)"*. **Answered against the guess, on the one property that makes a blind checker worth anything:
whoever spawns it chooses what it sees.** The checker's inbound is an extracted acceptance condition, the
bar, and the diff; the implementer is the party with an interest in passing, so an implementer that
extracts its own condition can extract it favourably. Extraction is copying, which is the scribe's work
and not authoring, so it costs the manager nothing to keep.

**Their actual requirement is met anyway, and by scheduling rather than by authorship:** the manager
refuses to raise the gate until the checker passes, so the human never sees a node whose checker findings
are still open. That was the point of the guess, and it survives it.

**One exception, stated rather than hidden.** A checker that will not pass — a condition the worker cannot
satisfy, or a bar the repo cannot meet — must still reach the human, because the gate is the *only* place
an implementation node becomes visible to them. Otherwise a stuck node loops silently. The escape hatch is
the human's own payload: the chronology carries "it failed three times, here is why", and the gate is
raised on a failing tree with that stated in the first line. Flagged, since it qualifies an expectation
the human gave as a plain statement.

**The checker's outcomes are now `PASS` and `FAIL`.** [Subagent context
contract](12-subagent-context-contract.md) fixed them as `PASS` / `REJECT` one session ago; the human has
now given `reject` to the gate, and two different things called reject in the two contracts that most
have to be read together is the ambient collision [Naming](14-naming.md) killed `issue` for. The same move
that node made, one level down: **`review` and `approve` are the human's, `check` is the agent's — so
`reject` is the human's and `FAIL` is the agent's.** Free today because [Write the worker contract
skills](22-worker-contract-skills.md) is unwritten; not free once six contracts say `REJECT`.

### The correction round

Four parts, three of which were already fixed elsewhere and are recorded here only because this is the
node someone will read:

- **The human's words reach the worker verbatim**, by the scribe rule, and are written into `## Review`
  before the worker is resumed — the one ordering rule [Subagent context
  contract](12-subagent-context-contract.md) applied to both logs.
- **The bar is re-checked every round. The acceptance condition is re-checked only when the worker
  reports that its correction touched something a condition names.** The human's call. The trigger sits
  on the worker because it is the party that knows, and it has to report what it touched anyway — the
  path list is *reported, never inferred from `git status`*. The evidence this rule exists for is last
  session's: the correction that moved a section into a sibling file changed whether acceptance condition
  4's second clause was satisfied, and only the implementer's own prose caught it.
- **A worker that dies mid-round** falls to [Relay protocol](08-relay-protocol.md)'s machinery, with
  `## Review` as the replay log — already stated by [Git and code-landing
  policy](11-git-and-code-landing.md).
- **Rounds are uncapped, and the cap is on the agent rather than the human.** *"Until I am happy"* is the
  authority.

### What `## Review` has to hold

The shipped conventions document says *"everything that happened after the code landed, appended per
round: the checker's outcome, and the human's corrections at the gate."* That is loose enough to permit a
gate whose outcome is unrecoverable, so this node tightens it — a **third delta** on that document,
alongside the two the map already carries:

1. the checker's chronology, one entry per run, each naming `PASS` or `FAIL` and which of the two it
   failed;
2. each correction round numbered, with the human's words verbatim and what the worker changed;
3. **the gate's outcome named as one of the three**, and on a reject, what popped up and which of the
   three routes was taken.

Nothing beyond that. Last session's improvised `## Review` already had shapes 1 and 2 and named its
outcome in prose (*"### The gate: approved"*); what it could not do is 3's second half, because reject
did not exist yet.

### Review is recorded; its depth is not measured

Recording is forced rather than chosen: the ordering rule writes the human's words the moment they speak,
so approval and every correction are on the node whether or not anyone wanted them to be.

**Depth is deliberately unmeasured.** The workflow never asks which files the human actually read.
Coverage is structurally complete at the node level — every implementation node passes a gate — and
*"at least partially"* now describes depth alone. Asking for it would tax the scarce resource for a number
nobody acts on, and [Done-ness and termination](10-done-ness.md) already named unmeasured depth as this
design's accepted residual risk. Flagged rather than merely decided, because it is the one place the
design's own backstop is left unquantified on purpose.

### Consequences

- ~~**[Write the worker contract skills](22-worker-contract-skills.md) is unblocked**~~ — true when
  written, false within the hour: the human's steering created [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md) and that node blocks it. What stands is the rest: its
  implementation row now has the gate payload's shape, and its checker row changes one word — `FAIL`, not
  `REJECT`.
- **The gate's `reject` turns out to be one end of something larger.** [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md) is the same discovery — *implementing this taught us the code
  should not exist* — reaching the human before there is a diff instead of at the gate. The two must not
  end up with different names for one finding.
- **The glossary gains one term and two of its entries grow.** `Reject` is added; `Checker` now states
  who starts it and names `PASS` / `FAIL`, refusing `reject` for the agent by name; `Gate` states its
  three outcomes and that the manager assembles rather than renders. This is a write into the product
  tree from a grilling node, which passes no checker and no gate — it rides the `ASSUMPTION` flag
  [Naming](14-naming.md) already carries for exactly that, rather than raising a second one.
- **The conventions document owes a third delta**, recorded in the map's `## Notes` with the other two,
  since a second commit against a resolved node is what the landing policy forbids.
- **The async-landing fog item gains the thing it was missing** — a synchronous gate to be a delta on —
  and one real cost that [Git and code-landing policy](11-git-and-code-landing.md)'s *"the seam is a
  single step"* did not price: after a commit, reject cannot clean a tree. It becomes a forward revert,
  so the cheapest of the three outcomes becomes the most expensive one.
- **No new node.** Everything this answer surfaced landed on nodes that already exist, which is now true
  of the second session in a row.

## Flags

`ASSUMPTION` — **the code travels as a pointer and the diff is never rendered into the conversation.**
The human specified what the header carries and never addressed rendering; this is the manager's reading
of an answer that only makes sense if the code is read elsewhere. It is also their daily experience at
every implementation node, which is why it is flagged rather than assumed quietly. One line to overturn.

`ASSUMPTION` — **a rejected diff is discarded, with a single line offering to keep it and no round
trip.** The human defined what reject *means* and not what happens to the work. Decided on their own
definition — the artifact of a reject is the discovery, not the code — but the opposite call was
obviously right under the weaker reading of reject that was offered, so the reasoning depends entirely on
a distinction they drew in one sentence. **Answered by [When an AFK worker cannot
proceed](23-worker-cannot-proceed.md)**, where the human ruled that a stop saves what can be salvaged before
the tree is cleaned — *"do not work on it, just save it"*. A reject is the gate's stop, so it saves too, and
the offer this flag guessed at is unnecessary. Settleable in [flags.md](../flags.md) whenever the human likes.

`ASSUMPTION` — **a checker that will not pass still reaches the gate.** This qualifies the human's plain
statement that *"the issues raised by the checker should be already fixed by the impementor"*. The
qualification is forced — the gate is the only place an implementation node becomes visible, so the
alternative is a node that loops silently forever — but it is a qualification of something they stated
rather than asked.

`ASSUMPTION` — **the checker's `REJECT` was renamed to `FAIL` to free the word for the gate**, which
corrects a token [Subagent context contract](12-subagent-context-contract.md) fixed one session ago.
Done on this node's own authority because the collision is this node's creation and the six contracts
that would carry it are unwritten. An annotation records it on that node; nothing that ships says
`REJECT` today.

`ASSUMPTION` — **depth of review is never measured.** The workflow does not ask what the human read, so
the residual risk [Done-ness and termination](10-done-ness.md) accepted stays unquantified by
construction rather than by oversight.

## Interview

### The gate payload — what the manager puts in front of the human

Asked as four options: a short structured header with the code by pointer; the same plus the checker's
full report and the acceptance condition; the diff rendered into the conversation; a bare pointer.

**No option taken. Verbatim:** *"I would say a summary of what happened with the checker and the flags
as they are things to be looked at ? Note that the issues raised by the checker should be already fixed
by the impementor. (I guess the implementor could be the one to start the checker ? I am not sure)"*

Three things, and only the first was the question asked:

- **The checker travels as a summary of what happened, not as a verdict and not as a full report.** A
  narrative of what it checked, what it found, and what the implementer then did about it.
- **The flags are the part that wants the human's eye** — *"things to be looked at"*. This reprices
  them: see the answer's flags-at-the-gate section.
- **The implementer fixes what the checker found before the gate**, stated as an expectation rather
  than a preference. That fixes the loop's shape, and it is a stronger requirement than anything the
  map had written down.

**The question inside the answer — who starts the checker — is answered against the human's guess, and
the reason is blindness.** See the answer. Marked as a question rather than a divergence: they raised
it as uncertainty (*"I am not sure"*), not as an instruction.

**Rendering versus pointing is inferred rather than answered.** The human specified the header's
contents and never asked for a diff in the thread; a summary of the checker only earns its place if the
human is reading the code somewhere else. Recorded as the manager's reading of their answer.

### Whether the checker re-runs after a correction round

Asked with last session's evidence attached: the correction that split the conventions document into two
files changed whether acceptance condition 4's second clause was satisfied, and only the implementer's
own prose caught it.

**Answer: the bar re-runs every round; the acceptance condition is re-checked only when the worker
reports that its correction touched something a condition names.** The recommendation, taken as offered.
Not taken: a full blind checker every round, no re-check at all, and manager discretion.

### Whether the human can kill a node at the gate

Asked as a 2×2 — two outcomes or three, and the abandoned diff kept or discarded — with the
recommendation being two outcomes on the grounds that correction rounds are uncapped.

**No option taken. Verbatim:** *"I guess approve = ok, correct = change something, reject = doing the
implementation made something pop up that mean that the code will not be kept."*

**Three outcomes, and the third is not the one that was offered.** Both three-outcome options defined
reject as *the approach was wrong, supersede and replace*. The human's reject is narrower and sharper:
the act of implementing surfaced something meaning the code should not exist. That distinction is what
the answer is built on, and it is also what makes the abandoned diff's disposition a different question
than the one asked — so the diff was decided rather than re-asked, and flagged.

The 2×2's second axis went unanswered. Recorded as decided-not-asked in the answer.

## Annotation: the reject clause keeps its decision and loses its premise

*Filed by the manager at [Run an implementation node's work in a worktree](68-implementation-in-a-worktree.md)'s
resolution, in that worker's own words.*

> Its clause *"The tree must be cleaned — the code slot is discovered from the working tree, so leaving a rejected
> diff in place would read as a dead worker forever"* loses its premise. The slot is no longer discovered from the
> working tree, so a rejected diff left in a worktree does not read as a dead worker. **The decision it supports is
> unchanged; its reasoning is.**

**And the discard default gets cheaper on both sides**, which refines this node's `ASSUMPTION` flag rather than
contradicting its decision: discarding is now `git worktree remove --force` with no path-limited cleaning of a tree
that also holds the human's bookkeeping, and **keeping costs nothing** — the work is committed onto the unmerged
worktree branch and the directory removed, so a kept reject cannot be miscounted as an occupied slot. Node 68 notes
that keeping was defaulted against partly because it meant a standing directory of dead work, and it no longer does.
