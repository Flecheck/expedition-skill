# Ship dropping `flags.md`

Type: implementation
Status: resolved
Blocked by: ~~14~~

## Question

This makes each node's `## Flags` section the only record of an effort's flags. Agents then write each flag once, and an effort that runs indefinitely no longer needs a flag cleanup to keep an index short. What the shipped files say about `flags.md`, the flag index, check 6, flag cleanup, and which flags reach the effort closing report and region cleanup must change to match.

*Manager's note:* minted by the worker of [node 15](15-whether-flags-md-is-dropped.md) on its `NEW NODES` part, with the question and condition below as it wrote them. It gave the blockers as "14 (it edits the four worker contracts, `graph-conventions.md` and `SKILL.md`, including the flag-raising text). Node 16 also edits `SKILL.md`, in another section."

## Acceptance condition

Scope: the following command was run on 2026-10-13 over the working tree at commit `872398c449`: `grep -rlE -i "flags\.md|index of flags|seven files|flag cleanup|check 6|outstanding flag|for the index|both of a flag's entries|two separate texts|link to (your|its) node" .claude/ CLAUDE.md`. It returned these ten files:
- `.claude/skills/expedition/SKILL.md`
- `.claude/skills/expedition/graph-conventions.md`
- `.claude/skills/expedition/adoption.md`
- `.claude/skills/expedition-grilling/SKILL.md`
- `.claude/skills/expedition-implementation/SKILL.md`
- `.claude/skills/expedition-precondition/SKILL.md`
- `.claude/skills/expedition-prototype/SKILL.md`
- `.claude/skills/expedition-cleanup/SKILL.md`
- `.claude/skills/expedition-triage/SKILL.md`
- `.claude/skills/expedition-upgrade/SKILL.md`
These ten files are the ones this work may change. Other work may land in these files first, so re-run the command on the tree this work starts from. Report any instance the command finds outside the ten files, and do not edit it.
1. No file under `.claude/skills/` or `.claude/rules/` mentions `flags.md`, an index of flags, or a flag's line or checkbox.
2. In `.claude/skills/expedition/graph-conventions.md`, the heading `## The seven files` is renamed `## The graph's files`. Its file listing no longer includes `flags.md`. `grep -rn "The seven files" .claude/` returns nothing, and each place that cited the old heading now cites `## The graph's files`.
3. `.claude/skills/expedition/graph-conventions.md` states each of the following:
   - A flag's id `NN.k` stands in front of its marker on the node's `## Flags` entry.
   - The entry's first sentence is the raising agent's one-sentence report of the judgement, written for a reader who has not read the node. The full account of what produced the flag follows it.
   - A flag is outstanding until its entry carries `**· settled**`, in a position that `### How a check reads the files` allows.
   - The outstanding flags are found by searching the node files for entries not marked settled.
   - The settled-entry form shown in the file is consistent with these statements.
4. In `.claude/skills/expedition/graph-conventions.md`:
   - `### Raise a flag`, `### Settle a flag` and `### Amend an acceptance condition` each write the flag only to the node file. Each still has its writer run check 6 over the flag's entry.
   - `### Start an effort` no longer creates `flags.md`.
   - The opening paragraphs give no example drawn from `flags.md`.
   - In the passage on a `FRICTION` flag raised on an effort whose product is not the expedition skill files, "its line stays unchecked" and "check the flag's line by hand" become the entry's staying unmarked, and the human's marking it settled by hand.
5. In `.claude/skills/expedition/graph-conventions.md`, under `## Mechanical checks`:
   - Check 6 reads that every `## Flags` entry begins at the start of a line with an id `NN.k` whose `NN` is its node's number, and that no two entries on one node share an id.
   - Checks 1 to 5 and 7 onward keep their numbers and their meaning.
   - `### How a check reads the files` has no rule about `flags.md`.
6. In `.claude/skills/expedition/SKILL.md`:
   - `## Flags` says that the flag's entry on its node is the raising agent's text, and that the manager adds only the id and the state.
   - `## Flags` says that only an outstanding `FRICTION` flag on an effort whose product is not the expedition skill files reaches the effort closing report.
   - The list under `## Closing an effort` carries each such flag, found by searching the node files, each with its id and the first sentence of its entry. That list carries no other flag.
   - The checker's spawn gives, for each flag the node holds, the first sentence of its entry with its id.
7. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-prototype/SKILL.md`:
   - The worker is not told to leave `flags.md` unread.
   - The manager's recording duty names `decisions.md` and not `flags.md`.
   - The section on raising a flag describes one entry, on the node. Its first sentence is a one-sentence report for a reader who has not read the node, and the full account follows it. The manager adds only the id and the state.
   - The handover's `FLAGS` placeholder asks for the sentence that opens the entry, then the rest of its prose.
8. In `.claude/skills/expedition-cleanup/SKILL.md`:
   - The frontmatter description, `## Two operations` and `## Reporting` describe region cleanup as the skill's only operation. The `## Flag cleanup` section is gone.
   - In `## Region cleanup`, a node in the set holding an outstanding `FRICTION` flag on an effort whose product is not the expedition skill files does not stop the removal. That flag, with its id and the first sentence of its entry, is listed in the set put to the human for confirmation.
   - No other outstanding flag stops the removal.
   - The report to the human lists the ids of the outstanding flags removed with their nodes.
   - The step that removes the region from the other files names no `flags.md`.
9. In `.claude/skills/expedition-triage/SKILL.md`, an older flag entry with no id is settled by giving it the next unused id on its node and marking it settled, with a note of the manager's on the node saying so.
10. In `.claude/skills/expedition/adoption.md`, the list of names reserved for the record does not include `flags.md`.
11. No other sentence in the ten files changes in meaning.
12. `.claude/rules/expedition-triggers.md` changes only where this work edits, in `.claude/skills/expedition/SKILL.md`, the governing statement of one of the manager's trigger-duties or of the priority that orders them. In that case it changes to match.
Every demand above was fixed by the human's answers on node 15, quoted in its `## Answer`, or by the text of the shipped files at `872398c449`.

*Manager's note, before the claim:* re-ran the recorded command at `5dc2681779`; it returned the same ten files, so the scope has not grown. Nothing else is written after the condition. Node 14 resolved, so the blocker is struck.

## Answer

The shipped files no longer have `flags.md`. The `## Flags` entry on each node is now the only record of a flag. All ten files the condition lists were changed, and no other file was touched.
- `graph-conventions.md`:
  - `## The seven files` is now `## The graph's files`. Its listing drops `flags.md`, and so does `### Start an effort`, whose steps are renumbered 1 to 8.
  - The `flags.md` passage is gone, including its line form, its checkbox states and the rule that `flags.md` wins a disagreement.
  - `### ## Flags` now holds the id rule (`NN.k`, in front of the marker). It says the entry's first sentence is the raising agent's one-sentence report, written for a reader who has not read the node, and that the full account follows it.
  - A flag is outstanding until its entry carries `**· settled**`, in a position that `### How a check reads the files` allows. Outstanding flags are found by searching node files for entries not marked settled.
  - The settled form reads `` `NN.k` `ASSUMPTION` **· settled** — <the one-sentence report> <the full account> ``.
  - `### Raise a flag`, `### Settle a flag` and `### Amend an acceptance condition` write only the node file, and each still runs check 6 over the entry. Settling now means adding `**· settled**` directly after the marker.
  - For a `FRICTION` flag on an effort whose product is not the expedition skill files, the outstanding case is now "its entry stays unmarked", and the human may "mark its entry settled by hand".
  - Check 6 now reads: every `## Flags` entry begins at the start of a line with an id `NN.k` whose `NN` is its node's number, and no two entries on one node share an id. Checks 1–5 and 7–12 are unchanged.
  - The `flags.md` rule under `### How a check reads the files` is removed.
  - The example from `flags.md` in the opening paragraphs is removed.
- `SKILL.md`:
  - All three citations of the heading are renamed.
  - "its flags index" is dropped from the list of the graph's files.
  - The checker's spawn now gives, for each flag, the first sentence of its entry with its id.
  - `## Flags` says the entry is the raising agent's text, and the manager adds only the id and the state. It also says only an outstanding off-product `FRICTION` flag reaches the effort closing report.
  - The list under `## Closing an effort` carries each such flag, found by searching the node files, with its id and the first sentence of its entry, and no other flag.
- The four worker contracts:
  - "Leave `flags.md` unread" is gone.
  - The recording duty names `decisions.md` only, and says the manager writes the flags onto the node.
  - `## When you raise a flag` describes one entry: an opening one-sentence report, then the full account. The manager adds only the id and the state.
  - The `FLAGS` placeholder asks for "the sentence that opens the entry, then the rest of its prose".
  - In the implementation contract, a widening flag's place, reason and ground go in "the sentence that opens the flag's entry".
- `expedition-cleanup`:
  - Region cleanup is the skill's only operation. `## Two operations` is renamed `## One operation`, and `## Flag cleanup` is gone.
  - Step 3 finds the set's outstanding flags. None of them stops the removal. Each off-product `FRICTION` flag is listed, with its id and first sentence, in the set put to the human.
  - Step 5 names no `flags.md`.
  - `## Reporting` lists the ids of the outstanding flags removed with their nodes.
- `expedition-triage`: an older flag entry with no id is settled by giving it the next unused id on its node and marking it settled, with a note of the manager's on the node.
- `adoption.md` and `expedition-upgrade`: `flags.md` is gone from the reserved names, and the heading citations are renamed.
- `.claude/rules/expedition-triggers.md` is unchanged. It holds no flag or closing-report duty, and none of the edited `SKILL.md` text is the governing statement of a trigger-duty or of the priority.

*Manager's note:* landed as `6cbf5ed0cf` on `master` by fast-forward, after the human's approval; the worktree and branch are removed. Afterwards, the manager compared every line of this effort's `flags.md` with its node's entry, found no mismatch, and deleted the file, as node 15's answer says. The file was not tracked by git, so it cannot be recovered from version control; every flag it indexed stands on its node.

## Flags

`19.1` `ASSUMPTION` **· settled** — In `expedition-cleanup` I renamed the heading `## Two operations` to `## One operation`, because the skill now has one operation. This edit is inside a listed file and goes beyond clause 8's words. Clause 8 names the section by its old heading and asks that it describe region cleanup as the only operation. A heading saying "Two operations" over that text would contradict it. A search of `.claude/skills/` found no other file citing the heading.

`19.2` `ASSUMPTION` **· settled** — In each of the four worker contracts, `## What you read` dropped the clause "leaving out any file this section tells you to leave unread". The cause is my own change: with "Leave `flags.md` unread" removed, the section names no file to leave unread, so the clause pointed at nothing. This edit is inside listed files, beyond clause 7.

`19.3` `ASSUMPTION` **· settled** — Two passages became wrong because of my change, and I reworded them without changing their meaning. Both are inside listed files and beyond the clauses.
(a) In `graph-conventions.md`'s `### Settle a flag`, the off-product `FRICTION` passage said it "changes two rules" under `SKILL.md`'s `## Flags`. The second of those rules now states this case itself. The passage now names only the settle-moment rule it changes, and says such a flag reaches the effort closing report "as `## Flags` in `SKILL.md` says".
(b) In `SKILL.md`'s `## Conflicts this contract leaves open`, "Neither of the agent's two entries has that form" became "The agent's entry does not have that form".

`19.4` `ASSUMPTION` **· settled** — In `### Settle a flag`, step 1 now says to place `**· settled**` "directly after its marker". The old step said only "mark that flag `settled`", and clause 3 requires the settled form to agree with the check-reading rule. Of the two positions that rule allows, I chose the one the settled form shows.

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

PASS

Recorded search: I ran the condition's command, `grep -rlE -i "flags\.md|index of flags|seven files|flag cleanup|check 6|outstanding flag|for the index|both of a flag's entries|two separate texts|link to (your|its) node" .claude/ CLAUDE.md`, as written, using `git grep` at the commits.
- At `872398c449` it returned the same ten files the condition records. The return matches.
- At the base `5dc2681779` it returned the same ten files.
- On the worktree after the work it returns only graph-conventions.md, expedition-cleanup/SKILL.md and expedition-triage/SKILL.md. Every remaining hit is a legitimate use of "outstanding flag" or "check 6".
- It found nothing outside the ten files. `git status` shows that only the ten listed files changed.

Clause by clause (I read `git diff --word-diff`, and searched text unwrapped by paragraph):
1. No file under `.claude/skills/` or `.claude/rules/` mentions `flags.md`, the index of flags, or a flag's line or checkbox.
   - Searches: `grep -rn flags\.md`, plus an unwrapped regex for checkbox, unchecked, `- [ ]`, `- [x]`, flag…index and capped index.
   - The only remaining "index line" hits are about `decisions.md`: the INDEX LINE handover part, "a missing index line" in `### What a failure produces`, and the glossary.
2. The heading is now `## The graph's files` (graph-conventions.md, line 43), and the `flags.md` row is gone from its listing.
   - `grep -rn "The seven files" .claude/ CLAUDE.md` returns nothing.
   - Every old citation found by `git grep "The seven files" 5dc2681779` now reads `## The graph's files`, in SKILL.md (32, 340, 391), upgrade (96), adoption (21) and graph-conventions (17, 120, 474).
   - The old citation at SKILL.md 511 pointed at the `flags.md` form, and the work dropped it.
3. `### `## Flags`` in graph-conventions.md states all of the following:
   - the id `NN.k` stands in front of the marker;
   - the first sentence is the one-sentence report for a reader who has not read the node, and the full account follows it;
   - a flag is outstanding until its entry carries `**· settled**` in a position `### How a check reads the files` allows;
   - the outstanding flags are found by searching the node files.
   The settled form is `` `NN.k` `ASSUMPTION` **· settled** — <the one-sentence report> <the full account> ``. That marker sits directly after the kind marker, which is an allowed position.
4. `### Raise a flag`, `### Settle a flag` and `### Amend an acceptance condition` each write only the node file. Each still has its writer run check 6 "over … the flag's entry on its node".
   - `### Start an effort` no longer creates `flags.md`, and its steps are renumbered 1 to 8.
   - The example in the opening paragraphs now names only `decisions.md`.
   - The FRICTION passage now reads "its entry stays unmarked" and "they may mark its entry settled by hand".
5. Check 6 now reads "Every `## Flags` entry begins at the start of a line with an id `NN.k` whose `NN` is its node's number. No two entries on one node share an id."
   - The diff of `## Mechanical checks` touches only check 6 and the removed `flags.md` bullet in `### How a check reads the files`.
   - Checks 1 to 5 and 7 to 12 are unchanged.
6. SKILL.md meets each part:
   - `## Flags` says "A flag's entry on its node is the raising agent's text", and that the manager adds only the flag's id and its state.
   - `## Flags` says "Only an outstanding `FRICTION` flag raised on an effort whose product is not the expedition skill files reaches the effort closing report".
   - The list under `## Closing an effort` says such a flag is "found by searching the node files … Give each with its id and the first sentence of its entry. The report carries no other flag."
   - The checker's spawn now gives "for each, the first sentence of its entry, with its id."
7. All four worker contracts meet each part. I found this by grep for "unread" and "leaving out", and by word-diff.
   - The line "Leave `flags.md` unread" is removed.
   - The recording duty names only `decisions.md`.
   - `## When you raise a flag` describes one entry on the node. It opens with a one-sentence report for a reader who has not read the node, and the full account follows. The manager adds only the id and the state.
   - The `FLAGS` placeholder reads "the sentence that opens the entry, then the rest of its prose".
8. expedition-cleanup meets each part:
   - The description and the section now headed `## One operation` describe only region cleanup.
   - `## Flag cleanup` is removed.
   - Step 3 reads "No outstanding flag stops the removal". It has each such FRICTION flag listed with its id and first sentence in the set put to the human in step 4.
   - `## Reporting` lists the ids of the outstanding flags removed with the nodes.
   - Step 5 names only `decisions.md`.
9. triage now reads "Where an older flag entry has no id, this changes step 1 of `### Settle a flag`: give the entry the next unused id on its node, mark it settled, and write a note of your own on its node saying so."
10. The list of reserved names in adoption.md no longer includes `flags.md`.
11. I read the whole word-diff of all ten files.
   - The changes outside clauses 2 to 10 follow from a flag now having one entry: SKILL.md's "its decisions index and its node files", the contracts' "The manager writes your answer and your flags onto your node", the implementation contract's "the sentence that opens the flag's entry", and the reworded scribe-conflict and FRICTION passages.
   - The one rewrap is in SKILL.md, in the paragraph starting "How code lands", and its words are unchanged.
   - I found no other change in meaning.
12. `.claude/rules/expedition-triggers.md` is unmodified (`git status`). None of the SKILL.md edits touches a trigger-duty or the priority.

The bar:
- The root `CLAUDE.md` `## Commands` says the repository has no build, no tests, no formatter and no CI. I confirmed this: the repository root holds only `.claude`, `CLAUDE.md`, `CONTEXT*.md`, `.gitignore` and `.scratch`, and there is no `.github`. So I ran no build command.
- `git diff --check` is clean (rc=0).
- Standards: I read only the standards in `.scratch/rename-split-upgrade/map-implementation-rules.md`.
  - These bore on the work: the `_Avoid_` lines of the glossary, `graph-conventions.md`, the rules for writing under `## Rules for the files under .claude/skills/` in the root `CLAUDE.md`, `/writing-for-agents` (held by hand, and the skill was not invoked), and the trigger-file rule.
  - `/coding-principles` and `/naming` had little to bear on, because the work is prose.
  - I searched the added lines for the distinctive refused words and found none. The phrase "one-sentence report" is the condition's own wording.
- The work changes `graph-conventions.md`, which is one of the standards. The elements that moved are the flag rules, which are exactly what the condition demands. Every other element is unmoved, and I held the work against those.

Flags: I checked each claim against the work after reaching the outcome.
- 19.1 is true. `## Two operations` is now `## One operation`, and `git grep` at the base finds no citation of it. Clause 8 names the section by its old heading, so I took the section by its content.
- 19.2 is true. No "unread" or "leaving out" remains in the four contracts.
- 19.3 is true.
- 19.4 is true.
No flag is false.

### Gate outcome — approve

The human's words, `verbatim`:

> approve
