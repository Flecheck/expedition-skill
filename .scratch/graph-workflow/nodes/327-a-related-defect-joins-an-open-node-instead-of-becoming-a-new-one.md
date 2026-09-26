# A related defect joins an open node instead of becoming a new one

Type: implementation
Status: open
Blocked by: none

## Question

Workers report every defect they find as its own new node, and nearly every condition fences its node to a few lines ("no other entry changes", "no other path changes"). So the graph fills with nodes that change a few lines each and pay a full spawn, check and gate apiece. The human's instruction, `verbatim`: *"To avoid the issue, maybe we can make so that if it is related, put the defect in an already existing node ?"* Ship that rule into the contracts.

*Minted by the manager from the human's instruction, recorded in the map under `## Notes`.*

## Acceptance condition

*Written by the manager, which minted this node.*

1. In each of the five worker contracts (`.claude/skills/expedition-grilling/SKILL.md`, `expedition-implementation`, `expedition-precondition`, `expedition-prototype` and `expedition-research`), the instructions for the handover's new-nodes part say: where a defect the worker would report concerns the same file and the same concern as an open node the worker found, the worker names that node and gives the clauses to add to its acceptance condition, instead of proposing a new node.
2. `.claude/skills/expedition/SKILL.md` says the manager files such a report as an amendment to the named node's condition when that node is open and unclaimed, and as a new node when it is not.
3. `.claude/skills/expedition/SKILL.md` says the manager may amend the acceptance condition of a node that is open and unclaimed without first asking the human, recording the amendment on the node with a flag of its own that settles at the node's gate, and that the condition of a claimed node stays as written. The human's words behind this clause, `verbatim`: *"I think we shouldn't be too afraid of updating a node before it is started"*.
4. `.claude/skills/expedition/graph-conventions.md` says how the amendment is recorded on the node, or points at the rule it already has for recording an amendment.
5. No other rule in those files changes, and no other path changes.
6. The working tree meets the bar.
