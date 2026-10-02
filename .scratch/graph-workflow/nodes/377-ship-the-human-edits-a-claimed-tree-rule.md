# Ship the human-edits-a-claimed-tree rule

Type: implementation
Status: open
Blocked by: none

## Question

Carry node 85's answer into the implementation contract and the manager's skill.

*Reported by [node 85](85-human-edits-a-claimed-tree.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none".*

## Acceptance condition

*Authored by node 85's worker and filed by the manager.*

>  Done when all of the following hold.
>
> 1. In `.claude/skills/expedition-implementation/SKILL.md`, the sentence "The tree your spawn names is yours alone for the whole node." is replaced. The new text states three things, in this order: the tree the spawn names is the worker's alone among the agents for the whole node; the human may also edit it; and "Edit only files inside it." stays.
> 2. In the same file, the bulleted list that follows the line "In a correction round:" gains one bullet. The bullet states two things. First, where the human has edited the worker's tree, the worker keeps what the human wrote. Second, where the human's text conflicts with the acceptance condition or with something the checker found, the worker raises it and does not change that text.
> 3. In `.claude/skills/expedition/SKILL.md`, the section headed `### Three outcomes, and no fourth`, or the text directly under it, gains at most two sentences. They state that where the human says they edited a claimed node's tree, the manager passes the human's words to that node's worker at the worker's next resume, and asks the human nothing about what changed.
> 4. `.claude/skills/expedition-checker/SKILL.md` is not changed by this work.
> 5. Scope search: `grep -rn "yours alone" .claude/skills` was run over the working tree on 2026-10-02. It returned exactly one line: `.claude/skills/expedition-implementation/SKILL.md:18`. An instance the same search reaches outside the files this condition names is reported and not edited.
> 6. Each added passage follows the writing rules in `map.md`'s `## Notes`: plain English, one idea per sentence, stated as what to do. The whole change adds no more than five lines across the two files.
> 7. The working tree meets the bar.
