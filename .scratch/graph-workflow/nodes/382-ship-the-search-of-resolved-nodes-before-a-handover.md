# Ship the search of resolved nodes before a handover

Type: implementation
Status: claimed
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

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-05.*

`````
HANDOVER:      Ship the search of resolved nodes before a handover
ANSWER:        Node 37's answer is now in the shipped files. In each of the five worker contracts (grilling, research, prototype, precondition, implementation), the paragraph that begins "Before you write your handover, search the open nodes' `## Acceptance condition` sections" has one new sentence. It sits between the sentence that searches the open nodes' `## Question` sections and the sentence "Name in `CONDITIONS` what you searched for." The new sentence reads: "Search the resolved nodes' `## Answer` and `## Acceptance condition` sections the same way, for the same words, paths and phrases, read only what matches, and report in `INVALIDATIONS` each resolved node your work changes." The paragraph's lines are kept unchanged up to the line holding the anchor sentence. From there to the end of the paragraph the lines are re-filled greedily at 105 columns, and no code span is split across lines. The paragraph is byte-identical across the five contracts (same md5 in all five, before and after). Nothing else in those files changes. Their `INVALIDATIONS:` handover line, "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them.", and the "In `INVALIDATIONS`, an outright contradiction is the minority case" sentence are untouched. In `.claude/skills/expedition/SKILL.md`, under `## What nothing here settles`, item 2 ("Does anything tell a worker to look at the record when it reports what its work invalidates?", five lines) is removed, and the old items 3 and 4 are renumbered 2 and 3. The file goes from 824 to 819 lines.
INDEX LINE:    The five worker contracts now tell a worker to search resolved nodes' Answer and condition sections before handing back and report what it changes in INVALIDATIONS. The manager contract's matching open question is removed.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: - Node 337, a contradiction that node 37 decided on purpose. Its condition clause 13 required that the `## What nothing here settles` item "Does anything tell a worker to look at the record…" still stand as an unsettled question, stating that no general duty over the record exists. This work removes that item, and the worker contracts now carry a duty over resolved nodes.
- Node 362, a narrowing. Its answer's Tier 2 item 22 measures `## What nothing here settles` "item 4" ("One bounded class does carry a duty to look … states that duty.", 30 words) as a pointer that summarises its target. That passage no longer exists, so the measurement no longer applies. The item number was already stale after node 379.
- Node 76, a stale count made staler. Its answer says `What nothing here settles` "carries nine open questions". The list now holds three.
- Node 37, an extension. This work carries out its answer. Nothing in that answer is contradicted.
- Node 350, an extension. The paragraph its condition (a) shaped gains one more search sentence. Its demand still holds.
CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open or claimed node (32, 40, 41, 135, 149, 170, 185, 209, 214, 317, 386, 387, 388, 389) for these handles: "Does anything tell a worker to look", "What nothing here settles", "INVALIDATIONS", "Before you write your handover", "resolved nodes' `## Answer`", "duty to look", and the six paths. Results:
- Node 387: matches only in a pasted handover's `INVALIDATIONS: none`. Not affected.
- Nodes 32, 41, 386 and 388 name the worker-contract paths. Node 317 names the manager contract path. None of them names this paragraph or the removed item, so no clause is made wrong.
- Node 386 has the same six files. Its clause 4 ("Apart from clauses 1 and 3, no sentence in the six files changes") is judged against its own starting commit, so it still holds.
No replacement clauses are written, and no open node's question changes. The resolved-node search used the same handles plus "read only what matches", "nothing checks the answer" and "item N" / "N items" counts, run over `## Answer` and `## Acceptance condition` sections only. Its results are in INVALIDATIONS.
MISSING FROM MAP: none
GATE PAYLOAD:  The checker has not run yet, so there are no findings.
Paths touched:
- .claude/skills/expedition-grilling/SKILL.md
- .claude/skills/expedition-research/SKILL.md
- .claude/skills/expedition-prototype/SKILL.md
- .claude/skills/expedition-precondition/SKILL.md
- .claude/skills/expedition-implementation/SKILL.md
- .claude/skills/expedition/SKILL.md
All six are in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/382-resolved-search, and the work is uncommitted.
Checks run:
- The condition's scope searches, rerun on the finished tree. `grep -l "^Before you write your handover, search the open nodes'" .claude/skills/*/SKILL.md` returns exactly the five worker contracts. `grep -rln "Does anything tell a worker to look at the record" .claude/` returns nothing. Neither search reaches a file outside the list.
- For each contract, the old and new texts are equal once whitespace is collapsed, apart from the added sentence (checked by script). `git diff` shows one hunk per contract.
- `wc -l` on the manager contract: 824 before, 819 after.
- No change under `.scratch/`, `expedition-checker` or `expedition-cascade`.
- The bar: the repo states no build, test or format commands (its root holds CONTEXT.md, CONTEXT-MAP.md and .gitignore, and no manifest, CLAUDE.md or AGENTS.md). That matches map-implementation-rules.md's record, so the bar is the standards plus the condition. The added sentence's words are fixed verbatim by the condition.
Proposed commit message:
"Ship the search of resolved nodes before a handover

The five worker contracts now tell a worker to search resolved nodes' Answer and Acceptance condition sections for its work's handles and report what it changes in INVALIDATIONS. The manager contract's open question on this is removed and the list renumbered.

Node: graph-workflow/382"

RETROSPECTIVE
1. What I had to hunt for: the open/resolved status of nodes and the section boundaries for the resolved-node search. I found them by grepping `^Status:` lines and by writing a small section extractor. Nothing ships a tool for searching only the `## Answer` and `## Acceptance condition` sections. I also had to learn that the (j) derivation block must run from `.scratch/graph-workflow/`, because its glob is `nodes/...`. I first ran it from the repo root and it failed.
2. What arrived that this node did not need:
- `map-read-whole-for-a-few-items` (6 retrospectives now carry it; the 5 earlier ones are nodes 178, 205, 220, 284, 387). Of map.md, only the writing rules and ground rules bore on a six-sentence edit.
- `rules-file-read-whole-for-one-section` (4 earlier retrospectives: nodes 178, 220, 387, as derived). Only the bar paragraph of map-implementation-rules.md mattered.
3. What would have made this node easier: a ready-made search over resolved nodes' `## Answer` and `## Acceptance condition` sections. The duty this node ships now asks every worker to run that search.
- `record-is-not-mechanically-scannable` (5 earlier retrospectives: nodes 178, 212, 220, 385, 387). Shipping a small section-scoped search in derivations.md would help every future worker meet this new duty.
4. What I read that was stale or wrong:
- `stale-number-in-the-record` (4 earlier retrospectives: nodes 178, 212, 220, 385). Node 76's "nine open questions" and node 362's "item 4" both name a list that has since shrunk.
The manager's notes held: nodes 379 and 380 had landed as described, and the list as it stood had four items.
`````
