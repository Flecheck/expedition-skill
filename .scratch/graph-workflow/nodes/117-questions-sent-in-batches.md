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
