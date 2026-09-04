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

> `CONTEXT.md` is changed, and no other file.
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

## A second condition, offered by a later worker and filed beside the one above rather than replacing it

[Node 133](133-carry-the-method-skill-deletion-into-the-contracts.md)'s worker surfaced this node again, not knowing
it existed, and wrote its own acceptance condition for it. **The condition above stands**: it was written by node
113's worker, which is the node that surfaced this one, and neither the manager nor any later worker may rewrite it.
This is filed because it carries something the one above does not.

**What it carries that the filed condition does not: an enumerator with a domain.** Its clause 1 names six contract
files and seven strings and demands the scan return nothing; the filed clause 1 states the same demand as a property
and names no way to establish it. Under [node 94](94-condition-scope-as-a-predicate.md)'s rungs that is the
difference between rung 2 and rung 1, and under [node 110](110-does-the-checker-rerun-the-enumerator.md)'s rule an
enumerator with a recorded return is something this node's checker would re-run and report.

**Pasted as node 133's worker wrote it.**

> `CONTEXT.md` at the repository root is changed, and no other file is.
>
> 1. The sentence "Each names what its worker does, and three of them name a skill the worker invokes." no longer
>    claims that any number of the kinds names a skill the worker invokes. No shipped worker contract does: a scan of
>    `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`,
>    `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`,
>    `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-checker/SKILL.md` for the
>    strings `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`, `/research`, `/prototype` and
>    `mattpocock` returns nothing, and that is the state the sentence must describe.
> 2. The **grilling** entry no longer says the human is interviewed "one question at a time". It states instead that
>    a worker may put more than one of its own questions to the human in a single payload, and that two questions
>    share a payload only where neither's answer depends on the other's.
> 3. Neither change deletes an entry or a `_Avoid_` line, and no `_Avoid_` line is weakened: every word refused
>    before is still refused.
> 4. Nothing else in the file is changed.
>
> Held against the bar.

***The manager's note.*** **The manager has substituted nothing and chosen nothing.** Whoever holds this node reads
both, and where it judges the filed condition defective, that is a raise rather than a rewrite — a condition that is
wrong goes to the human. **One fact bearing on that raise:** node 133 has landed the deletion its clause 1 turns on,
and node 133's own checker independently reported the same `CONTEXT.md` sentence as now contradicting the shipped
state, giving the same enumerator's domain.
