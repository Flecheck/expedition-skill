# Who writes the acceptance condition for an implementation node the manager mints itself

Type: grilling
Status: resolved

## Question

The five worker contracts now say that a worker reporting an implementation node writes that node's
acceptance condition. That closes the case which produced the defect and leaves the other one open: a node
the **manager** mints itself — from the human's steering, from its own reading of the graph, or as a
replacement in a supersession — has no minting worker, so nobody is assigned its condition. Every
manager-written condition in the evidence table on [A worker's handover carries no acceptance condition for
the node it mints](35-handover-mints-no-condition.md) is of that kind, that node's own included.

Two shipped rules collide on it. [`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)
and [`CONTEXT.md`](../../../CONTEXT.md) both fix a condition as *"written by the node that spawned it"*, which
a manager-minted node has no way to satisfy. And the scribe rule says the manager pastes and never authors —
sharpened by [An acceptance condition is self-contained text](33-condition-is-self-contained.md) into the
manager not being allowed to supply what a condition omits, on the ground that doing so makes it the author
of the standard the work is judged against. A condition it wrote whole is the same act, larger.

So: **may the manager author a condition at all, and if not, does every manager-minted implementation node
cost the human a condition to write?** That is the human's time and therefore the human's call.

A third answer is already on the record and costs neither. Node 35's evidence is that the **audit at claim
time** is what made two manager-written conditions cost nothing while two unaudited ones cost five defects
between them — so the manager could keep the pen for the nodes it mints and inherit the read-back duty the
five contracts now carry.

### One thing that answer now has to survive, measured at the node that proposed it

The audit is not sufficient, and the measurement is on [A worker's handover carries no acceptance condition
for the node it mints](35-handover-mints-no-condition.md) itself. Its condition was manager-written and
audited at claim time; the audit found and repaired two defects, and **the blind checker then found a third
the audit had missed** — a clause the condition dictated that was complete for three of the five contracts
and incomplete for two, discovered only by holding the condition against a file the condition does not name.

So the honest shape of the third answer is *audit plus a check that can still catch what the audit missed*,
which is what happened here and worked. Whether that is good enough for a node whose checker has less to
hold the condition against is this node's to weigh.

### Where the answer lands

The **manager's own skill**, which is still fog on [map.md](../map.md). It touches no worker contract, which
is why it is not blocked by anything and blocks nothing.

Reported by [A worker's handover carries no acceptance condition for the node it
mints](35-handover-mints-no-condition.md)'s worker.

### What the record now holds, gathered by the manager before this node was claimed

*The manager's own note, not a decision.* Two things have happened since this node was written, and both bear
on the third answer it already holds.

**Fact 1 — one more manager-written condition, audited, and its checker found nothing.** [Record a checker's
not-covered part on `## Review`](38-recording-a-not-covered-part.md)'s condition was written by the **manager**
for a node the manager did not mint: node 31's worker reported the work and wrote no condition for it. It was
audited at claim time against nodes 33 and 36, the audit recorded on that node, and its blind checker returned
`PASS` with **nothing reserved and no questions**. So the evidence table this node reasons from gains a row
where *audit plus a check that can still catch what the audit missed* cost nothing at all — against node 35's
row, where the same shape let a third defect through to the checker. One row each way; the practice is not yet
a pattern in either direction.

That condition also did something this node should weigh, because it is the manager holding the pen without
deciding the node: it **stated properties and refused to choose the form**, on the ground that choosing would
have been deciding the node rather than framing it. Whether that is the shape a manager-authored condition
must always take is a question this node can answer and nothing else has.

**Fact 2 — the readiness floor has landed, and it changes what the pen costs.** [What the manager works on
next, and how the human redirects it](16-human-steering.md) settled that **an implementation node is startable
when its acceptance condition can be written in full**, with nothing deferred to an open question — derived
from node 33 rather than invented. And it fixed a limit the manager proposed and the human did not separately
endorse: **a condition made writable by deciding the open question inside it does not pass the floor**, that
being a decision reaching the graph on the manager's own authority, which is a raise or a flag and never a
condition.

That reaches this node directly. If the manager may author a condition, the floor already forbids the failure
mode this node most feared — the manager writing a standard into being — because deciding inside the condition
is now explicitly not allowed. So the question may be narrower than it was written: not *may the manager
author one*, but *what is left of that worry once deciding-by-fiat is already forbidden*.

**One live instance of the same rule being applied honestly**, worth reading because it is the floor's first
use after being decided: [What the manager reports to the human, in one place](46-what-the-manager-reports.md)
was minted by node 16's own worker as a `precondition` rather than an implementation node, precisely because
its condition could not be written in full — two of its duties come from a node that worker had not read.

## Interview

### Attempt 1 — routing key `graph-workflow/39/a1`

**Q1, from the worker**, pasted as it wrote it.

```
NODE:          Who writes the acceptance condition for an implementation node the manager mints itself

ABOUT:         Every implementation node needs an acceptance condition — what "done" means for it —
               written down before any worker may touch it. A fix two days ago put that pen in the
               hand of the worker that reports the node. But the manager sometimes mints a node
               itself: from your steering, from its own reading of the graph, or as a replacement
               when a node is retired. Then there is no such worker, and two shipped files still say
               a condition is "written by the node that spawned it" — which that case cannot satisfy.
               Being decided now because it is the last thing standing in the way of the manager's
               own skill, the only file left that describes the manager's own conduct.

SO FAR:        Measured, not argued: this case has arisen twice in 47 nodes, and both of those nodes
               are stuck right now — node 32 for four days and nine node resolutions, its own file
               recording that the manager deliberately declined to write its condition. Since the
               fix landed, every worker-reported implementation node has come with its condition
               written, so manager-minted is the whole remaining gap.
               The failure this node most feared — the manager writing a standard into being — was
               already forbidden two days ago by a separate decision: a condition made writable by
               *deciding* the open question inside it does not pass.
               Evidence on whether the manager writing one is safe, and it is one row each way. Four
               conditions the manager has written. The two written before any discipline existed cost
               five defects between them. The two written after it — the manager reading its own
               condition against the two shipped rules before spawning anyone — cost nothing on one;
               on the other the audit missed one defect, the independent checker caught it, and one
               correction round fixed it. So the audit is not sufficient alone, and it is not worthless.
               Settled on my own authority, both already being established practice: the same answer
               covers a replacement node when one is retired (its condition is mostly the retired
               node's, copied), and the manager marking a condition as its own on the node file is
               required rather than optional.

ASK:           May the manager write the acceptance condition for a node it minted itself — and if
               it may, do you see that condition before the work starts, or not at all?

RECOMMENDED:   Yes, it may write it; and you see it but never wait on it.
               Four constraints, three of which are already practice:
               1. It may demand only what is *already fixed* — by a resolved node, by the node's own
                  question, or by the state of the files. Anything it would have to decide is not
                  written into the condition: it states the property and leaves the form to the
                  worker, or it asks you. This is not a new rule; it follows from the readiness floor
                  plus the self-containment rule.
               2. It reads the condition back against those two rules before spawning anyone, and
                  records that audit on the node.
               3. The condition is marked on the node as the manager's own.
               4. The report you already get when work starts names that the condition is the
                  manager's and, in a line or two, what it demands. Your override is one line. The
                  work does not wait for a reply.
               And the escape valve that already exists: where the manager cannot write it in full,
               the shipped route applies — write the part you can, say plainly what is missing, and
               that part comes to you.
               What this rests on: your time is what the node says is at stake, and this costs you a
               read rather than an authoring — roughly twice in 47 nodes so far. It targets the
               failure nobody is watching for (the manager quietly deciding something by writing it
               as a demand) and leaves the failure that is already caught to the checker that caught
               it. It rides a report you are owed automatically anyway, so it adds nothing to the
               queue of things waiting on you.

ALTERNATIVES:  - Same permission, but you never see the condition. Cheapest for you, and leaves the
                 one failure this node was written about with nobody looking for it before a whole
                 node is spent on it.
               - Same permission, but the manager waits for your approval before starting. Puts you
                 on the critical path of every manager-minted node, and adds a fourth member to the
                 short list of things allowed to interrupt you — a list you closed two days ago at
                 exactly three.
               - You write it. Costs you two conditions today, both about the workflow's own skill
                 files, which the standing preference says you do not read. You have answered eleven
                 questions across two nodes this session and have never once been asked to author
                 an artifact.
               - The manager is forbidden to mint an implementation node at all: it mints a smaller
                 node first, whose worker then reports the implementation node with its condition.
                 Dissolves the collision with no shipped-file edit and costs you nothing — but pays
                 an extra node and an extra worker every time, which at the first real target's
                 scale is tens of nodes existing only to write conditions; and its hard cases end at
                 the same question to you anyway.
```

**The manager's notes, put to the human beside Q1 and recorded here as the manager's own.** The manager is the
party with the conflict of interest on this node, so these are corrections of fact rather than argument.

1. **One count is wrong and it widens the collision rather than narrowing it.** The worker wrote that *"two
   shipped files still say a condition is `written by the node that spawned it`"*. **Seven** files carry that
   phrase: `graph-conventions.md:111`, `CONTEXT.md:168`, and all five worker contracts. The five contracts are
   **not** a collision — there the sentence is followed by *"Where you report one, that is you"*, which is node
   35's fix doing its job. So the collision is the two the worker named, and the other five are the fix. The
   count is wrong; the reasoning built on it is not.
2. **The worker's own framing of the two manager-minted nodes is looser than the record.** Node 32 was minted by
   the manager at node 28's close, and its file records the decision not to write its condition. Node 40 was
   **promoted by the human** from a checker's note — *"we will need to do something"* — so the manager wrote the
   file but did not choose the work. Both lack a condition and both are stuck, which is the worker's point and
   it survives; the two are not the same act.
3. **Node 32's own file already carries a reason for the refusal that this node has to overrule, not merely
   outweigh**: *"Deliberately not written by node 28's manager, on node 31's warning: node 26's condition was
   the first written by a manager rather than by a spawning node or its worker, and it had to be amended
   twice."* Whatever is decided here supersedes that sentence.
4. **The manager's own view, since the human asked for it as standing practice.** The recommendation is right
   and the reason the worker gives is not the strongest one available. The strongest is that
   *the fourth constraint is free*: the human is already owed a report at the moment work starts, so naming the
   condition's author and what it demands costs one line in a message that is being sent anyway. Every
   alternative either buys nothing (never seeing it) or buys the same protection at the price of a new thing
   that can block (waiting for approval). The manager also notes against its own interest that constraint 1 —
   *demand only what is already fixed* — is the one it will be tempted to bend, because the temptation is
   invisible from outside: a condition that quietly decides something reads exactly like a condition that
   does not.

**A1, from the human**, `verbatim`: *"ok for recommendation"*.

The option it points at, quoted from Q1's `RECOMMENDED` and attributed to the worker that wrote it: *"Yes, it
may write it; and you see it but never wait on it"*, with its four constraints — demand only what is already
fixed; read the condition back against the two rules and record that audit on the node; mark the condition as
the manager's own; and name the author and what it demands in the report the human already gets when work
starts, their override being one line and the work never waiting for a reply. Plus the escape valve that
already exists: where the manager cannot write it in full, it writes the part it can, says plainly what is
missing, and that part comes to the human.

**No divergence.** The reply takes the recommendation as offered and names no alternative, so nothing here is
`paraphrase` and there is nothing for the manager to ask about. Recorded under [What is recorded when the human
takes an option as offered](25-recording-an-option-taken.md).

This also **overrules the sentence on [Narrow the flags.md clause in the worker
contracts](32-narrow-flags-file-clause.md)** that recorded the opposite practice — *"Deliberately **not**
written by node 28's manager, on [What the checker contract owes to having been run](31-checker-contract-owes.md)'s
warning"* — which is the third of the manager's three notes above being discharged by the answer rather than
answered separately.

## Answer

**The manager may write the acceptance condition for an implementation node it minted itself, under four
constraints, and the human sees that condition without ever waiting on it.** The human's words, `verbatim`, on
the recommendation as offered: *"ok for recommendation"*. Everything under *The rule* is theirs by that assent,
the recommendation having been taken whole rather than amended.

### The rule

1. **The condition may demand only what is already fixed** — by a resolved node, by the node's own
   `## Question`, or by the state of the files. Anything the manager would otherwise have to decide is not
   written into the condition: it states the property and leaves the form to the worker, or it raises the
   question to the human.
2. **The manager reads the condition back against the two rules that bind every condition** — that a condition
   is self-contained text, and that no condition may quantify over the record — before the node is claimed, and
   records that reading on the node.
3. **The condition is marked on the node as the manager's own.**
4. **The report that already accompanies the manager's pick names that the condition is the manager's, and in a
   line or two what it demands.** The human's override is one line. **The work does not wait for a reply**, so
   this adds no member to the list of things allowed to interrupt the human — a list closed at exactly three by
   [What the manager works on next, and how the human redirects it](16-human-steering.md).

**And the escape valve, which already exists rather than being added here.** Where the manager cannot write the
condition in full, [A worker's handover carries no acceptance condition for the node it
mints](35-handover-mints-no-condition.md)'s shortfall route applies unchanged, with the manager in the worker's
place: write the part you can, say plainly what is missing and why, never leave it out in silence, and what
could not be written is what goes to the human. **The node is not claimed until it is complete.**

### Why permission is the answer, and not the prohibition the question expected

**The scribe rule does not reach this act.** [An acceptance condition is self-contained
text](33-condition-is-self-contained.md) forbids the manager *supplying what a condition omits*, on the ground
that doing so makes it the author of the standard the work is judged against — and this node's `## Question`
read a whole condition as the same act, larger. It is not. What node 33 forbids is text reaching the
**checker's payload** that is nowhere on the graph, unread by the worker and unquotable by anyone. A condition
written onto the node file is on the graph, is what the worker reads, is what the checker is handed, and is
auditable by anyone who opens the node. **The two acts differ in visibility, not in authorship.** And the
scribe rule proper — from [Subagent context contract](12-subagent-context-contract.md) — protects *another
party's words* from being re-authored, shortened or re-rendered; there is no other party's words in a condition
for a node no other node spawned. Recorded as flag `39.1`, this reading being the answer's load-bearing premise
and the worker's rather than the human's.

**The failure this node most feared was already forbidden before this answer said anything.** Node 16's
readiness floor, and flag `16.5` inside it, fix that a condition made writable by **deciding** the open
question inside it does not pass. **Constraint 1 is that limit widened** from *the open question inside it* to
*anything not already fixed*, which is what makes the pen safe rather than merely supervised.

**The prohibition has already cost more than the permission.** [Narrow the flags.md clause in the worker
contracts](32-narrow-flags-file-clause.md) has been unclaimable since 2026-08-19 — ten node resolutions and
seven landed commits — and its own file records why in as many words: its condition was *"deliberately not
written by node 28's manager"*. [Nothing carries a flag's account of what produced it out of a
worker](40-flag-account-has-no-handover-part.md) has been unclaimable on the same ground since 2026-08-20.
**Two nodes stopped, no defect avoided.**

**That sentence in node 32 is superseded by this answer, not outweighed by it.** Its stated ground — *"node
26's condition was the first written by a manager rather than by a spawning node or its worker, and it had to
be amended twice"* — is now the wrong half of the evidence. Node 26's was written before any discipline
existed; the two written under constraint 2's discipline cost nothing on [Record a checker's not-covered part on
`## Review`](38-recording-a-not-covered-part.md), whose blind checker returned `PASS` with nothing reserved, and
cost one defect on node 35 that the audit missed, the independent checker caught, and one correction round
fixed. **A node left stuck on a superseded reason is the failure this node exists to end.**

**The evidence is one row each way and this answer does not pretend otherwise.** Constraint 2 is *audit plus a
check that can still catch what the audit missed*, exactly as node 35 phrased it, and never an audit that makes
the check a formality. **Constraint 4 exists because** the two rows say the audit and the check together catch
what is visible in the condition's own terms or in the files — and **neither of them looks for the one thing
this node was written about**, a manager quietly deciding something by writing it as a demand. That failure is
caught by the human reading two lines, before a whole node is spent on it.

### The collision, exactly located: two files, and five that are the repair

Seven shipped files carry the phrase *"written by the node that spawned it"*.

- **The two that collide** are `graph-conventions.md` and `CONTEXT.md`, where the phrase stands unqualified and
  a manager-minted node has no way to satisfy it.
- **The five worker contracts are not part of the collision.** In each, the phrase is followed by *"Where you
  report one, that is you: its condition goes in the `NEW NODES` block"* — node 35's fix doing its job, and the
  case this answer does not touch. **A worker-minted node's condition stays the minting worker's, and the
  manager authoring one remains explicitly wrong.**

The four constraints land in `graph-conventions.md` rather than waiting for the unwritten manager skill, on
flag `38.1`'s own ground: **that document is where manager procedures live.** What the manager's own skill still
owes is the *conduct* — when it audits, how the pick report carries constraint 4 — which reaches the map's fog
alongside the other nine requirements, and reaches [What the manager reports to the human, in one
place](46-what-the-manager-reports.md) as a **fourth component** of that report.

### The three ways a manager mints a node, and which one has actually happened

All three are covered by the same rule. **Node 32 is the second route** — the manager's own reading of the
graph, at node 28's close. **Node 40 is the first** — the human promoted it from a checker's note, their words
being *"we will need to do something"*; the manager wrote the file and did not choose the work. **The third has
not arisen**: a replacement node's condition is mostly the retired node's, copied in, which is the copy rule
rather than authoring. Settled on the worker's own authority as flag `39.2`.

### Frequency, measured rather than estimated

**Two implementation nodes in the graph's history have needed the manager's pen, and the graph is now 54
nodes.** The rate is falling rather than rising: of the last seven nodes added, **none** needed it, six carrying
conditions written by their reporting workers. So the human's cost under this answer is reading one or two
lines, roughly twice in fifty — against authoring two conditions today, both about the workflow's own skill
files, which the map's standing preference records that they do not read.

### What this does not decide

Whether node 38's shape — **stating properties and refusing to choose the form** — is the *only* shape a
manager-authored condition may take. Constraint 1 makes it the shape wherever the form is not already fixed,
and permits the manager to dictate a form that a resolved node already fixed, that being a copy. Nothing here
says more.

## Flags

`39.1` `ASSUMPTION` **· settled** — **The reading of the scribe rule and of node 33 that this whole answer rests on, decided
alone.** In the worker's words: *"node 33 forbids text reaching the **checker's payload** that is nowhere on the
graph, while a condition on the node file is read by the worker, handed to the checker, and auditable by anyone
— the two differing in visibility rather than in authorship… The human endorsed the recommendation this premise
supports and was not asked to rule on the premise itself. If the premise is wrong, the permission goes with it
and the alternative on the record is the manager minting a smaller node whose worker writes the condition —
which costs no human time and pays an extra node and worker per case."*

`39.2` `ASSUMPTION` **· settled** — **That a replacement node in a supersession is covered by the same rule, decided alone.**
The only one of the three routes that has never arisen, so there is no evidence either way. Its ground: a
replacement's condition is mostly the retired node's copied in, which is the copy rule every condition already
obeys rather than fresh authoring. *"It was stated in what went to the human and their reply did not reach
it. The risk I accepted is that a supersession replacing an implementation node whose **condition** was the
thing found wrong is exactly the case where copying is the wrong move, and nothing here says what happens
then."*

### Manager's note on why both flags are outstanding rather than settled

*The manager's own note.* The standing rule is that approving the end of a node settles its flags — *"the
approval at a gate, or the last answer on a grilling node, is the settlement"* — with the manager's own
consequence attached, that the payload must present every flag because approval discharges them. **On a grilling
node the flags arrive after the last answer**, in the handover, so *"ok for recommendation"* could not have
reached flags that did not yet exist. Both are therefore **outstanding and presented**, not settled silently.
This is the first case where that ordering has mattered, and it is worth a line in whatever eventually states
the settle-at-close practice: a gate's flags exist before the approval, and a grilling node's do not.

## Annotation: the prohibition is narrowed to authoring, and does not reach widening a scope

*Filed by the manager from [How a condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s
`INVALIDATIONS`. This narrows one sentence of the answer above rather than superseding it, on the disposition node 86
set as flag `86.1`. The answer's text is left as it stands under the never-delete rule.*

`### The collision, exactly located` states without qualification: *"A worker-minted node's condition stays the
minting worker's, and the manager authoring one remains explicitly wrong."* **That sentence is now true of
*authoring* and false of *widening the scope*.**

Node 82 permits the manager to extend a worker-written condition to further instances of a defect the condition
already describes, **on this node's own ground**: the prohibition rests on the manager becoming the author of the
standard the work is judged against, and an amendment that adds no requirement does not make it one. The set of
places grew; the standard did not.

**Constraint 1 above is what bounds it** — *demand only what is already fixed* — and node 82's test is that limit
applied to an amendment rather than to a whole condition: *the amendment adds places, never demands.* Its guard 2
applies all four of this node's constraints to an amendment unchanged.

**The clause survives intact for every other edit to a worker-minted condition**, and three things stay outside the
permission: a new demand at any place, an ambiguous demand at a place already listed, and a defect the condition does
not describe.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
