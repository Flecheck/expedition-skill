# Triage the open nodes and the outstanding flags

Type: grilling
Status: resolved
Blocked by: none

## Answer

Triage closed 10 moot nodes, ruled 13 out of scope, made five merges, settled every outstanding flag on resolved or superseded nodes, and ships triage as an invoked skill.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human took all five recommendations, with node 89's clauses going to node 371. The manager performed the writes on 2026-09-29. The node it surfaced is [node 372](372-ship-an-expedition-triage-skill.md). Flags 366.1, 366.2, 366.3, 366.4, 366.5 settle at the node closing report.

## Question

On 2026-09-28 the graph holds 60 open nodes, 13 of the 32 open implementation nodes with no usable acceptance condition, and 252 outstanding flags, none reviewed. Much of the open work fixes this effort's own record, and landed work has made some of it moot (nodes 236 and 186 were closed with no edit). Which open nodes are dropped or superseded, which flags are settled in batches, and in what form, if any, does a triage step belong in the shipped skill?

*Filed by the manager from its own retrospective, 2026-09-28. The human's words on it, `verbatim`: "we can do a triage, I don't know if it should be added to the skill also in some form".*

## Interview

#### Questions 1 to 5, relayed 2026-09-29

*Pasted as the worker handed it back.*

```
NODE:          Triage the open nodes and the outstanding flags (366)
ABOUT:         Decides which of the 60 open nodes to drop or merge, how to settle the 251 outstanding flags in batches, and whether a triage step ships in the skill. It is being decided now because much of the open work is stale and four claims in two days stopped on raises for that reason.
SO FAR:        I checked every open node against the current working tree, not against what the record says. Four read-only helper agents did this, each quoting the current text as evidence. Findings:
               - 10 nodes are moot: later work already fixed the thing they target.
               - About 13 are live but low value. They mostly concern this effort's own record or this machine's sandbox, or the human already marked them low priority.
               - About 30 are live, and I recommend keeping them. The live ones that bear most on the skill working elsewhere are 34, 66, 67, 85, 365, 363, 214, 172 and 317.
               - Six live implementation nodes have conditions that quote moved text: 80, 88, 149, 219, 220 and 284. None is claimed, so the manager may amend their conditions without asking the human first (map rule). I have not asked about them.
               - Node 221's premise is wrong. The ten "lost" retrospectives survive in the worker transcripts under ~/.claude/projects/.../subagents/.
               - Flags: 251 outstanding, 225 of them ASSUMPTION. 192 sit on 61 resolved nodes, 45 on 25 superseded nodes, and 14 on 8 open or claimed nodes. The last group are condition-amendment flags that settle at those nodes' own gates.
               - Under the standing rule, a node's flags settle at its gate or node closing report, on the human's next word. The resolved-node flags are outstanding only because the two "Settle a flag" writes were never made. They are not outstanding because the human never saw them.

Q1. Close the moot nodes
ASK:           May these 10 nodes be closed as superseded by the work that made them unnecessary, with no edit?
RECOMMENDED:   Yes. In each case the tree already shows the fix:
               - 152: node 265 replaced the paragraph it would move.
               - 159: the .gitignore comment already points at the right file (node 249).
               - 237: both passages now name one path (node 265).
               - 254: same clause and same fix as 276, which has the complete condition.
               - 51: node 113 removed every plugin skill name from the contracts.
               - 77: worktrees give every worker a consistent snapshot (SKILL.md, "Picking the next node").
               - 121: no respawn cap exists any more; the rule is now resume wherever possible.
               - 154: the Lang path now exists on this machine.
               - 157: the manager banks work now; a worker never needs to commit.
               - 282: the Edit denial no longer reproduces (about 78 of 79 recent worktree edits succeeded).
ALTERNATIVES:  Name any of these to keep open.
               Re-check each one in its own attempt: this costs a spawn per node for the same answer.

---

Q2. Drop the low-value nodes
CONTEXT:       You said the small improvements may have to stop at some point. These are the smallest.
ASK:           May these 13 nodes be ruled out of scope, each with its reason as its line in the out-of-scope list?
RECOMMENDED:   Yes:
               - 62: moving the AFK passes to the workflow runtime is speculative, with no measured failure behind it.
               - 63: wording of this effort's own out-of-scope line.
               - 83: periodic open-ended review, which you marked low priority.
               - 84: the glossary headword check pays off mostly on this self-hosting effort.
               - 104: one `recovered/` file from node 46, whose use is finished.
               - 125: the checker re-running a baseline would only improve diagnosis.
               - 180: the read-only overlay is now predictable from the sandbox settings.
               - 182: the shadow instrument was never shipped, and node 345 already cut the map.
               - 251: sandbox needs already measured piecemeal by later landings.
               - 232: the shipped graph-conventions.md already states the two never-delete tests in full.
               - 88: the check that produced the false failure no longer exists.
               - 65: frontier.sh now ships as the cheap route to the graph state.
               - 221: old retrospectives, recoverable from the transcripts but of little use now.
ALTERNATIVES:  Name any of these to keep open.
               Keep them all open: they stay in the frontier, and each costs a spawn when picked.

---

Q3. Merge overlapping nodes
ASK:           May these open nodes be merged, so the smaller one's clauses join the larger one's condition and the smaller one is superseded?
RECOMMENDED:   Yes. Each pair edits the same passage for the same concern, which is your standing rule for grouping nodes by file:
               - 271 into 190: same bar paragraph of map-implementation-rules.md; 271's clause 1 is already done.
               - 208 into 214: a condition quoting a refused word is one case of a condition contradicting a standard.
               - 89's remaining clause (cleaning up after a superseded node) into 363: same landing-policy bullet; 89's lifecycle question is already answered as per-effort.
               - 170 and 41 together: both edit the closed list of flag markers.
               Also, node 80 shrinks to its one live clause, the reject-as-forward-revert line in map-manager-only.md.
ALTERNATIVES:  Keep them separate and only sequence them: each file then takes two edits and two checks.

---

Q4. Settle the flags in batches
ASK:           May the 237 outstanding flags on resolved and superseded nodes be marked settled in one batch, leaving the 14 on open or claimed nodes to settle at their own gates?
RECOMMENDED:   Yes. Your standing instruction already settles a node's flags when you approve its end or speak after its node closing report. These nodes all closed before you spoke again, so this batch only makes the writes that were owed. On superseded nodes, the work the flags judged was replaced.
ALTERNATIVES:  Settle only the ASSUMPTION flags now, and first see the 24 non-ASSUMPTION flags as a short list: 19 MANAGER-WRONG, 3 CONDITION-WRONG, 2 SPAWN-WRONG.
               Review them node by node: 86 nodes, many payloads.

---

Q5. Whether triage ships in the skill
ASK:           Should a triage step ship in the skill, and in what form?
RECOMMENDED:   A short skill you invoke, like expedition-cleanup and expedition-standing-yes. It would do what this node did:
               - check each open node against the current tree;
               - propose, in one numbered batch, which nodes are moot, which are dropped and which merge, each with a one-line reason;
               - propose settling the flags whose settling moment has already passed.
               The manager's contract forbids it to drop a node or settle a flag on its own judgement, so an invoked act is where that authority comes from. It pairs with node 365's check before a claim, which is the per-node counterpart.
ALTERNATIVES:  Fold it into node 365's question only: that catches stale nodes one at a time, never the backlog as a whole.
               Make it a third operation of expedition-cleanup: that skill's job is to remove record, while triage changes node statuses.
               Ship nothing and keep it as this effort's practice: the next effort in another repo meets the same backlog with no route.
```

#### The human's answer to questions 1 to 5, 2026-09-29

`verbatim`: *"ok"*

The manager had put the questions with the line "Please answer Q1 to Q5. "ok for recommended" takes all five, with 89's clause going to node 371." So the reply takes the worker's `RECOMMENDED` on all five, with one change the manager had put in that line: on Q3, node 89's remaining clause goes to [node 371](371-say-what-a-review-entry-records-for-a-manager-started-round.md), not node 363. The manager's reason, given to the human with the questions: node 363 was claimed after the worker wrote Q3, and its work has since landed as commit `2cf3730`. Node 371 edits the same file.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Triage the open nodes and the outstanding flags (366)

ANSWER:
The open nodes and the outstanding flags were triaged on 2026-09-28/29. Every open node was checked against the working tree and the shipped files rather than against what the record says about it. The human answered "ok" to all five recommendations, and Q3 carried one change, made before they answered: node 89's clauses go to node 371.

**1. Moot nodes are closed with no edit (Q1).** Later work already did what each asked for.
- 152 is superseded by node 265, which replaced the paragraph 152 would have moved.
- 237 is superseded by node 265. Both passages now name `.scratch/graph-workflow/worktrees/<NN>-<name>`.
- 157 is superseded by node 265. Under that landing route the manager banks the work, so a worker never needs to commit.
- 159 is superseded by node 249. The `.gitignore` comment already points at `map-manager-only.md`, "Landing an implementation node's work".
- 254 is superseded by node 276, which repairs the same clause and carries the complete condition.
- 51 is superseded by node 113, which removed every plugin skill name from the contracts.
- 77 is superseded by node 68. With worktrees, every worker reads a consistent snapshot.
- 121 is superseded by node 119. No respawn cap exists any more, and a dead attempt is resumed wherever it can be.
- 154 is resolved and discharged with no edit: `/home/mathieu/projects/Lang` now exists on this machine, so the link resolves.
- 282 is resolved and discharged with no edit. The Edit denial no longer reproduces: about 78 of 79 recent Edit or Write calls on worktree paths succeeded.

**2. Low-value nodes are ruled out of scope (Q2).** They are live, but small against the destination, and most concern this effort's own record or this machine's sandbox: 62, 63, 83, 84, 104, 125, 180, 182, 251, 232, 88, 65, 221. The reason for each is its line in `map-manager-only.md`'s `## Out of scope`.

**3. Merges (Q3).**
- 271 joins 190 and is superseded by it. Both edit the bar paragraph of `map-implementation-rules.md`.
- 208 joins 214 as one case of it, a condition quoting a word the glossary refuses, and is superseded by it.
- Node 89's remaining clauses, which came from node 275, join node 371, and 89 is superseded by 371. They could not go to 363, which had already landed as `2cf3730`.
- 41 and 170 edit the same closed list of flag markers, so 41 is now blocked by 170 and the list is settled once.
- 80 shrinks to its one live clause, the "When to flip landing to asynchronous" fog item in `map-manager-only.md`.

**4. Flags (Q4).** Every outstanding flag on a node whose status is `resolved` or `superseded` is settled in one batch: 237 flags when counted on 2026-09-28, 192 of them on 61 resolved nodes and 45 on 25 superseded nodes. The human's standing instruction already settles a node's flags when they approve its end or speak after its node closing report. These nodes had all closed, and only the two writes of `### Settle a flag` were owed. The 14 flags on open or claimed nodes (41, 80, 87, 89, 149, 190, 284 and 234) stay outstanding and settle at those nodes' own gates. Node 89's flag goes with its clauses to node 371.

**5. Triage ships as a skill the human invokes (Q5).** It is a short skill in the family of `expedition-cleanup` and `expedition-standing-yes`, and it does what this node did: it checks each open node against the tree, proposes in one numbered payload which nodes are moot, dropped or merged, each with a one-line reason, and proposes settling the flags whose settling moment has already passed. The manager's contract forbids it to drop a node or settle a flag on its own judgement, and the invocation is where that authority comes from. Node 365's check before a claim is the per-node counterpart. The new node that writes the skill is below.

INDEX LINE:    Triage closed 10 moot nodes, ruled 13 out of scope, made five merges, settled every outstanding flag on resolved or superseded nodes, and ships triage as an invoked skill.

FLAGS:
- ASSUMPTION: For nodes 154 and 282 no node made them moot. For 154 the machine changed, and for 282 the symptom stopped. So they are resolved as "discharged with no edit", the form nodes 236 and 186 took, rather than superseded by a node that does not exist. They are resolved rather than ruled out of scope because the human agreed to close them as moot, not to drop them.
  Index: Nodes 154 and 282 are resolved as discharged with no edit, because nothing but the machine or the harness made them moot.
- ASSUMPTION: Node 89's clauses are about `.claude/skills/expedition/SKILL.md`, while node 371 is scoped to `graph-conventions.md` and its clause 2 forbids any other sentence under `.claude/skills/` from changing. So the merge also widens 371's clause 2 to admit those SKILL.md sentences. The human's "ok" named the destination node, not the scope change.
  Index: Joining node 89's SKILL.md clauses to node 371 widens 371's clause 2 so the edit may reach those SKILL.md sentences.
- ASSUMPTION: "170 and 41 together" is carried out as an edge, 41 blocked by 170, rather than as a merge. Node 170 has no condition and waits on a choice only the human can make (a fourth marker, an open list, or elsewhere), while 41's condition is complete.
  Index: "Work 41 and 170 together" is recorded as node 41 blocked by node 170, since 170 still waits on a human choice.
- ASSUMPTION: The verdict on each node rests on reports from four read-only helper agents, each quoting current tree text. I re-verified a sample myself: 363's still-live lines at that time, the SKILL.md reject line, and the landing-policy text for 80.
  Index: The node-by-node verdicts came from read-only helper agents quoting current tree text, spot-checked rather than all re-derived by the worker.
- ASSUMPTION: The flag batch covers every `- [ ]` line whose linked node is `resolved` or `superseded` at the moment the manager writes it, rather than a frozen list of 237. Nodes that closed since the count had their flags settled by the normal rule anyway.
  Index: The flag batch is defined by the linked node's status at write time, not by the 237 lines counted on 2026-09-28.

NEW NODES:
Block 1 (new node)
- Name: Ship an `expedition-triage` skill
- Kind: implementation
- Question: Ship, as a skill the human invokes in an expedition's manager thread, the triage node 366 ran by hand: check the open nodes and the outstanding flags against the current tree, and propose in batches what to close, drop, merge and settle.
- Blockers: none. Node 365, the check before a claim, is its per-node counterpart and does not block it.
- Acceptance condition:
  1. A new file `.claude/skills/expedition-triage/SKILL.md` exists. Its front matter has `name: expedition-triage` and a `description` saying the human invokes it in an expedition's manager thread to triage the effort's open nodes and outstanding flags.
  2. The file tells the manager to check each open node against the current working tree and the current shipped files, not against what the effort's record says about them. It permits the manager to give that checking to read-only agents.
  3. The file sorts each open node into exactly one of four classes, and defines each class:
     - moot: the work the node asks for is already done, or the text it targets no longer exists;
     - dropped: the node is still live, but not worth its cost to the effort's destination;
     - merged: the node concerns the same file and the same concern as another open node;
     - kept.
     For a kept implementation node, the file tells the manager to report whether its acceptance condition quotes text that no longer exists.
  4. The file tells the manager to put its proposal to the human as one payload, with one numbered question per class and per flag batch. Each question lists its nodes, each with a one-line reason, so that one reply can answer it. The file says that no node's status and no flag's state changes before the human has answered.
  5. The file tells the manager to propose settling, in one batch, the outstanding flags whose node is `resolved` or `superseded`, and to leave outstanding the flags on nodes that are `open` or `claimed`.
  6. The file says what follows the human's answer:
     - a moot node is superseded by the node whose work made it unnecessary, or, where no node did, resolved with an answer saying it was discharged with no edit and why;
     - a dropped node is ruled out of scope;
     - a merged node's clauses are added to the other node's acceptance condition, and the merged node is superseded by that node;
     - a flag in an approved batch is settled.
     The file names the procedures for these acts by the headings `### Supersede`, `### Resolve`, `### Rule out of scope`, `### Amend an acceptance condition` and `### Settle a flag` in `.claude/skills/expedition/graph-conventions.md`, and does not restate their steps.
  7. The file says the skill runs only when the human invokes it, and that nothing in it runs on a schedule or on the manager's own judgement.
  8. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
  9. Scope came from no search: the work creates a file.

Block 2 (defect joined to open node 190, from node 271). Clauses to add to 190's acceptance condition:
  - In `.scratch/graph-workflow/map-implementation-rules.md`, the sentence of the bar paragraph that states which patterns the repository's ignore file ignores is replaced by its current form, with no struck-through text in it. It names every pattern that `.gitignore` at the repository root then holds, which the worker verifies by opening `.gitignore` and quotes in its handover. The text it replaces is appended verbatim to `.scratch/graph-workflow/map-history.md` under a heading mirroring the section it came from, with struck-through text staying struck through.
  - The same sentence still says that this repo has no build, no tests, no formatter and no CI, that `.gitignore` invokes nothing, and that the bar's command half being empty is a complete bar rather than a deficient one.
  - `.gitignore` is not edited.
  - Scope came from no search: the sentence named is the place of the work.

Block 3 (defect joined to open node 214, from node 208). Node 214 has no condition, so this is an addition to its question: "This includes the case where a condition quotes a phrase containing a word the glossary refuses for the very concept the condition means. The worker cannot ship the condition's word without breaking the bar, and cannot know whether a checker will accept a substitute. Nodes 196, 197 and 200 each met this, as flags 196.1, 197.1 and 200.x record."

Block 4 (defect joined to open node 371, from node 89, clauses originally from node 275). Clauses to add to 371's acceptance condition:
  - `.claude/skills/expedition/SKILL.md` also states what happens to the working state of an implementation node that is superseded while its work has not landed. The graph is edited first. After that, the node's tree, and anything else that holds its unlanded work, is removed, in the same order the file gives for a reject. The file states this as properties rather than as commands of any one version-control tool, and names no command that a repository without that tool could not run.
  - The line in `.claude/skills/expedition/SKILL.md` that reads "reject: edit the graph first, and clean the working state after." still states the reject outcome in the same order: the graph first, the working state after.
  - Scope came from no search: the file named is the place of the work, not an instance of a defect.
  Replacement for 371's clause 2: "No other sentence of any file under `.claude/skills/` changes, except the sentences of `.claude/skills/expedition/SKILL.md` that the clauses carried from node 89 require, and no file under `.scratch/` changes."

Block 5 (edge): node 41 gains `Blocked by: 170`.

Block 6 (node 80's condition, replaced whole, since it is unclaimed):
  > The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, and no other file is edited.
  > 1. The item under `## Not yet specified` beginning "When to flip landing to asynchronous" no longer says that the seam is one step, and no longer says that reject becomes a forward revert rather than a cleaned tree. It describes the seam and what a reject costs against the landing policy that the same file's `## Landing an implementation node's work` states: on approval, a path-limited commit, a rebase onto the branch the manager thread is on, a re-run of the bar's commands, and `git merge --ff-only`; on reject, the worktree is removed and its branch deleted.
  > 2. The item's replaced text is appended verbatim to `map-history.md` under a heading mirroring the section it came from. `map-history.md` gains text and loses none.
  > 3. No other item of `map-manager-only.md` changes.
  > 4. Scope came from no search: the item named is the place of the work.

Out-of-scope lines for `map-manager-only.md`'s `## Out of scope`, one per node (Q2):
- 62: moving the AFK passes onto the workflow runtime. Speculative, with no measured failure behind it; ruled out at node 366.
- 63: narrowing this effort's own cost-accounting out-of-scope line. It concerns this effort's scope wording only; node 366.
- 83: a periodic open-ended review. The human marked it low priority, and it is ruled out at node 366.
- 84: checking one's own diff against the glossary headwords. It pays off mostly on this self-hosting effort; node 366.
- 104: whether `recovered/` is a file kind. A single use, now finished; node 366.
- 125: a checker re-running an enumerator's baseline. It would only improve diagnosis; node 366.
- 180: which trees get the read-only skills overlay. Now predictable from the sandbox settings; node 366.
- 182: pricing map sections with the shadow instrument. The instrument never shipped, and node 345 already cut the map; node 366.
- 251: what the manager's own session cannot write. Measured piecemeal by later landings; node 366.
- 232: stating the two never-delete tests in `map.md`. The shipped `graph-conventions.md` already states them; node 366.
- 88: twenty legacy flags with no ids. The check that produced the false failure no longer exists; node 366.
- 65: a cheap route to the graph state. `frontier.sh` ships; node 366.
- 221: filing ten missing retrospectives. Of little use now. The text is recoverable from the worker transcripts under `~/.claude/projects/-home-mathieu-projects-graph-agent/0e2d7caf-7b86-4009-bb71-5e76adb6ec22/subagents/`, so the loss the node assumed did not happen; node 366.

INVALIDATIONS:  none. No resolved node's answer changes. The flag batch carries out the settling rule the human already gave; it does not change that rule.

CONDITIONS:
- What I searched: every open node's `Blocked by:` line, and every open node's text, for links to or mentions of the nodes this answer closes or merges (152, 159, 237, 254, 51, 77, 121, 154, 157, 282, 62, 63, 83, 84, 104, 125, 180, 182, 251, 232, 88, 65, 221, 271, 208, 89, 170, 41, 80).
  - No open node is `Blocked by:` any node closed here, so no edge is left that nothing satisfies.
  - Node 276's manager note (its paragraph naming nodes 237 and 254) says whether 276 supersedes 254 "is the human's". The human has now answered yes, so that note is out of date but needs no edit.
- Replacements written: node 371's clause 2 and node 80's whole condition, both in NEW NODES. The words of 371's replacement are fixed by 371's own condition and by node 275's clauses. The words of 80's replacement are fixed by the current text of `map-manager-only.md` `## Landing an implementation node's work`.
- Node 219: clauses 1 and 4 name `.scratch/graph-workflow/map.md` `## Notes`, but the retrospective bullet now lives in `map-manager-only.md` `## Notes`. `map.md`'s own pointer line says node 345 moved it there. Replacement: read `.scratch/graph-workflow/map-manager-only.md`, `## Notes`, wherever those clauses say `.scratch/graph-workflow/map.md` `## Notes`.
- Stale conditions I found but have not rewritten, because their fixes need material I did not establish:
  - 149 picks the rules file as the holder of `**Ground rules for this effort.**`, which is now in `map.md`.
  - 220's clause 2 is held for the human's amendment.
  - 284's clause 4 and its second author's clause 1 target text that has moved; its scope should also reach `map-implementation-rules.md`, "An implementation node's worktree is made with plain git".
- Questions changed: 214's question is widened by Block 3. Node 365's question is unchanged, but Q5 now names it the per-node counterpart of the triage skill.

MISSING FROM MAP: The map does not say where the rule on when a node's flags settle binds this effort; the rule is in `map-manager-only.md` `## Notes`, "Approving a node's end settles that node's flags", which I found by searching. Counts of open nodes and flags are, rightly, not in the map; I got them from `frontier.sh` and by grepping `Status:` and `- [ ]`. Nothing says whether a node made moot by a change to the machine rather than by a node is superseded or resolved; I followed the precedent of nodes 236 and 186.

RETROSPECTIVE:
1. What I had to hunt for. Why 192 flags on resolved nodes were still outstanding. The answer is that the settling rule held but its writes were never made, which I found in `map-manager-only.md`, "Approving a node's end settles that node's flags", after first looking in the shipped `SKILL.md` `## Flags`. Also how a moot node is closed: the `Statuses` in `graph-conventions.md` and node 236's answer.
2. What arrived that this node did not need. Nearly all of `map.md`'s standing preferences and its writing rules bore on nothing here. The contract's `## When a node you report is an implementation node` I needed only for the new node's condition.
3. What would have made this easier. A spawn line saying that the flag-settling rule lives in `map-manager-only.md`. A script listing each open node with its type, its blockers, whether it has a condition, and its annotation headings. I built that listing by hand.
4. What was stale, wrong or contradictory.
   - The manager's count of 252 outstanding flags is really 251: the 252nd `- [ ]` line is the format example in `flags.md`'s header.
   - Node 221's premise that the retrospectives are unrecoverable is false.
   - Node 32's question cites contract line numbers that no longer match.
   - Node 317's note names `CONTEXT.md`'s `**Flag**:` entry, which now lives in the glossary.
   - Node 185's header says implementation, while node 356's note calls it grilling.
   - Node 270's "first executable artifact this effort ships" is false: `frontier.sh` already ships.
`````

## Flags

`366.1` `ASSUMPTION` **· settled** — Nodes 154 and 282 are resolved as discharged with no edit, because nothing but the machine or the harness made them moot. *(The worker's full text is under its handover's `FLAGS`.)*

`366.2` `ASSUMPTION` **· settled** — Joining node 89's SKILL.md clauses to node 371 widens 371's clause 2 so the edit may reach those SKILL.md sentences. *(The worker's full text is under its handover's `FLAGS`.)*

`366.3` `ASSUMPTION` **· settled** — "Work 41 and 170 together" is recorded as node 41 blocked by node 170, since 170 still waits on a human choice. *(The worker's full text is under its handover's `FLAGS`.)*

`366.4` `ASSUMPTION` **· settled** — The node-by-node verdicts came from read-only helper agents quoting current tree text, spot-checked rather than all re-derived by the worker. *(The worker's full text is under its handover's `FLAGS`.)*

`366.5` `ASSUMPTION` **· settled** — The flag batch is defined by the linked node's status at write time, not by the 237 lines counted on 2026-09-28. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-29:* flags 366.1, 366.2, 366.3, 366.4, 366.5 settle at the node closing report that closes this node.
