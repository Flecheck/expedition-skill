# A worker's handover carries no acceptance condition for the node it mints

Type: implementation
Status: resolved

## Question

All five worker contracts write the same handover part:

```
NEW NODES:     <name, kind, question, blockers — one block each>
```

Nothing there is an **acceptance condition**. Yet [Node type taxonomy](07-node-type-taxonomy.md) and
`CONTEXT.md` both fix that a condition is written by the node that spawned it, **before any work starts**,
and [`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s `### Claim` procedure
forbids claiming an implementation node without one:

> An `implementation` node may not be claimed until it has an `## Acceptance condition`.

So a worker that surfaces an implementation node returns no condition, and the manager writes one later.

### This is why three conditions in a row were manager-written

- [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md)'s — and
  [What the checker contract owes to having been run](31-checker-contract-owes.md) records that it **had to
  be amended twice**, once for naming a glossary entry that does not exist, once for a clause true only of
  implementation nodes.
- That same node's own condition 6, added by [Whether a spawn may override a shipped worker
  contract](28-spawn-overriding-a-contract.md), marked `Manager-written` in place with the warning attached.
- [An acceptance condition is self-contained text](33-condition-is-self-contained.md)'s, whose condition 6
  then **failed the very rule that node shipped** — it named four node files inside the record and put its
  deliverable in the node's `## Answer`, which a checker is never given. The blind checker declined to
  establish it rather than passing or failing it.

Three instances, one cause, and the warning has been carried forward by hand each time instead of fixed.

**The rule node 33 shipped binds whoever writes a condition. The handover gives them nowhere to write one.**

### What the fix probably is, and what it must not assume

A sixth element on the `NEW NODES` block, required for an implementation node and absent for every other
kind — plus the self-containment rule stated where the writer will actually read it, which is the worker
contract rather than `graph-conventions.md`.

One thing to decide rather than assume: a worker mints a node **at the end of its own work**, having never
read the node it is minting for. Whether it is in a position to write a condition at all, or whether the
honest answer is that the manager raises it to the human, is this node's to settle — and *"the manager writes
it"* is the option already known to cost two amendments.

Reported by [An acceptance condition is self-contained text](33-condition-is-self-contained.md)'s worker.

### The same defect on a second handover part: `FLAGS` names one artifact where the graph needs two

Added in place by [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md) at its gate, this node being open and
unstarted. It is the **same shape** as the node's own subject — a handover part naming one artifact where
the graph needs two — so it belongs here rather than in a node of its own.

All five contracts write:

```
FLAGS:         <one line each, prefixed ASSUMPTION>
```

But a flag lands in **two** places under **two different caps**, fixed by
[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s `### Raise a flag`
procedure: free prose under the node's `## Flags`, and one capped sentence in [flags.md](../flags.md).
*"One line each"* names neither, and nothing in any contract says which of the two a worker is writing.

**What happens in practice, twice measured.** The worker writes the prose — the more useful half — and the
manager condenses each flag into its index line, authoring text that is neither the worker's nor the
human's. That is the scribe rule broken by omission rather than by choice: the manager is not re-authoring
what it was given, it is writing what it was not given at all.

- Flag `33.4` recorded it at [An acceptance condition is self-contained
  text](33-condition-is-self-contained.md), where the manager authored all four index lines. Settled at
  that node's gate, and **settled is not fixed**.
- It recurred immediately at [The clause that says no resolved node changes cannot be
  self-contained](36-resolved-node-clause-cannot-be-self-contained.md) — two flags, two index lines, both
  the manager's. No flag was filed the second time: a duplicate of a settled flag is noise, and what the
  recurrence establishes is that **nothing owned the fix**, which is what this annotation changes.

Whoever takes this node decides both parts together or says why they differ. One thing not to assume: the
answer may be that a worker writes only the prose and the *capped line is the manager's by design* — in
which case the contracts should say so, and `graph-conventions.md`'s *"written report-shaped at raise time
by whoever holds the context"* is the clause to hold that answer against.

### Three things checked in the files before the condition was written, one of them a correction to this node

Checked by the manager at claim time, the condition below being manager-written and the practice established
at [What the checker contract owes to having been run](31-checker-contract-owes.md) being to read it against
the files first.

**1. `NEW NODES` is identical in all five contracts, and this node's quotation of it is exact.** Four
elements, no condition among them:

```
NEW NODES:     <name, kind, question, blockers — one block each>
```

**2. `FLAGS` is *not* identical in all five, so this node's claim that it is needs narrowing.** Three write
`<one line each, prefixed ASSUMPTION or DELEGATED>` — grilling, precondition, prototype — and two write
`<one line each, prefixed ASSUMPTION>` — implementation, research. The marker list differs because
`DELEGATED` is only reachable by a worker that talks to the human. What *is* common to all five, and is the
defect, is **`one line each`**: one artifact named where the graph has two.

**3. A worker never reads `graph-conventions.md`, so a rule stated only there does not reach the party
writing a condition.** Every contract's `## What you read` lists the node's own file, `map.md`, the
`decisions.md` sections the spawn names, and the paths the spawn expects — and nothing else. The
self-containment rule lives in `graph-conventions.md` alone; `grep -l self-contained` over all six skill
files returns that document and no contract. That is not a guess about where the writer will look, it is a
closed list of what the writer is given.

### The evidence this node has to weigh, and it points away from the fix the question proposes

Copied in rather than pointed at, being spread across five node files the worker has no reason to open. The
`## Question` above frames the fork as *who writes the condition*, with *"the manager writes it"* discounted
as the option already known to cost two amendments. **Five data points now exist, and the discriminator is
not the author.**

| condition | written by | audited against the self-containment rule before handover | outcome |
| --- | --- | --- | --- |
| [26](26-carry-deltas-into-shipped-files.md) | manager | no — the rule did not exist yet | **amended twice** |
| [33](33-condition-is-self-contained.md) | manager | no | **three clauses came back unestablishable** |
| [36](36-resolved-node-clause-cannot-be-self-contained.md) | manager | yes, by the writer at claim time | checker **reserved nothing** |
| [31](31-checker-contract-owes.md) | manager | yes, by the writer at claim time | six defects found and repaired; checker **reserved nothing** |
| every condition written by a **spawning node's worker** | worker | — | [node 33's audit](33-condition-is-self-contained.md) measured them and **all pass** |

Two readings of that table are available and they differ in what this node should build.

- **The author is the variable.** Workers' conditions have a perfect record and the manager's do not, so move
  the pen: a fifth element on `NEW NODES`, which is the fix the `## Question` proposes.
- **The audit is the variable.** Within the manager-written set, the two audited conditions cost nothing and
  the two unaudited ones cost five defects between them. On that reading, moving the pen fixes nothing and
  what has to travel is **the rule and the duty to check the condition against it**, whoever holds the pen.
  The map records this reading: *"what fixed it was the writer applying node 33's rule against their own
  text, not a different party writing it, so moving the pen may not be the repair that node is looking
  for."*

The two are not exclusive and the cheap answer may be both. What the node may not do is take the first
reading silently, since the second is the one the evidence arrived to support.

**One clause already in the shipped files speaks to the second half of the node**, and the answer is held
against it: `graph-conventions.md` fixes the `flags.md` line as *"one line per flag, one sentence, written
report-shaped at raise time by whoever holds the context."* At raise time the party holding the context is
the **worker**. So the document already says the capped line is the worker's, and the practice — measured
twice, at nodes 33 and 36 — has been the manager writing it. Either the practice is wrong or the clause is,
and this node says which.

### Standing instructions to whoever works this node

Binding on the worker rather than on the checker, and held here rather than in the condition because a
checker cannot establish them.

- **The fork above is yours to settle, and the raise is there if you hold no recommendation you believe.**
  That is your contract's trigger 3. Do not settle it by picking the reading the `## Question` proposes
  because it is proposed there — it was written before the last two data points existed.
- **Say your ground in the handover's `ANSWER`**, naming which reading of the table you took and what the
  other would have cost. Not in the acceptance condition's terms and not in a file the checker reads: the
  ground is for the human at the gate and for the next reader of this node.
- **Where the answer touches `graph-conventions.md`'s clause about who writes the capped line, reconcile it
  rather than leaving two documents disagreeing.** A shipped clause left standing against a new practice is
  the exact defect [What keeps the shipped files consistent when a decision changes a
  term](29-shipped-file-consistency.md) owns.
- **`expedition-checker/SKILL.md` is not one of the five and is out of scope.** A checker mints no nodes and
  raises no flags; it returns `PASS`, `FAIL` or a raise, with `QUESTIONS:` and `NOT COVERED:` riders. Six
  skill files exist and only five are worker contracts.

### The acceptance condition is owed

Written by whoever spawns this, and it may not be claimed without one — which is this node's own subject
arriving in its own paperwork.

**Now written, below**, by the manager, there being no spawning node's worker to write it — which is itself a
data point for the fork: this node was minted by node 33's worker, whose handover had nowhere to put a
condition, so the manager wrote one. The manager-written warning applies, and the audit above discharges it
as far as one reading can.

**Sequencing, not a blocker.** It touches the five `expedition-<type>/SKILL.md` files, which are also the
live territory of [Checking a flag before the human sees it](30-checking-a-flag-before-the-human.md) and [Narrow the
flags.md clause in the worker contracts](32-narrow-flags-file-clause.md). The landing policy forbids a second
commit against one **node**, not against one **file**, so these may run in any order — but not concurrently,
the code slot being exclusive.

## Acceptance condition

**The five worker contracts, named once and referred to below as *the five*:**
`.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`,
`.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`,
`.claude/skills/expedition-research/SKILL.md`.

1. **Each of the five states what a worker minting an `implementation` node owes toward that node's
   acceptance condition.** Each writes today, identically, a handover part with four elements and no
   condition among them:

   ```
   NEW NODES:     <name, kind, question, blockers — one block each>
   ```

   while a minted implementation node cannot be claimed until it has an `## Acceptance condition`. Any of
   these three answers satisfies this, provided **all five say the same thing**: the minting worker writes
   the condition; the minting worker writes a named and bounded part of one, and the file says who completes
   it; or the minting worker writes none, and the file says who writes it and when. A contract that leaves
   the question unstated does not satisfy this, and neither does one that states an answer the other four do
   not.

2. **Where the answer puts a condition, or any part of one, in a worker's hands, the self-containment rule
   reaches that worker inside the contract.** It does not reach one today: every contract's `## What you
   read` is a closed list — the node's own file, `map.md`, the `decisions.md` sections the spawn names, and
   the paths the spawn expects — and the rule lives only in `graph-conventions.md`, which is on no
   contract's list. Six things have to be present, in the contract's own words and in whatever order suits
   it:

   - everything needed to judge whether the work is done is **in the condition**, and its reader never goes
     anywhere else to find out what it demands;
   - that reader is the **checker**, which is handed the condition as text and has not read the node;
   - a **path** may say where — the work must touch that file, produce it, or leave it in a stated state —
     because the checker has the repo;
   - what may never sit outside the text is **the demand itself**: *as decided at node NN*, *the section
     agreed in the interview*, *the wording the human chose*;
   - material genuinely held elsewhere is **copied in** by whoever writes the condition, and **the bar is
     the one exemption**, because it reaches the checker by its own route;
   - a demand that **quantifies over the record** — that the work contradicts no decision, that everything
     traces to one — no copy repairs, and it belongs on the handover's `INVALIDATIONS` instead of in any
     condition.

   Where the answer puts none of a condition in a worker's hands, this is satisfied by the contracts not
   gaining the rule — and each of the five then says where the party that does write it reads the rule.

3. **Each of the five names both places a flag lands, rather than one.** The current text names one artifact
   and it is the shared defect: three write `FLAGS:         <one line each, prefixed ASSUMPTION or
   DELEGATED>` and two write `FLAGS:         <one line each, prefixed ASSUMPTION>`, so *"one line each"* is
   common to all five while the marker list is not. A flag lands in two places under two different caps:

   - **on the node, under `## Flags`** — one entry per flag, free prose, prefixed with the flag's id and its
     marker, ~~where a one-line summary is enough and more is permitted~~ **where a one-line summary is
     enough and more is permitted — except where the node has no round at all, and then that entry carries
     the account of what produced the flag itself.** *(Amended mid-node at the gate, on the human's
     instruction, after the blind checker found the struck wording complete for three of the five contracts
     and incomplete for two. `graph-conventions.md`: "A one-line summary is enough under `## Flags`; it is
     not enough in the round that created it. Where there is no round at all — a `research` node, an AFK
     `precondition` node — the `## Flags` entry carries that account itself." The two kinds with no round
     were being told the opposite, and `graph-conventions.md` is on no contract's read list, so nothing else
     reaches them. The exception must reach the worker of a kind that has no round; stating it in all five,
     phrased over the node rather than over the kind, satisfies this and keeps the byte-identity flag `35.3`
     bought.)*
   - **in `flags.md`** — one line per flag, **one sentence**, carrying the same id and marker, linking the
     node, and carrying the flag's checked state.

   After the work each of the five says which of the two a worker is writing, and where the answer is both,
   says that they are two things under two caps rather than one line serving both. The marker lists stay as
   they are unless the answer requires otherwise; correcting the `DELEGATED` asymmetry is not this node's
   work.

4. **Who writes the capped `flags.md` line is stated, and the shipped clause that already answers it does
   not end up standing against the answer.** That clause, in `graph-conventions.md`:

   > One line per flag, one sentence, written report-shaped at raise time by whoever holds the context.

   At raise time the party holding the context is the worker, so the document already assigns the line to the
   worker. Where the answer agrees, the five say so. Where the answer is that the line is the **manager's**
   by design, `graph-conventions.md` is edited so that the two documents agree, and the edit is confined to
   that reconciliation.

5. **The bar as [map.md](../map.md) records it for this repo**: no build, no tests, no formatter, no CI, and
   nothing to invoke. So the project criteria, this map's standing preferences, `CONTEXT.md`'s `_Avoid_`
   lines, and these conditions are the whole of it — a complete bar on its remaining half rather than a
   deficient one.

6. **Which files change.** The five are in scope. `graph-conventions.md` is in scope only for the
   reconciliation condition 4 may require, and for the `NEW NODES` and `### Raise a flag` procedures if the
   answer contradicts what they say. `.claude/skills/expedition-checker/SKILL.md` stays exactly as it is: a
   checker mints no nodes and raises no flags, so it is not one of the five. `CONTEXT.md` is edited only
   where a term genuinely moves, and where one does, **no sweep of the other files happens from inside this
   node**. The reason, copied in rather than pointed at: **nothing checks the shipped files against the
   glossary**, so a decision that changes a word leaves every other shipped file carrying the old one with no
   mechanical check and no agent's contract looking for it — which makes a sweep from here look necessary and
   makes it wrong. Reporting the move is owed on the **handover**, where `NEW NODES` and the `ANSWER` already
   live, and is no part of this condition.

**One warning to whoever claims this, and it demands nothing** — it is addressed to the party that claims
the node, not to anyone checking the work, and there is nothing in it for a check to establish. It is also
this node's own subject: **this condition is
manager-written**, because the handover that minted this node had nowhere to carry one. Two manager-written
conditions in this effort cost five defects between them and two cost none, and the difference was an audit
by the writer before handover. That audit was run here and is recorded above the condition. It is one
reading and not a guarantee — read these against the files, and raise what does not survive it.

**The audit missed one, and the check caught it.** Condition 3's dictated wording for the node-side cap is
complete for three of the five contracts and incomplete for two. Found by the blind checker and recorded
under `## Review` below, which is the honest measure of what an audit by the writer is worth: it removed the
defects visible in the condition's own terms and not the one that only appears when the condition is held
against a file it does not name.

## Answer

*(This replaces the handover written before correction round 1, per the never-delete rule's escape for
a near-duplicate; the round-by-round difference is in `## Review`.)*

**Both halves of this node land the same way: the worker authors, the manager files.** The five
worker contracts each gain two sections and lose *"one line each"* from `FLAGS`. The text of both
new sections is **byte-identical in all five files** (verified by hash over the section range).

**What changed, in each of `.claude/skills/expedition-{grilling,implementation,precondition,prototype,research}/SKILL.md`:**

1. The `NEW NODES` template line now reads `<name, kind, question, blockers — one block each, and
   for an implementation node its acceptance condition too>`.
2. The `FLAGS` template line now reads `<per flag, prefixed ASSUMPTION[ or DELEGATED]: the prose for
   your node, then the one sentence for the index>`. The marker lists stay exactly as they were —
   two files `ASSUMPTION`, three `ASSUMPTION or DELEGATED` — the `DELEGATED` asymmetry being out of
   scope.
3. A new `## When you raise a flag` section: a flag **entry** lives in two places under two caps and
   the text for both is the worker's — free prose under the node's `## Flags`, one report-shaped
   sentence for `flags.md` — written as part of raising the flag and never as a tidy-up, each
   carrying the marker. What the manager adds is named as bookkeeping rather than text: the flag's
   id, the link to the node, and its state. Two things inside it arrived at the gate and are
   recorded below: **the exception for a node with no round**, and **the account of what produced a
   flag being a third artifact rather than a third place the entry lives**.
4. A new `## When a node you report is an implementation node` section: the minting worker writes
   that node's acceptance condition, plus the self-containment rule in six parts and the duty to
   read the condition back against it before handing it over.

Both sections sit between `## What you hand back` and `## If you are a replacement attempt` (at the
end of the file in `expedition-research`, which has no such closing section).

**The fork, and the reading taken.** The `## Question` framed it as *who writes the condition* and
discounted *"the manager writes it"* as the option already known to cost two amendments; the
evidence table pointed the other way, at the audit rather than the author. **Both readings are
taken, and the decisive argument is in neither.** No shipped file has ever assigned a condition to
the manager. Four places assign it to the spawning node — `graph-conventions.md`'s node-file
template (*"implementation only; written by the spawning node"*), its `### ## Acceptance condition`
section (*"Written by the node that spawned it, before any work starts"*), `CONTEXT.md`'s glossary
entry, and node 07's decision line. So the five "written by: manager" rows in the evidence table are
five instances of a **departure**, not five instances of a design, and they happened for exactly the
reason this node names: the handover had nowhere to carry one. Moving the pen is therefore not a
change of author but the removal of a workaround — and it is the same defect as the `FLAGS` half,
where a missing handover part left the manager authoring text it was not given, against the scribe
rule.

**What each reading alone would have cost.** Reading A alone (move the pen, leave the rule in
`graph-conventions.md`) hands the new writer the failure mode that produced the five defects: node
33 measured that conditions fail *by clause rather than by author* — what fails is a clause
summarising something the writer had open in front of them, which is most available to a worker
writing at the end of its own work with everything open. Reading B alone (the rule and the read-back
travel, the manager keeps the pen) leaves the manager authoring the standard its own worker is
judged against, contradicts four shipped statements, and leaves the handover defect that minted this
node unfixed — node 35's own condition being the third instance. Neither is sufficient; together
they are two sections and no new machinery.

**The one thing the `## Question` said to decide rather than assume** — whether a worker minting a
node at the end of its own work is in a position to write a condition at all. It is, and the framing
that it *"has never read the node it is minting for"* is inverted: it found the work and phrased the
question, so it holds more of that node than anyone will until a worker claims it. The manager holds
the graph, not the work. Where the worker's context genuinely does not reach, the contracts state a
shortfall route rather than a silent gap: write the part you can, say plainly what is missing and
why, and what you could not write is what the manager puts to the human. Deliberately **not** routed
through a raise — `expedition-research` has no channel to the human at all, and all five had to say
the same thing.

**Why "report" and not "create" or "mint".** Every one of the five forbids a worker to create a
node (*"never create another one"*; the implementation contract's hard rule 6). The condition
therefore travels as text on the handover exactly like every other part, and the sections say
"a node you report", which is the contracts' own existing verb (*"Report `NEW NODES` and
`INVALIDATIONS` yourself"*).

**A flag's cap is not uniform across the five, and the exception is phrased over the node.** The
blind checker found that the node-side cap this node's condition dictated — *"a one-line summary is
enough and more is permitted"* — is complete for three kinds and wrong for two.
`graph-conventions.md`: *"A one-line summary is enough under `## Flags`; it is not enough in the
round that created it. Where there is no round at all — a `research` node, an AFK `precondition`
node — the `## Flags` entry carries that account itself."* Since `graph-conventions.md` is on no
contract's read list, `expedition-research` and `expedition-precondition` were being told the
opposite of what the conventions require, with nothing else reaching those workers. The exception is
now in all five, and the call inside it: it is phrased over **the node** — *no exchange with the
human, and no gate* — rather than over the **kind**. That yields the same two cases the conventions
name (`research` always; `precondition` only when it never relayed), keeps the five byte-identical,
and stays correct if a kind's shape changes, where a list of kinds would silently go stale. Checked
against all five kinds: it does not fire for `grilling`, `prototype`, an HITL `precondition`, or
`implementation`, which always reaches a `## Review`.

**Flag text reaches three places, and only two of them are the entry.** Also from the gate: the
round that raised a flag must say *what produced it*, *"in its words"*, and no handover part carries
that text out of any worker. So the section's claim is now about where a flag **entry** lives, and a
closing paragraph names the account of what produced the flag as a **different artifact** — carried
by the round that created it, or by the `## Flags` entry itself where there is no round. The third
handover part that would carry it out of a worker with a round is deliberately **not** built here; it
is a node of its own, minted at this gate.

**Why `graph-conventions.md` was not edited, condition 6's allowance going unused.** Its `flags.md`
clause — *"written report-shaped at raise time by whoever holds the context"* — already assigns the
capped line to the worker, so condition 4's first branch applies and the five now say plainly what
that clause left to be derived. `### Raise a flag` is untouched because it fixes who *performs* the
two writes (the manager) and never said who authored the text; its *what produced it* paragraph is
now reflected in the contracts rather than contradicted. `## Adding a node` is silent on the
acceptance condition rather than assigning it elsewhere, and silence does not stand against the
answer. Recorded as a flag, since the derivation demonstrably did not happen by itself.

**Why `CONTEXT.md` was not edited.** No term moved: `acceptance condition`, `checker`, `the bar`,
`flag` and `marker` are all used in their glossary senses, and the glossary's `Acceptance condition`
entry already says *"written by the node that spawned it, before any work starts"* — which this work
implements rather than changes. The `Handover` entry lists the parts as a gist and already omits
`GATE PAYLOAD`, so it does not become wrong by not naming the condition.

**Two practices are now explicitly wrong, and neither is a resolved node.** The manager authoring a
capped `flags.md` line (measured at nodes 33 and 36, and the subject of flag `33.4`), and the manager
authoring a condition for a node a worker minted. Both were workarounds for a missing handover part.

**What this does not fix.** A node the manager mints *itself* — from the human's steering, from its
own reading of the graph, or as a replacement in a supersession — has no minting worker, and every
manager-written condition in the evidence table above is of that kind, including this node's own. The
five contracts cannot reach that case, and it is minted as a node below.

**Cost note for a later reader.** A self-contained condition on a handover is longer than a
four-element block, but it reaches the graph as a paste rather than as authoring, so it costs the
manager the cheapest act it has. The alternative was the manager reconstructing from the graph what
the worker already held.

**Not carried into the shipped files:** the effort's own history. No evidence table, no node numbers,
no *"this cost five defects"* — the shipped files state the rules and not their history, per node 21
and the map's delta note.

## Flags

`35.1` **· settled** `ASSUMPTION` — **Left `graph-conventions.md` untouched, though condition 6 had opened it.** The
worker's own words: *"The answer contradicts neither: the `flags.md` clause already assigns the capped line
to whoever holds the context at raise time, which is the worker, and `## Adding a node` is silent on the
acceptance condition rather than assigning it elsewhere while two other places in the same file already say
'written by the spawning node'. I read silence and agreement as **not standing against the answer** and made
no edit."* And the residual it names: *"A human who wants that document to name the **worker** outright,
rather than leaving it to be derived, would edit two clauses there — and the practice measured at nodes 33
and 36 is evidence that the derivation does not happen by itself."*

`35.2` **· settled** `ASSUMPTION` — **Wrote the route for a worker that cannot state what done means, no resolved node
covering it.** The condition permitted a file to say who *completes* a partial condition; nothing said what
the worker owes when it cannot write one at all. The worker's route: write the part you can, say plainly
what is missing and why, never leave it out in silence, and what you could not write is what the manager
puts to the human. Two calls inside that are its own, in its words: it is *"not routed through a raise,
because `expedition-research` has no channel to the human and all five had to say the same thing"*; and it
*"assigns the manager a duty from inside a worker contract — the minimum needed to keep the gap loud, since
a node reported without a condition cannot be claimed at all — while the manager's own side of it stays
unwritten and belongs to the manager's skill."*

`35.3` **· settled** `ASSUMPTION` — **Made the two new sections byte-identical in all five rather than trimming each to
what it alone needs.** Its ground: condition 1 fails a contract *"that states an answer the other four do
not"*, and these contracts are standalone files by design. The cost it names itself: *"a five-way edit for
any future change to either section, in a set of files nothing checks for divergence — the shape of problem
node 29 owns, and the shape that let node 26 and node 27 write the same flag marker two different ways."*
One consequence it accepted: inside `expedition-implementation/SKILL.md` the new text restates what that
file's own `## Words used exactly` already says about the **checker** and **the bar**. **Held after
correction round 1**, which edited the same section in all five and was verified identical again by hash.

`35.4` **· settled** `ASSUMPTION` — **Phrased the no-round exception over the node rather than naming the two kinds.** From
correction round 1, where the amendment permitted either. Its text: *no exchange with the human, and no
gate*. In its words: *"I checked it against all five: it fires for `research` and for a `precondition` node
that never relayed, and not for `grilling`, `prototype`, an HITL `precondition`, or `implementation`, which
always reaches a `## Review`. A named list of kinds would have been more literal and would go stale the
moment a kind's shape changes, and it would have broken the byte-identity flag `35.3` bought. The risk I
accepted is that a worker now judges its own node against a two-part test rather than reading its kind off a
list."*

## Review

### Check 1 — `PASS`, with one question attached

The blind checker, given the four things its contract allows. It established all six conditions and the bar,
and attached a `QUESTIONS:` rider that does not narrow the outcome.

**The rider is the route [What the checker contract owes to having been run](31-checker-contract-owes.md)
shipped one node earlier, firing on its first opportunity and finding a real defect.** That node added a
route for *a condition that is checkable, that the work complies with, where complying is itself what
produced the defect* — a case improvised four times before it was written down. This checker reached for it
unprompted and named it in those terms: *"a defect produced by complying, not by departing."*

**What it found, and it is a defect in this node's manager-written condition.** Condition 3 dictated the
node-side cap as *"where a one-line summary is enough and more is permitted"*. That is complete for three of
the five contracts and **incomplete for two**, because `graph-conventions.md` says:

> A one-line summary is enough under `## Flags`; it is not enough in the round that created it. Where there
> is no round at all — a `research` node, an AFK `precondition` node — the `## Flags` entry carries that
> account itself.

`research` and AFK `precondition` are exactly the two kinds with no round, and their contracts now
positively tell their worker that a one-line summary is enough, with no mention of the exception. And
because every contract's `## What you read` is a closed list that `graph-conventions.md` is not on, **that
requirement has no route to those two workers at all.** The checker did not fail the work for it, correctly:
the wording was the condition's own and so not the worker's to depart from, and the condition had narrowed
scope explicitly elsewhere.

**Two smaller findings from the same passage, and the second is this node's own defect recurring a third
time.** `graph-conventions.md` requires the round that raised a flag to say **what produced it** *"in its
words"*, and **no handover part carries that text out of any worker**. So a flag's text lands in **three**
places, not two — the node's `## Flags`, `flags.md`, and the round that created it — and the work's new
section says two. That is the same shape as this node's two halves: a handover part naming fewer artifacts
than the graph needs. Neither finding is reached by any part of this condition.

**On its own blindness.** It settled the moved-standard question first, under the rule node 31 shipped: no
standard the bar carries is among the changed paths, so it had unmoved text to hold the work against. It
found the same reviewing skill and took condition 8's preferred discharge — invoking the Standards axis with
the fixed point, the diff command, the standards sources and the Fowler baseline supplied, plus an explicit
read boundary forbidding the node files, `decisions.md`, `flags.md` and all of `map.md` except its
`## Notes`. It left the Spec axis unrun on the now-familiar ground, and verified each of the axis's findings
against the files itself before keeping any.

**How it established condition 1's identity requirement**, which is the clause the whole answer turns on: it
extracted every added line from each file with `git diff -U0 | grep '^+'` and diffed them pairwise against
the grilling copy. The only differences are the two preserved marker lists and one blank line at a file end.

Bar: the command half confirmed empty rather than assumed — `ls -a` returning `.claude CONTEXT.md .scratch
.git` and nothing else, and a `find` over eleven manifest and config patterns printing nothing.

### Correction round 1

The human's words, `verbatim`, on reading the gate payload and the checker's question:

> correct the thing. For "
> One more finding from the same passage, which I'd mint rather than fix here. graph-conventions.md requires
> the round that raised a flag to say what produced it "in its words" — and no handover part carries that
> text out of any worker. So a flag's text lands in three places, not two, and the new section says two.
> That's this node's own defect recurring a third time, and it's a node rather than a clause.
> " we will need to do something.

**Two instructions, and the second is not the worker's.** *"Correct the thing"* names the gate outcome
`correct` and takes the checker's question — the manager's recommendation had been `correct` on the ground
that the fix is two clauses in files already open in the code slot, against a follow-up node paying a
worker, a checker and a gate for two sentences. *"We will need to do something"* quotes the manager's own
proposal to **mint rather than fix here** and does not contradict it, so the third-artifact finding becomes
[Nothing carries a flag's account of what produced it](40-flag-account-has-no-handover-part.md) rather than
work in this round.

**Condition 3 was amended before the worker was resumed**, its node-side bullet struck and replaced in
place, because the work had complied with the struck wording — so without the amendment the fix would have
been a departure from the condition rather than a repair of it. The amendment is recorded at the bullet
itself with the `graph-conventions.md` clause it was missing.

**What the worker was sent**, both in the same turn as this record per the eighth delta: the amended
condition, the two contracts affected, the permission to state the exception over *the node* rather than the
*kind* so byte-identity survives, and one bounded precision fix — make the new section's flat *"two places"*
claim precise, since flag text reaches three artifacts while a flag **entry** lives in two. With an explicit
limit: **do not build the third handover part**, that being a piece of work rather than a repair, and a
raise if it judges the precision fix impossible without it.

**This is the first correction round in the effort that came from a checker's question rather than from the
human reading the work.** The route it arrived on was shipped one node earlier by [What the checker contract
owes to having been run](31-checker-contract-owes.md), which is the shortest interval between a rule landing
and paying for itself that this map has recorded.

**What the worker changed**, both edits inside `## When you raise a flag` and both applied to all five:

- **The node-side cap gained the exception, phrased over the node** rather than by naming the two kinds:
  *"Except where your node holds no round at all — no exchange with the human, and no gate — because then
  nothing else records what produced the flag, and this entry carries that account itself: what you actually
  did, in your words."* It reported checking the test against all five kinds, and that it fires for
  `research` and for a `precondition` that never relayed while not firing for `grilling`, `prototype`, an
  HITL `precondition`, or `implementation`. Flag `35.4`.
- **The flat *"two places"* claim is now about the flag's entry**, with a closing paragraph naming the
  account of what produced the flag as a different artifact — carried by the round that created it, or by
  the `## Flags` entry where there is no round. It built no handover part for it, as instructed, and did not
  raise, so it judged the precision fix possible without one.

It reported the change as touching **condition 3 only**, which is the condition that was amended, and named
the other five as standing. Its `## Answer` **replaces** the pre-correction handover rather than stacking
beside it — the worker invoked the never-delete rule's escape for a near-duplicate itself, which is the
second deliberate use of the prune remedy in this effort after [Carry the recorded deltas into the shipped
skill files](26-carry-deltas-into-shipped-files.md)'s, and the first taken by a worker rather than the
manager.

**The manager verified the identity claim rather than taking it**, that being the clause condition 1 turns
on: the added lines of `grilling`, `precondition` and `prototype` hash identically, while
`expedition-implementation` and `expedition-research` differ — by their preserved `ASSUMPTION`-only marker
list, and in `research`'s case one trailing blank line, that file having no `## If you are a replacement
attempt` section. That is exactly the divergence the worker declared.

### Check 2 — `PASS`, no questions

The same checker, resumed with a statement of what changed, the previous outcome's time, the amended
condition, and the fact that modification times could not separate the two rounds. Its own summary: the
amendment answered the question it raised, and the fix matches it clause for clause.

**It re-established condition 3 from scratch and said so**, rather than inheriting what it had concluded
against the struck wording — which is the rule [What the checker contract owes to having been
run](31-checker-contract-owes.md) shipped for a condition amended mid-check, firing on the node immediately
after it landed. It also held the phrasing to the amendment's own requirement: the exception is *"phrased
**over the node**, as the amendment requires"*, and it read the worker's gloss — *no exchange with the
human, and no gate* — as a faithful reading of `graph-conventions.md`'s *"an `## Interview` attempt or a
`## Review` round"*.

**It compared words rather than lines, because the bullet had been rewrapped** — unwrapping both its own
previous extract and the current text to one word per line and diffing. That is the other half of node 31's
condition 3, arriving on the same node as its condition 6. It found **exactly three** edits and no fourth,
and verified the word-level delta identical across all five: the delta files differ only in hunk line
numbers, *"because the two short-marker-list files carry two fewer words earlier"*.

**It did not take `untouched` on the worker's word.** It re-extracted `## When a node you report is an
implementation node` and found it word-for-word identical to its last round's extract, re-read all ten
template lines rather than the report, and ran `git status --porcelain` on `CONTEXT.md`, the checker contract
and `graph-conventions.md` — all three unmodified. It also re-read the two `graph-conventions.md` passages
this node turns on at their current bytes, confirming the amendment's quotation of the first was accurate.

**Three findings for the manager, and the second is a real gap in what a re-check spawn carries.**

**1. It corrected its own previous outcome.** It had labelled its first-round baseline `49e77f2`, taken from
the session-start snapshot, which was already stale when it began; the real `HEAD` was `87543ba` throughout.
Its first-round diff used a bare `git diff` against the real `HEAD`, so the work it checked was the right
work and only the printed commit id was wrong. Worth keeping because the error is one a blind checker is
structurally exposed to: the snapshot it is handed at session start is a fact that expires, and nothing tells
it when.

**2. Two files it holds standards against had moved, and nothing in the spawn said so.** `graph-conventions.md`
and its own contract both changed between `49e77f2` and `87543ba` — the commits this effort landed at nodes
31 and 36. It settled that before reading a line of the work, under the rule node 31 shipped, and found both
had landed **before** its first outcome and were byte-identical in the tree to what it used last round, so
nothing had moved under either check and no raise was warranted. Its finding, in its own words:

> a statement of what changed which names only the working tree can leave a checker to discover a moved
> standard on its own

That is a duty the manager was not discharging. The statement of what changed described the **working tree**,
and a standard can move by a **commit** landing between a checker's baseline and its resume — which is
exactly what this effort does after every implementation node. Carried to
[map.md](../map.md) as a requirement on the manager's skill.

**3. One known item stays open and is not a defect in this work.** The three kinds that *do* have a round
still have no handover part carrying the account of what produced a flag, and the new closing paragraph
asserts the round carries it. The checker judged that neither a condition nor a bar failure, the assertion
being `graph-conventions.md`'s own claim restated faithfully and the amended condition demanding no handover
part. It noted an untracked node file named for exactly this had appeared in the tree and **did not open
it** — [Nothing carries a flag's account of what produced it](40-flag-account-has-no-handover-part.md).

### Gate — `approve`

One correction round, then approved. The human's reply, `verbatim`:

> flags ok, approve

**The flags were settled in the human's own words rather than read from the outcome**, which is the first
gate in this effort where that is true. Nodes 31 and 36 both closed on a bare `approve` and their
settlements had to be recorded as the manager's reading of a word that answered the whole payload. *"Flags
ok"* names them directly, so all four of `35.1`–`35.4` are settled by the human and nothing here is a
reading.

Both halves of the gate payload's ask were answered in one line: the outcome named as one of the three, and
the flags settled — which is what [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md)'s payload clause was added to get and
what node 33's *"you can continue"* had cost a recorded reading for.

Bar re-run in full: command half re-confirmed empty rather than assumed, `_Avoid_` sweep over the words added
this round returning no hits, and the two that needed a deliberate look — `## Interview` and `## Review` —
being code-formatted section names in `graph-conventions.md`'s own verbatim phrase rather than the refused
senses.
