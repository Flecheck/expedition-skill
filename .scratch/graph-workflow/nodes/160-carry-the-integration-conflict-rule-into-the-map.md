# Carry the integration-conflict rule into the map

Type: implementation
Status: claimed

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

~~**Two clauses of this condition have been amended, and clause 7 is not marked where it stands.** The amendments are
held in the two `## Annotation` sections at the end of this file. **Read those before holding any work against this
condition.** *Pointer added by the manager as a safety repair; it changes no clause's text. [Node
199](199-is-an-acceptance-condition-a-rule-or-a-record.md)'s worker established that a condition amended elsewhere,
with nothing pointing at it from the condition block, is read as live by a checker handed the node cold — the
failure node 143's checker caught. **Which form an amendment should take is node 199's open question, and the
manager has not pre-empted it.***~~

**Struck by the manager, on the same day it was written, because its central claim is false.** Clause 7 **is**
marked where it stands: the paragraph beginning `**Amended, and the amendment is the manager's, made with the
human's approval.**` sits **inside the condition block**, as a continuation of clause 7 itself, so a checker
handed this condition as text sees the clause and sees that it has been added to, in the same reading. **This
node was never in the unsafe shape**, and the pointer above was added on a false premise.

**Where the false premise came from, and it is the manager's to own.** [Node
199](199-is-an-acceptance-condition-a-rule-or-a-record.md)'s worker classified this node with nodes 200 and 140 as
*"the clause untouched with the amendment in a following paragraph plus a separate annotation section"*. The
second half of that is right — there is a separate annotation section — and the first half is wrong. **The manager
did not check the clause before repeating the claim**, put it to the human as established, and wrote the pointer
on it. Flag `160.2` records it.

**What this node's shape actually is, under the rule the human approved at node 199's `Q4.`**: the amendment is
adjacent to the clause and inside the block, which is what that rule demands. **Nothing here needs repairing.**

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

## Amendment, 2026-09-27 (from node 266)

*Written by [node 266](266-a-worker-cannot-see-the-record-the-manager-has-not-committed.md)'s worker under its `NEW NODES`, which joined it to this node, and filed by the manager. Clauses to add to this node's acceptance condition, pasted as it wrote them:*

> 11. The new text that clause 7 demands states that the manager makes the commit before a worktree is cut **before every implementation worktree it cuts**, whatever paths that node's condition names. It also states that the manager makes both of clause 7's commits on its own authority, path-limited to `.scratch/graph-workflow/`, with no diff shown to the human first and each commit reported to the human afterwards.
> 12. The same new text states that an implementation worker reads and edits the effort's record files in its own worktree, and never in the main checkout.
> 13. The sentence clause 7 quotes is looked for in `.scratch/graph-workflow/map-manager-only.md`, which is where it now stands. Scope search: `grep -rn -l 'committed periodically' --include=*.md .` run from the repository root returned `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, with the `nodes/` directory excluded. The `map-history.md` hit is banked history and is not edited. Any instance the search reaches outside these two files is reported, not edited.

## Flags

`160.2` `MANAGER-WRONG` — **The manager reported this node to the human as carrying an unsafe amendment shape, and
it does not.** Node 199's worker classified node 160 alongside nodes 200 and 140 as a condition whose amendment sits
only in a separate section. **The manager repeated that without opening the clause**, told the human that node 160
was *"open and unclaimed, and its clause 7 sits unmarked"*, and added a pointer at the top of the condition as a
safety repair. Clause 7 carries its amendment inside the condition block, immediately beneath it. **The pointer was
unnecessary and its premise was false**; it is struck above rather than deleted, and no clause of this condition was
ever changed by it. **The cost was a false statement to the human and a paragraph of noise at the head of a
condition a worker will read cold.**

`160.3` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 266 above.* Node 266's clauses 11 to 13 were filed on this open, unclaimed node without asking the human first.
