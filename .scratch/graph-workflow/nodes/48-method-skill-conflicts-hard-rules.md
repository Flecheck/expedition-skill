# Reconcile a method skill's instructions with the contract's hard rules

Type: implementation
Status: resolved

## Question

Four contracts tell a worker to invoke a named method skill; on this machine each of those skills instructs
something the same contract forbids — writing a file, addressing the human, committing, or placing work outside
the allowed paths. Only the checker contract says which wins. Give the other four the same rule, and take two
adjacent wording repairs while the files are open.

Reported by [Review every shipped file against `/writing-great-skills`](47-review-shipped-skills.md)'s worker,
which wrote the acceptance condition below and **bundled three repairs into this one node rather than three**,
flagged there as `47.2`: *"All three edit the same six contract files; the code slot is exclusive and four open
nodes already contend for it, so three nodes would mean three checks and three gates for edits totalling a few
dozen lines."*

**The conflict was demonstrated on the reporting worker itself, not predicted.** It declined to invoke
`/research`, which its own contract instructs, because that skill instructs *"Write the findings to a single
Markdown file"* against its hard rule 1, *"You write no file"*. It had no precedence rule to lean on, applied
the checker contract's *"blindness wins"* by analogy, and raised flag `47.1` because a research node has no
raise channel.

## Acceptance condition

Three repairs land in the shipped worker-contract skill files. This work edits skill files rather than graph
files, so text these clauses remove is removed outright and is not marked in place. Clause 1 is substantive;
clauses 2 and 3 are wording.

**1. A precedence rule for the method skill each contract names.** These four files each hold a section telling
the worker to invoke a named method skill if it is present:

- `.claude/skills/expedition-grilling/SKILL.md` — `## How you grill`, naming `/grilling` and `/domain-modeling`
- `.claude/skills/expedition-prototype/SKILL.md` — `## How you prototype`, naming `/prototype`
- `.claude/skills/expedition-research/SKILL.md` — `## How you research`, naming `/research`
- `.claude/skills/expedition-implementation/SKILL.md` — `## How you implement`, naming `/coding-principles` and
  `/naming`

In each of the four, that section states all three of the following:

a. where an instruction inside an invoked method skill conflicts with this contract's hard rules, the hard rules
   govern;
b. the three classes of conflict to expect — an instruction to write or update a file, an instruction to address
   the human directly or wait for a reply, and an instruction to commit, branch, or place work somewhere the
   contract does not allow;
c. what the worker does with the conflicting part, stated as an action and not only as a prohibition: it leaves
   that part unrun and reports which part it left and why.

`.claude/skills/expedition-precondition/SKILL.md` is out of scope for this clause — it states it has no method
skill. `.claude/skills/expedition-checker/SKILL.md` is out of scope — it already carries such a rule.

**2. Two bare prohibitions gain a stated positive beside them.** Each is a sentence whose reader is told nothing
about what to do instead, while the contract states the positive elsewhere in the same file.

- `You never resolve your node, never mark it, and never create another one.` — a numbered hard rule in
  `expedition-grilling`, `expedition-precondition`, `expedition-prototype` and `expedition-research`, and as
  `You never resolve your node and never mark it.` in `expedition-implementation`. In each of the five the rule
  additionally states what the worker does instead: it hands its answer back for the manager to write, and a
  node it has found is reported on the handover's `NEW NODES` part rather than created as a file.
- `You never create the node that would replace your own, and you never split your own node.` — a numbered hard
  rule in `expedition-implementation` only. It additionally states what the worker does instead: it raises, its
  own node's size not being its to change.

No hard rule is removed, renumbered or weakened.

**3. The six descriptions are pruned to their invocation work.** Each of `.claude/skills/expedition-checker`,
`-grilling`, `-implementation`, `-precondition`, `-prototype`, `-research` (`/SKILL.md`) carries a frontmatter
`description` of the form `The worker contract for an expedition <kind> node. Read it when a spawn names it, and
follow it exactly.` Afterwards each of the six:

a. begins with what distinguishes it from the other five — its node kind, or `checker` — rather than with
   wording all six share;
b. carries no instruction about how to follow the contract; the clause `and follow it exactly`, and any
   equivalent, is gone from all six;
c. still states the condition under which the skill is reached, which is that a spawn names it;
d. is no longer in words than it is today.

Each file's `name:` field is unchanged and still matches its directory name.

### The manager's note on the standard this condition was written against

*Not a change to the condition above.* This condition cites `/writing-great-skills`, which was superseded
upstream on the day it was written — see the annotation on [Review every shipped file against
`/writing-great-skills`](47-review-shipped-skills.md). **All three clauses survive the rewrite**, checked
against upstream rev `5b15a47`: clause 1 rests on the hard-rule conflict, which is this effort's own; clause 2
rests on the prohibition-pairing rule, which the new standard states more strongly rather than dropping (it
names **negation** a failure mode, *"steering by prohibition drags the forbidden behaviour into context and makes
it more available, not less"*); clause 3 rests on the pointer-pruning rules, which survive verbatim as
*"Front-load the leading word"*, *"One trigger per branch"* and *"Cut identity the body already carries"*. So
this node is **not** blocked on the re-review.

### Audit at claim time, by the manager

*The manager's own note, not a change to the condition above.* Read against [An acceptance condition is
self-contained text](33-condition-is-self-contained.md) and [The clause that says no resolved node changes
cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md).

**All three clauses pass, and this is a condition written by a reporting node's worker rather than by the
manager** — the class the record says has never yet failed the self-containment rule.

- **Clause 1** names four files and the section inside each, and states requirements a/b/c as text. Paths say
  *where*; the demand is in the condition. Passes.
- **Clause 2** quotes both sentences in full rather than pointing at them, and names every file each appears in.
  This is the clause most likely to have pointed, and it does not. Passes.
- **Clause 3** quotes the description form verbatim and states four properties. **3d — *"is no longer in words
  than it is today"* — references a before-state not in the text**, which is the shape node 33 warns about. It
  passes on established practice rather than on the rule's letter: the checker's third given is the work paths,
  from which `git diff` yields the before-state exactly, and node 49's clause 2 uses the same construction. Named
  so the checker meets it rather than being surprised by it.
- **Nothing quantifies over the record.** Node 36's prohibition is not engaged.

**Two facts the worker should have, both established after this condition was written.**

**The precedence defect has now fired twice on real workers, both this session, and both times the worker
resolved it the same way unaided** — node 47's, which declined `/research` and raised flag `47.1` because a
research node has no raise channel; and node 54's, which declined it again and, per its spawn, neither
re-reported nor re-flagged it. **Both reached for the checker contract's *"blindness wins"* by analogy.** That is
the strongest possible evidence for clause 1's shape: the rule the four contracts lack is one two independent
workers invented identically when they needed it.

**Clause 3's justification has moved, and the clause survives on the better half.** [How an agent workflow and
its skills reduce their own token cost](52-token-cost-of-a-workflow.md) measured the six `description:` lines at
**725 characters ≈ 180 tokens total** — the entire always-loaded surface the shipped corpus imposes — and settled
it as a non-issue by measurement. So clause 3 buys almost nothing on **context load**, which is what node 47's
finding 4 argued from. It still buys what the standard actually cares about: a pointer's *"wording, not the
target, decides when the agent reaches the material, and how reliably"*, and the discriminating word currently
sits at position six behind wording all six share. **Do clause 3 for trigger reliability, not for tokens**, and
do not let a saved-token argument into the work — it would be false.

One thing this node is **not**: the naming question. Whether a contract may name `/research` or must name
`mattpocock-skills:research` is [What a contract may name as a method skill](51-what-a-contract-may-name.md)'s,
and clause 1's rule holds however the skill is addressed.

## Answer

Three repairs landed across the six shipped worker-contract skill files. Nothing else under `.claude/skills/`
was touched — `graph-conventions.md` and `wayfinder-divergences.md` are unchanged.

**Clause 1 — the precedence rule, in four contracts.** One paragraph, byte-identical, placed immediately after
each section's *invoke if present* sentence:

> **Where a method skill's instructions and this contract's hard rules conflict, the hard rules govern.** Such a
> skill was written for an agent working alone, so three of its instructions collide with the rules above: to
> write or update a file of its own; to address the human directly, or wait for their reply rather than ending
> your turn; and to commit, branch, or place work somewhere this contract does not allow. Leave the conflicting
> part unrun, run the rest, and say in your handover which part you left and why.

Calls a later reader would otherwise re-derive.

**The shape was matched, not the wording.** The checker contract's *"Where a skill's procedure and your
blindness conflict, blindness wins"* is the sentence two workers reached for by analogy; the worker's ground is
its hard rules, not blindness, so the sentence names the hard rules and the same *X wins* shape carries it. The
checker's own sentence was left exactly as it stands.

**The conflicting part is left unrun and the rest is run, stated as an action rather than as a prohibition.**
Deliberate against the standard's *negation* failure mode and against what actually happened twice: node 47's
worker declined `/research` and could only flag it; node 54's declined it and recorded nothing. **Neither had an
action to take.**

**The report goes in the handover, and no new handover part was minted.** *"Say in your handover"* mirrors the
checker contract's *"say in your outcome"*. It needs no flag — with the rule written down, following it is no
longer an unprompted judgement — and the manager, as scribe, files it under the node's `## Answer`.

**Placement cost one existing sentence a rewrite in each of the four.** Each section's *"Where they are not,
this is the whole of the discipline"* fallback was split into its own paragraph after the new one, so the
invocation case is stated in one place instead of being separated from its rule by a bullet list. The split left
the pronoun stranded, so *"Where it is not,"* became *"Where it is not present,"*.

**It is silent on how the skill is addressed**, so it holds whether a contract names `/research` or
`mattpocock-skills:research`. That question is [What a contract may name as a method
skill](51-what-a-contract-may-name.md)'s and is untouched.

**Clause 2 — a positive beside each bare prohibition.** No hard rule was removed, renumbered or weakened; each
gained a second sentence. *"You never resolve your node, never mark it, and never create another one"* — at
grilling rule 4, precondition rule 2, prototype rule 5, research rule 2, and in short form at implementation
rule 2 — is now each followed by *"You hand your answer back and the manager writes it, and a node you have
found is reported on your handover's `NEW NODES` part rather than created as a file."* **This also closes the
ambiguity node 47 named:** *create* alone did not separate reporting a node from writing its file. Implementation
rule 6 gained *"Where either is what the work needs, you raise: the size of your own node is not yours to
change"*, reusing that contract's own raise-trigger wording rather than inventing a second phrasing.

**Clause 3 — the six descriptions pruned to their invocation work.** The shared opening and *"and follow it
exactly"* are gone from all six; each begins with its discriminator and keeps the trigger:

| file | description |
| --- | --- |
| `expedition-checker` | `Checker contract for an expedition. Read it when a spawn names it.` |
| `expedition-grilling` | `Grilling node worker contract for an expedition. Read it when a spawn names it.` |
| `expedition-implementation` | `Implementation node worker contract for an expedition. Read it when a spawn names it.` |
| `expedition-precondition` | `Precondition node worker contract for an expedition. Read it when a spawn names it.` |
| `expedition-prototype` | `Prototype node worker contract for an expedition. Read it when a spawn names it.` |
| `expedition-research` | `Research node worker contract for an expedition. Read it when a spawn names it.` |

Word counts fall 19→14 for the five kinds and 18→12 for the checker; every `name:` field is unchanged and still
matches its directory. **The checker's carries neither *node* nor *worker*, the glossary making it neither.**

**One thing was kept against the standard's letter, on the ground this node names.** `/writing-for-agents` says
*"cut identity the body already carries"*, and *expedition* is carried by every `name:` field as well as by each
body. It was kept anyway because clause 3's justification is **trigger reliability**: the manager's spawn is
written in that word, and the standard's own leading-word rule says a word shared between the prompt and the
material makes the material reached more reliably. **No token argument was used anywhere in this work** — per
the manager's audit, that argument would be false.

**Measured, as a side effect and not as a justification.** The six `description:` lines fall from **725
characters to 556** — the 725 reproducing node 52's measurement **exactly**, which corroborates it. Files:
checker 318 unchanged, grilling 208→218, implementation 254→265, precondition 221→223, prototype 212→223,
research 137→148. 63 insertions, 18 deletions.

**Verified live rather than reasoned about.** The descriptions were reloaded by the running harness as they were
written, and the worker's own skill listing re-rendered with the new text — so all six remain reachable and none
was broken. **The manager confirms this independently: its own skill listing re-rendered with the six new
descriptions mid-turn.**

**A fact on node 47 has gone stale.** Its finding 1 records `expedition-checker/SKILL.md:132` as *"the only file
that resolves this"*. **Five of the six now do.** Finding 1 discharged, not contradicted.

**What node 51's worker inherits, reasoned rather than omitted.** The rule now produces a per-node record of
which method-skill part a worker left unrun and why, in that node's `## Answer`. **Nothing aggregates those
across an effort, and the aggregate is exactly the signal that would say a contract is naming the wrong skill**
— which is node 51's question. Building a `## Review`-style form and a tenth mechanical check for it would be
machinery for a predicted need, against this map's standing preference, so it was left as prose. The asymmetry
with the checker's side is deliberate: node 45's `NOT COVERED` machinery tracks an **obligation still owed**,
whereas a left-unrun part is a fact about how work was done and nothing stays open.

## Flags

`48.1` **· settled** `ASSUMPTION` — **The conflict paragraph was written byte-identical in all four contracts rather than
tailored to each one's own hard rules.** In the worker's words: *"Each contract's collisions differ in detail —
research forbids every file, prototype confines what it builds to `prototypes/NN-<name>/`, implementation
forbids the commit, grilling routes questions through the manager — and a tailored paragraph would have named
each. Uniform text was chosen for the same reason flag `35.3` gives: it buys exact agreement across the four…
The cost is the one that flag already named and did not solve — a fourth shared block in a set of files nothing
checks for divergence, in an effort where [Whether the five contracts' shared blocks stay
duplicated](50-shared-blocks-stay-duplicated.md) is open on precisely whether such blocks stay duplicated.
Placement was made identical in all four for the same reason, at the price of rewriting one existing fallback
sentence per file."*

## Review

**Checker, run 1 — spawned.** With the five givens, and told the two things the worker named as findable in the
diff: this work changed **its own contract** (the `description:` line only, no operative content) and the
**implementation contract** (rules 2 and 6 plus `## How you implement` gained text, nothing altered or
renumbered). Both are the hazard flag `31.2` records — a node that edits a contract silently changes the
contract of every worker spawned after it, including its own checker.

**Outcome of run 1: dead.** Terminated by the harness partway through: *"Agent terminated early due to an API
error: You've hit your session limit."* Its last recorded line was *"Now the mechanical verifications: word
counts for clause 3d, name/directory match, and a refused-word scan over the added text"* — so it had reached
the mechanical half and **judged nothing, established nothing and raised nothing that survives.** No partial
outcome is usable: a check is its verdict, and there is none.

**Not re-spawned immediately, and the reason is a measurement rather than a preference.** The limit resets at
21:40 Europe/Paris and a fresh checker spawned before then would die the same way. This is the **fourth** dead
checker run in this effort and the **third in one day** — two of the three on a session limit rather than on
anything about the work. Recorded here because the pattern is now data for [Friction from running this map by
hand](24-self-hosted-friction.md)'s finding that the runtime's weakest point is the long-lived thread, and it
adds a second weak point that node had no case for: **the fleet is rate-limited as a shared resource, so a
check is not merely expensive but sometimes unavailable**, and an implementation node's code slot idles on it
with nothing the manager can do. That is a third claimant on the *when to flip landing to asynchronous* fog
item, alongside the gate and a blocked worker.

**Run 2 is owed and will be spawned fresh**, with the same five givens and **no statement of what changed**, run
1 having established nothing — telling it a predecessor existed would be the account of what happened that [The
checker's spawn carries the effort's ground rules](42-checker-spawn-carries-ground-rules.md) forbids travelling
by the ground-rules route.

**Run 2 spawned at 22:04, past the reset**, with the same condition, bar, paths and name — and with the
**five-item ground rules block the human approved minutes earlier** at [What keeps the shipped files consistent
when a decision changes a term](29-shipped-file-consistency.md)'s A2, rather than the manager's own selection
from the standing preferences. **This is the first checker spawn in the effort whose ground rules were declared
rather than authored per check**, and the first that does *not* carry the manager's product-file gloss, which the
human struck. Whether a checker reaches the right disposal on a product file without it is now observable rather
than argued, on a work that edits six product files.

**Outcome of run 2: `PASS`. Nothing reserved, no questions, nothing handed back as not covered** — the fourth
consecutive check in this effort with no residual for the manager to hold.

**It established all three clauses mechanically rather than by eye, and one method is worth keeping.** For
clause 2's *no hard rule removed, renumbered or weakened*, it **unwrapped each file before and after into one
word per line and diffed** — giving **zero deleted words anywhere in any rule**, the only removals in the whole
change being the six frontmatter descriptions plus `not,` becoming `not present,` in the four files that gained
the new paragraph. It used the same word-level diff to confirm the two things the spawn flagged: the change to
its **own** contract is exactly the nine description words and nothing else, *"so no operative content of it
moved and I had something unmoved to check against"*, and the implementation contract gained text in rules 2
and 6 and `## How you implement` while altering no existing wording.

**It verified that the added sentence points at something real.** Clause 2's positive names the handover's
`NEW NODES` part, and it checked that part exists in each of the five handover shapes — research:83,
grilling:136, implementation:187, precondition:135, prototype:138 — rather than trusting that the contract it
was told about is the contract on disk.

**It cross-checked that clause 1's three conflict classes are live rather than theoretical**, against the four
named method skills as they exist on this machine: *"`/research` writes a Markdown file into the repo,
`/prototype` writes files, `/naming` confirms with the user past five references."*

**It handled the reviewing skill with six set-asides and one disagreement, and named the ground of each.** Six
findings it declined to hand back, *"each because the acceptance condition mandates the text it objects to… or
because the objection is to a pre-existing property the work did not introduce"* — `method skill` already
appearing in the precondition contract before this change, and `hand what you found back in your handover`
being baseline idiom. And one it checked and rejected: the skill read *"wait for their reply rather than ending
your turn"* as forbidding the implementation raise, and *"rule 4 forbids a human-facing tool and the raise is
delivered as the worker's entire final output, so ending the turn is how that contract waits."*

**The bar's command half was verified empty rather than trusted**, and more thoroughly than any previous run:
`find` over the whole repo returns **nine** files — the six contracts, the two documents under
`.claude/skills/expedition/`, and `CONTEXT.md` — with no manifest or task runner of any kind, no CI directory,
**no `.claude/settings.json` carrying hooks, no active `.git/hooks`**, and nothing executable. It also confirmed
`git diff --cached` is empty, *"so the unstaged diff is the whole of the work and nothing was hidden in the
index"* — a check no previous run in this effort has made.

### Two facts about this run that are about the workflow rather than about the work

*The manager's own note.* **This was the first checker spawn in the effort whose ground rules were declared
rather than authored per check**, and the first without the manager's product-file gloss, which the human
struck as redundant. **The gloss was not missed.** The run reached the same disposal from the standards document
itself, unprompted: *"it governs the `.scratch/` graph files, not skill files, and its `No edit deletes` rule is
scoped to graph files — which independently corroborates the condition's note that text these clauses remove is
removed outright."* So the human's reasoning is confirmed by measurement on the first case that could test it.
It also located `/writing-for-agents` **by name rather than by path**, as ground rule 5 requires, and noted that
*"the two older builds of the same plugin do not carry the skill"* — the discovered-over-declared preference
working on the exact dependency that moved twice today.

**And the harness flagged this run's output as instruction-shaped**, on the `settings-json` pattern, because
verifying the bar's command half means naming configuration filenames. Benign here — the checker was reporting
absence, and nothing in its output was a directive. Recorded because it is a **new** friction with no home: a
checker doing its job on an empty bar produces text that a safety filter reads as an attempted instruction, and
nothing in the workflow anticipates that. It belongs with [Off-contract subagent
output](17-off-contract-output.md)'s subject rather than being a defect in this work.

**Gate: awaiting the human.**

**Gate: `approve`.** The human's words, `verbatim`: *"approve 48, only run stuff about lowering token use for
now"*. **Flag `48.1` settled by that approval**, with no separate assent asked for, the payload having presented
it in full.
