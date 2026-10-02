# What an implementer does with a checker finding it believes is false

Type: grilling
Status: claimed

## Question

The checker's findings reach the implementation worker through the manager, and the shipped contract gives
the worker no discretion over them: it fixes all of them. **Nothing says what it does with one it believes is
wrong.**

Raised by the human at [Whether a spawn may override a shipped worker
contract](28-spawn-overriding-a-contract.md)'s close, on reading that node's answer, in their own words:
*"for the checker, when it does the review, the review gets sent to the implementor and then he can either
fix or not (flag ?) ?"* — and, on being shown that the contract closes the flag route: *"I think we need
something."*

### What is shipped today

[`expedition-implementation/SKILL.md`](../../../.claude/skills/expedition-implementation/SKILL.md) lines
136–152 fix the loop and close the third route by name:

```
you finish the code
    → the checker checks it → you fix everything it found → the checker runs again
    → the manager raises the gate
        → approve → the manager commits; your node resolves
        → correct → you fix; the manager raises the gate again      (uncapped)
        → reject  → you are finished; nothing you wrote is kept
```

> *"What reaches you is what it found, and **you fix all of it before the gate**."*

The one escape is **size, not disagreement**: *"Where fixing one of its findings would be a piece of work
rather than a repair, raise it instead… **do not carry the finding past the gate unfixed on your own
authority**."* That last clause is exactly the flag route, named and forbidden — and rightly, on what a flag
is: a flag does not block, so flagging a finding would let unfixed work reach the human as a footnote rather
than as a decision.

**Flags exist in this loop for the opposite direction.** They are the worker's own judgements, read by the
human at the gate, and line 158 inverts it: *"A flag of yours that the human disagrees with arrives as a
correction round."* Judgements flow worker → human; findings flow checker → worker, and the worker has no
say.

### None of the three raise triggers fits

| trigger | a finding the worker believes is false |
| --- | --- |
| the broken thing is not yours to change — the condition, an upstream resolved node, the size of your node | no: the finding is about the worker's own code |
| the decision reaches past this node's own code | no |
| a genuine fork where you hold **no recommendation you believe** | no — the worker holds one exactly: *this finding is false* |

So a worker convinced a finding is mistaken must either **edit code that is not broken**, or depart from its
contract. There is no third thing.

### Why it may be deliberate rather than a defect

The protection against a false finding sits **upstream**, in
[`expedition-checker/SKILL.md`](../../../.claude/skills/expedition-checker/SKILL.md)'s hard rule 2: *"You
check against what you were given and never against your own preference. A property nobody stated is not a
finding."* Constrain what counts as a finding and no downstream veto is needed. The answer has to say whether
that is enough — and it is untested, because **the checker has never been overruled, nothing being able to
overrule it.**

### Three things the answer must account for

**The manager cannot arbitrate.** [Subagent context contract](12-subagent-context-contract.md) made it a
**scribe**, and [Relay protocol](08-relay-protocol.md) fixes that the manager never answers anything. So a
worker-versus-checker disagreement has exactly one possible referee, the human, and every candidate route
therefore ends at a raise or at the gate.

**The concrete harm is a wrong fix shipping quietly.** The worker edits to satisfy a false finding, the
checker re-checks and passes because its finding was addressed, and the diff carries a change nobody wanted.
Partially mitigated already: `GATE PAYLOAD` requires *"for each thing the checker found, what you changed"*,
so the human sees finding-and-change pairs — but never *"I made this change and I think it was unnecessary."*

**It is the mirror of a hole already recorded on the other side.** [What the checker contract owes to having
been run](31-checker-contract-owes.md) item 2 records the checker having no route for *the condition is bad
and the work complies with it* — checkable, complied with, and complying produced the defect. It invented one
live: it handed the observation back as a **question alongside its `PASS`**, and the human took it. **Both
ends of the check loop lack a way to say *the other party is wrong*.** One end improvised a channel; this end
has never had to. Whether the two want the same shape of answer is this node's to say — a shared shape is
cheaper and a forced symmetry is a trap.

### Candidate routes, none of them decided

- **Nothing changes.** Rule 2 is the protection; the worker fixes it and the gate is where a human notices.
- **A fourth raise trigger** — *a finding you believe is false*. Blocking, costs the code slot and human
  attention, and the human arbitrates once.
- **A rebuttal back to the checker**, through the manager, with the checker adjudicating its own finding.
  Cheapest in human attention and the only route that does not spend the scarce resource — but it needs the
  checker's contract to accept one, and a checker that re-reads its own finding is no longer independent of
  it.
- **Reopen the flag route deliberately**, for this case alone: the work reaches the gate with the finding
  unfixed and marked as disputed. This is what the contract forbids today, so taking it means saying why the
  prohibition was too wide.

One thing already on the record that any answer has to sit beside: [Human review of landed
code](20-human-code-review.md) carries an **outstanding** flag that *"a checker that will not pass still
reaches the gate, qualifying the human's statement that its findings are fixed first"*. So *fix all of it*
already has one acknowledged exception, and it is unsettled.

Feeds [`expedition-implementation/SKILL.md`](../../../.claude/skills/expedition-implementation/SKILL.md),
possibly [`expedition-checker/SKILL.md`](../../../.claude/skills/expedition-checker/SKILL.md), and the
**manager's own skill**, which carries the findings between the two and may not answer either of them.

*The manager's note, 2026-09-28:* [node 353](353-whether-implementer-becomes-a-glossary-headword.md)'s worker reports this node's question changed. Its words, pasted: Node 34 (open, grilling): a term is renamed in its title, "What an implementer does with a checker finding it believes is false". Its body already says "implementation worker". The shipped line it concerns (`.claude/skills/expedition/SKILL.md:830`) will read "a worker" or "the implementation worker" once the rename node lands. The title is record text and stays as it is under never-delete.

*The manager's note, 2026-09-28:* [node 162](162-how-much-of-the-integration-rule-ships.md)'s worker reports this node's question changed. Its words, pasted: **Node 34** (open, grilling) quotes the implementation contract's diagram, including `→ approve → the manager commits; your node resolves`, under "What is shipped today". Once the new node lands, that quotation is out of date. Its question, about a finding the implementer believes is false, is unchanged in substance.

## Interview

#### Questions 1 and 2, relayed 2026-09-29

*Pasted as the worker handed it back.*

```
NODE:          What an implementer does with a checker finding it believes is false (node 34)
ABOUT:         The implementation contract says the worker fixes every checker finding. It gives the worker no way to say a finding is wrong. You asked for "something" at node 28's close. This node decides what that is.
SO FAR:        I read the node, map.md, the decisions.md lines for nodes 28, 160, 162 and 363, and the shipped contracts as they stand now.
               - Implementation contract, `## After the code is written`: "Fix all of it before the gate." and "Never leave the finding unfixed at the gate on your own authority." The only exception is a fix that would be a new piece of work, which is raised under trigger 1. The GATE PAYLOAD part reads "for each thing the checker found, what you changed".
               - The manager contract already names the referee. Its table of things that are never the manager's has the row "deciding between a worker and its checker | put that disagreement to the human, who alone settles it". `## The gate` already lets the manager raise a gate on a failing tree ("a check that will not pass"). Item 3 of `## What nothing here settles` lists this exact gap as open. So the human referee and the failing-tree gate both exist already. The only missing piece is the worker being allowed to leave a finding unfixed and say why.
               - The checker's side of this (node 31 item 2) has already shipped. Its row "you can check it, the work complies, and complying is what produces the defect" hands back "your outcome, and a question". So the checker disagrees in its own report, and the manager carries that report to the gate. The same pattern fits the worker, without a new channel.
               - Manager's note: in practice this session, a worker that disagreed said so in its correction-round handover, and the manager put it to you at the gate. My recommendation writes that practice down.
               - Settled on my own authority: the checker still runs again after the other findings are fixed. It will fail again on the disputed finding, and that FAIL is the expected "check that will not pass" case. The checker contract is left unchanged.

Q1. Which route
ASK:           When the worker believes a checker finding is false, what does it do?
RECOMMENDED:   It leaves that finding unfixed and says in GATE PAYLOAD why it believes the finding is false. You settle it at the gate, and if you uphold the finding it comes back to the worker as a correction round. The shipped edits are small and remove text overall:
               (a) Implementation contract, `## After the code is written`, becomes: "Fix all of it before the gate, except a finding you believe is false. Leave that one unfixed and say why in `GATE PAYLOAD`. The human settles it at the gate, and a finding they uphold arrives as a correction round. Leave no other finding unfixed on your own authority." The diagram's "you fix everything it found" becomes "you fix what it found".
               (b) GATE PAYLOAD part: "for each thing the checker found, what you changed, or why you left it unfixed".
               (c) Manager contract, `### The payload`: "What the worker changed for each thing the checker found, or why it left it unfixed, in the worker's own words." Delete item 3 of `## What nothing here settles`. No other file cites it by number, which I checked by search.
               This adds about 2 lines to the implementation contract and removes about 4 from the manager contract. Your attention is spent only at a gate you would review anyway. It also removes the harm the node names, a wrong fix shipping quietly: the finding reaches you as a decision you make at the gate rather than a footnote.
ALTERNATIVES:  - Nothing changes: the checker contract's hard rule 2 ("A property nobody stated is not a finding") is the only protection, and a worker still edits code that is not broken.
               - A fourth raise trigger: blocks mid-node and holds the code slot so you can decide something the gate would show you anyway.
               - A rebuttal sent back to the checker: needs new text in the checker contract, and a checker ruling on its own finding is not independent of it.
               - A flag for the disputed finding: a flag does not block, so the dispute would reach you as a footnote, which is why the contract forbids it today.

---

Q2. Scope
ASK:           Does this go into the shipped skill files, or stay a rule for this effort only?
RECOMMENDED:   Shipped files, as edits (a) to (c). The gap is in the contracts themselves, and the manager contract already lists it as open. This does not depend on Q1's answer: whichever route you choose, you still have to say where it goes.
ALTERNATIVES:  - This effort's map only: the next effort starts with the gap back in place, and manager item 3 stays.
```

#### The human's answer to questions 1 and 2, 2026-10-02

`verbatim`: *"ok"*

The manager had put the questions with the line "Please answer node 34's Q1 and Q2: a disputed finding is left unfixed with the reason in the gate payload, and that ships in the contracts. "ok for recommended" takes both." So the reply takes the worker's `RECOMMENDED` on both: the worker leaves a finding it believes false unfixed and says why in `GATE PAYLOAD`, the human settles it at the gate, and the change ships as the worker's edits (a) to (c) in the shipped contracts.
