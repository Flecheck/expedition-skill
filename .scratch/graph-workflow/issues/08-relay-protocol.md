# Relay protocol

Type: prototype
Status: resolved

## Question

How does a question from an issue subagent reach the human, and the answer get back to the right subagent — when the human only ever talks to the manager?

Build the smallest real thing that proves one round-trip end to end, then react to it. This is the highest-risk mechanism in the design and has the least precedent: firstmate's crewmates are autonomous, so it never had to pipe a one-question-at-a-time interview through a supervisor.

What the prototype must demonstrate:

- A subagent running `/grilling` **pauses** on a question instead of answering it itself, and does so without discarding its context.
- The manager surfaces that question to the human **attributed to its issue**, so the human knows which thread they are answering.
- The answer returns to the *correct* subagent, which resumes where it left off.
- The above works with **two HITL subagents live at once** (per [Concurrency model](04-concurrency-model.md)) — this is the multiplexing case, and it is where a naive design breaks.

Known starting point: this harness's `SendMessage` resumes a spawned agent with its context intact, so return-a-question then resume is mechanically possible. The prototype is to find out whether it is *pleasant* — how many round-trips a real grilling needs, whether the pause/resume cycle preserves interview momentum, and how badly it degrades when two interviews interleave.

Questions the prototype should also expose:

- What happens when a subagent dies or errors mid-question?
- Does the manager ever answer on the subagent's behalf? (It must not — a grilling agent that answers its own questions has broken the HITL contract.)
- Does the human need a way to redirect a question back ("ask me later", "you decide")?

Blocks: [Subagent context contract](12-subagent-context-contract.md)

Prototype asset: [run 1](../prototypes/08-relay-protocol/run-1.md) — two HITL subagents in flight, four relayed questions, two `SendMessage` resumes, run live in the harness. All findings below are labelled `F1`–`F9` there.

## Answer

**Routing was never the hard part. The payload is.**

The node was written on the assumption that multiplexing a question channel was the risk — that attribution and return-routing were where a naive design breaks. The prototype proved routing nearly free, and then the human's reaction landed almost entirely on the *shape of what gets relayed*, which this node had not considered at all.

### What the prototype settled mechanically

- **Addressing is asymmetric.** The human addresses a thread by **node name**; the manager routes by an opaque runtime key the human never sees. The manager owns the only mapping between them, so that mapping is state it cannot afford to lose (`F1`).
- **There is no such thing as a live idle subagent.** A resumed subagent reports *"no active task; resumed from transcript"* — it had already stopped, and the harness replays its transcript to continue it. This is true between every turn (`F5`). Two consequences: a waiting interview holds **no machine resource**, so the ~2 HITL budget from [Concurrency model](04-concurrency-model.md) is purely about human attention — confirmed mechanically rather than assumed — and parking costs nothing.
- **Concurrency needs no scheduler in v1.** Both subagents were launched in one message and ran at once (`F3`). The HITL budget is a number the manager respects, not a limit the runtime imposes.
- **The human's channel is serial regardless of how many subagents are live** (`F4`). Two in flight means the manager always has a next question ready, not that two questions sit in front of the human. The manager therefore chooses between **streaming** questions as they arrive and **batching** them. v1 streams, because a ready question should never wait — accepting that the human answers in arrival order rather than an order they chose. That cost is real and is what surfaced [Human-initiated steering](16-human-steering.md).

### The relay payload

This is the deliverable. Upward, manager → human:

```
NODE:          <node name — the human's only address for this thread>
ABOUT:         <1-2 lines: what this node decides, and why it is being decided now>
SO FAR:        <digest of the thread: what the subagent read, what it concluded, and
                what it has already decided on its own authority. Summarized if long.>
ASK:           <the subagent's question, verbatim>
RECOMMENDED:   <the subagent's recommendation and why>
ALTERNATIVES:  <the options it rejected>
MANAGER NOTES: <optional; cross-thread facts the subagent could not see>
```

`ABOUT` and `SO FAR` exist because of the run's largest miss (`F7`, `F8`): the subagent reads the node, the map and several resolved nodes, and **the human reads none of that**. Attribution by name is necessary and nowhere near sufficient — a frame-less question makes the human spend the scarce resource on orientation instead of judgement. `SO FAR` is not optional politeness either: subagent B silently settled two ambiguities before asking its second question, and without a digest the human would have answered it unaware that ground had shifted underneath.

`MANAGER NOTES` makes the manager a third perspective rather than a pipe, and it is well placed for it because it sees across threads while each subagent sees only its own. The run's live example: the manager told subagent A that a parked interview needs a durable routing key — a fact discovered in subagent B's thread that A could not have known. **The notes are capped at what the manager already holds in context: it does not read code or run research to produce them.** Without the cap the manager duplicates the subagent's work and becomes a second implementer instead of a second pair of eyes (`F9`).

Downward, manager → subagent:

```
HUMAN ANSWER:  <the human's own words, verbatim>
DIVERGENCE:    <required when the answer contradicts the subagent's recommendation:
                say so explicitly, so it does not resolve as though it had won its point>
MANAGER NOTES: <optional; marked as the manager's, never blended into the human's answer>
```

**Verbatim is a hard requirement, not a preference** (`F6`). Subagent A's self-check quoted "the human's exact answer" while actually holding the manager's paraphrase of an option label. For subagent B the manager passed raw text, and it mattered: B had argued from context ownership, while the human's actual words revealed they were reasoning from **stakes** — which led to a different answer than B's own reasoning would have. A paraphrase silently becomes the permanent record.

`DIVERGENCE` is also load-bearing, and also learned from the run: the human overruled subagent B, and the manager had to state that explicitly to stop B resolving as if vindicated.

**Provenance travels with the answer.** Subagent B's most useful move was noting it could not verify whether what it received was the human's wording or the manager's. Rather than trusting discipline, an answer is marked verbatim or paraphrased, so a later reader can tell how far from the human a recorded decision sits.

### When a subagent dies mid-question

The node file is the only thing that survives, so it carries a **per-attempt relay block**: the attempt's routing key, then each relayed question and each human answer appended **at relay time** — the answer written the moment the human gives it, before the manager attempts the resume. The ordering is the whole point: the manager cannot learn the agent is dead until a resume fails, by which time the human's effort is already spent, and their words are the only thing in this system that cannot be regenerated.

- **Death is detected lazily and only by a failed resume**, since the manager can neither read a running subagent's transcript nor inspect a dead one (`F2`). A key that fails to resume means gone; the manager marks that attempt dead rather than retrying it.
- **Recovery is automatic and AFK.** The node keeps its number, its file and its claim — **the claim belongs to the node, not the agent instance**, and is never released by a crash. This is the same carve-out [Node type taxonomy](07-node-type-taxonomy.md) made for a rejected review. A fresh subagent is spawned with the node plus the full replayed transcript and an instruction that already-answered questions are settled facts, never to be re-asked. Its new key is appended as the next attempt.
- **The human is told once**, by node name: that the agent for that node died, that their answer is recorded and being replayed, and that they may see a follow-up but will never see the same question twice.
- **Capped at two respawns.** Replay re-inflates exactly the context that killed the previous attempt, so a third failure is not a crash to retry but evidence the node is too coarse; it escalates to the human as a graph-shape decision. At that escalation the node does hold work — the transcript — so its smaller replacements arrive by ordinary supersession under [Revision semantics](06-revision-semantics.md). That is the one path on which a death eventually becomes a revision.

Note this partially answers the map's open *Resume and recovery* item: durable routing keys on disk mean a fresh manager can re-adopt still-live interviews after its own death or compaction.

### The four redirects, when the answer is not an answer

All four are supported in v1; only two cost machinery.

| Redirect | What happens |
| --- | --- |
| **"Go read X first"** | Free. Ordinary answer text, relayed verbatim; the resumed subagent reads X and carries on. |
| **"You decide"** | Answered by the **subagent, never the manager** — on the human's own reasoning that delegation signals the question does not matter much to them. That same reasoning settles what it does: it **resolves** the node rather than waiting for confirmation, because blocking on a question the human has just priced as cheap pays a round-trip for nothing. |
| **"Ask me later"** | A **prioritization** act, not a pause. The manager instructs the subagent to store its progress and stop; the subagent returns the dump; the manager writes it onto the node (subagents stay off the graph, single writer preserved); the node returns to **`open`** with its banked answers intact. No new status, nothing deleted, and the HITL slot frees the instant the human says it — which is the whole point of them saying it. |
| **"Wrong question — here is the real one"** | Relayed to the live subagent, and the node's question is updated **in place**, with the old wording marked superseded rather than removed. [Revision semantics](06-revision-semantics.md) supersedes only to preserve work, and a mid-interview node holds no answer, so a replacement node would be pure noise. An *additive* reframe becomes a new node instead; a reframe arriving after the node resolved is ordinary supersession. |

**Stored progress must include the questions already answered and the human's words verbatim, not a summary.** Losing live context is the price of store-and-stop, and this is the only thing that stops a fresh subagent re-asking what the human already paid for.

### What the manager may never do

The manager gains exactly four powers in this protocol — relay verbatim, instruct-store-and-stop, write a returned dump, and annotate from context it already holds. There is **no path on which it answers anything**. Both "you decide" and a mid-interview reframe route to the subagent, which holds the interview; the manager's temptation to shortcut either one is the failure this node exists to prevent.

### Adopted on agent judgement, revisable

1. **The human-delegated flag is a record, not a blocker.** A delegated answer is marked so a later reader can see which parts of a node the human did not personally decide, but it does not gate done-ness. [Done-ness](10-done-ness.md) owns that question; this is an input saying this particular flag does not block.
2. **Per-question and whole-node delegation are two different acts.** Bare "you decide" is per-question and the interview stays HITL. Whole-node delegation must be said explicitly and converts the remainder to AFK: the subagent finishes alone, each remaining call is recorded as a delegated flag, and the slot frees at once. **The manager may never infer whole-node scope from a per-question answer** — silence about scope means per-question, because widening it on inference silently removes the human from a node.
3. **`CONTEXT-PROOF` was instrumentation and is dropped** from the shipped contract. What replaces it is the provenance marker above, which is cheaper and answers the question that actually mattered.

### Consequences

- **[Subagent context contract](12-subagent-context-contract.md) unblocks**, and inherits the payload above as a first draft of both halves, plus a third return variant — parked-with-progress — and delegated-answer marking. The inbound contract used in the run is recorded verbatim in the [prototype asset](../prototypes/08-relay-protocol/run-1.md); passing context as **file pointers rather than inlined text** worked, so wayfinder's zoom-as-needed pattern is confirmed for that node.
- **Two new nodes:** [Human-initiated steering](16-human-steering.md), because "ask me later" turned out to be prioritization and nothing in the graph lets the human say what they want *instead*; and [Off-contract subagent output](17-off-contract-output.md), which is a distinct failure mode from death — the agent is alive and resumable, so the remedy is rejection and a re-prompt, not a respawn.
- **[Graph file format](13-graph-file-format.md)** inherits per-attempt relay blocks, a durable routing key per attempt, dead-attempt marking, an append-only Q&A log, banked progress, and delegated flags — and needs **no new status** for any of them.
- **[Naming](14-naming.md)** inherits: relay, park, attempt, banked answer, delegated flag, manager note, provenance.
- The map's *Failure handling* fog splits: the death half is answered here, the garbage half becomes a node. *Resume and recovery* gains a mechanism. *How the human sees graph progress* gains a sharp requirement — parked nodes now hold banked human answers, so a graph read must surface **which nodes are half-interviewed**, or a deferral becomes invisible debt.
