# Graph file format

Type: grilling
Status: open
Blocked by: 06, 07

## Question

What files represent the graph, with what fields, and where do they live?

Settled input: markdown files and prose rules, wayfinder-style, not a CLI ([Graph state mechanism](05-graph-state-mechanism.md)). This issue fixes the actual shape.

- Directory: reuse `.scratch/<effort>/` as this map does, or a distinct location since this workflow is not wayfinder?
- One file per node plus an index map, as wayfinder does — or a different split?
- How are edges encoded? Wayfinder's `Blocked by: NN, NN` covers blocking, but revision may need a second edge kind (supersedes, invalidated-by) depending on [Revision semantics](06-revision-semantics.md).
- What is the status vocabulary? Wayfinder has open / claimed / resolved. Revisable nodes may need more — superseded, needs-revision — and implementation nodes may need a landed-but-unverified state.
- Does the index still carry a one-line gist per closed node, and does that stay accurate when a node is later revised?
- Is node identity stable across revision? If a node is superseded, does the number get reused, and do inbound edges follow?

Settled by [Revision semantics](06-revision-semantics.md), so this node encodes rather than decides it:

- Status vocabulary gains `superseded`, and `superseded` does **not** satisfy a `Blocked by` edge — a dangling edge onto a superseded node is an error the format should make detectable.
- Two edge directions, both required: `Superseded by: NN, NN` on the old node (so a stale answer is never read as current) and `Supersedes: NN` on the replacement (so "is this a revision?" is a local read).
- Node identity is stable and numbers are never reused.
- No `Touches:` field on implementation nodes — cascade scope is agent judgement, explicitly not declared bookkeeping.
- Superseded text stays in the file, marked as superseded, rather than being deleted — so the format needs a place to put it.

Settled by [Node type taxonomy](07-node-type-taxonomy.md), so this node encodes rather than decides it:

- The type vocabulary is exactly five: `research`, `prototype`, `grilling`, `task`, `implementation`.
- Implementation nodes carry an **acceptance condition**, written by the spawning node before work starts — so it is a field the spawner fills, not one the worker fills.
- There must be somewhere to put an implementer's **flagged assumptions**, and somewhere for the **reviewer's outcome**. Neither is a status: a node under review or carrying flags is still just claimed or resolved.
- No landed-but-unverified status is needed, because verification happens inside the implementation node rather than after it.

Settled by [Relay protocol](08-relay-protocol.md), which adds a whole dimension this node did not know about — a node file is now also an **interview log**:

- A node carries **per-attempt relay blocks**: the attempt's opaque routing key, and an append-only log of each relayed question and each human answer, written at relay time. Whether the log sits inline in the node file or in a sibling file is a format call and belongs here.
- Answers carry **provenance** — the human's verbatim words versus a manager paraphrase — because a paraphrase silently becomes the permanent record.
- Attempts can be marked **dead**, and there is a **two-respawn cap** to count against.
- A parked node carries **banked progress**: answers already paid for by the human, on a node that has gone back to `open`. The format must make a half-interviewed node distinguishable from a never-started one, or a deferral becomes invisible debt.
- **Delegated flags**, where the human said "you decide" and the subagent answered.
- Still **no new status** for any of this: parked is `open`, under-review is `claimed`, and flags are not statuses. The status vocabulary stays at open / claimed / resolved / superseded.

Blocked on revision semantics and the taxonomy because the fields are a direct encoding of both. Fixing the format first would just be deciding those two by accident.
