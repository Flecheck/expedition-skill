# Who performs a stop, and what the human's own stop destroys

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [What can actually stop a running worker](122-what-can-stop-a-running-worker.md)'s worker, and pasted as
it wrote it.*

> Two stops exist and they differ in one consequence. A stop the manager issues with `TaskStop` leaves the agent
> resumable from its transcript. A stop the human issues from the task UI sets a persisted `stoppedByUser` flag that
> refuses every agent-initiated resume for ever, so for that agent the map's standing rule — *"Whenever it can be
> resumed, resume I think"* — is dead, and only the human typing to the agent can revive it. Two agents on this
> project are already in that state, one of them a checker holding 65 records and 483,376 bytes of work, and nothing
> in the graph records either as human-stopped. So: when a worker must be abandoned, who should perform the stop?
> Should the human's own stop be reserved for work that is genuinely to be discarded, with a redirection or a runaway
> routed to the manager instead? Does the manager owe the human a line, at the moment it reports a worker as running,
> saying which of the two they are choosing between? And is there a case where the human wants a worker gone
> permanently and unrevivably, which is the one thing the manager's stop cannot give them?

**Blockers, in the worker's words:** *"Node 122 resolved. **Sharper if the manager has run node 122's Test 1
first**, since the human's answer is worth less if the manager's stop turns out not to work at all."*

## The manager's note at filing

*Not a change to anything above.*

**Both of this node's preconditions are met.** Node 122 is resolved, and **the manager has run Test 1 and Test 2 and
both passed** — the manager's stop works and leaves the agent resumable, recorded on node 122 under `## The manager
ran Tests 1 and 2, and both pass`. So the worker's *"worth less"* case does not arise: the two stops really do
differ in exactly the consequence this node asks about.

## Answer

The manager performs every stop of a worker with `TaskStop`, at the human's word. A worker found stopped by the human is not replaced silently: the human chooses between reviving it and a replacement.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human's answers are under `## Interview`. The worker proposed a replacement acceptance condition for [node 124](124-a-procedure-for-stopping-a-running-worker.md); that goes to the human as the manager's own raise.

## Interview

### Attempt 1

**Q1–Q3, from the worker**, pasted as it wrote them, 2026-09-26. **Held, not yet put to the human**: they arrived while [node 257](257-whether-a-finished-gate-may-jump-an-older-question.md)'s question was in front of the human, with the gates of nodes 319 and 302 queued ahead of them.

```
NODE:          Who performs a stop, and what the human's own stop destroys (node 123)
ABOUT:         There are two ways to stop a running worker, and they leave it in different states. This node decides who stops a worker when one has to be abandoned, what the manager does when it finds a worker the human stopped, and whether the human gets a reminder. It is decided now because node 124 (writing the stop procedure into the manager's contract) is waiting on this node.
SO FAR:        What I read: node 123 and node 122, the resume rule in map.md, the stop and resume lines in decisions.md, node 124's acceptance condition, and the shipped files on master. I also read the harness's compiled source myself, in the version installed now (Claude Code 2.1.280). Node 122 read an older one, 2.1.238.
               - The manager's stop (the `TaskStop` tool, run from the manager's own thread) aborts the worker at once. The manager tested it at node 122: the worker was stopped and could still be resumed from its transcript afterwards. This is "stop now, keep the work", but only until the manager's session ends. Resumability ends with the session anyway.
               - A stop from the human's side stamps a `stoppedByUser` flag on the agent and saves that flag to disk. After that, every resume the manager attempts is refused. The harness's own refusal text says: "Treat its work as cancelled; only launch a new agent if the user explicitly asks." The human can still revive the agent by typing to it, which clears the flag. So even the human's stop is not permanent. It only locks the manager out.
               - New from the 2.1.280 source: the stop button in the task panel is not the only thing that sets the flag. Two other actions set it too. Rewinding the conversation stops every agent spawned after the point you rewind to, with the flag set (function `Lh`, which calls `mZ` and then `_Y`, which sets `stoppedByUser:true` and saves it). Interrupt sweeps in SDK and remote mode, and the `--max-budget-usd` halt, do the same. The `ctrl+x ctrl+k` chord, pressed twice ("stop background agents"), stops all background agents, but I did not trace whether it sets the flag. I did not establish whether a plain Esc in the terminal does. So the flag does not record why an agent was stopped. It can come from a deliberate discard, a rewind, or a sweep of all agents.
               - What the shipped files say now. `.claude/skills/expedition/SKILL.md`, section `## When an agent dies or is stopped`, says: "An agent the human stopped cannot be resumed either. Handle a stop by starting a fresh attempt, never by re-prompting the stopped agent." That section says nothing about the manager stopping anything. The pick-report text says only "You then stop or redirect what you started." `expedition-stop/SKILL.md` is about closing the manager's session and does not cover stopping a worker. Node 124's draft condition (clause 4) has the manager replace a human-stopped attempt automatically. That contradicts the harness's own advice above.
               - Settled on my own authority: the node's question 4 asks whether the human ever wants a worker gone "permanently and unrevivably". Neither stop gives that, as the facts above show. So I have folded it into Q1 as "discard is said in words and written in the record."

Q1. Who performs a stop
ASK:           When a worker has to be abandoned (you redirect a node, it goes off-contract, it runs away, or it is made redundant), who stops it?
RECOMMENDED:   You tell the manager in one line ("stop node N", or "stop and discard node N"), and the manager stops it with `TaskStop`. A plain stop keeps the worker resumable. A discard is also written onto the node as a discarded attempt, so no manager ever resumes it. You don't use the task-panel stop at all. Grounds: the manager's stop loses nothing it doesn't have to. Your stop blocks resumes, which the map's rule "Whenever it can be resumed, resume I think" relies on. Your stop also leaves no trace in the record. And a discard needs a line in the record anyway, whoever performs the stop, because a later manager must know not to revive it.
ALTERNATIVES:  - Use your task-panel stop for true discards and send everything else through the manager. The catch: your stop still leaves no mark in the record, and you can undo it yourself by typing to the agent, so it is not really final.
               - Leave the route unspecified and let either party stop. That is the current state, and it has already left two human-stopped agents on this project that the record does not know about.

---

Q2. What the manager does when it finds a worker the human stopped
ASK:           When a resume is refused because the agent carries the human-stop flag, what does the manager do?
RECOMMENDED:   The manager does not replace it on its own. It keeps the node claimed and puts one question to you. The question names the node, says the manager cannot resume that attempt, and says what would be lost: the worker's own investigation, not your answers, which are already recorded. It then offers two choices: you revive the agent by typing to it, which keeps its work, or the manager replaces it and replays your answers. Grounds: the flag does not record why the agent was stopped, since a rewind or a stop-all sweep sets it the same way a deliberate stop does. The harness itself says to relaunch only if you explicitly ask. The shipped text "Handle a stop by starting a fresh attempt", and node 124's clause 4, would change to match.
ALTERNATIVES:  - Replace it automatically and tell you afterwards what was lost. This is the current shipped text and node 124's draft. It is faster, but it can throw away a worker you only stopped by accident with a rewind.
               - Treat the flag as a discard and leave the node's attempt dead until you say otherwise, without asking. That is silent, so the node could sit unnoticed.

---

Q3. A reminder line when a worker starts
ASK:           When the manager reports a worker as started (the pick report), should it add a line reminding you which stop to use?
RECOMMENDED:   No. The route is written into the manager's contract once. The only moment you need to know the difference is when your stop has actually happened, and Q2 handles that. A line on every pick report would repeat the same text dozens of times per session.
ALTERNATIVES:  - One line, once per session, in the first pick report.
               - One line on every pick report.
```

*The manager: Q1–Q3 put to the human on 2026-09-26, once no gate or raise was waiting ahead of them.*

**A1–A3, the human**, `verbatim`, 2026-09-26: *"Q1. yes the manager stops it Q2 It shouldn't really happen in practice but ask the human Q3. no SO the recommendations"*

The reply names each question and ends *"SO the recommendations"*, so it takes the option the worker offered as `RECOMMENDED` for each, in the worker's words:
- Q1: *"You tell the manager in one line ("stop node N", or "stop and discard node N"), and the manager stops it with `TaskStop`. A plain stop keeps the worker resumable. A discard is also written onto the node as a discarded attempt, so no manager ever resumes it. You don't use the task-panel stop at all."*
- Q2: *"The manager does not replace it on its own. It keeps the node claimed and puts one question to you. The question names the node, says the manager cannot resume that attempt, and says what would be lost: the worker's own investigation, not your answers, which are already recorded. It then offers two choices: you revive the agent by typing to it, which keeps its work, or the manager replaces it and replays your answers."* The human added, on Q2: *"It shouldn't really happen in practice"*.
- Q3: *"No. The route is written into the manager's contract once."*

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Who performs a stop, and what the human's own stop destroys (node 123)

ANSWER:
**The manager performs every stop of a worker. The human asks for one in words, and never uses the task panel's stop.** The human's reply to the three questions, `verbatim`: *"Q1. yes the manager stops it Q2 It shouldn't really happen in practice but ask the human Q3. no SO the recommendations"*. The reply names each question and closes with "SO the recommendations", so each of the three recommendations below is the human's choice as it was offered.

1. **Who stops.** When a worker has to be abandoned (a node the human redirects, a worker gone off-contract, a runaway, or a replacement made redundant), the human tells the manager in one line, and the manager stops the worker with `TaskStop` from its own thread.
   - A plain stop keeps the attempt resumable from its transcript for the rest of the manager's session.
   - A stop the human means as final is also written onto the node, as an attempt that is not to be resumed, so no manager later revives it. The record is what makes the stop final, not the kind of stop.
   - The human does not use the task-panel stop.

   Grounds:
   - The manager's stop loses nothing it does not have to, and node 122's Tests 1 and 2 verified it.
   - The human's stop shuts out the map's standing rule, *"Whenever it can be resumed, resume I think"*, and leaves no trace in the record.
   - Neither stop can remove a worker for good. The human can revive a human-stopped agent by typing to it, which clears the flag. So the node's fourth question, a worker gone "permanently and unrevivably", is answered by writing the finality into the record, and by no harness act.

2. **A worker found stopped by the human.** When a send to an agent comes back refused because the agent carries `stoppedByUser`, the manager does not replace the attempt on its own.
   - It keeps the node claimed and puts one question to the human.
   - The question names the node and says the manager cannot resume that attempt. It says what would be lost: the worker's own investigation, and not the human's answers, which are already recorded.
   - It offers two choices: the human revives the agent by typing to it, which keeps its work, or the manager replaces the attempt and replays the human's answers.
   - The human expects this case to be rare: *"It shouldn't really happen in practice"*.

   Grounds:
   - The flag does not record why the agent was stopped (see the finding below).
   - The harness's own refusal text says *"Treat its work as cancelled; only launch a new agent if the user explicitly asks."*

   This replaces the shipped *"Handle a stop by starting a fresh attempt"* for this case.

3. **No reminder on the pick report.** The route is stated once, in the manager's contract. The only moment the human needs to know the difference is when their own stop has happened, and point 2 covers that moment.

**A finding this node read from the harness's compiled source, not run.** The installed harness is Claude Code 2.1.280, at `/nix/store/29dj17kq7vr7sf6wylvrmgh125cas41f-claude-code-2.1.280/bin/.claude-wrapped`. Node 122 read 2.1.238, which the profile no longer resolves to.

- In 2.1.280 the task panel's stop is not the only act that sets `stoppedByUser`.
  - Rewinding the conversation stops every agent spawned after the point rewound to, and sets the flag and saves it to disk. The function is `Lh`, which calls `mZ`, which calls `_Y`, which sets `stoppedByUser:!0` and writes it to the agent's metadata.
  - The same sweep runs on an interrupt in SDK and remote mode, and on the `--max-budget-usd` halt.
- Not established here:
  - whether the `ctrl+x ctrl+k` chord pressed twice ("stop background agents") sets the flag
  - whether a plain Esc in the terminal does
- So a set flag means only "stopped from the human's side, by some act". It does not mean "meant to be thrown away". That is the ground for point 2.

**Untouched.** Node 23's rule for a stop on an implementation node still holds: the salvage is saved first, then the tree is cleaned. This node changes who performs the stop, not what follows it.

INDEX LINE:    The manager performs every stop of a worker with `TaskStop`, at the human's word. A worker found stopped by the human is not replaced silently: the human chooses between reviving it and a replacement.

FLAGS:
- ASSUMPTION — On node: the node's fourth question asked whether the human ever wants a worker gone "permanently and unrevivably". I did not ask it separately. I folded it into the first question as "a final stop is written onto the node". The harness source shows neither stop gives that: the human's own stop is undone by the human typing to the agent. So the question's premise was false, and the only real choice left was whether finality lives in the record. I made that part of the first question's recommendation, which the human accepted. Index: A node's question about a permanent, unrevivable stop was folded into the question of who stops, because neither harness stop is permanent.
- ASSUMPTION — On node: the facts that a rewind, an SDK or remote interrupt, and the budget halt all set `stoppedByUser` come from reading the compiled source of 2.1.280. They were not produced in a run. I did not probe them: reproducing a rewind is the human's act, and the source path is direct (`Lh` calls `mZ`, which calls `_Y`, which sets the flag and saves it). Whether the `ctrl+x ctrl+k` kill chord or a plain Esc sets it is left unestablished. Index: That a rewind or a sweep of all agents sets the human-stop flag was read from the harness source, not produced in a run.
- ASSUMPTION — On node: my first question offered "stop and discard" as the wording for a final stop. `CONTEXT.md` lists "discard" as a word to avoid (under **Reject**), along with "refuse" and "abandon". I read the human's acceptance as settling the behaviour, not the word. The proposed condition for node 124 below leaves the term to the glossary and rules out those three words. Index: The accepted "stop and discard" is read as settling the behaviour only, since "discard" is a word the glossary says to avoid.

NEW NODES:     none. All the work lands through node 124, "Give the manager's contract a procedure for stopping a running worker", which is open, unclaimed and holds no work. Amending its condition is cheaper than adding a node beside it. A full replacement condition is under INVALIDATIONS. If the human would rather keep node 124's condition and add a separate node, this text can serve as that node's condition as it stands, with node 124 as its blocker.

INVALIDATIONS:
- **Node 124, its acceptance condition.** This answer contradicts it in two places, and the condition lacks two things this answer adds.
  - Clause 4 has the manager, "where the flag is set", *"replace the attempt and tell the human what was lost rather than attempting a resume"*. That is now wrong: the manager asks the human.
  - Clause 5 says a manager reading only three outcomes "misfiles a discarded worker". It is right in substance, but it assumes the flag means the worker is to be thrown away, which is false.
  - The condition does not say that the manager, not the human, performs the stop.
  - The condition does not say that a final stop is written onto the node.
  - Separately, the manager has already annotated clause 1's `stopped` as wrong: the notification actually reads `killed`.
  - Rewriting a condition is not the manager's act, so this goes to the human. Proposed replacement condition, self-contained:

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

  Node 124 edits the same section as node 120, and node 120 is sequenced first. So the replacement's items 6 and 7 build on whatever node 120 lands there.
- **Node 120, "Carry the resume rule into the shipped files", its acceptance condition.** Clause 3 requires that the section *"must no longer assert that an agent the human stopped cannot be resumed"*, and that replay be only the fallback where the resume fails. This answer adds that where the resume fails because of `stoppedByUser`, the fallback is a question to the human, not an automatic replacement. Node 120 does not say this, and node 124's replacement item 6 does. The two do not conflict if node 120's worker does not write "replace" as the unconditional fallback for the user-stopped case. Node 122 has already reported clause 3 and clause 1's three states as needing correction. This adds nothing to fix beyond that, but whoever corrects node 120 should know about it.
- **`.claude/skills/expedition/SKILL.md` on master, `## When an agent dies or is stopped`.** Its *"An agent the human stopped cannot be resumed either. Handle a stop by starting a fresh attempt, never by re-prompting the stopped agent"* contradicts point 2 of this answer. Node 124's replacement items 6 and 10 carry the fix.
- **Node 122, its `## Answer`.** Its table gives the human's stop as "the human's Esc / task UI", and calls it "stop now, discard — and it is the human's alone". In 2.1.280, rewinding the conversation and the SDK and remote interrupt sweeps also set the flag, and the flag does not mean "discard". Node 122's source was 2.1.238, which the profile no longer resolves to.

RETROSPECTIVE:
1. **What I had to hunt for.**
   - **Which acts set `stoppedByUser`.** That was the one fact that moved Q2 away from node 124's draft. The record gave only "Esc / task UI". I found it by grepping the harness binary for `source:"user"` and `stoppedByUser`, then reading the code around each hit by byte offset.
   - **The binary itself.** I first grepped node 122's path, the 2.1.238 binary. A `.{300}` regex over that 338 MB file timed out. `readlink` on `claude` then showed the profile now points at 2.1.280.
   - **A faster way to read it.** `grep -b -o -F` followed by `dd` around the offset is fast. The regex form is not.
2. **What arrived that this node did not need.**
   - Node 122's full answer, about 440 lines, of which I needed the table, the `stoppedByUser` section and the tests.
   - The expedition-stop skill, which is about closing a session and not about stopping a worker. The spawn called it "touching stops", and the word "stop" pulled it in.
   - A spawn that named "stop" in all three of its senses (a session stop, a gate or raise stop, a harness stop) would have spared that read.
3. **What would have made this easier.**
   - In the spawn: the current harness path, or the line "check that node 122's binary is still the installed one".
   - In the record: one line saying which word the glossary reserves for throwing away a worker's work. My recommendation used a word the glossary says to avoid, and I only found out while writing the handover.
   - In the node file: nothing. It was clear.
4. **What was stale, wrong or contradictory.**
   - Node 122's source version (2.1.238) is no longer the installed one.
   - Its "the human's Esc / task UI" as the only source of `stoppedByUser`, and its "stop now, discard", are too narrow in 2.1.280.
   - Node 124's clause 4 contradicts the harness's own refusal text ("only launch a new agent if the user explicitly asks").
   - The shipped "Handle a stop by starting a fresh attempt" contradicts the same text.
   - The spawn's description of the expedition-stop skill as touching stops is true only of the word, not of the subject.

## Flags

`123.1` **· settled** `ASSUMPTION` — On node: the node's fourth question asked whether the human ever wants a worker gone "permanently and unrevivably". I did not ask it separately. I folded it into the first question as "a final stop is written onto the node". The harness source shows neither stop gives that: the human's own stop is undone by the human typing to the agent. So the question's premise was false, and the only real choice left was whether finality lives in the record. I made that part of the first question's recommendation, which the human accepted.

`123.2` **· settled** `ASSUMPTION` — On node: the facts that a rewind, an SDK or remote interrupt, and the budget halt all set `stoppedByUser` come from reading the compiled source of 2.1.280. They were not produced in a run. I did not probe them: reproducing a rewind is the human's act, and the source path is direct (`Lh` calls `mZ`, which calls `_Y`, which sets the flag and saves it). Whether the `ctrl+x ctrl+k` kill chord or a plain Esc sets it is left unestablished.

`123.3` **· settled** `ASSUMPTION` — On node: my first question offered "stop and discard" as the wording for a final stop. `CONTEXT.md` lists "discard" as a word to avoid (under **Reject**), along with "refuse" and "abandon". I read the human's acceptance as settling the behaviour, not the word. The proposed condition for node 124 below leaves the term to the glossary and rules out those three words.
