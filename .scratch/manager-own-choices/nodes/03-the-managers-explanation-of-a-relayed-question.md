# What the manager may say when the human asks it to explain a relayed question

Type: grilling
Status: resolved
Deliverable: explain-a-relayed-question

## Question

*Written by the manager.* Settling this keeps a manager's explanation of a worker's question from
carrying claims the worker never made.

GitHub issue 1, saved in [issue-1.md](../issue-1.md), gives example 7: the human asked the manager to
explain a worker's question, and the explanation added a false claim the worker had not made, which
cost three rounds. The glossary's **Manager note** is "drawn only from context it already holds", and
its **Relay** says the manager "answers nothing itself". The issue says these leave open which side of
that line an explanation falls on. Its proposed change 6 is that the manager quotes the worker's own
words or sends the request back to the worker, and writes no explanation that adds claims.

What should the workflow say the manager does when the human asks it to explain a relayed question, or
anything else an agent wrote? Which shipped files change? Check first that the glossary entries the
issue cites still read that way at the current `HEAD`.

## Answer

The worker's answer, as it wrote it:

When the human asks the manager to explain something an agent wrote, the manager answers with quotes only, and sends to the agent anything that needs the agent's meaning. Worker contracts gain a reply row for a request to explain.

**The manager's rule.** The human took payload 1's Q1 `RECOMMENDED`:
- What an agent meant belongs to that agent.
- The manager may quote the agent's own words. It may also quote passages of the files the workflow ships, of the effort's record, or of the human's own words. Each quote says where it comes from.
- The manager adds no claim of its own. It gives no reading of what the agent meant, no example it made up, and no conclusion drawn from what it quoted.
- The manager may open a shipped file or the effort's record to find a passage to quote. It reads no code and runs nothing in order to explain.
- Where no quote answers the request, the manager sends the human's words to the agent that wrote the text, and relays what that agent hands back.
The rule covers anything an agent wrote, such as a relayed question, a flag or a checker's finding. It is stated as a principle, with no steps listed for particular cases.

**The worker's side.** The human took payload 1's Q2 `RECOMMENDED`. The table under `### When the answer is not an answer` in the grilling, precondition and prototype contracts gains one row. In it, a worker asked to explain something answers in the `SO FAR` of what it hands back next, then asks the same question again. In the grilling contract the question keeps its number. The other two contracts number no questions, so their row leaves the number out (flag 03.d). The implementation contract has no such table and is left alone.

**Where the rule is written.** It goes in a new subsection of `## What is in front of the human, and when` in `.claude/skills/expedition/SKILL.md`, placed directly before `### Picking the next node` (flag 03.a). No other part of the manager contract changes. The glossary, the opening paragraphs of the worker contracts and the checker contract also stay as they are. The work lands on deliverable `explain-a-relayed-question`, as the human directed: *"That lands as a separate deliverable."*

**Left unwritten.** There is no rule on how an explanation is recorded on the node (flag 03.b), and no change to the checker contract (flag 03.c).

**INVALIDATIONS, as the worker wrote it:** None of the resolved nodes is contradicted. Two notes: Node 01's answer, as node 07 writes it, says the manager "reads nothing and runs nothing" to find information it hands back to an agent. This node lets the manager open a shipped file or the record to find a passage it quotes to the human. The two rules cover opposite directions and do not conflict, but a reader may want them set side by side. Node 02's `## Interview` records the manager giving "made-up scenarios" and setting the human's reading against the worker's recommendation. Both are now outside the rule. Node 02's answer is unchanged.

**CONDITIONS, as the worker wrote it:** **What I searched for.** In the `## Acceptance condition` and `## Question` sections of the open nodes 05, 06, 07 and 08, and in the `## Answer` sections of the resolved node 02 and the superseded node 04, I searched for `explain`, `Manager note`, `When the answer is not an answer`, `What is in front of the human`, `The last line of a report`, `Picking the next node` and `Two things the human can say`. **What matched.** Node 07 clause 1k names `## What is in front of the human, and when` only as a reference, and node 07's own work adds a short paragraph inside that section's body. The new subsection is placed after `### The last line of a report`, so the two deliverables do not touch the same lines. Node 07's clause 12 is unaffected. Node 06's clauses 3 and 4 stay right, because this work leaves `### Two things the human can say that are not answers` unchanged. Nodes 05 and 08 had no match. No clause needs replacing, and no open node's question changes. This node's own `## Question` quotes the **Relay** entry's "answers nothing itself", which node 07 changes. That quote goes out of date once node 07 lands, and it is historical text on a resolved node.

**MISSING FROM MAP, as the worker wrote it:** The map does not list the effort's deliverables, or which open node edits which shipped sections. I needed both to place the work where it would not conflict with node 07. I got them from node 07's acceptance condition and from the diff in its worktree, `.scratch/manager-own-choices/worktrees/07-own-choices-rule`, against `d49b11e`.

*Manager's note:* the worker's proposed node is [node 09](09-write-the-rule-for-explaining-what-an-agent-wrote.md). The worker labelled its flags 03.a to 03.d. They are filed as `03.1` to `03.4`, in that order.

## Flags

`03.1` `ASSUMPTION` **· settled** — (the worker's 03.a) I placed the manager's rule in a new subsection of `## What is in front of the human, and when`, directly before `### Picking the next node`, and in none of the places the issue or the first payload named. Three constraints decided the place: Node 06's condition requires the heading `### Two things the human can say that are not answers` to stay unchanged, and adding a third thing there would make "Two" false. Node 07, on the separate deliverable `own-choices`, edits the glossary's **Relay** entry, two rows of `## What is never yours`, the opening paragraph of each worker contract, and a paragraph near the end of the body of `## What is in front of the human, and when`. Edits in those places would conflict when the two pull requests are integrated. I checked node 07's diff in its worktree to place the new subsection away from its changes. The glossary needs no change. "Explanation" is plain English, and the new rule does not use the term **Manager note**. So the line the issue said the glossary leaves open is now drawn in the manager contract itself. The human was not asked, because the place follows from these constraints and the human asked that only what the issue needs be put to them.

`03.2` `ASSUMPTION` **· settled** — (the worker's 03.b) I wrote no rule for how the manager records an explanation on the node. The issue does not ask for one, and the human asked for no question beyond the issue. Because an explanation is now made of quotes only, the manager can record it in its own marked note naming the passages quoted, as it already did on nodes 02 and 03 under the existing scribe rule. If an explanation that nobody can see turns out to cause trouble, that is a later node.

`03.3` `ASSUMPTION` **· settled** — (the worker's 03.c) I changed nothing in the checker contract. Under the rule, a request about a checker's finding goes back to the checker. How a checker answers it is left to the manager, as the human's note on the fix in issue 1 asks for cases nobody specified.

`03.4` `ASSUMPTION` **· settled** — (the worker's 03.d) The human took Q2's row as "explain it in your next payload's `SO FAR`, then ask the same question again under its number". The precondition and prototype contracts ask one unnumbered question at a time, so their row leaves out "under its number" and says "in the `SO FAR` of the question you hand back next". The grilling row is as the human took it.

## Interview

### Attempt 1

#### Payload 1, as the worker handed it back

```
NODE:          What the manager may say when the human asks it to explain a relayed question

ABOUT:         This node decides what the manager does when the human asks it to explain a question a worker relayed, or anything else an agent wrote. It is decided now because GitHub issue 1, example 7, reports a case where the manager's explanation added a false claim the worker never made, and that cost three rounds. The issue's proposed change 6 is that the manager either quotes the worker's own words or sends the request back to the worker.

SO FAR:        I read the node, the map, issue-1.md, the glossary's `## Talking to the human`, the relevant sections of the manager contract (`.claude/skills/expedition/SKILL.md`), the not-an-answer tables in the worker contracts, and nodes 01, 02 and 06.
               **The issue's quotes still hold at `HEAD` `d49b11e`.**
               - The glossary's **Relay** still ends: "The manager passes the questions and the answers along unaltered, and answers nothing itself."
               - Its **Manager note** still reads: "The manager's own annotation on a relayed question, drawn only from context it already holds."
               - The opening paragraph of each worker contract repeats the relay sentence.
               **No shipped file says what the manager does when the human asks for an explanation.** These rules come closest:
               - The `## What is never yours` row "re-authoring what an agent wrote" says to "paste it, and put your own words beside it as your own marked note". It limits nothing about what those words may claim.
               - The rule for spawn notes says "Write a note only from context you already hold" and "It may not say what you think the answer is". It covers spawns only.
               - `### Two things the human can say that are not answers` sends a "you decide" and a reframing back to the worker. It says nothing about a request to explain.
               **Node 02 is a live instance.** Counted on 2026-11-12, for scale only, not authoritative: the human asked the manager to explain 7 times on payload 1's Q1 before reframing it, and twice more on payload 2. The manager answered every one of them itself. Its notes on the node say it answered from shipped files and from the worker's own words. Twice it went past quoting: once it "set the human's reading against the worker's recommendation", and once it "gave one made-up scenario per marker". The explanations themselves were not recorded, so nobody can now check whether any of them added a claim. The reframing went back to the worker, and the worker's payload 2 said its own payload-1 wording "was too broad". None of the manager's 7 explanations had brought that to light.
               **How this node relates to nodes 01 and 06.**
               - Node 01's Q2, still unanswered, covers the other direction: the manager handing an agent information the agent is missing. This node does not depend on it.
               - Node 06 (open) writes into `### Two things the human can say that are not answers`. Its condition requires that section's heading to stay unchanged and no other part of `SKILL.md` to change. Putting this rule in that section would conflict with node 06 and would make the heading's "Two" wrong.
               **Held for later payloads, because their answers depend on Q1:**
               - where the rule is written and which shipped files change, given the clash with node 06;
               - how an explanation is recorded on the node (an explanation made only of quotes can be recorded by naming the passages it quoted, while one in the manager's own words would have to be pasted in full);
               - what a checker does when it is asked to explain a finding at the gate.

Q1. What the manager may put in an explanation
CONTEXT:       This is the core of the node. The other questions depend on it.
ASK:           When the human asks the manager to explain something an agent wrote, may the manager answer only with quoted text and where it comes from, and send everything else back to the agent that wrote it?
RECOMMENDED:   Yes. The rule would be:
               - What an agent meant belongs to that agent.
               - The manager may quote the agent's own words. It may also quote passages from the shipped files, from the effort's record, or from the human's own words. Each quote says where it comes from.
               - The manager adds no claim of its own. It gives no reading of what the agent meant, no example it made up, and no conclusion drawn from what it quoted.
               - The manager may open a shipped file or the record to find the passage to quote. It reads no code and runs nothing in order to explain.
               - Where no quote answers the request, the manager sends the human's words to the agent that wrote the text, and relays what that agent hands back.
               Two things support this:
               - Example 7's false claim was an inference of the manager's. A quote with its source can be checked, and an inference cannot.
               - On node 02, quotes answered the factual questions well, such as which markers a flag can have. The questions about what Q1 meant, and the request for a scenario, needed the worker's own reasoning. Under this rule they would have gone to the worker at the first request, not after 7 explanations by the manager.
               The cost: the human waits for a worker round whenever they ask what an agent meant, where today the manager answers at once.
ALTERNATIVES:  - The issue's literal change 6, quoting only the agent's own words: a factual question about the workflow, such as which markers exist, would then also cost a worker round.
               - The recommended rule, but quoting only what is already in the manager's context and reading nothing, as the **Manager note** entry's "drawn only from context it already holds" suggests: fewer factual questions would be answered at once, but no claim would be added either way.
               - Let the manager explain in its own words, marked as its own and with a source for each claim: this is what produced example 7.

---

Q2. What a worker does when the human's reply asks it to explain
CONTEXT:       Every option in Q1 sends some requests back to the worker, and today's rule already does that for a reframing. Nothing in the worker contracts tells a worker what such a reply means, and the reply rules say "A reply naming a question ... settles what it names". So a reply like "Q1 I agree in principle ... can you please explain further?" could be read as an answer.
ASK:           Should the not-an-answer tables in the worker contracts gain a row saying that a request to explain gets an explanation in the next payload, with the same question asked again?
RECOMMENDED:   Yes. Add one row to `### When the answer is not an answer` in the grilling, precondition and prototype contracts: "explain X | explain it in your next payload's `SO FAR`, then ask the same question again under its number". The implementation contract has no such table, so it is left alone. This settles nothing new. It records what node 01's worker already did without being told, when it answered the human's question about example 2a in its payload 2, and it stops a worker from reading a request to explain as assent.
ALTERNATIVES:  - No row, and leave it to each worker's judgement: node 01 shows a worker can get it right, but the reply rules as written point the other way.
               - A row in the grilling contract only: precondition and prototype workers relay questions too, and would be left without the rule.

What is expected of you: answer Q1 and Q2.
```

#### The human on payload 1, Q1 and Q2, 2026-11-12 — `verbatim`

*"Q1 & Q2 what's the current behavior ?"*

*Manager's note:* the manager answered with quotes only, from the worker's own `SO FAR` and `CONTEXT` in payload 1.

#### The human on payload 1, Q1 and Q2, 2026-11-12 — `verbatim`

*"then aren't those questions again out of topic?"*

*Manager's note:* the manager answered from the issue's own text: Q1 is the issue's proposed change 6 and example 7; Q2 is not in the issue. It said that its own question for this node widened Q1 with "or anything else an agent wrote".

#### The human on payload 1, Q1 and Q2, 2026-11-12 — `verbatim`

*"ah, then yes to 1 and 2. That lands as a separate deliverable."*

The options this takes, payload 1's Q1 and Q2 `RECOMMENDED`, as the worker wrote them: Q1, "Yes. The rule would be: What an agent meant belongs to that agent. The manager may quote the agent's own words. It may also quote passages from the shipped files, from the effort's record, or from the human's own words. Each quote says where it comes from. The manager adds no claim of its own…"; Q2, "Yes. Add one row to `### When the answer is not an answer` in the grilling, precondition and prototype contracts…".

## Annotation: node 10 narrows the explain rule to what the manager already holds

As the worker of [node 10](10-explain-only-from-what-the-manager-already-holds.md) wrote it: Node 03 (`03-the-managers-explanation-of-a-relayed-question.md`): its answer says "The manager may open a shipped file or the effort's record to find a passage to quote." This is now narrowed: the manager opens no file and quotes only what is already in its context.

## Annotation: node 11 lets the manager explain in its own words

As the worker of [node 11](11-explain-in-own-words-without-inventing.md) wrote it: Node 03: contradicted on its "only quotes ... adds no claim" part. The send-back-to-the-agent part still stands.
