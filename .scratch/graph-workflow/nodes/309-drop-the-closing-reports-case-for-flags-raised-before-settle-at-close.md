# Drop the closing report's case for flags raised before settle-at-close existed

Type: implementation
Status: resolved
Supersedes: 320
Blocked by: 300

## Question

`### Settle a flag` says flags reach the closing report in two cases. One is "a flag raised before this settling rule existed, on a node already resolved". No effort started after the rule shipped can hold such a flag. Should the shipped file drop that case?

*Reported by [node 300](300-rewrite-graph-conventions-part-2.md)'s worker.*

## Acceptance condition

*Authored by node 300's worker and filed by the manager.*

In `.claude/skills/expedition/graph-conventions.md`, under `### Settle a flag`, the paragraph beginning "Flags reach the closing report" states one case only: a flag whose pick report the human never answered, because they never spoke again. It no longer states the case of a flag raised before the settling rule existed. No other sentence in the file changes, and no other path changes. The working tree meets the bar.

## Amendment, 2026-09-25 (from node 312)

*Written by [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s worker and filed by the manager, after that node's work landed as commit `e64b3de`. Every word of the replacement is fixed by that commit: it quotes the after-text of `expedition/SKILL.md` and `expedition/graph-conventions.md`. The minting author's condition and any earlier amendment above are left as they were. Node 312's worker's search is on node 312 under `RE-POINTING SEARCH:`.*

- **The whole condition.** Replace it with: "In `.claude/skills/expedition/SKILL.md`, under `## Flags`, the paragraph beginning "Flags reach the closing report" states one case only: a flag whose pick report the human never answered, because they never spoke again. It no longer states the case of a flag raised before the settling rule existed. No other sentence in the file changes, and no other path changes. The working tree meets the bar."

*The manager's note:* the worker reported that the paragraph moved from `graph-conventions.md`'s `### Settle a flag` to `SKILL.md`'s `## Flags`, where it now reads "Flags reach the closing report in two cases only. The first is a flag raised before this settling rule existed, on a node already resolved. The second is a flag whose pick report the human never answered, because they never spoke again."

## Answer

The manager contract's `## Flags` now names one case of a flag reaching the closing report, an unanswered pick report, and drops the transitional case of flags raised before the settling rule existed.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `c52c03e`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Drop the closing report's case for flags raised before settle-at-close existed

ANSWER:        Yes, the shipped file drops that case. In `.claude/skills/expedition/SKILL.md`, under `## Flags`, the paragraph that said flags reach the closing report "in two cases only" now reads: "Flags reach the closing report in one case only: a flag whose pick report the human never answered, because they never spoke again." The case removed was "a flag raised before this settling rule existed, on a node already resolved". It was a transitional case. An effort started after the settling rule shipped cannot hold such a flag, so the manager contract has no reason to name it. The surviving case keeps its original wording, "pick report" included, as the acceptance condition requires. The paragraph was rewrapped to the file's existing width (the new first line is 100 characters). No other sentence in the file changed. Bar: the repo has no build, no tests, no formatter and no CI. The worktree root holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`, with no manifest or task runner. `.gitignore` lists `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/`, and invokes nothing. This matches the record in `map-implementation-rules.md`. So the bar is its non-command half: the ground rules, the five standing rules for writing, `CONTEXT.md`'s `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, `/coding-principles`, `/naming`, and the acceptance condition. The edit is one plain sentence with one idea, and it adds no new term.

INDEX LINE:    The manager contract's `## Flags` now names one case of a flag reaching the closing report, an unanswered pick report, and drops the transitional case of flags raised before the settling rule existed.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: No resolved node is contradicted. One open node is affected: node 320, "The glossary's `Flag` entry names one case of a flag reaching the closing report, and the manager contract names two". Its premise no longer holds. The manager contract now names one case, and `CONTEXT.md`'s `**Flag**:` entry already says "A flag goes into the closing report only where the human never spoke again.", so the two files agree. Node 320's acceptance condition, item 1, still asks to replace that glossary sentence with the two cases, including the case this node dropped. If 320 is worked as written, it would put the dropped case back into a shipped file. Its condition needs amending, or the node can be closed as already satisfied. Its other blocker, node 317 ("which outstanding flags reach the closing report"), may also bear on this. No other shipped file states the dropped case. I searched every tracked file outside `.scratch/` for "raised before", "already resolved", "settling rule existed" and "two cases", and for "closing report" near flag or case wording. Apart from the paragraph I edited, the only hit is `graph-conventions.md`'s `### Settle a flag`, which just points to `## Flags` in `SKILL.md`, and that pointer still holds.

GATE PAYLOAD:  The checker has not run yet, so there are no findings and no changes made for them. Paths touched: `.claude/skills/expedition/SKILL.md` in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/309-drop-pre-rule-flag-case`. Nothing else was touched and nothing was committed. Proposed commit message:

    Drop the closing report's case for flags raised before the settling rule

    The manager contract's ## Flags named two cases in which a flag reaches
    the closing report. The first, a flag raised before the settling rule
    existed, cannot arise in an effort started after the rule shipped. The
    paragraph now names only the flag whose pick report the human never
    answered.

    Node: graph-workflow/309

RETROSPECTIVE
1. What I had to hunt for: whether any shipped file still stated the dropped case, which needed a grep of the tracked files outside `.scratch/`. I also had to find the glossary's `Flag` entry, which is in `CONTEXT.md`. There is no file named "glossary". And I had to find the effort name for the trailer, which I took to be `graph-workflow` from the directory name.
2. What arrived that this node did not need: most of the implementation rules file (the review route, the rule on record files as work, the supersession mechanics), and the `.claude/rules/expedition-triggers.md` contents that were injected on read. The map's `## Notes` did not bear on a one-paragraph deletion either.
3. What would have made this easier: the spawn could have said that `CONTEXT.md` already states one case only, and named the effort slug for the `Node:` trailer. The manager's quote of the paragraph and the wrap-width note were exactly right and saved a lookup.
4. What was stale, wrong or contradictory: the node's `## Question` still points at `### Settle a flag` in `graph-conventions.md`. The amendment superseded that, but the Question text was never updated. Node 320's title and question say the glossary names one case and the manager contract names two. After this node, both name one, and 320's condition would reintroduce the dropped case. In `map-implementation-rules.md`, the bar paragraph's sentence about `.gitignore` has been patched in place into an awkward run-on (the struck text plus two bold insertions). It is still accurate against the repo.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 318's check.*

> PASS
>
> Node 309, "Drop the closing report's case for flags raised before settle-at-close existed", meets its acceptance condition, and the bar holds. The work rewrites one paragraph in the manager contract, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `.claude/skills/expedition/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/309-drop-pre-rule-flag-case`, on branch `worktree-309-drop-pre-rule-flag-case`, based on `7d6a67f`. I read the changed path only as the work.
>
> **Part by part**
> 1. **The paragraph states one case only: met.**
>    - The paragraph beginning "Flags reach the closing report" sits under `## Flags`, at line 339.
>    - Before, it read: "Flags reach the closing report in two cases only. The first is a flag raised before this settling rule existed, on a node already resolved. The second is a flag whose pick report the human never answered, because they never spoke again."
>    - Now it reads: "Flags reach the closing report in one case only: a flag whose pick report the human never answered, because they never spoke again."
>    - The pre-rule case is gone. `grep -n -i -E "before the settling rule|settling rule existed"` over the file returns nothing.
> 2. **No other sentence changes: met.** `git diff --numstat` shows 1 line added and 2 removed, all within this paragraph. The sentences before it in the section are unchanged.
> 3. **No other path changes: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition/SKILL.md` modified. That matches the worker's report, which I checked rather than relied on.
> 4. **The working tree meets the bar: met**, as below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the new sentence is plain and holds one idea.
>   - `CONTEXT.md`'s `_Avoid_` lines: no refused word is introduced.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*

## Flags

`309.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `e64b3de`.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
