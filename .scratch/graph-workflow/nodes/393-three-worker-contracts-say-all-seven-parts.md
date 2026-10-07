# Three worker contracts say "all seven parts" over a handover of eight

Type: implementation
Status: resolved
Blocked by: none

## Answer

No change: the three contracts' "all seven parts" was already right, because the shipped files count a handover's parts below the HANDOVER header (seven, plus the implementation worker's gate payload).

*The manager's note:* discharged with no edit, on the human's `verbatim` "ok" to the worker's raise. The worker's answer is under `## Handover, attempt 1`. The worktree held no change, so there was nothing to check or land. The node raised no flags.

## Question

This lets a grilling, prototype or precondition worker count its handover's parts correctly, so that a part is not dropped because the count is wrong. `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md` each say "Hand back all seven parts every time." Each lists eight parts in its handover shape: HANDOVER, ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, CONDITIONS and MISSING FROM MAP. The implementation contract already says "all eight parts".

*Reported by [node 40](40-flag-account-has-no-handover-part.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. It touches the same files as node 41, so it cannot run at the same time as node 41."*

## Acceptance condition

*Authored by node 40's worker and filed by the manager.*

> Done when all of the following hold.
> 1. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md`, the sentence that says how many parts the handover has states the number of parts that the file's handover shape lists.
> 2. No other text in those three files changes.
> 3. The working tree meets the bar.
> Scope: `grep -n "parts every time" .claude/skills/expedition-*/SKILL.md` over the working tree on 2026-10-06 returned four lines. The three files above say "seven" and `expedition-implementation/SKILL.md` says "eight". The implementation line is already correct and is not part of this work. An instance the search reaches outside this list is reported and not edited.

## Interview

#### Raise 1, relayed 2026-10-07

*Pasted as the worker handed it back.*

`````
NODE:          Three worker contracts say "all seven parts" over a handover of eight (node 393)
ABOUT:         Changes "Hand back all seven parts every time." in the grilling, prototype and precondition contracts. The change is made in the worktree and left unreverted, but the node's premise looks wrong: "seven" is already the count the rest of the shipped files use.
SO FAR:        I read the node, the implementation contract, map.md, map-implementation-rules.md and the decisions.md lines that matched. In /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/393-part-count, the edit "seven" -> "eight" sits on line 220 of .claude/skills/expedition-grilling/SKILL.md, line 151 of expedition-prototype/SKILL.md and line 156 of expedition-precondition/SKILL.md. These are the only changes, and they are uncommitted. I made the edit before I found the conflict below. Under the raise rule it stays as it is, and reverting it is three one-word changes.
               The conflict:
               (a) The implementation contract's handover shape has nine labelled lines: HANDOVER, ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, CONDITIONS, MISSING FROM MAP, GATE PAYLOAD. It still says "Write all eight parts". So the shipped convention does not count the `HANDOVER:` header line as a part.
               (b) .claude/skills/expedition/SKILL.md, bullet "A handover has seven parts every time", lists those seven parts (answer, index line, flags, nodes surfaced, INVALIDATIONS, CONDITIONS, MISSING FROM MAP) and adds "An implementation worker returns an eighth, the gate payload." decisions.md's line for node 335 says the glossary was meant to say the same, but the glossary's `Handover` entry no longer carries a count.
               (c) Under that convention, each of the three contracts lists seven parts after its HANDOVER header, so "seven" is already right. The node's question counts HANDOVER as a part to reach eight. That clashes with the implementation contract, whose count the node itself calls "already correct". If I ship "eight", the three contracts contradict SKILL.md's bullet and use a different counting rule from the implementation contract.
               Clause 1, "the number of parts that the file's handover shape lists", is therefore unmeasurable: whether the HANDOVER line counts as a part is exactly the open point. That is trigger 1 (the acceptance condition is not mine to fix).
               Also: the scope search `grep -n "parts every time" .claude/skills/expedition-*/SKILL.md` returns three lines over this tree at e6f079e03, not four. The implementation sentence wraps between "all" and "eight", so the grep does not reach it. This is harmless to the work.
               The bar: the repo states no build, test or format commands (no manifest and no CLAUDE.md or AGENTS.md at the root), which matches the copy in map-implementation-rules.md. The bar is therefore the standards and the condition.
ASK:           Do I revert the three edits and resolve the node as "no change needed", since "seven" matches SKILL.md's bullet and the implementation contract's convention that HANDOVER is the header and not a part?
RECOMMENDED:   Revert, and resolve the node with no change. This rests on (a)-(c): the shipped files agree that a handover has seven parts plus a gate payload for implementation, and only the node's question disagrees. The defect reported by node 40's worker comes from counting the header line.
ALTERNATIVES:  - Keep "eight" (HANDOVER counts as a part). This also needs the implementation contract changed to "nine" and SKILL.md's bullet changed, which is outside this condition and would need a widened or new node.
               - Make the three sentences unambiguous without changing the number (for example, "all seven parts below the HANDOVER line"). Clause 2 forbids any text change beyond the number, so the condition would have to be amended.

RETROSPECTIVE
1. What I had to hunt for:
   - `count-wrong-when-written` (carried by 2 earlier retrospectives: nodes 135, 40). The fact was the counting convention. I found it in .claude/skills/expedition/SKILL.md's bullet "A handover has seven parts every time" by grepping the shipped files for "seven parts". I first looked at the three contracts' shapes, which seemed to confirm the node's premise until I counted the implementation shape's labels. Node 40's worker wrote the count wrong when it wrote the condition.
   - `condition-scope-misplaces-a-match` (carried by 1 earlier retrospective: node 317). The condition says the grep returns four lines, but it returns three, because the implementation sentence wraps at "all / eight".
2. What arrived that the node did not need:
   - `map-read-whole-for-a-few-items` (carried by 18 earlier retrospectives, including nodes 40, 41, 392). None of map.md bore on a three-word change.
   - `rules-file-read-whole-for-one-section` (carried by 15 earlier retrospectives, including nodes 40, 41, 392). Only the bar's commands paragraph mattered.
3. What would have made it easier: a premise check by whoever files a count-fix node, comparing the count against every shipped statement of the same count (here SKILL.md's bullet and the implementation contract's own label count) before writing the condition.
4. Stale, wrong or contradictory: the node's question and condition (eight parts, four grep lines) contradict SKILL.md's "seven parts ... an eighth, the gate payload". decisions.md's line for node 335 says the glossary's `Handover` entry lists the seven parts, but the current glossary entry has no count. Either the line is stale or the glossary text it describes was later removed.
`````

#### The human's answer to raise 1, 2026-10-07

`verbatim`: *"ok"*

*The manager's note:* the manager's message ended "Please answer node 393. \"ok for recommended\" reverts and closes it with no change.", so the reply takes the worker's `RECOMMENDED`: "Revert, and resolve the node with no change." No divergence.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-07.*

`````
HANDOVER:      Three worker contracts say "all seven parts" over a handover of eight (node 393)
ANSWER:        No change was needed. In the grilling, prototype and precondition contracts, "Hand back all seven parts every time." is already correct under the counting rule the shipped files use. That rule does not count the `HANDOVER:` header line as a part. The implementation contract's handover shape has nine labelled lines (HANDOVER, ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, CONDITIONS, MISSING FROM MAP, GATE PAYLOAD) and says "all eight parts". `.claude/skills/expedition/SKILL.md`'s bullet "A handover has seven parts every time" lists the seven parts below the header and adds "An implementation worker returns an eighth, the gate payload." Each of the three contracts lists exactly those seven parts below its header. The node's premise of eight parts came from counting the header line. The scope search in the condition also misstated what it returns: `grep -n "parts every time" .claude/skills/expedition-*/SKILL.md` returns three lines, not four. The implementation contract's sentence wraps between "all" and "eight", so the grep does not reach it. A worker briefly edited the three sentences to "eight". The human answered "ok" to the raise recommending a revert, and the edits were reverted, so the tree holds no change.
INDEX LINE:    No change: the three contracts' "all seven parts" was already right, because the shipped files count a handover's parts below the HANDOVER header (seven, plus the implementation worker's gate payload).
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: none. Node 40's NEW NODES block and its retrospective item `count-wrong-when-written` describe the three contracts as saying seven over a handover of eight. This node's answer shows that description is wrong. It is a correction to a report and changes no resolved answer's rule.
CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of open and claimed nodes, and the resolved nodes' `## Answer` and `## Acceptance condition` sections, for "seven parts", "eight parts" and "parts every time". Among open or claimed nodes, only node 393 itself and node 41 matched. Node 41's match is its own note "Node 393 is unaffected: its 'all seven parts' sentences were not edited", which still holds. No replacement clauses and no changed questions.
MISSING FROM MAP: none
GATE PAYLOAD:  The checker has not run, so there are no findings. The worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/393-part-count holds no change: `git status --short` prints nothing after the three edits were reverted. No paths are left changed. The paths that were touched and then restored are .claude/skills/expedition-grilling/SKILL.md, .claude/skills/expedition-prototype/SKILL.md and .claude/skills/expedition-precondition/SKILL.md. The bar's commands: the repo states none, which matches map-implementation-rules.md. No commit is proposed, since there is nothing to land.

RETROSPECTIVE
- `condition-scope-misplaces-a-match` (carried by 1 earlier retrospective: node 317). New since the raise: the misstated grep line count also passed through the manager's filing unchecked, which is a second instance in the same node.
- `count-wrong-when-written` (carried by 2 earlier retrospectives: nodes 135, 40). New since the raise: the miscount that produced this node was in node 40's NEW NODES, and the effort's only other statement of the count (SKILL.md's "seven parts" bullet) would have caught it there. Nothing new beyond the items in the raise's retrospective.
`````
