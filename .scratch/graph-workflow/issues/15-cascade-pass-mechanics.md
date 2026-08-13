# Cascade pass mechanics

Type: grilling
Status: open
Blocked by: 07

## Question

The cascade is now a named mechanism with settled goals and no design. How does it actually run?

Settled by [Revision semantics](06-revision-semantics.md): it is aggressive, AFK and agent-driven; its scope is agent judgement over both blocking edges and the code itself; its output is queued graph edits — supersede resolved nodes, update open nodes in place, create intermediate nodes — and never a human interrupt. What is not settled:

- **When does it run?** Immediately when a revision lands, or as a step the manager takes before choosing the next node? Running late risks the manager scheduling work against a graph it already knows is stale; running immediately puts a pass between every revision and the next thing.
- **How many agents is it?** One agent per revision surveying the whole graph, or one per candidate node? The first is cheap and holds the whole picture but must fit the graph in one context; the second parallelises as AFK work and scales, at the cost of no agent seeing the pattern across nodes.
- **Who writes the edits** — does the cascade agent modify the graph files directly, or return a proposed edit list that the manager applies? The manager applying them keeps a single writer on the graph; the agent applying them saves a round trip and a large amount of relayed context.
- **Does it need the code-writing lock?** It reads the repo, and reading is safe under the single-writer rule — but if a cascade can ever be triggered while an implementation subagent is mid-edit, it is judging a tree that is in flux.
- **What does it report to the human, if anything?** Its whole design is to avoid interrupting, but a pass that supersedes eleven nodes silently is a surprise the next time the human looks at the graph.

Now unblocked by [Node type taxonomy](07-node-type-taxonomy.md), which also adds to the last two bullets:

- The pass creates and edits nodes drawn from five types, and the ones it will reach for when an implementation must change are `grilling` and `research` — both cheap, neither touching code.
- **On the code lock:** an implementation node now holds the exclusive slot from first edit through review and rework, which widens the window in which a cascade could be judging a tree in flux.
- Its queued output can also include **sharpening an unstarted node's acceptance condition**, since those are written by the spawner and updated in place.

Blocked on the taxonomy because the pass creates and edits nodes by type, and cannot be specified before the types are.
