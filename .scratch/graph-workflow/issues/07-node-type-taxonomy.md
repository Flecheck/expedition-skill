# Node type taxonomy

Type: grilling
Status: resolved

## Question

What is the complete set of node types, and what exactly distinguishes them?

Wayfinder has four: research, prototype, grilling, task. This workflow adds implementation. Open points:

- **Does implementation subsume prototype?** The stated thesis is that an implementation *is* a better prototype. If so, does `prototype` survive as a separate type — perhaps as the throwaway variant, where implementation is the kept variant — or does it disappear?
- **Is there a verification or review type**, or is verification an obligation attached to every implementation node rather than a node of its own?
- **Does `task` still earn its place** now that the graph can contain real work? Wayfinder's `task` exists precisely because that skill refuses to do; here doing is normal.
- Which types are HITL and which are AFK? This directly feeds the concurrency budget in [Concurrency model](04-concurrency-model.md) — the human-saturating parallelism only works if the HITL/AFK split per type is known.
- Does an implementation node carry an acceptance condition, and who writes it — the node itself, or the node that spawned it?

Blocks: [Done-ness](10-done-ness.md), [Subagent context contract](12-subagent-context-contract.md), [Graph file format](13-graph-file-format.md), [Naming](14-naming.md), [Cascade pass mechanics](15-cascade-pass-mechanics.md)

## Answer

**Five types: research, prototype, grilling, task, implementation.** One added to wayfinder's four, and nothing removed.

### Implementation and prototype are separated by one question: is the artifact the deliverable?

- **Implementation** — the output is product code. It lands in the repo, it must be correct, and it is what the destination is measured against.
- **Prototype** — the output is a probe. It exists to be reacted to and is then discarded, and it need not be code at all: an outline, a protocol sketch, a stub.

Prototype survives despite the thesis that an implementation is a better prototype, for two reasons. First, [Relay protocol](08-relay-protocol.md) is already a prototype node in this map, and what it will produce is a sketch of a message protocol rather than shippable code — a taxonomy that forced that node to become an implementation would be wrong about a case standing directly in front of it. Second, the two cannot share a priority rule: [Revision semantics](06-revision-semantics.md) sends code revisions to the front of the exclusive code slot precisely because a superseded implementation means the repo holds wrong code *right now*, while an invalidated prototype implies nothing at all about the repo.

The rejected alternative worth naming is restricting prototype to non-code artifacts, which would give a bright mechanical line — does it write code? — instead of relying on intent. It was rejected because it forbids the cheap throwaway spike, forcing every "how should this behave" question about code to be answered by building the real thing. Intent is the honest criterion here, and the kept/throwaway axis states it directly.

### `task` survives — decided from evidence rather than asked

Wayfinder's `task` exists because that skill refuses to do; here doing is normal, so the type looks redundant. It is not: this map's own Notes record `git init` as a prerequisite before any implementation node can run. That is work which unblocks the deliverable without being part of it, and no other type holds it — it decides nothing, probes nothing, and produces no product code. The test is **precondition versus deliverable**, and it keeps HITL tasks too, since provisioning and signups are still handed to the human as a checklist.

### Verification is an obligation, not a type

An implementation node is not resolved until a **second, independent agent** has checked the landed code against the node's acceptance condition. Self-review was rejected: [Revision semantics](06-revision-semantics.md) already accepted one unchecked-judgement risk in the cascade, and stacking a second one under a destination that claims the code ends up perfect is more trust than the design can carry. A separate verification type was also rejected — it would let an implementation node resolve while unverified, breaking "resolved means done" and forcing exactly the landed-but-unverified status that [Graph file format](13-graph-file-format.md) is already worried about.

The reviewer is AFK and read-only, so it needs no code lock and costs the human nothing. The accepted cost is that a rejection lengthens the serialized code path, since the implementer goes back to work while still holding the slot.

### Implementation is AFK and never asks a live question

The human's channel stays reserved for HITL nodes. When an implementer meets a decision it cannot make from the settled graph, it judges the size:

- **Small ambiguity** — pick the most defensible answer, **flag it on the node as an assumption**, and land. The flag reaches the human queued on the node, per discovery-is-not-resolution.
- **Genuine fork** — surface a grilling node and block on it.

Which of the two it is, is the implementer's judgement — the same judgement-based scoping the cascade already runs on. This is the workflow's thesis operating as designed: implementing under uncertainty is informative, and revision semantics is the machinery that makes a wrong assumption recoverable instead of fatal. Blocking on every ambiguity was rejected as paying a full scheduling round for a ten-second question; letting the implementer ask live was rejected because it would make code compete with grilling for the one scarce resource.

### Acceptance conditions are written by the spawning node

Whoever creates an implementation node states what done means, before any work starts. Two reasons fix the owner: it is independent of the agent that will be judged, and the reviewer above needs something objective to check against or its review collapses into a second opinion. It also composes with revision — an unstarted node is updated in place, so a cascade can sharpen a condition that proved too coarse.

The accepted risk is vagueness: a spawner that does not know the code may write a condition too loose to fail, and a loose condition is worse than none because the reviewer will rubber-stamp it. The mitigation is the assumption flag — see below.

### HITL / AFK, and what contends for the code slot

| Type | Human in the loop? | Code slot |
| --- | --- | --- |
| research | AFK | no |
| prototype | **HITL** — the reaction is the point | no |
| grilling | **HITL** | no |
| task | either; AFK where the agent can drive it | sometimes |
| implementation | AFK | **yes, exclusive** |
| *reviewer* (an obligation, not a type) | AFK | no — read-only |

The consequence for [Concurrency model](04-concurrency-model.md) is worth stating plainly: the ~2 HITL budget is a budget over **grilling, prototype, and HITL tasks**, and it is **disjoint from the code slot**. Code and review therefore progress while the human is grilling, which is what saturating the human actually requires. Only HITL tasks straddle both.

### Three things adopted on the agent's judgement rather than asked

These are the most revisable parts of this answer.

1. **Prototype artifacts live outside the product tree, so a prototype never contends for the code slot.** This follows from the axis chosen: an artifact that is discarded by definition is not the product, so writing it into the product tree contradicts the distinction that separates the two types. Recorded as an input to [Git and code-landing policy](11-git-and-code-landing.md), which owns where things land.
2. **Reviewer rejection is not supersession**, and this closes a real hole. [Revision semantics](06-revision-semantics.md) says a node is superseded once "code has landed", which taken literally would fire on every rejected review — producing a supersession chain per review round, and tripping the repeat-revision escalation rule into interrupting the human on the second rejection. That test is scoped to revision arriving from **outside** the node. A node still claimed and under review keeps its number, its identity, and its file; there is no chain and no replacement.
3. **An implementer may not rewrite its acceptance condition, but may flag it as wrong** — the same mechanism as an assumption flag, queued for the human. This is what stops a too-loose condition from being silently rubber-stamped, and it costs no new field.

### Consequences

- No new nodes. This answer fills in nodes that already exist rather than surfacing fresh questions, which is what a bottleneck node resolving well should look like.
- **Four nodes unblock:** [Done-ness](10-done-ness.md), [Graph file format](13-graph-file-format.md), [Naming](14-naming.md), [Cascade pass mechanics](15-cascade-pass-mechanics.md). [Subagent context contract](12-subagent-context-contract.md) still waits on [Relay protocol](08-relay-protocol.md).
- [Done-ness](10-done-ness.md) gains a sub-question it could not have had before: whether an unresolved flagged assumption blocks done-ness.
- [Graph file format](13-graph-file-format.md) inherits a five-value type vocabulary, an acceptance-condition field, and somewhere to put assumption flags and the reviewer's outcome.
- [Naming](14-naming.md) inherits five kinds to name, plus the reviewer, the acceptance condition, and the assumption flag.
- A clarifying note was added to [Revision semantics](06-revision-semantics.md) recording the scoping in point 2. That is an additive annotation to a resolved node, not a revision of it: its answer is not wrong, it simply did not consider mid-flight review. Superseding it would have manufactured a chain out of a cross-reference.
