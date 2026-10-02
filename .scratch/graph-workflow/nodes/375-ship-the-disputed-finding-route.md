# Ship the disputed-finding route into the implementation and manager contracts

Type: implementation
Status: claimed
Blocked by: none

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
