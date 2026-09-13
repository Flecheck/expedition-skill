# A failed `git merge --ff-only` can leave the tree partially updated, and the record says it cannot

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 216](216-what-a-correction-round-after-a-rebase-conflict-owes.md)'s worker, and pasted as it
wrote it. **The manager is the party that hit this**, at node 198's landing, and reported it to that worker.*

> `map-manager-only.md` states twice, of the sandboxed merge failure, that *"`HEAD` does not move and nothing is
> lost"* and that *"the merge succeeds outside the sandbox"*. Node 198 falsified the second half: the merge wrote
> one changed file before failing on the read-only mount, left the tree dirty, and the documented retry outside the
> sandbox then refused with *"Your local changes would be overwritten by merge"*. The record's line is what a
> manager reads before deciding this failure is harmless, and it currently promises a clean retry that does not
> happen.

**Blockers, in the worker's words:** *"none. It edits paragraphs node 160 does not freeze, but node 160 also lists
`map-manager-only.md` among its permitted files, so the manager should not run both in one slot pair."*

## Acceptance condition

*Written by node 216's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`. The worker
> may edit those two files and no other; it may not mark this node, resolve it, or write a line in `decisions.md` or
> `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `map-manager-only.md`, under the heading `## Landing an implementation node's work`, each of the two
>    sentences asserting that a sandbox-failed merge loses nothing and succeeds on a retry outside the sandbox is
>    **replaced** by text that also states the partial-write case: that the merge may write some of the changed
>    files before failing, that this leaves the working tree dirty, and that a retry outside the sandbox then
>    refuses with `Your local changes … would be overwritten by merge`.
> 2. The text of each sentence replaced under clause 1 is appended, **unaltered**, to `map-history.md` under the
>    heading mirroring the section it came from, appended rather than replacing anything. This is the `Change the
>    map` procedure for text stating a rule that currently binds.
> 3. New text beside it states the repair, in this order and as one pass: establish that the partially written
>    content is byte-identical to what the branch carries, discard it, and re-run the merge outside the sandbox. It
>    states that establishing byte-identity comes **first**, and that where it does not hold the manager stops
>    rather than discarding.
> 4. The paragraph beginning `**Landing policy**` is byte-identical to its state at `HEAD`. The sentence beginning
>    `**A rebase conflict is resolved by nobody in the moment**` is not edited, struck, moved or deleted by this
>    node.
> 5. No heading named `## Notes` is added to either file.
> 6. Every markdown link in both files resolves to a path that exists, except a link to a path outside this
>    repository, which is out of scope.
> 7. No file outside `.scratch/graph-workflow/` is modified.
> 8. The standing quality bar for this repository holds of the finished tree.

## The manager's note at filing

*Not a change to anything above.*

**The manager is a party to this node's subject and states its own conduct rather than a view.** At node 198's
landing it ran the sandboxed merge, met the partial write, established that the dirt was byte-identical to what the
branch carried, discarded it and re-merged — which is exactly the repair clause 3 demands be written down, arrived
at in the moment rather than read from the record. **Clause 3's insistence that byte-identity is established first
is the part the manager got right by luck rather than by rule**, and it is the clause that matters.

**A second instance arrived after this node was specified, and it points the other way.** Landing [node
229](229-bank-the-landing-sections-accounts-out-of-map-manager-only.md), the same sandboxed merge refused on **both**
changed files, leaving `HEAD` unmoved and **nothing** partially written — the record's line as written. So the
partial write is a case rather than the rule, and clause 1's *"may write some of the changed files"* is the right
shape. **Whoever claims this should not read node 198 as the normal case.**

**Its author's blocker note is scheduling and the manager holds it**: node 160 lists `map-manager-only.md` among its
permitted files, so these two must not run in one slot pair. No blocking edge is written.
