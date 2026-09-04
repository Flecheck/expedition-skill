# What the manager works on next, and how the human redirects it

~~# Human-initiated steering~~ — **renamed at resolution**, as this node's own text reserved: *"A better name
is this node's to choose when it resolves."* Its worker's reason, in its words: *"The heading changes; the
file stays at `nodes/16-human-steering.md`, because every link in the graph points at that path and
repointing them all to fix a name on a resolved node buys nothing — the name's remaining job is letting a
reader of `decisions.md` judge relevance, and the new heading does that."* Finding 15 of [Friction from
running this map by hand](24-self-hosted-friction.md) was that the old name covered the override and hid the
policy. Prose elsewhere in the graph still says the old name, which is the never-delete rule rather than
drift.

Type: grilling
Status: resolved

## Question

How does the human say what they want to work on next, rather than only answering what they are handed?

> **This node owns prioritisation, not just the override.** Stated up front because the name does not say
> so and that cost something real: the human proposed creating a separate node for *"priorisation of
> work, as just taking issues in order is not good enough"* while this one sat on the frontier already
> holding it — recorded as finding 15 of [Friction from running this map by hand](24-self-hosted-friction.md).
> Two questions, one node: **what the manager picks by default**, and **how the human overrides it**. A
> better name is this node's to choose when it resolves; renaming is free while a node is unstarted.
>
> One thing the human added that this node did not have: prioritisation should be able to **raise flags
> earlier** as a deliberate choice rather than leaving them to the closing report. The bullet added by
> [Done-ness and termination](10-done-ness.md) below has the *class* of thing right; what is new is that
> the friction record measured the consequence — 15 outstanding flags, 0 settled, across 24 nodes, so
> flags are write-only in practice and not merely in theory.

Surfaced by [Relay protocol](08-relay-protocol.md). "Ask me later" turned out not to be a pause but an act of **prioritization** — in the human's own words, *"if I want to work on something else, if there is something more important."* Declining the question in front of them is only half of that act. The other half — saying what they want instead — has no mechanism anywhere in the graph.

This is the **inverse direction of the relay**, and the one direction the design has never specified. [Concurrency model](04-concurrency-model.md) sizes the HITL budget, [Relay protocol](08-relay-protocol.md) routes questions from subagent to human and back, but nothing lets the human reorder the frontier.

Open:

- Can the human **pull a specific node forward**, and what happens to the interviews already in flight — do they park, or finish first?
- Can the human ask **what is banked and waiting**? Parked nodes now carry answers they already paid for, and a deferral they cannot see again becomes invisible debt.
- Does the manager's node choice become a **recommendation** the human can override, or does it stay the manager's call with steering as an occasional interrupt?
- The relay streams questions in arrival order rather than an order the human chose (finding `F4`). Is steering the answer to that, or is question **batching** a separate mechanism — offer several at once and let the human pick which to answer?
- What stops steering from starving nodes the human finds dull but the destination needs?

Sharpened by [Dogfood target](09-dogfood-target.md), which turns the third bullet above from a footnote into this node's main business. The first real effort is Lang: **~130 nodes, with roughly 40 plausibly unblocked at once.**

- **Wayfinder's inherited "first frontier node by number wins" is defensible at 17 nodes and indefensible at 130.** Numbering records the order questions were thought of, which at that scale is noise. So the manager needs an actual selection policy, and this node owns it — steering is the override, but there has to be something to override.
- **There is already evidence about what the policy should be.** Lang's `inventory.md` orders its gaps by **fan-out** — "ordered by fan-out: these block the most other gaps" — and names ten foundational ones on that basis. A human solving this problem by hand reached for blocking-count, not sequence.
- **At 40 unblocked nodes, the human cannot hold the frontier in their head**, so "pull a node forward" presupposes a way to ask *what is available* — which binds this node much more tightly to the map's *how the human sees graph progress* fog than the paragraph below assumed.

Added by [Done-ness and termination](10-done-ness.md):

- **There is a new class of thing the human may want to pull forward: a flag.** Assumptions an implementer decided for itself accumulate freely and cost nothing until the effort ends, which is deliberate — but it means a month-one guess goes unexamined until month six, with everything built since resting on it. So the second bullet above, *"can the human ask what is banked and waiting"*, now has **two** answers to give: parked nodes and outstanding flags.
- **A third face of the same problem now exists:** [Human review of landed code](20-human-code-review.md). This node is control over what gets worked, the fog item below is the graph view, and that node is the code view. Whether the human reaches all three through one surface or three separate ones is worth deciding once rather than three times.

Added by [Graph file format](13-graph-file-format.md), which supplies the mechanism this node's third bullet was missing — and it came from the human, unprompted, while deciding the format:

- **`Labels:` is a subset selector.** An optional multi-valued field naming the *family* or *part* a node belongs to, so the human can say *"work only on effects"* or *"only the first part of this feature"*. That is a **different axis from priority**: fan-out ranking orders the whole frontier but cannot express *not that area at all*, which is why this node had no answer for scoping. Both are now available and this node has to decide how they compose — does a label filter the frontier before ranking, or is a label itself a priority signal?
- **It arrives with real structure to select over.** Lang's 13 gap families become the vocabulary, and 38 of its 179 gaps are cross-cutting `X-*` entries that carry two labels each — so those surface under either area rather than being findable only by number.
- **A constraint that lands on this node:** labels are a filter and never structure. The format forbids inferring order from them, so *"do all `CLASS` before `LIN`"* cannot come from the label field — if the human wants that, this node has to give them a way to say it.
- **Two of the three "what is banked and waiting" answers are now readable files** — [flags.md](../flags.md) holds every outstanding flag with its state, and a parked node is detectable as `Status: open` with a non-empty `## Interview`. So the *asking* half of that bullet is mechanically satisfied; what remains is whether the human reaches it by asking the manager or by reading.

- **A third claimant on the human's attention**, added by [Git and code-landing policy](11-git-and-code-landing.md): an implementation node now ends in a gate where the human reviews the diff before it is committed. It is short compared with an interview, but it is the only claim that **holds a lock while it waits** — every other implementation node is blocked behind it. So whatever this node decides about how the human's attention is allocated, the gate is not just another queue item: deferring it has a throughput cost the interviews do not have, and a steering mechanism that cannot express *"the gate first"* will strand code work behind an unread diff.
- **One more thing the manager must be able to report:** which node, if any, is awaiting approval. That is the single blocking item in the whole system at any moment, and it is invisible in the graph files — the node reads `claimed` like any other.

Related but deliberately left in the map's fog: *how the human sees graph progress*. Steering is useless without a view to steer from, but the view is a presentation question and this is a control question.

## Annotation

Added by [Naming](14-naming.md).

- **The thing the human most needs to ask for by name now has one.** The **gate** is the step, **approval** is their yes, a **correction round** is one cycle of fixing. So *"the gate first"* — the steering expression this node was told it needed, since the gate is the only claimant holding the code slot while it waits — is sayable in the workflow's own words instead of described.
- **`promote` covers both halves of "what is banked and waiting".** A parked node holds banked answers; an outstanding flag is promoted into a node. One verb turns either into work.
- The **manager** may be overridden but never answers for the human — now a glossary guarantee rather than a convention, which matters here because steering is the one place the human's instruction and the manager's judgement compete directly.

## Annotation: the first fragment of the selection policy is decided, and it was not decided here

Added by [When an AFK worker cannot proceed](23-worker-cannot-proceed.md).

- **A blocking raise outranks grilling work.** The human's words: *"the manager should priorise answering the
  worker instead of continuing working on grilling (ask the user to do it)"*. So this node inherits one fixed
  rule rather than a blank sheet — and it is a **pre-emption** rather than a ranking: the manager stops
  feeding the human's queue and asks.
- **There are now two claimants that hold the code slot while they wait**, not one. The paragraph above says
  the gate is the only one; a blocked worker is the second, and unlike the gate it can arrive at any moment.
  Both have to be expressible as *"that first"*.
- **A third thing the manager must be able to report**, alongside *which node awaits approval*: whether a
  worker is blocked on a raise. Same property that made the first one worth naming — it is invisible in the
  graph files, because the node reads `claimed` like any other.

## Annotation: a second fragment of the queue discipline, and it refuses one of this node's own candidates

The human's instruction, `verbatim`, given unprompted while [Cascade pass mechanics](15-cascade-pass-mechanics.md)
held a live question, [The checker's spawn carries the effort's ground
rules](42-checker-spawn-carries-ground-rules.md) had just passed its gate, and this node was about to be
claimed:

> When the user is answering something, don't replace it by something else but wait for the answer.

- **It settles the fourth bullet above by refusing half of it.** That bullet asks whether steering is the
  answer to questions arriving in the relay's own order, *"or is question **batching** a separate mechanism —
  offer several at once and let the human pick which to answer?"* Batching is exactly putting a second thing
  in front of the human while the first is unanswered, so this instruction rules it out. What is asked for is
  the opposite: **one open question at a time**, whatever the concurrency underneath it.
- **It is a rule about the manager, not about the human's own act**, which makes it the second fragment of
  this node's policy decided somewhere else — after the pre-emption rule from [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md) in the annotation above. Both arrived as instructions to a working
  manager rather than as answers to this node, which is itself a datum about how steering actually reaches
  the manager.
- **It has a measured cause in the session that produced it.** Two claimants were live at once for the first
  time in this effort — an interview question and a gate — and the human's reply *"ok for recommandation"*
  named an option in one of the two messages and named nothing in the other, so the manager had to decide by
  content which node the reply belonged to. A queue of one makes that attribution free; a queue of two made
  it a judgement, and [What is recorded when the human takes an option as
  offered](25-recording-an-option-taken.md)'s rule for a terse reply was written for ambiguity *within* a
  node rather than *across* two.
- **The gate queues the same way, and that is in tension with what this node already records.** The
  paragraph above establishes that the gate is the only claimant holding the code slot while it waits, so
  holding a gate behind an interview question has a throughput cost that holding an interview question does
  not. One-at-a-time does not by itself say whether the order is strictly arrival or whether a gate — and,
  by the annotation above, a blocking raise — may jump the queue. This node still owes that.

## Answer

**Two rules — one for the human's attention queue, one for the manager's pick — and the human overrides either
by saying so, never by being asked.**

### 1. The attention queue: one question in front, two tiers behind

Exactly one question is in front of the human at a time. **Nothing ever replaces a live question.** The human's
instruction, `verbatim`: *"When the user is answering something, don't replace it by something else but wait
for the answer."*

Everything else waits in a pending queue ordered by two tiers:

| tier | members | within the tier |
| --- | --- | --- |
| **1** | a **gate**; a worker's **blocking raise**; the **manager's own raise** | arrival |
| **2** | a relayed **interview question** | arrival |

**Tier 1 is closed at exactly those three.** The test that produced it — *something other than this node stops
while it waits* — is the rationale and **not an extensible rule**: adding a fourth member is a decision, not an
inference. Without that closure the phrase quietly grows to cover anything.

**Three things are not claimants at all**, and a reader will look for them. **Flag settlement** rides the human
moment that already ends its node — a grilling node's last answer, an implementation node's gate — so it never
queues on its own. A **death notification** (*the worker for node NN died, your answer is recorded*) awaits no
answer. The **closing report** ends the effort rather than taking a turn in it.

**This reconciles two of the human's instructions without either losing.** Node 23's *"the manager should
priorise answering the worker instead of continuing working on grilling (ask the user to do it)"* is about what
the manager does **next**; the instruction above is about what is **live**. Pre-emption therefore acts on the
**queue** and never on the live question. Node 23 is not contradicted: it says the manager stops *feeding* the
queue, which is exactly what tiering does.

**Every relayed question names, in one line, whatever else is waiting** — by node name and kind only, never
restating the other question or its options. Two reasons, and the second is the load-bearing one. It is what
lets the human know there is a gate worth parking for, which is what makes the never-displace rule cheap. And
keeping it to a name and a kind is what keeps a terse reply attributable to exactly one thing: the attribution
failure that caused the instruction was two *asked* things, and a named-but-unasked item cannot be answered by
accident. It needs no new field — it is a `MANAGER NOTES` line, drawn from context the manager already holds.

**The cost of the never-displace rule is bounded to one answer's latency**, and the human holds the release
valve: parking the live question moves the queue on immediately.

**Waiting in tier 2 is cheap and not free.** A waiting worker holds no machine resource — measured, not
assumed — and a resume from transcript is reliable, four for four in one session. But a **stopped** worker
cannot be resumed at all, so latency on an interview is a risk rather than a free good. The tier-2 argument
survives that: the risk is a stop, which is an act, not a timeout.

**Question batching is dead**, and this closes the fourth bullet of this node's `Open:` list. Batching is by
definition two live questions. It is refused by the human's assent to a serial queue with an ordering inside
it, rather than by inference from an earlier instruction — which matters, because the earlier instruction only
literally forbade *replacing*. Node 08's *"the manager therefore chooses between streaming and batching"* no
longer has two branches.

### 2. What the manager picks: two streams, alternating over whatever capacity exists

**Fan-out is refused as the metric.** The human's own sentence contains the reason: general nodes *"will tend
to be important for the overhall design of the effort and will tend to unblock a lot"* — unblocking many is a
**symptom** of generality, not the thing to rank on. Measured on the only real graph available: **fan-out is
zero for every node on this frontier**, because everything anything is `Blocked by:` is already resolved. The
metric is empty where the distinction it was standing in for is obviously non-empty.

The frontier is read as **two streams**:

- **design** — general knowledge, running ahead. (*"For the very high level information, it should be grilled
  immediatly. For the slighy less general information you should try to be a bit ahead of the
  implementation."*)
- **delivery** — the implementation in focus, plus the specific knowledge that makes it startable. (*"For
  specific nodes, they are needed when you want to do the underlying implementation."*)

The human's *"balance between general nodes and implementation"* is the balance between those two. **Fill free
capacity by alternating between the streams, skipping a stream with nothing to offer, with a very-high-level
node pre-empting either.**

**Written over capacity `n` rather than over named slots, because the count is the human's to set** — *"the
user can ask more or less concurency from the default and it's needs to be general enough to still work."*
Alternation is what generalises: it says something sane at one slot (the higher-priority stream that has a
candidate), gives one of each at two, and three-and-two at five. It also reproduces both ends of the human's
own spectrum with **no exception anywhere**:

- **Start of an effort** — delivery has nothing to offer, so every slot goes to design. This is the current
  state of this effort, and it was confirmed independently: the manager found delivery unfillable here (four
  implementation nodes, three with no acceptance condition and the fourth's defective) and the human offered
  the same case unprompted as their first example. It is one end of a spectrum, not a hole to patch.
- **Design done or very far ahead** — design has nothing that matters yet, so every slot goes to delivery.

**Depth-first falls out for free.** One implementation in focus is a work-in-progress limit on knowledge, which
is *"you should try to do finish an implementation, not spreading the questions everywhere"*. Nothing has to be
added to get it.

**Two numbers are kept apart, having been conflated.** Interview slots count nodes **in flight**; the queue
rule counts questions **in front of the human**, which is one. Five slots at one live question means five
workers mid-node and four of them waiting — so concurrency buys **node** throughput, not **answer** throughput.
The human's answering rate is the ceiling, and slots added past it buy half-finished interviews; a parked node
is banked answers that nobody can see, which the map already calls invisible debt. That is why the default
stays near two rather than as high as it will go.

**The code slot stays at exactly one.** The variable capacity is the interview slots only.

**A `precondition` node joins whichever stream it serves**, rather than forming a third.

### 3. The readiness floor: where asking stops and building starts

**An implementation is startable when its acceptance condition can be written in full** — every demand stated
as text, with nothing deferred to an open question.

**This is derived, not invented.** A condition is already required before the node can be claimed, and node 33
already fixed it as self-contained text that never holds its demand elsewhere. So a condition whose demands
wait on an open question **cannot be written compliantly at all**. Nobody had drawn that consequence, and it is
exactly the human's constraint: *"No point in starting an implemtation if a few questions would make it
irrelevant."* A condition with a hole in it **is** that case, showing up in writing.

**It separated the day's two real cases correctly.** Node 38's design question was genuinely open and its
condition was still writable in full — and its work then passed a blind check with no part reserved. Node 41's
condition cannot be completed without deciding what `CONTEXT.md` must say, the general question behind it being
open. Ready and not-ready, told apart by a test already shipped.

**The floor has a limit, and it must be written down or the first person to lean on it will read *writable* as
*written*.** A condition can always be *made* self-contained by deciding the open question inside it by fiat.
Node 33 forbids pointing elsewhere; it does not forbid deciding. **Discharging the floor by deciding the open
question inside the condition does not pass it** — that is a decision made on the manager's own authority
reaching the graph, which is a raise or a flag, never a condition. The honest move is different and permitted:
stating properties precisely so the *worker* chooses the form.

**The residual is the manager's judgement, decided and reported.** Whether an open question would make the work
irrelevant cannot be mechanised. The pick report names the implementation being started and the open questions
judged non-fatal; the human overrides with one line. The same shape covers *"if the global design is done or
very ahead"*, which is the same judgement one level up: the manager states which stream it is favouring and
why, and the human corrects it if it has the effort's state wrong.

### 4. How the human overrides

**The manager picks and reports; it never asks.** The third `Open:` bullet is answered: the pick stays the
manager's call. Two reasons. With one question in front of the human at a time, a *"which node next?"*
confirmation would occupy the single channel that exists for real work — roughly 130 times on the dogfood
alone. And a pick is cheap to undo: an unstarted node is simply re-picked, and a claimed one banks every answer
already paid for if the human parks it.

**Steering has two forms, told apart by what the human says.**

- **A named node** — *"node 12 next"*, *"the gate first"* — is **one pick**, and expires when used. It goes to
  the front of the pending queue or takes the next free slot ahead of the stream rule. **It parks nothing**:
  under the never-displace rule, steering reorders what comes *next*, so an interview in flight is untouched
  and *"ask me later"* stays the human's separate act on the live question. This closes the first `Open:`
  bullet, whose second half — *do interviews park, or finish first?* — turns out not to arise.
- **A scope or an emphasis** — *"work only on effects"*, *"all `CLASS` before `LIN`"*, *"stay on design"* — is
  **standing**, and the manager **writes it into `map.md`'s `## Notes`**. That is the only durable home: the
  four-file rule forbids a fifth file, it is not any node's business, the region is manager-maintained and
  demonstrably survives (finding 13 of node 24), and it is read once per session by every worker. Steering held
  only in the manager's context dies with the session, and the manager compacts between nodes as standing
  procedure at ~200k per node.

**A `Labels:` scope filters the frontier before any stream rule is applied.** It cannot be a priority signal,
because the format fixed labels as a filter and forbade inferring order from them. An ordering *across* areas —
*"all `CLASS` before `LIN`"* — therefore cannot come from the label field, and arrives instead as standing
steering in the notes, which is what this node owed after node 13 removed the label field as a candidate.

**Promoting is how banked work re-enters.** The human names an outstanding flag or a parked node and it becomes
work: a promoted flag becomes a node, and a parked node returns to the frontier with its banked answers intact.
Either then enters the streams like anything else.

**What stops steering from starving what the destination needs** — the fifth `Open:` bullet. Three things, in
increasing strength. A named-node instruction is one pick, so it cannot skew anything past its own turn. A
standing instruction is **on disk and reported back in every pick it constrains**, so it cannot be silently
forgotten — the failure mode here is an emphasis nobody remembers setting, and visibility is the whole remedy.
And alternation is the default, so starvation requires the human to have asked for it explicitly and to keep
being told they did.

### 5. What the manager must be able to report

Three states are invisible in the graph files, because the node reads `claimed` like any other: **which node
awaits approval at a gate**, **whether a worker is blocked on a raise**, and **what is banked and waiting**.
The first two the manager volunteers; the third it answers on request.

**The second `Open:` bullet needs no new machinery.** Outstanding flags are `flags.md`, the graph's capped index
of every judgement an agent made alone; a parked node is mechanically detectable as `Status: open` with a
non-empty `## Interview`. The human asks the manager and the manager answers from those files — the map's
standing preference already fixes the human's interfaces as the manager's chat and the diff, not a rendered
graph.

**The pick report has grown duties from three different nodes and nothing states its contents.** That is the
shape of failure node 29 exists because of — a list that was correct about the files it knew. Collating it is
reported below as a node rather than settled thinly here, because two of the duties come from a node this one
did not read.

### 6. Consequences

- **The selection policy is judgement-based, and that has a price this node should not hide.** Reading which
  stream a node serves, and whether it is very high level, is a judgement over the node's text at pick time. So
  this policy does **not** keep open the cheap-manager door that a computable ranking would have — which bears
  directly on the map's open question about what model the manager itself needs, and on its sharp test that *if
  the scribe rule holds, a cheap manager is enough*. The human refused the mechanical metric knowing what it
  was; the cost lands here.
- **No new per-node field.** Knowledge versus implementation is read off `Type:` — `grilling`, `research` and
  `prototype` are all knowledge in the human's sense. General, specific and very-high-level are judged at pick
  time. The bounded cost is that a very-high-level node is recognised at most one pick late.
- **The manager's own skill is now unblocked**, this node having been its last blocker. It is where every rule
  above lands, there being no shipped file that carries the manager's own conduct. Its acceptance condition
  cannot yet be written in full by this node — it spans nodes this worker did not read — which under section
  3's own floor means it is not ready, and is the first case of that floor being applied after it was decided.
- **A manager note may name which of a worker's questions it believes sharpest, and may not say what it thinks
  the answer is.** Ordering a worker's own questions is squarely the manager's job — it owns the queue and sees
  across threads while a worker sees only its own — and the hard rule it must not touch is answering on the
  human's behalf. The hazard is adjacency: a note naming the sharpest question can imply the expected answer.
  The boundary is the sharpest / the answer line, and the note that raised this observed it, having said
  explicitly that the order was the worker's call and that the manager's inference was not the human's word.

## Flags

`16.1` **· settled** `ASSUMPTION` — **steering's two forms and where a standing one lives.** A named node is one pick and
expires; a scope or emphasis is standing and is written into `map.md`'s `## Notes`, including any ordering
across label scopes, which the label field is forbidden to carry. Decided on the four-file rule (no fifth
file), on the notes region being manager-maintained and measured as the one growing region that has not
decayed, and on the manager compacting between every node — steering held only in context dies with the
session. The human named neither form nor a home for either.

`16.2` **· settled** `ASSUMPTION` — **no new per-node field for the human's categories.** Knowledge versus implementation is
read off the existing `Type:`; general, specific and very-high-level are judged at pick time from the node's
text. Decided on the map's own instruction to reserve heavy design for the hard-to-reverse core: adding a field
touches that core and is hard to undo, while judging at pick time leaves it untouched and a field addable
later. The bounded cost is a very-high-level node recognised one pick late; the unbounded cost is that the
policy needs judgement and so does not keep the cheap-manager door open, recorded in the answer rather than
hidden. The human described the categories as how they think about nodes, not as a field they asked for.

`16.3` **· settled** `ASSUMPTION` — **the code slot stays at exactly one.** The human's *"the user can ask more or less
concurency from the default"* is narrowed to the interview slots. Decided because the single writer is what
makes worktrees unnecessary in v1, and raising the code slot is a change the concurrency model deliberately
deferred. Put to the human, who did not reach it, so it is neither confirmed nor refused.

`16.4` **· settled** `ASSUMPTION` — **the live question must name what else is waiting**, by node name and kind only, never
restating the other question or its options. Decided because the never-displace rule is only cheap if the human
can tell there is a gate worth parking for, and because a named-but-unasked item cannot be answered by accident
— which is what keeps a terse reply attributable. The manager had already been doing this unprompted and
nothing recorded it; it is now required, and it costs no new field, being a `MANAGER NOTES` line.

`16.5` **· settled** `ASSUMPTION` — **the readiness floor may not be discharged by fiat.** Making a condition writable by
deciding the open question inside it does not pass the floor, because node 33 forbids pointing elsewhere but
not deciding, and nothing shipped distinguishes that from the honest move of stating properties precisely so
the worker chooses the form. Adopted on its merits from the manager's rider, which the human did not separately
endorse. Without the limit written down, *writable* reads as *written*.

`16.6` **· settled** `ASSUMPTION` — **"what is banked and waiting" needs no new machinery.** Answered from `flags.md` for
outstanding flags and from `Status: open` with a non-empty `## Interview` for parked nodes, with the human
asking the manager rather than reading either. Decided from the map's standing preference that the human's
interfaces are the manager's chat and the diff rather than a rendered graph. The remaining half of that bullet
was which of the two routes the human takes, and it is settled by that preference rather than by asking.

`16.7` **· settled** `ASSUMPTION` — **a manager note may say which question it believes sharpest but not what it thinks the
answer is.** Settled on this node's own subject — what the manager may put in front of the human — after the
manager recorded that its spawn note had influenced which question was asked first and that nothing in the
design says whether that is proper. Decided permitted: ordering a worker's own questions is the manager's job,
it sees across threads where a worker sees one, and the rule it may not touch is answering on the human's
behalf. The hazard is adjacency, so the boundary is stated rather than the practice banned.

## Interview

### Attempt 1 — routing key `graph-workflow/16/a1`

**Q1, from the worker.** The human's two standing instructions collide the moment a gate or a blocking raise
arrives while they are already answering something else. Should a blocking claimant be answered **next** —
jumping ahead of any interview question already queued — while **never** displacing the question already in
front of them? Or is the order strictly **arrival**, so a gate takes its turn behind every interview question
queued before it?

The worker's recommendation: **answered next, never displacing the live question.** Two tiers — tier 1 is
anything where something *other than its own node* stops while it waits: a gate, any worker's blocking raise,
the manager's own raise. Tier 2 is an interview question, whose worker waits for free and whose node is *made
of* asking the human things. Arrival order within a tier, and nothing ever replaces what is already in front
of them.

Its argument, which is the part worth keeping: the two instructions are about **different acts**, so neither
has to lose. The instruction at [When an AFK worker cannot proceed](23-worker-cannot-proceed.md) is about what
the manager does **next**; the instruction in the annotation above is about not replacing what is **live**.
Applying pre-emption to the queue and not to the live question honours both exactly. The tier boundary is the
human's own cut — *"answering the worker"* against *"continuing working on grilling"* is the contrast in their
node-23 words. And the cost of being wrong is bounded to **one answer's latency**, the code slot idling only
as long as the one live question takes, with *"ask me later"* as a release valve that parks it and moves the
queue at once. Set aside: strict arrival for everything, which makes the node-23 instruction decorative and
can idle the code slot behind two interviews; a blocking claimant displacing the live question, which
contradicts the newer instruction and recreates the misattribution that caused it; and no rule at all, which
is what was happening the day this was asked.

**The manager's three notes, put to the human alongside Q1 and recorded here as the manager's own.**

1. **The worker's stated dependency is already practice, twice that day, and unrecorded anywhere.** It said
   its tier scheme is only safe if the live question tells the human what is waiting behind it, and named
   that as its next question. The manager had already been doing exactly that unprompted — closing node 42's
   gate payload with *"Still open and waiting on you: node 15's question"*, and again when reporting three
   nodes live. So the disclosure the worker was about to ask permission for exists as unrecorded manager
   behaviour, which is the same shape as the claim-time gathering on [Cascade pass
   mechanics](15-cascade-pass-mechanics.md): a practice with no rule behind it.
2. **Three substantive decisions were being taken on the worker's own authority while this question was
   live**, and the manager surfaced them rather than letting them arrive as flags at the end: that selection
   is **per free slot** rather than one global order; that a `Labels:` scope filters the frontier **before**
   ranking; and that *"what is banked and waiting"* needs no new machinery. The first is arguably most of the
   default-selection half of this node. The human was offered the chance to pull any of the three forward as
   its own question. **Their reply did not reach the offer**, so nothing about it is settled: the three remain
   the worker's own calls, to be returned as flags.
3. **One claim of the worker's is narrowly true and slightly misleading.** It wrote that a waiting worker
   *"costs no machine resource at all"*. True of resource and not of durability — [map.md](../map.md) records
   that a **stopped** worker cannot be resumed at all, so latency is a risk rather than a free good. The
   counter-evidence from the same day is worth as much: the manager resumed workers from transcript four
   times across one session and it worked every time.

**A1**, the human's words, `verbatim`:

> yes for recommendation

**What that endorses, quoted beside it, and attributed.** The **worker's** own recommendation above — the
two-tier scheme, pre-emption applied to the queue and never to the live question. The manager's read carried
one rider with it, that the tier-1 list be **closed** rather than open-ended so that *"something else stops
while it waits"* cannot quietly grow to cover anything, and **that rider was not separately endorsed**. It
travels to the worker as the manager's own note.

**One thing about this round rather than its content.** The question the worker chose first was the one the
manager's spawn note had named as probably the sharpest — so the manager influenced which question the human
was asked, without answering it. Recorded because nothing in the design says whether that is a proper use of
a manager note or an overreach, and this node is the one that owns what the manager may put in front of the
human.

**Q2 and Q3, and the answers to both.** Q2 asked whether the default should rank the frontier by **fan-out**,
and whether the manager should simply **make** the pick and report it. The worker recommended yes to both.
The human's words, `verbatim`:

> Yes for pick and report. for the default, I think I want something more complex. If I categorize nodes into
> different types, you have implementation nodes, knowledge nodes and knowledge nodes can be general or
> specific. General nodes will tend to be important for the overhall design of the effort and will tend to
> unblock a lot, specific nodes are needed to specify specific stuff needed for an implementation and
> implementation is implementation. I think I want to balance between general nodes and implementation. For
> the very high level information, it should be grilled immediatly. For the slighy less general information
> you should try to be a bit ahead of the implementation. For specific nodes, they are needed when you want
> to do the underlying implementation. You should try to do finish an implementation, not spreading the
> questions everywhere. Try to see how you can partition the work so that you have enough knowledge to do an
> implementation so you can learn, reduce the mental load and start to build onto it. To start an
> implementation, you don't need to be sure at 100% that it is perfect, you can modify it afterwards but you
> should have a pretty high confidence that it is correct. No point in starting an implemtation if a few
> questions would make it irrelevant. We most likely want to talk a bit more about the design.

**Pick-and-report is settled as recommended. Fan-out as the default ranking is refused**, and not on its
evidence or its cost — a richer scheme is wanted instead. The last sentence is an instruction about the
interview's own shape rather than about selection.

The manager's five notes on that answer are recorded with Q3 below, since Q3 was the worker's response to
them. The one worth keeping here: **fan-out is zero for every node on the frontier**, every node anything is
`Blocked by:` being already resolved, so the refused metric was measurably empty on the only graph available
while the general/specific distinction was plainly not.

**Q3, from the worker.** Two of the human's sentences describe choosing a **set** rather than the next node.
So: is the unit of selection **one implementation target at a time, with knowledge pulled toward it**, rather
than a node picked off a ranked frontier?

Its recommendation: **yes, and it needs no new structure**, because the concurrency model already has the
right shape. Give the three standing slots roles — the **code slot** holds the implementation in focus,
**interview slot A** holds the knowledge the next implementation target needs, pulled just in time,
**interview slot B** holds general design running ahead, and a **very high level** node pre-empts into the
next free interview slot. Then *balance between general nodes and implementation* **is** the slot assignment
rather than a ratio anyone tunes; depth-first falls out for free, one target at a time being a
work-in-progress limit on knowledge; and general-vs-specific mostly stops needing a field, because **a
knowledge node is specific when it stands between the manager and the current target**, read off at pick
time. Only *very high level* may still need marking on disk, having to be recognised when the node appears.
Set aside: a generality field on every node and rank on it; a recorded grouping construct partitioning nodes
into units each ending in an implementation; and leaving it to the manager's judgement.

**The manager's five notes on Q3, recorded as the manager's own.** (1) The relational-specificity move
dissolves the missing-field problem rather than paying for it, and means a node's classification changes over
time with nothing edited. (2) The residual *very high level* marker imports the exact cost the worker charged
against its own first alternative — classification at mint time — so it is a trade paid once rather than a
free one. (3) The scheme appeared to tighten [Concurrency model](04-concurrency-model.md) from *"roughly
two"* into exactly one of each role. (4) **Slot A is unfillable on this effort right now** — four
implementation nodes, three with no acceptance condition and the fourth's defective, so there is no
unambiguous next target to pull knowledge toward, and what happened organically is that both interview slots
went general. (5) An argument the worker did not make: one-question-at-a-time controls the **rate** of
questions and the slot scheme controls their **coherence**, so if context-switching is what *reduce the
mental load* meant, serialisation alone was never going to fix it.

**A3**, the human's words, `verbatim`:

> It's a good idea, it shouldn't be forced, for example at the start of an effort, I would still expect both
> interview slot to be general knowledge and if the global design is done or very ahead, I would expect both
> slot to be used for the next implementation. But for the default we can do this. Note that the user can ask
> more or less concurency from the default and it's needs to be general enough to still work.

**What that endorses, and what it changes.** The worker's scheme is accepted **as a default and not as a
constraint** — *"it shouldn't be forced"*. Two ends of a spectrum are given as examples: at the start of an
effort both interview slots are general knowledge; where the global design is done or well ahead, both serve
the next implementation. And a **new requirement arrives that no round had asked for**: the human may ask for
more or less concurrency than the default, so the policy must be general enough to work at any slot count
rather than being written over two named interview slots.

**Manager note 4 was confirmed independently and unprompted.** The manager reported that slot A is currently
unfillable and that both interview slots had gone general on their own; the human, without having been told
that was a defect, gave the same case as their first example. So the no-target-ready state is one end of a
spectrum the human already held rather than a hole in the scheme.

**And manager note 3 was wrong, which is worth recording because a worker was about to act on it.** The
manager reported that the scheme tightened [Concurrency model](04-concurrency-model.md)'s *"roughly two"*
into an exact structure, and suggested that was an invalidation of a resolved node. The human's refusal to
have the scheme forced, plus their statement that the concurrency number is theirs to set, means that node's
*"roughly"* survives intact and is if anything strengthened. No invalidation is owed there on this ground.

**Q4, from the worker**, after rewriting the scheme over variable capacity as instructed. Named slots are gone;
the rule is written over two **streams** — **design**, general knowledge running ahead, and **delivery**, the
implementation in focus plus the specific knowledge that makes it startable — filling whatever capacity exists
by **alternating** between them, skipping a stream with nothing to offer, with a *very high level* node
pre-empting either. That reproduces all three of the human's cases with no exception anywhere, and says
something sane at one slot and at five. The question: their last constraint was *"you should have a pretty
high confidence that it is correct. No point in starting an implemtation if a few questions would make it
irrelevant"* — **who decides that the knowledge is in, and how is that expressed**, and does the same answer
serve *"if the global design is done or very ahead"*, which is the same judgement one level up?

Its recommendation: **a mechanical floor that already exists on disk, plus the manager's judgement reported
rather than asked.** The floor is that an implementation is startable when its **acceptance condition can be
written in full** — every demand stated as text, nothing deferred to an open question. Not a new rule but a
consequence of two shipped ones nobody had connected: a condition is required before a node can be claimed,
and a condition is self-contained text that never holds its demand elsewhere, so a condition whose demands
wait on an open question cannot be written compliantly at all. The residual judgement — whether an open
question would make the work irrelevant — is the manager's, decided and reported in the pick report, which
names the implementation being started and the open questions judged non-fatal. Set aside: a standing written
instruction from the human; a per-node confidence field; asking before every implementation; and no test at
all, which is what produced a condition with a hole in it.

One narrowing the worker made and flagged rather than asked: *"more or less concurency"* applies to the
**interview slots only**, the code slot staying at exactly one, because the single writer is what makes
worktrees unnecessary in v1.

**The manager's four notes on Q4, recorded as the manager's own.** (1) The floor **reframes the manager's own
earlier finding and improves on it**: three of four implementation nodes having no condition is not an
administrative gap in the frontier, as the manager had reported it, but the readiness signal firing
correctly — and it separates the day's two real cases correctly, [Record a checker's not-covered part on
`## Review`](38-recording-a-not-covered-part.md) passing because its condition was writable in full by
stating properties even though its design question was open, and [Ship the FRICTION flag and the self-edit
disclosure duty](41-ship-the-friction-flag.md) failing because its condition cannot be completed without
deciding what `CONTEXT.md` must say, which is node 29's open question. (2) The floor's integrity rests on
something no rule enforces: a condition can always be *made* self-contained by deciding the open question
inside it by fiat, and node 33 forbids pointing elsewhere without forbidding deciding. (3) The worker
narrowed the human's own words on concurrency and flagged it rather than asking, on well-grounded reasoning.
(4) **The manager's per-resolution report has accreted three required components from three nodes and nobody
has counted them** — node 15's line naming what the cascade minted, this node's earlier line naming what
waits behind the live question, and now the implementation being started with its non-fatal open questions.
No single place says what the report contains, which is the shape of the delta-list failure node 29 exists
because of.

**A4**, the human's words, `verbatim`:

> For the question ok

**What that endorses, and one thing about its form.** The worker's recommendation as written — the mechanical
floor plus the manager deciding and reporting. This reply names **the question** rather than the source, which
is the first of this human's assents in either live node not to name a label; nothing turned on it here
because the manager's read agreed with the worker's recommendation on the substance, so both readings point at
the same text. The manager's read carried two riders — that note 2's limit be written into the answer, and
that note 4 be raised as its own node — and **neither was separately endorsed**. Both travel to the worker as
the manager's own notes.

## Annotation: two sentences of `### 1. The attention queue` are reversed or falsified

*Filed by the manager from [Whether the manager sends the human questions in
batches](117-questions-sent-in-batches.md)'s `INVALIDATIONS`, in that node's own words. **This answer is not
rewritten** — under the never-delete rule its text stands and this annotation sits beside it.*

> - *"**Question batching is dead**"* is reversed for the intra-node form. It is still correct for the inter-node
>   form, which this node refuses on that node's own ground.
> - *"Batching is by definition two live questions"* is too narrow as a definition, and being too narrow is what made
>   the conclusion above look forced. The form adopted here is **one** live payload carrying two questions, which
>   that definition does not contemplate.
> - *"keeping it to a name and a kind is what keeps a terse reply attributable to exactly one thing"* is falsified as
>   a **reason** while the rule it justifies survives on its other ground.
>
> **What that node keeps.** Its refusal of two *live* questions, its two tiers and their order, and its reading that
> node 08's manager-level choice between streaming and batching has one branch — the manager still streams.

**The manager's note.** The falsified reason is repaired by [node
127](127-manager-contract-one-payload-several-questions.md), which names it in clause 4 and keeps the rule in clause
3. **The measured failure this node recorded is what the adopted form is designed around rather than something it
overrides:** node 117's answer states that the manager performs no attribution at all, a payload coming from one
worker and its reply going back to that one worker unaltered, so the guess that failed here is never asked for.
