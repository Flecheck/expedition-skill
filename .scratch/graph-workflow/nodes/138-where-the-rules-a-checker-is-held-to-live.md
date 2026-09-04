# Where the rules a checker is held to live, now that it may not go and find them

Type: grilling
Status: resolved

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

### Attempt 1, a third payload — written, superseding Q2's framing, and never delivered

*Pasted as the worker wrote it. It arrived while Q2 sat in front of the human, unanswered.*

**Its ask:** *"Do these standing directions of yours reach the shipped skill files, or do they bind this effort
only?"*

**Its recommendation:** *"The checker direction ships — change the shipped checker contract. The plugin direction
needs no election here, being already a statement about what ships; its remaining half stays with the node that owns
it. The third direction, about packaging a docs discipline as a "plugin", stays effort-only for now because the thing
it constrains does not exist yet."*

**Where it reverses Q2, in its own words:** *"Where you say neither, an agent settled it as effort-only and you
approved that. So nothing is broken and nobody overstepped. **This is an invitation to elect, not a repair.**"* Q2 had
said the opposite — that *"the manager has now mis-scoped three of your directions in a row without noticing"* and
that the default *"misfires"* — and recommended changing the default rule rather than electing under it.

**Its alternatives:** effort-only for all three, which is today's default; ship both explicitly, *"honest and tidy, but
the plugin half buys a sentence rather than a change"*; ship the checker direction as a **permission** rather than a
prohibition, a checker discovering standards only where its spawn names none — *"keeps discovery for a repo that wants
it, but leaves the failure you objected to as the default behaviour"*; or defer until the workflow has run on a second
repo.

**What it settled itself, unchanged from Q2:** that the implementer is *pointed at* the new rules file rather than
handed its text, and that the first answer is unaffected by this one — *"the file gets built either way, only its
reader changes."*

***The manager's note.*** **This payload was never delivered and the manager did not deliver it.** Q2 was already in
front of the human, and nothing displaces a live question. **One claim in it the manager could not verify and does
not carry:** that the human *"approved"* the effort-only default. Flag `93.1` is marked settled, which under this
graph's rule means it rode the human's next word rather than that they addressed it; the manager finds no words of
theirs on it. That is a difference between *settled* and *approved* and the manager states it rather than resolving
it.

### Attempt 1, answer to Q2

**The human's word, `verbatim`**, written at the moment they spoke:

> 138 yes

**It reaches the delivered payload, Q2, and takes its recommendation** — quoted in full and attributed to this node's
worker:

> Yes, narrowly: keep your rule exactly as it is, with one exception — where the thing your direction is *about* is a
> file the workflow ships, silence means it reaches that file, and the manager may not quietly confine it to this
> effort's map. Everything else stays as you set it: on a project where the skills are never touched, a rule of yours
> still lives in the map and nowhere else, because there is nothing else for it to reach.

**No divergence.**

***The manager's note, and not the human's words.*** **Their word lands on the payload they were given.** The third
payload above supersedes Q2's framing and they never saw it, so reading their assent onto it would substitute the
worker's later judgement for their word — the failure [node 113](113-whether-the-method-skill-instruction-does-any-work.md)'s
worker named when it faced the same shape and refused it. **The manager has therefore filed this against Q2 and put
the reconciliation back to the worker**, which is the party that changed its mind and the party holding the
interview. The manager has not decided what the two payloads' difference comes to.

## Answer

*Attempt 1's handover, pasted as its worker wrote it. The manager authored none of it.*

**The rules a checker holds work against and an implementer works to live in one file beside `map.md`, named for
those two readers, and they arrive by the spawn rather than by a search. And where a standing direction of the
human's is about a file the workflow ships, silence means it reaches that file.**

### 1. Where the rules live

Their word, `verbatim`: *"138 recommendation taken"*. The recommendation it settles:

> Into its own new file beside `map.md`, separate from the manager's file, holding the standards list, the bar's
> commands and the landing policy, read directly by the checker and by the implementer, with `map.md` keeping a
> one-line pointer. The review-route paragraph moves here rather than into node 139's manager file, and its operative
> list is separated from its story.

*"At the map level"* therefore permits a sibling, and the sibling is **not** the one node 139 built. Two files rather
than one, and the line between them is a test that already exists rather than a new judgement: [node
42](42-checker-spawn-carries-ground-rules.md) fixed that only a standing constraint true of any node's work may reach
a blind checker, never an account of what happened. `map-manager-only.md` is full of accounts by design — the fog,
the dogfood target, what earlier checkers cost. Sharing one file would mean either a checker reading what it is kept
blind to, or the manager selecting by hand again, which is the defect the direction is aimed at.

**The narrow reading was rejected on its own ground rather than on cost.** `map.md` is the one file a checker may not
read, so rules kept there must be retyped into every spawn by the manager — which is not a file you edit, and which
failed within the hour: a checker was resumed with a statement that was not true and went and ran the plugin skill
the human had just barred. The saving is secondary and was measured anyway: the narrow reading drops the approved
split from ~41% to ~31% of the file every worker reads cold on every node.

**Sequencing, decided by the manager and recorded here because it changes where a paragraph sits today.** Node 139
finished and passed its check with all five bodies moved, `map.md` 43,847 → 31,481 bytes. The review-route paragraph
is therefore in `map-manager-only.md` right now and takes one further step in [node
140](140-move-the-implementers-and-checkers-material-out-of-the-map.md). The end state is the one taken above; only
the route to it has two legs.

### 2. Whether a standing direction reaches the shipped files

Their word, `verbatim`: *"138 yes"*, taking the payload's recommendation: **the default stands, with one exception —
where the thing a direction is *about* is a file the workflow ships, silence means it reaches that file, and the
manager may not quietly confine it to the map.**

This **amends [node 93](93-effort-scoped-custom-rules.md)**, which held that where the human says neither, the rule is
the effort's alone. That default is unchanged for a direction about how this effort is run. It no longer holds for a
direction whose subject is a shipped file.

Applying it to the three directions on the record:

- **The checker direction** — *"in the checker, it shouldn't try to find the skill/rules"* — is about
  `expedition-checker/SKILL.md` and `expedition-implementation/SKILL.md` by name. It **reaches both**.
- **The no-plugin direction** is about the shipped skill files and already binds them, which the shipped corpus
  already satisfies. What it does *not* settle is whether it also reaches **ground rule 5**, which is this effort's
  own never-shipped standard rather than a shipped file — the new rule speaks only to shipped files, so it leaves
  that open. [Node 132](132-does-the-plugin-direction-reach-the-efforts-own-bar.md) keeps its question and **its
  blocker on this node is discharged**.
- **The docs-packaging direction** — *"for the doc we should try to put it as a 'plugin' so that the skill can be
  used without it or the doc by itself"* — is about a deliverable the workflow will ship. It therefore **binds [node
  130](130-the-docs-discipline-this-workflow-ships.md)'s output** when that output exists.

**Two corrections this node owes the record, both against itself.**

*First.* A payload of this node asserted that the human had **approved** the effort-only default. They had not. Flag
`93.1` is marked *settled*, which on this graph means it rode their next word rather than that they addressed it, and
node 93 records no words of theirs on it — verified from that node's own text, `flags.md` being closed to a worker.
That claim was the load-bearing sentence in a framing which held that *"nothing is broken and nobody overstepped"*,
and with the claim gone the framing goes with it: their answer is not a reversal of something they had blessed, it is
them speaking for the first time on a default that had been applied to three of their directions in silence. **The
framing they answered was the better one, and this node does not prefer its own.**

*Second, and it is about what this node can attest to.* Two payloads of this node are in its own hold — the
destination question and a later scope question that was never delivered. The payload the human answered *"138 yes"*
to is not among them and its text is not in this worker's context. The answer is binding and is recorded above from
the manager's transcript of it; what this node cannot do is claim authorship of the words they read. Recorded because
a later reader will otherwise assume the node held what it answered for.

### 3. What a checker is given in place of a reviewing skill's procedure

Settled here, because each part follows from the direction or from a resolved node. Only the last part does not, and
it is reported as a node rather than decided.

- **Discovery goes.** The shipped checker contract's *"Find these before you read the work"* and *"Go and find them;
  no name for any of them is fixed here"* are the thing the direction names, and under section 2 the direction
  reaches that file.
- **The standards arrive by the spawn, on either of two routes** — copied in as text, or named as a path the checker
  reads. Both are the human's own words: *"sent by the manager or just read by the checker."* The contract permits
  both and each effort picks; this effort picks the file.
- **Pointing a checker at a rules file does not unblind it.** Its blindness is to **the record** — the reasoning
  behind the work — and never to the standards, which it already reads as files today. This is what makes the wide
  reading safe, and it is why *"just read by the checker"* costs nothing that the narrow reading would have
  protected.
- **A reviewing skill may still be run where a spawn names one, never where the checker found one.** The human barred
  a *generic* skill and barred *discovery*; neither bars a discipline somebody declared. So the contract's rule that
  no part of such a skill may run in an agent handed less than the checker was is kept and stays in force.
- **Where a spawn names no standards at all**, the checker holds the work against the acceptance condition and the
  bar alone and says so in its outcome. Today's contract fills that hole with *"hold the work against whatever rules
  you did find"*, which discovery is what made possible; something has to stand there or a checker on an unfamiliar
  repo has no stated behaviour. Flagged.
- **What is left is a genuine fork and is not settled here.** Removing discovery removes a *procedure* and not only a
  list: the checker is left with sources and no discipline for reviewing against them. Whether the workflow ships one
  of its own is reported below as a node, because it mints a deliverable.

### 4. How the implementer receives the same rules

**A pointer, not the text.** Settled from two resolved nodes rather than asked: [node
12](12-subagent-context-contract.md) established that inbound context travels as file pointers and that the checker
is the single exception, and [node 136](136-the-map-has-grown-back-what-node-59-saved.md)'s answer states *"Pointer,
not copy — copying into spawns would move the cost into the manager's context, which is this effort's first-failing
resource."* The implementer reads files, so *"the rules should also be used by the implementer"* is discharged by
pointing it at the same file the checker reads. That single source retires a defect three retrospectives have
reported: the implementation contract sends prose work to `/coding-principles` and `/naming` while the standard that
actually bites on prose was named only in material the implementer was never pointed at.

### 5. What the standards list still cannot do, and who owns it

The moved review-route paragraph names, as standards, *"this map's standing preferences, ground rules and four
standing rules"*. For a reader that does not read `map.md` those resolve to nothing, and the repair is not one move
but two different things:

- **The ground-rules block and the four standing rules of writing can move.** Both are standing constraints true of
  any node's work, which is node 42's own test for what may reach a blind checker.
- **The standing preferences cannot.** They are the map's universal content, read by every worker, and several of
  them are accounts or steers that node 42's test bars from reaching a checker at all. So that reference is not
  repairable by moving: **it has been wrong as a checker standard since node 42 fixed that test**, and the move
  exposes it rather than creating it.

**This is not node 140's work.** Node 140 is a move; this is an edit to what a standard says, it changes the shipped
checker contract's fifth given, and it must wait for the contract rewrite. It is reported below as its own node, and
node 140's condition holds the paragraph's wording untouched so the two do not contend.

### 6. Where this meets node 130

They are the same question about two bodies of text and they meet at one point rather than overlapping. Node 130 asks
how a docs discipline is packaged so that **nothing depends on it either way**; this node asks how a body of rules
reaches an agent **without the agent going to find it**. Both answers are the same shape — a named thing handed over,
rather than a thing discovered — and both are constrained by ground rule 2, which requires a contract to stand alone
rather than depend on a skill being invocable. The point where they touch is section 3's last bullet: if the workflow
ships its own reviewing discipline, that is a second shipped-discipline deliverable beside node 130's and it should
be packaged the way the human asked node 130's to be. **Node 130 is not answered here and nothing above decides it.**

## Flags this node raised

*Each in the worker's own words. The numbers are the manager's bookkeeping; the worker returned them unnumbered.*

`138.1` — `ASSUMPTION`: **The implementer gets a pointer to the rules file, not its text.** The human's direction
says the rules *"should also be used by the implementer"* and does not say how they arrive. Settled as a pointer, on
node 12's finding that inbound context travels as file pointers with the blind checker as the sole exception, and on
node 136's answer that copying into spawns moves the cost into the manager's context, which this effort measures as
its first-failing resource. The reading set aside: handing the implementer the text, which would make the same bytes
uncached in the manager rather than in the worker.

`138.2` — `ASSUMPTION`: **Where a spawn names no standards, a checker holds work against the acceptance condition and
the bar alone.** Removing discovery removes the contract's current fallback, *"where you find no reviewing skill at
all, hold the work against whatever rules you did find"*, which only discovery made possible. Settled as the stated
behaviour because a checker on a repo whose standards nobody has written down must still be able to return an
outcome, and because inventing standards would break the contract's rule that a property nobody stated is not a
finding. The alternative set aside: making an unnamed standard set a raise, which would stop a check for a condition
the work can perfectly well be held to.

`138.3` — `ASSUMPTION`: **A reviewing skill may still be run where a spawn names one.** The human barred a generic
skill by name and barred the checker going to find one; neither sentence reaches a discipline an effort declares.
Settled as permitted-when-named so that the delegation-blindness rule, which is about any agent a skill spawns, keeps
an object rather than being deleted with the discovery apparatus. The reading set aside: deleting the reviewing-skill
machinery outright, which would also delete a rule nothing else states.

`138.4` — `ASSUMPTION`: **The map's standing preferences are not among the standards work is held against.** The
review route names them as a standard; node 42's test bars an account of what happened from reaching a blind checker,
and several standing preferences are exactly that. Settled as: the two blocks that pass node 42's test move into the
rules file and the wholesale reference to the standing preferences is retired. Decided from node 42's shipped test
rather than from preference, and reported as a node's work rather than done here.

`138.5` — `ASSUMPTION`: **The docs-packaging direction now binds node 130's output, reversing this node's own earlier
election.** An undelivered payload of this node proposed leaving it effort-only because the thing it constrains does
not exist yet. Under the rule the human took, a direction about a thing the workflow ships reaches it, and a
deliverable that does not exist yet is still a deliverable. Recorded as a flag because it reverses a position this
node had put in writing, and because node 130 is open and unclaimed and its worker should not have to discover the
reversal.

`138.6` — `ASSUMPTION`: **The byte floor in node 140's acceptance condition is this node's number.** Node 139's
condition used a floor 931 bytes below what its move could remove; node 140's four bodies measure 4,376 bytes in the
post-139 tree, so the same proportional headroom gives 3,900. It is a floor that cannot be reached by trimming, only
by moving, which is what makes it a check rather than a target.

`138.7` — `ASSUMPTION`: **A worker cannot tell a settled flag from an approved one.** This node asserted in a payload
that the human had approved a default when the flag recording it was merely *settled* — it rode their next word. The
distinction is load-bearing and a worker cannot check it, `flags.md` being closed to workers by every contract, so
the error is reachable by any worker that reasons from a flag's state. Settled as: a worker states what a node's own
text shows and never that the human approved something unless their words are on the node.

## Nodes this node surfaced

- **1** → [node 143](143-rules-arrive-by-the-spawn-never-by-a-search.md), implementation, eleven clauses.
- **2** → **not a new node.** The completed acceptance condition for [node
  140](140-move-the-implementers-and-checkers-material-out-of-the-map.md), filed there as a supersession of the
  partial text its original author left.
- **3** → [node 144](144-make-the-rules-file-stand-alone.md), implementation, blocked by 140 and 143.
- **4** → [node 145](145-whether-the-workflow-ships-its-own-reviewing-discipline.md), grilling.
- **5** → [node 146](146-graph-conventions-map-rules-name-two-notes-sections.md), implementation, blocked by nothing
  now that node 139 has landed.

## What this node's work invalidates

*Pasted as the worker wrote it.*

> **[Rules added to one effort's map, and what makes them legitimate](93-effort-scoped-custom-rules.md)** — resolved,
> and its section 3 holds that *"Where they say neither, the rule is this effort's alone"*, with flag `93.1` settling
> silence as meaning map-only. The human's answer here carves an exception out of it: where the thing a direction is
> about is a file the workflow ships, silence means it reaches that file. Node 93's reasoning survives for every
> direction about how an effort is run, which is the ordinary case it was written for; its unqualified statement of
> the default does not.
>
> **[Subagent context contract](12-subagent-context-contract.md)** — resolved, and its per-type table gives the
> checker *"the acceptance condition as extracted text, the bar, and the diff. Nothing else"*, with the note that the
> checker *"is the one worker whose payload cannot be a pointer"*. Both clauses are now false: the checker may be
> given a path to a rules file and read it. The ground the note rests on is narrower than the note — pointing a
> checker at the **record** would unblind it, pointing it at a **standard** does not, and it already reads standards
> as files. Node 42 had already made *"nothing else"* false by adding a fifth given; this is the second time that row
> has moved.
>
> **[The checker's spawn carries the effort's ground rules](42-checker-spawn-carries-ground-rules.md)** — resolved,
> and its answer states that the ground rules are *"copied into the spawn rather than pointed at"* because *"anything
> the map holds that bears on your check reaches it only as words in the spawn"*. Once the ground rules live in a
> file the checker reads, that reason no longer holds and the copy is redundant. **Node 42's test is untouched and is
> load-bearing throughout this answer** — what is superseded is the delivery mechanism it chose, not the boundary it
> drew. New node 3 above is where this lands.
>
> **[`map.md` has grown back most of what node 59's restructure
> saved](136-the-map-has-grown-back-what-node-59-saved.md)** — resolved, and its answer classifies the review route as
> the manager's material on the ground that *"the checker never reads the map at all"*. Under this answer the review
> route is the checker's own and moves to the file it reads. The classification moves; the measurement behind it, and
> the admission test it produced, stand.

## Retrospective — attempt 1

*Pasted as the worker wrote it.*

**1. What I had to hunt for.** (a) **The actual state of node 139's worktree.** I was told its worker had written
nothing and had a table of what remained to move. The tree said otherwise: the split was finished,
`map-manager-only.md` existed at 14,314 bytes, and the 12,000-byte floor was already met at −12,366. The fact that
mattered was one `git -C <worktree> status` and I nearly missed it, because my first attempt used `cd` inside a
compound command, the `cd` silently did not take, and git reported the *main* tree as clean. **Every conclusion I
drew in that turn was against the wrong directory until I re-ran it with `-C`.** Two protections caught it: the file
sizes did not add up, and the headings did not match. Neither was a check I was told to run. (b) **The bodies' byte
sizes**, which nothing records, by `grep | wc -c` against the post-139 tree. (c) **Whether `map-manager-only.md`
carries its own `## Notes`**, which decides a clause I wrote — one grep, and nothing pointed me at it.

**2. What I read and did not use.** Node 12 in full, 326 lines, for one table row and three sentences — but it was
the single most load-bearing thing I read, so the cost was right. Node 93 in full, 267 lines, for section 3 and one
flag's marker. Node 42 in full for one test and one paragraph. `decisions.md` I grepped rather than read on the
spawn's advice: 13 lines returned, 4 used, and it worked exactly as promised — that instruction saved the most for
the least. The implementation contract I read whole and used two paragraphs of, though I could not have known which
two in advance.

**3. What would have made this node easier.** In the spawn: nothing about the node itself, which was well-prepared
and told me what it held no view on. What cost me most was **being told the state of a sibling node's tree instead of
being told to look** — three of the four facts I was handed about node 139 were stale or wrong by the time I read
them (its worker's progress, `map.md` at 43,707 against a measured 43,847, the review-route paragraph at 1,589
against a measured 1,595), and the one that mattered was wrong in a way that would have made me phrase an amendment
to a condition that needed none. A single line saying *the tree is authoritative, go measure it* would have replaced
all of it. **In the graph:** no file records `map.md`'s size over time, which is the number this effort's
most-prioritised concern turns on — reported by node 136's worker too, and still nobody's.

**4. What was stale, wrong, or contradicting something else.** (a) The report that node 139 had written nothing,
against a finished and passing worktree. (b) **My own claim that the human had approved the effort-only default**,
which they had not — I read a flag marked *settled* as a flag they had spoken to, and a worker cannot check that,
`flags.md` being closed to it. It was the load-bearing sentence in a framing I now think was worse than the one they
answered. (c) A payload attributed to this node whose text is not in my context and which I cannot attest to
authoring, recorded in the answer rather than resolved. (d) The checker contract's `Five things, in the spawn:`
against node 12's `Nothing else`, which node 42 falsified and nothing reconciled. (e) The map still names `/grilling`
and `/domain-modeling` as skills every session should consult while both are registered under the plugin the shipped
files must not depend on — reported by nodes 69, 110, 116 and 136's worker before me, and now a fifth time.

***The manager's note on the retrospective, and not the worker's.*** **Its 3 is the sharpest correction of the
manager on this graph so far, and the manager accepts it whole.** Three of the four facts the manager handed it about
node 139 were stale by the time it read them, and the one that mattered — that node 139's worker had written nothing
— was wrong in a way that would have had it phrase an amendment to a condition that needed none. **The manager was
reporting a sibling node's state instead of telling it the tree was authoritative.** Its own prescription is one
line, and the manager has none of it written anywhere.

**Its 1(a) names a failure mode the manager has hit twice this session in its own shell** — `cd` inside a compound
command silently not taking, so a command reports on the wrong directory. The worker caught it by arithmetic that
did not add up rather than by any check it was told to run.

**Its 4(b) and flag `138.7` are one finding and it is about the graph rather than about this worker.** A flag marked
`[x]` on this graph means it **rode the human's next word**, not that they addressed it — and `flags.md` is closed to
every worker by every contract, so no worker can check which. The distinction is load-bearing and unreachable from
where a worker stands.

## An annotation filed by the manager after this node resolved

*Not a change to the answer above. Filed from [node
145](145-whether-the-workflow-ships-its-own-reviewing-discipline.md)'s `INVALIDATIONS`, in that worker's own words.
**The node format defines no section for an annotation onto a resolved node** — that hole is [node
79](79-annotation-section-is-undefined.md), and this heading follows the ad-hoc precedent already in this file rather
than settling it.*

> **[Where the rules a checker is held to live](138-where-the-rules-a-checker-is-held-to-live.md)** — resolved, and
> its section 6 holds that *"if the workflow ships its own reviewing discipline, that is a second shipped-discipline
> deliverable beside node 130's and it should be packaged the way the human asked node 130's to be."* The antecedent
> is now satisfied and the consequent is false: the workflow ships one, and it is a section of a contract that
> already ships rather than a separately-installable thing, so the packaging direction does not bind it and node
> 130's count is unchanged. **Everything else in node 138's section 6 stands** — the two questions still meet at one
> point, both answers are still the same shape (a named thing handed over rather than discovered), and both are still
> constrained by ground rule 2. This node's own `## The manager's note at filing` carries the same sentence and is
> falsified with it.
