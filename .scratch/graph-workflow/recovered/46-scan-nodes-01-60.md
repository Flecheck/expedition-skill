# Recovered: node 46's scan of nodes 01–60

**What this is.** [What the manager reports to the human, in one place](../nodes/46-what-the-manager-reports.md)'s
first attempt dispatched a breadth scan across the node corpus and died on a session limit before the scan returned.
The scan completed; its output reached the **manager** rather than the worker that ordered it, and the manager wrote
it here verbatim so the replacement attempt could verify and extend it rather than re-run it.

**What it is not.** It is not a graph file, it is not an answer, and nothing in it is settled. It is one agent's
reading of sixty node files, to be checked rather than trusted. Node 46's answer is its worker's to write.

**A deviation, named rather than hidden.** `graph-conventions.md` fixes an effort's files as five, and this is a
sixth kind under a new `recovered/` directory. The manager wrote it because the alternative was to carry ~15k tokens
of another agent's text through its own context into a spawn, and the effort's standing instruction ranks reducing
token cost. Whether an effort may hold recovered material at all is nobody's decision yet.

**Coverage: nodes 01–60 only.** Nodes 61–103 were never reached.

---

*The scanning agent's own text, pasted. The manager added the headings above and nothing below.*

I read all 60 node files (01–60). Below is the exhaustive enumeration. Files are at
`.scratch/graph-workflow/nodes/`.

## 01 — `# Destination of this effort`
**No duty found.** Nothing about what the manager puts in front of the human.

## 02 — `# Runtime that hosts the manager and its subagents`
**1 duty (borderline — mechanism, not content).** `## Answer` — *"A subagent needing human input pauses by returning
a question; the manager relays it and resumes the same subagent with `SendMessage`, which continues it with its
context intact."* Word used: "relays" (no noun for the report). Settled decision, but the node is itself **flagged as
provisional by the user** (*"it might be a bit too simple but we will see."*).

## 03 — `# How much of the lifecycle the workflow owns`
**No duty found.**

## 04 — `# Concurrency model`
**1 duty (borderline).** `## Answer`, in the block annotated by node 11 — *"**The code slot is no longer purely
AFK.** An implementation node ends in a human gate — the manager raises the reviewed diff, the human approves or asks
for corrections — so the slot's occupant is a **third claimant** on the human's attention alongside the ~2
interviews."* Words used: "gate", "raises the reviewed diff". Settled decision (imported annotation from node 11).

## 05 — `# How the graph's bookkeeping is kept straight`
**No duty found.**

## 06 — `# Revision semantics`
**4 duties, all on *timing* — what may and may not reach the human, and when.**

1. `## Answer` → `### The cascade` — *"**Its output is queued graph edits, never a human interrupt.** Discovery is not
   resolution."* Settled.
2. `## Answer` → `### The cascade` — *"- A big decision surfaced → written into the node, to be raised with the human
   *when that node is worked*, not now."* Settled.
3. `## Answer` → `### The four sub-questions` — *"Only genuine conflicts reach a human, and they arrive queued on a
   node rather than as an interrupt."* Settled.
4. `## Answer` → `### The four sub-questions` — *"**Adopted on the agent's judgement rather than asked, and so the
   most revisable part of this answer:** a session about to supersede a node that is itself a replacement escalates
   to the human as a decision instead of revising again."* **Adopted on agent judgement**, flag-like, not settled by
   the human.

## 07 — `# Node type taxonomy`
**3 duties.**

1. `### Implementation is AFK and never asks a live question` — *"**Small ambiguity** — pick the most defensible
   answer, **flag it on the node as an assumption**, and land. The flag reaches the human queued on the node, per
   discovery-is-not-resolution."* Settled; later narrowed by node 23's annotation in this same file.
2. `## Annotation: implementation is AFK while it works and HITL at the gate` — *"**At the end, the node is HITL.**
   The lifecycle is implement → independent reviewer → manager raises the diff → human reviews → subagent corrects
   until the human is happy → manager commits → resolve. So an implementation node holds a claim on the human's
   attention that this answer did not budget for."* Settled, added on the human's instruction.
3. `### Three things adopted on the agent's judgement rather than asked` (point 3) — *"**An implementer may not
   rewrite its acceptance condition, but may flag it as wrong** — the same mechanism as an assumption flag, queued
   for the human."* Explicitly adopted on the agent's judgement; later re-homed by node 23's annotation here.

## 08 — `# Relay protocol`
**The single largest source. 8 duties.**

1. `### The relay payload` — the payload itself, verbatim:
   ```
   NODE:          <node name — the human's only address for this thread>
   ABOUT:         <1-2 lines: what this node decides, and why it is being decided now>
   SO FAR:        <digest of the thread: what the subagent read, what it concluded, and
                   what it has already decided on its own authority. Summarized if long.>
   ASK:           <the subagent's question, verbatim>
   RECOMMENDED:   <the subagent's recommendation and why>
   ALTERNATIVES:  <the options it rejected>
   MANAGER NOTES: <optional; cross-thread facts the subagent could not see>
   ```
   Settled decision (*"This is the deliverable."*).
2. `### The relay payload` — *"`ABOUT` and `SO FAR` exist because of the run's largest miss (`F7`, `F8`): the subagent
   reads the node, the map and several resolved nodes, and **the human reads none of that**. Attribution by name is
   necessary and nowhere near sufficient — a frame-less question makes the human spend the scarce resource on
   orientation instead of judgement."* Settled.
3. `### The relay payload` — *"**The notes are capped at what the manager already holds in context: it does not read
   code or run research to produce them.** Without the cap the manager duplicates the subagent's work and becomes a
   second implementer instead of a second pair of eyes (`F9`)."* Settled.
4. `### When a subagent dies mid-question` — *"**The human is told once**, by node name: that the agent for that node
   died, that their answer is recorded and being replayed, and that they may see a follow-up but will never see the
   same question twice."* An unnamed "told once" notice; node 16 later calls it a "death notification". Settled.
5. `### What the manager may never do` — *"The manager gains exactly four powers in this protocol — relay verbatim,
   instruct-store-and-stop, write a returned dump, and annotate from context it already holds. There is **no path on
   which it answers anything**."* Settled.
6. `### Adopted on agent judgement, revisable` (point 1) — *"**Narrowed — not overturned — by [Done-ness and
   termination](10-done-ness.md):** a delegated flag still does not gate the frontier, and it now appears in the
   **completion report** the human must read before an effort can be closed. So it blocks nothing, and no delegated
   answer reaches a closed effort unseen."* Adopted on agent judgement; narrowed by node 10.
7. `### Adopted on agent judgement, revisable` (point 2) — *"**The manager may never infer whole-node scope from a
   per-question answer.** Silence about scope means per-question, because widening it on inference silently removes
   the human from a node."* Adopted on agent judgement.
8. `## Annotation: a second kind of traffic, and replay on implementation nodes` — *"**The channel now carries traffic
   in the other direction.** Everything here is a *question* travelling from subagent to human with `ABOUT`, `SO
   FAR`, provenance and redirects. A gate is a **work product raised by the manager** — a reviewed diff, an
   acceptance condition, a reviewer's verdict, the flags the implementer left — and the human's reply is an
   instruction rather than an answer. Its payload shape is [Human review of landed code](20-human-code-review.md)'s
   to fix; what this node contributes is the discipline that the human's words go back **verbatim**, which now
   applies to correction instructions as well as answers."* Settled annotation.

**Also relevant (superseded):** `### What the prototype settled mechanically` — *"The manager therefore chooses
between **streaming** questions as they arrive and **batching** them. v1 streams, because a ready question should
never wait"* — explicitly overturned by node 16, recorded in this file's `## Annotation: finding `F4` is overturned —
the channel is one deep and batching is dead`.

## 09 — `# Dogfood target`
**1 duty (borderline — restates node 08's as a coverage criterion).** `### What counts as the run succeeding:
coverage, not completion` (item 3) — *"3. **The relay** — a subagent pauses mid-interview, its question reaches the
human carrying `ABOUT` and `SO FAR`, the answer returns verbatim, the subagent resumes. Per [Relay
protocol](08-relay-protocol.md)."* Settled coverage criterion, not a new duty.

## 10 — `# Done-ness and termination`
**6 duties, and the origin of the closing report.**

1. `### The done test` (condition 4) — *"4. **The human has read the completion report and closed the effort.**"*
   Settled.
2. `### The completion report, and what a flag costs` — the human's answer, verbatim: *"The human will review the
   changes, at least partially. So when the job is done, it is reported to the human so that it can look at it, give
   the flaged stuff. The human can decide to postpone it, then create a new node."* Settled.
3. `### The completion report, and what a flag costs` — the contents list, verbatim: *"The report carries: **What
   landed** — the code, and the supersession chains, which are the record of where the graph kept rubbing. **The
   bar's current state.** **Every outstanding flag** — assumptions an implementer decided for itself, acceptance
   conditions an implementer flagged as wrong, and **delegated answers** where the human said "you decide". **What
   the sweep found** — dangling edges, resolved nodes whose code no longer matches, coupling the graph never
   recorded. Scoped to **what the human has not already seen.** Because they review continuously, the report is a
   delta, not a replay. On an open-ended effort a report covering six months of changes would be unreadable, which is
   exactly the case the design has to survive."* Settled.
4. `### The completion report, and what a flag costs` — *"The human's four moves on it: **accept**; **settle a flag
   on the spot**; **postpone → which creates a node**; or **reject what landed**, which is a revision and belongs to
   [Revision semantics](06-revision-semantics.md)."* Settled. Node 46's annotation records that this duty **is in no
   shipped file**.
5. `### The final sweep, and why oscillation needs no counter` — *"**every sweep round appears in the report.** A
   graph that keeps producing work at the sweep simply never gets closed, and the human can see precisely why, round
   by round."* Settled.
6. `## Annotation: when a flag is paid for` — *"What that leaves for the **closing report** is the exception rather
   than the rule: flags raised before the practice existed — twenty of them, permanently unreachable at a close since
   their nodes are resolved — and flags from the two node kinds that never end in front of the human, a `research`
   node and an AFK `precondition` node. Everything else has been settled already."* Settled annotation, reported as
   an invalidation by node 27. Its ground about "the two node kinds that never end in front of the human" is later
   falsified — see node 27's last annotation.

**Also:** `## Annotation: `done` is gone as a word` — *"**`completion report` → `closing report`**, following
`closed`."* And `## Annotation: the sweep now has a shape` — *"plus the flag collection that node owes the closing
report, which is a single read of `flags.md`."*

## 11 — `# Git and code-landing policy`
**3 duties.**

1. `## Answer` (the lifecycle block) — *"implement (AFK) → independent reviewer (AFK) → manager raises the diff →
   human reviews → subagent corrects until the human is happy → manager commits → node resolves"*. Settled.
2. `### Two streams, separated by path and nothing else` — *"**If the product tree holds uncommitted code the node did
   not write** — the human's own hand-edits, or a dead agent's leftovers — the manager stops and says so rather than
   committing someone else's work under a node's name. Silently sweeping it in would attribute a change to a decision
   that never made it."* Settled.
3. `### The commit message carries the node's id` — *"The manager proposes the message; the human sees it before the
   commit happens."* Settled.

## 12 — `# Subagent context contract`
**4 duties.**

1. `### The handover` — *"An implementation worker adds a sixth *part* rather than a fourth variant: the **gate
   payload**, the diff plus the list of paths actually touched. Its presentation is [Human review of landed
   code](20-human-code-review.md)'s to fix. What this node fixes is that it belongs to the handover, and that the
   path list is **reported rather than inferred from `git status`**, per [Git and code-landing
   policy](11-git-and-code-landing.md)."* Settled; presentation explicitly left open to node 20.
2. `### The handover` — *"- **question**, HITL types only — the node, `ABOUT`, `SO FAR`, `ASK`, `RECOMMENDED`,
   `ALTERNATIVES`. The worker writes `ABOUT` and `SO FAR` itself: it has read the node, and it is the only thing that
   knows its own thread. The manager adds its note and nothing else."* Settled; the "HITL types only" restriction is
   later lifted in this same file.
3. `### The manager is a scribe, not an author` — *"The human's call. The manager pastes each part of a handover under
   its heading and adds nothing but separately-marked notes of its own. It does not shorten, re-render, re-order or
   improve."* Settled (the human's call) — **but** this node's own `## Interview` annotation records that *"the answer
   that established the scribe rule was itself recorded by the manager authoring"*, and the marker was struck through
   from `verbatim` to `paraphrase`.
4. `### One ordering rule, covering both logs` — *"One rule covers both: **the graph is written the moment the human
   speaks, before any worker is resumed.** A worker's context is never the record; the node is."* Settled; later
   corrected by node 17's `### Correction made mid-node: the write and the resume go together`.

## 13 — `# Graph file format`
**2 duties (both on the report's *inputs*).**

1. `## Question`, block added by node 10 — *"**Flags must be mechanically collectable.** The final sweep gathers every
   outstanding flag across the whole graph into the completion report: assumption flags, acceptance conditions an
   implementer marked as wrong, and delegated answers."* Settled input from node 10.
2. `### Four files, and why the count is not two` — *"The checkbox lives **only** in `flags.md`, so settling a flag
   never touches a node file and the two can never disagree — the completion report is the unchecked lines."*
   Settled; the "only in flags.md" half is later overruled at node 22's gate, and the "the report **is** the unchecked
   lines" claim is narrowed at node 26 correction round 1.

## 14 — `# Naming the workflow and its vocabulary`
**2 duties (naming the report).**

1. `## Question`, block added by node 10 — *"- The **completion report** — what the manager hands the human when the
   frontier empties."* Inherited term to be settled.
2. `### Four words killed outright` — *"**`done` → `resolved` and `closed`.** … `completion report` follows it to
   **closing report**."* Settled.

Also, via node 16's annotation: *"The **manager** may be overridden but never answers for the human — now a glossary
guarantee rather than a convention."*

## 15 — `# Cascade pass mechanics`
**2 duties.**

1. `### What it reports` — *"Nothing as an interrupt — unchanged from [Revision semantics](06-revision-semantics.md),
   and the sweep still reports through the closing report. What is added is one line rather than a channel: a minted
   node lands on the frontier where it is visible anyway, and the manager names in its ordinary narration at
   resolution what the pass minted, or that it found nothing. That is what stops a pass which supersedes eleven nodes
   from being a surprise at the next human read, and it costs nothing that is not already being said."* Settled, but
   flagged.
2. `## Flags` — *"`15.2` **· settled** `ASSUMPTION` — the one narration line. Settled by me, not asked. The design
   reports nothing as an interrupt, which leaves a pass that supersedes eleven nodes invisible until the next human
   read, and the manager is already narrating each resolution — so naming what the pass minted, or that it found
   nothing, is one line inside a message that already exists rather than a new channel."* Flag, marked settled,
   explicitly *"Settled by me, not asked"*.

Also: `### What it reports` — *"**The pass raises no flag of its own.** Its entire output is a judgement, so a flag per
judgement would put one line of noise in `flags.md` per resolution."* Settled; flag `15.5`.

## 16 — `# What the manager works on next, and how the human redirects it`
**The second-largest source. 11 duties.**

1. `## Question`, block added by node 11 — *"**One more thing the manager must be able to report:** which node, if
   any, is awaiting approval. That is the single blocking item in the whole system at any moment, and it is invisible
   in the graph files — the node reads `claimed` like any other."* Inherited requirement.
2. `## Annotation: the first fragment of the selection policy is decided…` — *"**A third thing the manager must be
   able to report**, alongside *which node awaits approval*: whether a worker is blocked on a raise. Same property
   that made the first one worth naming — it is invisible in the graph files, because the node reads `claimed` like
   any other."* Settled, inherited from node 23.
3. `## Annotation: a second fragment of the queue discipline…` — the human's verbatim standing instruction: *"When the
   user is answering something, don't replace it by something else but wait for the answer."* Settled.
4. `### 1. The attention queue: one question in front, two tiers behind` — *"Exactly one question is in front of the
   human at a time. **Nothing ever replaces a live question.**"* The two-tier table names *"a **gate**; a worker's
   **blocking raise**; the **manager's own raise**"* (tier 1) and *"a relayed **interview question**"* (tier 2).
   Settled.
5. `### 1. The attention queue…` — *"**Three things are not claimants at all**, and a reader will look for them.
   **Flag settlement** rides the human moment that already ends its node — a grilling node's last answer, an
   implementation node's gate — so it never queues on its own. A **death notification** (*the worker for node NN died,
   your answer is recorded*) awaits no answer. The **closing report** ends the effort rather than taking a turn in
   it."* Settled.
6. `### 1. The attention queue…` — *"**Every relayed question names, in one line, whatever else is waiting** — by node
   name and kind only, never restating the other question or its options. … It needs no new field — it is a `MANAGER
   NOTES` line, drawn from context the manager already holds."* Settled; also carried as flag `16.4`.
7. `### 3. The readiness floor: where asking stops and building starts` — *"**The residual is the manager's judgement,
   decided and reported.** Whether an open question would make the work irrelevant cannot be mechanised. The pick
   report names the implementation being started and the open questions judged non-fatal; the human overrides with one
   line. The same shape covers *"if the global design is done or very ahead"*, which is the same judgement one level
   up: the manager states which stream it is favouring and why, and the human corrects it if it has the effort's state
   wrong."* **First use of the term "pick report".** Settled.
8. `### 4. How the human overrides` — *"**The manager picks and reports; it never asks.** The third `Open:` bullet is
   answered: the pick stays the manager's call."* Settled (the human's `verbatim` *"Yes for pick and report"*).
9. `### 4. How the human overrides` — *"A standing instruction is **on disk and reported back in every pick it
   constrains**, so it cannot be silently forgotten — the failure mode here is an emphasis nobody remembers setting,
   and visibility is the whole remedy."* Settled.
10. `### 5. What the manager must be able to report` — *"Three states are invisible in the graph files, because the
    node reads `claimed` like any other: **which node awaits approval at a gate**, **whether a worker is blocked on a
    raise**, and **what is banked and waiting**. The first two the manager volunteers; the third it answers on
    request."* And the open item: *"**The pick report has grown duties from three different nodes and nothing states
    its contents.** That is the shape of failure node 29 exists because of — a list that was correct about the files
    it knew. Collating it is reported below as a node rather than settled thinly here, because two of the duties come
    from a node this one did not read."* First part settled; the collation **explicitly open**, minted as node 46.
11. `### 6. Consequences` — *"**A manager note may name which of a worker's questions it believes sharpest, and may
    not say what it thinks the answer is.** … The boundary is the sharpest / the answer line…"* Settled; also carried
    as flag `16.7`.

**Also flag `16.6`:** *"**"what is banked and waiting" needs no new machinery.** Answered from `flags.md` for
outstanding flags and from `Status: open` with a non-empty `## Interview` for parked nodes, with the human asking the
manager rather than reading either. Decided from the map's standing preference that the human's interfaces are the
manager's chat and the diff rather than a rendered graph."*

## 17 — `# Off-contract subagent output`
**2 duties.**

1. `### The narrow lane: one re-prompt, then the human` — *"A second unfileable return is not re-prompted again and is
   not respawned: the manager files what it can, leaves the node `open` holding what is already on it, and tells the
   human once by node name — the same single notice a death gets."* Settled; recorded `paraphrase`.
2. `### What fileability cannot see, and the one check against it` — *"**So before it files, the manager holds the
   handover's `ANSWER` against the `## Interview` it wrote itself, and anything resting on words the human did not say
   is filed as a flag beside it rather than refused.**"* Settled. Its own flag `17.4` records the check firing on this
   node and catching **the manager**.

**Also**, `## Interview` → `### Correction made mid-node: the write and the resume go together` — *"maybe first restart
the worker and then write the file, it might gain a bit of parralellism"* … the manager now issues **the resume and
the write in one turn**.

## 18 — `# Adopting an in-flight effort`
**No duty found** on what the manager reports to the human. Its seven manager steps are file-writing, not reporting.

## 19 — `# Workflow self-improvement during use`
**2 duties.**

1. `## Answer` (point 1) — *"One duty is attached. An implementation node that changes a file which other nodes of the
   same effort are written against must, at its gate, name which files it moved and which existing files are left in
   the older form. The manager carries that statement into every later spawn and re-check, which extends the
   requirement already recorded on **the manager's own skill** that a statement of what changed must cover commits and
   not only the working tree."* Settled.
2. `## Interview` → Q3 — *"Two riders it offered as cheap to overrule: the manager narrates a `FRICTION` flag when it
   is raised, because most efforts never close and the closing report would then never fire; and shipping it needs one
   paragraph in `graph-conventions.md` and one glossary entry"*. Offered as a rider, **not separately endorsed**; the
   frequency ground is later withdrawn, and the conclusion stands on *"because a foreign effort may never close."*

## 20 — `# Human review of landed code`
**The definitive gate-payload node. 9 duties.**

1. `### Added by [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md): the
   gate payload's flags` — the human, verbatim: *"Also for flags, when asking the user, please explain in more detail
   what was done and why and the context. Idealy I don't have to go into the files to find out what happened and how
   to respond"*. The ruling: *"**A flag reaches the human as what was done, why, and the context it needs to be
   answered — and answering it never requires opening a file.** Neither of a flag's two existing forms is a payload:
   its [flags.md](../flags.md) line is capped at one sentence by [Graph file format](13-graph-file-format.md), and its
   node entry is written for a reader who already has the node open. The manager writes a third form for the gate…"*
   Settled — a binding requirement given at a gate.
2. `### What the manager raises` — *"The human's own list, and it is shorter than any of the four options they were
   offered: **a chronology of the checker** — what it checked, what it found, and what the implementer did about each
   finding; **the flags the worker raised**, because those are *"things to be looked at"*; the node, the paths actually
   touched, and the proposed commit message with its `Node:` trailer; **a pointer to the tree. The diff is never
   rendered into the conversation.**"* Settled; the last bullet is **inferred, not instructed** and carries a flag.
3. `### What the manager raises` — *"**No acceptance condition in the payload.** It was one of the offered options and
   the human dropped it, correctly: the condition's reader is the checker, whose whole job is to hold the code against
   it, and a human who has to check the condition themselves is doing the checker's work at the gate."* Settled.
4. `### The chronology is assembled, not summarized…` — *"It is resolved by noticing that **every piece of the
   chronology is already text somebody else wrote** — the checker's verdict, the worker's account of what it changed in
   response. The manager lays them end to end, oldest first, and adds only separately-marked notes of its own. Ordering
   pasted pieces is scribe work; rewriting them into a gloss is not."* Settled.
5. `### Flags are read at the gate, and that is the last moment they are cheap` — *"The human's phrase makes the gate a
   flag's real audience, which nothing in this map had noticed… the human may **settle a flag at the gate** — `[x]` in
   [flags.md](../flags.md), the flag's text staying where it is, exactly as the settle procedure already works"*.
   Settled.
6. `### The abandoned diff: discarded by default, with one line offering to keep it` — *"The code itself is discarded,
   and the manager says so in one line as it does it: *"discarding `<paths>` — say so now if you want the diff
   kept."* No round trip, no standing directory of dead work."* **Flagged**; *"**Answered by [When an AFK worker cannot
   proceed](23-worker-cannot-proceed.md)**, where the human ruled that a stop saves what can be salvaged before the
   tree is cleaned"*.
7. `### The checker is started by the manager, and its verdicts are renamed` — *"**One exception, stated rather than
   hidden.** A checker that will not pass — a condition the worker cannot satisfy, or a bar the repo cannot meet — must
   still reach the human, because the gate is the *only* place an implementation node becomes visible to them.
   Otherwise a stuck node loops silently. The escape hatch is the human's own payload: the chronology carries "it
   failed three times, here is why", and the gate is raised on a failing tree with that stated in the first line."*
   **Flagged.**
8. `### The correction round` — *"**The human's words reach the worker verbatim**, by the scribe rule, and are written
   into `## Review` before the worker is resumed"*. Settled.
9. `### Review is recorded; its depth is not measured` — *"**Depth is deliberately unmeasured.** The workflow never
   asks which files the human actually read… Asking for it would tax the scarce resource for a number nobody acts
   on"*. **Flagged.**

**Also `## Flags`:** *"`ASSUMPTION` — **the code travels as a pointer and the diff is never rendered into the
conversation.** The human specified what the header carries and never addressed rendering; this is the manager's
reading of an answer that only makes sense if the code is read elsewhere… One line to overturn."*

**Also `## Annotation: the reject clause keeps its decision and loses its premise`** (from node 68): the discard
default's reasoning is replaced, decision unchanged.

## 21 — `# Write the graph conventions document`
**No new duty imposed.** One recorded instance: `## Review` records the node was raised at a gate with the checker's
absence stated (*"**The checker did not run, and its absence is not a pass.**"*), and `### The gate: approved` records
the human's verbatim *"seems good"*. These exercise node 20's duties rather than adding one.

## 22 — `# Write the worker contract skills`
**3 duties.**

1. `### The gate, round 1 — five flags settled, one question, one change` — *"The manager raised the work with the
   checker's absence stated in the first line, per [Human review of landed code](20-human-code-review.md)'s escape
   hatch, and the six judgement calls above as the flags."* Settled practice.
2. Same heading, the human's verbatim instruction — *"Maybe add ids to flag in the node, right now it is a bit hard to
   comment each one…"*. The ruling: *"**Flag ids are a format change, and the sixth delta on the shipped conventions
   document.** … without an id a flag can only be pointed at by its position in a list, which is what made this
   exchange awkward."* Settled — a duty on how flags are made addressable when put to the human.
3. `## Flags` preamble — *"~~**State is not here**: a flag's checkbox lives in [flags.md](../flags.md) and nowhere
   else.~~ **Overruled by the human at the gate:** a flag they have confirmed is marked **settled** here as well, so
   someone reading the node can see which judgements are still live without opening a second file."* Settled.

**Also borderline:** `22.11`'s note — *"**This entry was added late**… **A flag section assembled once does not stay
assembled. Whatever writes the manager's skill has to make gathering a step of raising a flag rather than a
tidy-up.**"*

## 23 — `# When an AFK worker cannot proceed`
**2 duties.**

1. `### The slot: block and keep it, and the raise goes to the front of the human's queue` — the human, verbatim:
   *"Block, keep the slot, the manager should priorise answering the worker instead of continuing working on grilling
   (ask the user to do it)"*. The ruling: *"**The manager asks rather than queues.** *"Ask the user to do it"* is an
   active duty: a blocking raise **pre-empts**, and the manager does not go on filling the human's queue with grilling
   questions while the code slot idles."* Settled.
2. `### Where a raise is recorded` — *"`## Interview`, and the format gains nothing. A raise is a relayed question with
   an answer — the same shape as an interview turn, with the same verbatim-or-paraphrase standing and the same
   divergence marker"*. Settled.

## 24 — `# Friction from running this map by hand`
**1 duty (borderline — an observation about narration, not a rule).** `### What worked…` — *"**12. Refer-by-name held
across 23 nodes.** Not once has narration needed a bare id, and the map is readable aloud. The cheapest rule on the map
by a wide margin."* Recorded finding.

**Also finding 5** (bears on when the human sees flags): *"**5. Flags are write-only.** Thirteen outstanding, zero
settled, across 23 nodes… On an effort that runs for months this is a large, invisible, growing pile."* Later dated by
node 27.

## 25 — `# What is recorded when the human takes an option as offered`
**1 duty.** `## Flags` — *"`25.3` **· settled** `ASSUMPTION` — decided alone that where a terse reply does not make
clear which option it points at, the manager records the reply and asks which, rather than choosing one and quoting it.
This is the only case left that costs a round trip, and it is a genuine ambiguity rather than a rendering. Settled in
the human's own words, which state it as a rule rather than as an exception: *"If an anwser is not clear, yes ask
again"*."* Flag, marked settled.

**Also flag `25.4`:** *"**This is the second consecutive node where that check has fired and the party it caught was
the manager** — the first time for words put into the human's mouth, this time for scope the human did not open."*

## 26 — `# Carry the recorded deltas into the shipped skill files`
**3 duties.**

1. `### The human's instruction on how a flag is put to them, `verbatim`` — the human: *"Also for flags, when asking
   the user, please explain in more detail what was done and why and the context. Idealy I don't have to go into the
   files to find out what happened and how to respond"*. The ruling: *"Given at this gate, after the manager had put
   eight flags to them as eight one-line labels and a file path. **A binding requirement on the gate payload, and the
   manager was failing it.**…"* Settled — explicitly "binding".
2. Same heading — *"**It creates a symmetry with the flag validity pass run minutes earlier, and the two point opposite
   ways.** For the **checker**, a flag is stripped to what was done and the reason is withheld… For the **human**, the
   same flag is expanded with what was done, why, and the context — so they can settle it without opening anything. One
   flag, two audiences, inverse payloads, and the manager writes both."* Settled observation, routed to node 30.
3. `### Flags `26.1`–`26.7` settled at the gate; `26.8` overruled` — the human: *"For a bit more context, I expect the
   nodes to be mostly targeted to agents, as I will mostly work from what the manager says (questions from subagents)
   and with code review. … For the flags information in the chat, it is much better"*. The ruling: *"**The opening
   sentence is not about this node at all** and is recorded as a standing preference on [map.md](../map.md)…"* Settled.

**Also:** flag `26.7`'s gate exchange records the manager's own failure of presentation — *"I don't really remember what
happened"*. … *"**A flag that records the absence of a condition still has to say what the condition would have
covered.**"*

## 27 — `# Whether flags.md survives the settle-at-close practice`
**3 duties — including the origin of the "pick report" as the settling moment.**

1. `## Annotation: approving the node's end settles its flags, with no separate assent` — the human, verbatim: *"Also,
   when I approve the end of the node, the flags should be considered ok"*. The manager's consequence: *"A flag exists
   to record a judgement the human may want to revisit, so settling one by implication is only sound if they saw it.
   That puts weight on the **gate payload**: it must present each of the node's flags — what was decided and on what —
   because approval now discharges them. … **A gate payload that omits a flag now settles it silently.**"* Settled
   instruction; the consequence stated as the manager's own note.
2. `## Annotation: one of the grounds is false — those two kinds do have a human moment` — *"**That ground is false.**
   Every node's close is reported by a **pick report** — the message the manager owes the instant a node closes — those
   two kinds included. So they do end in front of the human, and they have exactly the moment they are said to lack."*
   Settled correction; the consequent question is **open** as node 102.
3. `### The residual` — *"The twenty have exactly one route to the human: the closing report."* Settled; its frequency
   ground is withdrawn by annotation.

## 28 — `# Whether a spawn may override a shipped worker contract`
**2 duties — this is where the manager's *own* channel to the human is named.**

1. `### The manager's raise, which is the only new mechanism here` — *"So the manager raises, and the answer produces
   **two** outputs, always both: **a licence for that one attempt**, recorded as a flag on the node, so a later reader
   can see the worker was not running the shipped contract; **a node for the permanent fix**, so the repair is not
   lost."* Settled; later narrowed by node 19's `INVALIDATIONS`.
2. Same heading — *"So this is a **blocking raise by the manager on its own behalf**, and all this node adds is that the
   manager may make one. Nothing had described that channel: everything the manager says to the human today is a relay,
   a gate, or a flag settlement."* Settled; carried as flag `28.5`.

**Also flag `28.6`:** *"**the diagnostic clause about the raise's firing rate came from a manager note**, put to the
human alongside the recommendation and not covered by their assent to it."*

## 29 — `# What keeps the shipped files consistent when a decision changes a term`
**1 duty (borderline).** `### The half the effort must declare: this effort's ground rules` — *"**The manager copies the
block as text and adds nothing of its own.** Where a check needs a constraint the block does not hold, that is a
**raise** under [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md)'s rule, not
the manager's judgement."* Settled.

**Also `### Manager's note: all three flags outstanding, on the ordering node 39 exposed`:** *"Same case as node 39: a
grilling node's flags arrive **after** the last answer, in the handover, so *"ok for the recommandations"* could not
have reached flags that did not yet exist. All three are outstanding and presented rather than settled silently."*

## 30 — `# Whether a flag is checked before the human settles it` *(Status: open)*
**2 duties, both explicitly unsettled.**

1. `## Question`, quoting the human — *"For the flags, could we give a summarized version of the flags, with explict
   instruction to check if they are valid. It would be good to have a first check before the human check it. Maybe by
   simplifing the flag, only giving what was done and not the reason ?"* The node is **open** — *"So this node is not
   *whether* — it is *what*, *who*, and *when*."*
2. `### The same flag travels two ways, and the design must hold both` — *"So one flag has **three** forms and the
   manager writes two of them: its capped line in [flags.md](../flags.md), a **stripped** claim for the checker with the
   reason deliberately withheld, and an **expanded** payload for the human carrying exactly the reason the checker was
   denied. The two are not a compromise between each other — they are opposites, and each is right for its reader."* And
   the constraint: *"**any design here that describes only one direction will collide with the other.** It also puts both
   new forms in the manager's hands, which is where the scribe rule bites…"* **Open.**

**Also open:** *"**Who strips the flag.**…"* and *"**What a false flag does.** It is not a `FAIL`… Whether it blocks the
gate, reaches the human as a marked warning, or goes back to the worker is undecided."*

## 31 — `# What the checker contract owes to having been run`
**1 duty (borderline).** `### Gate — `approve`` — *"**Both flags settled by the same word.** The payload put `31.1` and
`31.2` in front of the human with their grounds inline and asked for them to be settled either way; `approve` covers the
payload it answers, which is the practice the map records — flags are settled as the node closes, eleven of eleven that
way before this. Recorded as a reading rather than as words of theirs, since neither flag was named."* Settled practice.

## 32 — `# Narrow the flags.md clause in the worker contracts` *(Status: open)*
**1 duty.** `## Annotation: the sentence that made this node unclaimable is superseded…` — *"The manager may write this
node's condition, under four constraints: … and the pick report names that it is the manager's and what it demands,
without the work waiting for a reply."* Settled, inherited from node 39.

## 33 — `# An acceptance condition is self-contained text`
**2 duties.**

1. `### Three calls a later reader would otherwise re-derive` (second bullet) — *"**The residual clause is the scribe
   rule pointed outward.** … it hands the condition over as written and supplies nothing it omits. Where what is missing
   is what the check turns on, it goes to the human — raised by the manager where it meets one before the check, or by
   the checker on a condition it cannot check."* Settled; carried as flag `33.3`.
2. `## Flags` — *"`33.3` **· settled** `ASSUMPTION` — **the manager may raise a pointing condition before the check
   rather than spending one it knows will raise.**…"* Flag, marked settled.

**Also flag `33.4`:** *"the manager condensed each of the four into its index line, authoring text that is neither the
worker's nor the human's."*

**Also, on the gate outcome being read rather than named:** `### Gate — `approve`` — *"The gate's three outcomes were
offered by name … and *continue* names none of them. Read as `approve`… **This is the first gate where the manager's
reading was not put back to the human**."*

## 34 — `# What an implementer does with a checker finding it believes is false` *(Status: open)*
**1 duty (a stated gap in the gate payload).** `### Three things the answer must account for` — *"**The concrete harm is
a wrong fix shipping quietly.** … Partially mitigated already: `GATE PAYLOAD` requires *"for each thing the checker
found, what you changed"*, so the human sees finding-and-change pairs — but never *"I made this change and I think it was
unnecessary."*"* **Open.**

## 35 — `# A worker's handover carries no acceptance condition for the node it mints`
**2 duties.**

1. `## Answer` — *"Where the worker's context genuinely does not reach, the contracts state a shortfall route rather than
   a silent gap: write the part you can, say plainly what is missing and why, and what you could not write is what the
   manager puts to the human."* Settled; carried as flag `35.2`.
2. `### Gate — `approve`` — *"**The flags were settled in the human's own words rather than read from the outcome**, which
   is the first gate in this effort where that is true. … *"Flags ok"* names them directly, so all four of `35.1`–`35.4`
   are settled by the human and nothing here is a reading."* And: *"Both halves of the gate payload's ask were answered in
   one line: the outcome named as one of the three, and the flags settled"*. Settled practice.

## 36 — `# The clause that says no resolved node changes cannot be self-contained`
**1 duty — the "name the outcome" clause on the gate payload.** `### Gate — `approve`` — *"The outcome was named. The
manager had asked for one to be named rather than inferred — *"please name one so I don't have to read it out of context
like last time"* — after node 33's gate arrived as *"you can continue"* and had to be read as `approve`… **Asking for the
word cost one clause of the payload and removed the reading entirely**, which is worth carrying into the manager's skill:
where the reply is a choice among named outcomes, the payload asks for the name."* Settled practice.

## 37 — `# Nothing tells a worker to hold its work against the record` *(Status: open)*
**No duty found** on what the manager reports to the human.

## 38 — `# Record a checker's not-covered part on `## Review``
**2 duties (borderline).**

1. `## Answer` — *"*Where the establishing lands.* On that same entry, beside the part: who established it and what they
   read or ran. Usually the manager, which holds the handover the checker does not; it may instead be the human at the
   gate reading it themselves, or a later run of the check. The `who` field is load-bearing precisely because the
   establisher varies."* Settled.
2. `## Flags` — *"`38.1` **· settled** `ASSUMPTION` — Nothing in the acceptance condition or in any resolved node fixes
   **when** an uncovered part must be established, and I wrote *"by the gate at the latest…"* Settled myself because a
   record with no deadline can be filed after the node resolves, which would mean the human approved work whose condition
   was only partly established and nobody was ever late."* Flag; recorded at the gate as **outstanding** — the human's
   reply did not reach it.

**Also, on queue discipline:** `## Review` — *"**One thing about the queue rather than the work.** This gate was raised
ahead of a further question from [Human-initiated steering](16-human-steering.md)'s live interview, which is the two-tier
rule that node's own worker designed and the human endorsed two rounds earlier — a gate being tier 1 because something
other than its own node stops while it waits."*

## 39 — `# Who writes the acceptance condition for an implementation node the manager mints itself`
**2 duties — the *fourth component* of the pick report.**

1. `### The rule` (constraint 4) — *"4. **The report that already accompanies the manager's pick names that the condition
   is the manager's, and in a line or two what it demands.** The human's override is one line. **The work does not wait
   for a reply**, so this adds no member to the list of things allowed to interrupt the human — a list closed at exactly
   three by [What the manager works on next…](16-human-steering.md)."* Settled.
2. `### The collision, exactly located: two files, and five that are the repair` — *"What the manager's own skill still
   owes is the *conduct* — when it audits, how the pick report carries constraint 4 — which reaches the map's fog
   alongside the other nine requirements, and reaches [What the manager reports to the human, in one
   place](46-what-the-manager-reports.md) as a **fourth component** of that report."* Settled routing.

**Also — the ordering fact:** `### Manager's note on why both flags are outstanding rather than settled` — *"**On a
grilling node the flags arrive after the last answer**, in the handover, so *"ok for recommendation"* could not have
reached flags that did not yet exist. Both are therefore **outstanding and presented**, not settled silently. … **a
gate's flags exist before the approval, and a grilling node's do not.**"*

## 40 — `# Nothing carries a flag's account of what produced it out of a worker` *(Status: open)*
**No duty found** on the manager's report. One recorded instance: *"Promoted to a node by the human, whose words on being
shown it were *"we will need to do something"* against the manager's proposal to mint rather than fix in place."*

## 41 — `# Ship the FRICTION flag and the self-edit disclosure duty` *(Status: open)*
**1 duty (to be shipped).** `## Acceptance condition` clause 6 — *"6. The same document states that an implementation node
which changes a file that other nodes of the same effort are written against must, at its gate, name which files it moved
and which existing files are left in the older form."* On an **open** node; the underlying duty is settled at node 19 but
**not yet shipped**.

**Also:** clause 3 — *"outstanding — left unchecked, meaning carried, and re-surfaced in that effort's closing report."*

## 42 — `# The checker's spawn carries the effort's ground rules`
**1 duty (borderline).** `**Gate — `approve`.**` — *"Two things this gate did **not** carry, recorded so neither is read as
having been settled here. Flag `42.1` was put to the human in the same message and their reply did not reach it, so it
stands **outstanding**: approving a diff that contains `Follow them.` is not the same act as confirming the judgement that
put it there."* **This reasoning is later superseded** by node 27's annotation — *"Under this instruction the approval did
reach it."*

## 43 — `# Widen the invalidation channel from contradiction to change` *(Status: open)*
**No duty found.**

## 44 — `# Write the cascade pass's worker contract` *(Status: open)*
**No duty found** on the manager's report.

## 45 — `# Nothing checks that a part a checker left uncovered was ever established`
**1 duty.** `**Gate: `approve`.**` — *"**Both flags settled by that approval, with no separate assent asked for**, under
the standing instruction filed at [Whether flags.md survives the settle-at-close
practice](27-does-flags-file-survive.md) — *"when I approve the end of the node, the flags should be considered ok"*. The
payload presented `45.1` and `45.2` in full, which is what the instruction requires of every gate: approval discharges
them, so a payload that omits one settles it silently."* Settled.

## 46 — `# What the manager reports to the human, in one place` *(Status: claimed)*
**The collating node. The entire node is the duty list; nothing is settled.**

1. `## Question` — the whole enumeration, verbatim: *"Collect every duty the manager's report to the human owes, from each
   node that added one, into a single statement of what that report contains. At least four are known and no file lists
   them: the line naming what a **cascade pass minted**, or that it found nothing — [Cascade pass
   mechanics](15-cascade-pass-mechanics.md), flagged there at `15.2`; the line naming **what waits behind the live
   question**, by node name and kind only — [What the manager works on next…](16-human-steering.md), flagged there at
   `16.4`; the **pick report**, naming the implementation being started and the open questions judged non-fatal — the same
   node; the three states **invisible in the graph files**, a node reading `claimed` like any other: which node awaits
   approval at a gate, whether a worker is blocked on a raise, and what is banked and waiting — the same node, inheriting
   them from [Git and code-landing policy](11-git-and-code-landing.md) and [When an AFK worker cannot
   proceed](23-worker-cannot-proceed.md)."* **Open.**
2. `## Question` framing — *"**Why it matters, in the reporting worker's words:** the pick report *"has grown duties from
   three different nodes and nothing states its contents"*, which is the shape of the failure [What keeps the shipped
   files consistent when a decision changes a term](29-shipped-file-consistency.md) exists because of — a list that was
   correct about the files it knew."* Open.
3. `## Annotation: a fifth duty for this list, found at node 76's gate` — *"**The human's four moves on the closing
   report.** Duty 141 of [Gather the manager's accumulated duties](75-gather-the-managers-duties.md), settled at
   [Done-ness and termination](10-done-ness.md): *"accept; settle a flag on the spot; **promote**, which creates a node; or
   reject what landed, which is a revision."*"* And the gap: *"**It is in no shipped file.** [Write the first version of
   the manager's skill](76-write-the-manager-skill.md) states what the closing report *contains*… and says nothing about
   what the human may do with it."* A **fifth duty**, unsettled.
4. Same annotation, the diagnostic — *"**A defined term with no conduct behind it is a reliable marker for a duty nobody
   wrote down** — the same question about `cascade` produced [The manager's cascade duties are in neither
   contract](87-managers-cascade-duties-have-no-contract.md) one message earlier."* And: *"**Two more terms have the same
   shape and are not filed anywhere yet**: `revision` and `AFK / HITL` each appear in the manager's contract only inside
   other entries' definitions. Whether either hides a duty has not been checked."* **Open.**

## 47 — `# Review every shipped file against `/writing-great-skills``
**No duty found** on the manager's report to the human.

## 48 — `# Reconcile a method skill's instructions with the contract's hard rules`
**No duty found** on the manager's report.

## 49 — `# Co-locate the scan rules with the mechanical checks` *(Status: open)*
**No duty found.**

## 50 — `# Whether the five contracts' shared blocks stay duplicated` *(Status: open)*
**No duty found** on the manager's report.

## 51 — `# What a contract may name as a method skill` *(Status: open)*
**No duty found.**

## 52 — `# How an agent workflow and its skills reduce their own token cost`
**No duty found** on the manager's report to the human. Bears on the manager's context budget, not on report content.

## 53 — `# What the token findings change in the workflow and its skills`
**3 duties (borderline, all about how the manager relays and whether it may be a source).**

1. `## Interview`, between Q2 and Q3 — *"**The first sentence was a failure of the manager's relay, not a doubt about the
   option.** The manager wrote *"third alternative"* without naming it. … Clarified to the human in the same message."*
   Recorded failure, corrected in place — no rule minted.
2. `### A2. What a worker reads of `map.md`, and how the residual is reached` — *"**Pull against push, stated explicitly,
   correcting its own earlier dismissal.** *The manager becomes the author* reaches pull **only where the manager
   summarises**; answering with a pointer keeps it a conduit."* Settled reasoning.
3. Same heading, on the human's own proposed mechanism — the human, verbatim: *"For the map, could we keep only what is
   stricly nessesary for all agents and then have the subagents ask the manager that should already have all the
   information loaded so it can answer question about the effort ? I am not sure it is a good idea since it is using the
   manager more but can you look into it ?"*. The ruling: *"**It spends the resource that actually fails**… **The pause is
   the cost, not the question**… Three smaller costs: it routes machine traffic into the one queue reserved for the scarce
   human; it is new machinery, no such channel existing; and **the failure mode is silent**"*. Settled — the blocking pull
   is refused; the **non-blocking** handover form is taken (becomes node 60).

## 54 — `# Re-review the shipped files against `/writing-for-agents``
**1 duty (borderline).** `### What the new text finds that the old could not` (item A) — *"The worker's inference, marked
as such: `map.md:37` has already settled that the human's two interfaces are the manager's chat and the diff, so **the
human is not the index for a file inside the skill tree**, and `:25`'s *"the human is the index"* has no holder here."* A
marked inference in a settled research answer.

## 55 — `# Say who writes a condition when no node spawned the node` *(Status: open)*
**1 duty (to be shipped).** `## Acceptance condition` clause 2, fourth bullet — *"- where the manager cannot write the
condition in full, it writes the part it can, says plainly what is missing and why, never omits it in silence, and puts
what is missing to the human; the node is not claimed until the condition is complete."* On an **open** node; the
underlying rule is settled at node 39.

**Note:** this node's condition **does not** carry node 39's constraint 4 (the pick-report naming duty) into the shipped
files — clause 2 lists only the other three constraints plus the escape valve.

## 56 — `# Ship the glossary inside the skill directory and make it state its own completeness` *(Status: open)*
**No duty found** on the manager's report.

## 57 — `# Give a research node the cannot-proceed raise` *(Status: open)*
**1 duty (borderline).** `## Acceptance condition` clause 1 — *"1. `.claude/skills/expedition-research/SKILL.md` gives its
worker the cannot-proceed raise, on the **same threshold and in the same terms** as
`.claude/skills/expedition-precondition/SKILL.md` already states it."* **Open**; the human's instruction is verbatim in the
`## Question` — *"I think a research node should be able to raise when it can do nothing."* — and it **reverses their own
earlier decision**.

## 58 — `# Qualify the graph-file ban in the worker contracts`
**2 duties.**

1. `### Attempt 1 — who writes the file when a node's work is a graph file` — *"**Q2, from the manager.**…"* and *"**The
   option taken**, quoted from the manager, which wrote it — **this recommendation was the manager's own and not a
   worker's**"*. A manager raise put to the human. Settled; carried as flag `58.3` — *"**What is not bound: nothing checked
   the amendment before it reached the worker.**"*
2. `### Checker run 1 — `PASS`` — *"**Questions handed back alongside the outcome.** These do not change it, and they
   travel to the human in the gate payload."* Settled practice.

## 59 — `# Restructure `map.md` to what every worker needs`
**3 duties.**

1. `## Review`, run 2's two questions — *"The first is clause 4 against clause 9, which is **the worker's flag `59.1`
   reached independently by a blind party** — and the checker went further than the worker did, naming which side gives way
   if the strict reading holds… It is the human's, and it is put at the gate rather than in the correction round because
   the repair does not depend on it."* Settled routing decision.
2. `**Gate: `approve`.**` — *"**All three flags settled by that approval, with no separate assent asked for**… The payload
   presented `59.1`, `59.2` and `59.3` in full."* Settled practice.
3. `**Gate: `approve`.**` — *"**`59.1` is settled as a reading, and the record should say which one.** The human approved a
   payload that named clause 9 as **passed on a reading rather than settled**, and that named the alternative and its
   consequence in the checker's own words… So the approval settles the flag by adopting the reading the worker and the
   checker reached independently"*. Settled as a **reading** — the duty is that a payload must name the alternative and its
   consequence for such a reading to be legitimate.

**Also:** `### Correction to the condition's stated before-state, by the manager, at claim time` — *"**The manager files
nothing further into `map.md` while this node is claimed.**"*

**Also — a standing rule about how the manager may state a state:** `### Correction by the manager: a dead run is not an
empty run…` — *"**The standing practice from here: a dead run is resumed, not respawned**, unless another live run has
already overtaken it. And a run's state is reported from its transcript's size and record count, never from the harness's
summary line."*

## 60 — `# A worker reports what the map did not tell it` *(Status: open)*
**No duty found** on the manager's report to the human. `MISSING FROM MAP:` is a worker→manager handover part; the
manager's obligation is to *"promote that material back into the live section"*, not to report it.

---

## Cross-cutting note on naming

The corpus uses, without normalising: **relay payload**, **question** (the return variant), **relayed question**, **pick
report**, **gate payload**, **payload**, **the gate**, **raise** / **blocking raise** / **the manager's own raise**,
**manager note** / **`MANAGER NOTES`**, **the chronology**, **completion report** → **closing report**, **narration** /
**ordinary narration at resolution**, **death notification** (node 16) vs. the unnamed "told once by node name" (node 08),
**flag settlement**, and **the manager's chat**.
