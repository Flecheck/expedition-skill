# What makes a change to a record file a node rather than the manager's bookkeeping

Type: grilling
Status: resolved

Blocked by: none

## Question

*The human's own, `verbatim`, on 2026-09-20, given at [node
277](277-the-removal-step-of-the-worktree-route-does-not-work-as-written.md)'s gate:*

> approve, I am a bit confused that it's an implementation node, I would have kinda expected it to be the manager ?
> Since it is only writing findings ?

**The contract draws the line and does not say where it falls.** `SKILL.md`'s `## Writing the graph` says the
manager is the only writer of the graph's record — *"the answer, the status, the `decisions.md` line, the flags"* —
and then immediately: *"**That is about recording, not about files.** Where a node's own work **is** a change to a
graph file, that worker makes the change itself, as it would any other work."* **So there are two sides and no
test for which side a given change is on.**

## The manager's note at filing

*Not a change to anything above. None of it is an answer.*

**The test the manager has been using, stated so it can be judged rather than inferred.** It is not written
anywhere and the manager has been applying it node by node:

- **The manager's own, as recording**: statuses, `decisions.md` lines, flags, annotations onto a node, invalidation
  marks, and a condition amendment under [node
  252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md). Every one **transcribes** something an agent
  handed back or a decision already settled.
- **A node's own work**: text that **states a rule that currently binds** — in `map.md`, `map-manager-only.md`,
  `map-implementation-rules.md`, or a shipped file. That text is authored prose, held to the bar, and changing it
  runs the `Change the map` procedure with banking.

**What the manager thinks the line actually buys, offered as material.** Node 277 is the sharpest available test of
it, because the manager wrote the node, the condition and the mechanism — **and the mechanism was wrong.** Its
worker refuted it and raised rather than shipping it; a checker blind to all of that reproduced the measurement and
reached the same corrected trigger. **None of that happens if the manager writes the text itself**, because there is
no condition to raise against and no checker on a manager's edit.

**What it costs, and the human's question is fair on this.** A worker, a checker and one of their turns, to change
about twenty-four lines. Three of the last six implementation nodes have been of this shape. **The manager holds no
position on whether that trade is right**, only on what the alternative gives up.

**Two things the answer has to reach beyond the test itself.** Whether the answer distinguishes *findings* from
*rules* — the human's *"only writing findings"* suggests it might, and node 277's text is both, a measured symptom
beside an instruction every future manager follows. And whether the manager's own conduct changing before the record
does — *"removals now run with the sandbox off"*, decided and acted on before any node landed — is legitimate or is
the thing that makes the node feel redundant.

## Flags

`283.1` `MANAGER-WRONG` **· settled** — ***Filed by the manager against itself, from its worker's correction.*** The manager's
note above and its spawn both stated that **three of the last six implementation nodes have been this shape.** The
worker re-derived it: that is true of the last six **filed** (276, 277, 281 of 276–281), but **four of those six
have not been built**, and of the last six that actually **landed**, two were record-only. **The real figure is 2 of
6.** The manager counted filings and reported them as landings, which overstates the cost of the very thing the
human was questioning — **by a factor of one and a half, in the direction that argues against the manager's own
position.** This is the **third** count in three days the manager has passed on without re-deriving; the other two
are `263.4` and `95.6`.

## Interview

### Attempt 1 — the question put to the human

*Pasted as the worker wrote it. Banked here so that a death leaves the worker's work on disk.*

**ABOUT:** You asked at node 277's gate why a change to the effort's own record was an implementation node rather
than something the manager just does — *"since it is only writing findings"*. Nothing written anywhere answers that,
so the manager has been deciding it node by node. This node fixes the line.

**SO FAR:**

**What the contract actually says.** The manager's skill file says the manager is the only writer of the record —
the answer, the status, the `decisions.md` line, the flags — and then immediately: *"That is about recording, not
about files. Where a node's own work **is** a change to a graph file, that worker makes the change itself."* So it
names two sides and gives no test for which side a change is on. **It is worse than silent**: the same sentence says
*"every procedure in `graph-conventions.md` are yours, and no worker performs one"*, and **`Change the map` — the
replace-and-bank procedure — is one of those procedures, handed to a worker by the conditions of nodes 268, 277 and
281 in a row.** That sentence needs repairing whichever way you answer, and I am carrying it as a separate finding.

**What the manager has been doing, unwritten.** Its side: statuses, index lines, flags, annotations onto a node,
amendments to an acceptance condition. A node's side: text that states a rule that currently binds. **I tested that
and it does not hold as stated** — node 199 already settled that an acceptance condition *is* rule-stating text, and
the manager amends those itself (it amended node 95's). So *"rule-stating"* is not what is doing the work. **The
line it has really been drawing is a file line**: `map.md` and its siblings, and shipped files, are nodes;
`decisions.md`, `flags.md` and the node files are the manager's.

**What actually happened inside node 277, which is the case you saw.** The manager wrote that node, its condition,
and the mechanism it was to write down — **and the mechanism was wrong.** Its worker did not transcribe it. It ran
two read-only probes, measured that the condition's stated trigger was false of both live worktrees, and **stopped
and raised rather than shipping it.** The manager then produced a measurement that killed the worker's own
replacement mechanism too, and the field narrowed to one candidate that fits all seven observations and is still
recorded as a fit rather than a proof. **So the thing that looked like "only writing findings" was the case where
the finding was false, and the node is what caught it.** That does not happen on a manager's own edit: there is no
condition to raise against.

**The measured cost, re-derived rather than taken from the record.** Node 277's landing: 2 files, 48 insertions, 4
deletions — and 24 of those insertions are the verbatim bank, so the new rule text is **about twenty-four lines,
exactly as you put it.** Node 268's: 3 files, 150 insertions, 49 deletions, 110 of them the bank. **Those two are
the only record-only implementation nodes that have landed.**

**A count the manager passed me, corrected.** *"Three of the last six implementation nodes have been this shape"* is
true of the last six *filed* (276, 277, 281 of 276–281) but **four of those six have not been built**. Of the last
six that actually *landed*, two were record-only. **The real figure is 2 of 6.**

**What each half of the machinery has produced, on those two landings.** The worker: **one refusal to write a false
mechanism into a binding file, out of two.** The checker: two `PASS`es and zero findings against the work — **but its
runs were not idle**, because what it verified mechanically was the never-delete bank: `map-history.md` proved a
byte-exact prefix of its new self, and each banked passage proved a byte-identical substring of the pre-change file
and absent from it afterwards. **Nothing else in the workflow verifies that invariant.**

**One thing I settled myself and will return as an assumption:** I read the question as reaching every file of the
effort's record, not only the ones node 277 touched, because the manager's line has to be drawn once for all of
them.

**ASK:** Where do you want the line between a node and the manager's own bookkeeping to fall on the effort's record
files — and separately, are you willing to keep paying one of your own turns for it?

**RECOMMENDED:** **Keep the line where it is, write it down as a file test, and take your turn out of it.**

The test, written so nobody has to infer it again: **rule-stating text in `map.md`, its siblings and any shipped
file changes on a node; everything inside `decisions.md`, `flags.md` and the node files** — statuses, index lines,
answers, annotations, flag entries, condition amendments — **is the manager's own.** That is a file test, decidable
by looking, with no judgement call left in it.

What it rests on is the case you asked about. **You read node 277 as transcription; so did the manager, which is why
it wrote the condition that way; and the transcription turned out to be false.** A rule that lets the manager write
it whenever the content looks already-settled hands that call to the party that got it wrong.

**But the cost you named is the right cost, and it is not the tokens** — your own map says the human is the scarce
resource and exactly one thing sits in front of you at a time. A gate on a twenty-four-line map edit spends that one
slot, and both record-only gates so far returned approve. So: **a record-only node lands on the manager's judgement
and appears in the pick report with its path, with no gate.** The pick report takes no place in your queue, you
still see the change in the diff, and you keep the route to reverse it. **That is strictly more review than making
these edits bookkeeping** — which would land them with no worker, no checker and no gate at all — **and it costs you
nothing.**

**ALTERNATIVES:**

- **Draw the line on content**, as *"only writing findings"* implies — the manager writes it where nothing needs
  establishing, a node where something does. *Setting aside:* on node 277 the manager graded it exactly that way and
  was wrong, so the test asks the one party with a stake in the answer.
- **Draw it on size** — below some number of lines it is the manager's. *Setting aside:* node 277 was twenty-four
  lines and is the one that mattered.
- **Keep the node but drop the checker**: the manager writes the condition, one worker does the edit, nothing
  reviews it. *Setting aside:* the checker is what verifies the never-delete bank mechanically, and nothing else
  does.
- **Drop the worker and keep the checker**: the manager writes the text, one read-only agent reads the diff.
  *Setting aside:* on the two landings, the worker produced the only refutation and the checker produced none — this
  drops the half that has paid.
- **Leave it exactly as it is, gate included.** *Setting aside:* it spends your one queue slot on edits that have
  been approved every time, and that slot is the resource your own map says is scarce.

#### The human's answer — **a divergence**

*Their reply on 2026-09-20, `verbatim`:*

> I am expecting the change to the map to be mostly the manager. The subagents should be used to update the
> deliverable, here the skills, or in special case if we change the skill we might need to update the map to keep it
> in line.

**Marked a divergence, and the mark is the manager's duty rather than a comment.** The worker's `RECOMMENDED` was
*"keep the line where it is"* — rule-stating text in `map.md`, **its siblings** and any shipped file changes on a
node. **The human's answer reverses the map half of that**: the map is **mostly the manager's**, a subagent's proper
object is **the deliverable — the skills**, and a map edit is a node only in the **special case** where a skill
change drags the map after it to keep the two in line. Without this mark the worker would read a bare answer as
agreement and resolve as though its recommendation had carried.

**It also answers the second half of the `ASK` by making it moot.** The worker asked whether the human would keep
paying a turn for these; on this answer most of them stop being nodes at all, so there is no gate to pay for.

***The manager's own note, beside their words and not part of them.*** **This reverses the manager's own practice
across six nodes and reaches live work**, and the manager is naming that rather than letting the worker discover it:
nodes **268**, **277** and **281** were map-only and landed as implementation nodes; **281's gate is assembled and
queued right now**; and **271**, **276** and **284** are open, map-only, and would become the manager's. **The
manager has not acted on any of it** — the answer is the worker's to write, and standing six nodes down on a reading
the manager made itself is exactly the move flag `95.5` records the cost of.

**The worker was resumed in the same turn**, carrying their words, this divergence mark, and the one thing the
manager holds that cuts against the answer and should not be quietly dropped: **at node 277 the manager wrote the
map text's mechanism itself and it was wrong.** A worker refused to ship it and a blind checker reproduced the
refutation. **Under this answer that node is the manager's and the false mechanism lands.** That is not an argument
for refusing the human's direction — it is theirs to give — but an answer that does not say what replaces the
refutation is incomplete.

***The resumed attempt died before writing the answer.*** Terminated by the harness on a weekly API limit, its last
words being *"The human diverged. Let me verify the three open nodes their answer would reach before I write it."*
**It wrote no file and no answer.** The human's words, the divergence mark and the three things the manager sent it
are all above, so **nothing it held is lost**: a replacement attempt replays what the human has already said,
marked settled, and they are not asked twice.

**This node is `claimed`, its question answered and its answer unwritten** — which is the one state the manager's
own stop procedure does not list among the three that read as an ordinary node. **It is neither waiting at a gate,
nor holding an unanswered question, nor parked.** Named here so a fresh manager does not have to derive it, and
named in the closing report as outstanding.

***Attempt 2 was spawned and wrote the answer below.*** The manager had told the human a replacement *"would die on
arrival"* because the weekly limit killed attempt 1. **That was an inference from one observation, asserted without
the one cheap test that settles it**, which is the same failure four of the manager's own flags record. The human
asked *"why would it die ?"*, the manager tested it, and it did not.

## Answer

*Written by this node's worker (attempt 2) and pasted as it wrote it.*

> ### The rule
>
> **A file test, with three branches and no fourth. It is decidable by looking at which file a change touches, and
> no judgement about the change's content enters it.**
>
> 1. **A change to a file the workflow ships is a node's work, always** — `.claude/skills/**`, `.claude/rules/**`,
>    the glossary. Whoever noticed the file was wrong does not matter; **the manager never makes one of these edits
>    itself.**
> 2. **A change confined to the files of this effort's own record is the manager's own** — `map.md`,
>    `map-manager-only.md`, `map-implementation-rules.md`, `map-history.md`, `decisions.md`, `flags.md`, and the node
>    files. **No node, no acceptance condition, no worker, no checker, no gate.**
> 3. **The special case: a record change that rides a shipped change.** Where a node of kind 1 would leave the record
>    contradicting what it ships, **that same node's worker makes the record change too** — inside that node, named
>    in its acceptance condition, landing in the same commit. **A separate node is not minted for the map half.**
>
> **The reverse does not hold.** Noticing that a record file is wrong never turns into a shipped-file node.
>
> **The word *"mostly"* is discharged by branch 3 and leaves no residual discretion.** It is deliberately not a
> licence for the manager to grade a record change by how much authoring it needs. **Grading by content is what
> failed here**, and a test that keeps it puts the call back with the party that has already got it wrong.
>
> **What the test does not distinguish is *findings* from *rules*.** This answer refuses that contrast on purpose:
> node 277's text was both at once, and no one could sort it by looking. **The file is what can be looked at.**
>
> ### What this gives up, measured rather than argued
>
> **The apparatus never verified that a map statement was true. The sharpest case cuts the opposite way from how it
> has been read on this node:**
>
> - **At [node 268](268-carry-the-plain-git-worktree-route-into-the-map.md) the whole machinery certified a
>   falsehood.** Its acceptance condition — **written by a subagent**, node 265's worker, not by the manager —
>   demanded the map state that *"no step of the route needs a harness tool call or a sandbox override"*. A worker
>   wrote it. The checker's Run 1 returned `PASS` and named that clause **MET**. The human approved at the gate.
>   **The claim was false when it was written**, and what caught it was the manager running `git worktree remove`
>   minutes after the landing and getting `Device or resource busy`.
> - **At node 277 a worker did catch a false mechanism** — the manager's own — by running two read-only probes.
>
> **So the record is one catch and one miss on the same claim, and the miss was the one that went through every
> stage.** A checker holds work against its condition; **where the condition asserts the falsehood, a correct
> checker certifies it.** What has actually caught every false mechanism on this effort is **somebody running the
> mechanism**, which is the manager's own act and survives this answer untouched.
>
> **The residual loss is real and is not that.** Two things stop: **`map.md` is read whole and cold by every worker
> on every node**, so a false line there is the most widely read false line in the effort; and **the checker was the
> only thing verifying the never-delete bank, and it verified it mechanically** — node 281's checker established
> `map-history.md`'s base as a **strict byte prefix** of the new file, node 268's did the same. **No mechanical
> check in `graph-conventions.md` covers this**, so the bank becomes a procedure nobody verifies.
>
> ### What replaces them
>
> Two duties, both the manager's, neither costing a turn of the human's:
>
> 1. **A map line that states a mechanism is written only from a run the manager performed, and says what was
>    measured.** Both false claims on this effort were mechanism claims written from reasoning rather than from a
>    run. **This is the discipline the two catches actually came from, made standing.**
> 2. **The bank gets a mechanical check**, so that what the checker was doing survives the checker.
>
> ### One thing this answer buys back
>
> **The manager's conduct and the record now change in one act.** *"Removals now run with the sandbox off"* was
> decided and acted on before any node landed, and **the gap existed only because writing it down was a node.**
> Under branch 2 there is no gap.
>
> ### How far this reaches
>
> - **Work already landed is untouched.** Nodes 244, 268, 277 and 281 stand exactly as they resolved.
> - **Work finished and waiting at a gate, or under check, finishes as a node.** Converting it mid-flight throws
>   away work to save nothing. **No node is in this state as this is written.**
> - **Work open and not started stands down**, by node 264's widened `superseded` — *"a node made unnecessary rather
>   than replaced"* — whose own precedent is this exact shape. **No sixth status, and no new mechanism.**
>
> | node | its work | disposal |
> |---|---|---|
> | 256 | `map.md`, `map-history.md` | manager's |
> | 262 | `map.md`, `map-manager-only.md` | already assigned to node 268 by node 264 |
> | 271 | `map-implementation-rules.md`, `map-history.md` | manager's |
> | 276 | `map-manager-only.md`, `map-history.md` | manager's |
> | 284 | `map-manager-only.md`, `map-history.md` | manager's |
>
> **Node 254 stays a node**: its work is `.gitignore`, which is not the effort's record.
>
> **Standing a node down is not doing its work.** Every one describes something currently false in a file that
> binds. **Node 284 is the one to look at first** — the doubled path that escapes `.gitignore`, measured.
> **Superseding that node without making the edit loses a live defect.**
>
> ### How big this class actually is
>
> **The figure in circulation is *"that kind has occurred three times"*. It is at least ten**, re-derived by reading
> every resolved implementation node's acceptance condition: **171, 188, 193, 196, 200, 229, 244, 268, 277, 281** —
> and nodes below 171 were not enumerated, so **ten is a floor**. **The answer reaches a standing class of this
> effort's work, not a recent cluster.**
>
> ### The defect this answer must also repair
>
> `SKILL.md` says *"every procedure in `graph-conventions.md` are yours, and no worker performs one"*, and `Change
> the map` has been handed to a worker by **seven** acceptance conditions. **This answer makes that sentence nearly
> true and not true**: branch 2 returns the procedure to the manager, branch 3 still hands it to a worker.
>
> ### This answer's own carriage, which the answer decides
>
> **Into `map.md`: the manager's own edit, under branch 2. Into the shipped skill files: a node, under branch 1.**
> That split is the answer applied to itself.

**The index line the worker wrote:**

> A file test: shipped files are a node's work always, the effort's record is the manager's own, and a record edit
> rides the shipped node that would otherwise contradict it.

## Flags

*All three are the worker's own text, pasted.*

`283.2` `ASSUMPTION` **· settled** — Read the human's *"the map"* as the effort's whole record rather than `map.md` alone, on the
deliverable-versus-record split their own sentence draws. A narrower reading would make `map-manager-only.md` a
node's work while `map.md` is the manager's, **which nothing supports.**

`283.3` `ASSUMPTION` **· settled** — Read the special case as the map edit **riding inside** the shipped-file node rather than
being minted as a node of its own, because *"to keep it in line"* is a simultaneity requirement and **a second node
guarantees a window in which the two disagree.**

`283.4` `ASSUMPTION` **· settled** — **The two safeguards are the worker's own and were never put to the human**, this session
closing under `/expedition-stop` with no fresh payload permitted. Stated because *"an answer that removes the only
review a class of edits had and does not say what replaces it is incomplete."* **Both are cheap and reversible;
either can be struck without disturbing the file test.**

## Invalidations

*The worker's own text, pasted.*

> **[Node 171](171-carry-the-record-node-reading-rule-into-the-rules-file.md) — narrowed, not contradicted.** Its
> rule survives and still fires, **but only inside branch 3.** Its ordinary case — a node whose entire work is a
> record file, which is **all ten of the landed instances counted above** — no longer exists. The rule's text needs
> no change; **a reader who takes its frequency as evidence of how the workflow normally runs would now be wrong.**
>
> **No resolved node is contradicted.** Nodes 189, 264 and 252 are used by this answer rather than displaced.
>
> **One piece of bookkeeping I found open, reported because this answer depends on the same route.** Node 264
> resolved and stood five nodes down — 203, 245, 250, 261 and 262 — and **none of the five has been marked**: all
> five still read `Status: open`, and not one carries a `Superseded by:` line. **The disposal this answer prescribes
> uses that same procedure, so the earlier five are worth clearing in the same pass.**

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.** **The load-bearing fact of the whole answer — who wrote the false no-override claim
> — is in no file that names it as such.** Node 277 states the claim is false and never says who wrote it. I found
> it at line 42 of node 268's acceptance condition, attributed in that node's header to node 265's worker, and
> confirmed the checker had certified it by reading node 268's Run 1. **I looked at node 277 and `map.md` first,
> which cost two reads.** Second: **the true size of the record-only class, which exists nowhere** and had to be
> derived by scanning every node file's acceptance condition. Third: **the disposal route, node 264's answer — the
> spawn did not name it**, and I reached it only because its filename appeared in a directory listing.
>
> **2. What arrived that this node did not need.** The grilling contract's payload shapes, numbering rules, re-ask
> rules and `park` shape — roughly a third of that file — **all bear on putting a question to the human, and my
> spawn's first instruction was that I must not put one.** A contract separating *asking* from *answering* would let
> a no-ask attempt skip it. `graph-conventions.md` I opened for the two sections the spawn named and got one usable
> sentence; **what I actually needed was `## Mechanical checks` and `## Statuses`, neither of which the spawn
> named.**
>
> **3. What would have made this node easier.** **The spawn enumerated six nodes in a form that reads complete. It
> is not** — 244 landed in the same class, 256 and 262 are open in it, and at least six more landed before 244.
> **The correction a spawn can make cheaply is to say *"here is the class and I have not enumerated it"* rather than
> list what it happens to remember, because a list that looks closed invites a worker to build on it** — which is
> how the *"three times"* figure was about to reach this answer unexamined. **Naming node 264 would have saved the
> largest single search.**
>
> **4. What I read that was stale, wrong, or contradicted something else.** **The *"three times"* figure is wrong by
> at least a factor of three, and it is the fourth count on this effort passed on without re-derivation.** **Node
> 264's answer is not applied to the graph**: five nodes it stood down still read `Status: open` with no `Superseded
> by:`, **so the graph and the decision disagree, and mechanical check 5 would not catch it because the disagreement
> is on the superseded side.** And `SKILL.md`'s *"no worker performs one"* was **contradicted by seven acceptance
> conditions at the time it was written.**

## The manager's disposal

*Not the worker's text.*

- **Both surfaced nodes minted**: [node 287](287-ship-the-record-file-test-and-repair-the-procedures-sentence.md) and
  [node 288](288-nothing-mechanically-verifies-the-never-delete-bank.md), each carrying its author's own condition.
- **Node 264's five supersessions are performed in this same turn**, the worker having found them undone. **That is
  the manager's bookkeeping, owed since node 264 resolved, and it had been named as owed and not done.** Under the
  answer just given it is also branch 2 work, which is the first act taken under this rule.
- **The manager's *"three times"* is wrong and reached the human** as well as this worker. **Filed as `283.5`** —
  the fourth count in four days.
- **This answer's own carriage is the answer's, not the manager's**: the `map.md` half is the manager's under
  branch 2 and is **not done**; the shipped half is node 287. **Both are named in the closing report.**

`283.5` `MANAGER-WRONG` **· settled** — ***Filed by the manager against itself.*** It told this worker, and the human, that a map
change with no skill near it *"has occurred three times"*. **It is at least ten** — 171, 188, 193, 196, 200, 229,
244, 268, 277, 281, with nodes below 171 unenumerated. **The manager counted what it remembered from this session
and reported it as the class.** Its worker's repair is the generalisable half: **a spawn should say *"here is the
class and I have not enumerated it"* rather than list what it happens to recall, because a list that looks closed
invites a worker to build on it.**

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.

*The manager's note, 2026-10-09:* flags 283.1 carry the settled mark now. They were settled in the triage batch the human approved at node 366's Q4, and the manager did not mark the entries then. Their `flags.md` lines were added by [node 398](398-fix-the-small-graph-defects-the-first-sweep-found.md).
