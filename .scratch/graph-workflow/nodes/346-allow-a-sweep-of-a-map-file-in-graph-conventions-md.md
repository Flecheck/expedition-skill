# Allow a sweep of a map file, in `graph-conventions.md`

Type: implementation
Status: resolved
Blocked by: none

## Question

The shipped reader test forbids a sweep of a map file, so items nobody edits never meet it and the map regrows. Relax that to "not owed, but allowed".

*Reported by [node 345](345-workers-report-most-of-map-md-bore-on-nothing.md)'s worker under its `NEW NODES`, and filed by the manager. The human's words behind it, on node 345's question 2, `verbatim`: *"ok for recommended"*. Once this lands, the manager makes the pass node 345's answer describes, as its own change with no node.*

## Acceptance condition

*Authored by node 345's worker and filed by the manager.*

> The work edits `.claude/skills/expedition/graph-conventions.md` and
> `.scratch/graph-workflow/map-implementation-rules.md`, and, where the latter's superseded text must be kept,
> `.scratch/graph-workflow/map-history.md`. No other file changes. Done means all of the following hold.
>
> 1. In `.claude/skills/expedition/graph-conventions.md`, under `## Writing the map`, the sentence "The test
>    requires no sweep of a file, and permits none." is replaced by a statement that no sweep of a file is
>    owed and that one is allowed. The sentence before it ("Whoever is already editing a passage applies that
>    test to that passage.") is unchanged. No other sentence of the file changes.
> 2. In `.scratch/graph-workflow/map-implementation-rules.md`, the clause "no sweep of the file is owed or
>    licensed by it" is replaced so that the file says no sweep is owed and one is allowed, and no longer says
>    one is not licensed. The superseded sentence, as it stood before this work, appears verbatim in
>    `.scratch/graph-workflow/map-history.md` under a heading mirroring the section it came from.
> 3. No file in `.claude/` or `CONTEXT.md` still states that a sweep of a map file is forbidden or not
>    licensed. Check it with a case-insensitive search for "sweep" across those paths.
> 4. The bar applies as it does to any implementation node.

## Answer

`graph-conventions.md`'s reader test and `map-implementation-rules.md` now say a sweep of a map file is not owed but allowed; the old clause is in `map-history.md`.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1 with one question. The human took the manager's recommendation. The shipped change landed as commit `477d350`; the record changes stay in the main checkout's record. Flag 346.1 is settled at this gate. The word clash is [node 347](347-rename-sweep-of-a-file-to-a-word-the-glossary-does-not-own.md).

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Allow a sweep of a map file, in `graph-conventions.md`

ANSWER:        The shipped reader test now says a sweep of a map file is not owed but is allowed. Node 345 recorded the reason: items nobody edits never meet the test, so the map grows back.
                - `.claude/skills/expedition/graph-conventions.md`, `## Writing the map`: "The test requires no sweep of a file, and permits none." is replaced by "No sweep of a file is owed under the test, and one is allowed." The sentence before it ("Whoever is already editing a passage applies that test to that passage.") is unchanged. The paragraph is re-wrapped at the file's 105-column width, and no other sentence in it changed.
                - `.scratch/graph-workflow/map-implementation-rules.md`, the opening paragraph **What this file admits.**: ", and no sweep of the file is owed or licensed by it." is replaced by ". No sweep of the file is owed, and one is allowed." The node-191 citation stays, and a citation of node 346 is added after it, per step 2 of `Change the map`. Only the lines from the changed sentence onward are re-wrapped, at the file's 116-column width.
                - `.scratch/graph-workflow/map-history.md`: a new block is appended, `## Superseded from `map-implementation-rules.md` at node 346 — the clause that no sweep of the file is licensed`, with the subheading `### From the file's opening, *What this file admits* — the sentence on who applies the test`. The rules file's opening has no heading of its own, so the subheading names that paragraph. The block holds the superseded text verbatim with its original line breaks. It copies the whole three-line span that the diff removed, which includes the unchanged "Settled at [node 191](…)." sentence, so that check 11 holds byte for byte.
                A case-insensitive search for "sweep" over `.claude/` and `CONTEXT.md` in the worktree now finds no statement that a sweep of a map file is forbidden or not licensed. The remaining hits are the whole-graph sweep (SKILL.md lines 46, 767, 789; CONTEXT.md lines 197, 383; graph-conventions.md line 109) and the new sentence.

INDEX LINE:    `graph-conventions.md`'s reader test and `map-implementation-rules.md` now say a sweep of a map file is not owed but allowed; the old clause is in `map-history.md`.

FLAGS:         ASSUMPTION: The history block copies the whole three-line span the diff removed from `map-implementation-rules.md`, including the unchanged node-191 citation, with its original line breaks. The condition asks only for "the superseded sentence". Check 11 under `## Mechanical checks` needs every removed passage to appear byte-for-byte in the appended text, and re-wrapping the paragraph also "removed" the citation line, so copying the wider span satisfies both. I also added a citation of node 346 to the rules file, per step 2 of `Change the map`. Index sentence: Node 346's map-history block copies the whole re-wrapped span, citation included, so check 11 holds byte for byte, and the rules file now cites node 346.

NEW NODES:     none

INVALIDATIONS: Node 191 (the rules file carries accounts rather than rules) is narrowed. The part of its rule saying "no sweep … licensed" is reversed to "a sweep is allowed". Its admission test and "whoever is editing applies it" are unchanged.

CONDITIONS:    I searched the `## Acceptance condition` of every open or claimed node for "sweep", "permits none", "licensed" and "owed or". The only hit outside node 346 is node 230, clause 3, which forbids restating "that no sweep is owed". That clause is still correct, because the test still says no sweep is owed; it is just silent on "allowed". No replacement is written.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet (no checker run has reached me).
                Paths touched:
                - worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/346-sweep` (branch `worktree-346-sweep`, uncommitted): `.claude/skills/expedition/graph-conventions.md`
                - main checkout `/home/mathieu/projects/graph-agent/` (uncommitted record): `.scratch/graph-workflow/map-implementation-rules.md` and `.scratch/graph-workflow/map-history.md` (append only; the diff has 0 deleted lines, so the file before the change is a prefix of the file after it)
                Checks run: check 11 (every line the diff removed from the rules file is found verbatim in map-history.md; nothing removed from map-history.md). Check 10 has nothing to list, because the rules file has no `## Notes` section and `map.md` is untouched. Check 4 does not apply, because no labels were touched. The bar: I confirmed against the repo that it has no build, tests, formatter or CI. The top level holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, and `.gitignore` matches the recorded three entries. So the bar here is the non-command half only.
                Proposed commit message (the worktree commit carries the shipped file; the manager commits the record as it usually does):
                  Allow a sweep of a map file in the reader test

                  graph-conventions.md's reader test now says no sweep of a map file
                  is owed, and one is allowed, so items nobody edits can still be
                  brought to the test.

                  Node: graph-workflow/346

RETROSPECTIVE:
1. What I had to hunt for: the heading that should mirror the section in `map-history.md`. The rules file's clause sits in its untitled opening, not under a `##`, so I read the earlier blocks near the end of map-history.md to copy their shape. I also had to find check 11's exact demand (removed passages must appear byte-identically), which decided that the history copy keeps the original line breaks. I looked under `## Mechanical checks` in graph-conventions.md.
2. What arrived that this node did not need: almost all of map.md (about 50KB). None of its Notes bore on a two-sentence edit; I needed only the rule on where the record lives. Most of the implementation contract's sections on raising, correction rounds and writing new nodes' conditions were also unused.
3. What would have made this easier: a line in the node file or the spawn naming the history heading and quoting check 11's byte-identity rule, since re-wrapping silently makes the "removed passage" wider than the "superseded sentence" the condition names. The spawn's note pointing at the exact passage and at `Change the map` was useful.
4. Stale, wrong or contradictory: the condition says "the superseded sentence … verbatim", while check 11 demands every removed passage byte-for-byte. After a re-wrap those two differ, and I resolved it by copying the wider span (see the flag). The main checkout's `.claude/skills/expedition/graph-conventions.md` still holds the old sentence until the worktree lands; that is expected, not stale.

## Review

### Checker run 1 — `PASS`, with one question

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 285's check; the condition reached it as a verbatim copy in `$TMPDIR/c346.md`.*

> PASS
>
> This is the check of node 346, "Allow a sweep of a map file, in `graph-conventions.md`". The work sits in two places:
> - `.claude/skills/expedition/graph-conventions.md`, uncommitted in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/346-sweep` on base 8c1053b;
> - the record files `.scratch/graph-workflow/map-implementation-rules.md` and `map-history.md`, uncommitted in the main checkout. In `map-history.md`, only the block headed "Superseded from `map-implementation-rules.md` at node 346" is this work.
>
> I read the condition whole in `/tmp/claude-1000/c346.md`. Under the rules file, I read the changed parts of the two record files as the work.
>
> **Settled first: the work moved a standard.** `map-implementation-rules.md` is the file my standards come from, and this work changes one element of it: "no sweep … is owed or licensed" becomes "No sweep of the file is owed, and one is allowed." This work is not a sweep, so it does not have to be held against that element. Every other element of the file is unmoved, and I held the work against those.
>
> **Parts of the condition**
>
> - **Scope: the two record files, their history file, and nothing else.** Met.
>   - `git status --short --untracked-files=all` in the worktree shows only `graph-conventions.md`.
>   - In the main checkout, the diff of the two record files shows only the changes described below. The other uncommitted record changes there are not this work, as the spawn says.
> - **Clause 1.** Met.
>   - `git diff --word-diff=plain` changes only this sentence: `[-The test requires no-]{+No+} sweep of a [-file,-]{+file is owed under the test,+} [-permits none.-]{+one is allowed.+}`. It now reads "No sweep of a file is owed under the test, and one is allowed."
>   - "Whoever is already editing a passage applies that test to that passage." is unchanged.
>   - Every other difference in the hunk is rewrapping, with no word changed. So no other sentence changes.
> - **Clause 2.** Met.
>   - `map-implementation-rules.md` now reads "**Whoever is already editing a passage applies this to that passage**. No sweep of the file is owed, and one is allowed." It no longer says "licensed".
>   - The sentence cites the shaping node: "and the sweep allowed at [node 346](nodes/346-….md)". That link target exists in the live `nodes/` directory, as do the targets for nodes 345 and 191.
>   - The superseded sentence appears verbatim in `map-history.md`, line breaks included, under `### From the file's opening, *What this file admits*`. That heading mirrors the section the sentence came from. The sentence reads "**Whoever is already editing a passage applies this to that passage**, and no sweep of the file is owed or licensed by it. Settled at [node 191](…)." I compared it against `git show HEAD:.scratch/graph-workflow/map-implementation-rules.md` lines 11–13, from "**Whoever" onward.
>   - The `map-history.md` diff only adds lines. So the file gains text and loses none, and the removed clause is inside the appended text.
> - **Clause 3.** Met. I searched case-insensitively for "sweep" (`grep -rli sweep .claude/ CONTEXT.md`) over each hit file, joined into unbroken paragraphs. No hit says a sweep of a map file is forbidden or not licensed. The hits are:
>   - `graph-conventions.md`: the new allowance, and "the sweep and the effort closing report are built from it";
>   - `SKILL.md`: "A sweep runs only on an empty frontier", the whole-graph sweep at the effort closing report, and "What the sweep found";
>   - `CONTEXT.md`: the **Sweep** entry and the effort closing report's contents.
>   
>   All of these except the new allowance are the glossary's **Sweep**, the pass that looks for revisions nobody propagated. See QUESTIONS.
> - **Clause 4 (the bar).** Met. See below.
>
> **The bar**
>
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean in the worktree (exit 0), and also on the two record files in the main checkout (exit 0).
> - The added lines keep each file's wrap width.
>
> **Standards**
>
> I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, excluding the element the work moved, as settled above.
>
> - These bore on the work, and I found nothing against them:
>   - `graph-conventions.md`'s `### Change the map`. The superseded text was appended verbatim first, under a mirroring heading. The new statement cites the node that shaped it by markdown link. Check 11 holds: the history file only gained text, and the removed clause is inside the appended text.
>   - The writing rules.
>   - `CONTEXT.md`'s `_Avoid_` lines.
>   - `/writing-for-agents`.
>   - The ground rules.
> - `/coding-principles` and `/naming` did not bear on the work.
> - No reviewing skill is named, so I ran none.
>
> QUESTIONS:
> - A possible clash of the word "sweep". The condition's wording, which the work follows, allows "a sweep of a file" in `graph-conventions.md`. The glossary defines **Sweep** as a different thing: the pass looking for revisions nobody propagated. `SKILL.md`'s `## Words used exactly` says "A sweep runs only on an empty frontier."
>   - *Why it matters:* a reader holding the glossary term could read that line as limiting when a map-file sweep may run.
>   - *Why it is not a failure:* the word is the condition's own, and the file used it this way before this work ("requires no sweep of a file"), so it was not the worker's to change.
>   - *Form:* a use of "sweep" meaning a pass over a map file under the admission test, in a file where **Sweep** is the glossary term.
>   - *Extent:* `grep -rniE 'sweep of (a|the) file' .claude/ CONTEXT.md .scratch/graph-workflow/map-implementation-rules.md`.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The main checkout's record carries many uncommitted changes that are not this work, and I cannot attribute them. The two files handed to me as the work contain no such write.

*The manager's note:* the checker handed back a question beside its outcome, which the standing yes never covers, so this gate goes to the human.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"ok"*. The manager reads it as taking its recommendation, the one option marked recommended: "approve node 346 as it is. I'll then open a small node that renames "sweep of a file" in those two files to a word the glossary doesn't use, such as "a pass over a file", so the two meanings stop colliding. After 346 lands I'll run the `map.md` pass myself."

## Flags

`346.1` `ASSUMPTION` **· settled** — The history block copies the whole three-line span the diff removed from `map-implementation-rules.md`, including the unchanged node-191 citation, with its original line breaks. The condition asks only for "the superseded sentence". Check 11 under `## Mechanical checks` needs every removed passage to appear byte-for-byte in the appended text, and re-wrapping the paragraph also "removed" the citation line, so copying the wider span satisfies both. I also added a citation of node 346 to the rules file, per step 2 of `Change the map`. — Node 346's map-history block copies the whole re-wrapped span, citation included, so check 11 holds byte for byte, and the rules file now cites node 346.
