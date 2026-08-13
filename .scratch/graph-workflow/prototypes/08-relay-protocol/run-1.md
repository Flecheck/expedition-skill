# Relay protocol — prototype run 1

Asset for [Relay protocol](../../issues/08-relay-protocol.md). Built live in the Claude Code harness: two HITL issue subagents in flight at once, each pausing on a question, relayed through the manager to the human, resumed with `SendMessage`.

The two subagents were given **Relay protocol's own listed open sub-questions**, so the human's answers feed the node's resolution rather than being spent on a toy.

- Subagent A — *Failure handling: a subagent that dies mid-question*
- Subagent B — *Human redirects: when the answer is not an answer*

## The contract each subagent was spawned with

Structurally identical for both, differing only in the node name and question. This *is* the prototype of the inbound half of [Subagent context contract](../../issues/12-subagent-context-contract.md).

```
You are an **issue subagent** in a graph workflow that is currently being prototyped.
You are NOT the manager thread, and you have **no channel to the human**.

Your node: <name>
Your node's question: <question>

Context to read (read them; do not trust any summary of them):
  <file pointers — map.md, the node this feeds, related resolved nodes>

Your job: grill the human to a decision on your node's question, following /grilling
discipline — ONE question at a time, always offer a recommended answer, and look facts
up in the files rather than asking about things you can read.

HARD RULES:
1. You must NEVER answer your own question on the human's behalf.
2. You have no human-facing tool. Do NOT call AskUserQuestion. When you have a question,
   **end your turn** and make the question your entire final output.
3. Do not edit, create, or delete any file. You are strictly read-only.
4. Your final output IS a machine-consumed return value, not a message to a person.

Return shape when pausing to ask — use exactly these labels:
  QUESTION FOR: <node name>
  ASK: <one question>
  RECOMMENDED: <recommendation and why, max 2 sentences>
  ALTERNATIVES: <1-3 other options, one line each>

You will then be resumed with the human's answer, with your context intact. Ask at most
two questions in total, then return:
  ANSWER FOR: <node name>
  DECISION: <the resolution>
  CONTEXT-PROOF: <restate your first question verbatim and the human's exact answer>
  NEW-NODES: <any new node this surfaces, or "none">
```

Three deliberate design choices in that contract, each of which the run tests:

1. **Context is passed as file pointers, not inlined.** Settles the open question in [Subagent context contract](../../issues/12-subagent-context-contract.md) in favour of wayfinder's zoom-as-needed pattern — if the subagents come back well-oriented, pointers are enough.
2. **Read-only.** Two HITL subagents live at once must not both be writing the graph. This is the concurrency lock from [Concurrency model](../../issues/04-concurrency-model.md) expressed as a contract clause rather than a scheduler.
3. **`CONTEXT-PROOF` is an instrumented probe**, not part of the real protocol — it exists only to prove the resume preserved context, and would be dropped from the shipped contract.

## Mechanical findings from the harness itself

These came from the harness's own constraints, before either subagent reported, and neither was anticipated when the node was written.

### F1 — The routing key is manager-private, and attribution must therefore be by node name

Spawning returns an opaque agent id which is the routing key for `SendMessage`, and the harness explicitly forbids surfacing that id to the human. So the relay is not symmetric: the manager routes by agent id, the human reads and answers by **node name**. The manager owns the mapping, and that mapping is state the manager must not lose — it is the whole reason an answer can find its way back.

This makes the attribution requirement in the node concrete: node name is the human-facing address, agent id the machine-facing one, and the manager is the only thing that knows both.

### F2 — The manager's view of a subagent is its return value and nothing else

The harness forbids reading a running subagent's transcript file: it is the full JSONL and would overflow the manager's context. So the manager cannot inspect a subagent's internal state, cannot see its progress, and cannot recover its partial work.

This bears directly on subagent A's question. A subagent that dies mid-question does not leave a readable partial state behind for the manager to salvage — whatever it had figured out is simply gone. Any failure-handling answer that assumes the manager can pick up where a dead subagent left off is not implementable in this runtime.

It also confirms the taxonomy's decision that a subagent must **report** its own new nodes and invalidations: the manager has no way to notice them otherwise.

### F3 — Concurrency was free at the manager level

Both subagents were launched in a single message and both ran at once, with no queueing visible to the manager. The two-HITL budget from [Concurrency model](../../issues/04-concurrency-model.md) needs no scheduler in v1 — it is a number the manager chooses to respect, not a limit the runtime imposes.

### F4 — The human's channel is serial no matter how many subagents are live

Subagent B's question arrived while subagent A's was still outstanding and unanswered. The manager buffered B and relayed it only after A's answer came back. Two HITL subagents in flight does **not** mean two questions in front of the human at once — it means the manager always has a next question ready.

That makes batch-versus-stream a real protocol choice the node did not anticipate: the manager could hold questions and present several at once, or stream them one at a time as they arrive. This run streamed, on the reasoning that a ready question should never wait. The cost of streaming is that the human answers in arrival order rather than an order they chose — which is exactly what the human's answer to subagent B then pushed back on.

### F5 — There is no such thing as a live idle subagent, so parking is free

Resuming a paused subagent reported *"had no active task; resumed from transcript"*. The subagent was not a suspended process being held in memory — it had **already stopped**, and the harness replayed its transcript to continue it. This is true of every subagent between turns.

Three consequences, and this is the finding that most changes the design:

1. **The ~2 HITL budget is not a resource constraint.** No machine resource is held by a waiting interview. The number is purely about the human's attention, which is precisely what [Concurrency model](../../issues/04-concurrency-model.md) claimed on principle — now confirmed mechanically rather than assumed.
2. **"Suspend in place" and "store progress then stop" are much closer than either the subagent or the human assumed**, because there is no live thing to stop and no slot to release. The real difference between them is not resource release but whether the *graph* records the half-finished interview durably.
3. **The harness already persists subagent context to disk** — that is what makes transcript replay possible. But the manager cannot read it (F2) and it is harness-internal, so the graph still cannot rely on it. The node-file log the human asked for is not redundant with it; it is the part the graph can actually see.

## Findings from the human's reaction — the payload was wrong

The point of a prototype is the reaction, and the reaction was mostly about the **shape of the relay payload**, which the node had not thought about at all. It assumed the hard part was routing. Routing turned out to be nearly free (F1, F5); the payload is the hard part.

### F6 — Relay the human's verbatim words, not the manager's paraphrase

Subagent A's `CONTEXT-PROOF` quoted what it called "the human's exact answer" — but what it actually held was the manager's paraphrase of an option label. For subagent B the manager passed the human's raw text instead, and B's answer then hinged on wording the paraphrase would have destroyed: B reasoned from *context ownership*, while the human's actual words revealed they were reasoning from **stakes**. Those lead to different designs.

So the rule is: the durable log and the downward relay both carry the human's own words. Manager framing is additive and separately marked. A paraphrase silently becomes the permanent record.

### F7 — A relayed question must carry the node's context, because the human has not read the node

The human's words: *"Since the issues are taken by the manager and sent to a subagent, I don't really know what the subagent question is about."*

This is the run's most important miss. The subagent reads the node, the map and several resolved nodes; the human reads none of that. A bare question arrives frame-less, and the human has to reconstruct why it is being asked before they can answer it — spending the scarce resource on orientation rather than judgement. Attribution by node **name** (F1) is necessary but nowhere near sufficient.

### F8 — A relayed question must carry a digest of what the subagent has done so far

Also the human's: there should be *"a summary of what the subagent did — in the answer there can be questions or information that should be shown to the user during the next question, or at least a summary if too long."*

The relay is not stateless. Each question after the first has a thread behind it: what the subagent read, what it concluded, what it decided on its own authority. Subagent B is the concrete case — it silently resolved two ambiguities before asking its second question, and without a digest the human would have seen the second question with no idea that ground had been settled underneath it. Long threads get summarized rather than dropped.

### F9 — Manager notes are a wanted feature, and are capped at current context

The human on the manager's own annotations: *"the Manager notes seems nice, that adds a cheap 2 third set of eyes tho the manager shouldn't look into the code, just give the notes using his current available information."*

So the manager is not a dumb pipe — it adds a third perspective, and it is well placed to, because it can see across threads while each subagent sees only its own. This run's notes were exactly that: the manager told subagent A that a parked interview needs a durable routing key, a fact discovered in subagent B's thread that A could not have known.

The cap is what keeps it cheap: notes come only from what the manager already has in context. **The manager does not read code or run research to produce them.** Without that cap the manager duplicates the subagent's work and becomes a second implementer rather than a second pair of eyes.

## Transcript

Four relayed questions, two `SendMessage` resumes, both subagents closed. Recorded because the *sequence* is the finding — in particular where the manager buffered, where it paraphrased, and where the human overruled.

**1 — A pauses.** Subagent A returned its question as its entire final output, in the specified shape, without answering it. The contract held on the first try.

**2 — Manager streams A's question.** Relayed with a manager note: a dead subagent leaves no salvageable state, so without durability the human's words are gone. **The manager paraphrased the human's answer when relaying it back down** — the mistake that produced F6.

**3 — B pauses while A's question is still outstanding.** Manager buffered B (F4). B had triaged its own four cases and asked only about the one with machinery cost, citing a rule it had read in a resolved node — grilling discipline working as intended: four questions compressed to one.

**4 — Human answers A: log on the node file, at relay time.** Recommendation accepted as stated.

**5 — Manager relays B's question**, noting that parking only survives the manager's own death if the routing key is durable — a fact from A's thread that B could not see. This is the manager-as-third-party behaviour the human later endorsed (F9).

**6 — Human overrules B**, choosing store-progress-and-stop over suspend-in-place, and revealing that "ask me later" is a prioritization act. The manager relayed the words **verbatim** this time, and had to add an explicit *"this does not match your recommendation — do not resolve as if it did"*, which became the `DIVERGENCE` field.

**7 — A closes**, with context intact across the resume. Its self-check quoted "the human's exact answer" while actually holding the manager's paraphrase from step 2 — the run's own contract violation, caught by the instrument that was measuring it.

**8 — B asks its second question**, having settled two ambiguities alone: whether the subagent or the manager writes stored progress, and whether a parked node returns to `open`. It escalated only the one touching a core invariant — whether "you decide" is supported at all, since it ends with a subagent answering its own HITL question.

**9 — Manager relays.** The human rejected the framing and asked to clarify, then supplied four things at once: relayed questions need node context; they need a digest of what the subagent did; manager notes are wanted but capped at current context; and "you decide" is answered by the subagent, because delegation signals the question does not matter much to them.

**10 — B closes**, adopting the delegation target from the human's answer but re-deriving the rest from the human's *stakes* reasoning rather than its own context-ownership reasoning — which changed its conclusion: a delegated answer resolves the node rather than waiting for confirmation. It also noted it could not verify whether what it received was the human's wording or the manager's, which is what produced the provenance marker.

### What the run cost

Two subagents, four questions, roughly 178k subagent tokens. The human answered three questions and rejected one framing. Both interviews reached a decision.

### What would be done differently

- Relay the human's words verbatim from the first exchange, not the third.
- Send `ABOUT` and `SO FAR` with every question from the start; the human should not have had to ask for them.
- The `CONTEXT-PROOF` instrument earned its place and then argued for its own replacement — it caught a real violation, and what it revealed (that provenance is unverifiable from inside a subagent) is better handled by a marker than by an honour-system field.
