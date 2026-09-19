# Review the priority list the human committed, and decide how much of it the shipped contract carries

Type: grilling
Status: resolved

Blocked by: none

## Question

*Minted by the manager on the human's direction. The question below is the manager's own; the direction in it is
theirs.*

The human committed a `## Priority` section into `.claude/rules/expedition-triggers.md` at commit `70ac77c`, *Add
priority to rule*, and then directed that it go further.

**Their words**, `verbatim`:

> I did a commit to add a priority to the rule, I think it should be added to the skill also. It seems like a
> simpler thing to follow and should remove a lot of one time rules on when to do things. At the same time, it
> should be reviewed to check I didn't do any mistake

**The list as they committed it**, from `.claude/rules/expedition-triggers.md`:

> ## Priority
>
> - Writing info to files (writing what is supposed to be written)
> - Resuming a task
> - Spawning a new task (respecting the limits)
> - Giving an question to the user
> - Waiting (all subagents are working)

The same commit also added a third trigger bullet: *"**The human should have one thing to do**, if the human has
nothing to do and there is a question/gate, give it to him. Wait for him to answer before giving him a question"*.

**Three things are being asked at once, and only the first two are this node's.**

1. **Is the list right?** They asked to be checked. It is an ordering over acts the manager performs, and the
   contract it would join already states orderings that may or may not agree with it — the human's queue and its two
   tiers, the never-idle rule, the rule that the graph is written the moment the human speaks, and the unresolved
   collision the contract already names between arrival order and the cost of a waiting gate.
2. **How much of it ships, and in place of what?** Their stated ground is that it is *"a simpler thing to follow"*
   that *"should remove a lot of one time rules on when to do things"* — so the value claimed is a **deletion**, and
   what it would delete has to be named before it can be judged. A priority list added beside every rule it was
   meant to replace makes the contract longer rather than simpler.
3. The write itself, which is a separate implementation node this one surfaces.

**Why this is grilling rather than implementation.** Both halves need the human. Reviewing a rule *they wrote* and
finding it wrong is a proposal they must accept — and this effort's map settles that a decision of theirs may be
proposed for change on the same footing as one the workflow made, so the reviewing worker is not to soften its
finding on the ground that the rule is theirs. And deciding which existing rules the list replaces is a scoping act
on the shipped contract, which the manager does not perform on its own judgement.

## The manager's note at filing

*Not a change to anything above.*

**The manager has reviewed nothing and holds no position on whether the list is right.** It records only what it
already holds, from having worked under the list for this whole session: the list resolved every ordering question
the manager met, and the manager never had to reach past it. That is one session's evidence from the party the rule
governs, and it is not a review.

**One thing the manager did notice while working and has not judged**, offered as material rather than as a finding:
the third new trigger bullet and the list's fourth item both bear on when a question reaches the human, and the
contract's `## What is in front of the human, and when` section already governs that with a two-tier queue. Whether
those three agree is exactly what this node is for.

**Under the map's rule that a standing rule binds this effort only once written in the map, and reaches a shipped
file only where the human says so:** they have said so here — *"it should be added to the skill also"* — so the
carriage is licensed. What is not settled by that sentence is how much, which is question 2.

## Interview

### Attempt 1 — the questions put to the human

*Pasted as the worker wrote them, in its own order and its own words. **No answer has arrived**, and the payload had
not reached the human when this was written — node 243's raise arrived first and is ahead of it. Banked here so that
a death leaves the worker's work on disk rather than losing it. The attempt's routing key does not survive the
manager's session.*

**ABOUT:** You committed a five-item `## Priority` list into `.claude/rules/expedition-triggers.md` (commit
`70ac77c`) and said it should go into the skill too, that it should "remove a lot of one time rules on when to do
things", and that it should be reviewed for mistakes. This node does the review and decides how much of it the
shipped manager contract carries. It is being decided now because the list is already governing the manager's
behaviour while living in a repo-local file that does not travel to any other repo.

**SO FAR:** I read the list, both of your commits to that file, the shipped manager contract
(`.claude/skills/expedition/SKILL.md`), `graph-conventions.md`, the glossary (`CONTEXT.md`), this effort's map and
its index of decisions.

**The list is sound.** Every item is in the right place and I am recommending no re-ordering. Two things in
particular I checked and found correct rather than wrong:

- *Resuming above spawning* is right and this effort's map already says so on a different ground — a resume hands
  work to an agent that already holds its context, a spawn pays for a cold one, and a resumed worker is one that
  stops sitting blocked.
- *Giving a question ranking below spawning* looks at first like the fault you corrected when you said "Stop waiting
  for me to ask to give the questions", and it is not. What was wrong then was the trigger — the manager was waiting
  for you to speak. Here the trigger is still the payload being ready; it just goes out after a spawn that takes
  seconds. And because spawning is capped by the counts ("respecting the limits"), the manager runs out of spawns
  and the question goes. Your parenthetical is what stops item 4 from starving, and it is doing real work.

**Three findings I am not asking about, reported so you have them:**

- *The list does not settle the collision the contract already names* between arrival order and the cost of a
  waiting gate (whether a finished gate may jump an older question). It cannot: that collision is inside item 4, and
  the list ranks classes of act rather than claimants within one. Your third trigger bullet says "question/gate" as
  one thing and does not distinguish them either. I am surfacing that as its own node rather than spending a turn of
  yours on it here.
- *The `## Priority` section breaks the file's own charter.* That file ends with "This file holds triggers only, and
  overrides nothing there" — a sentence that was put there deliberately, under an acceptance condition. A priority
  is not a trigger, and a priority that resolves a contradiction does override. The repair rides in Q2.
- *Your earlier commit `a70fb82` left the title as "# For a manager acts on"*, truncated from "# Triggers a manager
  acts on". One word, and I will fold it into whichever node writes the file.

**Settled on my own authority:** I read "task" in items 2 and 3 as meaning an *agent* (a worker or a checker), not a
node, since resuming is something you do to an agent. And I did not read `map-manager-only.md` — this effort's map
says no worker reads it — so any collision between the list and manager-only material is unchecked by me.

#### Q1. Is the list right — five corrections before it ships

**ASK:** Do you accept these five corrections to the list and the file around it?

(a) **There is a contradiction inside the file.** The first trigger bullet says a replacement is started "before
anything else continues", and the Priority list puts writing above spawning. One of the two has to give.

(b) **Item 5's condition is not the real one.** "Waiting (all subagents are working)" names a case that is neither
necessary nor sufficient. Concretely: two workers are running, a third worker's question has been sitting in the
queue because your channel was busy, and you have just answered. Every agent is working — and the manager must not
wait, because that queued question is ready and your channel is free.

(c) **Three words are ones this workflow refuses by name.** The glossary refuses `task` twice over (it is also the
harness's own word for something else), refuses `user` for `human`, and refuses `subagent` for `worker`. Plus "an
question" → "a question".

(d) **What the list ranges over is not stated, and the two readings differ.** "Do the higher thing first, then the
lower one in the same turn" against "do the higher thing instead of the lower one". The second starves item 4 for as
long as anything at all is spawnable.

(e) **The same commit deleted a rule the list does not carry.** `70ac77c` removed the bullet "A node resolves, so
its retrospective is filed in the same edit that writes its answer." Item 1 says writing outranks everything but
never says what is owed, so "(writing what is supposed to be written)" points at a list that is not in that file.
The duty itself survives in this effort's map, so nothing is lost for this effort — what is lost is the copy that
survives a compaction, which was the entire reason that file exists.

**RECOMMENDED:** Accept all five.

(a) The Priority wins and the bullet is reworded to "...and a replacement is started as soon as what is owed to the
record is written." Writing first is right on your own contract's ground — the manager's context is the resource
that fails first, and anything unwritten dies with a compaction or a crash. The contract already applies exactly
this ordering in the one place it happens to state it, telling the manager to write your words "at the moment they
speak, in the same turn you resume the worker". Your list generalises a rule the contract had only as a special
case.
(b) "Waiting — and only where nothing above is available."
(c) "Resuming an agent" / "Spawning an agent (respecting the limits)" / "Giving a question to the human" /
"Waiting".
(d) One added sentence: "Every item you can do, you do, in this order — a lower item is never skipped, only deferred
within the same turn."
(e) **Keep it deleted.** It is a genuine instance of the trade the list was meant to make, and the map still holds
the duty. I want you to have chosen it rather than have it happen quietly.

**ALTERNATIVES:** Take them one at a time and reject any — say which.
On (a), keep "before anything else continues" and demote item 1 below item 3 instead: I am against it, because the
thing you lose by spawning first is the record, and the thing you lose by writing first is about four seconds.
On (c), keep your own words on the ground that the file is yours and you read it: I am against it because this
file's reader is the manager, which is held to the glossary, and "task" is the one word the harness already owns.
On (e), restore the retrospective bullet alongside the list.

#### Q2. How much ships, and in place of what

**ASK:** Where does the list land, and what does it replace? Your stated ground for it is that it "should remove a
lot of one time rules on when to do things" — so I went looking for them, and **in the shipped files they are almost
not there.** The entire harvest across the manager's contract and the conventions document is four clauses:

1. "in the same turn you resume the worker, not after it comes back" → becomes item 1 above item 2;
2. "never to a tidy-up afterwards", said twice (raising a flag, settling a flag) → becomes item 1. The other half of
   those rules — "the node first, then the index" — stays, being an order *inside* one write, which the list does
   not reach;
3. "you pick, you spawn its worker, and you send the pick report" → the ordering half becomes item 3;
4. the triggers file's "before anything else continues" → goes either way, per Q1(a).

That is six or seven lines. `graph-conventions.md`'s ten procedures are all orderings *within* one act — which file
to write first — and the list reaches none of them.

**So the list's value in the shipped contract is not deletion.** It is a default for everything nothing covers,
which is what a session of the manager working under it actually evidences: it never had to reach past the list, and
the list never disagreed with anything. That is worth shipping on its own terms — but it is a different claim from
the one you made for it, and I would rather tell you than quietly ship the list under a reason that does not hold.

**Where the deletion you expected does exist is the map, not the skill.** This effort's `map.md` holds at least two
long live rules the list subsumes — "The manager never idles, and *starts* the next work itself the moment a node
finishes", and "A payload goes over as soon as it is ready, and still one at a time". Collapsing those is a real
cut, but it is a never-delete operation on the record with your verbatim words in it, and it is not the same change
as shipping.

**RECOMMENDED:** Ship the list whole into `.claude/skills/expedition/SKILL.md` as a short new section placed right
after `## What is never yours` — that section says what the manager must not do, and this says the order of what it
does. Absorb the four clauses above. **Keep the copy in `.claude/rules/expedition-triggers.md`**, and widen that
file's closing sentence from "holds triggers only" to cover the priority. The two copies are not redundant and each
has a job the other cannot do: `.claude/rules/` is this repo's own and does not travel, so the skill is the only
route by which the list ever reaches another repo — which is what you asked for — while the rules file is the copy
the harness re-injects after a compaction, which a skill read does not survive. Then mint a **separate** node for
the map collapse, so a shipped edit is not held behind a never-delete operation on the record.

**ALTERNATIVES:** Ship it and collapse the map's two notes in the same node — one change, but it couples a shipped
file edit to a never-delete map operation and neither lands until both do.
Ship into the skill and delete it from the rules file — no duplication, but the post-compaction copy goes and that
was the point of that file.
Leave it in the rules file only — it then never reaches another repo, which refuses your instruction.
Fold it into the contract's existing `## What is in front of the human, and when` — I am against it: that section
answers *which claimant goes next*, the list answers *which class of act goes next*, and folding them would lose the
two tiers.

**The human's answer**, `verbatim`: *"Q1. For (a), the logic was that writing and resuming are very simple and very
fast so they should be done first, to spawn a new task, you need to find a new task to spawn for example. What do
you think about it ? For the rest ok Q2. what do you propose ?"*

Three things in one reply, and the manager has treated them as three, answering none of them.

**Q1 (b), (c), (d) and (e) are accepted** — *"For the rest ok"*. The options that takes are the worker's own text:
(b) *"Waiting — and only where nothing above is available."*; (c) the four reworded items using `agent` and `human`;
(d) the added sentence *"Every item you can do, you do, in this order — a lower item is never skipped, only deferred
within the same turn."*; (e) **keep the deleted retrospective bullet deleted**. No divergence on any of the four.

**Q1 (a) is not answered — it is a ground given and a question back.** The human states the reasoning behind their
own ordering (*"writing and resuming are very simple and very fast so they should be done first, to spawn a new
task, you need to find a new task to spawn for example"*) and asks the worker what it thinks of it. It is relayed
unaltered.

**Q2 is a question back too.** The worker's payload carried a `RECOMMENDED` for Q2; the human asks *"what do you
propose ?"*, which the manager has not read as a rejection of it and has not answered. Relayed as written.

### Attempt 1, second payload — the questions put to the human

*Pasted as the worker wrote them. **No answer has arrived**, and the payload had not reached the human when this was
written — two gates were ahead of it. Banked here so that a death leaves the worker's work on disk.*

**SO FAR:** **Settled by your last answer** — four of the five corrections are accepted: item 5's condition becomes
"only where nothing above is available"; `task`/`user`/`subagents` become `agent`/`human`/`worker` and "an question"
is fixed; the list gains one sentence saying it is *do the higher one first, then the lower one in the same turn*
rather than *instead of*; and the retrospective bullet your commit deleted stays deleted, the duty surviving in this
effort's map.

**What is left is two things**: your ground for the ordering, which you asked me to react to, and the shape of the
change, which you asked me to propose.

**On the wording of my last payload** — you asked "what do you propose?" and I had already written a recommendation,
which means it was not findable. That is my error and worth naming: I put five paragraphs of findings inside the ASK
field instead of keeping it to the question, so the proposal sat behind a wall. This one is short.

#### Q1. Your ground for the ordering, and the one bullet still contradicting the list

**ASK:** You said writing and resuming are very simple and very fast so they go first, and that spawning needs you
to find a node to spawn. **I think your ground is right and better than mine, and I am dropping mine in favour of
it** — with one qualification, and then one line of the file still has to change either way.

Your ground is stronger because it explains something mine did not: *where the boundary between items 2 and 3
falls*. Mine was that unwritten context dies with a compaction or a crash, which argues for item 1 being first and
says nothing about resume against spawn. Yours explains the whole run — a write is one edit, a resume is one
message, and a spawn is a *decision* (read the frontier, pick, compose the spawn) before it is an act. And your
ground independently justifies the sentence you already accepted in (d): if the ordering is about what each act
costs, nothing in it can license a cheap act to *replace* an expensive one — only to go first.

**The qualification.** Cost alone does not put item 3 above item 4, and would put them the other way round: giving a
question is cheap, because the worker already wrote the payload and the manager only pastes it. So item 4's position
rests on a second ground rather than on cost — a spawn starts work that then runs in parallel, so delaying it costs
throughput, whereas a question's cost is dominated by your latency and your channel takes one thing at a time
regardless. And the limits are what stop that from starving item 4: spawning runs out, waiting for you does not.

**What is still open** is the thing my (a) was actually about, which your answer settles but does not mention. The
first trigger bullet in that same file says a replacement is started "**before anything else continues**" — spawning
before writing, which is the opposite of your list. Your own ground decides it against the bullet.

**RECOMMENDED:** Reword that bullet to: "**A node finishes**, so the frontier is looked at and a replacement is
started as soon as what is owed to the record is written." And state the list's ground in one line where it ships,
as two grounds rather than one — ascending cost for items 1 to 3, and throughput bounded by the limits for item 3
above item 4 — because a rule whose reason is written down is the one that survives being edited by someone who was
not here.

**ALTERNATIVES:** Keep the bullet as it is and move item 1 below item 3 — I am against it and so is your own ground.
Reword the bullet but ship the list without any statement of its ground — shorter, and it leaves the next person to
re-derive why 3 sits above 4, which is the one step in the list that is not obvious.

#### Q2. What I propose

**ASK:** Do you approve this shape? It is four pieces of work, and only the first is a change to a shipped file.

1. **The list ships into `.claude/skills/expedition/SKILL.md`** as a new short section, placed immediately after
   `## What is never yours` — that section says what the manager must not do, this one says the order of what it
   does. It carries the five corrected items, the scope sentence, and the one line of ground from Q1.
2. **Four clauses in that contract are absorbed into it** and deleted: "in the same turn you resume the worker, not
   after it comes back"; "never to a tidy-up afterwards", which appears twice; and the ordering half of "you pick,
   you spawn its worker, and you send the pick report". The other half of the flag rules — "the node first, then the
   index" — stays, being an order inside one write, which the list does not reach.
3. **The rules file keeps its copy**, because it is this repo's own file and does not travel, so the skill is the
   only route by which the list reaches another repo, while the rules file is the only copy that survives a
   compaction. Its closing sentence widens from "holds triggers only" to cover the priority, its first bullet is
   reworded per Q1, and its title is repaired.
4. **Two separate nodes**, neither of them this work: collapsing the two long when-to-do-things items in this
   effort's map that the list now subsumes, which is a never-delete operation on the record and should not hold a
   shipped edit behind it; and the collision the list turned out not to settle — whether a finished gate may go
   ahead of an older question.

**RECOMMENDED:** Approve it as one implementation node covering pieces 1 to 3 (one file set, one gate), with piece 4
minted as two nodes I hand back. I am recommending 1-to-3-as-one because the three files disagree with each other
today and landing them separately leaves a window where they contradict.

**ALTERNATIVES:** Split piece 3 off as its own node — the rules file is yours and you may want it separately
reviewable; I am mildly against it, for the contradiction window above.
Do pieces 1 to 4 as one node — I am against it: it couples a shipped edit to a never-delete map operation and
neither lands until both do.
Ship piece 1 only and leave the four clauses standing — the list is then added beside the rules it was meant to
replace, which is the failure your own stated value for it names.

**The human's answer**, `verbatim`: *"Q1 ok Q2 ok but the rule will ship as optional"*

**Q1 and Q2 are both accepted.** The options that takes are the worker's own text: on **Q1**, rewording the first
trigger bullet to *"**A node finishes**, so the frontier is looked at and a replacement is started as soon as what
is owed to the record is written"*, and stating the list's ground in one line where it ships as two grounds rather
than one. On **Q2**, the four-piece shape, worked as one implementation node covering pieces 1 to 3 with piece 4
minted as two nodes. No divergence on either.

**The trailing clause is a qualification the manager has not interpreted.** *"but the rule will ship as optional"*
is the human's own addition, offered against neither an option the worker named nor an alternative it listed, and
the manager has neither construed *which* rule nor what *optional* makes true of the shipped text. It is relayed to
the worker unaltered, which holds the interview.

### Attempt 1, third payload — the question put to the human

*Pasted as the worker wrote it. **No answer has arrived** when this was written. Banked here so that a death leaves
the worker's work on disk.*

**SO FAR:** **Settled.** The five corrections to the list are accepted. The ordering ships on your ground —
ascending cost for items 1 to 3, plus throughput for item 3 above item 4 — and the trigger bullet that contradicted
it is reworded. The shape is approved: one implementation node ships the list into the manager's contract, absorbs
four clauses there, and repairs the rules file; two further nodes are minted separately.

**One correction to something I was told, because it bears on what I write next.** I was told that `.claude/rules/`
does not exist inside a harness worktree, which would have meant no checker could ever verify that file. I checked
both live worktrees directly: the file is present in both, and tracked. So the condition I write can demand that
file's state and a checker can verify it. Nothing in the plan changes; what would have changed is what I could ask
anyone to check.

**What I still need.** You said the rule ships as optional. I read *the rule* as the priority list itself — it is
the thing shipping — and if you meant the trigger bullets or the whole rules file, say so and the rest of this
question drops. I am not settling what *optional* makes true on my own, because it is the difference between two
standards and I am about to write the one the implementation node is held to.

**ASK:** What does *optional* make true of the shipped section — and does it reach the four clauses the same change
deletes?

Three readings, and they are not close together:

**A. An effort may replace it.** The skill ships the ordering as the default; an effort's map may state a different
one; where it does not, the ordering binds.
**B. The manager may depart from it in the moment**, on its own judgement.
**C. The section is advisory** and binds nothing.

The reason this cannot wait until the writing: piece 2 of what you just approved **deletes four clauses that are
mandatory today** and folds them into this section — that the manager writes your words before resuming the worker,
that a flag's two entries are written as part of raising it rather than as a tidy-up afterwards (twice), and the
ordering inside the pick. Under B or C those four stop being requirements at all. Under A they keep their full force
everywhere, and only an effort that writes its own ordering into its map can weaken them.

**RECOMMENDED:** **A.** Three grounds.

It is already this workflow's idiom for everything that varies: how many nodes needing the human run at once, how
many code slots, the landing policy, the bar's commands — each ships as a default and is set by the effort's map.
*Optional* means that here without inventing a mechanism, and an effort that departs leaves a written record of
having done so.

B and C have no register in this contract to sit in. Where its rules pull against each other it tells the manager to
raise rather than improvise, and says in as many words *"Do not invent an answer for one in the moment"*. An
ordering the manager may silently set aside is not a rule, and would not be worth the section.

And A is the only reading under which the deletions are safe. The point of this change was to remove rules rather
than add a list beside them; A lets the four go without anything losing force, where B and C would quietly downgrade
four requirements as a side-effect of a change that was never about them.

Concretely, the section opens with one sentence: *this ordering is the default; an effort may state a different one
in its map, and where it does not, this binds.*

**ALTERNATIVES:** **B** — the manager departs in the moment. Against: it silently downgrades four requirements and
gives the contract a discretion register it has nowhere else.
**C** — the whole section advisory. Same objection, and the deletions would no longer be worth making.
**A, but the four clauses stay where they are too.** Belt and braces; it costs exactly the deletion that was the
point, and leaves one rule stated in two places that can drift apart.
**Something else you meant by optional** — say it and I will build the condition to it.

## Flags

`248.1` `MANAGER-WRONG` — ***Filed by the manager against itself.*** The manager told this worker, and told the
human twice, that **`.claude/rules/` does not exist inside a harness worktree** and that a worker therefore never
sees it. **That is false.** This worker checked both live worktrees and reported the file present and tracked in
each; the manager then verified it directly — `expedition-triggers.md` is present at 1,190 bytes in the worktrees
for nodes 250 and 242, `git ls-files` lists it, and `git status` reports it unmodified. **What the manager actually
observed was one worktree at one moment**: during node 244's landing, `git worktree remove` reported that file as
deleted and `ls` found no `.claude/rules/` directory there, and the same appeared for node 166's worktree. The
manager generalised one observation into a property of every harness worktree, stated it as measured fact in a spawn
and in two reports to the human, and **still does not know why those two worktrees differed** — it has not
established the cause and is not guessing at one here. The cost: this worker was told a fact that would have
narrowed what its acceptance condition could demand a checker verify, and it only escaped by checking.

**The human's answer**, `verbatim`: *"The fact that it is optional explains why the priority it is put also in the
skill. It is a reminder for the agent that stays across compaction."*

**It names none of the three readings the worker offered**, and the manager has construed nothing. It states a
ground rather than a choice — why the list is in the skill as well as in the rules file — and the worker holds the
interview. Relayed unaltered.

## Answer

*The worker's own text, pasted.*

**The list is right, it ships into the manager's contract whole, and what it displaces there is two clauses rather
than the "lot of one time rules" it was expected to remove.**

### 1. Is the list right?

Yes. The ordering is sound at every position and none of it is re-ordered. Five corrections were put to the human
and accepted:

- **Item 5's condition was not the real one.** "Waiting (all subagents are working)" names a case that is neither
  necessary nor sufficient: two workers can be running while a queued question is ready and the human's channel is
  free, and the manager must not wait then. It becomes **"Waiting, and only where nothing above is available."**
- **Three words are refused by name in `CONTEXT.md`.** `task` is refused twice over and is also the harness's own
  word for something else; `user` is refused for `human`; `subagent` for `worker`. The items become *resuming an
  agent*, *spawning an agent*, *giving a question to the human*. "An question" is fixed.
- **What the list ranges over was unstated**, and the two readings differ: *do the higher act first, then the lower
  one in the same turn* against *do the higher act instead*. The second starves item 4 for as long as anything is
  spawnable. One sentence is added: **"Every item you can do, you do, in this order — a lower item is never skipped,
  only deferred within the same turn."**
- **The file contradicted itself.** Its first trigger bullet says a replacement is started "before anything else
  continues" — spawning before writing, the opposite of the list. The list wins and the bullet is reworded.
- **The same commit deleted a rule the list does not carry.** `70ac77c` removed the bullet *"A node resolves, so its
  retrospective is filed in the same edit that writes its answer."* Item 1 ranks writing first but never says what
  is owed. The deletion stands — the duty survives in this effort's map, and it is a genuine instance of the trade
  the list was meant to make — but it is now a chosen deletion rather than an incidental one.

**The ground for the ordering is the human's own, and it is better than the one this node first proposed.** Their
words, `verbatim`: *"writing and resuming are very simple and very fast so they should be done first, to spawn a new
task, you need to find a new task to spawn for example."* That explains where the boundary between items 2 and 3
falls — a write is one edit, a resume is one message, and a spawn is a decision before it is an act — which the
durability argument this node opened with (unwritten context dies with a compaction) does not. It also independently
justifies the scope sentence above: if the ordering is about what each act costs, nothing in it can license a cheap
act to *replace* an expensive one, only to go first.

**Cost alone does not put item 3 above item 4, and would invert them**, a question being cheap to send because the
worker already wrote the payload. Item 4's position rests on a second ground: a spawn starts work that then runs in
parallel, so delaying it costs throughput, while a question's cost is dominated by the human's latency and their
channel takes one thing at a time regardless. The limits on spawning are what stop item 4 from starving. Both
grounds ship with the section, because the step that is not obvious is the one a later editor will get wrong.

**Two things the list does not do, established rather than assumed:**

- **It does not settle the collision the contract already names** between arrival order and the cost of a waiting
  gate. It cannot: that collision sits *inside* item 4, and the list ranks classes of act rather than claimants
  within one. The third trigger bullet says "question/gate" as one thing and does not separate them either. Reported
  as a new node.
- **It does not conflict with `## What is in front of the human, and when`.** The two answer different questions —
  the queue says *which claimant goes next*, the list says *which class of act goes next* — and the third trigger
  bullet states the one-at-a-time rule that both assume. All three agree.

### 2. How much ships, and in place of what?

**The whole list ships into `.claude/skills/expedition/SKILL.md`**, as a new section placed immediately after
`## What is never yours` — that section says what the manager must not do, this one says the order of what it does.

**What it displaces there is two clauses.** This node searched the manager's contract and `graph-conventions.md` for
rules that say *when* to do a thing relative to another. The whole harvest is `SKILL.md`'s "in the same turn you
resume the worker, not after it comes back" and its "never to a tidy-up afterwards". `graph-conventions.md`'s ten
procedures are orderings *inside* one act — which file to write first — which the list does not reach, and it loses
nothing.

**So the stated ground for the change does not hold, and the change is still right.** The human's value for the list
was that it *"should remove a lot of one time rules on when to do things"*; in the shipped files those rules are
almost not there. What the list is worth there is a **default for everything nothing covers**, which is what a
session of the manager working under it evidences: it never had to reach past the list, and the list never disagreed
with anything it met. That is a different claim from the one the list was offered under, and it is recorded here
rather than absorbed quietly.

**Where the deletion the human expected does exist is this effort's map, not the skill.** `map.md`'s `## Notes` hold
two long live rules the list subsumes — that the manager never idles and starts the next work the moment a node
finishes, and that a payload goes over as soon as it is ready. Collapsing them is a real cut and a never-delete
operation on the record, so it is a separate node and does not hold a shipped edit behind it.

**The rules file keeps its copy**, and its charter widens to admit it. `.claude/rules/` is this repo's own and does
not travel, so the skill is the only route by which the list reaches another repo — which is what the human asked
for — while the rules file is the copy the harness re-injects after a compaction, which a skill read does not
survive. Their words on that, `verbatim`: *"The fact that it is optional explains why the priority it is put also in
the skill. It is a reminder for the agent that stays across compaction."*

**That file contradicts its own charter today** and the repair rides with the shipping node: it says *"This file
holds triggers only, and overrides nothing there"* — a sentence placed there deliberately — while a priority is not
a trigger, and a priority that resolves a contradiction does override. Its title is also a truncation, left as
`# For a manager acts on` by commit `a70fb82`.

`248.2` `ASSUMPTION` — **what *"the rule will ship as optional"* names.** The human's qualification was `verbatim`
*"Q2 ok but the rule will ship as optional"*, and this worker put three readings of *optional* to them — an effort
may replace the ordering, the manager may depart from it in the moment, or the section binds nothing — because the
three produce different standards for the implementation node. Their reply named none of the three and instead
explained why the list sits in the skill as well as in the rules file. This worker settled it as **"the rule" naming
the rules file rather than the priority list**, on four grounds: the human's own commit messages for that file are
*"Add priority to rule"* and *"Improve rule"*, so that file is what they call *the rule*; the causal claim only
works that way round, an optional repo-local file being exactly why the skill must carry the list authoritatively;
*"stays across compaction"* is true of an auto-loaded rules file and false of a skill read, and is that file's
stated reason for existing; and this worker's own question had already offered that escape — *"if you meant … the
whole rules file, say so and the rest of this question drops"* — which is what their answer does. **The
consequence, which is what makes this worth checking:** the priority section ships as an ordinary binding part of
the manager's contract, and the two clauses it absorbs lose no force. Had the other reading been meant, deleting
those two clauses would have silently downgraded two requirements.

`248.3` `ASSUMPTION` — **the count of clauses the list displaces was reported to the human as more than it is.**
This worker told the human the list would absorb "four clauses", including "never to a tidy-up afterwards, said
twice (raising a flag, settling a flag)". Verified against the file before writing the acceptance condition: that
clause appears **once**, on raising a flag only; the settling sentence has no such clause. A third item named — the
ordering inside "you pick, you spawn its worker, and you send the pick report" — is **not** absorbed either, the
list having no item for a report that awaits no answer. The true count in the shipped contract is **two**, plus the
rules file's own contradicting bullet. This worker did not go back to the human for it: they approved a shape, not a
count, and two deletions rather than three sits inside that shape and changes no standard. The acceptance condition
demands only what was verified. **It sharpens the answer's central finding rather than softening it** — the deletion
available in the shipped contract is smaller still.

`248.4` `ASSUMPTION` — **items 2 and 3 of the list range over agents, not nodes.** The list says "resuming a task"
and "spawning a new task". Resuming is something done to an agent rather than to a node, and a checker is spawned by
the same act as a worker, so this worker read both items as ranging over **agents** — a worker or a checker — and
the corrected wording says so. The alternative reading, that they range over nodes, would leave the spawning of a
checker unranked.

`248.5` `ASSUMPTION` — **`map-manager-only.md` was not read, so collisions with it are unchecked.** That file is one
of the two paths the rules file's frontmatter scopes itself to, so it is a plausible site for an ordering rule
colliding with the list. `map.md` declares it a part of the map that no worker reads, and this worker did not open
it. Any collision between the priority list and manager-only material is therefore unchecked by this node, and
checking it is available only to the manager.

## Retrospective

*This effort's own standing instruction, carried in the spawn and shipped nowhere. Pasted as the worker wrote it.*

**1. What I had to hunt for.**

*The actual content of the commit under review.* My node file said `70ac77c` "also added a third trigger bullet". It did not: that bullet came from the earlier `a70fb82`, and what `70ac77c` actually did was **delete** a bullet. I looked at the node file first, then ran `git show 70ac77c` — which should have been step one and was nearly not. **The node file described a diff instead of carrying it.** Quoting the diff, or simply saying "read the commit", removes both the error and my verification.

*That the file had a second human edit at all.* `a70fb82` truncated the title, deleted a trigger, and narrowed the path globs. Nothing pointed me at it; the node's framing — "the human committed a `## Priority` section at commit `70ac77c`" — actively pointed away from it, and I found it only by running `git log` on the file out of habit. Reviewing a file on the strength of one of its two recent commits is reviewing half of it.

*Where the deleted retrospective duty survived.* One grep across `.claude/skills/`, `.claude/rules/` and the map. Cheap, and I would not know how to make it cheaper.

*Whether `.claude/rules/` exists inside a worktree.* One command, after being told it did not.

**2. What arrived that this node did not need.**

*`CONTEXT.md`, read whole — 302 lines for about six entries.* What I went for was the refusals on `task`, `user` and `subagent`; what came with it was the landing, closing, salvage and node-trailer vocabulary, which bore on nothing here. The map already says the `_Avoid_` lines are the operative part, and `grep -n "_Avoid_"` would have given me every refusal in one screen. For a node whose output is prose the whole-file read is defensible; for this node it was not, and **the spawn could say which part of the glossary a node needs — the refusals, or the definitions.**

*`map.md`, read whole.* Six of about twenty-five `## Notes` items were load-bearing, which is an unusually high hit rate for a node about ordering rules and I would not call the read wasted. But the items are **an undifferentiated list**, so a reader looking for "rules about when the manager does things" reads all twenty-five to find five. Sub-headings inside `## Notes` — what binds the human's channel, what binds the record, what binds code — would let most workers read a third of it. That is the cheapest change on this list.

*`decisions.md`, 151 lines for about six.* Judged backwards, it earned its place weakly: I never cited most of it, and it is how I knew that a precedent for a record-changing implementation node existed, and it kept me from proposing things already settled. I am aware node 165 is measuring exactly this by shadowing grilling workers at their first question; as one such data point my vote is **keep, narrowly**.

*The spawn.* Nothing in it was dead weight, which is worth saying because it is not the usual answer. The manager's note that it had worked a session under the list became the evidence for the answer's central claim; its note about the unresolved collision became a finding and a node; its steer that the second question was the sharper one was right. The one line that told me nothing was that `decisions.md` is unscoped — I would have read it flat either way.

**3. What would have made this node easier.**

*The node file should have carried the diff rather than a description of it* — see above. It is the only thing here that produced a false belief.

*The payload shape cost a human turn, measurably.* The contract's multi-question shape has no per-question home for what a question rests on, so findings go into `ASK` and bury the question. The human read my Q2 and asked *"what do you propose ?"* when a recommendation was written directly below. That is a full round trip of the scarcest resource this effort has, spent on formatting. Reported as a node above.

*A worker cannot tell a measured fact from a generalised one.* The manager's worktree claim arrived described as measured twice this session and was a generalisation from a single observation. It cost me one command; had I taken it, I would have narrowed an acceptance condition on a false premise and a checker would have had no way to catch it. The spawn convention distinguishes *material* from *conclusion* but not *measured* from *inferred*, and those are the two that matter.

*Four rounds where the contract expects fewer.* Two of the four were spent on my own imprecision rather than on anything the record lacked — one on a buried recommendation, one on a referent I read wrongly. Worth recording as the worker's cost rather than the workflow's.

**4. What I read that was stale, wrong, or contradicted something else.**

- **My node file's claim that `70ac77c` added a third trigger bullet.** False, twice over: the bullet predates that commit, and that commit deleted a bullet rather than adding one.
- **`.claude/rules/expedition-triggers.md` contradicts itself three ways.** Its first bullet's "before anything else continues" against its own `## Priority`; "This file holds triggers only" against a `## Priority` section that is not a trigger; and "overrides nothing there" against a priority whose whole function is to resolve contradictions. All three are repaired by node 1 above.
- **Its title, `# For a manager acts on`**, is a truncation of `# Triggers a manager acts on`, left by `a70fb82`. Repaired by node 1.
- **`SKILL.md` contradicts itself in two adjacent vocabulary entries** — `worker` says a worker "is resumed in place rather than replaced", `attempt` says "a dead worker is replaced" — and `CONTEXT.md` agrees with the wrong one. Surfaced as node 4 above.
- **The manager's claim that `.claude/rules/` is absent from a harness worktree.** Checked against both live worktrees: the file is present and tracked in each. The manager has since verified this itself and filed it as flag `248.1`; I record it here because it travelled to me as a measured fact and I was within one step of building an acceptance condition on it.
- **`map.md`'s count of `CONTEXT.md`'s entries** (51 entries, 41 `_Avoid_` lines, dated 2026-09-10) — I did not re-derive it and did not use it. The map already says to re-derive rather than trust it, so this is a note that the instruction is working rather than a finding against the number.

## The manager's disposal of the retrospective's record items

*Not the worker's text. Each item naming the record, and what the manager did with it.*

- **The node file describing a diff instead of carrying it, and producing a false belief** → **acted on, not
  minted.** The manager wrote that description and it was wrong: `70ac77c` deleted a bullet rather than adding one,
  and the third bullet came from `a70fb82`. The manager's conduct change is to quote the diff or name the commit and
  stop describing it. **Filed as flag `248.6`** rather than left in the retrospective, because it is a manager error
  that reached a worker.
- **The rules file's frontmatter narrowing, reviewed by nobody** → **not minted**, and annotated onto [node
  218](218-put-the-managers-trigger-duties-where-a-compaction-re-injects-them.md) instead. The manager cannot tell
  whether the human narrowed it deliberately, and minting a node on that premise is the failure flag `160.2`
  already records. **Named for the human.**
- **A spawn distinguishing *material* from *conclusion* but not *measured* from *inferred*** → **not minted, and it
  is the sharpest item in this retrospective.** It is the general form of flags `248.1` and `250.1`, both of which
  are the manager stating an inference as a measurement. The manager has changed its own conduct — it now says which
  it is — but whether the spawn convention should carry the distinction is a question about the workflow, and the
  manager has not decided it. **Named for the human.**
- **`map.md`'s `## Notes` being an undifferentiated list** → **already minted**, as [node
  246](246-map-notes-mixes-what-a-worker-acts-on-with-what-a-manager-acts-on.md). This worker's remedy is different
  from the other eight reports — sub-headings inside `## Notes` rather than a further split — and is recorded here
  for whoever claims that node.
- **`CONTEXT.md` read whole for six refusals** → **not minted.** [Node
  165](165-measure-whether-a-fed-file-earns-its-place.md) is measuring it; this worker explicitly offered itself as
  a data point and voted *keep, narrowly*, on `decisions.md`. Both are recorded here for that node.
- **The multi-question payload shape** → minted as [node
  259](259-a-multi-question-payload-has-no-per-question-ground.md).

`248.6` `MANAGER-WRONG` — ***Filed by the manager against itself.*** This node's `## Question`, written by the
manager, said that commit `70ac77c` *"also added a third trigger bullet"*. **It did not.** That bullet came from the
earlier commit `a70fb82`, and what `70ac77c` actually did to the trigger list was **delete** a bullet — the
retrospective duty — which this node's answer then had to establish and put to the human as its correction (e). The
manager described a diff instead of carrying it, described it wrongly, and pointed the worker at one of the file's
two recent commits, so that the second was found only because the worker ran `git log` out of habit. Its words,
`verbatim`: *"Reviewing a file on the strength of one of its two recent commits is reviewing half of it."*
