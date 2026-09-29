# The rules file's account of `.gitignore` names two patterns where there are three

Type: implementation
Status: superseded
Superseded by: 190

Blocked by: [node 269](269-ignore-the-new-worktree-path.md)

## Question

*Superseded 2026-09-29: this question no longer needs doing here. See `## Superseded, 2026-09-29` below.*

*Surfaced by [node 269](269-ignore-the-new-worktree-path.md)'s worker, and pasted as it wrote it.*

> `map-implementation-rules.md`'s bar section states that this repo's one ignore file *"ignores `.worktrees/` and
> `.claude/worktrees/`"*. Node 269 adds a third pattern, `.scratch/graph-workflow/worktrees/`, so that enumeration
> becomes incomplete the moment node 269 lands. The same sentence was already corrected once, at node 114's check,
> for claiming no ignore file existed after one had been added — so this is the second time the record of
> `.gitignore` has drifted behind `.gitignore`. Repair the sentence, and while there consider whether an enumeration
> of a file's contents belongs in the record at all or whether the citation alone would do.

**Blockers, in the worker's words:** *"node 269 must land first, or the repair states something not yet true.
Nothing else — node 268 edits `map.md`, `map-manager-only.md` and `map-history.md` and does not touch
`map-implementation-rules.md`, which I confirmed by reading node 268's condition."*

## Acceptance condition

*Written by node 269's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md` and `.scratch/graph-workflow/map-history.md`,
> and no other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md`
> or `flags.md`. Done means every one of the following is true of the finished tree.
>
> 1. `map-implementation-rules.md` no longer contains any statement that the repository's one ignore file ignores
>    exactly `.worktrees/` and `.claude/worktrees/`, or any other enumeration of that file's patterns that omits
>    `.scratch/graph-workflow/worktrees/`.
> 2. Whatever replaces it is true of `.gitignore` at the repository root as that file then stands, which the worker
>    verifies by opening `.gitignore` and reports in its handover by quoting the patterns it found.
> 3. The surrounding statement still says that this repo has no build, no tests, no formatter and no CI, that
>    `.gitignore` invokes nothing, and that the bar's command half being empty is a complete bar rather than a
>    deficient one.
> 4. The displaced wording states a rule that currently binds, so it is **replaced** rather than struck in place,
>    and its existing text is appended **verbatim** to `map-history.md` under a heading mirroring the section it came
>    from, with any struck-through text staying struck through. `map-history.md` gains text and loses none.
> 5. Any new statement cites the node that shaped it by markdown link, cites no file by line number, and recounts no
>    attempt count, cost, or who was wrong.
> 6. `.gitignore` itself is not edited, and no file outside the two named above is modified.
> 7. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The `Blocked by` edge is real rather than a sequencing note.** Clause 2 requires the replacement be true of
`.gitignore` *as it then stands*, and the third pattern is uncommitted in node 269's worktree. A worker claiming
this before node 269 lands would either write something false or be unable to satisfy clause 2 at all.

**Its author's aside is the more interesting half and the condition deliberately leaves it open**: *"consider
whether an enumeration of a file's contents belongs in the record at all or whether the citation alone would do."*
Clause 1 forbids the stale enumeration and clause 2 constrains any replacement, but **nothing forces a replacement
enumeration to exist** — dropping it for the citation alone satisfies both. That is the claiming worker's judgement
and the manager has not made it.

**This is the second drift of one sentence**, the first corrected at node 114's check for claiming no ignore file
existed after one had been added. **[Node 268](268-carry-the-plain-git-worktree-route-into-the-map.md) also holds
`map-history.md`**, so two workers must not hold that file at once; the manager holds that sequencing.

## Superseded, 2026-09-29

*The manager's note:* superseded by [node 190](190-the-rules-file-states-one-list-twice.md), under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q3 (`verbatim`: *"ok"*, recorded on node 366). Node 366's worker's reason: merged: its clauses join node 190's condition, both editing the bar paragraph of `map-implementation-rules.md`.
