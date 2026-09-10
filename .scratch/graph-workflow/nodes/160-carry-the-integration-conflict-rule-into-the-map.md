# Carry the integration-conflict rule into the map

Type: implementation
Status: open

Blocked by: 144

## Question

*Surfaced by [Two writers edit the map at once](115-two-writers-edit-the-map-at-once.md)'s worker, and pasted as it
wrote it.*

> Carry node 115's answer into the map: a rebase conflict is resolved rather than aborted, the resolver depends on
> what conflicted, the slot count is a dial with a stated price, and the manager's pick prefers candidates whose
> conditions name disjoint paths.

**Blockers, in the worker's words:** *"node 144, whose condition clause 5 demands that no other paragraph of
`map-implementation-rules.md` changes — a direct contradiction rather than a merge conflict. Node 152 edits the same
section and will merely conflict, which this node's own answer says is acceptable."*

## Acceptance condition

*Written by node 115's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/`. The worker may edit `map-implementation-rules.md`, `map-manager-only.md`
> and `map-history.md`, and no other file; it may not mark this node, resolve it, or write a line in `decisions.md`
> or `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `map-implementation-rules.md`, inside the paragraph beginning `**Landing policy**`, the sentence `**A rebase
>    conflict is resolved by nobody in the moment**: the manager runs `git rebase --abort` and the node takes a
>    correction round with the worker respawned.` is struck through in place with `~~`, and its text is otherwise
>    unchanged. It is not deleted and not moved.
> 2. That struck sentence's full text, unaltered, also appears in `map-history.md` under the heading mirroring the
>    section it came from, appended rather than replacing anything.
> 3. New text sits immediately after the struck sentence, stating all four of these and nothing that contradicts
>    them: that a rebase conflict is resolved rather than aborted; that a conflict in text held under the
>    never-delete rule is resolved by the manager by keeping both sides, which is assembly rather than authoring, and
>    is reported without the work returning to the checker or the gate; that any other conflict, product code
>    included, is resolved by the worker whose branch is being rebased, which the manager resumes to edit the
>    conflicted files in place while the manager itself runs every git command, and that this resolution returns to
>    the checker and to the gate; and that where the two sides contradict each other so that keeping both would make
>    the file assert two incompatible things, the manager runs `git rebase --abort` and the node takes a correction
>    round.
> 4. In the paragraph beginning `**How many implementation workers run at once`, new text states that raising the
>    count buys parallel implementation at the price of integration conflicts, that the human sets it, and that the
>    manager neither raises it on its own judgement nor treats the effort's current value as a ceiling. The existing
>    text of that paragraph is unchanged.
> 5. That new text quotes, marked `verbatim`, the words `but the framework should allow user to tell the manager to
>    increase parallelization, at the expanse of odds of having to resolve merge conflicts`.
> 6. `map-manager-only.md` states that when more than one code slot is free the manager prefers candidates whose
>    acceptance conditions name disjoint sets of paths, and gives the reason in one sentence: a condition already
>    lists its paths, so conflict likelihood is readable before either node starts.
> 7. The sentence in `map-implementation-rules.md` reading `The graph's own files are *not* committed per node; they
>    are committed periodically by the human, which is safe only because node files are append-only.` is struck
>    through in place with `~~`, its text otherwise unchanged, with its full text appended to `map-history.md` as in
>    clause 2, and new text beside it stating that the manager commits the graph's own files itself, before a
>    worktree is cut, so that the tree a worker is given equals the tree the manager is standing on.
>
>    **Amended, and the amendment is the manager's, made with the human's approval.** *The clause above stands
>    unchanged and this is added to it, both moments being wanted.* The new text also states that when the human
>    approves a node at its gate, the manager commits its own outstanding record edits, path-limited to the record
>    directory, as the **first step of landing and before the rebase** — because `git merge --ff-only` is refused
>    where a dirty file is one the branch also changes, and because a record commit made after the rebase leaves the
>    branch unable to fast-forward. Committing at the cut keeps the worker's base current; committing before the
>    rebase is what unblocks the merge, and neither substitutes for the other.
> 8. No heading named `## Notes` is added to any file this node edits.
> 9. Every markdown link in the files this node edits resolves to a path that exists, except any link to a path
>    outside this repository, which is out of scope.
> 10. No file outside `.scratch/graph-workflow/` is modified.

## Annotation: why clause 7 was amended, and by whom

*Filed by the manager.*

**The defect and its wording are [node 176](176-the-managers-record-edits-collide-with-a-landing.md)'s worker's, not
the manager's.** It established, by running git in a scratch repository rather than reasoning about it, that
committing the record *before a worktree is cut* does not prevent the collision the clause exists to prevent: the cut
happens when a node is claimed, the manager writes the record continuously for that node's whole life, and node 144's
colliding edits were written minutes before its landing. It said in as many words that *"amending a live condition is
the manager's act with the human, not a worker's"*, and supplied the text the amendment needed to demand.

**The manager put it to the human rather than amending on its own authority**, under the rule that rewriting an
acceptance condition is never the manager's. Their word, `verbatim`:

> ok

**What was done and what was not.** The original clause is left standing and unchanged; the amendment is added
beneath it, because the finding is that the clause is *insufficient* rather than wrong. This node is open and
unclaimed, so no worker was mid-flight when it changed.

## Annotation: this node's clause 7 inherited an error from a resolved node

*Filed by the manager from node 176's handover, and pasted as that worker wrote it.*

> **Node 115 (resolved) — its section 5 states a remedy that does not fix the failure it names.** Its words: *"an
> uncommitted graph edit blocks the landing step even when the rebase is clean. It is why the manager's graph state
> must be committed before a worktree is cut."* **The *"It is why"* does not follow.** The block occurs at the merge,
> at the end of the node; committing at the cut, at the start, leaves every edit the manager makes in between — which
> is several commits' worth, and was the whole of node 144's collision.

***The manager's note.*** **Node 115 is resolved and its section 5 is uncorrected there.** The manager has recorded
the finding here, on the node that inherited it, rather than editing a resolved node's answer. Whether an annotation
onto an already-resolved node has a home in the graph's format at all is one of the manager contract's own declared
unsettled questions.

## Annotation: node 188 has landed, and two of this condition's file names are now wrong

*Filed by the manager from [node 188](188-move-the-landing-section-out-of-the-workers-file.md)'s worker, in its own
words. Nothing above is changed, and **the condition is not amended.***

> **Node 160** (*Carry the integration-conflict rule into the map*) — **satisfiable after a smaller repair.** Its
> clause 1 names *"In `map-implementation-rules.md`, inside the paragraph beginning `**Landing policy**`"* and its
> clause 7 names *"The sentence in `map-implementation-rules.md` reading `The graph's own files are *not* committed
> per node…`"*. Both sentences are now in `map-manager-only.md` — which that node's file list already permits, its
> clause 6 making a demand of it. Only the two file names in clauses 1 and 7 are wrong.

**Why the manager has not repaired it even though it looks like bookkeeping.** The file this condition would now
name is already in its own permitted list, so the fix is two words — but rewriting a condition is not the manager's,
and *"only the two file names are wrong"* is itself a judgement of the worker's that whoever claims this node should
confirm against the tree rather than inherit.
