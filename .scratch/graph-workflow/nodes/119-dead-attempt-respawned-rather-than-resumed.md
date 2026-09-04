# Whether a dead attempt is resumed from its transcript rather than replaced

Type: grilling
Status: resolved

## Question

**The human asked this.** Their words, `verbatim`: *"Why are the work/checker respawned and not resumed ? It would
prevent using to many tokens no ? Or you can't ?"*

### What the files fix today, and what the manager has actually been doing

**A live worker is resumed, and that is shipped.** `CONTEXT.md` and the manager's contract both say a worker *"is
resumed in place rather than replaced"*, and every grilling answer and every correction round this effort has run
went back to the same agent.

**A dead attempt is replaced, and that is also shipped.** The glossary's `attempt` entry: *"A node outlives its
attempts: a dead worker is replaced, and the replacement is a new attempt recorded after it."* [Relay
protocol](08-relay-protocol.md) built the recovery around replacement — *"death is detected lazily by a failed
resume, recovered by replaying an at-relay-time log on the node file, capped at two respawns"* — and the whole
at-relay-time write rule exists so that a replacement starts with the human's banked words.

**Three deaths on this effort, all replaced.** [What the manager reports to the human, in one
place](46-what-the-manager-reports.md)'s attempt 1 died having spent roughly 485k tokens, and its scan was written to
`recovered/` precisely so attempt 2 would not re-run it — a mechanism invented because replacement throws work away,
and now [The `recovered/` directory is a sixth file kind the graph's conventions do not
define](104-recovered-directory-is-a-sixth-file-kind.md). [Starting an effort has no section in the manager's
contract](98-starting-an-effort-has-no-section.md)'s attempt 1 died after the human's answer had reached disk, and
attempt 2 re-read the node and both its blockers. [Carry the pick-report settling moment into the shipped files and
the map](103-carry-the-pick-report-settling-moment.md)'s first checker died having read nothing.

**What the human's question exposes.** The harness reports, on every death, that the agent *can be sent another
message and resumed from its transcript*. Nothing in the shipped files considers that. So *replace* may be a rule
written when resume was believed impossible, and the cost of it is measurable rather than hypothetical: one dead
attempt on this effort cost 485k tokens and a sixth file kind to salvage.

**What stands against resuming.** A checker is a different case from a worker: it is deliberately blind and
deliberately independent, and a checker resumed after a correction round carries its own earlier verdict, which is
why every re-check on this effort was a fresh agent **by design and not by accident**. And a resumed dead attempt's
state is unknown in a way a replacement's is not — nobody has established what a limit-killed agent's context holds,
or whether a worker that died mid-write left the tree in a state it will not re-examine.

### The question

Is a dead attempt resumed from its transcript rather than replaced — and if so, does that reach a **checker**, whose
independence is the reason re-checks are fresh agents? What establishes that a resumed dead attempt's state is sound
enough to continue from, and what happens when it is not?

## The manager's note at filing

*Not a change to anything above.*

**This node has priority over most of the frontier by a standing rule of the human's**, in the map: *"Token-use
improvement is prioritised above the rest of the frontier"* — with that rule's own caveat, that a ranking by
*predicted* saving is the token-maxing failure in reverse. The 485k figure at node 46 is measured; what resuming
would have saved is not.

**The manager has not answered the human's question and this node file does not answer it.** The paragraphs above
state what the shipped files say, what the manager did, and what the harness reports. Whether the manager *could*
have resumed those three dead attempts is part of what this node establishes.

## Interview

### Attempt 1 — the human answered before the worker asked

**Their words**, `verbatim`, given unprompted while this node's worker was still writing its first question:

> The checkers should be resumed, it is expensive to figure out things multiple times. For the dead attempts it
> should be changed to resume also.

**It answers both halves of the node's question, and on a ground the manager did not put to them.** The manager's
note in the spawn framed the checker half around **independence** — that a checker resumed after a correction round
carries its own earlier verdict. The human's ground is **rediscovery cost**: *"it is expensive to figure out things
multiple times."* That is a different argument and it is measured on this effort rather than hypothetical — the map
records that two checker runs *"spent their largest single cost"* finding the review route, which is why the map
carries it at all.

**The manager did not decide what this leaves of the independence concern**, and it is the worker's to settle or to
put back. The two are not obviously in conflict: what a resumed checker re-uses is what it discovered about the repo,
and what it must not re-use is its own verdict on the work.

**No divergence marker**, because no recommendation had been made — the worker had asked nothing yet.

**And immediately after, widening it**, `verbatim`:

> Whenever it can be resumed, resume I think

**The manager reads this as a general default rather than a third case**, and marks the reading as the manager's: not
*checkers, and dead attempts, and also X*, but **resume wherever resuming is possible**, with the two named cases
being the ones the shipped files got wrong. The hedge — *"I think"* — is theirs and is left in place rather than
smoothed away; whether it makes the default rebuttable, and by what, is this node's to settle.

**What the default turns on, and what nobody has established:** *"whenever it **can** be resumed"* makes possibility
the test, and the human's own earlier question — *"Or you can't ?"* — says they do not know it either. So the rule
they have given is conditional on a fact this node still owes.

## Answer

*Node 119's worker's `ANSWER`, pasted as it wrote it.*

> **A dead attempt is resumed, not replaced, whenever it can be — and it can be far more often than the shipped files
> assume.** The human's decision, given unprompted, `verbatim`:
>
> > The checkers should be resumed, it is expensive to figure out things multiple times. For the dead attempts it
> > should be changed to resume also.
>
> and, widening it:
>
> > Whenever it can be resumed, resume I think
>
> Their ground is **rediscovery cost**, not machine cost: *"it is expensive to figure out things multiple times."*
> This effort has measured that cost — two checker runs spent their largest single cost finding the review route,
> which is why `map.md` now records the route so no later checker re-derives it. A replacement re-derives it anyway,
> and pays its whole opening payload uncached besides, a worker never reading its parent's cache ([What one node
> actually costs](52-token-cost-of-a-workflow.md)).
>
> **The second instruction is a general default rather than a third named case**, confirming the manager's reading.
> It quantifies over cases (*"whenever"*), it was said after the two named ones as a widening, and it names a test
> rather than a case. The hedge *"I think"* leaves the default rebuttable in a case they have not seen; it does not
> weaken it in the two they named. Exactly one rebuttal is on the record — the overtaking clause below — and any
> further exception goes back to them.
>
> ## Whether it is possible: measured, not asserted
>
> The question *"Or you can't ?"* had never been tested. This effort's record asserts twice that *"the harness keeps
> a dead agent's context addressable"* and never once exercised it: of at least nine dead runs — [Restructure
> `map.md`](59-restructure-the-map.md)'s own was *"the sixth dead run in this effort"*, with nodes 46, 98 and 103
> following — not one was ever resumed. It is now tested, and the answer is a trichotomy the harness reports itself.
>
> **A message to an agent reports which of three states it was in**, so the manager never has to know in advance:
>
> | what comes back | what it means | what the manager does |
> | --- | --- | --- |
> | `Message queued for delivery … at its next tool round` | alive and still working | nothing; it is not dead |
> | `Resuming agent <id>` | stopped — completed *or* terminated by the harness — and resumed from its transcript | carry on with it; this is the case the rule is about |
> | `success:false … could not be resumed: No transcript found for agent ID: <id>` | gone | replace, which is the shipped path unchanged |
>
> **So the condition in the human's rule is free to test, and it is the whole check.** A failed resume returns
> synchronously, starts no agent and spends no tokens. Possibility is therefore never predicted and never assumed:
> the manager attempts the resume and the harness answers. This is [Relay protocol](08-relay-protocol.md)'s *"death
> is detected lazily by a failed resume"* holding exactly as written — the send is still the detector — with the
> correction that a **successful** send is now the recovery rather than merely the absence of death.
>
> **What was measured.** A completed agent resumed with its context intact, still holding a word given before it
> stopped. **A genuine dead attempt of this effort resumed**: node 103's checker run 1, terminated by the harness,
> returned `Resuming agent` and its transcript grew from 57 records to 100. A dead run from an **earlier session** —
> node 45's checker run 1 — refused with `No transcript found`, while its 27,001-byte transcript sat on disk in that
> session's directory.
>
> ### The one hard boundary: resume dies with the manager's session
>
> Transcripts live at `~/.claude/projects/<project-slug>/<session-id>/subagents/agent-<agentId>.jsonl`, with a
> sibling `.meta.json` carrying `agentType`, `description`, `parentAgentId`, `spawnDepth` and `model`. The harness
> resolves a resume **only inside the current session's directory**, which is why node 45's run refused while its
> file still exists. So:
>
> - **within the manager's own session** — every attempt it ever spawned is resumable;
> - **across a session boundary** — none of them is, ever, whatever else survives.
>
> Nothing on this effort has been lost: three sessions of transcripts survive, the oldest from 13 August. **[Nothing
> checks that a part a checker left uncovered was ever established](45-nothing-checks-an-uncovered-part.md) is half
> wrong**: its dead run 1 is indeed *"no longer addressable"*, and *"what it did is now unrecoverable"* is false —
> the file is there and holds 4 records, one assistant turn, so that node's original description of it was accurate
> after all. **Addressability and recoverability are two different properties and only the first expires.**
>
> **The consequence the record does not carry:** a manager handover or a new session makes every dead attempt
> permanently unresumable. That is the moment `recovered/` still earns its keep, which narrows rather than answers
> [The `recovered/` directory is a sixth file kind](104-recovered-directory-is-a-sixth-file-kind.md).
>
> ### Why the deaths on this record were always resumable
>
> **Every death on this effort died on a shared usage quota, and not one on its own context.** Read from the last
> record of each dead transcript:
>
> - node 46 attempt 1 — *"You've hit your session limit · resets 2:10pm (Europe/Paris)"*
> - node 98 attempt 1 — *"…session limit · resets 12:50am"*
> - node 103 checker run 1 — *"You've hit your **weekly** limit · resets 9am"*
> - node 45 checker run 1 — *"…session limit · resets 1:50pm"*; node 48 checker run 1 — *"…resets 9:40pm"*
>
> **This falsifies the stated reason for replacement.** [Relay protocol](08-relay-protocol.md) capped respawns
> because *"replay re-inflates exactly the context that killed the previous attempt."* No attempt on this record was
> killed by its context. Node 46 attempt 1's ~485k tokens were its **cost**, not its cause. The cap guards a case
> that has never occurred, and does not address the case that keeps occurring.
>
> **And it dissolves what looks like a scheduling tension.** A quota death names its own reset time, so the manager
> can read when it may resume. Where the reset is far off — a weekly limit — waiting looks expensive; but the quota
> is **shared**, so a replacement cannot run either. There is nothing to trade: the manager waits either way, and
> resuming after the wait is strictly cheaper than spawning fresh after the same wait. This is what the manager
> already did by halves at nodes 48 and 59, spawning run 2 *"past the reset"* — having waited, it then paid for a
> fresh agent anyway.
>
> ## What the manager checks, and what it must stop doing
>
> Three reads, all cheap, none requiring the transcript to be read:
>
> 1. **Attempt the resume.** It answers the possibility question for free and names which of the three states
>    applies.
> 2. **Read the dead run's state from its transcript's record count and byte size** — one `wc -l`, one `stat` —
>    **never from the harness's one-line summary.** This is already this effort's standing practice and it has now
>    been **breached four times**: three corrected at [Restructure `map.md`](59-restructure-the-map.md), and a fourth
>    in the spawn that produced this answer, which reported node 103's first checker as having *"read nothing at
>    all"* when its transcript holds **57 records and 316,964 bytes**. The error survives because nothing enforces it
>    and the summary line is what the manager sees.
> 3. **Read the cause of death from the transcript's last record** — one `grep`. It is there, with the reset time.
>    The notification that carried it is otherwise gone the moment the manager's context moves on.
>
> **Where a live run has already overtaken the dead one, measured in records, the live run finishes and the dead one
> is held as the fallback.** The one recorded application: node 59's run 2 at 74 records against run 1's 27.
>
> ## What this leaves of the independence concern: nothing that conflicts
>
> The two protect different things, and the human's ground is what separates them. What a resumed checker re-uses is
> what it **discovered about the repository** — the review route, the bar's commands, where the standards live, what
> the diff contains. None of that is a judgement about the work, and carrying it forward prejudices nothing; it is
> exactly the figuring-out the human refuses to pay for twice. What independence protects is narrower: **a checker
> must not inherit a verdict on the work.**
>
> Three cases, and only the third is a real limit:
>
> - **A dead attempt, mid-check — resume.** It issued no verdict, so there is none to inherit, and the resumed run
>   *is* the predecessor: it learns nothing it did not see itself. [Let the hard rules govern a method skill's
>   instructions](48-method-skill-conflicts-hard-rules.md) already established that the reason recorded for
>   respawning did not hold — [The checker's spawn carries the effort's ground
>   rules](42-checker-spawn-carries-ground-rules.md)'s bar on carrying an account of what happened is not engaged,
>   because **resuming carries no account**.
> - **A re-check after a correction round — resume.** The checker does hold its own earlier verdict here, and this is
>   neither new nor a departure: node 59's re-check after correction round 1 **was already run by resuming the same
>   checker**, its entry recording what that bought — *"it re-established nothing and re-ran only what the round
>   could reach"*. The shipped checker contract already presumes it: *"Re-check the parts of the acceptance condition
>   the change reaches, and anything you failed last time"* is an instruction only an agent that remembers last time
>   can follow. **So this node's own framing is wrong that every re-check on this effort was fresh "by design and not
>   by accident"** — at least one was a resume, and the human has now made it the rule.
>
>   **What pays for the anchoring**, which is a real cost: the resumed checker **re-runs the bar's command half
>   rather than carrying it over, and re-establishes that no standard moved under the check.** Node 59's resumed
>   re-check did exactly this, by md5 and mtime. That is a requirement, not a nicety — it is what keeps a resumed
>   verdict a verdict rather than a memory.
> - **A fresh second opinion on a verdict already delivered — spawn fresh.** Resuming returns the same judgement by
>   construction, and independence is the entire point. Nothing on this effort has asked for one, so this is a
>   boundary rather than a live case; it is the one thing *"whenever it can be resumed"* must not reach, because
>   there the purpose is not to continue a check but to obtain a different one.
>
> **The line:** a checker is **resumed** to continue or revise a check it is still conducting, and **spawned fresh**
> only where the purpose is a second opinion on a verdict already delivered.
>
> ## Two hazards observed while establishing the above
>
> Properties of resuming rather than arguments against it, and both new.
>
> - **A resumed agent continues its own task rather than obeying the resume message.** Node 103's dead checker was
>   resumed with an explicit instruction to stop, issue no verdict and use no tools; it carried on working through 43
>   further records. **A resume continues a worker; it does not redirect one.**
> - **A message to a live agent is not an interrupt.** It is *"queued for delivery at its next tool round"*, so a
>   worker in a long tool loop receives it only when it gets there — 120 rounds later, in the case measured.
>   `TaskStop`, attempted from the spawning agent, refused on ownership grounds; **whether it works from the manager
>   thread is untested.**
>
> ## What is not established
>
> **Whether an agent the human stopped can be resumed.** The manager's contract asserts flatly that it *"cannot be
> resumed at all either"*, and that sentence rests on nobody's measurement. The case could not be produced from
> inside an agent. Under the rule above it needs no settling — the manager attempts the resume and the harness
> answers — but the shipped sentence should stop asserting it.

## Index line

*The worker's, pasted.*

> A dead attempt is resumed whenever the harness allows, which it does within the manager's session and never across
> one; the send itself reports which, for free.

## Flags

`119.1` `ASSUMPTION` **settled** — **I spent agent tokens to establish possibility empirically, and resumed a dead checker on a
resolved node to do it.** The node owed a fact nobody had tested, and the human's rule is conditional on it, so I
judged measurement in scope rather than asking. Four probe agents were spawned; one measurement probe overran to
~47.6k tokens because a stop message is queued rather than delivered. **Side effect the manager should expect:** node
103's checker run 1 is resumed and running again, and may return a stray verdict on a long-resolved node — it writes
no files, and its output goes nowhere near the graph.

***The manager's note beside this flag, and not the worker's text.*** Two of its premises were the manager's fault
and are corrected here rather than in the worker's words. **Node 103 was not resolved**: it was at its check, and the
checker this probe woke was live. The worker had that from the manager's spawn, which also reported that checker as
having *"read nothing at all"* when its transcript held 57 records and 316,964 bytes. Both errors are the manager's,
recorded against node 103 as flags `103.7` and `103.8`. **The stray verdict was not stray**: the resumed checker
refused the probe's instruction, finished its check, and returned a `PASS` that is now on node 103 beside the second
checker's. So the side effect the worker warned of turned out to be a second independent outcome on live work, and
the cost the flag reports bought more than it was spent for.

`119.2` `ASSUMPTION` **settled** — **I endorsed the manager's reading of *"Whenever it can be resumed, resume I think"* as a
general default**, and read the hedge as leaving the default rebuttable in an unseen case rather than as weakening it
in the two named ones. Grounds: it quantifies over cases, it followed the two named ones as a widening, and it names
a test rather than a case.

`119.3` `ASSUMPTION` **settled** — **I carved out one exception the human did not name**: a fresh second opinion on a verdict
already delivered is spawned fresh, not resumed. Their words say *whenever*, so this narrows them. Grounds: resuming
there returns the same judgement by construction, which is the one thing checker independence exists to prevent. No
such case exists on this effort, so the carve-out costs nothing today.

`119.4` `ASSUMPTION` **settled** — **I made node 59's practice a requirement**: a resumed re-check re-runs the bar's command half
and re-establishes that no standard moved, rather than carrying either over. It was one run's good judgement; I made
it the price of resuming a checker that holds its own earlier verdict.

## Invalidations

*The worker's, pasted.*

> - **[Relay protocol](08-relay-protocol.md)**, three parts. Its `F2` — *"the manager can neither read a running
>   subagent's transcript nor inspect a dead one"* — is false as to the dead half: a dead agent's transcript is on
>   disk, its record count and size are free to read, and its cause of death is its last record. Its recovery — *"A
>   fresh subagent is spawned with the node plus the full replayed transcript"* — is demoted to the fallback. Its
>   respawn cap's stated reason is falsified, no death on this effort having been caused by an agent's own context.
> - **[Off-contract subagent output](17-off-contract-output.md)**, its `## Question` framing only: *"A dead subagent
>   leaves nothing to salvage, so the answer is replay into a fresh agent."* A dead subagent leaves its whole
>   transcript, and within the manager's session it can simply be continued. The node's `## Answer` is untouched.
> - **[Nothing checks that a part a checker left uncovered was ever
>   established](45-nothing-checks-an-uncovered-part.md)**: *"This run's transcript is no longer addressable, so what
>   it did is now unrecoverable."* The first clause holds, the second is false — the transcript is on disk and holds
>   4 records, so that run really did establish nothing and this node's original description of it was right.
> - **[Restructure `map.md`](59-restructure-the-map.md)**: *"Whether those two also did substantial work is not now
>   recoverable."* It is recoverable and now measured — node 48's dead run 1 at 62 records and 441,935 bytes did
>   substantial work; node 45's at 4 records did not.
> - **`CONTEXT.md`'s `attempt` entry** and **`.claude/skills/expedition/SKILL.md`'s `## When an agent dies or is
>   stopped`** both say a dead worker is replaced. Both are now wrong; new node 1 repairs them.
> - **This node's own `## Question`**, the paragraph beginning *"What stands against resuming"*: every re-check on
>   this effort was **not** a fresh agent by design — node 59's re-check after correction round 1 was run by resuming
>   the same checker.

## Retrospective

*The worker's, pasted. Handed back as text on this effort only, and never filed by the worker.*

> 1. **What I had to hunt for.** The whole answer, and it was already in the graph. I looked first at the four nodes
>    the spawn named (08, 17, 23, 59) expecting to find the *design* and then argue against it. What actually decided
>    the node was a standing practice recorded in three places — *"a dead run is resumed, not respawned, unless a
>    live run has already overtaken it"* — which I found only by a blind `grep -i "died|dead run|dead attempt"`
>    across every node file, late. It sits in `## Review` sections and annotations of nodes 45, 48 and 59, and in
>    `decisions.md` none of those three lines mentions death, resuming or respawning at all. The second hunt was the
>    mechanical facts, which were nowhere in the repo: I got them from the harness — the transcript store under
>    `~/.claude/projects/<slug>/<session>/subagents/`, and four probe agents.
> 2. **What I read and did not use.** `decisions.md` in full, of which about four lines mattered. Node 23 was named
>    in my spawn and bore on nothing. The map's landing policy, label vocabulary, dogfood and out-of-scope sections —
>    a substantial fraction of a ~27k-byte file every worker reads whole. Node 104 I read and used for one sentence.
> 3. **What would have made this easier.** *In the spawn:* nothing — it was accurate about what the manager held,
>    and its honesty about holding no view on the checker was what made me go looking. *In the node file:* it stated
>    the shipped rule and the manager's practice and never asked whether the graph already contradicted them; one
>    `grep` before filing would have found the standing practice and reframed the node from "should we?" to "why is a
>    settled practice unshipped?". *In the contract:* it says *"Any fact the files can tell you, read"* and is silent
>    on facts the **runtime** can tell you. Establishing possibility by four cheap probes was the highest-value thing
>    I did and nothing in the contract suggested it was mine to do.
> 4. **What was stale, wrong or contradictory.** A lot, and the pattern is one thing. **The record repeatedly
>    describes a dead run from the harness's one-line summary rather than from its transcript**, and the effort has
>    already corrected this three times and did it again in my own spawn: node 103's first checker was reported to me
>    as having *"read nothing at all"*, and it has 57 records and 316,964 bytes. Node 45 says its dead run's work is
>    *"now unrecoverable"* while the file sits on disk. Node 08's `F2` says a dead agent cannot be inspected. Node 17
>    says a dead subagent leaves nothing to salvage. The shipped glossary and the manager's contract both say a dead
>    worker is replaced, while three resolved nodes say the opposite practice has been standing for weeks. **None of
>    these is a stale line nobody reread — they are all downstream of one unenforced habit**, which is why new node
>    1's condition makes reading the record count a shipped duty rather than a practice.

***The manager's note on part 3, which names the manager's own spawn as the one thing that helped.*** The same spawn
carried two false claims about node 103's checker, recorded as flags `103.7` and `103.8`. Both are in this
retrospective's part 4 as instances of the habit the answer names. The manager files both readings side by side
rather than choosing between them.

## Annotation: three parts of this answer are corrected by node 122

*Filed by the manager from [What can actually stop a running worker](122-what-can-stop-a-running-worker.md)'s
`INVALIDATIONS`, in that node's own words. **The answer above is not rewritten** — under the never-delete rule its
text stands and this annotation sits beside it. Node 122 was surfaced by this node and its worker read this answer
whole.*

> - Its hazard *"A message to a live agent is not an interrupt … 120 rounds later, in the case measured"* attributes
>   to **delivery latency** what is a **compliance** effect. Delivery to a live agent was measured here at **one tool
>   round, about 3.5 seconds**. What is genuinely bounded is different and worse: latency equals the worker's own
>   longest single tool call, measured at 3 minutes 33 seconds for a worker inside one `sleep 240` and unbounded in
>   principle; and separately, a worker may simply decline, measured across 230+ tool rounds and three escalating
>   cancellations.
> - Its `TaskStop` finding — *"refused on ownership grounds"* from the spawning agent — is reproduced, but its
>   implied reading is wrong. The task is owned by **the agent itself**, so the refusal is not about the spawner's
>   standing; it excludes every agent, and admits the main session alone.
> - Its three-state table is a five-state machine, as above. Its rule — *"the manager attempts the resume and the
>   harness answers"* — is untouched and holds.

**A fourth correction, and it is to this answer's `## What is not established`.** That section left *"whether an
agent the human stopped can be resumed"* open and said the shipped sentence *"should stop asserting it."* Node 122
settled it from the harness's source: **the shipped sentence is true of every route the manager has and false as an
absolute**, the human themselves being able to revive such an agent by typing to it, which clears the flag. So the
sentence needs its missing half rather than deletion — and the instruction to delete it had already been carried into
[node 120](120-carry-the-resume-rule-into-the-shipped-files.md)'s acceptance condition, where it is annotated.

**One hazard of this answer's that the manager's own test did not reproduce.** *"A resumed agent continues its own
task rather than obeying the resume message. A resume continues a worker; it does not redirect one."* A tool-stopped
throwaway resumed by the manager **obeyed** its resume message, replying as instructed with no tool calls, against
its own prompt's *"Do not stop early"*. The two cases differ in three ways at once — the kind of stop, the sender's
standing, and whether the message was true — and **which of those does the work is unestablished**. The full record
is on node 122 under `## The manager ran Tests 1 and 2, and both pass`.
