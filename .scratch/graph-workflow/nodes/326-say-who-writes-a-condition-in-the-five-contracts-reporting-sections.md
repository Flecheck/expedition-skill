# Say who writes a condition in the five contracts' reporting sections

Type: implementation
Status: superseded
Superseded by: 333
Blocked by: none

## Question

In all five worker contracts, `## When a node you report is an implementation node` opens with a general statement: "An `implementation` node can be claimed only once it carries an **acceptance condition**: what done means for that node, written by the node that spawned it, before any work on it starts." Read alone, as a definition of every implementation node, it is false for a node the manager created. Node 325's own question judged this phrase "correct in place", because the next sentence says the reporting worker's node is the spawning node. That second sentence is correct. The opening sentence, though, makes a claim about every implementation node. Should it be qualified the way the glossary (node 318) and the implementation words list (node 325) were? This node overlaps node 325's question text, so the human may judge it unneeded.

*Reported by [node 325](325-say-who-writes-a-condition-in-the-implementation-contracts-words-list.md)'s worker, which gave it no blockers. The manager put it to the human at node 325's gate, saying it would mint it unless told to drop it; the human approved without dropping it.*

## Acceptance condition

*Authored by node 325's worker and filed by the manager.*

1. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-research/SKILL.md`, the first sentence under `## When a node you report is an implementation node` no longer says without qualification that an implementation node's acceptance condition is written by the node that spawned it. It says the condition is written before any work on the node starts, by the agent that created the node, or by the manager where the manager created it.
2. In each of those five files, the sentence saying that when you report one, your node is the one that spawned it, and that you write its condition in the `NEW NODES` block, is unchanged.
3. No other text in those five files changes, and no other path changes.
4. The working tree meets the bar.

*The manager's note, 2026-09-26:* claimed and then released before any worker started, and its empty worktree removed. The human asked for open nodes to be grouped by file, and this node goes to the worker-contracts group, [node 329](329-group-the-open-nodes-against-the-worker-contracts.md).

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md), the merge [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
