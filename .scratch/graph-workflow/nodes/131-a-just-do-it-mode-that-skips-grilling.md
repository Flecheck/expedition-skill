# A "just do it" mode that skips grilling and puts the work up for review

Type: grilling
Status: claimed

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
