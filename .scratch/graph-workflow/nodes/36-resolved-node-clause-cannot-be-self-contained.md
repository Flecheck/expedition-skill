# The clause that says no resolved node changes cannot be self-contained

Type: implementation
Status: resolved

## Question

Four of the nine acceptance-condition failures found by [An acceptance condition is self-contained
text](33-condition-is-self-contained.md)'s audit are **one boilerplate sentence**:

- *"No decision on any resolved node changes"* — node 33's condition 8, [What the checker contract owes to
  having been run](31-checker-contract-owes.md)'s condition 4, [Carry the recorded deltas into the shipped
  skill files](26-carry-deltas-into-shipped-files.md)'s condition 4.
- *"Every rule in every contract traces to a resolved node"* — [Write the worker contract
  skills](22-worker-contract-skills.md)'s condition 3, the same demand in the other direction.

**It cannot be repaired by copying, which is the remedy node 33 shipped for every other pointing clause.**
Its content is the whole record: to state it self-containedly a condition would have to carry every decision
the effort has ever made.

There is hard evidence about what it costs. Node 22's condition 3 was handed to **four independent blind
checkers and each declared it not establishable** — before anyone could say why. Node 33's rule now names
why: the demand's content sits outside the text, and no copy can bring the record inside it.

### It is already owed somewhere else, by a party that can answer it

Every worker contract carries this handover part:

```
INVALIDATIONS: <which resolved node your work contradicts, and how>
```

That is the same duty, addressed to the party that **has read the record** and can therefore discharge it.
The condition clause is a duplicate pointed at the party that structurally cannot.

### The fork

- **The clause leaves acceptance conditions**, resting on `INVALIDATIONS` — the reading node 33's worker
  recommends, and the one consistent with the rule it shipped.
- **The clause stays**, and `graph-conventions.md` says which party checks it — which means naming something
  other than the blind checker, and there is no third checking party today.

A grilling node first is defensible: four resolved nodes wrote this clause deliberately, so removing it from
the standard form is not obviously a repair. Whoever spawns this decides which, and says so.

### Landing

`graph-conventions.md`'s `### `## Acceptance condition`` section, the same section node 33 just changed. A
later commit against that file is lawful — the landing policy forbids a second commit against one **node**,
not against one **file**.

Reported by [An acceptance condition is self-contained text](33-condition-is-self-contained.md)'s worker.

### ~~The acceptance condition is owed~~ **Now written, below**

~~Written by whoever spawns this, and it may not be claimed without one.~~ **Written by the manager at this
node's spawn**, there being no spawning node's worker to write it — this node was minted by [An acceptance
condition is self-contained text](33-condition-is-self-contained.md)'s worker as a report rather than as a
piece of that node's own work, and a handover carries no condition to mint one with anyway, which is [A
worker's handover carries no acceptance condition for the node it
mints](35-handover-mints-no-condition.md). So it carries [What the checker contract owes to having been
run](31-checker-contract-owes.md)'s standing warning in full: it is manager-written, and it should be read
against the files before it is trusted.

### The kind is `implementation`, and not a grilling node first

The `## Question` above leaves that call to whoever spawns this — *"A grilling node first is defensible:
four resolved nodes wrote this clause deliberately, so removing it from the standard form is not obviously
a repair."* Taken as `implementation`, on three grounds.

**The clause was copied forward, not decided four times.** [An acceptance condition is self-contained
text](33-condition-is-self-contained.md)'s audit calls it *"boilerplate on every implementation condition
this map has written"*. Boilerplate carried forward is one act repeated, not four deliberations, and what
would make it four is a node that argued for it — none did.

**The fork has an evidenced recommendation available**, so it does not need the human's live judgement to be
decided. And where the worker finds it holds no recommendation it believes, its contract already gives it
the raise: the human is reached at the cost of one message rather than a whole HITL node, and the answer
lands on this node either way.

**The human is the scarce resource.** Spending a grilling slot to decide whether one sentence leaves a
standard form inverts the map's own standing preference — the more so when the sentence has already cost
four blind checkers a verdict each.

## Acceptance condition

1. **The demand is named in full, and the shipped file says what becomes of it.**
   `.claude/skills/expedition/graph-conventions.md`'s `### `## Acceptance condition`` section states
   whether an acceptance condition may carry a demand of this shape, and the answer is recoverable from
   that file alone. Two wordings of the demand exist and both are meant:

   - *"No decision on any resolved node changes."*
   - *"Every rule in every contract traces to a resolved node."*

   Each holds the work against decisions recorded across the whole of an effort's record: the first that
   the work contradicts none of them, the second that every rule in it descends from one.

2. **The file says why this demand is not the case that section already covers.** As it stands, that
   section tells whoever writes a condition depending on material held elsewhere to **copy that material
   into it**. This demand cannot be repaired that way — its content is every decision the effort has ever
   made, so no copy brings it inside the condition. Whichever way condition 3 goes, the file states that
   much, in the document's own voice: no node named, no history, no rejected alternative.

3. **One of these two is true of the shipped text, and it is legible which.**

   - **The demand does not belong in an acceptance condition.** Then the section says so, and says where
     the duty is discharged instead rather than dropping it silently. Something already carries it: a part
     of every worker's handover, addressed to a party that has read the record. In the implementation
     worker's contract it reads `INVALIDATIONS: <which resolved node your work contradicts, and how>`, and
     the other four worker contracts carry the same line with *your facts* or *your answer* in place of
     *your work*.
   - **The demand may stay.** Then the section names the party that establishes it — and that party cannot
     be the checker, for the reason the same section already gives: the checker is handed the condition as
     text, has not read the node, and does not read the record. If the honest answer needs a checking
     party that does not exist today, that is a decision reaching past this document. **Raise it rather
     than inventing one.**

4. **What the file says is about the shape of the demand and not about those two sentences.** A later
   writer holding a third wording of the same thing — *the work is consistent with every decision so far*,
   *no rule here is unsupported by the record* — can tell from the file alone which side of the line it
   falls on. A rule that only catches the two wordings quoted above does not satisfy this.

5. **No existing acceptance condition is repaired, and no graph file changes.** Four acceptance conditions
   in this effort's own graph carry the clause; three sit on nodes that are resolved and one on a node
   that is open, and fixing them belongs to another commit. Where you conclude a repair is owed somewhere,
   report it under `NEW NODES` and write none of it.

6. **Only `.claude/skills/expedition/graph-conventions.md` changes.** `CONTEXT.md`, the five
   `.claude/skills/expedition-<type>/SKILL.md` worker contracts and
   `.claude/skills/expedition-checker/SKILL.md` are untouched: the contracts are the live territory of
   three other open nodes, and a second commit against one of them from here would collide. Where you
   conclude the glossary or a contract also needs a word about this, report that under `NEW NODES` too and
   write none of it.

7. **Rewriting a sentence of that file in place is permitted, and text may be deleted from it.** One of
   this repo's standing preferences reads *"An in-place update never deletes. When any file in the graph
   is edited — a node or this map — superseded text is marked as superseded and left where it is"*. That
   rule governs an effort's own four files. `.claude/skills/expedition/graph-conventions.md` is product,
   so it is edited as ordinary code and carries no struck-through text.

8. **The bar for this repo, in full.** `graph-agent` has no build, no tests, no formatter and no CI —
   nothing to invoke — so the bar is entirely its non-command half: the project's coding principles and
   naming discipline, the standing preferences in `map.md`'s `## Notes`, `CONTEXT.md`'s `_Avoid_` lines,
   and these conditions. That is a complete bar, not a deficient one.

## Answer

**`graph-conventions.md`'s `### `## Acceptance condition`` section gains two paragraphs, and the demand is
ruled out of acceptance conditions entirely.** Sixteen lines inserted, nothing deleted, one file. They sit
between the copy remedy they are the exception to and the manager's *not repaired on the way to the
checker* rule, so the section now reads: the rule, the boundary and the copy remedy, the one demand
copying cannot repair, and then what the manager does with a defective condition either way.

**The fork was taken as *the clause leaves acceptance conditions*.** The shipped text states it as a
prohibition — a condition may not hold the work against every decision the effort has recorded, in either
direction: that the work contradicts none of them, or that everything in it traces back to one. Both
boilerplate wordings are quoted in the file, plus a third paraphrase, so the two that exist today are
unambiguously covered and are visibly examples rather than the rule.

**The load-bearing call is where the line was drawn: a demand that *names* material held elsewhere versus
one that *quantifies over the record*.** That is what makes the rule about the shape rather than about the
two sentences. Copying repairs the first because there is a bounded thing to bring inside the text; it
cannot reach the second, because there is no bounded material and what there is grows every time a node
resolves — so even a complete copy made at writing time goes stale before the check. A later writer with a
fresh wording applies that one test.

**A carve-out was written to stop the new prohibition being over-read: a demand about what changed in the
tree stays permitted.** *No file under `.scratch/` changes* is answerable from the diff whatever those
files decided, and it is the near-miss a real writer hits immediately — this node's own conditions 5 and 6
are of that shape. It restates the path permit two paragraphs above in the record's own terms rather than
adding a new permission.

**One sentence was weakened for accuracy after being written.** The first draft said `INVALIDATIONS` is
*answered by a party that has read the effort's own files*. A worker reads its node, `map.md`, and only the
sections of `decisions.md` its spawn names — so that overclaimed. The shipped wording is *answered by the
party that built the work and may read the record to see what it touches*, which is the true asymmetry:
the worker may go and read, the checker may not and does not.

**Four things were deliberately not written.**

- **No checking party was invented.** Condition 3's second branch would have needed one and there is none
  today; taking the first branch removes the need rather than inventing it.
- **Nothing about the manager as residual checker.** [An acceptance condition is self-contained
  text](33-condition-is-self-contained.md) established that the manager is the residual checker of
  anything a condition addresses to a party that cannot see it, and `map.md` records it as a requirement
  on the manager's own skill. With this clause gone from conditions there is no residual for the manager to
  hold, so this document says nothing about it.
- **`CONTEXT.md` is unchanged and no term moves.** The *Acceptance condition* entry says what one is and
  who writes it; self-containment and its limits are properties of how one is written, which is this
  document's job. Same reading node 33 reached.
- **The four existing conditions carrying the clause are untouched**, and no contract file is touched.

**The honest cost of the choice, stated so a later reader does not have to find it.** The duty's new home
is checked by nobody: the five contracts ask a worker to *report* `INVALIDATIONS`, not to go and look, and
nothing says how much of the record a worker is expected to hold its work against. That is strictly better
than where it was — four independent blind checkers each spent a verdict on node 22's condition 3 and each
declared it not establishable — but it is not enforcement, and it is the first new node below.

**The operative-why clauses rest on settled precedent rather than a fresh judgement.** [Write the graph
conventions document](21-conventions-document.md)'s *instructions only — no reasoning, no rejected
alternatives, no history* permits a statement of what a rule protects, which is flag `33.1`, settled by the
human at node 33's gate on this same section. The new text names no node, no history and no rejected
alternative.

### The two nodes this surfaced

The worker reported both; the manager's disposition of each is in `## Review` below.

```
name:     Nothing tells a worker to hold its work against the record
kind:     grilling
question: The record-wide demand has left acceptance conditions, and `INVALIDATIONS` on
          the handover is now the only thing carrying it. The five worker contracts word
          it as a report — "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else
          reports them" — with no instruction to go and look and no statement of how much
          of the record a worker is expected to read to answer it. A worker reads its node,
          `map.md`, and only the `decisions.md` sections its spawn names, so it cannot hold
          its work against the whole record either. Is `INVALIDATIONS` a duty to check or
          only to report what surfaced while working? If the former, against what — and
          does the spawn have to hand the worker more of the record than it does today?
          Nothing checks it in either case, which was also true of the clause it replaces.
blockers: none. Lands on the five `.claude/skills/expedition-<type>/SKILL.md` contracts,
          which are the live territory of other open nodes — so this must not be written
          from here, and whoever takes it collides with them unless they are sequenced.
```

```
name:     Repair node 31's acceptance condition before it is claimed
kind:     precondition
question: [What the checker contract owes to having been run](31-checker-contract-owes.md)'s
          condition 4 is the one instance of the clause on a node that is open and unstarted,
          so revision-in-place reaches it and no supersession is needed. It fails twice per
          node 33's audit: the record-wide clause, now ruled out by this node, and "the
          glossary-does-not-travel problem" whose content is only in node 29, which is node
          33's copy remedy. Both repairs are to one clause on one node.
blockers: none. The three other instances — node 33's condition 8, node 26's condition 4,
          node 22's condition 3 — sit on resolved nodes whose work is done and checked, so
          they are record rather than live text and no repair is owed on them. Annotating
          node 31 in place may be cheaper than a node at all; that is node 33's gate's own
          precedent for this shape and it is the manager's call, not mine.
```

Nothing is owed to `CONTEXT.md`: no term moved, and the *Acceptance condition* entry stays true as
written.

**`INVALIDATIONS`: none.** One near-miss worth naming so it is not re-derived: [Write the worker contract
skills](22-worker-contract-skills.md)'s condition 3 was the standard its work was judged against, not a
decision its `## Answer` made, and this rule explains why its four checkers could not establish it rather
than contradicting anything it decided. Same for nodes 33 and 26 — the clause lived in their conditions,
never in their answers. No resolved node decides that a condition must carry this demand.

## Flags

`36.1` **· settled** `ASSUMPTION` — **the fork was decided alone rather than raised.** The `## Question` left the choice
between the clause leaving acceptance conditions and the clause staying with a named checking party, and
noted a grilling node first was defensible. Taken as the first, on node 33's recommendation plus the hard
evidence beside it — four independent blind checkers on node 22's condition 3, each declaring it not
establishable — and because the second branch needs a checking party that does not exist, which the
condition itself says to raise rather than invent. No raise was opened: the recommendation is one I
believe, the reach is channelled into `NEW NODES` by conditions 5 and 6, and the human sees the whole of it
as a sixteen-line diff at the gate.

`36.2` **· settled** `ASSUMPTION` — **the tree-versus-record carve-out is mine and no node asked for it.** *A demand
about what changed in the tree is a different thing and stays permitted* adds a sentence to a document
whose standing preference is short prose. Judged worth the line because the prohibition reads as catching
file-scoped clauses like *no graph file changes* — two of this node's own conditions — and because
condition 4 is a legibility demand that this sentence materially serves. It grants nothing the path permit
two paragraphs above did not already grant.

## Review

### Check 1 — `PASS`

Blind. Handed the acceptance condition as extracted text, the bar as [map.md](../map.md) records it, one
work path, and the name of the work. Every one of the eight conditions was established and named: the
prohibition and its two quoted wordings at lines 131–139 of the shipped file, the copy-cannot-reach clause
at 132–135, the route taken legibly at 145 (*"So the demand belongs on the handover and in no
condition"*), and conditions 5, 6 and 7 from `git status --porcelain --untracked-files=all` and
`git diff --stat` — two paths, nothing untracked, 16 insertions and 0 deletions.

**Nothing was reserved as not establishable.** That is the first check in this effort where the manager
held no residual: node 33's condition 6 addressed its deliverable to a party the checker is not given, and
three separate clauses of it came back unestablished. This condition put every demand in a file, so the
whole of it was checkable by the party it was written for.

**It verified the discharge site rather than taking the file's word for it.** Condition 3's first branch
requires the shipped text to say where the duty goes instead; the checker went and confirmed
`INVALIDATIONS` is present in all five worker contracts and **absent from the checker's own**, so the
worker-versus-checker asymmetry the new paragraph rests on is factually true.

**It tested condition 4 by trying wordings the condition did not give it** — *no rule here is unsupported
by the record* (caught), *consistent with the decision at node 21* (not caught, and correctly falling to
the pre-existing copy rule), *no rule contradicts the three decisions quoted below* (permitted). A rule
that only caught the two quoted sentences would have failed, and this is how it established that one
did not.

**Three hard claims and four judgement calls came out of the reviewing skill, and it dismissed every one
with a reason rather than waving them off.** The one worth keeping is that it disagreed with its own
sub-agent about *"may read the record"* overstating the contracts, and settled it from the files: all five
contracts read `decisions.md`, which is one line per resolved node and therefore the index of the whole
decision record, and only `flags.md` is withheld. The asymmetry holds absolutely — the worker reads at
least the index of all of it, the checker none. It also passed on one thing it did not treat as a finding:
*the record* has no glossary entry, though `expedition-checker/SKILL.md` already uses the phrase in this
sense, and it noted that condition 6 makes any glossary work a `NEW NODES` item rather than an edit.
**Manager verification of that:** the worker's handover reports `CONTEXT.md` unchanged and states why, so
the question was reached and answered rather than missed.

**A blind checker preserved its blindfold *through* delegation, which is the second answer this effort has
seen to the same problem.** It found the same reviewing skill node 33's checker found, and where that one
**declined to invoke it** — *"it runs its axes in spawned sub-agents that would be handed none of that and
would go looking, including into the record"* — this one **invoked the Standards axis with the standards
and the smell baseline pasted into the sub-agent**, and left the Spec axis unrun on the same ground as
before: that axis holds work against an originating document, and its search order points into
`.scratch/`, which is the record. Two checkers, one uncovered case, two different correct answers. Carried
to [What the checker contract owes to having been run](31-checker-contract-owes.md) item 6, which had only
the first.

### Gate — `approve`

The human's reply, `verbatim`: *"approve"*.

The outcome was named. The manager had asked for one to be named rather than inferred — *"please name one so I
don't have to read it out of context like last time"* — after node 33's gate arrived as *"you can continue"*
and had to be read as `approve` by the manager and recorded as a reading. **Asking for the word cost one
clause of the payload and removed the reading entirely**, which is worth carrying into the manager's skill:
where the reply is a choice among named outcomes, the payload asks for the name.

Both flags settled as recommended — `36.1` and `36.2`. All four dispositions carried as recommended:

- **[Nothing tells a worker to hold its work against the
  record](37-invalidations-is-not-a-check.md) created**, as the worker reported it. It is the honest cost
  of this node's own answer: the duty left acceptance conditions and its new home is checked by nobody.
- **The worker's second new node was not minted.** Its own text said the call was the manager's —
  *"Annotating node 31 in place may be cheaper than a node at all"* — and [What the checker contract owes
  to having been run](31-checker-contract-owes.md) is open and unstarted, so revision-in-place reaches it
  and a whole `precondition` node for one clause is overkill. Its condition 4 is annotated there instead.
- **Node 31's item 6 gains this check's answer**, delegation-with-givens-pasted-in beside node 33's
  decline-to-invoke.
- **The `FLAGS` two-caps problem is annotated onto [A worker's handover carries no acceptance condition for
  the node it mints](35-handover-mints-no-condition.md)** rather than minted, that node already being the
  case of a handover part naming one artifact where the graph needs two. Flag `33.4` recorded the defect
  and is settled; it recurred here, the manager authoring both index lines again, and nothing owned the
  fix until now.
