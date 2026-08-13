# Human-initiated steering

Type: grilling
Status: open

## Question

How does the human say what they want to work on next, rather than only answering what they are handed?

Surfaced by [Relay protocol](08-relay-protocol.md). "Ask me later" turned out not to be a pause but an act of **prioritization** — in the human's own words, *"if I want to work on something else, if there is something more important."* Declining the question in front of them is only half of that act. The other half — saying what they want instead — has no mechanism anywhere in the graph.

This is the **inverse direction of the relay**, and the one direction the design has never specified. [Concurrency model](04-concurrency-model.md) sizes the HITL budget, [Relay protocol](08-relay-protocol.md) routes questions from subagent to human and back, but nothing lets the human reorder the frontier.

Open:

- Can the human **pull a specific node forward**, and what happens to the interviews already in flight — do they park, or finish first?
- Can the human ask **what is banked and waiting**? Parked nodes now carry answers they already paid for, and a deferral they cannot see again becomes invisible debt.
- Does the manager's node choice become a **recommendation** the human can override, or does it stay the manager's call with steering as an occasional interrupt?
- The relay streams questions in arrival order rather than an order the human chose (finding `F4`). Is steering the answer to that, or is question **batching** a separate mechanism — offer several at once and let the human pick which to answer?
- What stops steering from starving nodes the human finds dull but the destination needs?

Related but deliberately left in the map's fog: *how the human sees graph progress*. Steering is useless without a view to steer from, but the view is a presentation question and this is a control question.
