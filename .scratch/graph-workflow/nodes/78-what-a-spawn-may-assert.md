# Nothing bounds what a spawn may assert about the answer its node is meant to reach

Type: grilling
Status: claimed

## Question

A manager note is capped at **context the manager already holds** ([Relay protocol](08-relay-protocol.md)'s `F9`),
which bounds where the material comes from and **not what it may claim.**

**Measured twice, both against the manager.** [How an agent workflow and its skills reduce their own token
cost](52-token-cost-of-a-workflow.md)'s annotation records the manager writing an unestablished inference into node
68's `## Question` and into two spawns *"in each case as settled fact"*. [Review every shipped file against
`/writing-great-skills`](47-review-shipped-skills.md)'s annotation records four manager pointers travelling into
node 54's spawn and **all four coming back falsified.**

**And the two workers said the same thing independently, in their own retrospectives.** Node 69's: *"A spawn that
hands a worker the conclusion it is meant to test costs the worker the work of unpicking it."* Node 68's: *"A spawn
that asserts findings rather than pointing at sources costs a correction round when the assertion is stale."*

The manager's remedy in the node 54 case — instructing the worker to **treat manager material as evidence rather
than argument** — is its own invention and is written nowhere.

## What has to be decided

1. **Must a spawn mark what the manager asserts as evidence rather than as a settled fact?**
2. **Does the same bound reach a node's `## Question`**, which the manager also writes and which a worker reads as
   the frame for its own work? Node 52's annotation records an inference landing there as well as in the spawns.
3. **Is there anything a spawn may never assert at all — the conclusion the node exists to test?**

**Blockers: none.**

Reported by node 75's worker as item 177 of §Q2, *practice the manager adopted on its own authority*.

## Interview

#### Questions 1 and 2, relayed 2026-10-02

*Pasted as the worker handed it back.*

```
NODE:          What a spawn may assert (node 78)
ABOUT:         This node decides what limits a manager's spawn on what it may claim. Today the limit covers only where a note's material may come from, not whether its claims are true. It is being decided now because the manager's claims keep arriving wrong, and the manager has started improvising a "treat these as claims to check" line in its spawns.
SO FAR:        I read the node, map.md, the grilling contract, the manager contract's `## Spawning a worker` as it stands, the annotations on nodes 47, 52 and 69, and the evidence in nodes 66 and 67. Node 211 has no decisions.md line yet because it is still open.
               - The shipped manager contract says: "Write a note only from context you already hold. Do not read code, or go and find things out, in order to write one. A note may name the one of a worker's questions you believe is sharpest. It may not say what you think the answer is." So the third question this node asks ("may a spawn assert the conclusion?") is already settled for notes. That sentence has been there since the contract was first written (commit 4f9781b00, 2026-08-29).
               - Both of the node's original cases came before that contract existed. Node 68 was created on 2026-08-22 and node 54 on 2026-08-26.
               - The cases after the contract shipped are claims of fact, not claims about the answer. The cap does not reach them. One: the manager's spawn for node 66 called node 367 an instance, and node 66's worker found it was not. Two: this very spawn says node 67's handover called node 214 "claimed" and node 375 "open". The handover actually says 214 claimed and 375 claimed. At that commit (9213ad95a), 214 was open and 375 was resolved. So the worker was wrong, and the manager's retelling of the worker's error was also wrong.
               - What failed each time was a false or stale fact the manager honestly held. A limit on where a note's material comes from cannot catch that, and the manager cannot mark claims it does not know are wrong. The worker reading the note is the one party that can check.
               - Nothing in any worker contract says how to treat manager notes. Five contracts (grilling, research, prototype, precondition, implementation) share the sentence "Read each of the following. Do not trust any summary of them." That sentence covers the files the worker is told to read, not the notes.
               - Settled on my own authority (it will come back as an ASSUMPTION flag): the third question needs no new rule, because the shipped "It may not say what you think the answer is" already answers it for notes. The question of whether the same limit reaches a node's `## Question` is Q2 below.
               - Settled on my own authority: whatever rule ships covers only the manager's own material. A direction from the human, a permission the human granted, and an acceptance condition stay authoritative, because the manager contract already sets them apart from notes.

Q1. Whose job it is to catch a wrong claim
CONTEXT:       The node asks whether a spawn must mark what the manager asserts as evidence rather than settled fact. The recorded failures suggest the check works better on the reading side.
ASK:           Should the fix be a rule for the worker reading the spawn (check each claim in the manager's notes before relying on it), rather than a rule that the manager mark its claims?
RECOMMENDED:   Yes, a reader-side rule. Ship it by rewording the existing sentence in the five worker contracts, for example: "Read each of the following rather than any summary of them, and check each claim of fact in the manager's notes before you rely on it." That adds about 15 words per contract, with no new section and nothing added to the manager contract. It rests on the finding above: the manager cannot mark claims it does not know are wrong, and the worker can check them cheaply. This spawn's opening line already does this by hand, and it caught a wrong claim this time. Implementation spawns that carry "confirmed at <commit>" notes stay cheap to check, because the commit is given.
ALTERNATIVES:  Writer-side: the manager labels every assertion as a claim and gives its source. This costs more in every spawn, and it fails exactly when the manager believes the wrong claim.
               Both rules together: more text, and the writer-side half adds nothing the reader-side half does not already catch.
               No rule: the manager keeps improvising the line, and a spawn that leaves it out goes unchecked.

---

Q2. Does the same check reach a node's `## Question`
CONTEXT:       Node 52 records the manager writing an inference into node 68's `## Question` as settled fact. A worker reads its question as the frame for all its work, and nothing tells it to check the premises in that frame.
ASK:           Should the worker also check the claims of fact in its own node's `## Question` before relying on them, apart from text marked as the human's own words?
RECOMMENDED:   Yes, in the same sentence as Q1: "check each claim of fact in your node's `## Question` and in the manager's notes before you rely on it". It costs about six more words per contract. It rests on the node 68 case. A wrong premise in the question shapes every turn of the attempt, so it costs more than a wrong note. A question pasted from another worker's NEW NODES is the same kind of unverified claim.
ALTERNATIVES:  Notes only: the cheapest option, but it leaves out the recorded node 68 case.
               A writer-side rule in the manager contract against stating an inference as fact when it writes a question. This has the same weakness as Q1's writer-side option, because the manager does not know which of its inferences are wrong.

RETROSPECTIVE
1. What I had to hunt for: whether the shipped cap already answers the third question (it does, and I found that with git log -S). I also had to find the dates of the node 54 and 68 spawns to see whether the cap was in force then (it was not). And I had to find which worker contracts share the sentence a rule would edit.
2. What arrived that this node did not need: the decisions.md line for node 8. Its content is the same as the cap in the shipped manager contract. Node 211 has no decisions.md line, because it is open, so pointing me at its "line" sent me to the node file, which I needed only to see that it is a sibling rule.
3. What would have made this easier: the node's `## Question` saying that "It may not say what you think the answer is" already ships. That would have answered half the node before I started.
4. What was stale, wrong or contradictory: the manager's note says node 67's worker called node 375 "open". The handover says "node 375 (claimed)". At that commit, 214 was open and 375 was resolved. The node's Question cites the cap as "capped at context the manager already holds (node 8's F9)". The shipped wording is now "Write a note only from context you already hold", as the manager predicted.
```

*The manager's note:* the worker is right that the manager's spawn misquoted node 67's handover: it said node 375 "open" where the handover says "claimed".

#### The human's answer to questions 1 and 2, 2026-10-02

`verbatim`: *"ok"*

The manager had closed the payload with "Please answer Q1 and Q2. "ok for recommended" takes both." The reply "ok" names no alternative, so it takes the worker's `RECOMMENDED` on both. Q1, the worker's: "Yes, a reader-side rule. Ship it by rewording the existing sentence in the five worker contracts, for example: "Read each of the following rather than any summary of them, and check each claim of fact in the manager's notes before you rely on it."" Q2, the worker's: "Yes, in the same sentence as Q1: "check each claim of fact in your node's `## Question` and in the manager's notes before you rely on it"."
