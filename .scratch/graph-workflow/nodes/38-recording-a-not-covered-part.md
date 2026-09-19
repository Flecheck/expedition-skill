# Record a checker's not-covered part on `## Review`

Type: implementation
Status: resolved

Blocked by: 31

## Question

[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md) fixes the `## Review`
chronology as **three entry kinds** — a run naming `PASS`, a run naming `FAIL` and which of the two failed,
or a run that raised instead of judging. [What the checker contract owes to having been
run](31-checker-contract-owes.md) has now given the checker a fourth thing it can hand back: a `PASS` or a
`FAIL` that **names a part of the acceptance condition it does not cover**.

An entry that says only `PASS` loses that. A later reader cannot tell which parts the check actually covered,
and the residual the manager picked up has nowhere to be recorded as discharged.

**What does the entry record, and where does the manager's discharge of a reserved part land?**

### Why this exists

Reported by [What the checker contract owes to having been run](31-checker-contract-owes.md)'s worker, as the
cost of the rider it had just shipped. Its own framing: this is the same shape [Whether a spawn may override a
shipped worker contract](28-spawn-overriding-a-contract.md) ruled for the mid-node amendment — **an uncovered
case rather than a departure** — and the same cost flag `26.7` records, a described case with no rule reaching
it.

### Two things already established, and they bound the answer

**The duty being recorded is real and already named.** [An acceptance condition is self-contained
text](33-condition-is-self-contained.md) found that *the manager is the residual checker of anything a
condition addresses to a party that cannot see it*, and the manager verified that node's reserved clause
itself. So a reserved part is not a gap in the check; it is a handoff, and what this node designs is the
record of the handoff.

**The duty is also now avoidable, which changes how much machinery it deserves.** [The clause that says no
resolved node changes cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md) wrote a
condition with every demand landing in a file and its checker reserved nothing; node 31's did the same and
its checker reserved nothing either. Two consecutive checks with no residual, against node 33's three
reserved clauses on one condition. So the recording form is for the **exception** rather than the common
case, and a form that costs every entry something to serve a case that a well-written condition never
reaches would be the wrong trade.

### One thing not to assume

That the answer is a fourth entry kind. The rider is deliberately **not** a fourth return shape — node 31's
worker split `NOT COVERED:` from `QUESTIONS:` into the same structural slot precisely so the three shapes and
the three entry kinds would stay valid, and flag `31.1` records that call. An entry kind is the parallel
choice one level up, and taking it would undo the reason the rider was shaped that way. The cheaper
candidates are a required field on an existing entry, or the manager's discharge recorded where it happens
rather than as part of the chronology.

### What the answer touches

[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s `## Review` shape, and
possibly `expedition-checker/SKILL.md` if the entry form needs anything the rider does not already carry.

**Sequencing.** `Blocked by: 31` is a real edge rather than a preference: the rider has to ship before a
recording form can name it. Nothing else on the frontier touches `graph-conventions.md`.

## Acceptance condition

Done when all of the following hold.

1. The section of `.claude/skills/expedition/graph-conventions.md` that documents a node's `## Review`
   states what a checker run's chronology entry records when that run named a part of the acceptance
   condition it did **not** cover, so that a later reader of a node's `## Review` can tell which parts of
   the condition that run covered and which it left uncovered.
2. That same section states where the manager's discharge of an uncovered part is recorded, and requires
   that record to name who established the part.
3. That section currently reads *"Three things, and nothing beyond them:"* and then fixes those three: the
   checker's chronology, one entry per run, a run either naming `PASS`, or naming `FAIL` and which of the
   two it failed — the acceptance condition or the bar — or having raised instead of judging, in which case
   it issued no verdict at all and the entry says what it raised; each correction round, numbered, with the
   human's words verbatim and what the worker changed; and the gate's outcome, named as one of approve /
   correct / reject, a reject also recording what implementing the node surfaced and which of the three
   routes it then took. After this work all three are still present and none has lost anything it required.
   Where the count word or the phrase *"and nothing beyond them"* is no longer true of the section, it is
   made true in the same change.
4. An entry for a run that covered the whole condition and reserved nothing gains no required field and no
   new mandatory sentence. Whatever form this work adds is reached only by an entry that has something to
   record under it.
5. That section says, in at least one sentence, why the form it fixes is the form chosen rather than the
   other candidate, the two candidates being a part of an existing entry and a record made where the
   manager discharges the reserved part.
6. Where `.claude/skills/expedition-checker/SKILL.md` is changed by this work, its `NOT COVERED:` shape and
   its three return shapes — `PASS`, `FAIL`, and a raise that hands back no outcome — all remain valid, and
   none of them is renamed or removed.
7. No file outside `.claude/skills/expedition/` and `.claude/skills/expedition-checker/` is changed by this
   work.
8. The working tree meets the bar.

### Audit at claim time, by the manager, of a condition the manager wrote

*The manager's own note, not part of the condition above.* Written and then read back against [An
acceptance condition is self-contained text](33-condition-is-self-contained.md) and [The clause that says
no resolved node changes cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md).

**Self-containment.** Clause 3 copies the three entry kinds in full rather than sending the checker to read
them, which is the one place this condition would otherwise have pointed at material held elsewhere — and
the material is not merely elsewhere but *pre-change*, recoverable only from git. Clause 7 quantifies over
the **tree** and not the record, which node 36 permits. Clause 8 is the bar, the one exemption.

**This condition states properties and does not dictate a form, on purpose.** The node's question — *what
does the entry record, and where does the manager's discharge land* — is genuinely open, and its own text
names two candidates without choosing. A manager choosing between them here would be deciding the node
rather than framing it, so clauses 1, 2, 4 and 5 fix what must be true of any answer and clause 5 makes the
worker say why it picked what it picked. The cost is that the checker can establish that a reason is stated
and not that it is the right reason.

**Two things the manager notes against itself.** This condition is manager-written for a node the manager
did not mint — it was reported by [What the checker contract owes to having been
run](31-checker-contract-owes.md)'s worker, which named the work and did not write a condition for it. Who
should write one in that case is [A worker's handover carries no acceptance condition for the node it
mints](35-handover-mints-no-condition.md)'s settled rule for the reporting worker and [What writes the
acceptance condition for a node the manager mints](39-condition-for-a-manager-minted-node.md)'s open
question for everyone else, and this is the manager acting ahead of that node rather than under it. And
three of the four remaining implementation nodes on this frontier carry no condition at all — nodes 32 and
40 say so in as many words — so this gap is not particular to this node.

## Answer

The form is fixed in `.claude/skills/expedition/graph-conventions.md`, in the section documenting a node's
`## Review`. Both halves live on **the entry for the checker run that named the part** — nothing else was
added to the log.

*What the entry records.* Entry kind 1 gains a conditional clause: a run may additionally name a part of the
acceptance condition it did **not cover**, and its entry then carries that part as the checker wrote it,
quoted. The outcome on that entry covers the rest of the condition and no more, so the entry states both
halves — the parts named are what the run left, and the rest of the condition is what it covered. A reader
needs the node's `## Acceptance condition` and nothing else to read coverage off the entry.

*Where the establishing lands.* On that same entry, beside the part: who established it and what they read or
ran. Usually the manager, which holds the handover the checker does not; it may instead be the human at the
gate reading it themselves, or a later run of the check. The `who` field is load-bearing precisely because the
establisher varies.

*Why this rather than a record made where the establishing happens.* Stated in the file, and it is the reason
acted on. The part is an obligation left **open**, and what a later reader needs is whether it still is. Keyed
to the act, the record moves with whoever acted — three parties, each writing somewhere else — so there is no
one place to look; and a part nobody ever established writes nothing anywhere, which is exactly the case the
record exists for. An absent record is invisible. Keyed to the entry that named the part there is one place
whatever happened, and a part still open is legible there as a part with nothing beside it.

*Three calls a later reader would otherwise re-derive.*

1. **Not a fourth entry kind, and the count word did not move.** `## Review` still says *"Three things, and
   nothing beyond them"*, and the file now says so explicitly: this is entry kind 1 carrying what its run
   handed back. All three kinds keep every word they required — item 1's only textual change is an appended
   clause plus the reflow of its last line.
2. **The clean entry pays nothing.** Stated as its own paragraph: no part to name, nothing owed, no field and
   no sentence, and the entry reads exactly as it did before. The form is reached only by an entry with
   something under it. The paragraph also names why the exception is rare — a condition whose every demand
   lands in a file gives a checker nothing to name — pointing at the self-containment rule already in the same
   document rather than restating it.
3. **`expedition-checker/SKILL.md` needed nothing and was not touched.** Checked rather than assumed: the
   entry needs the part quoted (the rider gives `<the part, quoted, and why establishing it is outside what
   you were given>`) and needs the outcome's narrowed meaning (the contract already says *"Your `PASS` then
   means the parts you established and no more, so say that plainly"*). *Who* established it is the
   establisher's own text, never the checker's. The contract also already tells the manager it is still
   holding the material. So the rider carries the whole input to this form, and its three return shapes and
   `NOT COVERED:` are untouched and still valid.

*One addition no clause asked for, flagged below:* the establishing happens **by the gate at the latest**, the
node resolving there with nothing after it to establish anything.

*No new vocabulary was minted.* The document uses **not covered**, the label the checker prints, so the
manager filing the block recognises what it is pasting; and **establish**, the verb the checker contract and
the condition both already use. `reserve`, `residual` and `discharge` are effort-record words absent from
`CONTEXT.md` and were deliberately not shipped into the document.

## Flags

`38.1` **· settled** `ASSUMPTION` — Nothing in the acceptance condition or in any resolved node fixes **when** an uncovered
part must be established, and I wrote *"by the gate at the latest, the node resolving there with nothing after
it to establish anything."* Settled myself because a record with no deadline can be filed after the node
resolves, which would mean the human approved work whose condition was only partly established and nobody was
ever late. It is a duty on the manager, and the conventions document is where manager procedures live, so it
is stated there rather than left for the unwritten manager skill. Below all three raise triggers: it is my
section's own text, it changes no other file, and I hold a recommendation I believe.

## Review

**Checker, attempt 1 — dead, no outcome.** The first blind checker was spawned with the five givens the
contract now requires and died on its first turn, on an API session limit rather than on anything about the
work. Its entire output was *"I'll first find the standards this repo and machine carry, before reading the
work."* — the contract's own instruction to find the standards before reading the work, and nothing beyond it.
It read no part of the work, established nothing, and issued no verdict, so nothing from it is inherited by
the attempt that follows and the whole condition is checked again from the start.

Recorded because a dead run is a real entry rather than an absence: [Write the worker contract
skills](22-worker-contract-skills.md)'s `## Review` set the precedent that a checker which dies is written
down, and [When an AFK worker cannot proceed](23-worker-cannot-proceed.md) added the third entry kind for a
run that issues no verdict — of which this is a fourth case again, a run that issued no verdict because it
never ran rather than because it raised. What the shipped chronology has no word for is a run that neither
judged nor raised, and this is the second such run in the effort's history.

**Checker, attempt 2 — `PASS`.** All eight parts met, nothing reserved, no questions. A fresh agent with no
statement of what changed, checking the whole condition as though for the first time, since attempt 1
established nothing and telling it about a dead predecessor would have been an account of what happened —
which the ground rules given in its own spawn now forbid travelling that route.

How it read the work is the part worth keeping: it extracted the `## Review` section from `HEAD` and from the
working tree, **unwrapped both into one unbroken line per paragraph, and diffed those** — establishing that
the single deleted line is item 1's last line re-emitted with one sentence appended, that items 2 and 3 are
byte-identical, and that the intro line is untouched. That is the reflow rule from [Carry the recorded deltas
into the shipped skill files](26-carry-deltas-into-shipped-files.md) applied without being prompted.

It settled the standard-moved question first, and on the right ground: *"The one changed path is the product
of this work, not a yardstick over it."* Everything the bar names — the two machine skills, `CONTEXT.md`, the
ground rules as text — is untouched by the change set, so a check was possible without a raise. Where it used
the changed file's own rules as internal-consistency context, it noted that that text sits outside the changed
hunk and did not move. **This disposes of the hazard the manager flagged before spawning it** and had
deliberately declined to resolve on the checker's behalf: that a node whose work *is* a standards document
would trip its own checker's operative-content raise ground. It does not, and the distinction that saves it —
product of the work versus yardstick over it — is the checker's own.

It declined the one reviewing-skill candidate on a sharper ground than the previous run had: the plugin's
skill bodies are **not on disk at all**, only a marketplace listing sourcing them from a remote, so it could
neither read the internals nor constrain what that skill's sub-agents would receive or search. It held the
work by hand instead, and confirmed the command half of the bar was vacuous by searching the whole tree for
any lint, format, CI, manifest or task-runner config and printing nothing.

Three things it weighed against the project criteria and judged not failures, recorded because it said so
rather than leaving them to be found: *"both halves"* denotes two different pairs in two places,
disambiguated by context and sitting in a rationale paragraph where no instruction turns on it; *"the node
resolving there"* is exact on the approval path and loose on a reject, while the operative deadline holds on
every path; and the manager's half of the entry is not restated as its own marked note, the file's global
scribe rule already governing it. It also reported that `map.md` had become dirty during the check, which was
not on the list in its spawn — correct, and excluded either way.

**Gate — `approve`.** The human's word, `verbatim`: *"approve"*. No correction round was run and none was
asked for, so this node's chronology is one dead run and one `PASS`.

Two things this gate did not carry. Flag `38.1` was put to the human in the same message and their reply did
not reach it, so it stands **outstanding** — the deadline *by the gate at the latest* is in the shipped file
and the judgement behind it is unconfirmed. And this is the third gate in a row answered with the outcome word
the gate asks for, against node 33's gate which arrived as *"you can continue"* and cost a recorded reading;
the practice of asking for the word is holding.

**One thing about the queue rather than the work.** This gate was raised ahead of a further question from
[Human-initiated steering](16-human-steering.md)'s live interview, which is the two-tier rule that node's own
worker designed and the human endorsed two rounds earlier — a gate being tier 1 because something other than
its own node stops while it waits. It is the first time that rule governed the manager's behaviour rather than
describing it, and the node it governed was the one that wrote it.

## Annotation: one statement here is superseded, from node 45's work

*Filed by the manager, in the reporting worker's own words.* [Nothing checks that a part a checker left
uncovered was ever established](45-nothing-checks-an-uncovered-part.md)'s worker reported this as an
`INVALIDATION` against this node, resolved earlier the same day as commit `d6eb665`:

> Its design is unchanged and one of its statements no longer holds: it describes an unestablished part as
> legible *"as a part with nothing beside it"*, i.e. as an absence, and describes establishing as written
> *"beside the part"*. Under the form this node fixes, an unestablished part is positively marked `OWED` and
> establishing rewrites that marker at the head of the same item. The shipped sentences were updated; whatever
> node 38's own `## Answer` says about the open state being an absence is superseded by this, and it is the
> manager's to mark. Nothing else in that node's answer is contradicted.

So: **this node's design stands and its guarantee is strengthened rather than weakened** — the case it exists
for is now positively marked instead of being read off an absence, which is what made it uncheckable. Every
sentence in this node's `## Answer` describing an unestablished part as *an absence* or an establisher as
*beside* the part is superseded by node 45's form, and is left in place under the never-delete rule.

## Annotation: the reason this answer gave for its own addition no longer stands

*Filed by the manager from [node 235](235-graph-conventions-says-a-node-resolves-at-its-gate.md)'s
`INVALIDATIONS`, in that worker's own words. This node's answer is not changed and nothing above is struck.*

> [Record a checker's not-covered part on `## Review`](nodes/38-recording-a-not-covered-part.md), resolved. Its
> `## Answer` reads: *"One addition no clause asked for, flagged below: the establishing happens **by the gate at
> the latest**, the node resolving there with nothing after it to establish anything."* The addition stands; the
> reason given for it does not, and the shipped file no longer carries it. The contradiction is with the answer's
> stated ground, not with its demand.
