# Collapse the rules file's two statements that accounts live in `map-history.md`

Type: implementation
Status: resolved

Blocked by: 196

## Question

*Surfaced by [Give `map-implementation-rules.md` its admission
test](196-give-the-rules-file-its-admission-test.md)'s worker, and pasted as it wrote it.*

> The opening of `map-implementation-rules.md` now says twice that the account behind a line belongs in
> `map-history.md` — once in the new admission test, which states it as a consequence of the test and is where a
> reader needs it, and once as the trailing sentence of the *"Nothing below was reworded on the way here"*
> paragraph, whose subject is otherwise the verbatim move. The second is subsumed by the first and sits under a
> lead-in it does not belong to. Which one stays, and does the loser move to `map-history.md` under the supersession
> rule or leave plainly under node 189's boundary?

**Blockers, in the worker's words:** *"none. It is the same class of defect as node 190 and touches only the file's
opening, so it must not hold a worktree over that file concurrently with another node."* **The manager has added the
edge to 196**, whose uncommitted work creates the duplication this node repairs; the two cannot run together.

## Acceptance condition

*Written by node 196's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited. The worker may
> not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. Done means all of the following
> are true of the finished tree.
>
> 1. The text before the file's first `##` heading states exactly once that the account behind a line in the file
>    belongs in `map-history.md`; the sentence *"The account behind a line here is in
>    [map-history.md](map-history.md), as it is for a line in `map.md`."* no longer stands as a second statement of
>    it.
> 2. The paragraph beginning *"Nothing below was reworded on the way here"* still carries its warning that a
>    paragraph saying *above* or *below* may point into `map.md`, and both of its worked examples — the review
>    route's two phrases — are unchanged.
> 3. Whichever text is retired leaves under one of the two routes the file itself states: appended verbatim to
>    `map-history.md` under a heading mirroring the section it came from, or removed plainly where it is a live rule
>    statement being replaced. The finished file states which route was taken.
> 4. The statement beginning **What this file admits.** keeps all of: that a line belongs only where an
>    implementation node's worker or its checker would act differently for having read it; that how a rule was
>    learned is not that; the trigger-versus-history distinction; and that whoever is already editing a passage
>    applies the test to that passage with no sweep owed. It stays at most 1,000 bytes.
> 5. Every paragraph under `## Landing an implementation node's work` and under `## What the work is held against`,
>    and both blocks of numbered rules — the five ground rules and the four standing rules for writing — is
>    byte-identical to what it was in the worker's tree before this work.
> 6. Every markdown link in the file resolves to a path that exists.
> 7. No file outside `.scratch/graph-workflow/` is modified.
> 8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its author created the duplication under a condition that forbade it from doing anything else, and said so.** Node
196's clause 1(c) required the new statement to say in its own text that such material belongs in `map-history.md`;
its clause 7 forbade removing the older sentence that already said it. **Neither clause could be breached, so both
sentences stand**, and the worker surfaced this rather than reading either clause generously. That is flag `196.2`.

**This is the fifth node this session created by a condition fencing its own worker out of a defect it created** —
after the chain 144 → 169 → 184, node 139 → 142, node 142 → 195, and node 140's *"unchanged in wording"* → node
191. **The manager records the shape and takes no view**; whether narrow conditions are worth their cost is not
this node's question and has never been anyone's.

**Its clause 3 is answerable now in a way its author could not assume.** [Node
189](189-where-the-never-delete-rule-stops.md) settled that a superseded **rule statement** is replaced plainly and
banked verbatim to `map-history.md`, while text recording what happened is struck in place — so which of the two
routes clause 3 offers applies turns on what the retired sentence *is*, and that test now exists in the file
itself.

## Interview

### Attempt 1 — the gate, and the condition amended there

**What was put to the human.** The manager raised this node's gate on a `PASS`, and the human read the finished
file and asked why history stands in it. What they were looking at is the tail of the paragraph this node edited:
*"A second statement of where the account behind a line lives once trailed this paragraph… it moved verbatim to
map-history.md rather than being struck in place."* That is *what this file said before*, which the admission test
three paragraphs above it sends to `map-history.md`. **Clause 3's last sentence is what put it there**, and both the
worker (flag `200.1`) and the checker reported the collision rather than resolving it.

**The human's word, `verbatim`.**

> 1

**The option that `1` names, quoted from the gate, and it is the manager's wording rather than a worker's:**

> **Amend clause 3** so the route statement lives in `map-history.md` only — I send node 200 a correction round to
> delete those two sentences, and it re-checks.

*The two options it was taken over: approve as it stands and leave the sentence for whoever next edits that passage
under the admission test's own rule; or reject.*

## The acceptance condition, clause 3 as amended

**The amendment is the human's.** The manager wrote the option and does not author or rewrite a condition; what
follows is the clause with its last sentence replaced, and nothing else in the condition is touched.

> 3. Whichever text is retired leaves under one of the two routes the file itself states: appended verbatim to
>    `map-history.md` under a heading mirroring the section it came from, or removed plainly where it is a live rule
>    statement being replaced. ~~The finished file states which route was taken.~~ **The `map-history.md` entry
>    states which route was taken. `map-implementation-rules.md` states none of it, and what stands in its place
>    there is the markdown link to the node that shaped the passage — which is what that file's own admission test
>    prescribes.**

**What this settles about the two flags.** `200.1` is answered by the amendment rather than by the human agreeing
with the worker: the clause the worker could not satisfy without contradicting the file no longer asks for it.
`200.2` — clause 3's two routes overlapping — is untouched by the amendment and still stands as filed.

## Flags

*Both are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`200.1` **· settled** `ASSUMPTION` — Clause 3 required the finished file to state which route the superseded sentence took, and such a statement — *what this file said before* — is exactly what the admission test three paragraphs above it sends to `map-history.md`. Both cannot be honoured in full, so the statement is one sentence, is the shortest form naming the route and its ground, and is duplicated in the `map-history.md` entry's italic note so a later editor of that passage can drop the rules-file sentence without losing the account. Decided rather than raised: the condition is satisfiable either way and the cost of the wrong choice is one sentence.

`200.2` **· settled** `ASSUMPTION` — Clause 3 offers its two routes as alternatives — banked verbatim, or *"removed plainly where it is a live rule statement being replaced"* — and the second names the very case for which the file's own procedure requires the first. Read strictly they overlap and disagree. This work took clause 3's first route as the available one and node 189's rule as deciding it, rather than reading the clause's gloss as licence to drop the sentence unbanked. Not raised: the banking reading satisfies both the clause and the file, and the other loses text.

## Review

### Checker run 1 — `PASS`

*The manager holds this run's text in the gate payload it relayed; its two questions and its outcome are
quoted in the correction round below and in the gate entry. The run is recorded as `PASS` with two questions and no
`NOT COVERED`.*

### Correction round — the human amended clause 3 at the gate

*The worker's report of the round, pasted as it wrote it.*

> Done. Amended clause 3 satisfied, and the change to `map-implementation-rules.md` is now a single line.
>
> **What I changed this round.** The two sentences stating what the file said before and which route the text took are gone from the *"Nothing below was reworded on the way here"* paragraph. What stands where the account was is a bare citation, the admission test's own prescription:
>
> > … its *"the same ground as the bar's commands above"* resolves here, the bar's commands standing above it in this file. **Shaped by [node 200](nodes/200-collapse-the-rules-files-two-map-history-statements.md).**
>
> Four words and the link. It states no route and no history, and *"Shaped by"* is the admission test's own wording for what stands in the account's place — *"the markdown link the line already carries to the node that shaped it standing in its place."*
>
> **Did the change touch anything the acceptance condition names.** Yes — clause 3's subject directly, and clauses 1, 2 and 5 re-verified because the edit is inside the paragraph all three constrain.
>
> **Verified, clause by clause.**
>
> 1. **Exactly once.** The opening holds five occurrences of the string `map-history` on three lines. Line 8 (the admission test) is the one statement that the account behind a line belongs there. Line 16 is the supersession procedure, whose subject is superseded *rule text* rather than accounts — pre-existing and untouched. Line 26's single occurrence is now **inside the node's filename** (`nodes/200-collapse-the-rules-files-two-map-history-statements.md`) and is not a statement; the link text reads *"node 200"*, so none of the node's name leaks into the prose. One statement stands.
> 2. **Warning and both worked examples byte-identical.** `cmp` of the paragraph's prefix against `HEAD` up to *"standing above it in this file."* passes.
> 3. **Route stated in `map-history.md` only.** The rules file now states none of it — the one remaining `strike-in-place` phrase in the file is line 20's pre-existing general rule, not a statement of which route this text took. `map-history.md`'s entry carries the route in its fuller form.
> 4. **`What this file admits.` — 939 bytes**, under the 1,000 cap, untouched all round.
> 5. **First `##` heading to EOF byte-identical to `HEAD`** — `cmp` passes.
> 6. **Every markdown link in both files resolves.**
> 7. Two files modified, both inside `.scratch/graph-workflow/`.
> 8. **Bar.** Nothing to run (no build, no tests, no formatter, no CI). The four words added carry no word `CONTEXT.md` refuses, and the citation-only form is what standing rule 2 asks for — *states its current form and cites the nodes that shaped it; it does not restate what they hold.*
>
> **`map-history.md` is untouched.** Its diff against `HEAD` is still `13 0` — the original append, nothing added, nothing reworded.
>
> **Byte counts.** The paragraph went 499 (at `HEAD`) → 795 (at the gate) → **483** now, 16 bytes below where it started. The whole change to `map-implementation-rules.md` is one line, `+1 −1`; both files together are `+14 −1`.
>
> **Uncommitted, same worktree, same base** — `/home/mathieu/projects/graph-agent/.claude/worktrees/200-collapse-two-map-history-statements` at `7343289`. Diff: `git -C /home/mathieu/projects/graph-agent/.claude/worktrees/200-collapse-two-map-history-statements diff`.
>
> **One line correcting what I filed.** My `ANSWER`'s paragraph *"Where the route is stated, and it is stated twice on purpose"* no longer holds: under the amended clause 3 the route is stated in `map-history.md` alone, `map-implementation-rules.md` carries only the link to node 200, and the edited paragraph measures 483 bytes rather than 795. Nothing else in my answer, index line, flags or surfaced nodes is affected — `200.1`'s judgement is unchanged, the clause that forced it simply no longer asks for it.
>
> My proposed commit message still stands, with one clause now inaccurate — the body's *"and the paragraph it left says so"* should read **"and the paragraph it left carries the link to the node that shaped it"**:
>
> ```
> The rules file states once that accounts live in map-history.md
>
> The opening's trailing sentence saying an account belongs in
> map-history.md is superseded by the admission test that states the same
> thing as its own consequence. Being a rule statement rather than a
> record of what happened, it took node 189's supersession route: it moved
> verbatim to map-history.md, and the paragraph it left carries the link
> to the node that shaped it. Every byte from the first ## heading to EOF
> is unchanged.
>
> Node: graph-workflow/200
> ```

### Checker run 2 — `PASS`, against the amended clause

*Pasted as the checker wrote it. The same checker was resumed rather than replaced, on this effort's standing
rule; it says itself which findings it re-established and which it carried forward.*

> All eight clauses re-established. Here is my outcome.
>
> ---
>
> ```
> PASS
> ```
>
> Second run on node 200, against the **amended** clause 3 as the whole of it. I read the two changed paths as **the work under check**, under the implementation-rules file's own rule that an implementation node's work on this effort may be the effort's own record; I derived no statement of intent from their content, and no node status line, `decisions.md` line or `flags.md` line appears among the work.
>
> **What I re-established, and what I carried forward**
>
> Re-derived fresh this round, from the worktree's `HEAD` blobs rather than from the main tree: base `HEAD` `7343289`, base blobs `27bacef` (rules) and `bc2fed0` (history); the work is now `bebe6c0` (rules, moved from run 1's `2486bdd`) and `1972a47` (history, **the same hash I recorded on run 1**, so that file did not move). Re-established from scratch: clauses 1, 2, 3, 4, 5, 6, 7, the bar in full, and the moved-standard branch. Carried forward, on the strength of that identical history hash: the survey of all 33 `##` headings in `map-history.md` that grounds the heading-mirroring judgement, my reading of `graph-conventions.md`'s `### Change the map`, and the `/writing-for-agents` text I read on run 1. I checked for changes the statement did not mention and found none — `git status --porcelain -uall` lists the same two files, and an unwrapped paragraph comparison against `HEAD` shows exactly one of 24 paragraphs differing, the same reading aid as before.
>
> **The moved-standard branch, re-settled rather than inherited.** The differing paragraph is different text this round, so I settled it again on operative content. What left is the locator sentence; what arrived is a node citation. The requirement that an account belongs in `map-history.md` is still stated by the unchanged admission test, and the route for superseded rule text by the unchanged supersession paragraph. No element the file requires or refuses was added, removed or altered — a duplicate statement and its surrounding wording moved, operative content did not. The standards stand and the check survives.
>
> **Clause 3, against the amended words**
>
> - **Route.** `map-history.md` is a **pure append** — the base blob is a byte-prefix of the finished file — carrying the retired sentence verbatim as a blockquote under `## Superseded from `map-implementation-rules.md`'s opening — the second statement that an account belongs here`, which mirrors the section it came from and follows that file's established pattern.
> - **"The `map-history.md` entry states which route was taken."** Met, twice over: *"Moved verbatim under the `Change the map` procedure at [node 200]"*, and *"It stated a rule rather than recorded what happened, so it took this route rather than strike-in-place"*, which names the alternative it did not take.
> - **"`map-implementation-rules.md` states none of it."** Met. What now stands there in place of the retired sentence is exactly `Shaped by [node 200](nodes/200-collapse-the-rules-files-two-map-history-statements.md).` and nothing else. I probed that replacement text for *verbatim*, *strike*, *struck*, *route*, *second statement*, *used to*, *before*, *replaced*, *superseded* and *account*: no hit. The route statement, and the statement of what the file previously said, are gone from the working file and live only in `map-history.md`.
> - **"the markdown link to the node that shaped the passage."** Met — a markdown link to node 200, the node whose work shaped the passage, in the form the admission test prescribes.
>
> **The clause the manager flagged, counted again.** In the text before the first `##` heading, exactly **two** sentences mention `map-history.md`. The admission test's *"…and it belongs in map-history.md, the markdown link the line already carries to the node that shaped it standing in its place"* is the one statement of the proposition. The supersession paragraph's *"its existing text is appended verbatim to map-history.md under the heading mirroring the section it came from"* states a **different** proposition — where a replaced rule's own former text goes, not where a line's account lives — and the file itself keeps the two apart, the admission test governing the account (attempts, cost, who was wrong, what the file said before) while the supersession rule governs the superseded text, with the route following *"the text's own job"*. That distinction is a judgement I am naming so it can be seen: on it, the proposition is stated **exactly once**. The retired sentence resolves to nothing anywhere in the finished file, searched unwrapped. The opening also shrank 312 bytes, from 3,667 to 3,355.
>
> **The remaining clauses**
>
> - **2. Met.** The paragraph's first 395 characters are byte-identical to `HEAD`; warning and both worked examples present verbatim, divergence beginning only after them.
> - **4. Met.** Byte-identical to `HEAD`, all four elements present, **938 bytes** within 1,000.
> - **5. Met.** From the first `##` heading to end of file, byte-identical to `HEAD` — 25,235 bytes both sides — which covers every paragraph under both headings and both numbered blocks.
> - **6. Met.** 45 markdown links, 28 unique, every relative target resolving from the file's own directory. The count fell from 46 to 45 exactly as removing one link and keeping the node link predicts.
> - **7. Met.** Only the two files, both under `.scratch/graph-workflow/`, no untracked files.
> - **8. Met.**
>
> **The bar, re-run in full.** Command half re-confirmed empty against the repo: top level holds only `.claude`, `CONTEXT.md`, `.gitignore`, `.scratch`; the manifest and task-runner sweep printed nothing; no `.github`, `.gitlab-ci.yml`, `.circleci` or `.travis.yml`; no test directory or file; the one ignore file is `.gitignore`, which invokes nothing. Nothing to invoke, so this is a **complete** bar on its remaining half. Non-command half: I re-parsed all 105 `_Avoid_` tokens and rescanned both added blocks — the rules-file addition hits **none**, and the history block hits only `where`, which the rules file itself records as measured not to be refused by any `_Avoid_` line. The four standing rules for writing hold more cleanly than on run 1: the account is now wholly out of the working file with the shapes byte-identical (rule 1), and the passage states its current form and cites the node that shaped it without restating what that node holds (rule 2) — which is rule 2 in its purest form. Rule 3 holds via the history entry's own heading, rule 4 via citation by node link with no line number. Ground rules 1-4 are untouched by a record edit that assumes no toolchain, ships nothing, and tells no agent to address the human. `/coding-principles` and `/naming` do not bite: no code, and the one name is a heading following an established convention. No reviewing skill is named for this repo, so I ran none and looked for none; the condition records no enumerator command, so there was none to run.
>
> **Run 1's second question is closed.** The amendment forbids precisely what the clause used to compel, and the work now complies: the rules file states none of the account, and the admission test's prescribed node link stands in its place.
>
> ```
> QUESTIONS:
> - The preamble's "no other file may be edited" has sharpened against the amended clause 3, not softened. Clause 3's new second sentence asserts a property of "The `map-history.md` entry", which presupposes such an entry exists — so route 2 ("removed plainly") would leave that sentence with no referent, and the verbatim-append route is now effectively mandatory rather than one of two. Strictly read together with the preamble, the amended condition is therefore satisfiable by no work at all: it requires an entry in a file it forbids editing. I did not adopt that reading. I read the condition whole — clause 7 draws the modification boundary at `.scratch/graph-workflow/`, which contains `map-history.md`, and the preamble's sentence does its work through the bookkeeping enumeration that immediately follows it (do not mark the node, do not resolve it, do not write `decisions.md` or `flags.md`) — and on that reading the condition is coherent and the work meets it. The wording is the condition's own and was not the worker's to depart from. One sentence in the preamble naming those bookkeeping files instead of "no other file" would retire this for good.
> - On the standing instruction that a collision both parties knew should have drawn a raise: I cannot establish what the worker knew, being blind to the record, so I can speak only for myself. My contract on disk routes this to a question rather than a raise, because a raise hands back no outcome and stops the check, and I can check this condition — passing that up would withhold an outcome I am able to give on work that meets the condition on the only reading under which any work could. I note that the spawn's gloss that "a raise from you does not wait on anything" differs from the contract's raise, which explicitly stops the check and issues no outcome; the file on disk won. If the human wants a collision of this shape to stop a check that could otherwise conclude, that is a change to the shipped checker contract's raise grounds rather than something I can reach by departing from the file.
> ```
>
> Nothing is left uncovered: every clause was establishable from the paths I was given plus the worktree's base blobs, so I hand back no `NOT COVERED` items. I ran no command that writes.

### Gate — `approve`

**The human's word, `verbatim`.**

> approve

*Two checker runs, both `PASS`, with one correction round between them driven by the human's own amendment.
Both flags are settled by the approval.*

## Answer

*Pasted as the worker wrote it at run 1, with its own correction after the round appended below.*

> The duplicate is gone by moving it, not by dropping it. `map-implementation-rules.md`'s opening now states once — in the admission test under **What this file admits.** — that the account behind a line belongs in `map-history.md`. The trailing sentence of the *"Nothing below was reworded on the way here"* paragraph is gone from that paragraph and stands verbatim in `map-history.md` under `## Superseded from map-implementation-rules.md's opening — the second statement that an account belongs here`.
>
> **Clause 3's route, and the call behind it.** The sentence's job was to state where an account lives — a rule that binds its reader — and not to record what happened. Node 189's boundary, as this file itself states it under *"How a rule in this file is superseded"*, puts that case on the **supersession** route: replaced here, banked verbatim there. Strike-in-place is for text whose job is to record what happened, and this text's is not. So the verbatim move, and the paragraph the sentence left says so in one sentence. **Clause 3's second route, *"removed plainly"*, was declined**: by the file's own procedure a live rule statement being replaced is banked rather than dropped, so clause 3's two routes are not symmetric alternatives for this text — one of them is what node 189 actually requires of it, and the other would lose it.
>
> **The route is stated twice, on purpose.** *"The finished file"* in clause 3 reads most naturally as the file under edit, so the route is stated there. It is also in the `map-history.md` entry's italic note, which covers the other reading at no cost.
>
> **What did not change.** The warning about *above* and *below* and both worked examples are byte-identical. So is every byte of the file from its first `##` heading to EOF, verified by `cmp` against `HEAD` rather than by reading the sections. The **What this file admits.** statement was not touched at all: it already carries all four things clause 4 names, and measures **939 bytes** against the 1,000-byte cap. The edited paragraph went 499 → 795 bytes.
>
> **One naming correction the bar forced.** The first draft used *retired* for what happened to the sentence. `CONTEXT.md` refuses that word — *"retired (that is supersession, a different thing)"*, under **Out of scope** — so the text uses this effort's settled vocabulary, *supersede* and *verbatim*, instead. The acceptance condition's own use of *retired* is the condition's text and not this file's.

**The worker's own correction to that answer after the round**, in its words:

> My `ANSWER`'s paragraph *"Where the route is stated, and it is stated twice on purpose"* no longer holds: under
> the amended clause 3 the route is stated in `map-history.md` alone, `map-implementation-rules.md` carries only the
> link to node 200, and the edited paragraph measures 483 bytes rather than 795. Nothing else in my answer, index
> line, flags or surfaced nodes is affected — `200.1`'s judgement is unchanged, the clause that forced it simply no
> longer asks for it.

**What the worker reported its work invalidates**, pasted as it wrote it:

> none. The work carries out node 189's boundary and completes what node 196's clauses 1(c) and 7 could not do together; it contradicts no resolved node.

## Annotation: the retrospective

*Filed by the manager, pasted as the worker wrote it. Its items 2 and 3 were promoted to [node
208](208-a-condition-quoting-a-refused-word-traps-its-worker.md) and [node
209](209-a-byte-identity-clause-is-discharged-by-diff.md) before this node landed.*

**RETROSPECTIVE** (the effort's standing preference, seventh part):

1. **What I hunted for.** Whether `nodes/200-…md` existed in the worktree, since clause 6 makes every link resolve and standing rule 2 makes me cite my own node — found by `ls nodes/`; I looked in the main tree first. And the `_Avoid_` line refusing *retired*, which I found only by grepping the avoid lines after drafting.
2. **What arrived that this node did not need.** `map.md` is a mandatory read and two of its ~50 items bore on the work (the never-delete preference, the seven-files line); ~28KB read for two facts. The rules file's `## Landing an implementation node's work` section — roughly 10KB of sandbox and rebase measurement — bore on nothing: clause 5 forbade changing it, and `cmp` against `HEAD` proved byte-identity without my reading a line of it. **A condition demanding byte-identity is discharged by diff, not by reading**, and saying so in the condition would let its worker skip the section outright.
3. **What would have made this easier.** The spawn's manager note 1 — clause 3's answer is in the file you are editing — was the single most useful line in the spawn and removed the whole hunt. What was missing: nothing warned that the condition's own word *retired* is refused by `CONTEXT.md` while the bar holds my prose answerable for it. A condition quoting vocabulary the bar refuses sets a small trap for its worker.
4. **What was stale, wrong or contradictory.** Clause 3's two routes overlap and disagree with the file's own supersession procedure (flag 2), and the admission test the file now carries would exclude the very sentence clause 3 makes the file state (flag 1). No number was stale: 939 bytes under the 1,000 cap and 499 bytes on the edited paragraph both held as the record had them.

## Flag `200.3` — the manager's own, against itself

*Filed by the manager. Its text is the manager's, and it is outstanding rather than settled: the human approved the
work at the gate and this is not about the work.*

**What was wrong.** The resume that sent this node's checker into run 2 told it, in the manager's words, that *"a
raise from you does not wait on anything"*. **The checker's contract says the opposite** — a raise stops the check
and issues no outcome — and what does not wait is a **question handed back alongside an outcome**. The manager's
own contract states that distinction correctly and the manager still collapsed it in a spawn.

**Why it matters beyond a wrong sentence.** The gloss was passed on to inform the checker about a standing
instruction of the human's on when a collision should draw a raise, so the one payload that carried new steering
about raising also misdescribed what raising costs. **The checker caught it and said the file on disk won**, which
is the rule that made the error harmless here and would not have made it harmless on a payload the checker read
less carefully.

**Where the repair lives.** [Node 214](214-a-condition-that-contradicts-a-standard-is-a-raise.md), which the
checker's own words now sharpen.
