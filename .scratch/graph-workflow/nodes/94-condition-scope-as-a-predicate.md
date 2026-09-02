# Whether a condition's scope stops being a list of files

Type: grilling
Status: resolved

## Question

*Surfaced by [How a condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md)'s worker,
and pasted as it wrote it.*

> Node 82's guard 1 re-derives a condition's file enumeration before the claim, which repairs an ageing list rather
> than removing it. The alternative is that a condition addressing a defect with instances states the defect as a
> predicate over a named search domain — "every place under `.claude/skills/**/*.md` where X" — and gives any file
> list as illustration rather than as the bound. That shape is already self-contained text a checker can run against
> the repo, it is the shape [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md) already
> makes a checker hand back, and it would have reached all four recorded shortfalls with no amendment at all,
> including the file that did not exist when node 58's condition was written.
>
> What is genuinely at stake against it: a scope clause has one load-bearing job, which is stopping a worker
> wandering into unrelated work, and a predicate is a weaker fence than a list. A predicate scope also moves the
> moment of judgement — who decides whether a given place matches, and what a worker does when it thinks the
> predicate reaches somewhere the author did not intend.
>
> So: should a condition addressing a defect with instances be written as a predicate over a search domain rather
> than as a list of files — always, never, or on a stated trigger — and if so, what keeps the fence doing its job?

**Blockers, in the worker's words:** *"none. Node 82 is resolved and node 71 has shipped."*

## Answer

*Written by this node's worker and pasted as it wrote it.*

**A condition keeps its list of files and gains the search that produced it.** The human, on the recommendation as
offered: *"for 94 ok for recommended"* — taken whole, so everything below under *The rule*, *The three rungs* and
*The three fence-keepers* is theirs by that assent.

The node posed a binary — predicate **or** list — and the answer is neither side of it. This is the second node in a
row whose binary was narrower than its own source: [What a finding must carry so it can be
swept](71-what-a-finding-must-carry.md) has the same history, and the same resolution.

### The rule

Where a condition's scope was **derived from a search**, that search goes in the condition. The list of files stays
exactly as it is, and so does *"and no other file is edited"*. The search is written **beside** the fence as the
thing that produced it, never in place of it.

The trigger is *"how did you get this list?"*, and its author can answer it every time, because they either ran a
search or they did not. Where they enumerated from memory, that is the defect all the recorded shortfalls share
rather than a case the rule excuses.

### The three rungs

A condition addressing a defect with instances owes **exactly one** of three, and one carrying none of them is
**malformed**. This is word for word the ladder node 71 already makes a checker use for a finding's extent, pointed
at the other end of the pipe:

1. **An enumerator** — the command, and what it returned when run.
2. **A bounding set**, where no command fits — the smallest set that provably contains every instance, together with
   how that set was computed.
3. **An explicit statement that the scope came from no search** — the work creates a file, or the named places *are*
   the work rather than instances of a defect.

**Why the symmetry is the argument and not an ornament.** A checker's finding must state its extent because its
reader cannot go and look. A condition's scope **is a finding stated in advance**, and its reader — the blind
checker, and the worker before it — likewise cannot go and look. The two artifacts have the same reader problem, so
they owe the same answer. And it costs the author nothing, for node 71's own recorded reason: the enumerator was
built in order to write the list, so supplying it hands back work already done.

### The three fence-keepers

The node's third question — *what keeps the fence doing its job* — is the one this answer turns on, and none of the
three answers is trust in the worker.

1. **The list stays, and so does the exclusion clause.** A scope clause's one load-bearing job, per [How a
   condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md), is stopping a worker
   wandering into unrelated work. The fence is the same fence; nothing was removed from it.
2. **An instance outside the list is reported, not edited.** A worker whose search matches somewhere unlisted gains a
   **duty to report**, never a **permission to edit**. So a loose predicate costs one line in a handover rather than
   a wandering commit, and the moment of judgement never moves to the worker at all — it judges only *"does this look
   like a match"*, and a false positive is free. This is node 71's own condition's wording — *"it is reported and not
   edited — reporting it is the whole of what this condition asks for it"* — and that node's checker demonstrated it
   working, searching outside the scope, finding two near-misses and correctly owing nothing.
3. **The enumerator is run by the author, while writing.** This is the fence-keeper that reaches the case node 82
   cannot. A short list surfaces its own overflow *after* the condition is frozen, when the only party holding the
   overflow is the manager — who, under [Who writes the acceptance condition for an implementation node the manager
   mints itself](39-condition-for-a-manager-minted-node.md), is not entitled to decide what the new place must
   satisfy. Running the search at writing time forces that judgement onto the condition's author, at the one moment
   it is theirs. **The enumerator widens nobody's authority; it moves a judgement earlier, to the party who already
   owns it.**

### What the answer rests on, measured rather than argued

Three measurements decided this node, and all three were absent from the record.

**1. The predicate shape works on the newest and hardest instance — in one form and not the other.** Node 103's
condition already contains a predicate: *"no file in the repository still says that a grilling node's flags are
settled at that node's last answer"*. It is keyed to the **wording** of the one wrong sentence its author knew about,
and [the sixth site](102-do-afk-nodes-flags-settle-at-the-pick-report.md) states the same rule on a different false
ground, so it slips through. Keyed to the rule's **subject** instead — `grep -rln "closing report"` over `.claude/`
and `CONTEXT.md` — it returns exactly four files: `CONTEXT.md`, `expedition/SKILL.md`, `graph-conventions.md`, and
`expedition-precondition/SKILL.md`. All four are genuine sites, **zero false positives**, and the fourth is the site
node 103's condition does not name. **The miss was recoverable at minting time by one grep.**

So the discriminator, and it is what makes the rule bite: **an enumerator over the rule's subject is wider than the
author's knowledge of the defect; an enumerator over the defect's wording is exactly as narrow as it.** A condition
satisfies rung 1 with the former and only appears to with the latter.

**2. Of the 43 acceptance conditions on this graph, one records the search that produced its scope.** Node 71's. That
condition is also the only one carrying all three parts at once — the list, the grep with what it returned, and the
report-don't-edit residual — and **it is the only one on the record that never overflowed.** Node 82 cited node 71
for the shape it makes a *checker* hand back and did not notice that node 71's own condition already **is** that
shape. The existence proof was on the record the whole time.

This is also what node 82's guard 1 was missing. It instructs the manager to *"re-run the search that produced that
list"*, and in 42 of 43 cases that search exists nowhere — so the manager reconstructs a search it never saw, from a
list. That is precisely how node 103's miss survives a re-derivation.

**3. Two open conditions are short by measurement, and one of them is node 82's own carrier.** Found by running the
rule against the graph in minutes; see the invalidations below.

### What this answer does not change

- **[An acceptance condition is self-contained text](33-condition-is-self-contained.md) is untouched, and this makes
  a condition *more* self-contained rather than less.** A command is text the reader runs against a repo it already
  has; it sends nobody anywhere. Node 71's own read-back established this for the same construction.
- **[The clause that says no resolved node changes cannot be
  self-contained](36-resolved-node-clause-cannot-be-self-contained.md) is untouched, and it draws this rule's one
  hard boundary: an enumerator's domain is the *tree*, never the *record*.** A search over `nodes/`, `decisions.md`
  or `flags.md` is the quantification that node forbids, and no copy repairs it. Flag `94.2`.
- **Node 82's permission, its test and both guards stand entirely.** This strengthens guard 1 by giving it something
  real to re-run; it removes nothing.
- **Nothing here lets a scope widen without a human where node 82 would not have.** The routing of an enumerator's
  output is node 82's existing test, unchanged: further instances of a defect the condition already describes are the
  manager's to add; a new or changed demand at any place is not.

### How far it reaches back

Stated here because the human said nothing either way, and because leaving it unstated would put the question to
whoever next writes a condition.

- **A resolved node's condition is out of reach and needs no repair.** It has been discharged; there is no work left
  to fence.
- **An open condition, claimed or not, is repaired rather than reopened**, on the precedent node 33 set when it
  audited four existing conditions and repaired none: *"the audit is evidence that the rule bites on real text;
  fixing what it catches is somebody else's commit."*
- **Supplying the missing search to an already-written condition is within node 82's permission**, and is the
  manager's to do at guard 1. Writing down the search that produced a list adds no demand — it records how the list
  was got. Rung 2's residual clause likewise demands only what this node has now fixed.
- **Acting on what the search returns is a separate act, and it routes by node 82's test exactly as before.** Adding
  places, yes. A demand at a new place that nobody has fixed, no — that is the human's or a node of its own. Flag
  `94.3`.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`94.1` `ASSUMPTION` **settled** — **The rule binds a condition whoever wrote it.** I did not put this to the human. [A worker's
handover carries no acceptance condition for the node it mints](35-handover-mints-no-condition.md) gives the pen to
the minting worker and [Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md) gives it to the manager under four constraints, and the rule I was
asked about is silent on which. I read it as binding both, on the ground that the party who suffers a short scope —
the worker that meets an unlisted instance, and the checker handed a scope it cannot measure — is the same whichever
hand wrote it, and that node 39's constraint 1 (*demand only what is already fixed*) already makes a manager-written
condition the stricter case rather than the looser one. The risk I accepted: a minting worker on a grilling node
writes a condition for work it will never touch, and it may have run no search at all, in which case rung 3 is the
honest answer and nothing forces it to notice that rung 3 is a confession rather than a pass.

`94.2` `ASSUMPTION` **settled** — **An enumerator's domain is the tree and never the record.** Settled from the files rather than
asked, and I told the human in the question's `SO FAR` that I had settled it this way. [The clause that says no
resolved node changes cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md) already
establishes that a demand quantifying over the record cannot be made self-contained by copying, and node 71's own
read-back applied exactly this distinction to exactly this construction — its quantifications *"are over the **tree**
— the grep, and *no other file is* — which that node permits."* So a condition whose enumerator globs `nodes/` or
`decisions.md` is malformed under a rule that already exists, and I state it rather than deriving it because an
author reaching for a search will reach for the record's own files first.

`94.3` `ASSUMPTION` **settled** — **How far the rule reaches back.** The human said nothing either way and the manager offered it
as mine to state. I settled it in three parts: resolved conditions are out of reach (discharged, nothing left to
fence); open conditions are repaired in place on node 33's audit-but-do-not-repair precedent; and supplying a missing
search is within node 82's permission while *acting* on its output routes by node 82's unchanged test. The
alternative was to surface it as its own node, which I judged wrong because it would leave every author between now
and that node's resolution without an answer to a question my own rule creates. The risk I accepted: the third part
turns on reading *"writing down how the list was got"* as adding no demand, and a stricter reader could hold that a
recorded enumerator constrains a later manager who would otherwise have reconstructed a narrower one.

`94.4` `ASSUMPTION` **settled** — **Node 102's worker's judgement that node 103's sixth site exceeds node 82 was right when
written and is overtaken by its own node resolving.** That worker wrote that repairing
`expedition-precondition/SKILL.md` *"adds a place **and** changes the rule's coverage, where that procedure licenses
adding places and no demand"* — and it wrote that sentence **inside the answer that was about to fix the coverage.**
Node 102 is now resolved, and its answer names that site, quotes the sentence, states that *"having no gate is now
irrelevant to where a flag settles"*, and states the rule that replaces it. So the demand at that place is fixed by a
resolved node, and the amendment would copy node 102's words rather than compose new ones — which is the
justification node 81's amendment already ran on, *"copied across rather than composed here, which is why the
amendment decides nothing."* On that reading it is a widening node 82 licenses. **I am not repairing node 103 and
this is not a resolution of it** — the act is the manager's under node 82's guard 2. What I accepted is the risk that
node 102's replacement rule is stated generally rather than as the precondition contract's own sentence, and a
stricter reader could hold that composing that sentence is authoring.

`94.5` `ASSUMPTION` **settled** — **`/grilling` and `/domain-modeling` were not invoked.** My contract's `## How you grill` says
to invoke them where present, and both are present as `mattpocock-skills:grilling` and
`mattpocock-skills:domain-modeling`. I ran the discipline the contract states in full — one question, a
recommendation I believed, the alternatives named, and every fact the files could give me read rather than asked —
and spent the budget on three measurements instead, which is what actually decided the node. This is a departure from
an instruction rather than a conflict between a method skill and a hard rule, so it is reported here and not under
the conflict clause. **The same departure is already recorded as flag `102.3`, which asked for the judgement back and
which I read as still outstanding**, so this is a pattern across two consecutive grilling nodes rather than one
worker's call, and the human may want to settle whether that instruction is doing any work.

## Interview

### Attempt 1, round 1

**Asked**, in the worker's words:

> Should a condition addressing a defect with instances keep its list of files and additionally state the search that
> produced it — mandatory wherever the scope came from a search, in the same three-rung form node 71 already makes a
> checker use — rather than replacing the list with a predicate?

**Answered**, `verbatim`:

> for 94 ok for recommended

**The option taken**, written by this node's worker and quoted here as it offered it:

> Yes — neither side of the binary as posed. Keep the list, add the search, in node 71's own three rungs, and add one
> residual clause.
>
> **The rule.** Where a condition's scope was derived from a search, that search goes in the condition. The author
> owes exactly one of three, and a condition addressing a defect with instances that carries none of the three is
> **malformed** — which is word for word the ladder you already approved for a checker's findings at node 71:
>   1. **an enumerator** — the command, and what it returned when run;
>   2. **a bounding set** where no command fits — the smallest set that provably contains every instance, and how it
>      was computed;
>   3. **an explicit statement that the scope came from no search** — the work creates a file, or the places *are* the
>      work rather than instances of a defect.
>
> **What keeps the fence doing its job.** Three things, and none of them is trust in the worker: the list stays, and
> so does *"no other file is edited"*, the predicate being written beside the fence rather than in place of it; an
> instance outside the list is **reported, not edited**, so a loose predicate costs one line in a handover rather
> than a wandering commit; and the enumerator has to be **run by the author, while writing**, which moves the
> coverage judgement to the party who already owns it instead of surfacing it after the condition is frozen.

*Not a divergence: the reply takes the worker's own recommendation.*

## Retrospective

*The worker's own text, pasted, handed back as the sixth handover part this effort asks for. Filed as an annotation,
which is why it sits after the node's mandatory sections.*

**What I had to hunt for.** Four things, and the two that decided the node were not in any file.

*The measurements.* Nothing on the record tested whether the predicate shape actually works, so I built the test: the
two greps on node 103's case, and the census of 43 conditions. I looked first at node 82's `### What this does not
settle` bullet, expecting the argument to be there — it carries the framing and the stakes and no measurement at all.
About four minutes of grep produced the three facts the answer rests on. That asymmetry is the node's own subject
arriving in the work.

*That node 71's own condition is already the shape.* This is the find that reframed the node, and I got it by luck.
My node file and node 82 both cite node 71 for the shape it makes a **checker** hand back, so the pointer sent me to
the right file for the wrong reason; I only saw the condition because I read the file whole. Had I read only the
section the citation pointed at, I would have argued the node from first principles and missed the existence proof.

*Node 95's short scope.* Found in the last minutes, by one grep, because my own rule told me to look. Nothing pointed
at it, and it is the strongest single piece of evidence in the answer — the node carrying node 82's rule reproduces
node 82's defect.

**What I read and did not use.** `map.md` in full, and it is the largest read of the node: the destination, the
landing and worktree policy, the code-slot count, the dogfood target, the bar's commands, the review route, the label
vocabulary, the out-of-scope section and eight fog items. Three lines bore on the work — the retrospective preference
and standing writing rules 2 to 4. `decisions.md`, about sixty-five lines, of which roughly eight mattered and I
reached six of those nodes anyway. Node 33 in full: its 31-condition audit across four nodes is a fine artifact and I
used one sentence of it (the repair-none precedent) and one flag (the bar exemption) — the verdict tables themselves
I did not need, though I could not have known that without reading them. Node 102's `## Interview` and its
`## Retrospective`, read after I already had the two paragraphs I needed. Node 71's `## Review` and its correction
round, which were confirmation rather than input.

**What would have made this node easier.** The node file's question is the best-written one I could ask for: it
states the alternative, the counter-argument against its own proposal, and a three-part ask. What it lacks is the one
thing that decided the node — **a count with its enumerator.** It says *"all four recorded shortfalls"*; there were
five by the time I claimed it, and I found two more live ones by grep. A node whose whole argument rests on a set of
instances should carry the search for that set, which is precisely what this node decided — so the node file is an
instance of its own finding, and naming that is cheaper than my rediscovering it.

Second, the spawn's manager notes were the most valuable part of the payload: the live node 102 instance was the
evidence I built the decisive test on, and the note that the third sub-question was the sharpest was right. Neither
was reachable from the files, and the note that they were offered as evidence rather than as a steer is what let me
use them without deferring to them.

Third, a structural one. My contract's `## What you read` sends me to `decisions.md` as a pointer and tells me to
follow the lines that bear on my question. That worked. But a `decisions.md` line says what a node **decided**, and
the thing I needed from node 71 was not its decision but the **shape of its own acceptance condition** — a property
of the node file rather than of the answer, which no index line would ever carry. I do not have a fix for that; I
record it because the same shape will recur wherever a node's value to a later worker is how it was written rather
than what it settled.

**What was stale, wrong, or contradicted something else.**

- **Node 82's closing table, *"The four instances, and what each would have cost under this answer"*, is now five**,
  and the fifth is the one its answer does not reach. My node file inherits the *four* count in its question text.
- **Node 102's worker's judgement that node 103's sixth site exceeds node 82 was true when written and is overtaken
  by its own node resolving** — the sentence sits inside the answer that fixed the coverage it says is unfixed. This
  is a class of staleness nothing on this graph reports: a judgement about what is *not yet fixed*, invalidated by
  the node containing it becoming resolved. Every such sentence is born stale one moment after it is written, and the
  cascade fires on decisions moving rather than on a node's own conditional going true.
- **Two open conditions are short by measurement** (node 95's and node 103's), and nothing reported either. Node
  95's was reported by nobody because its scope came from a worker's `INVALIDATIONS` rather than from a search, which
  is the exact case rung 3 exists to expose.
- **Two consecutive grilling nodes were minted as binaries their own evidence did not support** — node 71
  (*mandatory or owed*) and this one (*predicate or list*) — and both were answered *neither as posed*. Worth a look
  as a minting pattern rather than two coincidences.
- **One thing that was right and is worth recording because a node exists to fix it.** My spawn did **not** list
  `flags.md` among my pointers. Node 82's flag `82.2` records the spawn doing exactly that, and [Narrow the flags.md
  clause in the worker contracts](32-narrow-flags-file-clause.md) is still open, so the flat clause is presumably
  still on disk in five contracts — but the spawning practice has already corrected itself ahead of the contract. I
  read no `flags.md` and nothing was lost.

**The manager's note on the retrospective.** *Not a change to anything above.* Its last point is the manager's own
correction landing: the `flags.md` clause is still on disk in five contracts and node 32 is still open, but every
spawn since node 82's flag has excluded it. Its fourth point — two consecutive nodes minted as binaries their
evidence did not support — is a **minting** defect and therefore the manager's, and joins the promotions it owes off
retrospectives. Its third point, that an index line can never carry why a node file is worth reading, is the one the
manager has no answer for either.

## Annotation: the exemplar this answer rests on is weaker than the answer takes it for

*Filed by the manager from [Whether the checker re-runs a condition's own
enumerator](110-does-the-checker-rerun-the-enumerator.md)'s `INVALIDATIONS`, in that node's own words. **The rule
above is untouched.** Nothing here reaches the three rungs, the three fence-keepers, or the reach-back.*

> One supporting sentence is narrowed, and the rule is untouched. Its measurement 2 says node 71's condition *"is the
> only one on the record that never overflowed"*, offered as the existence proof the rule rests on. That condition's
> recorded return is false and its domain reaches the record, so it is a weaker exemplar than the node takes it for.
> **What this does not touch:** the rule, the three rungs, the three fence-keepers, and the reach-back — the argument
> for recording a search does not depend on the first recorded one being correct, and this node's own measurement is
> that two of four recorded returns were false, which strengthens the case for reading them back rather than
> weakening the case for writing them down.

**Flag `94.2` is the one this bears on hardest**, and it is settled. It bars an enumerator's domain from reaching the
effort's record; the exemplar breaks it, nothing enforced it, and node 110's answer is what puts an enforcer there.
