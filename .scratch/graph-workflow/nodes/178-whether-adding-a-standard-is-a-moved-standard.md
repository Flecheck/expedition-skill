# Whether adding a standard is a case of `### Where the work moved one of them`

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [Carry the record-node reading rule into the implementation-rules file](171-carry-the-record-node-reading-rule-into-the-rules-file.md)'s worker, and pasted as it wrote it.*

> The checker contract tells a checker that when an element of a standard it holds work
> against was added, removed or altered, it has nothing unmoved left to hold the rest of the
> work against and must raise. On this effort the standards file is itself frequently the
> work — nodes 140, 144, 169 and 171 all edit it — and every such node *adds* an element by
> construction. Does a pure addition, which leaves every pre-existing element unmoved, fall
> under that bullet, or does the bullet reach only a standard rewritten in place? If it
> reaches additions, every node that extends this file deadlocks its own check.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**This is [flag `171.1`](171-carry-the-record-node-reading-rule-into-the-rules-file.md)'s subject**, and the two are
the halves of one thing: the flag records that the worker judged a check still possible and shipped, and this node is
where that judgement gets tested by the party that can settle it.

**It has already been met once, from the other side.** [Node 144](144-make-the-rules-file-stand-alone.md)'s checker
hit the same bullet, described it as *"a bright line"*, and **declined to cross it** — it proceeded and reported
rather than raising, on the ground that the bullet's own stated reason (*"nothing unmoved left to hold the rest of the
work against"*) did not obtain when seven of eight elements were unmoved. That checker asked in as many words whether
*"the contract wants a middle branch for a list that loses an entry"*. **The human saw that question at node 144's
gate and approved without answering it.** So two agents have now improvised past this bullet in the same direction,
neither with authority to.

**Node 171's own check is live as this is filed**, and the manager spawned it without pre-authorising anything, so a
raise on this bullet is a possible outcome rather than one that has been ruled out.
