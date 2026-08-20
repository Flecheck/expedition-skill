# Nothing tells a worker to hold its work against the record

Type: grilling
Status: open

## Question

The record-wide demand has left acceptance conditions, and `INVALIDATIONS` on the handover is now the only
thing carrying it. **Nothing tells a worker to go and look.**

All five worker contracts word it as a report:

```
INVALIDATIONS: <which resolved node your work contradicts, and how>
```

> *"Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them."*

There is no instruction to check, and no statement of how much of the record a worker is expected to read
to answer it. A worker reads its own node, `map.md`, and only the `decisions.md` sections its spawn names —
so it cannot hold its work against the whole record either.

**Is `INVALIDATIONS` a duty to check, or only to report what surfaced while working?** If the former,
against what — and does the spawn have to hand the worker more of the record than it does today?

### Why this exists

Created at [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md)'s gate, reported by that node's own
worker as **the honest cost of the answer it had just shipped**. That node ruled the demand out of
acceptance conditions on the ground that `INVALIDATIONS` already carries it, addressed to a party that can
discharge it. Its worker then said what that leaves, in its own words:

> The duty's new home is checked by nobody: the five contracts ask a worker to *report* `INVALIDATIONS`,
> not to go and look, and nothing says how much of the record a worker is expected to hold its work
> against. That is strictly better than where it was — four independent blind checkers each spent a verdict
> on node 22's condition 3 and each declared it not establishable — but it is not enforcement.

**Nothing checks it in either case, which was also true of the clause it replaces.** So this node is not a
regression opened by node 36; it is the same hole, now in one place instead of two, and visible.

### One fact already established, and it bounds the answer

Node 36's checker went and confirmed the asymmetry the shipped paragraph rests on, rather than taking the
file's word for it: `INVALIDATIONS` is present in all five worker contracts and **absent from the
checker's own**. It also settled how much of the record a worker can reach — all five contracts read
`decisions.md`, which is one capped line per resolved node and therefore **the index of the whole decision
record**; only `flags.md` is withheld, and flags are not decisions.

So a worker can already reach an index of every decision the effort has made. What it cannot reach cheaply
is the reasoning behind any of them, which lives in the node files. Whether the index is enough to answer
`INVALIDATIONS` honestly is the crux: an index is enough to notice a collision and not enough to judge one.

### What the answer touches

The five `.claude/skills/expedition-<type>/SKILL.md` contracts, and possibly
[Subagent context contract](12-subagent-context-contract.md)'s spawn template if the answer is that the
spawn must hand over more of the record.

**Sequencing, not a blocker.** Those five files are also the live territory of [Checking a flag before the
human sees it](30-checking-a-flag-before-the-human.md), [A worker's handover carries no acceptance
condition for the node it mints](35-handover-mints-no-condition.md) and [Narrow the flags.md clause in the
worker contracts](32-narrow-flags-file-clause.md). The landing policy forbids a second commit against one
**node**, not against one **file**, so these may run in any order — but not concurrently, the code slot
being exclusive.

### Adjacent, and not the same question

[Cascade pass mechanics](15-cascade-pass-mechanics.md) owns the pass that propagates a *known* revision
outward, and [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md) owns the same problem for product files. Both are about acting on an
invalidation once someone has found one. This node is about **finding** it, at the one moment a party with
the work in front of it is already being asked.
