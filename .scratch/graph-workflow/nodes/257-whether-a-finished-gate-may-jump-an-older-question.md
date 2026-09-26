# Whether a finished gate may go ahead of an older tier 1 question

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 248](248-review-the-priority-list-and-decide-how-much-ships.md)'s worker, and pasted as it wrote
it.*

> The manager's contract names this collision and leaves it open: tier 1 is ordered by arrival, and a gate holds a
> code slot while it waits where a relayed question does not, so holding a gate behind an older question has a
> throughput cost the older question does not have. The priority list does not settle it — the list ranks classes of
> act, and this collision is inside one of them, item 4 — and the trigger file's "question/gate" phrasing does not
> separate them either. Decide whether a gate may jump an older tier 1 question, and on what test.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The reverse case happened this session and is not what this node is about.** The manager put a newer question
ahead of an older gate, which nothing in the contract leaves open; that is flag `242.3`, filed against the manager.
This node is the case the contract does leave open, and the two should not be run together.

## Answer

Arrival order stands inside tier 1: a finished gate waits behind an older raise like any tier 1 item. Only the human's one-time "the gate first" puts a gate first. The contract drops the conflict.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human's `"ok for 257"` is under `## Interview`. The fix is [node 323](323-state-that-a-finished-gate-waits-in-arrival-order-inside-tier-1.md).

## Interview

### Attempt 1

**Q1, from the worker**, pasted as it wrote it, 2026-09-26. Put to the human in the same turn.

```
NODE:          Whether a finished gate may jump an older question
ABOUT:         While a gate waits for your approval, it keeps one of this effort's two code slots occupied. The manager's contract states that the gate is queued in arrival order behind any older item in the first tier of the waiting queue. It also says nothing decides whether the gate may go ahead of them. This node decides that, so the manager stops having to judge it case by case.
SO FAR:        How the queue works (manager contract `.claude/skills/expedition/SKILL.md`, section "What is in front of the human, and when"): exactly one thing is in front of you at a time, and nothing displaces it. Everything else waits in two tiers. Tier 1 holds only three kinds of thing: a gate, a worker blocked on a raise, and the manager's own raise. Tier 2 holds a worker's interview question, relayed to you. Tier 1 goes before tier 2. Within each tier, the oldest goes first.
               The open conflict is still in the contract, in the section "Conflicts this contract leaves open": "Tier 1 is ordered by arrival. A waiting gate holds a code slot, and a relayed question does not. So a gate held behind an older question costs throughput. Nothing says whether a gate may go ahead of an older tier 1 question."
               I found that wording partly wrong, and I settled that myself; it will come back as an ASSUMPTION flag. A relayed question is in tier 2, so a gate already goes ahead of it. The only thing a gate can wait behind is an older raise. An implementation worker blocked on a raise also holds a code slot, which node 16 already recorded. So the gate is not the only tier 1 item that holds a slot. Everything in tier 1 stops something while it waits; that is how tier 1 was defined in the first place. The real difference is smaller: a gate holds a slot, while a raise from a non-implementation worker or from the manager does not.
               The cost is limited to the time you take to answer each older raise. This effort has two code slots, so a waiting gate leaves one free. You can already say "the gate first" whenever you want. That is a one-time steer the contract already provides.
               The manager's note from this session: gates for nodes 304 and 301 waited behind a raise of the manager's own. That is exactly this case. A gate also waited behind relayed questions (that one was most likely the live question). You answered each question and then approved each gate, with no sign of friction. That is one session, not a measurement.
               Node 248 said the priority list cannot settle this, because the conflict sits inside one of its items. The trigger file's line "if ... there is a question or a gate" does not separate them either.
ASK:           When a gate is ready and an older tier 1 item (a blocked worker's raise, or the manager's own raise) is waiting, may the gate go ahead of it? If so, on what test?
RECOMMENDED:   No. Arrival order stands inside tier 1. The contract then drops this conflict from its open list and says a gate waits in arrival order like the rest of tier 1, with "the gate first" as your override. Reasons: the cost is one answer's time per older raise, and raises are rare. The throughput argument applies just as much to an implementation worker's raise, so a gate-only exception would have no principle behind it. The rule stays one line. With two code slots, a waiting gate stalls nothing unless the other slot is also held. You already have the override, and one session of doing it this way caused no friction. If you agree, I will report an implementation node to make that edit to the manager contract.
ALTERNATIVES:  - A gate always goes ahead of older raises: a sub-tier above them. It is simple, but it treats the gate as the only thing blocking a code slot, and that is false.
               - Anything holding a code slot goes first: gates and implementation workers' raises go ahead of other raises. This follows the throughput reasoning, but it adds a second ordering rule inside tier 1.
               - A gate jumps only when no code slot is free: the cost exists only then. This is the most exact, but the manager has to check slot occupancy before every send, and that check could go wrong.
               - Leave it open: the manager keeps judging each case, which is the situation this node exists to end.
```

*The manager's note, 2026-09-26, sent to the human with Q1:* the spawn's note that "nodes 304 and 301 waited behind a question of mine", which Q1's `SO FAR` repeats, was wrong in part. Only node 304's gate waited behind the manager's own raise, the question of node 56's name. Node 301's gate waited behind node 304's gate, not behind a raise.

**A1, the human**, `verbatim`, 2026-09-26: *"ok for 257"*

This takes the option the worker offered as `RECOMMENDED`, in the worker's words: *"No. Arrival order stands inside tier 1. The contract then drops this conflict from its open list and says a gate waits in arrival order like the rest of tier 1, with "the gate first" as your override."*

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Whether a finished gate may jump an older question
ANSWER:        **No. Arrival order stands inside tier 1, and a finished gate waits behind an older tier 1 item like the other two kinds.** The human, `verbatim`, answering the question with its recommendation shown: *"ok for 257"*. The reply assents to the recommendation, so it is read as the human's own choice.

               **What was decided.** Inside tier 1, the oldest item is still sent first. A gate that is ready goes behind an older blocked worker's raise, or an older raise of the manager's own. It gets no sub-tier and no exception based on code slots. The human is the only one who can put a gate first, by asking for it (*"the gate first"*). That request is used once and then lapses. The manager never reorders tier 1 on its own judgement. The manager's contract drops this conflict from its list of conflicts it leaves open. The queue section says that a gate waits in arrival order, and names the human's override.

               **What it rests on.**
               - The cost is small. It is the time the human takes to answer each older raise, and raises are rare.
               - A gate is not the only tier 1 item that holds a code slot while it waits. An implementation worker blocked on a raise holds one too, as node 16 already recorded. So an exception for gates alone has no principle behind it.
               - Every tier 1 item stops something while it waits. That is the test that defined tier 1.
               - This effort has two code slots, so a waiting gate stops no code work unless the other slot is also held.
               - The one-line rule stays one line.
               - In one session this was the practice and caused no friction. Node 304's gate waited behind the manager's own raise (the question of node 56's name). Node 301's gate waited behind node 304's gate. The human answered and approved each, with no sign of friction. That is one session, not a measurement.

               **The contract's own statement of the conflict was partly wrong.** It said a waiting gate holds a code slot and "a relayed question does not". But a relayed question is in tier 2, so a gate already goes ahead of it. Inside tier 1, the only thing a gate can wait behind is an older raise.

               **Options set aside:**
               - A gate always goes ahead of older raises.
               - Anything holding a code slot goes first.
               - A gate goes first only when no code slot is free.
               - Leave the conflict open.
INDEX LINE:    Arrival order stands inside tier 1: a finished gate waits behind an older raise like any tier 1 item. Only the human's one-time "the gate first" puts a gate first. The contract drops the conflict.
FLAGS:         ASSUMPTION: The contract's wording of the conflict was taken as partly wrong and was not asked about. It compared a gate with a relayed question, which is tier 2 and already goes behind a gate. Inside tier 1 the real comparison is with raises, and an implementation worker's raise also holds a code slot (node 16's annotation). The question was put to the human in those corrected terms. The new node's condition removes the old wording rather than repairing it.
               Index: The contract said a waiting gate was unlike a relayed question, but only raises share tier 1 with a gate, and one of those also holds a code slot; node 257 was framed on that correction.

               ASSUMPTION: I treated the human's override *"the gate first"* as an existing one-time steer. Node 16's answer names it as one ("A named node — "node 12 next", "the gate first" — is one pick"). The shipped contract only says "A named node is one pick", and it says so about picking nodes, not about the queue. So the new node's condition states the override in the queue section rather than leaving it implied.
               Index: The one-time "the gate first" override comes from node 16's answer but was never stated for the queue in the shipped contract, so node 257's follow-up states it there.
NEW NODES:     Name: State that a finished gate waits in arrival order inside tier 1
               Kind: implementation
               Question: Carry node 257's decision into the manager's contract. Inside tier 1, a gate waits in arrival order behind older items. Only the human's one-time request puts a gate first. The conflict comes off the list of conflicts left open.
               Blockers: none, beyond node 257 being resolved.
               Acceptance condition: The file `.claude/skills/expedition/SKILL.md` is changed as follows, and no other file is changed.
               (1) Under the heading `## Conflicts this contract leaves open`, the bullet that begins "Arrival order against the cost of a waiting gate." is gone entirely. That bullet includes the sentences "A waiting gate holds a code slot, and a relayed question does not." and "Nothing says whether a gate may go ahead of an older tier 1 question." The other two bullets in that section are unchanged. The section's opening paragraph still reads true of what remains.
               (2) Under the heading `## What is in front of the human, and when`, the text near the tier 1 list states two things in plain words. First, a gate waits in arrival order like the other two kinds in tier 1. A finished gate is sent after any older tier 1 item, such as an older blocked worker's raise or an older raise of the manager's own, and the manager never moves a gate ahead on its own judgement, for example because the gate holds a code slot. Second, the human may ask for a waiting gate to be sent first. That request applies once and lapses once used.
               (3) The existing rules in that section still hold as written: tier 1 holds exactly three kinds of thing, tier 1 goes ahead of tier 2, nothing displaces a live question, and the manager never asks the human which waiting thing to take next. Nothing added contradicts any of them.
               (4) No sentence anywhere in the file still says the ordering of a gate against an older tier 1 item is unsettled or left open.
INVALIDATIONS: none. Node 16's answer set tier 1 in arrival order. This node confirms that and does not contradict it. It settles the question node 16's annotation said "This node still owes that". Node 16's early claim that the gate is the only item holding the code slot was already corrected by node 16's own later annotation.

RETROSPECTIVE (effort-scoped)
(1) What I had to hunt for.
- Whether the conflict still stood after the plain-English rewrite. I looked first in `## What is in front of the human, and when`, as the spawn pointed. It is not there. It is in `## Conflicts this contract leaves open`, about 140 lines further down the same file, and I found it by grepping for "slot|collision|arrival".
- The slot count. `map.md` strikes out its old location. The live figure is in `map-manager-only.md`, line 59.
- The fact that a blocked implementation worker also holds a slot. It is only in an annotation on `nodes/16-human-steering.md`, which I found by grepping decisions.md for tier/gate/queue and then reading node 16.
(2) What arrived that this node did not need. The git status snapshot in the harness context listed dozens of modified node files. Most of what the decisions.md grep matched was irrelevant: the words gate and slot appear everywhere. A pointer in the node file to node 16 and to the contract section would have made both searches unnecessary.
(3) What would have made it easier.
- The spawn or the node file naming the contract section `## Conflicts this contract leaves open` as the place the conflict now lives.
- The node file linking node 16. It is where the conflict was first raised ("This node still owes that"), and the node's question, pasted from node 248, doesn't mention it.
- Node 16's decisions.md index line saying it left gate ordering inside tier 1 open.
(4) What was stale, wrong or contradictory.
- The contract's conflict bullet compares a gate with "a relayed question", which is tier 2. That is the wrong comparison for a conflict inside tier 1.
- Node 16's main paragraph says the gate is "the only claimant holding the code slot". Its own later annotation contradicts that.
- The spawn's note that node 301's gate waited behind a raise was wrong. The manager corrected it: that gate waited behind node 304's gate.
- The node file's heading ("...may go ahead of an older tier 1 question") differs from the name the spawn used ("...may jump an older question").
- The trigger file's third bullet ("there is a question or a gate") still does not separate the two. That is harmless once arrival order is the rule, so I proposed no change to it.

Skipped parts of a method skill: none; no method skill was invoked.

## Flags

`257.1` **· settled** `ASSUMPTION` — The contract's wording of the conflict was taken as partly wrong and was not asked about. It compared a gate with a relayed question, which is tier 2 and already goes behind a gate. Inside tier 1 the real comparison is with raises, and an implementation worker's raise also holds a code slot (node 16's annotation). The question was put to the human in those corrected terms. The new node's condition removes the old wording rather than repairing it.

`257.2` **· settled** `ASSUMPTION` — I treated the human's override *"the gate first"* as an existing one-time steer. Node 16's answer names it as one ("A named node — "node 12 next", "the gate first" — is one pick"). The shipped contract only says "A named node is one pick", and it says so about picking nodes, not about the queue. So the new node's condition states the override in the queue section rather than leaving it implied.
