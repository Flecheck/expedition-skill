# Give the manager's contract a procedure for stopping a running worker

Type: implementation
Status: open

Blocked by: 123, 120

## Question

*Surfaced by [What can actually stop a running worker](122-what-can-stop-a-running-worker.md)'s worker, and pasted as
it wrote it.*

> No shipped file tells the manager it can stop a running agent at all, or how the mechanisms differ. The manager has
> four situations that need one — a node the human redirects mid-run, a worker gone off-contract, a runaway loop, and
> a replacement made redundant by resuming the attempt it replaced — and one of those has already happened and been
> paid for twice. Write the procedure.

**Blockers, in the worker's words:** *"Node 122 resolved; new node 1 above resolved, because what the manager may
promise the human about a stop turns on it; **and the manager having run node 122's Test 1 and Test 2 and recorded
the results, because clauses 1 and 4 of the condition below state as fact what those two tests verify.** It also
touches the same section as [Carry the resume rule into the shipped
files](120-carry-the-resume-rule-into-the-shipped-files.md), so it is sequenced after that node lands rather than
beside it."*

**The manager's note at filing:** the tests are run and recorded, so that blocker is discharged. The header carries
`Blocked by: 123, 120` — new node 1 is [Who performs a stop, and what the human's own stop
destroys](123-who-performs-a-stop.md).

## Acceptance condition

*Written by node 122's worker. Pasted as it wrote it, and not the manager's.*

> The work edits the files below and leaves each in the state described. The checker has the repository and reads
> only this text.
>
> 1. `.claude/skills/expedition/SKILL.md` gains, in its own prose, a procedure for stopping a running worker. It must
>    say all of: that a running agent is stopped with `TaskStop`, addressed by the agent's id; that **only the
>    manager's own thread can do it**, a worker that calls `TaskStop` on another agent being refused with an error
>    naming the agent as its own owner; that the stop is an immediate abort of whatever the agent is doing rather
>    than a stop at its next tool round; that it also stops any agent the stopped agent had spawned; that the manager
>    learns of it as an ordinary task-notification whose status reads `stopped` rather than `completed`; and that the
>    manager confirms the stop by watching the agent's transcript record count stop growing rather than by trusting
>    the success message.
> 2. The same file must say that a worker stopped this way keeps its transcript and can be resumed afterwards like
>    any other stopped agent, and that this is what makes stopping a worker a cheaper act than replacing it.
> 3. The same file must say that a message asking a worker to stop is **not** a stop: it reaches the worker as text
>    at the end of the worker's next tool call, so a worker inside one long command is unreachable for the whole of
>    that command, and the worker may decline it — a worker whose own instructions tell it not to stop early is the
>    case where declining is most likely, and that is the runaway case. It must state that the manager therefore does
>    not use a message where it needs the worker to actually stop.
> 4. The same file must say that a stop the **human** performs from the task UI is a different act with one different
>    consequence: it marks the agent as stopped by the user, permanently, and every attempt the manager makes to
>    resume it is refused. It must say that the manager can tell the two apart before attempting anything, by reading
>    `stoppedByUser` from the agent's metadata file beside its transcript, and that where the flag is set the manager
>    replaces the attempt and tells the human what was lost rather than attempting a resume.
> 5. The same file's account of what a message to an agent reports back must cover **four** outcomes for an agent
>    target, not three: alive and still working; stopped and resumed from its transcript; **stopped by the user,
>    where no resume is attempted at all and the reply says so explicitly**; and gone, no transcript found. It must
>    say that the third of these is not the fourth, and that a manager reading only three outcomes misfiles a
>    discarded worker as either gone or resumable.
> 6. `CONTEXT.md`'s glossary gains or amends whatever entries are needed so that the words this procedure uses for
>    the two stops are defined there, and so that no entry states or implies that a running worker cannot be stopped.
>    Superseded wording is marked as superseded and left in place rather than deleted.
> 7. Any other file under `.claude/skills/` that states or implies that the manager has no way to stop a running
>    agent, or that a message to a running agent interrupts it, is brought into line with items 1–6. The work reports
>    the search that found them — the terms searched and the files searched — and reports any instance found outside
>    items 1–6 rather than silently editing it or silently omitting it.
> 8. No latency, token or cost figure appears anywhere in the work as a measured quantity unless the number and what
>    measured it are in the work's own text.
> 9. The standing bar for this repository.
>
> *What I could not write, and why:* nothing. Clauses 1 and 4 state as fact what Test 1 and Test 2 verify, which is
> why the manager running them is a blocker rather than a nicety — if Test 1 fails, clauses 1, 2 and 5 are wrong and
> this condition must be rewritten before the node is claimed.

## Annotation: clause 1 states one thing as fact that the manager's own test contradicts

*Filed by the manager. **The condition above is not amended by this annotation**, and the manager has not touched it:
rewriting a condition is not the manager's, and a condition that is wrong goes to the human.*

**Clause 1 requires the shipped prose to say the manager learns of a stop as a task-notification *"whose status reads
`stopped` rather than `completed`"*.** The worker took that from the harness's compiled source, where the emit call
reads `qg(id,"stopped",…)`. **The notification the manager actually received reads `killed`**, with the summary
*"Agent "Stop test target" was stopped by Claude"*. The full record of the run is on node 122 under `## The manager
ran Tests 1 and 2, and both pass`.

**What this does and does not touch.** Clause 1's other seven demands were verified by the test and hold, as do
clauses 2, 4 and 5 — the stop is immediate, the agent stays resumable, `stoppedByUser` is absent after a tool stop,
and the resume succeeded. Only the status word is wrong, and it is wrong in a clause that a checker would read as
satisfied only by prose repeating a false word.

**Why the manager did not fix it.** Node 122's worker wrote this condition and its own closing note fixes the
remedy: *"if Test 1 fails, clauses 1, 2 and 5 are wrong and this condition must be rewritten before the node is
claimed."* Test 1 did not fail — one detail inside clause 1 did — so the remedy the worker named does not reach it,
and widening a demand is outside [How a condition's scope is
amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s add-places-no-demands permission. **This node is
not claimed and holds no work**, so the correction is cheap for whoever is entitled to make it.

*The manager's note, 2026-09-26:* [node 123](123-who-performs-a-stop.md) resolved, and its worker reports that this node's condition is contradicted in clauses 4 and 5 and lacks two things the answer adds. It proposed a full replacement condition, filed under node 123's `INVALIDATIONS`. The manager has put that proposal to the human, because rewriting a condition is not the manager's act. This node is not started until the human answers.

## Amendment, 2026-09-26 (from node 123, by the human's answer)

*Written by [node 123](123-who-performs-a-stop.md)'s worker under its `INVALIDATIONS`, and pasted by the manager as it wrote it. The human chose to replace this node's condition with it; their words are under `## Interview`. The condition written by node 122's worker, and the manager's annotation on it, are left above as they were and are superseded by this one.*

- **The whole condition.** Replace it with:

> The work edits the files below and leaves each in the state described. The checker has the repository and reads only this text.
>
> 1. `.claude/skills/expedition/SKILL.md` gains, in its own prose, a procedure for stopping a running worker. It must say all of:
>    - that a running agent is stopped with `TaskStop`, addressed by the agent's id;
>    - that only the manager's own thread can do it, a worker that calls `TaskStop` on another agent being refused with an error naming the agent as its own owner;
>    - that the stop is an immediate abort of whatever the agent is doing, rather than a stop at its next tool round;
>    - that it also stops any agent the stopped agent had spawned;
>    - that the manager learns of it as an ordinary task-notification whose status reads `killed`;
>    - that the manager confirms the stop by watching the agent's transcript record count stop growing, rather than by trusting the success message.
> 2. The same file must say that the manager performs every stop of a worker. The human asks for one in words, naming the node, and the manager performs it with `TaskStop`. The file must not tell the human, or the manager to tell the human, to stop an agent from the task UI.
> 3. The same file must say that a worker stopped with `TaskStop` keeps its transcript and can be resumed afterwards within the manager's session, like any other stopped agent, and that this is what makes stopping a worker a cheaper act than replacing it.
> 4. The same file must say that where the human says a stopped attempt is to be final, the manager records on the node that the attempt is not to be resumed, and that no manager resumes an attempt so recorded. `.claude/skills/expedition/graph-conventions.md`, section `` ### `## Interview` ``, must say how such an attempt is marked in its own heading, beside the existing marking of a dead attempt. Whatever word the work uses for this kind of stop is defined in `CONTEXT.md`, and is not "discard", "refuse" or "abandon", which `CONTEXT.md` lists as words to avoid under **Reject**.
> 5. The same file must say that a message asking a worker to stop is not a stop:
>    - it reaches the worker as text at the end of the worker's next tool call, so a worker inside one long command is unreachable for the whole of that command;
>    - the worker may decline it, and a worker whose own instructions tell it not to stop early is the case where declining is most likely, which is the runaway case;
>    - the manager therefore does not use a message where it needs the worker to actually stop.
> 6. The same file must say that a stop performed from the human's side is a different act with one different consequence: it marks the agent as stopped by the user, and every resume the manager attempts is refused, while the human can still revive the agent by typing to it. It must also say all of:
>    - that the mark is set not only by the task UI's stop but also by rewinding the conversation past the agent's spawn, so the mark does not show that the human meant the work to be thrown away;
>    - that the manager can tell the two stops apart before attempting anything, by reading `stoppedByUser` from the agent's `.meta.json` metadata file beside its transcript;
>    - that where the mark is set, the manager neither replaces the attempt on its own nor retries the resume. It keeps the node claimed and puts one question to the human. The question names the node, says the attempt cannot be resumed by the manager, says what would be lost (the worker's own work, not the human's recorded answers), and offers two choices: the human revives the agent by typing to it, or the manager replaces the attempt and replays the human's answers.
>
>    The file must no longer tell the manager to handle such a stop by starting a fresh attempt without asking.
> 7. The same file's account of what a message to an agent reports back must cover four outcomes for an agent target, not three:
>    - alive and still working;
>    - stopped and resumed from its transcript;
>    - stopped by the user, where no resume is attempted at all and the reply says so explicitly;
>    - gone, no transcript found.
>
>    It must say that the third of these is not the fourth, and that the third leads to the question in item 6.
> 8. The pick report's instruction in the same file, that on a redirection the manager "stop or redirect what you started", must say that a stop there is performed with `TaskStop` as in item 1.
> 9. `CONTEXT.md`'s glossary gains or amends whatever entries are needed so that the words this procedure uses for the kinds of stop are defined there, and so that no entry states or implies that a running worker cannot be stopped. Superseded wording is marked as superseded and left in place rather than deleted.
> 10. Any other file under `.claude/skills/` that states or implies any of the following is brought into line with items 1–9:
>     - that the manager has no way to stop a running agent;
>     - that a message to a running agent interrupts it;
>     - that the human should stop an agent from the task UI;
>     - that an agent stopped by the user is replaced without asking the human.
>
>     The work reports the search that found them, the terms searched and the files searched, and reports any instance found outside items 1–9 rather than silently editing it or silently omitting it.
> 11. No latency, token or cost figure appears anywhere in the work as a measured quantity unless the number and what measured it are in the work's own text.
> 12. The standing bar for this repository.

## Interview

### The manager's raise, 2026-09-26

*The manager's own raise, sent after node 307's gate.* Should this node's acceptance condition be replaced by the 12-item condition node 123's worker proposed under its `INVALIDATIONS`, or kept as it is with a separate node added that uses the proposal as its condition and this node as its blocker? The manager recommended replacing it, as node 123's worker did, because this node is unclaimed and holds no work.

The human, `verbatim`: *"yes replace"* — taking the option the manager offered: *"Should this node's acceptance condition be replaced by the 12-item condition node 123's worker proposed"*.

*The manager's note, 2026-09-26:* on the human's "ok" to [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s recommendation, nodes 120, 124 and 258 merge into node 124. [Node 341](341-draft-one-condition-for-nodes-120-124-and-258.md) drafts the merged condition; this node is not started until it is filed.
