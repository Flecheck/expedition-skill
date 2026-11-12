# Let the manager explain in its own words, stating only what it holds

Type: implementation
Status: resolved
Deliverable: explain-a-relayed-question

## Question

*Written by the manager.* This lets the human get the clearer, more basic explanation they ask for when a relayed question lacks the context to answer it, while keeping the manager from stating things it does not hold. It revises [node 03](03-the-managers-explanation-of-a-relayed-question.md)'s answer, as landed by [node 09](09-write-the-rule-for-explaining-what-an-agent-wrote.md) and narrowed by [node 10](10-explain-only-from-what-the-manager-already-holds.md), on pull request #4.

The human, `verbatim`, 2026-11-12, after the manager showed how it would explain under the rule at `4fca813`: *"I think this favors quoting too much. The human will ask this when they think a question is not worded in such a way that they have enough context to answer it and they want a more basic explanation.

Right now, the form under which the agent, you, the manager, typically behaves when I ask for this is quite good. It gives an answer that is very much clearer and typically has the extra context.

The main issue we had here was just that it invented stuff because it did not have the context of the underlying agent. So the main issue was really the assumption side of things, but not the way it formulates."*

## Acceptance condition

*Written by the manager.* Scope: the named place is the work, and the scope came from no search. The one file this work may change is `.claude/skills/expedition/SKILL.md`, on the deliverable branch `explain-a-relayed-question`. Any other file found to need a change is reported, not edited.

1. In `.claude/skills/expedition/SKILL.md`, the subsection `### When the human asks you to explain what an agent wrote` lets the manager explain in its own words, and add context, to make what the agent wrote clearer to the human.
2. The subsection no longer requires the manager to answer with quotes only, and no longer forbids an explanation in the manager's own words.
3. The subsection says that the manager states only what it already holds in its context, drawn from the agent's own text, the files the workflow ships, the effort's record, or the human's own words. It says that the manager does not state as fact what the agent meant, or anything else, where it does not hold it.
4. The subsection still says that the manager opens no file and runs nothing in order to explain.
5. The subsection still says that where the explanation needs something the manager does not hold, such as the agent's own reasoning, the manager sends the human's words to the agent that wrote the text, and relays what that agent hands back.
6. The subsection still says what the rule applies to: the human asking the manager to explain something an agent wrote, such as a relayed question, a flag or a checker's finding.
7. No other part of `.claude/skills/expedition/SKILL.md` changes, and no other file under `.claude/` changes. In particular, the `explain X` rows of the grilling, precondition and prototype contracts are unchanged.

*Manager's note, reading the condition back against `### Acceptance condition` under `## The node file` in `graph-conventions.md`:* it is self-contained and states what must be true in its own words; its one path is relative to the repository root; it states that its scope came from no search, because the named place is the work; it makes no demand about the record as a whole; and every demand is fixed by the human's words above, by node 10's answer (clause 4), or by the subsection's text at `4fca813` (clauses 5 and 6). It leaves out what the human did not settle, such as whether an illustrative example is allowed, for the worker to word.

## Answer

The worker's answer, as it wrote it (in full under `## Handover, attempt 1`): the subsection `### When the human asks you to explain what an agent wrote` no longer requires quotes and no longer forbids claims of the manager's own. Its first paragraph is unchanged. Its body reads: "Explain in your own words, and add the context that makes the text clear to the human." "State as fact only what you already hold in your context, drawn from the agent's own text, the files the workflow ships, the effort's record, or the human's own words. Where you do not hold something, such as what the agent meant by a phrase its text leaves unexplained, do not state it." "Open no file and run nothing in order to explain." "Where the explanation needs something you do not hold, such as the agent's own reasoning, send the human's words to the agent that wrote the text. Then relay what that agent hands back. That agent already holds the answer."

*Manager's note:* landed on the deliverable branch `explain-a-relayed-question`, pull request #4, as a commit of its own; the gate taken under standing yes 1. The branch is not pushed.

## Flags

`11.1` `ASSUMPTION` **· settled** — I kept the opening sentence "What the agent meant belongs to that agent" and dropped the old ban on a made-up example and on a drawn conclusion. My grounds: the condition leaves the example question to the worker, and the human's complaint was only about stating what the manager does not hold. The single "State as fact only what you already hold" sentence covers that failure. Naming examples or conclusions again would bring back the bias toward quoting that the human rejected.

## Handover, attempt 1

The worker's handover, as it wrote it, with its `FLAGS` filed under `## Flags` above:

```
ANSWER:        In `.claude/skills/expedition/SKILL.md`, the subsection `### When the human asks you to
               explain what an agent wrote` no longer requires quotes and no longer forbids claims of
               the manager's own. Its first paragraph is unchanged. It says what the rule applies to (a
               relayed question, a flag or a checker's finding), and that what the agent meant belongs
               to that agent. Its body now reads, in order:
               "Explain in your own words, and add the context that makes the text clear to the human."
               "State as fact only what you already hold in your context, drawn from the agent's own
               text, the files the workflow ships, the effort's record, or the human's own words. Where
               you do not hold something, such as what the agent meant by a phrase its text leaves
               unexplained, do not state it."
               "Open no file and run nothing in order to explain."
               "Where the explanation needs something you do not hold, such as the agent's own
               reasoning, send the human's words to the agent that wrote the text. Then relay what that
               agent hands back. That agent already holds the answer."
               The calls inside it:
               - The limit is on what is stated as fact, not on how it is worded, as the human asked.
               - The two parts of the old ban that the human did not keep are gone: a made-up example,
                 and a conclusion drawn from the quotes. What the agent meant is still not stated
                 unless the manager holds it.
               - The trigger for sending the request back to the agent changed. It was "nothing in
                 context answers the request". It is now "the explanation needs something you do not
                 hold". The agent's own reasoning is the example.
INDEX LINE:    The manager now explains what an agent wrote in its own words, adding context, but states
               as fact only what its context holds, and otherwise asks that agent.
NEW NODES:     none
INVALIDATIONS: Node 03: contradicted on its "only quotes ... adds no claim" part. The send-back-to-the-
               agent part still stands.
               Node 09: its "quotes with sources, adds no claim" subsection is replaced. Its three
               "explain X" worker rows are unchanged.
               Node 10: narrowed. "Explain only by quoting what is already in context" becomes "state
               only what is already in context". "Opens no file" and the send-back still stand.
CONDITIONS:    Searched the open and claimed nodes' conditions and questions for "quote", "add no
               claim", "Answer with quotes" and "explain what an agent wrote". Nothing matched outside
               node 11 except node 05's unrelated quoting of the human. No replacement clauses.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none yet.
               Paths touched: .claude/skills/expedition/SKILL.md, only that subsection.
               - Clause 7: nothing else under `.claude/` changed. The "explain X" rows in the grilling,
                 precondition and prototype contracts are untouched.
               - Trigger file: the subsection is not a trigger-duty or the priority, so
                 `.claude/rules/expedition-triggers.md` needs no change.
               - No other file under `.claude/` cites this subsection's old wording.
               The bar: the root `CLAUDE.md` `## Commands` says the repository has no build, no tests,
               no formatter and no CI. That matches the record. I found no build or test files in the
               tree, so there was no command to run.
               Proposed commit message:
                 Explain in own words: state only what the manager holds, else ask the agent

                 Node: manager-own-choices/11
```

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

```
PASS

1. Part 1, explaining in its own words with added context: met. `sed -n '/^### When the human asks you to explain what an agent wrote/,/^### Picking the next node/p' .claude/skills/expedition/SKILL.md` shows the line "Explain in your own words, and add the context that makes the text clear to the human."
2. Part 2, no quotes-only rule and no ban on its own words: met. The diff (`git diff`) removes "Answer with quotes." and the whole "Add no claim of your own beside the quotes ..." paragraph. Over the subsection that `sed` printed, nothing requires quotes only or forbids the manager's own words.
3. Part 3, state only what it holds: met. The same subsection contains "State as fact only what you already hold in your context, drawn from the agent's own text, the files the workflow ships, the effort's record, or the human's own words." It also contains "Where you do not hold something, such as what the agent meant by a phrase its text leaves unexplained, do not state it." The general "something" covers both "what the agent meant" and "anything else". This sentence carries no "as fact" qualifier. The two sentences together give both halves of the part.
4. Part 4, open no file and run nothing: met. The same subsection contains "Open no file and run nothing in order to explain."
5. Part 5, send the human's words to the agent and relay its answer: met. The same subsection contains "Where the explanation needs something you do not hold, such as the agent's own reasoning, send the human's words to the agent that wrote the text. Then relay what that agent hands back."
6. Part 6, what the rule applies to: met. The opening paragraph is unchanged: "This rule applies when the human asks you to explain something an agent wrote, such as a relayed question, a flag or a checker's finding."
7. Part 7, no other change: met. `git status --porcelain --untracked-files=all` shows only ` M .claude/skills/expedition/SKILL.md`. `git diff --stat` shows 1 file, 8 lines added and 8 removed. The one hunk lies entirely between the subsection heading and `### Picking the next node`. The `explain X` rows of the grilling, precondition and prototype contracts are unchanged, because those files are not in the status output. `grep -rn 'explain X'` confirms each row is present. The heading is unchanged, so no citation of it needed updating. `grep -i explain .claude/rules/expedition-triggers.md` returns nothing, so this rule is not a trigger-duty and the trigger file needs no edit. No other file under `.claude/`, nor `README.md`, `CONTEXT.md` or `CLAUDE.md`, restates the old quote rule. The search was `grep -rn -i quote` filtered for explain, own words and answer with.

The bar:
- The root `CLAUDE.md` `## Commands` says the repository has no build, no tests, no formatter and no CI. I confirmed this against the tree: `git ls-files` outside `.claude/` and `.scratch/` lists only `.claude-plugin/plugin.json`, `.gitignore`, `CLAUDE.md`, `CONTEXT-MAP.md`, `CONTEXT.md` and `README.md`. There is no `.github/` and no build manifest. So no command was run, and the bar rests on the standards.
- I read only the standards in `/home/ten/Projects/expedition-skill/.scratch/manager-own-choices/map-implementation-rules.md`. Those standards are `/coding-principles` and `/naming`, the glossary's `_Avoid_` lines, `graph-conventions.md`, `/writing-for-agents`, the root `CLAUDE.md` writing rules, and the trigger-file rule.
- The standards that bore on this work were the following, and all hold: Glossary `_Avoid_` lines (the new text uses none of the refused words; checked by hand). The `CLAUDE.md` writing rules (the one prohibition, "do not state it", sits beside its positive statement, "State as fact only what you already hold"; pronouns have one referent each; nothing is cited by line number). `/writing-for-agents`, read from the `mattpocock-skills` plugin (the work prompts the positive behaviour, and the old ban list, which steered by negation, is gone). The trigger-file rule (it does not apply, as part 7 shows).
- These did not bear on this work: `/coding-principles` and `/naming`, because the change is prose only and introduces no new name; `graph-conventions.md`, including its mechanical checks, because the change touches no map, node or record file.

No reviewing skill is named in the standards, so none was run. I wrote no file, temporary or otherwise.

QUESTIONS:
- Flag `11.1` is true of the work, so there is nothing to report on it. The sentence "What the agent meant belongs to that agent." is still in the opening paragraph. The phrases "an example you made up" and "a conclusion you draw" do not appear in the subsection, by `grep`.
```

### Gate 1 — approve, `standing yes`

Taken under standing yes 1, whose scope text is, word for word: "commits on feature branches dedicated to deliverables, in the current effort". What was taken: checker run 1's `PASS`. Committed on the node's branch, and the deliverable branch `explain-a-relayed-question`, checked out in the main checkout for the human's review, is fast-forwarded there.

## Annotation: node 12 reduces the explain rule to what not to assume

As the worker of [node 12](12-explain-rule-says-only-what-not-to-do.md) wrote it: Node 11 (resolved): its answer's body text is replaced. The "own words, add context" sentence and the "state as fact only what you already hold ..." paragraph are gone. This contradicts the parts of node 11 that require them.
