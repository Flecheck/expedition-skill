# Human-initiated steering

Type: grilling
Status: open

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
