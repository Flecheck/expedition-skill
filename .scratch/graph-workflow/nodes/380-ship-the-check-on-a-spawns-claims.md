# Ship the check on a spawn's claims into the five worker contracts

Type: implementation
Status: claimed
Blocked by: none

## Question

Write node 78's answer into the worker contracts. A worker checks each claim of fact in the manager's notes, and in its own node's `## Question` outside the human's quoted words, before relying on it. The rule goes into the existing sentence each contract uses to tell the worker to read its sources rather than summaries of them.

*Reported by [node 78](78-what-a-spawn-may-assert.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. It shares the `## What you read` section of the same five files with open node 32 (the `flags.md` sentence) and edits the same files as open node 41 (FRICTION). The concerns differ, so this is code-slot scheduling, not a defect to join."*

## Acceptance condition

*Authored by node 78's worker and filed by the manager. The manager turned the worker's indented block into a quote and changed none of its words.*

> The work is these five files:
>   `.claude/skills/expedition-grilling/SKILL.md`
>   `.claude/skills/expedition-research/SKILL.md`
>   `.claude/skills/expedition-prototype/SKILL.md`
>   `.claude/skills/expedition-precondition/SKILL.md`
>   `.claude/skills/expedition-implementation/SKILL.md`
> Scope came from a search over the working tree: `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md`, which on 2026-10-02 returned exactly one line in each of the five files above and in no other file. If the search reaches an instance outside this list when the work is done, report it and do not edit it.
>
> Done means every one of the following is true of the finished tree.
> 1. In each of the five files, the sentence "Read each of the following. Do not trust any summary of them." is gone. In its place, at the same spot, the text states all three of the following:
>    (a) the worker reads each listed source itself rather than a summary of it;
>    (b) ~~the worker checks each claim of fact in the manager's notes in its spawn before relying on it;~~ *(superseded 2026-10-04 by the human's amendment under `## Amendment, 2026-10-04`)*
>    (c) the worker checks each claim of fact in its own node's `## Question` before relying on it, except text marked there as the human's own words.
> 2. The replacement text says (a) to (c) as what to do, with no prohibition. It adds no heading and adds at most 40 words to each file compared with the removed sentence. An example of wording that meets clauses 1 and 2: "Read each of the following rather than any summary of them. Before you rely on a claim of fact in the manager's notes, or in your node's `## Question` outside the human's quoted words, check it."
> 3. The replacement text is the same in all five files.
> 4. Nothing in the replacement tells the worker to check, doubt or re-derive a direction from the human, a permission the human granted, or an acceptance condition.
> 5. No other sentence of the five files changes.
> 6. No other file changes. That includes `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-cascade/SKILL.md` and every file under `.scratch/graph-workflow/`.
> 7. The tree meets the bar.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Ship the check on a spawn's claims into the five worker contracts

ANSWER:        In each of the five worker contracts (`.claude/skills/expedition-grilling/SKILL.md`, `-research`, `-prototype`, `-precondition`, `-implementation`), the opening line of `## What you read`, "Read each of the following. Do not trust any summary of them.", is replaced in place by one paragraph that is identical in all five files:

               "Read each of the following yourself rather than any summary of them. Before you rely on a claim of fact in the manager's notes in your spawn, or in your node's `## Question` outside any text marked as the human's own words, check it."

               It is wrapped over three lines at the files' usual width. Each file grows by two lines and by 32 words, against a limit of 40. No other line changes. Choices inside the wording that a later reader would otherwise have to work out again:
               - "yourself" makes clause (a) explicit: the worker reads the source itself.
               - "the manager's notes in your spawn" names the spawn part that the manager contract's spawn list calls "Your own notes". A direction from the human and a permission the human granted travel in a spawn as "Two things that travel in a spawn and are not yours". So does the acceptance condition, which is its own part of an implementation spawn. None of these is the manager's notes, so the sentence does not reach them (clause 4).
               - The carve-out uses "text marked as the human's own words". That is the condition's clause (c) wording and the glossary's sense of `verbatim`. The condition's example said "the human's quoted words".
               - The text is two sentences, one idea each, both stating what to do. It contains no prohibition.
               The condition's scope search, `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md`, now returns nothing. Before the edit it returned exactly one line in each of the five files (grilling 38, precondition 39, implementation 47, prototype 38, research 28) and nothing else. That confirms the manager's first note. Under `.claude/` it reaches no instance outside the list. The other hits for the phrase are all record text under `.scratch/graph-workflow/nodes/`, which is not in scope and was not edited.

INDEX LINE:    The five worker contracts' `## What you read` now opens by telling the worker to read sources rather than summaries, and to check claims of fact in manager's notes and its `## Question` first.

FLAGS:         ASSUMPTION: The condition said "claim of fact" and gave the example "outside the human's quoted words". I kept "claim of fact". It is the condition's own phrase, and "of fact" keeps it apart from the glossary term **Claim** (taking a node off the frontier). For the carve-out I wrote "outside any text marked as the human's own words", because that is clause (c)'s wording and matches how the record marks the human's words (`verbatim`). The glossary refuses "summary" only as another name for the effort closing report. The kept phrase "any summary of them" uses it in its ordinary sense, which node 22 had already judged acceptable.
               Index sentence: Node 380 kept "claim of fact" and phrased the carve-out as "text marked as the human's own words", following its condition's clause (c) rather than its example wording.

NEW NODES:     none

INVALIDATIONS: none. This carries out node 78's answer as that answer states it. Node 78 is extended into the shipped files, and nothing it says is contradicted.

CONDITIONS:    I searched the `## Question` and `## Acceptance condition` sections of every open or claimed node for:
               - "summary of"
               - "manager's notes"
               - "What you read"
               - "claim of fact"
               - the phrases "Read each of the following", "Read each of these" and "Do not trust any summary"
               - the five contract paths
               Results:
               - The sentence phrases matched only resolved or superseded nodes (12, 22, 46, 78, 155, 290-294, 329, 333) and this node.
               - The path matches were nodes 32, 41 and 382. Nodes 41 and 382 edit other paragraphs of the same files: the `FLAGS` markers, and the handover-search paragraph. Their clauses still hold as written, and node 382's byte-identity clause is about a paragraph this work does not touch.
               - Node 32's `## Question` cites the `flags.md` line by line number (grilling 41, implementation 54, research 37, prototype 43, precondition 45). It also quotes an older wording. Both were already stale before this work: on master the lines are 54/66/47/55/57. This work moves each down by two more, to 56/68/49/57/59. No clause replacement is owed, because the numbers are in the question and not in the condition.
               - The "summary of" and "manager's notes" matches in nodes 32, 214 and 379 are prose that this work does not affect.
               I replaced no clause and changed no question.

MISSING FROM MAP: none

GATE PAYLOAD:  The checker has not run yet, so there are no findings.
               Paths touched (all uncommitted, in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/380-spawn-claims, on branch worktree-380-spawn-claims):
                 .claude/skills/expedition-grilling/SKILL.md
                 .claude/skills/expedition-research/SKILL.md
                 .claude/skills/expedition-prototype/SKILL.md
                 .claude/skills/expedition-precondition/SKILL.md
                 .claude/skills/expedition-implementation/SKILL.md
               `git diff` shows the same one removed line and the same three added lines in each file, five times. No other file changed.
               The bar: the repo states no build, test or format commands. It has no manifest, no task runner and no CI, and `.gitignore` only ignores worktree paths. That matches what map-implementation-rules.md records, so the command half of the bar is empty and complete. On the other half, I held the new text against the glossary's `_Avoid_` lines and the six writing rules. It states rules as what to do, has one idea per sentence, one referent for each of "them" and "it", and no bold, figure of speech or prohibition.
               Proposed commit message:
                 Tell workers to check the claims of fact in their spawn's notes and node question

                 The five worker contracts' `## What you read` now opens by telling the
                 worker to read each listed source rather than a summary of it, and to
                 check each claim of fact in the manager's notes and in its node's
                 `## Question`, outside the human's own words, before relying on it.

                 Node: graph-workflow/380

RETROSPECTIVE:
1. What I had to hunt for: what the manager contract calls the notes ("Your own notes", under the spawn list), and which parts of a spawn are not the manager's (`### Two things that travel in a spawn and are not yours`). I needed both to be sure clause 4 holds. I also looked up the commit trailer's effort name (`graph-workflow`) in git log.
2. What arrived that this node did not need: the note about node 382, which said itself that it did not bear on the work. Almost all of map.md, apart from the ground rules and the writing rules. Most of map-implementation-rules.md, apart from the standards list and the bar's commands.
3. What would have made this easier: nothing much. The condition was precise and its example wording met it. A one-line pointer to where the manager contract defines a spawn's notes would have saved one search.
4. What was stale, wrong or contradictory: both of the manager's notes checked out. Node 32's `## Question` cites line numbers and a `flags.md` wording that were already stale on master. It breaks writing rule 4, which says to cite by heading or quoted phrase rather than line number. This work moves those lines down by two more.
`````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-04. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/c380.md`.*

> PASS
>
> Read as the work: the five changed paths in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/380-spawn-claims. HEAD is the base 4f8925a46, so nothing is committed on the branch and all of the work is uncommitted.
>
> Acceptance condition, one line per part:
> - Scope and residual clause: I ran the recorded search `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md` over the finished tree. It returns nothing (exit 1). The condition records five lines, one in each listed file. The difference is explained by the work itself, which removed the sentence. To test the recorded claim, I ran the same search on the base commit: `git grep -n 'Do not trust any summary of them' 4f8925a46 -- '.claude/skills/*/SKILL.md'`. It returns exactly one line in each of the five listed files and no other file, so the recorded claim holds. A search over unwrapped text in every `.claude/skills/*/SKILL.md` also finds no instance in the finished tree, so there is no instance outside the list to report.
> - 1 (sentence gone, replaced in the same spot with (a), (b) and (c)): `git diff` shows one line removed and three lines added at the same spot under `## What you read` in each file. The new text is: "Read each of the following yourself rather than any summary of them. Before you rely on a claim of fact in the manager's notes in your spawn, or in your node's `## Question` outside any text marked as the human's own words, check it." It covers (a) "yourself rather than any summary", (b) "manager's notes in your spawn … check it" and (c) "`## Question` outside any text marked as the human's own words … check it".
> - 2 (said as what to do, no prohibition, no heading, at most 40 words added): the new text has no "not", "never" or "do not", and the diff adds no `#` line. `wc -w` gives 12 words for the removed sentence and 44 for the new text, so 32 words were added.
> - 3 (same text in all five files): I ran `git diff -U0 <file> | grep '^[+-][^+-]' | md5sum` on each file. All five give the same hash, 6c8fe4c43c2de7bfec0c85e471cbcf4c.
> - 4 (nothing tells the worker to check a direction from the human, a permission or an acceptance condition): I read the new text. It tells the worker to check only claims of fact, and only those in the manager's notes and in `## Question`, with the human's marked words exempt. The shipped `.claude/skills/expedition/SKILL.md` (spawn list and "### Two things that travel in a spawn and are not yours") carries the human's direction and the acceptance condition as separate items, not as the manager's notes.
> - 5 (no other sentence changes): `git diff --word-diff=porcelain` shows changes only inside the replaced sentence, the same five removed or added spans in each file. `git diff --stat` shows 3 lines added and 1 removed per file, with no rewrap elsewhere.
> - 6 (no other file changes): `git status --short --ignored --untracked-files=all` lists only the five files: no untracked file, no ignored file, nothing under `.scratch/graph-workflow/`, and none of the expedition, checker or cascade SKILL.md files.
> - 7 (the bar): see below.
>
> The bar:
> - Commands: I found no agent-instruction file at the repo root and no manifest, build, test, formatter or CI config. The root holds only `.claude`, `CONTEXT.md` (a stub), `CONTEXT-MAP.md`, `.gitignore` and `.scratch`. The standards file also states that this repo has no build, tests, formatter or CI, so the command half of the bar is empty and the bar is complete without it. `git diff --check` prints nothing (exit 0). The new lines are at most 103 characters, within the files' existing wrap width.
> - Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, under "What the work is held against", and opened no other file in the effort's directory. The list is `/coding-principles` and `/naming`, the glossary's `_Avoid_` lines, the ground rules, the six standing rules for writing, `graph-conventions.md` and `/writing-for-agents`. The file names no reviewing skill, so I ran none.
> - Standards that bore on this work:
>   - The ground rules: the text assumes no repo or toolchain, invokes no skill, and does not address the human.
>   - Writing rules 5 and 6: the rule is said as what to do, with no bold, no figure of speech and no slogan-shaped contrast. Each pronoun has one referent ("them" is the listed sources, "it" is the claim of fact).
>   - The glossary's `_Avoid_` lines: I searched them unwrapped. "summary" is refused only for the "Effort closing report" concept, which does not apply here. No other word of the new text is refused.
>   - `graph-conventions.md`: `## Question` is a node-file heading it defines.
>   - `/writing-for-agents` (located by name in the mattpocock-skills plugin): it prefers a positive instruction over negation, and the change turns a prohibition into a positive instruction.
>   - `/coding-principles` and `/naming` did not bear on this prose change.
> - Under the rules file's record-as-work rule, I read the changed paths as the work. None of them is a status line, `decisions.md` or `flags.md`.
>
> QUESTIONS:
> - Is the clash between "the manager's notes" and the glossary's "Manager note" intended? The phrase comes from the condition's clauses 1(b) and 2. The glossary defines **Manager note** as "The manager's own annotation on a relayed question". The grilling, prototype and precondition contracts also have a `MANAGER NOTES:` field in their resume shape ("the manager's own, never the human's"). The new text limits the duty to check claims to the notes "in your spawn". So a manager note that comes back on resume, the glossary sense, is not covered, and "manager's notes" now means two different things in the same file. The wording is the condition's own, so departing from it was not the worker's call. Should notes that arrive on resume be checked too, and should the spawn notes get a different name?
>   - Form: a passage in a worker contract that says "manager's notes" for a spawn's notes while the glossary's "Manager note" names something else.
>   - Extent: `grep -n "manager's notes\|MANAGER NOTES" .claude/skills/expedition-{grilling,research,prototype,precondition,implementation}/SKILL.md`.
>
> I wrote no temporary files.

*The manager's note:* the checker handed back a question beside its outcome, so the standing yes does not cover this gate. It goes to the human.

### The gate, 2026-10-04

`verbatim`: *"ok"*

The manager had offered "Recommended: a correction round that amends clause 1(b) so the check covers the manager's notes in a spawn or on a resume. For example: "…a claim of fact in the manager's notes, in your spawn or on a resume, or in your node's `## Question`…". That's about 4 more words, still under the 40-word cap." and the alternative "approve as is, covering spawn notes only", closing with "Please answer node 380's gate: "ok for recommended", or "approve as is"." The reply takes the correction round. Flag `380.1` was in the payload and settles here.

## Amendment, 2026-10-04

*The human's amendment at the gate. The human's reply, `verbatim`: "ok". It took the correction the manager offered, so the words are the manager's and the decision is the human's. Its ground is checker run 1's question: the glossary's **Manager note** is the note that arrives on a resume, and the shipped text covered only notes in the spawn.*

**Clause 1(b), as it now binds:**

> (b) the worker checks each claim of fact in the manager's notes, whether they arrive in its spawn or on a resume, before relying on it;

Clause 2's 40-word cap and every other clause stand.

## Handover, correction round 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Ship the check on a spawn's claims into the five worker contracts

ANSWER:        In each of the five worker contracts (`.claude/skills/expedition-grilling/SKILL.md`, `-research`, `-prototype`, `-precondition`, `-implementation`), one paragraph now stands at the head of `## What you read` where "Read each of the following. Do not trust any summary of them." used to be. The paragraph is identical in all five files:

               "Read each of the following yourself rather than any summary of them. Before you rely on a claim of fact in the manager's notes, in your spawn or on a resume, or in your node's `## Question` outside any text marked as the human's own words, check it."

               It is wrapped over three lines at the files' usual width, and no other line changes. It adds 36 words to each file against the removed sentence, within the cap of 40.

               Correction round 1 carried out the amendment of 2026-10-04 to clause 1(b). The notes covered now include those that arrive on a resume as well as those in the spawn. That matches the glossary's **Manager note** ("The manager's own annotation on a relayed question"). It also matches the `MANAGER NOTES:` field of the resume block in the grilling, prototype and precondition contracts. I used the shorter form "in your spawn or on a resume". The longer "whether they arrive in your spawn or on a resume" would have taken the file to 39 words over the removed sentence, one under the cap.

               Clause 4 still holds:
               - The resume block's `HUMAN ANSWER:` field and the "never the human's" note on its `MANAGER NOTES:` field keep the human's words outside "the manager's notes".
               - A direction from the human, a permission the human granted, and the acceptance condition each travel as a separate part of a spawn.
               - So the sentence reaches none of them.

               In the research and implementation contracts, "on a resume" names no field. Neither has a `MANAGER NOTES:` resume block. It still covers the notes a manager sends when it resumes a worker in those kinds, as this round's own message did. Clause 3 requires identical text, so the phrase stays in all five.

               The condition's scope search, `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md`, returns nothing.

INDEX LINE:    The five worker contracts' `## What you read` tells the worker to read sources, not summaries, and to check claims of fact in manager's notes (spawn or resume) and its `## Question`.

FLAGS:         ASSUMPTION: The condition said "claim of fact" and gave the example "outside the human's quoted words". I kept "claim of fact". It is the condition's own phrase, and "of fact" keeps it apart from the glossary term **Claim** (taking a node off the frontier). For the carve-out I wrote "outside any text marked as the human's own words", because that is clause (c)'s wording and matches how the record marks the human's words (`verbatim`). The glossary refuses "summary" only as another name for the effort closing report. The kept phrase "any summary of them" uses it in its ordinary sense, which node 22 had already judged acceptable. In correction round 1 I wrote the amended clause 1(b) as "in your spawn or on a resume" rather than "whether they arrive in your spawn or on a resume", so that the file stays clear of the 40-word cap.
               Index sentence: Node 380 kept "claim of fact", phrased the carve-out as "text marked as the human's own words", and wrote the amended 1(b) in its shorter form to stay under the word cap.

NEW NODES:     none

INVALIDATIONS: none. This carries out node 78's answer and extends it to notes that arrive on a resume, as the human's amendment to this node's condition asks. Nothing node 78 says is contradicted. Node 78's answer speaks of "the manager's notes" in a spawn only, so the resume case is an extension of it.

CONDITIONS:    Same search as round 1, over the `## Question` and `## Acceptance condition` sections of every open or claimed node. I searched for:
               - "summary of"
               - "manager's notes"
               - "What you read"
               - "claim of fact"
               - the phrases "Read each of the following", "Read each of these" and "Do not trust any summary"
               - the five contract paths
               In this round I also searched for "MANAGER NOTES" and "on a resume", which the amendment brings in.
               Results:
               - Nodes 41 and 382 edit other paragraphs of the same files, and their clauses still hold as written.
               - Node 32's `## Question` cites line numbers for the `flags.md` line. They were already stale on master, and this work moves each down by two lines.
               - The new terms matched no open node outside this one.
               I replaced no clause and changed no question.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker run 1: PASS, with one question. The glossary's **Manager note** arrives on a resume, and the round-1 text covered only notes in the spawn. Settled by the human's amendment to clause 1(b), which this round carries out in all five files with identical text.
               Paths touched (all uncommitted, in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/380-spawn-claims, on branch worktree-380-spawn-claims):
                 .claude/skills/expedition-grilling/SKILL.md
                 .claude/skills/expedition-research/SKILL.md
                 .claude/skills/expedition-prototype/SKILL.md
                 .claude/skills/expedition-precondition/SKILL.md
                 .claude/skills/expedition-implementation/SKILL.md
               Against master, `git diff` shows the same one removed line and the same three added lines in each file, five times. No other file changed.
               Did the change touch anything the acceptance condition names? Yes. It changes only the replacement text that clauses 1 to 4 govern, to meet the amended clause 1(b).
               The bar: the repo states no build, test or format commands, the same as in round 1. That command half is empty and complete. I held the changed text against the glossary's `_Avoid_` lines and the six writing rules. It states rules as what to do, has one idea per sentence and one referent for each pronoun, and adds no bold and no prohibition.
               Proposed commit message:
                 Tell workers to check the claims of fact in manager's notes and their node question

                 The five worker contracts' `## What you read` now opens by telling the
                 worker to read each listed source rather than a summary of it, and to
                 check each claim of fact in the manager's notes, in its spawn or on a
                 resume, and in its node's `## Question` outside the human's own words,
                 before relying on it.

                 Node: graph-workflow/380

RETROSPECTIVE (correction round 1):
1. What I had to hunt for: which contracts actually have a `MANAGER NOTES:` field on a resume, so I could check the round message's claim about it.
2. What arrived that this node did not need: nothing.
3. What would have made this easier: the round message saying which contracts carry the `MANAGER NOTES:` resume field.
4. What was stale, wrong or contradictory: the round message's claim is only partly right. It called the glossary's Manager note "the `MANAGER NOTES:` field a worker receives on a resume". Only the grilling, prototype and precondition contracts have that field. The research and implementation contracts have no `MANAGER NOTES:` resume block, though a manager does send notes when resuming them. The other claims checked out: the glossary entry, the amendment recorded on node 380, and clause 2's cap still standing.
`````

*The manager's note:* the worker is right that the manager's round message overstated the glossary sense: only the grilling, prototype and precondition contracts carry a `MANAGER NOTES:` resume field.

## Review, continued

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-10-04. The run 1 checker, resumed for this node's re-check, given the amendment to clause 1(b) as text.*

> PASS
>
> Re-check after correction round 1. I followed "## When you are handed the same work again" in the checker contract as it now stands on master at 3a0b93e0a, which includes node 379's changes: a seventh given (flags) and "### The flags, after your outcome". This spawn gave no flags, so the seventh given is absent and I have no flag to check. The worktree HEAD is still the base 4f8925a46, so nothing is committed on the branch. The work is the five uncommitted paths. I re-checked every clause against the amended condition and re-ran the bar in full.
>
> What changed in the work: I compared the words with a word-level diff over the whole change (`git diff --word-diff=porcelain`). The one change from run 1 is inside the replacement. "in the manager's notes in your spawn" became "in the manager's notes, in your spawn or on a resume". The replacement now reads, in all five files: "Read each of the following yourself rather than any summary of them. Before you rely on a claim of fact in the manager's notes, in your spawn or on a resume, or in your node's `## Question` outside any text marked as the human's own words, check it."
>
> Acceptance condition, as amended:
> - Scope and residual clause: the recorded command `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md` returns nothing over the finished tree (exit 1). The condition records five lines, one in each listed file. The work explains the difference, since it removed the sentence. In run 1 I ran the same search on base 4f8925a46 and it returned exactly those five lines, so the recorded claim holds. A search over unwrapped text in every `.claude/skills/*/SKILL.md` also finds no instance outside the list.
> - 1(a): the new text says "yourself rather than any summary of them". Established by `git diff`.
> - 1(b), amended: the new text says "a claim of fact in the manager's notes, in your spawn or on a resume … check it". That covers notes arriving either way. Established by `git diff`.
> - 1(c): the new text says "in your node's `## Question` outside any text marked as the human's own words, check it". Established by `git diff`.
> - 1, same spot: each file loses one line and gains three at the same place under `## What you read`. Established by `git diff -U1`.
> - 2: the new text has no "not", "never" or "do not", and the diff adds no `#` line. `wc -w` gives 12 words for the removed sentence and 48 for the new text, so it adds 36 words, under the cap of 40.
> - 3: `git diff -U0 <file> | grep '^[+-][^+-]' | md5sum` gives the same hash, 643ba42f582f314736e0c5abcc73ad09, for all five files.
> - 4: the new text tells the worker to check only claims of fact, and only those in the manager's notes and in `## Question`, with the human's marked words exempt. Read as intended, it says nothing about checking a direction from the human, a permission the human granted, or an acceptance condition. See the finding below for a second reading.
> - 5: the word diff shows the same five removed or added spans in each file, all inside the replaced sentence. Nothing else moved.
> - 6: `git status --short --ignored --untracked-files=all` lists only the five files. Nothing is untracked or ignored, and nothing changed under `.scratch/graph-workflow/` in the worktree.
> - 7: see below.
>
> The bar:
> - Commands: the repo has no build, tests, formatter or CI, and its root holds no agent-instruction file or manifest. The standards file says the same. So the bar has no commands to run here, and the standards alone make it up. `git diff --check` prints nothing (exit 0). The new lines are 42 to 103 characters, within the files' existing wrap width.
> - Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md` ("What the work is held against"). `git diff 4f8925a46 HEAD` shows no change to that file, `glossary.md` or `graph-conventions.md` since run 1, so I am holding the work to the same standards as in run 1.
> - Standards that bore on this work: the ground rules (nothing tied to this repo, no skill invoked, nothing addressed to the human), writing rules 5 and 6 (said as what to do, no bold, no figure of speech, one referent per pronoun), the glossary's `_Avoid_` lines (I searched them unwrapped; "summary" is refused only for "Effort closing report"), `graph-conventions.md` (`## Question` is a node-file heading it defines) and `/writing-for-agents` (it prefers a positive instruction over negation). `/coding-principles` and `/naming` did not bear on this prose change. No reviewing skill is named, so I ran none.
> - I read the changed paths as the work, under the rules file's rule for work that is part of the record. None of them is a status line, `decisions.md` or `flags.md`.
>
> Finding, handed back alongside the PASS (it does not change the outcome):
> - Instances: the same line in all five files reads "in the manager's notes, in your spawn or on a resume, or in your node's `## Question`". Without a serial comma, "the manager's notes, in your spawn or on a resume" can be read as a flat list of three places: the notes, anything in the spawn, and anything on a resume. Read that way, the worker would check every claim of fact in its spawn. An implementation worker's spawn carries its acceptance condition, and a spawn can carry a direction from the human, which is what clause 4 keeps out. The double "or" points to the intended grouping, where "in your spawn or on a resume" says where the notes arrive, so I judged clause 4 met. The other reading is still available. The condition's own wording removes it: "in the manager's notes, whether they arrive in your spawn or on a resume". That adds 2 words, for 38 added in total, still under the cap.
> - Form: in the replacement, a phrase saying where the manager's notes arrive is punctuated so that it can also be read as further places whose claims must be checked.
> - Extent: `grep -n "in the manager's notes, in your spawn or on a resume" .claude/skills/expedition-{grilling,research,prototype,precondition,implementation}/SKILL.md` returns one line per file, five in total.
>
> I did not check the flags, because this spawn carries none. I wrote no temporary files.

*The manager's note:* the checker handed back a finding beside its outcome, so the standing yes does not cover this gate. It goes to the human.

### The gate, second time, 2026-10-04

`verbatim`: *"ok for 380"*

The manager had offered "Recommended: a short correction round to use "whether they arrive in your spawn or on a resume". It's already within the condition as amended, so no amendment is needed, and the same checker re-checks." and the alternative "approve as is", closing with "Please answer: "ok for recommended", or "approve as is"." The reply takes the correction round. Flag `380.1` was in the payload and settles here.

## Handover, correction round 2

*Pasted as the worker handed it back.*

`````
HANDOVER:      Ship the check on a spawn's claims into the five worker contracts

ANSWER:        In each of the five worker contracts (`.claude/skills/expedition-grilling/SKILL.md`, `-research`, `-prototype`, `-precondition`, `-implementation`), one paragraph now stands at the head of `## What you read` where "Read each of the following. Do not trust any summary of them." used to be. The paragraph is identical in all five files:

               "Read each of the following yourself rather than any summary of them. Before you rely on a claim of fact in the manager's notes, whether they arrive in your spawn or on a resume, or in your node's `## Question` outside any text marked as the human's own words, check it."

               It is wrapped over three lines at the files' usual width, and no other line changes.

               Word count against the removed sentence:
               - 38 added words if `## Question` counts as one word, which is the checker's count.
               - 39 if the backticked `##` counts as a separate word.
               - Either way it is within the cap of 40.

               Correction round 2 replaced "in your spawn or on a resume" with the amended clause 1(b)'s own wording, "whether they arrive in your spawn or on a resume". The clause that starts "whether they arrive" attaches to "the manager's notes", and "they" can refer only to those notes. So the spawn and the resume are where the notes arrive, not two more places whose every claim the worker checks. That closes the reading checker run 2 found, under which a worker would have checked every claim in its spawn or on a resume.

               Clause 4 still holds:
               - On a resume, the human's words arrive in their own field.
               - A direction from the human, a permission the human granted, and the acceptance condition each travel as a separate part of a spawn and are not the manager's notes.

               Round 1 settled what "on a resume" covers: the `MANAGER NOTES:` resume field in the grilling, prototype and precondition contracts, and in the research and implementation contracts the notes a manager sends when resuming a worker.

               The condition's scope search, `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md`, returns nothing.

INDEX LINE:    The five worker contracts' `## What you read` tells the worker to read sources, not summaries, and to check claims of fact in manager's notes (spawn or resume) and its `## Question`.

FLAGS:         ASSUMPTION: The condition said "claim of fact" and gave the example "outside the human's quoted words". I kept "claim of fact". It is the condition's own phrase, and "of fact" keeps it apart from the glossary term **Claim** (taking a node off the frontier). For the carve-out I wrote "outside any text marked as the human's own words", because that is clause (c)'s wording and matches how the record marks the human's words (`verbatim`). The glossary refuses "summary" only as another name for the effort closing report. The kept phrase "any summary of them" uses it in its ordinary sense, which node 22 had already judged acceptable. The round-1 choice of the shorter "in your spawn or on a resume" was reversed in correction round 2, which used the amended clause 1(b)'s own wording to remove a misreading the checker found.
               Index sentence: Node 380 kept "claim of fact", phrased the carve-out as "text marked as the human's own words", and in the end used clause 1(b)'s own "whether they arrive" wording.

NEW NODES:     none

INVALIDATIONS: none. This carries out node 78's answer and extends it to notes that arrive on a resume, as the human's amendment to this node's condition asks. Nothing node 78 says is contradicted.

CONDITIONS:    Same search as rounds 1 and 2, over the `## Question` and `## Acceptance condition` sections of every open or claimed node. I searched for:
               - "summary of"
               - "manager's notes"
               - "What you read"
               - "claim of fact"
               - "MANAGER NOTES"
               - "on a resume"
               - the phrases "Read each of the following", "Read each of these" and "Do not trust any summary"
               - the five contract paths
               This round adds no new term, so the results are unchanged:
               - Nodes 41 and 382 edit other paragraphs of the same files, and their clauses still hold.
               - Node 32's `## Question` cites line numbers for the `flags.md` line. They were already stale on master, and this work moves each down by two lines.
               I replaced no clause and changed no question.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker run 1: PASS, with one question about notes that arrive on a resume. Settled by the human's amendment to clause 1(b) and carried out in round 1.
               Checker run 2: PASS, with one finding. "in the manager's notes, in your spawn or on a resume" could be read as a flat list of three places, which would reach an acceptance condition or a direction from the human and break clause 4. Fixed in round 2: the phrase is now "in the manager's notes, whether they arrive in your spawn or on a resume". It is identical in all five files and adds 38 or 39 words depending on how `## Question` is counted, under the cap of 40.
               Paths touched (all uncommitted, in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/380-spawn-claims, on branch worktree-380-spawn-claims):
                 .claude/skills/expedition-grilling/SKILL.md
                 .claude/skills/expedition-research/SKILL.md
                 .claude/skills/expedition-prototype/SKILL.md
                 .claude/skills/expedition-precondition/SKILL.md
                 .claude/skills/expedition-implementation/SKILL.md
               Against master, `git diff` shows the same one removed line and the same three added lines in each file, five times. No other file changed.
               Did the change touch anything the acceptance condition names? Yes. It changes only the replacement text that clauses 1 to 4 govern.
               The bar: the repo states no build, test or format commands, the same as in rounds 1 and 2. That command half is empty and complete. On the other half: one idea per sentence, "they" has the single referent "the manager's notes", and the text adds no bold and no prohibition.
               Proposed commit message:
                 Tell workers to check the claims of fact in manager's notes and their node question

                 The five worker contracts' `## What you read` now opens by telling the
                 worker to read each listed source rather than a summary of it, and to
                 check each claim of fact in the manager's notes, whether they arrive in
                 its spawn or on a resume, and in its node's `## Question` outside the
                 human's own words, before relying on it.

                 Node: graph-workflow/380

RETROSPECTIVE (correction round 2):
1. What I had to hunt for: nothing. I only checked the word count myself.
2. What arrived that this node did not need: nothing.
3. What would have made this easier: in round 1, using the amended clause's own wording instead of shortening it. I shortened it to keep a margin under the cap that turned out not to be needed, and the shorter form is what caused the misreading.
4. What was stale, wrong or contradictory: the checker's count of 38 added words depends on how it is counted. Counting whitespace-separated tokens gives 39, because the backticked `##` becomes a separate token. Both counts are under the cap, so nothing changes.
`````

## Flags

`380.1` `ASSUMPTION` **· settled** — Node 380 kept "claim of fact", phrased the carve-out as "text marked as the human's own words", and in the end used clause 1(b)'s own "whether they arrive" wording. *(The worker's full text is under each handover's `FLAGS`; the flag was put to the human at both gates.)*

### Checker run 3 — `PASS`

*The checker's own text, pasted, 2026-10-04. The same checker, resumed for this node's re-check, given the node's flag under node 379's rule.*

> PASS
>
> Re-check after correction round 2. I followed "## When you are handed the same work again". My contract is the checker contract on master. `git diff 3a0b93e0a HEAD` shows no change to it, to `.scratch/graph-workflow/map-implementation-rules.md`, to `glossary.md` or to `graph-conventions.md` since run 2. So the contract and the standards I check against are the ones I used in run 2. The worktree HEAD is still the base 4f8925a46. The work is the five uncommitted paths. I re-checked every clause against the condition as amended before run 2 and re-ran the bar in full.
>
> What changed in the work: I compared the words with `git diff --word-diff=porcelain` over the whole change. The one change since run 2 is inside the replacement. "in the manager's notes, in your spawn or on a resume," became "in the manager's notes, whether they arrive in your spawn or on a resume,". The words are otherwise the same as in run 2, and the line breaks moved with the insertion. The replacement now reads, the same in all five files: "Read each of the following yourself rather than any summary of them. Before you rely on a claim of fact in the manager's notes, whether they arrive in your spawn or on a resume, or in your node's `## Question` outside any text marked as the human's own words, check it."
>
> Acceptance condition, as amended:
> - Scope and residual clause: the recorded command `grep -n 'Do not trust any summary of them' .claude/skills/*/SKILL.md` returns nothing over the finished tree (exit 1). The condition records five lines, one in each listed file. The difference comes from the work removing the sentence. In run 1, the same search on base 4f8925a46 returned exactly those five lines, so the recorded claim holds. A search over unwrapped text in every `.claude/skills/*/SKILL.md` finds no instance outside the list.
> - 1(a): the new text says "yourself rather than any summary of them". Established by `git diff`.
> - 1(b), amended: the new text says "a claim of fact in the manager's notes, whether they arrive in your spawn or on a resume … check it". Established by `git diff`.
> - 1(c): the new text says "in your node's `## Question` outside any text marked as the human's own words, check it". Established by `git diff`.
> - 1, same spot: each file loses one line and gains three at the same place under `## What you read`. Established by `git diff -U1`.
> - 2: the new text has no "not", "never" or "do not", and the diff adds no `#` line. `wc -w` gives 12 words for the removed sentence and 51 for the new text, so it adds 39 words. The cap is 40. `wc -w` counts `## Question` as two words, so a count that takes it as one gives 38.
> - 3: `git diff -U0 <file> | grep '^[+-][^+-]' | md5sum` gives the same hash, 87b669ab9a08fdf5fcae55e44c3bf1d6, for all five files.
> - 4: the new text tells the worker to check only claims of fact, and only those in the manager's notes and in `## Question`, with the human's marked words exempt. "whether they arrive in your spawn or on a resume" can only be read as saying where the notes arrive. So the reading I handed back in run 2, in which anything in the spawn had to be checked, is gone. Nothing in the new text tells the worker to check a direction from the human, a permission the human granted, or an acceptance condition.
> - 5: the word diff shows the same five removed or added spans in each file, all inside the replaced sentence.
> - 6: `git status --short --ignored --untracked-files=all` lists only the five files. Nothing is untracked or ignored, and nothing changed under `.scratch/graph-workflow/` in the worktree.
> - 7: see below.
>
> The bar:
> - Commands: the repo has no build, tests, formatter or CI, and its root holds no agent-instruction file or manifest. The standards file says the same. So the command half of the bar is empty, and the bar is complete without it. `git diff --check` prints nothing (exit 0).
> - Line width: the new lines are 59 to 105 characters. At base, every one of the five files already holds lines of 105 characters or more (7, 4, 4, 6 and 9 such lines), so the new lines are within the files' existing width.
> - Standards: I read only the standards in `map-implementation-rules.md` ("What the work is held against").
> - Standards that bore on this work: the ground rules (nothing tied to this repo, no skill invoked, nothing addressed to the human), writing rules 5 and 6 (said as what to do, no bold, no figure of speech, "they" has the one referent "the manager's notes", "it" has the one referent "a claim of fact"), the glossary's `_Avoid_` lines ("summary" is refused only for "Effort closing report"), `graph-conventions.md` (`## Question` is a node-file heading it defines) and `/writing-for-agents` (it prefers a positive instruction over negation). `/coding-principles` and `/naming` did not bear on this prose change. No reviewing skill is named, so I ran none.
> - I read the changed paths as the work, under the rules file's rule for work that is part of the record. None of them is a status line, `decisions.md` or `flags.md`.
>
> Flags, checked after the outcome:
> - 380.1 is true of the work. "kept 'claim of fact'": the new text contains "a claim of fact". "phrased the carve-out as 'text marked as the human's own words'": the new text contains "outside any text marked as the human's own words". "used clause 1(b)'s own 'whether they arrive' wording": the new text contains "whether they arrive in your spawn or on a resume". Established by `git diff`.
> - No flag is false, so I have nothing to hand back under QUESTIONS.
>
> I wrote no temporary files.

### The gate, third time, 2026-10-04 — standing yes

`standing yes`. The scope, word for word: *"Approve all gates automatically"*. The checker's `PASS` (run 3) is taken as the human's approval. The run covered every part, handed back no question, and found flag 380.1 true. That flag was settled at the human's earlier gates.
