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
