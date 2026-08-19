# An acceptance condition is self-contained text

Type: implementation
Status: open

## Question

[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s
`### Acceptance condition` section says **who** writes one and **when**, and never says it must be readable
by the party that will check it.

Add that a condition is written as text that stands on its own and **never points into the record** — because
the checker reads it cold and may not follow the pointer. A condition that points leaves the manager
authoring the referent into the checker's payload, which is the manager writing the standard the work is
judged against.

### Found three times, owned by nobody

1. [Write the worker contract skills](22-worker-contract-skills.md) — *"a path in one is a hole in the
   blindfold"*.
2. Flag `26.4` — *"nothing says who dereferences it when it does"*. Two of [Carry the recorded deltas into
   the shipped skill files](26-carry-deltas-into-shipped-files.md)'s conditions pointed into the record; the
   manager dereferenced one into the checker's spawn and **stripped a bookkeeping preamble that asserted the
   work had already been done**, which would otherwise have told a blind checker the answer.
3. [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md), which is where
   the defect was finally placed. That node ruled the dereferencing **not an override at all** — the manager
   was complying with the checker contract's own clause, *"as text… not somewhere to go and read them"* —
   and located the fault one level up, here. Recorded as flag `28.4`, decided by the worker alone.

The same node's `## Answer` states the general form: the file states the rules, the spawn states the
parameters. An acceptance condition is a parameter, so it has to arrive whole.

### The acceptance condition is owed

Written by whoever spawns this, and it may not be claimed without one. There is an irony to keep in view while
writing it — **this node's own condition must satisfy the rule this node ships** — and a warning from [What
the checker contract owes to having been run](31-checker-contract-owes.md): node 26's condition was the first
written by a manager rather than by a spawning node or its worker, and it had to be amended twice, once for
naming a glossary entry that does not exist.
