# The checker has no form for two clauses of one condition that cannot both hold

Type: grilling
Status: claimed

## Question

A checker met two clauses of one acceptance condition that **cannot both be satisfied**, where which one gives way
is a **reading** rather than a fact. Its contract's routing table has no branch for it.

In the checker's own words, from [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md):

> No form for the case I actually hit: two clauses of one condition that cannot both hold, where which one gives
> way is a reading rather than a fact. The routing table has *"you can check it and disagree"*, *"complying is what
> produced the defect"*, *"a part you cannot establish"*, and *"the condition is broken, raise"*. None fits. I took
> the reading that keeps the condition satisfiable and put the alternative in `QUESTIONS`, but the contract did not
> tell me to, **and a checker taking the strict reading would have failed the work for obeying clause 4.**

That last clause is what makes this more than a gap in a table. **The same work passes or fails on which reading
the checker happens to take**, and the contract is silent, so the outcome is set by the checker's disposition
rather than by the work.

**Why *the condition is broken, raise* is the wrong branch, and this is the substance of the decision.** A raise
stops the check. But the condition here was **satisfiable** — the checker found a reading under which every clause
holds, and the work met it. Raising would have spent a gate on a question the check could answer, on an effort where
a check is sometimes *unavailable* and six runs have died. The cheap disposition is what the checker improvised:
**take the satisfiable reading, establish the clauses under it, and hand the alternative back as a question.** The
decision is whether that becomes a fifth branch, and what it must carry so the human can overrule it.

**It is the third return shape improvised at the same place.** [What the checker contract owes to having been run
](31-checker-contract-owes.md) fixed the first two — the reserved clause and the non-blocking `QUESTIONS:` — and
this is the same defect recurring: a checker meeting a case its contract does not name, doing the sensible thing,
and the sensible thing reaching the next checker only if someone writes it down.

## What has to be decided

1. **Whether the satisfiable reading is the mandated default**, or whether the checker must raise and let the human
   choose. The trade is a gate against a wrong-way failure.
2. **What the handover must carry when it takes that route** — at minimum the reading taken, the reading declined,
   and which clauses would be unmet under the declined one, since the checker on node 59 supplied all three
   unprompted and the value was entirely in the third.
3. **Whether the verdict is qualified.** A `PASS` under a reading is not the same object as a `PASS`, and nothing in
   the shipped form distinguishes them.
4. **Who owns the repair afterwards.** The checker said it plainly — *"if the strict one does, it is the condition
   that needs amending rather than the work"* — and an acceptance condition is not the manager's to rewrite
   ([An acceptance condition is self-contained text](33-condition-is-self-contained.md)), so amending one after a
   check has run has no owner.

## Two instances already on the record

- **Node 59's clauses 4 and 9.** Clause 4 required moved history verbatim; the moved text contains a line-number
  citation that clause 9 bans. **Both the worker and the blind checker independently took the same reading** —
  clause 9 governs the pointers the files offer, not a preserved quotation — which is evidence the satisfiable
  reading is discoverable rather than arbitrary. It is flag `59.1` and the checker's first question.
- **Node 45's clauses 1 and 2**, where the manager's own audit recorded that *"if clause 1 is done loosely, clause 2
  is unsatisfiable rather than merely hard."* That one resolved by the ordering being load-bearing rather than by a
  reading, so it is a near miss rather than an instance — worth reading beside this because it shows the shape
  arriving a fourteen nodes earlier without being recognised.
