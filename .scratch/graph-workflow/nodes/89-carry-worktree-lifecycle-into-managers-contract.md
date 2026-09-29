# Carry the worktree lifecycle into the manager's contract

Type: implementation
Status: superseded
Superseded by: 371

Blocked by: 68

## Question

*Superseded 2026-09-29: this question no longer needs doing here. See `## Superseded, 2026-09-29` below.*

*Reported by [Write the first version of the manager's skill](76-write-the-manager-skill.md)'s worker, in its
handover, and pasted as it wrote it.*

> [Run an implementation node's work in a worktree](68-implementation-in-a-worktree.md) put the whole worktree
> lifecycle on the manager, and [Carry the worktree lifecycle into the shipped
> files](74-carry-the-worktree-lifecycle.md) landed it in `map.md` because the manager had no file of its own. It
> now has one, and the lifecycle is still not in it: the contract states the two fixed orderings and points at the
> effort's landing policy for the rest. What has to be settled first is whether the lifecycle is a rule of the
> **workflow** or a practice of **one effort** — `map.md` currently says the second in as many words, and flag
> `68.2` refused to assume an ignore rule for a repository the workflow does not own.

**Blockers, in the worker's words:** *"flag `68.2` being settled, or a decision on whether the shipped contract may
require a worktree at all. Not startable before then."*

## Acceptance condition

*Written in part by [Write the first version of the manager's skill](76-write-the-manager-skill.md)'s worker, under
[A worker's handover carries no acceptance condition for the node it mints](35-handover-mints-no-condition.md)'s
shortfall route. Pasted as it wrote it.*

> **What is missing, and why:** the condition turns on whether the workflow ships the worktree mechanism or merely
> permits it, which this worker did not settle and which no resolved node settles — so the central demand cannot be
> phrased without deciding it. That is the question the manager puts to the human before this node is claimed.
>
> **The part that can be written:** the work changes `.claude/skills/expedition/SKILL.md` and no other file under
> `.claude/skills/`; after it, that file states what happens to a worker's tree on each of the three gate outcomes,
> and states it as properties rather than as commands of any one version-control tool, naming no command that a
> repository without that tool could not run; the file's existing headings, listed by `grep -n '^#\{1,6\} '`, are
> all still present and in the same order, with any new heading added rather than substituted; no file under
> `.scratch/` is changed; and the working tree meets the bar.

**The node is not claimed until the condition is complete**, and what is missing goes to the human first.

## The manager's note at filing

*Not a change to anything above.*

**This node was reported in three consecutive handovers and filed only at the manager's handover to a fresh
session.** It was named at node 76's gate as a thing the approval did not settle, but no file existed for it until
after that node had resolved. Nothing in the record caught the delay: `NEW NODES` is reported by the worker and
filed by the manager, and nothing checks that a reported node became a file. **A handover part that only the
manager acts on has no backstop when the manager does not act on it.**

**Two things that have moved under it since it was reported**, and whoever claims it should not assume either way:

- **Flag `68.2` is still open**, and its property is untouched: *no ignore rule may be assumed in a repository the
  workflow does not own.*
- **But this effort now has an ignore rule of its own.** The human directed worktrees inside the repository —
  *"otherwise it is too anoying for the review"* — and a `.gitignore` was added for `.worktrees/` where none
  existed. `map.md` records that as this effort's own practice and **not** a change to what the workflow ships, so
  the question this node turns on is exactly the one that decision deliberately did not answer.
- **[A human edit lands in a worker's tree while the node is claimed](85-human-edits-a-claimed-tree.md)** was minted
  from the same change and bears on what the lifecycle has to say about who may write into a worker's tree.

## Amendment, 2026-09-27 (from node 275)

*Written by [node 275](275-node-250s-finished-work-is-on-a-branch-nothing-will-land.md)'s worker under its `NEW NODES`, which joined it to this node, and filed by the manager. The worker's words, clauses to add to this node's acceptance condition:*

> - `.claude/skills/expedition/SKILL.md` also states what happens to the working state of an implementation node that is superseded while its work is not landed. The graph is edited first, and after that the node's tree, and anything else that holds its unlanded work, is removed, in the same order the file gives for a reject. The file states this as properties rather than as commands of any one version-control tool, and names no command that a repository without that tool could not run.
> - The line in `.claude/skills/expedition/SKILL.md` that reads "reject: edit the graph first, and clean the working state after." still states the reject outcome with the same order: the graph first, the working state after.
> - Scope came from no search: the file named is the place of the work, not an instance of a defect.

*The worker's remark, pasted:* "Node 89's condition is still incomplete and waits on a question (\"ships or merely permits the worktree mechanism\") that the landed plain-git route in `map-manager-only.md` may effectively have answered for this effort. The manager may want to revisit it before the joined clauses can ship."

## Flags

`89.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 275's clean-up clauses were filed on this open, unclaimed node without asking the human first.

*The manager's note, 2026-09-28:* [node 162](162-how-much-of-the-integration-rule-ships.md)'s worker reports this node's question changed. Its words, pasted: **Node 89** (open, implementation, "Carry the worktree lifecycle into the manager's contract") asks whether the worktree lifecycle is a rule of the workflow or a practice of one effort. This answer settles the conflict-handling part of that question as per-effort: the shipped files only require the policy to state it. The rest of node 89's question stays open.

## Superseded, 2026-09-29

*The manager's note:* superseded by [node 371](371-say-what-a-review-entry-records-for-a-manager-started-round.md), under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q3 (`verbatim`: *"ok"*, recorded on node 366). Node 366's worker's reason: merged: its remaining clauses, from node 275, join node 371; node 363 had already landed as `2cf3730`.

*The manager's note, 2026-09-29:* flag 89.1 is the exception: it judges the clauses that moved to [node 371](371-say-what-a-review-entry-records-for-a-manager-started-round.md), so it stays outstanding and settles at node 371's gate, as node 366's worker proposed. Otherwise, this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
