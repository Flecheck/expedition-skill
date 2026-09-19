# The manager's contract contradicts itself on whether a dead worker is resumed or replaced

Type: implementation
Status: open

Blocked by: 255

## Question

*Surfaced by [node 248](248-review-the-priority-list-and-decide-how-much-ships.md)'s worker, and pasted as it wrote
it.*

> In `SKILL.md`'s vocabulary, the `worker` entry says a worker "is resumed in place rather than replaced" and the
> very next entry, `attempt`, says "a dead worker is replaced, and the replacement is a new attempt".
> `CONTEXT.md`'s `Attempt` entry says replaced too. The substance is already settled — an agent is resumed wherever
> the harness allows — so this is carriage that was done at one site and not the others.

**Blockers, in the worker's words:** *"node 1 above, both touching `SKILL.md`."* That is [node
255](255-ship-the-priority-list-into-the-managers-contract.md), recorded in this node's `Blocked by:` field.

## Acceptance condition

*Written by node 248's worker. Pasted as it wrote it, and not the manager's.*

> The work is done when all three hold.
>
> **1.** In `.claude/skills/expedition/SKILL.md`, the vocabulary entry for `attempt` no longer states
> that a dead worker is replaced. It states instead that a dead attempt is resumed where the harness
> allows and replaced only where it does not, and that a replacement is a new attempt recorded after the
> one it replaces.
> **2.** In `CONTEXT.md`, the `Attempt` entry is changed the same way and for the same reason.
> **3.** No statement anywhere in either file says that a dead worker is replaced without saying that
> resuming is tried first. The two files do not contradict each other on this point.
>
> The bar applies as it does to any implementation node.

## The manager's note at filing

*Not a change to anything above.*

**This session is the evidence the substance is settled.** Node 243's attempt stopped on a harness error, the
manager attempted the resume, the harness allowed it, and the same attempt carried on and answered its node. The
record of it is on that node, corrected from an earlier entry that called the attempt dead.
