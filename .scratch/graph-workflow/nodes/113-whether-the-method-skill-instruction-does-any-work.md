# Whether the contracts' instruction to invoke a method skill is doing any work

Type: grilling
Status: claimed

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
