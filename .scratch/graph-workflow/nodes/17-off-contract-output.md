# Off-contract subagent output

Type: grilling
Status: resolved
Blocked by: 12

## Question

What happens when a subagent is alive but returns garbage — output that does not satisfy its return contract?

Split out from the map's *Failure handling* fog by [Relay protocol](08-relay-protocol.md), which answered the other half: a subagent that **dies** mid-question. The two are genuinely different failures and share no remedy.

- A dead subagent leaves nothing to salvage, so the answer is replay into a fresh agent.
- An off-contract subagent is **alive and resumable**, so the remedy is rejection and a re-prompt against the contract — no respawn, no replay, and the node's claim never in question.

Open:

- What counts as off-contract? A missing required field is mechanical; a well-shaped answer that is merely **thin** is a judgement call, and the manager is the only one positioned to make it.
- How many re-prompts before the manager gives up, and what does giving up mean — respawn, escalate as a node-too-coarse decision (the route [Relay protocol](08-relay-protocol.md) took for repeated death), or hand it to the human?
- Does a rejected return get **recorded** on the node? [Revision semantics](06-revision-semantics.md) says nothing is deleted, but a log of rejected garbage may be noise rather than history.
- Does the same rule cover an **implementation** subagent whose code fails its acceptance condition? [Node type taxonomy](07-node-type-taxonomy.md) already routes that through the independent reviewer, so these may be one mechanism or two.
- The dangerous case: output that satisfies the contract's *shape* while inventing content — a subagent that answers its own HITL question and formats it as though the human had. Nothing currently detects this, and it is the exact failure [Relay protocol](08-relay-protocol.md) exists to prevent.

Blocked on [Subagent context contract](12-subagent-context-contract.md), because "garbage" is only definable against a fixed return shape.

## Answer

**On-contract means the manager can file it. It never meant that the worker followed the script.**

This node was written expecting the opposite — that a live worker's bad return is garbage, and that the remedy is to refuse it and ask again. The record says otherwise. [Write the worker contract skills](22-worker-contract-skills.md) ran the six contracts for the first time, over six checker attempts on one node, and four of the most valuable things that happened there were workers doing what their contracts did not name: two axes of a reviewing skill left unrun to protect the checker's own blindness, a refusal to take the manager's word for what had changed, and a verdict handed back with one condition marked not establishable, where the contract offered only a raise that costs the whole verdict or a verdict with a silent gap. Three of those became rules in the shipped checker contract. The fourth is why `PASS` and `FAIL` now carry `QUESTIONS:` alongside them — the contract was amended because a worker went outside it. A manager that had refused those four and asked again would have paid tokens to receive the worse of two answers, four times over.

### The test is fileability

A handover is on-contract when the manager can paste it under the node's headings. That is the whole test, and nothing else in it is about conformance:

- **Everything required is present, plus something the contract does not name** — on-contract. File it.
- **A route the contract does not offer, taken in place of one it does** — on-contract, provided what came back can still be filed. File it.
- **A required part absent, or a shape with no heading to sit under** — the manager cannot file it, and only this case re-prompts.

**What a handover departs by becomes a flag beside it**, filed by the manager against the node — at the gate where the node has one, and as the manager closes the node where it does not, which is where a flag is still cheap because the work is still there. Where the human wants a departure kept, **amending the contract is an implementation node against that skill file**, never something the manager does mid-flight. That path has already run once, on these very files.

**Annotated by [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md),
which made that sentence load-bearing and found the hole beside it.** The sentence holds unqualified and is
not amended. What node 28 adds is what the manager does when the defect is found **while a node is being
worked**: the repair is an implementation node and a gate, and the node in front of the manager cannot wait
for it. So the manager raises, and the human's answer produces a **licence for that one attempt** — recorded
as a flag on the node — alongside a **node for the permanent fix**. **A licence is not an amendment: nothing
on disk changes**, so the prohibition above is untouched and the two rules are not competing. The evidence
that both outputs are needed is that [Whether flags.md survives the settle-at-close
practice](27-does-flags-file-survive.md) took the departure and minted no node, and a session later the
clause was still unchanged in five contracts.

### What fileability cannot see, and the one check against it

A handover that satisfies its shape while inventing its content files perfectly. The exposure is narrower than this node feared, for a structural reason: a worker writes no graph file, and the manager writes the human's words into `## Interview` itself, in the same turn it resumes the worker. That record is the manager's own text and never passes through a worker, so no worker can forge an entry in it. What a worker can still do is write an `ANSWER` — the node's permanent text, pasted unaltered — resting on something the human never said, or rendering its own call as theirs.

**So before it files, the manager holds the handover's `ANSWER` against the `## Interview` it wrote itself, and anything resting on words the human did not say is filed as a flag beside it rather than refused.** This is the only join in the design where the checking party already holds both sides: both texts are the manager's own and both were made in the exchange just finished, so nothing is re-read and nothing is re-derived. It stays inside the scribe rule — reading is not re-authoring, and the manager is already permitted separately-marked notes of its own.

**The check has a limit, stated rather than fixed.** Its baseline can itself be one remove from the human: an answer given by taking an option as it was written is recorded in the manager's wording. The check catches a worker inventing the human's words and cannot catch a manager having supplied them, and afterwards the two look alike on the page. All three answers on this node were given that way. The remedy belongs to the relay's verbatim rule, not here, and is the new node below.

**The limit is now closed**, by [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md): the manager pastes the human's reply as they wrote it, however
terse, and quotes the option beside it attributed to the worker. The baseline of this check is therefore
the human's own words from here on, and *resting on words the human did not say* becomes decidable rather
than merely stated. This node's own three `paraphrase` markers **stand** — they were accurate about the
text they carried — while [Subagent context contract](12-subagent-context-contract.md)'s three `verbatim`
markers for the same act were corrected there.

### The narrow lane: one re-prompt, then the human

Where the manager genuinely cannot file the thing, it re-prompts **once**, naming exactly which part is missing. A second unfileable return is not re-prompted again and is not respawned: the manager files what it can, leaves the node `open` holding what is already on it, and tells the human once by node name — the same single notice a death gets.

One re-prompt is enough because the lane is mechanical: naming the absent part fixes a formatting slip on the first attempt, and a worker told exactly what is missing and still unable to produce it is not failing at formatting — it is saying it has nothing for that part, and a third asking cannot change that. **[Relay protocol](08-relay-protocol.md)'s cap of two does not transfer**, and the reason is worth keeping: that cap is two because replay re-inflates the context that killed the previous attempt. Nothing is replayed here. The worker is alive, holds its own context, and is handed one line.

**A worker that cannot be reached at all is a death, and that node owns it whole.** A stop by the human is the live case: the harness refuses to resume a stopped worker, so re-prompting is a route that can simply be unavailable, and what remains is the fresh attempt this answer otherwise declines. The manager's only difference from an ordinary death is that it already holds an unfileable return, which goes into the replay rather than being discarded.

**Nothing rejected is written onto the node.** The never-delete rule governs what is in the graph's files rather than what must enter them, and an unfileable return is by construction the thing with no heading to sit under.

**The word `reject` is deliberately not used for any of this.** It is the human's at the gate, and the checker's `REJECT` was renamed `FAIL` to free it. A handover the manager cannot file is *unfileable*, and what the manager does is *re-prompt*.

### What this does not touch

- **An implementation worker whose code fails its acceptance condition is not this node's business.** The checker returns `FAIL`, the worker corrects, the gate is raised. That never reaches the manager as a handover.
- **The scribe rule stands unqualified.** The manager still pastes and never re-authors; reading before filing, and adding a marked flag, are both already its.
- **The death route stands unqualified**, including its cap of two.

## Flags

`17.1` **· settled** `ASSUMPTION` — an implementation worker whose code fails its acceptance condition was ruled outside
this node alone, on the ground that [Node type taxonomy](07-node-type-taxonomy.md) and [Human review of
landed code](20-human-code-review.md) already route it through the checker's `FAIL`; the human was not asked
whether the two are one mechanism.

`17.2` **· settled** `ASSUMPTION` — decided alone that an unfileable return is never written onto the node, and that it
goes into the replay only where the worker turns out unreachable; the never-delete rule was read as
governing what is in the graph's files rather than what must enter them.

`17.3` **· settled** `ASSUMPTION` — decided alone not to use the human's own word `reject` for a handover the manager
cannot file, because the gate and the checker already split that word once; their wording was changed rather
than followed.

`17.4` **· settled** `ASSUMPTION` — **filed by the manager, by running this node's own check on this node's own handover.**
The `ANSWER`'s paragraph beginning *"A worker that cannot be reached at all is a death"* rests on no words
the human said. It came from a manager note that named three places the stopped-worker case could go and
added *"I lean to the last of the three, and I am not deciding it"*; the worker adopted the lean and wrote it
into the node's permanent text. The substance is structural rather than a preference, and it is the reading
[Relay protocol](08-relay-protocol.md) already supports — but it is the manager's reading, filed here because
the check the human had just approved is what surfaced it. **The check found something on its first run, and
what it found was the manager.**

## Interview

### Attempt 1 — routing key `graph-workflow/17/a1`

The first node on this map grilled by a **worker under a shipped contract** rather than by the manager
directly. Spawned against [`expedition-grilling/SKILL.md`](../../../.claude/skills/expedition-grilling/SKILL.md),
which [Write the worker contract skills](22-worker-contract-skills.md) landed one session earlier.

**Q1 — is a departure from the contract off-contract at all?**

The worker's `ASK`, verbatim: *"Is a return that carries everything its contract requires, plus something
the contract does not name — or in place of a route the contract does name — off-contract at all?"*

Its `RECOMMENDED` was **no** — cut the question on whether the manager can *file* the return, not on
whether it matches the script — resting on the six checker attempts recorded on [Write the worker contract
skills](22-worker-contract-skills.md), where four departures produced three shipped rules and one outcome
better than either route the contract offered. Three alternatives were set aside: strict conformance, a
third handover state, and leaving it unwritten to the manager's judgement.

**A1 — the human took the recommendation.** `paraphrase`: the offered option as written, chosen without
amendment — *"No — cut it on filability. On-contract means the manager can paste it under the node's
headings, however far it departs. What it departs by becomes a flag at the gate. Reject-and-re-prompt is
reserved for a missing required part or a shape with no heading."* No `DIVERGENCE`.

One **manager note** travelled with the question, drawn only from context the manager already held: the
manager ran those six checker attempts itself and confirmed the worker's reading of the record, adding that
the fourth departure is what forced round 6 to give `PASS`/`FAIL` a `QUESTIONS:` companion — the contract
was amended *because* a worker went outside it, so the recommendation's own mechanism had already run once.

**Q2 — does anything hold a handover against the record of what the human said?**

The worker's `ASK`, verbatim: *"Before the manager files the handover of a worker that has talked to you
through the relay, does anything hold what it says against the record of what you actually said?"*

It reported Q1 as closing the mechanical half of this node and leaving the half the node's own text calls
dangerous — a return satisfying the shape while inventing content, which fileability cannot see because
such a return files perfectly. Its finding was that the exposure is **narrower than the node feared**: a
worker writes no graph file and the manager writes the human's words at relay time, so the record is the
manager's own text and no worker can forge an entry in it. What a worker can still do is write an `ANSWER`
resting on words the human never said. Its `RECOMMENDED` was the cheapest check available — the manager
holds the `ANSWER` against the `## Interview` it wrote itself, both texts already its own — with the
departure **flagged beside it rather than rejected**, matching Q1's answer. Three alternatives were set
aside: nothing at all, a blind second worker per relay-using node, and forbidding a handover from restating
the human's answers at all.

**A2 — the human took the recommendation.** `paraphrase`, the offered option as written and unamended —
*"Yes — the manager reads the handover's `ANSWER` against the `## Interview` it wrote itself. Anything
resting on words I didn't say is flagged beside it, not rejected. Both texts are already the manager's own,
so nothing is re-read and nothing is re-derived."* No `DIVERGENCE`.

Two **manager notes** travelled with it, both from context the manager held and neither an answer. That
**this node's own record is an instance of the hazard one level down**: both answers were given by taking
an option as the manager had written it, so this `## Interview` holds the human's decisions in the
*manager's* words — the record the proposed check reads against is already one remove from the human, and
the check catches a worker inventing their words but not a manager having supplied them. And the ordering
correction below, since the recommendation rests on when the write happens.

### Correction made mid-node: the write and the resume go together

Verbatim: *"maybe first restart the worker and then write the file, it might gain a bit of parralellism"*.

[Graph file format](13-graph-file-format.md)'s ordering requirement — carried into the shipped
[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md) as *"write the human's
answer into `## Interview` at relay time — the moment the human gives it, **before** the manager attempts to
resume the worker"* — was written assuming the resume blocks the manager. It does not: a resume is a
background send. So the manager now issues **the resume and the write in one turn**, and the worker thinks
while the record lands.

What the original rule protects is unchanged: the answer is still on disk before the worker can return, so a
worker that dies still leaves the human's words banked for a replacement attempt. What is lost is only the
word *before*. The remaining window is the manager dying between the two calls of a single turn, against
which the old order gave the same protection this one does — the manager could equally die between writing
and relaying, having banked an answer no worker ever received. **Eighth delta on the shipped conventions
document**, and the first correction to that document's text that came from the human watching the manager
work rather than from a node deciding something.

**Q3 — how many re-prompts in the narrow lane, and what happens when it stops?**

The worker's `ASK`, verbatim: *"In the narrow lane you kept — a required part missing, or a shape with no
heading — how many times does the manager re-prompt before it stops, and what happens when it stops?"*

Its `RECOMMENDED` was **once**, naming exactly which part is missing, with a second unfileable return
neither re-prompted again nor respawned: the manager files what it can, leaves the node `open`, and tells
the human once by node name — the notice a death already gets. Its argument against borrowing [Relay
protocol](08-relay-protocol.md)'s two-respawn cap is that the cap *"is two because replay re-inflates the
context that killed the previous attempt, and nothing is replayed here"* — the worker is alive, holds its
own context, and is being handed one line. Four alternatives were set aside: two re-prompts for symmetry,
no cap, zero, and respawning on the second failure.

**A3 — the human took the recommendation.** `paraphrase`, the offered option as written and unamended —
*"Once, then hand it to me. One re-prompt naming exactly which part is missing. A second failure is not
re-prompted or respawned: the manager files what it can, leaves the node open, and tells me once by node
name — the same notice a death gets."* No `DIVERGENCE`.

One **manager note** travelled with it, from context the worker did not hold: its reasoning assumes a live
worker is always **resumable**, which held twice on this node and does not always hold. At [Write the worker
contract skills](22-worker-contract-skills.md) the human stopped an attempt by accident and the harness
refused to resume it — *"was stopped by the user and won't be resumed. Treat its work as cancelled"* — so the
only route left was a fresh spawn carrying the established results as text, which is the respawn this answer
rules out. The note named three places that could go and did not decide between them.
