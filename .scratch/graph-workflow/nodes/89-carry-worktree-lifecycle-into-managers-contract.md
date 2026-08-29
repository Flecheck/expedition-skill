# Carry the worktree lifecycle into the manager's contract

Type: implementation
Status: open

Blocked by: 68

## Question

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
