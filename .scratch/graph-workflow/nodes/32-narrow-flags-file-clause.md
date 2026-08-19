# Narrow the flags.md clause in the worker contracts

Type: implementation
Status: open

## Question

*"`flags.md` is not yours. Leave it unread"* stands unchanged in **five** shipped contracts —
[`expedition-grilling`](../../../.claude/skills/expedition-grilling/SKILL.md) line 41,
[`expedition-implementation`](../../../.claude/skills/expedition-implementation/SKILL.md) line 54,
[`expedition-research`](../../../.claude/skills/expedition-research/SKILL.md) line 37,
[`expedition-prototype`](../../../.claude/skills/expedition-prototype/SKILL.md) line 43, and
[`expedition-precondition`](../../../.claude/skills/expedition-precondition/SKILL.md) line 45.

The clause exists to keep a worker's read small and to stop it second-guessing decisions outside its own
node. A node **about** that file is a case it did not consider. Give it the carve-out it lacks.

One thing to decide while doing so, and the answer must state which it chose: is the carve-out **a
conditional pointer the spawn names** — which keeps a worker's behaviour readable from its own file and keeps
the authority explicit — or **a condition the worker judges for itself**? Under [Node type
taxonomy](07-node-type-taxonomy.md) a small ambiguity is decided and flagged while a genuine fork becomes a
grilling node; if the implementer judges this one a genuine fork, that is the route.

### Why it is worth a node

**The clause has cost twice, and only one of the two was a suspension.**

- [Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md)'s spawn
  **suspended** it, because that node's whole subject was the file. Well-grounded, plainly stated, and the
  node could not have been worked otherwise.
- [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md)'s worker
  **complied** with it while writing that same file's own conventions, and so had to guess a punctuation
  detail blind — flag `26.2`, whose manager note records that the guess happened to match what was already
  in the file. **Compliance was as expensive as the departure**, and only luck kept it from being worse.

Created by [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md), which
is also the node that says why this repair is a node at all rather than something the manager does in
passing: node 27's departure produced no node, and a session later the clause was still unchanged in all five
files while node 28 was still carrying the narrowing as an open question. **This node is the repair that got
lost**, minted late and on the record.

### The acceptance condition is owed

Written by whoever spawns this, per [Node type taxonomy](07-node-type-taxonomy.md), and it may not be claimed
without one. Deliberately **not** written by node 28's manager, on [What the checker contract owes to having
been run](31-checker-contract-owes.md)'s warning: node 26's condition was the first written by a manager
rather than by a spawning node or its worker, and it had to be amended twice.
