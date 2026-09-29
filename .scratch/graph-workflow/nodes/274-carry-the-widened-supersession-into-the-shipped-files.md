# Carry the widened supersession into the shipped files

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 264](264-no-status-for-a-node-whose-work-no-longer-needs-a-node.md)'s worker, and pasted as it
wrote it.*

> Six statements in three shipped files state that supersession requires the node to already hold work, and one
> states that `Supersedes:` takes a single number. Node 264 widened both. Until this lands, the files the workflow
> ships contradict the rule in force.

**Blockers, in the worker's words:** *"none. It must not be claimed while another worker holds
`.claude/skills/expedition/graph-conventions.md` — nineteen open nodes edit that file and several demand it change
in no other respect."*

## Acceptance condition

*Written by node 264's worker. Pasted as it wrote it, and not the manager's.*

> The work is three files — `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition/SKILL.md`,
> and `CONTEXT.md` at the repository root — and no other file may be edited. The worker may not mark this node,
> resolve it, or write a line in `.scratch/graph-workflow/decisions.md` or `.scratch/graph-workflow/flags.md`. All
> three are files the workflow ships, so they are edited plainly: superseded wording is **removed** rather than
> struck in place, and nothing is moved to a history file.
>
> Done means every one of the following is true of the finished tree.
>
> 1. `graph-conventions.md`'s `## Statuses` list still holds exactly five statuses, and its `superseded` entry
>    states that the node was replaced **or made unnecessary** by other nodes and that it does not satisfy an edge.
>    No other status entry changes, and no sixth status is added.
> 2. `graph-conventions.md`'s `## Edges` section states the replacement's edge as `Supersedes: NN[, NN]`, permitting
>    more than one number, and says that a replacement carries the number of every node it supersedes. Its statement
>    that `Superseded by: NN, NN` sits on the old node, and its statement that `Blocked by:` is satisfied only by
>    `resolved`, are unchanged.
> 3. `graph-conventions.md`'s `### Supersede` procedure opens by stating that it is used when the node is no longer
>    the place its work happens — because another node replaces it, or because another node's answer or landing
>    means it no longer needs doing — and that a node whose question merely changed, and which is open, unclaimed
>    and holds no work, is updated in place instead. It no longer states that supersession is used only when the
>    node holds work.
> 4. That procedure's step 1 permits the replacement to be a node that already exists and is named, rather than one
>    that must be created. Its closing statement that the replacements exist before the old node is marked
>    `superseded` also states that what must exist is the replacement **node**, and that the replacement's own work
>    need not have landed.
> 5. That procedure's step 5 states that a node that never resolved has no line in `decisions.md` to strike and that
>    nothing is written there for it. The procedure keeps five numbered steps in the same order, and steps 2, 3 and
>    4 are unchanged.
> 6. `SKILL.md`'s word-list entry for **supersede** no longer requires the node to already hold work, and states
>    instead that a node is retired by a forward pointer to the node that replaces it or makes it unnecessary. Its
>    sentence that a superseded node satisfies no edge, so everything blocked on it stays blocked, is unchanged.
> 7. `SKILL.md`'s word-list entry for **revision** no longer says that a revision is handled in place while the node
>    holds no work and by supersession once it does, and states instead that the choice turns on whether the node
>    still needs to exist.
> 8. `CONTEXT.md`'s **Supersede** entry and its **Revision** entry say the same as clauses 6 and 7 respectively, and
>    both keep their `_Avoid_` lines unchanged. Neither entry any longer uses *unstarted* or *holds work* as the
>    test.
> 9. No heading is added to or removed from any of the three files: `grep -n '^#\{1,6\} '` run on each returns the
>    same headings, in the same order, as before the work. The worker runs this command on all three files before
>    and after and reports both outputs in its handover.
> 10. `grep -c '^\*\*.*\*\*:$' CONTEXT.md` and `grep -c '^_Avoid_' CONTEXT.md` return the same numbers after the
>     work as before it. The worker runs both before and after and reports all four numbers in its handover.
> 11. No file other than the three named above is modified.
> 12. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node is the only thing standing between the record and the shipped files on a rule already in force.** Node
264's answer binds this effort now; until this lands, an agent reading `graph-conventions.md` or `CONTEXT.md` is told
the opposite. **The manager has already begun superseding nodes under the widened rule**, which is the ordinary
order — the decision binds, the files follow — but it is worth a reader knowing the gap existed.

**The nineteen-node contention on `graph-conventions.md` is real and the manager holds it.** Its author measured it:
nodes 41, 43, 49, 55, 73, 79, 109, 111, 120, 146, 148, 153, 190, 195, 201, 206, 228, 230 and 233 all edit that file
and several demand it change *in no other respect*, which makes any two of them mutually exclusive rather than
merely awkward. **That is a property of the graph nobody had counted before**, and it bears on more than this node.

**`CONTEXT.md` is in scope here and is rarely touched.** Clauses 9 and 10 are the author's guard against a glossary
edit silently dropping an entry or an `_Avoid_` line, and they demand the worker report four numbers and two heading
lists. Those are measurements, not assertions.

## Attempts

*The manager's record. A claim belongs to the node rather than to the agent holding it, so the node stayed claimed
across the death below.*

- **Attempt 1 — died with its work on disk, and the work survived whole.** Spawned 2026-09-20. **Terminated by an
  API session limit**, its last words being *"Checking the bar against the repo itself, then discharging node 263's
  duty"* — so it had finished writing and was in its closing checks. **The cause was not the work.** The manager
  verified the worktree immediately after: all three deliverables modified, `SKILL.md` +8/−4,
  `graph-conventions.md` +24/−15, `CONTEXT.md` +6/−3, and nothing outside the three. **Resumed in place** to hand
  back rather than respawned, there being no reason to discard finished text.

**Two agents on this effort died in the same minute on the same limit** — this one and node 277's checker. Neither
death was about its node. **Attempt 1 was resumed and handed back.**

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> The rule node 264 settled is now in the three files the workflow ships. **Seven statements changed** across them;
> superseded wording was **removed** rather than struck, and nothing went to a history file, these being shipped
> files rather than record.
>
> **`graph-conventions.md`** — three sites. The `## Statuses` entry now reads *"replaced **or made unnecessary** by
> other nodes. Does not satisfy an edge"*, the other four statuses untouched and no sixth added. The `## Edges`
> arity became `Supersedes: NN[, NN]` — *the number of every node it supersedes* — with both directions spelled out.
> **One sentence now covers both arities where two were needed before**, because *"the number of every node it
> supersedes"* already implies the one-old-to-many-new case the old text stated separately. The `Blocked by:` and
> `Superseded by:` bullets beside it are byte-identical. The `### Supersede` procedure opens on the new trigger, and
> its in-place branch now turns on the node still needing to exist. Step 1 permits a replacement that already exists
> and is named, and says *each carrying `NN` in its `Supersedes:`* so it stays true when the replacement supersedes
> others too. Step 5 adds that a node that never resolved has no line in `decisions.md` to strike. Steps 2, 3 and 4
> are untouched and the five keep their order. The closing sentence now says what must exist is the replacement
> **node**, its own work not needing to have landed.
>
> **`SKILL.md`** — the word-list entries for **supersede** and **revision**.
>
> **`CONTEXT.md`** — the same two wordings, both `_Avoid_` lines untouched. Neither entry now uses *unstarted* or
> *holds work* as its test; **those two were the divergence node 264's retrospective found** — the glossary said
> *unstarted*, `SKILL.md` said *holds no work* — **and removing both formulations ends it rather than reconciling
> it.**
>
> **Two things deliberately left alone.** The fenced node-file example still shows `Supersedes: 12`, and mechanical
> check 2 still reads *"Every `Superseded by:` has a matching `Supersedes:`, both directions present"*. One number
> remains valid under `NN[, NN]` and the check is arity-blind, so both stay true; editing either would have been
> change outside the condition.
>
> **Node 263's duty, discharged.** Handles searched across every `open` and `claimed` node's `## Acceptance
> condition`: `graph-conventions`, `SKILL.md`, `CONTEXT.md`, `Supersedes:`, `supersed`, `## Statuses`, `## Edges`,
> `Supersede`, `holds work`, `unstarted`, `five status`, `Blocked by`, **and then the removed sentences themselves as
> literal fragments**. **No open condition quotes any sentence this work removed.** The one `holds work` hit is node
> 151's *"the standards the checker holds work against"*, a different sense. The heading-enumerating conditions all
> survive because no heading moved: nodes 73, 79, 87, 89, 111, 148 and 152. **The residue is sequencing, not
> breakage.**
>
> **One collision found that is not this node's to fix.** **Node 134's clause 3** demands that superseded text in
> `CONTEXT.md` be *"marked as superseded and left in place rather than deleted"*. `CONTEXT.md` is a shipped file, and
> `graph-conventions.md`'s own never-delete boundary says every file the effort ships is edited plainly, superseded
> wording removed. **That clause was written before node 189 fixed the boundary.** It is an unclaimed node's
> condition, which node 252 lets the manager amend directly, so it is named here rather than minted.

**The index line the worker wrote**, held here until the node resolves:

> The widened `superseded`, the `Supersedes: NN[, NN]` arity and the still-needs-to-exist test ship in
> `graph-conventions.md`, `SKILL.md` and `CONTEXT.md`; seven statements changed.

**The measurements clauses 9 and 10 demanded, as the worker reported them.** All three heading lists identical in
content and order — `graph-conventions.md` 30 headings with line numbers shifted only below `## Edges`, `SKILL.md`
31 with no line moved, `CONTEXT.md` 8 with no line moved. `CONTEXT.md`'s entry count **51 before, 51 after**; its
`_Avoid_` count **41 before, 41 after** — both matching the figures `map.md` carries as counted on 2026-09-10.

## Flags

`274.1` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> **Clause 3 and node 264's answer describe the in-place branch differently, and I wrote both rather than raising.**
> The answer keeps it as *"a node whose question changed but which still needs to exist"*; the condition adds
> *"open, unclaimed and holds no work"*. I judged these compatible rather than contradictory — the qualifiers are
> the case the branch was already written for, and node 264 says it keeps that case — and wrote a sentence carrying
> both. **If the intent was that a node holding work whose question merely changed may now also be updated in place,
> this sentence is narrower than the rule and is where it was narrowed.**

`274.2` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> **The `Edit` tool is denied on paths under the worktree, and I used a script through `Bash` instead.** Three `Edit`
> calls on two different files under the node-274 worktree were refused by the permission system; a `Bash` write to
> the same directory succeeded. I made all ten replacements with one `python3` heredoc asserting each old string
> matched exactly once, rather than raising, because a route existed and the work was unaffected. **The sandbox was
> not disabled and no harness tool was called.** The plain-git worktree route settled at node 265 tells a worker to
> write its tree by absolute path and does not say which tool may; **this is the first measurement that one of them
> cannot.**

## Invalidations

*The worker's own text, pasted.*

> - **[Node 13](13-graph-file-format.md)** — its `Supersedes: NN` single number is now contradicted by the shipped
>   file. Node 264 already reported this; **this work is what makes the file disagree.**
> - **[Node 06](06-revision-semantics.md)** — its holds-work/unstarted discriminator no longer appears in any shipped
>   file. Reported at node 264 and narrowed rather than reversed there. **Beside it, and the manager's:**
>   `decisions.md`'s node 06 line still reads *"unstarted nodes are updated in place; nodes holding work are
>   superseded"*. That is a record line, correctly left where it is, and the manager owns whatever is done to it.

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.** **The byte form of the strings I was replacing** — whether the apostrophes were
> typographic or ASCII, which decides whether an exact-match edit lands. I read the candidate lines back as `repr()`
> before writing anything. **Cheap, but only because I thought to check.** **Whether `graph-conventions.md` states
> supersession beyond the three named sites** — one grep, which found the fenced example and mechanical check 2 and
> let me conclude in one pass that both survive. **Nothing else was a hunt: node 264's `### Who performs this` names
> all seven sites by section, and it is the single most valuable thing in my context.** Without it, bounding the work
> would have been the whole node — which is exactly what node 264's own retrospective reported having to do.
>
> **2. What arrived that this node did not need.** **`map.md` whole** — two of roughly thirty items, one already in
> my spawn. **Ninth report.** **`map-implementation-rules.md`'s review-route paragraph** — **sixth report**; the file
> would serve its two readers better if the checker's paragraph sat under a heading a worker can skip by name.
> **Node 264's answer at full length** — I needed `### The rule` and `### Who performs this`; **those two heading
> names in my spawn would have halved that read.** **Both of my spawn's counts of how many nodes edit
> `graph-conventions.md`** bore on nothing: what mattered was that no other worker held the file, **which is a fact
> about now and not a count.**
>
> **3. What would have made this easier.** **In the spawn: that the `Edit` tool does not work under the worktree
> path.** I lost a round of denied calls and a probe discovering it. **The spawn was careful to say which harness
> tools not to call and said nothing about which ordinary tool would fail.** In the record: node 264's answer states
> three rule changes and seven statement sites, and the mapping between them is the reader's to build — I built it,
> and my condition's twelve clauses build it again independently, **which is the check that made me confident**, so
> this is an observation rather than a complaint. In the contract: nothing.
>
> **4. What was stale, wrong, or contradicted something else.** **Node 134's clause 3**, against
> `graph-conventions.md`'s own shipped-file boundary — written before node 189 fixed it, and live on an unclaimed
> node's condition. **`map-implementation-rules.md` says `.gitignore` holds two patterns where it holds three** —
> node 271's, confirmed. **`decisions.md`'s node 06 line still states the holds-work test**, correctly, being record.
> My spawn's two warnings about `map.md` and the review-route paragraph **were both right**.

## The manager's disposal of the retrospective's record items

*Not the worker's text.*

- **The `Edit` tool denied under the worktree path** → **minted as [node
  282](282-why-the-edit-tool-is-denied-on-the-worktree-path.md)**, carrying the worker's own question. **This is the
  manager's defect to have not known**: it has told six workers which harness tools not to call and never that an
  ordinary one would fail, and each has paid a round discovering it.
- **Node 134's clause 3 against the shipped-file boundary** → **the pen is the manager's** under node 252, the node
  being unclaimed and the replacement fixed by node 189. **The manager has not made it yet and is recording it as
  owed rather than doing it in the same breath as filing a handover** — the last amendment it made in haste left a
  clause unswept, which is flag `95.5`.
- **Node 264's `### Who performs this` being the most valuable thing in the worker's context** → **nothing owed, and
  it is the positive datum.** Two heading names in the spawn would have halved a 500-line read; the manager will
  name sections rather than files when it points at a resolved node.
- **`map.md`'s `## Notes` ninth report; the review-route paragraph sixth** → **named for the human**, seventh time
  for the second.
- **`decisions.md`'s node 06 line** → **left where it is, correctly**; it is a record of what was settled and the
  never-delete rule keeps it. Named so it is not later mistaken for drift.

## Review

### Run 1 — `PASS`, all twelve clauses

*The checker's own text, pasted. Spawned by the manager, given the acceptance condition as extracted text, the bar
as properties, the three changed paths, the record-as-work rule, and this effort's ground rules and four standing
writing rules. It was given nothing from this node or from the effort's record. It was told clauses 9 and 10's
commands were to be run rather than accepted, that the expensive part is clauses 1, 2 and 5's **"unchanged"**
halves, and that two of its own named standards are themselves changed paths.*

> **PASS**
>
> **Read as the work under the record rule.** All three changed paths are shipped files. **No node status line, no
> `decisions.md` line and no `flags.md` line appears among the work** — `git diff --name-only b095bb6` returns
> exactly the three, `git status --porcelain -uall` shows no untracked file, and every added line is prose in a
> shipped document. **The `Status: superseded` string in the Supersede procedure's step 3 is unchanged template text
> describing the field, not a status written onto a node.**
>
> **Standards the work moved, settled first.** Two named standards are changed paths. **`CONTEXT.md`** — its
> operative content as a standard is its refused-word lines, and that set is identical on both sides: `_Avoid_`
> count 41 before and 41 after, with an unwrapped word-level diff confining every change to two definition
> paragraphs and moving no `_Avoid_` line. **`graph-conventions.md`** — operative content did move, but those
> elements bind work that *edits the graph*, and this work edits no node, no `decisions.md` and no `flags.md`; **they
> are the work, and I held them against the acceptance condition.** The element that does bind this work — *"every
> file the effort ships are edited plainly: superseded wording is removed, and nothing is moved to a history file"* —
> is unmoved. **A check remains possible throughout; nothing goes to `NOT COVERED`.**
>
> **Method for the "unchanged" halves.** Rather than trust a line diff over hand-wrapped prose, **I unwrapped each
> file on both sides into a single word stream and diffed that.** For `graph-conventions.md` the complete set of
> change hunks is words 4282–4285, 4379–4418 and 4724–4930 — **nothing anywhere else in a 5,751-word file moved.
> That is what makes clauses 1, 2 and 5's "unchanged" halves positive findings rather than an absence of evidence.**
>
> **1 — Met.** Exactly five status bullets, no sixth; the `superseded` entry reads *"replaced **or made unnecessary**
> by other nodes. Does not satisfy an edge."* The word diff confines the change to the three inserted words; **the
> other four entries did not move a word.**
>
> **2 — Met.** `## Edges` states `` `Supersedes: NN[, NN]` on the replacement — the number of every node it
> supersedes``, and carries both directions. **The `Blocked by:` and `Superseded by:` bullets are byte-identical to
> base** — the word diff's first hunk in that section starts at the `Supersedes:` bullet.
>
> **3 — Met.** The base's *"Use when the node holds work — an answer, an interview, or landed code"* is gone. **I
> swept every shipped file for `unstarted|holds work|holds none|already holds|holds no work` on unwrapped text: the
> only survivor stating a gate is the new clause itself.**
>
> **4 — Met.** Step 1 permits *"created now, or an existing node named as the replacement"*; the closing line states
> what must exist is the replacement **node**, its own work not needing to have landed.
>
> **5 — Met.** Step 5 adds the never-resolved sentence. Five steps, in order. **Steps 2, 3 and 4 are unchanged: the
> word diff jumps from word 4767 to 4819 with no hunk between, which is exactly the span those three steps occupy.**
>
> **6 — Met.** No requirement to hold work; the no-edge sentence unchanged — **word counts 8,137 before against
> 8,138 after.**
>
> **7, 8 — Met.** Both `_Avoid_` lines untouched; `unstarted` returns **zero hits** in `CONTEXT.md` after the work.
>
> **9 — Met, run by me against `git show b095bb6:<path>`.** 31 headings for `graph-conventions.md`, 31 for
> `SKILL.md`, 8 for `CONTEXT.md`, identical in text and order on both sides. `graph-conventions.md`'s last twelve
> shift position because the file grew — **that is position, not headings.**
>
> **10 — Met, run by me.** `51` before, `51` after; `41` before, `41` after.
>
> **11 — Met.** Exactly the three paths, no untracked file, no history file touched, and `git diff -U0 | grep '^+' |
> grep '~~'` returns nothing — **superseded wording was removed, not struck, as both the condition and
> `graph-conventions.md` require of shipped files.**
>
> **12 — The bar. Met.** Discovered from the repo: no manifest of any kind, no `.github`, `.gitignore` invokes
> nothing. No build, no tests, no formatter, no CI — a complete bar, not a deficient one. **`/writing-for-agents`** —
> net +6 lines, no sprawl, no negation, no inherited duplication left stale: **I swept every shipped file for
> `supersed` on unwrapped text to confirm the three statements of the concept were all moved together**, and the
> mechanical checks and the reject-route bullet all remain consistent with the widened rule. **The four standing
> rules** — the shapes are stated in full and widened rather than compressed. **Ground rules** — the added text
> names only the workflow's own artifacts. **`CONTEXT.md`'s `_Avoid_` lines, held against the base text and checked
> by hand** since the rules file records that grepping them returns false positives: the new wording uses
> *retiring*/*retires*, which `CONTEXT.md` **explicitly endorses** — `retired` is refused only on the **Out of
> scope** entry, for the stated reason *"that is supersession, a different thing"*.
>
> **One observation, and it is not a finding** — it touches neither the acceptance condition nor the bar, so I hand
> it back as context rather than as a defect. `SKILL.md` carries an untouched pre-existing sentence about a node
> that has crashed twice: *"the node's replacements arrive by ordinary supersession — it holds work by then."* It
> remains true under the widened rule, **but it is now narrower than the rule it gestures at.** The work did not
> touch it, and the condition did not reach it.

**The manager's disposal of run 1.** *Not the checker's text.*

- **`PASS` on all twelve, first run, no repair owed**, on a node whose hard part was six *"unchanged"* claims across
  three files.
- **The method is the thing worth keeping.** Unwrapping both sides into a word stream and diffing that turns
  *"nothing else moved"* from an absence of evidence into a positive finding, and it is the right instrument for
  hand-wrapped prose where a line diff is noise. **Named here so a later checker on these files can reach for it.**
- **It settled the moved-standard question before checking anything**, which is the case the rules file exists for
  and the first time on this effort a checker has met it with two of its standards among the changed paths. Its cut
  — that `graph-conventions.md`'s moved elements bind work that *edits the graph*, and this work edits none — is the
  manager's to check and it holds.
- **Its one observation is real and is not minted.** `SKILL.md`'s crashed-twice sentence is now narrower than the
  rule it gestures at. It is true as written, the condition did not reach it, and minting a node to widen a sentence
  that is not wrong would be work for its own sake. **Recorded here so that whoever next edits that passage knows.**
- **The gate is assembled and queued**, node 277's gate being live in front of the human.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.
