# Whether a checker may write scratch files outside the work

Type: grilling
Status: open

## Question

The checker contract's hard rule 1 is *"write no file"*. A checker on [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md) had to establish that **nothing was deleted** across ~40,000 characters of prose
on both sides of a diff — a set operation. It wrote five scratch files outside the work to do it, and removed them.

In its own words:

> Hard rule 1 says *"write no file"*. Establishing clause 4 meant set operations over ~40,000 characters of prose on
> both sides of a diff. I did most of it with process substitution but wrote five files under `/tmp` for the
> comparison and removed them afterwards. Saying whether scratch outside the work is permitted would settle it,
> because **the honest alternative is to establish clause 4 by eye, which on 35 lines averaging 1,500 characters is
> not establishing it.**

**That last sentence is the whole node.** The rule as written does not merely inconvenience the checker; on any
clause requiring an exact comparison over more text than fits in a judgement, it makes the difference between
**establishing** a clause and **asserting** it. A checker that obeys the rule literally and reports `PASS` on clause
4 has done the thing the mechanical checks exist to prevent.

**Why the rule exists, so the decision does not undo it by accident.** The prohibition keeps the checker from
writing the graph, from writing the product, and from leaving anything behind that a later reader mistakes for the
work. None of those reasons reaches a temporary file outside the tree that is removed before the handover. But the
rule is stated absolutely, and a hard rule read down by an agent on its own authority is precisely what [Reconcile a
method skill's instructions with the contract's hard rules](48-method-skill-conflicts-hard-rules.md) was opened to
stop — so the reading has to be **granted**, not inferred.

## What has to be decided

1. **Whether scratch outside the work is permitted at all**, or whether the checker's route is instead to be given
   a mechanism that needs no files.
2. **Where.** The machine-local temporary directory is the obvious answer and the wrong shape for a shipped file —
   ground rule 1 forbids assuming this machine, and the human's own standing instruction refuses a bare `/tmp`.
   Stating the **property** (a location outside the work, discovered rather than declared) is the likely form.
3. **Whether it must be cleaned up, and whether an uncleaned file is a finding against the checker.** The checker
   here removed its own without being asked.
4. **Whether the same permission is owed to the other five contracts.** A worker under a no-file rule establishing
   its own work faces the identical wall, and node 59's worker reported keeping *"the scratch build scripts and the
   before-state copy"* outside the repo — so **it took the same licence, unasked, and disclosed it.** Two agents,
   two contracts, the same unstated permission exercised.

## Where it came from

Reported by node 59's checker in its retrospective, under the human's standing instruction. The manager records one
thing beyond what the checker said: **this is the second agent on the same node to write scratch outside the tree
under a no-file rule**, and neither was faulted for it, so the practice already exists and only the permission is
missing. That is the [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md) problem in its purest form — a rule the shipped files state absolutely and
that every agent quietly reads down.
