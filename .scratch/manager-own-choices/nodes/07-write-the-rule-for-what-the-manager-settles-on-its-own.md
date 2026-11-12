# Write the rule for what the manager settles on its own

Type: implementation
Status: resolved
Deliverable: own-choices

## Question

*Proposed by the worker of [node 01](01-what-the-manager-settles-on-its-own.md), as it wrote it:* This lets a manager stop pausing an effort to ask the human about a choice it made itself, where fixing that choice needs no new decision. It also lets the manager hand back to a worker or a checker information it already holds, instead of putting the item to the human. It fixes GitHub issue 1's proposals 1 to 4 in the shipped expedition skill files.

## Acceptance condition

*Written by the worker of node 01, filed by the manager:*

1. `.claude/skills/expedition/SKILL.md` has a new section at the same heading level as `## What is never yours`, placed directly after it. It states all of the following, in words the worker chooses:
   a. A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node.
   b. A choice taken under a standing yes is the manager's, recorded as taken under that standing yes.
   c. ~~A choice is the manager's when it is a condition or an amendment marked as the manager's own, a node split, an edge, the order work is done in, or a scope list the manager got by re-running a recorded search.~~ *(superseded by amendment 1, after clause 12)*
   d. A choice a worker made, including a condition it wrote, is not the manager's.
   e. A fix to a choice "needs a new decision" when it reverses or narrows something the human decided, or needs a judgement nobody has made. The section uses the phrase "needs a new decision" for this.
   f. The manager settles a fix only when the choice is its own and the fix needs no new decision. Every other fix goes to the human.
   g. A worker's raise, or a checker's question or raise, may say the agent is blocked by missing information that is already in the manager's context. The manager then hands that information back and resumes the agent, instead of putting the item to the human.
   h. The manager reads nothing and runs nothing to find that information.
   i. To a checker, the manager hands back only where something is or how to reach it, and never a recorded decision or a reading of the condition. To a worker, it may hand back any fact or recorded decision.
   j. An item the agent hands back again takes the usual route.
   k. The handling in f and g comes before the item enters the queue under `## What is in front of the human, and when`, and before any standing yes is taken.
   l. A choice the manager settles under f carries no flag, and is named in no gate payload and no node closing report.
   The section states the rule as a principle. It gives no list of steps for particular cases.
2. In `.claude/skills/expedition/SKILL.md`, `### Changing one after it is written` permits the manager to amend the condition of a node a worker already holds, without asking the human, under all of the following:
   - The clause shown wrong is the manager's own.
   - The fix needs no new decision.
   - Every word of the replacement is already fixed, and the amendment names the source that fixed it.
   - The manager hands the amended text to the worker, and to the checker where a check is live.
   - A condition made out of date by a later decision of the human falls under the same permission.
   - A clause someone else wrote still goes to the human.
   The section's sentences "apply only to a node nobody holds yet" and "Where a worker already holds the node, its condition is handed over as written. A worker that judges the condition wrong raises it, and the human answers." no longer contradict this permission.
   The list of things every amendment comes with says that an amendment the manager makes under this permission comes with the first three of those things, and with neither a flag nor a mention in a node closing report.
3. In `.claude/skills/expedition/SKILL.md`, `## What is never yours` no longer contradicts the new section, in either of two rows:
   - The row "rewriting an acceptance condition" names the permission in clause 2 as an exception.
   - The row "answering anything on the human's behalf" allows what the new section permits.
4. In `.claude/skills/expedition/SKILL.md`, `## The checker`'s paragraph on passing amended text to the worker and the checker also covers an amendment the manager makes under clause 2.
5. In `.claude/skills/expedition-standing-yes/SKILL.md`, `## What a standing yes never covers` no longer says that its items go to the human "whatever the scope says" without exception. It says that the manager's handling under the new section of `.claude/skills/expedition/SKILL.md` comes first.
6. In `.claude/skills/expedition/glossary.md`, two entries no longer contradict the new section:
   - In the **Manager** entry, the sentence "the manager never answers one on the human's behalf".
   - In the **Relay** entry, the clause "answers nothing itself".
   The glossary gains no entry for "needs a new decision". The phrase "product effect" appears in no file under `.claude/`.
7. The opening paragraph of each of four contracts no longer says, without exception, that the manager passes everything to the human and "answers nothing itself". The four are `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-prototype/SKILL.md`. In `.claude/skills/expedition-checker/SKILL.md`, the sentences "The manager carries the raise to the human." and "The manager carries the questions to the human" no longer say that without exception either.
8. In `.claude/skills/expedition-implementation/SKILL.md`, under `### The raise`, the answer "Continue" no longer limits the corrected acceptance condition to one the human has rewritten.
9. Each of the five contracts named in clause 7 says that an agent reporting it cannot read or do something states what it tried: the path, the command and the error.
10. In `.claude/skills/expedition/graph-conventions.md`, step 2 of `### Amend an acceptance condition` (raising the amendment's flag) does not apply to an amendment the manager makes under clause 2.
11. In `.claude/rules/expedition-triggers.md`, the second trigger, beginning "When an agent hands back something for the human", no longer tells the manager to put in front of the human an item that the new section has the manager handle first. The file's `## Priority` list is unchanged.
12. `### Two things the human can say that are not answers` in `.claude/skills/expedition/SKILL.md` is unchanged. The list of flag markers in `.claude/skills/expedition/graph-conventions.md` is unchanged.

Scope: clauses 1 to 4, 9 and 12 name the work itself, and came from no search. The places in clauses 5 to 8 and 10 came from this command, run over the working tree at `d49b11e`:
`grep -rnE "answers nothing itself|never answers one on|where the human has rewritten|goes to the human as usual|carries the raise to the human|carries the questions to the human|and the human answers|a node nobody holds yet|product effect" .claude/`
It returned these lines:
- `.claude/skills/expedition-standing-yes/SKILL.md` line 49;
- `.claude/skills/expedition/glossary.md` lines 83 and 231;
- line 11 of each of the precondition, grilling, implementation and prototype contracts;
- `.claude/skills/expedition-implementation/SKILL.md` line 212;
- `.claude/skills/expedition-checker/SKILL.md` line 442;
- `.claude/skills/expedition/SKILL.md` lines 56, 570 and 572.
The command misses the checker's sentence "The manager carries the questions to the human", which spans a line break, so it was added by reading. Clause 10's place was added by reading too. Clause 11's place is required by the root `CLAUDE.md`'s rule on the trigger file.
Edit an instance the search reaches outside this list only on one of three grounds, and raise a flag naming the place and the reason:
- this work's own change makes the place wrong;
- the place is a further instance of the contradiction this condition describes;
- the work cannot meet this condition or the bar without the change.
Report any other instance, and do not edit it.

### Amendment 1 — by the human, at gate 1, filed by the manager

What fixed the words: the human's answer to the worker's raise in correction round 1, recorded under `## Review`, which takes the raise's `RECOMMENDED`: "amend clause 1c to read "A choice is the manager's when the manager made it."" Clause 1c now reads:

   c. A choice is the manager's when the manager made it.

*Manager's note:* the human's own amendment carries no flag, as node 01 decided for an amendment the human makes.

## Answer

The worker's answer, as it wrote it in its handover, followed by its correction round 1 (both are under `## Handover, attempt 1` and `## Review`): the rule is stated once, in a new section of `.claude/skills/expedition/SKILL.md`, `## What you handle before the human`, directly after `## What is never yours`, as a principle with no steps for particular cases. Before an item enters the queue and before any standing yes, the manager settles a fix to its own choice that needs no new decision, and hands back to a worker or a checker information it already holds. After correction round 1, the paragraph on whose choice it is reads: "A choice is yours when you made it. A choice taken under a standing yes is yours too, recorded as taken under that standing yes. A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node. A choice a worker made, a condition it wrote included, is not yours." Every place that contradicted the section now points at it.

*Manager's note:* this paragraph assembles the worker's own sentences from its handover and its correction. Landed on the deliverable branch `own-choices` as `ed2ec0e` and `132e855`, the gate taken under standing yes 1. The branch is not pushed.

## Flags

`07.1` `ASSUMPTION` — In `### Changing one after it is written`, the no-flag rule also covers an amendment the manager makes before the claim to a clause of its own, where the fix needs no new decision, and not only the permission for a node a worker holds. Clause 2 names only the permission for a held node. But clause 1(l) says that no choice the manager settles under the rule carries a flag. Node 01's answer says the same "for an amendment the manager settles this way". If item 4 still said "every amendment" carries a flag, it would contradict the new section. Ground: this work's own change makes the place wrong, inside a listed file.

`07.2` `ASSUMPTION` — I added a two-sentence pointer to `## What is in front of the human, and when` in `.claude/skills/expedition/SKILL.md`, which no clause of the condition names. That section is the governing statement of the trigger I changed under clause 11, and without the pointer it would contradict the new trigger text. Ground: this work's own change makes the place wrong, inside a listed file.

`07.3` `ASSUMPTION` — I edited two sentences in `.claude/skills/expedition-checker/SKILL.md` that the condition's list does not name: the opening sentence "which carries both a raise and whatever you hand back alongside your outcome", and hard rule 5's "What you hand back alongside it does reach the human, through the manager". Ground: each is a further instance of the contradiction clause 7 describes, because each says without exception that the manager carries the checker's items to the human.

`07.4` `ASSUMPTION` — I put the "state what you tried" line in each of the five contracts as a new last hard rule, because I judged that the place every reader of the contract reaches. The condition leaves the place to the worker.

`07.5` `ASSUMPTION` — I named the new section `## What you handle before the human`. The name pairs with `## What is never yours`, and covers both settling a fix and handing back information. Node 01 named no heading.

## Handover, attempt 1

The worker's handover, as it wrote it, with its `FLAGS` filed under `## Flags` above:

```
ANSWER:        The rule is stated once, in a new section of `.claude/skills/expedition/SKILL.md`, `## What you handle before the human`. It sits directly after `## What is never yours` and is written as a principle, with no steps for particular cases. It says the following:
               - The section's handling comes before an item enters the queue under `## What is in front of the human, and when`, and before any standing yes is taken.
               - Whose choice it is: the human's only when it is in their own words or in an answer they gave on a node; the manager's when it was taken under a standing yes (recorded as such), or when it is a condition or amendment marked as the manager's own, a node split, an edge, the order work is done in, or a scope list got by re-running a recorded search; never the manager's when a worker made it, a condition the worker wrote included.
               - "Needs a new decision": the fix reverses or narrows something the human decided, or it needs a judgement nobody has made.
               - The manager settles a fix only when the choice is its own and the fix needs no new decision. Every other fix goes to the human. A choice settled this way carries no flag and is named in no gate payload and no node closing report.
               - Held information: when a worker's raise, or a checker's question or raise, is blocked by information already in the manager's context, the manager hands that information back and resumes the agent. It reads nothing and runs nothing to find it. A checker gets only where something is or how to reach it. A worker may get any fact or recorded decision. An item handed back again takes the usual route.
               Pointers to the section, each stating its own change in its own words:
               - `## What is never yours`: both rows named in the condition now allow the new section's handling.
               - `### Changing one after it is written`: a new paragraph lets the manager amend a clause of its own in a held node's condition when the fix needs no new decision, under the two existing provisos. It hands the text to the worker, and to the checker where a check is live. A clause made out of date by a later decision of the human is covered. A clause someone else wrote still goes to the human. The paragraph on handing a held condition over as written is reworded around this exception. A paragraph after the list of five things says that such amendments come with items 1 to 3 only.
               - `## The checker`: the paragraph on passing amended text now covers these amendments too.
               - `## What is in front of the human, and when`: a two-sentence pointer.
               - `expedition-standing-yes`: `## What a standing yes never covers` now opens by saying the new section comes first.
               - glossary: the **Manager** and **Relay** entries.
               - The four worker contracts: the opening paragraph has dropped "answers nothing itself" and names the two exceptions.
               - Checker contract: the opening, hard rule 5, the sentence on carrying questions, and the sentence on carrying the raise all name the exceptions.
               - Implementation contract: "Continue" now reads "where it has been rewritten".
               - All five contracts gain a hard rule: whoever reports that it cannot read or do something states what it tried, meaning the path, the command and the error.
               - `graph-conventions.md`: in `### Amend an acceptance condition`, step 2 is skipped for an amendment made without a flag, and step 3 runs only where step 2 raised a flag.
               - `.claude/rules/expedition-triggers.md`: the second trigger now settles or hands back first. Its `## Priority` is unchanged.
               What is unchanged: `### Two things the human can say that are not answers`, the list of flag markers, and the `## Flags` rule "never on your own judgement". The glossary has no entry for "needs a new decision". "product effect" appears nowhere under `.claude/`.

INDEX LINE:    Added `## What you handle before the human` to the manager contract: it settles fixes to its own choices that need no new decision, and hands back held information, before the queue. Every contradicting place now points at it.

NEW NODES:     none

INVALIDATIONS: Node 01, which is resolved, is extended in two small ways. First, the new section is also pointed at from `## What is in front of the human, and when` and from two checker sentences that node 01's list did not name. Second, the no-flag rule for an amendment that settles a fix to the manager's own clause also covers one made before the claim. Node 01's text supports this: "For an amendment the manager settles this way". Nothing contradicts node 01 or node 02.

CONDITIONS:    What I searched for. In every open node's `## Acceptance condition` and `## Question` (nodes 03, 05, 06 and 08), and in the resolved nodes' `## Answer` and `## Acceptance condition` (nodes 01 and 02), I searched for: `What is never yours`, `answers nothing itself`, `Changing one after it is written`, `Amend an acceptance condition`, `What a standing yes never covers`, `carries the raise`, `where the human has rewritten`, `Relay`, `five things` and `item 4`.
               - Node 03 (claimed): its question quotes the glossary's **Relay** entry, "answers nothing itself". That quote goes out of date once this work lands. The entry now reads "answers none of the questions that reach the relay", followed by a pointer to `## What you handle before the human`. Any edit node 03 makes to **Relay** touches the same entry as this work.
               - Node 08 (open): clauses 2 and 3 still hold. Item 4 of the list of five things, and step 2 of `### Amend an acceptance condition`, both still exist. Node 08's worker should know that step 2 now has a skip sentence for amendments made without a flag, and that a new paragraph after the list exempts the manager's own amendments. An `AMENDMENT` marker applies only to the amendments that still carry a flag. No clause needs replacing.
               - Node 06 (open): no match. Its clause 4 is about its own diff and still holds. Its target section is untouched.
               - Node 05: no match.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched, all in /home/ten/Projects/expedition-skill/.scratch/manager-own-choices/worktrees/07-own-choices-rule:
               - `.claude/skills/expedition/SKILL.md`
               - `.claude/skills/expedition/glossary.md`
               - `.claude/skills/expedition/graph-conventions.md`
               - `.claude/skills/expedition-standing-yes/SKILL.md`
               - `.claude/skills/expedition-implementation/SKILL.md`
               - `.claude/skills/expedition-grilling/SKILL.md`
               - `.claude/skills/expedition-precondition/SKILL.md`
               - `.claude/skills/expedition-prototype/SKILL.md`
               - `.claude/skills/expedition-checker/SKILL.md`
               - `.claude/rules/expedition-triggers.md`
               Files other nodes are written against: `SKILL.md`'s `### Changing one after it is written` gains two paragraphs, and its five-item list is unchanged (node 08 edits item 4). `graph-conventions.md`'s step 2 of `### Amend an acceptance condition` gains a sentence (node 08 edits that step). The glossary's **Relay** entry changed (node 03 quotes it). `### Two things the human can say that are not answers` is untouched (node 06).
               Bar: the repository's `CLAUDE.md` `## Commands` states no build, tests, formatter or CI. The worktree root has no build, test or CI files, which matches `map-implementation-rules.md`. So the bar is the standards and the condition. The scope command, re-run after the change, matches only lines that now carry their exception.
               Proposed commit message:
                 Manager settles its own choices and hands back held information before the human

                 Add `## What you handle before the human` to the manager contract and point
                 every contradicting place at it: the never-yours rows, amending a held
                 node's condition, the checker, standing yes, the glossary, the worker and
                 checker contracts, graph-conventions and the trigger file.

                 Node: manager-own-choices/07
```

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

```
PASS

Acceptance condition, one line per part. Every check below was run over the worktree at `/home/ten/Projects/expedition-skill/.scratch/manager-own-choices/worktrees/07-own-choices-rule`, using `git diff --word-diff=plain` and paragraphs unwrapped with awk.

- 1 (placement): In `.claude/skills/expedition/SKILL.md`, `## What you handle before the human` sits directly after `## What is never yours` and directly before `## The order you act in`. Established with `grep -n "^#"` and the diff.
  - 1a: "A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node." Met.
  - 1b: "A choice taken under a standing yes is yours, and is recorded as taken under that standing yes." Met.
  - 1c: The section covers a condition or amendment marked as your own, a node split, an edge, the order work is done in, and a scope list from re-running a recorded search. Met.
  - 1d: "A choice a worker made is not yours. That includes a condition a worker wrote." Met.
  - 1e: The paragraph uses the phrase "needs a new decision" and covers both reversing or narrowing and a judgement nobody has made. Met.
  - 1f: "Settle a fix ... only when the choice is your own and the fix needs no new decision. Every other fix goes to the human." Met.
  - 1g: "A worker's raise, or a checker's question or raise ... Hand that information back and resume the agent". Met.
  - 1h: "read nothing and run nothing to find it". Met.
  - 1i: For a checker, only where something is or how to reach it, and never a recorded decision or a reading of the condition. For a worker, any fact or recorded decision. Met.
  - 1j: "Where the agent hands the item back again, the item takes the usual route." Met.
  - 1k: The section's opening sentence puts this handling before the queue under `## What is in front of the human, and when` and before any standing yes. Met.
  - 1l: "carries no flag. Name it in no gate payload and in no node closing report." Met.
  - The section is prose with no per-case list of steps. Met.
- 2: In `### Changing one after it is written`, the new permission paragraph covers: the clause being your own; the fix needing no new decision; both provisos; handing the text to the worker, and to the checker where a check is live; a clause made out of date by a later decision of the human; a clause someone else wrote going to the human. The work says "clause" where the condition says "condition" in the out-of-date sentence. I read that as the same coverage. The two quoted sentences now carry "The one exception is the permission in the next paragraph", "otherwise" and "unless that permission covers the clause". The five-things list now has "apart from the amendments the paragraph after the list names". The paragraph after it grants items 1–3 (recorded, marked, kept apart), with no flag (item 4) and no closing-report mention (item 5). Met.
- 3: In the table, the "rewriting" row names "two exceptions ... amending a clause of your own in the condition of a node a worker holds". The "answering anything" row adds "or by settling or handing back what `## What you handle before the human` lets you". Met.
- 4: The `## The checker` paragraph now reads "or you amend it under `### Changing one after it is written`". Met.
- 5: `## What a standing yes never covers` in `.claude/skills/expedition-standing-yes/SKILL.md` now opens by putting `## What you handle before the human` first. Its list applies to the items "that remain". Met.
- 6: The Manager entry now limits "never answers one" to "A question that reaches the human" and adds the before-the-human handling. The Relay entry reads "answers none of the questions that reach the relay" and points at the new section. `grep -n "needs a new decision"` over the glossary finds nothing. `grep -rn "product effect" .claude/` finds nothing. Met.
- 7: In the grilling, implementation, precondition and prototype contracts, "answers nothing itself" is replaced by the settle-or-hand-back exception, confirmed by diff. Both checker sentences now carry "unless/except ... settles ... or hands you where something is or how to reach it". Met.
- 8: The implementation contract's Continue answer now reads "where it has been rewritten". Met.
- 9: A new last hard rule, "state what you tried: the path, the command and the error", is in all five contracts: checker 7, grilling 6, implementation 8, precondition 9, prototype 7. Met.
- 10: Step 2 of `### Amend an acceptance condition` in `graph-conventions.md` gains "Skip this step for an amendment that `### Changing one after it is written` ... makes without a flag". Step 3 is made conditional on step 2 having raised a flag, as a consequence. Met.
- 11: The second trigger in `.claude/rules/expedition-triggers.md` now settles or hands back first, and only "Otherwise" puts the item in front of the human. The diff has no hunk under `## Priority`. Met.
- 12: The diff has no hunk in `### Two things the human can say that are not answers`, and none in the flag-marker list of `graph-conventions.md`. Met.

The recorded search:
- Run as written at base, with `git grep` at `d49b11e`, it returned exactly the 12 lines the condition records. That matches.
- Run over the worktree, it returns `.claude/skills/expedition-checker/SKILL.md:447` and `.claude/skills/expedition/SKILL.md:56,596,599`. All four are listed places, now reworded with their exceptions, and none is a new place.

Edits outside the condition's list: none. All 10 changed files are named by the condition.
- Flag 07.2's pointer is in `.claude/skills/expedition/SKILL.md`. It also has a ground-1 reason: that section lists what never enters the queue, and without the pointer the new section would leave that list incomplete.
- Flag 07.3's two sentences are in the checker contract, which is in the list. They are further instances of the contradiction (ground 2), since they said that what is handed back reaches the human without exception.

Bar:
- The root `CLAUDE.md` `## Commands` states there is no build, no tests, no formatter and no CI. `ls -a` of the worktree shows no build or test tooling, so I ran no build or test command.
- `git diff --check` printed nothing, so the change adds no whitespace errors.
- The remaining half of the bar is the standards below.

Standards:
- I read only the standards in `.scratch/manager-own-choices/map-implementation-rules.md`.
- The following bore on this work: the `_Avoid_` lines of the glossary, checked by hand: "decision" is refused only for the grilling-node concept, and "rewrite" only for Supersede, and both appear here in their ordinary sense; `graph-conventions.md`; the root `CLAUDE.md` rules for writing, where every cited heading resolves (`grep -rn` for "What you handle before the human" gives 9 hits, and for "Changing one after it is written" every cite resolves) and no line numbers are cited; the trigger-file rule, which is met because the trigger file was edited in the same change.
- `/coding-principles` and `/naming` had nothing code-shaped to bear on.
- `/writing-for-agents` names no reviewing skill to run. I applied it by hand and found no breach.

QUESTIONS:
- None. Flags 07.1 to 07.5 are each true of the work: the no-flag sentence beside the five-things list, the pointer in `## What is in front of the human, and when`, the two checker sentences, the new last hard rule in each of the five contracts, and the heading `## What you handle before the human`.
```

### The human at gate 1, 2026-11-12 — `verbatim`

*""a scope list you got by re-running a recorded search" -> what is that referring to?"*

*Manager's note:* the manager answered with quotes from `### Changing one after it is written` in `SKILL.md`, from `### Acceptance condition` in `graph-conventions.md`, and from example 1 of issue 1. No gate outcome yet.

### Gate 1 — correct

The human's words, 2026-11-12, `verbatim`:

*"node 07 -> It looks like in this section we are over-specifying what manager vs. worker vs. human is, and the manager can probably answer that question itself without all of these details, which would bloat less and give it more flexibility in case the condition change. (this can land in a separate commit so I can clearly see the new diff that you're doing in answer to these notes)"*

*Manager's note:* as the human asked, the work as checked by run 1 is committed on the node's branch `worktree-07-own-choices-rule` before the correction, so the correction lands as a second commit. The deliverable branch `own-choices` is not moved until the gate is approved.

### Correction round 1

The human's words are under `### Gate 1 — correct` above. Passed to the worker as written.

#### The worker's raise in correction round 1, as it wrote it

```
NODE:          Write the rule for what the manager settles on its own
ABOUT:         Correction round 1 on node 07. The human asked that the new section `## What you handle before the human` stop spelling out what counts as the manager's, a worker's or the human's choice, and leave the manager to judge it. The commit `ed2ec0e` holds the checked work. The correction is uncommitted in the tree.
SO FAR:        I have already made the part of the correction that I believe keeps the condition met. It is uncommitted in .scratch/manager-own-choices/worktrees/07-own-choices-rule, in `.claude/skills/expedition/SKILL.md` only.
               The ownership paragraph went from five sentences to three short ones:
               "A choice is yours when you made it. A choice taken under a standing yes is yours too, recorded as taken under that standing yes. A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node. A choice a worker made, a condition it wrote included, is not yours."
               - The list is gone: a condition or amendment marked as the manager's own, a node split, an edge, the order work is done in, and a scope list got by re-running a recorded search.
               - Clauses 1a, 1b and 1d are still stated outright.
               - Clause 1c is now met only because each of its items is a choice the manager made. The section no longer names the items. A checker reading 1c literally ("It states all of the following") may judge it unmet.
               - The human's note reads as asking to cut more, perhaps 1a, 1b and 1d too ("over-specifying what manager vs. worker vs. human is"). That would break the condition outright. Clauses 1a to 1d were written by node 01's worker, so they are not mine to change.
               Nothing else changed. Flags: unchanged so far.
ASK:           Does the three-sentence paragraph now in the tree answer the correction, with clause 1c read as met because each of its items is a choice the manager made? Or should the condition be amended so the section states less, or nothing, about who owns a choice?
RECOMMENDED:   Keep the three-sentence paragraph now in the tree, and amend clause 1c to read "A choice is the manager's when the manager made it." That amendment comes from the human's own correction, so its words are fixed. It removes the risk that a literal reading fails 1c.
               I would keep 1a, 1b and 1d, each one sentence:
               - 1b records the human's own ruling from node 01, that a standing yes is not the human's validation.
               - 1a and 1d are the boundary the whole rule turns on. Without them, "your own choice" has no edge.
               The paragraph is now short. Cutting further saves little and drops the human's own standing-yes ruling.
ALTERNATIVES:  - Keep the paragraph as it now is, with no amendment, and let the checker judge 1c. This risks a FAIL on a literal reading.
               - Amend the condition to drop 1a to 1d, and cut the ownership paragraph entirely, leaving only "the choice is your own" in the rule. This is the leanest. It drops the standing-yes ruling from the shipped files.
               - Restore the full five-sentence paragraph from `ed2ec0e`. This declines the correction.

Changes: one paragraph in `.claude/skills/expedition/SKILL.md`, under `## What you handle before the human`. It touches clauses 1a to 1d, which the condition names.
Path touched: `.claude/skills/expedition/SKILL.md`.
Flags: no change.
Proposed second commit message, to use once the raise is settled:
  Manager contract: state whose choice it is without listing the cases

  Shorten the ownership paragraph of `## What you handle before the human`
  to the principle, as the human asked at the gate.

  Node: manager-own-choices/07
```

#### The human on the raise, 2026-11-12 — `verbatim`

*"the proposed corection seems good to me"*, then, asked whether this meant node 09 or node 07: *"the correction to "A choice is yours when you made it""*

The option this takes, the raise's `RECOMMENDED`, as the worker wrote it: "Keep the three-sentence paragraph now in the tree, and amend clause 1c to read "A choice is the manager's when the manager made it." That amendment comes from the human's own correction, so its words are fixed. It removes the risk that a literal reading fails 1c."

#### What the worker changed in correction round 1, as it wrote it

```
The correction is finished. The three-sentence paragraph you approved is the whole change, and nothing more was needed.

What I changed: in `## What you handle before the human`, the paragraph on whose choice it is now states the principle. It no longer lists the manager's choices (a condition or amendment marked as its own, a node split, an edge, the order work is done in, a re-run scope list). It now reads:

"A choice is yours when you made it. A choice taken under a standing yes is yours too, recorded as taken under that standing yes. A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node. A choice a worker made, a condition it wrote included, is not yours."

The rest of the section and every other file are as committed in `ed2ec0e`. I searched `.claude/` for anywhere else that repeats the removed list, and found none.

Does it touch the condition? Yes, clauses 1a to 1d. Under the amended condition each is stated outright:
- 1a: the human's own words, or an answer the human gave on a node.
- 1b: a choice taken under a standing yes is the manager's, recorded as such.
- 1c, as amended: a choice is the manager's when the manager made it.
- 1d: a worker's choice, a condition it wrote included, is not the manager's.

Path touched: `.claude/skills/expedition/SKILL.md`, uncommitted, in `.scratch/manager-own-choices/worktrees/07-own-choices-rule`.

Flags: no change.

Proposed commit message for the second commit:
  Manager contract: state whose choice it is without listing the cases

  Shorten the ownership paragraph of `## What you handle before the human`
  to the principle, as the human asked at the gate.

  Node: manager-own-choices/07
```

### Checker run 2 — `PASS`

The checker's entry, as it wrote it:

```
PASS

The work passes again on the amended condition. The human's correction changed only the paragraph that says whose a choice is. That paragraph meets the new clause 1c, and nothing else in the work moved.

What changed since run 1:
- The committed work: `git diff --stat d49b11e ed2ec0e` gives 10 files, +103 −33, the same as the work I checked in run 1. `ed2ec0e` is that work. I kept no hash of run 1's diff, so this rests on the matching size, plus the fact that every other changed file was last modified before the correction.
- The correction: `git diff ed2ec0e` (`--stat`, then `--word-diff=plain`) touches only `.claude/skills/expedition/SKILL.md`, 3 insertions and 5 deletions. Compared word for word, only the second paragraph of `## What you handle before the human` changed. The list of manager-owned choices (condition, amendment, node split, edge, order of work, re-run scope list) is replaced by "A choice is yours when you made it." The other three sentences are reworded without changing their meaning. The worker's account matches the diff.

One line per part of the condition (whole work, `d49b11e` to the working tree):
- 1a: "A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node." Met, read from the paragraph.
- 1b: "A choice taken under a standing yes is yours too, recorded as taken under that standing yes." Met.
- 1c (amended): "A choice is yours when you made it." Met.
- 1d: "A choice a worker made, a condition it wrote included, is not yours." Met.
- 1e to 1l, and the placement: these paragraphs are untouched by the correction, so my run 1 findings stand. I re-read the whole section to confirm. Met.
- No leftover list: `grep -rnE "node split|re-running a recorded search|order work is done in" .claude/` finds only implementation contract hard rule 6 ("needs your node split, raise"). That line predates the work and is not a list of the manager's own choices. So the removed list survives nowhere.
- 2 to 12: the correction does not touch them, so my run 1 findings stand. Clause 2 says "the clause shown wrong is your own", and both the glossary Manager entry and the rewriting row say "a choice / clause of your own". All three still read correctly against the new ownership rule.
- The recorded search: run over the tree, it returns `expedition-checker/SKILL.md:447` and `expedition/SKILL.md:56, 594, 597`. These are the same listed places as in run 1, now reworded; 594 and 597 shifted up two lines because the correction removed two lines. "product effect" appears 0 times. The run against `d49b11e` was already shown to match the recorded 12 lines in run 1.
- Edits outside the list: there are still none. The correction is inside a listed file.

Standards:
- `map-implementation-rules.md` was last modified on 2026-11-11 at 23:48, and its content is as I read it in run 1. I read only the standards in it.
- `git diff d49b11e -- CLAUDE.md` is empty, so the root `CLAUDE.md` rules are unmoved.
- The work changed no `_Avoid_` line in the glossary. In `graph-conventions.md` it adds only the step 2 exception, which I checked under clause 10. So I am holding the work against unmoved standards.
- The standards that bear on this work are the same as in run 1. The new paragraph is plain and has one idea per sentence. It breaches no `_Avoid_` refusal and no writing rule.

Bar:
- The root `CLAUDE.md` states there is no build, no tests, no formatter and no CI. The repository confirms it, so I ran no command for those.
- `git diff --check d49b11e` reports nothing, so the whole work adds no whitespace errors.

QUESTIONS:
- None. Flags 07.1 to 07.5 are unchanged and still true of the work.
```

### Gate 2 — approve, `standing yes`

Taken under standing yes 1, whose scope text is, word for word: "commits on feature branches dedicated to deliverables, in the current effort". What was taken: checker run 2's `PASS`. The correction is committed as the node's second commit, and the deliverable branch `own-choices` is fast-forwarded to it.
