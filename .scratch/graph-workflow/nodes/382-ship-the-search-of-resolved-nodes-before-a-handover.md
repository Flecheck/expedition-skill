# Ship the search of resolved nodes before a handover

Type: implementation
Status: open
Blocked by: none

## Question

Carry node 37's answer into the five worker contracts and the manager contract: a worker searches the resolved nodes' `## Answer` and `## Acceptance condition` sections for its work's handles before handing back, and reports what it changes in `INVALIDATIONS`.

*Reported by [node 37](37-invalidations-is-not-a-check.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. Sequencing only, because the code slot is shared: node 379 (at its gate) edits `## What nothing here settles` in `.claude/skills/expedition/SKILL.md`, and node 380 (open) edits a different sentence of the same five worker contracts. Not joined to node 380: it is the same files but a different concern (what a worker checks in its spawn), so this is new work rather than a defect of that node."*

## Acceptance condition

*Authored by node 37's worker and filed by the manager.*

> The work is these six files, and no other file may be edited:
>   `.claude/skills/expedition-grilling/SKILL.md`
>   `.claude/skills/expedition-research/SKILL.md`
>   `.claude/skills/expedition-prototype/SKILL.md`
>   `.claude/skills/expedition-precondition/SKILL.md`
>   `.claude/skills/expedition-implementation/SKILL.md`
>   `.claude/skills/expedition/SKILL.md`
> These are files the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file.
>
> Scope came from two searches over the working tree, run on 2026-10-04. `grep -l "^Before you write your handover, search the open nodes'" .claude/skills/*/SKILL.md` returned exactly the five worker contracts listed above. `grep -rln "Does anything tell a worker to look at the record" .claude/` returned exactly `.claude/skills/expedition/SKILL.md`. If either search reaches a file outside this list when the work is done, report it and do not edit it.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In each of the five worker contracts, the paragraph beginning "Before you write your handover, search the open nodes' `## Acceptance condition` sections" gains one sentence. The sentence is placed immediately after the sentence "Search the open nodes' `## Question` sections the same way, for the same words, paths and phrases, in every open node, claimed or not, and read only what matches." and immediately before "Name in `CONDITIONS` what you searched for." The added sentence is exactly: "Search the resolved nodes' `## Answer` and `## Acceptance condition` sections the same way, for the same words, paths and phrases, read only what matches, and report in `INVALIDATIONS` each resolved node your work changes." Line wrapping may differ. The words may not.
> 2. The paragraph named in clause 1 is byte-identical across the five worker contracts after the work, as it was before.
> 3. In each of the five worker contracts, no other sentence changes. In particular, the handover block's line beginning `INVALIDATIONS:`, the sentence "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them.", and the sentence beginning "In `INVALIDATIONS`, an outright contradiction is the minority case" are unchanged. Re-wrapping the lines of the paragraph named in clause 1 to fit the added sentence is not a change of sentence.
> 4. In `.claude/skills/expedition/SKILL.md`, under `## What nothing here settles`, the numbered item beginning "Does anything tell a worker to look at the record when it reports what its work invalidates?" is removed with all of its sentences. The items after it are renumbered in their existing order, so the list's numbers run from 1 with no gap. Every other item keeps its words.
> 5. In `.claude/skills/expedition/SKILL.md`, nothing outside the change in clause 4 changes. The file does not grow, counting lines as `wc -l` prints them, compared with the commit the work starts from.
> 6. No file under `.scratch/` changes, and `.claude/skills/expedition-checker/SKILL.md` and `.claude/skills/expedition-cascade/SKILL.md` do not change.
> 7. The tree meets the bar.
