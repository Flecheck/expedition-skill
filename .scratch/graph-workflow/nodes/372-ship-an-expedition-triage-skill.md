# Ship an `expedition-triage` skill

Type: implementation
Status: claimed
Blocked by: none

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

## Flags

`372.1` `ASSUMPTION` — *The worker's own text.* The name the condition fixes, `expedition-triage`, shares the word "triage" with the cascade contract's triage role (`.claude/skills/expedition-cascade/SKILL.md`, `## Triage`, `ROLE: triage`). Node 87's question also speaks of a "triage agent". I kept the name the condition fixes and titled the H1 "Triaging the open nodes and the outstanding flags", so that the skill's heading does not read as the cascade role. The glossary defines neither use.

`372.2` `ASSUMPTION` — *The worker's own text.* I added two rules the condition does not demand, both from the cases the manager met while carrying out node 366's answer. First, a flag on a merged node that judges the clauses that move stays outstanding and settles at the receiving node's gate (the flag 89.1 case). Second, a flag entry with no id is settled by its `flags.md` line plus a note from the manager on the node (the same note the manager wrote in commit 44588fca). Both are short, and neither contradicts a clause.
