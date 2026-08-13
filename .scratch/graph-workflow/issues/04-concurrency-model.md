# Concurrency model

Type: grilling
Status: resolved

## Question

How many issue subagents are in flight at once, and what constrains that number?

## Answer

**Parallel, sized to saturate the human — with an exclusive lock on code modification.**

- Roughly **two HITL (grilling) subagents in flight at once**, so the human always has a question waiting and never idles.
- **Exactly one code-modifying subagent at a time.** This is what makes worktrees unnecessary in v1.
- AFK work (e.g. research) may fan out freely.

The governing principle, in the user's framing: **parallelism exists to saturate the human, not the machine.** The human is the scarce resource; concurrency is tuned to keep their question queue full, not to maximise machine throughput.

Later (not v1): subagents run in their own worktrees and, on finishing, land work on the manager's branch with `git merge --ff-only`.

Note on why that ordering is coherent: with a single writer, the manager's branch is always an ancestor of the subagent's, so the fast-forward cannot fail. `--ff-only` only becomes a real merge problem once the single-writer restriction is lifted — so the lock and the ff-only policy are two views of the same invariant.

Consequence to carry downstream: with two HITL subagents live, the manager is **multiplexing** a question channel. Attribution of questions to issues, and of answers back to the right subagent, is now a real problem — see [Relay protocol](08-relay-protocol.md).
