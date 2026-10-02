# Ship an `expedition-triage` skill

Type: implementation
Status: claimed
Blocked by: none

## Question

Ship, as a skill the human invokes in an expedition's manager thread, the triage node 366 ran by hand: check the open nodes and the outstanding flags against the current tree, and propose in batches what to close, drop, merge and settle.

*Reported by [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. Node 365, the check before a claim, is its per-node counterpart and does not block it."*

## Acceptance condition

*Authored by node 366's worker and filed by the manager.*

> 1. A new file `.claude/skills/expedition-triage/SKILL.md` exists. Its front matter has `name: expedition-triage` and a `description` saying the human invokes it in an expedition's manager thread to triage the effort's open nodes and outstanding flags.
> 2. The file tells the manager to check each open node against the current working tree and the current shipped files, not against what the effort's record says about them. It permits the manager to give that checking to read-only agents.
> 3. The file sorts each open node into exactly one of four classes, and defines each class:
>  - moot: the work the node asks for is already done, or the text it targets no longer exists;
>  - dropped: the node is still live, but not worth its cost to the effort's destination;
>  - merged: the node concerns the same file and the same concern as another open node;
>  - kept.
>  For a kept implementation node, the file tells the manager to report whether its acceptance condition quotes text that no longer exists.
> 4. The file tells the manager to put its proposal to the human as one payload, with one numbered question per class and per flag batch. Each question lists its nodes, each with a one-line reason, so that one reply can answer it. The file says that no node's status and no flag's state changes before the human has answered.
> 5. The file tells the manager to propose settling, in one batch, the outstanding flags whose node is `resolved` or `superseded`, and to leave outstanding the flags on nodes that are `open` or `claimed`.
> 6. The file says what follows the human's answer:
>  - a moot node is superseded by the node whose work made it unnecessary, or, where no node did, resolved with an answer saying it was discharged with no edit and why;
>  - a dropped node is ruled out of scope;
>  - a merged node's clauses are added to the other node's acceptance condition, and the merged node is superseded by that node;
>  - a flag in an approved batch is settled.
>  The file names the procedures for these acts by the headings `### Supersede`, `### Resolve`, `### Rule out of scope`, `### Amend an acceptance condition` and `### Settle a flag` in `.claude/skills/expedition/graph-conventions.md`, and does not restate their steps.
> 7. The file says the skill runs only when the human invokes it, and that nothing in it runs on a schedule or on the manager's own judgement.
> 8. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
> 9. Scope came from no search: the work creates a file.
