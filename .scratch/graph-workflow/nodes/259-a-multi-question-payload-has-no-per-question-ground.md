# A multi-question payload has no per-question place for what the question rests on

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [node 248](248-review-the-priority-list-and-decide-how-much-ships.md)'s worker, and pasted as it wrote
it.*

> The grilling contract's multi-question shape gives each question `ASK`, `RECOMMENDED` and `ALTERNATIVES`, and
> `SO FAR` is written once for the whole payload. A question resting on findings of its own has nowhere to put them,
> so they go into `ASK` and bury the question. This cost a measured human turn on node 248: the human read a long
> `ASK` and replied *"what do you propose ?"* when a recommendation was already written below it. Decide whether the
> shape gains a per-question field, or whether `ASK` is instructed to hold the question only.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The measured turn is real and the manager watched it happen.** The human's reply was `verbatim` *"Q1. … What do
you think about it ? For the rest ok Q2. what do you propose ?"*, and the worker's own next payload opens by naming
the cause: *"you asked 'what do you propose?' and I had already written a recommendation, which means it was not
findable. That is my error and worth naming: I put five paragraphs of findings inside the ASK field instead of
keeping it to the question, so the proposal sat behind a wall."*

**The manager relayed that payload unaltered, as it must**, so the burial reached the human through a channel that
cannot repair it. That is what makes this the contract's problem rather than one worker's.
