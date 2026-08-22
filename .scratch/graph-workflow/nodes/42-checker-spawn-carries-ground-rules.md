# The checker's spawn carries the effort's ground rules

Type: implementation
Status: resolved

## Question

The blind checker reads no map, so an effort's ground rules — including a workaround the human instructed
after friction — reach every worker except the one whose own contract is a measured source of friction. Make
the ground rules a given in its spawn, by the same route the bar's non-command half already travels.

Reported by [Workflow self-improvement during use](19-workflow-self-improvement.md)'s worker, which wrote the
acceptance condition below. The observation behind it was the manager's, put to the human alongside that
node's sixth question and endorsed in their words: *"fair point from the manager"*. The remedy is the worker's
own and is flagged as such on that node, `19.3`.

## Acceptance condition

Done when all of the following hold.

1. `.claude/skills/expedition-checker/SKILL.md`'s section listing what the checker is given in its spawn
   includes the effort's **ground rules**, given as text copied into the spawn rather than as a pointer to any
   file, and says that where the effort declares none there is nothing to give.
2. That section states why the copy is necessary: the checker does not read the map, so anything the map holds
   that bears on the check reaches it only as text in its spawn.
3. That section states the boundary on what may be copied — a standing constraint on the effort, true of any
   node's work — and that an account of what happened on this node or anywhere in the record may not be
   copied, that being what the checker is kept blind to.
4. The count word introducing that list is correct for the number of items it now holds. It currently reads
   `Four things, in the spawn:`.
5. No item already in that list is removed, renumbered out of existence, or changed in meaning.
6. No file outside `.claude/skills/expedition-checker/` is changed by this work.
7. The working tree meets the bar.

### Audit at claim time, by the manager

*The manager's own note, not a change to the condition above.* Read against [An acceptance condition is
self-contained text](33-condition-is-self-contained.md) and [The clause that says no resolved node changes
cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md) before the node was handed to
anyone, which is the practice [What the checker contract owes to having been run](31-checker-contract-owes.md)
established and [A worker's handover carries no acceptance condition for the node it
mints](35-handover-mints-no-condition.md) bounded — an audit that can still miss what a blind check catches.

**All seven clauses pass the self-containment rule.** Clauses 1–3 state their demand in their own words and
name the file it lands in, so the checker reads the file and judges; none of them says *as decided at node NN*
or sends its reader to the record. Clause 6 quantifies over **the tree** rather than over the record, which is
the distinction node 36 shipped — *no file under this path changes* is answerable from the diff. Clause 7 is
the bar, the one exemption, and it reaches the checker by its own route.

**One thing found, and handed over as written.** Clause 4's second sentence — *"It currently reads `Four
things, in the spawn:`"* — is a fact about the file **before** the work, and once the work lands it is false
of the file the checker will be reading. It is orientation rather than a demand, and it is what makes the
clause self-contained at all: without it the checker has no anchor for *"the count word introducing that
list"*. The hazard is only that a cold reader may take it as an assertion to verify and report a discrepancy
against a correct file. Left as written, because `graph-conventions.md` fixes that the manager *"hands it over
as written and supplies nothing it omits"*, and this condition is the minting worker's text rather than the
manager's.

**Clause 6 leaves nothing behind, and this was checked rather than assumed.** The clause forbids touching any
file outside `.claude/skills/expedition-checker/`, which is the shape that on [Ship the FRICTION flag and the
self-edit disclosure duty](41-ship-the-friction-flag.md) leaves `CONTEXT.md` in the older form. Here no
sibling file describes what the checker is given: `graph-conventions.md` names the checker four times and
never enumerates its spawn — its statement is that the checker *"is handed the condition as text and has not
read the node"*, which a fifth given does not contradict — and the five worker contracts describe the checker
only as a second, independent, read-only worker. So the count word in clause 4 is the only count in the
repository that has to move.

**One absence that predates this node.** `ground rules` is used by all five worker contracts and by
`graph-conventions.md` and has no entry in [`CONTEXT.md`](../../../CONTEXT.md). This node adds a sixth user of
the term rather than coining one, so the gap is not clause 6's doing and not this node's to fix. It is [What
keeps the shipped files consistent when a decision changes a term](29-shipped-file-consistency.md)'s, and it
is the second such absence found by a claim-time audit rather than by anything that checks — node 41's
`FRICTION` being the first.

## Answer

`.claude/skills/expedition-checker/SKILL.md`'s `## What you are given` now lists **five** things rather than
four. The fifth is the effort's ground rules, as text: *"the standing constraints the whole effort works
under, as text. Follow them. They are written in the effort's map, which every other worker reads and you do
not, so they are copied into the spawn rather than pointed at: anything the map holds that bears on your check
reaches you only as words in the spawn. Where the effort declares none there is nothing to give, and this
given is absent."*

The boundary on what may travel that route is a paragraph of its own, placed immediately after the paragraph
that establishes the record and the checker's blindness to it — the concept the boundary leans on, so the
reader meets it before the constraint that uses it. A ground rule is a standing constraint on the effort, true
of any node's work, and that is what makes it safe to hand a blind checker: a rule holding everywhere tells it
nothing about the work in front of it. An account of what happened, on this work or anywhere in the record, is
not a ground rule and never travels by this route, that being exactly what the checker is kept blind to.

Items 1–4 are byte-identical to before; the only text removed anywhere is the word `Four`.

Three calls a later reader would otherwise re-derive.

**The given carries a duty, `Follow them.`** The acceptance condition asked only that the section *include*
the ground rules and said nothing about what the checker does with them — and a given handed over with no
instruction attached is text the checker holds and cannot act on. The wording matches the five worker
contracts, each of which closes its own ground-rules paragraph with *"Follow both."*, so the checker becomes
the sixth contract to carry the duty rather than the first to invent one. Flagged as an assumption.

**The map is named, and glossed for a reader who has never heard of it.** Before this change the word `map`
appeared nowhere in the checker contract. Clause 2 requires the reason for the copy to be stated and the
reason *is* the map, so the item names it and says in the same breath what it is to the checker — the file
every other worker reads and it does not — rather than leaning on a term the contract had never introduced.

**Nothing else in the repository holds a count of the checker's givens, and this was verified rather than
assumed.** `graph-conventions.md` states only that the checker *"is handed the condition as text and has not
read the node"*, which a fifth given does not contradict, and the five worker contracts describe the checker
as a second, independent, read-only worker without enumerating what it gets. So the count word in this file
was the only count that had to move, and **no sibling file is left in the older form**.

One absence stands deliberately: `ground rules` still has no `CONTEXT.md` entry, and this change adds a sixth
user of the term rather than coining it. Clause 6 confined the work to `.claude/skills/expedition-checker/`,
and the gap belongs to [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md).

## Flags

`42.1` **· settled** `ASSUMPTION` — The fifth given carries the duty `Follow them.`, which the acceptance condition never
asked for: it required the section to include the ground rules and said nothing about what the checker does
with them. Settled on parity with the five worker contracts, each of which ends its own ground-rules paragraph
with *"Follow both."*, on the ground that a given handed over with no duty attached is text the checker holds
and cannot act on.

## Review

**Checker, run 1 — `PASS`.** Nothing found, no questions, and no part of the condition named as not covered.
The checker established all seven clauses one by one, naming file and line for each; on clause 5 it ran
`git diff --word-diff=plain --unified=0` over the whole file and reported exactly one word altered
(`Four` → `Five`) against 11 inserted lines in two hunks, with no paragraph rewrapped, so there was no
wrap-hidden edit to unwrap and compare. On clause 2 it went and verified the *premise* rather than the
sentence — confirming that all five sibling worker contracts and `graph-conventions.md` do point their worker
at the map's `## Notes` for the ground rules, which is what makes the copy necessary.

Two things it settled before reading the work, both required by its own contract:

- **The standard-moved question.** The changed file is the checker's own contract, which is not among the
  standards the bar carries here — those being the machine's coding principles and naming discipline,
  `CONTEXT.md`'s refused vocabulary, the effort's ground rules as given, and the acceptance condition, none of
  them in the diff. So nothing the bar rests on moved under the check and no raise was due on that ground. It
  read the contract from disk in its post-change state, and reported that the added given matched what its
  spawn had actually supplied — so the change altered nothing about how it checked.
- **The reviewing skill.** It found two candidate skills and one command and ran no part of any of them,
  declining under the contract's second permitted route and saying why for each: one is registered inline with
  no files on disk, so it could neither read nor constrain what that skill's own sub-agents would be handed,
  and its spec axis is aimed at an originating request that does not exist here and whose search order points
  into the record; the other applies fixes, which its first hard rule forbids. It held the work against the
  standards it had found by hand instead.

It also confirmed the command half of the bar is vacuous rather than assuming it from the spawn, scanning the
root for every manifest, task runner, formatter and CI directory it could name and reporting none, and it
unwrapped the added text into one unbroken line before scanning for the refused vocabulary.

**The manager's note on this run, not the checker's.** This was the first spawn in the effort bound by the
rule this node ships, so the manager had to decide what this effort's ground rules are before it could hand
them over — and [map.md](../map.md) is ambiguous on exactly that point, saying the effort *"declares
neither"* of the two optional blocks and then that *"its ground rules are the standing preferences above"*.
The manager passed the subset of those preferences that are standing constraints true of any node's work,
stated plainly, and withheld everything that is an account of what happened — the boundary this node ships,
applied to its own check. The checker reported using them, under the bar, without remarking on them.

**Gate — `approve`.** The human's words, `verbatim`: *"approve for the implementation"*. No correction round
was run and none was asked for, so the checker's single `PASS` is the whole of this node's chronology. They
named the outcome in the word the gate asks for, which is the second gate in this effort to do so without a
reading having to be recorded for it.

Two things this gate did **not** carry, recorded so neither is read as having been settled here. Flag `42.1`
was put to the human in the same message and their reply did not reach it, so it stands **outstanding**:
approving a diff that contains `Follow them.` is not the same act as confirming the judgement that put it
there. And the ambiguity the manager's note above reports in [map.md](../map.md) — *"declares neither"* against
*"its ground rules are the standing preferences above"* — was raised at this gate and is untouched by it. It
is not this node's to fix, and it is now load-bearing for every checker spawn under the rule this node ships.

## Annotation: the ambiguity this node's `## Review` declared "not this node's to fix" is now closed

*Filed by the manager, in the reporting worker's own words.* From [What keeps the shipped files consistent when
a decision changes a term](29-shipped-file-consistency.md):

> no clause of it changes, and the ambiguity its own `## Review` recorded and declared *"not this node's to
> fix"* is closed here. Its shipped *"where the effort declares none there is nothing to give"* branch stops
> applying to this effort, which now declares a block, and every checker spawn from here carries that block as
> text instead of the manager's per-check judgement.

**So this node is completed rather than contradicted.** It shipped the fifth given and the boundary on what may
travel it; what it could not do was make the effort it was running on *declare* anything, and `map.md` said in
one sentence both that this effort *"declares neither"* and that *"its ground rules are the standing preferences
above"*. The manager resolved that per check, on its own judgement, at every check from this node's own onward.

**The five declared items were tested against this node's boundary and that is what kept the map out of them** —
the manager-context findings, the token measurements and the landing policy's history are all *accounts of what
happened*, which this node forbids travelling by the ground-rules route.

**One thing measured here rather than predicted.** [Reconcile a method skill's instructions with the contract's
hard rules](48-method-skill-conflicts-hard-rules.md)'s second checker run is the **first spawn in this effort
whose ground rules were declared rather than authored per check**, and the first that does not carry the
manager's product-file gloss, which the human struck as redundant. Its outcome is evidence about this node's
fifth given rather than only about that node's work.
