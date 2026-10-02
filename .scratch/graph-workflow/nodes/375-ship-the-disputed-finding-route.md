# Ship the disputed-finding route into the implementation and manager contracts

Type: implementation
Status: resolved
Blocked by: none

## Answer

The implementation and manager contracts now let a worker leave a checker finding it believes false unfixed, give its reason in GATE PAYLOAD, and have the human settle it at the gate.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `0f8401da`. Flag 375.1 settles at the node closing report.

## Question

Carry node 34's answer into the shipped files.

*Reported by [node 34](34-implementer-disputes-a-finding.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none".*

## Acceptance condition

*Authored by node 34's worker and filed by the manager.*

> 1. In `.claude/skills/expedition-implementation/SKILL.md`, under `## After the code is written`, the diagram line `    → the checker checks it → you fix everything it found → the checker runs again` reads `    → the checker checks it → you fix what it found → the checker runs again`. No other line of the diagram changes.
> 2. In the same section, the sentence "Fix all of it before the gate." is replaced by text saying all of the following, in plain English: fix everything the checker found before the gate, except a finding you believe is false; leave that finding unfixed and say in `GATE PAYLOAD` why you believe it is false; the human settles it at the gate; a finding the human upholds arrives as a correction round.
> 3. In the same section, the sentence "Never leave the finding unfixed at the gate on your own authority." is replaced by a sentence saying that no other finding is left unfixed on the worker's own authority. The paragraph about a fix that would be a new piece of work, raised under trigger 1, otherwise stays as it is.
> 4. In the same file, under `## What you hand back`, the `GATE PAYLOAD` part of the handover shape starts `<for each thing the checker found, what you changed, or why you left it unfixed;` and the rest of that part is unchanged.
> 5. In `.claude/skills/expedition/SKILL.md`, under `### The payload`, the bullet "What the worker changed for each thing the checker found, in the worker's own words." reads "What the worker changed for each thing the checker found, or why it left it unfixed, in the worker's own words."
> 6. In `.claude/skills/expedition/SKILL.md`, under `## What nothing here settles`, the numbered item that begins "What does a worker do with a finding it believes is false?" is removed. The items after it are renumbered so the list is numbered consecutively from 1. No other item's text changes.
> 7. `.claude/skills/expedition-checker/SKILL.md` and `.claude/skills/expedition/glossary.md` are not changed by this work.
> 8. Scope: no search was run to find these places. They are the work itself, not instances of a defect. A search of `.claude/skills` for the phrases "Fix all of it", "fix everything it found" and "for each thing the checker found" returned only the lines named above (2026-10-02). If the checker or worker finds another place outside this list that needs the same change, it reports that place and does not edit it.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Ship the disputed-finding route into the implementation and manager contracts
ANSWER:        Node 34's route now ships in two contracts. A worker that believes a checker finding is false leaves it unfixed, says why in `GATE PAYLOAD`, and the human settles it at the gate.
               `.claude/skills/expedition-implementation/SKILL.md`, `## After the code is written`:
               - The diagram line now reads "you fix what it found". No other diagram line changed.
               - "Fix all of it before the gate." is replaced by four sentences: "Fix everything it found before the gate, except a finding you believe is false. Leave that finding unfixed, and say in `GATE PAYLOAD` why you believe it is false. The human settles it at the gate. A finding the human upholds arrives as a correction round."
               - In the trigger-1 paragraph, "Never leave the finding unfixed at the gate on your own authority." is replaced by "Apart from a finding you believe is false, leave no finding unfixed on your own authority." The rest of that paragraph is unchanged. The wording uses "Apart from a finding you believe is false" instead of the bare "no other finding" in node 34's draft. In that paragraph, "other" would seem to point at the new-work finding the paragraph is about (see the flag).
               `## What you hand back`: the `GATE PAYLOAD` part now starts "<for each thing the checker found, what you changed, or why you left it unfixed;". The rest of its words are unchanged, but the lines are reflowed to fit the block's width.
               `.claude/skills/expedition/SKILL.md`:
               - The `### The payload` bullet now reads "What the worker changed for each thing the checker found, or why it left it unfixed, in the worker's own words.", wrapped over two lines.
               - Under `## What nothing here settles`, the item "What does a worker do with a finding it believes is false? …" is removed. Old items 4 to 6 are now 3 to 5, with their text unchanged.
               - A search of `.claude/` found no other file that cites these items by number.
               The checker contract and the glossary are untouched.
INDEX LINE:    The implementation and manager contracts now let a worker leave a checker finding it believes false unfixed, give its reason in GATE PAYLOAD, and have the human settle it at the gate.
FLAGS:         ASSUMPTION: Condition clause 3 asks for a sentence saying no other finding is left unfixed on the worker's own authority. Node 34's draft said "Leave no other finding unfixed on your own authority." That sentence sits in the paragraph about a fix that would be a new piece of work, so there "other" would seem to mean "other than the new-work finding" rather than "other than a finding you believe is false". I wrote "Apart from a finding you believe is false, leave no finding unfixed on your own authority." It says the same thing with one clear referent, which follows standing writing rule 5. I also dropped "at the gate" from the old sentence, because the new sentence covers the whole time before the gate. The `GATE PAYLOAD` part was reflowed across three lines, and its words after the new opening are unchanged. Index: Node 375 worded the "no other finding" sentence as "Apart from a finding you believe is false, leave no finding unfixed on your own authority", so its referent is clear inside the trigger-1 paragraph.
NEW NODES:     none
INVALIDATIONS: none. This carries node 34's answer into the shipped files. In the manager contract, the items in `## What nothing here settles` after the removed one are renumbered: old 4, 5, 6 are now 3, 4, 5. A search of `.claude/` and of the open nodes found no citation of them by number.
CONDITIONS:    I searched all 32 open or claimed node files for "Fix all of it", "fix everything it found", "for each thing the checker found", "on your own authority", "believes is false", "believe is false", "What nothing here settles", "item [3-6] of" and "unfixed". Only this node's own condition matched. No replacements are owed, and no open node's question changes.
MISSING FROM MAP: none
GATE PAYLOAD:  The checker has not run yet, so there are no findings.
               Paths touched (worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/375-disputed):
               - .claude/skills/expedition-implementation/SKILL.md
               - .claude/skills/expedition/SKILL.md
               The bar: the repo has no build, no tests and no formatter. This matches map-implementation-rules.md, and I confirmed it by finding nothing to invoke. I added no line over the files' existing width. The long lines already in both files were there before.
               Method skills: none invoked.
               Proposed commit message:
               "Let a worker leave a checker finding it believes false unfixed, reasoned in the gate payload

               The human settles the finding at the gate, and one they uphold returns as a correction round. Removes the matching open item from the manager contract's `What nothing here settles`.

               Node: graph-workflow/375"

RETROSPECTIVE
1. What I had to hunt for: very little. Clause 6 needed a check that nothing cites the `What nothing here settles` items by number. Node 34's worker said it had checked, and I re-ran the search.
2. What arrived that this node did not need: almost all of map.md and map-implementation-rules.md. Only the ground rules, the writing rules and "no build, tests or formatter" bore on the work. Node 34's draft wording was mildly useful.
3. What would have made this easier: nothing much. The condition quoted every sentence to change, which made the work mechanical.
4. What was stale, wrong or contradictory: nothing stale. In clause 3, "no other finding" would have had an unclear referent once placed in the trigger-1 paragraph. I worded around it and flagged it.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c375.md`.*

> PASS
>
> Work: the uncommitted diff in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/375-disputed (`git -C <worktree> diff`). The worktree is based on e6114e45. I read the two changed paths as the work.
>
> 1. The diagram line. `grep -n "the checker checks it →" .claude/skills/expedition-implementation/SKILL.md` returns only line 177, `    → the checker checks it → you fix what it found → the checker runs again`. Running `git diff -U0` on that file shows the diagram's only -/+ pair is this line, so no other diagram line changed. Met.
> 2. The "Fix all of it" sentence is replaced. The diff hunk at lines 186-190 reads: "Fix everything it found before the gate, except a finding you believe is false. Leave that finding unfixed, and say in `GATE PAYLOAD` why you believe it is false. The human settles it at the gate. A finding the human upholds arrives as a correction round." I unwrapped it and checked it against the four required elements. All four are present. The sentences that follow it ("The checker's outcomes are `PASS` and `FAIL`...") are unchanged in wording and only rewrapped. Met.
> 3. The "Never leave..." sentence is replaced by "Apart from a finding you believe is false, leave no finding unfixed on your own authority." This says that no other finding is left unfixed. The `-U0` diff shows the trigger-1 paragraph's other sentences are untouched. Met.
> 4. GATE PAYLOAD. The diff shows the part now starts `<for each thing the checker found, what you changed, or why you left it unfixed;`. I unwrapped the rest ("the paths you actually touched; a proposed commit message carrying the trailer `Node: <effort>/NN`>"). It matches the old wording word for word and was only rewrapped. Met.
> 5. The `### The payload` bullet in .claude/skills/expedition/SKILL.md line 287 unwraps to "What the worker changed for each thing the checker found, or why it left it unfixed, in the worker's own words." It matches exactly. Met.
> 6. `## What nothing here settles`. The diff removes the three lines of the "What does a worker do with a finding it believes is false?" item. Old items 4, 5 and 6 changed only their number prefix, to 3, 4 and 5. `sed -n 795,825p` shows the list now runs 1 to 5 with no gaps. No other item's text changed. Met.
> 7. `git status --porcelain` lists only the two changed SKILL.md files, so expedition-checker/SKILL.md and expedition/glossary.md are unchanged. Met.
> 8. The scope search the condition records. I ran `git grep -n -E "Fix all of it|fix everything it found|for each thing the checker found" e6114e45 -- .claude/skills` against the base. It returned 4 lines: the impl diagram line, the impl "Fix all of it" line, the impl GATE PAYLOAD line, and the expedition payload bullet. That matches the condition's claim that the search returned only the places it names. The same grep on the worktree returns only the two new "for each thing the checker found" lines. Nothing outside the list needed the same change: `grep -rn -i -E "\bfix(es|ed)? (all|every)|unfixed|all of it" .claude/` found nothing else relevant. The work edited no file outside the condition's list.
>
> The bar:
> - Build, warnings, formatting and tests: the repo has no agent-instruction file at its root (no CLAUDE.md or AGENTS.md) and no manifest, test suite or formatter. That matches the bar's commands recorded in map-implementation-rules.md. The bar is therefore its non-command half.
> - Formatting consistency: the added lines are 12 to 106 characters wide (`git diff -U0 | grep '^+[^+]' | awk ...`), within the files' existing wrap widths.
> - Standards: I read only the standards in .scratch/graph-workflow/map-implementation-rules.md. They are /coding-principles, /naming, glossary.md's `_Avoid_` lines, the ground rules, the six standing rules for writing, graph-conventions.md and /writing-for-agents. Three bore on this work, and none is breached:
>   - The writing rules: plain English, one idea per sentence, and the rule stated as what to do.
>   - The ground rules. Rule 3 holds because "The human settles it at the gate" tells no agent to address the human. Rules 1, 2 and 4 hold.
>   - The `_Avoid_` lines. `grep -n -i '_Avoid_' glossary.md | grep -E 'find|uphold|unfix|settle|false|authority|dispute|fix'` returned no refusal that touches the new wording.
> - Trigger-mirror rule: the edits are under `## The gate` / `### The payload` and `## What nothing here settles`. Neither is `## The order you act in` or `## What is in front of the human, and when`, so .claude/rules/expedition-triggers.md owed no change.
> - No reviewing skill is named for this repo, so I ran none. I held /writing-for-agents and /coding-principles by hand rather than invoking them.
> - The work does not move any standard: none of the changed paths is a standards file.
>
> What I left unread: the node file and the rest of the record. In the rules file I read only the standards.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and left no part of the condition uncovered. This settles none of the node's flags; they settle at the node closing report.

## Flags

`375.1` `ASSUMPTION` **· settled** — *The worker's own text.* Condition clause 3 asks for a sentence saying no other finding is left unfixed on the worker's own authority. Node 34's draft said "Leave no other finding unfixed on your own authority." That sentence sits in the paragraph about a fix that would be a new piece of work, so there "other" would seem to mean "other than the new-work finding" rather than "other than a finding you believe is false". I wrote "Apart from a finding you believe is false, leave no finding unfixed on your own authority." It says the same thing with one clear referent, which follows standing writing rule 5. I also dropped "at the gate" from the old sentence, because the new sentence covers the whole time before the gate. The `GATE PAYLOAD` part was reflowed across three lines, and its words after the new opening are unchanged.

*The manager's note, 2026-10-02:* flag 375.1 settles at the node closing report that closes this node, which names its gate as taken under the standing yes.
