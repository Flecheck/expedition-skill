# Carry node 82's widening rule into the two shipped files that state the old one

Type: implementation
Status: resolved

*Landed at commit `b095bb6`. Rebased from `7aa89cb` onto `8933f1d` with no conflict; `git merge --ff-only`, worktree
removal and branch deletion all run with the sandbox off in one pass, per the finding at [node
277](277-the-removal-step-of-the-worktree-route-does-not-work-as-written.md) — **no `EBUSY` and no stale entry.***

Blocked by: ~~58~~ **none — [node 58](58-qualify-the-graph-file-ban.md) resolved and the edge is satisfied.**

## Question

*Reported by [How a condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s worker in
its `INVALIDATIONS`, and pasted as it wrote it. Whether it became one node or rode an existing one was left to the
manager; this is that node.*

> Two shipped statements go stale with it, and both are downstream of that node rather than resolved nodes of their
> own: `graph-conventions.md`'s `### Acceptance condition` — *"its worker may not rewrite it"*, with no word on who
> may widen its scope — and `.claude/skills/expedition/SKILL.md`'s `## Acceptance conditions`, *"Where a node was
> minted by an agent, that agent wrote the condition and you file it"*, which now needs the widening carve-out and
> guard 1's re-derivation. Reported here because nothing else reports them; whether they become one implementation
> node or ride an existing one is the manager's.

**Why it is blocked by [node 58](58-qualify-the-graph-file-ban.md).** Both files are in node 58's own change and its
work is uncommitted at a gate. Claiming this before that lands would put two workers in the same two files.

## The amendment of 2026-09-19, and the human's direction that produced it

***Filed by the manager. The amendment above is the manager's own text and is marked as such at each clause,
distinguished from the minting author's.***

**The human's words**, `verbatim`, answering the manager's raise on where the acceptance-condition rule ships:

> ok

**The option it takes**, quoted so the reply is attributable to exactly one thing — the manager's own
`RECOMMENDED`, there being one assent among four options and three named refusals of it:

> On node 95, and I amend its condition first under the rule you granted — all three shortfalls in one pass, each
> citing what fixes it. Its condition already names the right two files and the right sentence; a new node would
> duplicate that scope and leave node 95 still short.

**Stated against [node 252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s own test, so a reader
can check it rather than take it.** The node is open and unclaimed. The pen is the manager's by the fallback limb —
nodes 252's and 263's workers have both finished. Every word of clauses 1, 2 and 2b is fixed by a resolved node,
and each amendment names which. Node 82's guard 2 is met: recorded on the node beside what justified it, marked as
the manager's, distinguished from the minting author's text, carried as flag `95.1`, and named in the report that
goes with this.

**Two of the three shortfalls this was supposed to close are closed. The third is not, and it is not amendable.**

- **Node 94's finding is NOT amended here.** It measured that this condition's scope names two files while the
  sentence it must repair sits verbatim in **five worker contracts**. Widening the scope to those five is licensed
  cleanly by [node 82](82-amending-a-condition-whose-scope-was-too-narrow.md) — *"adds places and no demand"* — but
  **node 82's guard 1 requires the manager to re-run the search that produced the list**, and the manager has not
  run it. Amending on node 94's count without re-deriving it would be the exact failure node 82's guard exists to
  prevent, and the manager asserted an unverified count once already today (`263.4`). **It stays short until that
  search is run**, and running it is the manager's.
- **Where the trigger in 2b belongs is a second, separate question and is NOT settled here.** Node 263's worker
  observed that [node 43](43-widen-the-invalidation-channel.md) already rewords the `INVALIDATIONS` line in those
  same five worker contracts, *"beside"* which this duty attaches. Whether 2b's duty also belongs in the five
  contracts, or only in the two files this condition names, **is fixed by nothing** — no resolved node states it.
  Under node 252's own test that part is not amendable and goes to the human. **Named for them rather than
  guessed.**

**This is the second exercise of node 252's rule and the first on a node the manager did not itself just park.**

## Attempts

*The manager's record. A claim belongs to the node rather than to the agent holding it, so the node stayed claimed
across the deaths below.*

- **Attempt 1 — died twice and wrote nothing.** Spawned 2026-09-19 into
  `.scratch/graph-workflow/worktrees/95-widening-rule-into-shipped-files` on `7aa89cb`, the first worktree this node
  ever had and one made by the plain-git route. **Terminated first by an API session limit**, its last words being
  *"Now node 82, the map files, and the two deliverables"* — it had finished its first reads and had not begun
  writing. Resumed in place; **then stopped a second time with no completion record at all**, which the harness
  reports as either an external stop or the process exiting under it. **Neither death was about the work.** The
  worktree was verified clean after both: `git status --porcelain` empty, `HEAD` still `7aa89cb`, nothing to undo
  and nothing lost.
- **Attempt 2 — spawned 2026-09-20** into the same clean worktree.

**What the two deaths cost is one thing worth recording**: this node has been claimed across two sessions and has
produced nothing, while its own condition is the one the manager amended under node 252's rule and the one the human
chose as the carrier. **It is not stalled on a judgement; it is stalled on the harness.** **Attempt 2 finished the
node.**

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> Both files now state who may change an acceptance condition after it is written, and the duty that fires it.
> Nothing was removed, reworded or renumbered: the change is 95 added lines across two sections, and `git diff` shows
> **zero deletions**.
>
> **`graph-conventions.md`'s `### Acceptance condition`** gains four paragraphs at the end of the subsection: the
> **four parties** (the condition's own worker, unchanged; the party that established a falsifying fact, which
> writes the replacement as text on its handover for the manager to file, under two provisos — every word already
> fixed by a resolved node, by landed work, by the glossary or by the shipped files, and the amendment names which;
> the manager, holding that same pen where no such party exists and separately holding node 82's scope extension;
> and the human for everything else); a paragraph saying **an amendment is a transcription and never an
> authorship**; the **three things no amendment reaches**, stated as properties, with exclusion 2 carrying node 252's
> qualification; and the **duty to search** before handing back.
>
> **`SKILL.md`'s `## Acceptance conditions`** gains one `###` subsection, *Changing one after it is written*, stating
> the same rule as the manager's own duties: what it files and what it refuses, the two provisos, its fallback pen,
> the scope extension, the three limits, an explicit *amending is never authoring*, the duty to re-derive an
> enumerated scope before the claim, the five things that accompany an amendment, and the search duty with its
> *where no such party exists, the search is yours*.
>
> **Placement, and why it is at the end of each section rather than beside the sentence it repairs.** In
> `graph-conventions.md` the five paragraphs on self-containment are one continuous argument and the opening
> paragraph is the one that says who may not rewrite a condition; inserting between them would split the argument.
> In `SKILL.md` it is a new final subsection rather than items appended to `### The four constraints on a condition
> you write yourself` — **appending there would have renumbered a list of node 39's whose heading states its own
> count, which is the failure clause 8 exists to prevent.**
>
> **Three calls a later reader would otherwise re-derive.**
>
> 1. **Node 252's unclaimed-only boundary is stated explicitly in both files, and no clause of the condition names
>    it.** Without it the new text reads as a flat contradiction of the manager contract's `What is never yours` row
>    *"rewriting an acceptance condition | hand it over as written; a condition that is wrong goes to the human"* —
>    a row clause 8 forbids touching. With it, the row is the claimed case and the new pen is the unclaimed one.
> 2. **Clause 5 says an amendment is *"marked as the manager's own"*; the text says *"marked as its author's own — as
>    yours where you wrote it"*.** Clause 5 transcribes node 82's guard 2, written when the manager was the only
>    amender. Clause 1 now admits a second amender, so writing clause 5 literally would have made a falsifying
>    party's amendment marked as the manager's, which is false. The manager's case is stated explicitly inside the
>    wider form, so clause 5 is met as a special case rather than departed from.
> 3. **Clause 5's *"beside the search that justified it"* is written as *"beside the search or the fact that
>    justified it"*.** Node 82's pen is fired by a search and node 252's by a fact; the search is not dropped, a
>    place is added.
>
> **The five worker contracts were not edited**, node 94's finding being outside this condition's scope, and **the
> count was re-derived rather than trusted**: `grep -rn "not that worker's to fix" .claude/` returns that sentence in
> exactly the five worker contracts and nowhere else. **Node 94's reading of it is narrower than node 94 states**,
> and that matters to whoever widens it: the sentence says *"A condition its worker judges wrong is not that
> worker's to fix: it stops that node and goes to the human"*, and node 252 leaves the mid-node case exactly there.
> What node 82 falsified is only the **scope** case. So the repair owed in those five files is *"a raise about a
> short scope the manager may answer itself"*, not the whole four-party distinction.
>
> **The node-263 duty was run. The handles searched**, over the `## Acceptance condition` section of every `open` or
> `claimed` node — **83 nodes, 2,538 lines**: the paths `graph-conventions.md` and `expedition/SKILL.md`; the section
> names `### Acceptance condition` and `## Acceptance conditions`; the phrases *"may not rewrite"*, *"minted by an
> agent"*, *"not that worker's to fix"*, *"self-contained"*, *"four constraints"*. **No breakage found. Four
> sequencing facts found**, each reported rather than acted on: **node 43's clause 3 quotes verbatim a sentence that
> sits inside this node's own deliverable section**, which is why that sentence was left byte-for-byte; node 109's
> clause 5 requires the same two sections to carry its extent rule and its clause 7 forbids changing anything else;
> node 55's clause 5 requires the worker-may-not-rewrite rule to survive in that subsection, and it does; node 79's
> clause 8 requires `graph-conventions.md`'s heading list to be unchanged and in order, verified by diffing the two
> heading lists.

**The index line the worker wrote**, held here until the node resolves:

> The two shipped files state who may change a condition after it is written — four parties, three limits, the
> re-derivation duty and the duty to search the open conditions.

**On the condition's quality, since its provenance invited the question** — *the worker's own words, and the manager
is filing them unedited:*

> It is a good condition. It is self-contained, every clause is decidable from the diff, and **clause 8 is the clause
> that did the most work** — it stopped me editing the `What is never yours` row and open question 5, both of which I
> wanted to fix and neither of which was mine. **Where the manager's authorship shows is not in the amended clauses
> but in the unamended one**: clause 5 transcribes node 82's guard 2 and was left alone while clauses 1 and 2, which
> transcribe the same node, were repaired — **so the condition contains two statements of one rule at two different
> dates.** That cost two flags and no more.

## Flags

`95.2` `ASSUMPTION` — *The worker's own text, pasted.* **Wrote clause 5's marking requirement in a wider form than
clause 5 states.** Clause 5 demands the section say an amendment is *"marked as the manager's own"*. Clause 1, as
amended, admits an amender who is not the manager, so the literal wording would require a falsifying party's
amendment to be marked as the manager's, which is false and would collide with clause 1 in the same section. I wrote
*"marked as its author's own — as yours where you wrote it"*, which states the manager's case explicitly and covers
the wider one, and which is node 252's own restatement of node 82's guard 2. Not raised, because the condition is
satisfiable as written by the wider form and the narrower one is contained in it.

`95.3` `ASSUMPTION` — *The worker's own text, pasted.* **Added node 252's unclaimed-only boundary to both files,
which no clause names.** The new text opens in each file by saying it reaches a node nobody holds yet and that a
condition under a live worker goes to the human by the raise and no other route. No clause asks for it; node 252's
answer fixes it, and without it the new material reads as contradicting the manager contract's `What is never yours`
row on rewriting a condition, which clause 8 forbids me to touch.

`95.4` `ASSUMPTION` — *The worker's own text, pasted.* **Read clause 5's *"beside the search that justified it"* as
adding a place rather than fixing one.** Written as *"beside the search or the fact that justified it"*, node 82's
pen being fired by a search and node 252's by a fact.

`95.5` `MANAGER-WRONG` — ***Filed by the manager against itself, and the worker's diagnosis is the repair.*** **When
the manager amended clauses 1 and 2 of this condition under node 252's rule, it did not sweep clause 5, which
transcribes the same source — node 82's guard 2 — and which the amendment of clause 1 falsified.** The condition
therefore shipped to its worker carrying **two statements of one rule at two different dates**, and the worker paid
two flags to reconcile them. The manager also recorded at the time that it had closed *"two of the three
shortfalls"*; it had in fact opened a fourth. **The worker's generalisable form, and it is what the manager will
carry forward:** *"an amendment that repairs one clause should say whether it checked the clauses that transcribe
the same source."*

`95.6` `MANAGER-WRONG` — ***Filed by the manager against itself.*** The spawn asserted that **nineteen** open nodes
edit `graph-conventions.md`. The worker measured **27** whose `## Acceptance condition` names that path. **The two
numbers do not measure the same thing** — the manager's came from node 264's worker counting nodes that edit the
file, the worker's from counting conditions that name it — but **the manager passed a number on as a fact of its own
without saying whose measurement it was or that it was unverified**, which is the second time in three days it has
relayed an unre-derived count. The worker tested it only because the spawn's closing note told it to test anything
shaped like an assertion about its answer. **That note is why two of this node's three findings exist**, and it is
recorded here as the thing that worked rather than only the thing that failed.

## Invalidations

*The worker's own text, pasted.*

> **No resolved node is contradicted by this work.** It ships nodes 82, 252 and 263 into the two files and takes
> nothing else.
>
> **[Node 94](94-condition-scope-as-a-predicate.md)'s annotation on node 95 is narrowed by a node that resolved
> after it.** Its words: the five-contract sentence *"states the worker's half of exactly the three-party
> distinction node 95's clauses 1 and 2 exist to write, and node 82 falsified its routing"*. The first limb is now
> too wide: node 252, resolved after node 94, confines its pen to **unclaimed** nodes and states *"The claimed case,
> unchanged … A worker meeting a broken condition mid-node raises."* That sentence sits in a worker's contract and
> speaks to a worker holding the node, so for the case it describes it is correct and node 95's four-party rule does
> not reach it. **The second limb stands**: a raise whose content is a short scope is answerable by the manager
> under node 82 without a human turn. Reported here because the annotation is the standing instruction to whoever
> runs the manager's guard-1 search.
>
> **Untouched, stated so they are not read as moved.** Node 39 — the prohibition on the manager authoring a
> condition for an agent-minted node is stated explicitly in both files by this work and is not weakened. Node 199 —
> the mechanics of a superseded clause are not mentioned by either addition. Node 43 — its clause 3's quoted
> sentence sits inside this work's own deliverable section and was left byte-for-byte. Node 33 and node 36 —
> self-containment and the record-quantification ban are untouched.

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.** Almost nothing, and the spawn is why: it named node 252's and node 263's `## Answer`
> sections as the authority and they were. The one thing I had to find myself was **where node 43's clause 3
> points**, which turned out to be a sentence inside my own deliverable section — **found by running node 263's
> duty, not by reading node 43, and it is the single most useful thing the duty returned.** I also had to derive the
> boundary between my new text and the `What is never yours` table row, which nothing in the record states.
>
> **2. What arrived in my context that this node did not need.** *From `map.md`:* I acted on four of ~25 `## Notes`
> items. **At least the eighth report; node 246 holds it.** Worse, **`map.md`'s worktree paragraph still names
> `EnterWorktree` as the settled route while my spawn told me that route was dropped** — so the file I was told to
> read whole contradicted my spawn on a point I had to act on. Node 268 holds it. *From
> `map-implementation-rules.md`:* the review-route paragraph is the checker's and I acted on none of it — **the fifth
> report.** *Whole files taken for one fact:* node 252 (511 lines) and node 263 (491 lines) both paid in full and
> are the node's real input. Node 82 paid for two paragraphs. `map.md` did not pay.
>
> **3. What would have made this node easier.** *In the spawn:* nothing material — it named the authorities, warned
> about the exact trap I hit (clause 6), and told me not to grep `decisions.md` for `worktree`, which saved a read.
> **Its one measurable error was in my favour:** it said *"nineteen open nodes edit `graph-conventions.md`"*; the
> number whose `## Acceptance condition` names that path is **27**. I tested it because the spawn's own closing note
> told me to test anything shaped like an assertion about my answer, **and that note is the reason two of my three
> findings exist. That correction mechanism works and is worth keeping.** *In the node file:* the condition's
> amendment section is excellent about what it does **not** amend, and silent about what clause 5 inherits from a
> pre-252 world. **The generalisable form: an amendment that repairs one clause should say whether it checked the
> clauses that transcribe the same source.** *In the record:* there is still no index of which shipped sentence
> belongs to which open node; node 43's claim on a sentence inside my section was findable only by running node
> 263's duty, **which is not what that duty is for.**
>
> **4. What I read that was stale, wrong, or contradicted something else.** `map.md`'s worktree paragraph names a
> route my spawn says was dropped — node 268. `map-implementation-rules.md` says `.gitignore` holds two patterns
> where it holds three — node 271. The spawn's *"nineteen open nodes"* is 27. Node 94's annotation on node 95 is
> wider than node 252 leaves it. **Node 95's own clause 5 is pre-node-252 text inside a post-node-252 condition.**

## The manager's disposal of the retrospective's record items

*Not the worker's text.*

- **Clause 5 left un-swept, and the count passed on unverified** → **flags `95.5` and `95.6`**, both the manager's,
  with the worker's generalisable form carried as the repair rather than only the correction.
- **The three nodes the worker surfaced** → **minted** as [node 278](278-the-never-yours-table-states-the-amendment-rule-as-absolute.md),
  [node 279](279-five-worker-contracts-route-a-scope-raise-to-the-human.md) and
  [node 280](280-open-question-5-and-the-search-duty-do-not-know-about-each-other.md), each carrying its author's
  own question and condition.
- **`map.md` contradicting the spawn on the worktree route** → **already repaired**: node 268 landed at `8933f1d`
  while this worker was running, so the file it read was one commit stale. **Nothing owed**, but it is the second
  time this session a worker has read a map that moved under it, and that is node 266's subject.
- **No index of which shipped sentence belongs to which open node** → **not minted, and it is the third report of
  this shape.** Node 43's claim on a sentence inside this work's own deliverable was findable only by running node
  263's duty — which, as the worker says, is not what that duty is for. **Named for the human.**
- **`map.md`'s `## Notes`, eighth report; the review-route paragraph, fifth report** → node 246 holds the first;
  the second is still unheld. **Named for the human, and the manager notes that naming it is now the fifth time.**

## Review

### Run 1 — `FAIL` on the acceptance condition; **the bar holds**

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text — **with the struck wording of clauses 1 and 2 shown and marked as not part of the standard** — the bar as
properties, the two changed paths and the tree holding them, the record-as-work rule, and this effort's ground rules
and four standing rules for writing copied as text. It was given nothing from this node or from the effort's record.
It was told clause 8 was where the work was and clause 5 the likeliest departure, and that `graph-conventions.md` is
itself a changed path so the standard is its text at the base commit.*

> **FAIL: acceptance condition**
>
> **How I reached the tree.** By absolute path and `git -C`; no harness tool, no `EnterWorktree`, sandbox left on. No
> read was refused. `git status --porcelain --untracked-files=all` returns exactly the two named paths.
>
> **Under the record rule:** I read the two changed paths as the work under check. Both are shipped files. **No node
> status line, no `decisions.md` line and no `flags.md` line appears among the work** — established from
> `--untracked-files=all` and from a scan of the added text for `Status:`, `decisions.md`, `flags.md`, `- [ ]`,
> `- [x]`, which returns zero hits.
>
> **`graph-conventions.md` is itself a changed path, so I settled what moved before checking anything.** The edit is
> **purely additive**: `git show 7aa89cb:<path> | diff - <path>` returns **0 base lines absent from current** in both
> files. So every pre-existing element of that standard is unmoved and binds.
>
> **1 — MET.** All four parties present with the amended clause's content, and the pre-existing *"its worker may not
> rewrite it"* is unmoved. **2 — MET**; I checked the one wording risk — the clause says *extension*, the file says
> *amendment* — and the file calls the extension an amendment in the bullet that grants it, so extension is inside
> the scope of the three limits. **2b — MET, both files**, carrying every element including *claimed or not* and the
> naming of handles on the handover. **3 — MET**; the new subsection is written in the second person as the
> manager's duties throughout. **4 — MET.** **5 — MET.** Two widenings, both stated rather than dropped and both
> forced by clause 1's four-party model — *"beside the search **or the fact** that justified it"*, and *"marked as
> its author's own — **as yours where you wrote it**"*. Each still states the case the clause demands. **This was the
> clause I was told was most likely departed from; it is the widening above and nothing more.** **6 — MET**; I
> grepped every occurrence of `author` in both files against the base — nothing new grants the manager authorship,
> and three statements refuse it. **7 — MET.** **9 — MET.**
>
> **8 — NOT MET.** The *removed or renumbered* half holds: zero deletion lines, and no base line absent from either
> file, so nothing was removed, reworded, rewrapped or renumbered. **The *changes its meaning* half does not hold —
> one instance.**
>
> **The finding — one instance.** `SKILL.md`, `## What is never yours`, the row:
>
> ```
> | rewriting an acceptance condition | hand it over as written; a condition that is wrong goes to the human |
> ```
>
> That row is unmoved, and no clause of 1–5 names it. The added subsection narrows **both** of its columns. The
> *never yours* column: the manager may now write a replacement clause itself where no falsifying party exists, and
> may extend a condition's scope — both are the manager putting its own text into an acceptance condition, which the
> row forbids without qualification. **The second column is the sharper break**: the row routes *a condition that is
> wrong* to the human; the added text routes it to the falsifying party's pen or to the manager's, and to the human
> only for the residue that *"needs a judgement nobody has made"*.
>
> **I tested the counter-reading before calling this.** The added section's first sentence — *"Everything here
> reaches a node nobody holds yet… its condition goes over as written"* — deliberately echoes the row's *"hand it
> over as written"* and fences the new pen off from the claimed-node case. **That reconciles the first column on a
> narrow reading. It does not reconcile the second**: *"a condition that is wrong goes to the human"* is now false
> for exactly the case the new section exists to create. The row was neither amended nor cross-referenced, and it
> sits 330 lines above the new subsection and is read first, **so a manager reading the table concludes the pen does
> not exist.**
>
> **Form, as a predicate.** A rule statement in either changed file, outside the two sections clauses 1–5 name, whose
> force over *who may write into an acceptance condition* or over *where a wrong condition goes* is narrowed or
> contradicted by the added text, and which the added text neither amends nor reconciles.
>
> **Extent — an enumerator** over the two files the implementer may edit, which is the whole of the work: a script
> that unwraps both files into paragraphs (*"a line is not a unit of meaning here — several of these rules wrap"*),
> drops the added line ranges so only unmoved text is a candidate, and keeps every paragraph mentioning *condition*
> — **17 in `SKILL.md`, 14 in `graph-conventions.md`. I read all 31. The row above is the only one that meets the
> predicate.** Four near-misses cleared, and why, so a repair does not over-reach: `graph-conventions.md`'s *"its
> worker may not rewrite it"* — inside the section clause 1 names and expressly preserved; both files' *"hand it over
> as written [to the checker]"* — a checker exists only on a claimed node, which the new pen does not reach;
> `SKILL.md`'s scribe rule and its `## Words used exactly` entry — scoped to the worker or reconciled by *"kept
> distinct from the minting author's text"*; and *"An implementation node is startable when its acceptance condition
> can be written in full"* — clause 4's re-derivation is an act before the claim, not a new bar on startability.
>
> **One note on routing.** The same instance also breaches `/writing-for-agents`' relevance rule. **I have not
> entered it as a separate bar failure**: it is one instance with one repair, and naming the bar as well would split
> a routing signal that belongs wholly with the feature.
>
> **The bar — MET.** Commands discovered from the repo itself: no manifest, no task runner, no `.github`, no
> formatter or linter config anywhere in the tree. No build, no tests, no formatter, no linter to invoke — **a
> complete bar on its remaining half, not a deficient one. There was nothing to run, and I ran nothing.** On the
> non-command half: **`CONTEXT.md`'s `_Avoid_` lines** scanned over the 1,225 added words, unwrapped, **by stem and
> not only by whole word** — four hits, all cleared by hand as the glossary's own usages or ordinary English.
> **Ground rules** 1–4 all hold; the proviso list names only workflow concepts. **The four standing rules** hold;
> no line-number citation anywhere in the added text. **`graph-conventions.md` at base commit** — both changed
> paths are shipped files, edited plainly: zero strikethroughs in the added text and `map-history.md` unchanged.
> **`/writing-for-agents`** — read and applied by hand, no part delegated, **so nothing ran in an agent handed less
> than I was.** One thing weighed and cleared: *pen* is new to both files and `SKILL.md`'s single use has no prior
> introduction in that file, but the two antecedents sit in the paragraphs immediately above.
>
> ```
> QUESTIONS:
> - An amendment flag has no marker to take. SKILL.md's new list says an amendment "is carried as a flag",
>   which is clause 5's own wording and so was not the worker's to depart from. graph-conventions.md's
>   "### `## Flags`" — unmoved — admits exactly three markers: ASSUMPTION, CONDITION-WRONG, DELEGATED.
>   None fits a manager's or a falsifying party's amendment. CONTEXT.md's **Flag** entry sharpens it: a
>   flag records "a judgement an agent made on its own", and the new text insists an amendment "is a
>   transcription and never an authorship". So the thing being flagged is by construction not a judgement.
>   Which marker does an amendment carry, or does it need a fourth?
> - The duty in clause 2b binds workers, and no worker contract states it. That party is usually a worker.
>   `grep -l graph-conventions .claude/skills/expedition-*/SKILL.md` returns nothing — no worker contract
>   points at graph-conventions.md — and the manager's own spawn list names the node file, the map and the
>   index of decisions, not graph-conventions.md. The condition named exactly two files, so the worker
>   could not have added it to a worker contract. So the duty is stated where the manager will read it and
>   not where the party that owes it will.
> - Two different lists of "what counts as already fixed" now sit in one SKILL.md section. The unmoved
>   "### The four constraints on a condition you write yourself" says a condition "may demand only what is
>   already fixed — by a settled node, by the node's own question, or by the state of the files". The new
>   amendment proviso says "already fixed by a resolved node, by work landed in the tree, by the glossary
>   or by the shipped files" — clause 1's own wording. Nothing says how the two relate.
> ```

**The manager's disposal of run 1.** *Not the checker's text.*

- **The bar holds and clause 8 is the only failure.** Eight of nine clauses met, and the checker established the
  additions-only claim itself against the base rather than trusting a diffstat.
- **The worker and the checker are both right, and the condition is what cannot be satisfied.** The worker reported
  that row as a defect it was forbidden to touch and minted [node
  278](278-the-never-yours-table-states-the-amendment-rule-as-absolute.md) for it; the checker fails the work
  because the row's meaning changed. **Clause 8 forbids the added text from changing that row's meaning, and no
  text stating clauses 1, 2 and 2b can avoid changing it** — the row states the same rule, absolutely, that those
  clauses narrow. **Repairing the row is also forbidden by clause 8.** So the condition demands a thing and forbids
  every route to it.
- **The manager did not adjudicate it and cannot amend it.** Under [node
  252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md) the pen reaches an **unclaimed** node only;
  this node is claimed and its work is at a gate. **That boundary is being observed rather than argued around**, and
  it goes to the human, which is where node 252's own answer sends it.
- **The contradiction is the manager's doing.** Clause 8 pre-dates the amendment, but the tension it now creates was
  widened by clauses 1, 2 and 2b, which the manager wrote. This is the **third** defect that amendment introduced,
  after `95.5`'s un-swept clause 5.
- **The checker's three questions travel in the gate payload** rather than queueing. The second is the largest: **the
  duty node 263 settled is now stated only where the manager reads it, and the party that owes it is usually a
  worker whose contract does not point at that file at all.**

### Gate — `approve`, on a failing check

**The human's answer**, `verbatim`: *"approve"*

**The gate was raised on a `FAIL` and said so in its first line.** The manager recommended nothing either way, the
disagreement being one it may not adjudicate, so this is not a divergence — there was no recommendation to diverge
from.

**What the approval does and does not settle.** It lands the work. **It does not repair clause 8's breach**: the
`## What is never yours` row still states the amendment rule absolutely, and the new subsection still narrows it
330 lines below. [Node 278](278-the-never-yours-table-states-the-amendment-rule-as-absolute.md) is the repair and
its `Blocked by: 95` edge is satisfied by this landing. **It does not amend this condition either** — clause 8
stands as written, breached and recorded, rather than being rewritten after the fact to match what shipped.

**The three questions the checker handed back are not answered by an approval** and are carried forward: the flag
marker an amendment has no home for, the search duty stated only where the manager reads it, and the two lists of
what counts as already fixed. **The manager holds them rather than treating the gate as having closed them.**

## Acceptance condition

***Written by the manager, for a node the manager minted itself.*** Marked as the manager's own under [Who writes the
acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed. **What
it demands was fixed by node 82 and by nothing of the manager's**; its wording is not, so the condition states the
properties and leaves the form.

1. ~~`.claude/skills/expedition/graph-conventions.md`'s `### Acceptance condition` states who may change a condition
   after it is written, and distinguishes three parties: **the condition's own worker**, which may not rewrite it and
   raises instead where it judges it wrong — unchanged from what that section says today; **the manager**, which may
   extend the condition's scope to further instances of a defect the condition already describes, provided the
   amendment writes no requirement that was not already fixed; and **the human**, to whom anything else goes.~~

   **Amended by the manager on 2026-09-19, superseded in place and not removed.** The same, with **four** parties
   rather than three: **the condition's own worker**, unchanged; **the party that established a fact which falsified
   a clause**, which writes the replacement as text on its handover for the manager to file, provided every word of
   that replacement is already fixed by a resolved node, by work landed in the tree, by the glossary or by the
   shipped files, and provided the amendment names which; **the manager**, which holds that same pen where no such
   party exists, and which separately may extend a condition's scope as the struck text says; and **the human**, to
   whom anything else goes, including any replacement part of which needs a judgement nobody has made.
   *What fixes it:* [node 252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md), resolved, whose
   answer states the test and the pen in those terms.
2. ~~The same section states the three things that extension does **not** reach, and states them as properties rather
   than as examples: a new demand at any place; an ambiguous demand at a place the condition already lists, which
   stays the worker's to decide-and-flag or to raise; and a defect the condition does not describe, which is a new
   node.~~

   **Amended by the manager on 2026-09-19, superseded in place and not removed.** The same three, with the second
   qualified: a new demand at any place, unchanged; **an ambiguous demand at a place the condition already lists,
   which stays the worker's while the ambiguity is open and is amendable once a resolved node has settled it**,
   sharpening being the amender's act in the first case and that node's in the second; and a defect the condition
   does not describe, which is a new node, unchanged.
   *What fixes it:* [node 252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md), resolved, whose
   answer qualifies exactly this exclusion and leaves the other two whole.

2b. **Added by the manager on 2026-09-19.** Both files state the **trigger** that fires the pen in clause 1, and
   state it as a duty rather than as a permission: before handing back, the party that established a fact searches
   the open nodes' `## Acceptance condition` sections for the handles its own work fixes — a word it refuses, a path
   it changes or moves something out of, a phrase it supersedes — and reads only what matches; where no such party
   exists the manager searches; the search reaches **every open node's condition, claimed or not**, while what is
   *done* about a claimed node stays the manager's under the standing raise rule; and the party names on its
   handover which handles it searched.
   *What fixes it:* [node 263](263-nothing-tells-the-falsifying-party-to-go-and-look.md), resolved, whose answer
   states the duty, its hand, its width and the naming requirement in those terms.
3. `.claude/skills/expedition/SKILL.md`'s `## Acceptance conditions` — which today says *"Where a node was minted by
   an agent, that agent wrote the condition and you file it"* — carries the same permission and the same three
   limits, stated as duties of the manager rather than as a description of the rule.
4. That same section states the manager's duty to **re-derive an enumerated scope before the node is claimed**: where
   a condition's scope is a list of files, the manager re-runs the search that produced that list, and where the list
   has grown, widens it before the node is claimed rather than after a worker has read the short version.
5. That same section states what accompanies an amendment: it is recorded on the node beside the search that
   justified it, marked as the manager's own and distinguished from the minting author's text, carried as a flag, and
   named in the report accompanying the pick — or, where the amendment is made after the node is claimed, named in
   that node's closing report instead.
6. Neither file states that the manager may **author** a condition for a node an agent minted. That prohibition is
   untouched by this work, and where either file states it today, it still stands after.
7. `CONTEXT.md` is not changed, and no file under `.scratch/` is changed.
8. No rule in either file is removed or renumbered, and no rule other than the ones clauses 1–5 name changes its
   meaning.
9. The working tree meets the bar.

### The manager's read-back, recorded before the claim

*[Node 39](39-condition-for-a-manager-minted-node.md)'s constraint 2 requires the condition to be read back against
the two rules that bind every condition, and that reading recorded on the node.*

- **Self-contained text.** It passes. Every demand is stated in the condition's own words rather than by pointing at
  node 82 — the permission, the three limits, the re-derivation duty and the five things that accompany an amendment
  are all written out here. The two existing sentences it changes are quoted. The checker has both files.
- **It does not quantify over the record.** It passes. Clauses 6 and 8 are demands about **what changed in the two
  files**, answerable from the diff, which `graph-conventions.md` permits by name. No clause holds the work against
  the effort's resolved nodes.

## Annotation: this condition's scope is short by measurement — five worker contracts it does not name

*Filed by the manager from [Whether a condition's scope stops being a list of
files](94-condition-scope-as-a-predicate.md)'s `INVALIDATIONS`, in that node's own words. **The condition above is
not amended by this annotation**; amending it is a separate act under [How a condition's scope is
amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s guard 2, and the manager has not performed it.*

> **This one is the sharper finding, because node 95 is node 82's own carrier.** Its scope names two files. Its
> subject is *who may change a condition after it is written*, and `grep -rn "not that worker's to fix"` over
> `.claude/` returns that sentence **verbatim in all five worker contracts**, none of which the condition names: *"A
> condition its worker judges wrong is not that worker's to fix: it stops that node and goes to the human."* That
> sentence states the worker's half of exactly the three-party distinction node 95's clauses 1 and 2 exist to write,
> and node 82 falsified its routing — a short scope now goes to the **manager** and never spends a human turn. So a
> worker reading its contract after node 95 lands would still be told to stop the node and go to the human, which is
> the wasted turn node 82 exists to prevent. **Node 82's carrier reproduces node 82's defect, five files over.** The
> demand at the five new places is fixed by node 82's resolved answer, so this is a widening node 82 licenses
> cleanly.

**Why nobody reported it earlier**, in node 94's words: *"its scope came from a worker's `INVALIDATIONS` rather than
from a search, which is the exact case rung 3 exists to expose."*

## Annotation: this node's acceptance condition is now short a second way

*Filed by the manager on 2026-09-19, carrying [node
252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s worker's words rather than the manager's.
**The condition is not amended here.***

> Its clauses 1 and 2 state node 82's permission and node 82's three limits as the whole of who may change a
> condition after it is written, which node 252 falsifies: clause 1's three-party split now needs a fourth party, the
> amendment's author under the fallback limb, and clause 2's three limits now need exclusion 2's qualification.
> **Node 95 already carries a second, separate shortfall** its own annotation records — node 94's finding that its
> scope names two files while the sentence it must repair sits verbatim in five worker contracts. Both are amendable
> under node 252 and neither has been amended. Whether node 252 rides node 95 or gets a carrier of its own is the
> manager's, exactly as node 82's worker left the same choice.

***The manager's own note, beside that text.*** **Both shortfalls are amendable under node 252 and the manager has
amended neither.** The pen here is the manager's, node 252's and node 94's workers having both finished. It is not
being exercised silently: whether this node carries node 252's rule or a fresh node does is a judgement about scope,
and it is named for the human in node 252's pick report. **This node is also the standing evidence in node 252's own
answer** that a permission can be granted and never exercised.

*The manager's note, 2026-09-26:* [node 311](311-may-the-human-amend-a-held-nodes-condition-of-their-own-accord.md) reports that it contradicts part of this node's landed work: flag 95.3's unclaimed-only boundary was applied in `graph-conventions.md` to the human as well as to the two agents, and it holds only for the agents. The fix is [node 321](321-remove-graph-conventions-limit-on-the-human-amending-a-held-nodes-condition.md). The rest of this node's work stands.
