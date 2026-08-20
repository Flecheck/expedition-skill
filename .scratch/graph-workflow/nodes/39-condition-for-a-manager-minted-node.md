# Who writes the acceptance condition for an implementation node the manager mints itself

Type: grilling
Status: open

## Question

The five worker contracts now say that a worker reporting an implementation node writes that node's
acceptance condition. That closes the case which produced the defect and leaves the other one open: a node
the **manager** mints itself — from the human's steering, from its own reading of the graph, or as a
replacement in a supersession — has no minting worker, so nobody is assigned its condition. Every
manager-written condition in the evidence table on [A worker's handover carries no acceptance condition for
the node it mints](35-handover-mints-no-condition.md) is of that kind, that node's own included.

Two shipped rules collide on it. [`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)
and [`CONTEXT.md`](../../../CONTEXT.md) both fix a condition as *"written by the node that spawned it"*, which
a manager-minted node has no way to satisfy. And the scribe rule says the manager pastes and never authors —
sharpened by [An acceptance condition is self-contained text](33-condition-is-self-contained.md) into the
manager not being allowed to supply what a condition omits, on the ground that doing so makes it the author
of the standard the work is judged against. A condition it wrote whole is the same act, larger.

So: **may the manager author a condition at all, and if not, does every manager-minted implementation node
cost the human a condition to write?** That is the human's time and therefore the human's call.

A third answer is already on the record and costs neither. Node 35's evidence is that the **audit at claim
time** is what made two manager-written conditions cost nothing while two unaudited ones cost five defects
between them — so the manager could keep the pen for the nodes it mints and inherit the read-back duty the
five contracts now carry.

### One thing that answer now has to survive, measured at the node that proposed it

The audit is not sufficient, and the measurement is on [A worker's handover carries no acceptance condition
for the node it mints](35-handover-mints-no-condition.md) itself. Its condition was manager-written and
audited at claim time; the audit found and repaired two defects, and **the blind checker then found a third
the audit had missed** — a clause the condition dictated that was complete for three of the five contracts
and incomplete for two, discovered only by holding the condition against a file the condition does not name.

So the honest shape of the third answer is *audit plus a check that can still catch what the audit missed*,
which is what happened here and worked. Whether that is good enough for a node whose checker has less to
hold the condition against is this node's to weigh.

### Where the answer lands

The **manager's own skill**, which is still fog on [map.md](../map.md). It touches no worker contract, which
is why it is not blocked by anything and blocks nothing.

Reported by [A worker's handover carries no acceptance condition for the node it
mints](35-handover-mints-no-condition.md)'s worker.
