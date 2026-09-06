# Whether the workflow ships the shadow-spawn instrument for pricing fed context

Type: grilling
Status: open

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
