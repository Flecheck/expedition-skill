# Explain only from what the manager already holds

Type: implementation
Status: resolved
Deliverable: explain-a-relayed-question

## Question

*Written by the manager.* This lets the human get an answer about what an agent wrote without waiting while the manager searches files for a quote, when the agent that wrote it already has the answer. It revises [node 03](03-the-managers-explanation-of-a-relayed-question.md)'s answer, as landed by [node 09](09-write-the-rule-for-explaining-what-an-agent-wrote.md) on pull request #4.

The human, `verbatim`, 2026-11-12, quoting the subsection node 09 wrote: *"relayed questions: "To find a passage to quote, you may open a file the workflow ships or a file of the effort's record. Read no code and run nothing in order to explain." -> at this point it may be faster to just hand back the question. I guess the manager answering itself is more for when it has the context directly, no?
Because if it spends 15 minutes searching for a quote
rather than just asking the agent that already has the
answer, it's gonna be a huge loss of time for nothing."*

The manager took this as the human choosing the alternative node 03's payload 1 Q1 offered, as its worker wrote it: "The recommended rule, but quoting only what is already in the manager's context and reading nothing, as the **Manager note** entry's "drawn only from context it already holds" suggests".

## Acceptance condition

*Written by the manager.* Scope: the named place is the work, and the scope came from no search. The one file this work may change is `.claude/skills/expedition/SKILL.md`, on the deliverable branch `explain-a-relayed-question`. Any other file found to need a change is reported, not edited.

1. In `.claude/skills/expedition/SKILL.md`, the subsection `### When the human asks you to explain what an agent wrote` says that the manager quotes only what is already in its own context, and that it opens no file and runs nothing in order to explain.
2. The same subsection says that where nothing already in the manager's context answers the request, the manager sends the human's words to the agent that wrote the text, and relays what that agent hands back.
3. The subsection no longer says that the manager may open a file the workflow ships, or a file of the effort's record, to find a passage to quote.
4. Every other statement of that subsection keeps its meaning: what the rule applies to, that what the agent meant belongs to that agent, which sources a quote may come from and that each quote says where it comes from, and that the manager adds no claim of its own.
5. No other part of `.claude/skills/expedition/SKILL.md` changes, and no other file under `.claude/` changes.

*Manager's note, reading the condition back against `### Acceptance condition` under `## The node file` in `graph-conventions.md`:* it is self-contained and states what must be true in its own words; its one path is relative to the repository root; it states that its scope came from no search, because the named place is the work; it makes no demand about the record as a whole; and every demand is fixed by the human's words above, by node 03's Q1 alternative they took, or by the subsection's text at `be58249`. The wording is left to the worker.

## Answer

The worker's answer, as it wrote it (in full under `## Handover, attempt 1`): the subsection `### When the human asks you to explain what an agent wrote` no longer lets the manager search for a passage to quote. Its two closing paragraphs read: "Quote only what is already in your context. Open no file and run nothing in order to explain." and "Where nothing already in your context answers the request, send the human's words to the agent that wrote the text. Then relay what that agent hands back. That agent already holds the answer." The first three paragraphs are unchanged.

*Manager's note:* landed on the deliverable branch `explain-a-relayed-question`, pull request #4, as a commit of its own; the gate taken under standing yes 1. The branch is not pushed.

## Handover, attempt 1

The worker's handover, as it wrote it:

```
ANSWER:        In `.claude/skills/expedition/SKILL.md`, the subsection `### When the human asks you to explain what an agent wrote` no longer lets the manager search for a passage to quote. Its two closing paragraphs now read:

               "Quote only what is already in your context. Open no file and run nothing in order to explain.

               Where nothing already in your context answers the request, send the human's words to the agent that wrote the text. Then relay what that agent hands back. That agent already holds the answer."

               This replaces "To find a passage to quote, you may open a file the workflow ships or a file of the effort's record. Read no code and run nothing in order to explain." and "Where no quote answers the request, …".

               The first three paragraphs are unchanged. They hold what the rule applies to, that what the agent meant belongs to that agent, which sources a quote may come from and that each quote says where it comes from, and that the manager adds no claim of its own. Read together, those sources are now narrowed to the parts already in the manager's context.

               "Read no code" is gone because "Open no file" covers it. The last sentence gives the reason in one short line, as the human's steer asked, so the rule stays shorter than before (3 insertions, 4 deletions). The node revises node 03's answer as landed by node 09: it is the alternative from node 03's payload 1 Q1, quoting only from what the manager already holds.

INDEX LINE:    The manager now explains what an agent wrote only by quoting what is already in its context, opens no file to do so, and otherwise sends the human's words to that agent.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: Node 03 (`03-the-managers-explanation-of-a-relayed-question.md`): its answer says "The manager may open a shipped file or the effort's record to find a passage to quote." This is now narrowed: the manager opens no file and quotes only what is already in its context.
               Node 09 (`09-write-the-rule-for-explaining-what-an-agent-wrote.md`): its condition clause e and its answer quote the replaced sentence. That clause no longer describes the shipped text. Its other clauses still hold, and the fall-back to the agent now applies whenever nothing already in context answers.

CONDITIONS:    I searched every node file, open and resolved, for "passage to quote", "run nothing in order", "Read no code", "open a file the workflow ships" and "explain what an agent wrote".
               - Only nodes 03 and 09, both resolved, matched on the changed sentence (see INVALIDATIONS).
               - Node 05 (open, grilling) also appeared in the search. It matches on nothing my work changes, so its question is unaffected.
               - I wrote no replacement clauses.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Path touched: `.claude/skills/expedition/SKILL.md` only, in the worktree `/home/ten/Projects/expedition-skill/.scratch/manager-own-choices/worktrees/10-explain-from-context`.
               I searched `.claude/` and `CLAUDE.md` for the replaced sentence and found no other citation of it.
               - The "explain X" rows in the three worker contracts are about what a worker does, so they are unaffected.
               - `.claude/rules/expedition-triggers.md` holds nothing on explaining, and this subsection is not a trigger-duty, so the trigger file needs no edit.
               The bar: I confirmed that the repository has no build, tests, formatter or CI. The root `CLAUDE.md` says so under `## Commands`, and the tree has no build or tooling files. So there was no command to run, and the work is held to the standards and the acceptance condition.
               No method skill was invoked, so I skipped nothing.
               Proposed commit message:
                 Explain from context only: quote what the manager holds, else ask the agent

                 Node: manager-own-choices/10
```

## Review

### Checker run 1 — `PASS`

The checker's entry, as it wrote it:

```
PASS

1. Part 1 holds. Running `awk` over the subsection (`### When the human asks you to explain what an agent wrote` up to `### Picking the next node`) in the worktree shows the sentence "Quote only what is already in your context. Open no file and run nothing in order to explain."
2. Part 2 holds. The same output shows "Where nothing already in your context answers the request, send the human's words to the agent that wrote the text. Then relay what that agent hands back."
3. Part 3 holds. In `git diff`, the old lines "To find a passage to quote, you may open a file the workflow ships or a file of the effort's record. Read no code and run nothing in order to explain." are removed. The subsection output contains no permission to open a file. "Read no code" is covered by the new "Open no file".
4. Part 4 holds. `git diff` touches only the last two paragraphs of the subsection. The paragraphs that keep these statements are byte-identical: "This rule applies when the human asks you to explain something an agent wrote…"; "What the agent meant belongs to that agent."; the quote sources: the agent's words, files the workflow ships, the effort's record, the human's words; "Say where each quote comes from."; "Add no claim of your own beside the quotes…". The sources paragraph is now limited by the new rule that a quote must already be in context, and it does not contradict it.
5. Part 5 holds. `git diff --stat` shows one file changed (3 insertions, 4 deletions), with one hunk inside the subsection. `git status --porcelain --untracked-files=all` lists only `M .claude/skills/expedition/SKILL.md`, so no untracked files were added under `.claude/`.

The condition records no search command, so I had no command to re-run.

Bar:
- Commands: the root `CLAUDE.md`, under `## Commands`, says the repository has no build, no tests, no formatter and no CI. Listing the worktree root confirmed this: there is no build manifest or CI configuration. I ran no command because there is none to run.
- Standards I read: `/home/ten/Projects/expedition-skill/.scratch/manager-own-choices/map-implementation-rules.md`, its standards only. I opened no other file in the effort's directory. The standards that bore on this work: the rules for writing in the root `CLAUDE.md` (the added sentences are plain, hold one idea each, and have one clear referent each; the prohibition "Open no file and run nothing" sits beside the positive rule "Quote only what is already in your context", as rule 5 allows); `/writing-for-agents`, read from the `mattpocock-skills` plugin (negation is paired with the positive; "In your context" is the same wording `SKILL.md` already uses elsewhere); the glossary's `_Avoid_` lines (by grep and by hand, the added text uses no refused word in a refused sense; "run" appears only in its ordinary sense); the trigger-file rule (`grep -i "explain\|quote"` over `.claude/rules/expedition-triggers.md` returns nothing, so no edit there is owed). The subsection's heading is unchanged, and `grep -rn "When the human asks you to explain" .claude/` finds only the heading itself.
- Standards that did not bear on this work: `/coding-principles` and `/naming`, because the work contains no code and no new names, and `graph-conventions.md`, because the work does not touch the graph format.

The node holds no flags, so there were no flags to check.
```

### Gate 1 — approve, `standing yes`

Taken under standing yes 1, whose scope text is, word for word: "commits on feature branches dedicated to deliverables, in the current effort". What was taken: checker run 1's `PASS`. Committed on the node's branch, and the deliverable branch `explain-a-relayed-question`, checked out in the main checkout for the human's review, is fast-forwarded there.

## Annotation: node 11 lets the manager explain in its own words

As the worker of [node 11](11-explain-in-own-words-without-inventing.md) wrote it: Node 10: narrowed. "Explain only by quoting what is already in context" becomes "state only what is already in context". "Opens no file" and the send-back still stand.

## Annotation: node 12 reduces the explain rule to what not to assume

As the worker of [node 12](12-explain-rule-says-only-what-not-to-do.md) wrote it: Node 10's "opens no file" is now removed as well, which contradicts that part of node 10's answer. Node 10 (resolved): this narrows its "explain only by quoting what is already in its context" framing. No source rule remains.
