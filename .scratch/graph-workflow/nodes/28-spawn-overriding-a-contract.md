# Whether a spawn may override a shipped worker contract

Type: grilling
Status: open

## Question

May a spawn suspend a clause of the contract it names, and if so under what conditions?

It has already happened once. [Whether flags.md survives the settle-at-close
practice](27-does-flags-file-survive.md)'s spawn suspended one rule of
[`expedition-grilling/SKILL.md`](../../../.claude/skills/expedition-grilling/SKILL.md) — *"`flags.md` is
not yours. Leave it unread."* — on the ground that the node was about that file. The override was
well-grounded, it was stated plainly in the spawn, and the node could not have been worked without it.
Nothing in the design permits it.

Reported by that node's own worker, which was told the override had happened and put it on the record
rather than deciding it.

### Why it is not obviously fine

[Write the worker contract skills](22-worker-contract-skills.md) fixed the opposite direction: a spawn
**names the contract's path** and **the file on disk wins**, because the harness serves the skill body it
loaded and a contract edited mid-session does not reach a worker spawned afterwards. An override inverts
that — the spawn now beats the file for one clause.

It also costs a property [map.md](../map.md)'s `## Notes` bought deliberately as v1's insurance for v2: a
worker contract that **stands alone as a file** rather than depending on skill invocation, so that a
non-Claude harness can be handed the same contract. If a spawn may suspend a clause, a worker's behaviour
is no longer readable from its contract alone, and the insurance is worth less than it looks.

### What the answer has to decide

- Whether a spawn may override at all, or whether the correct move was something else — a different
  contract, a wider clause, or an exception written into the contract itself so that no override is needed.
- If it may: what must hold. Candidates, none of them decided — the override is **stated in the spawn**
  rather than implied; it **names the clause** it suspends; it is **recorded on the node** so a later
  reader can see the worker was not running the shipped contract; and it may **never widen what the worker
  may write**, since the write rules are what keep the manager the graph's only writer.
- Whether the specific clause that was overridden should instead be narrowed in the contract. *"`flags.md`
  is not yours"* exists to keep a worker's read small, and a node **about** that file is a case the clause
  did not consider.

Feeds the **manager's own skill**, which is where any rule about spawns would live, and which is the last
product file to be written.
