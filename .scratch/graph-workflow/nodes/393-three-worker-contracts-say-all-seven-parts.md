# Three worker contracts say "all seven parts" over a handover of eight

Type: implementation
Status: open
Blocked by: none

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
