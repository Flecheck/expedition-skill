# A failed `git merge --ff-only` can leave the tree partially updated, and the record says it cannot

Type: implementation
Status: claimed

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

## Amendment, 2026-09-27 (from node 160)

*Written by [node 160](160-carry-the-integration-conflict-rule-into-the-map.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it.*

Node 234, clause 4, second sentence. Current text: "The sentence beginning `**A rebase conflict is resolved by nobody in the moment**` is not edited, struck, moved or deleted by this node." That sentence no longer exists, so the clause is vacuously true and no longer protects anything. Replacement: "The text in that paragraph beginning `A rebase conflict is resolved, and the rebase is not aborted.` and ending `the manager runs `git rebase --abort` and the node takes a correction round.` is not edited, struck, moved or deleted by this node." What fixes these words: this node's work, once landed in the tree.
Clause 4's first sentence, "The paragraph beginning `**Landing policy**` is byte-identical to its state at `HEAD`", still holds against whatever HEAD is when node 234 runs.

## Interview

#### Raise 1, relayed 2026-09-28

*Pasted as the worker handed it back. The worker is stopped until the human answers.*

```
NODE:          234, "A failed `git merge --ff-only` can leave the tree partially updated, and the record says it cannot"
ABOUT:         Replace the record's claim that a merge failed in the sandbox loses nothing and retries cleanly, bank the old text, and write the repair down. I stopped at the check you asked for, before any edit. Nothing in the worktree is touched.
SO FAR:        I read the contract, the node file (with its node-160 amendment), map.md, map-implementation-rules.md, and the landing, merge and sandbox lines in decisions.md. Then I searched the worktree (`7093c67`) for the passages the condition names.
               - Clause 1 says "each of the **two** sentences" claiming that a sandbox-failed merge loses nothing and succeeds on a retry outside the sandbox. Only **one** such sentence is left in `.scratch/graph-workflow/map-manager-only.md` under `## Landing an implementation node's work`, in the "One sandbox restriction bites this lifecycle" bullet, sub-bullet "What it hits": "`HEAD` does not move and nothing is lost in either case; both succeed outside the sandbox." It covers two operations: the merge, and `git reset --hard` inside an entered worktree. That reset is a step of no route any more (node 265).
               - The two sentences node 216's worker quoted ("`HEAD` does not move and nothing is lost; the merge succeeds outside the sandbox" and "the merge succeeds on a retry outside the sandbox") are already gone. Node 229 (`38709b7`, 2026-09-13 09:49) moved them to `map-history.md`, word for word, under `## Superseded from map-manager-only.md — the landing section's accounts`, as Edit 13 and Edit 14. That was 14 minutes before this node was minted (`5d8507c`, 10:03). At minting, `git show 5d8507c:` already shows only the one combined sentence. So the condition was out of date from the day it was written, which is the kind of case you told me to raise.
               - Everything else checks out. Clause 4's `**Landing policy**` paragraph is there. The node-160 replacement span ("A rebase conflict is resolved, and the rebase is not aborted." … "the manager runs `git rebase --abort` and the node takes a correction round.") is there too. Clauses 5 to 8 raise no problem. The bar for this repo is entirely non-command (no build, tests, formatter or CI), and I confirmed there is no manifest to contradict that record.
               Settled on my own authority: nothing.
ASK:           Clause 1's "two sentences" no longer exist as two. Do I go ahead by treating clause 1 as covering the one surviving combined sentence, with the other two counted as already banked by node 229?
RECOMMENDED:   Go ahead on that reading. This is the concrete shape, which you can approve as worded:
               (a) Replace the surviving sentence with the following. "`HEAD` does not move in either case. The reset loses nothing and succeeds outside the sandbox. The merge may instead write some of the changed files before it fails. That leaves the main tree dirty, and a retry outside the sandbox then refuses with `Your local changes to the following files would be overwritten by merge`." The reset keeps its old claim because nothing has falsified it, and the partial write has only been seen on the merge. The wording keeps "may" because node 229's own landing hit the clean case.
               (b) Right after it, add a repair line for clause 3. "The repair is one pass, in this order: first establish that every dirty file is byte-identical to the branch's version (`git diff --quiet <branch> -- <path>`); then discard the dirt (`git checkout -- <path>`); then re-run the merge outside the sandbox. Where any dirty file differs from the branch, stop and discard nothing."
               (c) Append the replaced sentence, word for word, to `map-history.md` under a new heading "Superseded from `map-manager-only.md` at node 234", with a "### From *Landing an implementation node's work*" subheading. That follows the node-160 and node-336 pattern.
               (d) Clause 2 is then met for the other two sentences, because Edit 13 and Edit 14 already hold them word for word. I would not append them a second time.
               This rests on the node's purpose, which is that the record stops promising a clean retry. That purpose is fully served by fixing the one place that still makes the promise. The claims node 216 quoted now live only in the history file, which holds superseded text.
ALTERNATIVES:  - Rewrite clause 1 (and clause 2) so they name the one surviving sentence, then continue. This is cleaner for the checker, which reads only the condition and will count "two sentences". But the condition would change after the node was claimed.
               - Also correct the reset's half of the sentence, or drop it since the reset belongs to no route. This goes beyond the node's scope and nothing measured supports it.
               - Stop the node as already partly done by node 229 and file a smaller replacement. More bookkeeping for the same edit.

Manager-facing notes (not part of the raise):
- Touched paths: none. The worktree is exactly as it was cut.
- I have not appended anything to `map-history.md`. If I continue, I will append only the one new section described in (c).
- Whichever way you answer, the checker's copy of the condition needs to show how "two sentences" was settled, or the checker will FAIL clause 1 by counting.

RETROSPECTIVE
1. What I had to hunt for: whether the second sentence had been moved to history or deleted outright. It took `git log -S` together with reading Edit 13 and Edit 14 in map-history.md, then an ancestry check to learn it predated this node's minting.
2. What arrived that this node did not need: the landing-merge-sandbox fact (merges run with the sandbox off), and node 186's parallel run on the rules file. Both only matter once the edit happens.
3. What would have made this easier: the node file recording that node 229 landed shortly before minting and banked Edit 13 and Edit 14. Better still, a check at minting that the condition's premises hold against the tree.
4. What was stale, wrong or contradictory: clause 1's "two sentences" and the Question's two quotes were already out of date when the node was minted. The node-160 amendment is accurate. The manager's filing note ("the record's line as written" for node 229's clean case) points at the single combined sentence, without saying that it is now the only one.
```

## Flags

`234.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 160 above.* Node 160's replacement for clause 4's second sentence was filed on this open, unclaimed node without asking the human first.
