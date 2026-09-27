# Give the manager's contract a procedure for stopping a running worker

Type: implementation
Status: resolved
Supersedes: 120, 258

Blocked by: ~~123~~

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

## Amendment, 2026-09-26 (from node 341, by the human's answer)

*Written by [node 341](341-draft-one-condition-for-nodes-120-124-and-258.md)'s worker, which merged nodes 120, 124 and 258 into one condition, and pasted by the manager as it wrote it. The human took it with their "ok" to node 341's K1 to K5; their words are on node 341 under `## Interview`. It replaces this node's condition as amended from node 123 above; that amendment and the original condition are left above as they were. Nodes 120 and 258 are superseded by this node.*

- **The whole condition.** Replace it with:

> The work edits `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md` and `CONTEXT.md` at the repository root, and leaves each in the state described below. The checker has the repository and reads only this text. Another file under `.claude/skills/` changes only where clause 17's search finds an instance in it, and every such change is reported. No file under `.scratch/` changes. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. All three files are files the workflow ships, so they are edited plainly: superseded wording is removed, and nothing in them is struck through, left in place marked as superseded, or moved to a history file. *(120, 124, 258)*
>
> **Where the work may change**
>
> 1. *(120, 124, 258)* Inside the three files, the work changes only these places:
>    - in `SKILL.md`: the line under `## Words used exactly` that before this work reads "A worker is resumed in place rather than replaced."; the section `## When an agent dies or is stopped`; the sentence under `### Picking the next node` that before this work reads "You then stop or redirect what you started."; and one new section holding the stop procedure of clauses 2 to 6, where the worker does not put that procedure inside `## When an agent dies or is stopped`;
>    - in `graph-conventions.md`: the section `` ### `## Interview` ``;
>    - in `CONTEXT.md`: the entry headed `**Attempt**:`, and the entries clause 15 adds or amends.
>
>    Inside `## When an agent dies or is stopped`, the paragraph that before this work begins "After two replacements, treat a third failure as evidence that the node is too large." keeps its meaning. The work adds nothing that says whether a resume counts toward those two replacements.
>
> **Stopping a running worker**
>
> 2. *(124)* `SKILL.md` gains, in its own prose, a procedure for stopping a running worker. It says all of:
>    - a running agent is stopped with `TaskStop`, addressed by the agent's id;
>    - only the manager's own thread can do it, and a worker that calls `TaskStop` on another agent is refused with an error naming the agent as its own owner;
>    - the stop is an immediate abort of whatever the agent is doing, not a stop at its next tool round;
>    - it also stops any agent the stopped agent had spawned;
>    - the manager learns of it as an ordinary task-notification whose status reads `killed`;
>    - the manager confirms the stop by watching the agent's transcript record count stop growing, and does not trust the success message for it.
> 3. *(124)* The file says that the manager performs every stop of a worker. The human asks for one in words, naming the node, and the manager performs it with `TaskStop`. The file does not tell the human to stop an agent from the task UI, and does not tell the manager to tell the human to do so.
> 4. *(124)* The file says that a worker stopped with `TaskStop` keeps its transcript and can be resumed afterwards within the manager's session, like any other stopped agent, and that this is what makes stopping a worker cheaper than replacing it.
> 5. *(124)* The file says that where the human says a stopped attempt is to be final, the manager records on the node that the attempt is not to be resumed, and that no manager resumes an attempt recorded that way. Whatever word the work uses for this kind of stop is defined in `CONTEXT.md`. The word is not "discard", "refuse" or "abandon", which `CONTEXT.md` lists as words to avoid under **Reject**.
> 6. *(124)* The file says that a message asking a worker to stop is not a stop:
>    - it reaches the worker as text at the end of the worker's next tool call, so a worker inside one long command cannot be reached for the whole of that command;
>    - the worker may decline it. Declining is most likely when the worker's own instructions tell it not to stop early, which is the runaway case;
>    - so the manager does not use a message where it needs the worker to actually stop.
> 7. *(124)* The sentence under `### Picking the next node` that before this work reads "You then stop or redirect what you started." says that a stop there is performed with `TaskStop`, as in clause 2.
>
> **Resuming an agent that stopped**
>
> 8. *(120)* `## When an agent dies or is stopped` says, in its own prose, all of:
>    - an agent that stopped before handing back, whether by a harness error or a usage quota (it died) or by a stop, is not gone for that reason. Its attempt is resumed, not replaced, wherever the manager can resume it. Replacement is the fallback where the resume fails, with one exception, in clause 10: an attempt whose agent was stopped from the human's side is never replaced without the human's answer;
>    - the manager finds out whether a resume is possible by attempting it and acting on what the harness answers (the outcomes in clause 11), and never decides in advance. A failed resume starts no agent and costs nothing, so possibility is tested and never predicted;
>    - resumability is limited to the manager's own session. An attempt spawned in the current session can be resumed, except one whose agent carries the mark described in clause 10. No attempt from an earlier session can be resumed at all, even though its transcript still exists on disk;
>    - a dead run's state is read from its transcript's record count and byte size, and never from the one-line summary the harness shows as its result;
>    - a dead run's cause of death is the last record of its own transcript. Where that cause is a usage quota, that record names the time the quota resets;
>    - where the cause is a shared usage quota, the manager waits for the stated reset and then resumes. No replacement can run in that window either, so waiting loses nothing that replacing would gain;
>    - where a live run has already overtaken a dead one, measured in transcript records, the live run finishes and the dead one is held as the fallback.
> 9. *(120)* The same section says that the resume rule covers the checker. A checker is resumed to continue or revise a check it is still conducting, including a re-check after a correction round. It is spawned fresh only where the purpose is a check independent of a verdict already delivered. The section says that a resumed re-check establishes again that no standard the work is held against moved under the check. The words "second opinion" are not used for the fresh check, because `CONTEXT.md`'s **Checker** entry says the checker "is not a second opinion".
> 10. *(124)* The file says that a stop performed from the human's side is a different act, with one different consequence: it marks the agent as stopped by the user, and every resume the manager attempts is refused, while the human can still revive the agent by typing to it. It also says all of:
>     - the mark is set not only by the task UI's stop but also by rewinding the conversation past the agent's spawn, so the mark does not show that the human meant the work to be thrown away;
>     - the manager can tell the two stops apart before attempting anything, by reading `stoppedByUser` from the agent's `.meta.json` metadata file beside its transcript;
>     - where the mark is set, the manager does not replace the attempt on its own and does not retry the resume. It keeps the node claimed and puts one question to the human. The question names the node and says the manager cannot resume the attempt. It says what would be lost: the worker's own work, not the human's recorded answers. It offers two choices: the human revives the agent by typing to it, or the manager replaces the attempt and replays the human's answers.
>
>     The sentence that before this work reads "Handle a stop by starting a fresh attempt, never by re-prompting the stopped agent." is gone. Nothing in the file tells the manager to handle a stop from the human's side by starting a fresh attempt without asking.
> 11. *(124)* The file's account of what a message to an agent reports back covers four outcomes for an agent target, not three:
>     - alive and still working;
>     - stopped and resumed from its transcript;
>     - stopped by the user, where no resume is attempted at all and the reply says so explicitly;
>     - gone, no transcript found.
>
>     It says that the third of these is not the fourth, and that the third leads to the question in clause 10. The sentence that before this work reads "An agent that fails to resume is gone." no longer says that every failed resume means the agent is gone.
> 12. *(258)* The line under `## Words used exactly` that before this work reads "A worker is resumed in place rather than replaced." says instead three things: a dead attempt is resumed where the manager can resume it and replaced only where it cannot; an attempt stopped from the human's side is replaced only on the human's answer; and a replacement is a new attempt, recorded after the one it replaces.
>
> **The record of an attempt**
>
> 13. *(120, 124)* In `graph-conventions.md`, the section `` ### `## Interview` ``, which before this work says "A dead attempt is marked in its own heading. A node holds at most three attempt blocks.", says all of:
>     - *(120)* an attempt whose agent died and did not continue is marked in its own heading, as before. Its entry carries the dead run's transcript record count and its cause of death as the harness stated it;
>     - *(120)* an attempt whose agent died and was resumed is recorded as the same attempt continuing, not as a new attempt block. Its block carries the same two facts about the death. So no resume counts toward the limit of three attempt blocks;
>     - *(124)* how an attempt the human said is final is marked in its own heading, beside the marking of a dead attempt.
>
> **The glossary**
>
> 14. *(120, 258)* In `CONTEXT.md`, the entry headed `**Attempt**:`, which before this work reads "One worker instance on one node. A node lasts longer than any of its attempts: a worker that dies is replaced, and the replacement is a new attempt.", no longer says that a worker that dies is replaced. It says that a worker that dies is resumed where the manager can resume it and replaced only where it cannot, that one stopped from the human's side is replaced only on the human's answer, and that a replacement is a new attempt.
> 15. *(124)* `CONTEXT.md` gains or amends whatever entries are needed so that the words the procedure uses for the kinds of stop are defined there, including the final stop of clause 5, and so that no entry says or implies that a running worker cannot be stopped.
>
> **Across the files**
>
> 16. *(258)* No statement anywhere in `SKILL.md` or `CONTEXT.md` says that a dead worker is replaced without saying that resuming is tried first. The two files do not contradict each other on whether a dead worker is resumed or replaced.
> 17. *(120, 124)* Any other file under `.claude/skills/` that states or implies any of the following is brought into line with clauses 2 to 16:
>     - that a dead worker or a dead checker is replaced, respawned, or given a replayed transcript as the first recovery tried;
>     - that the manager has no way to stop a running agent;
>     - that a message to a running agent interrupts it;
>     - that the human should stop an agent from the task UI;
>     - that an agent stopped by the user is replaced without asking the human.
>
>     The work reports the search that found them: the terms searched and the files searched. It reports any instance found outside the places clauses 1 to 16 name, and neither edits it silently nor leaves it out silently. The following statements are true before this work and need no change under this clause:
>     - `.claude/skills/expedition-stop/SKILL.md`'s section `## Agents still running when the session ends`, which says an attempt still running when the manager's session ends is replaced;
>     - `.claude/skills/expedition-grilling/SKILL.md`'s "A worker that replaces you is a new attempt.";
>     - the section `## If you are a replacement attempt` in the grilling, implementation, precondition and prototype contracts.
>
>     Where the work renames `## When an agent dies or is stopped`, the reference to that heading in `.claude/skills/expedition-stop/SKILL.md` is updated to the new heading.
> 18. *(120, 124)* No latency, token or cost figure appears anywhere in the work as a measured quantity unless the number, and what measured it, are in the work's own text.
> 19. *(120, 124, 258)* The standing bar for this repository.

## Answer

The manager stops a worker only with `TaskStop`, never by message; a stopped or dead attempt is resumed first, and a stop from the human's side goes to the human.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `d3b1a14`. Flags 124.1 to 124.3 are settled at this gate.

## Interview

### The manager's raise, 2026-09-26

*The manager's own raise, sent after node 307's gate.* Should this node's acceptance condition be replaced by the 12-item condition node 123's worker proposed under its `INVALIDATIONS`, or kept as it is with a separate node added that uses the proposal as its condition and this node as its blocker? The manager recommended replacing it, as node 123's worker did, because this node is unclaimed and holds no work.

The human, `verbatim`: *"yes replace"* — taking the option the manager offered: *"Should this node's acceptance condition be replaced by the 12-item condition node 123's worker proposed"*.

*The manager's note, 2026-09-26:* on the human's "ok" to [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s recommendation, nodes 120, 124 and 258 merge into node 124. [Node 341](341-draft-one-condition-for-nodes-120-124-and-258.md) drafts the merged condition; this node is not started until it is filed.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Give the manager's contract a procedure for stopping a running worker (node 124, merging 120 and 258)

ANSWER:
**The manager's contract now says how to stop a running worker, and it resumes a stopped or dead agent before it replaces one.** This work meets the condition from node 341's amendment. It is uncommitted in `.scratch/graph-workflow/worktrees/124-stop`, on branch `worktree-124-stop`, and touches three files: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md` and `CONTEXT.md`.

What was built, file by file:

- **`SKILL.md`, new section `## Stopping a running worker`**, placed just before `## When an agent dies or is stopped`:
  - The manager performs every stop. The human asks for one in words, naming the node. The section never tells the human to use the task UI's stop.
  - Five numbered steps:
    1. `TaskStop`, addressed by the agent's id. Only the manager's own thread can do it, and a worker trying it on another agent is refused with an error naming that agent as its own owner.
    2. The stop aborts at once, not at the next tool round, and it also stops every agent the stopped agent had spawned.
    3. The manager learns of it from a task-notification whose status reads `killed`.
    4. The manager confirms it by watching the transcript's record count stop growing, and does not trust the success message.
    5. A final stop is recorded on the node, and no manager resumes that attempt.
  - Three paragraphs follow:
    - A stopped worker keeps its transcript and can be resumed in the same session. That is why stopping costs less than replacing.
    - A message asking a worker to stop is not a stop. It arrives late and the worker may decline it, most likely when the worker is looping without end.
    - A stop from the human's side sets `stoppedByUser`, which is read from the agent's `.meta.json` beside its transcript. The task UI's stop sets it, and so does rewinding the conversation past the agent's spawn. So the mark does not show that the human meant the work to be thrown away.
- **`SKILL.md`, `## When an agent dies or is stopped`, rewritten.** The heading is unchanged, so `expedition-stop`'s reference to it still holds. The section now says:
  - A stopped or dead agent is resumed first. Replacement is the fallback, with one exception: a stop from the human's side is never replaced without the human's answer. An attempt recorded as a final stop is never resumed.
  - Whether a resume is possible is found out by trying it, never predicted. Resuming only works within the current session.
  - A message to an agent has four outcomes. The third (stopped by the user) is not the fourth (gone), and the third leads to a single question to the human with two choices: the human revives the agent by typing to it, or the manager replaces the attempt and replays the human's answers.
  - A dead agent's state is read from its transcript's record count and byte size, and its cause of death from its last record. On a shared quota the manager waits for the reset. Where a replacement has already overtaken the dead attempt, the replacement finishes.
  - The checker is resumed for a re-check. A fresh checker is spawned only for a check independent of a verdict already given.
  - The replacement paragraphs are kept, now opening "Where you replace an attempt". The paragraph "After two replacements…" is unchanged, and nothing says whether a resume counts toward those two.
- **`SKILL.md`, two single lines:**
  - Under `## Words used exactly`, the old line "A worker is resumed in place rather than replaced." now says three things: resume where possible, a stop from the human's side is replaced only on the human's answer, and a replacement is a new attempt recorded after the old one.
  - Under `### Picking the next node`, the sentence about stopping what was started now says the stop is done with `TaskStop`.
- **`graph-conventions.md`, `` ### `## Interview` ``:**
  - A dead attempt is marked `dead` in its heading and carries its record count and cause of death.
  - A resumed attempt continues the same block, so no resume counts toward the limit of three blocks.
  - An attempt the human said is final is marked `final stop` in its heading.
- **`CONTEXT.md`:**
  - `**Attempt**:` is rewritten: resume where possible, a stop from the human's side is replaced only on the human's answer, and a replacement is a new attempt.
  - New entry `**Stop**:`, with `_Avoid_: kill, cancel`.
  - New entry `**Final stop**:`.

Calls a later reader would otherwise have to re-derive:
- **The word for the human's final stop is "final stop".** It avoids the three words `CONTEXT.md` refuses under **Reject** (discard, refuse, abandon).
- **The condition's "runaway" became "looping without end", and its "dead run" and "live run" became "dead agent", "dead attempt" and "a replacement already working".** "Runaway" is a figure of speech, which writing rule 5 forbids. `run` is refused under **Attempt**.
- **"moved under the check" became "has changed since the checker last read it"**, which is plain wording for the same meaning.
- **The mark for a dead attempt was made the literal word `dead`.** The earlier text said only "marked in its own heading" and named no word, and no node file in the record uses one.
- **The cases where a stop is needed (redirected node, off-contract worker, looping worker, replacement made unnecessary) are listed as cases where the human may ask.** They are not listed as the manager's own authority, which follows node 123's "at the human's word".

INDEX LINE:    The manager stops a worker only with `TaskStop`, never by message; a stopped or dead attempt is resumed first, and a stop from the human's side goes to the human.

FLAGS:
- ASSUMPTION: On node: I named the kind of stop the human says is final a "final stop". I defined it in `CONTEXT.md`, and made the heading marks for `## Interview` the literal words `final stop` and `dead`. The condition left the word to the work and ruled out discard, refuse and abandon. The earlier text marked a dead attempt "in its own heading" with no word, and no node file uses one, so giving both marks a literal word was an extension I chose. Index: The final stop and the dead attempt got the literal heading marks `final stop` and `dead`, where the condition fixed no word for either.
- ASSUMPTION: On node: I did not say what happens to a node's work after a final stop, beyond "no manager resumes it". The condition demands only that. Node 123 said nothing about whether such a node gets a new attempt. So a manager meeting a final stop with no instruction about the node has no rule for whether to replace it. Index: After a final stop the contract says only that the attempt is never resumed, not whether the node gets a new attempt.
- ASSUMPTION: On node: the new **Stop** glossary entry says "a message asking a worker to stop is not a stop". But `CONTEXT.md`'s **Raise** entry ("Its answer either continues that worker or stops it") and graph-conventions' `### Park` step 1 ("Tell the worker to store its progress and stop") use "stop" for a message to a worker that is waiting, not running. I read those as not contradicting the new entry, because the entry is about a running worker, and I left both alone because both are outside the places the condition lets me change. Index: "Stop" now names ending a running worker, while the Raise entry and the Park step still use it for a message to a waiting worker; left unedited.

NEW NODES:     none

INVALIDATIONS:
- Node 08 (Relay protocol): its index line says death is "recovered by replaying an at-relay-time log… capped at two respawns". That is narrowed: recovery is now a resume first, and replay only where the resume fails or on the human's answer.
- Node 119 (resume a dead attempt): extended. Its rule, resume whenever the harness allows and test rather than predict, is now in the shipped contract, together with the fourth outcome (stopped by the user).
- Node 122 (what can stop a running worker): its original condition's status word `stopped` is contradicted, and the shipped text says `killed`. The manager's annotation on node 124 already records this.
- Node 123 (who performs a stop): carried out as written. Its "stop and discard" wording is replaced by the term "final stop".
- Nodes 120 and 258: carried out, as the condition merged them.

CONDITIONS:    I searched the `## Acceptance condition` sections, amendments included, of all 84 open and claimed nodes for:
- the phrases this work removes or replaces: "resumed in place", "fresh attempt", "fails to resume", "worker that dies", "stop or redirect", "dead attempt", "re-prompting", "replaced without";
- the headings and sections it touches: "dies or is stopped", "Stopping a running", "three attempt", "attempt block", `**Attempt**`;
- the new or harness terms: "task UI", "task panel", `TaskStop`, `stoppedByUser`, "killed", "final stop", "stop from the human", "resum".

Matches outside node 124: nodes 256, 221, 342 and 160. Each matched only on ordinary uses of "resume" (the order of acts, a resumed worker, a `STANDING YES` resume, a worker resumed to rebase), and this work makes none of them wrong. No replacement clause was written.

Clause 17's search of the shipped files covered every file under `.claude/skills/` (the 8 skill directories plus `wayfinder-divergences.md`) and `CONTEXT.md`. Terms searched: respawn, replay, fresh, replac, resum, TaskStop, task UI, task panel, stopped by, stoppedByUser, interrupt, dies, died, dead, cannot be stopped, no way to stop, and then stop, kill, cancel, abort, halt. Instances found outside clauses 1 to 16, none edited:
- `expedition-stop/SKILL.md`, `## Agents still running when the session ends`: true, as the condition says. I did not rename the heading it cites, so no update was needed.
- `expedition-grilling/SKILL.md`, "A worker that replaces you is a new attempt.", and the `## If you are a replacement attempt` sections: true, as the condition says.
- `graph-conventions.md`, `### Park` step 1, "Tell the worker to store its progress and stop.": a message to a waiting worker at a park. Not an instance of any listed claim, and outside the section I may edit. See the third flag.
- `CONTEXT.md`, **Raise**, "Its answer either continues that worker or stops it": the same. See the third flag.
- `.claude/skills/expedition/SKILL.md` line 271, "instead of sending it back or respawning": this is about an unfileable handover, not a dead worker. Not an instance.

Nothing found says the manager has no way to stop an agent, that a message interrupts, that the human should use the task UI, or that a user-stopped agent is replaced without asking.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet, as no check has run.
- Paths touched, all in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/124-stop`: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, `CONTEXT.md`. Nothing else was touched, and nothing under `.scratch/`.
- The bar: I confirmed against the repo that it has no build, no tests, no formatter and no CI. The root holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`. This matches `map-implementation-rules.md`, so the bar is its non-command half. `git diff --check` is clean. Each file keeps its wrap width (about 104 columns, 102 for `CONTEXT.md`), and no added line exceeds it.
- No latency, token or cost figure appears in the work.
- Overlap with node 340: I stayed out of `## The node file`'s annotation material and out of any hard-rule text. The only `graph-conventions.md` change is inside `` ### `## Interview` ``, and I added no procedure, so node 339's check-step rule is not triggered.
- Proposed commit message:

  Give the manager's contract a procedure for stopping a running worker, and resume before replacing

  Adds `## Stopping a running worker` to the manager contract (TaskStop only, a message is not a stop, the human's own stop and `stoppedByUser`), rewrites `## When an agent dies or is stopped` so it resumes before it replaces, with four outcomes of a message and the question the human's stop leads to, marks dead and final-stop attempts in `## Interview`, and adds **Stop** and **Final stop** to the glossary.

  Node: graph-workflow/124

RETROSPECTIVE
1. What I had to hunt for:
   - The word for the final stop. The condition left it open, so I searched node 123, which was the only place that said it was deliberately left to the glossary.
   - Whether any node file already uses a word to mark a dead attempt in its heading. I grepped the node headings, and none does.
   - Whether the manager may stop a worker on its own authority. Node 123's `## Answer` says "at the human's word".
2. What arrived that this node did not need:
   - Most of `map.md`: about 40KB, of which only the resume standing preference (the one headed "An agent is resumed wherever it can be resumed") bore on this node.
   - The two superseded conditions in the node file, about 130 lines, which I read only to skip them.
   - The retrospective, worktree and token-priority preferences in `map.md`.
3. What would have made this easier:
   - The spawn, or the amendment itself, saying up front that the word for the final stop is the worker's to choose, and that "runaway", "dead run" and "live run" collide with writing rule 5 and with **Attempt**'s refusal of `run`.
   - A node file whose superseded conditions are folded or moved below the condition in force.
4. What was stale, wrong or contradictory:
   - Clause 8 of the condition uses "dead run" and "live run", although `CONTEXT.md` refuses `run` for an attempt.
   - Clause 9's "moved under the check" is a figure of speech.
   - The node file's header still reads `Blocked by: 123`, and its `## Question` note says the header carries `Blocked by: 123, 120`. Node 120 is now superseded by this node.
   - The manager's notes were accurate: `## When an agent dies or is stopped` had been left untouched by node 337.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 337's check; the condition reached it as a verbatim copy in `$TMPDIR/m124.md`, which the message told it to read whole.*

> PASS
>
> This is my check of node 124, "Give the manager's contract a procedure for stopping a running worker". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/124-stop`, on base 3c25240. It touches three files:
> - `.claude/skills/expedition/SKILL.md` (+103)
> - `.claude/skills/expedition/graph-conventions.md` (+15)
> - `CONTEXT.md` (+19)
>
> For the searches below, I first joined each paragraph of SKILL.md and CONTEXT.md onto one line with awk, then ran `grep -noiE` over the result. Two parts could not be checked from the files I hold; they are listed under NOT COVERED.
>
> **Parts of the condition**
>
> - **Scope:** met.
>   - `git status --short` shows exactly the three files. Nothing under `.scratch/` changed, and no node file, `decisions.md` or `flags.md` changed.
>   - No other file under `.claude/skills/` changed; clause 17 finds no instance that would call for one.
>   - Superseded wording is removed plainly, with nothing struck through or marked.
> - **1:** met.
>   - SKILL.md hunks fall only in these places: the `## Words used exactly` line, the `### Picking the next node` sentence, the new `## Stopping a running worker` section (placed outside `## When an agent dies or is stopped`), and that section itself.
>   - graph-conventions.md changes only in `` ### `## Interview` ``.
>   - CONTEXT.md changes only in `**Attempt**:`, plus two new entries, `**Stop**:` and `**Final stop**:`.
>   - The paragraph "After two replacements, treat a third failure…" is unchanged; it is a context line in the diff.
>   - Nothing in SKILL.md says whether a resume counts toward those two replacements. graph-conventions.md says "no resume counts toward the limit of three attempt blocks", which is clause 13's own demand and about a different limit.
> - **2:** met. The steps of `## Stopping a running worker` state:
>   - `TaskStop` is addressed by the agent's id;
>   - only the manager's own thread can stop an agent, and another caller gets an error "naming that agent as its own owner";
>   - the stop "aborts whatever the agent is doing at once. It does not wait for the agent's next tool round";
>   - it "also stops every agent the stopped agent had spawned";
>   - the manager learns of it by a task-notification with status `killed`;
>   - the stop is confirmed by the transcript's record count, and "The success message … does not confirm it."
> - **3:** met. The section says "You perform every stop of a worker. The human asks for one in words, naming the node, and you perform it with `TaskStop`." It also says "Never tell the human to stop an agent from the task UI." Nothing tells the human to stop an agent themselves.
> - **4:** met. A stopped worker "keeps its transcript. It can be resumed afterwards within your session, like any other stopped agent. That is what makes stopping a worker cheaper than replacing it".
> - **5:** met.
>   - Step 5 says a final stop is recorded on the node, and "No manager resumes an attempt recorded that way."
>   - `**Final stop**:` is defined in CONTEXT.md.
>   - A grep for `discard|refuse|abandon` finds none of those words used as the name for this stop.
> - **6:** met. The message paragraph covers all three sub-demands:
>   - a message is not a stop;
>   - it arrives "at the end of the worker's next tool call", so a worker inside one long command cannot be reached;
>   - the worker may decline it, most likely when its instructions forbid stopping early;
>   - "where you need a worker to actually stop, use `TaskStop`, and never a message."
> - **7:** met. The sentence now reads "…stop or redirect what you started, and you perform such a stop with `TaskStop`, as `## Stopping a running worker` says."
> - **8:** met. All seven bullets are in `## When an agent dies or is stopped`:
>   - an agent that stopped is not gone for that reason: resume it, with replacement as the fallback, except a stop from the human's side;
>   - whether a resume is possible is found by attempting it; a failed resume starts no agent and costs nothing;
>   - resuming is limited to the current session, excluding an agent marked by the human's stop and anything from an earlier session;
>   - a dead agent's state is read from its record count and byte size, never from the one-line summary;
>   - the cause of death is the transcript's last record, and a quota record names the reset time;
>   - for a shared quota, wait for the reset, then resume;
>   - where a replacement has already overtaken the dead attempt, let it finish and hold the dead attempt as the fallback.
> - **9:** met.
>   - The paragraph says "The resume rule covers the checker": resume a checker to continue or revise a check, including a re-check after a correction round, and spawn a fresh checker only for a check independent of a verdict already delivered.
>   - It says a resumed re-check establishes again that no standard moved.
>   - A grep for `second opinion` over SKILL.md finds nothing; the only hit in the two files is CONTEXT.md's existing **Checker** entry.
> - **10:** met.
>   - The paragraph on the human's stop covers: the mark; every resume refused; the human can revive by typing; the task UI stop and rewinding past the spawn both set the mark, "So the mark does not show that the human meant the work to be thrown away"; and reading `stoppedByUser` from `.meta.json` beside the transcript.
>   - Where the mark is set: do not replace on your own, do not retry, keep the node claimed, and ask one question. The question names the node, says what would be lost (the worker's work, not the recorded answers) and offers the two choices.
>   - "Handle a stop by starting a fresh attempt…" is gone.
>   - The grep for `replac|respawn|fresh (agent|attempt|checker)` finds no instruction to replace an attempt stopped from the human's side without asking.
> - **11:** met.
>   - The file lists four outcomes: alive; stopped and resumed; stopped by the user, where no resume is attempted and the reply says so; and gone, with no transcript.
>   - It says "The third outcome is not the fourth", and that the third leads to the question.
>   - "An agent that fails to resume is gone." is replaced by "Where a resume fails for any other reason, the agent is gone".
>   - A grep for `outcomes` finds no other account of what a message reports back.
> - **12:** met. The words line gives all three statements: resume where possible and replace otherwise; a stop from the human's side is replaced only on the human's answer; a replacement is a new attempt, recorded after the one it replaces.
> - **13:** met. `` ### `## Interview` `` gains three bullets:
>   - a dead attempt that did not continue is marked `dead` in its heading, with its record count and its cause as the harness stated it;
>   - a dead attempt that was resumed is the same attempt continuing, not a new block, carries the same two facts, and no resume counts toward the three blocks;
>   - a final stop is marked `final stop` in its heading, beside `dead`.
> - **14:** met. `**Attempt**:` now says a worker that dies is resumed where possible and replaced only where not, a worker stopped from the human's side is replaced only on the human's answer, and a replacement is a new attempt.
> - **15:** met.
>   - `**Stop**:` and `**Final stop**:` define the words the procedure uses.
>   - `grep -noiE 'cannot be stopped|can.t be stopped|no way to stop|interrupt'` finds nothing about stopping a worker. Its only hits are the existing "does not interrupt the human" and a raise's `_Avoid_` line.
> - **16:** met. Every replacement statement in SKILL.md and CONTEXT.md is either conditioned on the resume failing or is about something else, such as supersession replacements or condition "replacement" clauses. The two files agree.
> - **17:** met, apart from the reporting part (see NOT COVERED).
>   - I searched every other `.md` file under `.claude/skills/` for `replac|respawn|replay|died|dies|dead|TaskStop|interrupt|task UI|stopped by the user|stop (an|the|a) (agent|worker)|cannot stop|no way to stop`, with paragraphs joined.
>   - The only relevant hits are the three statements the condition excepts: expedition-stop's `## Agents still running when the session ends`; grilling's "A worker that replaces you is a new attempt."; and the `## If you are a replacement attempt` headings.
>   - The heading `## When an agent dies or is stopped` is not renamed, so expedition-stop's reference to it still resolves.
> - **18:** met. Listing every token with a digit in the added lines returns only list-item numbers. No latency, token or cost figure appears.
> - **19:** met. See the bar below.
>
> **The bar**
>
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean, exit 0.
> - No added line exceeds the files' wrap width.
>
> **Standards**
>
> As in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
>
> - **CONTEXT.md `_Avoid_` lines:** checked by hand on the added text.
>   - The **Attempt** entry avoids "retry, run, session" as names for an attempt. The added text uses "retry" only as a verb about a resume, a wording the old text already had, and "session" only for the manager's own session, which the condition itself uses.
>   - `killed` appears only in code, as the harness's status word, which the new **Stop** entry's `_Avoid_: kill` explains.
> - **Writing rules:** citations are by heading, and every "never" has its positive instruction beside it.
> - **`/writing-for-agents`:** nothing found.
> - **Ground rules:**
>   - `TaskStop`, `.meta.json` and `stoppedByUser` are harness-specific, but clauses 2 and 10 require them word for word, so I did not count them against ground rule 1.
>   - Nothing tells a spawned agent to address the human.
> - **`/coding-principles` and `/naming`:** did not bear on the work, since it is prose.
> - **Reviewing skill:** none is named, so I ran none.
> - **Standards moved by the work:** graph-conventions.md is part of the work, and the change touches no element I hold the work against.
>
> The condition records no search command with a return, so there was nothing to re-run. Clause 17's search belongs to the worker's report.
>
> NOT COVERED:
> - Clause 17's "The work reports the search that found them: the terms searched and the files searched. It reports any instance found…". That report is handed back by the worker, not held in the working tree, so it is outside what I was given. My own search is described under clause 17 above.
> - "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

*The manager's note:* on the first NOT COVERED item, the worker's `CONDITIONS` part reports clause 17's search: the terms, the files, and the instances found.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*

## Flags

`124.1` `ASSUMPTION` **· settled** — I named the kind of stop the human says is final a "final stop". I defined it in `CONTEXT.md`, and made the heading marks for `## Interview` the literal words `final stop` and `dead`. The condition left the word to the work and ruled out discard, refuse and abandon. The earlier text marked a dead attempt "in its own heading" with no word, and no node file uses one, so giving both marks a literal word was an extension I chose. — The final stop and the dead attempt got the literal heading marks `final stop` and `dead`, where the condition fixed no word for either.

`124.2` `ASSUMPTION` **· settled** — I did not say what happens to a node's work after a final stop, beyond "no manager resumes it". The condition demands only that. Node 123 said nothing about whether such a node gets a new attempt. So a manager meeting a final stop with no instruction about the node has no rule for whether to replace it. — After a final stop the contract says only that the attempt is never resumed, not whether the node gets a new attempt.

`124.3` `ASSUMPTION` **· settled** — the new **Stop** glossary entry says "a message asking a worker to stop is not a stop". But `CONTEXT.md`'s **Raise** entry ("Its answer either continues that worker or stops it") and graph-conventions' `### Park` step 1 ("Tell the worker to store its progress and stop") use "stop" for a message to a worker that is waiting, not running. I read those as not contradicting the new entry, because the entry is about a running worker, and I left both alone because both are outside the places the condition lets me change. — "Stop" now names ending a running worker, while the Raise entry and the Park step still use it for a message to a waiting worker; left unedited.
