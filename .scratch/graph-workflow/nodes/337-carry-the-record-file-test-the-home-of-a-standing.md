# Carry the record-file test, the home of a standing rule, the second supersession and starting an effort into the manager contract

Type: implementation
Status: resolved
Supersedes: 101, 105, 111, 278, 280, 287
Blocked by: ~~339~~

## Question

Nodes 101, 105, 111, 278, 280 and 287 each add or repair a few statements in the manager contract's sections on writing the graph, standing rules, what is never the manager's, its open questions and starting an effort, with small matching changes in `graph-conventions.md`. Make all their changes in one piece of work.

*Proposed by [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker and filed by the manager, on the human's "ok" to node 330's merge and its conflicts' recommendations. The worker wrote each condition to the recommended option of every conflict.* *Sequencing, from the worker's C11(a):* G2 ([node 339](339-tie-graph-conventions-mds-mechanical-checks-to-the-writes-that.md)) lands before this node.

*The worker's blockers:* none

## Acceptance condition

*Written by node 330's worker.*

> The work is `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md`, and no other file changes. No file under `.scratch/` changes. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. Both files are files the workflow ships, so they are edited plainly: superseded wording is removed, and nothing is struck through or moved to a history file.
>
> **How this scope was got.** For clauses 15 to 25, `grep -rln -i "starting an effort\|start an effort\|charting\|adoption" .claude/skills CONTEXT.md` returned no files at commit `c3ecda3`. So that work adds text rather than repairing instances of a defect. Every other place named below is the work itself, so its scope came from no search. A place this work touches outside the two files is reported and not edited.
>
> Done means every one of the following is true of the finished tree. Each clause names, in brackets, the node its demand comes from.
>
> **The record-file test**, in `SKILL.md`'s `## Writing the graph`
>
> 1. (287) The section states a test with these three branches and no fourth. The test is decided by looking at which file a change touches, taking no account of the change's content.
>    - A change to a file the workflow ships, meaning its skill files, its rules files and its glossary, is a node's work, always, whoever noticed that the file needed changing.
>    - A change confined to the files of an effort's own record, meaning its map, the siblings of its map, its history file, its decisions index, its flags index and its node files, is the manager's own. It is made with no node, no acceptance condition, no worker, no checker and no gate.
>    - Where a node of the first kind would otherwise leave the record contradicting what that node ships, the same node's worker makes the record change too, inside that node and named in that node's acceptance condition, so that both land together.
> 2. (287) The section states that the reverse of the third branch does not hold. Noticing that a record file is wrong never makes a shipped-file node, and a defect confined to the record falls in the second branch whatever produced it.
> 3. (287) The section no longer states without qualification that every procedure in `graph-conventions.md` belongs to the manager and that no worker performs one. Before this work it reads "The answer, the status, the `decisions.md` line, the flags, and every procedure in `graph-conventions.md` are yours, and no worker performs one." What stands in its place says that the procedures are the manager's except the one that changes a map file, `### Change the map`. A worker performs that one in the third branch of clause 1, and the manager performs it otherwise.
> 4. (287) The section still says that the manager's sole authorship covers recording rather than files, and that a worker whose node's own work is a change to a graph file makes that change itself. Before this work that reads "That rule covers recording only. Where a node's own work is a change to a graph file, that node's worker makes the change itself, as it would any other work." Nothing that clauses 1 to 3 add contradicts it.
> 5. (287) `graph-conventions.md`'s `### Change the map` procedure states who runs it, in the same two cases as clause 3. Its numbered steps are otherwise unchanged.
>
> **The home of a standing rule**, in `SKILL.md`'s `### Standing steering, and standing instructions of one effort`
>
> 6. (101) The section states all four of the following. Each is findable in the section as a statement rather than an implication. The wording and the order are the worker's.
>    1. A standing rule the human gives, about what to work on or about how work is done, is written into the effort's map when they state it. That is what makes it bind on that effort, and it binds nobody until it is there. This holds for rules of conduct and not only for steering about what gets worked.
>    2. The map is the ordinary home and usually the only one. On most efforts the workflow's own skill files are not modified at all, so a rule the human gives lives in the map and nowhere else, and the next effort starts without it.
>    3. A rule reaches a shipped skill file only where the human says so, and it does so as a node. The manager never carries one into a shipped file on its own judgement, including where it judges the rule to be about the workflow rather than about the effort. Where the human says nothing about a rule's scope, the rule is the effort's alone.
>    4. Every worker on an effort is bound by everything in that effort's map whatever a rule's origin. So no scope marking is owed for a worker's sake, and the map carries no per-rule scope field.
> 7. (101) The paragraph beginning "Some of what binds you on a given effort is a standing instruction of that effort's human, and not a rule of this workflow." is kept.
> 8. (101) The section cites nothing by line number: a citation to another part of the file names a heading or quotes a phrase. The section is still reachable and readable by its own heading, so a reader following a pointer to it reads that section and nothing else.
>
> **A second supersession**
>
> 9. (105) `SKILL.md` states that where the manager is about to supersede a node that is itself a replacement, it does not supersede again, and instead puts the chain to the human as a decision about the shape of the graph. It states that there is no depth counter and no budget on supersession, the chain being what makes the friction visible.
> 10. (105) Both statements sit together in an existing section of `SKILL.md` whose subject includes superseding a node, and the worker names that section in its handover. The term `revision` is used in the body of that passage.
>
> **The table of what is never the manager's**
>
> 11. (278) In `SKILL.md`'s `## What is never yours` table, the second cell of the row whose first cell is "rewriting an acceptance condition" states both of the following. Before this work that cell reads "hand it over as written; a condition that is wrong goes to the human".
>     - A condition is handed over as written, and a condition a worker already holds and judges wrong goes to the human.
>     - The one narrow exception, amending a clause of the condition of a node nobody holds yet, is stated in the file's `## Acceptance conditions` section, named by that heading and not by a line number.
> 12. (278) The table keeps every row it has, each with its first cell unchanged, in the same order, and gains no row. This work changes no other row's second cell.
>
> **The open question about looking at the record**
>
> 13. (280) Under `## What nothing here settles`, the item reading "Does anything tell a worker to look at the record when it reports what its work invalidates?" still stands as an unsettled question. It still states that the general duty over the effort's record does not exist. It also names the one bounded class where a duty to look does exist, the open nodes' acceptance conditions, and points at the section of the same file that states that duty by its heading, not by a line number.
> 14. (280) The items of that list keep the numbers and order they have when this work starts. This work removes none, and no item other than the one in clause 13 changes meaning.
>
> **Starting an effort**
>
> 15. (111) `SKILL.md` gains a section headed `## Starting an effort`, placed before its `## Closing an effort` section.
> 16. (111) That section states that an effort begins in one of two ways, told apart by their input. One takes a conversation with the human as its input. The other is adoption, whose input is a directory of work that already exists. It names the first way by its input only, and the word `charting` appears nowhere in either file. It states that both ways produce the same thing, the effort's files and its first nodes, and that they differ only in their input.
> 17. (111) That section states that the manager performs the act, and that it happens before the graph exists.
> 18. (111) That section states all six of the following as what the act establishes, and as the parts both ways share:
>     - the effort's name, which is its directory's;
>     - the destination, meaning what reaching the end of the effort looks like;
>     - whether the effort is expected to reach that destination;
>     - the map's standing preferences, the effort's ground rules where it has any, and its declaration of which sources are authoritative, which are evidence only, and which hold statements known to be false, where it has one;
>     - the label vocabulary, declared or declared to be absent;
>     - the effort's first nodes.
> 19. (111) That section states that the mechanical detail, which files the act creates and in what order, is in `graph-conventions.md` and not in the manager contract.
> 20. (111) That section states both halves of what the expectation in clause 18 governs:
>     - where the effort is expected to reach its destination, an empty frontier is the milestone that triggers the whole-graph sweep and the report that precedes a close;
>     - where it is not, an empty frontier is a surprise rather than a milestone, and that report is an exception path rather than where the effort is heading.
> 21. (111) Adoption's own steps are not written into either file. These seven stay out:
>     - taking the effort's name from a directory that already exists rather than choosing one;
>     - resolving a reserved graph name the directory is already using for something else;
>     - deriving the map from the foreign record rather than from a conversation;
>     - declaring the label vocabulary from foreign label families;
>     - appending an expedition section to a target repository's tracker doc;
>     - building the table that repoints citations inside imported material;
>     - minting a bulk import as `precondition` nodes.
> 22. (111) `graph-conventions.md` gains, under its `## Procedures` heading and in the same shape as the procedures already there, a procedure headed `### Start an effort`. It lists every file the act creates, in order: `map.md` first; then every other file listed under `## The seven files`, including the `nodes/` directory; and last the effort's first node files, by the steps under `## Adding a node`.
> 23. (111) That procedure's step for `map.md` states that its `## Destination` section says both what reaching the end of the effort looks like and whether the effort is expected to reach it.
> 24. (111) Under `## The seven files`, the description of `map.md`'s `## Destination` section, which before this work reads "`## Destination` — what reaching the end of the effort looks like.", is extended. It states that the section also says, in one line, whether the effort is expected to reach the destination. It states that where the effort is not expected to, this is where a manager reads that a non-empty frontier is that effort's steady state rather than a defect.
> 25. (111) Neither file states, in any wording, how often efforts end or fail to end.
>
> **What does not change**
>
> 26. (278, 280) `SKILL.md`'s `## Acceptance conditions` section is not changed.
> 27. (105) In `SKILL.md`'s `## What is in front of the human, and when`, the one-at-a-time rule, the two tiers and the list beginning "Three things never enter the queue:" are unchanged.
> 28. (287) Neither file states how many attempts any of this took, what it cost, who was wrong, or what a file said before. A trigger by which a reader knows a rule applies is not such a statement and may stay.
> 29. (101, 105, 111, 278, 280, 287) No section of either file is removed. No existing numbered step under `## Procedures` is reworded, renumbered or removed. No rule in either file changes its meaning other than as clauses 1 to 25 state.
> 30. The working tree meets the bar.

## Amendment, 2026-09-26 (from node 330's C11(a), by the human's answer)

*Written by [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker as the text of its conflict C11's option (a), which the human took with their "ok". That worker said its conditions were written to each recommended option, but this clause did not reach the condition above; the manager adds it, pasted as the worker wrote it. [Node 339](339-tie-graph-conventions-mds-mechanical-checks-to-the-writes-that.md)'s worker, which is writing the check steps, proposed a narrower wording of the same demand under its `NEW NODES`, naming checks 1, 3 and 4; that is not added here.*

- **A new clause, after clause 22.** "`### Start an effort` ends with a numbered step naming, by number, the checks under `## Mechanical checks` that its writes can make false, and stating that the party performing the act runs them itself at that act."

## Answer

The manager contract now holds the file test for graph edits, the map as home of standing rules, a stop on second supersession, and a Starting an effort section with its procedure.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `3c25240`. Flags 337.1 to 337.5 are settled at this gate.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Carry the record-file test, the home of a standing rule, the second supersession and starting an effort into the manager contract

ANSWER:        Built in worktree `.scratch/graph-workflow/worktrees/337-m2` (branch `worktree-337-m2`, base `968b1ec`). The change is uncommitted. Only `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md` changed.

`SKILL.md`:
- `## Writing the graph`: the first paragraph now makes every `graph-conventions.md` procedure the manager's except `### Change the map`. A worker performs that one in the third branch of the test, and the manager performs it otherwise. The paragraph "That rule covers recording only. …" is kept word for word. After it comes the file test, with three branches and no fourth, decided only by which file a change touches:
  - A change to a file the workflow ships (skill files, rules files, glossary) is a node's work, always.
  - A change confined to the graph's files (map, its siblings, history file, decisions index, flags index, node files) is the manager's own. It takes no node, no condition, no worker, no checker and no gate.
  - Where a first-branch node would otherwise leave the graph's files contradicting what it ships, that node's worker makes the record change inside the node, named in its condition.
  - A last paragraph says the third branch does not hold in reverse.
  - Call: the record side is called "the graph's files" and not "record files". The glossary (`CONTEXT.md`) defines "record" narrowly as answers, statuses, index lines and flags. "Graph file" is also the word in the kept paragraph that clause 4 protects, so the test and that paragraph share one term.
- `## What is never yours`: the "rewriting an acceptance condition" row now says a condition a worker already holds and judges wrong goes to the human. It names the one narrow exception, amending a clause of the condition of a node nobody holds yet, and points at it by the heading `## Acceptance conditions`. No other row changed.
- `### What reject means`: this is the section chosen for the second supersession (clauses 9 and 10). It is the one existing section whose subject includes superseding a node, other than `## When an agent dies or is stopped`, which node 124 is about to rewrite. The new paragraph says: where a reject or a revision would have the manager supersede a node that is itself a replacement, it does not supersede again and puts the chain to the human as a decision about the shape of the graph. There is no depth counter and no budget, and the chain itself makes the friction visible. It is written to cover a revision as well as a reject, so the rule is not read as reject-only.
- `### Standing steering, and standing instructions of one effort`: four paragraphs added after the kept paragraph "Some of what binds you …":
  - A standing rule binds only once written into the map, and is written there when stated. This holds for rules of conduct as well as steering.
  - The map is the ordinary and usually only home, and the next effort starts without the rule.
  - A rule reaches a shipped skill file only on the human's word and as a node, never on the manager's judgement, and silence means effort-only.
  - Every worker is bound by the whole map, so there is no scope marking and no scope field.
  - No line-number citations.
- `## Starting an effort` is new, placed before `## Closing an effort`. It says:
  - The manager performs the act, before the graph exists.
  - There are two ways, told apart by input: a conversation with the human, or adoption from an existing directory of work. Both produce the effort's files and first nodes, and they differ only in input.
  - The six shared things the act establishes.
  - Both halves of what the expectation governs.
  - The mechanical detail is in `graph-conventions.md`.
  - Adoption's own steps are left out, and the word `charting` appears in neither file.
- `## What nothing here settles`, item 4: still an open question, and still says no general duty over the record exists. It now names the bounded class, the open nodes' acceptance conditions, and points at `### Changing one after it is written` under `## Acceptance conditions`. Numbering and order are unchanged.

`graph-conventions.md`:
- `## The seven files`: the `## Destination` description is extended. It now says the section also states, in one line, whether the effort is expected to reach the destination, and that where it is not, this is where a manager reads that a non-empty frontier is a steady state rather than a defect.
- `### Start an effort` is new, the first procedure under `## Procedures`. Its steps, in order:
  1. `map.md`, whose `## Destination` states both things.
  2. `map-history.md`.
  3. `map-manager-only.md`, holding the declared label vocabulary or a line saying there is none.
  4. `map-implementation-rules.md`.
  5. `decisions.md`.
  6. `flags.md`.
  7. The `nodes/` directory.
  8. The first node files, by `## Adding a node`.
  9. A check step: the manager runs checks 1, 3 and 4 itself at this act.
  - Call on step 9: the creation writes can falsify only checks 1, 3 and 4. Check 11 cannot fail, because creating files removes nothing. Check 10 never fails. Checks 2 and 5 to 9 concern supersession, resolution, flags, claims, interviews and reviews, and this act writes none of those.
- `### Change the map`: one paragraph added saying who runs it. It is the manager, except in the third branch of the `SKILL.md` test, where the shipping node's worker runs it inside that node. The numbered steps are unchanged.

INDEX LINE:    The manager contract now holds the file test for graph edits, the map as home of standing rules, a stop on second supersession, and a Starting an effort section with its procedure.

FLAGS:
ASSUMPTION: Clauses 9 and 10 needed an existing section whose subject includes superseding a node. I put the passage in `### What reject means`, the only such section other than `## When an agent dies or is stopped`, which node 124 will rewrite. I worded the rule to cover a revision as well as a reject, because clause 9 states it for any supersession of a replacement. — The second-supersession rule sits in `### What reject means`, worded to cover revisions too, to keep it out of the section node 124 will rewrite.
ASSUMPTION: Clause 1 calls the second branch "the files of an effort's own record". The glossary defines "record" as answers, statuses, index lines and flags only. So I wrote "the graph's files" with the full list the clause gives. That also matches "graph file" in the paragraph clause 4 keeps. — The file test calls the effort's own files "the graph's files", because the glossary's "record" is narrower than the list clause 1 gives.
ASSUMPTION: Clause 18 says the label vocabulary is "declared or declared to be absent", and no file said where an absence is recorded. So `### Start an effort` step 3 has `map-manager-only.md` hold either the vocabulary or a line saying the effort declares none. — The Start an effort procedure records a declared-absent label vocabulary as a line in map-manager-only.md, a place no earlier text named.
ASSUMPTION: The amendment's check step names checks 1, 3 and 4. I judged these to be the only checks the act's writes can make false: creating files removes nothing (check 11), check 10 never fails, and the act writes no supersession, resolution, flag, claim, interview or review. This is the same set node 339's worker proposed. — Start an effort's check step names checks 1, 3 and 4, judged the only ones that creating an effort's files can falsify.

NEW NODES:     none

INVALIDATIONS: None contradicted. Extensions:
- Node 283 (the file test): carried as decided. It also narrows the old `SKILL.md` statement that no worker performs any procedure.
- Node 98 (starting an effort has no section): carried out, with a section and a procedure.
- Node 91 (the destination records whether an effort ends): carried into the shipped files.
- Node 93 (effort-scoped rules): carried into the shipped files.
- The one extension beyond what those nodes state is the third assumption flag: a declared-absent label vocabulary is written as a line in `map-manager-only.md`.

CONDITIONS:    I searched every open and claimed node's `## Acceptance condition`, and any amendment sections, for these phrases: "no worker performs", "every procedure in", "condition that is wrong goes", "Nothing does. The worker", "reaching the end of the effort looks like", "Start an effort", "Starting an effort", "What reject means", "Writing the graph", "Standing steering", "Change the map", "What is never yours", "What nothing here settles", "Closing an effort", "charting". Matches outside node 337:
- Node 340 cites `## Writing the graph` as making the manager the only writer of the graph's record. That still holds.
- Node 342 records an invocation in the map as standing steering. Consistent.
- Node 97 (unclaimed, writes `adoption.md`) describes adoption as a mode of starting an effort that the manager performs before the graph exists, which is consistent. Its step "creating the remaining graph files empty" sits a little uneasily beside my step 3, where `map-manager-only.md` holds the label vocabulary. But node 97 declares the vocabulary from foreign label families and does not say which file holds it, so no clause is wrong.
No replacement clauses written.

MISSING FROM MAP: The map does not say that the glossary is still `CONTEXT.md` at the root in this tree, or that it already holds `## Starting an effort` and `Adoption` entries, which I needed to avoid its refusals. Found by searching `CONTEXT.md`. The map's glossary paragraph says node 56 moves the file, and it has not moved in this tree.

GATE PAYLOAD:
- Checker findings: none yet (no check has run).
- Bar: confirmed against the repo. There is no manifest, build, test, formatter or CI. `.gitignore` holds the three worktree entries the rules file records, so the record matches the repo. Wrap width is kept at 105 columns. The only longer added line is the table row, and markdown table rows cannot wrap; the existing rows are longer than 105 too.
- Other checks: `charting` appears nowhere in either file, and neither file cites by line number.
- Paths touched (in the worktree):
  - `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/337-m2/.claude/skills/expedition/SKILL.md`
  - `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/337-m2/.claude/skills/expedition/graph-conventions.md`
  - Nothing else.
- Proposed commit message:

  Carry the file test, a standing rule's home, the second supersession and starting an effort into the manager contract

  SKILL.md: Writing the graph gains the three-branch file test and makes Change the map the one procedure a worker may run. Standing steering says a standing rule lives in the map and reaches a shipped file only on the human's word. What reject means stops a second supersession and sends the chain to the human. A new Starting an effort section. The never-yours table's condition row and open item 4 are qualified. graph-conventions.md: a Start an effort procedure ending in its check step, the Destination line says whether the effort is expected to reach it, and Change the map says who runs it.

  Node: graph-workflow/337

RETROSPECTIVE
1. What I had to hunt for: which glossary entries exist in this tree, and what "record" means there. I found them by searching `CONTEXT.md`. I first looked in the map, whose glossary paragraph implies the file has moved. I also had to work out which checks the new procedure can falsify, by reading all eleven checks.
2. What arrived that this node did not need: most of `map.md`'s standing preferences (worktree route, token priority, retrospective rules, the moved-standard licence). They bore on nothing here. The rules file's paragraphs on record-file checking and superseding its own rules were not needed either. From the decisions index I needed only about six lines, and a narrow search got them cheaply.
3. What would have made this easier: the manager's note naming node 124's rewrite was useful. A one-line note that the glossary's "record" is narrower than the condition's "record files" would have saved a judgement. So would a note on where a declared-absent vocabulary is recorded.
4. What was stale, wrong or contradictory:
   - The node file's `Blocked by: 339` still stands, although 339 has landed (`5c629f4`).
   - The condition's "How this scope was got" grep result is dated to `c3ecda3`. It is no longer true for `CONTEXT.md`, which node 332 has since given starting-an-effort entries. It is still true for `.claude/skills`.
   - The map's glossary paragraph says node 56 moves `CONTEXT.md` to `.claude/skills/expedition/glossary.md`, but the tree still has it at the root, and `SKILL.md` and `graph-conventions.md` still name `CONTEXT.md`.
   - Every quote the condition gives as "before this work it reads" still matched the tree at `968b1ec`.

*The manager's note, 2026-09-27:* the checker was resumed from node 343's check. The condition and amendment reached it as a verbatim copy in `$TMPDIR/m337.md` (13.9 kB), which the message told it to read whole, instead of pasted into the message itself. Node 339's `Blocked by:` edge is struck through: node 339 landed as `5c629f4`.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 343's check.*

> PASS
>
> Node 337, "Carry the record-file test, the home of a standing rule, the second supersession and starting an effort into the manager contract". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/337-m2`, on base 968b1ec. It touches `.claude/skills/expedition/SKILL.md` (+77/-2) and `graph-conventions.md` (+30/-2). The parts I established are listed below. Two parts are outside what I hold; they are under NOT COVERED.
>
> **Parts of the condition**
>
> - **Scope:** met. `git status --short` shows only the two files. Nothing under `.scratch/` changed, and no node file, decisions.md or flags.md changed. Both files are edited plainly: the old wording is removed, with nothing struck through or moved.
> - **1:** met. A paragraph added to `## Writing the graph` says "The file a change touches decides whose change it is. Look only at which file it touches… The test has three branches, and no fourth". Its three bullets give:
>   - shipped files, meaning the skill files, rules files and glossary, are always a node's work, whoever noticed;
>   - a change confined to the graph's files, meaning the map, its siblings, the history file, decisions, flags and node files, is the manager's own, with "no node, no acceptance condition, no worker, no checker and no gate";
>   - the same node's worker makes the change to the graph's files, and the acceptance condition names it, "so both land together".
> - **2:** met. "The third branch does not hold in reverse. Noticing that a graph file is wrong never makes a node for a shipped file. A defect confined to the graph's files falls in the second branch, whatever produced it."
> - **3:** met. The old sentence is replaced by "…every procedure in `graph-conventions.md` except `### Change the map` are yours. A worker performs `### Change the map` in the third branch of the test below, and you perform it otherwise."
> - **4:** met. "That rule covers recording only. Where a node's own work is a change to a graph file…" is unchanged; it is a context line in the diff. The added text does not contradict it.
> - **5:** met. `### Change the map` gains one paragraph before its steps: "The manager runs this procedure, except in one case…" It names the third branch. The diff shows the numbered steps unchanged.
> - **6.1–6.4:** met. `### Standing steering…` gains four paragraphs:
>   - 6.1: a rule "binds an effort only once it is written into that effort's map. Write it there when the human states it. Until it is there, it binds nobody", and this holds "for rules of conduct as well as for steering".
>   - 6.2: "The map is a rule's ordinary home, and usually its only one. On most efforts the workflow's own skill files are not changed at all…"
>   - 6.3: a rule reaches a shipped skill file only on the human's word, as a node, "never on your own judgement, even where you judge the rule to be about the workflow…", and "Where the human says nothing about a rule's scope, the rule is the effort's alone."
>   - 6.4: "Every worker on an effort is bound by everything in that effort's map, whatever a rule's origin. So no rule needs a scope marking… and the map has no field for a rule's scope."
> - **7:** met. The paragraph beginning "Some of what binds you…" is kept; it is a context line in the diff.
> - **8:** met. `git diff | grep '^+' | grep -niE 'line [0-9]|lines [0-9]|:[0-9]+'` finds nothing. The section's heading is unchanged.
> - **9:** met. The new paragraph says "Where a reject or a revision would have you supersede a node that is itself a replacement, do not supersede it again. Put the chain to the human instead, as a decision about the shape of the graph. There is no depth counter and no budget on supersession. The chain itself makes the friction visible…"
> - **10 (the passage):** met. The passage sits in the existing `### What reject means`, whose subject includes superseding ("a replacement supersedes it"), and it uses "revision" in its body. Whether the handover names that section is under NOT COVERED.
> - **11, 12:** met. The row's second cell now says the condition is handed over as written, a condition "a worker already holds and judges wrong goes to the human", and "the one narrow exception, amending a clause of the condition of a node nobody holds yet, is stated under `## Acceptance conditions`". It is the only table line in the diff, so every row keeps its first cell and order, and no row is added.
> - **13, 14:** met. Item 4 is still a question. It says "does in general: no duty to look covers the effort's record as a whole", then names "the open nodes' acceptance conditions" and points to "`### Changing one after it is written`, under `## Acceptance conditions`". That section's last paragraph does state the search of open nodes' `## Acceptance condition` sections. Item 4 is the only list item in the diff, and the numbering is unchanged.
> - **15–20:** met. `## Starting an effort` sits directly before `## Closing an effort` and covers each clause:
>   - 15: the section exists, before `## Closing an effort`.
>   - 16: two ways, told apart by input: a conversation, and adoption from a directory that already exists. Both produce the same files and first nodes.
>   - 17: "You perform it, and it happens before the graph exists."
>   - 18: all six things are listed as bullets.
>   - 19: the file mechanics are "in `### Start an effort` in `graph-conventions.md`, and not in this contract."
>   - 20: both halves of what an empty frontier means are given as bullets.
> - **"charting" appears nowhere in either file:** met. `grep -n -i charting` over both files finds nothing.
> - **21:** met. `git diff | grep '^+' | grep -niE 'tracker|reserved|foreign|import|repoint|citation|precondition|bulk|existing directory|already exists'` returns one hit. It is the clause-16 definition of adoption's input, not one of adoption's seven steps. No adoption step appears in the added text.
> - **22:** met. `### Start an effort` is the first subsection under `## Procedures` and is a numbered list of files, in order:
>   1. `map.md`;
>   2. map-history.md;
>   3. map-manager-only.md;
>   4. map-implementation-rules.md;
>   5. decisions.md;
>   6. flags.md;
>   7. `nodes/`;
>   8. the first node files, by `## Adding a node`.
>
>   That covers all seven files, with map.md first and the nodes last.
> - **Amendment clause:** met. Step 9 names checks 1, 3 and 4 by number and says the manager "runs [them] itself, as part of this act". The other checks cannot be made false by these writes:
>   - check 2 (supersession) and checks 5–9 (resolved nodes, flags, claims, interviews, reviews) have nothing to test when an effort starts;
>   - check 10 only reports and never fails;
>   - check 11 has nothing taken out.
> - **23:** met. Step 1 says `## Destination` "says both what reaching the end of the effort looks like and whether the effort is expected to reach it."
> - **24:** met. The `## Destination` bullet under `## The seven files` gains the one-line expectation, and says a manager reads there that a non-empty frontier is that effort's steady state rather than a defect.
> - **25:** met. `git diff | grep '^+' | grep -niE 'often|rarely|most efforts|seldom|never end|usually'` returns only clause 6.2's sentence. That sentence is about skill files going unchanged, which the condition itself demands, not about how often efforts end.
> - **26, 27:** met. No diff hunk falls in `## Acceptance conditions` or in `## What is in front of the human, and when`.
> - **28:** met. `git diff | grep '^+' | grep -niE 'attempt|cost|wrong|before this|used to|previously|earlier'` returns only rule text: "judges wrong" and "a graph file is wrong". There is no account of how the work went.
> - **29:** met. The added text removes no heading and touches no existing step under `## Procedures`. The only changed lines are the ones the clauses above name.
> - **30:** met. See the bar below.
>
> **The bar**
>
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check`: clean, exit 0.
> - The only added line over the file's wrap width is the table row. The file's other table rows are also over it.
>
> **Standards**
>
> I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`, as in my earlier checks.
>
> - **Bore on the work:**
>   - `CONTEXT.md` `_Avoid_` lines, checked by hand on the added text, including the glossary's `Starting an effort` and `Adoption` entries (charting, kickoff, onboarding, bootstrap, setup, init, migration, import, port). Nothing found.
>   - The five writing rules. Citations are by heading, prohibitions stand beside their positive form, and no bold was added.
>   - `/writing-for-agents`. Nothing found.
>   - The ground rules. Nothing assumes a repo, machine or toolchain, and nothing tells an agent to address the human.
> - **Did not bear:** `/coding-principles` and `/naming`, since the work is prose and the new headings follow the condition.
> - No reviewing skill is named, so I ran none. graph-conventions.md is part of the work, so I held its additions against the condition and against no element the work introduced.
>
> **The search the condition records**
>
> I ran it as written. `git grep -l -i "starting an effort\|start an effort\|charting\|adoption" c3ecda3 -- .claude/skills CONTEXT.md` returns no files, which matches the recorded return. At the current tree, `grep -rln` returns `SKILL.md`, `graph-conventions.md` and `CONTEXT.md`. The first two are this work. This is handed back alongside the outcome, not as a FAIL:
>
> - **Instances:** `CONTEXT.md` matches at its `## Starting an effort` section, lines 314–333, which cover `**Starting an effort**:`, `**Adoption**:` and an `_Avoid_: charting…` line. `git log c3ecda3..HEAD -- CONTEXT.md` shows these came from c365a75 ("add its Starting an effort section"), which landed after the recorded search. This work does not touch CONTEXT.md, and the entries agree with the new SKILL.md section.
> - **Form:** a file the recorded search returns now that is outside the condition's two files.
> - **Extent:** `grep -rln -i "starting an effort\|start an effort\|charting\|adoption" .claude/skills CONTEXT.md | grep -v '^.claude/skills/expedition/\(SKILL\|graph-conventions\).md$'` returns only `CONTEXT.md`.
>
> NOT COVERED:
> - Clause 10's "and the worker names that section in its handover". The handover is something an agent handed back, not part of the working tree, so it is outside what I was given.
> - "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

*The manager's note:* on the first NOT COVERED item, the handover names the section: its ANSWER says "`### What reject means`: this is the section chosen for the second supersession (clauses 9 and 10)". On the recorded search, the `CONTEXT.md` match is the glossary's `## Starting an effort` section landed by node 332 (`c365a75`), after the search was recorded at `c3ecda3`.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*

## Flags

`337.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above.* The clause is added from node 330's C11(a) text on the ground that the human took that option and it had not reached this condition.

`337.2` `ASSUMPTION` **· settled** — Clauses 9 and 10 needed an existing section whose subject includes superseding a node. I put the passage in `### What reject means`, the only such section other than `## When an agent dies or is stopped`, which node 124 will rewrite. I worded the rule to cover a revision as well as a reject, because clause 9 states it for any supersession of a replacement. — The second-supersession rule sits in `### What reject means`, worded to cover revisions too, to keep it out of the section node 124 will rewrite.

`337.3` `ASSUMPTION` **· settled** — Clause 1 calls the second branch "the files of an effort's own record". The glossary defines "record" as answers, statuses, index lines and flags only. So I wrote "the graph's files" with the full list the clause gives. That also matches "graph file" in the paragraph clause 4 keeps. — The file test calls the effort's own files "the graph's files", because the glossary's "record" is narrower than the list clause 1 gives.

`337.4` `ASSUMPTION` **· settled** — Clause 18 says the label vocabulary is "declared or declared to be absent", and no file said where an absence is recorded. So `### Start an effort` step 3 has `map-manager-only.md` hold either the vocabulary or a line saying the effort declares none. — The Start an effort procedure records a declared-absent label vocabulary as a line in map-manager-only.md, a place no earlier text named.

`337.5` `ASSUMPTION` **· settled** — The amendment's check step names checks 1, 3 and 4. I judged these to be the only checks the act's writes can make false: creating files removes nothing (check 11), check 10 never fails, and the act writes no supersession, resolution, flag, claim, interview or review. This is the same set node 339's worker proposed. — Start an effort's check step names checks 1, 3 and 4, judged the only ones that creating an effort's files can falsify.
