# Carry the open-question search into the shipped contracts

Type: implementation
Status: claimed
Blocked by: 348

## Question

Node 272 decided that the search every party runs before handing back a fact covers the open nodes' `## Question` sections as well as their `## Acceptance condition` sections. The party reports each open node whose question its work changes, and the manager updates it in place. The shipped files state the search over conditions only.

*The manager's note: blocked on node 348, which is editing the same paragraph of the five worker contracts.* *Reported by [node 272](272-the-cascades-open-node-half-is-parked-on-a-ground-that-turns-out-to-be-false.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 272's worker and filed by the manager.*

> The files in scope are these six. The five worker contracts are `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`. The sixth is the manager's contract, `.claude/skills/expedition/SKILL.md`.
> The scope came from a search. `grep -n -F "search the open nodes' \`## Acceptance condition\` sections for what your" .claude/skills/*/SKILL.md` returned exactly the five worker contracts, and `grep -n -F "It searches the open nodes' \`## Acceptance condition\` sections" .claude/skills/expedition/SKILL.md` returned the manager's contract. An instance the same searches reach outside these six files is reported and not edited.
> After this work:
> - (a) In each of the five worker contracts, the paragraph beginning "Before you write your handover, search the open nodes' `## Acceptance condition` sections" also tells the worker to search the open nodes' `## Question` sections. It uses the same handles: each word its work refuses, each path it changes or moves something out of, and each phrase it supersedes. It covers every open node, claimed or not, and the worker reads only what matches.
> - (b) In each of those five contracts, the handover's `CONDITIONS` part, or a part placed beside it, asks the worker to name the open nodes whose `## Question` its work changes (a renamed term, a part answered, or the node made unnecessary) and to say how.
> - (c) In `.claude/skills/expedition/SKILL.md`, the paragraph beginning "Before a party hands back a fact it established" says three things. The search also covers the open nodes' `## Question` sections. The manager updates an unclaimed node's question in place with the old wording marked, per graph-conventions.md's rule for an open, unclaimed node whose question has only changed. Where no party established the fact, the manager does that search.
> - (d) Each of the six files states that a question naming a thing in different words from the change's will not match, and that this is accepted.
> - (e) No file under `.scratch/` is changed.
> - (f) Every heading in each of the six files, as listed by `grep -n '^#\{1,6\} '` before the work, is still present afterwards, in the same order.
