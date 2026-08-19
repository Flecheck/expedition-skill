# An acceptance condition is self-contained text

Type: implementation
Status: resolved

## Question

[`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md)'s
`### Acceptance condition` section says **who** writes one and **when**, and never says it must be readable
by the party that will check it.

Add that a condition is written as text that stands on its own and **never points into the record** — because
the checker reads it cold and may not follow the pointer. A condition that points leaves the manager
authoring the referent into the checker's payload, which is the manager writing the standard the work is
judged against.

### Found three times, owned by nobody

1. [Write the worker contract skills](22-worker-contract-skills.md) — *"a path in one is a hole in the
   blindfold"*.
2. Flag `26.4` — *"nothing says who dereferences it when it does"*. Two of [Carry the recorded deltas into
   the shipped skill files](26-carry-deltas-into-shipped-files.md)'s conditions pointed into the record; the
   manager dereferenced one into the checker's spawn and **stripped a bookkeeping preamble that asserted the
   work had already been done**, which would otherwise have told a blind checker the answer.
3. [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md), which is where
   the defect was finally placed. That node ruled the dereferencing **not an override at all** — the manager
   was complying with the checker contract's own clause, *"as text… not somewhere to go and read them"* —
   and located the fault one level up, here. Recorded as flag `28.4`, decided by the worker alone.

The same node's `## Answer` states the general form: the file states the rules, the spawn states the
parameters. An acceptance condition is a parameter, so it has to arrive whole.

### ~~The acceptance condition is owed~~ **Now written, below**

~~Written by whoever spawns this, and it may not be claimed without one.~~ There is an irony to keep in view
while writing it — **this node's own condition must satisfy the rule this node ships** — and a warning from
[What the checker contract owes to having been run](31-checker-contract-owes.md): node 26's condition was the
first written by a manager rather than by a spawning node or its worker, and it had to be amended twice, once
for naming a glossary entry that does not exist.

**Written by the manager at this node's spawn**, there being no spawning node to write it — this node was
minted by [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md) as a
repair rather than as a piece of that node's own work. So it carries node 31's warning in full: it is
manager-written, and it should be read against the files before it is trusted. Condition 6 turns that warning
into work by making the condition audit itself.

## Acceptance condition

1. **The rule lands in [`graph-conventions.md`](../../../.claude/skills/expedition/graph-conventions.md), in
   its `### `## Acceptance condition`` section.** That section today says who writes a condition, when, and
   that its worker may not rewrite it. It gains a statement that a condition is **self-contained text**:
   everything needed to judge whether the work is done is in the condition itself, and its reader never has
   to go and read something else to find out what it demands.

2. **The reason travels with the rule.** The checker is blind — it is handed the condition as extracted text
   and has not read the node — so a condition that points at something it was not given cannot be checked at
   all, and the manager ends up authoring the referent into the checker's payload, which makes the manager
   the author of the standard the work is judged against. Written in the document's own voice, because a rule
   with no reason attached gets narrowed back by whoever next finds it inconvenient.

3. **It says what the writer does instead**, as a positive instruction and not only as a prohibition: where a
   condition genuinely depends on material held elsewhere, the writer **copies that material into the
   condition**.

4. **However you word it, the shipped rule has both of these properties.**
   - It **permits** a condition to name a path in the repo that the work must touch, produce, or leave in a
     particular state. The checker has the repo; a path is not the defect.
   - It **forbids** a condition whose meaning cannot be recovered from its own text — *"as decided at node
     NN"*, *"the section agreed in the interview"*, *"the wording the human chose"* — where the reader must
     go and read to learn what is being required of them.

   If you judge that boundary drawn in the wrong place, it is not yours to redraw: raise it.

5. **It says what is done about a condition that points anyway**, since forbidding it forward does not clear
   the ones already written, and the party who meets one is the manager assembling a checker's payload. One
   thing that answer may not be: **the manager writing the missing material into the payload**. That is the
   defect this rule exists to stop and it is what happened at node 26. If the honest answer reaches past this
   document into *who may amend a condition after it is written*, that is a raise rather than yours to
   decide.

6. **You audit the rule you shipped against four conditions that already exist**, and report the result in
   your `ANSWER`: for each, whether it passes, and where it fails, which clause fails.
   - This node's own acceptance condition — the text you are reading.
   - `.scratch/graph-workflow/nodes/31-checker-contract-owes.md`'s — written, unstarted, and the next
     implementation node likely to be spawned.
   - `.scratch/graph-workflow/nodes/22-worker-contract-skills.md`'s and
     `.scratch/graph-workflow/nodes/26-carry-deltas-into-shipped-files.md`'s — the two this node's
     `## Question` records as having shown the defect.

   **You repair none of them.** Two sit on resolved nodes and one belongs to another open node. The audit is
   evidence that the rule bites on real text; fixing what it catches is somebody else's commit.

7. **Only `.claude/skills/expedition/graph-conventions.md` changes.** If you conclude that a worker contract
   or the checker contract also needs a word about this, report it under `NEW NODES` and write none of it:
   `expedition-checker/SKILL.md` and the five `expedition-<type>/SKILL.md` contracts are the live territory
   of two other open implementation nodes, and a second commit against one of those files from here would
   collide.

8. **No decision on any resolved node changes.** [`CONTEXT.md`](../../../CONTEXT.md) is touched only if a term
   genuinely moves; if one does, say so in your handover rather than assuming the change travels, because
   nothing checks the shipped files against the glossary.

9. **The bar for this repo, in full.** `graph-agent` has no build, no tests, no formatter and no CI — nothing
   to invoke — so the bar is entirely its non-command half: the project's coding principles and naming
   discipline, the standing preferences in `map.md`'s `## Notes`, `CONTEXT.md`'s `_Avoid_` lines, and these
   conditions. That is a complete bar, not a deficient one.

## Answer

**`graph-conventions.md`'s `### `## Acceptance condition`` section gains three paragraphs: the rule, its
reason, and what happens to a condition that points anyway.** Nineteen lines, one file, no other change.

The rule as shipped: a condition is **self-contained text** — everything needed to judge whether the work is
done is in the condition, and its reader never goes anywhere else to find out what it demands. The boundary
is drawn as **object versus content**: a **path** may say *where* (the work must touch that file, produce it,
or leave it in a stated state) because the checker has the repo; what may never sit outside the text is **the
demand itself**, and the three forms named as forbidden are the condition's own — *as decided at node NN*,
*the section agreed in the interview*, *the wording the human chose*. The positive instruction is that
material genuinely held elsewhere is **copied into the condition**.

The reason travels in the document's own voice and names the party: the reader is the **checker**, handed the
condition as text and having not read the node, so a condition pointing at something it was not given cannot
be checked at all — and the manager, supplying what the condition left out, becomes the author of the
standard the work is judged against.

**Three calls a later reader would otherwise re-derive:**

- **The bar is exempt from the copy rule**, and only because it reaches the checker by its own route. Without
  this the rule would demand every condition inline the whole bar, and three of the four conditions audited
  below fail on their bar clause alone. Flag `33.2`.
- **The residual clause is the scribe rule pointed outward.** The document already binds what the manager
  writes *onto* the graph; this binds what it hands *out*: it hands the condition over as written and
  supplies nothing it omits. Where what is missing is what the check turns on, it goes to the human — raised
  by the manager where it meets one before the check, or by the checker on a condition it cannot check.
  Nothing is said about *who may amend a condition*, which condition 5 ruled out of this node's reach. Flag
  `33.3`.
- **The reason is stated as what the rule protects, never as why it was chosen**, which is the reading of
  [Write the graph conventions document](21-conventions-document.md)'s *"no reasoning, no rejected
  alternatives, no justification"* the document has already been maintained under — node 26 added five such
  operative clauses to it. Flag `33.1`.

`CONTEXT.md` is unchanged and no term moves: the *Acceptance condition* entry stays true as written, and
self-containment is a property of how one is written, which is this document's job — the file states the
rules, the spawn states the parameters.

### The audit (condition 6) — 31 conditions across four nodes

Verdicts are against the **demand clause** (the forbid), the **path permit**, and the **bar exemption**.

**This node's own condition (33).** Six pass; two fail; one is exempt.

| # | verdict |
| --- | --- |
| 1, 2, 3, 4, 5, 7 | **pass** — each states its demand whole; the paths in 1 and 7 are the path permit's case, naming the file the work must change |
| 6 | **fails the demand clause, twice.** It names four node files by path and requires their text to be judged: they are neither touched nor produced, so the path permit does not reach them, and they sit inside the effort's own directory — the record the checker does not read. Second, its deliverable lands in the node's `## Answer`, which the checker is not given at all, so the clause is addressed to a party that structurally cannot check it — [Write the worker contract skills](22-worker-contract-skills.md)'s condition 3 again |
| 8 | **fails the demand clause** on *"No decision on any resolved node changes"*; its second half (`CONTEXT.md` touched only if a term genuinely moves) passes |
| 9 | **points, and is exempt.** Its non-command half is three pointers — the project's coding principles, `map.md`'s standing preferences, `CONTEXT.md`'s `_Avoid_` lines — none copied in. Harmless because the bar reaches the checker by its own route, which is why the shipped rule exempts it |

**One consequence the manager meets immediately: condition 6 may not be repaired in what it hands the
checker.** Pasting the four conditions into the checker's spawn is precisely the act this rule exists to stop,
and it is what happened at node 26. Under the residual clause the condition goes over as written, and the
checker either raises or records the clause as not establishable — the third route [Write the worker contract
skills](22-worker-contract-skills.md)'s attempt 2 invented.

**[What the checker contract owes to having been run](31-checker-contract-owes.md).** Four pass; one fails;
one is exempt.

| # | verdict |
| --- | --- |
| 1, 2, 3, 6 | **pass.** 2 is the good form: it quotes *"a condition you can check but disagree with"* rather than pointing at it, and names nodes 20 and 22 only as attribution for who owns the return shapes. 1 and 3 name the file and its section as objects, and 3 quotes the sentence being removed |
| 4 | **fails the demand clause, twice**: *"no decision on any resolved node changes"*, and *"the glossary-does-not-travel problem"* whose content is only in node 29 |
| 5 | **points, exempt** — same shape as 33.9 |

**[Write the worker contract skills](22-worker-contract-skills.md).** Six pass; three fail. It carries no bar
clause at all — the bar reached that checker through the spawn, which is the shipped rule's exemption working
in practice a year before it was written down.

| # | verdict |
| --- | --- |
| 1, 2, 8, 9 | **pass** |
| 3 | **fails the demand clause.** *"Every rule in every contract traces to a resolved node"* has the whole record as its content. Four independent blind checkers each declared it not establishable, alone; the rule now names why — the demand's content is outside the text, and no copy can bring the record inside it |
| 4 | **passes.** *"Instructions only — no reasoning, no rejected alternatives, no history"* carries the entire demand; *"The same bar [node 21] was held to"* is corroboration that could be deleted without changing what is required. **A pointer beside a stated demand is not the defect** |
| 5 | **fails the demand clause.** The refused set is not in the condition. Two things do not save it: `CONTEXT.md` is a repo file rather than the record, so the checker could read it — but it read a **moving** standard, and at node 26 the work itself edited an `_Avoid_` line, which is [What the checker contract owes to having been run](31-checker-contract-owes.md)'s first item. Copying the refused words in would have frozen it |
| 6 | **fails the demand clause, worst of the set.** *"everything that [run-1] contract carried"* is content held in a file **inside the effort's own directory**. This is the instance the node's own `## Review` named — *"a path in one is a hole in the blindfold"* |
| 7 | **passes**, at the boundary. *"names neither the node file nor any part of it"* sends the reader nowhere; what it assumes is **vocabulary** — what a node file's parts are — rather than material at a location. Assumed vocabulary is not a pointer, and the rule does not reach it. Same note on 8 |

**[Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md).** Three
pass; two fail; one fails on its headline; one is exempt.

| # | verdict |
| --- | --- |
| 1 | **fails the demand clause**, and it is *the* instance: the whole demand is a paragraph in `map.md`. It is what the manager dereferenced into the checker's spawn, stripping a preamble asserting the work was already done — flag `26.4`. Its second half (the map's paragraph annotated in place) is the path permit and passes |
| 2 | **passes, and it is the model.** It names node 25 and then states the rule in full, residual case included. The copy is what made it checkable — condition 3 of this node's own demand, already demonstrated |
| 3, 7 | **pass.** 7 states the general sense of *Raise* in full and quotes the amended wording; the two contract files are named as objects |
| 4 | **fails the demand clause** — *"No decision on any resolved node is changed"* |
| 5 | **fails on its headline, passes in substance.** The operative sentence is *"Everything [node 27] requires of `graph-conventions.md`"* — a pointer into the record — and the body then enumerates the five items in full. Had node 27 required a sixth, the condition would demand it without stating it. Both halves of this node's rule are visible in one condition |
| 6 | **points, exempt** — same shape as 33.9 and 31.5 |

**Nothing above was repaired.** Two sit on resolved nodes and one belongs to an open node.

### What the audit found that no single condition shows

- **Nine of thirty-one fail, and one sentence accounts for four of them.** *"No decision on any resolved node
  changes"* (33.8, 31.4, 26.4) and its variant *"every rule traces to a resolved node"* (22.3) are boilerplate
  on every implementation condition this map has written, and **the clause cannot be made self-contained by
  copying** — its content is the whole record. It is also already discharged elsewhere: `INVALIDATIONS` is a
  part of every worker's handover, addressed to the party that reads the record and can answer it. The clause
  is a duplicate pointed at the wrong party. New node below.
- **A second boilerplate, the bar clause, accounts for three more** (33.9, 31.5, 26.6) and is exactly why the
  shipped rule exempts it.
- **The failures are not evenly spread by author.** Every condition written by a spawning node's worker or
  copied in full passes; the failures cluster on clauses that summarise something the writer had open in front
  of them. That is the mechanism the rule describes: the writer can see the referent, and the checker cannot.

## Flags

`33.1` **· settled** `ASSUMPTION` — the reading of [Write the graph conventions document](21-conventions-document.md)'s
condition 3, *"no reasoning, no rejected alternatives and no justification"*, under which this node's own
condition 2 is satisfiable at all: an operative statement of **what a rule protects** is not the reasoning
that document refuses, which is the record behind a decision. Settled from the file rather than raised, on
the ground that the shipped document already carries five such clauses — *"because the sweep and the closing
report are built from it"*, *"Without it a flag can only be pointed at by its position in a list"*, and three
more — every one added by [Carry the recorded deltas into the shipped skill
files](26-carry-deltas-into-shipped-files.md) under a condition requiring the document's own voice. The new
text names no node, no history and no rejected alternative.

`33.2` **· settled** `ASSUMPTION` — **the bar is exempt from the copy rule**, decided alone. No node decided that a
condition may leave anything out; the ground is the checker contract's second given, which hands it the bar
by its own route, and node 28's line between a slot the contract opens and a parameter that must arrive
whole. Without the exemption the rule would demand that every condition inline the whole bar, and three of
the four conditions audited fail on their bar clause alone.

`33.3` **· settled** `ASSUMPTION` — **the manager may raise a pointing condition before the check rather than spending one
it knows will raise.** [Whether a spawn may override a shipped worker
contract](28-spawn-overriding-a-contract.md) wrote the manager's own raise for a shipped contract's clause
blocking the node in front of it; this extends it to a malformed condition. The alternative — hand it over
and let the checker raise — is also written, and costs a whole verdict, a raise issuing no outcome at all.

`33.4` **· settled** `ASSUMPTION` — filed by the manager, and not the worker's judgement. The handover's `FLAGS` part asks
for *"one line each"*, but a flag lands in **two** places under two different caps: free prose under
`## Flags`, and one capped sentence in [flags.md](../flags.md). The worker wrote the prose and nothing else —
the more useful half — so the manager condensed each of the four into its index line, authoring text that is
neither the worker's nor the human's. Nothing in the contract says which of the two a worker is writing. This
is the same omission the worker's own third new node reports about `NEW NODES`: a handover part naming one
artifact where the graph needs two.

## Review

### Check 1 — `PASS`

Blind. Handed the acceptance condition as extracted text, the bar as [map.md](../map.md) records it, and one
changed path. Verified conditions 1–5 clause by clause against lines 117–134 of the shipped file, confirmed
condition 7 with `git status --porcelain -- .claude/ CONTEXT.md` returning the one file, and condition 8 with
an empty `git diff --stat -- CONTEXT.md`. The bar's non-command half was checked in full, including
*"an in-place update never deletes"* against `git diff --numstat` — **19 insertions, 0 deletions**.

**It reported one part of the condition as not established rather than passing or failing it**, and the
account is this node's own subject arriving in the check:

> Its reporting half — *"report the result in your `ANSWER`"* — I did not establish and could not. The
> `ANSWER` is the worker's handover, not among the paths I was given, and the spawn states the `.scratch/`
> changes are the manager's bookkeeping and not the work. Reading it as "in the file" would be checking
> against my own repair of the condition, which my contract forbids. **The manager holds that handover and is
> the only party that can verify the audit was reported; my `PASS` does not cover it.**

The same reservation is recorded against condition 7's *"report it under `NEW NODES`"* and condition 8's
*"say so in your handover"*: in each case the checker verified the tree half — nothing repaired, no contract
touched, `CONTEXT.md` unchanged — and named the reporting half as outside what it was given.

**This is the third route [Write the worker contract skills](22-worker-contract-skills.md)'s attempt 2
invented, arriving unprompted for the fourth time**, and it is what [What the checker contract owes to having
been run](31-checker-contract-owes.md) item 2 exists to write down. The manager predicted it before spawning
and handed the condition over unrepaired anyway, which is the rule this node ships being obeyed by the party
it binds.

**Manager verification of the reserved half**, held against the handover the manager holds and the checker
did not: condition 6's audit **was** reported — 31 conditions across four nodes, verdict and failing clause
for each. Condition 7's `NEW NODES` carries three. Condition 8's `CONTEXT.md` statement is present and
negative. All three reporting halves are met.

**Standards the checker found and how it used them**, recorded because the bar's non-command half is
discovered per repo and this is the first run to go looking beyond `map.md`: it found `coding-principles`,
`naming` and a general `code-review` skill on the machine, applied the reviewing skill's **Standards** axis by
hand rather than invoking it — *"because it runs its axes in spawned sub-agents that would be handed none of
that and would go looking, including into the record"* — and left its **Spec** axis unrun, that axis holding
work against an originating document which here is the node file. **A blind checker that invokes a reviewing
skill loses its blindfold to the sub-agents the skill spawns.** Nothing in its contract says so.

### Gate — `approve`

The human's reply, `verbatim`: *"ok for the flags, you can continue"*.

**What the first half points at**, quoted beside it and attributed to the manager, which offered it: all four
flags, each carrying a *"Recommend settling"* line. Settled as recommended — `33.1`, `33.2`, `33.3` and
`33.4`.

**What the second half points at.** The gate's three outcomes were offered by name — *"**approve** (I commit),
**correct** (say what's wrong, uncapped rounds), **reject** (nothing kept)"* — and *continue* names none of
them. Read as `approve`: no correction was given and nothing was withdrawn, and continuing from a gate is
committing. Recorded rather than asked again, against [What is recorded when the human takes an option as
offered](25-recording-an-option-taken.md)'s residual case, on the ground that that rule covers a reply which
could point at **either** of two live options and here only one was reachable. It also carries the three new
nodes, each of which was offered with a recommendation: create the first two, annotate
[What the checker contract owes to having been run](31-checker-contract-owes.md) in place rather than mint
the third.

**This is the first gate where the manager's reading was not put back to the human**, and the flag it would
have produced is not filed because the reading is stated here instead. If it is wrong, the commit is local,
path-limited and unpushed.
