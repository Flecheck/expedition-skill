# What the manager settles on its own, rather than putting it to the human

Type: grilling
Status: resolved

## Question

*Written by the manager.* Settling this lets a manager stop pausing an effort to ask the human about
choices the manager made itself, where the human's answer changes nothing the human decided.

GitHub issue 1, saved in [issue-1.md](../issue-1.md), reports that the manager sends the human choices
it authored: a condition it wrote and that a check showed slightly wrong, a scope it re-derived by
re-running a recorded search, clauses it moved after the human reordered a rollout, and a checker's
question the manager already held the answer to. The issue's comment proposes changes 1 to 4 under
`Proposed changes, smallest first`, and says they share one principle: the author of a choice, and
whether a fix has a product effect. The comment's `A note from the human on how to write the fix`
asks that the fix be kept to that principle, with no list of steps per scenario.

What should the workflow say about which matters the manager settles itself and which go to the human?
Settle at least the following. Whether the principle the issue proposes is the one to ship, and how its
terms are defined. How it relates to the rows of `## What is never yours` in the manager contract, to
the rule in `### Changing one after it is written` that a claimed node's condition is handed over as
written, and to the rule in `## Flags` that no flag is settled on the manager's own judgement. What the
manager does with a worker's raise, or a checker's question, that it can answer from what it already
holds, including where a standing yes is in force. Which shipped files change. Check first that each
clause the issue quotes still reads that way at the current `HEAD`.

Proposals 5 and 6 of the issue are other nodes. Example 8 is out of this node.

## Answer

The worker's answer, as it wrote it:

The manager settles a fix to a choice only when the choice is its own and the fix needs no new decision. Everything else goes to the human. Every clause the issue quotes was checked at `HEAD` `d49b11e` and still reads as the issue quotes it.

**Whose choice it is.** The human answered on payload 1's Q1 and corrected one point of the recommendation (`DIVERGENCE`).
- A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node.
- A choice taken under a standing yes is not the human's. It is the manager's, recorded as taken under that standing yes. The human: "Standing yes" should not be considered as a human validation - although in this case we can record e.g. manager via standing yes as the source".
- A choice is the manager's when it is any of these:
  - a condition or an amendment marked as the manager's own;
  - a node split;
  - an edge;
  - the order work is done in;
  - a scope list the manager got by re-running a recorded search.
- A choice a worker made is neither the human's nor the manager's. That includes a condition the worker wrote for a node it reported. A fix to it still goes to the human.

**Needs a new decision.** A fix to a choice needs a new decision when it reverses or narrows something the human decided, or when it needs a judgement nobody has made. Equivalently, it needs none when the manager could have written the fixed version in the first place under constraint 1 of `### The four constraints on a condition you write yourself`.
- The human accepted the definition: "its definition is fine".
- The human asked for a different name than "product effect", and took the plain phrase "needs a new decision": "ok for decision for now and I'll see when reviewing the change what it looks like."
- No term is coined, and the glossary gains no entry. "Product effect" appears in no shipped file.
- Example 2a goes to the human only if the human wrote the clause. The human: "2a should be raised if created by human, otherwise not."

**Information the manager already holds** (payload 3, Q2 "yes"). A worker's raise, or a checker's question or raise, may say the agent is blocked by missing information that the manager already holds. The manager then hands that information back and resumes the agent, instead of putting the item to the human.
- It hands back only what is already in its context. It reads nothing and runs nothing to find the information.
- To a checker, it hands back only where something is or how to reach it. It never hands a checker a recorded decision or a reading of the condition.
- To a worker, it may hand back any fact or recorded decision.
- If the agent hands the item back again, the item takes the usual route.
- Every worker contract and the checker contract say that an agent reporting it cannot read or do something states what it tried: the path, the command and the error.

**When this applies.** Settling a fix to the manager's own choice, and handing back held information, both come before an item enters the queue, and before any standing yes is taken.

**No flag for what the manager settles itself** (Q3 "yes").
- A choice the manager settles under the rule carries no flag. It is named in no gate payload and no node closing report.
- For an amendment the manager settles this way, items 1 to 3 of the five things under `### Changing one after it is written` still apply, and items 4 and 5 do not.
- The `## Flags` rule "never on your own judgement" stays as it is, because no flag exists to settle.

**Amending the manager's own condition after the claim** (Q4 "yes").
- A worker's raise, or a checker's finding, question or raise, may show a clause of the manager's own wrong. Where the fix needs no new decision, the manager amends the claimed node's condition under the two existing provisos: every word is already fixed, and the source is named.
- It hands the amended text to the worker, and to the checker where a check is live, then the check runs again.
- A condition made out of date by a later decision of the human, such as a reordered rollout, falls under the same rule.
- A clause someone else wrote still goes to the human.

**The `AMENDMENT` marker** (payload 3, Q6). This is a sixth flag marker: "an agent amended a condition after it was written; the manager files it".
- It is for an amendment an agent wrote that still carries a flag. An amendment the human makes carries no flag.
- It joins `ASSUMPTION` and `DELEGATED` under node 02's rule: a "you decide" on it keeps the amendment and settles the flag.
- The human: "yes ok for AMENDMENT but once again it looks like we're working on things separate to the issue at hand?" The issue does not raise this marker. It entered this node through node 02's gap. So it ships as its own node, apart from the fix for issue 1.

**Where it is written.**
- The rule is stated once, in a new section of `.claude/skills/expedition/SKILL.md` directly after `## What is never yours`.
- Each other place it touches points at that section by heading, and none restates it. Those places are: `## What is never yours`, `### Changing one after it is written`, `## The checker`, `expedition-standing-yes`'s `## What a standing yes never covers`, the glossary's **Manager** and **Relay** entries, the opening sentence of each worker contract, the checker's raise, the implementation contract's `### The raise`, `graph-conventions.md`'s `### Amend an acceptance condition`, and the second trigger in `.claude/rules/expedition-triggers.md`.
- The fix states the principle and lists no steps per case, as the human's note on the fix asks.
- Proposals 5 and 6 of the issue are nodes 02 and 03. Example 8 stays out.

**INVALIDATIONS, as the worker wrote it:** Node 02, which is resolved, is extended. Its answer says "Two of the five markers in `graph-conventions.md` record a choice an agent made" and "No marker changes". There will now be six markers. A third of them, `AMENDMENT`, records a choice an agent made, and joins `ASSUMPTION` and `DELEGATED` under node 02's rule. Nothing else in node 02 changes.

**CONDITIONS, as the worker wrote it:** **What I searched for.** I searched every open node's `## Acceptance condition` and `## Question` sections (nodes 03, 05 and 06), and the `## Answer` sections of the resolved and superseded nodes (02 and 04). The search terms were: `product effect`, `ASSUMPTION`, `DELEGATED`, `marker`, `answers nothing itself`, `Relay`, `Manager`, `Changing one after it is written`, `What is never yours`, `standing yes`, `graph-conventions.md` and `expedition-triggers.md`. **Node 06 (unclaimed): replacement for clause 1.** Only the list of markers changes. The text is fixed by node 01's answer once it resolves (payload 3 Q6, which the human took). [Filed on node 06 as its amendment 1.] Node 06 should also be blocked on node B, so that it does not name a marker before that marker exists. Node 06's clause 4 ("graph-conventions.md … unchanged") is still right for node 06's own work. I noticed that clause 1 says "these two sentences" over a quote of four sentences. I left that wording as it was, because nothing my work fixes reaches it. **Node 03 (claimed).** Its question quotes the glossary's **Relay** entry, "answers nothing itself", and the **Manager note** entry. Node A's clause 6 changes the **Relay** entry, so the question's quote will go out of date once node A lands. Any implementation node that comes out of node 03 and edits **Relay** would edit the same entry as node A. The manager should order those two nodes, or raise the overlap. **Node 05 (open).** No match. Its question is unchanged.

**MISSING FROM MAP, as the worker wrote it:** none

*Manager's note:* the worker's node A is [node 07](07-write-the-rule-for-what-the-manager-settles-on-its-own.md), and its node B is [node 08](08-add-the-amendment-flag-marker.md).

## Flags

`01.1` `ASSUMPTION` **· settled** — I settled Q5 myself: the rule is written once, in a new section of `SKILL.md` placed directly after `## What is never yours`, and gets no glossary entry. The human took Q7's recommendation, whose text reads "coin no term" and "It needs no glossary entry". With no term coined, the glossary's rule that a term needs an entry does not apply. Writing the rule once and pointing at it from each place it touches follows rule 6 of the root `CLAUDE.md`'s rules for writing, and the human's note to keep the fix to the principle. Placing it beside `## What is never yours` keeps it next to the rows it makes exceptions to. I did not ask, because the human's answers to Q7 and Q2 to Q4 left nothing about placement open.

`01.2` `ASSUMPTION` **· settled** — I derived the list of shipped files that change by searching, and did not ask the human about it. The command was `grep -rnE "answers nothing itself|never answers one on|where the human has rewritten|goes to the human as usual|carries the raise to the human|carries the questions to the human|and the human answers|a node nobody holds yet|product effect" .claude/`, run at `d49b11e`. It found the standing-yes line "Each of the following goes to the human as usual", glossary lines 83 and 231, the opening sentence of the precondition, grilling, implementation and prototype contracts, the implementation contract's "where the human has rewritten", the checker's "The manager carries the raise to the human", and `SKILL.md`'s "rewriting an acceptance condition" row and its "a node nobody holds yet … the human answers" passage. By reading I added the checker's wrapped sentence "The manager carries the questions to the human", which the grep missed because it spans a line break. I also added `graph-conventions.md`'s `### Amend an acceptance condition` step 2, and the trigger file. The trigger file is in the list because the root `CLAUDE.md` requires it to follow any edit to the governing statement of a trigger duty. Each place says something the answer makes untrue.

`01.3` `ASSUMPTION` **· settled** — I split the `AMENDMENT` marker into an implementation node of its own, blocked on the node that writes the rule for issue 1, rather than writing it into that node. The human approved the marker and also asked whether the work had strayed from the issue. A separate node keeps the fix for issue 1 to the issue. Running the two in order keeps them from conflicting, because both edit the list of five things under `### Changing one after it is written`. Node 06 then has to wait for the marker node, because its new clause 1 names a marker that does not exist until that node lands.

`01.4` `ASSUMPTION` **· settled** — I read the human's "I think I agree with your definition" on payload 1 as agreement. The human's next reply confirmed it: "its definition is fine".

## Interview

### Attempt 1

#### Payload 1, as the worker handed it back

```
NODE:          What the manager settles on its own, rather than putting it to the human

ABOUT:         This node decides which matters the manager settles itself and which go to the human. It is decided now because GitHub issue 1 reports that efforts stop to ask the human about choices the manager made itself. The first payload settles the principle and its terms. It also settles the separate case where the manager already holds the information an agent is missing.

SO FAR:        I read the node, the map, issue-1.md, the manager contract (`.claude/skills/expedition/SKILL.md`), the glossary, `expedition-standing-yes`, and the raise and question sections of the checker and implementation contracts.
               Every clause the issue quotes still reads that way at `d49b11e`:
               - `### Changing one after it is written` still says "Where a worker already holds the node, its condition is handed over as written. A worker that judges the condition wrong raises it, and the human answers." The same section still says "Re-derive an enumerated scope before the node is claimed". Its list of five things still says each amendment "is carried as a flag of its own, which settles at that node's gate".
               - `## Flags` still says "Settle a flag only at the moments this section names, never on your own judgement or on the passage of time."
               - `expedition-standing-yes`, under `## What a standing yes never covers`, still lists "a checker's raise, which includes a question a checker hands back beside its outcome", with no exception.
               - `### Two things the human can say that are not answers` is unchanged. It belongs to node 02.
               Three facts in the files bear on the principle:
               - The manager's own conditions are already marked as its own: constraint 3 of `### The four constraints on a condition you write yourself` says so, and so does item 2 of an amendment's five things. So which conditions the manager wrote can be checked on the node.
               - Constraint 1 already limits what the manager may write in a condition: "Demand only what is already fixed, by a settled node, by the node's own question, or by the state of the files."
               - `### Changing one after it is written` already sends to the human any replacement where "any part of the replacement needs a judgement nobody has made".
               Held for later payloads, because their answers depend on Q1:
               - whether a flag on the manager's own choice settles when it is filed (proposal 2, example 1);
               - whether the manager may amend its own condition after the claim (proposal 3), and how that fits the "rewriting an acceptance condition" row of `## What is never yours`, the "handed over as written" rule, and the `## Flags` rule;
               - whether the terms go into the glossary or only into `SKILL.md`;
               - which shipped files change, including whether `.claude/rules/expedition-triggers.md` must follow.

Q1. The principle, and what "product effect" means
CONTEXT:       The manager's note says the sharpest point is where a correction of a manager-written condition stops "changing nothing the human decided". Examples 2 and 3 sit near that line. Read literally, the issue's test puts example 2a on the human's side, and 2a is one of the examples the issue means to clear.
ASK:           Do we ship the issue's principle (the author of a choice, and whether a fix has a product effect), and is "product effect" measured against what the human decided, or against how the product reads to its user?
RECOMMENDED:   Ship the principle, and measure product effect against what the human decided:
               - **Author of a choice.** This is whoever made the choice:
                 - the human: their own words, or an answer recorded on a node, an item taken under a standing yes included;
                 - a worker: what it handed back, including a condition it wrote for a node it reported;
                 - the manager: a condition or an amendment marked as its own, a node split, an edge, the order work is done in, or a scope list it got by running a recorded search.
               - **Product effect.** A fix has a product effect when it reverses or narrows something the human decided, or when it needs a judgement nobody has made. Put another way, the fix has none when the manager could have written the fixed version in the first place under constraint 1.
               - **The rule.** The manager settles a fix only when the choice is its own and the fix has no product effect. Everything else goes to the human.
               How the issue's examples come out under this rule:
               - Example 1: the manager settles it. The longer list is just the output of the recorded command.
               - Example 2a: the manager settles it. The manager wrote the comment's wording, and the fix makes the comment true of the code. If the human had dictated that invariant, the fix would go to the human.
               - Example 2b: the manager settles it. The fix follows from the state of the files.
               - Example 3: the manager settles it, unless the human themselves decided the column is non-null.
               - Example 4: the moves carry out the order the human chose, so the manager settles them. Suspending the clause that became impossible is the manager's to settle too, unless that clause was something the human asked for.
               This rests on two points. First, the issue's literal test ("would the finished product behave or read differently for its user?") sends 2a to the human, because the comment does read differently, and the test is hard to apply where the product is prose. Second, measuring against the human's decisions adds no new idea: it reuses constraint 1 and the existing "judgement nobody has made" rule.
ALTERNATIVES:  - The issue's literal test, "behave or read differently for its user". It sends 2a to the human and is hard to apply to prose.
               - The same line, but with the term "product effect" dropped and the rule worded only as "changes nothing the human decided". The substance is the same, but it loses one of the two terms your note on the fix names.
               - Also let the manager settle fixes to conditions a worker wrote. That conflicts with the `## What is never yours` row "authoring an acceptance condition for a node an agent minted".
               - Ship no principle, and keep sending every correction of the manager's own choices to the human.

---

Q2. A raise or question the manager can answer from what it already holds
CONTEXT:       Example 5 and proposal 4. This is independent of Q1, because handing back information decides nothing.
ASK:           When a worker's raise, or a checker's question or raise, says the agent is blocked by missing information that the manager already holds, does the manager hand that information back and resume the agent instead of putting the item to the human, and within what limits?
RECOMMENDED:   Yes, within these limits:
               - The manager hands back only what is already in its context. It reads nothing and runs nothing to find the answer. That is the same limit spawn notes already have: "Write a note only from context you already hold".
               - This step comes before the queue and before any standing yes. The manager settles and answers nothing in it, so a standing yes has nothing to take. If the agent hands the item back again, the item follows the usual route.
               - To a checker, the manager hands only where something is or how to reach it, such as a path or a repository's location. It never hands a checker a recorded decision or a reading of the condition. The checker is blind to the record by design, and `## The checker` says to "supply nothing it leaves out".
               - To a worker, the manager may hand any fact or recorded decision, because a worker reads the record anyway.
               - Every worker contract and the checker contract gain one line: an agent that reports it cannot read or do something states what it tried, meaning the path, the command and the error.
               In example 5, the manager would have handed the checker the sibling repository's location and resumed it. The checker would then have established the answer itself. The manager would not have read the path, and the human would not have been asked.
ALTERNATIVES:  - Also hand a checker recorded decisions from the map. This breaks the checker's blindness and supplies what the condition leaves out.
               - Let the manager read or run things to answer, as it did in example 5. This spends the manager's context, which is the first resource to run out, and makes the manager the author of a finding.
               - Keep sending such items to the human, and only let a standing yes cover a checker's question. This still costs a round trip, and without a standing yes the human is still asked.
               - Drop the "state what you tried" line.
```

#### The human on payload 1, Q1, 2026-11-12 — `verbatim`

*"2a should be raised if created by human, otherwise not. "Standing yes" should not be considered as a human validation - although in this case we can record e.g. manager via standing yes as the source
I think I agree with your definition of "product effect".
"One clause asked a comment to state an invariant that the code contradicts" -> not sure how just from that reading of the example you can deduce it does have a product effect? (which I imagine is why you're saying it would have been raised?)"*

*Manager's note:* this answers part of Q1 and asks the worker a question about its reading of example 2a. It diverges from the recommendation on one point: the worker's recommendation counted "an item taken under a standing yes" as the human's choice, and the human says it is not. `DIVERGENCE` on that point. Q2 has no answer yet. Sent back to the worker.

#### Payload 2, as the worker handed it back

```
NODE:          What the manager settles on its own, rather than putting it to the human

ABOUT:         This node decides which matters the manager settles itself and which go to the human (GitHub issue 1). This payload answers your question about example 2a, records what Q1 now settles, asks Q2 again, and asks the questions that were waiting on Q1.

SO FAR:        **Your question on example 2a.** I did not conclude from the example that its fix has a product effect, and the example's text does not show one. What I meant was conditional. The fix would count as having a product effect only if you had written that invariant's wording yourself, because changing it would then reverse something you decided. That is your own reading: raise it if the human created it, settle it otherwise. The effect comes from who wrote the wording, not from what the comment says. The example does not say who wrote it. The issue says "Both were wordings the manager had written", so as reported, the manager settles it.

               **What Q1 now settles**, read from your reply:
               - The principle ships.
               - "Product effect": a fix has a product effect when it reverses or narrows something the human decided, or when it needs a judgement nobody has made. Equivalently, the manager could not have written the fixed version in the first place under constraint 1 of `### The four constraints on a condition you write yourself`. Your words were "I think I agree". I read that as agreement. Say so if it was not.
               - Author of a choice. A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node. A choice taken under a standing yes is not the human's. It is recorded as the manager's, taken under that standing yes. This follows your correction of my recommendation.
               - The rule: the manager settles a fix only when the choice is its own and the fix has no product effect. Everything else goes to the human.
               One consequence follows. A choice taken under a standing yes is not something the human decided. So a later fix to it is the manager's to settle when that fix has no product effect.
               I see nothing else still open on Q1.

               **Provisional list of files that change.** It is only a list, and it depends on the answers below:
               - `.claude/skills/expedition/SKILL.md`: `## What is never yours`, `## Flags`, `### Changing one after it is written`, `## The checker`, and `## What is in front of the human, and when`;
               - `glossary.md`;
               - `graph-conventions.md`, for the flag markers and the definition of a settled flag;
               - `expedition-standing-yes`;
               - the checker and implementation contracts;
               - possibly `.claude/rules/expedition-triggers.md`, whose trigger "put it in front of the human as soon as nothing else is in front of them" would gain a step before it if Q2 is yes.
               The question of which files change waits for the answers below.

Q2. A raise or question the manager can answer from what it already holds
CONTEXT:       This comes from example 5 and proposal 4. It is independent of Q1. It is asked again because it has no answer yet.
ASK:           When a worker's raise, or a checker's question or raise, says the agent is blocked by missing information that the manager already holds, does the manager hand that information back and resume the agent, instead of putting the item to the human? If so, within what limits?
RECOMMENDED:   Yes, within these limits:
               - The manager hands back only what is already in its context. It reads nothing and runs nothing to find the information. That is the same limit spawn notes already have.
               - The step comes before the queue and before any standing yes, because it answers nothing. If the agent hands the item back again, the item takes the usual route.
               - To a checker, the manager hands back only where something is or how to reach it, such as a path or a repository's location. It never hands a checker a recorded decision or a reading of the condition. The checker is blind to the record by design, and `## The checker` says to "supply nothing it leaves out".
               - To a worker, the manager may hand back any fact or recorded decision.
               - Every worker contract and the checker contract gain one line: an agent that reports it cannot read or do something states what it tried (the path, the command, the error).
               Applied to example 5: the manager hands the checker the sibling repository's location and resumes it. The checker then establishes the answer itself.
ALTERNATIVES:  - Also hand a checker recorded decisions. That breaks the checker's blindness.
               - Let the manager read or run things to answer, as it did in example 5. That spends the manager's context and makes the manager the author of a finding.
               - Keep sending such items to the human, and let a standing yes cover a checker's question. That still costs a round trip.
               - Drop the "state what you tried" line.

---

Q3. What record a choice the manager settles itself leaves
CONTEXT:       This is proposal 2. The proposal is a flag marked settled at filing, with the reason `own choice, no product effect`. Your note on the fix says no log or report line is needed for these choices. `graph-conventions.md` also defines a settled flag as "one the human has dealt with".
ASK:           When the manager settles one of its own choices under the principle, does that choice carry a flag at all?
RECOMMENDED:   No flag, and no line in the node closing report or the gate payload. The choice is recorded only where the choice itself lives:
               - For an amendment to a condition, items 1 to 3 of `### Changing one after it is written` still apply: it is recorded beside the search or fact that justified it, marked as the manager's, and kept apart from the author's text. Items 4 (a flag) and 5 (named in the node closing report) are dropped for it.
               - A node split or an edge is recorded in the graph as it is today.
               What this rests on:
               - It follows your note on the fix.
               - The `## Flags` rule "never on your own judgement" stays true unchanged, because no flag exists to settle.
               - The definition of a settled flag stays true too.
ALTERNATIVES:  - The issue's form: a flag marked `**· settled**` at filing, with the reason `own choice, no product effect`. This adds a third settling moment, and it breaks "a settled flag is one the human has dealt with".
               - Keep a flag that settles at the gate, as today. This is the behaviour the issue reports.

---

Q4. The manager amends its own condition after the node is claimed
CONTEXT:       This is proposal 3, covering examples 2, 3 and 4. Today `### Changing one after it is written` limits amendments to "a node nobody holds yet". The `## What is never yours` row "rewriting an acceptance condition" sends a held node's wrong condition to the human.
ASK:           May the manager amend a claimed node's condition, without asking the human, where the clause shown wrong is its own and the fix has no product effect?
RECOMMENDED:   Yes:
               - The trigger is a worker's raise or a checker's finding, question or raise that shows the manager's own clause wrong.
               - The manager writes the replacement under the two provisos that already exist: every word is already fixed, and the source is named.
               - It hands the amended text to the worker. If a check is live, it hands the text to the checker too, by the route `## The checker` already gives for an amendment by the human. It then resumes or re-runs the check.
               - A condition made out of date by a later decision of the human, such as the reordered rollout in example 4, falls under the same rule. That decision is fixed, so following it has no product effect.
               - The worker still raises a condition it judges wrong. The manager takes the raise before the queue, and before any standing yes.
               - The `## What is never yours` row gains this as a second exception.
               - The implementation contract's "against the corrected acceptance condition where the human has rewritten it" becomes "where it has been rewritten".
               - A clause someone else wrote still goes to the human.
ALTERNATIVES:  - Amend only before the claim, as today. Examples 2 to 4 then still reach the human.
               - Also let the manager amend a worker-written clause when the fix has no product effect. That conflicts with the row "authoring an acceptance condition for a node an agent minted".

---

Q5. Where the principle and its term are written
CONTEXT:       The glossary requires an entry for every term the skill files use in its vocabulary. A term is added only once a node has settled it.
ASK:           Where are the principle and its terms written?
RECOMMENDED:   Add one glossary entry, **Product effect**, with the definition Q1 settled. "The author of a choice" is plain English and gets no entry. State the rule once, in a new section of `SKILL.md` beside `## What is never yours`. `## Flags`, `### Changing one after it is written`, `## The checker` and `expedition-standing-yes` point at that section by heading. They do not restate it. This keeps the fix to the principle, with no list of steps per scenario, as your note on the fix asks.
ALTERNATIVES:  - Also add a glossary entry for "author of a choice" or "own choice".
               - Add no glossary entry, and write "product effect" out in plain words wherever it is used.
               - Restate the rule in each section it touches. That is what the repository's writing rule 6 refuses.

---

Q6. The marker for an amendment someone else wrote
CONTEXT:       Node 02's worker found this gap and left it to this node. Item 4 of `### Changing one after it is written` carries every amendment "as a flag of its own". None of the five markers in `graph-conventions.md` fits: `ASSUMPTION` is defined as the worker's, and the others name other things. If Q3 is answered as recommended, only an amendment whose clause another party wrote, or whose fix has a product effect, still needs that flag.
ASK:           What marker does the flag for an amendment carry?
RECOMMENDED:   Add a sixth marker, `AMENDMENT`, defined as "a condition was amended after it was written; the manager files it", in `graph-conventions.md`'s list of markers. Its entry's first sentence is the amending party's own sentence, where one exists.
ALTERNATIVES:  - Drop the flag for every amendment written under the two provisos, whoever wrote it. That goes beyond the principle, because the choice is not the manager's own.
               - Reuse `ASSUMPTION` for it. That breaks that marker's definition.
```

#### The human on payload 2, Q1 and Q5, 2026-11-12 — `verbatim`

*"Not sure about the "product effect" concept's naming: its definition is fine but I fear it may be a general concept that may confuse users that interact with the manager if the manager refers to it as such. Can you suggest other names? (/naming)"*

*Manager's note:* this confirms the definition and questions the term's name. Sent back to the worker. Q2, Q3, Q4 and Q6 have no answer yet.

#### Payload 3, as the worker handed it back

```
NODE:          What the manager settles on its own, rather than putting it to the human

ABOUT:         This node decides which matters the manager settles itself and which go to the human (GitHub issue 1). This payload asks for a name for the concept you called "product effect". It also asks again Q2, Q3, Q4 and Q6, which have no answer yet.

SO FAR:        Settled by your earlier replies:
               - The principle ships: the manager settles a fix only when the choice is its own and the fix has no effect on what the human decided.
               - A choice is the human's only when it is in the human's own words, or in an answer the human gave on a node. A choice taken under a standing yes is recorded as the manager's, taken under that standing yes.
               - The definition stands: a fix has the effect when it reverses or narrows something the human decided, or needs a judgement nobody has made. Equivalently, the manager could not have written the fixed version in the first place under constraint 1 of `### The four constraints on a condition you write yourself` ("Leave out anything you would otherwise have to decide").
               - Example 2a goes to the human only if the human wrote the clause.
               - Node 02 has resolved, and its ruling bears on Q6: a *"you decide"* on an `ASSUMPTION` or `DELEGATED` flag keeps the agent's choice and settles the flag. On any other flag, the manager asks what was meant.
               Held until Q7 is answered: Q5, where the rule and its term are written. Whether a glossary entry is needed depends on whether the name is a coined term or plain words. Also held: which shipped files change.

Q7. A name for the concept you called "product effect"
CONTEXT:       I ran the `/naming` method on it. The sentence it names is: "the fix to the manager's own choice reverses or narrows something the human decided, or needs a judgement nobody has made". The path already says "a fix to the manager's own choice". What is left is "decides something the human has not decided". Both halves are one thing: reversing the human's decision means deciding anew, and a judgement nobody has made is a decision not yet taken.
ASK:           Which name should the workflow use for the concept you called "product effect"?
RECOMMENDED:   Use the plain phrase "needs a new decision", and coin no term. The rule then reads: "The manager settles a fix to its own choice when the fix needs no new decision. A fix that needs a new decision goes to the human."
               Round trip: "a fix to the manager's own choice that needs no new decision" gives back "every word of the fix is already fixed, and nothing the human decided is reversed". That matches the definition.
               It suits your worry:
               - It is ordinary English, and it says what it means to a user who reads it cold.
               - It mirrors constraint 1's own words, "anything you would otherwise have to decide".
               - It needs no glossary entry, which keeps the change small.
               One caution: the glossary refuses "decision" only as a name for the grilling kind of node. Using the word in its ordinary sense breaks nothing.
ALTERNATIVES:  - "Touches a human decision". This misses the half about a judgement nobody has made.
               - "Already determined" (a fix whose every word is already fixed). This names the other side of the line and is vaguer.
               - A coined term such as "decision effect". It needs a glossary entry, and it is as opaque as "product effect" to a user.
               - Keep "product effect". This is the confusion you raised.

---

Q2. A raise or question the manager can answer from what it already holds
CONTEXT:       This comes from example 5 and proposal 4. It is unchanged from the last payload.
ASK:           When a worker's raise, or a checker's question or raise, says the agent is blocked by missing information that the manager already holds, does the manager hand that information back and resume the agent, instead of putting the item to the human? If so, within what limits?
RECOMMENDED:   Yes, within these limits:
               - The manager hands back only what is already in its context. It reads nothing and runs nothing to find the information.
               - The step comes before the queue and before any standing yes, because it answers nothing. If the agent hands the item back again, the item takes the usual route.
               - To a checker, the manager hands back only where something is or how to reach it, such as a path or a repository's location. It never hands a checker a recorded decision or a reading of the condition, because `## The checker` says to "supply nothing it leaves out".
               - To a worker, the manager may hand back any fact or recorded decision.
               - Every worker contract and the checker contract gain one line: an agent that reports it cannot read or do something states what it tried (the path, the command, the error).
ALTERNATIVES:  - Also hand a checker recorded decisions. That breaks the checker's blindness.
               - Let the manager read or run things to answer. That spends the manager's context and makes the manager the author of a finding.
               - Keep sending such items to the human, and let a standing yes cover them. That still costs a round trip.
               - Drop the "state what you tried" line.

---

Q3. What record a choice the manager settles itself leaves
CONTEXT:       This is proposal 2. It is unchanged from the last payload.
ASK:           When the manager settles one of its own choices under the principle, does that choice carry a flag at all?
RECOMMENDED:   No flag, and no line in the node closing report or the gate payload. This follows your note on the fix.
               - For an amendment to a condition, items 1 to 3 of `### Changing one after it is written` still apply: it is recorded beside the search or fact that justified it, marked as the manager's, and kept apart from the author's text. Items 4 (a flag) and 5 (named in the node closing report) are dropped for it.
               - The `## Flags` rule "never on your own judgement" stays true, because no flag exists to settle.
ALTERNATIVES:  - A flag marked `**· settled**` at filing, with a reason. This breaks "a settled flag is one the human has dealt with".
               - Keep a flag that settles at the gate, as today. This is the behaviour the issue reports.

---

Q4. The manager amends its own condition after the node is claimed
CONTEXT:       This is proposal 3, covering examples 2, 3 and 4. It is unchanged from the last payload, apart from using the Q7 recommendation's wording.
ASK:           May the manager amend a claimed node's condition, without asking the human, where the clause shown wrong is its own and the fix needs no new decision?
RECOMMENDED:   Yes:
               - The trigger is a worker's raise, or a checker's finding, question or raise, that shows the manager's own clause wrong.
               - The manager writes the replacement under the two provisos that already exist: every word is already fixed, and the source is named.
               - It hands the amended text to the worker. If a check is live, it hands the text to the checker too, by the route `## The checker` already gives. It then resumes or re-runs the check.
               - A condition made out of date by a later decision of yours, such as the reordered rollout in example 4, falls under the same rule.
               - The `## What is never yours` row "rewriting an acceptance condition" gains this as a second exception.
               - The implementation contract's "where the human has rewritten it" becomes "where it has been rewritten".
               - A clause someone else wrote still goes to the human.
ALTERNATIVES:  - Amend only before the claim, as today.
               - Also let the manager amend a clause a worker wrote. That conflicts with the row "authoring an acceptance condition for a node an agent minted".

---

Q6. The marker for an amendment, and what a "you decide" on it does
CONTEXT:       Item 4 of `### Changing one after it is written` carries every amendment "as a flag of its own". No current marker fits it. Revised since the last payload: node 02's ruling now makes this question also cover what a *"you decide"* on such a flag does.
ASK:           What marker does an amendment's flag carry, and does a *"you decide"* on it keep the amendment and settle the flag, as it does for `ASSUMPTION` and `DELEGATED`?
RECOMMENDED:   Add a sixth marker, `AMENDMENT`, to the list of markers in `graph-conventions.md`, defined as "an agent amended a condition after it was written; the manager files it".
               - It covers only an amendment an agent wrote that still needs a flag. That means one by the party that established a fact, or by a worker reporting a related defect, and not one the manager settles under Q3.
               - An amendment the human makes carries no flag, because a flag records an agent's judgement.
               - It joins `ASSUMPTION` and `DELEGATED`: a *"you decide"* on it keeps the amendment and settles the flag, because it records a choice an agent made.
               - If you agree, my handover gives node 06 a replacement for clause 1 of its condition that names the three markers.
ALTERNATIVES:  - Drop the flag for every amendment written under the two provisos, whoever wrote it. That goes beyond the principle.
               - Reuse `ASSUMPTION` for it. That breaks that marker's definition.
               - Add `AMENDMENT`, but leave it out of the *"you decide"* rule, so the manager asks what was meant. That costs a round trip on a choice that has already been made.
```

#### The human on payload 3, Q2, 2026-11-12 — `verbatim`

*"Q2: I don't understand why you want to handle differently the checker and the worker."*

*Manager's note:* the manager answered with quotes only: the worker's own reason from payload 3's Q2, and the `SKILL.md` passages it rests on. It offered to send the question to the worker.

#### The human on payload 3, Q7, 2026-11-12 — `verbatim`

*"Q7: your proposed definition seems to bear on a strongly defined concept of decision, I wonder where that is defined?"*

*Manager's note:* the manager answered with quotes only: the glossary's one use of "decision", the worker's own caution from payload 3's Q7, and what payload 3's `SO FAR` records the human's earlier reply settling about whose choice counts. It offered to send the question to the worker.

#### The human on payload 3, Q7, 2026-11-12 — `verbatim`

*"ok for decision for now and I'll see when reviewing the change what it looks like."*

The option this takes, payload 3's Q7 `RECOMMENDED`, as the worker wrote it: "Use the plain phrase "needs a new decision", and coin no term. The rule then reads: "The manager settles a fix to its own choice when the fix needs no new decision. A fix that needs a new decision goes to the human.""

*Manager's note:* Q2, Q3, Q4 and Q6 have no answer yet. The manager holds the resume until they do.

#### The human on payload 3, Q2, Q3, Q4 and Q6, 2026-11-12 — `verbatim`

*"Q2 yes
Q3 yes
Q4 yes
Q6 I don't understand what amendment here is about. Why would an agent amend a condition? What does it mean for an agent to amend the condition that the manager files? I have no idea."*

The options these take, as the worker wrote them in payload 3: Q2, Q3 and Q4 each take that question's `RECOMMENDED`. Q6 has no answer yet.

*Manager's note:* the manager answered Q6 with quotes only, from `### Changing one after it is written` in `SKILL.md` and from node 16 of the closed `rename-split-upgrade` effort, and offered to send it to the worker.

#### The human on payload 3, Q6, 2026-11-12 — `verbatim`

*"yes ok for AMENDMENT but once again it looks like we're working on things separate to the issue at hand?"*

The option this takes, payload 3's Q6 `RECOMMENDED`, as the worker wrote it: "Add a sixth marker, `AMENDMENT`, to the list of markers in `graph-conventions.md`, defined as "an agent amended a condition after it was written; the manager files it". … It joins `ASSUMPTION` and `DELEGATED`: a *"you decide"* on it keeps the amendment and settles the flag, because it records a choice an agent made."

*Manager's note:* the manager told the human that Q6 entered this node through the manager's own note on resuming the worker, passing on a gap node 02's worker found, and that the issue does not raise it.

## Annotation: node 07 widens two places

As the worker of [node 07](07-write-the-rule-for-what-the-manager-settles-on-its-own.md) wrote it: Node 01, which is resolved, is extended in two small ways. First, the new section is also pointed at from `## What is in front of the human, and when` and from two checker sentences that node 01's list did not name. Second, the no-flag rule for an amendment that settles a fix to the manager's own clause also covers one made before the claim. Node 01's text supports this: "For an amendment the manager settles this way". Nothing contradicts node 01 or node 02.

*Manager's note:* at node 07's gate the human also narrowed the list of the manager's choices to the principle "A choice is yours when you made it", and amended node 07's clause 1c to match.
