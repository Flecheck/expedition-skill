# Give each question in a multi-question payload a context line

Type: implementation
Status: superseded
Superseded by: 333
Blocked by: none

## Question

Carry the payload-shape rules decided at node 259 into the grilling worker contract.

*Reported by [node 259](259-a-multi-question-payload-has-no-per-question-ground.md)'s worker, which gave it no blockers: "Node 322 edits the "What a reply settles" bullets of the same file, a different part of it. The manager sequences the two edits."*

*The manager's note:* node 322 has landed (`a57f9cd`). This node changes the grilling contract, which [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s proposed worker-contracts merge fences; under the human's instruction that a related defect joins an existing node, the manager proposes folding it into that merge.

## Acceptance condition

*Authored by node 259's worker and filed by the manager.*

In `.claude/skills/expedition-grilling/SKILL.md`, under the heading `### question — you need the human`:
1. In the fenced block that shows the shape for more than one question, each of the two example questions (Q1 and Q2) has a line beginning `CONTEXT:`, with the field name padded to the same column as the other field names. The line is placed after that question's `Q<n>. <short title>` line and before its `ASK:` line. Its placeholder says that the line holds why this one question is asked, and that the line is left out when the question needs none.
2. The fenced block that shows the shape for one question contains no `CONTEXT:` line and is otherwise unchanged.
3. The prose of that section states each of the following:
   a. In both shapes, `ASK` holds only the question, in a sentence or two.
   b. `CONTEXT` belongs to the multi-question shape only. It holds why its question is asked, and it is left out when there is nothing of that kind to say.
   c. A finding that explains why the recommendation is recommended goes in that question's `RECOMMENDED`, after the recommendation itself.
   d. A fact that more than one question in the payload rests on goes in `SO FAR`.
4. The sentence that lists what each question in the multi-question shape carries (today: a number, a short title, its own recommendation, and the alternatives it sets aside) also names the optional context line.
5. No other part of the file changes what it requires, and no other file under `.claude/` is changed.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md), the merge [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
