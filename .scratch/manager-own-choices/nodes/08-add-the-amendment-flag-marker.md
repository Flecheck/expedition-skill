# Add the AMENDMENT flag marker

Type: implementation
Status: resolved
Deliverable: own-choices
Blocked by: ~~07~~

## Question

*Proposed by the worker of [node 01](01-what-the-manager-settles-on-its-own.md), as it wrote it:* This gives the manager a marker for the flag of an amendment an agent wrote to an acceptance condition, which today fits none of the five markers. It also lets node 06's rule for a "you decide" on a flag name that marker.

## Acceptance condition

*Written by the worker of node 01, filed by the manager:*

1. In `.claude/skills/expedition/graph-conventions.md`, under the heading ``### `## Flags` ``, the sentence "There are five markers:" reads "There are six markers:". The list beneath it gains this entry, word for word: "- `AMENDMENT` — an agent amended a condition after it was written; the manager files it."
2. In `.claude/skills/expedition/SKILL.md`, under `### Changing one after it is written`, the passage saying that an amendment is carried as a flag of its own says that the flag carries the marker `AMENDMENT`. It also says that an amendment the human makes carries no flag.
3. In `.claude/skills/expedition/graph-conventions.md`, step 2 of `### Amend an acceptance condition` names `AMENDMENT` as the marker of the flag it raises.
4. No other file under `.claude/` changes. In particular, `### Two things the human can say that are not answers` in `.claude/skills/expedition/SKILL.md` is unchanged.

Scope: clauses 2 and 3 name the work itself. Clause 1's place came from `grep -rn "five markers" .claude/`, run at `d49b11e`, which returned only `.claude/skills/expedition/graph-conventions.md` line 276. Edit an instance the search reaches outside this list only on one of three grounds, and raise a flag naming the place and the reason:
- this work's own change makes the place wrong;
- the place is a further instance of the defect this condition describes;
- the work cannot meet this condition or the bar without the change.
Report any other instance, and do not edit it.

## Answer

The worker's answer, as it wrote it in its handover (under `## Handover, attempt 1`): The shipped files now carry a sixth flag marker, `AMENDMENT`. `graph-conventions.md`'s list reads "There are six markers:" and opens with "- `AMENDMENT` — an agent amended a condition after it was written; the manager files it." `SKILL.md`'s item 4 under `### Changing one after it is written` goes on "The flag carries the marker `AMENDMENT`. An amendment the human makes carries no flag." Step 2 of `### Amend an acceptance condition` raises the flag "with the marker `AMENDMENT`". After checker run 1, the list's lead-in reads "Every amendment, whoever wrote it, comes with five things, apart from the exceptions that item 4 and the paragraph after the list name."

*Manager's note:* this paragraph assembles the worker's own sentences from its handover and its fix. Landed on the deliverable branch `own-choices` as `2f0a2a9`, the gate taken under standing yes 1. The branch is not pushed.

## Flags

`08.1` `ASSUMPTION` **· settled** — I edited the sentence that introduces the list of five things under `### Changing one after it is written` in `.claude/skills/expedition/SKILL.md`, outside my condition's clauses, on ground 1, because my own change to item 4 made it wrong. Item 4 now says an amendment the human makes carries no flag. The sentence still said every amendment, whoever wrote it, comes with all five things, apart from the manager's amendments that the paragraph after the list exempts. I changed it to name item 4 as an exception too, and kept the exception's own wording in item 4 alone. The checker's run 1 found the sentence.

## Handover, attempt 1

The worker's handover, as it wrote it:

```
ANSWER:        The shipped files now carry a sixth flag marker, `AMENDMENT`.
               - `.claude/skills/expedition/graph-conventions.md`, under ``### `## Flags` ``: "There are five
                 markers:" now reads "There are six markers:". The list opens with the entry, word for word:
                 "- `AMENDMENT` — an agent amended a condition after it was written; the manager files it." It
                 stands first because the list is in alphabetical order.
               - `.claude/skills/expedition/SKILL.md`, under `### Changing one after it is written`: item 4 of
                 the five things now goes on: "The flag carries the marker `AMENDMENT`. An amendment the human
                 makes carries no flag."
               - `graph-conventions.md`, step 2 of `### Amend an acceptance condition`: the step now reads
                 "raise the amendment's flag, with the marker `AMENDMENT`, by the steps under
                 `### Raise a flag`." Node 07's sentence that skips the step for an amendment made without a
                 flag is kept, with its lines reflowed.
               - The marker covers only the amendments that still carry a flag. The paragraph node 07 added after
                 the list of five things, which exempts the manager's own fixes, is unchanged.
               - `### Two things the human can say that are not answers` is unchanged. Node 06 writes the
                 "you decide" rule that names the marker.
               - No other file under `.claude/` changes. The search `grep -rn "five markers\|six markers"
                 .claude/` over the tree returns only the new "There are six markers:" line. Nothing else in
                 `.claude/` lists every flag marker. The worker contracts' "Two/Three markers are yours"
                 sentences list only the markers each worker owns, so they stay as they are.
INDEX LINE:    Added `AMENDMENT` as the sixth flag marker in graph-conventions.md. SKILL.md's item 4 and the
               amendment procedure's step 2 name it, and a human's amendment carries no flag.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: Node 02 (resolved) is extended as node 01's worker already reported. Its answer's "Two of the
               five markers" and "No marker changes" now meet six markers, and `AMENDMENT` is a third marker
               that records a choice an agent made. Nothing is contradicted. Node 01's answer and node 07's
               answer hold as written.
CONDITIONS:    Searched for: `five markers`, `six markers`, `AMENDMENT`, `Amend an acceptance condition`,
               `Changing one after it is written`, `as a flag of its own`. I searched the open nodes'
               conditions and questions (05, 06), the claimed node 09, and the resolved answers (01, 02, 03,
               07). Node 06 (open): its amendment 1 already names `AMENDMENT`, which now exists. Its clause 4
               ("graph-conventions.md … unchanged") still holds for node 06's own work, because node 06 is
               based on `own-choices`, which will hold this change. No clause needs replacing. Node 05 and
               node 09: no match. No question changes.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none yet.
               Paths touched: `.claude/skills/expedition/graph-conventions.md`,
               `.claude/skills/expedition/SKILL.md`.
               The bar: I confirmed against the repo that it has no build, no tests and no formatter. Its
               `CLAUDE.md` `## Commands` says so, and the tree root holds no build or package files. This
               matches `map-implementation-rules.md`. The trigger file is unchanged because item 4 is not the
               governing statement of a manager trigger-duty or of the priority.
               Node 06, of this effort, is written against `graph-conventions.md`. Its clause 4 keeps that
               file unchanged for its own diff only.
               Proposed commit message:
                 Flags: add the AMENDMENT marker for an agent's amendment to a condition

                 Node: manager-own-choices/08
```

## Review

### Checker run 1 — `FAIL`, the acceptance condition

The checker's entry, as it wrote it:

```
FAIL: acceptance condition

All four clauses hold as written. The work fails on one place that its own change made wrong. Under `### An edit outside the condition's list`, such a place is a finding wherever it lies.

How each clause was established:
1. Clause 1 holds. `grep -rn "six markers" .claude/` returns only `graph-conventions.md:276`. Printing the list under that line shows `` - `AMENDMENT` — an agent amended a condition after it was written; the manager files it. `` word for word, and it is the first entry. The list is still alphabetical.
2. Clause 2 holds. Running `grep -rn AMENDMENT .claude/` on SKILL.md finds it at line 661, in item 4 of the list under `### Changing one after it is written` ("It is carried as a flag of its own…"). The item now reads "The flag carries the marker `AMENDMENT`. An amendment the human makes carries no flag."
3. Clause 3 holds. The same grep finds `graph-conventions.md:586`. Step 2 of `### Amend an acceptance condition` now reads "raise the amendment's flag, with the marker `AMENDMENT`, by the steps under `### Raise a flag`".
4. Clause 4 holds. `git status --short -- .claude/` shows only the two listed files. `git diff -U0 SKILL.md` has one hunk, at line 660. `### Two things the human can say that are not answers` is at line 177, so it is untouched.

Finding: a sentence the work now contradicts
- Instance. The lead-in to the list in `.claude/skills/expedition/SKILL.md`, under `### Changing one after it is written`, is still "Every amendment, whoever wrote it, comes with five things, apart from the amendments the paragraph after the list names." Item 4 now says an amendment the human makes carries no flag. The paragraph after the list exempts only the manager's own amendments ("An amendment you make under the permission above…"), so the lead-in still says the human's amendment comes with all five things, flag included. Before this work, item 4 had no exception, so the work made this sentence wrong. Both sentences are inside the section and file the condition lists, so ground 1 let the worker fix it. Found by reading the section around the diff hunk.
- Form. A sentence in the listed files that says which amendments come with the five listed things, or which amendments carry a flag, and that disagrees with item 4 as it now reads.
- Extent. I joined wrapped lines and then searched each tracked file under `.claude/` with `perl -ne 'print if /amend\w*[^.]{0,150}flag|flag[^.]{0,150}amend/i'`. It returns only `SKILL.md` item 4, the paragraph after the list, and `graph-conventions.md` steps 2 and 3. None of those contradicts item 4. The lead-in sentence is the one instance: it ties amendments to the five things without the word "flag", so that search does not catch it. The smallest set that contains every instance is the lead-in sentences of the list in that section, and that is one sentence.

The bar holds. The repository has no build, tests, formatter or CI: the root `CLAUDE.md` `## Commands` says so, and the repository root has no tooling files. `git diff --check` printed nothing (rc=0).

Standards: I read only the standards in `.scratch/manager-own-choices/map-implementation-rules.md`. These bore on this work: the glossary's `_Avoid_` lines: no refused word appears in the added text; `graph-conventions.md`: the marker list is still ordered and its entry form is unchanged; the root `CLAUDE.md` writing rules: met, and the semicolon in the clause-1 entry was dictated by the condition.

Not checked: I did not load `/writing-for-agents` and held the two added sentences against the repository's own writing rules by hand. `/coding-principles` and `/naming` do not bear on prose this small.

Trigger file: the change does not touch the governing statement of any manager trigger-duty or of their priority. `grep` finds no mention of amendments or flags in `.claude/rules/expedition-triggers.md`.

Recorded search: `grep -rn "five markers" .claude/` returns nothing in the work, because the work replaced the phrase. Run at `d49b11e` with `git grep`, it returns only `.claude/skills/expedition/graph-conventions.md:276:There are five markers:`. That matches the recorded return, and it returns the same at `132e855`.

Edits outside the condition's list: none.

Flags: the node holds none, so there was nothing to check.
```

### The worker's fix after checker run 1

What the worker changed for the finding, as it wrote it:

```
FINDING:       The sentence introducing the list under `### Changing one after it is written` in
               `.claude/skills/expedition/SKILL.md` said every amendment comes with all five things. Since
               item 4 now says a human's amendment carries no flag, that sentence was wrong. The finding is
               correct, and I fixed it.
CHANGED:       The sentence now reads: "Every amendment, whoever wrote it, comes with five things, apart from
               the exceptions that item 4 and the paragraph after the list name." The exception is stated once,
               in item 4, and this sentence only points at it. Item 4 keeps the text clause 2 requires.
               A search of `.claude/` for "five things" and "whoever wrote it" found no other sentence that
               introduces this list.
TOUCHES CONDITION: Yes. The sentence is in the section of `SKILL.md` that clause 2 names, though outside
               clause 2's text. Clauses 1 to 4 still hold. `### Two things the human can say that are not
               answers` is unchanged, and no other file changed.
PATHS TOUCHED: .claude/skills/expedition/SKILL.md, .claude/skills/expedition/graph-conventions.md
FLAGS:         (filed as 08.1 above)
PROPOSED COMMIT MESSAGE:
               Flags: add the AMENDMENT marker for an agent's amendment to a condition

               Node: manager-own-choices/08
```

### Checker run 2 — `PASS`

The checker's entry, as it wrote it:

```
PASS

The work's correction to `SKILL.md` repairs the run-1 finding. It also brought no new defect. Only the standards in `map-implementation-rules.md` were read.

What changed since run 1: I found it in the work, not from the worker's account. `git diff` shows that `SKILL.md` gained one changed sentence, the lead-in to the list under `### Changing one after it is written`. The `graph-conventions.md` diff has the same three hunks as in run 1. `git status --short` still shows only those two files modified under `.claude/`.

The run-1 finding is repaired. The lead-in now reads "Every amendment, whoever wrote it, comes with five things, apart from the exceptions that item 4 and the paragraph after the list name." Item 4 names the human's amendment as having no flag. The paragraph after the list names the manager's own amendments. The lead-in now agrees with both. The extent search from run 1 (joining wrapped lines, then a perl search for `amend…flag` / `flag…amend` over `.claude/`) finds no other contradicting statement.

Clauses:
1. Clause 1 holds. `grep -rn "six markers\|AMENDMENT" .claude/` returns `graph-conventions.md:276` "There are six markers:" and `:278`, the `AMENDMENT` entry word for word. That hunk has not changed since run 1.
2. Clause 2 holds. The same grep returns `SKILL.md:661`, inside item 4: "The flag carries the marker `AMENDMENT`. An amendment the human makes carries no flag."
3. Clause 3 holds. The same grep returns `graph-conventions.md:586`, where step 2 says "with the marker `AMENDMENT`". Unchanged since run 1.
4. Clause 4 holds. `git ls-files -m -o --exclude-standard` lists only the two files. `git diff -U1 SKILL.md` has hunks only at lines 652 and 659. `### Two things the human can say that are not answers` is at line 177, so it is untouched.

The bar: the repository has no build, tests, formatter or CI. I re-confirmed this: the root `CLAUDE.md` is unchanged against HEAD, and the repository root has no tooling files. `git diff --check` printed nothing (rc=0).
- The corrected sentence was not rewrapped, so one line is now 114 characters. The file at HEAD already has lines up to 338 characters. No standard I read sets a wrap width, so this is not a finding.

Standards: no standard has changed since I last read it.
- `map-implementation-rules.md` was last modified 2026-11-11 23:48, before my first read.
- `glossary.md` has no diff.
- The root `CLAUDE.md` has no diff against HEAD.
- The work's only change to `graph-conventions.md` is the `AMENDMENT` marker. That is an added element and part of the work, so every earlier element still binds. It is the same change as in run 1.

These standards bore on the work: the glossary's `_Avoid_` lines: the new wording uses no refused word; `graph-conventions.md`: the marker list is still ordered; the root `CLAUDE.md` writing rules: met, with one referent per pronoun and the exceptions named by place.

As in run 1, I did not load `/writing-for-agents`. I held the work against the repository's own writing rules by hand. `/coding-principles` and `/naming` do not bear on this prose.

Recorded search: I re-ran `grep -rn "five markers" .claude/`. It returns nothing in the work, because the work replaced the phrase. Run at `d49b11e`, it returns only `graph-conventions.md:276`, which matches the recorded return. This is unchanged from run 1.

The edit outside the condition's clauses, and flag `08.1`: the corrected lead-in is in a listed file, but it is not one of the places clauses 1 to 3 name. Flag `08.1` names this sentence and gives ground 1. That reason holds: run 1 showed that the change to item 4 made the old lead-in wrong. The flag says the sentence was edited and why, and both are true of the work. It is not a false flag, so I raise no question.
```

### Gate 1 — approve, `standing yes`

Taken under standing yes 1, whose scope text is, word for word: "commits on feature branches dedicated to deliverables, in the current effort". What was taken: checker run 2's `PASS`. Committed on the node's branch, and the deliverable branch `own-choices` is fast-forwarded to it.
