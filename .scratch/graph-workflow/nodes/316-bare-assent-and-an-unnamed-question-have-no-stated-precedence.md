# Bare assent and an unnamed question have no stated precedence in the grilling contract

Type: grilling
Status: resolved
Blocked by: none

## Question

*Promoted by the manager from [node 291](291-rewrite-the-grilling-contract.md)'s retrospective, the worker's own words:* "A pre-existing tension, kept as it was. Under "What a reply settles", bare assent names no question yet settles every recommendation, while the next rule says a question the reply does not name stays unanswered. Only the order of the bullets implies that the assent rule wins. A later node may want to state the precedence."

Where the human replies with bare assent such as *"ok for recommended"*, does it settle the recommended option of every question in the payload, including questions the reply does not name, and should `.claude/skills/expedition-grilling/SKILL.md` say so?

## Answer

A bare assent settles every recommendation in the payload, as node 117 fixed; the grilling contract's unnamed-question bullet gains an opening exception stating that precedence outright.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human's `"ok for 316"` is under `## Interview`. The fix is [node 322](322-state-the-bare-assent-exception-in-the-grilling-contracts-unnamed-question-rule.md).

## Interview

### Attempt 1

**Q1, from the worker**, pasted as it wrote it, 2026-09-25. **Held, not yet put to the human**: it arrived while [node 311](311-may-the-human-amend-a-held-nodes-condition-of-their-own-accord.md)'s question was in front of the human.

```
NODE:          Bare assent and an unnamed question have no stated precedence in the grilling contract (node 316)
ABOUT:         The grilling contract has two rules about what a reply settles, and read literally they contradict each other when the reply is a bare "ok for recommended". This node decides whether to fix the wording. It comes from node 291's retrospective: node 291 rewrote this contract and kept the tension as it was.
SO FAR:        The shipped text is `.claude/skills/expedition-grilling/SKILL.md`, lines 159-164, under "What a reply settles". Bullet 2 says that a reply assenting to the recommendation "without naming any question", such as "ok for recommended", settles every question's recommendation in the payload. Bullet 3 says: "A question the reply does not name stays unanswered ... Never read an unnamed question as assent." A bare assent names no question, so bullet 3 read literally leaves every question unanswered, and bullet 2 settles them all. Only the order of the bullets suggests that bullet 2 wins.
               The substance is already yours. At node 117 you answered, verbatim: "ok for recommened says ok for everything but in practice it is unlikely I say it I think, as I will create my message one question at a time, so it will be more Q1 ok Q2 ok Q3 ..". So a bare assent settles every recommendation in the payload and nothing else. I am not reopening that. The only open point is whether the shipped text should state this outright.
               Settled on my own authority: the fix belongs in bullet 3, the rule that reads too widely, and not in bullet 2. I also rejected guarding bullet 3 with "where a reply names at least one question". That guard would stop bullet 3 covering a free-form reply that names no question and does not assent, and such a reply must still leave every question unanswered. I checked the other contracts. No other one has multi-question reply rules, and the manager contract's "The human's words" section does not have this tension. So the change touches one bullet in one file.
               If you say yes, this node hands over a small implementation node that makes the edit, and you will see the diff at its gate.
ASK:           Should the grilling contract state outright that the bare-assent rule takes precedence, by opening bullet 3 with an exception?
RECOMMENDED:   Yes. Rewrite bullet 3 as: "Unless the reply is a bare assent as in the rule above, a question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself." This keeps your node 117 rule as it is, removes the one reading where the two bullets clash, and still covers free-form replies. The cost is one clause. As the text stands, a worker has to infer the precedence from bullet order, and the contract's own design is that workers do not fill gaps by guessing.
ALTERNATIVES:  Leave the text as it is: the order already implies the precedence, and no worker has misread it so far. But the clash is literal, and it sits in the very rule a worker applies when it reads your reply.
               Guard bullet 3 with "where a reply names at least one question": it reads more cleanly, but it silently drops the free-form reply that names nothing.
               Reorder or merge the bullets into one partitioned rule: a larger rewrite of text that landed recently (node 291), for the same effect.
```

*The manager: put to the human on 2026-09-25, once node 311's question was answered.*

**A1, the human**, `verbatim`, 2026-09-26: *"ok for 316"*

This takes the option the worker offered as `RECOMMENDED`, in the worker's words: *"Yes. Rewrite bullet 3 as: "Unless the reply is a bare assent as in the rule above, a question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself.""*

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Bare assent and an unnamed question have no stated precedence in the grilling contract (node 316)

ANSWER:        Yes. A bare assent such as "ok for recommended" settles the recommended option of every question in the payload, the questions the reply does not name included, and it settles nothing in the payload that is not a recommendation. That substance was already the human's own, given at [node 117](117-questions-sent-in-batches.md), `verbatim`: "ok for recommened says ok for everything but in practice it is unlikely I say it I think, as I will create my message one question at a time, so it will be more Q1 ok Q2 ok Q3 ..". This node did not ask it again.

               What this node decided is that the shipped grilling contract states the precedence outright rather than leaving it to the order of the bullets. Under "What a reply settles" in `.claude/skills/expedition-grilling/SKILL.md`, the bullet about an unnamed question read literally leaves every question of a bare assent unanswered, because a bare assent names no question. That contradicts the bullet above it. The fix is an exception that opens the unnamed-question bullet, and the bare-assent bullet stays unchanged. The new bullet reads:

               "Unless the reply is a bare assent as in the rule above, a question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself."

               Two alternatives were rejected. Guarding the bullet with "where a reply names at least one question" would stop it covering a free-form reply that names no question and does not assent, and such a reply must still leave every question unanswered. Leaving the text as it is keeps a literal clash in the very rule a worker applies when it reads the human's reply. No other worker contract carries rules for replies to several questions, and the manager contract's "The human's words" section has no such clash. So the change is one bullet in one file.

               Settled by the human, `verbatim`: "ok for 316", assenting to the recommendation as offered.

INDEX LINE:    A bare assent settles every recommendation in the payload, as node 117 fixed; the grilling contract's unnamed-question bullet gains an opening exception stating that precedence outright.

FLAGS:         ASSUMPTION: The node's question had two parts: whether a bare assent reaches unnamed questions, and whether the contract should say so. I treated the first as already settled by the human's own answer at node 117 ("ok for recommened says ok for everything"), which node 126 carried into the contract as conditions 4 and 5. I asked the human only the second. Grounds: the contract tells me to ask only what no source can tell me, and to re-ask a decision the human made would be to reopen it without cause.
               Index sentence: Node 316's worker took bare assent's reach as already the human's from node 117 and asked only whether the grilling contract should state its precedence.

NEW NODES:     Name: State the bare-assent exception in the grilling contract's unnamed-question rule
               Kind: implementation
               Question: Rewrite the unnamed-question bullet under "What a reply settles" in the grilling contract so that it opens with an exception for a bare assent.
               Blockers: none
               Acceptance condition:
               In `.claude/skills/expedition-grilling/SKILL.md`, the list of bullets that follows the sentence "A reply settles what it covers and nothing else, under the following rules." holds a bullet that currently reads, as one sentence run across two lines: "A question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself."
               1. That bullet's text is replaced by exactly this text, wrapped across lines the way the neighbouring bullets are wrapped: "Unless the reply is a bare assent as in the rule above, a question the reply does not name stays unanswered, and the human has not deferred it. Put it in a later payload. Never read an unnamed question as assent, and never answer it yourself."
               2. The bullet immediately above it is the one that begins "A reply that assents to the recommendation without naming any question", and its text is unchanged. So "the rule above" refers to it.
               3. The other bullets of that list, the sentence that introduces it and the order of the bullets are unchanged.
               4. No other line of `.claude/skills/expedition-grilling/SKILL.md` changes, and no other file changes.

INVALIDATIONS: none. The answer agrees with node 117's §4, with node 126's conditions 4 and 5, and with the text node 291 shipped. It makes that text say explicitly what those nodes meant.

Method skill: none was invoked, so no part of one was skipped.

RETROSPECTIVE:
(1) What I had to hunt for. The human's own words on what a bare assent does in a payload of several questions. I looked first in `decisions.md`, as the spawn told me. Node 117's index line says only that batching is adopted inside a node, and nothing about bare assent. The term "several questions" matched nothing, and "payload" matched mostly token-cost lines. I found the answer with a repo-wide grep for "assent", which led to node 117 ("Attempt 1, answer 2" and §4) and to node 126's condition items 4 and 5. I also grepped every worker contract to confirm that only the grilling contract carries rules for replies to several questions.
(2) What arrived in my context that this node did not need. Almost all of `map.md`: I needed only to confirm that nothing in its Notes bore on this. The auto-loaded `.claude/rules/expedition-triggers.md`, which holds manager duties only. The token-cost hits in `decisions.md` for "payload". A better arrangement: the spawn or the node file links node 117 as the governing decision and quotes its answer, and then the map is barely needed.
(3) What would have made it easier. A node question split into what is settled (node 117) and what is open (whether the text should say so, and in what wording). As written, it asks the settled substance again, and a worker who missed node 117 would have put it to the human a second time. The index line for node 117 would also help if it said that a bare assent reaches every recommendation in the payload, since that is the fact a reader of the index most needs.
(4) What was stale, wrong or contradictory. The node's title, "have no stated precedence", is true only of the shipped text. The record states the precedence, in node 117 §4 and node 126's condition. The manager relayed my unnumbered single question as "Q1". The contract keeps numbering for payloads of several questions, so this is minor but inconsistent. The spawn's search term "several questions" matched nothing in `decisions.md`. I found nothing wrong in the contract text beyond the clash this node fixes.

## Flags

`316.1` **· settled** `ASSUMPTION` — The node's question had two parts: whether a bare assent reaches unnamed questions, and whether the contract should say so. I treated the first as already settled by the human's own answer at node 117 ("ok for recommened says ok for everything"), which node 126 carried into the contract as conditions 4 and 5. I asked the human only the second. Grounds: the contract tells me to ask only what no source can tell me, and to re-ask a decision the human made would be to reopen it without cause.
