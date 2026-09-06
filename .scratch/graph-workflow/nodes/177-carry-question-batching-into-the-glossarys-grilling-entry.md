# Carry intra-node question batching into the glossary's grilling entry

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [Carry intra-node question batching into the grilling worker contract](126-carry-question-batching-into-the-grilling-contract.md)'s worker, and pasted as it wrote it.*

> `CONTEXT.md` defines the node kind **grilling** as *"A decision only the human can make, reached by interviewing them
> one question at a time"*, and its **Relay** entry as the payload carrying *"a worker's question"* in the singular.
> Node 126 has removed both claims from the grilling worker contract, so the glossary — which the map declares
> authoritative for a term — now contradicts the shipped contract. Neither node 126's condition nor node 127's reaches
> this file.

**Blockers, in the worker's words:** *"none. Its subject exists only once node 126's change lands, so it is worked
after that gate rather than blocked by an edge."*

## Acceptance condition

*Written by node 126's worker. Pasted as it wrote it, and not the manager's.*

> 1. `CONTEXT.md`'s entry for the node kind **grilling** does not say the decision is reached one question at a time,
>    and nothing in that entry limits a worker to putting one question to the human at once.
> 2. `CONTEXT.md`'s **Relay** entry states that what a relay carries may hold more than one of one worker's questions,
>    rather than describing a worker's question in the singular only.
> 3. Both entries keep their existing `_Avoid_` and `_Note_` lines, and no other entry in the file is required to
>    change by this condition.
> 4. No other line in `CONTEXT.md` states that a worker puts one question at a time to the human, or that exactly one
>    *question* is in front of them. A statement that exactly one *thing awaiting a reply* is in front of them is
>    permitted and is not what this forbids.

## The manager's note at filing

*Not a change to anything above.*

**Its blocker is discharged: [node 126](126-carry-question-batching-into-the-grilling-contract.md) landed as
`8cc9b79`.** Its author wrote no edge and said why; the manager has added none.

**Two agents found this independently.** Node 126's worker reported it on its handover, and node 126's **checker** —
blind to the record and to that handover — reached `CONTEXT.md:114` from the other side and asked whether the human
wanted it amended. The checker also ran an enumerator over the shipped files and cleared two further hits as
non-defects, naming them so nobody re-derives them: `expedition-prototype/SKILL.md`'s own one-at-a-time rule, which is
a different node kind's scope decision, and `expedition/SKILL.md`'s line about concurrent nodes queueing, which stays
true. Its `CONTEXT.md:29` hit is a false positive. **The manager records those three as the checker's findings and
asserts nothing about them**; clause 4 of the condition above is what reaches them, and it is the condition's author's
wording rather than the manager's.

**The human saw the checker's question at node 126's gate and answered it in neither direction**, approving the node.
The manager records the question rather than reading approval as an answer to it.
