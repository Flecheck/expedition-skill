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
