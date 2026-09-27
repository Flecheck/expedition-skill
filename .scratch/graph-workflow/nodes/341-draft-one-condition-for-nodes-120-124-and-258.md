# Draft one condition for nodes 120, 124 and 258

Type: precondition
Status: resolved
Blocked by: none

## Question

Nodes 120 ("Carry the resume rule into the shipped files"), 124 ("Give the manager's contract a procedure for stopping a running worker") and 258 ("The manager's contract contradicts itself on whether a dead worker is resumed or replaced") share one section of `.claude/skills/expedition/SKILL.md` (`## When an agent dies or is stopped`), one section of `.claude/skills/expedition/graph-conventions.md` (`` ### `## Interview` ``) and one glossary entry (`CONTEXT.md`'s **Attempt**). 124 is blocked by 120. The human approved merging them into one node. Write its condition.

*Minted by the manager on the human's "ok" to [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s recommendation, in its worker's words: "Its condition would be 124's approved condition, plus 120's clauses 1 (without the three-state table and the unconditional replacement fallback), 2, 5, 6 and 7, plus 258's clause 1, with strike-in-place dropped."*

## What must be true when this is done

- One acceptance condition, self-contained for a checker that reads only it, carrying: node 124's condition as amended on 2026-09-26 (the 12-item version, which the human approved); node 120's clauses 1 (without the three-state table and without replacement as an unconditional fallback), 2, 5, 6 and 7; and node 258's clause 1. Each clause is tagged with the node it came from.
- No clause asks for superseded text to be marked and left in place in a shipped file: the human took node 330's C2(a), that shipped files are edited plainly.
- Where a user-stopped worker's resume fails, the condition sends the case to the human as a question, as [node 123](123-who-performs-a-stop.md) decided, and never to an automatic replacement.
- Every quote of current text is checked against the files on master and re-pointed where stale. Demands already met are left out, with the reason.
- The fences of the three nodes are replaced by one fence over the union.
- Every conflict between the three nodes' demands, or between a demand and a resolved node, is listed with the options, for the human.
- Nodes that bear on the same section are listed, including node 121 ("What the two-respawn cap becomes") on the "After two replacements" paragraph.

**Later nodes depend on:** the condition, which the manager files as an amendment replacing node 124's condition, superseding nodes 120 and 258 by node 124.

## Answer

One condition for node 124 now carries nodes 120, 124 and 258: the stop procedure, the resume rule with the human's own stop going to the human, the Attempt entry and a section fence.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, and the human's decision under `## Interview`. The condition is filed on [node 124](124-a-procedure-for-stopping-a-running-worker.md) as its amendment of 2026-09-26 from node 341; nodes 120 and 258 are superseded by 124.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Draft one condition for nodes 120, 124 and 258

ANSWER:
One acceptance condition now replaces the conditions of nodes 120, 124 and 258. It is written for node 124 to hold in place of its 12-item condition, and nodes 120 and 258 are superseded by 124. Every quote of current text in it was checked against master at `64db5aa`. Five conflicts are left for the human (K1 to K5 below). The condition is written to the RECOMMENDED option of each, and the alternative wording is given so another choice can be pasted in.

### The merged condition

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

### Where each source clause went

- **124**, the 2026-09-26 12-item condition. Item 1 went to clause 2, 2 to 3, 3 to 4, and 4 to clauses 5 and 13 (third bullet). Item 5 went to 6, 6 to 10, 7 to 11, 8 to 7, and 9 to 15, without strike-in-place. Item 10 went to 17, 11 to 18, and 12 to 19.
- **120.** Clause 1 went to clause 8 without the three-state table, and with replacement as a fallback that has the user-stopped exception. Clause 2 went to 9, without its bar re-run half (see "Left out"). Clause 5 went to 13 (first two bullets), 6 to 17, 7 to 18, and 8 to 19. Clause 4 went to 14, without strike-in-place (see K1). Clause 3 was left out.
- **258.** Clause 1, as amended from node 296, went to clause 12. Clause 2 went to 14 (see K1), clause 3 to 16 (see K1), and the bar to 19.
- **The fence.** None of the three conditions had a fence of the "no other X changes" kind. Clause 1 and the opening paragraph are the fence over the union: the files and places all three name, the files clause 17's search reaches, and nothing under `.scratch/`. The opening follows the form used by the merged nodes 336 to 339.

### Quotes checked against master `64db5aa`

- `SKILL.md:34`, "A worker is resumed in place rather than replaced.": matches. It was already re-pointed by node 296's amendment to 258.
- `SKILL.md` `## When an agent dies or is stopped` (line 534): the heading matches. The condition quotes three of its sentences, all matching: "An agent that fails to resume is gone.", "Handle a stop by starting a fresh attempt, never by re-prompting the stopped agent." (124 item 6 had given this only as a paraphrase) and "After two replacements, treat a third failure as evidence that the node is too large."
- `SKILL.md` `### Picking the next node`, "You then stop or redirect what you started.": matches. **Re-pointed.** 124 item 8 located it as "The pick report's instruction". It is now located by the subsection heading so that it survives node 137's rename of "pick report".
- `graph-conventions.md` heading: **re-pointed.** 120 clause 5's `### ## Interview` becomes `` ### `## Interview` ``, as it stands on disk. Its "A dead attempt is marked in its own heading. A node holds at most three attempt blocks." matches.
- `CONTEXT.md` `**Attempt**:`: matches 120 clause 4 as amended from node 302.
- `CONTEXT.md` `**Reject**:` `_Avoid_`, "refuse, discard, abandon": matches.
- `CONTEXT.md` `**Checker**:`, "it is not a second opinion": matches. The checker contract says the same: "you are not a second opinion".
- `.claude/skills/expedition-stop/SKILL.md:52-57` `## Agents still running when the session ends`: matches.
- No shipped file names `TaskStop` today, so none of 124's demands is met already.

### Demands left out, with the reason

- **120 clause 2's half "a resumed re-check re-runs the bar's command half rather than carrying it over".** Already met. `SKILL.md` `### Three outcomes, and no fourth` says "The bar is re-checked in every correction round.", and the checker contract's `## When you are handed the same work again` says "Re-run the bar in full." Its other half, that the question of whether a standard moved is settled again, is not met and is kept: the checker contract lets "everything else you already established stand".
- **120 clause 3, whole.** Its first half ("must no longer assert that an agent the human stopped cannot be resumed") asks for a true statement to be deleted, as node 122 showed. Clause 10 adds the human's revival route instead. Its second half (replay only as the fallback) is carried by clause 8's first bullet.
- **120 clause 1's three-state table.** Replaced by clause 11's four outcomes.
- **Strike-in-place in 120 clause 4 and 124 item 9.** Dropped under the human's C2(a) at node 330: shipped files are edited plainly.
- **Kept although already true on master.** 124 item 9's "no entry states or implies that a running worker cannot be stopped" holds today: `CONTEXT.md`'s only use of "stopped" is **Salvage**'s "a stopped attempt". It is kept because the work adds stop entries. 124 item 10's first three search terms find nothing on master and are kept as the search.

### Conflicts for the human

- **K1. The recipe leaves out the Attempt entry.** Node 341 was minted to carry 120's clauses 1, 2, 5, 6 and 7 and 258's clause 1 only. That drops 120 clause 4 and 258 clauses 2 and 3, the only clauses that change `CONTEXT.md`'s **Attempt** entry. Node 330's ground for leaving out 258's entry clause was that the entry "is the same entry as 120's clause 4, which 120's clause 6 already reaches". But 120 clause 6 reaches only files under `.claude/skills/`, and `CONTEXT.md` is at the repository root. Node 328's C8 had sent the Attempt conflict to this grouping, so if it is dropped here, no open node holds it.
  - (a) RECOMMENDED: carry them, as clauses 14 and 16.
  - (b) Drop clauses 14 and 16, and "the entry headed `**Attempt**:`" from clause 1. The entry then keeps "a worker that dies is replaced", which contradicts clause 12 and the map's resume rule.
- **K2. "Second opinion" (120 clause 2 against the glossary and the checker contract).**
  - (a) RECOMMENDED: clause 9 as written.
  - (b) 120's wording: "…and is spawned fresh only where the purpose is a second opinion on a verdict already delivered", with clause 9's last sentence dropped.
  - (c) No fresh-spawn case: "A checker is resumed wherever it can be resumed", with clause 9's second-to-last sentence and its last sentence dropped.
- **K3. What the heading's "dead" marking covers.** Node 120 was written when a dead attempt could still be resumed. The shipped text marks dead only an attempt that failed to resume. Marking dead in its heading an attempt that goes on would contradict "the same attempt continuing".
  - (a) RECOMMENDED: clause 13's first two bullets as written. The heading is marked only for an attempt that did not continue, and a death that was resumed is noted inside the block.
  - (b) 120's wording: "Its dead-attempt marking must additionally require that the attempt's entry carries the dead run's transcript record count and its cause of death as the harness stated it. It must also say that a resumed attempt is recorded as the same attempt continuing rather than as a new attempt block, so the at-most-three-attempt-blocks limit is unaffected by any resume." This leaves the worker to decide.
- **K4. A fence inside the files.** None of the three nodes had one. Clause 1 fences places inside the files so that this node can run beside nodes 336, 337 and 339, which change other sections of the same files.
  - (a) RECOMMENDED: clause 1 as written.
  - (b) A fence on files only: drop clause 1's list and keep its last paragraph and the opening paragraph.
- **K5. Node 121's paragraph.**
  - (a) RECOMMENDED: clause 1's last paragraph. The "After two replacements" paragraph keeps its meaning, and whether a resume counts toward the cap stays node 121's question. Clause 13 only says that a resume adds no attempt block, which node 121's own question already assumes ("given that it adds no attempt block").
  - (b) Block this node on node 121 and add its answer to the condition.
- **Resolved without a choice, recorded for completeness.**
  - Replacement as the fallback (120 clause 1, 258 clause 1, 120 clause 4), against node 123's decision that a user-stopped attempt goes to the human: the exception is in clauses 8, 12 and 14.
  - 120 clause 1's "every attempt spawned in the current session being resumable", against 124 item 6: the exception is in clause 8's third bullet.
  - 120 clause 1's three states, against 124's four: four outcomes.
  - 120 clause 3, against node 122: left out.
  - Strike-in-place, against C2(a): dropped.

### Nodes that bear on the same places

- **121** (open grilling), "What the two-respawn cap becomes": the "After two replacements" paragraph in `## When an agent dies or is stopped`, and whether a resume counts toward the cap (K5).
- **337** (M2, open, blocked by 339): clauses 9 and 10 place its second-supersession statements in "an existing section of `SKILL.md` whose subject includes superseding a node". Node 330's C3 names the last paragraph of `## When an agent dies or is stopped` ("its replacements come by ordinary supersession") as one of the nearest. If M2's worker picks that section, the two nodes edit the same section. **This is the one real collision with a merged node's fence.**
- **336** (M1, open): its clause 10 edits another bullet of `### Picking the next node`, the same subsection as clause 7 here. The text does not overlap.
- **339** (G2, open): adds a `## Procedures` subsection for appending to `## Interview`, ending with a step that names check 8 (at most three attempt blocks). This is consistent with clause 13. Its clause 7 forbids that subsection to restate `## Interview`'s shape.
- **340** (G3, open): adds an annotation section to `## The node file`. Its clause 7 forbids rewording existing text of `graph-conventions.md` in its own work. The only overlap is the file.
- **332** (claimed, at its gate): edits `CONTEXT.md`'s Code slot, Reject, kinds, grilling and Closed entries, not Attempt. Its handover says Reject's `_Avoid_` line is unchanged, which clause 5 names.
- **333** (claimed): edits the five worker contracts. Clause 17 lists their replacement-attempt text as needing no change, so this node should not touch those files.
- **137** (open): renames "pick report". Clause 7 avoids the term.
- **56** (open): moves `CONTEXT.md` to `.claude/skills/expedition/glossary.md`. If it lands first, every `CONTEXT.md` path in this condition must follow the move.
- **327** (open): ships the related-defect rule. Node 330 lists it as a crossing node on `SKILL.md`.

### The search behind clause 17, run on master `64db5aa`

- **Terms:** `resum`, `replac`, `respawn`, `replay`, `stopp`, `TaskStop`, `task UI`, `task panel`, `dies`, `died`, `dead`. The search was case-insensitive.
- **Files:** everything under `.claude/skills/` and `.claude/rules/`, and `CONTEXT.md`.
- **Instances the work changes:** `SKILL.md:34`, `SKILL.md:534-556` and `SKILL.md:480-481`; `graph-conventions.md:263-264`; `CONTEXT.md:103-106`.
- **Instances that are consistent as they stand:**
  - `SKILL.md:74`, `:116` and `:469`: notice of a death, answers banked if an attempt dies;
  - `graph-conventions.md:269` (a claim survives a death) and mechanical check 8;
  - `expedition-stop/SKILL.md:54-57`;
  - `expedition-grilling/SKILL.md:26-27`;
  - `## If you are a replacement attempt` in the grilling, implementation, precondition and prototype contracts;
  - `.claude/rules/expedition-triggers.md:21` ("Resume an agent.");
  - `CONTEXT.md:283` (**Salvage**).
- **Unrelated hits:** `SKILL.md:252` ("respawning" an unfileable handover) and the supersession uses of "replace".

INDEX LINE:    One condition for node 124 now carries nodes 120, 124 and 258: the stop procedure, the resume rule with the human's own stop going to the human, the Attempt entry and a section fence.

FLAGS:
- ASSUMPTION — On node: the manager's recipe for this condition (120's clauses 1, 2, 5, 6 and 7, and 258's clause 1) leaves out every clause that changes `CONTEXT.md`'s **Attempt** entry. Its source, node 330, said 120's clause 6 reaches that entry, but clause 6 reaches only files under `.claude/skills/`. I carried 120 clause 4 and 258 clauses 2 and 3 anyway, as clauses 14 and 16, and put the choice to the human as K1. Index: the merged condition carries the Attempt-entry clauses the recipe dropped, because the recipe's reason for dropping them was false.
- ASSUMPTION — On node: none of the three nodes had a fence of the "no other X changes" kind, so the node's demand for "one fence over the union" had nothing to join. I wrote one over the places the three name, fenced to sections inside each file so that this node can run beside nodes 336, 337 and 339. It is K4 for the human. Index: the merged condition fences sections inside each file, a fence none of its three sources had.
- ASSUMPTION — On node: I left out 120 clause 2's demand that a resumed re-check re-runs the bar. `SKILL.md` ("The bar is re-checked in every correction round.") and the checker contract ("Re-run the bar in full.") already say it. I kept its moved-standard half, which the checker contract does not guarantee on a re-check. Index: node 120's bar re-run demand was left out of the merged condition as already met by the shipped files.

NEW NODES:     none

INVALIDATIONS:
- **Node 330, its `## Answer`, the entry for 258:** "That is the same entry as 120's clause 4, which 120's clause 6 already reaches." This is false. 120's clause 6 reaches only "any other file under `.claude/skills/`", and `CONTEXT.md` is at the repository root. The recipe built on it, which node 341 was minted with, drops the only clauses that change the Attempt entry (K1 above).

RETROSPECTIVE:
1. **What I had to hunt for.**
   - **What a "fence" is here.** Neither node 341 nor the three conditions define it. I found the meaning in node 330's `What must be true` ("Where a replaced node's clause fences its own node ('no other entry changes')…") and the form in the opening paragraphs of nodes 336 to 339.
   - **Whether the recipe covered the Attempt entry.** It did not. I found that by checking 120 clause 6's reach against `CONTEXT.md`'s path.
   - **Which merged nodes touch my sections.** This took a grep over nodes 336 to 340, plus node 330's C3 to see that M2 might land in the dies section.
2. **What arrived that this node did not need.**
   - Of `map.md`, only the grouping bullet, the resume bullet and the never-delete scope bullet bore on this node. The rest (roughly 90% of it) did not. The spawn pointed at the right bullet, but the contract makes the whole file a mandatory read.
   - Node 123's handover retrospective, and its long `SO FAR` block, arrived with the node read. Only its Answer and its INVALIDATIONS condition were needed.
   - Node 120's two annotations are superseded by node 124's approved text, but they had to be read to confirm that.
3. **What would have made this easier.**
   - In the spawn or the node file: a line saying what "fence" means, and whether a missing fence is to be written or reported.
   - In the node file: a note that the recipe's list was node 330's, taken on its stated ground, so the ground can be checked (it was false).
   - In the record: node 330's per-group tables naming the exact SKILL.md sections each merged node may place text in, since M2's "an existing section whose subject includes superseding a node" is open-ended.
4. **What was stale, wrong or contradictory.**
   - Node 330's claim that 120 clause 6 reaches `CONTEXT.md` is wrong (see INVALIDATIONS).
   - 120 clause 5's `### ## Interview` is stale against `` ### `## Interview` ``.
   - 124 item 8's "The pick report's instruction" will be stale once node 137 lands.
   - 120 clause 2's "second opinion" contradicts the glossary's **Checker** entry and the checker contract.
   - 120's "dead attempt" means an agent that can still be resumed, while the shipped text's "dead" means one whose resume failed.
   - The shipped "An agent that fails to resume is gone." is wrong for a resume refused because the human stopped the agent.

## Flags

`341.1` **· settled** `ASSUMPTION` — the manager's recipe for this condition (120's clauses 1, 2, 5, 6 and 7, and 258's clause 1) leaves out every clause that changes `CONTEXT.md`'s **Attempt** entry. Its source, node 330, said 120's clause 6 reaches that entry, but clause 6 reaches only files under `.claude/skills/`. I carried 120 clause 4 and 258 clauses 2 and 3 anyway, as clauses 14 and 16, and put the choice to the human as K1.

`341.2` **· settled** `ASSUMPTION` — none of the three nodes had a fence of the "no other X changes" kind, so the node's demand for "one fence over the union" had nothing to join. I wrote one over the places the three name, fenced to sections inside each file so that this node can run beside nodes 336, 337 and 339. It is K4 for the human.

`341.3` **· settled** `ASSUMPTION` — I left out 120 clause 2's demand that a resumed re-check re-runs the bar. `SKILL.md` ("The bar is re-checked in every correction round.") and the checker contract ("Re-run the bar in full.") already say it. I kept its moved-standard half, which the checker contract does not guarantee on a re-check.

## Interview

### The manager's raise, 2026-09-26

*The manager's own raise, sent after node 131's answer:* whether to file the merged condition as the amendment replacing node 124's condition, superseding nodes 120 and 258 by node 124, taking the worker's recommended option on each of K1 to K5.

The human, `verbatim`: *"ok"* — taking the whole proposal as the manager put it.
