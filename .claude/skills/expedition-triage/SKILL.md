---
name: expedition-triage
description: Triage an expedition's open nodes and outstanding flags. The human invokes it in an expedition's manager thread, and the manager checks every open node against the current working tree and proposes, in one payload, which nodes are moot, dropped, merged or kept, and which flags settle.
---

# Triaging the open nodes and the outstanding flags

You are the manager of an expedition, and the human has invoked this skill. It checks the open nodes
and the outstanding flags against the current state of the repo, and proposes what to do with each.

This skill runs only when the human invokes it. Run none of it on a schedule or on your own judgement.

## Check each open node

Check each open node against the current working tree and the current shipped files, and not against
what the effort's record says about it. You may give this checking to read-only agents. Have each one
quote the current text its finding rests on.

Also check an open node whose `Deliverable:` field names deliverables against the tip of each named
deliverable's branch. Read each tip's files through git, without checking the branch out.

Sort each open node into exactly one of four classes:

- **moot**: the work the node asks for is already done, or the text it targets no longer exists.
- **dropped**: the node is still live, but it is not worth its cost to the effort's destination.
- **merged**: the node concerns the same file and the same concern as another open node.
- **kept**: none of the three above.

For a kept implementation node, say in the proposal whether its acceptance condition quotes text that
no longer exists.

## Check the outstanding flags

Propose settling, in one batch, the outstanding flags whose node is `resolved` or `superseded`. Leave
outstanding the flags whose node is `open` or `claimed`. This changes the rule under `## Flags` in your
contract for this one case: the human's approval of the batch is the moment its flags settle.

Where a merged node holds a flag, and the flag judges the clauses that move, leave the flag outstanding.
This changes the rule under `## Flags` in your contract for this one case: the flag settles at the gate
of the node that receives those clauses, and not at its own node's gate or node closing report.

## The proposal

Put the proposal to the human as one payload. It holds one numbered question per class and one for the
flag batch. Each question lists its nodes or flags, each with a one-line reason, so that one reply
answers the question.

Change no node's status and no flag's state before the human has answered.

## After the human answers

Carry out what the human approved. Each act uses the procedure under its heading in
`graph-conventions.md`.

- A moot node is superseded by the node whose work made it unnecessary, under `### Supersede`. Where no
  node did, resolve it under `### Resolve`, with an answer saying it was discharged with no edit, and
  why.
- A dropped node is ruled out of scope, under `### Rule out of scope`.
- A merged node's clauses are added to the other node's acceptance condition, under
  `### Amend an acceptance condition`. The merged node is then superseded by that node, under
  `### Supersede`. `### Changing one after it is written` in your contract says which nodes may be
  amended.
- A flag in an approved batch is settled, under `### Settle a flag`. Where an older flag entry has no
  id, this changes step 1 of `### Settle a flag`: give the entry the next unused id on its node, mark it
  settled, and write a note of your own on its node saying so.
