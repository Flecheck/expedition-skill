# Ship the check on a spawn's claims into the five worker contracts

Type: implementation
Status: claimed
Blocked by: none

## Question

Write node 78's answer into the worker contracts. A worker checks each claim of fact in the manager's notes, and in its own node's `## Question` outside the human's quoted words, before relying on it. The rule goes into the existing sentence each contract uses to tell the worker to read its sources rather than summaries of them.

*Reported by [node 78](78-what-a-spawn-may-assert.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. It shares the `## What you read` section of the same five files with open node 32 (the `flags.md` sentence) and edits the same files as open node 41 (FRICTION). The concerns differ, so this is code-slot scheduling, not a defect to join."*

## Acceptance condition

*Authored by node 78's worker and filed by the manager. The manager turned the worker's indented block into a quote and changed none of its words.*

> The work is these five files:
>   `.claude/skills/expedition-grilling/SKILL.md`
>   `.claude/skills/expedition-research/SKILL.md`
>   `.claude/skills/expedition-prototype/SKILL.md`
>   `.claude/skills/expedition-precondition/SKILL.md`
>   `.claude/skills/expedition-implementation/SKILL.md`
> Scope came from a search over the working tree: `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md`, which on 2026-10-02 returned exactly one line in each of the five files above and in no other file. If the search reaches an instance outside this list when the work is done, report it and do not edit it.
>
> Done means every one of the following is true of the finished tree.
> 1. In each of the five files, the sentence "Read each of the following. Do not trust any summary of them." is gone. In its place, at the same spot, the text states all three of the following:
>    (a) the worker reads each listed source itself rather than a summary of it;
>    (b) the worker checks each claim of fact in the manager's notes in its spawn before relying on it;
>    (c) the worker checks each claim of fact in its own node's `## Question` before relying on it, except text marked there as the human's own words.
> 2. The replacement text says (a) to (c) as what to do, with no prohibition. It adds no heading and adds at most 40 words to each file compared with the removed sentence. An example of wording that meets clauses 1 and 2: "Read each of the following rather than any summary of them. Before you rely on a claim of fact in the manager's notes, or in your node's `## Question` outside the human's quoted words, check it."
> 3. The replacement text is the same in all five files.
> 4. Nothing in the replacement tells the worker to check, doubt or re-derive a direction from the human, a permission the human granted, or an acceptance condition.
> 5. No other sentence of the five files changes.
> 6. No other file changes. That includes `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-cascade/SKILL.md` and every file under `.scratch/graph-workflow/`.
> 7. The tree meets the bar.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Ship the check on a spawn's claims into the five worker contracts

ANSWER:        In each of the five worker contracts (`.claude/skills/expedition-grilling/SKILL.md`, `-research`, `-prototype`, `-precondition`, `-implementation`), the opening line of `## What you read`, "Read each of the following. Do not trust any summary of them.", is replaced in place by one paragraph that is identical in all five files:

               "Read each of the following yourself rather than any summary of them. Before you rely on a claim of fact in the manager's notes in your spawn, or in your node's `## Question` outside any text marked as the human's own words, check it."

               It is wrapped over three lines at the files' usual width. Each file grows by two lines and by 32 words, against a limit of 40. No other line changes. Choices inside the wording that a later reader would otherwise have to work out again:
               - "yourself" makes clause (a) explicit: the worker reads the source itself.
               - "the manager's notes in your spawn" names the spawn part that the manager contract's spawn list calls "Your own notes". A direction from the human and a permission the human granted travel in a spawn as "Two things that travel in a spawn and are not yours". So does the acceptance condition, which is its own part of an implementation spawn. None of these is the manager's notes, so the sentence does not reach them (clause 4).
               - The carve-out uses "text marked as the human's own words". That is the condition's clause (c) wording and the glossary's sense of `verbatim`. The condition's example said "the human's quoted words".
               - The text is two sentences, one idea each, both stating what to do. It contains no prohibition.
               The condition's scope search, `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md`, now returns nothing. Before the edit it returned exactly one line in each of the five files (grilling 38, precondition 39, implementation 47, prototype 38, research 28) and nothing else. That confirms the manager's first note. Under `.claude/` it reaches no instance outside the list. The other hits for the phrase are all record text under `.scratch/graph-workflow/nodes/`, which is not in scope and was not edited.

INDEX LINE:    The five worker contracts' `## What you read` now opens by telling the worker to read sources rather than summaries, and to check claims of fact in manager's notes and its `## Question` first.

FLAGS:         ASSUMPTION: The condition said "claim of fact" and gave the example "outside the human's quoted words". I kept "claim of fact". It is the condition's own phrase, and "of fact" keeps it apart from the glossary term **Claim** (taking a node off the frontier). For the carve-out I wrote "outside any text marked as the human's own words", because that is clause (c)'s wording and matches how the record marks the human's words (`verbatim`). The glossary refuses "summary" only as another name for the effort closing report. The kept phrase "any summary of them" uses it in its ordinary sense, which node 22 had already judged acceptable.
               Index sentence: Node 380 kept "claim of fact" and phrased the carve-out as "text marked as the human's own words", following its condition's clause (c) rather than its example wording.

NEW NODES:     none

INVALIDATIONS: none. This carries out node 78's answer as that answer states it. Node 78 is extended into the shipped files, and nothing it says is contradicted.

CONDITIONS:    I searched the `## Question` and `## Acceptance condition` sections of every open or claimed node for:
               - "summary of"
               - "manager's notes"
               - "What you read"
               - "claim of fact"
               - the phrases "Read each of the following", "Read each of these" and "Do not trust any summary"
               - the five contract paths
               Results:
               - The sentence phrases matched only resolved or superseded nodes (12, 22, 46, 78, 155, 290-294, 329, 333) and this node.
               - The path matches were nodes 32, 41 and 382. Nodes 41 and 382 edit other paragraphs of the same files: the `FLAGS` markers, and the handover-search paragraph. Their clauses still hold as written, and node 382's byte-identity clause is about a paragraph this work does not touch.
               - Node 32's `## Question` cites the `flags.md` line by line number (grilling 41, implementation 54, research 37, prototype 43, precondition 45). It also quotes an older wording. Both were already stale before this work: on master the lines are 54/66/47/55/57. This work moves each down by two more, to 56/68/49/57/59. No clause replacement is owed, because the numbers are in the question and not in the condition.
               - The "summary of" and "manager's notes" matches in nodes 32, 214 and 379 are prose that this work does not affect.
               I replaced no clause and changed no question.

MISSING FROM MAP: none

GATE PAYLOAD:  The checker has not run yet, so there are no findings.
               Paths touched (all uncommitted, in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/380-spawn-claims, on branch worktree-380-spawn-claims):
                 .claude/skills/expedition-grilling/SKILL.md
                 .claude/skills/expedition-research/SKILL.md
                 .claude/skills/expedition-prototype/SKILL.md
                 .claude/skills/expedition-precondition/SKILL.md
                 .claude/skills/expedition-implementation/SKILL.md
               `git diff` shows the same one removed line and the same three added lines in each file, five times. No other file changed.
               The bar: the repo states no build, test or format commands. It has no manifest, no task runner and no CI, and `.gitignore` only ignores worktree paths. That matches what map-implementation-rules.md records, so the command half of the bar is empty and complete. On the other half, I held the new text against the glossary's `_Avoid_` lines and the six writing rules. It states rules as what to do, has one idea per sentence, one referent for each of "them" and "it", and no bold, figure of speech or prohibition.
               Proposed commit message:
                 Tell workers to check the claims of fact in their spawn's notes and node question

                 The five worker contracts' `## What you read` now opens by telling the
                 worker to read each listed source rather than a summary of it, and to
                 check each claim of fact in the manager's notes and in its node's
                 `## Question`, outside the human's own words, before relying on it.

                 Node: graph-workflow/380

RETROSPECTIVE:
1. What I had to hunt for: what the manager contract calls the notes ("Your own notes", under the spawn list), and which parts of a spawn are not the manager's (`### Two things that travel in a spawn and are not yours`). I needed both to be sure clause 4 holds. I also looked up the commit trailer's effort name (`graph-workflow`) in git log.
2. What arrived that this node did not need: the note about node 382, which said itself that it did not bear on the work. Almost all of map.md, apart from the ground rules and the writing rules. Most of map-implementation-rules.md, apart from the standards list and the bar's commands.
3. What would have made this easier: nothing much. The condition was precise and its example wording met it. A one-line pointer to where the manager contract defines a spawn's notes would have saved one search.
4. What was stale, wrong or contradictory: both of the manager's notes checked out. Node 32's `## Question` cites line numbers and a `flags.md` wording that were already stale on master. It breaks writing rule 4, which says to cite by heading or quoted phrase rather than line number. This work moves those lines down by two more.
`````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-04. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c380.md`.*

> PASS
>
> Read as the work: the five changed paths in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/380-spawn-claims. HEAD is the base 4f8925a46, so nothing is committed on the branch and all of the work is uncommitted.
>
> Acceptance condition, one line per part:
> - Scope and residual clause: I ran the recorded search `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md` over the finished tree. It returns nothing (exit 1). The condition records five lines, one in each listed file. The difference is explained by the work itself, which removed the sentence. To test the recorded claim, I ran the same search on the base commit: `git grep -n 'Do not trust any summary of them' 4f8925a46 -- '.claude/skills/*/SKILL.md'`. It returns exactly one line in each of the five listed files and no other file, so the recorded claim holds. A search over unwrapped text in every `.claude/skills/*/SKILL.md` also finds no instance in the finished tree, so there is no instance outside the list to report.
> - 1 (sentence gone, replaced in the same spot with (a), (b) and (c)): `git diff` shows one line removed and three lines added at the same spot under `## What you read` in each file. The new text is: "Read each of the following yourself rather than any summary of them. Before you rely on a claim of fact in the manager's notes in your spawn, or in your node's `## Question` outside any text marked as the human's own words, check it." It covers (a) "yourself rather than any summary", (b) "manager's notes in your spawn … check it" and (c) "`## Question` outside any text marked as the human's own words … check it".
> - 2 (said as what to do, no prohibition, no heading, at most 40 words added): the new text has no "not", "never" or "do not", and the diff adds no `#` line. `wc -w` gives 12 words for the removed sentence and 44 for the new text, so 32 words were added.
> - 3 (same text in all five files): I ran `git diff -U0 <file> | grep '^[+-][^+-]' | md5sum` on each file. All five give the same hash, 6c8fe4c43c2de7bfec0c85e471cbcf4c.
> - 4 (nothing tells the worker to check a direction from the human, a permission or an acceptance condition): I read the new text. It tells the worker to check only claims of fact, and only those in the manager's notes and in `## Question`, with the human's marked words exempt. The shipped `.claude/skills/expedition/SKILL.md` (spawn list and "### Two things that travel in a spawn and are not yours") carries the human's direction and the acceptance condition as separate items, not as the manager's notes.
> - 5 (no other sentence changes): `git diff --word-diff=porcelain` shows changes only inside the replaced sentence, the same five removed or added spans in each file. `git diff --stat` shows 3 lines added and 1 removed per file, with no rewrap elsewhere.
> - 6 (no other file changes): `git status --short --ignored --untracked-files=all` lists only the five files: no untracked file, no ignored file, nothing under `.scratch/graph-workflow/`, and none of the expedition, checker or cascade SKILL.md files.
> - 7 (the bar): see below.
>
> The bar:
> - Commands: I found no agent-instruction file at the repo root and no manifest, build, test, formatter or CI config. The root holds only `.claude`, `CONTEXT.md` (a stub), `CONTEXT-MAP.md`, `.gitignore` and `.scratch`. The standards file also states that this repo has no build, tests, formatter or CI, so the command half of the bar is empty and the bar is complete without it. `git diff --check` prints nothing (exit 0). The new lines are at most 103 characters, within the files' existing wrap width.
> - Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, under "What the work is held against", and opened no other file in the effort's directory. The list is `/coding-principles` and `/naming`, the glossary's `_Avoid_` lines, the ground rules, the six standing rules for writing, `graph-conventions.md` and `/writing-for-agents`. The file names no reviewing skill, so I ran none.
> - Standards that bore on this work:
>   - The ground rules: the text assumes no repo or toolchain, invokes no skill, and does not address the human.
>   - Writing rules 5 and 6: the rule is said as what to do, with no bold, no figure of speech and no slogan-shaped contrast. Each pronoun has one referent ("them" is the listed sources, "it" is the claim of fact).
>   - The glossary's `_Avoid_` lines: I searched them unwrapped. "summary" is refused only for the "Effort closing report" concept, which does not apply here. No other word of the new text is refused.
>   - `graph-conventions.md`: `## Question` is a node-file heading it defines.
>   - `/writing-for-agents` (located by name in the mattpocock-skills plugin): it prefers a positive instruction over negation, and the change turns a prohibition into a positive instruction.
>   - `/coding-principles` and `/naming` did not bear on this prose change.
> - Under the rules file's record-as-work rule, I read the changed paths as the work. None of them is a status line, `decisions.md` or `flags.md`.
>
> QUESTIONS:
> - Is the clash between "the manager's notes" and the glossary's "Manager note" intended? The phrase comes from the condition's clauses 1(b) and 2. The glossary defines **Manager note** as "The manager's own annotation on a relayed question". The grilling, prototype and precondition contracts also have a `MANAGER NOTES:` field in their resume shape ("the manager's own, never the human's"). The new text limits the duty to check claims to the notes "in your spawn". So a manager note that comes back on resume, the glossary sense, is not covered, and "manager's notes" now means two different things in the same file. The wording is the condition's own, so departing from it was not the worker's call. Should notes that arrive on resume be checked too, and should the spawn notes get a different name?
>   - Form: a passage in a worker contract that says "manager's notes" for a spawn's notes while the glossary's "Manager note" names something else.
>   - Extent: `grep -n "manager's notes\|MANAGER NOTES" .claude/skills/expedition-{grilling,research,prototype,precondition,implementation}/SKILL.md`.
>
> I wrote no temporary files.

*The manager's note:* the checker handed back a question beside its outcome, so the standing yes does not cover this gate. It goes to the human.
