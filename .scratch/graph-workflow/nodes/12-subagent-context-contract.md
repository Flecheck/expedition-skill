# Subagent context contract

Type: grilling
Status: resolved
Blocked by: 07, 08

## Question

Exactly what does an issue subagent receive when spawned, and what must it return?

A subagent starts with fresh context and cannot see the manager's conversation, so everything it needs must be handed to it deliberately. Both halves of the contract are open.

Inbound:

- The node's own question, obviously. What else — the whole graph, or just its ancestors' answers?
- How are ancestor answers passed: inlined, or as file pointers it reads on demand? (Wayfinder's "zoom as needed" pattern suggests pointers.)
- Does it get the destination and the standing notes for the effort?
- Which skills is it told to invoke — `/grilling`, `/domain-modeling`, `/naming`, `/prototype`?
- For implementation nodes: what code orientation, and what acceptance condition?

Outbound:

- The answer, in what shape? Free prose, or something structured enough for the manager to act on without re-reading?
- Whether it surfaced new nodes, and whether it invalidated an existing one — the manager cannot spot a needed revision if subagents do not report it.
- A pause-with-question, per [Relay protocol](08-relay-protocol.md), which is a different return shape from a finished answer. The contract has to cover both.

Settled by [Node type taxonomy](07-node-type-taxonomy.md), which confirms the contract does differ per type and fixes several entries:

- There are five types to write contracts for, and one extra worker that is not a type: the **independent reviewer**, which gets the node's acceptance condition and the landed code, and returns a pass or a rejection with reasons.
- An **implementation** subagent receives its acceptance condition, written by the spawning node, and may not rewrite it — but may flag it as wrong, which is part of its return shape.
- An implementation subagent **never pauses to ask**. Its outbound contract therefore needs two things a grilling contract does not: flagged assumptions it decided itself, and a request to create a grilling node when it met a genuine fork.
- **Prototype** is HITL and so does use the relay; its return links a throwaway artifact rather than reporting landed code.

**Now unblocked.** [Relay protocol](08-relay-protocol.md) was prototyped live and hands over a working first draft of both halves rather than an open question — see its [prototype asset](../prototypes/08-relay-protocol/run-1.md), which records the exact contract two real subagents were run under. What it settles:

- **Inbound context is file pointers, not inlined text.** Tested and confirmed: both subagents oriented themselves correctly from pointers to the map and the relevant resolved nodes. Wayfinder's zoom-as-needed pattern is the answer for this node.
- **The outbound question shape** — node name, the question verbatim, a recommendation, the alternatives — and the inbound answer shape, which carries the human's **verbatim** words, a **divergence** marker when the answer contradicts the subagent's recommendation, and manager notes kept separate from the human's words.
- **A third return variant: parked-with-progress.** A subagent told to stand down returns its progress as a dump, including the questions already answered and the human's words verbatim, which the manager writes onto the node. Subagents stay off the graph; the manager remains the single writer.
- **Delegated-answer marking**, for when the human said "you decide" and the subagent answered instead.
- A subagent must **report** its own new nodes and invalidations, because the manager cannot read a running subagent's transcript and so has no other way to learn of them.
- The run's `CONTEXT-PROOF` field was instrumentation and is **not** part of the shipped contract; what replaces it is a provenance marker on recorded answers.

What remains genuinely open for this node: whether a subagent gets the destination and standing notes (the run gave it the whole map, which worked but may be more than needed), which skills each type is told to invoke, and the contracts for the types the prototype did not exercise — research, task, implementation, and the independent reviewer.

Added by [Dogfood target](09-dogfood-target.md), which supplies real evidence on the open "does it get the destination and standing notes" question — and the answer is **more than the standing notes**:

- **Effort-local ground rules must reach every subagent.** Lang's are not stylistic: *"docs win over code"* where they disagree, *"no invented semantics — an unanswered question stays open rather than getting a plausible answer"*, and *"facts are the agent's job to look up; decisions are the author's"*. A subagent that does not receive these will confidently do the wrong thing while following its own contract perfectly.
- **Some sources are non-authoritative, and the contract has to say which.** Lang flags one file as *"not normative unless it is the author's own words"*, gives the exact line ranges where the author speaks, and warns that a specification document inside it *"overstates them in at least three places"*. A file pointer alone is dangerous here: pointers are how context is passed, so the contract needs a way to mark a pointer as **evidence rather than authority**.
- Same for `docs/superseded/`, which Lang keeps as a source that *"contains statements known to be false"*. A subagent handed the repo and left to explore will read it.

This generalizes past Lang: an effort has rules and a source hierarchy of its own, and neither is derivable from the node's question.

Added by [Done-ness and termination](10-done-ness.md), which adds a third thing the contract must carry and changes the reviewer's half of it:

- **The standing bar goes to two of the workers.** An implementation subagent must know it — it may not resolve leaving the tree failing to build, warning, unformatted, or with relevant tests red — and the **independent reviewer** must know it, because it now checks *two* things rather than one. That reshapes the reviewer's return: the taxonomy said it returns a pass or a rejection with reasons, and it must now say *which* failed, because "acceptance condition unmet" sends the implementer back to the feature while "bar unmet" sends it to the build.
- **The bar arrives as a pointer, not as prompt text.** Its commands are discovered per repo and recorded in the map's Notes, so this is one more entry in the pointer set — consistent with the run's confirmed finding that pointers beat inlining.
- **The contract has to work on a repo this machine has never seen**, since the workflow will be run on work projects elsewhere. So the pointer set cannot assume a fixed layout: it can name the *kinds* of thing a subagent needs — the effort's rules, its source hierarchy, its bar — but not where they live.

Added by [Graph file format](13-graph-file-format.md), which turns the pointer set from a shape into a list:

- **The graph-side pointers are now exactly three:** the node's own file, `map.md`, and `decisions.md`. That is the whole graph as far as a subagent is concerned — everything else it might need is reachable from a link inside one of those.
- **`Labels:` is what makes the third pointer usable.** Handing a subagent an index of 179 resolved decisions is not zoom-as-needed, it is inlining with extra steps; handing it the sections matching its node's labels is. So the contract's job for ancestor context is **scoping the index**, not choosing between pointers and inlining — that part is already settled.
- **`flags.md` is deliberately *not* in the set.** It is the sweep's file. A subagent that reads other nodes' outstanding assumptions starts second-guessing decisions outside its own node, which is the cascade's job and not a worker's.
- The reviewer's pointer set differs by one: it also gets the node's `## Acceptance condition`, which the format now fixes as a section rather than a field, so the pointer is a heading inside a file it already has.

Added by [Git and code-landing policy](11-git-and-code-landing.md), which gave the implementation contract an ending it did not have:

- **An implementation subagent must be resumable through human correction rounds.** It does not finish when the code is written — it finishes when the human is happy. So its context has to survive rounds of *"not like that"*, which is a longer life than an interviewer's and, unlike an interviewer, it holds the exclusive code slot the whole time. Whatever the contract is, it has to be replayable from the node's `## Review` log.
- **The manager needs the reviewed diff** to raise the gate, so the contract's *return* value from an implementation subagent is not just "done" — it is what changed, in a form the manager can hand to the human. Adjacent to [Human review of landed code](20-human-code-review.md), which owns the payload's shape.
- **What lands is a path list, not the whole tree.** The commit is limited to the paths the node touched, taken from the diff that was reviewed, so the contract has to make the subagent's own footprint knowable rather than inferred from `git status`.

Blocked on the taxonomy because the contract likely differs per node type, and on the relay because pausing is one of the things a subagent can return.

## Annotation

Added by [Naming](14-naming.md).

- **The thing this node writes a contract for is a `worker`**, named for its role rather than for the harness's `subagent` — because [Runtime host](02-runtime-host.md) is flagged as the most replaceable part of the design, and a contract named after a mechanism ages with the mechanism.
- **The glossary is now an input to the contract.** [`CONTEXT.md`](../../../CONTEXT.md) holds forty terms with their refused synonyms attached; a worker that has not read it will write `issue`, `postpone` or `done` back into the graph, which is exactly the drift the glossary exists to stop. Whether it travels as a pointer or inlined is this node's call, and the relay prototype's finding — context travels as file pointers — already leans one way.
- **One term this node needs and does not have:** the payload carrying a node's finished work *back* to the manager. The relay's inbound half is fully named; the return half has no vocabulary at all.

## Answer

One shape for every worker, with a small per-type delta. Both halves are now named: what goes down is
a **spawn**, what comes back is a **handover**.

### The spawn is a dispatch, not a briefing

```
You are a worker on node <name> — nodes/NN-<name>.md.
You are not the manager, and you have no channel to the human.

Your contract: /expedition-<type>. Invoke it and follow it exactly.

Read these. Do not trust any summary of them:
  nodes/NN-<name>.md
  map.md
  decisions.md — the <LABEL> sections
  <per-type additions>

Manager notes: <optional>
```

**The contract travels as a skill invocation, not as prompt text.** The human's call, over the
recommendation that the hard rules be copied into every spawn, and on a fact the recommendation
under-weighted: a skill invoked by name is loaded by the harness as instructions, not offered as a
file the worker may or may not open. This map's own prototype is evidence — both subagents were told
to follow `/grilling` discipline and both held it. What the manager adds on top is node-specific and
capped exactly as [Relay protocol](08-relay-protocol.md)'s F9 caps a manager note: only from context
the manager already holds.

That makes **independent invocability by name** a requirement on all six contracts, which is a
constraint on where the skill files land rather than something this node can settle. It inherits the
install-location assumption already flagged on [Write the graph conventions
document](21-conventions-document.md).

### The pointer set

Universal, and exactly the three [Graph file format](13-graph-file-format.md) fixed: the node's own
file, `map.md`, and `decisions.md` scoped by label. **Scoping a pointer is a filter instruction, not
an extract** — the contract names which label sections to read and the pointer stays a pointer.
Extracting sections into the prompt would be inlining with extra steps, which is what the relay
prototype ruled out. `flags.md` stays out of every set, as that node fixed.

**The glossary is not a pointer at all: it ships inside the contract skill.** This answers
[Naming](14-naming.md)'s open annotation with a third option it did not offer. The vocabulary belongs
to the *workflow*, not to the effort, so it has to travel with the skill to a machine that has never
seen this repo — a pointer to `CONTEXT.md` would resolve to nothing there. An effort's own domain
glossary, where it has one, is an ordinary pointer declared in the map's `## Notes`.

**The effort's ground rules and its source hierarchy live in the map's `## Notes`, and both are
optional prose.** The human's judgement, in their words: *"It seems specific to lang but I think it
should go in map.md, I belive it's not too long."* So no fifth file, no schema, and no required
subsystem for a need only one effort has demonstrated — absent any declaration, every source a worker
is pointed at is authoritative. The standing over sources is declared over **paths and globs** rather
than attached to individual pointers, because the failure mode is what a worker finds on its own:
Lang's `docs/superseded/` *"contains statements known to be false"*, and a worker handed the repo will
walk into it unprompted, having been pointed at nothing.

| type | added inbound | method skills |
| --- | --- | --- |
| grilling | — | `/grilling`, `/domain-modeling` |
| research | the sources and their standing; it may read outside the working directory | `/research` |
| prototype | `prototypes/NN-<name>/`, and that the artifact is discarded and never enters the product tree | `/prototype` |
| implementation | its `## Acceptance condition`; the bar, via the map's Notes; the paths the spawning node expects it to touch | `/coding-principles`, `/naming` |
| precondition | what must be true when it is done, and which resulting facts later nodes depend on | — |
| checker | the acceptance condition as **extracted text**, the bar, and the diff. Nothing else. | — |

Two rows are forced rather than chosen:

- **The implementer's acceptance condition is a heading; the checker's is extracted text.** Same
  content, different mechanism, because the checker is blind — the human's call — and pointing it at
  the node file would unblind it. It is the one worker whose payload cannot be a pointer. This was
  improvised under exactly that pressure on [Write the graph conventions
  document](21-conventions-document.md), where the checker was kept off the node so its reconstruction
  would count as evidence rather than an echo.
- **The paths a spawning node names are orientation, not permission.** Evidence from that same node:
  the document was split into two files *at the gate, by the human*, so any path list written in
  advance would have been wrong. A worker that writes outside the list is not in violation; it reports
  what it touched.

### The handover

Five parts, every time, with `none` written out rather than left off:

1. **Answer** — the node's `## Answer`, written as the node will hold it.
2. **Index line** — the capped `decisions.md` sentence, under its label group.
3. **Flags** — each with its marker, one line each.
4. **New nodes** — name, type, question, blockers.
5. **Invalidations** — which resolved node, and why.

The explicit `none` is there because the manager cannot otherwise tell *looked and found nothing* from
*did not look*. The prototype's contract already did this for `NEW-NODES`, and it is the cheapest
instrument in the run.

Two other variants, from [Relay protocol](08-relay-protocol.md); a worker returns exactly one of the
three:

- **question**, HITL types only — the node, `ABOUT`, `SO FAR`, `ASK`, `RECOMMENDED`, `ALTERNATIVES`.
  The worker writes `ABOUT` and `SO FAR` itself: it has read the node, and it is the only thing that
  knows its own thread. The manager adds its note and nothing else.
- **park** — the progress dump: every question already answered with the human's words verbatim, and
  where the thread stood.

An implementation worker adds a sixth *part* rather than a fourth variant: the **gate payload**, the
diff plus the list of paths actually touched. Its presentation is [Human review of landed
code](20-human-code-review.md)'s to fix. What this node fixes is that it belongs to the handover, and
that the path list is **reported rather than inferred from `git status`**, per [Git and code-landing
policy](11-git-and-code-landing.md).

**The checker returns no handover at all**: `PASS`, or ~~`REJECT`~~ **`FAIL`** naming which of the two failed —
acceptance condition or bar — with reasons. [Done-ness and termination](10-done-ness.md) fixed the
two-way split; what makes it load-bearing is routing, since condition-unmet sends the implementer back
to the feature while bar-unmet sends it to the build. A rejection goes to the implementation worker,
which holds the node, which is why the checker never needs it.

**The token was renamed to `FAIL` by [Human review of landed code](20-human-code-review.md)**, which gave
`reject` to the human as one of the gate's three outcomes. Two different things called reject, in the two
contracts most often read together, is the ambient collision [Naming](14-naming.md) killed `issue` for —
and the same split it made applies: `review`, `approve` and now `reject` are the human's, `check` and
`FAIL` are the agent's. A correction rather than a supersession: the mechanism this answer fixed is
unchanged, and nothing shipped had yet written the word down.

### The manager is a scribe, not an author

The human's call. The manager pastes each part of a handover under its heading and adds nothing but
separately-marked notes of its own. It does not shorten, re-render, re-order or improve. Two reasons,
one from the record and one from scale: F6 found that *"a paraphrase silently becomes the permanent
record"*, and re-authoring every resolution is the one cost that grows with the graph — at Lang's 179
nodes the manager would spend its context rewriting work it did not do. This is what *"the manager is
the graph's only writer"* means, and the shipped conventions document is ambiguous between the two
readings today.

A malformed handover is [Off-contract subagent output](17-off-contract-output.md)'s problem, not the
scribe's.

### One ordering rule, covering both logs

Two sections hold the human's words: `## Interview` for relayed answers and `## Review` for correction
rounds. The relay fixed at-relay-time writing for the first; the landing policy needs the second
replayable, because an implementation worker has to survive rounds of *"not like that"*. One rule
covers both: **the graph is written the moment the human speaks, before any worker is resumed.** A
worker's context is never the record; the node is.

### What this leaves elsewhere

[Off-contract subagent output](17-off-contract-output.md) is now unblocked — it has a contract to be
off. The gate payload's shape stays with [Human review of landed code](20-human-code-review.md). The
manager's own skill still waits on four open nodes. The worker contracts themselves have graduated out
of the fog into [Write the worker contract skills](22-worker-contract-skills.md), whose acceptance
condition is written there by this node.

One term was added to the glossary: **handover**.

## Flags

`ASSUMPTION` — decided alone that six independently-invocable contracts implies six sibling skill
directories rather than supporting files under one `expedition/` skill, since a supporting file cannot
be invoked by name. The layout itself is left to [Write the worker contract
skills](22-worker-contract-skills.md) and inherits node 21's install-location assumption; if that
assumption moves, this moves with it.

`ASSUMPTION` — the method skills the contracts name (`/grilling`, `/domain-modeling`, `/prototype`,
`/research`, `/naming`, `/coding-principles`) are **per-install, not per-repo**: four are a plugin on
this machine and two are the human's own. On a machine holding none of them a spawn would name skills
that do not exist. Decided that each contract names its method skills as *invoke if present* and
carries enough of its own discipline to stand without them, rather than vendoring six skills into the
expedition skill. Not verified on a machine without the plugin.

`ASSUMPTION` — resolved with no worker and no relay: the manager grilled the human directly, so this
node's `## Interview` records an exchange that the contract it just wrote would have routed through a
worker. Consistent with every earlier grilling node on this map, and the same gap
[Naming](14-naming.md) already carries.

## Interview

No worker, no attempt: the manager grilled directly, as on every earlier grilling node here. Five
questions, five answers, ~~all `verbatim` where quoted~~ **two of them verbatim and three of them not**,
corrected below.

**Annotation from [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md).** Three of these five entries record *the option's* text as
the human's answer. The human's own reply to those three was never kept and no session holds it now.
Under that node's answer such an entry is a `paraphrase`, and claiming `verbatim` for it is the one
direction that fails unsafely: it puts the manager's words on the permanent record as the human's, which
is [Relay protocol](08-relay-protocol.md)'s `F6` restated as practice. The three markers are struck
through and corrected in place; the entries themselves and this node's `## Answer` are untouched, so this
is an annotation and not a supersession.

One of the three is the reason the correction is worth making at all: **the answer that established the
scribe rule was itself recorded by the manager authoring.**

- **Does the checker read the node it is checking?** → *Blind — condition, bar, diff.* ~~`verbatim`
  (option chosen as written)~~ **`paraphrase`** — the manager's rendering of its own option, not the
  human's reply.
- **Is the manager a scribe or an author?** → *Scribe — paste, never rewrite.* ~~`verbatim` (option
  chosen as written)~~ **`paraphrase`** — the manager's rendering of its own option, not the human's
  reply.
- **How does a worker learn a source is untrustworthy?** → *"It seeems specific to lang but I think it
  should go in map.md, I belive it's not too long"* `verbatim`. Read as two things: the location, and a
  constraint that it stay short optional prose rather than a mechanism.
- **Is a worker handed its contract, or pointed at it?** → *"I would say pointers, agents seems pretty
  good at respecting skills when you do "/skill-name" if there is some additional things to know in
  addition, the manager can add it"* `verbatim`. **DIVERGENCE** — the recommendation was to copy the
  hard rules into the spawn, on the grounds that the prototype's rules were prompt text. Overruled,
  and the answer supplied the mechanism the recommendation was missing: not a path to read, a skill to
  invoke.
- **What is the return payload called?** → *Handover.* ~~`verbatim` (option chosen as written)~~
  **`paraphrase`** — the manager's rendering of its own option, not the human's reply.

## Annotation: "HITL types only" is lifted, and the checker gains a third outcome

Added by [When an AFK worker cannot proceed](23-worker-cannot-proceed.md) — the node this answer's
three-word restriction on the relay was holding shut.

- **AFK workers may use the relay's question variant**, on three triggers: the broken thing is not theirs to
  change, the decision changes a lot, or the choice is too hard to make alone. Below that line they still
  decide and flag.
- **The checker's return set widens.** This answer gave it `PASS` or `FAIL` and nothing else. It may now
  also raise, and it is the party best placed to — the only one that ever reads an acceptance condition
  cold. A raising checker **issues no verdict at all**, which makes this a third *outcome* rather than a
  third value, and gives [Human review of landed code](20-human-code-review.md)'s `## Review` chronology a
  third entry kind to carry.
- **The payload needed nothing.** A raise is the question variant already specified here — the node,
  `ABOUT`, `SO FAR`, `ASK`, `RECOMMENDED`, `ALTERNATIVES`, returned verbatim with its divergence marker.
  That is why the human's ask turned out to be a permission and a threshold rather than a build.
- **The scribe rule reaches one more place.** A raise lands under `## Interview` on an implementation node,
  which previously could not have one, and the manager files the human's answer there unaltered like any
  other.
