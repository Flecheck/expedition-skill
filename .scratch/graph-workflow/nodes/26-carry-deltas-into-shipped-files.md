# Carry the recorded deltas into the shipped skill files

Type: implementation
Status: resolved
Blocked by: 27

## Question

Three files have shipped and have since gone stale. Bring them up to date in one pass.

**[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)** owes the **nine
deltas** listed in [map.md](../map.md)'s `## Notes` — eight recorded there before this node existed, plus
[What is recorded when the human takes an option as offered](25-recording-an-option-taken.md)'s rule, which
is the ninth.

**[`expedition-grilling/SKILL.md`](../../../.claude/skills/expedition-grilling/SKILL.md)** and
**[`expedition-prototype/SKILL.md`](../../../.claude/skills/expedition-prototype/SKILL.md)** each carry one
sentence that is now wrong for a case the workflow has just made ordinary. Both say, of `HUMAN ANSWER`,
*"Reason from what they wrote rather than from the option you offered."* That was written against a
rendering. Against a **terse assent** — *"ok for recommended"* — the option **is** what the human endorsed,
and a worker obeying the sentence literally would discard the content of the answer. The two contracts need
a carve-out and have none. `expedition-precondition` and `expedition-implementation` carry the same
`HUMAN ANSWER` block without that sentence and need nothing; the sentence was verified on disk to live in
exactly those two files, both at line 98.

Reported by [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md)'s worker. Its own note on where this belongs: the map's delta
list covers only `graph-conventions.md`, so **the contract sentence has no home today** — which is what
makes this a node rather than another line on that list.

Why one node and not three: the landing policy allows exactly one commit per implementation node, so a file
touched here cannot be touched again without superseding this node. Everything owed to these three files at
the time this node is claimed goes in it.

That is also why this node is **blocked by [Whether flags.md survives the settle-at-close
practice](27-does-flags-file-survive.md)**: `graph-conventions.md` states where a flag's state lives, and
that node may move it. Writing the current answer here and the new one afterwards is precisely the second
commit the landing policy forbids.

## Acceptance condition

1. Every one of the nine deltas recorded in [map.md](../map.md)'s `## Notes` is present in
   `graph-conventions.md`, in that document's own voice rather than as a changelog. The map's delta
   paragraph is annotated as discharged **in place** — struck through, not deleted, per the standing rule.
2. `graph-conventions.md` states [What is recorded when the human takes an option as
   offered](25-recording-an-option-taken.md)'s rule for **both** `## Interview` and `## Review`: the
   manager pastes the human's reply as they wrote it, however terse, marked `verbatim`; the option or
   outcome it points at is quoted beside it and attributed to whoever wrote it; nothing is rendered, so
   nothing on either log is marked `paraphrase` unless the manager genuinely could not avoid rendering it.
   It also states the residual case — where a terse reply does not make clear which option it points at,
   the manager records the reply and asks which.
3. `expedition-grilling/SKILL.md` and `expedition-prototype/SKILL.md` carry the carve-out: where the
   human's words are an assent to a named option, that option is what they endorsed and the worker reads it
   as theirs. Placed with the sentence it qualifies. ~~The other four contracts are unchanged.~~ **Shrunk at
   correction round 2 by condition 7, which puts two of those four in scope: what survives is that
   `expedition-research` and `expedition-precondition` are unchanged.**
4. No decision on any resolved node is changed. This node moves text; where the shipped files and a node
   disagree, the node wins and the file is what moves.
5. **Everything [Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md)
   requires of `graph-conventions.md`**, which that node's answer states in full and which needs no
   re-deciding. Five items: a statement of `flags.md`'s **job**, which the document currently omits
   entirely — the capped index of the graph's agent judgements, one report-shaped line each, written at
   raise time by whoever has the context and never reconstructed later; the corrected **ground** for
   *"this file wins"*, which is that the sweep and the closing report are built from it, the old ground
   having been destroyed by the seventh delta; the **correction of a sentence that is wrong on disk
   today** — `### Settle a flag` reads *"No other file changes, and the node file is not touched"*, which
   the seventh delta contradicts; **settle-at-close as the norm and the closing report as the exception
   path**, covering only flags that had no human moment; and **mechanical check 6 extended to compare the
   two states**, so a flag `[x]` in `flags.md` must be marked `settled` on its node and the reverse. That
   last one is the human's overruling of flag `27.2`, given on the condition that the check already
   exists — it does, and the sixth delta already obliges this node to rewrite that same line as an id
   join, so the comparison is one clause added to it.
6. The bar as [map.md](../map.md) records it for this repo: no build, no tests, no formatter, so the
   project criteria, this map's standing preferences, [`CONTEXT.md`](../../../CONTEXT.md)'s `_Avoid_` lines,
   and these conditions are the whole of it.

**Added at correction round 2**, written by the manager from the human's instruction on flag `26.8` and
tested immediately as the first use of the rule flag `26.7` produced — a scope extension now arrives with its
own condition instead of as a bare instruction.

7. `CONTEXT.md`'s *Raise* entry states the general sense — a raise is an agent putting something to the
   human, and whether it blocks is a property of the channel rather than of the word: a worker's raise stops
   its work until the human acts, a checker's question handed back alongside its outcome does not, and a flag
   ~~waits for the gate~~ **waits for the human moment that ends its node — a grilling node's last answer, an
   implementation node's gate** *(amended at correction round 3: the struck wording was the manager's and was
   true only of an implementation node, which the checker found and correctly declined to fail on, the words
   being the condition's own)*. Where `expedition-implementation/SKILL.md` and `expedition-checker/SKILL.md` define
   `raise` under *Words used exactly*, each reads as its own channel's specialisation of that sense rather
   than as a competing definition. `CONTEXT.md`'s *Flag* and *Ask* entries do not contradict it. No other
   file changes.

## Answer

> **The worker's final handover, pasted unaltered**, as it stood after correction round 3 and checker run 4.
>
> It **replaces** the round-0 handover that stood here through three correction rounds, rather than being
> stacked beside it. The two were about 95% identical and the round-0 text had become wrong in five places —
> the file count, the flag's moment, and three whole paragraphs it lacked. Keeping both would have added
> ~1700 duplicated words to a file whose reader is the next agent, and every difference between them is
> already recorded round by round in `## Review`. So nothing is lost and the record stays readable. This is a
> deliberate exercise of the never-delete rule's own escape — *information leaves a file only when it is
> clearly wrong* — and it is logged as evidence on [map.md](../map.md)'s fog item about never-delete and
> load-once-cheaply being in direct conflict, which is the item that will have to rule on whether this becomes
> practice.

**Six product files, one pass. No graph file was touched.**

`graph-conventions.md` now carries all nine deltas from the map's `## Notes`, each in the document's
own voice and none as a changelog line:

1. **The map's two optional `## Notes` blocks** — the effort's **ground rules** and a **standing over
   sources** declared by path and glob (authoritative / evidence only / known false), absent any
   declaration everything a worker is pointed at being authoritative — into the `## Notes` bullet of
   `## The four files`.
2. **Scribe** — the opening statement now reads *"The manager is the graph's only writer, and it writes
   as a scribe"*: it pastes each part under its heading and never re-authors, shortens, re-orders or
   re-renders, and what the manager has of its own goes in beside that text as its own marked note.
3. **`## Review`'s required shape** — that subsection is now three numbered items and *"nothing beyond
   them"*: the checker's chronology one entry per run, each correction round numbered with the human's
   words verbatim and what the worker changed, and the gate's outcome named as one of
   approve / correct / reject with a reject also recording what implementing the node surfaced and
   which route it took.
4. **The chronology's third entry kind** — a run either names `PASS`, or names `FAIL` and which of the
   two it failed, **or raised instead of judging**, issuing no verdict at all, the entry saying what it
   raised. Written inside item 1 rather than as a separate rule, because it is a variant of one entry.
5. **The two stale `CONDITION-WRONG` sentences** are gone. `### Acceptance condition` now reads that
   the worker may not rewrite it and **raises** rather than shipping quietly past a condition it judges
   wrong, *"because a broken condition is not the worker's to fix"*; the marker list entry now reads
   *"the manager's, filed after a worker raised its acceptance condition as wrong and the human
   answered ship it anyway"*.
6. **Flag ids `NN.k`** — node number then a sequence within that node, in write order, never reused —
   in all four places they bear: the `flags.md` form, the `## Flags` prefix rule, `### Raise a flag`
   (step 1 allocates *"the next unused `k` for that node"*, step 2 carries the same id), and check 6.
7. **`settled` on the node as well as checked in `flags.md`**, with the two-place state named as such
   and `flags.md` declared the winner; the word fixed (*"a node resolves, a flag settles"*); and the
   companion rule that the round which raised a flag says **what produced it** — for a worker's own
   unprompted judgement, what the worker actually did in its words — a one-line summary being enough
   under `## Flags` and not enough in the round that created it. **Where there is no round at all**, a
   `research` node or an AFK `precondition` node, the `## Flags` entry carries that account itself.
   Those are exactly the nodes the closing report's residue is made of, so without that clause the
   production rule had nowhere to live for the flags that most need it; the gap was in the seventh
   delta's own wording rather than in the document.
8. **The write and the resume go together** — the ordering rule no longer says *before*. It says the
   graph is written the moment the human speaks, that resuming a worker is a background send and does
   not block, so the manager issues the resume and the write in one turn, and that what the rule
   protects is the answer reaching disk before the worker can return.
9. **What is recorded when the human takes an option as offered** — the manager pastes the reply as
   they wrote it, however terse, marked `verbatim`; the option or outcome it points at is quoted in the
   same entry and attributed to whoever wrote it, usually the worker; nothing is rendered, so nothing
   on either log is `paraphrase` unless the manager genuinely could not avoid rendering it; and where a
   terse reply does not make clear which option it points at, the manager records the reply and asks
   which.

**Node 27's five items are all in, in the same file.** `flags.md`'s **job** is stated where the file is
introduced — the graph's capped index of every judgement an agent made on its own, the flag counterpart
to `decisions.md` and standing to a node's `## Flags` as `decisions.md` stands to its `## Answer`, one
sentence per flag written report-shaped at raise time by whoever holds the context and never
reconstructed later, and the source of **the closing report's outstanding flags** — its unchecked lines.
The file supplies that part of the report and is not the whole of it: the report is also what was
decided and what landed, so the sentence says where those flags come from rather than what the report
is. The **ground** for *"this file wins"* is now *"because the sweep and the closing report are built
from it"*, replacing the destroyed one. The sentence that was **wrong on disk** — *"No other file
changes, and the node file is not touched"* — is gone, replaced by a second step marking the flag
`settled` on its node. **Settle-at-close is the norm and the closing report the exception path**,
carrying only the flags that never had a human moment. **Check 6** is one line with three clauses:
existence both ways, joined on the id, and state agreement in both directions.

`expedition-grilling/SKILL.md` and `expedition-prototype/SKILL.md` each gained the terse-assent
carve-out as the second clause of the sentence it qualifies, at the same line in both, and nowhere else.

**`CONTEXT.md` became the fourth file, because it was the side that went stale.** Delta 5 moved the
judgement about a wrong acceptance condition from a worker's flag to a worker's raise, and
`graph-conventions.md:5` declares the glossary authoritative for the terms — so the shipped document was
left pointing at a file that disagreed with it. Three entries were brought into line, in the glossary's
own plain style (no inner bold, no quoted speech, both properties of that file rather than of this one):

- **Acceptance condition** — *"Its worker may flag the condition wrong but may not rewrite it"* becomes
  the worker may not rewrite it, a condition it judges wrong being a raise rather than a flag of its
  own, and `CONDITION-WRONG` being the manager's to file and only where the human's answer to that
  raise was to carry on and ship it anyway.
- **Flag** — *"A note a worker leaves … It costs nothing until the effort closes"* was stale twice over
  beyond delta 5, and both are corrected. It is a note recording a judgement **an agent** made on its
  own, usually a worker's and the manager's where a judgement of its own reached the graph: this
  graph's own record carries manager-filed flags, so *a worker leaves* was wrong about who as well as
  about `CONDITION-WRONG`. And it is settled at the human moment that ends its node, reaching the
  closing report only where that moment never came — the queue reading node 27 retired. *Where that
  moment never came* is deliberately wider than the document's own two classes, because it has to cover
  both a flag whose node has no human moment at all and a flag raised before the practice existed.
- **Raise** — generalised rather than qualified or renamed. It now reads *an agent putting something to
  the human*, with whether it waits a property of the channel and not of the word: a worker's raise
  stops its work until the human acts, a checker's question handed back alongside its outcome does not,
  and a flag waits for **the human moment that ends its node — a grilling node's last answer, an
  implementation node's gate**. The machinery that was the whole of the old entry survives as the
  blocking kind's — the gate is its scheduled form on a finished diff, a worker opens an unscheduled one
  on the three triggers, below that line it decides and leaves a flag, and a blocking raise holds the
  code slot while it waits, pre-empts grilling work in the manager's queue, and is answered by a
  continue or a stop.

**Why widening `Raise` is a repair and not a redefinition, checked before anything was written.** The
design already used the general sense and already carried the qualifier where it needed one:
`decisions.md`'s line for node 23 reads *"three triggers open a **blocking** raise"*, and that adjective
is only necessary if the bare word is broader. A non-blocking channel to the human already shipped —
`expedition-checker/SKILL.md`'s `QUESTIONS:` block, whose own text says *"You do not wait for an answer,
and your outcome never depends on one"*. So the glossary's entry was narrower than the system it
described, and had been since before any delta. All three legs were verified on disk.

**The flag's moment is one wording used in three places, not three coinages.** *The human moment that
ends its node — a grilling node's last answer, an implementation node's gate* is `graph-conventions.md`'s
phrase for the settle-at-close norm, the *Flag* entry's phrase, and now the *Raise* entry's. The earlier
*waits for the gate* was true only of an implementation node and made two adjacent glossary entries point
at different moments for the same flag.

**What separates `ask` from `raise` is what the worker is built for, not what the turn is.** The
distinction is the human's own: asking is the ordinary mode of a worker built to question the human,
where a raise is what a worker meant to work mostly by itself does when it needs input it does not have.
That cut is decidable from the node's kind before any turn happens — a `grilling` or `prototype` worker
exists to put questions, and the other three are built to work alone — which is why it is better than
judging each turn on whether it was the node's own work. It is also what keeps the widened word from
swallowing a grilling node's interview, which is the boundary the `_Avoid_` clause exists to hold.

**One thing judged and deliberately not done: the general sense's first line was left broad.** Read
literally, *an agent putting something to the human* includes a grilling worker's interview turn, which
the `_Avoid_` clause then excludes — and defining a term widely and taking it back in a note is a real
smell. It was left alone for three reasons. The `_Avoid_` line is precisely the mechanism this glossary
uses for word boundaries, and no other entry pre-empts its own `_Avoid_` line inside its definition —
*Node* refuses `issue` and `ticket` there, *Reject* refuses `abandon` there, *Promote* refuses `postpone`
there. The entry's second sentence already enumerates the three channels the word covers, and an
interview turn is not among them, so the scope is signalled before the `_Avoid_` line is reached. And
narrowing that sentence in the same pass that widened it would work against the instruction that
produced it. Recorded here because the alternative is defensible and a later reader should not have to
rediscover that it was weighed.

**Two worker contracts define `raise` under *Words used exactly*, and only those two.** Verified by
scanning all six. Each reads as its own channel's specialisation, and each says so in a way that works
for a reader holding only that file — both files use `raise` as shorthand for their blocking channel
elsewhere (the implementation contract's *"your two outlets are a flag and a raise"*, the checker's
*"a raise is not one of the three, and hands back no outcome at all"*), so each entry names that
shorthand explicitly instead of leaving the widened word ambiguous against it:

- `expedition-implementation/SKILL.md` — putting something to the human; both your outlets do that, and
  where the contract says *raise* alone it means the one that stops your work until they act, a flag
  waiting for the gate. *The gate* is right in this file and not a third coinage: the gate **is** the
  human moment that ends an implementation node, and the contract already says its flags are read there.
- `expedition-checker/SKILL.md` — putting something to the human; both your channels to them do that,
  and where the contract says *raise* alone it means the one that stops your check and hands back no
  outcome, a question alongside your outcome stopping nothing.

**`expedition-research/SKILL.md` and `expedition-precondition/SKILL.md` are unchanged**, which is what
is left of condition 3's *"the other four contracts are unchanged"* now that two of the four are in
scope by condition 7. Both were checked: research does not contain the word at all, and precondition
uses it twice as an ordinary verb — *"**Raise** when any one of these holds"* at line 67 and *"A raise is
not a fourth thing to hand back: it is the question shape"* at line 75 — defining nothing and competing
with nothing. Its line 81, *"a flag here waits for the closing report"*, is independently consistent
with the widened sense and with the closing report as the exception path.

**Calls a later reader would otherwise have to re-derive:**

- **The option-taken rule and the ordering rule are stated once, not twice.** A new subsection
  `### The human's words, in either log` sits immediately before `### `## Review`` and
  `### `## Interview``, and names both sections in its first line. Both rules govern the two logs
  identically, and two copies of a rule is where drift starts. One visible consequence: the ordering
  rule, previously stated only under `## Interview`, now plainly governs `## Review` too — which is
  what node 12 decided (*"one ordering rule, covering both logs"*) and what node 20's correction round
  already relies on. The `verbatim` / `paraphrase` label moved up with it; `DIVERGENCE` stayed under
  `## Interview`, since it is about the worker's recommendation.
- **The practice is named by its moment, not by the phrase "settle-at-close".** `CONTEXT.md` gives
  `close` to an effort and refuses it for a node, so the document reads *"settling a node's flags at
  the human moment that ends it"*. Same rule as the condition's, in the vocabulary the file is written
  in — and the same phrase now carries the flag's moment in both glossary entries.
- **There is no *Ask* entry in the glossary.** `ask` is refused inside *Raise*'s own `_Avoid_` line, so
  condition 7's requirement about the *Ask* entry resolves to that clause. It carried a ground that
  stopped being self-evident once the word widened; the human replaced it with theirs, and theirs is
  what is written.
- **The id sits in the `flags.md` line as a bare space-separated token** between checkbox and marker:
  `- [ ] NN.k ASSUMPTION · [<node name>](nodes/NN-<name>.md) — <one line>`. The map fixes the id's
  position and not its punctuation, and `flags.md` was left unread per the contract.
- **`### Review` opens *"after the code was written"*, not *"after the code landed"*.** The section now
  holds the checker's chronology, which runs before the commit; node 20 records that the human's review
  stopped being about landed code when landing moved after approval.
- **The three reject routes are named inline** in item 3 — `out-of-scope`, `superseded` by a
  replacement, or back to `open` behind a new `Blocked by:` edge — because *"which route the node
  took"* is unusable in a document that lists none. Taken from node 20's table.
- **`## Flags` still has no checkbox**; it has the word `settled`. The duplication is deliberate and
  the document says which copy wins and why, so the two-place state is documented rather than latent.
- Both new fenced examples use placeholder ids (`NN.k`), matching every other form in the file.
- **`wayfinder-divergences.md` was checked and needs nothing.** Its only statement about the logs —
  each recorded answer marked `verbatim` or `paraphrase` — still holds.
- **The twenty un-id'd flags in `flags.md` were not retrofitted.** The document now states the id form;
  the live graph's conformance to it is graph state, not product code.

## Flags

- `26.1` `ASSUMPTION` **· settled** — stated the option-taken rule and the ordering rule **once**, in a new shared
  subsection naming both `## Interview` and `## Review`, rather than twice under each heading;
  acceptance condition 2 says "for both" and this satisfies it by reference rather than by duplication,
  and it also hoists the ordering rule into a place where it now visibly governs `## Review`.
- `26.2` `ASSUMPTION` **· settled** — chose the punctuation for the flag id in a `flags.md` line, a bare space between
  checkbox and marker, since the map fixes only its position and `flags.md` was left unread per the
  contract; any retrofit of the twenty existing lines has to follow this form. *(Manager's note on
  filing: the form the worker guessed blind is the form already in the file, verified after the
  handover arrived. The assumption was sound and the guess was right.)*
- `26.3` `ASSUMPTION` **· settled** — made two edits to `graph-conventions.md` that no delta strictly required, both
  grounded in node 20: `### Review` now opens *"after the code was written"* rather than *"after the
  code landed"*, and item 3 names the three reject routes inline instead of leaving "route" undefined.
- `26.4` `ASSUMPTION` **· settled** — **filed by the manager**, on spawning the checker. Two of this node's six
  acceptance conditions point **into the record**: condition 1 names the nine deltas by reference to
  `map.md`'s `## Notes` rather than stating them, and condition 4 forbids changing "any decision on any
  resolved node". A checker is blind by contract — *"run no part of one that would take you into the
  record"* — so neither condition is dischargeable as written without breaking that blindness. The
  manager **dereferenced** condition 1, pasting the map's delta paragraph verbatim into the checker's
  spawn as the condition's own referent, and handed condition 4 through unaltered to be raised if the
  checker judges it unmeasurable. Nothing in the design says an acceptance condition may not point at
  the record, and nothing says who dereferences it when it does.

Three more from correction round 1, the first two the worker's and the third the manager's.

- `26.5` `ASSUMPTION` **· settled** — corrected [`CONTEXT.md`](../../../CONTEXT.md)'s **Flag** entry on *who leaves a
  flag*, not only on `CONDITION-WRONG`: it now reads that a flag records a judgement **an agent** made on
  its own, usually a worker's and the manager's where a judgement of its own reached the graph. Judged
  inside the human's word `fix` because it is the same sentence delta 5 falsifies, and because this graph's
  own record already carries four manager-filed flags — `17.4`, `25.4`, `27.3`, `26.4`. The manager put the
  point to the worker to judge rather than deciding it, and this is the judgement.
- `26.6` `ASSUMPTION` **· settled** — also replaced that entry's *"It costs nothing until the effort closes"*, which **no
  delta names**, on the ground that [Whether flags.md survives the settle-at-close
  practice](27-does-flags-file-survive.md) retired the queue reading and condition 4 says a shipped file
  disagreeing with a node is what moves. The worker's own words: *"Went further than `fix` strictly asked
  for, in a file that had only just entered scope."* **Manager's note on filing: it went further and landed
  on something a resolved node had already annotated** — [Done-ness and
  termination](10-done-ness.md)'s `## Annotation: when a flag is paid for` says exactly that *"flags cost
  nothing until the report"* no longer holds. So the sentence the worker judged stale on its own authority
  was stale on the record too, in a node it never read.
- `26.7` `ASSUMPTION` **· settled** — **filed by the manager**, on re-spawning the checker. The node's work now includes a
  file **no acceptance condition covers**. The human's `fix` put `CONTEXT.md` in scope without rewriting
  the condition, which the contract permits them to do and permits the worker never to do — so conditions
  1, 2, 3 and 5 still name three files, and a later reader holding only the condition cannot tell the
  glossary was part of this node. The checker was told its remit on that file is the bar and condition 4
  and nothing else, and told not to invent a condition to fill the gap. Nothing in the design says what
  happens when a human extends a node's scope by instruction rather than by correcting its condition.

- `26.8` `ASSUMPTION` **· settled** — **filed by the manager**, from the checker's third run-2 question, and shipped
  unresolved. **`raise` carries two senses and the glossary now holds both in adjacent entries.** *Raise*
  reads *"Bringing something to the human that stops work until they act… Below that line it decides and
  leaves a flag instead"*, while *Flag* now reads *"Raising one blocks nothing."* The collision is
  **pre-existing and shipped** — it comes from the established `### Raise a flag` procedure and the phrase
  *at raise time*, not from any edit here — and the checker said so, declining to call it a finding. Left
  unfixed because the cheap remedy documents the collision (a clause on *Raise*'s `_Avoid_` line) while the
  right one removes it (renaming the procedure to *file a flag*), and the right one reaches
  [flags.md](../flags.md)'s own prose, which no implementation worker may touch. So the fix that would
  actually settle it is out of an implementation node's reach by construction. **Settled by the human at the
  gate with a third option the manager did not offer** — generalise the word instead of qualifying or
  renaming it — which became condition 7 and correction round 2. `26.8`'s own recommendation was wrong.

One more from correction round 2, the worker's.

- `26.9` `ASSUMPTION` **· settled** — **there is no *Ask* entry in the glossary**, so condition 7's requirement that it not
  contradict the general sense had to be read as the clause refusing `ask` inside *Raise*'s own `_Avoid_`
  line — and the worker **re-grounded that clause** rather than leaving it. From *"a HITL worker's ordinary
  relayed question is not a raise"* to *"is its node's own work rather than a raise"*. Its reason: once
  `raise` covers any agent putting something to the human, the old ground stops being self-evident and **the
  widened word would swallow a grilling node's interview** — an interview turn being the work the node exists
  to do, while everything the widened word covers is something put to the human beyond that. The alternative
  was leaving the entry contradicting its own `_Avoid_`. **Manager's note on filing: this is the one thing in
  correction round 2 that nobody asked for and that the round could not have been done correctly without.**
  The human's proposal and the manager's condition both missed it; the worker found it by reading the entry
  it was told not to contradict. **Settled at the gate, and settled by replacement rather than by assent**:
  the human supplied a different ground for the same refusal — *"ask is when a worker is designed to ask
  question to the user, raise is when the worker is supposed to work mostly by itself but it needs input from
  the user"*. The worker's ground is a property of **the turn** (is this the node's own work?); the human's is
  a property of **what the worker is built for**, which is decidable from the node's kind before any turn
  happens. The worker's reasoning about *why* the old ground had died was right and is what surfaced the
  question at all; the ground that replaces it is the human's.

  **Manager's note: the human's ground is not new vocabulary — it is [Node type
  taxonomy](07-node-type-taxonomy.md)'s HITL/AFK split arriving in the glossary.** *A worker designed to ask
  the human questions* is a HITL worker and *a worker supposed to work mostly by itself* is an AFK one, so the
  distinction reduces to **HITL workers ask; AFK workers raise**, which the taxonomy already fixed and which
  every worker contract already implements. That is strong evidence the ground is right rather than merely
  plausible: it was reached from the glossary and it lands on a split decided fourteen nodes earlier.
  **One edge, recorded and not resolved here:** `precondition` is the single kind the taxonomy says can be
  *either* HITL or AFK — *"the agent drives it alone where it can (AFK); otherwise it hands the human a precise
  checklist (HITL)"* — and its shipped contract uses `raise` at line 67 regardless. So a HITL precondition
  worker handing over a checklist is the one case the reduction does not decide, and nothing in this node's
  scope reaches it. Worth a look whoever writes the manager's skill.

## Review

### Checker chronology

**Run 1 — `PASS`.** First check, no previous outcome and no statement of what changed. All six conditions
established one by one against the dereferenced delta paragraph and the work itself; the bar found
complete on its remaining half by emptiness — the repo holds nine files, no manifest, no task runner, no
CI config, no formatter config — so nothing was run because there was nothing to run.

The first first-attempt `PASS` in this effort. The map's other implementation node of comparable size,
[Write the worker contract skills](22-worker-contract-skills.md), took three checker attempts.

Standards found and used: no repo-level reviewing skill and no repo standards document besides
[`CONTEXT.md`](../../../CONTEXT.md); the machine's `coding-principles` and `naming` skills; and
`CONTEXT.md`'s `_Avoid_` lines. Two machine-level reviewing skills were found and **partly left unrun, by
the contract's own blindness clause** — `mattpocock-skills:code-review`'s Spec axis holds work against an
originating issue or PRD, which is the record, and the plugin `/code-review` command reviews a GitHub pull
request through agents that read origin artifacts. The Standards axis was run in a read-only worker scoped
to the three product paths with `.scratch/` explicitly forbidden, because that skill's own procedure diffs
a fixed point and would otherwise have swept the record in. **This is the first evidence that the checker
contract's blindness clause survives contact with a real reviewing skill**, and what it took was not
refusal but partial execution — one axis run, one axis declined, and the declining said out loud.

The Standards worker's own output was triaged by the checker rather than passed through: most of it
second-guessed decisions the acceptance condition itself mandates — the duplicated flag state,
`CONDITION-WRONG`'s ownership, `approve / correct / reject`, *"a node resolves, a flag settles"* — which
under its contract's rule 2 are not its findings to hand back. Two of its naming objections the checker
verified **false**: `ground rules` and `a standing over sources` are pre-existing shipped vocabulary in two
of the worker contracts, so the new `## Notes` paragraph matches a settled term rather than coining one,
and was right to prefer it to the delta's own looser *"source hierarchy"*.

**Condition 4, checked blind.** The checker cannot read the nodes, so it established *no decision changed*
by tracing every altered passage to a delta or to conditions 2, 3 and 5, then holding the residue against
the glossary. Three edits did not trace to a delta, and it handed all three up rather than judging them.
The manager, which can read the record, confirms each:

- *"What the manager has of its own goes in beside that text as its own marked note"* — the glossary's
  **manager note**, and the sharper point is that this is the sentence flags `17.4`, `25.4` and `27.3`
  were all filed against. The document now says where a manager note goes; three nodes in a row found the
  manager putting one somewhere else.
- *"`- [x]` is the human having dealt with the flag, which is not the same as having agreed with it"* —
  [Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md), settled by
  precedent at flag `22.4` and again at `27.2`. Condition 5 did not list it among its five items, so the
  checker had no way to trace it. It is a real decision, correctly carried.
- `### Review` opening *"after the code was written"* rather than *"after the code landed"* — flag `26.3`,
  which the worker had already filed itself.

**Run 1 carried three questions**, not findings. All three were real and none of them failed the
condition, because all three are gaps in what the condition and the deltas themselves say rather than in
the work. They went to the human at the gate, which is where a checker's question is designed to arrive.

### Correction round 1

The human's reply, `verbatim`:

> 1. ok 2. It does seem weird as the flags are not the only conculsion ? 3. fix .

Their `1.`, `2.` and `3.` are the checker's three questions in the order the manager put them at the gate.
**No flag was settled in this reply and no gate outcome was given** — the corrections change the work, so
the gate is raised again after the re-check.

**1 — `ok`.** An assent to the option quoted beside the question, which the **manager** wrote and the human
did not: where a node has no `## Interview` attempt and no `## Review` round — a `research` node, an AFK
`precondition` node — the `## Flags` entry itself carries the full account of what produced the flag,
instead of the one-line summary that suffices when a round holds the account. The gap was in the seventh
delta's own wording (*"the round that created it"*), and this closes it.

**2 — the human's own reasoning, not an assent.** *"the flags are not the only conculsion"*: the closing
report has more in it than flags, so `graph-conventions.md:50` saying the report **is** this file's
unchecked lines is wrong about the report rather than loose about the file. Narrowed to say what `flags.md`
supplies — the report's outstanding-flags part. Lines 66 and 301 already said the weaker *"built from it"*
and *"carries"*, so line 50 was the outlier and is the only sentence that moves.

**3 — `fix`.** Puts [`CONTEXT.md`](../../../CONTEXT.md) into scope as a **fourth product file**. Its
*Acceptance condition* and *Flag* entries still say the worker flags a wrong condition, where delta 5 makes
the worker **raise** and the manager file `CONDITION-WRONG`. `graph-conventions.md:5` declares the glossary
authoritative for the terms, so the shipped document was pointing at a file that disagreed with it.

**This is the same failure a third time, and it is the one thing this node has found that is bigger than
itself.** The delta list tracked one file; this node's condition named three; the checker found a fourth.
Nothing in the design lists the product files that must move together when a decision changes a term —
which is what [map.md](../map.md)'s own note about the ninth delta already said in miniature (*"a delta list
works until a delta lands on a file the list does not track"*) without drawing the general conclusion.

One thing the manager put to the worker to judge rather than deciding for it: `CONTEXT.md`'s *Flag* entry
reads *"A note a worker leaves"*, which is stale for a second reason nobody has recorded — **four flags in
this graph were filed by the manager**, not by a worker (`17.4`, `25.4`, `27.3`, `26.4`). Whether that is
inside the human's word `fix` or beyond it was left to the worker, with an instruction to flag it if taken.

**What the worker changed**, in its own report: the flag-production rule gained the no-round clause written
*into* the rule rather than beside it; `graph-conventions.md:50` was narrowed to say the closing report's
outstanding flags are this file's unchecked lines rather than that the report is them, with lines 66 and 301
left alone because they were already right; and `CONTEXT.md`'s **Acceptance condition** and **Flag** entries
were brought into line with delta 5, written *"in the glossary's own plain style — no inner bold, no quoted
speech, both properties of that file rather than of this one"*. It took the manager's `## Flags` point and
flagged it (`26.5`), and went one sentence further and flagged that too (`26.6`).

It reported the round's own contract duty precisely and unprompted: this round **touched what the acceptance
condition names, twice over** — both `graph-conventions.md` edits fall inside condition 5's territory, and
condition 6 names `CONTEXT.md`'s `_Avoid_` lines as part of the bar, so *"the file the bar is partly read
from is now also a file this node edits"*. It also named the three graph files showing as modified in the
tree as the manager's own writes rather than leaving them to be found. **On the first attempt, at both
rounds, no worker on this node has written a graph file or left a path to be discovered in `git status`.**

Round 1 changed nothing the checker had found, because the checker had found nothing. Everything in it came
from the three questions it handed up — which is the first time in this effort a **question** rather than a
finding has driven a correction round, and the first time one has grown a node's scope by a whole file.

**Run 2 — `PASS`.** Re-check after correction round 1, run by the same checker so it re-established nothing
it already held. The bar re-run in full; conditions 1 and 5 re-checked on the parts the change reaches;
conditions 2 and 3 not reached, with 3's *"the other four contracts are unchanged"* re-verified cheaply
anyway.

Three things in it are worth more than the outcome.

**It refused to take the manager's statement of what changed as evidence, and its own contract told it to.**
Handed *"three things changed"*, it established the change independently: modification times placed against
the previous outcome, then the current `git diff` compared hunk by hunk against the run-1 diff it still
held — *"the `flags.md` hunk has identical line counts with only the one sentence's text differing, the
`Raise a flag` hunk grew by exactly one line, the check-6 hunk differs only in offset with byte-identical
text, and every other hunk is byte-identical."* First time that clause has been exercised, and it confirmed
the manager rather than catching it.

**It dissolved the circularity by measurement rather than by argument.** The manager had flagged that
`CONTEXT.md` was now both part of the bar and part of the work, so the file might license its own edit. Its
answer: the standard that file supplies is its `_Avoid_` lines, **all forty are byte-identical after the
edit**, the diff touching only two entries' prose — so the new text was held against an unmoved standard and
the file could not license itself. That is a better resolution than the flag that raised it.

**Its condition-4 residue was one clause, and the manager could close it.** See the questions below.

### The three questions from run 2

**Two the manager answered and handed back closed**, both of them things the checker could not have reached:

- *"usually a worker's, and the manager's where a judgement of its own reached the graph"* in the glossary's
  *Flag* entry — the checker could see only `CONDITION-WRONG`, where the manager files a **worker's**
  judgement, so the evidence available to it pointed the other way. It traces: **five flags in this graph
  were filed by the manager and every one records the manager's own judgement** — `17.4`, `25.4`, `27.3`,
  `26.4`, `26.7`. `CONDITION-WRONG` is the single exception. Its reasoning was sound on what it had.
- The glossary's closing-report clause looking narrower than the document's — it is not. The worker chose
  *"where that moment never came"* deliberately to cover both a node with no human moment and a flag raised
  before the practice existed. **The reason was in the record and withheld from it**, which is the cost of
  blindness landing on a non-issue.

**One went to the human**, as flag `26.8` below: `raise` carries two senses and the glossary now holds both
in adjacent entries.

### The flag validity pass — a declared extension of the checker's contract

Run at the human's instruction, given at this gate: *"could we give a summarized version of the flags, with
explict instruction to check if they are valid… only giving what was done and not the reason ?"*

Run **after** run 2's outcome was already given, so nothing it concluded could reach the verdict, and
declared to the checker as a fifth thing beyond the four its contract lists rather than slipped past it.
Five of the seven flags were put to it, stripped to what was done, with the instruction to judge only
whether each is **true of the work** and explicitly not whether the call was right.

**All five came back true.** It read the `flags.md` form through `cat -A` so no hidden markup could pass,
and it declined to treat the node-side example — which backticks the id where the `flags.md` form does not —
as a counterexample, on the ground that the claim was scoped to one of the two. **Cost: 51 seconds and one
tool call**, against roughly four minutes for a check run.

Three findings about the mechanism itself, recorded on [Whether a flag is checked before the
human settles it](30-checking-a-flag-before-the-human.md):

1. **Two of the seven were withheld because they make no claim about the work** — `26.4` records how the
   manager assembled a spawn and `26.7` how the node's scope was set. Nothing in the working tree could make
   either true or false. A flag-checking step covers *some* flags and the design has to say which.
2. **Withholding the reason cost a question on the first outing** — the closing-report non-issue above is
   exactly the failure mode *only what was done, not the reason* invites. One of two run-2 questions.
3. **Ordering did what argument could not.** Running the pass after the outcome makes the contamination
   objection vanish with no rule needed.

### The human's instruction on how a flag is put to them, `verbatim`

> Also for flags, when asking the user, please explain in more detail what was done and why and the context.
> Idealy I don't have to go into the files to find out what happened and how to respond

Given at this gate, after the manager had put eight flags to them as eight one-line labels and a file path.
**A binding requirement on the gate payload, and the manager was failing it.** A flag's line in
[flags.md](../flags.md) is capped at one sentence by [Graph file format](13-graph-file-format.md) and its
node entry is written for a reader who already has the node open; neither is a payload. Relaying either as
though it were makes the human open files to find out what they are answering.

Annotated onto [Human review of landed code](20-human-code-review.md), which fixed what the gate payload
contains and did not cover this.

**It creates a symmetry with the flag validity pass run minutes earlier, and the two point opposite ways.**
For the **checker**, a flag is stripped to what was done and the reason is withheld — so it checks the claim
rather than accepting the justification. For the **human**, the same flag is expanded with what was done,
why, and the context — so they can settle it without opening anything. One flag, two audiences, inverse
payloads, and the manager writes both. Recorded on [Whether a flag is checked before the human settles
it](30-checking-a-flag-before-the-human.md), since a design that only ever described one of the two would
have collided with the other.

### Flags `26.1`–`26.7` settled at the gate; `26.8` overruled

The human's reply, `verbatim`:

> For a bit more context, I expect the nodes to be mostly targeted to agents, as I will mostly work from what
> the manager says (questions from subagents) and with code review. 26.1 ok 26.2 ok 26.3 ok 26.4 it's fine
> 26.5 ok 26.6 ok 26.7 I don't really remember what happened but if CONTEXT was changed, even if it wasn't in
> the acceptance condition, the checker should check it ? no ? 26.8 We can say that raise is a subagent asking
> something to the human ? Doesn't matter if it waits or continues ? .
> For the flags information in the chat, it is much better

Given after the manager re-presented all eight flags with what was done, why, and the context — the format
that same reply confirms as *"much better"*. **The opening sentence is not about this node at all** and is
recorded as a standing preference on [map.md](../map.md): the node files are written for agents, and the
human's two interfaces are the manager's chat and code review.

`26.1`, `26.2`, `26.3`, `26.5` and `26.6` settled as `ok`. `26.4` settled as *"it's fine"*.

**`26.7` was not settled by assent but by a question**, and the manager answered it rather than re-asking:
*"if CONTEXT was changed, even if it wasn't in the acceptance condition, the checker should check it ? no ?"*
**It did check it** — against the bar, including that file's own `_Avoid_` lines, and against condition 4,
which is where it resolved the circularity by measurement. What no checker could do was hold it against a
statement of **intent**, because none existed. The bar catches quality; only a condition catches purpose. So
the answer to the question is *yes, and it did* — and the gap `26.7` recorded is narrower than it read: not
*the checker did not check* but *nothing said what the change was for*. **The rule that follows: a scope
extension arrives with its own acceptance condition rather than as a bare instruction.** Written by the
manager and tested within the hour, since `26.8`'s answer extended the scope again and became condition 7.

Also recorded, because it is the manager's failure and not the human's: *"I don't really remember what
happened"*. The manager's presentation of `26.7` opened with *"Done: nothing. This records a gap"* and never
restated **what had been changed in `CONTEXT.md`** — the thing the flag was about. A flag that records the
absence of a condition still has to say what the condition would have covered.

**`26.8` was overruled, by a third option the manager had not offered.** It had recommended shipping the
two-sense `raise` unresolved, having framed the choice as *document the collision* versus *rename the
procedure*. The human's answer was neither: generalise the word. *"We can say that raise is a subagent asking
something to the human ? Doesn't matter if it waits or continues ?"* — which turned out to be a **repair**
rather than a redefinition, because the design already used the general sense and already carried the
qualifier where it needed one. Two legs of that, both verified on disk before anything was written: node 23's
decision line reads *"three triggers open a **blocking** raise"*, an adjective only necessary if the bare word
is broader; and `expedition-checker/SKILL.md`'s `QUESTIONS:` block already shipped a non-blocking channel
saying *"You do not wait for an answer, and your outcome never depends on one."*

One word of the human's was not taken and the divergence is recorded: they wrote *"a subagent asking
something to the human"*, and the entry says **an agent**, because the manager also puts things to the human
and five flags in this graph are its own. Their round-1 instruction had already produced *an agent* in the
adjacent *Flag* entry, so the narrower word would have made the two entries disagree.

### Correction round 2

Three edits, all inside condition 7, and `graph-conventions.md` was **not** touched. `CONTEXT.md`'s *Raise*
entry generalised, with the old entry's whole machinery kept as the blocking kind's; its `_Avoid_` clause on
`ask` re-grounded (flag `26.9`); and `expedition-implementation/SKILL.md:36` and
`expedition-checker/SKILL.md:26` rewritten as each channel's specialisation — each naming the bare-word
shorthand its own body already uses, so the widened sense is not left ambiguous against it.

**Two contracts entered scope that had been verified unchanged twice**, which is why condition 3's second
sentence had to shrink rather than be re-read: a checker that had established *"the other four contracts are
unchanged"* in runs 1 and 2 would otherwise have failed the work on its own earlier finding.

**`### Raise a flag` and *at raise time* in `graph-conventions.md` needed no edit**, and that is the whole
reason this was cheap. Under the old entry those phrases sat in mild conflict with *raise = stops work*; under
the general sense they are simply correct. The generalisation improved that document's coherence without
touching it — the opposite of the rename, which would have reached [flags.md](../flags.md) and been out of an
implementation worker's reach.

`expedition-research` contains the word nowhere; `expedition-precondition` uses it twice as an ordinary verb
and defines nothing. Both checked, both unchanged.

**Run 3 — `PASS`.** Three things in it go beyond the outcome, and the third is the sharpest piece of work any
agent has done on this node.

**It verified the round's central claim instead of accepting it.** Told that both contracts already use bare
`raise` as shorthand for their blocking channel, it enumerated every occurrence — implementation at L66, 86,
96, 109, 149, 164, 182; checker at L44, 93, 97–98, 138, 140, 144, 157 — and confirmed the word *outlets* was
that file's own pre-existing term rather than a new synonym. It then grepped `**raise**` across all six
contracts to establish that **no competing definition survives anywhere**.

**It judged an edit to its own contract and found the old text was already broken.** Told plainly that
`expedition-checker/SKILL.md:26` had been rewritten under it, that the disk version binds it, and that finding
the new text incoherent would be a `FAIL` it should state plainly: *"Nothing here made my contract incoherent
or unfollowable, and being its subject changed nothing about how I checked it."* And it went further —
the **old** definition, *"bringing something to the human that stops work until they act"*, was already at
odds with its own L135–136, *"You do not wait for an answer, and your outcome never depends on one."* So it
confirmed the second leg of the widening's justification **from its own file**, while explicitly declining the
node-23 leg as record it may not read. It found the contract it had been running under was self-contradictory
before this node touched it.

**It resolved the circularity by finding the right thing to measure, and named what would have changed its
answer.** The manager had offered a framing and permission to raise. It did neither, and instead measured what
actually matters: `CONTEXT.md` carries forty `_Avoid_` lines before the work and forty after; thirty-nine are
byte-identical and one differs **only in its ground clause**; and the *refused set* — `{escalate, interrupt,
ask}` — is identical on both sides. **So the operative content of the standard never moved. Only the reason
given for one refusal did.** That left an unmoved standard to hold the work against, and it held the round's
added lines against it. Then the part that makes it a method rather than a lucky escape:

> What would have changed that: had the edit added or removed a refused word, the operative standard itself
> would have moved and I would have had nothing unmoved to check the rest of the work against — that I would
> have raised rather than resolved.

**That is the general answer to *can a check survive the work editing its own standard*, and it was produced
by the blindest party in the system, unprompted.** A standard has operative content and a rationale; moving
the rationale leaves the check intact, moving the operative content destroys it. Nothing in the design said
this and nothing had asked for it.

**One flag needed no separate validity pass.** `26.9`'s claim — that the `_Avoid_` clause was re-grounded and
nothing else about it moved — was established inside run 3's own bar measurement, before any flag was put to
it. **A check can already cover a flag's claim as a by-product of checking the bar**, which is a fourth
finding for [Whether a flag is checked before the human settles it](30-checking-a-flag-before-the-human.md):
the flag pass is sometimes redundant, and whether it is depends on which condition the flag's claim happens to
sit under.

### Correction round 3

The human's reply, `verbatim`:

> for the one thing to decide, fix it 26.9 ask is when a worker is designed to ask question to the user, raise
> is when the worker is supposed to work mostly by itself but it needs input from the user

Two items, and **both correct the manager rather than the worker.** No new flags.

**Item 1 — `fix it`**, an assent to the option the manager quoted beside it, which the manager wrote and the
human did not: *"a flag waits for the gate"* becomes *"waits for the human moment that ends its node — a
grilling node's last answer, an implementation node's gate."* The struck wording was condition 7's own, so
**the condition was amended before the work changed** — a worker may not depart from its condition, and the
checker had correctly declined to fail on a clause it could see was the condition's rather than the work's.
The replacement is `graph-conventions.md`'s existing phrase and the *Flag* entry's, not a third coinage: one
wording, three places.

**Item 2 — the human replaced the worker's ground for refusing `ask`**, settling `26.9`. See that flag for the
distinction between the two grounds and for the manager's note that the human's reduces to [Node type
taxonomy](07-node-type-taxonomy.md)'s HITL/AFK split.

**One judgement the worker made and deliberately did not act on**, recorded in its handover rather than
flagged, since it changed nothing. Asked whether the general sense's first line over-reaches — *an agent
putting something to the human*, read literally, includes a grilling worker's interview turn, which the
`_Avoid_` clause then excludes — it **left the sentence broad**, and it checked its reasoning against the file
rather than asserting it: the `_Avoid_` line is this glossary's own mechanism for word boundaries, and **no
other entry pre-empts its own `_Avoid_` line inside its definition** — *Node* refuses `issue` and `ticket`
there, *Reject* refuses `abandon` there, *Promote* refuses `postpone` there. So narrowing the first line would
have been the anomaly, not the fix. Its second reason is that the entry's own second sentence enumerates the
three channels the word covers and an interview turn is not among them, so the scope is signalled before the
`_Avoid_` line is reached. Its third is that narrowing in the same pass that widened it would work against the
instruction that produced it.

**Three correction rounds, and two of the three fixed the manager's text rather than the worker's.** Condition
7 was amended twice — once for naming an *Ask* entry that does not exist, once for a clause true only of
implementation nodes — and it is the first acceptance condition in this effort written by the **manager**
rather than by a spawning node or its worker. Both defects were found downstream: one by the worker reading
the entry it was told not to contradict, one by the blind checker holding two glossary entries against each
other.

**Run 4 — `PASS`, and no questions.** The first run on this node to carry none; both of run 3's are closed by
the work rather than argued away.

**It defeated the reflow rather than trusting the statement about it.** Told the entry had been rewrapped, it
reconstructed the run-3 *Raise* body verbatim from the diff it had read the round before, unwrapped both, and
word-diffed them — establishing that *the entire change is the insertion of one phrase* and that every other
word is identical. It also unwrapped the files before grepping to confirm the shared wording, noting that
**a plain line-based grep misses both phrases because they wrap** — which is the same class of false negative
[map.md](../map.md)'s fog item on extracting a graph tool has been collecting for five sessions.

**It applied its own run-3 test instead of inheriting its own conclusion.** Counted the `_Avoid_` lines itself
— forty at `HEAD`, forty now — found exactly one differing line, the same one, and compared its refused list
against the run-3 baseline: `escalate, interrupt, ask`, identical. *"My raise condition is therefore not
tripped."* The instrument it built one round earlier, used on the recurrence it was built for.

**And it converged, blind, on the manager's note about the human's ground.** Independently of anything it was
told, it found that the new ground *"grounds the refusal on the AFK/HITL distinction the same file already
defines"*, quoting that entry, and judged it **firmer than either ground it replaced, since it does not depend
on whether the channel waits.** The manager had recorded the same reduction on flag `26.9` from the taxonomy
side; the checker reached it from inside the glossary with no access to the record. Two parties, opposite
directions, same answer.

**It re-checked a sentence the amendment reached without being asked to.** Condition 7's second sentence: the
implementation contract still ends *"a flag waits for the gate"*, unchanged — and under the amended general
sense that is now *exactly* a specialisation rather than a competing claim, since the glossary names both
kinds' moments and that contract addresses only implementation workers. The checker contract names no flag,
so the amendment does not reach it.

**And it declined the one thing offered to it that was not its business** — the worker's judgement to leave
the general sense broad, and its supporting claims about *Node*, *Reject* and *Promote*: *"outside my
condition. I neither verified nor formed a finding on them."* The manager had said as much when handing it
over; the value is that it said so back.

### Gate outcome: **approve**

The human's words, `verbatim`:

> You can commit, do you also want to do something also with the "What the checker did that I'd want kept"

Committed as **`0cec4e7`**, path-limited to the six product files, carrying the trailer `Node:
graph-workflow/26`, not pushed. The graph's own files follow in a separate prose-bodied commit, as at
[Write the graph conventions document](21-conventions-document.md) and [Write the worker contract
skills](22-worker-contract-skills.md).

The second clause is not about this node's work and is answered beyond it: what the checker built over four
runs became [What the checker contract owes to having been
run](31-checker-contract-owes.md), and one finding of its own went to
[map.md](../map.md)'s fog item on extracting a graph tool. **This is the first time an approval at a gate has
also created a node** — the human reading the payload found something in it that the payload's own author had
recorded as admiration rather than as work.

### The whole node, counted

Four checker runs, all `PASS`, the last with no questions. Three correction rounds, of which **two fixed the
manager's text and one the human's own earlier wording** — none fixed a checker finding, because there never
was one. Nine flags, all settled at this gate. Six product files, from a condition that named three. Two nodes
minted while it ran and a third at its approval.

**Nothing in this node was ever sent back by a check.** Every change after round 0 came from a checker
*question* or from the human, which is a different machine than the one the design was built around: the
`FAIL` path was never used, and the `QUESTIONS:` channel — added at [Write the worker contract
skills](22-worker-contract-skills.md) as a courtesy for a method skill wanting to ask something — carried the
entire correction history of the largest implementation node this effort has run.
