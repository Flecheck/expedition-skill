# Write the worker contract skills

Type: implementation
Status: open
Blocked by: 12, 20, 23

## Question

Write the six worker contracts as skills: one per node type, plus the checker.

Graduated from the map's fog by [Subagent context contract](12-subagent-context-contract.md), which
fixed what a contract contains — the spawn's shape, the pointer set and its per-type delta, the
handover's five parts and its three variants, and the scribe rule the manager holds up on its side.
This node writes those decisions down as instructions a worker actually receives.

Each contract is invoked by name from the spawn, rather than copied into it, so each must be
independently invocable — a supporting file under another skill cannot be. The glossary travels inside
these files, because the vocabulary is the workflow's and has to reach a machine that has never seen
this repo.

~~Blocked on [Human review of landed code](20-human-code-review.md) for one row of one contract: the
implementation worker's handover carries the gate payload, and that node owns its shape.~~

## Annotation: unblocked, and two of the six contracts changed

Added by [Human review of landed code](20-human-code-review.md). ~~**Both blockers are now resolved, so
this node is on the frontier** — the map's second implementation node, and the first one written after
the gate it will pass through was specified.~~ **A third blocker arrived within the hour:** [When an AFK
worker cannot proceed](23-worker-cannot-proceed.md), from the human's steering. Two of the six contracts
cannot be written until it resolves, because condition 2 requires every return variant a worker may use
and condition 3 forbids a rule no node decided — and that node may give both the implementer and the
checker a variant they do not have today.

The acceptance condition is **not** touched: it was written by [Subagent context
contract](12-subagent-context-contract.md) and only the spawning node writes one. What that node fixed
generically, this one now fixes concretely:

- **The implementation contract's gate payload has a shape.** Condition 2's *"shape of every return
  variant"* now has a referent for this row: a chronology of the checker assembled from others' text, the
  worker's flags, the node, the paths actually touched, the proposed commit message with its trailer, and
  a pointer to the tree — never a rendered diff. Plus the correction-round rule the worker has to obey:
  it reports whether its correction touched something a condition names, because that is what decides
  whether the acceptance condition is re-checked.
- **The checker contract says `FAIL`, not `REJECT`.** The word `reject` now belongs to the human at the
  gate. Condition 5 binds on the glossary, which now refuses `reject` for the agent by name — so a
  contract written with the old token fails that condition rather than merely reading oddly.
- **The gate is raised even when the checker will not pass**, so the implementation contract cannot treat
  a passing check as a precondition of finishing.

## Annotation: the third blocker resolved, and both affected contracts have their answers

Added by [When an AFK worker cannot proceed](23-worker-cannot-proceed.md). **All three blockers are resolved
and this node is on the frontier** — the map's second implementation node. The `Blocked by:` line keeps all
three, because unblockedness is computed rather than recorded.

- **The implementation contract gains a `raise` as a return variant** (condition 2), with the threshold
  stated as three triggers a worker can test on itself, and the rule that a raise **blocks while keeping the
  code slot** rather than parking.
- **The checker contract gains a third outcome, not a third value.** `PASS`, `FAIL`, or a raise that issues
  no verdict at all. Its characteristic case is an acceptance condition that is incoherent or unmeasurable,
  since it is the only party that reads one cold.
- **Both must say what happens on a stop.** The worker writes nothing and is dropped; the manager saves the
  salvage and cleans the tree. Condition 8 is untouched — a worker still writes no graph file, and the
  salvage is the manager's to write.
- **One rule to trace for condition 3**: `AFK` now means *does not need the human in order to proceed*.
  That is [Node type taxonomy](07-node-type-taxonomy.md)'s clause as corrected there, not a new rule
  invented in a contract.

## Acceptance condition

1. Six contracts exist and each is independently invocable by name from a spawn prompt: one per node
   type — grilling, research, prototype, implementation, precondition — plus the checker.
2. Each contract states, for its own type: the worker's identity and that it has no channel to the
   human; its hard rules; the shape of every return variant it may use; and the method skills it
   invokes, named as *invoke if present*.
3. Every rule in every contract traces to a resolved node. No contract introduces a rule that no node
   decided.
4. Instructions only — no reasoning, no rejected alternatives, no history. The same bar [Write the
   graph conventions document](21-conventions-document.md) was held to.
5. The vocabulary is the glossary's, and no `_Avoid_` word appears in any of the six.
6. The grilling contract is diffable against the relay prototype's [run-1
   contract](../prototypes/08-relay-protocol/run-1.md): everything that contract carried is either
   present or deliberately absent, and `CONTEXT-PROOF` is absent.
7. The checker's contract names neither the node file nor any part of it except the acceptance
   condition, which reaches the checker as extracted text.
8. A worker following any of the six writes no graph file.
9. Each contract's text stands alone as a file: everything binding on the worker is *in* the file, so a
   runner with no skill-invocation mechanism gets the same instructions by reading it. The skill is the
   wrapper, never the content. Added after the contracts were specified, because the human intends to
   run workers on other models and harnesses later and this is the whole cost of keeping that open.
