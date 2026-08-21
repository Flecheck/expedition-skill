# Whether a spawn may override a shipped worker contract

Type: grilling
Status: resolved

## Question

~~May a spawn suspend a clause of the contract it names, and if so under what conditions?~~

**Widened, after four instances rather than one:** may a spawn **depart** from the contract it names — by
suspending a clause, by **adding** to the job the contract closes, or by **substituting** text the contract
says must travel unaltered — and if so under what conditions? The original wording asked only about
suspension, which turns out to be one shape of three and the only one that had been seen when this node was
written.

~~It has already happened once.~~ **It has happened four times, against two contracts.** The first is
below; the other three all ran during [Carry the recorded deltas into the shipped skill
files](26-carry-deltas-into-shipped-files.md) and are under *Three more, and not one of them a suspension*.
[Whether flags.md survives the settle-at-close
practice](27-does-flags-file-survive.md)'s spawn suspended one rule of
[`expedition-grilling/SKILL.md`](../../../.claude/skills/expedition-grilling/SKILL.md) — *"`flags.md` is
not yours. Leave it unread."* — on the ground that the node was about that file. The override was
well-grounded, it was stated plainly in the spawn, and the node could not have been worked without it.
Nothing in the design permits it.

Reported by that node's own worker, which was told the override had happened and put it on the record
rather than deciding it.

### Three more, and not one of them a suspension

All three ran against
[`expedition-checker/SKILL.md`](../../../.claude/skills/expedition-checker/SKILL.md) during [Carry the
recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md), and each is recorded
on that node. Every one of them worked. That is the difficulty rather than the reassurance.

**1. An addition — the flag validity pass.** The checker's contract fixes what it is given in four numbered
items and then closes the list: *"That is everything."* The spawn gave it a fifth — five of the node's
flags, stripped to what was done with the reason deliberately withheld, and the instruction to judge only
whether each is **true of the work**. It was declared in the spawn as a fifth thing beyond the four rather
than slipped past it, and run **after** the outcome had already been given, so nothing it concluded could
reach the verdict. All five came back true, in 51 seconds and one tool call.

**The human instructed it**, at that node's gate: *"could we give a summarized version of the flags, with
explict instruction to check if they are valid."* So one of the four is not the manager taking a liberty at
all — it is the human directing a worker through the only channel they have, which is the manager's spawn.
Whatever this node decides has to leave that possible, or say where it goes instead. [Whether a flag is
checked before the human settles it](30-checking-a-flag-before-the-human.md) holds the mechanism and says
in as many words that it cannot be delivered until this node answers.

**2. A substitution — the dereferenced acceptance condition.** The same contract fixes what the manager
must hand over: the acceptance condition *"as text. The words themselves, not somewhere to go and read
them"* — and separately forbids the checker to rewrite it. Condition 1 of that node **pointed into the
record**, at a paragraph of [map.md](../map.md), which a blind checker may not follow. Satisfying the
contract therefore required the manager to author: it pasted the paragraph in and **stripped a bookkeeping
preamble asserting the work had already been done**, which would otherwise have told a blind checker the
answer. Flag `26.4` records it.

This is not a liberty either — the contract's own clause forced it — and it is the shape the node's
original framing misses completely, because nothing was suspended and nothing was added. **Text the design
says travels unaltered was rewritten, by the party the design calls a scribe.**

**3. A case the contract has no clause for — the condition that moved mid-check.** The checker's *"When you
are handed the same work again"* section is written for a changed **work** against a fixed condition, and
the whole design says a condition is written before work starts and is not the worker's to rewrite. On that
node the acceptance condition was **amended twice while the check was live**, and the manager said so in
the resume. Nothing in the contract covers it; the checker handled it correctly with no instruction.

**And this one is not a spawn at all — it is a resume.** The node's framing reaches only the first message
to a worker, where the same channel is used repeatedly and every later use has the same power.

### What the four share, and where they diverge

All four were well-grounded, all four were stated plainly rather than implied, and in none of them could
the node have been worked otherwise. **None widened what a worker may write** — a candidate rule already in
the list below, now with four instances behind it instead of one.

What breaks the original framing is that only one of the four is a suspension. One **adds** to a closed
list, one **substitutes** for text the design says travels unaltered, and one arrives on a **resume**. An
answer that permits or forbids *suspension* decides one case in four.

### Why it is not obviously fine

[Write the worker contract skills](22-worker-contract-skills.md) fixed the opposite direction: a spawn
**names the contract's path** and **the file on disk wins**, because the harness serves the skill body it
loaded and a contract edited mid-session does not reach a worker spawned afterwards. An override inverts
that — the spawn now beats the file for one clause.

It also costs a property [map.md](../map.md)'s `## Notes` bought deliberately as v1's insurance for v2: a
worker contract that **stands alone as a file** rather than depending on skill invocation, so that a
non-Claude harness can be handed the same contract. If a spawn may suspend a clause, a worker's behaviour
is no longer readable from its contract alone, and the insurance is worth less than it looks.

### What the answer has to decide

- Whether a spawn may override at all, or whether the correct move was something else — a different
  contract, a wider clause, or an exception written into the contract itself so that no override is needed.
- If it may: what must hold. Candidates, none of them decided — the override is **stated in the spawn**
  rather than implied; it **names the clause** it suspends; it is **recorded on the node** so a later
  reader can see the worker was not running the shipped contract; and it may **never widen what the worker
  may write**, since the write rules are what keep the manager the graph's only writer.
- Whether the specific clause that was overridden should instead be narrowed in the contract. *"`flags.md`
  is not yours"* exists to keep a worker's read small, and a node **about** that file is a case the clause
  did not consider.

**Four more, added with the three instances above:**

- **Whether a resume is governed by whatever rule governs a spawn.** Every departure after the first
  arrives on a resume, and a resume is not covered by a word about spawns. If they differ, say how; if they
  do not, the rule has to be written over *what the manager sends a worker* rather than over the spawn.
- **Where the human's own instruction lands when it arrives mid-node.** They have exactly one channel — the
  manager — and they used it to extend a worker's job. Either a spawn may carry that, or the instruction
  waits for a contract edit and the human is told their instruction cannot take effect until then.
- **Whether a substitution is the same thing as an override at all.** Nothing was suspended when the
  acceptance condition was dereferenced; the contract *required* the manager to hand over text that could
  not be handed over as it stood. That may be a defect in the contract, a licence the scribe rule needs, or
  a third procedure — but it is not covered by permitting or forbidding an override.
- **Whether a contract may close a list.** *"That is everything"* is what the flag validity pass
  contradicted, and a contract that never closed a list would have had nothing to contradict. Whether the
  absolutism is load-bearing — it is what makes a blind checker's remit legible — or is the actual defect.

Feeds the **manager's own skill**, which is where any rule about spawns would live, and which is the last
product file to be written. Two open nodes wait on the answer for their delivery route rather than their
content: [Whether a flag is checked before the human settles
it](30-checking-a-flag-before-the-human.md) and [What the checker contract owes to having been
run](31-checker-contract-owes.md), both of which would otherwise land as contract edits.

## Answer

**A spawn may not depart from the contract it names on the manager's authority. Where a clause blocks the node in front of it, the manager raises; the human's answer licenses that one attempt and the repair becomes a node.** The human's words on the recommendation carrying that rule: *"ok for recommendation"*.

### The line that actually divides the four instances

Not suspension-versus-addition, and not spawn-versus-file. It is **a slot the contract opens** against **a clause the contract states**.

All six contracts already hand the spawn binding content by design — *"the sections the spawn names"*, *"the sources the spawn names"*, *"the paths the spawn expects you to touch"*, *"what the spawn says must be true when you are done"*, the acceptance condition as text, the record of an earlier attempt. A spawn filling one of those is not an override and never was: the file states the rules, the spawn states the parameters, and that is exactly the division that keeps [Write the worker contract skills](22-worker-contract-skills.md)'s condition 9 — *each contract stands alone as a file* — worth what [map.md](../map.md) bought it for.

Everything else falls into three routes and nothing else:

1. **A slot.** Fill it. There is nothing to permit and nothing to record.
2. **The human's own direction.** They have one channel and it is the manager. The spawn may carry it, marked as their words rather than as the manager's, and it is recorded as a flag on the node. Where the direction should bind later workers it becomes a contract edit — which is [Off-contract subagent output](17-off-contract-output.md)'s existing sentence, unchanged: *"amending the contract is an implementation node against that skill file, never something the manager does mid-flight."*
3. **Everything else is a defect in the contract**, and it is fixed in the contract.

### The manager's raise, which is the only new mechanism here

Route 3 has a hole that only shows up when the defect is found **while a node is being worked**: the repair is an implementation node and a gate, and the node in front of the manager cannot wait for it. So the manager raises, and the answer produces **two** outputs, always both:

- **a licence for that one attempt**, recorded as a flag on the node, so a later reader can see the worker was not running the shipped contract;
- **a node for the permanent fix**, so the repair is not lost.

A licence is not an amendment — nothing on disk changes — so [Off-contract subagent output](17-off-contract-output.md)'s prohibition stands untouched.

**The two outputs are not alternatives, and the record says why.** [Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md)'s spawn suspended *"`flags.md` is not yours. Leave it unread"*; the departure was well-grounded and the node could not have been worked otherwise; and a session later **no node was ever minted, the clause is still on disk in five contracts unchanged, and this node was still carrying the narrowing as an open question.** Leaving it to the manager's judgement lost the repair as well as the record.

**The channel needs no new word.** [`CONTEXT.md`](../../../CONTEXT.md)'s *Raise* is now *"an agent putting something to the human"*, general over agents since [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md) widened it, and five flags in this graph are the manager's own judgements. Its `_Avoid_` clause refuses `ask` on the human's own ground — *"ask is when a worker is designed to ask question to the user, raise is when the worker is supposed to work mostly by itself but it needs input from the user"* — which is the manager's position exactly. So this is a **blocking raise by the manager on its own behalf**, and all this node adds is that the manager may make one. Nothing had described that channel: everything the manager says to the human today is a relay, a gate, or a flag settlement.

**One floor over all three routes.** Nothing the manager sends a worker may **widen what that worker writes**. The write rules are what keep the manager the graph's only writer, and none of the four instances touched them. A direction that would widen them is a contract edit, never a licence.

**Written over anything the manager sends a worker, not over the spawn.** Three of the four departures arrived on a **resume**, and a rule about first messages is avoided by waiting for the second.

### What each of the four instances is under this answer

| instance | what it is | what it gets |
| --- | --- | --- |
| `flags.md` suspended on node 27 | a real departure, and a **contract defect** | a licence at the time, and a node — the node that was never minted |
| the flag validity pass on node 26 | **the human's direction**, route 2 | lawful as it happened; a contract edit if kept, which is node 30's route |
| the dereferenced acceptance condition | **not an override at all** — the manager complying with *"as text… not somewhere to go and read them"* | the defect is upstream: a condition that points into the record |
| the condition that moved mid-check | **not a departure** — an uncovered case | a clause the checker's contract does not have |

**Two of the four were never overrides**, which is why an answer that permits or forbids *override* decides half the cases at best. The dereferenced condition is the manager obeying a clause whose input was malformed: the defect is that an acceptance condition was written pointing into the record at all, which [Write the worker contract skills](22-worker-contract-skills.md) already found (*"a path in one is a hole in the blindfold"*) and flag `26.4` already recorded, and which nothing owns. The moved condition is a gap in *"When you are handed the same work again"*, which is written for changed **work** against a fixed condition.

### One reading in this node's own framing that does not hold

*"[Write the worker contract skills](22-worker-contract-skills.md) fixed the opposite direction… the spawn now beats the file for one clause"* reads too much into that node. **The file on disk wins** was found and written about the **harness serving a stale skill body** — a contract edited mid-session does not reach a worker spawned afterwards — so it settles a conflict between two copies of the same file, not between the spawn and the contract. An override does not invert it; it lands in a space nothing had ruled on. Confirmed across all six contracts and `graph-conventions.md`: **no shipped file states any precedence between a spawn and a contract, or says what a worker does when its spawn contradicts it.** The manager writes that precedence into spawns by hand today, which is practice and not design.

### Whether a contract may close a list

Yes, and *"That is everything"* is not the defect — it is **mis-grounded**. The sentence immediately under it is what it protects: *"There is a record behind this work… You do not read it, and you do not go looking for it."* So the closure is the blindfold, not an arbitrary absolutism, and it is load-bearing exactly there. What the flag validity pass contradicted was its **letter** while respecting the thing it protects — the flags reached it stripped of the reason, as claims about the work rather than as record. The repair is to state the closure as what it guards rather than to remove it, which is one clause in the file where node 30's answer lands.

### If the raise ever fires often, it is not reporting anything about the node

Two of thirty-one nodes have needed one, which is cheap and worth the frontier growth of a node per firing. A rate materially above that is a diagnostic and it points at the contracts rather than at the node in front of the manager — the same shape as six correction rounds at one gate pointing at the checker's under-specified row rather than at a node that was too coarse.

### What this leaves elsewhere

- **Node 30's delivery route is decided**: the flag validity pass was lawful as the human's direction and, being a standing practice rather than a one-off, it lands **in** `expedition-checker/SKILL.md` as a contract edit. It is not blocked on any further permission.
- **Node 31's is the same**, and it gains an uncovered case its acceptance condition does not name: **the acceptance condition that moved while the check was live**. Node 31 is unstarted, so this is an in-place addition rather than a new node — and the case is real, handled correctly with no instruction, and invisible to the next checker, which is that node's own criterion.
- **The manager's own skill** inherits the raise, its two outputs, the floor on write rules, and the rule that a carried direction is marked as the human's words rather than as the manager's.
- **[Subagent context contract](12-subagent-context-contract.md)'s spawn shape gains an element it does not list** — a carried direction, distinct from `<per-type additions>` and from a manager note capped to context the manager already holds.

### Narrowed by [Workflow self-improvement during use](19-workflow-self-improvement.md)

Reported as an `INVALIDATIONS` entry by that node's worker, in its words:

> its rule of **two outputs, always both** (a licence for the attempt, and a node for the permanent fix) is
> written unconditionally. It cannot hold on an effort whose repository does not own the thing being fixed,
> because the second output is impossible there. Narrowed rather than overturned: on such an effort the
> `FRICTION` flag takes the node's place, so the licence still has something behind it, which is what that
> node's evidence was actually about.

## Flags

`28.1` **· settled** `ASSUMPTION` — the **three-route triage** is this worker's, not the human's. They took the Q2 recommendation, whose opening clause — *the manager may not depart on its own authority* — is theirs by assent to the option as written. The triage itself was Q1's recommendation and was never picked; it is presupposed by what they took rather than chosen, and it is recorded here as a worker's judgement.

`28.2` **· settled** `ASSUMPTION` — the rule is written over **anything the manager sends a worker**, spawn or resume, decided alone on the ground that three of four departures arrived on a resume and a rule about first messages is avoided by waiting for the second. Not put to the human.

`28.3` **· settled** `ASSUMPTION` — the **closed list is load-bearing and mis-grounded**, settled from the file rather than asked: the closure sits directly above the blindfold clause it protects. The human was not asked whether the absolutism should go, and the repair proposed is a re-grounding rather than a removal.

`28.4` **· settled** `ASSUMPTION` — the **substitution case was ruled not an override at all** and its defect placed upstream, in how an acceptance condition is written. Decided alone. The human was asked nothing about it, and it is the shape this node's original framing missed entirely.

`28.5` **· settled** `ASSUMPTION` — the manager's own question is a **`raise`** under the glossary's generalised sense, checked against `CONTEXT.md`'s entry and its `_Avoid_` clause rather than taken from the manager's note that proposed it. This names a channel nothing in the design had described, on a reading of an existing term rather than on a decision.

`28.6` **· settled** `ASSUMPTION` — **the diagnostic clause about the raise's firing rate came from a manager note**, put to the human alongside the recommendation and not covered by their assent to it. Adopted into this node's permanent text on the worker's judgement because it is true of the record and useful to whoever writes the manager's skill. **Fourth consecutive node on which a manager note has reached a node's text**, after `17.4`, `25.4`, `27.3` and `26.4`; filed here so the manager does not have to find it.

**Manager note on `28.6`, beside the worker's text rather than in it.** The count is off by one in the worker's favour: the four ids it lists are on **four** nodes — 17, 25, 27 and 26 — so this is the **fifth** consecutive node, not the fourth. The substance is untouched. What matters more than the count is that **this is the first time the worker filed the flag rather than the manager catching it.** [Off-contract subagent output](17-off-contract-output.md)'s check exists because the manager kept finding its own notes in a node's permanent text after the fact; on this node the manager ran that check and found the flag already written. The check found nothing because the worker had already done its job.

## Interview

### Attempt 1 — routing key `graph-workflow/28/a1`

**Q1** — May the manager depart from a shipped contract **on its own authority**, or is a departure lawful
only when it carries the human's own direction, with everything else being either a slot the contract
already leaves to the spawn or a defect to be fixed in the contract?

The worker recommended **no manager-authority departure**: three routes and nothing else — a slot the
contract already opens, which needs no permission; the human's direction, which the spawn may carry, marked
as their words and flagged on the node, becoming a contract edit if it should bind later workers; and
everything else a defect, fixed in the contract. One floor over all three: **nothing the manager sends may
widen what a worker writes**, since the write rules are what keep the manager the graph's only writer, and
none of the four instances did. Rested on the stand-alone-file insurance [map.md](../map.md) bought for v2
and [Write the worker contract skills](22-worker-contract-skills.md) made an acceptance condition, which
survives only if the file states the rules and the spawn states parameters; on [Subagent context
contract](12-subagent-context-contract.md) already capping a manager's addition to *"context the manager
already holds"*; and on both real departures being better served elsewhere.

Three findings under it, each correcting this node rather than answering it.

**The rule this node leaned on does not reach the question.** Node 28's own text cited [Write the worker
contract skills](22-worker-contract-skills.md)'s *"the spawn names the contract's path and the file on disk
wins"* as fixing the opposite direction. That sentence is about the **harness serving a stale skill body** —
a contract edited mid-session does not reach a worker spawned afterwards — so it settles a conflict between
two copies of one file, not between the spawn and the contract. **No contract and no line of
`graph-conventions.md` states any precedence between spawn and contract at all**, or says what a worker does
when its spawn contradicts it. The worker observed that the manager writes that precedence into spawns by
hand, including the spawn that produced this observation.

**Only two of the manager's four instances are departures.** All six contracts already open slots for the
spawn to fill — *"the sections the spawn names"*, *"the sources the spawn names"*, *"the paths the spawn
expects you to touch"*, *"what the spawn says must be true when you are done"* — so a spawn has always
carried binding content lawfully, and the line is between **filling a slot the contract opened** and
**changing a clause it states**. The dereferenced acceptance condition is the manager **complying** with the
checker's own clause, exposing a defect one level up — a condition that points into the record, which node
22 already named (*"a path in one is a hole in the blindfold"*) and flag `26.4` already records. The
condition that moved mid-check is an **uncovered case**, the re-check section having no clause for it. That
leaves the `flags.md` suspension and the flag validity pass — and the second was the human's own
instruction.

**One sentence of [Off-contract subagent output](17-off-contract-output.md) already reaches this node**,
decided for the worker's side of the same seam: *"Where the human wants a departure kept, amending the
contract is an implementation node against that skill file, never something the manager does mid-flight."*

Settled on the worker's own authority and returning as an `ASSUMPTION`: whatever rule is picked is written
over **anything the manager sends a worker**, spawn or resume, since three of the four departures arrived on
a resume and a rule about first messages is avoided by waiting for the second.

**A1** — `verbatim`

> We could have the manager ask the human ? What do you think ?

A proposal rather than a choice among the options offered, and addressed to the manager rather than to the
worker. Recorded here because it is the human's own words on the node's question, and relayed onward with
the manager's answer to it below.

**The manager's position, put to the human and not to the worker:** the ask is not a fourth option but the
missing move inside the worker's own route 2 — the rule says a departure is lawful when it carries the
human's direction and never says how the manager **obtains** that direction when the need arises mid-node.
It closes a hole: as the rule stands, anything that is not a slot is a defect fixed in the contract, and
fixing a contract is an implementation node, so the node stalls. Node 26 could not have afforded that
mid-check. And it is the only route that **guarantees the record** — the strongest fact against
leave-it-to-judgement is not that the four departures were wrong but that **nothing on any node records that
the worker was not running the shipped contract**.

Against it, and the manager raised this itself: **on the four instances the residual is empty.** Every one
resolves without a question — the `flags.md` suspension as a **carve-out in the contract**, the flag pass as
**the human's direction**, the dereferenced condition and the moved condition as **contract defects**. So the
route may never fire, and the map's standing preference is short prose over machinery for predicted needs.
Hence one sentence rather than a procedure. Two things it should keep apart, with different outputs:
**asking for a licence** produces a flag and possibly a contract edit; **reporting a defect** produces a
node — and three of the four instances were the second.

One thing the proposal exposes: **the manager asking on its own behalf has no name and no described
channel.** Everything the manager says to the human today is a relay, a gate, or flag settlement. [What is
recorded when the human takes an option as offered](25-recording-an-option-taken.md)'s residual — *"the
manager records the reply and asks which"* — is the only other instance and is written as a one-off. If this
route goes in, that is twice, and `CONTEXT.md`'s generalised `raise` — *an agent putting something to the
human* — already covers it without a new word.

**A1, continued** — `verbatim`

> ok

Recorded and **put again** rather than acted on, per [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md)'s residual case, settled as flag `25.3` in the human's own words:
*"If an anwser is not clear, yes ask again"*. The manager had closed by offering two framings for what goes
back to the worker — *add the ask to route 2* as decided, or leave it open for the worker to place — and
recommended neither, so `ok` does not name which. It is also readable as assent to sending the proposal at
all, which is not in doubt.

**Second live instance of that residual case**, three nodes after it was decided. The first, on [Whether
flags.md survives the settle-at-close practice](27-does-flags-file-survive.md), arose because the manager had
recommended **against** a flag it was relaying. This one has a different cause and it is the manager's own:
**the manager offered a binary and attached no recommendation to it**, so a bare assent had nothing to attach
to. The first instance was ambiguity between the manager's position and the worker's; this one is ambiguity
the manager manufactured.

The question was put again with a recommendation attached — **leave it open for the worker to place**, on the
ground that the worker had already corrected the manager's framing twice on this node and had read all six
contracts where the manager had read two, so the empty-residual judgement was better made by it. The
alternative offered was *add the ask to route 2 as decided*.

**A1, put again** — `verbatim`

> you can leave it open and give it

Takes the recommended option, quoted above and **written by the manager**. The proposal goes to the worker
open — to place, to site elsewhere, or to refuse as not yet worth its sentence — rather than as a decision it
must integrate.

The relay carried the human's proposal verbatim, the manager's argument for it (the hole in route 2, and the
record guarantee), the manager's argument against it (the empty residual), the licence-versus-defect
distinction, and the observation that the manager asking on its own behalf has no name. It stated in as many
words that none of it is decided.

**Q2** — Does the ask **serve** the rule — fired only when a contract defect stands in the way of a node
already being worked, and producing **two** outputs, a licence for that one attempt and a node for the
permanent fix — or does it **replace** the triage, so that any departure at all is settled by asking the
human at the time?

The worker recommended **serves it, one sentence, two outputs**: the manager may not depart on its own
authority; where a contract clause blocks the node in front of it, it raises; the human's answer licenses
that one attempt, recorded as a flag on the node so a later reader can see the worker was not running the
shipped contract, while the repair becomes a node against the skill file. Both outputs, always — the licence
is what carries the node past a defect [Off-contract subagent output](17-off-contract-output.md) forbids
fixing mid-flight, and the node is what stops the repair being lost. It costs no procedure and no new word.

Four things under it, and the second is the strongest finding on this node.

**It tested the manager's reading of the human's proposal rather than inheriting it, and took it only half
way.** *"We could have the manager ask the human"* is coherent only if the manager has no unilateral
authority to depart — otherwise there is nothing to ask about — so both readings presuppose the spine the
worker recommended at Q1. What it does not settle is whether the ask **serves** that rule or **replaces** it:
*"whenever the manager wants to depart, it asks at the time"* is a genuinely simpler design than three
routes, and the human's sentence fits it too. **The worker declined to record the spine as decided by the
human**, on the ground that they had not picked.

**The manager's argument against the ask does not survive the record.** The manager had claimed the residual
is empty — run the four instances through the three routes and none needs a question. **True of the permanent
fix and false of the node in front of the manager.** Route 3 sends a defect to the contract, and node 17
fixes what that means: *"an implementation node against that skill file, never something the manager does
mid-flight."* So a defect found **while a node is being worked** either stalls that node behind a whole
implementation node and its gate, or is worked around off-record. [Whether flags.md survives the
settle-at-close practice](27-does-flags-file-survive.md) is the case: it was ordered ahead of [Carry the
recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md), which blocked on it,
and the `flags.md` clause stood in its way. The departure happened, no node was ever minted, and **the
carve-out is still unwritten on disk a session later** — `expedition-grilling/SKILL.md:41` still reads
*"`flags.md` is not yours. Leave it unread"*, and this node was still carrying the narrowing as an open
decision point. Manager-confirmed on both halves. **Leaving it unwritten lost the permanent fix as well as
the record.**

**The record test, run on all four instances.** Three are on the record — `26.4` and `26.7` because the
manager filed flags about its own conduct, and the flag validity pass because the human's own words were in
the chat. **The one not recorded on its own node is the only real suspension.** And under an ask rule at
least two of the four fire rather than none: `26.4` and `26.7` are both *defect reports written after the
fact*, and for the dereferenced condition, asking at the time would have been better than recording
afterwards, because the manager authored text into a **blind** checker's payload on its own judgement.

**The channel exists and needs no new word**, checked against the glossary rather than taken from the
manager. `Raise` is now *"an agent putting something to the human"*, general over agents since [Carry the
recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md) widened it, and five
flags in this graph are the manager's own judgements. Its `_Avoid_` clause refuses `ask` on the human's own
ground from that node's third correction round — *"ask is when a worker is designed to ask question to the
user, raise is when the worker is supposed to work mostly by itself but it needs input from the user"* —
which is exactly the manager's position. So the manager's own question is a **blocking raise**, and the only
thing this node adds is that the manager may make one.

Set aside: **replace the triage**, simplest to state and spending the scarce resource on cases a one-line
carve-out answers once and for all; **serve it with one output only**, a licence and a flag with no node,
which is the delta-list pattern [map.md](../map.md) has already recorded as failing; and **refuse it**, which
keeps the contract absolute at the price of a stall the record shows nobody has ever paid.

**A2** — `verbatim`

> ok for recommendation

The option that phrase points at is the worker's `RECOMMENDED` block for Q2, quoted above and **written by
the worker, not by the human**. The manager had agreed with it in the relay and said so, having been the party
arguing the other way at Q1 — the `flags.md` evidence is what moved it — and had added one cost the worker did
not mention: **two outputs means every manager raise mints a node**, so the frontier grows each time. At the
observed rate that is two nodes in thirty-one, which is cheap; were it to fire often, the ask would be
reporting that the contracts are wrong more than it would be reporting anything about the node.
