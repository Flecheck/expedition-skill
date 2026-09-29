# What keeps the shipped files consistent when a decision changes a term

Type: grilling
Status: resolved

## Question

A resolved node changes a word or a rule. Which shipped files have to move, and what makes sure every one
of them does?

Nothing answers this today. The workflow has a list of decisions owed to **one** file and no list at all of
the files a decision might be owed to.

### It has failed three times, each time one level further out

1. **[map.md](../map.md)'s delta list tracked `graph-conventions.md` alone.** Eight deltas accumulated
   against it correctly. Then [What is recorded when the human takes an option as
   offered](25-recording-an-option-taken.md) invalidated one sentence in **two of the six worker
   contracts**, and the list had nowhere to put it — which is why [Carry the recorded deltas into the
   shipped skill files](26-carry-deltas-into-shipped-files.md) was minted as a node instead of a tenth line
   on the list. The map recorded the lesson at the time: *"A delta list works until a delta lands on a file
   the list does not track."*
2. **That node's acceptance condition named three files** — the document and the two contracts — written by
   a worker that had just done the analysis and by the manager adding a fifth condition on top.
3. **The checker found a fourth.** Blind, tracing condition 4, it reported that
   [`CONTEXT.md`](../../../CONTEXT.md) had become the stale side: its *Acceptance condition* and *Flag*
   entries still described a worker flagging a wrong condition, where the fifth delta had made that a
   **raise**. `graph-conventions.md` declares the glossary authoritative for the terms it uses, so the
   shipped document was pointing at a file that contradicted it. The human put it in scope with one word,
   `fix`.

Three for three, and the general conclusion was never drawn — only the miniature version of it, once, about
one list.

### Why the obvious answer is not obviously right

*"Keep a list of the shipped files"* is the first thing anyone reaches for, and it is what just failed three
times — each failure being a list that was correct about the files it knew. A list is only as good as
whoever remembers to extend it when a file joins the set, and the file that joins is exactly the one nobody
was thinking about.

What the answer has to decide, then, is whether the mechanism is a **list**, a **check**, or a **procedure**:

- A **list** in `map.md` or the conventions document, naming the product files — cheap, and has failed.
- A **mechanical check**, joining a decision to the files that must carry it. The eight existing checks are
  all decidable without judgement; this one may not be, which is the boundary [Graph file
  format](13-graph-file-format.md) drew between a script's work and the cascade's.
- A **procedure** at resolution: the node that changes a term names the files it invalidates. This is
  nearly free, since a handover already reports `INVALIDATIONS` — but `INVALIDATIONS` is defined over
  **resolved nodes**, not over product files, and no worker has ever reported one.
- Or the **cascade** ([Cascade pass mechanics](15-cascade-pass-mechanics.md)) already owns this and only
  ever gets described over graph edges. If a cascade scans code for decisions that have moved, a shipped
  prose file is code.

### Two things the answer must not miss

**The glossary does not travel.** `CONTEXT.md` sits at the repo root, not under `.claude/skills/`, so
copying the expedition skills to another repository carries none of it — while `graph-conventions.md`
declares it authoritative for every term. That is the same defect as the *"invoke if present"* patch on
method skills, recorded in [map.md](../map.md)'s fog under *how the workflow reaches a repository that is
not this one*, and this node is where it becomes concrete rather than adjacent.

**The failure was found by the party with the least context.** Not by the manager holding the delta list,
not by the worker that had just read every delta — by a **blind checker** tracing a condition that told it
to account for every changed line. Whatever the mechanism turns out to be, that is a datum about where this
class of miss is visible from.

Feeds the **manager's own skill**, and possibly the cascade.

## Annotation: largely absorbed, and what is left of it

Added by [Cascade pass mechanics](15-cascade-pass-mechanics.md)'s worker, which named this node in its
consequences and said it should be updated in place, this node being open and unclaimed. In its words:

> Of its four candidate mechanisms, *the cascade already owns this* is now answered: a shipped prose file
> is code for this pass, and the finding mechanism is triage plus the widened handover. What triage cannot
> reach is what is left of that node — the glossary not travelling to another repository, and a term
> shipped with no `CONTEXT.md` entry at all, which the manager has hit twice while filing acceptance
> conditions at nodes 41 and 42. Neither is a decision that moved, so neither is reachable from a resolved
> answer.

**The manager's note beside it, not the worker's.** The two absences that worker cites are `FRICTION` at
[Ship the FRICTION flag and the self-edit disclosure duty](41-ship-the-friction-flag.md) and `ground rules`
at [The checker's spawn carries the effort's ground
rules](42-checker-spawn-carries-ground-rules.md) — both found by a claim-time audit rather than by anything
that checks. A third belongs here now and was found the same way: [map.md](../map.md) says of this effort's
ground rules both that it *"declares neither"* optional block and that *"its ground rules are the standing
preferences above"*, and that contradiction became load-bearing the moment node 42 made the ground rules a
checker's given, since the manager must now decide what they are before every check.

## Annotation: a second worker found this node's glossary defect independently, the same day

*Filed by the manager while this node's own interview was live.* [Review every shipped file against
`/writing-great-skills`](47-review-shipped-skills.md)'s worker — a research worker reading a different set of
files, with no knowledge of this node's interview — reported the same defect and offered it as a new grilling
node, adding that *"the manager may prefer to fold this into"* this one. It is folded here and **no node was
minted for it**, because two blind agents converging on one defect from different evidence belongs on one node
rather than split across two.

Its words, which are this node's own finding arrived at independently:

> `graph-conventions.md:5` points at a glossary by bare filename, outside the skill tree. *"Terms are used
> exactly as the glossary (`CONTEXT.md`) defines them."* `CONTEXT.md` lives at the repo root, not under
> `.claude/skills/`, so copying the skill tree to another repository carries the pointer and not its target.
> **Inference:** it does not merely dangle there — `/domain-modeling`, one of the skills the grilling contract
> itself points at, creates a root `CONTEXT.md` as *that* repo's own domain glossary, so the pointer resolves to
> the wrong file rather than to nothing.

**Two facts it adds that this node's worker did not hold.** The pointer's exact site is
`graph-conventions.md:5`. And — this is the sharper one — **no `SKILL.md` points at `graph-conventions.md` at
all**: `grep -rn "graph-conventions\|CONTEXT\.md\|wayfinder-divergences" .claude/skills/*/SKILL.md` returns
nothing, so the file that carries the authoritative-glossary sentence is itself reached by no pointer from
anywhere. The record already held this twice, at node 22 line 251 and node 35 line 108. It bears on this node's
`ASK` part 1: moving the glossary into `.claude/skills/expedition/` puts it beside a file that is itself
unreachable, so *reachable inside the shipped set* and *reachable by a worker* are not the same property, and
part 1 secures the first without the second.

Its three determined wording repairs were bundled into one implementation node rather than landing here; the
positive-pairing repair for *"`flags.md` is not yours. Leave it unread"* stays with [Narrow the flags.md clause
in the worker contracts](32-narrow-flags-file-clause.md), as that worker judged.

## Interview

### Attempt 1 — routing key `graph-workflow/29/a1`

**Q1, from the worker**, pasted as it wrote it. **Held, not yet put to the human** — it arrived while [Who
writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md)'s question was going to the human, and the standing rule is
one live question with the rest named behind it. Recorded on disk at arrival time so that a dead worker still
leaves the question banked.

```
NODE:          What keeps the shipped files consistent when a decision changes a term

ABOUT:         This node decides what keeps the eight shipped expedition skill files consistent with
               the vocabulary they are written in. Node 15 (the cascade) just answered the half where
               a decision moves and shipped files go stale: a triage agent at every resolution. What
               is left is the half no moving decision can reach — the glossary itself. It is being
               decided now because two terms are already shipped with no glossary entry, both found
               by hand, and nothing in the workflow would ever have told us.

SO FAR:        WHAT I READ. My node, its annotation from node 15, the map, all 33 lines of
               decisions.md, `CONTEXT.md`, all eight shipped files, and nodes 15, 41, 42, 45.

               THE GEOGRAPHY. The glossary is `CONTEXT.md` at the repo root — 40 terms, each with an
               `_Avoid_` list of the synonyms we refused. The product is eight files under
               `.claude/skills/expedition*/`. The first rule in the shipped `graph-conventions.md` is
               "Terms are used exactly as the glossary (`CONTEXT.md`) defines them."

               THE SAME DEFECT, THREE TIMES — each a shipped file requiring something that lives
               outside the shipped set:
               1. Copy `.claude/skills/` to a work repo and that pointer carries none of the
                  glossary. Worse than dangling: `CONTEXT.md` at a repo root is the
                  `/domain-modeling` convention, so the pointer silently resolves to THAT repo's own
                  glossary and tells the reader to use its terms exactly.
               2. A term ships with no entry at all. `FRICTION` (node 41) and `ground rules` (node
                  42, used by six of the eight shipped files). Both found by the manager reading an
                  acceptance condition by hand, neither by anything that checks.
               3. Node 42 just made "the effort's ground rules" a required given in every checker's
                  spawn — and the map says of this effort both that it "declares neither" optional
                  block and that "its ground rules are the standing preferences above". The manager
                  has been deciding what they are on its own judgement before each check. That one is
                  the map rather than a shipped file, and it is my second question.

               WHY NOTHING CATCHES THIS, WHICH IS THE FINDING THAT DECIDES IT. The blind checker's
               contract carries a hard rule: "A property nobody stated is not a finding." The duty to
               add a glossary entry is stated nowhere, so the one party that reads a shipped file
               cold is forbidden from reporting it. The single time it did catch this class (node 26,
               where `CONTEXT.md` had gone stale) it was because that node's acceptance condition
               happened to tell it to account for every changed line.

               SETTLED ON MY OWN AUTHORITY, both returned as flags: that node 15's triage genuinely
               cannot reach any of this (it fires when a decision moves, and a term is missing from
               the day it ships); and that the eight mechanical checks are the wrong home, the map
               having measured twelve false results from scans over prose.

               COUNTED RATHER THAN GUESSED: 26 markdown links in the graph files point at the root
               `CONTEXT.md` path. `/domain-modeling`'s own format documents a multi-context shape —
               a root `CONTEXT-MAP.md` naming per-directory `CONTEXT.md` files.

ASK:           Is this the mechanism? Three parts.

               (1) THE GLOSSARY JOINS THE SHIPPED SET. It moves to
               `.claude/skills/expedition/CONTEXT.md`; the repo root gets the `CONTEXT-MAP.md` that
               the convention uses to name where a context lives; and the root `CONTEXT.md` stays as
               a one-line forward pointer, so all 26 existing links still resolve. Copying
               `.claude/skills/` then carries the vocabulary with it, and a shipped file's
               authoritative pointer resolves inside the shipped set.

               (2) THE GLOSSARY STATES ITS OWN COMPLETENESS, in one paragraph at its top: a term the
               files that declare it authoritative use in this vocabulary has an entry here, and
               coining the term and writing its entry are one change. That paragraph is the whole
               finding mechanism.

               (3) NOTHING IS ADDED to the mechanical checks, and nothing to any acceptance
               condition.

RECOMMENDED:   Yes to all three.

               Part 2 is the part that does the work, and it is one paragraph. It converts "a term
               with no entry" into a stated property, which is precisely what the blind checker is
               permitted to report — so the finder becomes the party with the least context, which is
               my node's own best datum about where this class of miss is visible from. Node 15 set
               the checker aside on coverage grounds, correctly for its subject: a checker runs only
               on implementation nodes, so it covers nothing across a run of decision nodes. That
               objection does not reach this class. A term can only reach a shipped file through an
               implementation node, and every implementation node runs a checker. Coverage is
               complete here, where triage's is zero.

               It also costs nothing anyone has to remember. It travels on the bar — "whatever else
               the repo itself demands" — which reaches the checker by its own route, so no
               acceptance condition has to mention it and the manager authors nothing. That is the
               answer to your standing practice of leaving these unrepaired rather than writing the
               entry yourself: under this, the rule demands it of the worker and the manager stays
               out of it. And it is cheap to check, because the checker holds the diff: what it has
               to consider is the terms this work added, not every term in the file.

               Part 1 makes part 2 true anywhere rather than only here, and it repairs the thing the
               map already calls the anti-drift mechanism — the `_Avoid_` lines are what stop a
               settled term from drifting back, and today none of them travel. The name stays
               `CONTEXT.md` because the convention that owns the file names it that. Two things
               beside it: node 14 raised a flag, still live, that the glossary "passed no checker and
               no gate" because a grilling node wrote it — this puts it under both for the first
               time; and node 41, which ships `FRICTION`, should land after this so that its worker
               owes the entry.

               Cost: one implementation node, one commit, three files. Nothing recurring.

ALTERNATIVES:  - Vendor the vocabulary into each contract instead of shipping one glossary. Each
                 already carries its own "Words used exactly" block, so the precedent exists. Set
                 aside: the 40 `_Avoid_` lines are the half that stops drift and would not travel,
                 and seven copies of a definition is the drift this node is about.
               - Leave the glossary at the root and only fix the pointer's wording. Set aside: the
                 file still does not travel, which is the defect.
               - A ninth mechanical check over the shipped files. Set aside: matching "a term" in
                 prose is the class of scan the map records twelve false results against.
               - Put the duty in every acceptance condition. Set aside: it is the condition that
                 omitted it, twice, and you have ruled that the manager may not repair one.
               - Put the rule in `graph-conventions.md` rather than in the glossary. A real option;
                 set aside because a checker that finds the glossary should find the rule with it,
                 and one of the two files is guaranteed to reach it.
               - Let the manager's claim-time audit be the finder, since it found both. Set aside: it
                 found both and repaired neither by design, which is the state that is failing.
```

**The manager's notes on this question, to travel with it when it is put to the human.**

1. **Two counts are stale, both in the same direction.** `CONTEXT.md` holds **50** terms, not 40; and
   `map.md`'s figure of *"forty terms"* is itself the stale one this worker read. The `_Avoid_` argument is
   unaffected and gets stronger.
2. **A ninth mechanical check now exists**, from [Nothing checks that a part a checker left uncovered was ever
   established](45-nothing-checks-an-uncovered-part.md), which was at its checker while this question was being
   written. Part 3's *"nothing is added to the mechanical checks"* is still a coherent choice; the count in the
   alternative it sets aside is now nine.
3. **The independently-confirmed half is part 1**, and it is confirmed by a worker that never saw this node —
   see the annotation above. What that worker adds is that `graph-conventions.md`, the file carrying the
   authoritative-glossary sentence, is **itself reached by no pointer from anywhere**. So part 1 makes the
   glossary reachable *inside the shipped set* without making it reachable *by a worker*, and those are two
   properties rather than one.
4. **A live upstream fact bears on part 1's naming choice.** The plugin whose `/domain-modeling` convention part
   1 leans on was renamed and rewritten upstream between two of this effort's sessions. Leaning on a foreign
   convention for a filename is exactly the dependency [What a contract may name as a method
   skill](51-what-a-contract-may-name.md) exists to decide, and this is evidence for that node rather than an
   objection to part 1.

**A1, from the human**, `verbatim`: *"ok for 29"*.

The option it points at, quoted from Q1's `RECOMMENDED` and attributed to the worker that wrote it: *"Yes to
all three."* So all three parts are assented to as offered — (1) the glossary moves to
`.claude/skills/expedition/CONTEXT.md`, the repo root gains the `CONTEXT-MAP.md` the convention uses, and the
root `CONTEXT.md` stays as a one-line forward pointer so all 26 existing links still resolve; (2) the glossary
states its own completeness in one paragraph at its top, which is the whole finding mechanism; (3) nothing is
added to the mechanical checks and nothing to any acceptance condition.

**No divergence.** The reply takes the recommendation whole, names no alternative and asks for no change, so
nothing here is `paraphrase`. Recorded under [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md). The manager's four notes above travelled with the question and
their reply did not single any of them out; the two stale counts are corrections of fact rather than options,
so they bind the answer regardless.

**Q2, from the worker**, pasted as it wrote it.

```
NODE:          What keeps the shipped files consistent when a decision changes a term

ABOUT:         Second and last question on this node. My first settled the shipped-file half: the
               glossary joins the shipped set and states its own completeness, so the blind checker
               becomes the finder. This one settles the third instance of the same defect, which is
               in `map.md` rather than in a shipped file: node 42 made "the effort's ground rules" a
               required given in every checker's spawn, and the map does not supply them in the form
               that given needs. It is decided now because every checker spawn from here needs it,
               and four implementation nodes are queued.

SO FAR:        WHAT A1 SETTLED, and I am not reopening it: the glossary moves into
               `.claude/skills/expedition/`, states in one paragraph that a term used by the files
               declaring it authoritative has an entry in it, and nothing is added to the mechanical
               checks or to any acceptance condition.

               CORRECTIONS I ABSORBED, all verified myself: the glossary holds 50 terms and 40
               `_Avoid_` lines, not the 40 terms I said — and `map.md`'s own "forty terms" is that
               same stale figure, so my answer will correct the map too. There are nine mechanical
               checks, not eight, node 45 having landed check 9 as commit `5a4ae83`. And the standard
               this effort holds its own prose against was renamed and rewritten upstream from
               `/writing-great-skills` to `/writing-for-agents`, which node 54 established.

               THE CONTRADICTION ITSELF. `map.md` says of this effort both that it "declares neither"
               of the two optional blocks — ground rules, and a source hierarchy — and, in the same
               sentence, that "its ground rules are the standing preferences above". Those cannot
               both be acted on. The shipped checker contract offers the manager two branches and no
               third: hand over the ground rules as text, or "where the effort declares none there is
               nothing to give".

               WHAT IT HAS COST SO FAR. At node 42's own check — the first spawn bound by the rule it
               shipped — the manager had to decide what this effort's ground rules were before it
               could hand them over, and it passed the subset of the standing preferences it judged
               to be standing constraints, withholding the rest. That worked, and it is the manager
               deciding a standard per check, with no record of what was handed over. Every
               subsequent check repeats the judgement, and two checks need not receive the same text.

               WHY IT IS ON THIS NODE AT ALL. It is the same defect my answer is about, from the
               other side: a shipped file requiring something that lives outside the shipped set. A1
               fixed the case where what is required should travel with the files. This is the case
               where what is required is the effort's to declare, and the effort did not declare it
               in the form the requirement needs. My answer holds both halves of that rule, so this
               is the second half's live instance.

               WHAT I SETTLED MYSELF and will return as a flag: my own new rule from A1 does not go
               in this block. Once it ships, the glossary states it and the bar carries it to the
               checker, and a second home for one rule is the drift this node exists to stop.

ASK:           Should `map.md`'s `## Notes` declare this effort's ground rules as an explicit block —
               marking the "declares neither" sentence superseded in place — so that the manager
               copies that block as text into every checker spawn and adds nothing of its own? And
               is this the list?

               1. Nothing in the shipped files may assume this repo, this machine, or a toolchain.
                  Prefer properties that are discovered over commands that are declared.
               2. Each shipped worker contract stands alone as a file, rather than depending on any
                  skill being invocable.
               3. The human talks only to the manager. No agent the workflow spawns addresses the
                  human directly, and nothing in the files may tell one to.
               4. Prefer short, simple prose that can be changed later over machinery built for
                  predicted needs. Reserve heavy design for the hard-to-reverse core.
               5. Prose deliverables are held against the `/writing-for-agents` standard, which is
                  specific to this repo, is never shipped, and is located by name in the
                  `mattpocock-skills` plugin rather than by path.

RECOMMENDED:   Yes, and those five.

               Each is drawn from a standing preference the map already holds, and each passes the
               test node 42 shipped for what may travel to a blind checker: a standing constraint,
               true of any node's work, rather than an account of what happened. That test is what
               keeps most of the map out of the block — the manager-context findings, the token
               measurements, the landing policy's history are all accounts, and a checker holding
               them would be reading the record it is kept blind from.

               Item 5 is the one that most needs to be in there and is least likely to arrive by
               accident. The map says of that standard that it "belongs here more than any of the
               others do, because this effort's product **is** skill files" — and a blind checker
               reads no map, so today it reaches one only if the manager happens to pass it. Its name
               moving under us in one day is itself the argument for naming it in one declared place
               rather than re-deriving it per spawn.

               Two things follow that are the point of the change rather than side effects. The
               manager stops authoring a standard per check: it copies a block the human approved,
               and where a check needs a constraint the block does not hold, that is a raise under
               node 28's rule rather than the manager's own judgement. And the second optional block
               stays genuinely undeclared — all sources here are authoritative — so the map says
               "declares one of the two" rather than "neither".

               What I am not claiming: that these five are everything. They are what the map's own
               text will support today, and the block is appended to like any other.

ALTERNATIVES:  - Leave it, and let the manager keep deciding per check. Set aside: the checker's
                 given then varies with whoever is holding the graph that day, and nothing records
                 what was handed over — which is the same class of miss as a term with no entry.
               - Declare all the standing preferences, verbatim, as the ground rules. Set aside:
                 several are accounts of what happened or rules about the manager rather than
                 constraints on a node's work, and node 42 shipped the boundary that an account never
                 travels that route.
               - Declare none, and take the contract's "nothing to give" branch honestly. Set aside:
                 the `/writing-for-agents` standard would then reach no checker at all, and the map
                 says it is the standard this effort's product should be held against.
               - Mint a separate grilling node for it. Set aside: it is one question, and a node
                 costs a whole spawn — this is what my node was given the item for.
```

**The manager's notes on Q2, to travel with it, and the first is a self-accusation rather than a correction.**

1. **The list omits the one ground rule the manager has been passing that the map does not contain at all**, and
   omitting it is *correct* on the worker's own test while being the sharpest instance of the defect this
   question is about. Every checker spawn in this effort has carried, in the manager's own words, a rule of the
   shape *"An in-place update never deletes — but this applies to the effort's own graph files only, not to the
   product. A product file — anything under `.claude/skills/` — is edited normally: text that is replaced is
   removed outright and is not marked in place."* **The second half of that exists nowhere.** `map.md`'s
   standing preference says only *"When any file in the graph is edited — a node or this map"*, and
   `graph-conventions.md` says nothing about product files being edited normally — verified,
   `grep -in 'removed outright\|edited normally' ` returns nothing in either. So the manager has been handing
   blind checkers **its own gloss** as though it were the effort's declared rule. **Two checkers leaned on it.**
   Node 45's checker used it to dispose of the operative-content hazard itself, quoting the spawn text back:
   *"The ground rules given to me separate the two explicitly."* Node 48's checker was given the same. So the
   choice this question actually forces is sharper than the worker knew: either that distinction becomes a
   **new** standing preference the human declares — it has never been put to them — or every future checker
   loses a given that two checkers have already used correctly.
2. **The counts are verified.** `CONTEXT.md` holds **50** term entries and **40** `_Avoid_` lines. The worker's
   correction is right in both directions, and `map.md`'s *"forty terms"* is the stale figure it read.
3. **The contradiction is verified verbatim**: *"This* effort declares neither: its sources are all
   authoritative, and its ground rules are the standing preferences above."* One sentence, both halves.
4. **One item on the list is under active question elsewhere, and its absence is load-bearing.** The map's
   *"completeness for an agent beats brevity for a human"* is **not** among the five. [Re-review the shipped
   files against `/writing-for-agents`](54-review-against-writing-for-agents.md) found it collides head-on with
   the standard's **sprawl** failure mode, and [What the token findings change in the workflow and its
   skills](53-what-token-findings-change.md) is live on whether it survives. So item 5 would hand a checker a
   standard whose central charge the effort's own preference contradicts — and that preference would not be in
   the block to say so. Not an objection to item 5; a reason the block will need appending to the moment node 53
   answers.

**A2, from the human**, `verbatim`: *"ok for the recommandations. I think we should try without the sixth item,
the checker should know that the skills are not the map and that they can be modified, no ?"*

The option it points at, quoted from Q2's `RECOMMENDED` and attributed to the worker that wrote it: *"Yes, and
those five."* So `map.md`'s `## Notes` declares this effort's ground rules as an explicit block, the *"declares
neither"* sentence is marked superseded in place, the manager copies that block as text into every checker spawn
and adds nothing of its own, and the block is the five items as listed.

**One divergence, and it is a ruling on the manager's own note rather than on the worker's recommendation.** The
manager's note 1 offered a sixth item — the product-file half of the never-delete rule, which the manager had
been passing to every checker as its own gloss and which exists in no file. **The human declined it**, with their
reason: *"the checker should know that the skills are not the map and that they can be modified"*. So the block
is **five items, and the manager stops passing the gloss.**

**The manager's note on why that is right, and it is right for a better reason than the manager gave.** The
gloss was **redundant rather than load-bearing**, and the evidence is on the very check that appeared to depend
on it. `map.md`'s standing preference is already scoped by its own words — *"When any file in the graph is
edited — a node or this map"* — so a product file is outside it by the rule's own text, with no gloss needed.
Node 45's checker found exactly that route unprompted and wrote it down: *"its one rule that might reach further,
`No edit deletes`, is scoped by its own words to graph files."* It cited the manager's ground rules **as well**,
which is what made the gloss look necessary when it was only first to hand.

**And the checker contract's own hard rule makes the omission safe rather than merely tolerable.** *"A property
nobody stated is not a finding."* A checker handed a five-item block that says nothing about never-delete
**cannot** fault a product file for removing text, because no property it holds is violated. The gloss was
buying protection against a finding the contract already forbids. So this is not a risk the human accepted; it
is a redundancy they removed.

**What that leaves as a live gap, recorded rather than repaired here.** Nothing anywhere states that a product
file is edited normally — not `map.md`, not `graph-conventions.md`, verified by grep in both. Under this answer
nothing needs to, for a checker. Whether a **worker** needs it stated is a different reader and a different
question, and it is not this node's; a worker reads the map, meets a rule scoped to graph files, and is in the
same position the checker is.

## Answer

**The mechanism is not a list, a check, or a procedure over files. It is a rule about what a shipped file may
require.** A shipped file may require only **what travels with it**, or **what the effort is obliged to declare
in the form the requirement needs.** Both halves were being broken, and each of the three failures this node was
opened for is one half of it.

That is the general conclusion this node's question complained had never been drawn. *"It was drawn three times
in miniature and each time about one list — and a list is not what was wrong. What was wrong is that the shipped
set has been pointing outside itself."*

### The half that travels: the glossary joins the shipped set

The glossary moves to `.claude/skills/expedition/CONTEXT.md`. The repository root gains the `CONTEXT-MAP.md`
that the `/domain-modeling` convention uses to name where a context lives, and the root `CONTEXT.md` stays as a
marked forward pointer, so the **26** markdown links from the graph files still resolve. Copying
`.claude/skills/` then carries the vocabulary, and `graph-conventions.md`'s authoritative pointer resolves
inside the shipped set instead of resolving, in another repository, to *that* repository's own root
`CONTEXT.md` — *"the failure that made this worse than a dangling link, since under the same convention the
wrong file is there to be found."*

**What was protected is bigger than this node thought when it asked: 50 term entries and 40 `_Avoid_` lines**,
not the forty terms the question and `map.md` both said. Verified independently by the manager. The map's
*"forty terms"* is stale on its own count and is corrected as part of resolving this node.

Two things stated rather than assumed. The name stays `CONTEXT.md` because the convention that owns the file
names it that — a **known dependency on a foreign convention**, whose plugin was renamed and rewritten upstream
between two of this effort's sessions and whose store path moved twice in one day; what a contract may name from
that plugin is [What a contract may name as a method skill](51-what-a-contract-may-name.md)'s. And node 14
raised a flag, still live, that the glossary *"passed no checker and no gate"* because a `grilling` node wrote it
into the product tree; **this is the first change to it that goes through both.**

**What this claims, and what it does not.** It makes the glossary reachable **inside the shipped set**. It does
not make it reachable **by a worker**, and those are two properties. No shipped skill points at
`graph-conventions.md`, at `CONTEXT.md`, or at anything else in that directory, and
`.claude/skills/expedition/` **holds no `SKILL.md` at all** — a skill directory containing no skill and two
documents nothing points at. Pointing a worker at the glossary is what a **spawn** does, and the spawn is the
manager's own skill, still unwritten; recorded there as a requirement and flagged as `29.1`.

### The finding mechanism is one paragraph, and it is why the checker can be the finder

The glossary states its own completeness at its top: a term the files that declare it authoritative use in this
vocabulary has an entry here; coining such a term and writing its entry are one change; and a term used with no
entry is a defect in the change that introduced it.

**What makes it work is a sentence in a sibling contract.** The checker's hard rule is *"A property nobody
stated is not a finding."* The duty was stated nowhere, so **the one party that reads a shipped file cold was
forbidden from reporting it** — which is why both live absences were found by the manager reading a condition by
hand, and why the single time a checker caught this class, at node 26, it was because that node's condition
happened to tell it to account for every changed line. *"Stating the property is therefore not a reminder to
anybody. It converts a miss nobody was permitted to report into one the blind checker must."*

It reaches the checker on **the bar** — *whatever else the repo itself demands* — the one thing an acceptance
condition need not copy, because it travels by its own route. So no condition mentions it and **the manager
authors nothing.** *"That answers the practice the manager has been holding deliberately: it hit this twice
while filing conditions and left it unrepaired both times, on the ground that supplying what a condition omits
makes the manager the author of the standard. Under this answer nobody has to choose."* And it is cheap, because
the checker holds the diff: it considers the terms **this work added**, not every term in the file.

**Coverage is complete here, where the pass's is zero.** [Cascade pass mechanics](15-cascade-pass-mechanics.md)
set the checker aside on coverage grounds and said plainly that *"a mechanism with catches to its name is being
set aside for one with none"*. Right for its subject, and it does not reach this class: a checker runs only on
implementation nodes, **but a term can only reach a shipped file through an implementation node**, and every one
runs a checker. Triage covers none of this, a term being missing from the day it ships rather than from the day a
decision moves.

**Nothing is added to the mechanical checks or to any acceptance condition.** There are nine checks now, and a
tenth over prose terms is the class of scan `map.md` records twelve false results against. The condition route is
refused because *"it is the condition that omitted this, twice, and a condition is not the manager's to
repair."*

### The half the effort must declare: this effort's ground rules

`map.md` said both that this effort *"declares neither"* optional block and that *"its ground rules are the
standing preferences above"*. The shipped checker contract offers two branches and no third, so the manager had
to decide which before it could spawn a check, and did so on its own judgement at **every** check, with no
record of what it handed over. **That is a standard authored per check.**

The *"declares neither"* sentence is marked superseded in place. This effort **declares a ground-rules block and
no source hierarchy**, all its sources being authoritative, and the block holds five items:

1. Nothing in the shipped files may assume this repo, this machine, or a toolchain. Prefer properties that are
   discovered over commands that are declared.
2. Each shipped worker contract stands alone as a file, rather than depending on any skill being invocable.
3. The human talks only to the manager. No agent the workflow spawns addresses the human directly, and nothing
   in the files may tell one to.
4. Prefer short, simple prose that can be changed later over machinery built for predicted needs. Reserve heavy
   design for the hard-to-reverse core.
5. Prose deliverables are held against the `/writing-for-agents` standard, which is specific to this repo, is
   never shipped, and is located by name in the `mattpocock-skills` plugin rather than by path.

Every one is drawn from a standing preference the map already held, and every one passes node 42's test: **a
standing constraint true of any node's work, rather than an account of what happened.** *"That test is what
keeps most of the map out — the manager-context findings, the token measurements, the landing policy's history
are accounts, and a checker holding them would be reading the record it is kept blind from."*

**The manager copies the block as text and adds nothing of its own.** Where a check needs a constraint the block
does not hold, that is a **raise** under [Whether a spawn may override a shipped worker
contract](28-spawn-overriding-a-contract.md)'s rule, not the manager's judgement.

**A sixth item was offered and declined, and the reason is why five is enough.** The manager proposed the
product-file half of the never-delete rule, a gloss it had been passing to every checker and which exists in no
file; the human's answer was *"the checker should know that the skills are not the map and that they can be
modified, no ?"*. **Redundant rather than load-bearing**, on three grounds: the map's preference is scoped by its
own words to files *"in the graph"*; node 45's checker found that route unprompted — *"its one rule that might
reach further, `No edit deletes`, is scoped by its own words to graph files"*; and decisively, the checker's
hard rule that a property nobody stated is not a finding means a checker handed a five-item block **cannot**
fault a product file for removing text. *"The gloss bought protection against a finding the contract already
forbids."*

**The block is complete as of today, and one change to it is already known to be coming.** [What the token
findings change in the workflow and its skills](53-what-token-findings-change.md) is live on whether `map.md`'s
*completeness for an agent beats brevity for a human* preference survives and over which document classes —
which bears directly on item 5, **the central charge of the standard it names being sprawl, the thing that
preference contradicts.**

**One residual, recorded and not repaired.** Nothing anywhere states that a product file is edited normally. For
a **checker** nothing needs to. A **worker** is a different reader in the same position: it reads the map, meets
a rule scoped to graph files, and is told nothing about the files it is about to edit. Not this node's; flagged
as `29.3`.

### Consequences

- **One implementation node**, [Ship the glossary inside the skill directory and make it state its own
  completeness](56-ship-the-glossary-into-the-skill-set.md), carrying the move, the completeness paragraph and
  the missing `ground rules` entry.
- **[Ship the FRICTION flag and the self-edit disclosure duty](41-ship-the-friction-flag.md) gains `Blocked by:`
  that node.** It coins `FRICTION` and its condition never reaches the glossary; landing it second means its
  worker owes the entry **under the bar**, without the condition being amended and without the manager writing
  it. *"That is this answer's first real test, and it is the case the manager recorded twice and left alone."*
- **The manager's own skill** gains two requirements: the spawn points a worker at the effort's glossary, and the
  shipped set's own documents are reachable — `.claude/skills/expedition/` holding no `SKILL.md` being why
  nothing points at `graph-conventions.md` today.
- **`map.md` is corrected twice** — *"forty terms"* becomes fifty, and *"declares neither"* is marked superseded
  by the declared block.
- **[Whether the five contracts' shared blocks stay duplicated](50-shared-blocks-stay-duplicated.md) gains an
  input and is not decided here.** A shipped glossary is where a de-duplicated vocabulary would go if that node
  chooses to; whether seven homes are a defect or a purchase stays its question.
- **The instance count in this node's question is a floor.** Three were known; the same defect has since been
  found from the other side by two research workers and is now [Reconcile a method skill's instructions with the
  contract's hard rules](48-method-skill-conflicts-hard-rules.md), and the *"invoke if present"* patch in the
  fog is a fourth. **The rule at the top of this answer is what they are all instances of.**

## Flags

`29.1` `ASSUMPTION` **· settled** — **What part 1 claims, and where the rest of it was routed.** *"The glossary becoming a
shipped file makes it reachable inside the shipped set; it does not make it reachable by a worker, and I settled
myself that only the first is this node's to claim… I routed worker-reachability to the manager's own skill as a
requirement — on the ground that what a worker is pointed at is the spawn's content, which node 12 made that
skill's — rather than minting a node for it. If that routing is wrong, the property has no owner and needs one,
because the last file written is the one nothing checks."*

`29.2` `ASSUMPTION` **· settled** — **The new completeness rule does not go in the ground-rules block.** *"Once the glossary
states its own completeness, the bar carries that statement to the checker by the route the bar already travels,
so putting it in the ground rules as well would give one rule two homes — which is the drift this node exists to
stop, arriving inside its own answer. The cost if I am wrong is that a checker whose spawn carries the block but
which never finds the glossary is told nothing about it."*

`29.3` `ASSUMPTION` **· settled** — **The unstated permission to edit a product file is left as a gap.** *"I settled that this
needs no repair for a **checker**, which cannot fault what nobody stated, and that whether a **worker** needs it
stated is a different reader and not this node's question. I minted nothing for it. The judgement is that a gap
which produces no wrong action today is better recorded than filled by me."*

### Manager's note: all three flags outstanding, on the ordering node 39 exposed

*The manager's own note.* Same case as node 39: a grilling node's flags arrive **after** the last answer, in the
handover, so *"ok for the recommandations"* could not have reached flags that did not yet exist. All three are
outstanding and presented rather than settled silently. `29.1` is the load-bearing one — it names a property
that may have **no owner**, and the worker says so against its own routing.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
