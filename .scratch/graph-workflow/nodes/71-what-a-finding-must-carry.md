# What a finding must carry so it can be swept

Type: implementation
Status: resolved

## Question

A checker hands back **instances**. The implementer repairs the instances, and the rest of the class stays in the
file. On [Restructure `map.md` to what every worker needs](59-restructure-the-map.md) the checker reported three
findings; the worker repaired them, swept its own prose on its own initiative, and **found four more of the same
form**. Nothing in either contract asked for that sweep, and nothing would have caught the four if the worker had
not thought of it.

Two repairs, both reported by that node's checker in its retrospective, and one of them is its own correction.

### 1. A finding carries three parts, not one

In the checker's words:

> Last round I handed back instances plus, in finding 2, half a form. What I did not hand back was the thing that
> makes a sweep runnable: **the discriminator that separates text the implementer may touch from text clause 4
> freezes.** Without it, sweeping `map-history.md` for that form returns 87 hits of which 87 are untouchable, and
> the implementer either drowns or abandons the sweep. Building that filter was most of my work this round.

So a finding carries:

- **the instances**, as now;
- **the form, stated as a predicate** — what makes something an instance, not just what these two were;
- **the extent** — the command that enumerates the form's candidates *over the editable part of the work*.

**The checker had already written the enumerator in order to find the instances**, which is what makes this cheap:
it is handing back work already done rather than asking for new work. In its words, *"it is four lines of shell, it
is worth more than the two instances."*

**Its own two qualifications, which the condition must not lose.** Not every finding reduces to a regex — the
over-claims in authored prose had no mechanical enumerator, *"and that is precisely the class where the implementer
found four more by hand."* But such a finding still has an extent, coarser: **the smallest set that provably
contains every instance** — here the 48 authored lines, computed by the same set-difference. And where a finding
genuinely has no extent, **the checker says so rather than implying the instances are exhaustive.**

### 2. A blind checker may not assert a universal negative

The same checker reported *"No such rule exists"* of a rule that does exist, in a file it was correctly kept from
reading. Its own diagnosis:

> What I could actually establish — that the pointer resolved to nothing in every file I was permitted to read —
> was true, and the defect was real. But the sentence I wrote was wrong, and **it was wrong in the same way the
> thing I was faulting was wrong: I asserted a universal from a bounded search.** A checker blind by design should
> say *"resolves to nothing in the files I hold"* and not *"does not exist"*.

**This is a standing property of the role rather than a slip.** A checker is kept from the record by design, so it
can never establish that something is absent from the effort — only that it is absent from what it holds. The
manager, which holds the record, is the party that can resolve such a finding, and did here.

### The open question, and how it was settled

Both repairs land in `.claude/skills/expedition-checker/SKILL.md`. This node was filed with **no acceptance
condition on purpose**, because one open question stood in front of it: **whether the extent is *mandatory* on every
finding or *owed where it exists*.** Mandatory is simpler to check and would force a checker to invent enumerators
for prose findings, which the checker itself says do not have them. Owed-where-it-exists is honest and gives a
checker a way out that nothing verifies. Under [What the manager works on next, and how the human redirects
it](16-human-steering.md)'s readiness floor a condition made writable by *deciding* the open question inside it does
not pass, so the manager raised it rather than writing one.

**The human settled it**, taking the recommendation as offered — the exchange is at `## Interview`. The answer is
neither side of the binary the node posed: **the extent statement is mandatory and its form varies**, being exactly
one of an enumerator, a bounding set, or an explicit statement that the finding has no extent. That is what the
checker itself proposed in the retrospective above; the binary was narrower than its own source.

The condition below is therefore written by the **manager**, for a node the manager minted, under [Who writes the
acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md)'s four constraints.

## Acceptance condition

*Written by the manager, for a node it minted itself. The audit constraint 2 requires is recorded below the
condition.*

### Scope, and the extent behind it

`.claude/skills/expedition-checker/SKILL.md` is edited, and no other file is.

**The extent, so the scope is measured rather than asserted.** `grep -rln "one entry per failure" --include="*.md" .`
over the repository returns that path and nothing else, and that file is the only shipped contract that states what a
checker hands back. Where the work turns up a statement of finding shape in some other file, **it is reported and not
edited** — reporting it is the whole of what this condition asks for it.

### 1. What a finding carries

After this change, the contract requires that **every finding the checker hands back** carry three things. A finding
means any defect in the work it reports, by whichever of the routes this contract gives it — an entry under a `FAIL`,
or something handed back alongside an outcome — and not only a `FAIL` entry.

- **The instances**, which the contract already requires: what is wrong, where, and what was run or read to find it.
- **The form, stated as a predicate**: what makes something an instance, rather than what these particular ones were.
- **The extent**, which is exactly one of the three below. **A finding carrying none of the three is malformed**, and
  the contract says so.
  1. **An enumerator** — the command that lists the form's candidates over the part of the work the implementer may
     edit. Not the candidates over the whole tree: a command whose hits are mostly text the implementer may not
     touch is not an extent, and building the filter is part of supplying one.
  2. **A bounding set**, where no command fits — the smallest set that provably contains every instance, together
     with how that set was computed.
  3. **A statement, in as many words, that the finding has no extent and its instances are not exhaustive.**

The contract also states why this costs the checker little: it built the enumerator in order to find the instances,
so supplying it hands back work already done rather than asking for new work.

### 2. What a checker blind by design may not assert

After this change, the contract states that **a checker kept from the record cannot establish that something is
absent from the effort — only that it is absent from what it holds** — and requires its findings to be worded that
way.

The property is fixed and **the wording is the worker's**; this condition does not dictate it. What the wording has
to carry is fixed by the checker's own diagnosis of its own error, which is the whole of the evidence and is quoted
here so that nothing outside this condition need be read to check it:

> What I could actually establish — that the pointer resolved to nothing in every file I was permitted to read —
> was true, and the defect was real. But the sentence I wrote was wrong, and **it was wrong in the same way the
> thing I was faulting was wrong: I asserted a universal from a bounded search.** A checker blind by design should
> say *"resolves to nothing in the files I hold"* and not *"does not exist"*.

The contract must leave it possible for such a finding still to be a finding: the defect that checker reported was
real, and what was wrong was the sentence and not the report.

### The bar

The standing bar applies: the working tree builds, warns about nothing, is formatted, and passes the tests relevant
to the change. This repository has no build, no tests and no formatter, which is a complete bar on its remaining
half and not a deficient one — so what remains is `/coding-principles`, `/naming`, and the file's own form: it
addresses the checker as *you*, states rules rather than explaining them, and its existing sections are what a new
rule joins rather than sits beside.

### The manager's audit at claim time, required by constraint 2

Read back against the two rules that bind every condition, and against constraint 1.

**[An acceptance condition is self-contained text](33-condition-is-self-contained.md).** Nothing in the demands
above requires going and reading something. The one piece of evidence the wording of repair 2 turns on — the
checker's diagnosis — is **quoted in the condition** rather than pointed at, for exactly that reason. The two skills
the bar names are discovered from the machine, which is how the bar already works everywhere.

**[A resolved node's clause cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md).**
Nothing here quantifies over the record. The two quantifications present are over the **tree** — the grep, and *no
other file is* — which that node permits, and one is over the **shipped contract's own text**, not over the graph.

**Constraint 1, *demand only what is already fixed*.** The three-rung ladder is the human's answer, taken as
offered. Repair 2's property is the checker's own words; its wording is left open, which is [Record a checker's
not-covered part on `## Review`](38-recording-a-not-covered-part.md)'s shape — state the property, refuse to choose
the form. The scope was measured with the grep above rather than chosen. **Where in the file each rule goes is not
dictated**, that being a form the worker settles.

**One reading the manager made and is naming rather than burying.** The human's answer said *every finding*, and the
contract's existing finding shape lives under `FAIL`. Reading *finding* to reach a defect handed back alongside a
`PASS` is the manager's reading of their word. It is the broader one, and node 74's checker is why: the enumeration
that proved this idea worth shipping arrived **outside a `FAIL`**, alongside a `PASS`. Narrowing to `FAIL` entries
would exclude the case that made the argument.

**What the audit does not cover.** Whether the contract can carry both repairs without growing a section for them is
the worker's problem and not settled here.

## Where it came from

Reported by node 59's checker in its retrospective under the human's standing instruction, in answer to a question
the manager put to it: *is there something a checker could hand back that turns a finding into the sweep, rather
than into three repairs?* It is the fourth return-shape defect found at the same place, after the two [What the
checker contract owes to having been run](31-checker-contract-owes.md) fixed and the one now at [The checker has no
form for two clauses of one condition that cannot both hold](66-two-clauses-that-cannot-both-hold.md).

## Answer

**A checker's finding now carries three things, and a blind checker's claims are bounded to what it holds.** Landed
in `.claude/skills/expedition-checker/SKILL.md` as commit `0d49586`.

**`finding` became a word used exactly**, which the work discovered rather than the condition demanding it: the
contract used the word three times — in hard rule 2, in the reviewing-skill limits, and in the reflow rule — and
defined it nowhere. The new entry fixes the breadth at the one place a reader meets the word: *"a defect in the work
that you report, by either route this contract gives you: an entry under a `FAIL`, or something handed back
alongside an outcome."* Defining it once is what let both new sections state rules without restating what a finding
is.

**`### What every finding carries`** and **`### What you can establish, and what you cannot`** sit at the head of
`## What you hand back`, before `### PASS`, so they govern every route an outcome travels rather than sitting inside
one. The extent is *"exactly one of these, and a finding carrying none of them is malformed"*, with the enumerator,
the bounding set and the explicit no-extent statement as its three rungs. `### FAIL`'s old line — *"one entry per
failure: what is wrong, where, and what you ran or read to find it"* — became *"one entry per failure, in the shape
every finding takes above"*, that sentence having been word for word the instances rung.

**Repair 2 is worded as a permission and a limit rather than as a ban**, which was the worker's call and not the
condition's: *"You can establish that something is absent from what you hold. You cannot establish that it is absent
from the effort"*, then *"word each finding to the search that produced it"*. Its reason, recorded because it
generalises: a ban on the phrase *"does not exist"* would put that phrase in front of the checker as the thing to
think about. It closes with the part the condition insisted on keeping possible — *"The bound is on the sentence and
not on the report"*.

**The mechanism was exercised by its own checker one node after landing.** Run 1's finding arrived in the shape this
node had just created, with an enumerator that proved its own extent exhaustive, and it caught a defect in the work
that created it. That is recorded under `## Review`.

## Review

### Run 1 — `FAIL: the bar`

**The acceptance condition met in full**, established part by part: the scope and its extent grep, both numbered
demands, and the *reported and not edited* clause, under which nothing was owed — the checker searched the shipped
tree and found two near-misses, `graph-conventions.md`'s `## Review` (a *run's* record entry, not finding shape) and
`CONTEXT.md`'s **Checker** entry (outcome names, not finding shape). It also established that nothing was hidden by
rewrapping, unwrapping both sides into paragraphs and confirming exactly three changes with no paragraph moved.

**One failure, on the bar.** A glossary headword used in a sense the glossary does not give it: the new text closed
with *"turns three repairs into a sweep"*, where `CONTEXT.md` defines **Sweep** as an effort-level pass looking for
revisions nobody propagated. The manager verified it independently — `sweep` appears twice in the shipped tree
outside the glossary, and the other use, in `graph-conventions.md`, is the glossary sense.

**The finding arrived in the shape this node had just created**, one node after it landed and on the work that
created it. Instances, the form as a predicate — *"a shipped file uses a term `CONTEXT.md` defines as a headword to
name a concept other than the one defined"* — and an **enumerator** over every `CONTEXT.md` headword against the
added text, returning two hits of which one was correct usage, which is what makes the extent exhaustive rather than
asserted. The checker then ran the same enumerator over the 110 `_Avoid_` words and dispositioned all five hits,
dropping bare-noun `report` as the `_Avoid_`-word false-positive class the review route warns about, on the ground
that an `_Avoid_` line refuses a word *for one concept* and this was not that concept.

**Run 1 stopped once on a session limit and was resumed rather than respawned**, having already read the diff. It
reported that its read of the binding contract came back truncated; the resume gave it a route around that and
carried no account of anything else.

**`NOT COVERED:` nothing.** The outcome covers the whole condition.

### The question run 1 handed back, and its disposition

The checker routed one observation as a question rather than a finding, correctly: the wording is the acceptance
condition's own and so was not the worker's to depart from. Its words:

```
- The contract now names a fourth actor, "the implementer", under `### What every finding carries`:
  "over the part of the work the implementer may edit" and "text the implementer may not touch".
  CONTEXT.md's actors are Manager, Worker and Checker, and this file already names that actor in
  Hard rule 5 as "the worker holding the code". The wording is the acceptance condition's own,
  quoted almost verbatim, so it was not the worker's to depart from — which is why this is a
  question and not a finding. Either the glossary gains the word or a later condition uses the
  existing one; the human may want to say which.
```

**The manager corrected its premise before relaying it.** *"A fourth actor"* overstates what is there: `CONTEXT.md`
already uses the word in its own prose, in the **Checker** entry — *"Started by the manager and never by the
implementer"* — so `implementer` is not new to the shipped corpus and names no new party. What is true is narrower:
the word is used and is not a headword. This is the second time a checker has asserted more than its bounded search
supports, and it is the defect this very node exists to fix — the fix binds findings, and this arrived as a
question.

**The human's word**, `verbatim`: *"ok"*, on the manager's recommendation that it be left rather than settled now,
and picked up by [Ship the glossary inside the skill directory and make it state its own
completeness](56-ship-the-glossary-into-the-skill-set.md), which is already moving that file. Recorded there too.

### Correction round 1

**The human's words:** none. The round was opened by the manager on run 1's `FAIL: the bar` without going to the
human, the finding being on the bar rather than on the condition and therefore the build's to fix.

**What the worker changed.** One clause, the close of `### What every finding carries`: *"and it is what turns three
repairs into a sweep"* became *"and it is what lets the implementer repair every instance rather than only the ones
you listed"*. It did not dispute the finding.

**It declined the checker's suggested wording**, which the checker did not require, and the reason is worth keeping:
the suggestion — *"one pass over every instance"* — uses `pass`, the noun `CONTEXT.md` uses to define both **Sweep**
and **Cascade**, so it trades one borrowed term for a fainter echo of the same two. The replacement is built from
the section's own vocabulary instead.

**The worker re-ran the finding's own enumerator rather than checking the one instance**, on the ground that one
instance is not a class: 50 headwords against the 36 added lines, one hit remaining — `effort`, in its glossary
sense. The manager rebuilt and re-ran it independently and got the same result, and confirmed `sweep` returns zero
in the file.

**No second check was run.** The manager judged a full re-check disproportionate to a one-clause change in text the
checker had already established, verified the fix mechanically instead, and **said so in the gate payload rather
than leaving it to be inferred**. The human approved on that basis.

### Gate: `approve`

**The human's word**, `verbatim`: *"approve"*.

**Flags: none.** This node minted none, and the worker returned `FLAGS: none` on both rounds, so the approval
settles nothing — recorded explicitly because the standing rule is that approving a node's end settles its flags,
and a payload that omits one settles it silently.

**Landed** as `0d49586`, one path-limited commit of `.claude/skills/expedition-checker/SKILL.md`. The rebase onto
`master` was a no-op, `master` not having moved since the worktree was cut; the bar's command half had nothing to
run; the merge was `--ff-only`; the worktree was removed and branch `node-71` deleted. **Two steps of that lifecycle
had to run with the manager's sandbox disabled**, on the human's word — recorded on [Run an implementation node's
work in a worktree](68-implementation-in-a-worktree.md) rather than here, being a property of the lifecycle and not
of this node.

## Interview

### Attempt 1 — the manager's raise, and the human's answer

The node had no acceptance condition and could not get one until its open question was settled, so the **manager**
put it to the human rather than a worker. Pasted as it was sent, `ASK` and `RECOMMENDED` only; the full block also
carried `ABOUT`, `SO FAR` and `ALTERNATIVES`.

```
ASK:           Must every finding carry an extent, or only those where an enumerator exists?

RECOMMENDED:   Neither as posed — make the *answer* mandatory and let its form vary. Every finding
               carries an extent statement, which is exactly one of three:
                 - an enumerator: the command that lists the form's candidates in the editable work;
                 - a bounding set, where no command fits: the smallest set that provably contains every
                   instance — on node 59 that was "the 48 authored lines", got by set-difference;
                 - an explicit "no extent; these instances are not exhaustive."
               A finding carrying none of the three is malformed.
               This is not my invention — it is what the checker itself proposed; the node's binary is
               narrower than its own source. What it rests on: mandatory-as-a-command forces a checker
               to fabricate enumerators for prose findings, which the checker says do not have them,
               and prose is precisely the class where the worker found four more by hand.
               Owed-where-it-exists is honest but unverifiable — nothing distinguishes "no enumerator
               exists" from "I did not build one". The third rung closes that: it is a positive
               statement the checker has to make, so silence becomes malformed rather than permitted.

ALTERNATIVES:  - Mandatory as a command. Simplest to check, and buys that by making checkers invent
                 enumerators they have said do not exist for the class that needs the sweep most.
               - Owed where it exists, as the node poses it. Honest, and gives a checker a way out
                 that nothing verifies.
               - Leave it out of the contract entirely — the status quo, where a checker supplies the
                 extent on its own initiative. It did so on node 74 and enumerated the defect
                 completely; that is also what produced this node, since nothing made it happen.
```

**A1, from the human**, `verbatim`: *"ok for recommended"*.

The option it points at, quoted from `RECOMMENDED` above: *"make the **answer** mandatory and let its form vary"*,
with the three rungs — an enumerator, a bounding set, or an explicit statement that the finding has no extent — and
*"a finding carrying none of the three is malformed."*

**No divergence.** The reply takes the recommendation as offered and names no alternative, so nothing here is
`paraphrase` and there is nothing for the manager to ask about. Recorded under [What is recorded when the human
takes an option as offered](25-recording-an-option-taken.md).

**Attribution, since the manager is the party that wrote the recommendation.** The three rungs are not the manager's
invention and the raise said so: they are node 59's checker's, from the retrospective quoted at `## Question` above.
What the manager contributed was noticing that the node's binary was narrower than the source it was drawn from.

## Retrospective

*Filed by the manager, as the worker wrote it. **The worker handed it back as text rather than writing it here**,
on the ground that the implementation contract's hard rule 1 — "You write product code. You write no graph file" —
keeps it out of every graph file. That is the right reading and the spawn was wrong to ask for the other one; see
the manager's note below.*

**What I had to hunt for.** Almost nothing, and that is the finding. The one thing I went looking for was whether
any file other than the target states finding shape — the condition asks for that to be reported. I looked first
where the condition pointed (its own grep), then widened to `.claude/skills/expedition/` because
`graph-conventions.md` is the other document a checker's output touches. Its `## Review` section came close enough
to need reading before I could say it was not a statement of finding shape. That was the only real search of the
node.

**What I read and did not use.** `CONTEXT.md` in full — 50 entries, of which four bore on the work (`Checker`,
`Acceptance condition`, `The bar`, `Handover`); the `_Avoid_` lines mattered as a check, but reading all 286 lines
to use four entries is the cost. `map.md` in full: the ground rules and the four standing rules for writing were
live, and the landing policy, the dogfood target, the fog and the out-of-scope section were not — the spawn had
already quoted me the parts I needed, so the map was largely re-reading what I already held. The node file's
`## Interview` and the manager's audit were confirmation rather than input, since the condition is self-contained by
construction and said so.

**What would have made this easier.** The spawn quoted the acceptance condition, the bar, the ground rules and the
four writing rules in full — which meant `map.md` and the node file were both redundant with it for everything
except the two things I actually used them for. That redundancy is the largest single cost of this node, and it is
a *duplication* rather than a shortfall: the spawn was complete, so the two files it told me to read cold added the
map's history and the node's provenance and nothing operative. A worker on a node whose condition is genuinely
self-contained could be told which of the standing reads the spawn has already superseded.

**Stale, wrong, or contradictory.** One contradiction, and it is between the spawn and the contract rather than
inside either. The spawn says *"file a `## Retrospective` annotation on the node file"*; the contract's hard rule 1
says *"You write product code. You write no graph file"*, and the spawn separately says the node file in the main
repo carries the manager's bookkeeping and is not mine. I resolved it by handing the retrospective back as text.
`map.md`'s own sentence has the same ambiguity — *"It files as a `## Retrospective` annotation on the node"* leaves
the subject open, and the worker is the wrong reading under hard rule 1. One other, smaller: `CONTEXT.md`'s
`Code slot` entry still says occupancy *"is discovered from the working tree"*, which `map.md` has since superseded
with *"discovered by counting the live worktrees"* at node 68. Not mine to edit, and it did not affect this work.

### The manager's note on the contradiction the worker found

*Not part of the retrospective.* **The worker is right and the defect is the manager's.** `map.md`'s sentence
*"It files as a `## Retrospective` annotation on the node"* leaves its subject open, the spawn read it as the
worker's act, and hard rule 1 forbids exactly that. Practice has always been the other reading — node 59's
retrospective, the first under the standing instruction, is headed *"filed as the worker wrote it"*, which is the
manager pasting. **Every retrospective spawn before this one carried the same wrong instruction**, and no worker
reported it.

Two things done about it, neither of them here: the map's sentence is made to name its subject, and the case is
recorded as evidence on [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md), whose clause 5 turns on whether *"the manager is the graph's only
writer, and it writes as a scribe"* still holds. **This is a live instance of it holding**: the worker returned
text and the manager wrote it.

The worker's second observation — `CONTEXT.md`'s `Code slot` entry — is already the work of [Bring the glossary's
code-slot and reject entries up to the worktree lifecycle](81-glossary-code-slot-and-reject.md), which is open and
whose condition names that entry.

## Annotation: this node's own recorded enumerator returns two paths, not one, and its domain reaches the record

*Filed by the manager from [Whether the checker re-runs a condition's own
enumerator](110-does-the-checker-rerun-the-enumerator.md)'s worker, which ran the command as written. The manager
re-ran it and confirms. **This node is resolved and its condition is discharged**, so under [node
94](94-condition-scope-as-a-predicate.md) nothing here is repaired — it is recorded because this node is the exemplar
the whole extent rule was modelled on.*

Node 94 called this *"the only one on the record that never overflowed"*. Run verbatim,
`grep -rln "one entry per failure" --include="*.md" .` returns **two** paths: `.claude/skills/expedition-checker/SKILL.md`,
and **this node's own file** — because the condition quotes the phrase, so **the condition became a hit on its own
enumerator**. Node 110's worker confirmed by git that this node file was committed the day before the work landed, so
it was already true when this node's checker ran. This node's `## Review` records that the checker *"established the
scope and its extent grep"*; either the command was not run or the difference was absorbed without being said.

**And a second thing, which bears on what [node 109](109-carry-the-extent-rule-into-the-shipped-files.md) ships.**
This enumerator globs `.`, so a checker running it as written **reads into `.scratch/` — the record it is blind to by
design.** Node 94's flag `94.2` already bars that domain for a condition's enumerator; nothing enforces it, and the
exemplar breaks it.

## Annotation: this node's recorded return was already false when its own checker recorded establishing it

*Filed by the manager from [Whether the checker re-runs a condition's own
enumerator](110-does-the-checker-rerun-the-enumerator.md)'s `INVALIDATIONS`, in that node's own words. It supersedes
nothing above — this node's condition is discharged and out of reach under [node
94](94-condition-scope-as-a-predicate.md)'s reach-back rule, so this records the fact rather than repairing it. It
sits beside the earlier annotation on the same enumerator rather than replacing it.*

> One factual claim on it is false, and the node's decision is untouched. Its `## Acceptance condition` records that
> `grep -rln "one entry per failure" --include="*.md" .` *"over the repository returns that path and nothing else"*.
> It returns two paths: the shipped contract, and node 71's own node file, which matches because the condition quotes
> the phrase it searches for. Git confirms the node file was committed before the work landed, so the claim was
> already false when that node's `## Review` recorded that the checker *"established the scope and its extent grep"*.
> Two consequences, neither reaching the node's answer: the condition is **discharged and out of reach** under node
> 94's reach-back rule, so this is an annotation and not a repair; and the enumerator's domain is `.`, which includes
> the effort's record, so **the exemplar node 94 modelled its rule on breaks flag `94.2`'s domain limit**. The three
> repairs that node landed in the checker contract stand exactly as they are.

**And what node 110 built on it**, since this node is where a later reader will come looking: part 3 of node 110's
answer — *an enumerator whose domain reaches the effort's record is reported as a defect in the condition* — exists
because of this instance. A record-reaching domain is invisible until somebody runs the command and reports where it
went.
