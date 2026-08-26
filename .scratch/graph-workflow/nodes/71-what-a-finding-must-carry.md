# What a finding must carry so it can be swept

Type: implementation
Status: open

## Question

A checker hands back **instances**. The implementer repairs the instances, and the rest of the class stays in the
file. On [Restructure `map.md` to what every worker needs](59-restructure-the-map.md) the checker reported three
findings; the worker repaired them, swept its own prose on its own initiative, and **found four more of the same
form**. Nothing in either contract asked for that sweep, and nothing would have caught the four if the worker had
not thought of it.

Two repairs, both reported by that node's checker in its retrospective, and one of them is its own correction.

### 1. A finding carries three parts, not one

In the checker's words:

> Last round I handed back instances plus, in finding 2, half a form. What I did not hand back was the thing that
> makes a sweep runnable: **the discriminator that separates text the implementer may touch from text clause 4
> freezes.** Without it, sweeping `map-history.md` for that form returns 87 hits of which 87 are untouchable, and
> the implementer either drowns or abandons the sweep. Building that filter was most of my work this round.

So a finding carries:

- **the instances**, as now;
- **the form, stated as a predicate** — what makes something an instance, not just what these two were;
- **the extent** — the command that enumerates the form's candidates *over the editable part of the work*.

**The checker had already written the enumerator in order to find the instances**, which is what makes this cheap:
it is handing back work already done rather than asking for new work. In its words, *"it is four lines of shell, it
is worth more than the two instances."*

**Its own two qualifications, which the condition must not lose.** Not every finding reduces to a regex — the
over-claims in authored prose had no mechanical enumerator, *"and that is precisely the class where the implementer
found four more by hand."* But such a finding still has an extent, coarser: **the smallest set that provably
contains every instance** — here the 48 authored lines, computed by the same set-difference. And where a finding
genuinely has no extent, **the checker says so rather than implying the instances are exhaustive.**

### 2. A blind checker may not assert a universal negative

The same checker reported *"No such rule exists"* of a rule that does exist, in a file it was correctly kept from
reading. Its own diagnosis:

> What I could actually establish — that the pointer resolved to nothing in every file I was permitted to read —
> was true, and the defect was real. But the sentence I wrote was wrong, and **it was wrong in the same way the
> thing I was faulting was wrong: I asserted a universal from a bounded search.** A checker blind by design should
> say *"resolves to nothing in the files I hold"* and not *"does not exist"*.

**This is a standing property of the role rather than a slip.** A checker is kept from the record by design, so it
can never establish that something is absent from the effort — only that it is absent from what it holds. The
manager, which holds the record, is the party that can resolve such a finding, and did here.

## What has to be decided by whoever claims this

Both repairs land in `.claude/skills/expedition-checker/SKILL.md`. Left unwritten here **on purpose**: this node
has no acceptance condition, and under [A worker's handover carries no acceptance condition for the node it
mints](35-handover-mints-no-condition.md) the manager may write one for a node it mints itself, under that node's
four constraints. It is deliberately deferred because the second repair's wording is the part that matters and the
manager should not fix it in a condition before the human has seen it.

**One open question the manager could not settle.** Whether the extent is *mandatory* on every finding or *owed
where it exists*. Mandatory is simpler to check and would force a checker to invent enumerators for prose findings,
which the checker itself says do not have them. Owed-where-it-exists is honest and gives a checker a way out that
nothing verifies. That is the substance of the node.

## Where it came from

Reported by node 59's checker in its retrospective under the human's standing instruction, in answer to a question
the manager put to it: *is there something a checker could hand back that turns a finding into the sweep, rather
than into three repairs?* It is the fourth return-shape defect found at the same place, after the two [What the
checker contract owes to having been run](31-checker-contract-owes.md) fixed and the one now at [The checker has no
form for two clauses of one condition that cannot both hold](66-two-clauses-that-cannot-both-hold.md).
