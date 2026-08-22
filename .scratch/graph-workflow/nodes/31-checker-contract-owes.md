# What the checker contract owes to having been run

Type: implementation
Status: resolved

## Question

`expedition-checker/SKILL.md` was written by the manager at [Write the worker contract
skills](22-worker-contract-skills.md) and had never been run by the agent it was written for. It has now been
run four times on one node, and it did **three things its own text does not describe** — each of them right,
and each invisible to the next checker, which gets the file and not the transcript.

Created at [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md)'s
gate, from the human's question on reading the gate payload: *"do you also want to do something also with the
'What the checker did that I'd want kept'"*. The manager had recorded all three on that node as things worth
keeping and had stopped there, which is a record of admiration rather than a change to anything.

### The three

**1. How to check work that edited the checker's own standard.** The bar for this repo includes
[`CONTEXT.md`](../../../CONTEXT.md)'s `_Avoid_` lines, and the work edited one of them — so the standard moved
under the check. Handed a framing and explicit permission to raise, the checker used neither and found the
right thing to measure instead: **a standard has operative content and a rationale.** It counted the forty
`_Avoid_` lines before and after, found one differing line, and compared the *refused set* — `{escalate,
interrupt, ask}` — which was identical. Only the appositive after `ask` had moved. Then it named its own raise
condition:

> What would have changed that: had the edit added or removed a refused word, the operative standard itself
> would have moved and I would have had nothing unmoved to check the rest of the work against — that I would
> have raised rather than resolved.

The next round moved the same clause again, and it applied its own test rather than inheriting its own
conclusion. **Moving a rationale leaves a check intact; moving operative content destroys it.** Nothing in the
contract says this and the contract is what the next checker gets.

**2. What to do when the defect is in the acceptance condition and the work complies with it.** The contract
has two routes for a bad condition and neither fits: `raise` is for a condition that *cannot be checked* —
incoherent, unmeasurable, unobservable — and *"a condition you can check but disagree with is not a raise.
Check it as written."* This condition was checkable, the work complied, **and complying produced a
contradiction between two entries of the shipped glossary.** Failing the work would have been wrong; saying
nothing would have shipped the defect. It did neither: it handed the observation back as a **question**
alongside its `PASS`, noting that the wording was the condition's own and so not the worker's to depart from.
The human took it, the condition was amended, and a real defect in the authoritative file was caught.

That is a third route and the contract sanctions the channel only for something else — *"where a skill you ran
wants to ask the human something."* Whether it is a use of `QUESTIONS:` or a fourth return shape is the one
genuinely open call in this node.

**3. What "the statement of what changed is not evidence" costs when the work was reflowed.** The contract
says comparing modification times against the last outcome *"is enough to find them."* It is not, once a file
is rewrapped: a reflow moves every line of a paragraph. The checker reconstructed the previous version of the
entry from the diff it had read the round before, unwrapped both, and word-diffed them — establishing that the
whole change was one inserted phrase. It also **unwrapped before grepping** to confirm shared wording, noting
that a line-based grep misses a phrase that wraps.

### A fourth, added in place by [Whether a spawn may override a shipped worker
contract](28-spawn-overriding-a-contract.md)

**4. What to do when the acceptance condition itself moves while the check is live.** On that same node,
condition 7 was **amended twice mid-node** and the manager said so in each resume. The contract's *"When you
are handed the same work again"* section is written for a changed **work** against a fixed condition — the
whole design says a condition is written before work starts and is not the worker's to rewrite — so nothing
in it covers this. The checker handled it correctly with no instruction: it re-checked against the amended
text and did not treat its own earlier conclusion as inherited.

Node 28 ruled this **not a departure from the contract but an uncovered case**, which is why it lands here
rather than being licensed. It meets this node's own criterion exactly — real, handled right without
instruction, and invisible to the next checker, which gets the file and not the transcript.

Added in place because this node was unstarted, per [Revision semantics](06-revision-semantics.md).

### A fifth and a sixth, added in place by [An acceptance condition is self-contained
text](33-condition-is-self-contained.md)

**5. The raise for a bad condition does not name the case node 33 routes to it.** The contract opens that
raise for a condition *"incoherent, self-contradicting, unmeasurable, or naming something that cannot be
observed"*. A condition whose **demand is held in material the checker was not given** is none of those on
its face: the thing named can be observed perfectly well, by somebody else. Node 33 shipped the rule that
sends exactly such a condition here — *"raised by the manager where it meets one before the check, or by the
checker on a condition it cannot check"* — so the list now owes it a clause.

What happened instead, for the fourth time: handed node 33's condition 6, whose deliverable lands in a node's
`## Answer` that no checker is given, the checker **neither passed nor failed nor raised it**. It returned
`PASS` and recorded that one clause was outside what it could establish, in its own words:

> Reading it as "in the file" would be checking against my own repair of the condition, which my contract
> forbids. **The manager holds that handover and is the only party that can verify the audit was reported; my
> `PASS` does not cover it.**

That is item 2's third route again, arriving unprompted on a different trigger — and it is now the shape this
node has seen most often. Whether the two cases want one return shape or two is this node's to say.

**6. A blind checker that invokes a reviewing skill loses its blindfold to the sub-agents that skill
spawns.** The contract tells the checker to run a reviewing skill for code standards. Node 33's checker found
one on the machine and **declined to invoke it**, giving the reason:

> because it runs its axes in spawned sub-agents that would be handed none of that and would go looking,
> including into the record

It applied that skill's standards axis by hand instead, and left its spec axis unrun on the ground that the
axis holds work against an originating document — which here is the node file the checker may not read.
Nothing in the contract says any of this. The blindfold is a property of what the checker is *given*, and
delegation hands a fresh agent a fresh set of givens; the contract treats *"invoke a reviewing skill"* as
free.

**A second checker met the same case and answered it differently, and both answers are right.** Added in
place by [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md). That node's checker found the same
reviewing skill and **invoked its standards axis anyway — with the standards and the smell baseline pasted
into the sub-agent**, so the delegate was handed givens rather than sent looking. It left the same spec
axis unrun, on the same ground and adding one detail the first did not: *its search order points into
`.scratch/`*, which is the record, so the axis would have walked there before reading anything.

So the uncovered case has two correct discharges — **decline to invoke**, and **invoke with the givens
supplied** — and the contract names neither. The second is strictly more useful, since it gets the axis run;
the first is safer where a skill's internals cannot be constrained. That is the distinction condition 8
below has to make, and it is why the honest answer may be a duty to *judge and report* rather than a
prohibition.

### The audit this node's own warning asked for, run before the work was claimed

The warning at the foot of the condition below says it is manager-written and to read it against the files
before trusting it. That was done at claim time by the manager, applying [An acceptance condition is
self-contained text](33-condition-is-self-contained.md)'s rule and [The clause that says no resolved node
changes cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md)'s to the manager's
own text — which is the repair the map records as the one that worked, node 36's condition having been the
first manager-written one in this effort established in full. Six findings, all repaired in place below.

1. **Condition 4 contradicted itself outright.** It listed `CONTEXT.md` among the files that do not change
   and then, one paragraph later, permitted `CONTEXT.md` to be edited where a term genuinely moves. A
   checker reading the condition cold has *self-contradicting* as a stated ground for a raise, so this would
   have cost a raise rather than a check. The struck original — *"`CONTEXT.md` is touched only if a term
   genuinely moves"* — was coherent; last session's replacement broke it while fixing something else.
2. **Its file list read as covering the work file.** The glob `expedition-<type>/SKILL.md` includes
   `expedition-checker/SKILL.md`, the one file this node exists to change. The five are now named.
3. **Condition 1 named a test whose content was only on this node.** *"The
   operative-content-versus-rationale test"* is a label; the substance is in case 1 above, which the checker
   never reads. Copied in.
4. **Three conditions carried instructions addressed to the worker rather than demands on a file.**
   *Raise rather than deciding it* in condition 2, *say so and write the reporting duty alone* in condition
   8, and the `NEW NODES` half of condition 4. A checker cannot establish whether a worker should have
   raised, and this is the exact shape node 36 proved avoidable: every demand lands in a file, and what is
   owed by another party is owed on the handover. They are moved to this section, below, verbatim — the
   worker reads the whole node, so nothing is lost by holding them here, and the conditions now permit
   either outcome and demand only that the file carry it.
5. **Condition 8 did not reach a requirement its own case states.** Case 6 says the two correct discharges
   are *"the distinction condition 8 below has to make"*, and the condition demanded a prohibition or a
   reporting duty without demanding that both discharges be named. That is flag `26.7`'s cost exactly — a
   described case with no condition covering it — arriving in the condition added to answer it.
6. **The provenance parentheticals on conditions 6, 7 and 8 point at material the checker is not given.**
   They name nodes 28, 33 and 36 and flag `26.7`. They are not demands, so they do not fail node 33's rule,
   but they are noise in the blind checker's only input and one of them instructs a party that is not
   reading. Moved here verbatim, beside the cases they belong to.

**What moved, verbatim, so the condition holds only demands on files.**

- From condition 2: *"**If the honest answer is a fourth return shape rather than a use of `QUESTIONS:`,
  raise it** rather than deciding it: the three return shapes are [Human review of landed
  code](20-human-code-review.md)'s and [Write the worker contract skills](22-worker-contract-skills.md)'s,
  not this node's."*
- From condition 4: *"so a term moving here is a report to the human and a `NEW NODES` entry"* — the report
  and the node are owed on the handover, where `NEW NODES` already lives.
- From condition 6: *"(Added with the fourth case above, by [Whether a spawn may override a shipped worker
  contract](28-spawn-overriding-a-contract.md). **Manager-written**, and so subject to the same warning as
  the rest of this condition — read it against the file before trusting it. Added rather than left to the
  `## Question` alone because flag `26.7` records what a described case with no condition covering it
  costs: one product file in scope and no condition reaching it.)"*
- From condition 7: *"(Added with the fifth case above, by [An acceptance condition is self-contained
  text](33-condition-is-self-contained.md). **Manager-written**, and subject to the same warning as the rest
  of this condition.)"*
- From condition 8: *"(Added with the sixth case above, by the same node, and **manager-written**. If the
  honest answer is that no contract can constrain a third-party skill's internals, say so and write the
  reporting duty alone.)"*

**Standing instructions to whoever works this node**, gathered from what moved and binding on the worker
rather than on the checker:

- **Where the honest answer to condition 2 is a fourth return shape rather than a use of `QUESTIONS:`,
  raise it rather than deciding it.** The three return shapes are [Human review of landed
  code](20-human-code-review.md)'s and [Write the worker contract skills](22-worker-contract-skills.md)'s,
  not this node's, and a fourth reaches the manager's own skill and the recording rules as well as this
  file. Same for condition 7, which routes a second case to whatever condition 2 settles.
- **Where the honest answer to condition 8 is that no contract can constrain a third-party skill's
  internals**, that is not a raise: write the reporting duty alone, and say in the handover that the
  prohibition was judged unwritable and why.
- **Where a term genuinely has to move in `CONTEXT.md`**, report it and mint the `NEW NODES` entry. Never
  sweep the other files from inside this node.
- Conditions 6, 7 and 8 are **manager-written**, as the warning at the foot of the condition says of the
  whole of it. The audit above is one reading; it is not a guarantee. Read them against the file, and raise
  what does not survive that reading.

## Acceptance condition

1. `expedition-checker/SKILL.md` states the operative-content-versus-rationale test for a standard the work
   itself moved, and the condition under which the checker raises instead of resolving: an added or removed
   refused element leaves nothing unmoved to check against. In the contract's own voice, general over
   standards rather than written about `_Avoid_` lines, since the next repo's bar will not have them.

   **The test itself, copied in** rather than named. A standard has **operative content** and a
   **rationale**, and a check survives one of them moving but not the other: *moving a rationale leaves a
   check intact; moving operative content destroys it*, because there is then nothing unmoved left to hold
   the rest of the work against. The file must carry that distinction and that consequence, in whatever
   words it chooses.
2. It states the route for a condition that is checkable and complied with, where compliance is what produces
   the defect — distinguished from the existing raise, which is for a condition that cannot be checked at all,
   and from *"a condition you can check but disagree with"*, which stays out of scope. ~~**If the honest answer
   is a fourth return shape rather than a use of `QUESTIONS:`, raise it** rather than deciding it: the three
   return shapes are [Human review of landed code](20-human-code-review.md)'s and [Write the worker contract
   skills](22-worker-contract-skills.md)'s, not this node's.~~ **Moved to the audit above**, that clause
   instructing the worker rather than demanding anything of a file. **Either shape satisfies this** — a use
   of `QUESTIONS:`, or a return shape of its own — and what the file owes is that a checker reading the
   contract cold can tell which one it has been given and when to use it.
3. Its *"When you are handed the same work again"* section no longer claims modification times are **enough**
   to find unmentioned changes, and says what to do about a reflow: reconstruct and compare content, not
   lines. Unwrapping before searching is stated wherever the contract tells the checker to search.
4. ~~No other contract changes, and no decision on any resolved node changes. `CONTEXT.md` is touched only if a
   term genuinely moves, and if it is, the [glossary-does-not-travel problem](29-shipped-file-consistency.md)
   applies and is reported rather than solved here.~~

   **Replaced in place**, by [The clause that says no resolved node changes cannot be
   self-contained](36-resolved-node-clause-cannot-be-self-contained.md) at its gate. That node's audit found
   this clause failing the self-containment rule **twice** — once on *"no decision on any resolved node
   changes"*, which node 36 has now ruled out of every acceptance condition because no copy can repair a
   demand that quantifies over the record; once on *"the glossary-does-not-travel problem"*, whose content
   sits only in node 29 and which node 33's rule says to **copy in**. Both repairs are below, and this node
   being open and unstarted, they are made here rather than by a node of their own — the worker that
   reported them said the call was the manager's.

   **No other contract file changes.** `expedition-checker/SKILL.md` is the only one this node's work
   touches; ~~the five `.claude/skills/expedition-<type>/SKILL.md` worker contracts and `CONTEXT.md` stay as
   they are~~ **the five worker contracts — `.claude/skills/expedition-grilling/SKILL.md`,
   `expedition-implementation`, `expedition-precondition`, `expedition-prototype` and `expedition-research` —
   stay exactly as they are.** Struck and rewritten at the audit above, on two counts: the old wording put
   `CONTEXT.md` among the files that do not change while the paragraph below it permits `CONTEXT.md` to be
   edited, which is a flat contradiction and a stated ground for a raise; and the glob `expedition-<type>`
   reads as covering `expedition-checker` too, which is the one file this node exists to change.

   **Where a term does genuinely have to move, `CONTEXT.md` is edited and the move is reported rather than
   propagated.** The reason, copied in rather than pointed at: **nothing checks the shipped files against
   the glossary.** A decision that changes a word leaves every other shipped file still carrying the old
   one, and no mechanical check and no agent's contract looks for it — so a term moving here is ~~a report to
   the human and a `NEW NODES` entry,~~ **never a sweep of the other files from inside this node.** The
   report and the new node are owed on the **handover**, where `NEW NODES` already lives; they are moved to
   the audit above for the same reason node 36 moved the record-wide demand there — a checker never sees a
   handover.

   The record-wide demand that used to sit here is now owed on the handover instead, where every worker
   returns `INVALIDATIONS` — which resolved node its work contradicts, and how. Nothing about it is this
   condition's business.
5. The bar as [map.md](../map.md) records it for this repo: no build, no tests, no formatter, so the project
   criteria, this map's standing preferences, `CONTEXT.md`'s `_Avoid_` lines, and these conditions are the
   whole of it.

6. Its *"When you are handed the same work again"* section says what the checker does when **the acceptance
   condition** has changed since its last outcome, distinguished from a changed work: re-check against the
   amended text, and do not inherit a conclusion reached against the old wording. *(Provenance moved to the
   audit above.)*

7. Its raise for a bad condition covers a condition the checker cannot check **because what the condition
   demands is held in material the checker was not given** — distinguished from the four grounds already
   listed, none of which fit: such a demand is neither incoherent nor self-contradicting nor unmeasurable,
   and what it names is observable by a party that has the material. Where the answer to condition 2 is a
   fourth return shape, this case uses it too, or the contract says why the two differ. *(Provenance moved
   to the audit above.)*

8. It states that a reviewing skill run under this contract must not delegate the check to agents that would
   not be handed the checker's own givens — or, where the contract cannot bind what a skill does internally,
   it says that the checker judges this itself before invoking one and reports which axes it ran and which it
   left. The blindfold is a property of what the checker is given, and the current text treats invoking a
   reviewing skill as free. *(Provenance and the worker instruction moved to the audit above.)*

   **And it names both ways of discharging this, distinguishing them.** Two are known to be correct:
   **declining to invoke** a reviewing skill whose delegates cannot be handed the checker's givens, and
   **invoking it with those givens supplied to the delegate** — the standards and any baseline pasted in, so
   the delegate is handed material rather than sent looking. The file says which is preferred and on what
   ground, the second getting the axis actually run and the first being the safe answer where a skill's
   internals cannot be constrained. A contract that permits only one of the two is not enough here.

**One warning to whoever spawns this**, learned the hard way on node 26: **that node's acceptance condition
was the first written by the manager rather than by a spawning node or its worker, and it had to be amended
twice** — once for naming a glossary entry that does not exist, once for a clause true only of implementation
nodes. This condition is also manager-written. Read it against the files before trusting it.

**Acted on**, at claim time, by the audit recorded at the end of the `## Question` above — six findings, one
of them a flat self-contradiction that would have cost a raise instead of a check. The warning stays: the
audit is one reading of the condition and not a guarantee of it.

## Answer

`expedition-checker/SKILL.md` now carries all six things the file had been doing right without
saying, and one section split so the new material lands where it belongs. The file grew from 171 to
306 lines; nothing else changed.

**The operative-content test, and the raise it opens.** A new `### Where the work moved one of
them` under the standards section splits any standard into its **operative content** — what it
requires or refuses — and its **rationale**, the wording that says why, and states the consequence:
moving a rationale leaves the check intact, moving operative content destroys it, because there is
then nothing unmoved left to hold the rest of the work against. The method is stated as a set
comparison element by element on either side of the change, prose around it ignored, with
unwrapping first because a standard rewritten in place is usually rewrapped too. Identical sets:
the standard stands, it does not matter which side you read it from, and the checker says it
settled that first. An element added, removed or altered: raise. Written over standards generally,
never over `_Avoid_` lines.

**A condition that is met and wrong anyway is a question, not a fourth return shape.** The call
this node reserved to itself, and the reason: what the checker improvised is a `PASS` with something
attached, not a fourth outcome. Widening `QUESTIONS:` keeps the return shapes at three, keeps the
outcome vocabulary `PASS`/`FAIL`, and keeps `graph-conventions.md`'s three `## Review` entry kinds
valid — a genuine fourth outcome would have needed a fourth entry kind, which is what the standing
instruction's raise protects. So `QUESTIONS:` now carries two triggers under one route: a skill's
question, and a condition the checker can check, that the work complies with, where complying is
itself what produced the defect. It says to hand the observation back and to say the wording was
the condition's own and so not the worker's to depart from, and it repeats the carve-out both ways
— a condition you can check and merely disagree with you check as written and say nothing.

**Two riders, not one, and the difference is what the outcome covers.** The other reserved call.
`### A part you could not establish` adds a `NOT COVERED:` block beside `QUESTIONS:`, in the same
structural slot, for a condition that demands something observable by somebody else — a thing that
lands in the record, something an agent handed back, anything outside the paths the checker was
given. Merging the two would have been cheaper and would have hidden the only difference the
manager acts on, so the file states it: a question leaves the outcome covering the whole condition,
and a not-covered part narrows what it covers. The block says the `PASS` then means the parts
established and no more, and that the manager needs to know it is still holding the rest. Neither
rider is a return shape; the file's own sentence already separates outcomes from what rides
alongside them, and that sentence was extended rather than replaced.

**The fifth raise ground, and where its boundary with the rider runs.** The raise section names it
and distinguishes it from the four: a demand held in material the checker was not given is not
incoherent, not self-contradicting, not unmeasurable, and what it names is observable perfectly
well by whoever holds the material. Raise where it reaches the whole condition and leaves nothing
establishable; hand the part back as not covered where it is confined and the rest stands. That
boundary is the same test as the operative-content one — is there anything unmoved left to hold the
work against — which is why the section is retitled `### raise — nothing left to check against` and
now holds two grounds: a broken condition, and a standard the work moved. Retitling was necessary:
the moved-standard raise is about the bar, not the condition, and the old title excluded it.

**A routing table before the three shapes**, so a checker reading cold can tell which one it has:
five rows over disagree-but-checkable, met-and-wrong-anyway, one part unestablishable,
uncheckable-at-all, and a moved standard.

**The delegation duty, and the prohibition judged writable.** `### What a skill delegates is not
blind` states that blindness is a property of what the checker was *given*, that a spawned agent
starts with none of it and will go looking — into the record first, where its own search order
points there — and that this contract cannot reach inside a skill to change what it spawns. So the
prohibition is written against the checker's own invocation instead of against the skill's
internals, which is what makes it writable: *let no part of a reviewing skill run in an agent that
would be handed less than you were.* Both known discharges are named — invoke with the givens
supplied, or decline to invoke — with the preference stated and grounded: prefer supplying the
givens because it gets the part actually run; decline where what the agent would receive cannot be
seen or constrained. The judge-and-say duty is written too, not instead: judge before invoking
anything, and say which of a skill's parts (axes, passes, whatever it calls them) were run, which
left, and how the run ones were run.

**Modification times, and the reflow.** The re-check section no longer says comparing modification
times is *enough*: they tell you which files were touched and nothing about what moved inside one,
so they are where you start. A new bullet says a reflow moves every line and changes nothing, and
what to do — reconstruct the earlier content from the diff read last round or from the change
itself, unwrap both sides, compare the words, then say what was compared, because an inserted
phrase found that way is a finding and *the paragraph changed* is not. Unwrapping before searching
is stated once generally, before every search instruction in the file (`**A line is not a unit of
meaning**`, under *What you are given*), and again at each of the three places the contract sends
the checker searching: the standards discovery, the operative-content comparison, and the reflow.

**A condition amended mid-check.** The re-check section is split in two — where the work changed,
and where the acceptance condition changed — since it was written for the first and silent on the
second. The second says the human may amend while the check is live, that the manager says so, that
it is still not the checker's to rewrite, that the amended text is now the whole of it, and that a
part established against wording that has since moved was established against a condition that no
longer exists, so it is established again. Where the same part is amended twice, the work is held
against the text in front of the checker rather than against the conclusion reached on the wording
before it. Parts the amendment does not reach stand, and the bar is re-run either way.

**Two calls that are housekeeping.** `a worker of its own` became `an agent of its own` where the
file described a reviewing skill's delegate: the glossary's **worker** is an agent spawned to work
exactly one node, and a skill's delegate is not one. And `### Running a reviewing skill` was added,
because inserting the moved-standard subsection as an H3 would otherwise have swallowed the
reviewing-skill material into it.

**`CONTEXT.md` was not touched, and no term moved.** Checked against the three entries this work
reaches: **Checker** names *"its characteristic case"* rather than an exhaustive list of raise
grounds, so a fifth ground does not contradict it, and its outcomes stay `PASS` and `FAIL`;
**Raise** illustrates non-waiting channels rather than enumerating them, so a second rider leaves it
true; **Acceptance condition** is untouched. So the glossary-does-not-travel problem does not arise
here.

## Flags

`31.1` **· settled** `ASSUMPTION` — **The worker gave the two improvised cases two riders rather than one, and treated
neither as a fourth return shape, so the standing instruction's raise did not fire.** Its ground, in its own
words: `NOT COVERED:` sits in the same structural slot as `QUESTIONS:`, so *"the return shapes stay three,
the outcome vocabulary stays `PASS`/`FAIL`, and `## Review`'s three entry kinds stay valid"* — a genuine
fourth outcome would have needed a fourth `## Review` entry kind, which is what the raise was there to
protect. On the split rather than a merge: *"One merged rider would have been cheaper and would have hidden
the only difference the manager acts on — a question leaves the outcome covering the whole condition, a
not-covered part narrows it and leaves the manager holding the residual."* Worth the human's eye because the
node reserved this call to itself twice, in conditions 2 and 7, and the worker discharged both without
asking — correctly under its own reasoning, and the reasoning is the thing to check.

`31.2` **· settled** `ASSUMPTION` — **Filed by the manager about itself: the check ran under the contract the work had just
rewritten, and the manager proceeded rather than raising it.** The file this node edits *is* the checker's
contract, so the checker's own instructions were the post-change text — confirmed by the checker, in its
words: *"my instructions match the post-change text"*. The manager knew this before spawning, named it in the
spawn, told the checker to follow the contract as its instructions reached it and to treat the disk copy
purely as the work, and went ahead. Two reasons it may be worth revisiting. The circularity is real but
narrow: the conditions are demands on the file's **content**, which the checker read from disk, so what it
established does not depend on which text was instructing it — but *how it ran* does, and it invoked the
reviewing skill with the givens supplied, which is exactly what the new text tells it to prefer and is the
opposite of what node 33's checker did under the old. And it falsifies something the map records as a
requirement on the manager's skill — *"the harness serves the skill body it loaded and a contract edited
mid-session does not reach a worker spawned afterwards"* — which is now known to be false at least for a
contract invoked by name in a fresh subagent. Recorded on the map as well.

## Review

### Check 1 — `PASS`

The blind checker, given the four things its contract allows and nothing else: the acceptance condition as
text, the bar's non-command half as `map.md` records it, the changed paths, and the name of the work. It
established all eight conditions and **reserved nothing** — the second consecutive check in this effort with
no residual for the manager, after [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md)'s was the first.

Four things it did that are worth keeping, in the same sense the `## Question` above collects six:

**It ran this node's own new rule on this node's own check, first, before anything else.** Condition 1's
operative-content test exists because a check is impossible once the standard moves under it — and the file
under check was a worker contract, which could have been such a standard. The checker settled that question
before opening the work: `git diff --stat HEAD` over `CONTEXT.md`, the five worker contracts,
`graph-conventions.md` and `wayfinder-divergences.md` came back empty, so *"nothing I hold the work against
moved and an outcome is possible."* The rule's first live use was on itself, unprompted.

**It took the second of condition 8's two discharges and gave the reason the condition asks for.** It found
`mattpocock-skills:code-review`, read its source, and ran its Standards axis in a spawned agent **with the
givens supplied** — the whole diff, all four standards sources and the Fowler smell baseline pasted in, with
explicit instructions not to search the repo, not to read `.scratch/`, and not to look for the change's
origin. Its stated ground for supplying over declining: *"the skill's internals were readable and its search
order therefore constrainable."* It left the Spec axis unrun on two grounds, one of them new — no
requirements document exists here, **and** the skill's spec-source step points at commit issue references
as well as `.scratch/`. That is the third instance of this case in the effort and the first where the
contract told the checker what to do about it.

**It handled a false antecedent in condition 7 without repairing the condition.** That condition says *"where
the answer to condition 2 is a fourth return shape, this case uses it too"* — and the answer turned out to be
a use of `QUESTIONS:`, so the clause's premise was false and nothing further was owed. It said so rather than
inventing an obligation or failing the work.

**It discarded eight of its reviewing skill's own findings and gave a traced reason for each**, under hard
rule 2 — *a property nobody stated is not a finding*. Two are worth keeping as evidence that a documented
standard beats a general one: the unwrap rule stated in four places was discarded because condition 3 demands
exactly that and the map endorses completeness for an agent reader over brevity, and the routing table
restating rules given in prose was discarded because it is how the file discharges condition 2's *"can tell
which one it has been given"*.

Bar: nothing to invoke, confirmed by probing for `package.json`, `Makefile`, `justfile`, `Taskfile.yml`,
`flake.nix`, `Cargo.toml`, `pyproject.toml`, `.pre-commit-config.yaml`, `.editorconfig`, `.prettierrc`,
`.github/` and `.gitlab-ci.yml` — all absent, `git ls-files` markdown only. Its remaining half holds: a
word-boundary scan of all 157 added lines against the full refused set returned zero hits, altitude is
served, and the only line over 110 characters is the unchanged frontmatter description.

### Gate — `approve`

No correction rounds. The human's reply, `verbatim`:

> approve

Named as one of the three outcomes rather than left to be read, which is what [The clause that says no
resolved node changes cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md)'s
payload clause asks for and the second gate to arrive that way.

**Both flags settled by the same word.** The payload put `31.1` and `31.2` in front of the human with their
grounds inline and asked for them to be settled either way; `approve` covers the payload it answers, which
is the practice the map records — flags are settled as the node closes, eleven of eleven that way before
this. Recorded as a reading rather than as words of theirs, since neither flag was named.

## Annotation: the ground this node discarded a finding on has been replaced

*Filed by the manager, in the reporting worker's own words.* From [What the token findings change in the workflow
and its skills](53-what-token-findings-change.md), reported as a partial `INVALIDATION` **of this node's
reasoning rather than its product**:

> Its answer records discarding a checker's finding that the `unwrap` rule is stated at four sites *"because
> condition 3 demands exactly that and the map endorses completeness for an agent reader over brevity"*. Ruling 2
> above replaces that ground for shipped contracts: they keep their completeness on the fragility of
> format-bearing text, and the boundary is that prose explaining why may be compressed while shapes may not —
> under which a leading-word refactor of the four `unwrap` sites is admissible. **The discard was correct on the
> record as it stood and node 31 is not reopened for having made it; what no longer holds is the reason given.**

**Why it was reported here rather than folded into a node**, in the same worker's words: *"the human's ruling 1
says the two discards already made stay discarded, and whether that reaches this one is theirs to read rather
than a worker's to assume."* It is flagged as `53.5` and the refactor node that node minted was scoped to
`scribe` alone, leaving the four `unwrap` sites unclaimed.

**So the four sites are a live, unowned finding.** [Co-locate the scan rules with the mechanical
checks](49-colocate-scan-rules.md) is the node whose subject they are — its own annotation already records the
inversion, that `unwrap` is stated four times in the checker contract and **zero** times in the file whose checks
it protects — but its condition names the co-location and not the restatement. One line from the human settles
which it is.
