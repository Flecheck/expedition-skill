# Ship the search of resolved nodes before a handover

Type: implementation
Status: resolved
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

## Answer

The five worker contracts now tell a worker to search resolved nodes' Answer and condition sections before handing back and report what it changes in INVALIDATIONS. The manager contract's matching open question is removed.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `dd6428981`.

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

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-05. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/check382.md`. The node holds no flags.*

> PASS
>
> Work: uncommitted changes in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/382-resolved-search against HEAD 3706023f3. `git status --short` shows exactly the six listed paths modified, with no untracked files.
>
> - Scope (only the six files edited). `git status --short` and `git diff --stat` list exactly the six paths. `git ls-files --others --exclude-standard` prints 0 lines. Met.
> - Clause 1 (the sentence is added, worded exactly, and placed correctly in all five worker contracts). Checked with a Python script that splits each file into paragraphs on blank lines and unwraps each one. In each of the five files, the paragraph starting "Before you write your handover, search the open nodes' `## Acceptance condition` sections" contains `<Question sentence> + " " + <added sentence> + " " + "Name in `CONDITIONS` what you searched for."`, and the added sentence appears exactly once. Met.
> - Clause 2 (the paragraph is byte-identical across the five files). I extracted the raw paragraph from each file with `awk 'BEGIN{RS=""} /^Before you write your handover/' | md5sum`. Before the change all five give 82cef63f…. After it all five give dd16dd6a…. Met.
> - Clause 3 (no other sentence changes). The same script checked two things. First, for each file, the unwrapped old paragraph with the added sentence inserted between the Question sentence and the "Name in `CONDITIONS`" sentence equals the unwrapped new paragraph. Second, every other unwrapped paragraph in the file is identical before and after, with the same paragraph count and an empty list of differing paragraphs. That covers the `INVALIDATIONS:` handover line, "Report `NEW NODES` and `INVALIDATIONS` yourself…", and "In `INVALIDATIONS`, an outright contradiction…". Met.
> - Clause 4 (the item is removed and the list renumbered). I printed `## What nothing here settles` onward with `sed`. The "Does anything tell a worker to look at the record…" item is gone with all its sentences. The list now runs 1, 2, 3 in the original order, and the remaining items keep their words; the diff changes only the numerals. `grep -rln "Does anything tell a worker to look at the record" .claude/` returns nothing. Met.
> - Clause 5 (nothing else changes in `.claude/skills/expedition/SKILL.md`, and the file does not grow). `git diff` shows one hunk, the item removal and renumbering, at 2 insertions and 7 deletions. `wc -l` gives 819 now against 824 at HEAD. Met.
> - Clause 6 (`.scratch/`, the checker contract and the cascade contract are untouched). `git diff HEAD --stat -- .scratch .claude/skills/expedition-checker .claude/skills/expedition-cascade` prints nothing. Met.
> - Clause 7 (the bar). See the bar below.
>
> Recorded searches, run as written in the worktree:
> - `grep -l "^Before you write your handover, search the open nodes'" .claude/skills/*/SKILL.md` returned exactly the five worker contracts: implementation, grilling, prototype, research and precondition. This matches the recorded return.
> - `grep -rln "Does anything tell a worker to look at the record" .claude/` returned nothing (exit 1). The recorded return was `.claude/skills/expedition/SKILL.md`. The difference is expected, because the work removed that item. The search reaches no file outside the list.
>
> The bar. This repo has no build, tests, formatter or CI. The repo root holds only CONTEXT.md, CONTEXT-MAP.md and .gitignore, with no CLAUDE.md, AGENTS.md or manifest, which agrees with the record in map-implementation-rules.md. So the bar comes down to its non-command half.
> - `git diff --check` printed nothing (rc=0).
> - Line length matches the surrounding text: the longest added line is 106 characters, and the count of lines over 110 characters is the same before and after in each file.
>
> Standards. I read only the standards in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md and opened no other file in that directory. That file lists six standards:
> - `/coding-principles` and `/naming`
> - the glossary's `_Avoid_` lines
> - the ground rules
> - the six standing rules for writing
> - graph-conventions.md
> - `/writing-for-agents`
>
> The ones that bore on this work were the `_Avoid_` lines, the writing rules and `/writing-for-agents`, applied to the one added sentence and the removal. The added sentence's wording is dictated word for word by the condition. Its verb "report in `INVALIDATIONS`" matches the unchanged existing sentence "Report `NEW NODES` and `INVALIDATIONS` yourself". The rules file itself says the glossary's `report` refusal applies to the noun for one concept only. No finding.
>
> Notes:
> - No reviewing skill is named for this repo, and none was run.
> - The record-as-work rule in the rules file did not apply, because no record file was among the changed paths.
> - The node holds no flags.
> - The temp directory I created has been removed.

### Gate — approve, `standing yes`, 2026-10-05

Taken under the standing yes recorded in `map-manager-only.md`, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and covered every clause.

