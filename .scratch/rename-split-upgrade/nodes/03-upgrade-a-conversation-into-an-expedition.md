# How a conversation that is not an expedition is upgraded into one

Type: grilling
Status: resolved
Labels: UPGRADE

## Question

The human wants to turn a conversation already under way into an expedition when they see the work is
too complex or is several tasks, and then split the work. What does that upgrade do? Settle at least
the following. How it is invoked, and whether the conversation's own thread becomes the manager. What
from the conversation is carried into the effort's record, and in whose words, given that the
conversation may already be large or compacted. How work already done or in progress in the
conversation, such as uncommitted changes, becomes nodes. How the upgrade relates to the two ways of
starting an effort that exist today: from a conversation with the human, and adoption from a directory
of work that already exists. The human links this to several deliverables in one effort, which node 02
settles.

## Answer

A conversation that was not started as an expedition is turned into one by a dedicated skill, `/expedition-upgrade <request>`. The human answered Q1 to Q6 across two payloads. Q1 and Q2 of payload 1 departed from the recommendation, and the human's replies reshaped them. The points marked as assumptions are the worker's own, and each is flagged.

**How it is invoked, and who manages (Q1).** The human invokes `/expedition-upgrade` in the conversation, with a request as its argument. The skill holds every step that only an upgrade needs, and it first tells the thread to read the manager contract, `expedition/SKILL.md`. The conversation's own thread becomes the effort's manager. From the upgrade on, it does no node's work itself. When its context grows heavy, the human either ends its session with `/expedition-stop` or compacts it. The human said, verbatim: *"I would guess an /expedition-upgrade as I feel like there will be logic only relevant for upgrade ? Or put the information in another file than the main /expedition to not split it ? For when the context gets heavy, I can do expedition-stop or just compact the context."* Their answer to the question that followed was *"Q1 ok"*.

**What the request carries.** The request given at invocation names the destination and the deliverables. It also names either a new effort or an existing one. Where the request leaves the destination, whether the effort is expected to reach it, or the deliverables unstated, the manager asks the human rather than writing them itself (assumption).

**What is carried into the record, and in whose words (Q2).** The human said, verbatim: *"I would guess just make one resolved node for the past decision, maybe a few if there was multiple different things done but one seems ok, it will be only one context, I don't think we should make a huge amount of nodes. I would guess for the destination/deliverable, it will be in the request when the skill will be called to convert. It shouln't be nessesarly only one question per node, but like usual with grilling nodes. otherwise seems ok"*.
- The decisions already made in the conversation go into one resolved node, or into a few where the conversation did several unrelated things. The human's words are its answer. Where the human said yes to the agent's recommendation, the recommendation is kept beside the yes (assumption).
- The questions still open become grilling nodes, grouped as grilling nodes usually are. A node is not limited to one question.
- Each choice the agent made without the human's agreement becomes an `ASSUMPTION` flag, and is never recorded as the human's decision.
- Findings that cost real effort and exist only in the conversation, such as benchmark results, go into one file in the effort's directory. That file is linked from the map's `## Notes` and marked as the agent's work.
- The conversation's chronology is not carried. Neither are facts the agent read from the tree, which can be read again.
- The record must be complete without the conversation, so that a later `/expedition-stop` or compaction loses nothing the effort needs.
- How the work is split into nodes is usually plain from the conversation, so the skill does not describe it in detail. The human said, verbatim: *"I also feel like for the upgrade, the split of nodes should be somewhat obvious when in a conversation so I don't think the skill needs to be extreamly detailed ?"*

**Words lost to compaction (Q5, "ok").** The manager checks whether the environment keeps a full transcript of the conversation, and never assumes that it does. Claude Code keeps one on disk, and it holds the messages from before each compaction. Where a transcript exists, a worker on a `precondition` node reads it, rather than the manager. That worker takes out the human's words and the decisions as above, and marks them `verbatim`, citing the transcript. Where none exists, the existing `paraphrase` rule applies. This changes the rule in `### The human's words` for the upgrade's own case. That rule makes the paraphrase depend only on whether the words are still in the thread's context.

**Work already done or under way (Q3, "ok"; and the human's addition to an assumption).**
- Commits made before the upgrade stay as they are and are linked to no node.
- A branch that already exists can be promoted to a deliverable: the upgrade declares that branch as the deliverable's branch, rather than creating a new branch from the deliverable's base. The human said, verbatim: *"I would say yes with the addition that a existing branch can be promoted to a deliverable"*.
- Uncommitted changes move into the worktree of a new implementation node, which names its deliverable. That is the deliverable the request ties the work to, and where this is unclear the manager asks (assumption). The manager writes the node's acceptance condition, which covers the whole change, including the part written before the upgrade. The change then goes through the checker and the gate like any other work.
- Planned work that was not started becomes open nodes.
- Background agents still running in the conversation finish before the upgrade starts, and what they return counts as part of the conversation (assumption).

**Relation to the two ways of starting an effort (Q4, "ok").** Today, starting an effort from a conversation has no steps of its own beyond the six things `## Starting an effort` lists and the files `### Start an effort` creates. The upgrade is that same way, starting from a conversation. Its extra steps sit in `/expedition-upgrade`, as adoption's sit in `adoption.md`. `## Starting an effort` points to the skill. The glossary keeps saying that the ways of starting differ only in what they start from, and the upgrade gets no glossary term of its own.

**Upgrading into an existing effort (Q6, "ok").** The request may name an existing effort. The upgrade then adds the deliverables and nodes to that effort, and the new nodes take the next unused numbers. Only one thread manages an effort at a time. Before invoking the upgrade, the human ends any other manager session on that effort with `/expedition-stop`, and the skill states that rule. An effort with no planned end needs nothing extra from the upgrade, because node 02 marks it with the map's existing "not expected to reach its destination" line (assumption).

**MISSING FROM MAP, as the worker wrote it:** The map does not say that node 02's answer binds node 03, or what that answer was. I got it from the manager notes on each resume and from node 02's `## Answer`, which I read because the manager pointed to it. Otherwise none.

## Flags

`03.1` `ASSUMPTION` **· settled** — Where the invocation's request leaves the destination, whether the effort is expected to reach it, or the deliverables unstated, the manager asks the human rather than writing them itself. The human said these come from the request but did not say what happens when it is silent. Adoption's step 3 asks the human in the same case, so I followed it.

`03.2` `ASSUMPTION` **· settled** — Uncommitted changes carried into an implementation node name the deliverable that the request ties that work to, and the manager asks where this is unclear. Node 02 requires every implementation node in an effort with deliverables to name exactly one deliverable, and nothing tells the upgrade which one, so I settled it this way.

`03.3` `ASSUMPTION` **· settled** — Where the human said yes to an agent's recommendation in the conversation, the resolved node of past decisions keeps the recommendation beside the yes, because a bare "ok" records nothing on its own. I put this to the human in payload 1's SO FAR, and they did not correct it.

`03.4` `ASSUMPTION` **· settled** — Background agents still running when the upgrade is invoked finish first, and what they return counts as part of the conversation. I put this in payload 1's SO FAR, and the human did not correct it.

`03.6` `ASSUMPTION` **· settled** — A branch promoted to a deliverable must hold no commit of the effort's own record, and must not stay checked out in the main checkout after the upgrade. Where either is not true, the manager asks the human rather than fixing it. The human allowed promotion but said nothing about how it meets `### Declaring a deliverable`, which exists so that graph commits never reach a pull request. I kept that rule's purpose for a promoted branch, and left the fix to the human, because the fix moves or rewrites their branch.

`03.5` `ASSUMPTION` **· settled** — An upgrade into an effort with no planned end needs nothing beyond node 02's answer. That answer marks such an effort with the map's existing "not expected to reach its destination" line. I had held this question for node 02. Its answer left nothing upgrade-specific to ask, so I did not put it to the human.

## Interview

### Attempt 1 — agent `a29bce55ca8567b10`

**Relayed question, payload 1, as the worker wrote it:**

NODE:          How a conversation that is not an expedition is upgraded into one

ABOUT:         This node decides what happens when you run the expedition workflow partway through a normal conversation. It covers how you trigger it, which thread becomes the manager, what goes from the conversation into the effort's record, and what happens to work already done. It is decided now because it is one of the three changes this effort has to ship.

SO FAR:        I read the node, the map, the grilling contract, `adoption.md`, the manager contract's `## Starting an effort` and `### The human's words`, `graph-conventions.md` `### Start an effort`, the start of `expedition-stop`, and the glossary entries for starting an effort. I also read node 02's open payload. The facts these questions rest on:
               - Today an effort starts in one of two ways, and they differ only in what they start from: a conversation with you, or adoption of a directory of work that already exists. Adoption's extra steps are in their own file, `adoption.md`, which the manager reads only when it adopts.
               - The manager contract says the manager's context runs out first, and that the manager does no node's work itself. A conversation that already did the work and grew large is the opposite of that.
               - A manager's session can already end and be continued by a new manager thread working from the record alone (`expedition-stop`). That new thread cannot resume agents from the earlier session.
               - The contract already says what to do when your words are gone from the thread's context, for example after compaction: the manager writes what it still has, marks it `paraphrase` rather than `verbatim`, and says why.
               - On this machine Claude Code keeps each conversation's full transcript on disk, under `~/.claude/projects/<project>/<session>.jsonl`. I checked a compacted transcript. The messages from before each compaction are still in the file, and the summary is added after them.
               - Node 02, on several deliverables in one effort, has settled nothing yet.
               I settled three things myself, so you can correct any of them now:
               - Commits made in the conversation before the upgrade stay exactly as they are and are not linked to any node. This is how adoption treats existing git history.
               - Background agents still running in the conversation finish before the upgrade starts, and what they return counts as part of the conversation.
               - When you said yes to a recommendation the agent made (for example *"ok"*), the record keeps the agent's recommendation next to your yes. Without it, the yes says nothing.
               Two questions come later, once node 02 has settled. The first is whether an upgrade can add its work to an effort that already exists and runs indefinitely, rather than always starting a new effort. That raises the problem of two manager threads on one graph. The second is how work that turns out to be several tasks is split across node 02's deliverables.

Q1. How it is triggered, and which thread becomes the manager
ASK:           How do you trigger the upgrade, and does the conversation's own thread become the effort's manager?
RECOMMENDED:   You run `/expedition` in the conversation, with no new skill and no argument. The skill notices for itself that the conversation already holds earlier work, and treats it as the starting material. The conversation's thread becomes the manager, because only that thread holds the conversation and you asked to convert the conversation you are in. From the moment of the upgrade it stops doing work itself and acts only as manager. The record it writes must be complete without the conversation (see Q2). Then, when its context is heavy, you can end its session with `/expedition-stop` and start a new manager thread from the record, using what already exists.
ALTERNATIVES:  A dedicated `/expedition-upgrade` skill. The trigger is more explicit, but it adds a skill whose only job is to say "a conversation came before this".
               The conversation thread only writes the record and then always hands over to a new manager thread. You get a clean context every time, but you have to switch threads at every upgrade, even for a small conversation.
               The conversation thread stays the manager with no expectation that the record stands alone. This is simpler, but the effort is lost the first time that thread compacts or ends.

---

Q2. What is carried into the record, and in whose words
ASK:           What goes from the conversation into the effort's record, and how is each piece marked?
RECOMMENDED:   What is carried:
               - Your request, and any later reframing of it, go into the map's destination and standing preferences. Your words are pasted and marked `verbatim`.
               - Each decision you made goes into its own node with status `resolved`. Your words are its answer.
               - Each question still open goes into its own open node.
               - Each choice the agent made without your agreement is written as an `ASSUMPTION` flag, never as your decision, so you can review it later.
               - Findings that took real effort to get and exist only in the conversation, such as benchmark results, go into one file in the effort's directory. That file is linked from the map's notes and marked as the agent's work. Adoption treats research output the same way.
               What is not carried: the step-by-step history of the conversation, and facts the agent read from the tree, because the tree can be read again.
               Whatever you said that is no longer in the thread's context follows the existing rule: it is marked `paraphrase`, with the reason given.
ALTERNATIVES:  Carry a single summary of the conversation as one file linked from the map. This is quick, but it turns the agent's paraphrase into the permanent record, which the scribe rule exists to prevent.
               Carry only the destination, and let new grilling nodes ask you again everything already decided. This is clean, but it makes you repeat decisions you already made.

---

Q3. Uncommitted and in-progress work
ASK:           What happens to uncommitted changes, and to work that was planned but not started, when the conversation is upgraded?
RECOMMENDED:   The uncommitted changes move into the worktree of a new implementation node, which leaves the main checkout clean. The manager writes that node's acceptance condition, which covers the whole change, including the part written before the upgrade. The change then goes through the checker and your gate like any other work. No code lands in an effort without a gate, even code you already saw in the conversation. Planned work that was not started becomes open nodes. Which branch the node lands on follows node 02, whatever it decides.
ALTERNATIVES:  You commit or throw away your uncommitted changes before the upgrade, so the upgrade never handles code that is not committed. This is simplest, but either the work skips the gate or you have to tidy up first.
               Leave the changes in the main checkout and have the first node continue them there. This breaks the rule of one worktree per implementation node and blocks parallel work.

---

Q4. How the upgrade relates to the two ways an effort starts today
ASK:           Is the upgrade a third way of starting an effort, or the existing "from a conversation" way with extra steps?
RECOMMENDED:   It is the existing "from a conversation" way, so the glossary's statement that the two ways differ only in what they start from stays true. The steps only a conversation already under way needs are about earlier decisions, uncommitted work and compaction. They go in their own file next to `SKILL.md`, as adoption's steps do, and are read only when the conversation holds earlier work. That keeps them out of the manager contract, which every manager reads in full. The file's name is left to the implementation, following the `/naming` skill.
ALTERNATIVES:  Make it a third way, with its own glossary term. This makes it more visible, but its input is still a conversation, so the line that separates the two ways stops being true.
               Put the steps as a passage inside `SKILL.md`'s `## Starting an effort`. This means one less file, but every manager reads that text even when no upgrade happens.

---

Q5. Recovering your exact words after compaction
CONTEXT:       You said compaction loses information. The transcript Claude Code saves on disk still holds the messages from before compaction.
ASK:           When a full transcript of the conversation is available to read, should the upgrade copy your words from it, rather than marking them `paraphrase`?
RECOMMENDED:   Yes. The manager checks whether such a transcript exists, rather than assuming one does, which keeps to ground rule 1. Where it exists, a worker on a `precondition` node, rather than the manager, reads it and extracts your words and the decisions as Q2 lists them. They are marked `verbatim`, with the transcript cited as their source. This keeps both the transcript and the manager's context small, as adoption does by giving the bulk import to workers. Where no transcript can be found, the existing `paraphrase` rule applies. This changes the rule in `### The human's words`, which today asks only whether your words are still in the thread's context.
ALTERNATIVES:  Use only what is still in the thread's context. This is simpler and assumes nothing about the tool, but whatever was compacted away stays lost.
               The manager reads the transcript itself. This is direct, but a transcript close to 1M tokens would fill the manager's context on the first step.

**The human's answer to payload 1, `verbatim`:**

> for "Commits made before the upgrade stay as they are, unlinked to any node, as adoption treats existing git history." I would say yes with the addition that a existing branch can be promoted to a deliverable Q1. I would guess an /expedition-upgrade as I feel like there will be logic only relevant for upgrade ? Or put the information in another file than the main /expedition to not split it ? For when the context gets heavy, I can do expedition-stop or just compact the context. Q2 I would guess just make one resolved node for the past decision, maybe a few if there was multiple different things done but one seems ok, it will be only one context, I don't think we should make a huge amount of nodes. I would guess for the destination/deliverable, it will be in the request when the skill will be called to convert. It shouln't be nessesarly only one question per node, but like usual with grilling nodes. otherwise seems ok Q3 ok Q4 I forgot this existed, it seems to be the same. What is the current logic ? Q5 ok

Q3 takes the worker's `RECOMMENDED`: *"The uncommitted changes move into the worktree of a new implementation node, which leaves the main checkout clean."* Q5 takes the worker's `RECOMMENDED`: *"Yes. The manager checks whether such a transcript exists, rather than assuming one does."*

`DIVERGENCE` on Q1: the worker recommended *"You run `/expedition` in the conversation, with no new skill and no argument."* The human leans to `/expedition-upgrade`, or to the steps in a file other than the main `/expedition`, and asks which; they add that heavy context can also be handled by compacting.

`DIVERGENCE` on Q2: the worker recommended *"Each decision you made goes into its own node with status `resolved`."* and *"Each question still open goes into its own open node."* The human prefers one resolved node for the past decisions, or a few, and open questions grouped as grilling nodes usually are; destination and deliverables come from the request that invokes the conversion.

*Manager's note:* Q4 carries a question from the human, *"What is the current logic ?"*, which goes back to the worker. The worker's self-settled point on earlier commits gains the human's addition that an existing branch can be promoted to a deliverable.

**Relayed question, payload 2, as the worker wrote it:**

NODE:          How a conversation that is not an expedition is upgraded into one

ABOUT:         This node decides what happens when you run the expedition workflow partway through a normal conversation. This payload covers the two points where you asked me something back, Q1 and Q4, and one question that node 02's answers now make possible to ask, Q6.

SO FAR:        What you settled in your last reply. I am reading these from your own words:
               - Commits made before the upgrade stay as they are, not linked to any node. A branch that already exists can be promoted to a deliverable: the upgrade declares that branch as the deliverable's branch, rather than creating a new branch from upstream.
               - For a heavy context, you choose whether to run `/expedition-stop` or to compact. The record must still be complete without the conversation, so that both choices are safe.
               - Q2: the decisions already made in the conversation go into one resolved node, or a few where the conversation did several unrelated things, not one node per decision. The destination and the deliverables come from the request you give when you call the upgrade. Open questions are grouped into grilling nodes in the usual way, not one question per node. The rest of Q2 stands: choices the agent made without your agreement become `ASSUMPTION` flags, costly findings go into one linked file, the conversation's history is not carried, and the `paraphrase` rule applies.
               - Q3 and Q5 as recommended. Uncommitted changes go into an implementation node's worktree and through the gate. Planned work that was not started becomes open nodes. A `precondition` worker takes your words from the transcript on disk, where one exists, and marks them `verbatim`.
               Node 02 has settled three things:
               - Deliverables are listed in `map-manager-only.md`.
               - Each implementation node names its deliverable in a header field.
               - Each node's worktree is cut from its deliverable's branch, and the manager pushes once you approve.
               I settled two more things myself, so you can correct either one now:
               - Where your request does not state the destination or the deliverables, the manager asks you, rather than writing them itself. Adoption does the same.
               - The node that takes over uncommitted changes names the deliverable your request ties that work to. Where the request leaves it unclear, the manager asks you.
               One question stays held until node 02 settles how an effort with no planned end is marked: how an upgrade affects that marking.

Q1. Dedicated skill or a separate file read by `/expedition`
CONTEXT:       You asked which one to use. In a dedicated skill, all the upgrade logic sits in one file of its own, so the two options can be the same thing.
ASK:           Should the upgrade be its own skill, `/expedition-upgrade`, that holds every upgrade-only step and tells the thread to load the manager contract?
RECOMMENDED:   Yes. Make it a dedicated skill, invoked as `/expedition-upgrade <request>`. Its file holds every step that only an upgrade needs: the decisions node, the transcript extraction, moving uncommitted work, and promoting a branch. It first tells the thread to read `expedition/SKILL.md` and become the manager. Three things support this:
               - The trigger is explicit. With plain `/expedition`, the skill would have to judge whether the earlier chat was work to carry or just the normal conversation that starts an effort. That judgement can go wrong.
               - Your request becomes the skill's argument, which is where you said the destination and the deliverables come from.
               - The main manager contract gets no text that only an upgrade needs. `expedition-stop` and `expedition-cleanup` already work this way.
ALTERNATIVES:  A file next to `SKILL.md`, read by `/expedition` when it finds earlier work. There is one less skill, but you lose the explicit trigger and the judgement above remains.
               A passage inside `SKILL.md`. Every manager would read it even when no upgrade happens.

---

Q4. How the upgrade relates to starting an effort from a conversation
CONTEXT:       You asked what the current logic is. Today, starting from a conversation has no steps of its own. `## Starting an effort` in `SKILL.md` lists six things both ways of starting establish:
               - the effort's name;
               - the destination;
               - whether the effort is expected to reach that destination;
               - the map's standing preferences, ground rules and statement of which sources to trust;
               - the label vocabulary;
               - the first nodes.
               `### Start an effort` in `graph-conventions.md` creates the seven files and the first nodes, and runs three checks. Nothing in it covers decisions already made, code already written or compaction. Adoption alone adds steps, in `adoption.md`.
ASK:           Should the upgrade be described as the existing "from a conversation" way, with the extra steps in `/expedition-upgrade`, rather than as a third way of starting an effort?
RECOMMENDED:   Yes. As you said, it is the same thing. Its starting point is still a conversation with you. The glossary's statement that the two ways differ only in their starting point stays true. `## Starting an effort` gets one sentence pointing to `/expedition-upgrade` for a conversation that already holds work, alongside its existing pointer to `adoption.md`. The upgrade needs no glossary term of its own.
ALTERNATIVES:  A third way of starting, with its own glossary term. It is more visible, but its starting point is still a conversation, so the line that separates the ways stops being true.

---

Q6. Upgrading into an effort that already exists
CONTEXT:       You said one effort with no planned end may become your main way of working. In that case most upgrades would add work to that effort rather than start a new one. Node 02's list of deliverables can already grow.
ASK:           Can an upgrade add its work to an existing effort, named in the request, as well as start a new effort?
RECOMMENDED:   Yes. The request names either a new effort or an existing one. In an existing effort, the upgrade adds the deliverables and the nodes. The new nodes take the next unused numbers. Only one thread may manage an effort at a time, and no thread can detect that another one is running. So the conversation's thread becomes that effort's manager, and before you invoke the upgrade you end any other manager session on that effort with `/expedition-stop`. The skill states this rule, and you are the one who keeps to it.
ALTERNATIVES:  The upgrade always starts a new effort. This is simpler, but it splits work across efforts, which goes against using one effort with no planned end.
               The conversation's thread writes a proposal file, and the effort's existing manager takes it in. This avoids a second manager, but it creates a new way for something other than the manager to write into the record, and you have to switch threads anyway.

**The human's answer to payload 2, `verbatim`:**

> Q1 ok Q4 ok Q6 ok   I also feel like for the upgrade, the split of nodes should be somewhat obvious when in a conversation so I don't think the skill needs to be extreamly detailed ?

Q1 takes the worker's `RECOMMENDED`: *"Yes. Make it a dedicated skill, invoked as `/expedition-upgrade <request>`."* Q4 takes the worker's `RECOMMENDED`: *"Yes. As you said, it is the same thing."* Q6 takes the worker's `RECOMMENDED`: *"Yes. The request names either a new effort or an existing one."*

## Annotation: the worker's correction of a summary in payload 2

As the worker wrote it, after its handover: "the manager pushes once you approve". This phrase appeared only in payload 2's SO FAR, where I summed up node 02 from the manager's note. It was wrong: the shipped rule asks for a separate yes for each push. The human's reply to that payload ("Q1 ok Q4 ok Q6 ok ...") said nothing about pushes. My handover's ANSWER, its flags and the new node's condition make no claim about pushing. No part of the record needs to change.

*Manager's note:* the worker also added, after its handover, flag `03.6` and amendment 1 to node 07's clause 5, and this INVALIDATIONS line: "clause 5 above extends node 05's `### Declaring a deliverable` for the upgrade's case. Node 05 is not contradicted, and its text needs no change, because the upgrade skill states the change for its own case. The new node is already blocked by 05."

## Annotation: node 08 narrows flag 03.6

As the worker of [node 08](08-a-deliverable-that-lands-by-merging-locally.md) reported it: Node 03: a narrowing of flag 03.6. The check that a promoted branch holds no commit of the effort's record applies only to a deliverable that lands by pull request.
