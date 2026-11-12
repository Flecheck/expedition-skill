# Write the rule for explaining what an agent wrote

Type: implementation
Status: resolved
Deliverable: explain-a-relayed-question

## Question

*Proposed by the worker of [node 03](03-the-managers-explanation-of-a-relayed-question.md), as it wrote it:* This lets the human ask the manager to explain a worker's question, a flag or a checker's finding without the manager adding claims the agent never made, the failure GitHub issue 1 reports in its example 7. It also tells workers what to do when a reply asks them to explain instead of answering. The work writes the rule into the manager contract and adds one row to three worker contracts.

## Acceptance condition

*Written by the worker of node 03, filed by the manager:*

1. `.claude/skills/expedition/SKILL.md` has a new subsection headed `### When the human asks you to explain what an agent wrote`, inside `## What is in front of the human, and when`, placed directly before the heading `### Picking the next node`. In words the worker chooses, it states all of the following:
   a. It applies when the human asks the manager to explain something an agent wrote, such as a relayed question, a flag or a checker's finding.
   b. What the agent meant belongs to that agent.
   c. The manager may quote the agent's own words, and passages of the files the workflow ships, of the effort's record, or of the human's own words. Each quote says where it comes from.
   d. The manager adds no claim of its own: no reading of what the agent meant, no example it made up, and no conclusion drawn from what it quoted.
   e. The manager may open a file the workflow ships, or the effort's record, to find a passage to quote. It reads no code and runs nothing in order to explain.
   f. Where no quote answers the request, the manager sends the human's words to the agent that wrote the text, and relays what that agent hands back.
   The subsection states the rule as a principle. It gives no list of steps for particular cases.
2. ~~In `.claude/skills/expedition-grilling/SKILL.md`, the table under `### When the answer is not an answer` gains one row. Its left cell says the human asks you to explain something. Its right cell says: explain it in your next payload's `SO FAR`, then ask the same question again under its number.~~ *(superseded by amendment 1, below)*
3. In `.claude/skills/expedition-precondition/SKILL.md` and in `.claude/skills/expedition-prototype/SKILL.md`, the table under `### When the answer is not an answer` gains one row. Its left cell says the human asks you to explain something. Its right cell says: explain it in the `SO FAR` of the question you hand back next, then ask the same question again.
4. Nothing else under `.claude/` changes. In particular, all of the following are unchanged: in `.claude/skills/expedition/SKILL.md`, `### Two things the human can say that are not answers`, `## What is never yours`, and every paragraph of `## What is in front of the human, and when` that stands before the subsection `### The last line of a report`; `.claude/skills/expedition/glossary.md`; the paragraph that opens each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-prototype/SKILL.md`; `.claude/skills/expedition-implementation/SKILL.md`; `.claude/skills/expedition-checker/SKILL.md`; and `.claude/rules/expedition-triggers.md`.

Scope: this scope came from no search. The named sections are the work itself, and none of them is an instance of a defect.

### Amendment 1 — by the human, at gate 1, filed by the manager

What fixed the words: the human's answer to checker run 1's question, recorded under `## Review`: "yes for "under its number, if it has one"". Clause 2 now reads:

2. In `.claude/skills/expedition-grilling/SKILL.md`, the table under `### When the answer is not an answer` gains one row. Its left cell says the human asks you to explain something. Its right cell says: explain it in your next payload's `SO FAR`, then ask the same question again under its number, if it has one.

*Manager's note:* the human's own amendment carries no flag.

## Answer

The worker's answer, as it wrote it (in full under `## Handover, attempt 1`), with its correction: the manager contract now holds the rule for what the manager says when the human asks it to explain something an agent wrote, in a new subsection `### When the human asks you to explain what an agent wrote`, inside `## What is in front of the human, and when`, between `### The last line of a report` and `### Picking the next node`. The manager answers with quotes and their sources, adds no claim of its own, may open a shipped file or the record to find a quote, and sends what needs the agent's meaning to that agent. The grilling, precondition and prototype contracts each gain an `explain X` row under `### When the answer is not an answer`. After correction round 1, the grilling row reads "explain it in your next payload's `SO FAR`, then ask the same question again under its number, if it has one".

*Manager's note:* this paragraph assembles the worker's own sentences. Landed on the deliverable branch `explain-a-relayed-question`, the gate taken under standing yes 1 after the human's correction. The branch is not pushed.

## Flags

`09.1` `ASSUMPTION` **· settled** — I wrote the new row's left cell as `explain X`, the shape of the existing row `go read X first`, rather than a sentence describing the request. The condition asks only that the left cell "says the human asks you to explain something". A cell in the column headed "the human says" that reads `explain X` does that, in the same style as the rows around it. Node 03's payload proposed the same text, "explain X".

## Handover, attempt 1

The worker's handover, as it wrote it, with its `FLAGS` filed under `## Flags` above:

```
ANSWER:        The manager contract now holds the rule for what the manager says when the human asks it to explain something an agent wrote. Three worker contracts gain a reply row for a request to explain.

               The manager's rule. A new subsection, `### When the human asks you to explain what an agent wrote`, is in `.claude/skills/expedition/SKILL.md`. It sits inside `## What is in front of the human, and when`, between `### The last line of a report` and `### Picking the next node`. It is written as a principle in five short paragraphs, with no steps for particular cases:
               - The rule covers anything an agent wrote, such as a relayed question, a flag or a checker's finding. What the agent meant belongs to that agent.
               - The manager answers with quotes. It may quote the agent, the files the workflow ships, the effort's record, or the human's own words, and it says where each quote comes from.
               - The manager adds no claim of its own: no reading of what the agent meant, no example it made up, and no conclusion drawn from what it quoted. One clause gives the reason: a quote with its source can be checked, and a claim of the manager's cannot.
               - The manager may open a shipped file or a file of the record to find a passage to quote. It reads no code and runs nothing in order to explain.
               - Where no quote answers the request, the manager sends the human's words to the agent that wrote the text, then relays what that agent hands back.

               The worker rows. Each table under `### When the answer is not an answer` gains one row, with `explain X` as its left cell. This matches the table's existing `go read X first`.
               - Grilling contract, right cell: "explain it in your next payload's `SO FAR`, then ask the same question again under its number".
               - Precondition and prototype contracts, right cell: "explain it in the `SO FAR` of the question you hand back next, then ask the same question again".
               The implementation contract, the checker contract, the glossary, the trigger file and every other part of `SKILL.md` are unchanged.

               Trigger file. The new rule is not a trigger-duty, and it is not the priority, so `.claude/rules/expedition-triggers.md` does not change.

INDEX LINE:    The manager contract gains a subsection: to explain what an agent wrote, the manager quotes with sources, adds no claim, and sends meaning questions to the agent. Three worker contracts gain an "explain X" row.

NEW NODES:     none

INVALIDATIONS: none. This lands what node 03 decided, as node 03 decided it. Node 03 already wrote the note that this rule and node 01's "reads nothing and runs nothing" cover opposite directions. That note still holds.

CONDITIONS:    What I searched for. In the open and claimed nodes (05, 06, 07, 08), and in the resolved nodes 01 and 02 and the superseded node 04: `When the answer is not an answer`, `Picking the next node`, `The last line of a report`, `explain`, `Manager note`, `answers nothing itself`, `reads nothing`, and the paths of the three worker contracts. What matched. Node 07's condition and handover name the three worker contracts, but only for their opening paragraphs. Node 07 also edits the **Relay** entry, which holds "answers nothing itself". Both are separate from these lines. Node 05's "explain" hit is about a different rule. Node 02's hit is the human's own words in its interview. Result. No clause needs replacing, and no open node's question changes. Overlap check. I applied node 07's current worktree diff (against `d49b11e`) on top of this work in a scratch copy, and it applied cleanly.

MISSING FROM MAP: none. The map now lists the deliverables and their nodes, which node 03 had found missing.

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched (all in worktree `.scratch/manager-own-choices/worktrees/09-explain-rule`):
               - `.claude/skills/expedition/SKILL.md` (+18 lines)
               - `.claude/skills/expedition-grilling/SKILL.md` (+1 row)
               - `.claude/skills/expedition-precondition/SKILL.md` (+1 row)
               - `.claude/skills/expedition-prototype/SKILL.md` (+1 row)
               Nothing else changed. No file was moved, and no other node is written against an older form of these files. Node 07 edits other lines of the same files, and its diff applies cleanly together with this one.
               The bar. The root `CLAUDE.md` `## Commands` states there is no build, no tests, no formatter and no CI. The repository has no manifest or script that says otherwise, so the record in `map-implementation-rules.md` matches. No command was run. The work is held to the condition and the standards: `/writing-for-agents`: the rule is stated positively, with the one prohibition placed beside "Answer with quotes". Glossary `_Avoid_` lines: none of the refused words is used for its refused concept. The writing rules in the root `CLAUDE.md`.
               Method-skill parts skipped: none.
               Proposed commit message:
                 Explain what an agent wrote: quote with sources, add no claim

                 The manager contract gains a subsection under "What is in front of the
                 human, and when": asked to explain something an agent wrote, the manager
                 answers only with quotes and their sources, adds no claim of its own, and
                 sends what needs the agent's meaning back to that agent. The grilling,
                 precondition and prototype contracts each gain an "explain X" row in
                 "When the answer is not an answer".

                 Node: manager-own-choices/09
```

## Review

### Checker run 1 — `PASS`, with a question

The checker's entry, as it wrote it:

```
PASS

1. Condition 1, subsection placement. `grep -n '^#' .claude/skills/expedition/SKILL.md` lists `## What is in front of the human, and when` at 643, `### The last line of a report` at 708, `### When the human asks you to explain what an agent wrote` at 722, and `### Picking the next node` at 740. No heading comes between the new one and `### Picking the next node`, so the subsection sits directly before it, inside the right section.
   - a. Met by the sentence "This rule applies when the human asks you to explain something an agent wrote, such as a relayed question, a flag or a checker's finding." (read in `git diff`).
   - b. Met by "What the agent meant belongs to that agent."
   - c. Met by "You may quote the agent's own words. You may also quote passages of the files the workflow ships, of the effort's record, or of the human's own words. Say where each quote comes from."
   - d. Met by "Add no claim of your own beside the quotes. That rules out a reading of what the agent meant, an example you made up, and a conclusion you draw from what you quoted."
   - e. Met by "To find a passage to quote, you may open a file the workflow ships or a file of the effort's record. Read no code and run nothing in order to explain."
   - f. Met by "Where no quote answers the request, send the human's words to the agent that wrote the text. Then relay what that agent hands back."
   - Principle form: the subsection is five short paragraphs of prose with no list of steps and no per-case breakdown (read in the diff).
2. Condition 2. `grep -n 'When the answer is not an answer' -A14` on `expedition-grilling/SKILL.md` shows that the diff adds exactly one row: `| explain X | explain it in your next payload's \`SO FAR\`, then ask the same question again under its number |`.
3. Condition 3. The same grep on the precondition and prototype contracts shows one added row in each: `| explain X | explain it in the \`SO FAR\` of the question you hand back next, then ask the same question again |`.
4. Condition 4.
   - `git status --porcelain --ignored .claude` and `git diff --stat` show only the four listed files changed (21 insertions, 0 deletions), with nothing untracked under `.claude/`.
   - The diff has one hunk per file, and each is a pure insertion at the places above. So `glossary.md`, `expedition-implementation/SKILL.md`, `expedition-checker/SKILL.md` and `.claude/rules/expedition-triggers.md` are unchanged.
   - In `expedition/SKILL.md`, `### Two things the human can say that are not answers`, `## What is never yours`, and the paragraphs that stand before `### The last line of a report` are unchanged. So are the opening paragraphs of the three worker contracts.

The bar:
- Commands: the root `CLAUDE.md` `## Commands` states the repository has no build, tests, formatter or CI. I confirmed this with `ls -a` of the worktree and a `find` for `package.json`, `Makefile`, `*.toml` and `flake.nix`, which found nothing. No command was run, and the bar rests on the standards below.
- Standards file: I read only the standards in `.scratch/manager-own-choices/map-implementation-rules.md`.
- `/coding-principles` and `/naming`: these have little to apply to prose rows. The new heading names its case plainly.
- Glossary `_Avoid_` lines: checked by hand. "payload" is refused only for a handover, and the grilling row uses it for the grilling payload, which the glossary defines. "question" is used in its ordinary sense. No distinctive refused word appears.
- `graph-conventions.md`: no map or graph file changed, so it does not bear on this work.
- `/writing-for-agents` (read from the `mattpocock-skills` plugin) and the root `CLAUDE.md` rules for writing:
  - The two prohibitions each sit beside a positive: "Answer with quotes" and "you may open a file …".
  - The new text cites no line numbers.
  - The new text duplicates no other heading.
  - The why-sentence is short.
- Trigger file: the change edits no governing statement of a trigger-duty or of the priority. I compared it against `.claude/rules/expedition-triggers.md`, so that file did not need to change.
- Ground rule 3: workers still reach the human only through `SO FAR` in what they hand back.

QUESTIONS:
- The wording "then ask the same question again under its number" was dictated by condition 2, so it was not the worker's to depart from. It leaves the single-question case undefined. `expedition-grilling/SKILL.md`, under `### question — you need the human`, says: "For one question, use the shape below and leave the question unnumbered". A lone question has no number to ask it under, so the row says nothing on how to ask it again.
  - Instances: the new row in `.claude/skills/expedition-grilling/SKILL.md`, under `### When the answer is not an answer`. Found by `grep -n 'unnumbered\|under its number'` on that file.
  - Form: a row in a worker's "not an answer" table that refers to a question's number, in a contract whose single-question payload is unnumbered.
  - Extent: `grep -n 'its number' .claude/skills/expedition-*/SKILL.md`. Only the grilling contract numbers its questions.
  - Should the row read "under its number, if it has one", or is the current wording intended?

Flags: `09.1` is true. The left cell reads `explain X` in all three files, checked with `grep -n '| explain X |' .claude/skills/expedition-*/SKILL.md`.
```

### The human at gate 1, 2026-11-12 — `verbatim`

*"the proposed corection seems good to me"*

*Manager's note:* it is unclear whether this answers node 09's checker question ("under its number, if it has one") or node 07's raise (the three-sentence paragraph), which the manager's previous message also showed. Recorded here, where the live item is, and the manager asked which. No gate outcome yet.

### The human at gate 1, 2026-11-12 — `verbatim`

*"`The wording "then ask the same question again under its number" was dictated by condition 2` -> who wrote this condition?"*

*Manager's note:* the manager answered with quotes from node 09's condition heading and from node 03's payload 1 Q2 and the human's answer to it. No gate outcome yet.

### Gate 1 — correct

The human's words, 2026-11-12, `verbatim`:

*"yes for "under its number, if it has one""*

The option this takes, from checker run 1's question, as the checker wrote it: "Should the row read "under its number, if it has one", or is the current wording intended?"

### Correction round 1

The human's words are under `### Gate 1 — correct` above. Passed to the worker with the amended clause 2.

#### What the worker changed in correction round 1, as it wrote it

```
I made the correction. The grilling row now matches the amended clause 2 word for word. Nothing is committed.

What I changed. In `.claude/skills/expedition-grilling/SKILL.md`, in the new row of the table under `### When the answer is not an answer`, the right cell now ends "under its number, if it has one". It now reads: "explain it in your next payload's `SO FAR`, then ask the same question again under its number, if it has one". Nothing else changed.

Whether it touched something the condition names. Yes. The edit is the row named by clause 2, which the human amended. Clauses 1, 3 and 4 are untouched. The precondition and prototype rows never mentioned a number, so they stay as they were.

Paths touched in this round: `.claude/skills/expedition-grilling/SKILL.md` only. The paths touched over the whole node are still these four: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`.

Change to my flags: none. The one `ASSUMPTION` flag, which explains the `explain X` left cell, stands unchanged.

The bar: this repository has no build, tests or formatter, so there was nothing to run. The added clause is plain English and uses none of the words the glossary refuses.

Proposed commit message:
  Explain what an agent wrote: quote with sources, add no claim

  The manager contract gains a subsection under "What is in front of the
  human, and when": asked to explain something an agent wrote, the manager
  answers only with quotes and their sources, adds no claim of its own, and
  sends what needs the agent's meaning back to that agent. The grilling,
  precondition and prototype contracts each gain an "explain X" row in
  "When the answer is not an answer"; the grilling row re-asks the question
  under its number, if it has one.

  Node: manager-own-choices/09
```

### Checker run 2 — `PASS`

The checker's entry, as it wrote it:

```
PASS on all four clauses of the amended condition, and the bar holds. My earlier question is settled by the amendment, and nothing new needs your attention.

What changed since my last outcome. Only `.claude/skills/expedition-grilling/SKILL.md` was touched again, which matches the worker's account.
- Every other file under `.claude/skills/` has a modification time from before the correction.
- `git diff --stat` again shows the same four files with 21 insertions and no deletions.
- The `explain X` lines in the precondition and prototype contracts read exactly as before (`grep -n 'explain X' .claude/skills/expedition-*/SKILL.md`).
- I printed the added lines of the manager file's hunk with `git diff .claude/skills/expedition/SKILL.md | grep '^+'`. They are word for word the subsection I checked last time.

Clause 2, checked again against the amended words. The `git diff` of the grilling contract adds exactly one row under `### When the answer is not an answer`:
`| explain X | explain it in your next payload's \`SO FAR\`, then ask the same question again under its number, if it has one |`
- The left cell says the human asks you to explain something.
- The right cell matches the amended wording.

Clauses 1, 3 and 4. The amendment does not touch them, and the work under them did not move, so they stand as I established them last time.
- Clause 1: the subsection is still placed directly before `### Picking the next node`, and it still states parts a to f as a principle.
- Clause 3: the precondition and prototype rows are unchanged.
- Clause 4: `git status --porcelain --ignored .claude` shows only the four listed files modified and nothing untracked. Every addition is a pure insertion, so every section the clause names is unchanged.

The bar. I ran it again in full.
- Commands: none exist. The root `CLAUDE.md` `## Commands` says there is no build, no tests, no formatter and no CI, and the worktree still holds no build manifest.
- The standards have not changed since I last read them: I read `.scratch/manager-own-choices/map-implementation-rules.md` again, and its text is the same as before. I read only the standards in it. The main checkout is still at `d49b11e`, with no change to `CLAUDE.md` or `.claude/`. In the worktree, the glossary, `graph-conventions.md` and the root `CLAUDE.md` are unmodified. `/writing-for-agents` comes from an immutable `/nix/store` path, so it cannot have changed.
- Against the new wording: the added clause ", if it has one" uses no word the glossary's `_Avoid_` lines refuse, and breaks none of the root `CLAUDE.md` rules for writing. It also matches the grilling contract, which leaves a lone question unnumbered.
- Trigger file: no trigger-duty or priority statement was touched, so `.claude/rules/expedition-triggers.md` did not need to change.

Flags. `09.1` is still true. The left cell reads `explain X` in all three files (`grep -n '| explain X |' .claude/skills/expedition-*/SKILL.md`).
```

### Gate 2 — approve, `standing yes`

Taken under standing yes 1, whose scope text is, word for word: "commits on feature branches dedicated to deliverables, in the current effort". What was taken: checker run 2's `PASS`. Committed on the node's branch, and the deliverable branch `explain-a-relayed-question` is fast-forwarded to it.

## Annotation: node 10 narrows the explain rule to what the manager already holds

As the worker of [node 10](10-explain-only-from-what-the-manager-already-holds.md) wrote it: Node 09 (`09-write-the-rule-for-explaining-what-an-agent-wrote.md`): its condition clause e and its answer quote the replaced sentence. That clause no longer describes the shipped text. Its other clauses still hold, and the fall-back to the agent now applies whenever nothing already in context answers.

## Annotation: node 11 lets the manager explain in its own words

As the worker of [node 11](11-explain-in-own-words-without-inventing.md) wrote it: Node 09: its "quotes with sources, adds no claim" subsection is replaced. Its three "explain X" worker rows are unchanged.
