# When an AFK worker cannot proceed

Type: grilling
Status: resolved

## Question

How does an AFK worker — an implementer or a checker — tell the human that the node's premise is broken,
and what happens to the node while it waits?

Raised by the human as steering, verbatim: *"One think that would be good is if the implementor or the
checker can also raise when the plan can not be followed, some asumption was wrong or if the
implementation is more complex than expected, some important suposition is wrong, ... They shouldn't be
able to close the node by themself but can raise the issue to the user."*

**The second sentence is already guaranteed and needs nothing.** A worker writes no graph file
([Subagent context contract](12-subagent-context-contract.md)), the manager is the graph's only writer,
and resolving is the manager's act on a handover. No worker can end its own node today.

### Four named cases, three existing destinations

The human's list is not one thing. Each case already has somewhere to land; what none of them has is a
way to *get there from inside a running worker*.

| what the worker hit | where the graph already sends it |
| --- | --- |
| the plan cannot be followed | the node's own premise is wrong — supersession, or the early form of [Human review of landed code](20-human-code-review.md)'s `reject` |
| an assumption was wrong | an **upstream decision** is wrong — a revision, and a cascade ([Revision semantics](06-revision-semantics.md)) |
| an important supposition was wrong | same, and whether it is distinct from the previous row is this node's to decide |
| more complex than expected | the node is too coarse — the escalation [Node type taxonomy](07-node-type-taxonomy.md) already owns |

What unifies them is not the remedy but the worker's position: **it cannot act on any of them, and it
cannot honestly continue without an answer.** That is the property a single channel is for, and it is why
this is one node rather than three.

### Most of the mechanism exists; what is missing is permission and a threshold

[Relay protocol](08-relay-protocol.md) built the channel and [Subagent context
contract](12-subagent-context-contract.md) fixed its payload: the **question** variant, carrying the
node, `ABOUT`, `SO FAR`, `ASK`, `RECOMMENDED` and `ALTERNATIVES`, with the human's answer returning
verbatim, the four redirects supported, lazy death detection, and **park** as an outlet. That node then
closed it off in three words — *"HITL types only"*. Lifting that clause is most of what the human asked
for.

So the open work is not the channel. It is:

- **The threshold.** [Node type taxonomy](07-node-type-taxonomy.md) fixed that implementation *"never
  asks live: small ambiguities are decided and flagged, genuine forks become grilling nodes."* The flag
  and the new node are both **deferrals** — a flag costs nothing until the effort closes, and a new node
  joins the frontier. Neither reaches the human now. This node has to say where the line falls, and the
  failure mode is not caution but noise: a worker that raises on every mild surprise destroys the AFK
  property the taxonomy exists to protect, and floods the queue of the resource the whole map calls
  scarce. The cheap instrument is probably the same one the relay already uses — the worker must state
  `RECOMMENDED`, so a raise it can answer itself is a flag by construction.
- **The code slot.** An implementation worker holds the **exclusive** code slot. If it can now block on
  the human mid-node, the slot has a *second* way to sit idle waiting on attention — and [Git and
  code-landing policy](11-git-and-code-landing.md) already named the gate as *"the only claimant that
  holds a lock while it waits"*, which would stop being true. Park exists and returns a node to `open`
  with its answers banked, which frees the slot; whether an implementer that parks discards its
  half-written code, or leaves it and blocks everything, is the sharpest question here.
- **The checker has no variant at all.** [Subagent context
  contract](12-subagent-context-contract.md) gives it exactly `PASS` or `FAIL`, and nothing else. Yet it
  is the **only** party that ever reads an acceptance condition cold, with none of the reasoning behind
  it — so it is uniquely placed to notice a condition that is incoherent, unmeasurable, or contradicts
  itself, and it currently has no way to say so. Adding a third return is a genuine addition to that
  node's answer, recorded there as an annotation once decided.
- **What the human's answer is allowed to do.** *"Carry on, the assumption is fine"* is cheap. But the
  interesting answers reach further than the node: rewriting an acceptance condition that a **spawning
  node** wrote and its worker may not touch; revising an upstream resolved node, which spends a
  supersession and a cascade; splitting the node; or killing it, which is `reject` before there is a diff
  to reject. Which of those the human can do from inside a raise, versus which drop the worker and become
  ordinary graph work, is undecided.
- **Where it is recorded.** `## Interview` holds relayed questions and `## Review` holds everything after
  the code lands. A raise from a mid-flight implementer is neither, or both.

### Evidence already on the record

- **The checker case has happened.** [Write the graph conventions
  document](21-conventions-document.md)'s checker found *"two ambiguities, both real"* in the shipped
  document and reported them — but only because that run was improvised under a hand-written four-phase
  protocol that invited it. Under the contract as it stands it would have had `PASS` or `FAIL` and no
  words.
- **The implementer case has happened too, and took the deferral.** That same node raised
  `CONDITION-WRONG` against acceptance condition 4 — the condition was **false**, not merely awkward —
  and shipped anyway with a flag, because a flag was the only outlet it had. Whether that was the right
  outcome is a good test of whatever threshold this node writes: it plausibly was, which means the
  answer is not simply *raise more*.
- **The gate's `reject` is this same discovery arriving later.** [Human review of landed
  code](20-human-code-review.md) fixed it as *the act of implementing surfaced something meaning the code
  should not exist*. A worker that spots that at hour one instead of at the gate saves the whole
  implementation — so this node is, in part, about moving a known outcome earlier, and the two must not
  end up with different names for the same finding.

### What this node must not quietly change

- **The worker still never resolves, and never decides.** The human's own constraint.
- **Implementation is still AFK.** If the answer makes an implementer routinely interactive, it has
  superseded [Node type taxonomy](07-node-type-taxonomy.md) rather than qualified it, and should say so
  in those terms rather than by drift.
- **The manager still answers nothing on the human's behalf.** A raise it can absorb from context it
  already holds is a **manager note** on a question, not an answer to it.

### Consequences already known

- **[Write the worker contract skills](22-worker-contract-skills.md) is blocked on this.** The
  implementation and checker contracts must both state every return variant their worker may use
  (condition 2) and may introduce no rule no node decided (condition 3), so those two of the six cannot
  be written until this resolves. It costs a second commit against a resolved node otherwise, which the
  landing policy forbids.
- Related, and deliberately distinct: [Human-initiated steering](16-human-steering.md) is the same
  channel in the opposite direction, and [Off-contract subagent output](17-off-contract-output.md) is
  about a worker that fails its contract rather than one correctly using a channel that does not exist
  yet.

## Answer

**An AFK worker gets one blocking channel — a `raise` — opened by three triggers. The human's answer
either continues that worker or stops it, and a stop saves what was built before the tree is cleaned.**

```
worker hits something wrong
    → below the threshold → decide it, flag it, the gate reads the flag
    → any one of three triggers → raise: the worker blocks, still holding the code slot
            → continue → the same worker carries on; nothing is lost
            → stop     → salvage saved, tree cleaned, slot freed, node handed back to the graph
```

`raise` is not a new word. [Human review of landed code](20-human-code-review.md) already has the manager
*raising* the gate, and that is the same verb with one meaning — **bring something to the human that stops
work until they act.** The gate is a scheduled raise of a finished diff; this is an unscheduled raise of a
broken premise. Same channel discipline, different subject, different outcomes.

### The threshold: three triggers, any one of them enough

Verbatim: *"if it is not the node scope, if the desision either would change a lot or if is hard to choose
by itself, otherwise flag and it is seen at review time"*.

| trigger | what it covers | the worker's own test |
| --- | --- | --- |
| **Not the worker's to change** | its acceptance condition, an upstream resolved node, the node's own size | *is the broken thing mine to fix?* |
| **The decision changes a lot** | a choice whose consequences reach past this node's own code | *if I pick wrong, what else has to change?* |
| **Hard to choose alone** | a genuine fork where the worker holds no defensible preference | *can I state a `RECOMMENDED` I believe?* |

They are **disjunctive** — one is enough — and they **broaden this node's own framing**. The question above
unified the four cases as *"it cannot act on any of them, and it cannot honestly continue without an
answer."* Triggers 2 and 3 do not require being stuck: a worker that *could* pick must still raise when the
pick is wide or genuinely balanced. So the threshold is about **the cost of being wrong**, not only about
being blocked, and the first trigger is the only one of the three that a worker can settle mechanically.

**Below the threshold, the flag is not a distant deferral, and the human's own clause says why** — *"it is
seen at review time"*. [Human review of landed code](20-human-code-review.md) made the gate the place flags
are settled, because there and only there the worker is still alive and still holding the code slot. So for
an implementation node the flag route costs **hours**, not the months that [Done-ness and
termination](10-done-ness.md)'s *"costs nothing until the effort closes"* implies. That is what makes a
narrow threshold safe. It is also a gap worth naming: a `research` or `precondition` node has no gate, so a
flag left there really does wait for the closing report.

**This overturns one judgement written into the question above.** [Write the graph conventions
document](21-conventions-document.md)'s implementer found acceptance condition 4 outright false and shipped
with a `CONDITION-WRONG` flag, and this node recorded that it *"plausibly was"* right. Under trigger 1 it is
a raise: a condition is never the worker's to change. The reason to prefer the raise is not the flag's
delay but the **checker**, which reads that condition cold and would have failed the work against a
condition everyone already knew was false.

### The slot: block and keep it, and the raise goes to the front of the human's queue

Verbatim: *"Block, keep the slot, the manager should priorise answering the worker instead of continuing
working on grilling (ask the user to do it)"*.

The worker stays alive, the node stays `claimed`, its half-written code stays in the tree, and no other
implementation node starts. Nothing is discarded on the way in — discarding is a consequence of the
*answer*, never of the asking. Three things follow:

- **[Git and code-landing policy](11-git-and-code-landing.md)'s claim that the gate is *"the only claimant
  that holds a lock while it waits"* is now false.** There are two, and this one is unscheduled. Recorded as
  an annotation there.
- **The manager asks rather than queues.** *"Ask the user to do it"* is an active duty: a blocking raise
  **pre-empts**, and the manager does not go on filling the human's queue with grilling questions while the
  code slot idles. This is the **first fragment of the manager's selection policy decided outside
  [Human-initiated steering](16-human-steering.md)** — that node owns the policy, and it now inherits one
  fixed rule rather than a blank sheet.
- **The pressure this puts on the code slot is the pressure that flips landing asynchronous.** [Git and
  code-landing policy](11-git-and-code-landing.md) named the trigger as the slot idling on human attention;
  there are now two ways for that to happen instead of one, so the trigger arrives sooner.

### The answer has exactly two shapes

| the human's answer | shape | what happens |
| --- | --- | --- |
| carry on as recommended | `continue` | the live worker resumes |
| take this option instead | `continue` | the live worker resumes |
| the condition is imperfect, ship anyway | `continue` | resumes, and the manager files a `CONDITION-WRONG` flag |
| here is the corrected acceptance condition | `continue` | resumes against the new condition |
| the node is too coarse — split it | `stop` | supersession by replacement nodes |
| an upstream decision is wrong | `stop` | revision plus a cascade ([Revision semantics](06-revision-semantics.md)) |
| this should not be built at all | `stop` | `reject` before there is a diff to reject |

The manager routes on which shape it received and needs no judgement to do it: a `continue` returns the
human's words to the living worker, a `stop` kills it, saves the salvage, cleans the tree and hands the node
back as ordinary graph work.

**Rewriting an acceptance condition mid-attempt is a third revision case, and [Revision
semantics](06-revision-semantics.md) named only two** — in place while unstarted, by supersession once the
node holds work. A `claimed` node with a live blocked worker is neither. It is edited **in place**, with the
old text struck through as everywhere else, and that is allowed for two reasons: the condition's author is
the *spawning node* and the human outranks it, and superseding an implementation node to fix one line of its
condition would throw away precisely the work the salvage rule below exists to preserve. `CONTEXT.md`'s
*"Its worker may flag the condition wrong but may not rewrite it"* is untouched — the worker still may not.

### Salvage: save it, do not work on it

Verbatim: *"when stoping, data that can be salvaged should be (do not work on it, just save it). If working
on the task later or if there is a new task liked what was done so that it is easier when implementing the
revised plan"*.

1. **Saved, not finished.** No tidying, no making it build, no bringing it to [the bar](10-done-ness.md).
   The instruction is literal, and it is what stops a dying worker from spending its last context on work
   that was just cancelled.
2. **The manager writes it without reading it**, exactly as it never renders a diff at the gate. The
   salvage costs the manager a command, not context.
3. **It is a diff, and it lands in the effort's own directory rather than the product tree** — 
   `<effort>/salvage/NN-<attempt>.patch`. The product tree is being cleaned to release the slot, and for the
   dogfood that tree is **Lang's repository**, where a stray untracked file would surface in the next
   `git status` as if it were live work. This is an **asset linked from the node**, not a fifth graph file,
   so [Graph file format](13-graph-file-format.md)'s four-file rule stands; `prototypes/` is the precedent.
4. **Untracked files must be captured deliberately.** A plain `git diff` of a from-scratch implementation is
   *empty*, which would make this rule silently useless in exactly the case it matters most. The manager
   marks the node's paths intent-to-add first, then diffs them, then cleans — path-limited throughout, per
   the landing policy.
5. **The pointer is inherited.** Whatever node succeeds this one — a replacement from a split, or this same
   node reopened behind a fix — carries the salvage link, which is the second half of what the human asked
   for: *"if there is a new task like what was done so that it is easier when implementing the revised
   plan."*

**This also answers an outstanding flag on [Human review of landed code](20-human-code-review.md)**, whose
`reject` cleans the tree and whose flagged guess was that the diff is *"discarded with one line offering to
keep it"*. A reject is the gate's `stop`. Salvage is saved first, always, and no offer is needed.

### The checker gets the same channel, and it costs a verdict

Not asked, because the human's steering named it: *"if the implementor **or the checker** can also raise"*.
[Subagent context contract](12-subagent-context-contract.md) gave it `PASS` or `FAIL` and nothing else, and
its *"HITL types only"* clause on the relay is what lifts.

- **Trigger 1 is the checker's characteristic case.** It is the only party that ever reads an acceptance
  condition cold, with none of the reasoning behind it, so it is uniquely placed to notice a condition that
  is incoherent, unmeasurable or self-contradicting — and it may not rewrite one either.
- **A raising checker issues no verdict at all.** That breaks a shape [Human review of landed
  code](20-human-code-review.md) fixed: the `## Review` chronology is *"one entry per run each naming `PASS`
  or `FAIL`"*. It needs a third entry kind for a run that raised instead of judging. **Fourth delta on the
  shipped conventions document.**
- **A checker's raise holds the slot too**, because the node holds it from implementation through the gate.
  Nothing special is needed.

### Where a raise is recorded

`## Interview`, and the format gains nothing. A raise is a relayed question with an answer — the same shape
as an interview turn, with the same verbatim-or-paraphrase standing and the same divergence marker — so
reusing the section costs no new heading and no new scanner rule. Two consequences:

- **An implementation node can now have a non-empty `## Interview`**, which was previously impossible by
  construction.
- **The parked detector still works, and there is an invariant keeping it working.** [Graph file
  format](13-graph-file-format.md) makes a parked node mechanically detectable as `Status: open` with a
  non-empty `## Interview`. A blocking raise is `claimed`, so it never collides. Every `stop` route also
  leaves the node either not `open` at all (superseded, out-of-scope) or `open` **with a new `Blocked by:`
  edge** (waiting behind the upstream fix) — so a stopped node is never mistaken for a parked one. That is a
  **constraint on any future stop route**, not a coincidence of these three.

### What this corrects on the taxonomy, in those terms rather than by drift

[Node type taxonomy](07-node-type-taxonomy.md) reads: *"Implementation is AFK and never asks live: small
ambiguities are decided and flagged, genuine forks become grilling nodes."* Two clauses change and the type
system does not.

- **"Never asks live" is qualified, and `AFK` is redefined to carry it.** AFK means the worker **does not
  need** the human in order to proceed — not that it **cannot reach** them. Under that reading the five
  types and their AFK/HITL assignment are untouched: a grilling node cannot resolve without the human, an
  implementation node can, and it reaches for them only when one of three triggers fires.
- **"Genuine forks become grilling nodes" moves from the worker to the human.** The worker's outlets are now
  exactly two, flag or raise. Minting the grilling node is one of the human's *answers* to a raise — which
  is the human's own constraint on this node holding: *"They shouldn't be able to close the node by themself
  but can raise the issue to the user."* A worker free to mint the node that replaces its own is deciding.

**A correction rather than a supersession**, on the precedent set last session when `REJECT` became `FAIL`
under [Subagent context contract](12-subagent-context-contract.md): the taxonomy's five types, their
deliverables, and their AFK/HITL split all stand, and only a clause inside one of them is narrowed.

**`CONDITION-WRONG` survives with a different origin.** [flags.md](../flags.md) defines it as *an implementer
judged its acceptance condition wrong but may not rewrite it*. Trigger 1 means that judgement now raises
instead of shipping quietly, so the flag stops being a worker's unilateral deferral and becomes **the record
of a raise the human answered `continue, ship it anyway`**. That is exactly the residual the closing report
should see, and it is a better flag than the one it replaces because a human has already looked at it.

### What this changes

- **[Write the worker contract skills](22-worker-contract-skills.md) is unblocked and on the frontier** —
  the map's second implementation node. It inherits four things: the three triggers, the two answer shapes,
  the salvage rule with its intent-to-add detail, and the checker's third outcome.
- **[Human-initiated steering](16-human-steering.md)** inherits one decided priority rule — a blocking
  raise outranks grilling work — plus a second claimant that holds the code slot while it waits.
- **[Git and code-landing policy](11-git-and-code-landing.md)** loses its *only claimant* claim, and its
  asynchronous-landing trigger arrives sooner.
- **[Subagent context contract](12-subagent-context-contract.md)** has *"HITL types only"* lifted and the
  checker's return set widened. Annotated there.
- **The shipped conventions document owes a fourth delta**: a `## Review` chronology entry for a checker run
  that raised instead of judging.
- **[Friction from running this map by hand](24-self-hosted-friction.md)'s finding 5** — flags are
  write-only, fifteen outstanding and zero settled — gets its first counter-example: an outstanding flag on
  [Human review of landed code](20-human-code-review.md) is now answerable, and the mechanism that answered
  it was a later node deciding the same question rather than a sweep.

## Flags

`ASSUMPTION` — **the salvage's form and location are chosen here, not stated by the human**: a `git diff`
written unread by the manager to `<effort>/salvage/NN-<attempt>.patch`, with the node's paths marked
intent-to-add first so new files appear. Inferred from the gate's pointer-not-render rule and the landing
policy's path limiting. The human said *"just save it"* and named neither form nor place.

`ASSUMPTION` — **[Node type taxonomy](07-node-type-taxonomy.md)'s *"never asks live"* is corrected by
annotation rather than supersession**, and `AFK` is redefined to absorb the change. Second time a resolved
node's settled clause has been corrected this way; if this becomes routine it is drift wearing a
correction's clothes.

`ASSUMPTION` — **the three triggers are read as disjunctive and ungated**, so a worker that *could* pick
must still raise when the choice is wide or balanced. This broadens the *cannot honestly continue* property
that made these four cases one node, and it is the reading most likely to produce the noise this node named
as the real failure mode.

`ASSUMPTION` — **rewriting an acceptance condition in place on a `claimed` node** is a third revision case
[Revision semantics](06-revision-semantics.md) does not name, permitted here on the argument that the human
outranks the spawning node. Not put back to that node.

`ASSUMPTION` — **resolved with no worker and no relay**: the manager grilled the human directly, so a node
about a worker's channel to the human routed nothing through it. Same flag every node since
[Dogfood target](09-dogfood-target.md) carries, and the reason [Write the worker contract
skills](22-worker-contract-skills.md) is now the priority.

## Interview

Three questions, all answered by the human directly to the manager. No option was taken as offered on any
of the three: each answer was a composite or an addition, recorded verbatim above in the section it governs.

1. **The threshold.** Four options offered, none marked recommended. The human took *"a mix of 1 2 and 4"* —
   composing three of them into disjunctive triggers, and declining the two-channel non-blocking variant
   entirely. Their trailing clause, *"otherwise flag and it is seen at review time"*, was not asked for and
   is what ties the flag route to the gate.
2. **The code slot.** The human interrupted before the question rendered and answered in their own words,
   taking the recommended option and adding a duty that was not offered: the manager must **prioritise**
   getting the raise answered over continuing grilling, and must **ask**.
3. **The answer's reach.** The human took the recommended two-shape option and added the salvage rule,
   which none of the three options contained. That addition reaches backwards into [Human review of landed
   code](20-human-code-review.md)'s `reject` and settles a flag left open there.
