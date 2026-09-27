# A "just do it" mode that skips grilling and puts the work up for review

Type: grilling
Status: resolved

Blocked by: none

## Question

*The human's own idea, `verbatim`. **Minted by the manager from their message and not surfaced by any worker.***

> I also had the idea of a "just do it" mode, where the grilling is skipped, it is implemented and then the user can
> review. For low stakes stuff or if the user wants to work by looking at what it could be. (It can be easier to
> spot issue when it is written than during planning)

**What has to be decided**, written by the manager and confined to what their words already fix:

1. **What the mode is a property of.** Their words leave three readings and do not pick: a property of one **node**,
   set when it is minted; a property of an **effort**, set when it is charted; or a thing the human **says in the
   moment**, which turns the next pick into an implementation node rather than a grilling one.
2. **What replaces the grilling node's output.** A grilling node produces a decision that later nodes are blocked
   on, and an implementation node needs an **acceptance condition written before any work starts** that its own
   worker may not rewrite. Under this mode nobody has decided the thing the condition would state. So: who writes
   the condition, and what does it say? [Who writes the acceptance condition for an implementation node the manager
   mints itself](39-condition-for-a-manager-minted-node.md) already permits the manager to write one under four
   constraints, the first of which confines it to **what is already fixed** — and in this mode, by construction,
   less is fixed.
3. **What the review at the end is.** The effort already has a **gate**: an implementation node's work stops there
   until the human acts, and the outcomes are approve or send back. Their *"then the user can review"* may be that
   gate unchanged, or may be a different act — because a gate sends work back against an acceptance condition, and
   here the thing being judged is partly the decision the grilling would have made.
4. **Whether the flags mechanism already is this mode, partly.** An AFK worker that meets an ambiguity **decides it
   and raises a flag**, and the flag reaches the human at the node's first human moment. That is already
   *decide-then-show*. What this mode adds is skipping the decision **node** rather than the decision, so the
   question is what is left that flags do not already cover.
5. **What makes a thing low stakes**, and whether that is the human's call in the moment or a property anything can
   read. Their words offer *"low stakes stuff"* and a second, different ground — *"if the user wants to work by
   looking at what it could be"* — and the second is not about stakes at all.

**Their stated reason, which is a claim about how review works rather than about the workflow:** *"It can be easier
to spot issue when it is written than during planning."* The manager records it as their ground and has not weighed
it.

## The manager's note at filing

*Not a change to anything above.*

**One thing on the record that bears on this and cuts both ways.** This effort has run **one** node in something like
this shape: [node 114](114-context-destination-entry-omits-the-expectation.md), whose acceptance condition the
manager wrote itself because no worker reached the defect. It landed a `PASS` on its first check with no part
uncovered — **and the manager got the condition's own recorded enumerator wrong on the first attempt**, both returns
false, caught only because another node's worker happened to re-run them. That is one instance of the mode working
and one instance of what it costs, on the same node.

**Also relevant and not yet resolved:** whether the manager may write a condition at all in a case where less is
fixed is flag `94.4`, which is outstanding.

## Answer

`/expedition-standing-yes` ships: the human gives a scoped yes in advance, which takes the worker's recommendation or the checker's PASS as their reply. Exclusions are listed, and the manager judges what falls inside a scope.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, and the human's answers under `## Interview`. The node the worker surfaced is [node 342](342-ship-expedition-standing-yes.md).

## Interview

### Attempt 1

**Q1–Q2, from the worker**, pasted as it wrote them, 2026-09-26. **Held, not yet put to the human**: they arrived while node 307's gate was in front of the human, with the manager's own raise on node 124, node 318's gate and [node 259](259-a-multi-question-payload-has-no-per-question-ground.md)'s question queued ahead of them.

```
NODE:          A "just do it" mode that skips grilling and puts the work up for review
ABOUT:         This node decides what your "just do it" idea becomes in the workflow. In that mode the grilling is skipped, the change is built, and you review what was built. It is being decided now because the node sits open with no blockers, and the answer decides whether later nodes change the shipped contracts.
SO FAR:        I read the node, the map, the index of decisions, the manager contract, the glossary, and the implementation and prototype contracts. What I found, stated as fact:
               - A grilling node's output is a decision that later nodes wait on. An implementation node can be claimed only once it has a complete acceptance condition. When the manager mints a node itself, it may write that condition, but only from what is already fixed; anything it would have to decide goes to you instead (node 39). In this mode, by design, less is fixed.
               - Flags already work as "decide, then show". An implementation worker decides small ambiguities itself and flags them, and you see them at the gate. What stops that from covering this mode is the implementer's raise rule. It must raise, not decide, when (2) a choice affects more than its own node's code, or (3) it has no recommendation it believes. The decisions a grilling would have made are mostly of kind (2). So in this mode the worker would raise at every such choice, and grilling would come back through the raise route. Whatever this mode is, it has to relax those triggers for the node, and let the condition be written with less fixed.
               - Your second ground, "if the user wants to work by looking at what it could be", is close to the existing prototype kind: a probe built for you to react to, then thrown away. The difference is that just-do-it keeps the work if you approve it. Prototype also cannot touch product code or hold a code slot.
               - The gate already has three outcomes: approve, correct (uncapped correction rounds), and reject. A reject can send a node to "asked the wrong question, a replacement supersedes it". That already covers "now that I see it, I want this grilled after all".
               - Your "you decide" is already a way to hand one question to a grilling worker. The worker decides it in text and flags it. Just-do-it differs because the decision is made in code, and you judge it by looking at the code.
               - The effort has run one node in roughly this shape (node 114). The manager wrote its condition, and it passed the first check. But the manager got the condition's list of files wrong on the first try, and it was caught only by chance.
               Settled on my own authority: I treat the node's question 5 (what makes something low stakes, and who judges it) as part of question 1 below, because who switches the mode on and on what ground is one decision. Question 4 (how much flags already cover) is answered by the facts above rather than put to you. What the condition says, what the worker may decide, and what the review is all depend on your answers here. They come in the next payload.

Q1. What switches the mode on
ASK:           Who turns "just do it" on for a piece of work, and when can they do it?
RECOMMENDED:   Only you, in your own words, for a named change or node. You can say it when you first state an idea, or at any point before a node is claimed, including as your reply to a grilling payload ("just do it"). A grilling worker may offer it as one of its alternatives when it judges a question low stakes, but only your reply switches it on. The manager never switches it on because it judges something low stakes. An effort-wide "just do it for everything of kind X" needs no new mechanism: the manager would record it in the map as standing steering, as it does any other standing emphasis. This rests on your own words ("if the user wants"), on low stakes being your judgement rather than a property anyone can read off a node, and on keeping the manager from deciding which decisions you never see.
ALTERNATIVES:  - A property of the effort, set when it is charted, so every node in it skips grilling unless you say otherwise.
               - The manager may judge a node low stakes and switch the mode on itself, telling you in the pick report.
               - No mode: point the "see what it could be" case at a prototype node, and leave low-stakes cases to "you decide". Lost: the built work being kept when you approve it.

---

Q2. Whether it ships or stays in this effort
ASK:           Should this mode become part of the shipped workflow (the expedition skill files), or be a standing rule of this effort only?
RECOMMENDED:   Ship it. Your reason, "it can be easier to spot issue when it is written than during planning", is about how review works in general, not about this effort. The map's rule is that a rule reaches the shipped files only where you say so, and otherwise stays this effort's alone. So it needs your word either way.
ALTERNATIVES:  - This effort only: the map records it as your standing instruction, and no contract changes.
               - This effort first, and ship it once it has been used here on at least one node.
```

*The manager's note, 2026-09-26:* the manager sent this node's worker, by mistake, a message meant for node 259's worker that held only the words "wrong recipient placeholder", then a second message telling it to disregard the first and that its Q1 and Q2 are still held. Nothing of the human's reached it.

*The worker's reply to that message, 2026-09-26, pasted:* it handed back its Q1 and Q2 payload again, unchanged in substance from the one held above, with this part for the manager:

> Note on your mid-task message: "wrong recipient placeholder" asked for nothing and looks misdirected, so I took no action on it. If you meant to send something, send it again.
>
> RETROSPECTIVE (effort-scoped; I wrote no graph file)
>
> (1) What I had to hunt for.
> - The meaning of "flag 94.4", cited in the node's filing note. flags.md shows 94.4 as settled ([x]), and it is about something else: whether node 103's sixth site went beyond node 82's permission. The flag that actually questions the premise of the manager writing a condition is 39.1, which is outstanding. I found this by grepping flags.md for the node-39 link; I looked for 94.4 first.
> - The implementer's raise triggers, which turned out to be the crux. The node file does not mention them. I found them in .claude/skills/expedition-implementation/SKILL.md under "## Flag, or raise"; I looked in the manager contract first.
> - The overlap with the prototype kind: found through the glossary's `prototype` entry, then the prototype contract.
>
> (2) What arrived that this node did not need.
> - Most of map.md: the worktree route, the gate diff command, the never-delete scope, the retrospective wording, tokens, resuming agents. Only the rule that a standing rule reaches shipped files only where the human says so (node 93), and "the human is the scarce resource", bore on this node.
> - In the manager contract, the sections on dying agents, closing an effort, and the two lists of open conflicts and unsettled duties were unused.
> - Neither the node file nor the spawn pointed at the implementer's raise triggers or the prototype kind. One line in the node file naming the sections that bear on it would have saved about half of the reading.
>
> (3) What would have made this node easier.
> - The node file's Q2 ("who writes the condition") should also name the implementer's raise triggers 2 and 3, since they, not the condition, are what bring grilling back.
> - The flag citation should be checked against flags.md before the node is filed.
>
> (4) What I read that was stale, wrong, or contradictory.
> - The node's filing note calls flag 94.4 outstanding and on this topic. It is settled and about something else; it probably meant 39.1.
> - The node's point 3 says the gate's outcomes are "approve or send back". There are three: approve, correct, reject.
> - The shipped manager contract (the gate payload list under "## The gate", and the "never yours" table) still tells the manager to give the command that shows the diff. map.md says that practice stopped, pending node 231. That is expected until 231 lands, but a reader of the contract alone gets the old rule.
> - map.md says CONTEXT.md is moving to .claude/skills/expedition/glossary.md. It is still at the repo root, which is consistent with node 56 not having landed.

*The manager put Q1 and Q2 to the human on 2026-09-26, after node 332's gate.*

**Q1 and Q2, the human's answer**, 2026-09-26, `verbatim`: *"Maybe do a skill "/expedition-auto-approve", I think it is more precise than a string, where you pass what is the scope. You can propose names for the feature. It should be part of the shipped workflow. The scope could be whatever you want. A specific part of the effort (ex: a refactor, part of the feature) or a type of demand (ex: auto approve gates if you trust the checker), etc."*

*The manager's note:* Q2 agrees with the worker's recommendation ("Ship it"). Q1 agrees that only the human switches the mode on, and **diverges in part**: the switch is a skill the human invokes with a scope argument, not words in a reply; the scope may be a part of the effort or a type of demand; and the human's example, auto-approving gates where they trust the checker, reaches past skipping grilling, which is all the node's question asked about. The human asks the worker to propose names for the feature. This reframes the node's question, so it goes back to the worker.


**Q3 to Q5, from the worker**, pasted as it wrote it, 2026-09-26. **Held, not yet put to the human**: it arrived while node 341's raise was in front of the human, with the gates of nodes 334 and 333 queued ahead of it. The worker sent the same payload twice, once by message and once as its hand-back; it is filed once.

```
NODE:          A "just do it" mode that skips grilling and puts the work up for review
ABOUT:         This node decides what your scoped approval skill does, now that you have made it a shipped skill you invoke with a scope, rather than a mode for skipping grilling. This payload settles its name, what it stands in for, and who decides what falls inside a scope.
SO FAR:        Settled by your answer. The feature ships in the workflow. Only you switch it on, by invoking a skill with a free-form scope. The scope may be a part of the effort (a refactor, part of a feature) or a type of demand (for example, auto-approve gates where you trust the checker). That widens the node from "skip grilling" to "a yes you give in advance for a scope". It can cover any moment the workflow would otherwise put to you.
               Facts this rests on:
               - Every moment put to you already carries something you could say yes to in advance. A grilling question and a worker's raise each carry a RECOMMENDED. A gate carries the checker's PASS.
               - The glossary's "Approval" is currently only your yes at the gate. It is "the only thing that permits a code commit".
               - Your flags settle at the first moment a node's close is put in front of you: the gate, or else the pick report that closes the node. A pick report awaits no answer, and its flags settle on whatever you say next.
               - Earlier I found that skipping the grilling node outright leaves nothing for the implementation node's acceptance condition to say. It would also make the implementer raise at every cross-node choice. Taking the grilling worker's recommendations as your answers avoids both problems: the grilling still runs, and the graph stays as it is.
               Settled on my own authority: an invocation is standing steering. So the manager writes it into the map in your words, under the existing rule for a standing scope. It stays in force until you change it, and the next effort starts without it.

Q3. The feature's name
ASK:           What should the skill and its concept be called?
RECOMMENDED:   `/expedition-standing-yes`, with the concept called a "standing yes": a yes you give in advance for a scope, which stays in force until you change it. "Standing" is already this workflow's word for what you set once and what then persists ("standing steering", "standing instruction"). It also avoids two collisions with "auto-approve". In Claude Code, "auto-approve" already means approving tool-permission prompts, so a reader of the skill list would expect it to be about permissions. And "approval" in the glossary means only your yes at the gate, while this also covers grilling questions and raises.
ALTERNATIVES:  - `/expedition-auto-approve`, your name: clear to you now, but it collides with Claude Code's permission auto-approval and widens the glossary's "approval".
               - `/expedition-yes-in-advance`: plainer English, but longer and less in line with the "standing" vocabulary.
               - `/expedition-pre-approve`: short, with the same "approval" widening as auto-approve.

---

Q4. What a standing yes stands in for, and what it never covers
ASK:           When an item falls inside a standing yes's scope, what exactly replaces your reply, and what may it never cover?
RECOMMENDED:   It stands in for your reply to the one thing already on the table, and changes nothing else:
               - On a grilling question or a worker's raise, the worker's RECOMMENDED is taken as your "ok for recommended".
               - On a gate, the checker's PASS is taken as your approval, and the manager commits.
               - Nothing waits in your queue for these items.
               - The node's interview records each entry with a new mark ("standing yes", beside the existing "verbatim" and "paraphrase"). The entry quotes your scope text word for word and never passes itself off as words of yours.
               - The node's close is reported in its pick report with every flag, as today, so you still see all of it after the fact. Its flags settle on whatever you say next, under the existing rule.
               It never covers:
               - a question with no recommendation the worker believes;
               - a checker's FAIL, or a checker's raise;
               - a gate whose check will not pass;
               - a reject, which stays your word alone;
               - an acceptance condition judged wrong;
               - closing the effort.
               This rests on keeping the graph and the node kinds exactly as they are. The only thing replaced is who gives the one answer.
ALTERNATIVES:  - For a scope that covers grilling, skip the grilling node entirely and mint an implementation node straight from your words. This saves the grilling worker's run, but leaves the condition with nothing fixed to say, and the implementer's raise rule would bring the questions back.
               - Let a standing yes also cover a FAIL or a failing gate. That would land work that no one, human or checker, has judged good.
               - Have the auto-taken moments settle nothing and go to the closing report instead. You would then see them only at the end.

---

Q5. Who decides that an item is inside a scope
ASK:           A scope is free-form ("the refactor of X", "gates where I trust the checker"). Who decides that a given item falls inside it?
RECOMMENDED:   The manager decides, at the moment it would otherwise put the item to you. It records on the node which standing yes it applied, and it names the item and the scope in the pick report. You can pull any item back out in one line, as you already redirect a pick. Where the manager cannot tell whether an item is inside the scope, it puts the item to you as usual. This rests on the scope being yours to write in any words, which leaves the manager as the only party present to read it, and on the pick report already being the report that awaits no answer.
ALTERNATIVES:  - The worker decides, and says in its payload that the item is inside a named scope. The manager passes that along without judging it. But a worker has not read the map's steering in the manager's sense, and would decide something the manager then acts on.
               - Scopes are limited to forms nobody has to judge (a list of node numbers, a node kind, "all gates"). That is exact, but it loses "part of the feature" and "if you trust the checker", which were your own examples.
```

*The worker's note for the manager, pasted:* (Manager: this is the same payload I already sent through SendMessage; send it only once. Q3 to Q5 are independent, so they share one payload. I will send the retrospective with the final handover.)

*The manager put Q3 to Q5 to the human on 2026-09-27, after node 336's gate.*

**Q3 to Q5, the human's answer**, 2026-09-27, `verbatim`: *"Q3 ok Q4 ok Q5 ok"* — taking, for each, the worker's RECOMMENDED: Q3 *"`/expedition-standing-yes`, with the concept called a "standing yes""*; Q4 *"It stands in for your reply to the one thing already on the table, and changes nothing else"*; Q5 *"The manager decides, at the moment it would otherwise put the item to you."*

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      A "just do it" mode that skips grilling and puts the work up for review

ANSWER:
**The workflow ships a skill, `/expedition-standing-yes`. The human invokes it with a free-form scope, and it gives a yes in advance to what the workflow would otherwise put to them inside that scope. The concept is called a "standing yes".** It replaces the "just do it" mode as first asked. The human reframed the question at their first reply, `verbatim`: *"Maybe do a skill "/expedition-auto-approve", I think it is more precise than a string, where you pass what is the scope. You can propose names for the feature. It should be part of the shipped workflow. The scope could be whatever you want. A specific part of the effort (ex: a refactor, part of the feature) or a type of demand (ex: auto approve gates if you trust the checker), etc."* The rest was settled by their assent to each recommendation, `verbatim`: *"Q3 ok Q4 ok Q5 ok"*.

1. **It ships, and only the human switches it on**, by invoking the skill with a scope written in any words. A scope may name a part of the effort, such as a refactor or part of a feature, or a type of demand, such as gates where they trust the checker.
2. **The name is `/expedition-standing-yes`**, and the human's `/expedition-auto-approve` is refused. In Claude Code, "auto-approve" already means approving tool-permission prompts. And the glossary's "approval" means only the human's yes at the gate, while a standing yes also covers questions and raises. "Standing" is already this workflow's word for what the human sets once and what then persists.
3. **A standing yes stands in for the human's reply to the one thing on the table, and changes nothing else.** The graph, the node kinds and the grilling all stay as they are.
   - On a worker's question or raise, the worker's `RECOMMENDED` is taken as the human's "ok for recommended".
   - On a gate, the checker's `PASS` is taken as the human's approval, and the manager commits.
   - An item covered this way never enters the pending queue.
   - The node records each such entry with a new mark, `standing yes`, beside `verbatim` and `paraphrase`. The entry quotes the scope text word for word and is never presented as the human's own words.
   - The node's close goes out in its pick report with every flag, as today. Its flags settle on whatever the human says next, under the existing rule.
4. **A standing yes never covers**:
   - a question or raise with no recommendation the worker believes;
   - a checker's `FAIL`, or a checker's raise;
   - a gate whose check will not pass;
   - a reject, which stays the human's word alone;
   - an acceptance condition judged wrong;
   - closing the effort.
5. **The manager decides whether an item is inside a scope**, at the moment it would otherwise put the item to the human. It records on the node which standing yes it applied. It names the item and the scope in the pick report, where the human can take any item back in one line. Where the manager cannot tell whether an item is inside a scope, the item goes to the human as usual.

**Why skipping the grilling node outright was set aside.** An implementation node can be claimed only once it has a complete acceptance condition. A manager-written condition may demand only what is already fixed, and with no grilling nothing is fixed. The implementer's raise rule also sends every choice that reaches beyond its own node's code back to the human. Taking the grilling worker's recommendations as the human's answers keeps both working, at the cost of the grilling worker's run.

**The node's original question 4** (what flags already cover) was answered by analysis, not put to the human. Flags already work as "decide, then show", and what this feature adds is the removal of the human's live moments. **Question 5** (what makes something low stakes) was absorbed into point 5 above: the human's scope decides it.

INDEX LINE:    `/expedition-standing-yes` ships: the human gives a scoped yes in advance, which takes the worker's recommendation or the checker's PASS as their reply. Exclusions are listed, and the manager judges what falls inside a scope.

FLAGS:
- ASSUMPTION (node prose): I settled that an invocation is standing steering. So the manager writes it into the effort's map in the human's words, under the existing rule that a scope or an emphasis from the human is standing and goes into the map. It stays in force until the human changes it, and the next effort starts without it. Ground: the manager contract's `### Standing steering, and standing instructions of one effort` already covers this, so no new rule was needed.
  (index) A standing yes is recorded in the map as the human's standing steering, in their words, in force until they change it; the next effort starts without it.
- ASSUMPTION (node prose): The worker needs to know that its question was answered by a standing yes and not by the human. So I set the resume a worker receives to carry a line `STANDING YES: <the scope text, verbatim>` in place of `HUMAN ANSWER`. The worker reads that line as assent to its recommendation. Ground: the three worker contracts that define `HUMAN ANSWER` say it holds only the human's own words, so putting a standing yes under that heading would make it false. The human did not rule on the resume's shape.
  (index) A worker answered by a standing yes is resumed with a `STANDING YES:` line quoting the scope, never under `HUMAN ANSWER`.
- ASSUMPTION (node prose): A payload holding several questions is covered only when every question in it is inside a scope. Otherwise the whole payload goes to the human, unchanged. Ground: a worker's payload is relayed whole, and splitting it would mean the manager re-authoring it. The human's "Q5 ok" gave the manager per-item judgement, but did not say whether a payload can be covered in part.
  (index) A multi-question payload is taken under a standing yes only when all its questions fall inside the scope; otherwise it goes to the human whole.
- ASSUMPTION (node prose): A gate is not covered while any part of its acceptance condition that the checker could not cover is still owed and the manager cannot establish it. Such a gate goes to the human. Ground: the manager contract says an owed part is established "by the gate at the latest", and a standing yes removes the human from that gate. I read this as belonging with the human's exclusion of work nobody has judged. The human was not asked about this case.
  (index) A gate holding a still-owed part of its condition that the manager cannot establish is not taken under a standing yes and goes to the human.

NEW NODES:
Name: Ship `/expedition-standing-yes`
Kind: implementation
Question: Ship the standing yes, as decided at node 131, into the workflow's skill files and glossary.
Blockers: none
Acceptance condition:
  The work leaves the tree meeting all of the following. Every file named is under the repo root.
  1. A new skill file exists at `.claude/skills/expedition-standing-yes/SKILL.md`. Its frontmatter `name` is `expedition-standing-yes`, and its description says the human invokes it, with a scope, in an expedition's manager thread. Its body tells the manager all of the following:
     a. The human invokes it with a scope written in any words. A scope may name a part of the effort (for example a refactor, or part of a feature) or a type of demand (for example gates where the human trusts the checker).
     b. The manager records the invocation in the effort's map, as the human's standing steering, in the human's own words. It stays in force until the human changes it, and the next effort starts without it.
     c. For an item inside a scope, the worker's `RECOMMENDED` is taken as the human's "ok for recommended" on a worker's question or raise. On a gate, the checker's `PASS` is taken as the human's approval, and the manager then commits as on an approval.
     d. The manager decides whether an item is inside a scope, at the moment it would otherwise put the item to the human. Where it cannot tell, it puts the item to the human as usual.
     e. A standing yes never covers any of the following: a question or raise with no recommendation the worker believes; a checker's `FAIL`; a checker's raise; a gate whose check will not pass; a gate holding a part of its condition that the checker could not cover, that is still owed, and that the manager cannot establish; a reject; an acceptance condition judged wrong; closing the effort.
     f. A payload holding several questions is covered only when every question in it is inside a scope. Otherwise the whole payload goes to the human, unchanged.
     g. An item covered by a standing yes never enters the pending queue.
     h. The manager records each covered item on the node, under `## Interview` for a question or raise and under `## Review` for a gate, with the mark `standing yes`. The entry quotes the scope text word for word and says which standing yes was applied. It never marks such an entry `verbatim`.
     i. The pick report that closes a node names every item on that node taken under a standing yes, with its scope, and carries every flag the node holds, as for any closing pick report. It states that the human may take any listed item back by naming it in a reply.
     j. A worker whose question or raise is covered is resumed with a line `STANDING YES: <the scope text, verbatim>` in place of `HUMAN ANSWER`.
  2. `.claude/skills/expedition/SKILL.md` (the manager contract):
     - points at `expedition-standing-yes` from `## The gate` and from `## What is in front of the human, and when`, stating in each place that an item covered by a standing yes is handled by that skill and not put to the human;
     - no longer says, anywhere, without qualification, that answering on the human's behalf is never the manager's, or that only the human's own approval permits a commit. Each such statement names the standing yes as the case it does not cover.
  3. `.claude/skills/expedition/graph-conventions.md`, under `### Recording the human's words`, names three markers instead of two: `verbatim`, `paraphrase`, and `standing yes`. It states that a `standing yes` entry quotes the scope text word for word and is not the human's words about that item.
  4. Each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-precondition/SKILL.md` states, beside its `HUMAN ANSWER` resume shape, that the worker may instead be resumed with `STANDING YES: <the scope text, verbatim>`, and that it reads this as assent to the recommendation of every question in that payload. `.claude/skills/expedition-implementation/SKILL.md` states the same beside its description of how the human answers a raise, reading it as "continue" on the raise's recommendation.
  5. The glossary (`CONTEXT.md` at the repo root, or `.claude/skills/expedition/glossary.md` if the glossary has moved there) has an entry **Standing yes**: a yes the human gives in advance, for a scope they state, which the manager takes in place of the human's reply on items inside that scope. Its `_Avoid_` line refuses `auto-approve` and gives the reason: in Claude Code the word means approving tool-permission prompts. The glossary's **Approval** entry no longer says, without qualification, that approval is the human's yes at the gate and the only thing permitting a code commit. It names a standing yes covering that gate as the other thing that permits one.
  6. No file in the tree names the skill `/expedition-auto-approve` except as a refused word.

INVALIDATIONS: none contradicted. Two resolved nodes are extended rather than overturned, and the new node's condition carries both extensions into the shipped files:
- [Human review of landed code](nodes/20-human-code-review.md) and the glossary say approval is the human's yes at the gate and the only thing permitting a commit. A standing yes is the human's yes given in advance, so the human still acts; that wording gains a qualification.
- The manager's "answering anything on the human's behalf is never yours" stands: under a standing yes the answer is the human's own scope text applied by the manager, and it is marked as such.
The tier-1 list of three kinds is untouched, because covered items never enter the queue. The flag-settling rule is untouched.

Contract departure: I sent payload 2 to you by SendMessage because SubagentHandback refused a second report, then sent it again by handback when that was enforced. Nothing else departed from the contract. I invoked the `naming` skill for Q3; it has no instruction that conflicts with the contract.

RETROSPECTIVE
(1) What I had to hunt for.
- The meaning of flag "94.4" cited in the node's filing note. flags.md shows 94.4 settled and about something else; the flag that bears on this node is 39.1, which is outstanding. Found by grepping flags.md for the node-39 link, after looking for 94.4 first.
- The implementer's raise triggers, which were the crux of the first payload. They are in `expedition-implementation/SKILL.md` under `## Flag, or raise`; I looked in the manager contract first.
- The prototype overlap: the glossary, then the prototype contract.
- For the condition: which contracts define `HUMAN ANSWER`, and where the recording marks live. Found by grep: `graph-conventions.md` `### Recording the human's words`, plus the grilling, prototype and precondition contracts. The implementation contract uses prose for the answer to a raise instead of a shape.

(2) What arrived that this node did not need.
- Most of map.md: the worktree route, the gate diff command, the never-delete scope, the retrospective wording, tokens, resuming. Only the rule on shipped versus effort-scoped rules (node 93), and the scarce-human line, bore on this node.
- The manager contract's sections on dying agents, closing, open conflicts and unsettled duties were unused.
- A line in the node file pointing at the raise triggers and the prototype kind would have replaced about half of the reading.

(3) What would have made this node easier.
- The node file's question 2 should name implementer raise triggers 2 and 3, since they, not the condition, are what bring grilling back.
- Check flag citations before filing.
- The single-handback rule caused three confused round trips once the node needed a second payload. The spawn or the harness should say how a second question payload travels.

(4) What was stale, wrong, or contradictory.
- The node cites flag 94.4 as outstanding and on this topic; it is settled and about something else (probably meant 39.1).
- The node's point 3 says the gate's outcomes are "approve or send back"; there are three: approve, correct, reject.
- The shipped manager contract still tells the manager to give the command that shows the diff (the gate payload list, and the never-yours table), while map.md says that stopped, pending node 231.
- map.md describes the glossary as moving to `.claude/skills/expedition/glossary.md`; it is still at the root as `CONTEXT.md`, so the condition names both paths.

## Flags

`131.1` **· settled** `ASSUMPTION` — I settled that an invocation is standing steering. So the manager writes it into the effort's map in the human's words, under the existing rule that a scope or an emphasis from the human is standing and goes into the map. It stays in force until the human changes it, and the next effort starts without it. Ground: the manager contract's `### Standing steering, and standing instructions of one effort` already covers this, so no new rule was needed.

`131.2` **· settled** `ASSUMPTION` — The worker needs to know that its question was answered by a standing yes and not by the human. So I set the resume a worker receives to carry a line `STANDING YES: <the scope text, verbatim>` in place of `HUMAN ANSWER`. The worker reads that line as assent to its recommendation. Ground: the three worker contracts that define `HUMAN ANSWER` say it holds only the human's own words, so putting a standing yes under that heading would make it false. The human did not rule on the resume's shape.

`131.3` **· settled** `ASSUMPTION` — A payload holding several questions is covered only when every question in it is inside a scope. Otherwise the whole payload goes to the human, unchanged. Ground: a worker's payload is relayed whole, and splitting it would mean the manager re-authoring it. The human's "Q5 ok" gave the manager per-item judgement, but did not say whether a payload can be covered in part.

`131.4` **· settled** `ASSUMPTION` — A gate is not covered while any part of its acceptance condition that the checker could not cover is still owed and the manager cannot establish it. Such a gate goes to the human. Ground: the manager contract says an owed part is established "by the gate at the latest", and a standing yes removes the human from that gate. I read this as belonging with the human's exclusion of work nobody has judged. The human was not asked about this case.
