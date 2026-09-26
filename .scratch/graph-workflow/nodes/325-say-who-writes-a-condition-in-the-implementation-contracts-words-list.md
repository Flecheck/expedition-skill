# Say who writes a condition in the implementation contract's words list

Type: implementation
Status: resolved
Blocked by: none

## Question

`.claude/skills/expedition-implementation/SKILL.md`, under `## Words used exactly`, defines **acceptance condition** as "what done means for your node, written by the node that spawned yours before you started". A node the manager created has no spawning node, and this node, 318, is one. So the definition is false for every manager-created node. The same phrase in the five contracts' `## When a node you report is an implementation node` sections is correct in place, because there the reporting worker's node is the spawning node.

*Reported by [node 318](318-say-who-writes-a-condition-in-the-glossary-and-the-node-template.md)'s worker, which gave it no blockers. "This node, 318" in the question above is that worker's node.*

## Acceptance condition

*Authored by node 318's worker and filed by the manager.*

1. In `.claude/skills/expedition-implementation/SKILL.md`, the `**acceptance condition**` bullet under `## Words used exactly` no longer says without qualification that the condition was written by the node that spawned yours. It says that the agent that created your node wrote the condition, or the manager where the manager created your node, before you started. It still says the worker leaves the condition as written and may not rewrite it.
2. No other text in that file changes, and no other path changes.
3. The working tree meets the bar.

## Answer

The implementation contract's words-list entry for acceptance condition now says the agent that created the node wrote it, or the manager where the manager created it.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `c3ecda3`. The node the worker surfaced is [node 326](326-say-who-writes-a-condition-in-the-five-contracts-reporting-sections.md).

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Say who writes a condition in the implementation contract's words list

ANSWER:        In `.claude/skills/expedition-implementation/SKILL.md`, under `## Words used exactly`, the `**acceptance condition**` bullet now reads: "what done means for your node, written before you started by the agent that created your node, or by the manager where the manager created your node. Leave it as written. You may not rewrite it." It replaces "written by the node that spawned yours before you started", which was false for every node the manager created. The wording follows node 318's glossary entry and uses "created" rather than the manager contract's "minted", as 318 did. "your node" is repeated where "it" would have been shorter, because "it" could have pointed at either the node or the condition, and standing rule 5 asks for one clear referent per pronoun. The bullet keeps the file's wrap width of about 105 columns and now runs to three lines. The sentence in `## When a node you report is an implementation node`, "written by the node that spawned it", was left alone as clause 2 requires. It is reported under NEW NODES.

INDEX LINE:    The implementation contract's words-list entry for acceptance condition now says the agent that created the node wrote it, or the manager where the manager created it.

FLAGS:         none

NEW NODES:     Name: Say who writes a condition in the five contracts' reporting sections
               Kind: implementation
               Question: In all five worker contracts, `## When a node you report is an implementation node` opens with a general statement: "An `implementation` node can be claimed only once it carries an **acceptance condition**: what done means for that node, written by the node that spawned it, before any work on it starts." Read alone, as a definition of every implementation node, it is false for a node the manager created. Node 325's own question judged this phrase "correct in place", because the next sentence says the reporting worker's node is the spawning node. That second sentence is correct. The opening sentence, though, makes a claim about every implementation node. Should it be qualified the way the glossary (node 318) and the implementation words list (node 325) were? This node overlaps node 325's question text, so the human may judge it unneeded.
               Blockers: none
               Acceptance condition:
               1. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-research/SKILL.md`, the first sentence under `## When a node you report is an implementation node` no longer says without qualification that an implementation node's acceptance condition is written by the node that spawned it. It says the condition is written before any work on the node starts, by the agent that created the node, or by the manager where the manager created it.
               2. In each of those five files, the sentence saying that when you report one, your node is the one that spawned it, and that you write its condition in the `NEW NODES` block, is unchanged.
               3. No other text in those five files changes, and no other path changes.
               4. The working tree meets the bar.

INVALIDATIONS: none

GATE PAYLOAD:  Checker findings: none yet (the checker has not run).
               Paths touched (in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/325-condition-words-list): `.claude/skills/expedition-implementation/SKILL.md` only. `git status --short` shows that file alone.
               Bar: I checked the recorded bar against the repo and it matches. The worktree root holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`. There is no manifest, task runner, formatter config or CI, so no commands exist to run. What remains is the non-command half. `git diff --check` is clean. The new lines are 104, 104 and 17 columns, within the file's wrap. No `_Avoid_` word in `CONTEXT.md` is used. The wording is plain and has one referent per pronoun.
               Method skills: none invoked, so nothing was skipped.
               Proposed commit message:
                 Say who writes a condition in the implementation contract's words list

                 Node: graph-workflow/325

RETROSPECTIVE:
1. What I had to hunt for: nothing of substance. The exact wording 318 landed came from `git show 3529bec`, because the spawn named the word "created" but not the full sentence. Quoting the landed glossary sentence in the spawn would have saved that one command.
2. What arrived that this node did not need: most of `map.md`, since only its Notes on sources and ground rules bear on a one-bullet edit. The rest of `map-implementation-rules.md` beyond the bar paragraph, the ground rules and the writing rules: the record-as-work rule and the supersession rules did not apply here. In `decisions.md`, only the line for node 39 and the line for node 318 mattered, and grep found them.
3. What would have made this easier: the spawn could quote 318's landed glossary sentence. It could also say whether the node-325 question's claim that the reporting sections are "correct in place" is settled or open, because that claim decides whether the line-234 sentence is a finding or a non-issue.
4. What was stale, wrong or contradictory: node 325's question says the phrase in the five reporting sections is "correct in place". Only the second sentence there is correct. The first sentence is a general definition that is false for manager-created nodes, as reported under NEW NODES. The question also says "this node, 318" inside node 325's file. Its italic note explains that, but it reads wrongly at first.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 309's check, and resumed again after a usage limit stopped it mid-check.*

> PASS
>
> Node 325, "Say who writes a condition in the implementation contract's words list", meets all three parts of its acceptance condition, and the bar holds. The work rewrites one bullet in the implementation contract, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `.claude/skills/expedition-implementation/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/325-condition-words-list`, on branch `worktree-325-condition-words-list`, with HEAD and merge-base both at `3529bec`. I read the changed path only as the work.
>
> After the usage limit I re-checked the worktree myself. It still shows only that one file modified, with the same 3 lines added and 2 removed that I read before the stop.
>
> **Part by part**
> 1. **The bullet names who wrote the condition: met.**
>    - Under `## Words used exactly`, the `**acceptance condition**` bullet went from "what done means for your node, written by the node that spawned yours before you started."
>    - It now reads "what done means for your node, written before you started by the agent that created your node, or by the manager where the manager created your node."
>    - That states both cases and keeps "before you started". The unqualified "written by the node that spawned yours" is gone from the bullet.
>    - It still says "Leave it as written. You may not rewrite it."
> 2. **No other text or path changes: met.**
>    - `git diff --numstat` shows 3 lines added and 2 removed, all within this bullet.
>    - `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition-implementation/SKILL.md` modified. That matches the worker's report, which I checked rather than relied on.
>    - The contract's shared section `## When a node you report is an implementation node` is outside the edit. It still reads as it did before, so it stays identical to the other worker contracts.
> 3. **The working tree meets the bar: met**, as below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the new wording is plain.
>   - `CONTEXT.md`'s `_Avoid_` lines: no refused word is introduced.
>   - All five ground rules, which are met.
> - Master has moved to `c52c03e`, which I was told changes only `.claude/skills/expedition/SKILL.md`. I checked against the branch's own base, as the before-state, and did not check the rebase that will happen at landing.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*
