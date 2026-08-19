# The clause that says no resolved node changes cannot be self-contained

Type: implementation
Status: open

## Question

Four of the nine acceptance-condition failures found by [An acceptance condition is self-contained
text](33-condition-is-self-contained.md)'s audit are **one boilerplate sentence**:

- *"No decision on any resolved node changes"* — node 33's condition 8, [What the checker contract owes to
  having been run](31-checker-contract-owes.md)'s condition 4, [Carry the recorded deltas into the shipped
  skill files](26-carry-deltas-into-shipped-files.md)'s condition 4.
- *"Every rule in every contract traces to a resolved node"* — [Write the worker contract
  skills](22-worker-contract-skills.md)'s condition 3, the same demand in the other direction.

**It cannot be repaired by copying, which is the remedy node 33 shipped for every other pointing clause.**
Its content is the whole record: to state it self-containedly a condition would have to carry every decision
the effort has ever made.

There is hard evidence about what it costs. Node 22's condition 3 was handed to **four independent blind
checkers and each declared it not establishable** — before anyone could say why. Node 33's rule now names
why: the demand's content sits outside the text, and no copy can bring the record inside it.

### It is already owed somewhere else, by a party that can answer it

Every worker contract carries this handover part:

```
INVALIDATIONS: <which resolved node your work contradicts, and how>
```

That is the same duty, addressed to the party that **has read the record** and can therefore discharge it.
The condition clause is a duplicate pointed at the party that structurally cannot.

### The fork

- **The clause leaves acceptance conditions**, resting on `INVALIDATIONS` — the reading node 33's worker
  recommends, and the one consistent with the rule it shipped.
- **The clause stays**, and `graph-conventions.md` says which party checks it — which means naming something
  other than the blind checker, and there is no third checking party today.

A grilling node first is defensible: four resolved nodes wrote this clause deliberately, so removing it from
the standard form is not obviously a repair. Whoever spawns this decides which, and says so.

### Landing

`graph-conventions.md`'s `### `## Acceptance condition`` section, the same section node 33 just changed. A
later commit against that file is lawful — the landing policy forbids a second commit against one **node**,
not against one **file**.

Reported by [An acceptance condition is self-contained text](33-condition-is-self-contained.md)'s worker.

### The acceptance condition is owed

Written by whoever spawns this, and it may not be claimed without one.
