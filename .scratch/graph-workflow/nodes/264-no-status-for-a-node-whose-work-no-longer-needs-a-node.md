# The graph has no status for a node whose work no longer needs a node

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [node 252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s worker, and pasted as it
wrote it.*

> Nodes 203 and 245 exist only to amend another unclaimed node's acceptance condition, which node 252 now permits
> directly. Neither should be worked, and neither has a status that says so. `out-of-scope` means the work is beyond
> the destination, which is false — the work is wanted and is simply no longer a node's worth of it. `superseded`
> requires the node to hold work and requires a replacement node to point at, and these hold none and have none.
> Leaving them `open` leaves two nodes on the frontier that nobody should take. What this decides: whether a sixth
> status exists, or whether such a node is disposed of some other way, and what happens to anything listing it in
> `Blocked by:`. Small and low-priority; it has two live instances and no more.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The two instances are live on the frontier right now**, [node
203](203-node-155s-condition-preserves-a-contradiction.md) and [node
245](245-node-156s-condition-re-derives-a-weaker-property.md), and the manager has not touched either. Standing them
down is the manager's by node 252's own words, and the manager is not inventing a status in order to do it.

**One thing the manager holds that the question does not name**: node 203's own acceptance condition is *itself*
falsified, by node 199, which is the fact node 252's worker found. So node 203 is simultaneously an instrument that
is no longer needed and an instance of the disease it was built to cure. Whichever disposal this node settles has to
be right for a node in that state.
