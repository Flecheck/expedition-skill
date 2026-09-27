# Whether the workflow ships the shadow-spawn instrument for pricing fed context

Type: grilling
Status: claimed

Blocked by: 165

## Question

*Surfaced by [Measure whether a fed file earns its place by running one node twice](165-measure-whether-a-fed-file-earns-its-place.md)'s worker, and pasted as it wrote it.*

> This effort has built a way to price a file it pushes into every worker's context: spawn a second worker on the same
> node without the file, compare the two at their first question, never resume the shadow. It assumes no toolchain and
> installs nothing — it is a spawn discipline over agents the harness already provides — so ground rule 1 does not bar
> it from the shipped files, and the problem it solves belongs to every effort rather than this one. Does it become
> part of the shipped workflow (a manager procedure in `graph-conventions.md`, or a section of the manager's
> contract), stay this effort's own practice, or neither?

**Blockers, in the worker's words:** *"the three pairs from node 165 returning, and their readout. Shipping an
instrument whose first and only use returned nothing would be ranking by predicted value, which this map names as the
token-maxing failure in reverse."*

## The manager's note at filing

*Not a change to anything above.*

**The `Blocked by: 165` edge is the manager's rendering of a blocker its author stated in prose.** Node 165 is
resolved, so the edge is satisfied on its face — but what its author named as the blocker is **the three pairs
returning and their readout**, which is a duty on the manager that has not yet been discharged. The manager records
the mismatch rather than papering over it: the graph's edges cannot express *"after the manager has run the thing this
node's sibling authorised"*, and this node should not be claimed until those three pairs exist.

## Interview

#### Question 1, relayed 2026-09-27

*Pasted as the worker handed it back.*

```
NODE:          181 — Whether the workflow ships the shadow-spawn instrument for pricing fed context

ABOUT:         Node 165 built a way to price a file pushed into every worker's context: spawn a second worker on the same node without that file, compare the two at their first question, and never resume the second one (the "shadow"). This node decides whether that becomes part of the shipped workflow. It is being decided now because you gave token use priority and asked for the skills to be compacted.

SO FAR:        I read the node, map.md, the decisions.md lines on token cost and fed context, and node 165 in full. I searched the rest of the record and the shipped skill files for "shadow".
               - The blocker has NOT been discharged. The node's author said not to decide until node 165's three pairs had returned with their readouts. Here is where they stand:
                 - Pair 1 (node 179) returned null on both readout questions, and under 165's own rules a null licenses nothing. The readout also found something neither question asked about: decisions.md had given the arm that was fed it a stale premise, and that premise carried one of its three grounds.
                 - Pair 2 (node 176) is recorded as spawned, but I can find no readout anywhere in the record.
                 - Pair 3 was never run.
               - The protocol's subject has drifted. Between pairs 1 and 2 the manager started scoping the decisions.md pointer to named entries (the practice from node 185, which is still open). So pair 2 measured something different from pair 1, and a flat decisions.md feed is no longer what spawns actually use. That is also true of this spawn.
               - Today the effort priced fed context another way and acted on it. Node 345 cut map.md from 42 KB to 22 KB because seven workers answered the retrospective's "what arrived that this node did not need" the same way. No shadow was involved.
               - The shipped files (.claude/skills/expedition*) contain no shadow procedure. Shipping one would add a manager procedure to graph-conventions.md or the manager's SKILL.md.
               - Settled on my own authority: I read "the three pairs" as the blocker the author meant, not the resolved-165 edge. I am asking now, not parking, because you gave this node priority and the question can be answered without the pairs.

ASK:           Should the shadow-spawn instrument be shipped in the workflow's files, kept as this effort's own practice, or dropped?

RECOMMENDED:   Keep it as this effort's own practice and ship nothing. The node then stops waiting on the missing pairs.
               - The only evidence so far is one null pair, plus one side finding that neither readout question was built to catch. Shipping it would rank it by predicted value, which is the failure the node's author named.
               - A shipped procedure makes the skills longer, which runs against your compaction ask.
               - A cheaper instrument, the retrospective's "what arrived that this node did not need", already prices fed context. The effort acted on it today with a 20 KB cut.
               - Rule 4 says prefer the simple thing that can be changed later. The shadow stays available to a manager who wants a measurement instead of self-report on a live, reversible choice about a fed file, and it can ship later if a pair ever turns up a divergence.
               - Node 165's leftover duty (filing pair 2's readout, running pair 3) is a separate matter. I would report it for you to decide separately, not keep this node waiting on it.

ALTERNATIVES:  - Ship it now as a manager procedure in graph-conventions.md. The mechanism is sound, it needs no toolchain, and it solves a problem every effort has, but it has returned no divergence yet and it makes the skills longer.
               - Ship it as a section of the manager's contract. Same objection, and it makes the file every manager session loads longer.
               - Wait for pairs 2 and 3 first, as the node's author wanted. The evidence would be better, but it is blocked on work the manager has not done, and the pairs now measure a scoped pointer instead of the flat feed they were designed for.
               - Drop it entirely, including as effort practice. This loses the one instrument that measures waste rather than self-report, at no saving, since running it is optional.
```
