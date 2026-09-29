# Twenty legacy flags have no ids, and the check reports a false failure every run

Type: implementation
Status: out-of-scope

## Question

Flag ids were added partway through this effort. **The twenty flags raised before that carry none**, which
[flags.md](../flags.md) states in as many words: *"The twenty lines below predate it and carry none."*

**That is now producing a standing false failure in the mechanical check.** Check 6 joins each `NN.k` appearing in
a node's `## Flags` section against the index, and reports one with no index line. It cannot distinguish **raising**
a flag from **citing** one, so a citation of a flag that has no id resolves to nothing and is reported as missing.

**The live instance.** [Write the first version of the manager's skill](76-write-the-manager-skill.md)'s flag `76.1`
cites `21.2` — meaning the second flag on [Write the graph conventions document](21-conventions-document.md), which
is real and is about an install location pinned inside live fog. That flag has no id, so `21.2` names nothing. Every
run of the check has reported `FAIL 6: node 76 flag 21.2 has no line in flags.md` since, and will go on doing so.

**Why this is worth a node rather than a shrug.** The check is the thing that catches real defects — it caught a
resolved node with no `## Answer` twice, and it caught flag entries written onto a node without their index lines,
which is the *"never as a tidy-up"* rule. **A check that always reports one failure teaches its reader to skim the
failures**, and the next real one arrives in the same list.

### Three routes, and they are not equivalent

- **Give the twenty legacy flags ids.** Fixes every future citation and makes the whole index uniform. It edits
  twenty lines of an **append-only** file and the ids would be allocated now rather than in write order, which is
  what `flags.md` says an id is: *"allocated in write order and never reused."* Whether backfilling satisfies that
  is the question.
- **Teach the check to tell a citation from a raise.** No file changes, and it needs a rule the check can apply —
  a raise is a flag whose entry begins the line, a citation appears inside prose. That is a real distinction and
  the current entries already follow it, but nothing states it.
- **Forbid citing a flag that has no id**, and cite the node and the flag's subject instead. Cheapest, and it
  leaves twenty flags permanently uncitable by id.

### What must not be lost

`flags.md` is **append-only** and a settled flag is checked, never removed. Any route that rewrites the twenty
lines has to say why that is a permitted edit rather than an exception, and [Graph file
format](13-graph-file-format.md) is where that rule lives.

## Acceptance condition

*Written in part by the manager, for a node it minted itself. **What is missing, and why:** the condition turns on
which of the three routes is taken, and that is a choice between a file edit, a tool change and a citation rule
which no resolved node settles. Choosing it here would be the manager deciding inside a condition. **That question
goes to the human before this node is claimed.***

**The part that can be written.** After this work, the mechanical check run over the graph reports **zero** failures
on a tree that has no other defect, and `FAIL 6` no longer fires on a flag that is cited rather than raised. No
flag's text and no flag's checkbox state changes. Nothing under `.claude/skills/` changes. The rule that
[flags.md](../flags.md) is append-only and that a settled flag is checked rather than removed still holds after the
work, stated wherever it is stated now. The working tree meets the bar.

## Where it came from

The manager, at [Write the first version of the manager's skill](76-write-the-manager-skill.md)'s close, having
watched the same false failure print on every check run for a day and having told the human twice that it was noise
to ignore. **Telling someone to ignore a check's output twice is the reason this is a node.**

## Ruled out of scope, 2026-09-29

*The manager's note:* under the human's answer to [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q2 (`verbatim`: *"ok"*). Its line in `map-manager-only.md`'s `## Out of scope` is node 366's worker's text.
