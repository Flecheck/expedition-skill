# Repair the two `CONTEXT.md` defects node 113 found

Type: implementation
Status: open

Blocked by: 133

## Question

*Surfaced by [Whether the contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md)'s worker, and pasted as it wrote it.*

> Correct the glossary's method-skill count and its superseded grilling entry.

**Blockers, in the worker's words:** *"node 2 above, whose deletion changes what the count should say."* That is
[node 133](133-carry-the-method-skill-deletion-into-the-contracts.md).

## Acceptance condition

*Written by node 113's worker. Pasted as it wrote it, and not the manager's.*

> `/home/mathieu/projects/graph-agent/CONTEXT.md` is changed, and no other file.
>
> 1. Its `## The five kinds of node` section no longer asserts that three of the five kinds name a skill the worker
>    invokes. Whatever replaces that clause is true of the shipped contracts as they stand when this work is done.
> 2. Its **grilling** entry no longer says the decision is reached by interviewing the human one question at a time.
>    It states instead that a worker may put several of its own questions to the human in one payload where no
>    question's answer depends on another's in that payload, and that a question whose answer depends on another in
>    the same payload is held for a later one.
> 3. Superseded text is marked as superseded and left in place rather than deleted, and new text is added around it.
> 4. The `_Avoid_` line on the grilling entry is preserved.
>
> Held against the bar.

## The manager's note at filing

*Not a change to anything above.*

**Clause 1's *"true of the shipped contracts as they stand when this work is done"* is the first condition on this
graph to state a demand against the tree at the moment of the work rather than at the moment of writing.** After node
133 lands, no contract will name a skill at all, so the clause the count sits in may need removing rather than
recounting. That is the worker's to determine from the tree.

**One collision the manager must sequence.** [Node 107](107-context-reserves-the-word-report.md)'s repair will own
`CONTEXT.md`'s `Handover` `_Avoid_` line, its `Closing report` entry, a new entry for the node-level report, and its
`Flag` and `Raise` entries. **This node touches neither of those** — the kinds-of-node section and the `grilling`
entry — so they do not collide, but both edit the same file and with a code slot of one they serialise.
