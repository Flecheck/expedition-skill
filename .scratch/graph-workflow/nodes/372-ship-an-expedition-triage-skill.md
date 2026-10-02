# Ship an `expedition-triage` skill

Type: implementation
Status: resolved
Blocked by: none

## Answer

Ships `expedition-triage`, an invoked skill: check open nodes against the tree, sort them into moot, dropped, merged or kept, propose with flag settling in one payload, then act by graph-conventions procedures.

*The manager's note:* the worker's answer is under `## Handover, attempt 1` and its two correction rounds. Run 1 failed on the bar; run 2 passed with run 1's question still open; the human chose the correction at the gate; run 3 passed, and the gate was taken under the standing yes. The work landed as commit `3196288d`. Flags 372.1, 372.2 settle at the node closing report.

## Question

Ship, as a skill the human invokes in an expedition's manager thread, the triage node 366 ran by hand: check the open nodes and the outstanding flags against the current tree, and propose in batches what to close, drop, merge and settle.

*Reported by [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. Node 365, the check before a claim, is its per-node counterpart and does not block it."*

## Acceptance condition

*Authored by node 366's worker and filed by the manager.*

> 1. A new file `.claude/skills/expedition-triage/SKILL.md` exists. Its front matter has `name: expedition-triage` and a `description` saying the human invokes it in an expedition's manager thread to triage the effort's open nodes and outstanding flags.
> 2. The file tells the manager to check each open node against the current working tree and the current shipped files, not against what the effort's record says about them. It permits the manager to give that checking to read-only agents.
> 3. The file sorts each open node into exactly one of four classes, and defines each class:
>  - moot: the work the node asks for is already done, or the text it targets no longer exists;
>  - dropped: the node is still live, but not worth its cost to the effort's destination;
>  - merged: the node concerns the same file and the same concern as another open node;
>  - kept.
>  For a kept implementation node, the file tells the manager to report whether its acceptance condition quotes text that no longer exists.
> 4. The file tells the manager to put its proposal to the human as one payload, with one numbered question per class and per flag batch. Each question lists its nodes, each with a one-line reason, so that one reply can answer it. The file says that no node's status and no flag's state changes before the human has answered.
> 5. The file tells the manager to propose settling, in one batch, the outstanding flags whose node is `resolved` or `superseded`, and to leave outstanding the flags on nodes that are `open` or `claimed`.
> 6. The file says what follows the human's answer:
>  - a moot node is superseded by the node whose work made it unnecessary, or, where no node did, resolved with an answer saying it was discharged with no edit and why;
>  - a dropped node is ruled out of scope;
>  - a merged node's clauses are added to the other node's acceptance condition, and the merged node is superseded by that node;
>  - a flag in an approved batch is settled.
>  The file names the procedures for these acts by the headings `### Supersede`, `### Resolve`, `### Rule out of scope`, `### Amend an acceptance condition` and `### Settle a flag` in `.claude/skills/expedition/graph-conventions.md`, and does not restate their steps.
> 7. The file says the skill runs only when the human invokes it, and that nothing in it runs on a schedule or on the manager's own judgement.
> 8. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
> 9. Scope came from no search: the work creates a file.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Ship an `expedition-triage` skill (372)

ANSWER:
A new invoked skill, `.claude/skills/expedition-triage/SKILL.md`, writes down the triage that node 366 ran by hand. It is about 3 KB and follows the form of `expedition-cleanup` and `expedition-standing-yes`. Its front matter carries `name: expedition-triage` and a description saying the human invokes it in an expedition's manager thread to triage the open nodes and outstanding flags. It has four sections.
- `## Check each open node`: check against the current working tree and the current shipped files, and not against the record. The checking may go to read-only agents, and each one quotes the current text its finding rests on. The section defines the four classes moot, dropped, merged and kept. For a kept implementation node, the proposal says whether its condition quotes text that no longer exists.
- `## Check the outstanding flags`: one batch proposes settling the flags on `resolved` or `superseded` nodes. Flags on `open` or `claimed` nodes stay outstanding. The section also states the node 89.1 case: a flag on a merged node that judges the clauses that move stays outstanding and settles at the gate of the node that receives them.
- `## The proposal`: one payload, with one numbered question per class and one for the flag batch. Each question lists its nodes or flags with a one-line reason. No status or flag state changes before the human answers.
- `## After the human answers`: each act points by heading at `### Supersede`, `### Resolve`, `### Rule out of scope`, `### Amend an acceptance condition` and `### Settle a flag` in `graph-conventions.md`, and restates none of their steps. It also points at `### Changing one after it is written` in SKILL.md for which nodes may be amended. It states the second case node 366 met: where an older flag entry has no id to mark, settle the flag by its line in `flags.md` and add the manager's own note on the node.
The skill's opening says it runs only when the human invokes it, and never on a schedule or on the manager's judgement.
Calls a later reader would otherwise re-derive:
- `kept` is defined as "none of the three above".
- The flag batch is one question, because clause 5 says "one batch".
- The H1 heading is "Triaging the open nodes and the outstanding flags" and not a bare "Triage". The cascade contract already uses "triage" as a role name, under its `## Triage` heading.

INDEX LINE:    Ships `expedition-triage`, an invoked skill: check open nodes against the tree, sort them into moot, dropped, merged or kept, propose with flag settling in one payload, then act by graph-conventions procedures.

FLAGS:
ASSUMPTION: The name the condition fixes, `expedition-triage`, shares the word "triage" with the cascade contract's triage role (`.claude/skills/expedition-cascade/SKILL.md`, `## Triage`, `ROLE: triage`). Node 87's question also speaks of a "triage agent". I kept the name the condition fixes and titled the H1 "Triaging the open nodes and the outstanding flags", so that the skill's heading does not read as the cascade role. The glossary defines neither use. — Index: Node 372 kept the condition's name `expedition-triage` though the cascade contract already names a "triage" role, and titled the skill's heading to tell the two apart.
ASSUMPTION: I added two rules the condition does not demand, both from the cases the manager met while carrying out node 366's answer. First, a flag on a merged node that judges the clauses that move stays outstanding and settles at the receiving node's gate (the flag 89.1 case). Second, a flag entry with no id is settled by its `flags.md` line plus a note from the manager on the node (the same note the manager wrote in commit 44588fca). Both are short, and neither contradicts a clause. — Index: Node 372's skill adds two cases node 366's carrying-out met, a flag that travels with merged clauses and a flag entry with no id, beyond what its condition demands.

NEW NODES:     none

INVALIDATIONS: none. The skill restates no rule it does not point at. It extends nothing a resolved node says. Node 366's answer said triage "ships as an invoked skill", and this is that skill.

CONDITIONS:    I searched the 37 open or claimed nodes' conditions and questions for `triage`, `invoked skill`, `expedition-cleanup`, `expedition-standing-yes` and `expedition-triage`. Matches outside node 372:
- Nodes 41, 214, 219, 190, 80 and 371 only cite node 366 as a provenance line.
- Node 370's match was incidental.
- Node 87's question speaks of the cascade's "triage agent", a different thing, and this work does not change it. See the first flag.
No replacement clauses, and no open node's question changed.

MISSING FROM MAP: How the manager settled flags with no id during node 366's carrying-out was not in the map or in node 366. I found it in commit 44588fca's manager notes ("this node's flags carry no ids, so none can be marked in place ... settled ... by their lines in `flags.md`"). The 89.1 case was found on nodes 89 and 371.

GATE PAYLOAD:
- Checker findings: none yet.
- Bar: the repo has no build, tests, formatter or CI. I checked the worktree root: only `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`. This matches `map-implementation-rules.md`. The non-command half was held to: the glossary `_Avoid_` lines (no "close" for resolve, no "item" for node, "tree" only as "working tree") and writing rules 5 and 6 (pointers by heading, one clause each).
- Clause 8: `git status` in the worktree shows only the new file.
- Paths touched: `.claude/skills/expedition-triage/SKILL.md` (new). Nothing else.
- Proposed commit message:
  Ship the expedition-triage skill

  An invoked skill for the manager: check open nodes against the working tree, sort them into moot, dropped, merged or kept, propose them and the flag batch in one payload, then act by the graph-conventions procedures.

  Node: graph-workflow/372

RETROSPECTIVE
1. What I had to hunt for: how the manager actually handled the two cases in the spawn's note. For the flags with no id, the answer was in commit 44588fca's notes and not in the record's prose. For 89.1, it was in nodes 89 and 371. I also checked that all five cited headings exist in `graph-conventions.md`, and they do.
2. What arrived that this node did not need: most of `map.md` (the history paragraphs, the standing preferences on v2 and Lang) and most of `map-implementation-rules.md` beyond the bar paragraph. I did not need the decisions.md line for node 365 beyond knowing it is the per-node counterpart.
3. What would have made this easier: a spawn note giving the 44588fca note text for the no-id case, or naming that commit. Also a warning that "triage" is already a cascade role name.
4. What was stale, wrong or contradictory: nothing contradictory. The spawn called the case "older entry forms had no marker position". The manager's own note says the entries "carry no ids", so the gap is a missing id rather than a missing marker. I wrote the skill to the id reading.
````

*The manager's note, from context it already holds:* on the worker's retrospective point 4, the carrying-out of node 366 met both cases. 14 flags had ids but were written in older entry forms with no marker position, and got a manager's settle entry appended on their node. 20 legacy flags had no ids at all. The skill states the no-id case.

## Review

### Checker run 1 — `FAIL` (the bar)

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c372.md`.*

> FAIL: the bar
>
> Node: 372, "Ship an `expedition-triage` skill". Work: the untracked file /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/372-triage/.claude/skills/expedition-triage/SKILL.md. The base is 7fe98da3.
>
> Acceptance condition: all nine parts are met. I searched the file as unwrapped text, using `tr '\n' ' ' < F | tr -s ' '` followed by `grep -oE '<phrase>' | wc -l`.
> 1. Met. Front matter has `name: expedition-triage`. The description contains "The human invokes it in an expedition's manager thread" and "Triage an expedition's open nodes and outstanding flags". Each search found 1 hit.
> 2. Met. "not against what the effort's record says about it" and "You may give this checking to read-only agents" each found 1 hit.
> 3. Met. "exactly one of four classes" was found, and `**moot**`, `**dropped**`, `**merged**` and `**kept**` are each defined with the condition's wording. Kept is defined as "none of the three above". "quotes text that no longer exists" is found, and it applies to a kept implementation node.
> 4. Met. "one payload", "one numbered question per class and one for the flag batch", "one-line reason" and "Change no node's status and no flag's state before the human has answered" are all found.
> 5. Met. "is `resolved` or `superseded`" (propose settling in one batch) and "is `open` or `claimed`" (leave outstanding) are both found.
> 6. Met. All four acts are present, and "discharged with no edit, and why" is found. The file names `### Supersede`, `### Resolve`, `### Rule out of scope`, `### Amend an acceptance condition` and `### Settle a flag`, and does not restate their steps. All five headings exist in .claude/skills/expedition/graph-conventions.md. The file cites the target as the bare `graph-conventions.md`, which is how the sibling skills cite it (expedition-cleanup and expedition-standing-yes).
> 7. Met. "This skill runs only when the human invokes it. Run none of it on a schedule or on your own judgement."
> 8. Met. `git status --porcelain --ignored --untracked-files=all` printed only `?? .claude/skills/expedition-triage/SKILL.md`, and `git diff 7fe98da3 --stat` was empty. No other path under .claude/skills/ or .scratch/ changed.
> 9. Met. The condition records no search, so there was nothing to run.
>
> The bar: the repo has no root agent-instruction file. The implementation-rules file records that the repo has no build, no tests, no formatter and no CI. The bar is therefore its non-command half, which is the standards below.
>
> Standards: I read only the standards in .scratch/graph-workflow/map-implementation-rules.md and opened no other file in the effort's directory. The standards it names are `/coding-principles`, `/naming`, glossary.md's `_Avoid_` lines, the ground rules, the six standing rules for writing, graph-conventions.md and `/writing-for-agents`. It names no reviewing skill. I read `/writing-for-agents` directly through the Skill tool and spawned no agent. I checked the `_Avoid_` lines by hand. "payload" is refused only for a handover, and this file uses it for a manager-to-human payload, which the condition itself dictates. The standards that bore on this work were writing rules 5 and 6, graph-conventions.md, the glossary, and `/writing-for-agents`.
>
> Findings (both in one paragraph):
>
> F1 — writing rule 6 ("A passage that changes a rule for its own case names that rule by heading and states the change in its own words").
> - Instance: under `## Check the outstanding flags`, the worker's own sentence "It settles at the gate of the node that receives those clauses." It changes, for merged nodes, the rule in .claude/skills/expedition/SKILL.md `## Flags`: "Settle a node's flags at its gate ... Otherwise, settle them at the node closing report ... none has a rule of its own". The passage does not name `## Flags`. The condition does not dictate this sentence.
> - Form: a sentence in the work that sets when or how a flag settles, or a status changes, differently from the rule in SKILL.md or graph-conventions.md, without naming that rule's heading.
> - Extent: `grep -n -E 'settle|settles|stays outstanding' .claude/skills/expedition-triage/SKILL.md`, run in the worktree. Each hit is a candidate.
>
> F2 — writing rule 5 ("one clear referent for each pronoun").
> - Instance: in the same paragraph, "A flag on a merged node that judges the clauses that move stays outstanding." The relative pronoun "that judges" can refer either to "a flag" or to "a merged node".
> - Form: a relative pronoun ("that", "which") that follows a noun phrase holding two candidate nouns.
> - Extent: the finding has no extent. Its instance is not exhaustive. A grep for ` that ` over the 60-line file lists the candidates, and they have to be read by hand.
>
> QUESTIONS:
> - The condition is met here, but meeting it creates a conflict. Part 5 has the manager propose settling outstanding flags on `resolved` or `superseded` nodes in one triage batch. .claude/skills/expedition/SKILL.md `## Flags` says "Settle a flag only at the moments this section names, never on your own judgement", and triage is not one of those moments. The wording is the condition's own, so departing from it was not the worker's call. Should `## Flags` name the human's approval of a triage flag batch as a settling moment, or should the triage file point at `## Flags` and state this case as a change to that rule?
>
> Not checked: nothing outside the one changed path. I read no part of the record.

*The manager's note:* an unmet bar goes back to the worker, with both findings, in one correction round. The checker's question on part 5 against `SKILL.md`'s `## Flags` goes to the human at the gate.

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-10-02, after correction round 1. The same checker, resumed within this node.*

> PASS
>
> Node 372, "Ship an `expedition-triage` skill", run 2, after a correction round. I re-ran the bar in full, re-checked the two run 1 findings, and re-checked parts 5 and 6 of the condition, which the edits touch. I read the whole changed file and diffed it against my run 1 reading myself; I did not rely on the handover. The only changes are the two passages the handover names.
>
> Condition, one line per part. I searched the text with line breaks removed (`tr '\n' ' ' < F | tr -s ' '`, then `grep -oE '<phrase>' | wc -l`).
> 1. Met. Established in run 1 and not touched by this round. Front matter has `name: expedition-triage` and a description reading "The human invokes it in an expedition's manager thread" to triage open nodes and outstanding flags.
> 2. Met. Established in run 1, untouched.
> 3. Met. Established in run 1, untouched.
> 4. Met. Established in run 1, untouched.
> 5. Met. Re-checked. "is `resolved` or `superseded`" (proposed for settling in one batch) and "is `open` or `claimed`" (left outstanding) each match once. The new merged-node paragraph also leaves those flags outstanding, so it agrees with this part. At triage time a merged node is still open.
> 6. Met. Re-checked. `### Supersede` (2), `### Resolve` (1), `### Rule out of scope` (1), `### Amend an acceptance condition` (1) and `### Settle a flag` (2) are named, and all five headings exist in .claude/skills/expedition/graph-conventions.md. "discharged with no edit, and why" is present. The no-id sentence states a change to step 2 of `### Settle a flag` and does not restate the procedure's steps.
> 7. Met. Established in run 1, untouched.
> 8. Met. Re-run. `git status --porcelain --ignored --untracked-files=all` printed only `?? .claude/skills/expedition-triage/SKILL.md`, and `git diff 7fe98da3 --stat` printed nothing.
> 9. Met. The condition records no search, so there is nothing to run.
>
> Bar. The repo has no build, tests, formatter or CI. map-implementation-rules.md records this, and the repo root has no agent-instruction file. So the bar is the standards in that file. I read only the standards in it.
> - F1 (writing rule 6) is cleared. "This changes the rule under `## Flags` in your contract for this one case: ..." matches once. "this changes step 2 of `### Settle a flag`" matches once.
> - F2 (writing rule 5) is cleared. The sentence now reads "Where a merged node holds a flag, and the flag judges the clauses that move, leave the flag outstanding." I listed every " that " and " which " in the file with `grep -oE '.{40} (that|which) .{30}'` and read the seven hits by hand. Each has one clear referent.
> - The standards that bore on this work are writing rules 5 and 6, graph-conventions.md, the glossary's `_Avoid_` lines, and `/writing-for-agents`. No reviewing skill is named for this repo, so none was run.
>
> My run 1 question, on part 5 against `## Flags`, is still open. On the coordinator's instruction I have not repeated it here. It goes to the human at the gate.
>
> Not checked: nothing outside the one changed path. I read no part of the record.

*The manager's note:* run 1's question beside its outcome is still open, so the standing yes does not cover this gate; it goes to the human.

#### The human's answer at the gate, 2026-10-02

The manager put checker run 1's question to the human, recommending one correction round: the skill's batch sentence names `## Flags` and states that, for this case, the human's approval of the batch is the settling moment, as rule 6 says a passage changes a rule for its own case. The alternative offered was approval as is, with a node adding the triage batch to `## Flags` as a settling moment. The human, `verbatim`: *"ok for recommended"*. So the gate's outcome is **correct**, and the node goes to correction round 2.

## Handover, attempt 1, correction round 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Ship an `expedition-triage` skill (372) — correction round after checker run 1

ANSWER:
A new invoked skill, `.claude/skills/expedition-triage/SKILL.md`, writes down the triage that node 366 ran by hand. It is about 3 KB and follows the form of `expedition-cleanup` and `expedition-standing-yes`. Its front matter carries `name: expedition-triage` and a description saying the human invokes it in an expedition's manager thread to triage the open nodes and outstanding flags. It has four sections.
- `## Check each open node`: check against the current working tree and the current shipped files, and not against the record. The checking may go to read-only agents, and each one quotes the current text its finding rests on. The section defines the four classes moot, dropped, merged and kept. For a kept implementation node, the proposal says whether its condition quotes text that no longer exists.
- `## Check the outstanding flags`: one batch proposes settling the flags on `resolved` or `superseded` nodes. Flags on `open` or `claimed` nodes stay outstanding. The section also states the node 89.1 case, as a named change to `## Flags` in SKILL.md: a merged node's flag that judges the clauses that move stays outstanding, and settles at the gate of the node that receives those clauses.
- `## The proposal`: one payload, with one numbered question per class and one for the flag batch. Each question lists its nodes or flags with a one-line reason. No status or flag state changes before the human answers.
- `## After the human answers`: each act points by heading at `### Supersede`, `### Resolve`, `### Rule out of scope`, `### Amend an acceptance condition` and `### Settle a flag` in `graph-conventions.md`, and restates none of their steps. It also points at `### Changing one after it is written` in SKILL.md for which nodes may be amended. The no-id case is stated as a named change to step 2 of `### Settle a flag`: where an older flag entry has no id to mark, the flag is settled by its `flags.md` line alone, and the manager writes a note of its own on the node.
The skill's opening says it runs only when the human invokes it, and never on a schedule or on the manager's judgement.
Calls a later reader would otherwise re-derive:
- `kept` is defined as "none of the three above".
- The flag batch is one question, because clause 5 says "one batch".
- The H1 heading is "Triaging the open nodes and the outstanding flags" and not a bare "Triage". The cascade contract already uses "triage" as a role name.

INDEX LINE:    Ships `expedition-triage`, an invoked skill: check open nodes against the tree, sort them into moot, dropped, merged or kept, propose with flag settling in one payload, then act by graph-conventions procedures.

FLAGS:
ASSUMPTION: The name the condition fixes, `expedition-triage`, shares the word "triage" with the cascade contract's triage role (`.claude/skills/expedition-cascade/SKILL.md`, `## Triage`, `ROLE: triage`). Node 87's question also speaks of a "triage agent". I kept the name the condition fixes and titled the H1 "Triaging the open nodes and the outstanding flags", so that the skill's heading does not read as the cascade role. The glossary defines neither use. — Index: Node 372 kept the condition's name `expedition-triage` though the cascade contract already names a "triage" role, and titled the skill's heading to tell the two apart.
ASSUMPTION: I added two rules the condition does not demand, both from the cases the manager met while carrying out node 366's answer. First, a flag on a merged node that judges the clauses that move stays outstanding and settles at the receiving node's gate (the flag 89.1 case). Second, a flag entry with no id is settled by its `flags.md` line alone, plus a note from the manager on the node (the same note the manager wrote in commit 44588fca). Each is stated as a named change to the rule it alters, and neither contradicts a clause. — Index: Node 372's skill adds two cases node 366's carrying-out met, a flag that travels with merged clauses and a flag entry with no id, beyond what its condition demands.

NEW NODES:     none

INVALIDATIONS: none. The skill restates no rule it does not point at. Its two changes for one case each name the rule they change. Node 366's answer said triage "ships as an invoked skill", and this is that skill.

CONDITIONS:    I searched the 37 open or claimed nodes' conditions and questions for `triage`, `invoked skill`, `expedition-cleanup`, `expedition-standing-yes` and `expedition-triage`. Matches outside node 372:
- Nodes 41, 214, 219, 190, 80 and 371 only cite node 366 as a provenance line.
- Node 370's match was incidental.
- Node 87's question speaks of the cascade's "triage agent", a different thing, and this work does not change it.
No replacement clauses, and no open node's question changed.

MISSING FROM MAP: How the manager settled flags with no id during node 366's carrying-out was not in the map or in node 366. I found it in commit 44588fca's manager notes. The 89.1 case was found on nodes 89 and 371.

GATE PAYLOAD:
Checker run 1 findings, and what I changed:
- F1 (rule 6). I ran `grep -n -E 'settle|settles|stays outstanding'` in the worktree. It gave four hits: the description, the batch sentence, the 89.1 sentence and the no-id sentence.
  - 89.1 sentence: rewritten as "Where a merged node holds a flag, and the flag judges the clauses that move, leave the flag outstanding. This changes the rule under `## Flags` in your contract for this one case: the flag settles at the gate of the node that receives those clauses, and not at its own node's gate or node closing report."
  - No-id sentence: it also changes a rule, step 2 of `### Settle a flag`, which marks the flag on the node. It now reads "Where an older flag entry has no id to mark, this changes step 2 of `### Settle a flag`: settle the flag by its line in `flags.md` alone, and write a note of your own on its node saying so."
  - Description: it states no settling rule, and is unchanged.
  - Batch sentence ("Propose settling, in one batch, ..."): clause 5 of the condition dictates it, and it is the subject of the checker's question that goes to the human. As told, I did not act on that question, so this sentence is unchanged and does not name `## Flags`.
- F2 (rule 5). The pronoun's referent is now unambiguous: "Where a merged node holds a flag, and the flag judges the clauses that move". I read every ` that ` and ` which ` hit by hand:
  - "the clauses that move", "the node that receives those clauses", "text that no longer exists": each follows a single noun.
  - "so that": a conjunction.
  - "that node": a demonstrative.
  - "which nodes" and "which flags": interrogatives.
  None is ambiguous.
- Touched anything the condition names: only the file of clause 1, and only in the two flag sentences. Clauses 5 and 6 stay met: the batch and the flags it leaves outstanding are unchanged, and `### Settle a flag` is still named without its steps being restated.
- Bar: the repo has no build, tests, formatter or CI, which I confirmed at the worktree root. No line other than the description exceeds 110 characters. `git status` shows only the new file.
- Paths touched: `.claude/skills/expedition-triage/SKILL.md` (new). Nothing else.
- Proposed commit message:
  Ship the expedition-triage skill

  An invoked skill for the manager: check open nodes against the working tree, sort them into moot, dropped, merged or kept, propose them and the flag batch in one payload, then act by the graph-conventions procedures.

  Node: graph-workflow/372

RETROSPECTIVE
1. What I had to hunt for: how the manager handled the two cases in the spawn's note. For the flags with no id, the answer was in commit 44588fca's notes. For 89.1, it was in nodes 89 and 371. In this round, nothing.
2. What arrived that this node did not need: most of `map.md`'s history and standing preferences, and most of `map-implementation-rules.md` beyond the bar paragraph.
3. What would have made this easier: knowing up front that a case rule which departs from a shipped rule must name that rule's heading. Rule 6 says so, but I read it only as a rule about pointers. A spawn note naming commit 44588fca would also have helped.
4. What was stale, wrong or contradictory: the spawn said the old entries had "no marker position". The manager's note says they "carry no ids", so the gap is a missing id. Otherwise nothing.
````

### Checker run 3 — `PASS`

*The checker's own text, pasted, 2026-10-02, after correction round 2. The same checker, resumed within this node.*

> PASS
>
> Node 372, "Ship an `expedition-triage` skill", run 3, after correction round 2. I re-ran the bar in full and re-checked part 5, the part the edit touches. I read the whole file and compared it with my run 2 reading myself. The only change is the one sentence the worker named. It was appended to the first paragraph under `## Check the outstanding flags` and reads: "This changes the rule under `## Flags` in your contract for this one case: the human's approval of the batch is the moment its flags settle."
>
> Condition:
> 1–4, 6–7, 9. Met. Established in runs 1 and 2. The text they rest on did not change.
> 5. Met, re-checked. Both sentences are unchanged: "Propose settling, in one batch, the outstanding flags whose node is `resolved` or `superseded`" and "Leave outstanding the flags whose node is `open` or `claimed`". The added sentence only names the rule the batch changes, and does not contradict part 5.
> 8. Met, re-run. `git status --porcelain --ignored --untracked-files=all` printed only `?? .claude/skills/expedition-triage/SKILL.md`. `git diff 7fe98da3 --stat` printed nothing.
>
> Bar: the repo has no build, tests, formatter or CI, so the bar is the standards in map-implementation-rules.md. I read only the standards in that file.
> - Writing rule 6: the batch sentence now names `## Flags`, the rule it changes, and states the change in its own words.
> - Writing rule 5: "its flags" has one referent, "the batch". The sentence is grammatical and holds one idea.
> - glossary `_Avoid_`: the sentence uses none of the avoided words.
> - The other standards, `/writing-for-agents` and graph-conventions.md, were checked in runs 1 and 2. This sentence does not bear on them.
>
> My run 1 question is answered by the human's decision at the gate, and the work now follows the recommended option. I have no further questions.
>
> Not checked: nothing outside the one changed path. I read no part of the record.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 3 outcome, `PASS`. No exclusion applies: run 3 handed back no question and no raise, and left no part of the condition uncovered. Run 1's question was settled by the human at the gate above. This settles none of the node's flags; they settle at the node closing report.

## Handover, attempt 1, correction round 2

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Ship an `expedition-triage` skill (372) — correction round 2

ANSWER:
A new invoked skill, `.claude/skills/expedition-triage/SKILL.md`, writes down the triage that node 366 ran by hand. It is about 3 KB and follows the form of `expedition-cleanup` and `expedition-standing-yes`. Its front matter carries `name: expedition-triage` and a description saying the human invokes it in an expedition's manager thread to triage the open nodes and outstanding flags. It has four sections.
- `## Check each open node`: check against the current working tree and the current shipped files, and not against the record. The checking may go to read-only agents, and each one quotes the current text its finding rests on. The section defines the four classes moot, dropped, merged and kept. For a kept implementation node, the proposal says whether its condition quotes text that no longer exists.
- `## Check the outstanding flags`: one batch proposes settling the flags on `resolved` or `superseded` nodes. Flags on `open` or `claimed` nodes stay outstanding. The section names `## Flags` in SKILL.md and changes it for this case: the human's approval of the batch is the moment its flags settle. It also states the node 89.1 case, as a second named change to `## Flags`: a merged node's flag that judges the clauses that move stays outstanding, and settles at the gate of the node that receives those clauses.
- `## The proposal`: one payload, with one numbered question per class and one for the flag batch. Each question lists its nodes or flags with a one-line reason. No status or flag state changes before the human answers.
- `## After the human answers`: each act points by heading at `### Supersede`, `### Resolve`, `### Rule out of scope`, `### Amend an acceptance condition` and `### Settle a flag` in `graph-conventions.md`, and restates none of their steps. It also points at `### Changing one after it is written` in SKILL.md for which nodes may be amended. The no-id case is stated as a named change to step 2 of `### Settle a flag`: the flag is settled by its `flags.md` line alone, and the manager writes a note of its own on the node.
The skill's opening says it runs only when the human invokes it, and never on a schedule or on the manager's judgement.
Calls a later reader would otherwise re-derive:
- `kept` is defined as "none of the three above".
- The flag batch is one question, because clause 5 says "one batch".
- The H1 heading is "Triaging the open nodes and the outstanding flags", because the cascade contract already uses "triage" as a role name.
- The triage batch's settling moment is a change made for this one case in the skill. `SKILL.md`'s `## Flags` is left unedited, on the human's "ok for recommended" in correction round 2.

INDEX LINE:    Ships `expedition-triage`, an invoked skill: check open nodes against the tree, sort them into moot, dropped, merged or kept, propose with flag settling in one payload, then act by graph-conventions procedures.

FLAGS:
ASSUMPTION: The name the condition fixes, `expedition-triage`, shares the word "triage" with the cascade contract's triage role (`.claude/skills/expedition-cascade/SKILL.md`, `## Triage`, `ROLE: triage`). Node 87's question also speaks of a "triage agent". I kept the name the condition fixes and titled the H1 "Triaging the open nodes and the outstanding flags", so that the skill's heading does not read as the cascade role. — Index: Node 372 kept the condition's name `expedition-triage` though the cascade contract already names a "triage" role, and titled the skill's heading to tell the two apart.
ASSUMPTION: I added two rules the condition does not demand, both from the cases the manager met while carrying out node 366's answer. First, a flag on a merged node that judges the clauses that move stays outstanding and settles at the receiving node's gate (the flag 89.1 case). Second, a flag entry with no id is settled by its `flags.md` line alone, plus a note from the manager on the node (as in commit 44588fca). Each is stated as a named change to the rule it alters. — Index: Node 372's skill adds two cases node 366's carrying-out met, a flag that travels with merged clauses and a flag entry with no id, beyond what its condition demands.

NEW NODES:     none

INVALIDATIONS: none. Three passages change a shipped rule for the triage's own case, and each names that rule by heading: the batch's settling moment and the merged-flag case change `## Flags` in SKILL.md, and the no-id case changes step 2 of `### Settle a flag`. No shipped file is edited.

CONDITIONS:    I searched the 37 open or claimed nodes' conditions and questions for `triage`, `invoked skill`, `expedition-cleanup`, `expedition-standing-yes` and `expedition-triage`. Matches outside node 372:
- Nodes 41, 214, 219, 190, 80 and 371 only cite node 366 as a provenance line.
- Node 370's match was incidental.
- Node 87's question speaks of the cascade's "triage agent", a different thing, and this work does not change it.
No replacement clauses, and no open node's question changed.

MISSING FROM MAP: How the manager settled flags with no id during node 366's carrying-out was not in the map or in node 366. I found it in commit 44588fca's manager notes. The 89.1 case was found on nodes 89 and 371.

GATE PAYLOAD:
Correction round 2, on the human's "ok for recommended":
- The batch sentence under `## Check the outstanding flags` gains "This changes the rule under `## Flags` in your contract for this one case: the human's approval of the batch is the moment its flags settle."
- Clause 5's content is unchanged: one batch for flags on `resolved` or `superseded` nodes, and flags on `open` or `claimed` nodes left outstanding.
- This touches clause 5's passage only, and does not alter what clause 5 demands. Clause 6 stays met, and no other file is changed (clause 8).
Earlier rounds, kept:
- F1 (run 1): the merged-flag and no-id sentences name the rule they change.
- F2 (run 1): the pronoun is unambiguous.
- Bar: the repo has no build, tests, formatter or CI. No line other than the description exceeds 110 characters. `git status` shows only the new file.
- Paths touched: `.claude/skills/expedition-triage/SKILL.md` (new). Nothing else.
- Proposed commit message:
  Ship the expedition-triage skill

  An invoked skill for the manager: check open nodes against the working tree, sort them into moot, dropped, merged or kept, propose them and the flag batch in one payload, then act by the graph-conventions procedures. The human's approval of the flag batch is its settling moment, named as a change to SKILL.md's `## Flags` for this case.

  Node: graph-workflow/372

RETROSPECTIVE
1. What I had to hunt for: in this round, nothing.
2. What arrived that this node did not need: in this round, nothing.
3. What would have made this easier: in round 1, reading rule 6's last sentence as applying to every sentence that departs from a shipped rule, including one the condition dictates.
4. What was stale, wrong or contradictory: clause 5 of the condition alone conflicted with `## Flags` in SKILL.md. The named change for this case resolves that, without editing SKILL.md.
````

## Flags

`372.1` `ASSUMPTION` **· settled** — *The worker's own text.* The name the condition fixes, `expedition-triage`, shares the word "triage" with the cascade contract's triage role (`.claude/skills/expedition-cascade/SKILL.md`, `## Triage`, `ROLE: triage`). Node 87's question also speaks of a "triage agent". I kept the name the condition fixes and titled the H1 "Triaging the open nodes and the outstanding flags", so that the skill's heading does not read as the cascade role. The glossary defines neither use.

`372.2` `ASSUMPTION` **· settled** — *The worker's own text.* I added two rules the condition does not demand, both from the cases the manager met while carrying out node 366's answer. First, a flag on a merged node that judges the clauses that move stays outstanding and settles at the receiving node's gate (the flag 89.1 case). Second, a flag entry with no id is settled by its `flags.md` line plus a note from the manager on the node (the same note the manager wrote in commit 44588fca). Both are short, and neither contradicts a clause.

*The manager's note, 2026-10-02:* flags 372.1, 372.2 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
