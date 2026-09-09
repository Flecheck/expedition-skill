# Collapse the rules file's two statements that accounts live in `map-history.md`

Type: implementation
Status: claimed

Blocked by: 196

## Question

*Surfaced by [Give `map-implementation-rules.md` its admission
test](196-give-the-rules-file-its-admission-test.md)'s worker, and pasted as it wrote it.*

> The opening of `map-implementation-rules.md` now says twice that the account behind a line belongs in
> `map-history.md` — once in the new admission test, which states it as a consequence of the test and is where a
> reader needs it, and once as the trailing sentence of the *"Nothing below was reworded on the way here"*
> paragraph, whose subject is otherwise the verbatim move. The second is subsumed by the first and sits under a
> lead-in it does not belong to. Which one stays, and does the loser move to `map-history.md` under the supersession
> rule or leave plainly under node 189's boundary?

**Blockers, in the worker's words:** *"none. It is the same class of defect as node 190 and touches only the file's
opening, so it must not hold a worktree over that file concurrently with another node."* **The manager has added the
edge to 196**, whose uncommitted work creates the duplication this node repairs; the two cannot run together.

## Acceptance condition

*Written by node 196's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited. The worker may
> not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. Done means all of the following
> are true of the finished tree.
>
> 1. The text before the file's first `##` heading states exactly once that the account behind a line in the file
>    belongs in `map-history.md`; the sentence *"The account behind a line here is in
>    [map-history.md](map-history.md), as it is for a line in `map.md`."* no longer stands as a second statement of
>    it.
> 2. The paragraph beginning *"Nothing below was reworded on the way here"* still carries its warning that a
>    paragraph saying *above* or *below* may point into `map.md`, and both of its worked examples — the review
>    route's two phrases — are unchanged.
> 3. Whichever text is retired leaves under one of the two routes the file itself states: appended verbatim to
>    `map-history.md` under a heading mirroring the section it came from, or removed plainly where it is a live rule
>    statement being replaced. The finished file states which route was taken.
> 4. The statement beginning **What this file admits.** keeps all of: that a line belongs only where an
>    implementation node's worker or its checker would act differently for having read it; that how a rule was
>    learned is not that; the trigger-versus-history distinction; and that whoever is already editing a passage
>    applies the test to that passage with no sweep owed. It stays at most 1,000 bytes.
> 5. Every paragraph under `## Landing an implementation node's work` and under `## What the work is held against`,
>    and both blocks of numbered rules — the five ground rules and the four standing rules for writing — is
>    byte-identical to what it was in the worker's tree before this work.
> 6. Every markdown link in the file resolves to a path that exists.
> 7. No file outside `.scratch/graph-workflow/` is modified.
> 8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its author created the duplication under a condition that forbade it from doing anything else, and said so.** Node
196's clause 1(c) required the new statement to say in its own text that such material belongs in `map-history.md`;
its clause 7 forbade removing the older sentence that already said it. **Neither clause could be breached, so both
sentences stand**, and the worker surfaced this rather than reading either clause generously. That is flag `196.2`.

**This is the fifth node this session created by a condition fencing its own worker out of a defect it created** —
after the chain 144 → 169 → 184, node 139 → 142, node 142 → 195, and node 140's *"unchanged in wording"* → node
191. **The manager records the shape and takes no view**; whether narrow conditions are worth their cost is not
this node's question and has never been anyone's.

**Its clause 3 is answerable now in a way its author could not assume.** [Node
189](189-where-the-never-delete-rule-stops.md) settled that a superseded **rule statement** is replaced plainly and
banked verbatim to `map-history.md`, while text recording what happened is struck in place — so which of the two
routes clause 3 offers applies turns on what the retired sentence *is*, and that test now exists in the file
itself.

## Interview

### Attempt 1 — the gate, and the condition amended there

**What was put to the human.** The manager raised this node's gate on a `PASS`, and the human read the finished
file and asked why history stands in it. What they were looking at is the tail of the paragraph this node edited:
*"A second statement of where the account behind a line lives once trailed this paragraph… it moved verbatim to
map-history.md rather than being struck in place."* That is *what this file said before*, which the admission test
three paragraphs above it sends to `map-history.md`. **Clause 3's last sentence is what put it there**, and both the
worker (flag `200.1`) and the checker reported the collision rather than resolving it.

**The human's word, `verbatim`.**

> 1

**The option that `1` names, quoted from the gate, and it is the manager's wording rather than a worker's:**

> **Amend clause 3** so the route statement lives in `map-history.md` only — I send node 200 a correction round to
> delete those two sentences, and it re-checks.

*The two options it was taken over: approve as it stands and leave the sentence for whoever next edits that passage
under the admission test's own rule; or reject.*

## The acceptance condition, clause 3 as amended

**The amendment is the human's.** The manager wrote the option and does not author or rewrite a condition; what
follows is the clause with its last sentence replaced, and nothing else in the condition is touched.

> 3. Whichever text is retired leaves under one of the two routes the file itself states: appended verbatim to
>    `map-history.md` under a heading mirroring the section it came from, or removed plainly where it is a live rule
>    statement being replaced. ~~The finished file states which route was taken.~~ **The `map-history.md` entry
>    states which route was taken. `map-implementation-rules.md` states none of it, and what stands in its place
>    there is the markdown link to the node that shaped the passage — which is what that file's own admission test
>    prescribes.**

**What this settles about the two flags.** `200.1` is answered by the amendment rather than by the human agreeing
with the worker: the clause the worker could not satisfy without contradicting the file no longer asks for it.
`200.2` — clause 3's two routes overlapping — is untouched by the amendment and still stands as filed.
