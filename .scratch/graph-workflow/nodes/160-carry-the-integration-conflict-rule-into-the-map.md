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
> 8. No heading named `## Notes` is added to any file this node edits.
> 9. Every markdown link in the files this node edits resolves to a path that exists, except any link to a path
>    outside this repository, which is out of scope.
> 10. No file outside `.scratch/graph-workflow/` is modified.
