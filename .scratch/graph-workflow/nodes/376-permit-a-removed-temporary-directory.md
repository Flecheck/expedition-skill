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
