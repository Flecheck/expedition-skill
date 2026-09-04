# Whether the manager sends the human questions in batches

Type: grilling
Status: claimed

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
