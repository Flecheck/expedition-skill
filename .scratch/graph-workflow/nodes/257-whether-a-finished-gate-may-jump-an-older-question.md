# Whether a finished gate may go ahead of an older tier 1 question

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [node 248](248-review-the-priority-list-and-decide-how-much-ships.md)'s worker, and pasted as it wrote
it.*

> The manager's contract names this collision and leaves it open: tier 1 is ordered by arrival, and a gate holds a
> code slot while it waits where a relayed question does not, so holding a gate behind an older question has a
> throughput cost the older question does not have. The priority list does not settle it — the list ranks classes of
> act, and this collision is inside one of them, item 4 — and the trigger file's "question/gate" phrasing does not
> separate them either. Decide whether a gate may jump an older tier 1 question, and on what test.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The reverse case happened this session and is not what this node is about.** The manager put a newer question
ahead of an older gate, which nothing in the contract leaves open; that is flag `242.3`, filed against the manager.
This node is the case the contract does leave open, and the two should not be run together.
