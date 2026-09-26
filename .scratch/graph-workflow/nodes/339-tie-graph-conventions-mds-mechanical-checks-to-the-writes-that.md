# Tie graph-conventions.md's mechanical checks to the writes that can make them false

Type: implementation
Status: open
Supersedes: 49, 238, 239, 286, 288
Blocked by: none

## Question

Nodes 49, 238, 239, 286 and 288 each change `graph-conventions.md`'s procedures, mechanical checks and scan rules: which act runs each check, two writes with no procedure, a check on the history bank, the rules a check needs, and how to read a `Blocked by:` field. Make all their changes in one piece of work.

*Proposed by [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker and filed by the manager, on the human's "ok" to node 330's merge and its conflicts' recommendations. The worker wrote each condition to the recommended option of every conflict.*

*The worker's blockers:* none

## Acceptance condition

*Written by node 330's worker.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file changes. No file under `.scratch/` changes. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. The file is one the workflow ships, so it is edited plainly. The places named below are the work itself, so this scope came from no search.
>
> Before this work the file holds these sections:
> - `## Procedures`, which opens "Each procedure lists every file it changes, in the order the changes are made." and holds subsections `### Claim`, `### Resolve`, `### Supersede`, `### Rule out of scope`, `### Park`, `### Raise a flag`, `### Settle a flag` and `### Change the map`, each a numbered list;
> - `## Adding a node`, which is prose;
> - `## Reading the graph`, which holds two numbered rules, "Read fields only from the header block, which is everything above the first `##` heading." and "Skip fenced code blocks.";
> - `## Mechanical checks`, which holds ten numbered checks.
>
> Check numbers below are those of the checks as numbered before this work.
>
> Done means every one of the following is true of the finished file. Each clause names, in brackets, the node its demand comes from.
>
> 1. (238) Each of the nine sections below ends with one added numbered step, continuing the section's numbering where it has one. The step names by number the checks it must run, and states that the party performing the act runs them itself, at that act, over the material that act touched. The sections, and the numbers each must name:
>    - (a) `### Claim`: 7
>    - (b) `### Resolve`: 5 and 9
>    - (c) `### Supersede`: 1 and 2
>    - (d) `### Rule out of scope`: 1
>    - (e) `### Park`: 8
>    - (f) `### Raise a flag`: 6
>    - (g) `### Settle a flag`: 6
>    - (h) `### Change the map`: 4 and 10
>    - (i) `## Adding a node`: 1, 3 and 4
> 2. (238) `## Mechanical checks` states all three of the following, in wording the worker chooses:
>    - every check is run by the party performing the act that can make it false, at that act, over the material that act touched;
>    - no schedule, no periodic pass and no separately spawned agent runs any of them;
>    - a whole-graph run of all the checks remains available at an empty frontier, and it is the only run not tied to an act.
> 3. (238) The same section states what a failure produces, and that no flag is raised in either case:
>    - where what failed is that act's own bookkeeping, such as a missing index line, a missing edge or a flag left unmarked, the party repairs it inside the same act and reports nothing;
>    - where the repair would change something the human decided, would rewrite or remove text already recorded, or would reverse a status, the party puts it to the human instead.
> 4. (238) Check 5 is worded so that a node satisfies it by having exactly one line in `decisions.md` that is not struck through. Struck-through lines are permitted in any number. Its wording before this work is "Every `resolved` node has an `## Answer` and exactly one line in `decisions.md`."
> 5. (239) `## Procedures` gains two new subsections. One is for appending a checker's run to a node's `## Review` section, and the other is for appending a relayed question or a human answer to a node's `## Interview` section. Each is a numbered list naming every file that changes, in order, in the form the existing subsections use.
> 6. (239) The `## Review` subsection ends with a numbered step naming check 9, and the `## Interview` subsection ends with one naming check 8. Each says that the party performing the act runs the named check itself, over the material that act touched.
> 7. (239) Neither new subsection restates the shape of `## Review` or of `## Interview`. Where a shape is needed, the subsection cites the section of the same file that holds it, by that section's heading.
> 8. (288) `## Mechanical checks` gains one check covering both halves of what a change to a map file owes the history file:
>    - the history file's content before the change is a byte-exact prefix of its content after the change, so the file gained text and lost none;
>    - every passage the change removed from a map file appears byte-identically inside the text the change appended to the history file.
> 9. (288) That check states how it is decided: by comparing the two states of the files character by character, not by reading them for sense. So it remains decidable by reading the files, as the list's opening sentence requires of every check.
> 10. (288) That check is stated as failing when it does not hold, like the list's other checks, and not as report-only like the check on the size of items under `## Notes`.
> 11. (288) `### Change the map` names that check, by its number, as what establishes that the procedure's first step was carried out.
> 12. (49) `## Mechanical checks` states all seven rules below, or points to the section of the same file that holds one, naming that section. The wording is the worker's; the content is not.
>     - a. Fields are read only from the header block, everything above the first `##` heading.
>     - b. Fenced code blocks are skipped.
>     - c. Text is unwrapped into unbroken lines before any phrase is matched, because a phrase that wraps is invisible to a search over lines.
>     - d. In `flags.md`, the flag's node is the first link on the line.
>     - e. In `decisions.md`, a resolved node's entry is identified by the first link on its line, so an entry whose text cites another node is not counted as an entry for that node.
>     - f. A `## Flags` entry is line-anchored: an entry begins at the start of a line with the flag's id, so a flag id appearing mid-sentence inside another entry's prose is not itself an entry.
>     - g. A flag counts as settled on its node only where the marker `**· settled**` stands in an entry's marker position. The bare word `settled` in an entry's prose does not settle it.
> 13. (286) `## Reading the graph` carries a third numbered rule beside its two. It states that the `Blocked by:` field is written under the never-delete discipline, so a blocker that has been satisfied is struck through in place rather than removed. It states that the field may also hold markdown links to node files, explanatory prose, and commit hashes inside code spans. It then states the rule a scanner follows: take a node number from that field only where the number lies outside every backtick-delimited code span, outside every `~~...~~` strikethrough, and outside the parenthesised target of every markdown link.
> 14. (286) The rule gives at least three short quoted examples of forms the field actually takes, each paired with what a scanner must take from it. At least one example is a struck-through blocker from which nothing is taken. At least one is a form whose code span holds digits that must not be read as a node number.
>
> **What does not change**
>
> 15. (286) `## Edges` is unchanged: the canonical form `Blocked by: NN, NN` that it states stays as it is.
> 16. (49, 238, 239, 288) The existing checks keep their numbers and their order. The only change to an existing check's text is the one clause 4 makes. Exactly one check is added, the one clause 8 describes, placed after the existing ones.
> 17. (238, 239) No existing numbered step under `## Procedures` is reworded, renumbered or removed, and `## Adding a node`'s existing prose is unchanged apart from the step clause 1 adds. `## Procedures` gains no subsection other than the two in clause 5.
> 18. (288) The file states nowhere how many attempts this took, what it cost, or who was wrong.
> 19. The working tree meets the bar.
