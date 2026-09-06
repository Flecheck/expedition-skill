# Measure whether a fed file earns its place by running one node twice

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [Nothing sweeps what a retrospective reports as
read-and-unused](141-nothing-sweeps-what-a-retrospective-reports-as-read-and-unused.md)'s worker, and pasted as it
wrote it.*

> Node 129 named the only sound measurement of whether fed material is worth its bytes — *"the same node run twice,
> once with the file in the payload and once without, the two handovers compared"* — and recorded that this effort
> has the instrument and has never used it. It was offered to the human as an alternative on node 141 and they
> corrected the node's premise instead, so it is unanswered rather than declined. The question is whether a node run
> is spent on it, and on what: after node 143 lands, the spawn-fed standards payload is the first candidate, and
> `decisions.md` — kept read-whole at node 129 on the ground that *"it's small enough"* — is the second. This is the
> one thing on the graph that could convert a judgement into a measurement, and this map forbids ranking an
> unmeasured saving.

**Blockers, in the worker's words:** *"node 143, for the first candidate only; none for the node itself."*

## The manager's note at filing

*Not a change to anything above.*

**This was alternative C on node 141's question and the human never declined it** — they corrected the node's premise
instead, and the worker's re-rendered answer neither needs it nor rules it out. It is filed unanswered rather than
set aside.

## Interview

### Attempt 1

*The attempt's routing key does not survive the manager's session, so it is not recorded here.*

*Banked at hand-back, not yet relayed: this question queues behind [node 144](144-make-the-rules-file-stand-alone.md)'s
gate, which was live when it arrived.*

**The worker's question, pasted as it wrote it.**

> I have what I need. One decision hangs on facts I've now checked, and two of them reshape the node.
>
> NODE:          Measure whether a fed file earns its place by running one node twice
>
> ABOUT:         Node 129 named the only sound way to tell whether a file we push into every worker's context is worth its bytes — run the same node twice, once with the file and once without, and compare. We have never done it. This node asks whether we spend the run, and on which file. It is being decided now because your standing instruction ranks token-cost work above the rest of the frontier and, in the same breath, forbids ranking a saving nobody has measured — so this is the one node on the graph that could unblock that.
>
> SO FAR:        I read node 165's file, `map.md`, `decisions.md`, and nodes 129, 141, 143 and 60. Three findings, then a design.
>
> **(1) The node's first candidate no longer exists.** It was written expecting node 143 to *feed* the standards to the checker and implementer in their spawn. At 143's gate you amended exactly that away — *"the manager doesn't actually need to pass them anything. Basically we replace the discovery pass with reading that file."* So the standards are now a file the worker reads, not a payload. And nobody is proposing to delete it: it is the rule set the work is graded against. There is no live decision for a measurement to settle there. I treat that candidate as dead.
>
> **(2) The second candidate has a live, reversible decision behind it, and it is getting bigger.** `decisions.md` is fed to every worker on every node. You kept it fed at node 129 — *"leave decisions in read-whole - it's small enough"* — on a stated mechanism: *"LLMs will otherwise hardly proactively search for decisions, whereas if it's fed to context, the LLM's engine will take it into account naturally."* That is a claim with a testable consequence. It was 24,345 bytes when you called it small enough; it is **27,430 bytes today**, up 12.7%. Node 129 set a trigger to re-offer the cut when it stops being small enough, anchored at ~43,847 bytes — a number its worker flagged as its own, borrowed from where `map.md` was judged to need splitting, not yours. With 80 nodes still open at ~250 bytes a line, that projects to about **47,000 bytes**. The question comes back to you inside this effort whether or not we measure. Together `map.md` (31,058 B) and `decisions.md` (27,430 B) are ~14.6k tokens every worker pays uncached on every node.
>
> **(3) Node 129 called the instrument expensive, and I think it costed the wrong design.** It assumed a whole extra node run compared at the handover. Two things make it far cheaper. A grilling worker's contract already makes it *end its turn* on its first question — so the manager gets a complete, comparable artifact (`SO FAR`, `ASK`, `RECOMMENDED`, `ALTERNATIVES`) from a fraction of a run, and simply never resumes the second worker. And grilling is 80 of this graph's 170 nodes, against 8 research and precondition nodes ever — so comparing at the first question is the only version that runs on the kind we actually have. No new mechanism, and the shadow never reaches you.
>
> One thing I settled myself: a shadow spawned without the pointer might go and find `decisions.md` anyway, since node 129 landed an instruction to search the record. That is not contamination — it is the measurement. If it goes looking unprompted, your premise about LLMs and proactive search is wrong; if it does not, we see what the absence costs.
>
> ASK:           Do we spend it on package A — drop the first candidate as dead, and measure `decisions.md` by shadowing the next three grilling workers, compared at their first question — or one of the alternatives?
>
> Package A, in four parts:
>
> (i) The first candidate is closed with the reason recorded: 143's amendment turned the standards from a payload into a read, and no decision hangs on the number.
>
> (ii) On each of the next three grilling nodes the manager spawns, it also spawns a second worker on the same node with an identical spawn minus the `decisions.md` pointer. Both stop at their first question. The real worker's question is relayed to you as normal and the node proceeds untouched; the shadow is never resumed and never reaches you.
>
> (iii) The readout is fixed *before* the first pair runs, so it cannot be chosen to fit the result. A read-only agent is given both first questions and `decisions.md` and asked two things only: does the shadow contradict, or propose re-deciding, something the index records; and does its `SO FAR` show it missing a fact the index carries that the fed arm used. Everything else is reported as noise, not as a difference.
>
> (iv) What each outcome licenses is written down in advance, and the two are not symmetric. **Any divergence in any pair settles it: the file earns its place, and node 129's size trigger is retired as unnecessary.** **No divergence in three pairs licenses nothing on its own** — three nulls mean those three nodes did not need it, not that no node does — and its only use is as evidence beside the size trigger when that fires.
>
> RECOMMENDED:   Package A.
>
> What it buys is not one number. It is the protocol: after this, any argument about a file we push into every worker's context costs one shadow worker instead of another round of reasoning. This effort has cut `map.md` three times by argument and watched it grow back twice, and `map.md`'s own opening line already promises that whether its split falls in the right place is *"settled by measurement rather than argument"* — but the only instrument we built for that is node 60's report of what the map failed to say. We have a way to measure what a fed file **lacks** and none for what it **wastes**. This is that one.
>
> It is honest about its own weakness, which is why part (iv) is in the package rather than left to be argued after the fact. A null result at n=3 is weak evidence and I say so up front, because the failure mode here is running the measurement and then reading a null as permission — which is node 129's citation-count mistake wearing new clothes.
>
> And it costs a fraction of what node 129 assumed. Three shadow workers stopped at their first question, on nodes that were being run anyway, with nothing reaching you.
>
> ALTERNATIVES:  B — Package A plus the first candidate: also shadow a checker with and without the implementation-rules file. Set aside because you amended 143 into a read three commits ago and nobody proposes removing the rules the work is graded against, so the number would decide nothing.
>
> C — Node 129's own design as written: one node run twice, whole handovers compared. Set aside as strictly worse — a full extra run, and on a grilling node it puts two questions in front of you, which your one-question-at-a-time rule forbids.
>
> D — Refuse; spend nothing and let node 129's size trigger fire on bytes alone. Cheapest, and defensible. Set aside because the threshold is a worker's borrowed anchor flagged as not yours, and it will fire inside this effort — so you pay for the decision either way, just without evidence.
>
> E — Shadow `map.md` instead, the bigger file at 31,058 bytes. Set aside for now: nobody proposes dropping the map, so a whole-file arm answers a question nobody asked. The sharp version is a per-section arm, which is a larger design and wants this protocol to exist first.
>
> F — Park until `decisions.md` nears the trigger, then measure. Set aside because the shadows have to ride nodes as they run; waiting means waiting for the same opportunities that are in front of us now, with fewer left.

**The human's reply, `verbatim`.**

> 165 ok

**The option it takes**, quoted from the worker's own `ASK` and `RECOMMENDED` and attributed to the worker:

> **ASK:** Do we spend it on package A — drop the first candidate as dead, and measure `decisions.md` by shadowing the
> next three grilling workers, compared at their first question — or one of the alternatives?
>
> **RECOMMENDED:** Package A.

***The manager's note.*** **Not a divergence**: the reply assents to the `RECOMMENDED` rather than contradicting it,
and takes none of alternatives B through F. It names this node, which is what makes it attributable — node 50's
question was also outstanding when it arrived.

**Package A places a standing duty on the manager**, not on this node's worker: on each of the next three grilling
nodes it spawns, it also spawns a shadow worker with an identical spawn minus the `decisions.md` pointer, both
stopping at their first question; the shadow is never resumed and never reaches the human; and the readout is fixed
before the first pair runs. The manager records that it now owes this, and the worker's answer is what defines it.

## Answer

*Pasted as the worker wrote it.*

> **The run is spent, on the second candidate only, and it costs a fraction of a node run rather than one.** The first candidate is closed. `decisions.md` is measured by shadowing the next three grilling workers, compared at their first question.
>
> ### 1. The first candidate is closed, because node 143 landed the opposite of what this node assumed
>
> This node's `## Question` names *"the spawn-fed standards payload"* as the first candidate and blocks on node 143 to create it. **Node 143 landed as a read, not a payload.** The human's amendment at its gate, `verbatim`: *"the manager doesn't actually need to pass them anything. Basically we replace the discovery pass with reading that file."* There is no spawn-fed standards payload to measure.
>
> **It is dead a second time over, independently of that.** Nobody proposes removing `map-implementation-rules.md` from a checker or an implementer: it is the rule set their work is graded against, and the human chose the read route deliberately three commits ago. A measurement decides something only where a decision is live and reversible. This one is neither, so the number would buy nothing. See flag `165.1`.
>
> ### 2. `decisions.md` is the candidate with a live decision behind it
>
> It is fed to every worker on every node and is the one file whose removal is a single reversible switch already drafted — node 129's part (ii), reverted by the human on a stated mechanism, `verbatim`: *"the rationale for decisions being kept fed is that LLMs will otherwise hardly proactively search for decisions, whereas if it's fed to context, the LLM's engine will take it into account naturally - and it's small enough."* That is a claim with a testable consequence, which is what makes it measurable at all.
>
> **Its size has moved since that judgement.** 24,345 bytes when the human called it small enough; **27,430 bytes** at this node, up 12.7%. Node 129's trigger to re-offer the cut is anchored at ~43,847 bytes — a number its worker flagged at `129.4` as its own rather than the human's, borrowed from where `map.md` was judged to need splitting. Node 129 projected ~42,000 from 70 open nodes; there are now **80 open**, which at ~250 bytes a line projects to about **47,000**. **The decision returns to the human inside this effort whether or not it is measured**, which is what makes measuring it now worth the spend rather than a luxury.
>
> ### 3. The instrument, and why it is not what node 129 costed
>
> Node 129 defined it as a whole extra node run with the two handovers compared, and called it expensive. **Two things make it cheap.**
>
> **The comparison point moves earlier.** A grilling worker's contract already makes it end its turn on its first question, so the manager receives a complete, comparable artifact — `SO FAR`, `ASK`, `RECOMMENDED`, `ALTERNATIVES` — without the run finishing. The shadow is simply never resumed.
>
> **That is also the only version that runs on the kind this graph has.** Of 170 nodes, **80 are grilling** against **8 research and precondition nodes ever**. Comparing whole handovers cannot use grilling without putting two questions in front of the human, which the one-question rule forbids. Comparing first questions never reaches the human at all.
>
> ### 4. The four parts, as the human took them
>
> **(i) The first candidate is closed** with section 1's reason recorded.
>
> **(ii) The next three grilling nodes are shadowed.** On each, the manager spawns a second worker on the same node with an identical spawn minus the `decisions.md` pointer. Both stop at their first question. The real worker's question is relayed and the node proceeds untouched; the shadow is never resumed.
>
> **Two properties of (ii) are load-bearing rather than incidental.** It is the **next** three and not three the manager chooses, because a chosen subject makes the result a selection. And **the shadow's output is evidence only and never steers the real node** — taking the better of two questions would make the comparison a choice rather than a measurement.
>
> **(iii) The readout is fixed before the first pair runs**, so it cannot be chosen to fit what comes back. A read-only agent is given both first questions and `decisions.md`, and asked two things only: does the shadow contradict, or propose re-deciding, something the index records; and does its `SO FAR` show it missing a fact the index carries that the fed arm used. Anything else is reported as noise rather than as a difference.
>
> **(iv) What each outcome licenses is written down in advance, and the two are not symmetric.** **Any divergence in any pair settles it**: the file earns its place, and node 129's size trigger is retired as unnecessary. **No divergence in three pairs licenses nothing on its own** — three nulls mean those three nodes did not need it, not that no node does — and its only use is as evidence beside the size trigger when that fires. This asymmetry is in the package rather than left to be argued afterwards because reading a null as permission is node 129's citation-count error wearing new clothes.
>
> **Parts (ii), (iii) and (iv) are standing duties on the manager**, recorded as such at the human's answer.
>
> ### 5. What the shadow does if it goes and reads the file anyway
>
> Node 129 landed an instruction telling every worker to search the record, so a shadow spawned without the pointer may find `decisions.md` unaided. **That is not contamination; it is the measurement.** If it goes looking unprompted, the human's premise about proactive search is wrong. If it does not, the absence is clean and its cost is what the readout sees.
>
> ### 6. What is actually bought
>
> Not one number. **The protocol.** After this, any argument about a file pushed into every worker's context costs one shadow worker instead of another round of reasoning. This effort has cut `map.md` three times by argument and watched it grow back twice, and `map.md`'s own first line already promises that whether its split falls in the right place is *"settled by measurement rather than argument"* — yet the only instrument built for that is node 60's report of what the map failed to say. **There was a way to measure what a fed file lacks and none for what it wastes.** This is that one.

**What the worker reported its work invalidates, pasted as it wrote it.**

> **1. Node 141's answer, section 5 — its factual premise is falsified by node 143's landed form.** It reads: *"node 143 moves the standards and the bar's commands out of a file the worker reads and into what its **spawn** names. Node 60 is about a *file*; the re-rendered question is about a *payload*."* And it builds on that: *"Node 143 makes this question more load-bearing, not less…"*
>
> **Node 143 landed the reverse.** The human's gate amendment removed the payload entirely — *"the manager doesn't actually need to pass them anything"* — and the standards became a file the worker reads. So the two objects node 141 separates have **converged** rather than diverged: the standards are now exactly node 60's kind of object. Node 141's conclusion may well survive on other ground, but the ground it states is gone. Node 141 is resolved and nothing marks this.
>
> **2. Node 129's answer, section 3a — its costing of the instrument, and its definition of it, are both narrowed by this node.** It reads: *"the same node run twice, once with the file in the payload and once without, the two handovers compared… That is the honest answer, and it is expensive."* This node establishes that the comparison point can be the worker's **first question** rather than its handover, at a fraction of the cost and without the human being touched, and that the handover version cannot be run on grilling nodes at all without breaching the one-question rule. Node 129's core claim — that the measurement is necessarily external and comparative — stands untouched.
>
> **3. This node's own `## Question`, for the record.** It names *"the spawn-fed standards payload"* as the first candidate. No such payload exists. The premise was written before node 143's gate and was never revisited when 143 landed.
>
> **No collision with nodes 163 or 167.** Both concern what a checker reads and where the bar's commands come from; this node touches `map-implementation-rules.md` only to say that measuring whether a checker needs it decides nothing. I cannot judge node 144, whose subject I was not told.

## Flags

*All five are the worker's own text, pasted. The ids and the links are the manager's bookkeeping and nothing else.*

`165.1` `ASSUMPTION` — **I closed the first candidate on the ground that no decision hangs on it, and nobody has checked that.** Node 143's amendment establishes that the standards are read rather than fed, which is a fact. What is mine is the second half: that no one would propose removing `map-implementation-rules.md` from a checker or an implementer, it being the rule set their work is graded against. Alternative B offered measuring it anyway and the human set it aside with the rest, so they saw the option — but they were shown my framing of it and not an argument for keeping the candidate alive.

`165.2` `ASSUMPTION` — **The sample is three pairs and the number is mine.** There is no power calculation available here and I did not pretend to one. Three rests on two things only: the marginal cost of a pair is a fraction of a run, so more than one is affordable; and a single pair could not distinguish a real effect from run-to-run variance in a nondeterministic sampler. Three is small enough that a null result is weak, which part (iv) states rather than hides.

`165.3` `ASSUMPTION` — **I chose the two questions the readout asks, and that choice bounds what the measurement can find.** Contradicting the index and missing a fact the index carries are the two consequences the human's stated mechanism predicts, so they are the testable form of their own claim. But a file fed to context can act in ways neither question sees — steering tone, framing, or what a worker treats as in scope — and those will be reported as noise.

`165.4` `ASSUMPTION` — **Comparing at the first question rather than at the handover is a departure from node 129's stated instrument, and it has a blind spot I am stating rather than burying.** A file whose effect appears only late in a node — during a correction round, or while writing the handover — is invisible to this comparison. I took it because it is the only version that runs on grilling nodes, which are 80 of this graph's 170, and because it never reaches the human.

`165.5` `ASSUMPTION` — **I wrote two constraints into part (ii) that the human's package did not spell out**: that it is the *next* three grilling nodes rather than three the manager picks, and that the shadow's output never steers the real node. Both were in my `SO FAR` rather than in the numbered parts they assented to. Without the first, the manager can select subjects and the result becomes a choice; without the second, taking the better of two questions turns the measurement into a selection too.

## Retrospective

*Pasted as the worker wrote it. Filed by the manager as an annotation.*

**(1) What I had to hunt for.**

**That node 143's landed form had destroyed my node's first candidate.** This was the fact that reshaped the node, and finding it was the largest single cost. My spawn told me 143 *"has resolved and landed as commit 7b5bcf0"* and that my blocker *"is discharged"* — framing 143 as having **created** the thing I was to measure. I looked first at `decisions.md`'s line for 143, which reads *"…nothing is passed to either"* — the fact **is** in the index line, I read it, and it did not register against my node's phrase *"the spawn-fed standards payload"*. I found it by reading node 143 whole and reaching `### Gate — correct` about 250 lines into a 415-line file.

**The node kind distribution** — 80 grilling of 170 nodes, 8 research and precondition ever — which carries my argument that the comparison must happen at the first question. Nothing records it. I computed it with a shell loop over `nodes/*.md`.

**Current file sizes.** `decisions.md` at 27,430 bytes against node 129's recorded 24,345. Nothing records the growth; I ran `wc -c`.

**(2) What arrived that this node did not need.**

**From the spawn:** the note that nodes 163 and 167 are running gave one clause on each subject and asked me to say whether my answer collides. To write that line I had to guess their subjects from their names. Either the note carries enough to judge collision or it does not ask for the judgement. And the report that two workers named the read-whole-a-file cost bore on nothing I decided.

**From the mandatory reads:** `map.md` is 31,058 bytes and I acted on four of its items — the token-priority rule, the never-delete rule, the retrospective item, and the first line's promise that the split is settled by measurement. Roughly twenty-five others bore on nothing here.

**`decisions.md` I read whole and cited four of about ninety lines — and I am refusing to report that as waste, which is the whole point of this node.** Reading it whole is what stopped me proposing an instrument nodes 128 and 129 had already refused, and what told me node 150 had been reissued. I would answer *"I used 4 of 90"* and that answer would be worthless. **I am an unwitting data point for the thing this node just voted to measure**, and the shadow exists precisely because my self-report here cannot be trusted.

**Where I went for one fact and took the whole file:** node 143, ~19 KB, opened for one fact — what its landed form did to the payload. I got four flags, two checker runs, a numbering-collision note and a postmortem on a failing `git rebase`. The file **is** navigable by heading, per the map's own writing rule 3; a pointer in my node file to `### Gate — correct` would have replaced the read. I also read node 125 whole on the strength of its name suggesting a prior use of a baseline re-run; it bore on nothing.

**The arrangement that would have avoided the last one: there is no index of open nodes.** `decisions.md` indexes the 86 resolved; the 80 open are discoverable only by filename. Any worker wanting to know what an open node is about — to judge a collision, to check whether its finding is already minted — pays a whole file read per candidate or guesses from a filename.

**(3) What would have made this node easier.**

**In the node file:** my `## Question` asserts a premise that node 143 falsified before I was spawned, and nothing marked it. A stale premise in a `## Question` is expensive in a specific way — the worker cannot tell it is stale without doing the reading that the premise made look unnecessary.

**In the spawn:** the manager's note said the blocker *"is discharged"*, which is true and misleading in one sentence. The manager wrote node 143's gate section itself, so it held the fact. One clause — *"and note 143 landed as a read, not a payload, so your first candidate may not exist"* — would have replaced my entire reconstruction. This is close to flag `143.5`'s finding on that same node: what the manager states about a node's context arrives at the worker as settled, and the worker pays to disprove it.

**In the record:** nothing measures the record about itself — file sizes over time, node counts, the kind mix. The map's token-priority rule ranks work by measured saving, and every number that ranking needs has to be re-derived by hand. Node 141 §3 records this reported three times already, by nodes 136, 138 and 139. **This is the fourth.**

**(4) What was stale, wrong, or contradictory.**

Node 141 §5 and node 129 §3a, both reported on `INVALIDATIONS` above, and my own node's `## Question`.

**Node 129 §6's projection is stale rather than wrong**: it computed *"near 42,000"* from 70 open nodes. There are 80 open now, so the same arithmetic gives ~47,000.

**One small inconsistency between my contract and my spawn**, which the record already resolves: `expedition-grilling/SKILL.md` says the handover has *"Five parts, every time"*, while the spawn and `map.md` require six on this effort. The contract file carries no note that an effort may add a part, so a worker working from the file alone would drop the retrospective. The spawn covered it, so it cost me nothing.
