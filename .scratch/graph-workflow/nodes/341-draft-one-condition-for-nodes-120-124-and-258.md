# Draft one condition for nodes 120, 124 and 258

Type: precondition
Status: claimed
Blocked by: none

## Question

Nodes 120 ("Carry the resume rule into the shipped files"), 124 ("Give the manager's contract a procedure for stopping a running worker") and 258 ("The manager's contract contradicts itself on whether a dead worker is resumed or replaced") share one section of `.claude/skills/expedition/SKILL.md` (`## When an agent dies or is stopped`), one section of `.claude/skills/expedition/graph-conventions.md` (`` ### `## Interview` ``) and one glossary entry (`CONTEXT.md`'s **Attempt**). 124 is blocked by 120. The human approved merging them into one node. Write its condition.

*Minted by the manager on the human's "ok" to [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s recommendation, in its worker's words: "Its condition would be 124's approved condition, plus 120's clauses 1 (without the three-state table and the unconditional replacement fallback), 2, 5, 6 and 7, plus 258's clause 1, with strike-in-place dropped."*

## What must be true when this is done

- One acceptance condition, self-contained for a checker that reads only it, carrying: node 124's condition as amended on 2026-09-26 (the 12-item version, which the human approved); node 120's clauses 1 (without the three-state table and without replacement as an unconditional fallback), 2, 5, 6 and 7; and node 258's clause 1. Each clause is tagged with the node it came from.
- No clause asks for superseded text to be marked and left in place in a shipped file: the human took node 330's C2(a), that shipped files are edited plainly.
- Where a user-stopped worker's resume fails, the condition sends the case to the human as a question, as [node 123](123-who-performs-a-stop.md) decided, and never to an automatic replacement.
- Every quote of current text is checked against the files on master and re-pointed where stale. Demands already met are left out, with the reason.
- The fences of the three nodes are replaced by one fence over the union.
- Every conflict between the three nodes' demands, or between a demand and a resolved node, is listed with the options, for the human.
- Nodes that bear on the same section are listed, including node 121 ("What the two-respawn cap becomes") on the "After two replacements" paragraph.

**Later nodes depend on:** the condition, which the manager files as an amendment replacing node 124's condition, superseding nodes 120 and 258 by node 124.
