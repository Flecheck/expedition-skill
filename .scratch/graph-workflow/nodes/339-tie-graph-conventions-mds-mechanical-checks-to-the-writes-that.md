# Tie graph-conventions.md's mechanical checks to the writes that can make them false

Type: implementation
Status: resolved
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

## Answer

Each graph-conventions.md procedure now ends by naming the checks its writes can falsify, run by the actor; new check 11 guards map-history, plus scan rules and two procedures.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. A first checker was stopped with the session before handing back an outcome; a fresh checker, on the human's word, passed it. The human approved. The work landed as commit `5c629f4`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Tie graph-conventions.md's mechanical checks to the writes that can make them false

ANSWER:        `.claude/skills/expedition/graph-conventions.md` now ties every mechanical check to the act that can make it false. It is the only file that changed.

               What was built, clause by clause:
               - Clause 1 (238). Each of the nine sections ends with one added numbered step. The step says that whoever performs the act runs the named checks itself, as part of that act, over the material the act touched, and it names that material.
                 - `### Claim` step 2: check 7.
                 - `### Resolve` step 6: checks 5 and 9, plus check 11 where steps 4 and 5 moved a fog item.
                 - `### Supersede` step 6: checks 1 and 2.
                 - `### Rule out of scope` step 3: check 1.
                 - `### Park` step 4: check 8.
                 - `### Raise a flag` step 3: check 6.
                 - `### Settle a flag` step 3: check 6.
                 - `### Change the map` step 3: checks 4, 10 and 11.
                 - `## Adding a node` step 1: checks 1, 3 and 4.
                 Where a section had prose after its numbered list, the step goes after that prose, so the section ends with it.
               - Clauses 2 and 3 (238). `## Mechanical checks` gains two subsections: `### Who runs a check, and when` and `### What a failure produces`.
                 - Who runs a check: the party performing the act, at that act, over the material it touched. No schedule, periodic pass or separately spawned agent runs any check. A run of every check over the whole graph stays available at an empty frontier, and it is the only run not tied to an act.
                 - What a failure produces: bookkeeping is repaired inside the same act and nothing is reported. A repair that would change a human decision, rewrite or remove recorded text, or reverse a status goes to the human instead. Neither case raises a flag.
               - Clause 4 (238). Check 5 now requires exactly one line in `decisions.md` that is not struck through, and permits any number of struck-through lines.
               - Clauses 5 to 7 (239). Two procedures are added after `### Park`:
                 - `### Record a question or an answer`: append to `## Interview`, then run check 8.
                 - `### Record a checker's run`: append to `## Review`, then run check 9.
                 Each cites the shape by heading ("the `## Interview` subsection of `## The node file`", and the same for `## Review`) and does not restate it.
               - Clauses 8 to 11 (288). Check 11 is added after check 10. It has two halves:
                 - `map-history.md` before the change is a byte-exact prefix of `map-history.md` after it.
                 - Every passage removed from a map file appears byte-identically in the text appended to `map-history.md`.
                 It is decided by comparing the files character by character, it fails when either half does not hold, and it defines "map file" as `map.md` or a sibling of it that states rules that currently bind. `### Change the map` names it as what establishes that step 1 was carried out.
               - Clause 12 (49). `### How a check reads the files` lists the seven rules. For rules a and b, and the `Blocked by:` rule, it points to `## Reading the graph` by name. It states rules c to g itself: unwrap text before matching; the first link on a line identifies the node in `flags.md` and in `decisions.md`; `## Flags` entries are line-anchored; and a flag counts as settled only when `**· settled**` stands in the marker position. These rules are bullets rather than a numbered list, so their numbers cannot be confused with check numbers.
               - Clauses 13 and 14 (286). `## Reading the graph` gains rule 3: take a number from `Blocked by:` only where it lies outside every code span, every `~~...~~` and every link target. Four examples follow:
                 - `~~31~~` gives nothing.
                 - A two-link form gives 95 and 103.
                 - `none — [node 139](...) landed as `4e38c11`` gives 139, and nothing from the digits of the hash.
                 - The real node-277 form gives 277.
                 The lead-in sentence now says "these rules" instead of "two rules".
               - Clauses 15 to 18: `## Edges` is unchanged. Existing checks keep their numbers and text, apart from check 5. No existing procedure step is reworded, and `## Adding a node`'s prose is unchanged. Nothing mentions attempts, cost or who was wrong.

               Things a later reader should know:
               - Every real struck-through `Blocked by:` form in this graph repeats the number in prose afterwards (for example `~~277~~ **none — node 277 resolved…**`). The rule as specified takes that repeated number. This does no harm, because the node it names is resolved, and the fourth example says so. A scanner that must take nothing from these forms needs a stronger rule.
               - Three writes still have no procedure and no check step: a correction-round entry in `## Review`, a gate-outcome entry in `## Review`, and establishing a `NOT COVERED:` item. Resolve's check 9 covers the last of these, because it runs before the node resolves.

               The bar: the repo has no build, no tests, no formatter and no CI. The worktree holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`, with no manifest or task runner. That matches the record in `map-implementation-rules.md`, so there was no difference to report. The bar is therefore its non-command half:
               - `/coding-principles` and `/naming`
               - the `_Avoid_` lines in `CONTEXT.md`
               - `graph-conventions.md` itself
               - `/writing-for-agents`, which I loaded and applied: I cut a restatement of rules a and b down to a pointer
               - the ground rules and the five writing rules
               Wrap width is 104, as before. The only line over 104 is line 156, which existed before this work. No method skill instruction was skipped.

INDEX LINE:    Each graph-conventions.md procedure now ends by naming the checks its writes can falsify, run by the actor; new check 11 guards map-history, plus scan rules and two procedures.

FLAGS:         ASSUMPTION: Check 11 is named in two steps beyond the numbers clause 1 lists. `### Change the map` step 3 names checks 4, 10 and 11, not only 4 and 10, and `### Resolve` step 6 adds check 11 where steps 4 and 5 moved a fog item. The file now says every check is run by whoever performs an act that can make it false. Resolve's step 5 removes text from `map-manager-only.md`, which is exactly what check 11 guards. Leaving 11 out of either step would contradict that sentence, and clause 11 requires `### Change the map` to name check 11 anyway. Clause 1 says what each step must name, and naming more still satisfies it.
               Index: The Change-the-map and Resolve check steps also name new check 11, because both acts can remove text from a map file; clause 1 listed only the older numbers.

               ASSUMPTION: The lead-in to `## Reading the graph` said "anything that scans these files follows two rules:". With a third rule added it would have been false, so it now reads "follows these rules:". It also gains the clause "and a field can hold text that is not a value", so the lead-in covers the new rule's reason. No clause forbids this edit.
               Index: The lead-in to Reading the graph changed from "two rules" to "these rules" once the Blocked-by scan rule became its third rule.

               ASSUMPTION: Three of the four `Blocked by:` examples are quoted from real node files. The example from which nothing is taken, `Blocked by: ~~31~~`, is a minimal form, because every real struck-through form in the graph repeats the number in prose, and the rule takes that number. I quoted one such real form (node 277's) and said what the rule takes from it, rather than choosing only examples that make the rule look complete.
               Index: The Blocked-by example that yields nothing is a minimal form; every real struck form repeats its number in prose, which the stated rule still takes.

NEW NODES:     none. Under the map's standing instruction, the related defects below are proposed as clauses to add to open nodes rather than as new nodes.
               - To node 337 (its clause 22 adds `### Start an effort` under `## Procedures`): "`### Start an effort` ends with a numbered step naming checks 1, 3 and 4 under `## Mechanical checks`. The step states that whoever starts the effort runs them itself, at that act, over the files it created." Without such a step, the new procedure contradicts `### Who runs a check, and when`, which now says every procedure ends with a step naming the checks its writes can make false.
               - To node 338 (its clause 19 lets it add one check, about a superseded condition clause marked in place): "Where the work adds a check, the act whose write can make the check false names it: in an existing check step, in a new step, or in the check's own text. This stays consistent with `### Who runs a check, and when`." Node 338's clause 20 forbids rewording any procedure except as its clause 7 states. Naming the new check in an existing check step would count as rewording, so the manager may need to resolve that conflict with the human before node 338 is claimed.

INVALIDATIONS: none. The work carries out node 213's resolved answer ("each procedure gains a final step naming the checks its writes can falsify; a failure is repaired inside the act, and reaches the human only where the repair would touch the record"), and contradicts no resolved node.

GATE PAYLOAD:  Checker findings: none yet; this is the first handover.
               Paths touched: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/339-checks-to-writes/.claude/skills/expedition/graph-conventions.md` (111 insertions, 3 deletions). No other path was touched. I read node files 337, 338 and 340 and the `Blocked by:` lines of other node files, and wrote none of them.
               Proposed commit message:
                 Tie graph-conventions.md's mechanical checks to the acts that can falsify them

                 Each procedure, and Adding a node, ends with a step naming the checks its
                 writes can make false, run by whoever performs the act. Adds procedures for
                 recording an interview exchange and a checker's run, check 11 on what a map
                 change owes map-history.md, the rules a check reads the files by, and the
                 rule for taking node numbers from a Blocked by: field. Check 5 counts only
                 decisions.md lines that are not struck through.

                 Node: graph-workflow/339

RETROSPECTIVE:
1. What I had to hunt for. Clause 14 wants "forms the field actually takes", so I needed real `Blocked by:` forms. I grepped `nodes/*.md` for them, and that search showed that every struck form repeats its number in prose. I also checked that the "sweep" and the "whole-graph run" are different things: I grepped `SKILL.md` and `CONTEXT.md`, and the glossary defines a sweep as a search for unpropagated revisions. Finally, to see whether my new rule collided with the sibling nodes' conditions, I read the relevant clauses of nodes 337 and 338.
2. What arrived that this node did not need. Most of `map.md`: the standing preferences on concurrency, payloads, retrospectives and worktrees bore on nothing here. Of `map-implementation-rules.md`, only the bar and the writing rules mattered. The decisions.md grep was useful for one line only (node 213). The spawn's notes about the checker contract and glossary changes, and about node 333's state, bore on nothing in this file.
3. What would have made this easier. Clause 1(h) lists "4 and 10" and clause 11 separately asks for check 11 in the same procedure. One sentence in the condition saying whether check 11 belongs in that step, and whether Resolve's fog-item removal also owes check 11, would have removed my first flag. The spawn could also have named which sibling nodes add procedures or checks (337 clause 22, 338 clause 19), so I would not have had to find them.
4. What was stale, wrong or contradictory. Clause 14's demand for a real struck-through form from which nothing is taken cannot be met by any form currently in the graph: each one repeats the number in prose, and the rule the condition specifies takes that number. The rule is harmless because those nodes are resolved, but it is weaker than its purpose. `decisions.md` line 82 (node 98) says `graph-conventions.md` has a `### Start an effort` procedure, but master does not have one yet (node 337 adds it), so that index line is ahead of the file.

## Review

### Checker run 1 — no outcome

*The manager's note, 2026-09-26:* the checker (resumed from node 333's re-check) was stopped mid-check by a usage limit, resumed once, then ended with the previous session. A resume after the restart was refused: "Agent a4c308111583f1790 was stopped by the user and won't be resumed. Treat its work as cancelled; only launch a new agent if the user explicitly asks." Under node 123's answer the manager does not replace it on its own; whether to revive it or spawn a fresh checker goes to the human.

*The human, on this checker, `verbatim`, 2026-09-26:* *"approve, you can start a fresh checker"* (given at node 333's gate).

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-09-26. A fresh checker, on the human's word.*

> PASS
>
> Work under check: `git -C /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/339-checks-to-writes diff`. HEAD is 5acd220. The diff is uncommitted and touches only `.claude/skills/expedition/graph-conventions.md`: 111 lines added, 3 removed. The 3 removed lines are the two-line intro to `## Reading the graph` and the old check 5. I read the changed path as the work, as the rules file says a checker does for a record file.
>
> Parts of the condition, and how I established each:
>
> - Scope (only this file changes; nothing under `.scratch/`; edited plainly; no node, decisions.md or flags.md write): established by `git status --short` in the worktree, which shows one `M` line, for graph-conventions.md. The diff also shows superseded wording removed rather than struck through. The worktree diff holds no node file, no decisions.md and no flags.md, so the rules file's bookkeeping-reserved-to-the-manager rule is not triggered. What the main tree's record holds is outside what I was given (see NOT COVERED).
> - 1(a–i): each of the nine sections now ends with one added numbered step, found by reading the diff's `+` hunks in each section.
>   - Claim: step 2, check 7.
>   - Resolve: step 6, checks 5 and 9. It also names check 11, conditional on steps 4 and 5 having moved a fog item. The condition does not forbid extra checks, and the step's writes can make check 11 false.
>   - Supersede: step 6, checks 1 and 2.
>   - Rule out of scope: step 3, check 1.
>   - Park: step 4, check 8.
>   - Raise a flag: step 3, check 6.
>   - Settle a flag: step 3, check 6.
>   - Change the map: step 3, checks 4, 10 and 11.
>   - Adding a node: step 1, checks 1, 3 and 4. The section had no numbering before.
>   - Each step says "Whoever … runs … itself, as part of this <act>, over the material <it> touched: …". Each step is the last line of its section.
> - 2: the new subsection `### Who runs a check, and when` states all three points:
>   - each check is run by whoever performs the act that can make it false, at that act, over what it touched;
>   - "No schedule, no periodic pass and no separately spawned agent runs any of them";
>   - "One run is not tied to an act: a run of every check over the whole graph, which remains available at an empty frontier."
> - 3: `### What a failure produces` says "neither raises a flag". It has one bullet each for the two cases: bookkeeping repaired inside the act with nothing reported, and a change to the human's decision, recorded text or a status put to the human.
> - 4: check 5 now reads "…exactly one line in `decisions.md` that is not struck through. It may have any number of struck-through lines there."
> - 5, 6: two subsections are added, `### Record a question or an answer` and `### Record a checker's run`. Each is a numbered list: step 1 names `nodes/NN-<name>.md`, and step 2 is the check step. The first names check 8 and the second names check 9, each with "itself … over the material it touched".
> - 7: neither new subsection restates a shape. They cite "the `## Interview` subsection of `## The node file` above" and "the `## Review` subsection of `## The node file` above". Both headings exist, as "### `## Interview`" and "### `## Review`". The first subsection also cites `### Recording the human's words`, which exists.
> - 8, 9, 10: new check 11 carries both demanded halves: the history file's old content is a byte-exact prefix of its new content, and every removed passage appears byte-identically in the appended text. It says it is "decided by comparing the two states of the files character by character, and not by reading them for sense", and it "fails where either half does not hold".
> - 11: Change the map step 3 says "Check 11 is what establishes that step 1 was carried out."
> - 12(a–g): the new subsection `### How a check reads the files` covers all seven rules.
>   - a and b point to `## Reading the graph` by heading.
>   - c: text is unwrapped before any phrase is matched.
>   - d: in flags.md, the flag's node is the first link on the line.
>   - e: in decisions.md, the first link identifies the entry, and an entry citing another node does not count for it.
>   - f: a `## Flags` entry is line-anchored.
>   - g: `**· settled**` counts only in the marker position, and the bare word does not.
> - 13, 14: `## Reading the graph` has a new rule 3.
>   - It states the never-delete rule for `Blocked by:` and that the field may hold links, prose and commit hashes in code spans.
>   - It states the scanner rule: take a number only outside code spans, `~~…~~` and link targets.
>   - It gives four quoted examples, each with what a scanner takes from it. `~~31~~` gives nothing (a struck blocker). The ones with `4e38c11` and `b94104a` show code-span digits not read. I also checked each example against the rule it illustrates: they agree.
> - 15: `## Edges` has no hunk in the diff, and `Blocked by: NN, NN` is unchanged.
> - 16: the only `-` line in `## Mechanical checks` is old check 5, and checks 1–10 keep their numbers and order. Exactly one check (11) is added, after check 10, followed by three prose subsections that are not checks.
> - 17: the diff has no `-` line in `## Procedures` or `## Adding a node`, and the only new subsections are the two from clause 5.
> - 18: `git diff | grep '^+' | grep -niE 'attempt|cost|wrong|earlier|previous|mistake|round'` returns one hit, and it uses "attempt" as the node-file term ("under the current attempt"). It says nothing about how many attempts this work took, what it cost or who was wrong.
> - 19: see the bar below.
>
> The bar:
>
> - The repo has no build, no tests, no formatter and no CI. The standards file says so, and the worktree root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, with no CLAUDE.md or AGENTS.md. So the bar is its non-command half.
> - `git diff --check` prints nothing.
> - `awk 'length>105'` over the new file and over HEAD's version prints nothing, so the new text keeps the file's wrap width.
> - `grep -nE ' +$'` prints nothing.
>
> Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md` and opened no other file in the effort's directory. The standards I read are:
>
> - `/coding-principles` and `/naming`;
> - `CONTEXT.md`'s `_Avoid_` lines;
> - graph-conventions.md itself;
> - `/writing-for-agents`;
> - the five ground rules;
> - the five standing rules for writing;
> - the rule on record files handed over as the work.
>
> Those that bore on this work:
>
> - `CONTEXT.md`'s `_Avoid_` lines. I checked the distinctive refusals by hand, as the file advises, and found none in the added text. "run" and "item" are used in senses the file already uses ("checker run", "fog item", `NOT COVERED:` items).
> - `/writing-for-agents`. I read it through the Skill tool: no reviewing agent, and it found nothing. The one prohibition ("No schedule, …") is wording clause 2 requires.
> - The writing rules. Citations are by heading and never by line number, no bold was added outside code spans, and each sentence carries one idea.
> - The ground rules. Nothing in the added text assumes this repo or a toolchain, and nothing tells a spawned agent to address the human.
> - The record-file rule. It was not triggered.
>
> `/naming` bore only on the two new headings, and I found nothing. The work is prose, not code, so `/coding-principles` did not bear on it. The standards name no reviewing skill, and I ran none. The work did not change what any standard requires, since graph-conventions.md's additions are the work itself, so I held the work against no element it introduced.
>
> The condition records no search command ("this scope came from no search"), so there was nothing to re-run.
>
> NOT COVERED:
> - "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The worktree diff contains no such write. Whether the main tree's record holds one is outside what I was given, because those files are the record I am blind to.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*

## Flags

`339.1` **· settled** `ASSUMPTION` — Check 11 is named in two steps beyond the numbers clause 1 lists. `### Change the map` step 3 names checks 4, 10 and 11, not only 4 and 10, and `### Resolve` step 6 adds check 11 where steps 4 and 5 moved a fog item. The file now says every check is run by whoever performs an act that can make it false. Resolve's step 5 removes text from `map-manager-only.md`, which is exactly what check 11 guards. Leaving 11 out of either step would contradict that sentence, and clause 11 requires `### Change the map` to name check 11 anyway. Clause 1 says what each step must name, and naming more still satisfies it.

`339.2` **· settled** `ASSUMPTION` — The lead-in to `## Reading the graph` said "anything that scans these files follows two rules:". With a third rule added it would have been false, so it now reads "follows these rules:". It also gains the clause "and a field can hold text that is not a value", so the lead-in covers the new rule's reason. No clause forbids this edit.

`339.3` **· settled** `ASSUMPTION` — Three of the four `Blocked by:` examples are quoted from real node files. The example from which nothing is taken, `Blocked by: ~~31~~`, is a minimal form, because every real struck-through form in the graph repeats the number in prose, and the rule takes that number. I quoted one such real form (node 277's) and said what the rule takes from it, rather than choosing only examples that make the rule look complete.
