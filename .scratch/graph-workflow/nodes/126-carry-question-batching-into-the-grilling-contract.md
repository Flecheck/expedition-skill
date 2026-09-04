# Carry intra-node question batching into the grilling worker contract

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [Whether the manager sends the human questions in batches](117-questions-sent-in-batches.md)'s worker,
and pasted as it wrote it.*

> The grilling worker contract still says one question at a time, its question shape admits one question, and its
> discipline list is prefaced so that the bullet does not bind when the invoked skill is present — while that skill
> now instructs the opposite. Make the file state the adopted rule in its own text.

**Blockers, in the worker's words:** *"none."*

**The worker's note on why this is two nodes rather than one**, pasted: *"I split these by file rather than by
sentence as the manager proposed, because the two manager-contract sentences are one edit to one section while the
worker contract is a different file with a different reader, and a code slot of one serialises them either way."*

## Acceptance condition

*Written by node 117's worker. Pasted as it wrote it, and not the manager's.*

> `.claude/skills/expedition-grilling/SKILL.md` states all of the following in its own text, and nothing in that file
> contradicts any of them.
>
> 1. A worker may put more than one of its own questions to the human in a single payload. Two questions may share a
>    payload only where neither's answer depends on the other's; a question whose answer depends on another in the
>    same payload is held for a later payload.
> 2. Where a payload carries more than one question, each question is numbered, carries a short title, carries its
>    own recommendation and the alternatives it sets aside, and is visibly separated from the next. Where a payload
>    carries exactly one question, that question is not numbered.
> 3. A question's number is fixed for the life of the attempt. Numbers are never reused and never renumbered: a
>    payload re-asking a question asked earlier in the same attempt uses that question's original number, and a
>    question asked for the first time takes the next number not yet used in that attempt.
> 4. A reply naming a question or naming an option settles what it names. A reply that assents to the recommendation
>    without naming any question — *"ok for recommended"* and forms like it — settles every question's recommendation
>    in that payload, and settles nothing in that payload which is not a recommendation.
> 5. A question the reply does not name is unanswered rather than deferred. It goes out in a later payload. The
>    worker never reads an unnamed question as assent and never answers one itself.
> 6. The human deferring is something they state. Nothing in the file treats a question the reply failed to name as a
>    request to defer.
> 7. The file places no requirement on the form of the human's reply, requires no numbered reply, and makes no claim
>    about what form a reply will take.
> 8. The file does not use the word "frontier" for the questions carried in a payload.
> 9. Every one of items 1 to 8 is stated in this file's own text. None of them is left to be supplied by any skill
>    the file instructs the worker to invoke, and the file does not make any of them conditional on such a skill
>    being present or absent.

## The manager's note at filing

*Not a change to anything above.*

**This condition carries no enumerator and states no scope beyond one file**, which is [node
94](94-condition-scope-as-a-predicate.md)'s rung 3 case rather than a malformation: its scope is one named file and
was not derived from a search. Clause 9's *"in this file's own text"* is a demand on that file rather than a
quantifier over the tree. **The manager has not amended it.**

**One fact the worker established that this condition does not name, and that its worker will meet.** The file
contradicts itself today: its discipline list is prefaced *"Where they are not present, this is the whole of the
discipline"*, so its *"One question at a time"* bullet does not formally bind while `/grilling` is present, and
`/grilling` now instructs the opposite. Clause 9 reaches that preface; nothing else does.
