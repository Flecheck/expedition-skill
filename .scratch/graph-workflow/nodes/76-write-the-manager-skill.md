# Write the first version of the manager's skill

Type: implementation
Status: open

Blocked by: 75

## Question

Write the manager's contract — the file that says what the manager does — as its **first version**, from the
enumerated duty list [Gather the manager's accumulated duties into one enumerated
list](75-gather-the-managers-duties.md) produces.

### The human's instruction, `verbatim`

> *"I think the priority should be writing the first version of the manager skill as now you don't have any way to
> know what to follow as the information is split everywhere."*

**"First version" is the scope**, and it is doing work: this file does not have to settle what is still open. Where
a duty is unsettled it is written as unsettled, and where two nodes conflict the file says so — node 75's clauses 4
and 5 exist to hand this node those cases already separated.

## Acceptance condition

**To be written by node 75's worker**, as clause 6 of that node's condition requires — not by the manager. Under
[A worker's handover carries no acceptance condition for the node it mints](35-handover-mints-no-condition.md), a
condition written by the party that did the gathering is the one that passes self-containment; the manager writing
it here would mean writing an enumeration it has not yet gathered.

## What this node already knows, and does not have to rediscover

*The manager's own note, filed at creation.*

- **Where it lands is not settled.** The six worker contracts sit at `.claude/skills/expedition-<type>/SKILL.md`,
  and the conventions document at `.claude/skills/expedition/graph-conventions.md`. Whether the manager's file is a
  seventh sibling, or lives inside `expedition/`, is open — and flag `21.2` already records that the install
  location was pinned inside live fog once before.
- **Two adjacent files are already split out and are not this node's**: [Write the cascade pass's worker
  contract](44-cascade-worker-contract.md) and [What the manager reports to the human](46-what-the-manager-reports.md).
- **[Whether the workflow ships explicit subagent definitions](69-explicit-subagent-definitions.md) settled that the
  manager does not become a declared subagent type**, and that a hard rule binds by being read rather than by being
  enforced.
- **Ground rule 2 applies to this file too**: it must stand alone as a file rather than depending on any skill being
  invocable.
- **[Run an implementation node's work in a worktree](68-implementation-in-a-worktree.md) put the whole worktree
  lifecycle on the manager**, and observed that the manager has no skill file — so until it does, that lifecycle
  lands in `map.md`. [Carry the worktree lifecycle into the shipped files](74-carry-the-worktree-lifecycle.md) does
  that; **this node is where it eventually belongs.**
