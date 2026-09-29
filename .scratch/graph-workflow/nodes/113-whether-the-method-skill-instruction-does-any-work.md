# Whether the contracts' instruction to invoke a method skill is doing any work

Type: grilling
Status: resolved
Supersedes: 51

## Question

*Surfaced by [Starting an effort has no section in the manager's contract](98-starting-an-effort-has-no-section.md)'s
worker, and pasted as it wrote it.*

> Five worker contracts tell a worker to invoke `/grilling` and `/domain-modeling` *"if they are present"*, then
> state the whole discipline inline for the case where they are not. Three consecutive grilling workers have now
> found them present — as `mattpocock-skills:grilling` and `mattpocock-skills:domain-modeling` — declined to invoke
> them, run the contract's own stated discipline instead, and flagged the departure: flags `102.3`, `94.5`, and this
> node's. Enumerator: `grep -rln "domain-modeling" nodes/` returns eleven node files, of which two record the
> departure as a flag and the rest concern naming or contract structure. So the instruction has a zero-for-three
> compliance record among the workers best placed to follow it, which is evidence that the inline discipline is
> sufficient and the invocation adds nothing — or that the instruction is worth enforcing and three workers were
> wrong. **Adjacent and deliberately not merged:** [What a contract may name as a method
> skill](51-what-a-contract-may-name.md) asks how the skill is addressed; this asks whether it should be invoked at
> all, and the two answers compose.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The three flags this node is about are `102.3`, `94.5` and `91.3`**, and all three are outstanding. Each asked for
the judgement back and none has been answered, which is why the third worker surfaced a node rather than filing a
fourth silent flag. **The enumerator in the question searches `nodes/`**, which [node
94](94-condition-scope-as-a-predicate.md)'s flag `94.2` bars an *acceptance condition's* enumerator from doing — that
bar is on conditions rather than on a question's evidence, so nothing here is in breach, and it is named so no later
reader mistakes one for the other.

## Interview

### Attempt 1, question 1 — written and queued, not yet put to the human

***Recorded by the manager as a queued payload, not as a question the human has been asked.*** Node 107's question
held the channel and node 116's gate was already queued when this arrived. **Pasted as the worker wrote it**; the
manager authored none of it and has taken no view on it.

> **ABOUT:** Four of the six shipped worker contracts tell their worker to "Invoke <skill> if it is present", and the
> grilling contract makes its whole stated discipline conditional on that skill's absence. Five workers have now
> reported on that line and it has never once worked as written. This decides what happens to the line.
>
> **What I did that nobody had done yet: I invoked both skills, and I measured what they cost.** The effort had four
> reports about that line and no measurement of it.
>
> **The cost, measured.** Byte counts are exact; the token column is derived at node 52's own ratio, which is exactly
> 4 bytes per token — i.e. the rule of thumb, not a tokenizer count.
>
> | named by | skill | bytes | ≈ tokens |
> | --- | --- | --- | --- |
> | grilling | `/grilling` | 1,987 | ~500 |
> | grilling | `/domain-modeling` | 3,331 | ~830 |
> | implementation | `/coding-principles` | 5,089 | ~1,270 |
> | implementation | `/naming` | 7,265 | ~1,820 |
> | research | `/research` | 794 | ~200 |
> | prototype | `/prototype` | 2,931 | ~730 |
> | **no contract names it** | `/writing-for-agents` | 10,886 | ~2,720 |
>
> The most expensive contract is implementation, at ~3,090 tokens. The same worker's `map.md` read is 40,344 bytes,
> ~10,090 tokens. **So no contract's skills cost more than 31% of a read that worker already pays, and the grilling
> pair is 13%.** Three workers declined to invoke on the ground that it was not worth its cost (flags `102.3`,
> `94.5`, `91.3` — *"not worth its cost"*, *"spent the budget on three measurements instead"*). **That ground does
> not survive measurement.** It was also never the binding objection, so retiring it changes nothing below.
>
> **What the skills actually contain, from invoking them.** `/domain-modeling` excludes its own reader in its opening
> paragraph: *"Merely reading `CONTEXT.md` for vocabulary is not this skill... This skill is for when you're changing
> the model, not just consuming it."* A grilling worker consumes the glossary and cannot change it — hard rule 3
> forbids writing any file. Of its six operative instructions, two write files and three are written as speech to the
> human, all forbidden. **One is runnable: challenge your text against the glossary — and running it found two real
> defects** (below). So 1 of 6, and the one that works is a duty the map's `## Notes` already imposes independently.
> `/grilling` fares a little better: **2 of its 7 instructions add something the contract's inline list lacks** —
> work decisions in dependency order, and dispatch a sub-agent for facts without blocking on it. Three conflict with
> hard rules or with the mandated `ASK:`/`RECOMMENDED:`/`ALTERNATIVES:` shape. One uses **frontier** in the sense
> this effort's glossary refuses.
>
> **The record is five instances with three different causes, not one failure repeated.** Flag `69.3`, which I found
> and which nobody offered me, is the earliest and it breaks the pattern: the bare names **do not resolve at all** —
> the skills register as `mattpocock-skills:grilling` and `mattpocock-skills:domain-modeling`, and that worker *"did
> not translate the names."* Flags `102.3`, `94.5` and `91.3` did translate them and declined on cost. Node 117's
> worker read `/grilling` in full, ran three of its instructions and refused a fourth on a hard-rules ground. So "did
> the worker comply?" is indeed not a binary, and all three flags read **settled** today rather than outstanding.
>
> **The decisive evidence is from the contracts where workers *did* comply.** `/coding-principles` and `/naming` were
> invoked as required at nodes 74 and 116, and reported: *"neither had a part to leave unrun"*, *"honestly thin on a
> prose deliverable"*, *"near-no-ops on prose"*. They are the most expensive pair the line names. Meanwhile
> `/writing-for-agents` — which **no contract's skill line names**, reachable only through the map's ground rule 5 —
> was invoked at node 103 and made four concrete edits to the deliverable. **The line's naming is anti-correlated
> with usefulness, and with cost too: the effort pays most for the least useful pair.** Compliance was never the
> variable.
>
> **What that tells me the real defect is.** The line names skills **by node kind**. What determines whether a skill
> does any work is whether the worker may write files and talk to the human — which by hard rule it may not — and the
> deliverable's medium, prose or code. **Neither is predicted by the kind.**
>
> **Two things I settled myself.** Running `/domain-modeling`'s one usable instruction against `CONTEXT.md` found: its
> `## The five kinds of node` says *"three of them name a skill the worker invokes"*, which is **wrong by one** —
> four do, and only `precondition` names none; and its **grilling** entry still says *"one question at a time"*,
> superseded by node 117, and **not covered by node 126**, whose condition names one file only. Both come back as
> flags.
>
> **One sequencing hazard.** Node 126 is open, is implementation, and edits the exact passage this node is about. Its
> clause 9 already forbids the conditional-on-a-skill construction for its own eight items: *"None of them is left to
> be supplied by any skill the file instructs the worker to invoke."* That is a partial answer to this node already
> banked in an open acceptance condition. Whichever of the two lands second re-edits the same lines. Node 51, which
> this node's answer composes with, is **open**.
>
> **ASK:** What happens to the "Invoke <skill> if it is present" line in the four contracts that carry it — grilling,
> implementation, research and prototype?
>
> **RECOMMENDED:** Delete it, along with the "Where they are not present, this is the whole of the discipline"
> preface, from all four. Each contract's stated discipline becomes the whole discipline, unconditionally; the
> grilling contract gains two bullets carrying what `/grilling` uniquely had (work decisions in dependency order;
> dispatch a sub-agent for facts rather than asking, and do not block on it); the skills stay named in `map.md`'s
> `## Notes`, which already lists all six and is how `/writing-for-agents` reaches a worker today anyway.
>
> It rests on five things. (1) Ground rule 2 is already this effort's commitment — *"each shipped worker contract
> stands alone as a file, rather than depending on any skill being invocable"* — and today four contracts depend on
> one; this is the option that makes the rule true rather than aspirational. (2) The measured content is thin: 2 of 7
> usable in `/grilling`, 1 of 6 in `/domain-modeling`, near-no-ops reported three times for the implementation pair.
> Two bullets recover nearly all of it. (3) Repairing the naming instead means predicting which skill will bite per
> node kind, and the evidence is that the medium decides, not the kind. (4) It removes the self-contradiction node
> 117 found instead of patching around it, and makes node 126's clause 9 trivially true. (5) Against it, honestly:
> this cuts a live tie to an upstream discipline that has been ahead of the contract exactly once — `/grilling` was
> rewritten to ask a round of questions at a time, which node 117 later adopted. But the effort reached that
> conclusion on its own, without the invocation, while the four workers who did have the skill available did not act
> on it. The tie's one demonstrated benefit did not arrive through the mechanism it would defend, and the map's own
> fog records an external standard moving under a resolved node within an hour — so keeping the line retains a hazard
> that has already fired and a benefit that never has.
>
> **ALTERNATIVES:**
> - Keep the line, repair what each contract names: drop `/domain-modeling` from grilling by name, name
>   `/writing-for-agents` where the deliverable is prose. Needs node 51 settled first, since flag `69.3` shows the
>   bare names do not resolve.
> - Keep the line, change what it asks for: read the skill for method only, with this contract's shapes and hard
>   rules governing and nothing in the file conditional on the skill. Cheapest edit; keeps the upstream tie.
> - Status quo, enforced as mandatory. Contradicted by all five grilling instances and by the three reports from
>   workers who did comply.
> - Delete the line only from the grilling contract, where the evidence is first-hand, and leave the other three
>   pending their own measurement.

***The manager's note beside it, and not the worker's. Three things it did that the manager records rather than
praises, because each is a fact the graph did not hold an hour ago.***

**It measured the cost the map's own priority rule requires and nobody had.** The map ranks a token-reducing node
above one that does not and refuses *"prioritising one whose size has not been measured"*. The manager's spawn told
this worker the number did not exist and not to estimate it. **It went and produced it**, marked the derivation as a
4-bytes-per-token rule of thumb rather than a tokenizer count, and used it to retire the ground three flags had
declined on — including by showing that ground was never the binding objection, so retiring it changes nothing.

**It found a fifth instance the manager did not offer, and it is the one that breaks the pattern.** Flag `69.3`: the
bare skill names **do not resolve at all**, the skills registering as `mattpocock-skills:grilling` and
`mattpocock-skills:domain-modeling`. So the record the node was built on — a compliance record — is five instances
with three distinct causes, and the manager's spawn had framed it as one failure repeated.

**It named a gap in a condition the manager filed twenty minutes earlier.** `CONTEXT.md`'s **grilling** entry still
says *"one question at a time"*, superseded by node 117, and [node
126](126-carry-question-batching-into-the-grilling-contract.md)'s condition **names one file only**, so nothing
covers it. The manager filed that condition and did not notice. **The manager has not amended it** — widening a
condition to a new file is a new demand, outside [node 82](82-amending-a-condition-whose-scope-was-too-narrow.md)'s
permission — and the gap is recorded here and named in this node's own flags by its worker.

### A direction of the human's, arriving while Q1 was live and not naming it

**Their words, `verbatim`**, written at the moment they spoke. The message carried three separate things and this is
the third; the other two became [node 128](128-whether-qmd-lowers-this-workflows-token-cost.md), [node
129](129-what-to-do-about-the-records-token-cost.md) and [node 130](130-the-docs-discipline-this-workflow-ships.md):

> I also would want the skill to not depend on mattpockock, I don't know what is the status of this. Add grilling
> directly on the skill and for the docs part we should make something. Inspired by "/domain-modeling" and
> https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

***The manager's note, and not their words. This is recorded as a direction beside Q1 rather than as an answer to
it, and the reading is the manager's.***

**Under [node 117](117-questions-sent-in-batches.md)'s rule a reply settles what it names, and this names neither Q1
nor any of its options.** So **Q1 is still live and unanswered.** Whether their direction nonetheless answers it is
the worker's to judge, not the manager's, and it has been put to the worker as their words.

**What the direction does and does not overlap.** Q1 asks what happens to the *"Invoke <skill> if it is present"*
line in four contracts. Their direction is wider in one way and narrower in another:

- **Wider:** it asks that the skill *not depend on mattpockock* **at all**, which reaches the map's `## Notes` line
  naming `/grilling`, `/domain-modeling`, `/naming`, `/coding-principles` and `/prototype` — and the worker's own
  recommendation would have **kept** the skills named there. It also reaches ground rule 5, which locates
  `/writing-for-agents` in that plugin by name and which every prose deliverable on this effort is held against.
- **Narrower, or at least different:** it asks that the grilling discipline be added **directly** to the skill,
  where the worker's recommendation added two bullets carrying what `/grilling` uniquely had. Whether *"add grilling
  directly"* means those two bullets or the whole of that skill's method is not settled by these words.
- **New:** *"for the docs part we should make something"* is a deliverable that does not exist and that no node
  reached. It is [node 130](130-the-docs-discipline-this-workflow-ships.md), minted from this message and not folded
  into this node.

**One fact the manager holds and states, since they said they did not know the status.** This node **is** the status:
it is claimed, running, and its first question — what happens to that line — has been in front of them since before
this message. Its worker measured the invocation cost, which nobody had, and found the line's naming anti-correlated
with usefulness.

### Attempt 1, second payload — two questions, and the first use of node 117's batching rule

***Pasted as the worker wrote it.*** The manager authored none of it and has taken no view on either question.

**Two facts it established before answering, and both change the shape of the node.**

> **No shipped file names the plugin at all.** `grep -rn "mattpocock" .claude/skills/expedition*/` returns nothing
> across all six shipped contracts. The shipped corpus's entire dependency on the plugin is the six bare names in
> the four `Invoke` lines. And **of those six, only four are plugin skills** — `/grilling`, `/domain-modeling`,
> `/research`, `/prototype`. `/coding-principles` and `/naming` are the human's own, at
> `/home/mathieu/dotfiles/programs/claude/skills/`, which is why they appear unprefixed in a worker's skill list
> while every plugin skill carries `mattpocock-skills:`. Their direction reaches four of the six literally.
>
> **The shipped corpus already contains the pattern their direction asks for.** `expedition-checker/SKILL.md` names
> *no* skill. It describes the shape instead — *"let no part of a reviewing skill run in an agent that would be
> handed less than you were"* — and offers a fork: *"Invoke it with the givens supplied"* or *"Decline to invoke it,
> and hold the work against the standards you found by hand instead."* The map supplies which skill. It is the only
> contract that names none, and the only one no worker reported as thin or unrun.

**What the human's direction did to its own earlier answer, in its words:**

> **Does the direction change my recommendation? Yes, in two ways, and it settles a third.**
>
> **It settles Q1's disposition half.** Each of my three alternatives — repair the naming, soften the verb, enforce
> as-is — keeps a plugin skill named inside a shipped contract. Their standing preference now forbids that, so only
> deletion survives. That is a consequence of their words rather than my pick, and I mark the reading as mine: if
> they meant only that the workflow must not *break* without the plugin, the alternatives return.
>
> **It withdraws part of my recommendation.** I had the skills resting in `map.md`'s `## Notes`. I withdraw that for
> `/grilling` and `/domain-modeling`: once node 126 lands the rounds half and node 130 ships the docs discipline,
> those two entries point at a dependency that has been replaced. I am not defending that part.
>
> **It does not change the two bullets, and the ambiguity the manager flagged mostly dissolves as a matter of fact.**
> "Add grilling directly on the skill" cannot mean the whole method, because the whole method is not addable. Of
> `/grilling`'s seven instructions: node 126 is already landing the rounds/numbering/independence half directly into
> the contract's own text; three cannot be added at all, conflicting with hard rules 2, 3 and 5; one uses
> **frontier** in the sense the glossary refuses. That leaves exactly the two I proposed. **Node 126 plus two
> bullets *is* `/grilling` added directly** — there is no third reading with more of it in.

**Its `ASK`, both questions, as numbered by the worker:**

> **Q1 — Which contracts owe shipped replacement text.** With the four `Invoke` lines deleted, the grilling contract
> is covered: node 126 lands the rounds half and two new bullets carry the rest. Research, prototype and
> implementation are not. Their inline disciplines are three, five and the bar's properties respectively. Do those
> three get shipped method text of their own now, or do they stand on the text they already have?
>
> **Recommended: add nothing to those three; their inline disciplines stand.** No node in the record shows
> `/research` or `/prototype` ever being invoked — I found no instance either way, so I have no evidence they add
> anything. `/coding-principles` and `/naming` were invoked three times and reported near-no-ops on prose, which is
> the only medium this effort produces. Where a shipped discipline is genuinely owed, this effort mints a node for
> it, as it just did with node 130. Ground rule 4 prefers short prose over machinery for predicted needs, and the
> first worker to find an inline discipline actually short can surface a node then.
>
> Set aside: ship a method file per kind now, so the workflow is self-contained in one pass rather than four; ship
> one shared method file the contracts point at — which runs against node 50, where shared blocks were settled to
> stay duplicated; keep `/coding-principles` and `/naming` named on the ground that they are the human's own skills
> and outside the direction's reach, accepting that a shipped contract then assumes this machine's dotfiles, which
> ground rule 1 forbids.
>
> **Q2 — Whether "not depend on mattpockock" reaches this effort's own bar.** Ground rule 5 holds every prose
> deliverable on this effort, including this node's, against `/writing-for-agents` — a plugin skill, named as such.
> The map's review route names `mattpocock-skills:code-review` too. Both live in `map.md` and neither ships. Does the
> direction reach them?
>
> **Recommended: no — it binds what the workflow ships, and ground rule 5 stands unchanged.** Ground rule 5 already
> anticipates this in its own text: the standard *"is specific to this repo, is never shipped, and is located by name
> in the `mattpocock-skills` plugin rather than by path."* It was written as a deliberate, marked exception. The
> constraint that matters is the map's own — that the workflow run on repositories this machine has never seen — and
> a never-shipped house style travels nowhere to violate it. After Q1's deletion the shipped corpus names no plugin
> skill, which is the whole of what "the skill should not depend on mattpockock" asks. The other reading is expensive
> for nothing: `/writing-for-agents` is the one skill my measurement found actually changed a deliverable, and
> replacing it would mint a third shipped-discipline deliverable on top of node 130's, improving the shipped workflow
> not at all.
>
> Set aside: it does reach them, so the effort's own bar and its recorded review route need a vendored prose
> standard, widening node 130; it reaches the review route only, the checker being a shipped mechanism even though
> the route naming its skill is not; keep ground rule 5 but require it to name the standard by its content rather
> than by plugin name, so a missing plugin degrades the bar instead of removing it.
>
> **One risk I am not asking about, because it is theirs to know rather than to decide.** Under my recommendation,
> ground rule 5 and the review route both remain single points of failure in the same plugin: if it goes away, this
> effort loses its only prose standard and its recorded review route, and the map's own fog already records an
> external standard moving under a resolved node within the hour. That is an effort-continuity risk, not a defect in
> what ships.

## Annotation: node 117's numbering clause was broken on its first application

*Filed by the manager against the payload above. **The payload is not altered by this annotation**, and the worker's
numbering stands as it wrote it.*

**What node 117 settled, resolved less than two hours before this payload:** *"A question's number is fixed for the
life of the attempt. Numbers are never reused and never renumbered: a payload re-asking a question asked earlier in
the same attempt uses that question's original number, and a question asked for the first time takes the next number
not yet used in that attempt."* Its worker derived that clause from the partial-reply case, on the ground that
*"renumbering per payload makes 'Q1 ok' denote a different question in each round."* It is flag `117.3`, settled.

**What happened.** This attempt's first payload asked *"What happens to the 'Invoke <skill> if it is present' line in
the four contracts that carry it"* and labelled it **Q1**. This second payload labels a different question **Q1** —
*"Which contracts owe shipped replacement text"* — and takes **Q2** for a second new one. **So `Q1` denotes two
different questions within one attempt, which is exactly what the clause forbids and exactly the failure it names.**

**The manager's part in it, stated first.** The manager relayed that clause to this worker in the spawn, in its own
words: *"Your Q1 keeps its number; numbers are fixed for the attempt and never reused"* — that instruction went to
node 107's worker. **The spawn that started this node carried the rule in general terms and did not say that its
earlier question already held `Q1`.** So the worker was told the rule and not the state it applied to.

**Why the payload was relayed rather than sent back.** The content is sound and the substance is unaffected; only the
labels collide. Sending it back would have held finished work out of the human's channel to fix a label, and node
108's floor says a written question waiting with a free channel is owed to them at once. **The manager relayed it
with the collision named in its own words**, and stated to the human that a reply naming a number will be recorded
against these two questions and not the earlier one — which removes the ambiguity for the human without altering the
worker's text. The earlier `Q1` is not in front of them: the worker's own reading is that their standing direction
settled its disposition, and that reading is marked as the worker's.

**What is not settled and is nobody's node.** Whether the manager owes a worker its own outstanding question numbers
in a spawn or resume, which is the state this worker was missing. It is a duty of the manager's that node 117's
answer does not mention.

### Attempt 1, answer to the first payload

**The human's word, `verbatim`**, written at the moment they spoke. It arrived inside a message carrying four things;
this is the third:

> For 113 ok

***The manager's determination of what it reaches, and it is narrower than a bare assent would normally be.***

**It answers the FIRST payload and cannot reach the second.** Under [node 117](117-questions-sent-in-batches.md)'s
rule a bare assent to the recommendation *"settles every question's recommendation in that payload"* — but **the
second payload was never delivered.** It was recorded here and queued behind node 114's gate under the tier order,
and the manager's last words to the human named the first payload's question as the live one. **The human cannot
assent to a payload they have not seen**, so the second payload's `Q1` and `Q2` remain **unanswered and still
owed to them**.

**The option it does take, quoted in full and attributed to the worker who wrote it**, not to the manager:

> Delete it, along with the "Where they are not present, this is the whole of the discipline" preface, from all
> four. Each contract's stated discipline becomes the whole discipline, unconditionally; the grilling contract gains
> two bullets carrying what `/grilling` uniquely had (work decisions in dependency order; dispatch a sub-agent for
> facts rather than asking, and do not block on it); the skills stay named in `map.md`'s `## Notes`, which already
> lists all six and is how `/writing-for-agents` reaches a worker today anyway.

**And here is the complication the manager will not resolve.** **The worker has already withdrawn part of that
recommendation**, in the second payload, before the human's assent arrived. Its words: *"It withdraws part of my
recommendation. I had the skills resting in `map.md`'s `## Notes`. I withdraw that for `/grilling` and
`/domain-modeling`: once node 126 lands the rounds half and node 130 ships the docs discipline, those two entries
point at a dependency that has been replaced. I am not defending that part."*

So the human has assented to a recommendation **whose author retracted one clause of it in the interval**, and the
retraction is on this node but was never in front of them. **The manager has not decided which text their assent
lands on.** It is put back to the worker, which is the party that wrote both the recommendation and the withdrawal.

**What the manager does read as settled**, and marks as the manager's reading: the **disposition** — the four
`Invoke` lines and the conditional preface go, and each contract's stated discipline becomes the whole discipline
unconditionally. That clause of the recommendation is untouched by the withdrawal, and it is also what the worker
independently concluded their standing direction had already forced: *"only deletion survives."*

**One thing this instance is evidence for, recorded against the manager.** The renumbering collision annotated above
was judged harmless on the ground that the earlier question was off the queue and a reply would be unambiguous.
**That judgement was wrong in a way the annotation did not anticipate**: the ambiguity that actually arrived was not
between two `Q1`s but between two *payloads*, one delivered and one not. Node 117's rule governs a reply to a
payload; **nothing governs a reply that arrives while a later payload of the same attempt is queued undelivered**,
and that is the state this node was in. No node covers it.

## The worker's determination of what the assent settled, and its retraction of its own retraction

*Pasted as it wrote it. **The manager put the complication to it without a position and this is its answer**, which
is the party that wrote both texts.*

> **On what "For 113 ok" settled — my judgement, since I wrote both texts.** Their assent lands on **payload 1 as
> written, all four clauses, the `## Notes` clause included.** Three grounds. The contract's own rule is that an
> assent to an option makes that option theirs — and the option in front of them was payload 1. Hard rule 1 forbids
> me answering on their behalf, and reading their "ok" onto a retraction they never received would substitute my
> later judgement for their word, which is exactly that failure. And a retraction that was never delivered cannot
> subtract from what they endorsed.
>
> **More than that: my withdrawal was overstated on its own terms, and I retract the retraction.** My stated ground
> was conditional — *"once node 126 lands the rounds half and node 130 ships the docs discipline"* — and both nodes
> are open. So the `## Notes` clause is **correct today** and becomes wrong only when two open nodes land. I wrote
> *"I am not defending that part"*, which is stronger than my own ground supported. What I actually found is an
> **expiry**, not an error. So nothing is owed back to them on this: the clause is implemented as endorsed, and the
> expiry becomes a cascade obligation that nothing currently watches.
>
> **Payload-2 Q1 is moot, and was my defect.** Payload 1's endorsed text already said what each contract gains —
> grilling gains two bullets, and the other three have their existing discipline made unconditional. I re-opened a
> question my own endorsed recommendation had closed. Its answer would have been the same either way. **Payload-2 Q2
> is not my node's subject** and goes out as a new node. Numbers consumed on this attempt: `Q1` (payload 1,
> answered); payload 2's `Q1` label is void and its `Q2` is superseded by the new node. Any further question on this
> node starts at `Q3`.

## Answer

*Node 113's worker's `ANSWER`, pasted as it wrote it.*

> **The instruction was doing almost no work, and the little it did was negative.** The four `Invoke <skill> if it is
> present` lines and the conditional preface come out of all four contracts that carry them. Each contract's stated
> discipline becomes the whole of that discipline, unconditionally. The grilling contract gains two bullets carrying
> what `/grilling` uniquely had. The skills stay named in `map.md`'s `## Notes`. Settled by the human, `verbatim`:
> *"For 113 ok"*, assenting to the recommendation as offered.
>
> **The cost was measured for the first time here, and it was never the objection.** Byte counts exact; tokens
> derived at node 52's own ratio, which is exactly 4 bytes per token — the rule of thumb rather than a tokenizer
> count. `/grilling` 1,987 B (~500 tok); `/domain-modeling` 3,331 B (~830); `/coding-principles` 5,089 B (~1,270);
> `/naming` 7,265 B (~1,820); `/research` 794 B (~200); `/prototype` 2,931 B (~730). The most expensive contract is
> implementation at ~3,090 tokens, against a `map.md` read of 40,344 B (~10,090) the same worker already pays. **No
> contract's skills cost more than 31% of that read, and the grilling pair is 13%.** So the ground given in flags
> `102.3`, `94.5` and `91.3` — that loading them was not worth its cost — does not survive measurement.
>
> **The content was the objection.** `/domain-modeling` excludes its own reader in its opening paragraph: *"Merely
> reading `CONTEXT.md` for vocabulary is not this skill... This skill is for when you're changing the model, not just
> consuming it."* A grilling worker consumes the glossary and cannot change it, hard rule 3 forbidding any file. Of
> its six operative instructions two write files and three are written as speech to the human; **one is runnable**,
> and running it here found two real defects in `CONTEXT.md`. `/grilling` offers **two of seven** instructions the
> contract's inline list lacked; three conflict with hard rules 2, 3 and 5; one uses **frontier** in the sense this
> effort's glossary refuses.
>
> **Compliance was never the variable, and the node's framing as a compliance record was too coarse.** The record is
> **five** instances with **three** distinct causes, not one failure repeated. Flag `69.3` is the earliest and is
> unlike the rest: the bare names did not resolve at all, the skills being registered as `mattpocock-skills:grilling`
> and `mattpocock-skills:domain-modeling`, and that worker *"did not translate the names."* Flags `102.3`, `94.5` and
> `91.3` did translate them and declined on cost. Node 117's worker read `/grilling` in full, ran three instructions
> and refused a fourth on a hard-rules ground. All three of the cost flags read `settled` today, not outstanding.
>
> **The decisive evidence came from the contracts where workers did comply.** `/coding-principles` and `/naming` were
> invoked as required at nodes 74, 103 and 116 and reported adding nothing: *"neither had a part to leave unrun"*,
> *"honestly thin on a prose deliverable"*, *"near-no-ops on prose"* — and they are the most expensive pair named.
> Meanwhile `/writing-for-agents`, which **no contract names** and which reaches a worker only through ground rule 5,
> was invoked at node 103 and made four concrete edits to the deliverable. **The line's naming was anti-correlated
> with usefulness, and with cost: the effort paid most for the least useful pair.**
>
> **Why, stated as the form rather than the instances.** The line named skills **by node kind**. Whether a skill does
> any work is decided by the worker's permissions — which by hard rule forbid writing files and addressing the human,
> the two things these skills mostly instruct — and by the deliverable's medium, prose or code. **Neither is
> predicted by the kind.**
>
> **Two facts that bound how far this reaches.** No shipped file names the plugin: `grep -rn "mattpocock"
> .claude/skills/expedition*/` returns nothing, so the shipped corpus's whole dependency was six bare names in four
> lines. And **only four of those six are plugin skills** — `/coding-principles` and `/naming` are the human's own,
> at `/home/mathieu/dotfiles/programs/claude/skills/`, which is why they appear unprefixed in a worker's skill list.
>
> **The pattern to follow already ships.** `expedition-checker/SKILL.md` names no skill. It states the shape instead
> — *"let no part of a reviewing skill run in an agent that would be handed less than you were"* — with an explicit
> fork between invoking with the givens supplied and declining to invoke and working by hand. It is the only contract
> naming none, and the only one no worker reported as thin or unrun.
>
> **What is deliberately not removed.** Node 48's clause — *"Where a method skill's instructions and this contract's
> hard rules conflict, the hard rules govern"* — **stays in all four contracts.** `map.md`'s `## Notes` still names
> the six skills as ones a session should consult, so a worker may still invoke one on its own initiative and the
> reconciliation rule keeps its subject. Node 48 is therefore not contradicted.
>
> **One expiry, recorded because nothing watches it.** The `## Notes` entries for `/grilling` and `/domain-modeling`
> are correct today and stop being correct when node 126 lands the batching rules into the grilling contract and node
> 130 ships the docs discipline that replaces `/domain-modeling`. That is a cascade obligation on two open nodes, not
> a defect in what was decided here.

## Index line

*The worker's, pasted.*

> The four `Invoke <skill> if it is present` lines and the conditional preface go; each contract's stated discipline
> becomes the whole discipline, and grilling gains two bullets.

## Flags

`113.1` `ASSUMPTION` **· settled** — **What the human's assent landed on, where its author had retracted a clause in the
interval.** Their *"For 113 ok"* reached payload 1; payload 2, carrying my withdrawal of the `## Notes` clause, was
never delivered to them. I read the assent as settling payload 1 as written, all four clauses included, on the
contract's rule that an assent makes the offered option theirs and on hard rule 1's bar against answering for them. I
also judged my own withdrawal overstated: its stated ground was conditional on two open nodes, so the clause is right
today and merely expires. I therefore asked nothing back and implemented the clause as endorsed. The human may want
the reading back, since it is the one place their word and their worker's later judgement diverged.

`113.2` `ASSUMPTION` **· settled** — **Both method skills were invoked in full, and the parts left unrun are named.** Reading them
was this node's own subject, so I invoked rather than declined. From `/grilling` I ran the dependency ordering, the
recommendation-per-question, and the rule that finding facts is mine; I left unrun its `❓ Q1` round format (the
contract mandates `ASK:`/`RECOMMENDED:`/`ALTERNATIVES:`), its instruction to wait in-turn for a reply and not act
until the human confirms (hard rules 2 and 5), and its use of *frontier* (the glossary refuses it). From
`/domain-modeling` I ran only the glossary challenge, leaving unrun the two instructions that write files and the
four written as speech to the human.

`113.3` `ASSUMPTION` **· settled** — **`CONTEXT.md` miscounts the contracts that name a method skill.** Its `## The five kinds of
node` says *"three of them name a skill the worker invokes"*; four do — grilling, research, prototype and
implementation — and only `precondition` names none, its contract saying so explicitly. I read this as a stale count
rather than as counting something I could not see. Found by running `/domain-modeling`'s one usable instruction.

`113.4` `ASSUMPTION` **· settled** — **`CONTEXT.md`'s grilling entry contradicts node 117 and no node covers it.** It still reads
*"reached by interviewing them one question at a time"*, which node 117 superseded by adopting several questions in
one payload. Node 126's acceptance condition names exactly one file,
`.claude/skills/expedition-grilling/SKILL.md`, so the glossary sits outside its scope. I judged this an uncovered
cascade miss rather than surviving prose under the never-delete rule, because the glossary is declared authoritative.

`113.5` `ASSUMPTION` **· settled** — **Payload-2 Q1 was redundant and I treated it as moot rather than asking it.** It asked
whether research, prototype and implementation owe shipped replacement text; payload 1's endorsed recommendation
already answered it by making their existing discipline the whole discipline and giving new text to grilling alone. My
own recommendation on it had been to add nothing, so the reading costs nothing either way.

## Invalidations

*The worker's, pasted.*

> none. Node 48 was checked specifically and is **not** contradicted: its clause stays in all four contracts and
> keeps its subject, because `map.md`'s `## Notes` still names the six skills and a worker may invoke one on its own
> initiative.

## Retrospective

*The worker's, pasted. Handed back as text on this effort only, and never filed by the worker.*

> **What I had to hunt for.** *Where the plugin lives* — six calls and three dead ends: `known_marketplaces.json`
> lists only the official marketplace, the plugin is registered `@inline` with no path, and the home-manager
> generation holds no reference. I resolved it by matching the `domain-modeling` description text in my own spawn's
> skill list against two candidate store paths, which also revealed the upstream rewrite. *Node 52's bytes-per-token
> ratio* — I had to open node 52 to find 79,361 B → 19,840 tokens, i.e. exactly 4.0, the rule of thumb rather than a
> measurement; worth knowing before another node builds on that figure. *Flag `69.3`*, which nobody offered me and
> which changed the finding's shape from four instances of one failure to five instances of three. *Whether
> `/coding-principles` and `/naming` are plugin or user skills* — nowhere in the record, and decisive for how far the
> human's direction reached.
>
> **What I read and did not use.** Both older store paths' full diffs, useful only to establish that the upstream
> skill was reworded. Node 126's condition items 1–8 in detail, when only clause 9 bore on me. `map.md`'s `## Out of
> scope` and most of `## Not yet specified`. `CONTEXT.md`'s `Claim`/`Handover`/`Resolve` entries.
>
> **What would have made this node easier.** Being told which question numbers I already held — the manager has
> recorded that omission. Being told node 126 existed: its clause 9 already pre-decided part of my node's answer, and
> I found it only by an unprompted `ls`. A single line anywhere in the record saying which named skills are plugin and
> which are the human's own. And a rule for the case that actually bit: a reply arriving to payload 1 while payload 2
> of the same attempt sits queued and undelivered. Nothing on this graph governs that, and it is the one thing here
> that could have made me mis-attribute the human's word.
>
> **What I found stale, wrong, or contradicting something else.** My node file and my spawn both said flags `102.3`,
> `94.5` and `91.3` are outstanding; all three read `settled` in their node files. My spawn called the evidence
> "four-for-four"; it is five instances with three distinct causes. `CONTEXT.md` miscounts the contracts naming a
> skill, and its grilling entry contradicts node 117. `map.md` is 40,344 bytes against node 59's 26,971. And the
> three cost flags' shared ground is measurably wrong — the invocation was always a small fraction of a read those
> workers already paid.

***The manager's note on the retrospective's first and last points, both against the manager.*** **Its spawn said
the three cost flags were outstanding and called the evidence four-for-four.** Both were the manager's, and both
were wrong at the moment they were written: the flags had settled with the human's earlier approvals, and the record
was five instances rather than four. **That is the third and fourth instance this session of the manager stating more
in a spawn than the record supported**, after flags `103.8` and the per-question-overhead conflation on node 117.
The worker corrected both from the files.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
