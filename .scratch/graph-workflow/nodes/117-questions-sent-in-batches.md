# Whether the manager sends the human questions in batches

Type: grilling
Status: resolved

## Question

**The human asked for this node.** Their words, `verbatim`: *"I think we might want to do like the new grilling
skill, where questions are sent in batches. I think it might be more efficient in terms of token and it reduces
context switching for the user. Can you create a grilling node for it"*

### What the effort has fixed against this, and what it has not

**One question at a time is settled and has just been restated.** [When the human's channel is free, and whether the
manager must fill every gap in it](108-when-the-humans-channel-is-free.md) closed on the human's own wording, `verbatim`:
*"there should be at most one question offered to the user and if there is none and there is a question waiting from
one of the subagents, it should be offered to the user"* — a ceiling of one and a floor of one. And [What the manager
works on next, and how the human redirects it](16-human-steering.md) records the measured cause of the ceiling: two
questions were asked at once, a reply named an option in one and named nothing in the other, and the manager could
not tell which node the reply belonged to. **So this node is not a fresh question. It asks the human to revisit a
rule they set, on a ground they have now supplied.**

**What is genuinely open.** The two claims in the instruction are both about cost rather than about correctness — that
batching is cheaper in tokens, and that it reduces the human's context switching — and neither has been measured on
this effort. Against them stands the attributability problem node 16 measured, which a batch reintroduces by
construction. The batch's shape is undecided in every part: how many, whether a batch may mix tiers, whether a gate
may sit in one, what happens when a reply answers three of four, and whether the ceiling of one becomes a ceiling of
one *batch*.

**The named prior art is a file this effort has not read.** The instruction points at *"the new grilling skill"* — an
external skill of the same family as the `/grilling` this effort's contracts name, and the effort's own record has
nothing about how it batches. Reading it is part of this node's work, and it is the one thing here that may need a
source outside the working directory.

## The manager's note at filing

*Not a change to anything above.*

**Filed as grilling and not as implementation**, because the shape is undecided and because a rule the human set is
what would change. The manager wrote none of the question's substance: the paragraphs above state what the record
already fixes and what it does not, and take no position on whether batching is right.

**Three of the effort's own flags are the standing evidence against the token claim being obvious**, and whoever
holds this node should weigh them rather than take the manager's word: `102.3`, `94.5` and `91.3` each record a
grilling worker declining to invoke a method skill *because the load was not judged worth its cost* — so this effort
has a measured habit of treating per-question overhead as small. Whether a batch's saving is in the manager's tokens,
the worker's, or the human's attention is not stated in the instruction and is not the same question.

**Adjacent and deliberately not merged:** [Whether the contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md) is about the same external skill family and decides
nothing about batching.

## Interview

### Attempt 1, question 1 — written and queued, not yet put to the human

***Recorded by the manager as a queued payload, not as a question the human has been asked.*** Node 103's gate held
the channel when this arrived, and node 108's answer caps what is in front of the human at one. It is written down
here so that a death of the manager's thread does not lose it. **Pasted as the worker wrote it**; the manager
authored none of it and has taken no view on it.

**The finding the worker leads with:** *"the skill's batching is structurally not the thing this effort's ceiling
governs."*

> **What the skill actually does.** `mattpocock-skills:grilling` used to say *"Ask the questions one at a time...
> Asking multiple questions at once is bewildering."* That text is gone. Alongside it there was an experiment,
> `batch-grill-me`, marked not-model-invocable; its text has been promoted verbatim into `grilling` itself and the
> experiment deleted. So the batch won upstream. Its mechanism: map the decisions as a **design tree**; the
> **frontier** is every decision whose prerequisites are settled; ask the whole frontier in one **round**, numbering
> each question `Q1`/`Q2` with a title, a `---` between them, and a recommendation under each; a question depending
> on another still open in this round waits for a later round; finding facts is the agent's job, never yours.
>
> **The part that matters, and that the record does not have.** That frontier is computed by the one agent holding
> the tree, and that same agent reads the answers. Two different things in this effort could be called a batch, and
> only one of them is what the skill does:
>
> - **(A) across nodes** — the manager puts two different workers' questions in front of you at once. This is what
>   raising node 108's ceiling means. The skill supports none of it: the manager holds no tree over other nodes'
>   questions, your map says most context lives in the workers and not in the manager, and each answer has to be
>   routed back to a different worker.
> - **(B) inside one node** — one worker puts several of its own independent questions in one relay, numbered. This
>   is literally the skill, and the worker is exactly the party the skill assumes. Node 108's ceiling of one need not
>   move at all: one relay payload in front of you, carrying a numbered round.
>
> **Both costs you named point at (B) and not at (A).** Tokens: your node 52 established from the harness's own docs
> that a subagent's prompt cache runs on a **five-minute TTL**, and wrote that *"a worker paused for a human answer —
> the whole interview shape — is liable to come back cold"*, against a `map.md` read of ~19,840 tokens in every
> worker's opening payload, paid uncached. So each extra interview **round** risks re-paying a worker's whole context
> at full rate, and cutting a worker's rounds cuts that directly. (A) changes no worker's round count, so it saves
> none of it — it merges manager messages, which are billed in the manager's warm window. **What I did not measure:**
> node 52 says in terms that nobody has measured a human-gated workflow, so the direction is established from a
> primary source and the size is not. Context switching: node 108's floor already makes the manager serve the queue
> at once, so you already get questions back-to-back. (A) merges the delivery and not the substance — two questions
> from two nodes need two node contexts loaded either way. (B) merges both: two questions about one node load that
> node once.
>
> **What I measured on your own replies, which cuts both ways.** Your modal reply to an interview question is a bare
> assent to the recommendation — *"ok for recommended"* five times, plus *"ok"* and *"yes for recommendation"*. Under
> (A) those are unattributable by construction, which is node 16's measured failure. But you already volunteer a node
> number when a bare assent would be ambiguous: *"for 91, ok"*, *"for 94 ok for recommended"*, *"For 98, ok for
> recommanded"*, *"for 108, there should be..."* — four instances, and nothing in the record cites them. Against
> that, the strongest thing I found against (B): node 16's own first round carried one worker question plus three
> manager notes, one explicitly offering you three decisions to pull forward. You replied *"yes for recommendation"*,
> and the node records *"Their reply did not reach the offer."* A multi-item ask inside one node whose reply landed
> on one item. It indicts unnumbered prose rather than the skill's numbered format, but it happened here.
>
> **Settled on my own authority, and reported as fact rather than asked.** Whatever you decide has to be written into
> the grilling contract's own text and cannot be adopted from the skill by reference: three consecutive workers ran
> the contract's inline *"one question at a time"* bullet with both skills present and flagged it (`102.3`, `94.5`,
> `91.3`), so a batch that lives only in the invoked skill would be picked up by nobody. Also noted: the skill's word
> **frontier** denotes the askable questions in one interview, while your glossary fixes **frontier** as *"the nodes
> that are open, unblocked and unclaimed"* — same word, two denotations, so the skill's vocabulary cannot be imported
> as-is.
>
> **ASK:** Which of the two is it? **(B)** one worker may put several of its own independent questions to you in one
> numbered round, with node 108's ceiling of one left standing over relay payloads — or **(A)** the manager may put
> different nodes' questions in front of you at once, raising that ceiling?
>
> **RECOMMENDED: (B) only.** It is the faithful reading of the skill you pointed at — in your own use of `/grilling`
> you are receiving a batch from the one agent holding the tree, which is the worker's position here and not the
> manager's. It is where both costs you named actually land: fewer rounds per worker is the only version that touches
> the five-minute-TTL exposure node 52 measured, and it is the only version that merges the context you have to load
> rather than just the messages. And it costs nothing you have already decided: node 108's ceiling, its floor, and
> node 16's tier order all stand untouched, because one numbered round is one thing awaiting one reply. Attribution
> stays inside the party that can do it — the worker numbered its own questions and reads its own answers, so a reply
> naming `Q2` needs no guess from the manager, which is exactly what failed at node 16.
>
> **ALTERNATIVES: (A) only** — raise node 108's ceiling and let the manager batch across nodes. Reintroduces the
> failure node 16 measured, on a reply form I measured as your modal one, and saves nothing on the token cost your
> own effort identified as dominant.
> **Both (A) and (B)** — the largest change, and the one where a reply answering three of four items has to be
> untangled by the manager, which holds none of the substance.
> **Neither** — node 16's *"Question batching is dead"* stands as written, and the answer to this node is that the
> skill changed upstream and the rule does not.

***The manager's note beside it, and not the worker's.*** The worker's `SO FAR` addresses the human in the second
person throughout — *"your map"*, *"your node 52"*, *"your own replies"* — which is the form its contract writes
questions in. It reaches the human unaltered when the channel frees.

### Attempt 1, answer 1

**The human's word, `verbatim`**, written at the moment they spoke:

> Yes, it's B

**The option it takes, quoted in full and attributed to the worker who wrote it**, not to the manager:

> **(B) inside one node** — one worker puts several of its own independent questions in one relay, numbered. This is
> literally the skill, and the worker is exactly the party the skill assumes. Node 108's ceiling of one need not move
> at all: one relay payload in front of you, carrying a numbered round.

**It agrees with the worker's recommendation**, which was *"(B) only"*, so it is not a divergence.

***The manager's note, and not the human's words.*** **What the manager did not read into it.** The reply is to the
question as asked — which of two things a batch is — and the worker's `ASK` offered `(B)` with one clause attached:
*"with node 108's ceiling of one left standing over relay payloads"*. The manager reads the ceiling as **untouched**
on that ground, and marks the reading as the manager's. **What is not settled by this word**, and is the worker's to
put or not put: how many questions one numbered round may carry, whether a worker must number them even when it has
one, what happens to a round answered in part, and whether the standing offer to raise the number of nodes that may
need the human at once — open and unanswered — is affected at all. None of those was asked.

#### The worker's correction of the manager's note above, pasted as it wrote it

***The worker read the manager's note and corrected it. The manager accepts the correction and has struck the clause
it applies to.***

> **On the clause you flagged as your reading.** I think it is theirs, not yours. The sentence *"with node 108's
> ceiling of one left standing over relay payloads"* was inside the `(B)` option text they assented to, and that text
> also said *"one numbered round is one thing awaiting one reply"*. They took the option as written, so the ceiling
> standing is part of what they endorsed rather than an inference laid on top of it. Record that beside yours.

**The manager's clause it corrects, struck:** ~~*"The manager reads the ceiling as **untouched** on that ground, and
marks the reading as the manager's."*~~ **The worker is right on the fact.** The `(B)` option text quoted above in
this node's own record contains *"Node 108's ceiling of one need not move at all: one relay payload in front of you,
carrying a numbered round"*, and the manager pasted that text into this file before writing the note that called it
an inference. **The ceiling standing is part of what the human endorsed**, and the manager's caution made their own
words look weaker than they were.

### Attempt 1, question 2 — written and queued, not yet put to the human

***Recorded by the manager as a queued payload, not as a question the human has been asked.*** Node 107's question
held the channel when this arrived. **Pasted as the worker wrote it**; the manager authored none of it and has taken
no view on it.

> **What that does oblige, and it is shipped text rather than a new decision.**
> `.claude/skills/expedition/SKILL.md:428` now reads *"Exactly one question is in front of the human at a time"*.
> Under (B) that sentence is false as worded and true as meant — the count is of payloads awaiting a reply, not of
> questions. The rule is untouched; the word has to change.
>
> **And one sentence in that file loses its stated reason.** Lines 442-444 say every relayed question names in one
> line whatever else is waiting, *"by node name and kind only"*, because *"keeping it to a name and a kind is what
> keeps a terse reply attributable to exactly one thing."* After (B) a relayed payload holds more than one answerable
> thing by design, so that justification no longer describes what is true. The rule survives on its other ground — a
> named-but-unasked item still cannot be answered by accident — but the clause stating why is now wrong.
>
> **Settled on my own authority, both reported as flags rather than asked.** No cap on how many questions a round may
> carry: membership is by independence, which is the skill's own rule and the only one with a reason behind it, and I
> measured that every grilling node in this effort ran one or two rounds carrying one question each — so a cap would
> bind on nothing and is machinery for a predicted need, which the map's standing preference refuses. And no number
> on a lone question: the presence of numbering is itself the signal that the payload holds more than one.
>
> **ASK:** When a round carries two questions and the reply is a bare *"ok for recommended"* naming neither — does it
> endorse **every** recommendation in that round, or is it ambiguous, so the worker re-asks what the reply did not
> name?
>
> **RECOMMENDED:** **It endorses every recommendation in the round, and nothing in the payload that is not a
> recommendation.** Anything that names a question or an option settles what it names and leaves the rest open, and
> whatever is left unnamed goes out in the next round rather than being guessed.
>
> It rests on what I measured about how this human actually replies: a bare assent to the recommendation is their
> modal answer to an interview question — *"ok for recommended"* five times, plus *"ok"* and *"yes for
> recommendation"*. Under the other reading their commonest reply fails against every batched round, so every round
> ends in a re-ask and (B) spends a round instead of saving one, which is a net loss on the exact cost they asked to
> reduce. It is also the plain reading: a round offers N recommendations, and *"ok for recommended"* assents to the
> recommendations. My own contract already fixes this direction for the single case, naming *"ok for recommended"* as
> an assent to be read as theirs.
>
> **And node 16 confirms it rather than refuting it.** That round held one recommendation plus three manager notes
> that were not recommendations; their *"yes for recommendation"* reached the recommendation and not the offer, which
> is what the node records as a miss. Under this rule that is the correct outcome — a bare assent reaches
> recommendations only — and what actually went wrong there was a non-recommendation put in a payload while expecting
> an answer to it, which this rule forbids by construction.
>
> **The risk, stated rather than smoothed.** Someone who meant *"ok for Q1, and I have not thought about Q2"* and
> wrote *"ok for recommended"* gets Q2 settled unmeant. Two things bound it, both already in force rather than
> proposed. They already volunteer a scope when they perceive ambiguity — *"for 91, ok"*, *"for 94 ok for
> recommended"*, *"For 98, ok for recommanded"*, *"for 108, ..."*, four instances — and numbering is what makes the
> ambiguity visible enough to trigger that reflex. And this effort already writes the option taken back to them in
> the worker's next message, on every recorded round, so a wrong reading surfaces one turn later at the cost of one
> turn.
>
> **ALTERNATIVES: Ambiguous, so the worker re-asks what the reply did not name** — safest, and it makes their most
> frequent reply unusable in exactly the mode (B) introduces.
> **Silence on a question counts as assent to its recommendation** — cheapest, and it is my contract's hard rule 1
> broken outright: the worker answering for the human.
> **The worker must ask them to number their reply** — puts the format burden on the scarce resource, and nothing in
> the record suggests they would keep to it.

***The manager's note beside it, and not the worker's.*** **Two shipped defects are named in this payload and neither
has a node yet.** `SKILL.md:428`'s *"Exactly one question"* and lines 442-444's stated reason are both consequences of
this node's own answer, and the worker has not yet handed over, so nothing has been minted. The manager is holding
them rather than minting from a mid-interview payload.

### Attempt 1, answer 2

**The human's word, `verbatim`**, written at the moment they spoke:

> ok for recommened says ok for everything but in practice it is unlikely I say it I think, as I will create my
> message one question at a time, so it will be more Q1 ok Q2 ok Q3 ..

**The option it takes, quoted in full and attributed to the worker who wrote it**, not to the manager:

> **It endorses every recommendation in the round, and nothing in the payload that is not a recommendation.**
> Anything that names a question or an option settles what it names and leaves the rest open, and whatever is left
> unnamed goes out in the next round rather than being guessed.

**It agrees with the worker's recommendation**, so it is not a divergence. The first clause is the answer, stated as a
restatement of it.

***The manager's note, and not the human's words. The second clause is a prediction about their own behaviour, and
it cuts at the ground the recommendation was built on rather than at the answer.*** The worker's case for that
recommendation was empirical and it was measured on this record: *"a bare assent to the recommendation is their modal
answer to an interview question — 'ok for recommended' five times, plus 'ok' and 'yes for recommendation'"*, and
*"under the other reading their commonest reply fails against every batched round, so every round ends in a re-ask
and (B) spends a round instead of saving one."* **The human now says that reply form is unlikely to appear under
batching at all**, because they will compose per question: *"Q1 ok Q2 ok Q3 .."*. If that holds, the failure mode the
recommendation was chosen to avoid mostly does not arise, and the rule settles the residual case rather than the
common one. **The answer is unaffected and is theirs.** What is affected is how much work the rule does, and whether
the risk the worker named — a bare assent settling an unmeant Q2 — is a live risk or a rare one.

**The hedge is theirs and is left in place rather than smoothed away**: *"it is unlikely I say it I think"*. It is a
prediction, not an undertaking, so nothing on this graph may treat per-question replies as guaranteed. **The manager
did not decide** whether the worker should now carry their predicted form into what it ships — that being the
worker's, which holds this node.

## Answer

*Node 117's worker's `ANSWER`, pasted as it wrote it.*

> **Batching is adopted in one form and refused in the other: a worker may batch its own questions, and the manager
> never batches across nodes.** The human's words, `verbatim`, on being offered the two: *"Yes, it's B"*.
>
> ### 1. What a batch is here
>
> One worker may put several of its own questions to the human in a single relayed payload. Two questions may share a
> payload only where neither's answer depends on the other's; one that depends on another in the same payload is held
> for a later one. **The manager never combines questions from different nodes**, and that half is refused rather
> than left open.
>
> ### 2. Why the inter-node and intra-node cases split, which is the whole of the answer
>
> The external skill the instruction named — `mattpocock-skills:grilling`, whose one-question text has been replaced
> upstream by the batch text of a deleted experiment, `batch-grill-me` — computes its round over a **design tree held
> by one agent**, and that same agent reads the answers. **A worker is that agent. The manager is not and cannot
> be**, the map fixing that most of the context lives in the workers and not in the manager.
>
> So under this answer **the manager performs no attribution at all**: a payload comes from one worker and its reply
> goes back to that one worker unaltered. [What the manager works on next, and how the human redirects
> it](16-human-steering.md) measured a failure of the manager guessing which node a reply belonged to. This never
> asks it to guess, which is why the thing that killed batching there does not reach the form adopted here.
>
> ### 3. What the ceiling counts
>
> **One thing awaiting a reply**, which may be a payload carrying more than one question from one worker. [When the
> human's channel is free](108-when-the-humans-channel-is-free.md) is untouched: its ceiling, its floor and its
> freeing rule all stand at their existing values.
>
> **One nuance, because that node's worker aimed at this one and missed slightly.** Flag `108.1` future-proofed the
> **number**, writing the rule as a ceiling plus a top-up so a later node could move it. What actually moved is the
> **unit**. The number is still one.
>
> ### 4. What a reply to a payload means
>
> - A reply **naming a question or an option** settles what it names.
> - A reply that **assents to the recommendation without naming any question** — *"ok for recommended"* and the like
>   — settles **every** question's recommendation in that payload, and settles **nothing in the payload that is not a
>   recommendation**.
> - A question the reply **does not name is unanswered**, and goes out in a later payload. The worker never reads
>   silence as assent and never answers it itself.
> - **The human deferring stays something they say.** An unnamed question is not a park.
>
> **That the bare assent reaches everything is the human's**, `verbatim`: *"ok for recommened says ok for
> everything"*. The rest is derived from it.
>
> **[What the manager works on next](16-human-steering.md) confirms this rather than contradicting it.** Its first
> round carried one worker recommendation plus three manager notes offering three decisions to pull forward; the
> reply *"yes for recommendation"* reached the recommendation and not the offer, which that node records as a miss.
> Under the rule above that is the **correct** outcome, and what went wrong was a non-recommendation placed in a
> payload while an answer to it was expected. This rule forbids that by construction.
>
> ### 5. Numbering
>
> More than one question: each is numbered, titled, carries its own recommendation and the alternatives it sets
> aside, and is separated from the next. Exactly one question: **not numbered** — the presence of numbering is itself
> the signal that the payload holds more than one.
>
> **A question's number is fixed for the life of the attempt.** Numbers are never reused and never renumbered, so a
> payload re-asking an earlier question uses that question's original number and a new question takes the next unused
> one. Without that, *"Q1 ok"* means a different question in each round.
>
> ### 6. How many a payload may carry
>
> **No cap.** Independence is the only membership rule, which is the skill's own and the only one with a reason
> behind it. Measured on this effort: every grilling node ran one or two rounds carrying one question each, so a cap
> would bind on nothing, and the map's standing preference refuses machinery built for a predicted need.
>
> ### 7. What the human predicted, and why none of it is shipped
>
> Their words, `verbatim`: *"in practice it is unlikely I say it I think, as I will create my message one question at
> a time, so it will be more Q1 ok Q2 ok Q3 .."*.
>
> **A prediction, not an undertaking, and it is recorded here and travels no further.** Shipped text says what a
> reply **means** and never what it will look like: no worker requires a numbered reply, and nothing anywhere assumes
> one. Numbering the questions is what invites a numbered answer, and putting the format burden on the scarce
> resource would buy nothing.
>
> **What it does change is where §4's weight sits.** The bare assent was this record's modal reply because every
> payload held one question, so assenting was unambiguous and correct. Under numbering they expect to answer per
> question, which makes §4's first clause the common case and its bare-assent clause the residual one. **The
> measurement is re-scoped rather than falsified**, and the residual clause is kept because a rule with no answer for
> the residual case is where a worker guesses.
>
> ### 8. The skill's word for a round's questions may not travel
>
> The skill calls them the **frontier**. [CONTEXT.md](../../CONTEXT.md) fixes **Frontier** as *"the nodes that are
> open, unblocked and unclaimed"*. Same word, two denotations, so the skill's vocabulary cannot be imported as
> written.
>
> ### 9. Where the rule has to live, established rather than assumed
>
> **In the contracts' own text, never delegated to the invoked skill.** Flags `102.3`, `94.5` and `91.3` are three
> consecutive grilling workers running the contract's inline discipline while both named skills were present in
> session. A batching rule that lived only in the invoked skill would have been picked up by none of them.
>
> **And the grilling contract is ambiguous on this today.** Its discipline list is prefaced *"Where they are not
> present, this is the whole of the discipline"* — so where `/grilling` is present the *"One question at a time"*
> bullet does not formally bind, while `/grilling` now instructs the opposite and the question shape's `ASK` field
> still admits one. The file has been contradicting itself since the skill changed upstream, and nothing reported it.
>
> ### 10. What this does not decide
>
> - **The target of concurrently running nodes that need the human**, and the open offer to raise it. Unaffected:
>   this changes what one payload carries, not how many payloads exist, and that target governs how many nodes may
>   produce one.
> - **Tier membership.** Untouched.
> - **The manager's own streaming-versus-batching choice**, which stays settled as streaming.
> - **The name of any term another node may rename.**

## Index line

*The worker's, pasted.*

> Batching is adopted inside a node and refused across them: one worker may put several independent questions in one
> numbered payload, and the manager never combines two nodes'.

## Flags

`117.1` `ASSUMPTION` **settled** — **No cap on how many questions a payload may carry.** Independence is the only membership
rule. I settled it rather than asking because I measured that every grilling node in this effort ran one or two
rounds carrying a single question each, so any cap I could name would bind on nothing, and because the map's standing
preference refuses machinery built for a predicted need. If the frontier of a node's design tree ever turns out wide,
this is the line to revisit.

`117.2` `ASSUMPTION` **settled** — **A lone question is not numbered.** Numbering only where a payload holds more than one, so
that the presence of numbering is itself the signal that there is more than one thing to answer. The alternative —
number always, for uniformity — costs the human a signal they get for free, and the human was not asked.

`117.3` `ASSUMPTION` **settled** — **A question's number is monotonic across an attempt and never reused.** A payload re-asking
an earlier question keeps that question's original number. Derived from the partial-reply case rather than from
anything the human said: renumbering per payload makes *"Q1 ok"* denote a different question in each round, and the
effort's own id discipline already prefers a sequential id that never changes.

`117.4` `ASSUMPTION` **settled** — **A question a reply does not name is unanswered, not parked.** It goes out in a later
payload, and the human deferring stays something they say. Settled because reading silence as a deferral would infer
an act they did not perform and would stop the node, where reading it as unanswered costs one payload and keeps the
node moving.

`117.5` `ASSUMPTION` **settled** — **The human's predicted reply form does not reach the shipped text.** They predicted answering
per question and hedged it themselves. I record it as evidence for where the rule's weight sits and ship none of it:
no worker requires a numbered reply and nothing assumes one, because a prediction about one human's habits is not a
property of the workflow.

`117.6` `ASSUMPTION` **settled** — **The skill's word `frontier` is forbidden for a payload's questions rather than qualified.**
The glossary fixes `Frontier` for the open, unblocked, unclaimed nodes. I chose outright refusal over a qualified
variant because a second sense of a fixed word is what the glossary's refusals exist to stop.

`117.7` `ASSUMPTION` **settled** — **`/grilling` was read in full and one of its instructions left unrun; `/domain-modeling` was
not invoked.** Reading `/grilling` was this node's own work. I ran its design-tree ordering, its
recommendation-per-question and its rule that finding facts is mine rather than the human's. I left *"Ask the whole
frontier in one round"* unrun, under the contract's clause that the hard rules govern: the question shape admits one
question, and batching in order to ask whether to batch would have settled this node's own question on the human's
behalf. `/domain-modeling` I did not invoke, running the glossary check by hand instead and finding one collision;
this is the fourth consecutive instance after `102.3`, `94.5` and `91.3`, and I record it as evidence for node 113
rather than asking for the judgement again.

## Invalidations

*The worker's, pasted.*

> **[What the manager works on next, and how the human redirects it](16-human-steering.md), its `### 1. The attention
> queue` section.** Two of its sentences no longer hold:
>
> - *"**Question batching is dead**"* is reversed for the intra-node form. It is still correct for the inter-node
>   form, which this node refuses on that node's own ground.
> - *"Batching is by definition two live questions"* is too narrow as a definition, and being too narrow is what made
>   the conclusion above look forced. The form adopted here is **one** live payload carrying two questions, which
>   that definition does not contemplate.
> - *"keeping it to a name and a kind is what keeps a terse reply attributable to exactly one thing"* is falsified as
>   a **reason** while the rule it justifies survives on its other ground. Repaired by the second node above.
>
> **What that node keeps.** Its refusal of two *live* questions, its two tiers and their order, and its reading that
> node 08's manager-level choice between streaming and batching has one branch — the manager still streams.
>
> **[When the human's channel is free](108-when-the-humans-channel-is-free.md) is not contradicted** and I name it
> because a reader will look. Its ceiling, floor and freeing rule stand at their existing values. Its flag `108.1`
> anticipated a node moving the **number**; what this node moved is the **unit**, and the number is still one.

## Retrospective

*The worker's, pasted. Handed back as text on this effort only, and never filed by the worker.*

> **1. What I had to hunt for.**
>
> - **The external skill, and decisively its history.** My node file told me to read it and did not say where it is,
>   and its path is not derivable from the session's skill list. I looked first in `/home/mathieu/.claude/plugins/`,
>   which holds only marketplaces. `find / -maxdepth 8 -type d -iname '*mattpocock*'` returned **two** nix store
>   paths, and the second one is what made the node answerable: the older copy holds an `in-progress/batch-grill-me`
>   experiment plus a `grilling` that says *"Asking multiple questions at once is bewildering"*, and the active copy
>   has promoted the experiment's text into `grilling` verbatim and deleted the experiment. **Nothing pointed me at
>   the superseded copy; I found it by listing both.** Working out which was active took cross-referencing the
>   session's skill list against each path's contents, where `writing-for-agents` against `writing-great-skills` was
>   the discriminator.
> - **The token mechanism, which was the instruction's first claim.** [How an agent workflow and its skills reduce
>   their own token cost](52-token-cost-of-a-workflow.md) has it — a subagent's five-minute cache TTL, and its own
>   sentence that *"a worker paused for a human answer — the whole interview shape — is liable to come back cold"*,
>   against a ~19,840-token map read paid uncached. **`decisions.md`'s line for that node does not mention the TTL at
>   all.** I found it by grepping the node for `TTL|resum`. The single most load-bearing fact for my node was
>   invisible from the index I was pointed at to judge relevance.
> - **How this human actually replies.** Nothing collects it. I built it by grepping every node file for recorded
>   answer blocks and sorting by word count, which produced the *"ok for recommended"* count and — the thing that
>   decided my first question — the four instances where they volunteer a node number themselves. It decided both of
>   my questions.
> - **Round counts, to price a cap.** `grep -c '### Attempt .*round'` matches only recent nodes; older ones head
>   their rounds `### Attempt 1 — routing key ...`. Two incompatible interview heading formats in one corpus, and the
>   first count I got was wrong because of it.
>
> **2. What I read and did not use.** Node 108 in full, about 320 lines, for its §3 and flag `108.1` — roughly twenty
> lines; its five annotations and its retrospective I read and did not use. Node 16's §2 through §6 — streams,
> readiness floor, overrides, reporting — where I used §1 and one interview round. `map.md`'s landing policy,
> worktree lifecycle, dogfood target, review route, most of the fog and all of out-of-scope, none of which bore on my
> node and which is most of a 19.8k-token read. The other forty-odd skills in both plugin copies, listed only to
> identify the active version.
>
> **3. What would have made this node easier.**
>
> - **A spawn that names an external source should carry its path**, and where that source is versioned on disk
>   should say so. Both facts that answered this node came from the file layout rather than the file, and one came
>   from a copy nothing mentions.
> - **`decisions.md`'s line for node 52 omits the fact that made node 52 relevant to me.** The index is for judging
>   relevance and it is one sentence by design, and on the question I was sent to answer it is silent about the
>   mechanism that answers it. That is the cap working as specified and still failing, which is worth more than a
>   complaint about the cap.
> - **No collected record of the human's own reply forms.** Every grilling node either re-derives it by hand or, more
>   likely, proceeds without it. Mine decided two questions and cost two greps.
> - **The spawn, the node file and the instruction all read as though batching were one thing.** The entire
>   difficulty was that it is two, and separating them is most of what I did. One line in the node file asking
>   *whose* questions and held by *whom* would have got me there sooner — though finding that out may simply have
>   been the node.
>
> **4. What was stale, wrong, or contradicted something else.**
>
> - **The grilling contract contradicts itself today, and nothing reported it.** Its discipline list is prefaced
>   *"Where they are not present, this is the whole of the discipline"*, so the *"One question at a time"* bullet does
>   not bind where `/grilling` is present — and `/grilling` now instructs the opposite, while the `ASK` field still
>   admits one question. It has been in that state since the skill changed upstream. **This is `map.md`'s fog item
>   *"Nothing watches a standard that lives outside this repository"* firing a second time**, and the first firing is
>   recorded on node 47.
> - **`.claude/skills/expedition/SKILL.md`'s *"Exactly one question is in front of the human at a time"*** is now
>   false as worded, as is the *"attributable to exactly one thing"* clause below it. Both surfaced as a node rather
>   than left as observations.
> - **Node 16's *"Question batching is dead"***, on `INVALIDATIONS`.
> - **The spawn's characterisation of flags `102.3`, `94.5` and `91.3` is not quite what they say.** It offered them
>   as evidence that *"this effort has a measured habit of treating per-question overhead as small"*. Each records
>   that loading a **method skill** was not judged worth its cost, which is the cost of invoking a skill and not the
>   cost of a relay round-trip. Two different overheads, and the flags are strong evidence for the first and none for
>   the second. They were still useful, for a different thing: they are what established that a batching rule has to
>   live in the contract's own text.
> - **My node file's premise that the record has nothing about the skill's batching** was right, and its
>   adjacent-node note pointing at node 113 was the most useful line in the file.

***The manager's note on part 4's last bullet, against itself.*** **The correction is accepted and the error is the
manager's.** The spawn offered flags `102.3`, `94.5` and `91.3` as evidence of a measured habit of treating
*per-question overhead* as small. They record no such thing: each is a worker judging that loading a **method skill**
was not worth its cost. The manager conflated the cost of invoking a skill with the cost of a relay round-trip, and
put that conflation into a spawn as though it were measured. **It is the same failure as flag `103.8`** — a claim
stated to a worker with more confidence than anything established supports — and this is its second instance in a
spawn. The worker used the flags correctly for a different thing and said so.
