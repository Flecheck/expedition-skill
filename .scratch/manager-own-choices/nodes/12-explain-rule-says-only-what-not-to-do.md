# The explain rule says only what not to do, and names "Q1 what" as its trigger

Type: implementation
Status: resolved
Deliverable: explain-a-relayed-question

## Question

*Written by the manager.* This keeps the manager explaining as it already does when the human asks what an agent wrote means, while stopping it from assuming what the agent intended or reasoned, and without pushing it into reading files it does not need. It revises [node 11](11-explain-in-own-words-without-inventing.md)'s landed subsection on pull request #4.

The human, `verbatim`, 2026-11-12, after node 11 landed: *"while we're at it, in that section, mention that the human writing "Q1 what" means they want to trigger this "please reexplain"
"Explain in your own words" -> we don't want "own words". We want what currently happens. No need to re-specify what the agent would already do. Just specify what it should *not* do, which is assume the intention or reasoning of the underlying agent, and to prefer asking it in that case. I think this: "State as fact only what you already hold in your context, drawn from the agent's own text, the files
the workflow ships, the effort's record" will tend to cause a lot of unnecessary systematic reads."*

## Acceptance condition

*Written by the manager.* Scope: the named place is the work, and the scope came from no search. The one file this work may change is `.claude/skills/expedition/SKILL.md`, on the deliverable branch `explain-a-relayed-question`. Any other file found to need a change is reported, not edited.

1. In `.claude/skills/expedition/SKILL.md`, the subsection `### When the human asks you to explain what an agent wrote` says that a reply from the human such as "Q1 what", naming a question and asking what it means, is a request this rule covers.
2. The subsection gives the manager no instruction on how to word an explanation. In particular, it no longer says "Explain in your own words, and add the context that makes the text clear to the human."
3. The subsection says that the manager does not assume the intention or the reasoning of the agent that wrote the text, and that where an explanation would need them, the manager prefers asking that agent: it sends the human's words to that agent and relays what the agent hands back.
4. The subsection no longer says "State as fact only what you already hold in your context, drawn from the agent's own text, the files the workflow ships, the effort's record, or the human's own words", and it lists no sources the manager is to draw an explanation from.
5. The subsection still says what the rule applies to: the human asking the manager to explain something an agent wrote, such as a relayed question, a flag or a checker's finding. ~~It still says that the manager opens no file and runs nothing in order to explain.~~ *(superseded by amendment 1, below)*
6. No other part of `.claude/skills/expedition/SKILL.md` changes, and no other file under `.claude/` changes. In particular, the `explain X` rows of the grilling, precondition and prototype contracts are unchanged.

*Manager's note, reading the condition back against `### Acceptance condition` under `## The node file` in `graph-conventions.md`:* it is self-contained and states what must be true in its own words; its one path is relative to the repository root; it states that its scope came from no search, because the named place is the work; it makes no demand about the record as a whole; and every demand is fixed by the human's words above, by node 10's answer (clause 5's "opens no file"), or by the subsection's text at `4bc3b26`. The wording is left to the worker.

### Amendment 1 — by the human, filed by the manager

What fixed the words: the human, `verbatim`, 2026-11-12, while the worker was correcting checker run 1's finding: *"For now I'd like to see how it behaves without "Open no file and run nothing in order to explain." - I'll come back with an extra fix if the issue that sourced this deliverable happens again."* Clause 5's second sentence is superseded. The amendment adds:

7. The subsection no longer says that the manager opens no file and runs nothing in order to explain.

*Manager's note:* the human's own amendment carries no flag.

## Answer

The worker's answer, as it wrote it in its last change (under `## Review`): the subsection `### When the human asks you to explain what an agent wrote` now reads in full: "This rule applies when the human asks you to explain something an agent wrote, such as a relayed question, a flag or a checker's finding. A reply such as "Q1 what", which names a question and asks what it means, is such a request." "Treat the intention and the reasoning of the agent that wrote the text as unknown to you. Where the explanation needs either, prefer asking that agent: send it the human's words, and relay what it hands back."

*Manager's note:* landed on the deliverable branch `explain-a-relayed-question`, pull request #4, as a commit of its own; the gate taken under standing yes 1, and the push under standing yes 2.

## Flags

`12.1` `ASSUMPTION` — *Manager's note: withdrawn by the worker after checker run 1; the work no longer makes this judgement.* The new explain subsection is written as a prohibition ("Do not assume the intention or the reasoning ..."). The root CLAUDE.md's writing rule 5 says to state a rule as what to do, and to use a prohibition only beside the positive. The human asked for exactly this prohibition ("Just specify what it should *not* do"), and clause 3 of the condition asks for it. The positive, "prefer asking that agent: send it the human's words, and relay what it hands back", sits in the same paragraph, as rule 5 requires.

`12.2` `ASSUMPTION` **· settled** — The subsection's sentence "What the agent meant belongs to that agent.", and the closing sentence "That agent already holds the answer.", were dropped. The condition did not name them. The first only states why, and the new prohibition already covers it. The second only states why the manager asks the agent. I dropped both to keep the rule short, as the human asked. Both edits are inside the one file the condition lists.

## Handover, attempt 1

The worker's handover, as it wrote it, with its `FLAGS` filed under `## Flags` above:

```
ANSWER:        In `.claude/skills/expedition/SKILL.md`, the subsection `### When the human asks you
               to explain what an agent wrote` now states only what the manager must not do. It
               reads in full:
               "This rule applies when the human asks you to explain something an agent wrote, such
               as a relayed question, a flag or a checker's finding. A reply such as "Q1 what", which
               names a question and asks what it means, is such a request."
               "Do not assume the intention or the reasoning of the agent that wrote the text. Where
               the explanation needs either, prefer asking that agent: send it the human's words, and
               relay what it hands back."
               "Open no file and run nothing in order to explain."
               Removed from node 11's text: "Explain in your own words, and add the context that
               makes the text clear to the human."; the paragraph "State as fact only what you
               already hold in your context, drawn from ...", which listed sources and pushed the
               manager toward reading files; "What the agent meant belongs to that agent."; and
               "That agent already holds the answer." The subsection gives no instruction on how to
               word an explanation and lists no sources. The manager therefore explains as it
               already does, within those limits. The subsection went from 11 lines of prose to 7.
               No other part of `.claude/` changed.
INDEX LINE:    The explain rule now only forbids assuming the writing agent's intention or reasoning, prefers asking that agent, names "Q1 what" as a trigger, and lists no sources.
NEW NODES:     none
INVALIDATIONS: Node 11 (resolved): its answer's body text is replaced. The "own words, add context"
               sentence and the "state as fact only what you already hold ..." paragraph are gone.
               This contradicts the parts of node 11 that require them. Node 10 (resolved): this
               narrows its "explain only by quoting what is already in its context" framing. No
               source rule remains, but "opens no file", and asking the agent otherwise, both
               stand. Node 09 / node 03: the "send meaning questions to the agent" part stands. It
               is now framed as preferring to ask where the intention or reasoning is needed.
CONDITIONS:    Searched the nodes for "explain", "own words", "already hold", "intention", "State as
               fact only", "belongs to that agent". The only open node besides this one is 05, and
               it matched only on the human's unrelated "own words"-free quote. No open node's
               condition or question changes. No replacement clauses.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none yet.
               Bar: the root CLAUDE.md `## Commands` states no build, tests, formatter or CI. This
               matches map-implementation-rules.md, so there was no command to run. The trigger file
               `.claude/rules/expedition-triggers.md` does not mention explaining, and this
               subsection is not a trigger-duty, so the trigger file does not change.
               Paths touched: .claude/skills/expedition/SKILL.md (that subsection only; 4 insertions,
               10 deletions). Clause 6: no other file under `.claude/` changed. The "explain X" rows
               of the grilling, precondition and prototype contracts are untouched.
               Proposed commit message:
                 Explain rule: forbid assuming the agent's intent or reasoning, else ask it

                 Name a reply such as "Q1 what" as a request the rule covers. Drop the
                 instruction to explain in own words, and the list of sources to state facts
                 from.

                 Node: manager-own-choices/12
```

## Review

### Checker run 1 — `FAIL`, the bar

The checker's entry, as it wrote it:

```
FAIL: the bar

Finding 1: a prohibition where the rule can be said as what to do
- Instances: the work added one sentence to `.claude/skills/expedition/SKILL.md`, under `### When the human asks you to explain what an agent wrote`: "Do not assume the intention or the reasoning of the agent that wrote the text." Two standards say how to write a rule. The root `CLAUDE.md`, `## Rules for the files under .claude/skills/`, rules for writing item 5, says: "State a rule as what to do. Use a prohibition only where the rule cannot be said as what to do, and then beside the positive." `/writing-for-agents`, under `## Leading words`, in the paragraph on Negation, says: "A prohibition earns its place only as a hard guardrail you cannot phrase positively." The sentence does sit beside a positive ("prefer asking that agent"). It fails the other test, because this rule can be said as what to do. One such wording is "Treat the intention and the reasoning of the agent that wrote the text as unknown to you." The acceptance condition (part 3) asks only that the subsection *say* the manager does not assume them. It does not ask for a prohibition, so this is the bar and not the condition.
- Form: a sentence the work added under `.claude/skills/` that states a rule as a prohibition, where the rule can be said as what to do.
- Extent: `git diff -U0 -- .claude/skills/expedition/SKILL.md | grep '^+[^+]' | grep -nE "\b([Dd]o not|[Dd]on't|[Nn]ever|[Nn]o)\b"`, run in the worktree. It lists every line the work added, and only those. Today it returns the one line above. "Open no file and run nothing in order to explain" is a prohibition too, but the work did not write it, and part 5 requires it to stay unchanged.

The acceptance condition: met on every part
I joined `SKILL.md`'s lines into one string and counted each phrase with `grep -o -F … | wc -l`.
1. `"Q1 what"` occurs once, in "A reply such as "Q1 what", which names a question and asks what it means, is such a request." Met.
2. "Explain in your own words" and "add the context that makes" occur 0 times. Reading the 4-line subsection, no other sentence says how to word an explanation. Met.
3. "Do not assume the intention or the reasoning of the agent that wrote the text" occurs once. "prefer asking that agent: send it the human" occurs once, and "relay what it hands back" occurs once. Met.
4. "State as fact only", "drawn from the agent" and "files the workflow ships" occur 0 times. Reading the subsection, it lists no sources. Met.
5. "such as a relayed question, a flag or a checker" occurs once, and "Open no file and run nothing in order to explain" occurs once. Met.
6. `git status --porcelain --untracked-files=all` and `git diff 4bc3b26 --stat -- .claude` list only `.claude/skills/expedition/SKILL.md`. `git diff -U0` shows three hunks (`@@ -725`, `@@ -727,5`, `@@ -735,4`), all inside this subsection. The `explain X` rows of the grilling, precondition and prototype contracts are unchanged, which `grep -rn "explain X"` confirms. Met.

The bar's commands
- The root `CLAUDE.md` `## Commands` states there is no build, no tests, no formatter and no CI. The worktree root agrees: it holds no build manifest, no `.github`, and nothing that runs tests. I ran no commands, because there are none, so the bar reduces to the standards.

Standards read, and which bore on this work
- I read only the standards in `.scratch/manager-own-choices/map-implementation-rules.md`, and nothing else in that directory.
- `/coding-principles` and `/naming` did not bear: the work adds no code and names nothing new.
- The glossary's `_Avoid_` lines bore. I checked the added words by hand. "question" and "asking" are used in their ordinary sense here, and neither is the refused concept (grilling, or a raise). No breach.
- `graph-conventions.md` did not bear on a prose edit to SKILL.md.
- `/writing-for-agents` bore. I found it by name in the `mattpocock-skills` plugin. Its Negation paragraph gives Finding 1.
- The rules for writing in the root `CLAUDE.md` bore. Item 5 gives Finding 1. Pronoun referents ("either", "it") are clear, and the work cites no headings or line numbers.
- The trigger-file rule did not bear. `.claude/rules/expedition-triggers.md` has no "explain" entry, and this subsection is not a trigger-duty or the priority.
- No standard names a reviewing skill, so I ran none.

QUESTIONS:
- None about the condition.

Flags, checked after the outcome
- `12.1` is true of the work: the subsection holds the prohibition "Do not assume the intention or the reasoning ...". That sentence is the subject of Finding 1.
- `12.2` is true of the work: "belongs to that agent" and "already holds the answer" each occur 0 times in the joined file.

I wrote no temporary files.
```

### The worker's fix after checker run 1

What the worker changed for the finding, as it wrote it:

```
I fixed the checker's Finding 1. The rule against assuming is no longer worded as a prohibition, and nothing is committed.

What changed for the finding. In `### When the human asks you to explain what an agent wrote`, the sentence "Do not assume the intention or the reasoning of the agent that wrote the text." is gone. It now reads "Treat the intention and the reasoning of the agent that wrote the text as unknown to you." That is the checker's own suggested wording. The sentence after it is unchanged, apart from where its lines wrap: "Where the explanation needs either, prefer asking that agent: send it the human's words, and relay what it hands back." The subsection now has no prohibition in it.

Whether it touched what the condition names. Yes, clause 3: the subsection must say the manager does not assume the agent's intention or reasoning, and prefers asking that agent. Treating both as unknown says the manager does not assume them. The checker agreed that this wording meets clause 3. The rest of clause 3 is unchanged.

I first tried adding ", and assume neither" so the sentence would match clause 3 word for word. I dropped it because it puts a prohibition back in.

Paths touched: `.claude/skills/expedition/SKILL.md`, that subsection only (5 insertions, 10 deletions against `4bc3b26`). Nothing else under `.claude/` changed.

Change to my flags. The first ASSUMPTION flag, which defended the prohibition under writing rule 5, is withdrawn. The second one stands unchanged.

Answer and index line, updated. The subsection's second paragraph now reads: "Treat the intention and the reasoning of the agent that wrote the text as unknown to you. Where the explanation needs either, prefer asking that agent: send it the human's words, and relay what it hands back." New index line: "The explain rule now treats the writing agent's intention and reasoning as unknown, prefers asking that agent, names "Q1 what" as a trigger, and lists no sources."

Proposed commit message:
  Explain rule: treat the agent's intent and reasoning as unknown, else ask it

  Name a reply such as "Q1 what" as a request the rule covers. Drop the
  instruction to explain in own words, and the list of sources to state facts
  from.

  Node: manager-own-choices/12
```

### The worker's change for the human's amendment 1

What the worker changed, as it wrote it:

```
I removed "Open no file and run nothing in order to explain." from the subsection, as the human asked. The checker's finding stays fixed. Nothing is committed.

What changed. In `### When the human asks you to explain what an agent wrote`, the sentence "Open no file and run nothing in order to explain." is gone. The subsection now has two paragraphs. The first says what the rule applies to, including a reply such as "Q1 what". The second treats the writing agent's intention and reasoning as unknown, and prefers asking that agent.

I searched `.claude/` for "open no file", "opens no file", "run nothing" and "explain X". Nothing else refers to the sentence. The three `explain X` rows in the worker contracts tell the worker what to do and say nothing about the manager.

Clauses this correction touched:
- Clause 5: now only its first sentence binds, and it still holds. The subsection still says the rule covers explaining something an agent wrote, such as a relayed question, a flag or a checker's finding.
- Clause 7 (new): met. The subsection no longer says the manager opens no file and runs nothing in order to explain.
- Clause 3: touched by the earlier fix for the checker's finding, and still met.
- Clause 6: still met. No other part of `SKILL.md` and no other file under `.claude/` changed.

Paths touched: `.claude/skills/expedition/SKILL.md`, that subsection only (5 insertions, 12 deletions against `4bc3b26`).

Flags. The flag about the prohibition is still withdrawn. The other ASSUMPTION flag stands unchanged.

Answer, updated. The subsection now reads in full:
- "This rule applies when the human asks you to explain something an agent wrote, such as a relayed question, a flag or a checker's finding. A reply such as "Q1 what", which names a question and asks what it means, is such a request."
- "Treat the intention and the reasoning of the agent that wrote the text as unknown to you. Where the explanation needs either, prefer asking that agent: send it the human's words, and relay what it hands back."

Index line, updated: "The explain rule now only treats the writing agent's intention and reasoning as unknown and prefers asking it, names "Q1 what" as a trigger, and lists no sources or file ban."

Invalidations, updated. Node 10's "opens no file" is now removed as well, which contradicts that part of node 10's answer.

Proposed commit message:
  Explain rule: treat the agent's intent and reasoning as unknown, else ask it

  Name a reply such as "Q1 what" as a request the rule covers. Drop the
  instruction to explain in own words, the list of sources to state facts
  from, and the ban on opening files to explain.

  Node: manager-own-choices/12
```

### Checker run 2 — `PASS`

The checker's entry, as it wrote it:

```
PASS

Scope of this check. This re-check covers the corrected work and the amended condition. I checked the corrected work against the diff itself, not against the worker's account of it. The diff now shows two hunks (`@@ -725`, `@@ -727,11`), both inside `### When the human asks you to explain what an agent wrote`. The changes the worker named are the whole of the change, and no other edit appears.

Acceptance condition (the amended text), one line per part. I joined `SKILL.md`'s lines into one string and counted each phrase with `grep -o -F … | wc -l`.
1. `"Q1 what"` occurs once, in "A reply such as "Q1 what", which names a question and asks what it means, is such a request." The amendment did not touch this part and the work did not change it, so my first-run result stands.
2. "Explain in your own words" and "add the context that makes" each occur 0 times. Reading the subsection, now 3 sentences, finds nothing that says how to word an explanation. Met.
3. Re-established, because the work changed. "Treat the intention and the reasoning of the agent that wrote the text as unknown to you" occurs once, which says the manager does not assume them. "prefer asking that agent: send it the human" occurs once, and "relay what it hands back" occurs once. Met.
4. "State as fact only", "drawn from the agent" and "files the workflow ships" each occur 0 times. Reading the subsection, it lists no sources. Met.
5. Re-established against the amended text, which keeps only the first sentence of this clause. "such as a relayed question, a flag or a checker" occurs once. Met.
6. `git status --porcelain --untracked-files=all` and `git diff 4bc3b26 --stat -- .claude` list only `.claude/skills/expedition/SKILL.md`. Both diff hunks fall inside the subsection. The `explain X` rows of the grilling, precondition and prototype contracts are in files the work did not touch. Met.
7. New clause. "Open no file" and "run nothing in order to explain" each occur 0 times. Met.

The bar. I re-ran it in full.
- Commands. The root `CLAUDE.md` `## Commands` states there is no build, no tests, no formatter and no CI, and the worktree root agrees. There is nothing to run.
- Finding 1 from the first run is resolved. I listed the prohibitions among the added lines with `git diff -U0 -- .claude/skills/expedition/SKILL.md | grep '^+[^+]' | grep -nE "\b([Dd]o not|[Dd]on't|[Nn]ever|[Nn]o)\b"`. It now returns nothing. The rule is now stated as what to do.
- Glossary `_Avoid_` lines. The added words were checked by hand again. No refused word appears in its refused sense.
- Rules for writing. Each pronoun has one clear referent ("either" means the intention or the reasoning, and "it" means that agent). Nothing is cited by line number.
- Trigger file. The subsection is not a trigger-duty or the priority, so the trigger-file rule still does not bear.

The standards have not changed since my first read. `map-implementation-rules.md` was last modified 2026-11-11 23:48, which is before my first read. The work did not touch the root `CLAUDE.md`, `glossary.md` or `graph-conventions.md`. Git status shows them unmodified in the worktree, and the main checkout has no tracked changes against `4bc3b26`. `/writing-for-agents` is in the read-only Nix store. As in the first run, I read only the standards in `map-implementation-rules.md`. No standard names a reviewing skill, so I ran none.

Flags, checked after the outcome
- `12.1` was withdrawn, so I did not check it.
- `12.2` is true of the work. "belongs to that agent" and "already holds the answer" each occur 0 times.

I wrote no temporary files.
```

### Gate 1 — approve, `standing yes`

Taken under standing yes 1, whose scope text is, word for word: "commits on feature branches dedicated to deliverables, in the current effort". What was taken: checker run 2's `PASS`. Committed on the node's branch, and the deliverable branch `explain-a-relayed-question`, checked out in the main checkout, is fast-forwarded there. Pushed under standing yes 2, whose scope text is, word for word: "pushing feature branches".
