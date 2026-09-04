# Where the rules a checker is held to live, now that it may not go and find them

Type: grilling
Status: open

Blocked by: none

## Question

*Minted by the manager from the human's standing direction, and not surfaced by any worker.*

**Their words, `verbatim`:**

> Also I don't know if I have talked about it but in the checker, it shouldn't try to find the skill/rules, they
> should be at the map level and sent by the manager or just read by the checker. I don't know if it is still the
> case but we shouldn't use matt pockock skills code review skill as it is too generic. (it is easier to change the
> rule when its in a file than when the checker finds stuff by itself. The rules should also be used by the
> implementer

**The direction itself is in force and is not this node's question.** It is recorded as a standing preference in
`map.md` under [node 93](93-effort-scoped-custom-rules.md). This node decides the three things the direction leaves
open:

1. **Where the rules live.** Their words say *"at the map level"*, which the manager has deliberately not read as
   *"in `map.md`"* — [node 136](136-the-map-has-grown-back-what-node-59-saved.md)'s Q1, which they answered in the
   same message, moves per-kind material **out** of `map.md` into siblings named for their reader. A sibling file is
   still a file rather than a discovery, so both readings satisfy the direction's stated ground. Which one they
   meant, or whether they mind, is the first question.
2. **What a checker is given in place of the reviewing skill's procedure.** Today the checker's contract devotes
   whole sections to *finding* a reviewing skill, running part of it, keeping its delegated agents unblinded, and
   reporting which of its parts were left unrun. If no skill is named, all of that has no object. What replaces it —
   a list of standards and nothing else, or a procedure written into the contract — is the second question.
3. **How the implementer receives the same rules.** *"The rules should also be used by the implementer"*, and today
   the implementation contract is held against *the bar* rather than against any named rule set. Whether the
   implementer is handed the text or pointed at the file is the third — and it is a token question as much as a
   design one, since a worker pays its whole opening payload uncached.

## What is already established, so this node does not re-derive it

**The checker's contract still contains the discovery apparatus**, verified by the manager rather than assumed:
`.claude/skills/expedition-checker/SKILL.md` has a section headed *"Find these before you read the work"* naming *"a
skill that reviews code, or anything doing that job under another name"*, and instructing that *"where you find no
reviewing skill at all, hold the work against whatever rules you did find"*. It has further sections on running such
a skill, on keeping what such a skill delegates unblinded, and on carrying such a skill's question to the human. So
the human's *"I don't know if it is still the case"* is answered: it is.

**The map's review route no longer names a reviewing skill.** The manager superseded that sentence when the
direction arrived; the archived text is in `map-history.md`. What survives in the map is the list of standards
themselves, the measured trap about `CONTEXT.md`'s refused words being unusable as a grep list, and the `where`
correction — the direction moves where rules come from, not what they are.

**Ground rule 5 is reached by this and by the earlier no-plugin direction both.** It locates `/writing-for-agents` in
the `mattpocock-skills` plugin by name, and it is the standard that bites hardest on this effort's prose deliverables.
[Node 132](132-does-the-plugin-direction-reach-the-efforts-own-bar.md) already asks whether the plugin direction
reaches the effort's own bar; this node should not answer node 132's question and should say where the two meet.

## The manager's note at filing

*Not a change to anything above.*

**The manager has taken no view on any of the three.** Every one of them lands on files the manager spawns workers
against, and the manager's own checker spawns have been supplying the rules by hand for several nodes already —
which is evidence about what is workable and not a decision about what should be written down.

**One collision to name rather than to sequence.** Node 136 is live and its Q1 answer is taken: per-kind material
moves out of `map.md` into siblings named for their reader, with the bar's commands and the landing policy going to
the file the implementation and checker spawns point at. **That sibling is the obvious home for these rules**, and if
it is, this node and node 136 are describing one file from two directions. The manager has told node 136's worker to
state how its split stands against this direction and to say where it needs the human's word rather than resolving
it.

## The same node, framed independently by node 136's worker

[Node 136](136-the-map-has-grown-back-what-node-59-saved.md)'s worker surfaced this node from the same standing
direction, not knowing it had been minted, and framed it as its own **B**. **Pasted as it wrote it**, because it
names one thing the framing above does not.

> **Where the bar's rules live, and what the checker is held to**
> Kind: grilling
> Blockers: none.
> Question: A standing direction of the human's, `verbatim`: *"in the checker, it shouldn't try to find the
> skill/rules, they should be at the map level and sent by the manager or just read by the checker. I don't know if
> it is still the case but we shouldn't use matt pockock skills code review skill as it is too generic. (it is easier
> to change the rule when its in a file than when the checker finds stuff by itself. The rules should also be used by
> the implementer"*. Three things are open in it. Does *at the map level* permit a sibling file the implementation
> and checker spawns point at, or does it mean literally inside `map.md`? What replaces
> `mattpocock-skills:code-review`, given that ground rule 5 holds every prose deliverable of this effort against
> `/writing-for-agents`, which is named by the same plugin? And does the direction reach the shipped contracts or
> bind this effort only — which under the map's own rule is the human's to declare and nobody else's.

***The manager's note.*** **Its third question is new and the manager had not asked it.** Whether a standing
direction reaches the **shipped files** or binds **this effort only** is settled by [node
93](93-effort-scoped-custom-rules.md) as the human's to declare, and the manager wrote this direction into the map as
an effort-scoped preference without putting that to them. The same is true of the earlier no-plugin direction. **This
node inherits the question for both.**

**What node 136's answer already establishes about the wide reading, and does not decide.** Its worker found that the
review route sits in `map.md`, *"which the checker cannot read, so the manager must transcribe it by hand"* — so a
sibling read by both the implementer and the checker is *"the single-source shape the direction asks for"*, retiring
a defect three retrospectives have reported. Under the narrow reading — literally inside `map.md` — the saving from
node 136's split falls from ~41% to ~31%, and *"that reading also implies the checker stops being blind to the map,
which is a larger change than this node."* **[Node 140](140-move-the-implementers-and-checkers-material-out-of-the-map.md)
is blocked on this node for exactly that reason**, its acceptance condition being written in part with the
destination left out.

## Interview

### Attempt 1, question 1 — delivered

*Pasted as the worker wrote it. The manager authored none of it and has taken no view.*

> **NODE:** Where the rules a checker is held to live, now that it may not go and find them
>
> **ABOUT:** Your direction says the checker must not go hunting for the rules it holds work against — they belong in
> a file, "at the map level", sent by the manager or read by the checker, and used by the implementer too. The
> direction is in force. This decides which file, and that is the one thing an implementation node already written and
> waiting cannot start without.
>
> **SO FAR:** I read the checker's and implementer's shipped contracts, map.md, the four decisions that bear on this,
> and the two nodes waiting on me. Three things I found matter, and one of them is happening right now.
>
> **1. THE LITERAL READING OF "AT THE MAP LEVEL" DOES NOT ACTUALLY WORK.** The checker is the one worker that never
> reads map.md — it is kept blind to the record so its check is independent, and its own contract says so in as many
> words. So if the rules stay inside map.md, the manager must keep hand-copying them into every checker spawn, which
> is precisely the arrangement your direction is aimed at. It is also the arrangement that just failed: about an hour
> ago the manager resumed a live checker telling it "no standard moved" when one had, and that checker then went and
> found and ran mattpocock's code-review skill by exactly the discovery route you barred. The manager has been
> transcribing a checker's rules by hand for several nodes. A rule in a file is editable; a rule that reaches the
> agent through a manager's retyping is editable and then mistyped.
>
> **2. A SIBLING FILE IS A FILE, AND YOUR OWN SENTENCE CONTEMPLATES ONE.** "or just read by the checker" is a file the
> checker reads. Your stated ground is changeability, and a sibling next to map.md is exactly as editable as map.md.
> It also gives you the single source your last clause asks for: one file the implementer reads and the checker
> reads, instead of today's split where the implementer is sent to /coding-principles and /naming while the standard
> that actually bites on prose is named only in map.md, which the implementer's contract never points it at. Three
> retrospectives have reported that defect.
>
> **3. A COLLISION THAT IS LIVE AS I WRITE.** You answered "Q1 ok" to moving per-kind material out of map.md into
> siblings named for their reader. Two implementation nodes came out of that: node 139 for the manager's material,
> running now, and node 140 for the implementer's and checker's, blocked on this question. Node 139's condition moves
> the paragraph headed "The review route for this repo" into the MANAGER's file — and that paragraph is the checker's
> standards list. Written before your direction arrived, it was right then (the manager read it to compose a spawn)
> and is wrong now (the checker should read it itself). Its worker has not written a byte yet, so this is fixable at
> no cost if it is decided now, and is a second move later if it is not.
>
> **WHAT I SETTLED MYSELF, coming back as assumptions:** that this question is answerable without first settling
> whether your direction reaches the shipped skill files or binds this effort only (it is — the material moves out of
> map.md either way, only the reader changes); and that a filename is bookkeeping rather than yours to choose.
>
> **ASK:** Where does the implementer's and checker's material go — the bar's commands, the landing and worktree
> policy, the code-slot count, and the standards list the checker holds work against?
>
> **RECOMMENDED:** Into ITS OWN new file beside map.md, separate from the manager's file, holding the standards list,
> the bar's commands and the landing policy, read directly by the checker and by the implementer, with map.md keeping
> a one-line pointer. The review-route paragraph moves here rather than into node 139's manager file, and its
> operative list is separated from its story — the part recording that two earlier checkers burned their biggest cost
> finding these standards stays with the manager or goes to map-history.
>
> It rests on three things rather than on preference. (a) It is the only reading under which nothing is retyped: a
> file the checker reads is a file you edit once. (b) The separation from the manager's file is forced by a rule this
> effort already fixed — only standing constraints true of any node's work may reach a blind checker, never an
> account of what happened on some other node. The manager's file is full of exactly that: the fog, the dogfood
> target, and the accounts. Share one file and either the checker reads material it is meant to be blind to, or the
> manager is back to selecting by hand, which is the defect. Two files, and the line between them is a test that
> already exists and needs no new judgement. (c) It preserves the measured saving in full: the split you approved
> takes ~41% off the file every worker reads cold on every node, and keeping this material in map.md drops that to
> ~31%.
>
> One consequence I should name rather than bury: the standards list currently points at "this map's standing
> preferences, ground rules and four standing rules", which sends the checker back into map.md. For the file to stand
> alone those rules have to live in it, with map.md pointing at them — which is a move, not a copy, so nothing is
> duplicated and nothing is deleted.
>
> **ALTERNATIVES:**
> — Literally inside map.md, as the words "at the map level" most plainly read: no new file, but the rules stay in
> the one file the checker may not read, so the manager keeps transcribing them by hand, and the saving you approved
> falls from ~41% to ~31%.
> — One shared sibling with the manager's material: cheapest, one file instead of two, and node 139 needs no
> correction — but the checker then reads the fog, the dogfood target and accounts of what happened elsewhere in the
> record, or the manager hand-selects again.
> — Keep the rules in map.md and let the checker read map.md: single source, no new file, and it ends the checker's
> blindness to the record, which is a far larger change than this node and would cost you the independence the
> checker exists for.
> — Change nothing structural and just ban the one skill by name: least work, and it leaves in place the thing you
> objected to — a rule the checker finds for itself, which nobody can edit.

***The manager's note beside it, and not the worker's.***

**Its point 3 is a raise about another node's acceptance condition, and the manager is carrying it as such rather than
acting on it.** A condition that is wrong goes to the human; it is not the manager's to amend and not this worker's to
rewrite. **The manager verified the one fact the timing turns on** rather than taking the worker's word: `git status`
in `.worktrees/139-map-split` returns nothing and `git diff` is empty, so node 139's worker has written no byte. That
was true at the moment of writing and is not guaranteed to hold.

**Its point 1 cites the manager's own failure accurately.** The manager recorded that failure on node 133 and named
it in the spawn as *"one data point about the status quo, not an argument for any option"*. The worker used it as
one, which is what it was offered as.

**The manager takes no view on the ask or on any alternative**, and has not weighed the two-files-versus-one
argument.

### Attempt 1, a reply that names a node other than the one asked — recorded, not read

**The human's word, `verbatim`**, written at the moment they spoke:

> 139 ok

***The manager's note.*** **The live question was this node's, and the reply names [node
139](139-move-the-managers-material-out-of-the-map.md).** Under [node 117](117-questions-sent-in-batches.md)'s rule
an unnamed question is **unanswered rather than parked**, and the manager's own contract says that where a terse
reply does not make clear which option it points at, the manager records it and asks which rather than picking. **So
nothing is settled by it and it has been put back to them.**

**The two readings, which are not variants of one act but opposites.**

1. **It means this node's question**, `138` mistyped as `139`, taking the recommendation. Then the checker's and
   implementer's material goes to **its own** new file, and **node 139's acceptance condition is wrong** — its clause
   3 moves the review-route paragraph into the manager's file, which under that answer is the wrong destination.
   Amending it is the human's act, not the manager's.
2. **It means node 139 itself** — *carry on, that node is fine* — in which case node 139's condition stands
   untouched, this node's question is still open, and node 140 is still unstartable.

**Reading 1 changes a live node's condition; reading 2 leaves it alone.** The manager has done neither and has told
node 139's worker nothing, its condition standing exactly as written.

**Why the manager is not guessing even though the payload was about node 139's collision.** The payload named node
139 four times, so a reply naming 139 is as consistent with *"that node is fine, proceed"* as with *"take the
recommendation"*. The manager holds both readings and neither is weaker.

### Attempt 1, answer 1 — the recommendation taken

**The human's word, `verbatim`**, written at the moment they spoke, in answer to the manager's question about which
node their previous reply named:

> 138 recommendation taken

**Reading 1 above is theirs.** The recommendation it settles, quoted in full and attributed to this node's worker
rather than to the manager:

> Into ITS OWN new file beside map.md, separate from the manager's file, holding the standards list, the bar's
> commands and the landing policy, read directly by the checker and by the implementer, with map.md keeping a
> one-line pointer. The review-route paragraph moves here rather than into node 139's manager file, and its operative
> list is separated from its story — the part recording that two earlier checkers burned their biggest cost finding
> these standards stays with the manager or goes to map-history.

**No divergence.**

***The manager's note. One measured consequence the worker did not have, and it breaks another node's condition.***

**Taking this answer makes [node 139](139-move-the-managers-material-out-of-the-map.md)'s clause 7 unsatisfiable.**
The manager measured the five bodies clause 3 moves, in the tree node 139's worktree was cut from:

| body | bytes |
| --- | --- |
| `**The review route for this repo, discovered on first use**` | 1,589 |
| `**The dogfood target is` | 743 |
| `**Label vocabulary for this effort` | 455 |
| `## Not yet specified` | 7,797 |
| `## Out of scope` | 2,347 |
| **total** | **12,931** |

`map.md` is **43,707** bytes. Clause 7 demands it end **at least 12,000 bytes smaller**, and clause 4 adds a pointer
of up to three lines back. Moving all five clears the floor by a few hundred bytes. **Moving four — the review route
now belonging to the checker's file rather than the manager's — leaves 11,342, which is below the floor and cannot be
reached by any other means the condition permits.**

**The manager has amended nothing and invented no number.** Adjusting the floor would be the manager authoring the
standard node 139 is judged against, which is not the manager's. The question is put back to this node's worker,
which raised the collision and holds the surrounding decision, so that whatever repair reaches node 139 is phrased by
an agent rather than by the manager.

### Attempt 1, question 2 — delivered

*Pasted as the worker wrote it. The manager authored none of it and has taken no view.*

> **NODE:** Where the rules a checker is held to live, now that it may not go and find them
>
> **ABOUT:** Your last answer settled where the checker's and implementer's rules live. What is still open on this
> node is whether directions like that one change the workflow's shipped skill files, or only bind this effort —
> which an agent settled on your behalf once already and flagged for you to revisit.
>
> **SO FAR:**
>
> **FIRST, THE HOUSEKEEPING YOUR ANSWER TRIGGERED — three lines, then I move on.** I was told your answer had broken
> the node that is moving material out of the map, because a size floor in it could no longer be met. I measured the
> tree instead of taking the figures, and it had not: that worker had already finished the move while you were
> answering, all five bodies including the review route, taking the map from 43,847 to 31,481 bytes and clearing its
> 12,000-byte floor by 366. So nothing needs amending, nothing needs a new number, and your answer cost that worker
> nothing. The review-route paragraph is sitting in the manager's file for now and the next node lifts it into the
> checker's file, which is the end state you approved. I have written that next node's missing clause and will hand
> it over with the rest. I also found one thing nobody owns — the standards list points at rules that live in the
> map, which the checker may not read — and that is a new node rather than something I fold in quietly. All of that
> is the manager's business, not yours.
>
> **NOW THE QUESTION.** A while back you fixed how a standing rule of yours travels. Your words: *"Write it in the
> map first. In efforts in other projects it will be only in the map as there will be no modifying the skills. For
> this effort, I can say to add a rule to this effort or to create a node depending on if I want it to be for the
> effort only or to change the skill itself."*
>
> You named two acts you can take. You did not say what happens when you take neither, and the worker that wrote that
> answer settled it for you — silence means the rule binds this effort and never reaches the shipped files — and
> raised a flag saying so, precisely so you could revisit it. This is me revisiting it.
>
> **SINCE THEN, THREE DIRECTIONS OF YOURS HAVE ARRIVED WITH NO SCOPE ATTACHED**, and the manager wrote all three into
> the map as this effort's alone without asking: that the shipped skill must not depend on the mattpocock plugin;
> that the checker must not go hunting for its own rules; and that the docs discipline should be packaged so nothing
> depends on it. Each of those names a shipped file as its subject.
>
> **WHY THE DEFAULT MISFIRES ON EXACTLY THESE.** Under it, the shipped checker contract still has a whole section
> telling every checker to go and find a reviewing skill and hold the work against whatever it found. This effort's
> map now forbids that. Both are in force, so every single time the manager starts a checker it has to override the
> contract by hand — and the graph's own rules class that override as something that must be put to you each time,
> not done quietly. An hour ago it went wrong in exactly that way: a checker was started under time pressure, told
> something untrue about which standards had moved, and went off and ran the mattpocock code-review skill by the very
> route you barred. **A shipped contract that has to be contradicted in every spawn is a shipped contract that is
> wrong.**
>
> **WHAT I SETTLED MYSELF, coming back as flags:** that the implementer is pointed at the new rules file rather than
> handed its text (two resolved decisions already fix that context travels as pointers, and copying it would load the
> manager instead); and that the review route may pass through the manager's file on its way to the checker's, since
> you fixed the destination and not the route.
>
> **ASK:** When a direction of yours names a shipped file as its subject and you do not say which you meant, should
> the manager read it as reaching that file — rather than filing it as this effort's alone, as it has now done three
> times?
>
> **RECOMMENDED:** Yes, narrowly: keep your rule exactly as it is, with one exception — where the thing your
> direction is *about* is a file the workflow ships, silence means it reaches that file, and the manager may not
> quietly confine it to this effort's map. Everything else stays as you set it: on a project where the skills are
> never touched, a rule of yours still lives in the map and nowhere else, because there is nothing else for it to
> reach.
>
> It rests on three things. Your stated ground for the checker direction — *"it is easier to change the rule when its
> in a file than when the checker finds stuff by itself"* — is a fact about checkers, not about this repo, so
> confining it here throws away the general thing you were saying. The exception only bites on this effort, whose
> subject is the workflow itself, so it changes nothing about how you work elsewhere. And it fixes the failure mode
> rather than the instance: the manager has now mis-scoped three of your directions in a row without noticing, and
> the cost of being wrong is a shipped file that says the opposite of what you asked for.
>
> Two consequences, so you are choosing with them in view. The checker's contract loses its "go and find the rules"
> apparatus and is handed them instead — I will put the replacement to you as my next question rather than deciding
> it. And the plugin direction's shipped half turns out to be already done, so what is left of it is the separate
> question of whether it also reaches this effort's own never-shipped writing standard, which stays with the node
> that owns it and which I am not touching.
>
> **ALTERNATIVES:**
> — Leave your rule untouched and declare each direction as it arrives: safest, nothing changes, but it puts a
> question in front of you every time you give an instruction, which is the exact cost your rule was written to
> avoid.
> — Keep the default as it stands: cheapest for you now, and it leaves the shipped checker contract permanently
> contradicting this effort's map, with the manager overriding it by hand in every spawn — the thing that already
> failed once.
> — Let the manager judge which of your directions are about the workflow and ship those: fastest, and it is the one
> thing your rule explicitly forbids, on the ground that the manager must never present its own judgement as your
> instruction.
> — Reverse the default outright, so silence always ships: wrong everywhere else, since on other projects the skill
> files are never modified, and it would turn every passing remark into a change to the product.

***The manager's note beside it, and not the worker's.***

**Its housekeeping paragraph corrects the manager, and the correction is accepted.** The manager raised that taking
this node's answer would make node 139's clause 7 unsatisfiable, and put the phrasing of a repair back to this
worker. **That was a conditional that was true when written and moot within minutes**: node 139's worker finished
while the human was answering, moving all five bodies including the review route, and clearing the floor by 366
bytes. The manager sent a second message retiring the question. **The worker did not rely on either message and
measured the tree**, which is the right instinct and is recorded as such.

**Its ask reaches a flag the manager filed and never surfaced.** The default it names — silence means effort-only —
was settled by [node 93](93-effort-scoped-custom-rules.md)'s worker and flagged there for the human to revisit.
**The manager has since applied that default three times without once naming it to them.**

**The manager takes no view on the ask or on any alternative.**
