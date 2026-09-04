# Restructure `map.md` to what every worker needs

Type: implementation
Status: resolved

## Question

Carry out parts 1 and 2 of [What the token findings change in the workflow and its
skills](53-what-token-findings-change.md)'s answer: `map.md` keeps only what is strictly necessary for all
agents, and everything else moves **verbatim** to a sibling file it points at.

**Why, measured on the file:** it is 89,214 characters, ~22,300 tokens, and every worker reads all of it **cold
and uncached, once per node**, a subagent never reading its parent's prompt cache. About **74%** of it is append
history a worker cannot act on. At the dogfood target's 179 nodes that is ~4M tokens of re-reading one file, and
it grows monotonically. **The largest measured recurring token cost in the design.**

Reported by node 53's worker, which wrote the acceptance condition below. **Blockers: none** — it touches no
worker contract, so it does not contend for the code slot with nodes 32, 48, 49, 50 or 58.

### The licence this node runs under, in the human's own words

*Carried into the spawn as the human's words rather than the manager's, per [Whether a spawn may override a
shipped worker contract](28-spawn-overriding-a-contract.md)'s fourth spawn element.*

The implementation contract's hard rule 1 is *"You write product code. You write no graph file."* Read
literally, this node could not exist. The manager raised that; the human's ruling, `verbatim`:

> *"The graph file ban is because the manager should handle progress but here it is a work on the map itself,
> not just an update on the map. The rule is more about only doing it's work and not updating when finished as
> it's the manager job."*

So the ban stops a worker doing the manager's **progress bookkeeping**, and does not reach work whose
**subject** is a graph file. **This node's worker may edit `map.md`.** It may still not mark this node, resolve
it, or write a line in `decisions.md` or `flags.md` — that is the part of the rule that stands.

**This licence is for this node only.** The permanent fix is [Qualify the graph-file ban in the worker
contracts](58-qualify-the-graph-file-ban.md), and **this node must not touch any contract's hard rules.**

## Acceptance condition

The work is `.scratch/graph-workflow/`, and the file being changed is
`map.md` in that directory. Editing that file is what this node is for: its subject is the map itself rather
than a report of progress on other work.

Before this change `map.md` is 105 lines and 89,214 characters and holds exactly five `##` headings, in this
order: `## Destination`, `## Notes`, `## Decisions so far`, `## Not yet specified`, `## Out of scope`.
`## Not yet specified` is 51,866 characters across seven items, one of which is a single 20,589-character
paragraph; `## Notes` is 33,210 characters. The whole before-state is recoverable from `git diff`.

Done means every one of the following is true of the finished tree.

1. `map.md` holds those same five `##` headings, in that order, and no other heading at `##` level.
2. `map.md` is at most **32,000 characters** by `wc -c`. For scale, the material that must stay measures about
   29,000 characters, so this is a ceiling with headroom rather than a squeeze.
3. A new file sits beside `map.md` in the same directory holding the history moved out of it, and `map.md`
   contains a markdown link to that file. **Neither its filename nor the name it gives itself contains the word
   `provenance`**: this effort's glossary refuses that word by name.
4. **Nothing was deleted, summarised, paraphrased or shortened by the move.** For every line `map.md` loses,
   that line's text appears in the new file. Compare after unwrapping both sides — every file here wraps at
   about 100 columns, so a line-by-line comparison reports differences that are only rewrapping. A difference
   confined to a line's leading markdown (list marker, heading marks, opening emphasis) does not count.
5. Each item under `## Not yet specified` in `map.md` is at most **900 characters**, states what is not yet
   specified and what would settle it, and names by markdown link the nodes that shaped it. **None of them
   recounts what those nodes hold.**
6. The block in `## Notes` beginning with the line `**Ground rules for this effort.**`, and the five numbered
   rules under it, are **byte-identical** to their before-state, recoverable from `git diff`. This block is
   copied verbatim into other agents' instructions, so it may not be reworded, renumbered or reordered.
7. `## Destination` and `## Out of scope` are **byte-identical** to their before-state.
8. The bulleted list in `## Notes` introduced by `**Standing preferences for this effort:**` still holds a
   bullet for every preference it held before. Its bullet beginning `- **The node files are written for agents.`
   says three things, in whatever wording the implementer chooses: that it governs node files, where it stands
   as written; that it governs the shipped worker contracts on the ground that those are mostly format-bearing
   instruction text, which compresses badly, so what may be compressed there is the prose explaining why and
   never the named shapes; and that it does not reach `map.md`.
9. Neither `map.md` nor the new file cites a place inside any file by line number. Where either points inside a
   file it points by heading or by a quoted phrase.
10. `.claude/skills/expedition/graph-conventions.md` currently says the graph
    is four files. In the one place it lists those files it names the correct number after this change and
    describes the new file's role in one sentence. It changes in no other respect.
11. No file under any of `.claude/skills/expedition-checker/`,
    `.../expedition-grilling/`, `.../expedition-implementation/`, `.../expedition-precondition/`,
    `.../expedition-prototype/`, `.../expedition-research/` is modified.
12. Every markdown link in `map.md` and in the new file resolves to a path that exists.

### Audit at claim time, by the manager

*The manager's own note, not a change to the condition above.* Read against [An acceptance condition is
self-contained text](33-condition-is-self-contained.md) and [The clause that says no resolved node changes
cannot be self-contained](36-resolved-node-clause-cannot-be-self-contained.md).

**All twelve clauses pass, and this is the most carefully self-contained condition in the effort so far.** It
states the before-state numerically **in the condition** rather than pointing at the file for it, and names
`git diff` as the route for the byte-identical clauses — the same repair node 48's condition used. Clause 4
anticipates the false-result family the map has counted twelve of, by ruling out rewrap-only and
leading-markdown-only differences **before** the checker can trip on them.

**Two clauses quantify, and both are permitted.** Clause 11 quantifies over the **tree**, which node 36
permits. Clause 12 quantifies over links in two named files, not over the record.

**One thing verified rather than trusted.** `provenance` is refused by name in `CONTEXT.md`, so clause 3's
prohibition is real and not the worker's invention.

**One risk the condition carries and names.** Clause 2's ceiling and clause 5's per-item cap are the only
clauses that could force a *summary* where clause 4 forbids one. They are reconcilable — the live material
measures ~29,000 characters against a 32,000 ceiling — but if the worker finds them irreconcilable that is a
**raise**, not a choice, because resolving it either way would decide what is safe to lose.

### Correction to the condition's stated before-state, by the manager, at claim time

*Not a change to the condition — the manager may not rewrite one. A correction of fact the checker must hold, and
the manager's own doing.*

The condition states *"Before this change `map.md` is 105 lines and 89,214 characters"*. **It is 106 lines and
92,113 characters.** The difference is one standing preference the manager filed **after** node 53's worker took
its measurement and before this node was claimed — the human's retrospective instruction, ~2,900 characters. The
section figures move with it: `## Notes` is larger by that amount and the fog is unchanged.

**Every clause survives**, and the condition's own design is why. Clauses 4, 6 and 7 name `git diff` as the route
to the before-state rather than the numbers, so they read the true state. Clause 2's 32,000 is a **ceiling**, and
the live material's ~29,000 is unaffected by an addition that is itself live material — though the headroom is now
thinner by ~2,900 characters, which is worth the worker knowing. Clause 5's per-item cap is unaffected, the
addition being in `## Notes` and not in the fog. **What is stale is two numbers in the condition's own preamble,
and nothing that is demanded.**

**Recorded rather than repaired for two reasons.** A condition is not the manager's to rewrite, and a blind
checker handed this condition as text would compare its stated before-state against `git diff` and be **right**
to report the mismatch — so it is told, rather than left to discover a discrepancy the manager caused. This is the
widened ninth requirement from [Workflow self-improvement during
use](19-workflow-self-improvement.md) applied to the manager's own edit: the statement of what changed is owed on
files left in an older form, and here the file left in an older form is the one the condition describes.

**And a commitment the manager makes for the duration of this node.** `map.md` grew ~12,600 characters today,
almost all of it filed by the manager, and this node's worker is editing it. **The manager files nothing further
into `map.md` while this node is claimed.** Anything that would have gone there waits, and goes in afterwards
under whatever structure this node lands — which is also the honest test of whether the new structure holds.

## Answer

*The worker's own words. The manager's verification sits beside them, under its own heading.*

`map.md` now holds only what a worker can act on, and the account of how each of its lines reached that form sits
verbatim in a sibling file. **Measured: 92,113 → 26,925 bytes, 106 → 82 lines — 70.8% smaller**, against a
32,000-byte ceiling. Derived at node 53's ratio for this corpus (~4 chars/token, no tokenizer here per flag
`52.1`): a worker's map read falls from ~23,000 to ~6,700 tokens, beating that node's expected *"at most ~8,000,
a cut of at least 64%"*.

**The sibling is [map-history.md](../map-history.md)** — 137 lines, 86,905 bytes. Named by the `/naming` method
from the sentence *the file beside the map holding, verbatim, the append history of how each of its notes came to
say what it says*; `history` over `archive` (which would claim retirement, false of a live preference's earlier
prose) and over `record` (which `CONTEXT.md` already spends on the whole graph). Its sections mirror the map's, in
the map's order. **Nothing was deleted, and the discharge is exact rather than argued: all 106 lines of the
before-state appear byte-verbatim in `map.md` or `map-history.md`** — clause 4 needed neither its unwrapping
allowance nor its leading-markdown allowance, because the map's paragraphs are single unwrapped lines.
Struck-through text moved struck.

**What stayed live, and why each.** `## Destination` and `## Out of scope` byte-identical; the ground-rules block
and its five numbered rules byte-identical. All eleven standing-preference bullets stayed bullets in their
original order, seven of them compressed to their preference and stripped of their accumulated account.
Byte-identical besides: the execution note, the domain note, the skills note, three bullets, the landing policy,
the portability constraint, the label vocabulary, the bar's commands, the `## Decisions so far` pointer.
Rewritten: the dogfood note (which absorbed the live residue of the retired `git init` prerequisite — the
dogfood's code lands in Lang's repo, not this one), the model-scarcity note, the file-count note, the naming note,
and the ground-rules preamble.

**The clause-8 bullet** now says all three: over node files the preference stands as written; over the shipped
contracts it stands on fragility — they are mostly format-bearing instruction text, so what may be compressed
there is the prose explaining why and never the named shapes; over `map.md` it does not reach, its reader being
every worker on every node rather than the next agent in the singular.

**The fog is nine items, none over 892 bytes.** Each states what is not specified, what would settle it, and links
the nodes that shaped it without restating what they hold — `decisions.md`'s founding rule, now the map's. **Two
before-state items left the fog rather than being restated**: *failure handling*, whose both halves are answered,
and *whether a research node is warranted*, spent as a question. Both are in `map-history.md` verbatim. The second
left live residue, which is now its own item — **nothing watches a standard that lives outside this repository**.
The never-delete item narrowed to the reader it still bites: a node file's, not this map's.

**The shipped conventions document** gained `## The five files`, the new path in its listing, and one sentence on
its role. Nothing else in it changed.

**Three facts the checker needs, none of them repairs.** First, **`git diff` overstates this node's change.**
`map.md` was already dirty at claim time, so `git diff HEAD` folds the manager's earlier in-place edits into mine:
HEAD's forms of two `## Notes` paragraphs (the naming note, the optional-blocks note) and of the last
`## Out of scope` bullet differ from the working-tree forms this node found. The before-state for every clause is
**the working tree at claim time**, which the manager's own correction pins numerically (106 lines, 92,113
characters — verified exactly). Under that before-state clauses 4, 6 and 7 hold as measured above. Under a strict
HEAD reading, two lines' pre-supersession arrangement is in neither of my files; that text is preserved in commit
`915d45a` and the retired substance survives inside the working-tree forms now in `map-history.md`. Second, **the
condition's preamble says the fog is "seven items"; it was ten bullets before and is nine now** — the third stale
number in that preamble, after the two the manager corrected. No clause depends on it: clause 5 quantifies over
the finished file. Third, **the bar was verified rather than trusted** — no manifest, no task runner, no formatter
config, no linter config, no `.github`, nothing invocable anywhere in the repo, matching what `map.md` records. So
the bar is entirely its non-command half, and ground rule 5 was discharged by locating `/writing-for-agents` by
name in the plugin (it is not in this session's skill list, exactly as the map predicts for a session started
before the rebuild) and holding the prose against it: it caught one real defect, a pointer steering by negation,
now stated positively.

### The first of those three facts was discharged by an event the worker could not see

*The manager's own note, not a change to the answer above.*

**The worker's caveat about `git diff` was true when it was written and is no longer true.** While this node ran,
the human committed the graph files themselves — `7d29001 periodic save of map`, authored 22 Aug 2026 23:04 —
which folded the manager's in-place edits into `HEAD`. `git show HEAD:.scratch/graph-workflow/map.md` is now
**106 lines and 92,113 characters**, matching the manager's corrected before-state exactly. So `HEAD` *is* the
claim-time state, `git diff HEAD` is exactly this node's change, and the worker's fallback reading —
*"two lines' pre-supersession arrangement is in neither of my files"* — never comes into play.

**The consequence is that clause 4 is discharged against the record rather than against the worker's own copy.**
The manager took all 106 lines of `HEAD`'s `map.md` and asked, of each, whether it appears byte-verbatim in
`map.md` or `map-history.md` after the change. **Result: 0 missing of 106.** No unwrapping allowance and no
leading-markdown allowance were needed, as the worker said. This is the strongest form clause 4 could have been
established in, and it was not available to the worker.

### The rest of the manager's verification, measured rather than relayed

Every clause that can be decided by reading the files was decided that way, before the checker.

- **Clause 1** — five `##` headings, in the stated order, none other: `## Destination`, `## Notes`,
  `## Decisions so far`, `## Not yet specified`, `## Out of scope`. Holds.
- **Clause 2** — `26,925` characters by `wc -c`, against a 32,000 ceiling. Holds, with 5,075 to spare.
- **Clause 3** — `map-history.md` sits in the same directory, `map.md` links to it twice, and neither the filename
  nor the name the file gives itself contains `provenance`. The word does occur in both files — inside the list of
  words the glossary **refuses** — which is the opposite of what the clause forbids. Holds.
- **Clause 5** — nine items, largest **888** characters, all under 900 by the stricter byte reading; every one
  carries between 2 and 5 markdown links. Fog total `51,865 → 7,306` characters, an **85.9%** cut. Holds.
- **Clause 6** — the header line and the five numbered rules are byte-identical: lengths `33 / 154 / 107 / 140 /
  148 / 202` on both sides. Holds as the clause names it. **One thing the checker should judge rather than take
  from the manager:** the paragraph *following* those five rules was rewritten, `1,639 → 453` characters. The
  clause says *"the block beginning with the line `**Ground rules for this effort.**`, and the five numbered rules
  under it"*, and whether that trailing paragraph is part of *the block* is a reading, not a measurement. The
  manager's own view is that the clause's stated reason — *"This block is copied verbatim into other agents'
  instructions"* — reaches exactly the header and the five rules, which is what the checker spawn copies, and not
  the commentary after them. But that is an argument, and the checker's is the one that counts.
- **Clause 7** — `## Destination` byte-identical at 423 characters; `## Out of scope` byte-identical at 2,345.
  Holds.
- **Clause 8** — **11 bullets before, 11 after, in the same order, each opening on the same words**; the block
  measures `9,609 → 6,040` characters, so seven were compressed and none was dropped. The clause-8 bullet states
  all three things in the clause's own three-part shape. Holds.
- **Clause 9** — `map.md` carries **zero** line-number citations. `map-history.md` carries **one**, which is the
  flagged one. Holds subject to that flag.
- **Clause 10** — the diff is 6 insertions and 1 deletion in one place: `## The four files` → `## The five files`,
  the new path in the listing, and one sentence on its role. Nothing else in the file changed. Holds.
- **Clause 11** — `git status` shows exactly three paths touched, none of them under any of the six contract
  directories. Holds.
- **Clause 12** — **221** local markdown links across the two files, **0** broken. Holds.

**The worker's second fact is confirmed and it is the manager's error, not the worker's.** The condition's
preamble says the fog is *"seven items"*; it was **ten** bullets and 51,865 characters, and is now nine. That
makes **three** stale numbers in one preamble — the two the manager corrected at claim time and this one, which
the manager did not count. The pattern is worth naming beyond this node: the correction filed at claim time
checked the two figures it had itself invalidated and did not re-derive the rest of the sentence they sat in.

**And the mechanical checks still pass on the graph as a whole**, which is what makes the restructure safe to
gate: `ALL EIGHT CHECKS PASS`, `0 broken links`, `claimed=1 open=21 resolved=41 | total 63`.

## Flags

`59.1` **· settled** `ASSUMPTION` — **Clause 9 forbids either file citing a place inside a file by line number; clause 4 forbids
altering a moved line. One moved paragraph contains "the fog paragraph at line 75".** In the worker's words:
*"I read clause 9 as governing the pointers these files offer — its own second sentence regulates where either
file 'points' — and not as reaching a preserved quotation of what the map used to say. So the text moved unaltered
and a note beneath it says that the pointer was already stale when written, that it is why this effort's fourth
standing rule exists, and which item it meant. The alternative reading makes clauses 4 and 9 jointly
unsatisfiable, and satisfying it would mean editing moved text, which is the one thing clause 4 exists to
prevent."* `map.md` itself carries zero line-number citations, verified by the manager.

`59.2` **· settled** `ASSUMPTION` — **Where the line was drawn between what a worker can act on and what it cannot.** Four cases
decided alone. In the worker's words: *"The `/writing-for-agents` saga's live residue is ground rule 5, so its
operational facts — that a session started before the rebuild does not see the skill, and that the store path
changed twice in a day — are now only in `map-history.md`. Lang's `docs/superseded/` as the reason the
source-hierarchy mechanism exists went with the paragraph that held it. The nine deltas went whole, every one
discharged and saying so. And the two spent fog items left the fog. Nothing was lost, all of it being verbatim in
the sibling; what is at stake is whether a worker will miss it"* — which node 53 settled is **measured rather than
argued**, and is [A worker reports what the map did not tell it](60-worker-reports-map-shortfall.md)'s to make
reportable.

`59.3` **· settled** `ASSUMPTION` — **The sibling file's name.** `map-history.md`, derived by the `/naming` method and
constrained only by clause 3's ban on `provenance`. In the worker's words: *"It is now also in a shipped file,
`graph-conventions.md`, so renaming it later costs two files rather than one."*

## Retrospective

*The first retrospective under the human's standing instruction, filed as the worker wrote it. Four questions were
asked; the worker was told not to estimate its own token usage, having no tokenizer, and the harness's number is
the manager's: **166,886 tokens, 52 tool uses, 29 minutes**.*

**1. What I had to hunt for.** (a) *The current state of the graph*, needed to write nine fog items truthfully.
`map.md`'s own fog said the manager's skill was *"down to two blockers, nodes 15 and 16"* — both have since
resolved, and a node for that skill still does not exist. I looked in the map first, because that is what the item
is; the authoritative answer was one `ls nodes/*.md` plus a grep of `Type:`/`Status:`/first line, which is cheap
and which nothing pointed me at. (b) *The true before-state.* The node told me the corrected line and character
counts, and I verified them exactly — but nothing told me that `git diff` mixes the manager's own uncommitted
edits into my diff. I found it by diffing `HEAD` against a copy of the working tree, which I had taken as a
precaution before my first edit. (c) *`/writing-for-agents`*, found by `find /nix/store -name writing-for-agents`
in two commands. The map's refusal to carry the path and its instruction to locate the skill by name worked
exactly as intended.

**2. What I read and did not use.** `decisions.md`'s ten pre-cap entries — I needed the register of the capped ones
and the file's opening rule, and the long early entries taught me nothing I used. `CONTEXT.md`'s *"Landing code"*
and *"Closing an effort"* sections. Node 53's `## Interview`, which I never opened — the spawn's pointer to
`## Answer` and to A1/A2 was precise and saved several hundred lines. And, unavoidably for this node only, the
~65,000 characters of `map.md` that no worker will read again.

**3. What would have made this easier.** In the spawn: one line saying that `map.md` was dirty *before* this node
and that `git diff` therefore overstates the change, naming the three lines — I had to derive it, and a blind
checker will meet the same thing without having derived anything. In the node file: the preamble's *"seven items"*
is stale by three (ten before, nine after), and it sits beside two numbers the manager did correct, which made me
trust it until I counted. Also unstated: whether clause 5's *"900 characters"* means bytes or characters — I
satisfied bytes, the stricter, and the two differ by up to six per item here. In the contract: nothing. It told me
what to do at every fork, including the one that mattered — that a clause tension I can resolve without deciding
what is safe to lose is a flag and not a raise.

**4. What was stale, wrong, or contradictory.** The two condition-preamble numbers the manager corrected, plus the
uncorrected item count. `map.md`'s fog item on the skill files, stale about its own blockers.
`graph-conventions.md` saying the map has four sections where it has five — pre-existing, and clause 10 forbade
fixing it, so it became the node I reported. Clause 9 against clause 4, as flagged. And a small confirmation of
this effort's own rule: the paragraph I moved says *"the fog paragraph at line 75"*, which was already pointing at
the wrong line before I started — the exact failure standing rule 4 was written for, found in the file that
records the rule.

### What the manager takes from it, and what it costs

*The manager's own note.* Three of the four answers name the **manager's own filing** as the friction, not the
contract and not the machinery: a stale figure in a condition preamble, a fog item stale about its own blockers,
and a dirty working tree the spawn did not disclose. That is the useful shape of the first retrospective — the
instrument found the nearest defect rather than a distant one, and the nearest defect was the manager's.

**Two of the four are directly actionable and neither needs a node.** The spawn should disclose the working tree's
state when the file under work is already dirty — which is [Workflow self-improvement during
use](19-workflow-self-improvement.md)'s ninth requirement pointed at the spawn instead of the gate, and the
manager will do it from here. And a condition's preamble figures should be re-derived whole when any one of them
is corrected, rather than the corrected ones checked in isolation.

**One is a real gap with no owner.** *"The authoritative answer was one `ls` plus a grep, which is cheap and which
nothing pointed me at."* A worker reconstructing the graph's live state has no cheap route offered to it, and the
expensive route it is given — the map — is exactly the file this node just proved a worker cannot trust for that
purpose. Reported as a node below rather than settled here.

**The cost, stated plainly, because the instruction is new and its price should be visible.** The retrospective
was ~4,800 characters of the worker's ~166,900-token run, so the marginal cost of asking is negligible against a
node. What it is not free of is the manager's own budget: filing it, judging it and acting on it is manager
context, which is the resource that has broken every session of this effort.

## Review

**Checker, run 1 — dead.** Spawned with the five givens [The checker's spawn carries the effort's ground
rules](42-checker-spawn-carries-ground-rules.md) fixed, plus the manager's before-state correction as marked
manager material. Terminated by the harness: *"Agent terminated early due to an API error: You've hit your session
limit · resets 3am (Europe/Paris)."* **It handed nothing back, and it is the sixth dead run in this effort, the
third inside two days.**

Recorded because the record of a check is the run and not only its verdict. The pattern is now the strongest weak
point in the design that the design cannot fix: the fleet is a **shared rate-limited resource**, so a check is
sometimes *unavailable* rather than failing, and the code slot idles with nothing the manager can do about it.

**Checker, run 2 — spawned fresh** after the reset window passed, with the same five givens and the same
before-state correction, and **no statement of what changed**. It is the run whose verdict this node gates on.

**Outcome of run 2: `FAIL: the bar`.** *"The acceptance condition is met. All twelve clauses established; the bar is
what failed, so this goes back to the build and not to the feature."* **This is the first check in this effort to
pass every clause of a condition and fail the work anyway** — and it is the shape node 10 designed the bar's
non-command half for, on a repo with nothing to invoke.

**All twelve clauses established, three of them on a stated reading.** It derived the before-state from the record
as instructed rather than from the preamble, and **verified the manager's `HEAD`-is-claim-time claim rather than
accepting it**: `HEAD` is `7d29001`, authored by the human at 23:04 and itself changing `map.md` by 42 lines, with
all three work files' mtimes after it (23:05, 23:13, 23:14). It confirmed the manager's correction independently —
the preamble's 89,214 / 105 / 7 understating the actual 92,113 / 106 / 10.

Its clause 4 method is worth keeping: normalising away **only** the tolerance the clause grants, it found **35 lines
lost from `map.md` and all 35 present in `map-history.md`, 0 missing**, and noted that no unwrapping was needed
because the moved content is unwrapped on both sides. It also disposed of the shortened-line case rather than
leaving it — *"each old full-length line is itself a lost line and each was found."*

**The three findings, all in newly authored text and none in moved text.** Two hard, one the checker marked a
judgement call and the manager verified and treated as a repair: an ordinal pointer to a rule that resolves to
nothing, a second ordinal pointer that is the cited rule violated by its own citation, and two over-claims in the
preamble every worker reads. **Correction round 1 sent.**

**The manager corrected the checker on one finding before relaying it, and the correction matters.** The checker
reported *"a newly authored sentence asserts a rule of this effort that does not exist"* — the note citing *"this
effort's fourth standing rule"* on line-number citation. **The rule exists and the worker's ordinal is right**:
[What the token findings change in the workflow and its skills](53-what-token-findings-change.md) holds a section
`### Four standing rules of this effort` whose fourth is *"Cite a file by heading or by a quoted phrase, never by
line number."* What does not exist is its landing in `map.md` — **because the manager committed on this node to
filing nothing into that file while it was claimed.** So the pointer resolves to nothing for the reason the manager
created, and relaying the checker's framing unchanged would have had the worker **delete a true statement**. The
repair sent was to cite node 53 by link and quoted phrase instead.

The checker was still right that it is a defect, and right for the reason that survives the correction: a pointer
that resolves to nothing is a defect however true the thing it points at. **And its finding 2 stands untouched and
is the sharper one** — an ordinal into a numbered list decays exactly as a line number does, which is the cited
rule's own argument, so the citation violates the rule it cites.

**How it ran the reviewing skill, which is the most careful route any checker has taken through one.** It read
`mattpocock-skills:code-review`'s `SKILL.md` before deciding, then **left its Spec step unrun** because that step's
search order includes `.scratch/` — *"which here is the record"*, the one thing its contract forbids it. It ran the
Standards sub-agent with the givens supplied, forbidding it the node files, `decisions.md` and `flags.md` so that
*"it was handed no less than I was and had nothing to go looking for"*. It then **discarded three of that agent's
five hard findings** as mandated by the condition or as over-reading, and most of its judgement calls *"as costs the
condition chose rather than defects — chiefly the ~23.6% corpus growth and the partial duplication of shortened
bullets, both of which clause 4 requires."*

**It noticed the tree moving under it, unprompted.** `.scratch/graph-workflow/decisions.md` and
`nodes/13-graph-file-format.md` appeared between two `git status` calls seconds apart — the manager's four-to-five
bookkeeping. It judged correctly that no clause reaches either, and **re-measured `map.md`, its heading count and
the ground-rules block md5 at the end of the check** to confirm nothing had moved under its conclusions. That is a
duty no contract gives it.

**Two questions handed back, neither blocking the correction round.**

The first is clause 4 against clause 9, which is **the worker's flag `59.1` reached independently by a blind
party** — and the checker went further than the worker did, naming which side gives way if the strict reading
holds: *"if the strict one does, it is the condition that needs amending rather than the work."* It is
the human's, and it is put at the gate rather than in the correction round because the repair does not depend on it.

The second is that clause 10's *"changes in no other respect"* **required the worker to leave a shipped standard
wrong**, and it found a third defect there beyond the two the worker reported: `## Procedures`, whose own rule is
*"Each lists every file that changes, in order"*, never mentions `map-history.md`. Filed on [Say in the conventions
document how the map and its history are written](64-conventions-say-how-the-map-is-written.md) as an annotation,
that node's condition having been written before it was known.

**Nothing handed back under `NOT COVERED:`** — every clause was establishable from the working tree and git. That
is the fourth consecutive check in this effort with no residual for the manager to hold, and the first under the
form that reached a `FAIL`.

### Correction by the manager: a dead run is not an empty run, and the manager wrote otherwise

*Filed against the manager's own text above, which first read* "It read its contract, took no other turn" *and*
"It established nothing, judged nothing and raised nothing" *— both false.*

The manager judged run 1 empty from the single line the harness surfaced as its result. **Its transcript is 27
records and 202,683 bytes**: it read widely and died before it could hand anything back. What was true is only the
narrow thing — *nothing reached the manager* — and the manager wrote the broad thing.

**This is [Naming](14-naming.md)'s lesson recurring in a new place**: *a delta stated without reading both sides is
not a delta.* Here it is a state stated without reading the run. The same error was recorded on the same evidence
at [Nothing checks that a part a checker left uncovered was ever
established](45-nothing-checks-an-uncovered-part.md) and at [Let the hard rules govern a method skill's
instructions](48-method-skill-conflicts-hard-rules.md), so **three dead runs are on the record as having "established
nothing" on no evidence beyond the harness's summary line.** Whether those two also did substantial work is not
now recoverable.

**And the reason it matters is a token finding, raised by the human.** A dead run's work is recoverable by
**resuming it** — the harness keeps its context addressable — and resuming is cheaper than respawning, because a
fresh checker re-pays its entire opening payload uncached, a subagent never reading its parent's cache
([What one node actually costs](52-token-cost-of-a-workflow.md)). It is **not** recoverable by reading: the transcript at
202,683 bytes would cost the manager more than the check.

**It is also cleaner than the manager claimed.** The reason recorded for respawning was that telling a fresh
checker a predecessor existed would breach node 42's bar on carrying an account of what happened. **Resuming
carries no such account** — the resumed run *is* the predecessor and learns nothing it did not see itself. So
respawning was never the required move; it was one option, and the expensive one.

**Why run 2 was still allowed to finish rather than run 1 resumed.** At the moment the human raised it, run 2 was
alive and at **74 records against run 1's 27** — nearly three times further on. Resuming run 1 would have put a
second checker on one node, behind the first. **Run 1 is instead held as the fallback** if run 2 dies too, which
on this effort's record is not a remote possibility.

**The standing practice from here: a dead run is resumed, not respawned**, unless another live run has already
overtaken it. And a run's state is reported from its transcript's size and record count, never from the harness's
summary line.

**Outcome of the re-check after correction round 1: `PASS`.** The condition met and the bar holding, over the whole
condition, with **nothing handed back under `NOT COVERED:`**. The re-check was run by **resuming the same checker
rather than spawning a third**, so it re-established nothing and re-ran only what the round could reach.

**It re-ran the bar's command half rather than carrying it over**, and confirmed no standard had moved under the
check by md5 and mtime — `graph-conventions.md` at `a543669c…`, `CONTEXT.md` unmodified, `/coding-principles` and
`/naming` unchanged since 30 July, `/writing-for-agents` a read-only store path.

**It verified finding 2 as a sweep rather than as two instances**, which is what the correction round asked of it.
It searched the general form over unwrapped text in both files and classified authored against moved **by
set-difference against `HEAD:map.md`**: **zero hits in authored text**, against 87 in moved or quoted text where
clause 4 freezes them and where the ordinals are ordinary prose rather than pointers. It validated the pipeline
against both known instances before trusting the zero, *"since a silent zero is indistinguishable from a broken
pipe"* — the discipline the map records eleven false scan results against, applied unprompted.

**And it independently verified the four repairs only the author had checked**, two of them by counting: **exactly
7 of the 11 standing preferences changed and 4 byte-identical**, and **exactly 2 history-only sections against 9
map items**, both matching the worker's claims. It then read all 48 authored lines in `map-history.md` and checked
every numeric and universal claim in them, finding no fresh instance. One soft figure it checked and chose not to
call: *"about three quarters"* measures 70.7%, *"inside ordinary prose rounding, not a finding."*

### The checker corrected its own finding, unprompted, and named the fault as the one it was faulting

*Recorded because it is the second time this effort has caught this shape, and the first time an agent caught it in
itself.*

The manager's correction of fact reached it and it checked it rather than accepting it — finding node 53's heading
and rule 4's verbatim sentence — then wrote:

> I reported that the rule did not exist; it exists. What I could actually establish — that the pointer resolved to
> nothing in every file I was permitted to read — was true, and the defect was real. But the sentence I wrote, *"No
> such rule exists"*, was wrong, and **it was wrong in the same way the thing I was faulting was wrong: I asserted a
> universal from a bounded search.** A checker blind by design should say *"resolves to nothing in the files I
> hold"* and not *"does not exist"*.

That is [Naming](14-naming.md)'s lesson a third time in one node — *a delta stated without reading both sides is not
a delta* — and this instance is structural rather than careless: **a blind checker cannot establish a universal
negative over files it is kept from**, so the wording is a standing property of the role and not a slip. It belongs
in the checker's contract, and is [What a finding must carry so it can be swept](71-what-a-finding-must-carry.md).

### One thing the check could not do, and it is the manager's to fix

**`map-history.md` is untracked, so the checker could not diff it against what it had read.** It re-derived the
property from `HEAD:map.md` plus the two current files instead, and judged the workaround *"a stronger check than a
diff would have been, since it establishes the property directly rather than the delta"* — but named it a
workaround that *"on a longer file might not have been available"*. It also paid a second full read of
`map-history.md`'s moved paragraphs purely to classify them as moved.

**The repair is the manager's and costs nothing: commit the new file before the check, or keep the pre-round copy.**
Recorded here rather than minted, being manager practice rather than a shipped rule.

**Gate: awaiting the human.**

**Gate: `approve`.** The human's word, `verbatim`: *"approve"*. Landed as commit `8a39024`, path-limited to the three work paths and not pushed.

**All three flags settled by that approval, with no separate assent asked for**, under the standing instruction
filed at [Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md) — *"when I approve
the end of the node, the flags should be considered ok"*. The payload presented `59.1`, `59.2` and `59.3` in full.

**`59.1` is settled as a reading, and the record should say which one.** The human approved a payload that named
clause 9 as **passed on a reading rather than settled**, and that named the alternative and its consequence in the
checker's own words — *"if the strict one does, it is the condition that needs amending rather than the work."* So
the approval settles the flag by adopting the reading the worker and the checker reached independently: **clause 9
governs the pointers `map.md` and `map-history.md` offer, not a paragraph they preserve verbatim.** The one
inherited `line 75` citation stands, marked as quoted rather than endorsed.

## Superseded in one respect by node 139: the file shape, not the answer

*Reported by [`map.md` has grown back most of what node 59's restructure
saved](136-the-map-has-grown-back-what-node-59-saved.md)'s worker and again by [Move the manager's material out of
the map](139-move-the-managers-material-out-of-the-map.md)'s, and filed by the manager. Nothing above is changed.*

This node's acceptance condition required `map.md` to hold **exactly five `##` headings, in this order**: `##
Destination`, `## Notes`, `## Decisions so far`, `## Not yet specified`, `## Out of scope`. **It holds three.** The
fog and out-of-scope moved to `map-manager-only.md` at node 139, landed as commit `4e38c11`.

**This node's answer is not falsified**, and both workers said so unprompted. In node 139's worker's words:

> This does not falsify node 59's answer, which is discharged and measured; it supersedes the file shape that answer
> landed, on node 59's own stated ground that the split *"is settled by measurement rather than argument"*.

**The measurement this node named node 60 to gather never came from node 60**, which is still `open` and unbuilt.
It came from the retrospective's second question — *what did you read and did not use* — which nineteen
retrospectives have now answered and thirteen of which name map sections. That instrument was built for another
purpose and nothing sweeps it: [node 141](141-nothing-sweeps-what-a-retrospective-reports-as-read-and-unused.md).
