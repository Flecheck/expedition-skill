# Let the four no-file contracts permit a removed temporary directory

Type: implementation
Status: claimed
Blocked by: none

## Question

Carry node 67's answer into the checker, grilling, research and cascade contracts.

*Reported by [node 67](67-whether-a-checker-may-write-scratch.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. It shares `.claude/skills/expedition-checker/SKILL.md` with node 214 (claimed), and the grilling and research contracts with node 41 (open). Those nodes' conditions concern other sentences, so this is a code-slot collision for the manager to schedule, not a defect to join."*

*The manager's note:* node 214 is open and unclaimed, not claimed as the worker's words say, and node 375 has landed.

## Acceptance condition

*Authored by node 67's worker and filed by the manager.*

> 1. Each of the four files below gains the following sentence, word for word, read with line breaks unwrapped into spaces: "A temporary file is not a file in this contract's sense: you may write one in a new directory under the system's temporary directory, and you remove that directory before you hand back." In each file it appears exactly once, as the last sentence of the numbered item under `## Hard rules` named here:
>    - `.claude/skills/expedition-checker/SKILL.md`, item 1, which begins "Leave everything as you found it"
>    - `.claude/skills/expedition-grilling/SKILL.md`, item 3, which begins "Put your work in what you hand back"
>    - `.claude/skills/expedition-research/SKILL.md`, item 1, which begins "Put all your work in your handover"
>    - `.claude/skills/expedition-cascade/SKILL.md`, item 2, which begins "Write no file, in either role"
> 2. In those four files, no other text changes except the rewrapping of the item that receives the sentence. Every other line keeps the width the file already uses. In particular, the sentences in the cascade contract that say "write no file" under its two `### What you do` sections stay as they are.
> 3. No other file in the repository changes.
> 4. Scope search: the command `grep -rn -i 'write no file' .claude/skills/`, run over the working tree, returned six lines in four files. Those are the checker contract's hard rule 1, the grilling contract's hard rule 3, the research contract's hard rule 1, and three lines of the cascade contract (hard rule 2 and one sentence in each of its two `### What you do` sections). The four files in clause 1 are the whole scope. If the same search, run while doing the work, finds the phrase in any file outside these four, report it and do not edit it.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Let the four no-file contracts permit a removed temporary directory

ANSWER:        Four shipped contracts now each end one hard-rule item with this sentence, word for word: "A temporary file is not a file in this contract's sense: you may write one in a new directory under the system's temporary directory, and you remove that directory before you hand back." The four items are checker item 1 ("Leave everything as you found it"), grilling item 3 ("Put your work in what you hand back"), research item 1 ("Put all your work in your handover") and cascade item 2 ("Write no file, in either role"). Each changed item was rewrapped greedily at 105 columns with the files' 3-space hanging indent. Rewrapping each item's original text at that width reproduces its original lines exactly, so the only change is the appended sentence and the reflow of that one item. No other line changed. The cascade contract's two "write no file" sentences under its `### What you do` sections are untouched. The sentence says "a new directory" rather than naming a path, because ground rule 1 forbids assuming a machine or toolchain.

INDEX LINE:    The checker, grilling, research and cascade contracts each end their no-file hard rule with one sentence permitting temporary files in a new directory under the system temp directory, removed before handback.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none. This carries out node 67's answer as written and does not change it.

CONDITIONS:    I searched every open node (42 files whose Status is not resolved, dropped, moot, merged or superseded) for each of these, in both the condition and the question: "write no file", "temporary", the four items' opening phrases, and the four paths expedition-{checker,grilling,research,cascade}/SKILL.md. The phrases matched only node 376. The paths also matched node 30 (checker), node 214 (checker), node 41 (checker, grilling, research) and node 32 (grilling, research). None of those conditions mentions hard rules, item numbering, line widths or "no other text/file" in a way this work affects. No replacement clauses, and no open node's question changes.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none received yet.
               Paths touched: .claude/skills/expedition-checker/SKILL.md, .claude/skills/expedition-grilling/SKILL.md, .claude/skills/expedition-research/SKILL.md, .claude/skills/expedition-cascade/SKILL.md (all in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/376-tempdir, uncommitted).
               Bar: the repo has no build, tests, formatter or CI. I found no manifest, task runner or CI config, which matches map-implementation-rules.md. So the bar is its non-command half. `git diff --check` is clean, and each file still ends in a newline.
               Checks run: in each file the sentence appears exactly once with whitespace squeezed. Clause 4's search, `grep -rn -i 'write no file' .claude/skills/` over the worktree, still returns six lines, all in the four files. Nothing outside those four is in scope. `git status` shows only these four files modified.
               Proposed commit message:
                 Let the four no-file contracts permit a removed temporary directory

                 The checker, grilling, research and cascade contracts each end their
                 no-file hard rule with one sentence: a temporary file may go in a new
                 directory under the system's temporary directory, removed before handback.

                 Node: graph-workflow/376

RETROSPECTIVE:
1. What I had to hunt for: each file's wrap width. I measured it from line-length distributions (105 columns) and confirmed it by checking that rewrapping each original item reproduces it exactly. I also had to find the commit trailer's effort name, which I took from git log ("graph-workflow").
2. What arrived that this node did not need: almost all of map.md and map-implementation-rules.md (the worktree, landing and record-as-work rules), and node 67's decisions line, which the condition already quotes in full.
3. What would have made this easier: a condition that states the target wrap width. Clause 2 says "the width the file already uses", which means measuring it.
4. What was stale, wrong or contradictory: nothing. The manager's note that node 214 is unclaimed is consistent with what I saw (Status: open).
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c376.md`.*

> PASS
>
> Node 376, "Let the four no-file contracts permit a removed temporary directory". Worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/376-tempdir, uncommitted diff against HEAD 4d1e6b34.
>
> Acceptance condition, one line per part:
> - 1, the sentence appears exactly once in each file. For each of the four files I unwrapped the text (`perl -0pe 's/\n(?!\n)/ /g; s/ +/ /g' <file> | grep -o -F "$S" | wc -l`, with $S set to the sentence word for word). The count was 1 in every file.
> - 1, the sentence is the last one of the named item under `## Hard rules`. I ran `awk '/^## /{h=$0} /temporary file is not/{print h}'` on each file, and every hit sits under `## Hard rules`. `git diff` shows the sentence closing these items:
>   - checker item 1, "Leave everything as you found it"
>   - grilling item 3, "Put your work in what you hand back"
>   - research item 1, "Put all your work in your handover"
>   - cascade item 2, "Write no file, in either role"
> - 2, no other text changes and widths are kept. `git diff --numstat` gives 3 lines added and 1 removed per file. The only removed line in each file is the last line of the receiving item, and its words come back unchanged at the start of the new text. Every new line is 105 characters or less (`git diff -U0 | awk '{print length}'`: 103/102/13, 102/105/24, 101/101/39, 101/101/39). The wrap is greedy at 105: the next word would not fit on any of the new lines. That matches the 105-column wrap the files use for prose. The longest line in each file is the same before and after (180/189/149/105). The cascade lines that say "write no file" in its `### What you do` sections (now lines 69 and 118) are not in the diff.
> - 3, no other file changes. `git status --porcelain --untracked-files=all` lists only the four paths, and nothing is untracked.
> - 4, the recorded scope search. I ran `grep -rn -i 'write no file' .claude/skills/` as written, over the worktree. It returned six lines in four files: cascade lines 45, 69 and 118, research line 56, checker line 72 and grilling line 70. That matches the recorded return of six lines and its breakdown, and finds nothing outside the four files.
>
> The bar:
> - The repo root has no agent-instruction file: no CLAUDE.md, AGENTS.md or manifest, only `.claude`, CONTEXT.md, CONTEXT-MAP.md and `.gitignore`. The standards file also records that the repo has no build, tests, formatter or CI. So there were no commands to run, and the bar is its non-command half.
> - I read only the standards in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md. I opened no other file in that directory.
> - The standards it names are `/coding-principles`, `/naming`, the `_Avoid_` lines in glossary.md, the ground rules, the six standing rules for writing, graph-conventions.md and `/writing-for-agents`. No reviewing skill is named, so I ran none and held the work against these standards by hand.
> - Bearing on this work:
>   - Ground rule 1: "the system's temporary directory" assumes no repo, machine or toolchain.
>   - Ground rule 3: nothing in the change addresses the human.
>   - Writing rule 5: the sentence is plain English with a clear referent. It joins two clauses with a colon, but the condition dictates the wording word for word.
>   - Glossary: grepping the `_Avoid_` lines for the sentence's words ("temporar", "director", "hand back", "contract", "sense", "file", "remove", "system") found nothing. Nothing in glossary.md or graph-conventions.md touches temporary files.
>   - `/coding-principles` and `/naming` have nothing to act on, since there is no code.
> - I found no breach.
> - The "Where the work moved one of them" section does not apply. The changed files are worker contracts, and none of them is among the standards I hold the work against.
> - The record-as-work rule in the standards file does not apply. None of the changed paths is a record file.
>
> I followed the checker contract in the main checkout and read the worktree's copy only as the work. I wrote no file.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and left no part of the condition uncovered. The node raised no flags.
