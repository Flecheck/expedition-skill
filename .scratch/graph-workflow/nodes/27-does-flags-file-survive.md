# Whether flags.md survives the settle-at-close practice

Type: grilling
Status: resolved

## Question

[flags.md](../flags.md) was built as a queue. Its checkbox is the state, and the closing report is defined
as the unchecked lines. Then [Write the worker contract skills](22-worker-contract-skills.md)'s gate
introduced a practice that empties the queue as fast as it fills: **the manager settles a node's flags as
it closes that node**, while the work is still there and settling is cheap.

The practice has never once failed to empty it. Nineteen flags have been raised under it — eleven on
[Write the worker contract skills](22-worker-contract-skills.md), four on [Off-contract subagent
output](17-off-contract-output.md), four on [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md) — and all nineteen were settled at their own node's close.
**Every one of them was settled as the manager recommended.**

So: does [flags.md](../flags.md) still have a job, and if so which one?

Two candidate shapes, and the node has to pick or invent a third.

- **The state moves onto the node and [flags.md](../flags.md) becomes a derived index** — the same shape
  [decisions.md](../decisions.md) already has, one line per flag rather than one per node, holding no state
  of its own. This inverts [Graph file format](13-graph-file-format.md)'s *"this file wins where they
  disagree"* and retires mechanical check 6 as a join, replacing it with a generation rule.
- **The file goes entirely**, superseded rather than deleted, and the sweep reads the nodes.

What the answer has to survive:

- **Twenty flags are outstanding today and none of them can be settled at a close.** Their nodes are
  already resolved; they predate the practice and predate flag ids. They are reachable only through the
  sweep, which is the thing this file exists to feed.
- **Not every node closes in front of the human.** Grilling and implementation both end in a human moment;
  a research node and an AFK precondition node do not, so their flags have nowhere to be settled at close.
- **[Graph file format](13-graph-file-format.md) split this file out to make the sweep a single-file
  read**, and the map's extraction fog item recorded that as the reason flag collection *"is no longer an
  argument for extraction"*. Removing the file hands that argument back, and at the dogfood target's 179
  nodes the sweep becomes a full scan again.
- **Never-delete binds this file**, so any of these is a supersession-with-annotation and not a removal.
- **[Done-ness and termination](10-done-ness.md) defines being closed partly as the human having read the
  closing report.** Whatever happens here has to leave that definition standing, including the case where
  the report is empty.

One observation that belongs to the question rather than to either option: nineteen settlements, nineteen
as recommended. That is either the practice working exactly as intended — flags put to the human while the
context is fresh and cheap to judge — or a gate that has stopped filtering. The node should say which
before it decides where the state lives, because the two readings do not want the same answer.

Raised by the human on reading node 25's four settled flags, in their own words: *"I think the flags file
should be removed if we say that flags are handled during review before closing the node ? All the flags
will be resolved."*

Ordered ahead of [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md),
which blocks on it: that node writes the flag conventions into
[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md), and deciding this
afterwards would need a second commit against a resolved node.

## Answer

**`flags.md` stays, unchanged in mechanism, with its job restated.** The human, on the recommendation:
*"ok for recommended"*.

What died is neither the file nor the checkbox but the **queue reading** — the assumption that an
unchecked box means *waiting for the closing report*. Under the settle-at-close practice the pile has
been frozen at twenty across three consecutive nodes while nineteen new flags were raised and settled.
The unchecked count stopped being a backlog and became a residue.

### What the file is

The graph's **capped index of every judgement an agent made on its own** — the flag counterpart to
[decisions.md](../decisions.md), and the same relation to a node's `## Flags` that
[decisions.md](../decisions.md) has to its `## Answer`.

A `flags.md` line is one capped sentence. The node's `## Flags` entry is free prose, several lines,
sometimes carrying struck-through corrections inside it. They are two renderings at two resolutions,
not one fact stored twice, and the checkbox is the least of the difference. The closing report is
readable **because** the one-liner was written report-shaped, at raise time, by the agent that had the
context. Without the file, that summary has to be authored for every flag in the graph at report time,
from prose whoever writes it did not write — at the moment the design most wants the manager cheap.

That is why the file survives the practice emptying it: its value was never the state column.

### Why the premise cannot hold

The node was raised on the reading that if flags are handled before a node closes, all flags will be
settled and the file has nothing left to hold. Three things falsify it.

- **Twenty flags are outstanding and none can be settled at a close.** Their nodes resolved before the
  practice existed. They are reachable only through this file.
- **The practice cannot reach every node by construction.** [Write the worker contract
  skills](22-worker-contract-skills.md) and [When an AFK worker cannot
  proceed](23-worker-cannot-proceed.md) both record that a `research` node's and an AFK `precondition`
  node's flags wait for the closing report, because those kinds never end in front of the human.
- **A flag can survive its own gate.** `22.4` was returned as a question and took two further rounds.

### The nineteen-of-nineteen reading: the practice working, not a gate that stopped filtering

Recorded because the node required it to be said, and because the answer's framing of what died rests
on it. An `ASSUMPTION` marker means *I believe this is right and was not authorised to decide it*, so a
high settle rate is what a calibrated marker should produce; a worker that doubted its own call would
raise instead. And four of the nineteen carried more than assent: `22.2` added a rule to the product,
`22.4` was refused, `25.3` was restated by the human as a rule, `25.4` had to be explained before they
would answer it. A gate that had stopped filtering would look like a batch of bare assents every time,
and that is not the record. Either reading keeps the file, so this did not gate the decision.

It also dates [Friction from running this map by hand](24-self-hosted-friction.md)'s finding 5 —
*"flags are write-only, thirteen outstanding, zero settled"*. The condition it measured no longer
holds: the finding is correct about the period it covers and the practice is what changed it.

### What is unchanged, stated because both were asked

- ~~**Mechanical check 6 stays exactly as it is** — every `## Flags` entry has a line in
  [flags.md](../flags.md), and none the other way, joined on the flag's id. Nothing in this answer moves
  state, so nothing about the join changes.~~ **Overruled by the human** at this node's own flag
  settlement, on the condition *"extend the check if it already exists"*. It does, twice over: the check
  is `graph-conventions.md`'s line 244 today, and the **sixth delta** already obliges
  [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md) to
  rewrite it as an id join. So **check 6 also compares the two states** — a flag `[x]` in
  [flags.md](../flags.md) must be marked `settled` on its node and the reverse — which is one clause on a
  line already being rewritten rather than a new invariant. The gap it closes was opened deliberately by
  the seventh delta and is the subject of flag `27.2`.
- **[Graph file format](13-graph-file-format.md)'s *"this file wins where they disagree"* holds, and
  its ground changes.** It originally rested on the checkbox living only here, so the two could never
  disagree — a ground the seventh delta destroyed when it put `settled` on the node too. The ground now
  is the one the index reading supplies and which generalises: **the authoritative copy is the one the
  sweep and the report are built from.** The rule is the same; what should be written down is the
  reason, because the old reason is false.
- **The raise and settle procedures are unchanged**, except where the seventh delta already changed
  them.

### What [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md) has to write

Four things, none of which requires re-deciding anything:

1. **A statement of the file's job** in `graph-conventions.md`, which currently states its form and
   never its purpose: `flags.md` is the capped index of the graph's agent judgements, one
   report-shaped line each; the closing report is its unchecked lines; the line is written at raise
   time by whoever has the context, and never reconstructed later.
2. **The ground for *"the checkbox lives only in `flags.md`"*** — which under the seventh delta is no
   longer true as written and becomes *this file wins, because the sweep and the report are built from
   it*.
3. **The `### Settle a flag` procedure is wrong on disk today.** It reads *"No other file changes, and
   the node file is not touched."* The seventh delta requires the flag to be marked `settled` in the
   node's `## Flags` too. That sentence is the exact text to correct.
4. **Settle-at-close as the norm and the report as the exception path**, so the report's flag section
   is understood as covering what had no human moment — flags predating the practice, and flags from
   the two kinds that never end in front of the human — rather than as the ordinary destination of
   every flag.

### The residual

The twenty have exactly one route to the human: the closing report. Most efforts are never closed, and
this effort's destination is a checklist rather than an empty frontier, so on efforts like it that
route may never open. This answer does not change that and does not claim to. It is the reason the file
holds them rather than the nodes: whatever eventually reads them reads one file of capped lines.

## Flags

`27.1` **· settled** `ASSUMPTION` — settled the nineteen-of-nineteen reading from the record rather than by asking the
human — the gate is filtering — and the answer's account of what died rests on it.

`27.2` **· settled, and overruled** `ASSUMPTION` — left mechanical check 6 as an existence join, so
nothing detects a node marked `settled` whose [flags.md](../flags.md) line is still unchecked; declined to
extend an invariant for a divergence that has not occurred. **The human reversed it** — *"extend the check
if it already exists"* — and it does, so check 6 gains the state comparison and
[Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md) carries
it. The checkbox in [flags.md](../flags.md) records that the human has **dealt with** a flag, not that
they agreed with it; `22.4` is the precedent, refused and checked. This is the second flag in the graph
whose settlement reversed the judgement it records.

`27.3` **· settled** `ASSUMPTION` — **filed by the manager, by running [Off-contract subagent
output](17-off-contract-output.md)'s check on this node's own handover.** The answer restates the
**ground** of [Graph file format](13-graph-file-format.md)'s *"this file wins"* rule — from *the checkbox
lives only here* to *the sweep and the report are built from it* — and instructs node 26 to write the new
reason into the shipped document. That restatement entered from a manager note asking whether the old
rule still held, not from the human and not from the worker's own reading; the rule itself is unchanged
and no resolved node's text is edited, but the reason a resolved node gave for it is being replaced in
the product. **Third consecutive node on which this check has fired, and the third on which what it found
was the manager.**

## Interview

### Attempt 1 — routing key `graph-workflow/27/a1`

**Q1** — Does `flags.md` stay?

The worker recommended **keeping it, mechanism unchanged, with its stated job corrected**: it stops being a
queue waiting for the closing report and becomes the graph's capped index of every judgement an agent made
alone — the flag counterpart to [decisions.md](../decisions.md) — carrying a state column that
settle-at-close now usually writes as already settled. In its words, *"what died is not the file and not the
checkbox but the assumption that an unchecked box means 'waiting for the report'"*.

Three findings under it. **The premise does not hold**: twenty lines are unchecked and unreachable at a
close, and the practice cannot reach a research node or an AFK precondition node by construction — both
recorded on [Write the worker contract skills](22-worker-contract-skills.md) and [When an AFK worker cannot
proceed](23-worker-cannot-proceed.md) — while `22.4` survived even a gate, for two further rounds. **The
checkbox is the least of what the file does**: a line here is one capped sentence and the same flag's node
entry is free prose, which is the relation [decisions.md](../decisions.md) already has to a node's
`## Answer`; delete the file and someone authors every flag's summary at report time, from prose they did
not write, at the moment the map most wants the manager cheap. **Two fog items lean on it**, extraction and
graph-progress. Set aside: moving the state onto the node and deriving this file, and removing the file so
the sweep reads the nodes.

Settled on the worker's own authority, against the manager's framing: the nineteen-of-nineteen settle rate
is the practice working rather than a gate that stopped filtering, since an `ASSUMPTION` flag means *"I
believe this is right and was not authorised to decide it"* and a calibrated marker should settle often —
and four of the nineteen carried more than assent. Both readings keep the file, so it does not gate the
decision.

**A1** — `verbatim`

> ok for recommended

The option that phrase points at is the worker's `RECOMMENDED` block, quoted above and **written by the
worker, not by the human**. It is also a divergence from the **manager's** position rather than from the
worker's: the manager had argued to the human that the checkbox was the dead part, relayed the worker's
disagreement, and said the worker's argument was the stronger one.

### Settling the flags

The manager put all three, recommending settlement of `27.1` and `27.3` and **recommending against**
`27.2` — arguing that mechanical check 6 should be extended to compare the two states rather than only
check that both exist, since the join on ids already exists, node 26 is the free moment to write it, and
the manager had hand-written eight `settled` marks in one session, one edit each.

**A** — `verbatim`

> 27.1 ok 27.2 ok 27.3 ok

`27.1` and `27.3` are settled on that. **`27.2` was not**, and the reason is this node's own sibling
decision: under [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md)'s residual case — settled as flag `25.3`, in the human's words
*"If an anwser is not clear, yes ask again"* — a terse reply that does not make clear which option it
points at is recorded and asked about rather than resolved by the manager. Here `ok` has two readings
that do opposite things: settle the flag as the worker wrote it, leaving check 6 alone, or take the
manager's recommendation, which is to extend it. The reply is recorded above and the question was put
again.

This is the first live instance of that residual case, two nodes after it was decided, and it arose
because the manager had recommended **against** one of the flags it was relaying — which is a shape
neither [Relay protocol](08-relay-protocol.md) nor [Off-contract subagent
output](17-off-contract-output.md) anticipated. A bare assent is unambiguous when the manager's
recommendation and the flag agree, and ambiguous exactly when they do not.

**A** — `verbatim`

> extend the check if it already exists

A conditional rather than a bare choice, and the manager answered the condition on disk before acting:
check 6 is `graph-conventions.md`'s line 244 and states existence only, with no id join in the shipped
text; the **sixth delta** already obliges [Carry the recorded deltas into the shipped skill
files](26-carry-deltas-into-shipped-files.md) to rewrite that line as an id join; and the throwaway
checker this map is run with compares counts per node rather than ids. So the check exists and is already
being rewritten, and the state comparison is one clause on it rather than new machinery. `27.2` is
reversed on that basis and node 26 carries it.

## Annotation: approving the node's end settles its flags, with no separate assent

The human's standing instruction, `verbatim`, given while four nodes were live: *"Also, when I approve the end
of the node, the flags should be considered ok"*.

This refines the settle-at-close practice this node was written about rather than replacing it. The practice
already put a node's flags to the human at **the human moment that ends its node** — a grilling node's last
answer, an implementation node's gate — and [What the manager works on next, and how the human redirects
it](16-human-steering.md) had just fixed that flag settlement *"rides the human moment that already ends its
node… so it never queues on its own"*. What is new is that riding that moment means **settled by it**: the
approval is the settlement, and the manager neither asks a second time nor waits for a second assent.

**It corrects a practice the manager had been following twice in one session.** At [The checker's spawn
carries the effort's ground rules](42-checker-spawn-carries-ground-rules.md)'s gate and at [Record a
checker's not-covered part on `## Review`](38-recording-a-not-covered-part.md)'s, the manager recorded the
node's flag as standing **outstanding** on the ground that the human's approval *"did not reach it"* —
reasoning that approving a diff is not the same act as confirming the judgement that produced it. Under this
instruction the approval did reach it. Both flags were settled shortly afterwards by an explicit word, so no
state was ever wrong; the reasoning written on those two nodes is superseded, and is left there under the
never-delete rule.

**The manager's note on what now makes this safe, not the human's.** A flag exists to record a judgement the
human may want to revisit, so settling one by implication is only sound if they saw it. That puts weight on
the **gate payload**: it must present each of the node's flags — what was decided and on what — because
approval now discharges them. The duty already existed and was being met; what changes is that it stops
being good practice and becomes the thing the settlement rests on. A gate payload that omits a flag now
settles it silently.

## Annotation: the frequency in `### The residual` is withdrawn, and the conclusion stands

*Filed by the manager from [The human rejects *most efforts never end*](86-most-efforts-never-end-rejected.md)'s
`INVALIDATIONS`, site 5. Corrects a cited ground rather than superseding the answer; the disposition is flag `86.1`.*

`### The residual` says *"Most efforts are never closed."* The human has rejected that claim and the workflow now
states no frequency in any wording. **The conclusion stands**, and the sentence's own next clause already carries the
surviving form: *"on efforts like it that route may never open."* A route that exists for a case that occurs rarely
is still required to exist.
