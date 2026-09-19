# Collapse the two map notes the priority list now subsumes

Type: implementation
Status: open

Blocked by: 255

## Question

*Surfaced by [node 248](248-review-the-priority-list-and-decide-how-much-ships.md)'s worker, and pasted as it wrote
it.*

> `map.md`'s `## Notes` hold two long live rules the shipped priority list now states more briefly — that the
> manager never idles and starts the next work the moment a node finishes, and that a payload goes over as soon as
> it is ready and still one at a time. Replace each with its current statement, pointing at the priority rather than
> restating the ordering, and bank the superseded text.

**Blockers, in the worker's words:** *"node 1 above, so the map points at a section that exists."* That is [node
255](255-ship-the-priority-list-into-the-managers-contract.md), recorded in this node's `Blocked by:` field.

## Acceptance condition

*Written by node 248's worker. Pasted as it wrote it, and not the manager's.*

> The work is done when both hold.
>
> **1.** In `.scratch/graph-workflow/map.md`, the `## Notes` item stating that the manager never idles
> and starts the next work itself the moment a node finishes, and the item stating that a payload goes
> over as soon as it is ready and still one at a time, each carry a current statement that no longer
> restates the ordering between writing, resuming, spawning and giving a question, and instead names the
> priority in the manager's contract as where that ordering is stated. Each item keeps the human's own
> words that it carries, marked `verbatim` as they are now, and keeps whatever it states that the
> priority does not — in particular that a payload's release is triggered by the payload being ready
> rather than by the human speaking, and that a live question does not block a start.
>
> **2.** The full existing text of both items, as it stands before this work, appears verbatim in
> `.scratch/graph-workflow/map-history.md` under the heading mirroring the section it came from. No text
> is lost: every sentence removed from `map.md` by this work is present in `map-history.md`.
>
> The bar applies as it does to any implementation node.

## The manager's note at filing

*Not a change to anything above.*

**This is the deletion the human expected from the priority list, and it is here rather than in the shipped
files** — node 248's answer establishes that the shipped contract holds only two such clauses while this map holds
two long ones. It is a never-delete operation on the record, which is why its author split it from the shipping node
rather than coupling them.
