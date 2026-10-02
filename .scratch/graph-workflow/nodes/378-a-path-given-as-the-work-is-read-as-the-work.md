# Say in the shipped checker contract that a path given as the work is read as the work

Type: implementation
Status: resolved
Blocked by: none

## Answer

The shipped checker contract's `## What you are given` now says a path given as the work is the work wherever it sits and is read, placed right after the implementation-rules exception.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `d942b1f9f`. The node raised no flags.

## Question

Add the one sentence node 172 decided to `.claude/skills/expedition-checker/SKILL.md`.

*Reported by [node 172](172-whether-the-shipped-contract-says-which-route-the-ban-governs.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. It shares `.claude/skills/expedition-checker/SKILL.md` with node 214 (open), whose condition concerns the table under `### When what you check against is itself the problem` and limits only that node's own changes. That is a scheduling clash over one file for the manager, not a defect to join."*

## Acceptance condition

*Authored by node 172's worker and filed by the manager.*

> 1. In `.claude/skills/expedition-checker/SKILL.md`, under the heading `## What you are given`, the sentence "A path you were given as the work is the work wherever it sits, and you read it." appears word for word. It comes immediately after the sentence "The one exception is `map-implementation-rules.md`, and only for the standards in it." and before the sentence "The acceptance condition as given to you is the only statement of intent you get." Compare on the text with its line breaks joined into single spaces. Before this work, both of those neighbouring sentences are present in that paragraph, and the new sentence appears nowhere in the file.
> 2. No other sentence of `.claude/skills/expedition-checker/SKILL.md` changes, and no heading in it is renamed. Re-wrapping the lines of the one paragraph that holds the new sentence is allowed, provided that paragraph's words are otherwise unchanged when compared with line breaks joined into single spaces.
> 3. No file other than `.claude/skills/expedition-checker/SKILL.md` changes.
> Scope: this came from no search. The named sentence and file are the work, not instances of a defect.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Say in the shipped checker contract that a path given as the work is read as the work
ANSWER:        `.claude/skills/expedition-checker/SKILL.md`, under `## What you are given`, now has the sentence "A path you were given as the work is the work wherever it sits, and you read it." It sits between "The one exception is `map-implementation-rules.md`, and only for the standards in it." and "The acceptance condition as given to you is the only statement of intent you get." Only the last two lines of that one paragraph were re-wrapped, and they stay within the paragraph's 104-column width. No other sentence or heading changed. Before the edit I checked at 5478a1376 that, with line breaks joined, the two neighbouring sentences stood next to each other exactly once, and that "wherever it sits" was not in the file. Both held. After the edit, the three sentences in order match exactly once on the joined text.
INDEX LINE:    The shipped checker contract's `## What you are given` now says a path given as the work is the work wherever it sits and is read, placed right after the implementation-rules exception.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: No resolved node is contradicted. This carries out node 172's answer. One extension: the rule in `map-implementation-rules.md` that begins "An implementation node's work on this effort may be the effort's own record" says the contract's "open no other file" instruction governs the route standards take, not the changed paths. The shipped contract now says the general part of that itself, for any path handed over as the work. The parts specific to this effort's record stay in the map: derive no intent from record files, the bookkeeping FAIL, and saying so in the outcome. Node 163 placed that record rule in the map rather than the skill, and that placement still stands, because the sentence added here is the general route statement node 172 decided, not the record rule.
CONDITIONS:    I searched every open node's file (107 files whose Status is not resolved, dropped, moot or merged) for: "expedition-checker/SKILL.md", "The one exception is", "only statement of intent", "given as the work", "wherever it sits", "## What you are given", "open no other file", "Leave the record unread", "six givens", "map-implementation-rules.md`, and only", "changed paths". Outside node 378 itself, nothing matched in any `## Acceptance condition` or `## Question` in a way this work makes wrong. "expedition-checker/SKILL.md" matched 15 other open nodes by path. None of their matched text quotes the edited paragraph. Node 214 (open) shares the file, and its condition concerns the table under `### When what you check against is itself the problem`. The other matches were in a superseded node (250) or in handover and review text (219, 30), not in conditions or questions. One scheduling note for the manager, outside the search sections: node 30 (claimed) records in its `## Interview` a plan to reword the "six givens above are everything you are given" sentence. That is the first sentence of the same paragraph this node edited, so the two edits may overlap when integrated. No replacement clauses written.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none received yet. Bar: the repo states no build, test or format commands. There is no CLAUDE.md or AGENTS.md at the root and no manifest, which matches the record in map-implementation-rules.md ("no build, no tests, no formatter and no CI"), so there was no difference to report. The bar is its non-command half: the standards plus the acceptance condition. Paths touched: .claude/skills/expedition-checker/SKILL.md (in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/378-work-path). Method-skill parts skipped: none invoked.
Proposed commit message:
  Checker contract: a path given as the work is read as the work

  Node: graph-workflow/378

RETROSPECTIVE:
1. What I had to hunt for: which open nodes are open (no index of status, so I derived it with a grep on Status lines), and whether "six givens" in node 30 sat in a condition or only in interview text.
2. What arrived that this node did not need: most of map.md and map-implementation-rules.md. Of map-implementation-rules.md only the bar's commands paragraph and the record-rule paragraph bore on this one-sentence edit.
3. What would have made this easier: a list of open node ids in the spawn, or a status-only index, so the CONDITIONS search does not need its own status derivation.
4. What was stale, wrong or contradictory: nothing found. The manager's pre-claim checks held exactly.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c378.md`.*

> PASS
> I took the checker contract from the main checkout, /home/mathieu/projects/graph-agent/.claude/skills/expedition-checker/SKILL.md. Its content is the same at the base commit 5478a1376 and at master HEAD: `git diff 5478a1376 HEAD --stat` on that file printed nothing. I read the worktree's copy as the work. I compared text with its line breaks joined: each blank-line-separated paragraph joined into one line (awk RS="", gsub "\n" to " ") for the base (`git show HEAD:<file>`, where worktree HEAD = 5478a1376) and for the working copy, then diffed the two.
>
> Condition part 1, the sentence is present, under `## What you are given`, between the two named sentences, and was absent before:
> - In the joined working copy, the exact string "The one exception is `map-implementation-rules.md`, and only for the standards in it. A path you were given as the work is the work wherever it sits, and you read it. The acceptance condition as given to you is the only statement of intent you get." matched once (`grep -o ... | wc -l` printed 1).
> - The nearest heading above the new sentence is `## What you are given` (awk tracking the last `^## ` line before the match).
> - Before the work, `grep -c` of the new sentence on the joined base printed 0. The joined base contains "...only for the standards in it. The acceptance condition as given to you is the only statement of intent you get." (`grep -c` printed 1), so both neighbouring sentences sat in that paragraph.
>
> Condition part 2, no other sentence changes and no heading is renamed:
> - The diff of the joined base against the joined working copy shows exactly one changed paragraph, the "The six givens above..." paragraph.
> - Its only difference is the inserted sentence. The re-wrap of its last two lines leaves the words otherwise unchanged.
> - `diff` of the `^#` lines from base and work printed nothing, so the headings are identical.
>
> Condition part 3, no other file changes:
> - `git -C <worktree> status --short --untracked-files=all` lists only ` M .claude/skills/expedition-checker/SKILL.md`.
> - `git diff --stat` shows 1 file, 2 insertions and 1 deletion.
>
> Recorded search: the condition says its scope came from no search, so there was no command to re-run.
>
> The bar's commands: the repo has no root agent-instruction file (`ls -a` of the worktree shows .claude, CONTEXT-MAP.md, CONTEXT.md, .gitignore, .scratch). The standards file records that the repo has no build, no tests, no formatter and no CI, so the command half of the bar is empty. As formatting hygiene I ran:
> - `git diff --check`, which printed nothing (no whitespace errors).
> - A line-length check. Base and work both have a maximum line length of 180. The only lines over 110 are the existing table rows in "When what you check against is itself the problem", which the work did not touch.
>
> Standards: I listed `.scratch/` once, giving graph-workflow, and read only the standards in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md. I opened no other file in the effort's directory. Its list is:
> - /coding-principles and /naming
> - the `_Avoid_` lines of glossary.md
> - the ground rules
> - the six standing rules for writing
> - graph-conventions.md
> - /writing-for-agents
>
> These bore on the work:
> - **The glossary's `_Avoid_` lines.** I grepped them for path, work, read, given, sits and wherever. No refused word is used for its refused concept. "subtask (which names the work...)" does not refuse "work".
> - **Ground rules 1 and 3.** The sentence assumes no repo, machine or toolchain, and it addresses no human.
> - **Writing rules 5 and 6.** The sentence is in plain English and states a positive rule. Its pronoun "it" has one referent, the path. It contains no slogan-shaped contrast. No heading was renamed, so rule 6's citation duty does not arise.
> - **/writing-for-agents**, read from the mattpocock-skills plugin. The sentence is a positive statement and adds no duplicate meaning within this file.
>
> /coding-principles, /naming and graph-conventions.md did not bear: the change is one sentence of prose in a shipped skill, with no code and no graph file. The standards name no reviewing skill, so I ran none.
>
> The work did not move any standard I hold it against, since the checker contract is not among the standards listed. The rule in the standards file about record paths handed over as the work did not apply, because no record file is among the changed paths.
>
> I wrote two temporary files directly in $TMPDIR rather than in a new directory under it, which departs slightly from the contract's temporary-file rule. I removed both before handing back.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and left no part of the condition uncovered. Its closing remark reports its own departure from the new temporary-file rule, not a finding about the work. The node raised no flags.
