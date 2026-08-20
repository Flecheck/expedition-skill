# Record a checker's not-covered part on `## Review`

Type: implementation
Status: open

Blocked by: 31

## Question

[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md) fixes the `## Review`
chronology as **three entry kinds** — a run naming `PASS`, a run naming `FAIL` and which of the two failed,
or a run that raised instead of judging. [What the checker contract owes to having been
run](31-checker-contract-owes.md) has now given the checker a fourth thing it can hand back: a `PASS` or a
`FAIL` that **names a part of the acceptance condition it does not cover**.

An entry that says only `PASS` loses that. A later reader cannot tell which parts the check actually covered,
and the residual the manager picked up has nowhere to be recorded as discharged.

**What does the entry record, and where does the manager's discharge of a reserved part land?**

### Why this exists

Reported by [What the checker contract owes to having been run](31-checker-contract-owes.md)'s worker, as the
cost of the rider it had just shipped. Its own framing: this is the same shape [Whether a spawn may override a
shipped worker contract](28-spawn-overriding-a-contract.md) ruled for the mid-node amendment — **an uncovered
case rather than a departure** — and the same cost flag `26.7` records, a described case with no rule reaching
it.

### Two things already established, and they bound the answer

**The duty being recorded is real and already named.** [An acceptance condition is self-contained
text](33-condition-is-self-contained.md) found that *the manager is the residual checker of anything a
condition addresses to a party that cannot see it*, and the manager verified that node's reserved clause
itself. So a reserved part is not a gap in the check; it is a handoff, and what this node designs is the
record of the handoff.

**The duty is also now avoidable, which changes how much machinery it deserves.** [The clause that says no
resolved node changes cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md) wrote a
condition with every demand landing in a file and its checker reserved nothing; node 31's did the same and
its checker reserved nothing either. Two consecutive checks with no residual, against node 33's three
reserved clauses on one condition. So the recording form is for the **exception** rather than the common
case, and a form that costs every entry something to serve a case that a well-written condition never
reaches would be the wrong trade.

### One thing not to assume

That the answer is a fourth entry kind. The rider is deliberately **not** a fourth return shape — node 31's
worker split `NOT COVERED:` from `QUESTIONS:` into the same structural slot precisely so the three shapes and
the three entry kinds would stay valid, and flag `31.1` records that call. An entry kind is the parallel
choice one level up, and taking it would undo the reason the rider was shaped that way. The cheaper
candidates are a required field on an existing entry, or the manager's discharge recorded where it happens
rather than as part of the chronology.

### What the answer touches

[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s `## Review` shape, and
possibly `expedition-checker/SKILL.md` if the entry form needs anything the rider does not already carry.

**Sequencing.** `Blocked by: 31` is a real edge rather than a preference: the rider has to ship before a
recording form can name it. Nothing else on the frontier touches `graph-conventions.md`.
