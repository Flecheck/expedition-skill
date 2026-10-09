# The manager starts the next node rather than proposing it and waiting

Type: implementation
Status: resolved
Supersedes: 192

## Question

**The human reported this as a defect in the shipped skill.** Their words, `verbatim`: *"Also the manager should
proactively start new nodes when one has finished."*

### What the files say now, and why it is not enough

[map.md](../map.md) carries their earlier standing instruction, `verbatim`: *"You can start new tasks. You should
automatically propose to start a new task when a task finish"*, and the map renders it as *"The manager never idles,
and proposes the next work itself as each node finishes."*

`.claude/skills/expedition/SKILL.md`'s `### Picking the next node` says: *"Pick it yourself and report the pick.
Never ask which node to work."*

**Both say pick, and neither says start.** Nothing in either file says the manager spawns the worker rather than
waiting for the human to react to the pick, and nothing names the moment at which it does so. **The instance that
produced this node is a manager doing exactly the permitted thing and still stalling**: at [Adopting an in-flight
effort](18-adopting-in-flight-effort.md)'s close it reported the node finished, named [Write the adoption
procedure](97-write-the-adoption-procedure.md) as the strongest next pick, wrote *"Nothing is expected of you"*, and
started nothing. The code slot sat empty and both grilling channels sat empty.

**Reporting a pick and then stopping is indistinguishable, from the human's side, from asking which node to work** —
which the contract already forbids. The prohibition has no effect because the report that replaces the question is
still a report the manager waits on.

## Acceptance condition

***Written by the manager, for a node the manager minted itself*** at the human's instruction. Marked as the
manager's own under [Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed. **The
human's instruction is fixed; its wording and its placement in the file are not, so this condition states the
properties and leaves the form.**

1. `.claude/skills/expedition/SKILL.md` states that when a node finishes, the manager **starts** the next work rather
   than proposing it and waiting: it picks, spawns, and reports the pick as something already under way.
2. It states that the report of a pick awaits no answer, and that the human's redirection of a pick is a correction
   after the fact rather than a permission the manager waits for.
3. It states what bounds how much the manager starts, in terms the file already carries: the effort's code-slot count
   for implementation nodes, and the rule that exactly one question is in front of the human at a time for nodes that
   need one. A pick that would exceed either is not started.
4. It states that the manager reports what it started, so that a pick the human would have made differently is
   visible to them at the moment it is made and not only at that node's close.
5. Where `### Picking the next node` today says *"Pick it yourself and report the pick. Never ask which node to work"*,
   that prohibition still stands after the work and is not weakened.
6. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
7. No section of `.claude/skills/expedition/SKILL.md` is removed, and no rule in it other than what clauses 1–4 add
   changes its meaning. In particular the nine duties it lists as unsettled are not reduced, and `## What is in front
   of the human, and when`'s one-question-at-a-time rule and its two tiers are unchanged.
8. The working tree meets the bar.

### The manager's read-back, recorded before the claim

*[Node 39](39-condition-for-a-manager-minted-node.md)'s constraint 2 requires the condition to be read back against
the two rules that bind every condition, and that reading recorded on the node.*

- **Self-contained text.** It passes. Each demanded property is written out here rather than pointed at; the one
  existing sentence it protects is quoted in clause 5; the file it changes is named by path and the checker has the
  repo. Clause 3 names two bounds by their function and the file states both, so a checker reads them there.
- **It does not quantify over the record.** It passes. Every clause is a demand about the state of one file or about
  what changed in the tree, which `graph-conventions.md` permits by name. No clause holds the work against the
  effort's resolved nodes.

### What this node does not settle, stated so no one reads it into the condition

**Whether the manager may start a node that needs the human before the human's channel is free.** Clause 3 forbids it
by pointing at the existing one-at-a-time rule, which is the conservative reading of what is already fixed. Whether a
worker may be spawned to do its reading while its question queues is a change to that rule and belongs to the human,
not to this condition.

## Where it came from

The human, unprompted, immediately after a manager reported a node finished and started nothing. Minted by the
manager at their instruction; the question above and the acceptance condition are the manager's, and the instruction
itself is quoted verbatim at the top.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`100.1` `ASSUMPTION` **settled** — **The human-channel bound reads as a bound on starting, not on running.** Clause 3 demands
that a pick exceeding *"exactly one question is in front of the human at a time"* is not started, and the node's own
unsettled section fixes the conservative reading. I settled the ambiguity it leaves: whether that forbids two HITL
nodes running concurrently, or only forbids starting one onto an occupied channel. I wrote the latter, and said so in
the text. The former would contradict the effort's map (*"Two grilling nodes run at once to keep the human's queue
full"*) and would empty tier 2 of the queue, which clause 7 requires be unchanged; under the latter, a second
grilling node is started the moment the channel frees and everything already in the file stays true.

`100.2` `ASSUMPTION` **settled** — **The pick report's "awaits no answer" was written in `### Picking the next node` rather than
added to the list of three non-claimants.** `## What is in front of the human, and when` enumerates *"Three things
are not claimants at all"*, and a pick report is arguably a fourth. I left that sentence untouched because clause 7
forbids changing the meaning of any rule clauses 1–4 do not add, and the sentence claims no exhaustiveness. If the
human would rather the list read four, that is a one-line edit to a sentence I deliberately did not touch.

`100.3` `ASSUMPTION` **settled** — **I treated the human's instruction of the correction round as superseding clause 3's second
named bound, rather than as something to reconcile with it.** Clause 3 demands the file bound starting by *"the rule
that exactly one question is in front of the human at a time for nodes that need one"*. The human replaced that bound
with a target count of two, topped up when a node finishes, and the manager has written it into `map.md`. The file
now bounds those nodes by the count, and states the one-question rule as bounding only the pick that cannot be
started without an answer first — so clause 3's first term and its *"a pick that would exceed either is not started"*
still hold exactly, and its second term holds for a narrower class of pick than it names. I did not raise a second
time, because the party that owns the condition's demands had just changed the demand in their own words, and asking
whether I may follow what they had just said would have spent a turn on a settled point. **If the condition needs
formal amendment rather than a flag, that is the manager's `CONDITION-WRONG` to file, not mine** — I state the gap
rather than working around it.

`100.4` `CONDITION-WRONG` **settled** — ***The manager's own flag, not a worker's, and marked as the manager's.*** Clause 3 above
still reads as it was written, and its second term — *"the rule that exactly one question is in front of the human at
a time for nodes that need one"* — is no longer the demand, the human having replaced that bound at this node's gate
in their own words. The manager did not rewrite the clause, which is never its to do. What it did instead, and what
this flag records so the human can revisit it: **it handed checker run 2 the condition exactly as written above, and
beside it the human's words verbatim with the note that they were given in answer to this node's raise and bear on
clause 3.** The checker therefore holds both texts and the manager authored neither. The judgement being flagged is
the manager's alone — that words the human addressed to this node's deliverable amend what done means for it — and
if that is wrong, the repair is a formal amendment to clause 3 and a re-check against it.

`100.5` `ASSUMPTION` **settled** — **I reworded clause 2's phrase rather than explaining it, and judged the reword to stay inside
the condition.** The human reported not understanding *"A redirection is a correction after the fact"*, and clause 2
uses that exact phrase, so a reword risks touching the condition — which is theirs. I judged it does not, because the
condition's own preamble states that it fixes properties and leaves wording and placement to the worker, and both of
clause 2's properties are still stated in the same paragraph. If they read clause 2's phrase as the demand rather
than as one rendering of it, this is theirs to correct and the old sentence goes back verbatim.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted. The manager added the heading, the outcome label and the two establishments below.*

**Outcome: `PASS`.** *"PASS covers the whole acceptance condition. No part is left uncovered, and I hand back no
questions."* All eight clauses met and the bar met.

**How the hard clause was established.** Clause 7 protects the meaning of every rule the change does not add,
including `## What is in front of the human, and when`'s *"Three things are not claimants at all"*. The checker
judged it intact on two pre-existing grounds: the file *"already coexisted with non-claimants outside that list
before this change"* — its own `## What is in front of the human, and when` says *"A checker's question is not a
claimant **either**"*, and `### Picking the next node` already said of the pick report *"The work does not wait for a
reply"* — so *"that sentence never meant a closed catalogue"*; and the reconciliation the file does make, *"tier 1
stays at three"*, is about tier 1's membership, which the new text explicitly leaves alone. It also diffed the whole
of that section against `HEAD` and found it **byte-identical**.

**One correction to the given, from the checker.** *"A `.gitignore` **does** exist — it ignores `.worktrees/` and
nothing else, invokes no tool and enforces no style, so the command half is still empty and the bar is met on its
remaining half."*

**What the Standards axis raised and the checker declined to hand back as findings**, reported so the manager could
overrule it: the restatement of the one-question rule and the code-slot count (demanded by clause 3 in terms the file
already carries); *"a correction after the fact"* overloading a word the gate loop owns (clause 2's own wording);
*"a node that needs the human"* rather than the coined `HITL`; and — *"the sharpest of the four, and the one worth
the manager's eye"* — *"in front of them"* used loosely at one line and strictly five lines later, each disambiguated
by its neighbouring sentence. The manager overruled none of the four.

**NOT COVERED:** none. Every clause names something observable in the working tree.

**Two scope confirmations the checker asked for, established by the manager, which holds the handover the checker
does not.**

- ESTABLISHED BY the manager · read `git worktree list` and the node's own spawn — *"If clause 6's baseline was meant
  to be `master` rather than the worktree HEAD, that commit falls in scope and my clause 6 does not reach it."* The
  worktree's baseline is correct as the checker took it. The worktree was created off `HEAD` at the moment of the
  claim, which was commit `392e0ae`, and that commit is [node 58](58-qualify-the-graph-file-ban.md)'s landed work
  approved at its own gate. This node's work is the uncommitted diff against that baseline, and nothing in clause 6
  reaches another node's landed commit.
- ESTABLISHED BY the manager · read `git status` in the main checkout — *"The main checkout … has uncommitted changes
  under `.scratch/`."* Those are the manager's own graph bookkeeping in a different checkout from the work, and the
  checker's reading of clause 6 as scoped to the tree holding the work is correct. They have since been committed as
  `94918f1`.

### Gate, round 1 — outcome: **correct**

**The human's words**, `verbatim`, given on being shown the gate and quoting the bullet at
`.claude/skills/expedition/SKILL.md` lines 465–468 in the worktree: *"For 100, i am not sure about \"- **a node that
needs the human starts only while nothing is in front of them.** Exactly one question is in front of the human at a
time, and a node started onto an occupied channel is a second one. The bound is on the moment of starting rather than
on how many such nodes run: one started while the channel was free keeps running, and a later question of its own
queues like any other.\n\", since there can be multiple grilling at once, also flag 100.1. ok for the flags fo 93 and
99"*

**What the manager did with it, and what it did not do.** The words were passed to the worker unaltered. The manager
did **not** decide what the bullet should say instead: the human named an unease and a flag rather than a
replacement, and the worker holds the node. Flags `100.1` and `100.2` are **not** settled by this reply — `100.1` is
named in it as part of the concern, and `100.2` is not mentioned.

**The manager's own report to the human at the gate, which is context for the round**: that flag `100.1` had bitten
within minutes of being written — both grilling channels were free, this gate was in front of the human, and under
the bullet as written the manager started no HITL node, leaving two channels idle for the length of the gate.

### Checker run 2 — `PASS`, with clause 3 not covered

*The checker's own text, pasted. The manager added the heading and the outcome label.*

**Outcome:** *"`PASS` — covering clauses 1, 2, 4, 5, 6, 8, and clause 7 except as noted"*, and *"My `PASS` means the
parts I established and no more. Clause 3 is still owed, and you are still holding it."*

**What it was given, and what it did with clause 3.** The manager handed it the acceptance condition as written and,
beside it, the human's words verbatim with the note that they were given in answer to this node's raise and bear on
clause 3 — flag `100.4` records that act. Its answer:

> **I took neither text as the demand, because they demand different files and choosing between them would make me
> the author of the standard.** You asked me to say which I took and why; the honest answer is that I could not take
> either without authoring.
>
> The condition's second bound is *the one-question rule itself*: a pick is not started if starting it would put a
> second question in front of the human. The human's words set a *count* instead — "by default 2 grilling nodes at
> once … you start a new one (or new ones) to get back to the current amount". Those cannot both hold. A grilling
> node's normal running state is a live question, so under clause 3's second bound you would essentially never have a
> second one running, and the default of 2 is unreachable. Clause 3 also says "in terms the file already carries",
> and the number 2 is a term the file did not carry. The work implements the human's words and states the opposite of
> clause 3's second bound in as many words: "Their questions do not collide, because what reaches the human is still
> one at a time: the rest wait in the queue above." The human's words additionally demand "A count is a target to
> reach rather than a ceiling to stay under", which clause 3's ceiling language ("a pick that would exceed either is
> not started") does not license at all.
>
> Checking clause 3 as written would `FAIL` the work for obeying words you handed me as the human's own and bearing
> on this clause; discarding the human's words would be checking against a standard you told me may not be the live
> one. Hard rule 3 forbids me repairing the condition, and nothing lets me discard a given. So clause 3 is the one
> part I cannot establish, it is confined (clauses 1, 2, 4, 5, 6, 8 stand without it), and it goes back to whoever
> can settle it — the human, or you by amending clause 3.

**What rides on that settlement**, in the checker's words, *"so you can re-check it in one pass once it is settled"*:
the bullet list *"**Two counts bound how much you start**"*, the paragraph *"**A count is a target to reach rather
than a ceiling to stay under**"*, and the bullet *"**One pick is bounded by the human rather than by a count**"*. Its
clause 7 result *"covers everything except those three passages"*, since whether they are *"what clauses 1–4 add"*
depends on which text governs clause 3.

**How clause 7 was established on everything else.** *"`diff <(git show HEAD:…SKILL.md) <(sed '451,477d' …SKILL.md)`
is **empty** — the file outside the 27 inserted lines is byte-identical to its baseline."* So no section removed, the
nine unsettled duties still nine and unedited, and the one-question rule and two tiers untouched. **One residue it
names and does not treat as a breach:** the insertion makes the pick report a further non-claimant while the file
still reads *"Three things are not claimants at all"* — *"that numeral was already strained pre-existing by line
442's checker-question clause… Not a breach; worth a node if you want the numeral fixed."* That is flag `100.2`.

**`NOT COVERED:` clause 3**, quoted in full by the checker and reproduced above.

**`QUESTIONS:` one**, handed back alongside the outcome and carried to the human with the gate:

> The insertion writes *"**A redirection is a correction after the fact.**"* `CONTEXT.md`'s `_Avoid_` line under
> **Revision** reads *"correction (a correction round is a different thing)"*, and **Correction round** is a live
> glossary term bound to the gate. The word now names a third thing. The wording is the acceptance condition's own —
> clause 2 says *"the human's redirection of a pick is a correction after the fact"* — so it was not the worker's to
> depart from. Does the human want the sentence reworded (the named term *"redirection"* carries the concept without
> the word), or the `_Avoid_` line relaxed?

Its three parts, as node 71 requires of a finding: **instances** — one, `.claude/skills/expedition/SKILL.md`, the
sentence quoted. **Form** — a word on a `CONTEXT.md` `_Avoid_` line used in a shipped skill for a concept other than
the glossary term it belongs to. **Extent** — `grep -rn "correction" .claude/skills/ | grep -v "correction round"`,
which returns two lines, the other pre-existing and legitimate.

**Six of seven Standards-axis findings the checker rejected rather than handing back**, reported so the manager could
overrule it: that `HITL` was paraphrased away (*"`HITL` appears nowhere in `SKILL.md`'s body — only in its glossary
line"*); *"gap"* for a free slot, cleared and flagged as cleared *"so you can overrule it cheaply"*; negation, the
paragraph leading positively with *"**Then start it.**"*; three duplication findings, *"a glossary term applied in
the body is use, not duplication"*; a co-location breach handled under clauses 7 and 3; and the baseline smells. It
also declined `/coding-principles`' 500-line split rule: *"it is explicitly a rule for organising code, the
deliverable is prose, and the file was already 581 lines before this change."* **The manager overruled none of the
seven.**

**Its own scope check, run rather than assumed:** *"`git status --porcelain` shows one modified file and nothing
else"*, and *"`git log master..HEAD` is empty (the branch is behind master, so `git diff master` shows master's own
graph commits in reverse — not the work)."* The bar's command half was confirmed empty by looking rather than by
taking the given: *"repo root holds only `.claude`, `.scratch`, `CONTEXT.md`, `.gitignore`; no `package.json`,
`Makefile`, `justfile`, `*.toml`, `flake.nix`, `.pre-commit-config.yaml`, no `.github`."* It ran the reviewing
skill's Standards axis and left its Spec axis unrun, *"its step 2 searches `.scratch/` for an originating spec, which
is the record I am blind to"*.

### Checker run 3 — `PASS`

*The checker's own text, pasted. The manager added the heading and the outcome label.*

**Outcome: `PASS`.** *"No questions and no uncovered parts. Every clause was establishable from the paths I was
given."* It was handed the condition as written, the human's words on clause 3, and the human's words on clause 2 —
and told which clause each bore on, with the manager writing no replacement for either.

**Clause 3 — which text it took as the demand.** *"I took the human's words as the demand, and I judge the two texts
reconcilable rather than in conflict."*

> The condition's own preamble fixes this: *"The human's instruction is fixed; its wording and its placement in the
> file are not, so this condition states the properties and leaves the form."* Clause 3 is therefore the manager's
> rendering of a fixed instruction, and where the rendering and the instruction diverge the instruction governs.
> Rewriting clause 3 is not mine to do, so I held the file against both.
>
> They reconcile because the file satisfies **both** readings at once. Clause 3's two named elements are each present
> — the code-slot count for implementation nodes … and the one-question-at-a-time rule for nodes that need the human
> … as is its closing demand … On top of those the file carries the human's count … and their top-up rule … Clause 3
> says the file states X and Y; it does not say *and nothing further*, so the count is an addition rather than a
> departure.

**And what it says the manager should see, in its words, *"even though it is not a finding"*:**

> Clause 3 as written presents one-question-at-a-time as *the* bound on human-needing nodes; the shipped file
> presents a count of two as the bound and one-question-at-a-time as why two is safe. The condition text now on the
> node no longer describes the bound the file states. The work is right and the condition's wording is stale;
> whether to amend it is the manager's and the human's, not mine.

**Clause 2 — what it took the demand to be.** *"The property, not the phrase."* On the same preamble ground, clause
2's phrase *"a correction after the fact"* is its description of the property rather than mandated wording, and both
properties are stated in the file as it now reads. *"The word `correction` is **absent from the added text**… That is
the right outcome on the bar as well as on the condition… The property survives and the colliding word is gone."*

**How clause 7 was established.** *"`git diff | grep -c '^-[^-]'` = **0**, so every pre-existing byte survives."* The
heading set is identical before and after, the unsettled duties still number nine, and *"the body of `## What is in
front of the human, and when` down to `### Picking the next node` is **byte-identical** to `HEAD`"*. Clause 6 was
established on `git status --porcelain --untracked-files=all` returning exactly one entry, with `.scratch/` confirmed
tracked so a change there would have shown.

**Five Standards-axis findings it declined to hand back**, reported so the manager could overrule it: three
duplication calls, on the ground that local restatement of a defined term is *"this file's established register,
present in text this work did not touch"* and that faulting it *"would fault it for complying with clause 3's own
'in terms the file already carries'"*; one about three justifications for one shape, *"a matter of degree with no
stated bright line"*; and one about `HITL` being left unused, which it found *"wrong on the file: `HITL` never
appears in the body, so the added text matches the file rather than departing from it."* **The manager overruled
none of the five.** As on run 2, it ran the reviewing skill's Standards axis and left its Spec axis unrun, that step
searching `.scratch/`.

## Interview

### Attempt 1 — the bound the human was uneasy about at the gate

**The worker's raise, at the correction round rather than a correction.** It touched nothing and reported the tree
standing exactly as it did at the gate. Its ground, in its words: *"The relief the human's sentence points at **is**
that change. It is not mine to make."* — the change being the one this node's own `### What this node does not
settle` reserved for the human, *"Whether the manager may start a node that needs the human before the human's
channel is free."*

**Q1, from the worker.** *"Should the shipped file bound the *starting* of a node that needs you — the conservative
reading, which idles the grilling channels for the length of every gate — or bound only what *reaches* you, so such
a node is started whenever it is the best pick and its question waits in the queue like any other?"*

**One wording it rejected outright, recorded because it is the obvious repair and it is closed:** scoping *"in front
of them"* to the same tier, so a gate would not block starting a grilling node — *"that invents a rule about the
tiers, which clause 7 protects."*

**A1, from the human**, `verbatim`: *"For 100, I would say by default 2 grilling nodes at once, and the rule is that
when a node finishes, you start a new one (or new ones) to get back to the current amount (2 by default by the user
can ask for more)"*

**Neither option as offered, and the manager did not decide which it is nearest.** The worker asked whether the file
should bound the *starting* of a node that needs the human or bound only what *reaches* them, and recommended the
second. The answer supplies a **third shape**: a target count of concurrently running nodes that need the human,
defaulting to two and settable by the human, with the rule being to **top up to the target whenever a node
finishes**. It is consistent with the recommendation's effect — a live question no longer blocks a start — but it
replaces the bound rather than choosing between the two that were offered, so it is passed to the worker as its own
answer rather than recorded as taking either. Whether it diverges from the recommendation is the worker's to say.

**The count is now a second per-effort setting alongside the code slot**, which the map already carries as *"How many
implementation workers run at once is a setting of the effort, and for this effort it is one."*

**Written into [map.md](../map.md) at the same time**, under [Rules added to one effort's map, and what makes them
legitimate](93-effort-scoped-custom-rules.md)'s rule that a standing rule of the human's binds this effort only once
it is in the map — this node's own work being uncommitted and therefore binding nobody yet.

### Attempt 1 — the sentence the human did not understand at gate round 2

**The human's words**, `verbatim`, on being shown the gate carrying checker run 2 and the checker's question about
the word `correction`:

> I am not sure I understand "A redirection is a
>   correction after the fact." but otherwise it seems ok

**And, in the same turn, they selected one line of `CONTEXT.md`** — line 154, the `_Avoid_` line of the **Revision**
entry, which reads in full: *"_Avoid_: correction (a correction round is a different thing), change request"*. That
is the exact line the checker's question is about.

**What the manager did with it, and what it did not do.** The words were passed to the worker unaltered. The manager
did **not** decide whether the sentence is explained or reworded, and did **not** treat *"but otherwise it seems
ok"* as approving the gate: the gate has three outcomes, this is the **correct** one, and the node returns to the
gate when the round closes. Flags `100.1`–`100.4` are therefore **not** settled by this reply, none being mentioned
in it. Clause 3 is still owed and was not answered.

**The manager's note on what the reply reaches.** *Not a change to anything above.* The sentence's wording is the
acceptance condition's own — clause 2 says *"the human's redirection of a pick is a correction after the fact"* — so
a reword may touch the condition, which is the human's and not the worker's or the manager's.

**The worker's report on returning**, in its words: *"The map's new wording and my file text agree on every point."*
Three edits in the correction round, all inside `### Picking the next node`: *"the next one"* → *"the next work"* in
the opening paragraph, *"so the top-up's plurality is not contradicted a paragraph earlier"*; the two-bound list
replaced by a two-count list; and two new paragraphs after it. Across both rounds the node touched
`.claude/skills/expedition/SKILL.md` and nothing else, 33 lines inserted, 0 deleted, 0 modified.

**On flag `100.1`, in the worker's words**, handed back *"for the manager's bookkeeping rather than as a flag of its
own"*: *"it recorded my choice of bound on starting over bound on running. That choice no longer exists in the file —
the human replaced the bound with a count — so the flag is overtaken by this round's work rather than settled by a
judgement. Which of retired or settled it is written as is yours."* **The manager leaves it outstanding** and puts it
to the human at gate round 2 with that sentence, rather than deciding on their behalf what a flag they named in their
own reply becomes.

## Retrospective

*The worker's own text, pasted, handed back as the sixth handover part this effort asks for. Filed as an annotation,
which is why it sits after the node's mandatory sections.*

- **What I had to hunt for.** (a) Whether writing the human-channel bound would contradict this effort's practice of
  running two grilling nodes at once — found in `map.md`'s standing preferences, after looking first in `SKILL.md`'s
  `## What is in front of the human, and when`, which describes the queue and its tiers but says nothing about how
  many such nodes may run. That hunt produced flag `100.1`, and the thing I flagged turned out to be exactly what the
  human queried at the gate, so the hunt was worth its cost and its conclusion was still wrong. (b) Whether anything
  already fixed the pick report's contents — found in node 46's question list, attributed to node 16; `SKILL.md`
  carries none of it. (c) Whether `graph-conventions.md` held a picking procedure that would go stale: one grep,
  nothing there. (d) This round, whether the map's new wording contradicted what I was about to write — one grep of
  `map.md`, and it agreed.
- **What I read and did not use.** `CONTEXT.md` end to end, of which only the `_Avoid_` lines bore on the work. Most
  of `map.md`: the landing policy, the dogfood target, the review route, the whole fog section and out-of-scope. Most
  of the implementation contract: checker outcomes, correction-round mechanics beyond the one line about re-checking
  the condition, replacement attempts, and the long section on writing an acceptance condition for a node I report —
  I reported none. `/coding-principles` in full, and `/naming`'s method: neither has anything to say about a prose
  edit whose vocabulary is already fixed.
- **What would have made this node easier.** The node file's `### What this node does not settle` resolved the hardest
  ambiguity in the condition and sits at the bottom of the file, after the read-back; a spawn line pointing at it
  would have got me there before I went looking in the map. Second, the thing that actually decided this node was
  **operational evidence the node file could not hold** — two grilling channels idling through my own gate. Nothing in
  the spawn, the node or the contract would have told me that the conservative reading was expensive; only running it
  did. Where a condition fixes a conservative reading of a rule, the cheapest possible check is to ask what it forbids
  on the day it lands, and I did not ask it. Third, the contract sends me to `/coding-principles` and `/naming`, which
  are near-total no-ops for a prose deliverable, while the standard that actually bites is `/writing-for-agents` —
  named only in `map.md`'s review route, which reads as the *checker's* route rather than the worker's. A line in the
  implementation contract saying a prose deliverable is held against the standard the map's review route names would
  have saved a wrong-footed first draft.
- **What was stale, wrong, or contradicted something else.** At the start of the node, `map.md` rendered the human's
  standing instruction as *"proposes the next work itself as each node finishes"* while the same sentence continued
  *"it names what is being started next"* — half-contradicting itself, and understating the shipped file once my
  change landed. The manager has since rewritten that line, so it is now current. The larger one: my own acceptance
  condition went stale inside the node. Clause 3 named the one-question rule as the bound on starting, the human
  replaced that bound at the gate, and the condition's text still names it — which is the flag above, and the one
  thing in this node I could not fix myself.

**The manager's note on the retrospective.** *Not a change to anything above.* Its third point names a defect in a
shipped file — the implementation contract sending a prose deliverable to `/coding-principles` and `/naming` while
the standard that bites is named only in the effort's map — and its first names a defect in the manager's own
spawning, which is that a node's `### What this node does not settle` is not pointed at from the spawn. **Both are
promotions the manager owes and has not yet made**, and this note stands in for them until it does. The worker's
token figures are not its to estimate and are the manager's to supply.

### Gate, round 3 — outcome: **approve**

**The human's words**, `verbatim`, on being shown the gate carrying checker run 3's `PASS`:

> approve

**What it settles.** All five of this node's flags — `100.1` through `100.5` — under the standing rule that
approving the end of a node settles the flags its payload presented. All five were presented in full at this gate.
**Flag `100.1` is written as settled rather than retired**, the worker having handed that choice to the manager and
the human's word having reached it in the same message as the other four; the record already carries the worker's
account of it being overtaken by the human's own change of the bound rather than by a judgement.

**What it does not settle**, stated so nothing is read into it: clause 3 of the acceptance condition above is
**still stale against the file it governs**, which checker run 3 reported explicitly as not a finding. The work is
right and the clause's wording names a bound the human replaced. Amending it is a separate act and has not been
performed.

## Answer

*The node's deliverable is the shipped text itself. What follows is the worker's own summary of what that text now
says, pasted, plus the landing record which is the manager's.*

`.claude/skills/expedition/SKILL.md`'s `### Picking the next node` now says the manager *starts* the next work rather
than proposing it. All 27 lines are **inserted** between the existing prohibition paragraph and the existing
readiness-floor sentence; no pre-existing line was deleted, reworded or moved.

- **"Then start it."** A node finishing is what triggers the next work: the manager picks, spawns its worker, and
  reports the pick as work already under way, naming the node and its kind.
- **The report awaits no answer and takes no place in the queue**, on the node's own diagnosis compressed to one
  clause — reporting a pick and then waiting is *the forbidden question in the shape of a statement*.
- **The human's redirection arrives after the work has started, and that is the ordinary case.** They name a
  different node in one line; the manager stops or redirects what it started; having started it was not a mistake,
  and the pick was never held open waiting for permission to begin.
- **Two counts bound how much is started**, each a setting of the effort, and a pick that would exceed one is not
  started — it waits, and the manager says what it is waiting for. The counts are *how many nodes that need the human
  run at once* — two, unless the effort's map sets another number — and *how many implementation nodes run at once*,
  the effort's code-slot count.
- **A count is a target to reach rather than a ceiling to stay under.** When a node finishes the manager starts
  enough work to fill every gap it leaves, which is sometimes more than one node.
- **One pick is bounded by the human rather than by a count**: the one that cannot be started without an answer
  first, such as a node whose acceptance condition cannot be written in full. Starting that *is* a question, so it
  waits until nothing is in front of them.

### The landing, which is the manager's record

Committed `47703bb`, path-limited to `.claude/skills/expedition/SKILL.md`, rebased onto `94918f1`, the bar re-run
after the rebase, then fast-forwarded onto `master`. The worktree is removed and the branch deleted. **Nothing was
pushed.**

**The bar's re-run after the rebase**, since the map records that this repo has no build, tests, formatter or CI: the
command half was re-confirmed empty by looking rather than by assumption — the repo root holds `CONTEXT.md` and
`.gitignore` and nothing that invokes a tool. The diff was unchanged at 27 insertions and 0 deletions, the word
`correction` was confirmed absent from every added line, and the protected prohibition was confirmed present intact.

**The sandbox blocked the fast-forward, exactly as it did at [node 58](58-qualify-the-graph-file-ban.md)'s landing.**
`git merge --ff-only` failed with *"unable to unlink old '.claude/skills/expedition/SKILL.md': Read-only file
system"*. Unlike at node 58, **nothing partially applied** — `master` stayed at `94918f1` and the tree stayed clean
under `.claude/`. The manager re-ran that one command outside the sandbox, having said why to the human first. **This
is the second recorded instance and the landing policy still does not describe it**; `git worktree remove` then hit a
related failure, *"could not write config file .git/config: Device or resource busy"*, which left the branch deleted
and the worktree gone from `git worktree list` with no stale config entry — verified by `git worktree prune -v` and
`git config --get-regexp '^worktree'`, both empty.
