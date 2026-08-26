# Carry the worktree lifecycle into the shipped files

Type: implementation
Status: resolved

## Question

The implementation worker contract and this map's landing-policy paragraph are both written for a workflow that
works in place, never branches and holds an exclusive code slot. **Both have to say what an implementation node's
lifecycle now is**, as settled by [Run an implementation node's work in a worktree](68-implementation-in-a-worktree.md).

Reported by node 68's worker, which wrote the acceptance condition below. **Blockers: none.**

## Acceptance condition

*Written by node 68's worker.*

Two files are edited, and nothing else is.

**1. `.claude/skills/expedition-implementation/SKILL.md`.** The sentence *"You hold the **code slot** for the whole
of this node — from your first edit until the human has approved your work. No other implementation worker is
running while you do."* is replaced by text stating: the worker holds **a** code slot for the whole of the node,
from its first edit until the human has approved the work; the number of code slots is set by the effort and may be
more than one; and the tree named in the worker's spawn is the worker's alone for the whole of the node, and the
worker does not edit files outside it. The `code slot` entry under *Words used exactly* is updated to match — it
currently reads *"the right to modify product code, held by one worker at a time"* and must stop asserting one. The
file's existing hard rule 3 — never commit, never branch, never switch branches, never push, never rewrite history
— is left exactly as it stands, wording included.

**2. `.scratch/graph-workflow/map.md`.** The paragraph beginning *"**Landing policy, now settled and binding on
this map too**"* is edited under this effort's standing never-delete rule: superseded text is marked as superseded
and left in place, and new text is added around it. The new text states, in this order: an implementation node's
worker works in a git worktree the manager creates for that node with `git worktree add` off the current `HEAD`, on
a branch whose name carries the node's id, placed outside the repository's working tree; the changes stay
uncommitted through the checker and through the human's gate; on approval the manager makes one path-limited commit
of that node's paths, rebases the branch onto the branch the manager thread is on, re-runs the bar's commands on the
rebased result, merges with `git merge --ff-only`, then removes the worktree and deletes the branch; a rebase
conflict is resolved by nobody in the moment — the manager runs `git rebase --abort` and the node takes a correction
round with the worker respawned; a post-rebase bar failure likewise takes a correction round and the work does not
land; on reject the worktree is removed and its branch deleted, and where the human asks for the work to be kept the
manager commits it onto that branch before removing the directory; nothing is ever pushed. It further states that
the number of concurrent implementation workers is a setting of the effort, that it is **one**, and that occupancy of
a code slot is discovered by counting the live worktrees rather than by inspecting the working tree for uncommitted
changes.

The map's existing sentence *"No branch is ever created or switched, nothing is ever pushed, and history is never
rewritten"* is marked as superseded on its first two counts, with the never-pushed clause stated as still standing.

Both files continue to state properties rather than assuming any particular repository, machine, or toolchain beyond
git, which the landing policy already assumes throughout. **Neither file gains a claim that worktrees are reused
between nodes.**

The standing bar applies: the working tree builds, warns about nothing, is formatted, and passes the tests relevant
to the change. This repository has no build, no tests and no formatter, which is a complete bar on its remaining
half and not a deficient one — so what remains is the project's own criteria, this map's standing preferences, and
the `_Avoid_` lines of the glossary the shipped files declare authoritative.

### The manager's note at filing, not a change to the condition

**Two facts in clause 1 were verified rather than trusted**, in the contract as it stands: the code-slot sentence is
present verbatim as quoted, and the *Words used exactly* entry reads exactly *"the right to modify product code,
held by one worker at a time."* Both hold.

**This node writes `map.md`, which the implementation contract's hard rule 1 forbids** — *"You write product code.
You write no graph file."* That is the same collision [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md) met, and it was answered there by the human's ruling that the ban stops a worker
doing the manager's **progress bookkeeping** and does not reach work whose **subject** is a graph file. **Here the
map is the subject of clause 2.** The permanent fix is [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md), still open — so whoever claims this node needs the human's licence
carried into the spawn in their own words again, exactly as node 59 did. **The manager may not grant it.**

### Audit at claim time, by the manager

*The manager's own note, not a change to the condition above.*

**Clause 1's two quoted facts hold**, verified in the contract as it stands: the code-slot sentence is present
verbatim, and the *Words used exactly* entry reads exactly *"the right to modify product code, held by one worker at
a time."* **Clause 2's two anchors hold** in `map.md`: the paragraph opening *"**Landing policy, now settled and
binding on this map too**"* occurs once, and the sentence *"No branch is ever created or switched, nothing is ever
pushed, and history is never rewritten"* occurs once.

**But clause 2 collides with a shipped standard that landed after this condition was written, and the manager cannot
repair it.**

Clause 2 says `map.md` is *"edited under this effort's standing never-delete rule: superseded text is **marked as
superseded and left in place**, and new text is added around it."* Node 68's worker wrote that while [Say in the
conventions document how the map and its history are written](64-conventions-say-how-the-map-is-written.md) was
still claimed. **That node has since resolved and landed as commit `91e9d27`, and what it shipped says the
opposite:**

> So the map is rewritten as it changes rather than grown by appending: **the superseded text moves out**, and what
> replaces it stands alone.

> **This deletes nothing.** Text moved to `map-history.md` is moved **verbatim**… The never-delete rule is
> *satisfied by the move* rather than exempted from it.

**Mark in place, or move out. The condition demands one and the shipped conventions document now requires the
other.** Both are honest readings of never-delete — the condition's is what never-delete meant before node 64, and
the document's is what it means now.

**Left unrepaired, and carried to the worker as a correction of fact.** A condition is not the manager's to rewrite
([An acceptance condition is self-contained text](33-condition-is-self-contained.md)), and choosing between them
would decide which text a reader of the map meets — a judgement about the deliverable rather than a clerical fix.
**The worker is told both, and told that resolving it is a flag rather than a silent choice.**

**This is [The checker has no form for two clauses of one condition that cannot both
hold](66-two-clauses-that-cannot-both-hold.md)'s shape, arriving across a node boundary rather than inside one
condition** — and it is the case that node was opened one node too early to cover. It is offered there as evidence:
a condition can be falsified not only by its own clauses but by a standard that lands between its writing and its
claiming, which no mechanical check reads and which only the claim-time audit catches.

**One thing the condition does not say and the worker must be told.** It writes `map.md`, which the implementation
contract's hard rule 1 forbids. The human's licence for this node is carried into the spawn in their own words.

### The human's ruling on the condition's two-file clause

*Recorded at the manager's raise, before any check was spent.* The manager put it to them that the condition demands
*"Two files are edited, and nothing else is"* while the work edits three — because the worker took
`graph-conventions.md`'s shipped `## Writing the map` rule over the condition's mark-in-place clause, and moving
superseded text out means writing `map-history.md`. Their word, `verbatim`:

> *"for 74 ok"*

**So the departure stands and the third file is permitted.** The condition is otherwise unamended: every other
clause is checked as written. **The manager did not repair the clause itself** — a condition is not the manager's to
rewrite, and [When an AFK worker cannot proceed](23-worker-cannot-proceed.md) makes amending one the human's act, in
place, which they did not do. What they gave is a **licence for this attempt**, so the checker is told the file
count is licensed and everything else is checked against the condition's text.

**The permanent fix has an owner already.** Node 74's condition inherited `map.md`'s own staleness — the map's
standing preference *"An in-place update never deletes"* still says superseded map text stays where it is, which
node 64 falsified — and the worker minted a node for exactly that, reported below. **Until it lands, any condition
written by quoting the map faithfully will inherit the same contradiction**, which is why the claim-time audit could
not have caught this one by reading the condition against `map.md`: the two agreed.

## Answer

The worktree lifecycle now stands in both files the condition names, and in a third the shipped conventions require.

**`.claude/skills/expedition-implementation/SKILL.md`.** The code-slot sentence now reads: *"You hold **a code
slot** for the whole of this node — from your first edit until the human has approved your work. How many slots an
effort runs is that effort's own setting, and it may be more than one, so another implementation worker may be
running alongside you. **The tree your spawn names is yours alone for the whole of the node**, and every file you
edit is inside it."* The *Words used exactly* entry now reads: *"**code slot** — the right to modify product code.
One worker to a slot; how many slots an effort runs is that effort's own setting."* **Hard rule 3 is untouched,
wording included.**

**The contract names no tree kind.** It says *the tree your spawn names*, so it is true of a worktree, of a main
tree, and of whatever a later runtime hands a worker — the same tree-agnostic property [Run an implementation node's
work in a worktree](68-implementation-in-a-worktree.md) found already true of the checker contract's third given.
**The isolation clause is written positively** (*every file you edit is inside it*) rather than as a ban, so the
forbidden behaviour is never spoken.

**`.scratch/graph-workflow/map.md`.** The landing-policy item is now three paragraphs: the lifecycle as it runs
(worktree off `HEAD` on a branch carrying the node's id, outside the repository's working tree; uncommitted through
checker and gate; on approval commit, rebase, re-run the bar, `git merge --ff-only`, remove and delete;
`git rebase --abort` and a correction round on conflict; a correction round on a post-rebase bar failure; worktree
removed and branch deleted on reject, committed onto that branch first where the human asks to keep it; nothing ever
pushed; graph files still committed periodically by the human) — then the slot count as a setting of the effort,
standing at one, with occupancy discovered by counting the live worktrees — then what it supersedes.

**A reader meets what holds now before what it replaced.** The superseded sentence is quoted in the third paragraph
with its two dead clauses named and *nothing is ever pushed* kept live, and the paragraph it came from lives in full
in `map-history.md`.

**`.scratch/graph-workflow/map-history.md`** carries the old landing-policy paragraph under a new heading, *The
landing policy in the form it had before worktrees*. **The move is byte-identical** — checked by diffing the moved
line against `git show HEAD:.scratch/graph-workflow/map.md`, not by eye.

### The one call a later reader would have to re-derive: which never-delete rule the map was edited under

The condition said mark in place; `graph-conventions.md`'s `## Writing the map`, shipped by [Say in the conventions
document how the map and its history are written](64-conventions-say-how-the-map-is-written.md) **after the
condition was written**, says the superseded text moves verbatim to `map-history.md` and the never-delete rule is
*satisfied by the move rather than exempted from it*. **The worker took the shipped conventions.** In its words,
three things decided it: *"the conventions are this effort's live standard and the condition's clause predates them;
the map's own header already tells its reader that history lives in `map-history.md`, so marking in place would put
the map back into the shape node 59 took it out of; and the reader the map is optimised for is every worker, cold,
once per node, which is the effort's largest measured recurring cost."* **The condition's *reason* — never-delete —
is honoured; its *mechanism* is not.**

**Why it was a flag and not a raise, in the worker's words:** *"The three raise triggers were tested. The decision
reaches no further than these files; I hold a recommendation I believe; and the broken thing is a procedural clause
overtaken by a standard, not a demand I had to rewrite to work — both routes are executable and deliver the same
content into `map.md`. What differs is where four sentences of superseded text sit and a file count, which the human
can flip in one correction round."*

### The correction the worker made to the manager's spawn

**The spawn said the tree was clean at `6fb738b` and that `git diff HEAD` would be exactly its change. It was not** —
two node files carried the manager's own claim-time bookkeeping, written after that commit. The worker caught it by
running `git status` before trusting the claim. Its words, which the manager has adopted as practice:

> **A worker told its baseline is clean has no reason to check, and the one that does not check reports a diff
> containing someone else's writing.** The cheap fix is for the spawn to name the paths the manager knows are dirty
> rather than to assert the tree is clean.

**Method skills.** `/naming` and `/coding-principles` were both invoked and neither had a part to leave unrun.
`/naming`'s method found no rename: *"`code slot` still round-trips against its changed definition, since *slot*
already carries 'one of a set of a fixed size', which is exactly what the count establishes."*

## Flags

`74.1` **· settled** `ASSUMPTION` — **The map was edited under the shipped conventions document rather than under the acceptance
condition's never-delete clause, and that wrote a third file.** In the worker's words: *"The condition required
superseded text to be marked as superseded and left in place; `graph-conventions.md`'s `## Writing the map`, which
landed after the condition was written, requires it to move verbatim to `map-history.md` instead. I took the
conventions: they are the live standard, the map's own header already points its reader at `map-history.md` for
history, and appending to `map.md` costs every worker on every node."* **The human licensed the departure** at the
manager's raise — *"for 74 ok"* — and the checker verified the move byte-identical.

`74.2` **· settled** `ASSUMPTION` — **Six statements elsewhere that the worktree lifecycle falsifies were left standing**, because
clause 2 reaches one paragraph. Three in `map.md`: the standing preference *"An in-place update never deletes"*, the
Claude Code runtime fog item still listing worktrees as an unadopted upgrade, and the asynchronous-landing item still
pricing a reject as *"a forward revert rather than a cleaned tree"*. Three in `CONTEXT.md`: **Code slot** (false on
both sentences), **Reject**, and **Salvage**. In the worker's words: *"Carrying a resolved node's decision into the
map is the manager's bookkeeping, which is the part of the graph-file ban the human's licence for this node
explicitly leaves standing, and `CONTEXT.md` is outside the two files the condition names."*

## Review

**Checker, run 1 — `PASS`**, over the whole acceptance condition and the bar, with nothing handed back under
`NOT COVERED:`.

**It settled the moved-standard question first, as its contract requires, and it had to derive that the question
even arose** — `map.md` is itself one of the bar's standards, which nothing told it. It compared the three
bar-bearing blocks byte-for-byte against `6fb738b`: standing preferences (6,566 bytes), ground rules (792), the four
standing rules (766) — **all three identical**. *"Only a `## Notes` item the condition told the work to change
moved. Check intact."*

**Every measurement was made on unwrapped text rather than line-by-line**, and the two that matter most were
hashed rather than eyeballed: the moved paragraph is `a4b3f0d1a9a0aa68c1db98466f06895f` **on both sides** with an
empty `diff`, and hard rule 3 extracted from both sides came out `IDENTICAL: YES`, with rules 4–7 identical in the
same extraction and the diff carrying exactly two hunks, neither in the hard-rules block.

**Four readings stated rather than taken silently.** The condition phrases the isolation clause negatively and the
shipped text states it positively — *"same extension, and `/writing-for-agents`'s Negation lever prefers the
positive form."* *"Must stop asserting one"* was read as *stop asserting that only one worker at a time may touch
product code*, which the new entry does, while *"one worker to a slot"* is a different claim and is what clause 1
requires. *"In this order"* was read as binding the seven items' relative order and not the paragraph's tail. And
the two further statements were not required inside the same paragraph, the condition introducing them with *"It
further states"*.

**It ran the `_Avoid_` scan by hand**, as the map's measured trap requires, over the unwrapped concatenation of
every added line across all three paths: four hits, all resolved — `run` and `where` the ordinary-English class,
`correction` only in *correction round*, and `tree` the condition's own word, which became its second question.

**It ran the reviewing skill's Standards axis as a dispatched agent handed its material rather than sent looking** —
six standards by absolute path, the captured diff, the fixed point, the smell baseline in full, the condition's
mandated constraints listed *"so it would not report them as the author's choices"*, and the `_Avoid_` trap; denied
`nodes/`, `decisions.md`, `flags.md` and commit-message bodies. **Of its six findings it dismissed four**: three as
condition-dictated wording the worker had no latitude over, and one on the file's own vocabulary — it read *"the
bar's commands"* as declaring a command where the repo has none, but both shipped files already use that phrase for
commands **discovered** per repo, which is what ground rule 1 asks for.

### The two questions it handed back, neither blocking

**1. The glossary now states the superseded rule, and the condition forbade touching it.** `CONTEXT.md`'s **Code
slot** — *"held by one worker at a time. Occupancy is discovered from the working tree rather than recorded"* —
**contradicts both shipped files on both counts**, and `.claude/skills/expedition-prototype/SKILL.md` still carries
*"held by one worker at a time"* in its own glossary. `map.md` calls that glossary a precondition for writing
anything and says *"the glossary is authoritative"*, **so the authoritative source now states the retired rule.**
Secondary and same cause: **Reject** and **Salvage**.

**It supplied the extent, which is what makes this a sweep rather than four instances**: a paragraph-level unwrapped
scan over every `.md` under `.claude/skills/` plus `CONTEXT.md` — *"the complete set of shipped prose in this
repo"* — matching `/code slot|one worker at a time|working tree is cleaned|worktree/i`. **Those four entries in two
files are every instance.** Note that it found one the worker did not: the `expedition-prototype` entry.

**2. `SKILL.md` uses bare *tree* for the worktree, in a file where *tree* already means something else.** The same
file says *"the standing quality properties every implementation leaves the **working tree** meeting"*, and
`CONTEXT.md` refuses *tree* as a synonym for **Graph**. `map.md` names the thing **git worktree**; `SKILL.md` never
uses that word, **so one concept has two vocabularies across the two files this node edited.** The word is the
condition's own, so it was not the worker's to change.

**Gate: awaiting the human.**

**Gate: `approve`.** The human's word, `verbatim`: *"approve"*.

**Both flags settled by that approval**, under the standing instruction at [Whether flags.md survives the
settle-at-close practice](27-does-flags-file-survive.md). The payload presented `74.1` and `74.2` in full, each with
what was done and why — the duty the manager failed at [Say in the conventions document how the map and its history
are written](64-conventions-say-how-the-map-is-written.md)'s gate and was corrected on.

**`74.1` was already licensed before the check was spent**, at the manager's raise, so the approval confirms rather
than discovers it. **`74.2` is settled as *reported and carried*, not as *fixed***: its six statements are still
false on disk, and they are [Update the map items that nodes 64 and 68 left
stale](80-map-items-nodes-64-and-68-left-stale.md) and [Bring the glossary's code-slot and reject entries up to the
worktree lifecycle](81-glossary-code-slot-and-reject.md). Settling the flag ends the manager's obligation to raise
it again, not the defect.
