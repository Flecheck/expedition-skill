# The manager's contract contradicts itself on whether a dead worker is resumed or replaced

Type: implementation
Status: superseded
Superseded by: 124

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

## Amendment, 2026-09-24 (from node 296)

*Written by [node 296](296-rewrite-the-manager-contract-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `6745f37`. Every word of the replacement is fixed by that commit or by `CONTEXT.md`. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 296's worker's search handles are on node 296 under its `#### Re-pointing search` and correction rounds.*

- **Clause 1.** Its target, "the vocabulary entry for `attempt`" in `SKILL.md`, no longer exists. Replacement: "**1.** In `.claude/skills/expedition/SKILL.md`, the `## Words used exactly` section, which today states *"A worker is resumed in place rather than replaced."*, states instead that a dead attempt is resumed where the harness allows and replaced only where it does not, and that a replacement is a new attempt recorded after the one it replaces." Clauses 2 and 3 are unchanged. Clause 2 is now where most of the fix lands, because `SKILL.md` takes its `attempt` definition from `CONTEXT.md`.

`258.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 296](296-rewrite-the-manager-contract-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `6745f37` or by `CONTEXT.md`.

*The manager's note, 2026-09-26:* [node 328](328-group-the-open-nodes-against-the-glossary.md)'s C8, taken by the human's "ok", leaves the conflict on the **Attempt** entry (this node's rewrite says "replaced only where it does not", while node 123 sends a user-stopped worker to the human) to the manager-contract grouping, [node 330](330-group-the-open-nodes-against-the-manager-contract.md).

*The manager's note, 2026-09-26:* on the human's "ok" to [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s recommendation, nodes 120, 124 and 258 merge into node 124. [Node 341](341-draft-one-condition-for-nodes-120-124-and-258.md) drafts the merged condition; this node is not started until it is filed.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 124](124-a-procedure-for-stopping-a-running-worker.md), whose condition, drafted by [node 341](341-draft-one-condition-for-nodes-120-124-and-258.md)'s worker and approved by the human's "ok", carries this node's demands tagged with its number.
