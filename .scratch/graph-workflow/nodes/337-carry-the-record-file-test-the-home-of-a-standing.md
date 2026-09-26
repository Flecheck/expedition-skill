# Carry the record-file test, the home of a standing rule, the second supersession and starting an effort into the manager contract

Type: implementation
Status: open
Supersedes: 101, 105, 111, 278, 280, 287
Blocked by: 339

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
