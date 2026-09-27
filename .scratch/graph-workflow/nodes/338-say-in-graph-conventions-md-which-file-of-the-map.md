# Say in graph-conventions.md which file of the map holds what, and where the never-delete rule reaches

Type: implementation
Status: resolved
Supersedes: 146, 153, 195, 201, 206, 228, 233, 308, 148, 43
Blocked by: none

## Question

Nodes 146, 153, 195, 201, 206, 228, 233 and 308 each correct a few lines of `graph-conventions.md` about which file of a split map holds what, and about where the never-delete rule applies. Make all their changes in one piece of work.

*Proposed by [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker and filed by the manager, on the human's "ok" to node 330's merge and its conflicts' recommendations. The worker wrote each condition to the recommended option of every conflict.* *The manager's note:* on the manager's proposal, which the human took, node 329's remainder R1 (the `graph-conventions.md` sentences of nodes 148 and 43, written by node 329's worker) is folded in as clauses 17a and 17b, and clause 20's "1 to 17" is widened to "1 to 17b".

*The worker's blockers:* none

## Acceptance condition

*Written by node 330's worker, with clauses 17a and 17b from node 329's worker.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file changes. No file under `.scratch/` changes. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. The file is one the workflow ships, so it is edited plainly: superseded wording is removed, and nothing is struck through or moved to a history file. The places named below are the work itself, so this scope came from no search.
>
> Done means every one of the following is true of the finished file. Each clause names, in brackets, the node its demand comes from.
>
> **Which file of the map holds what**
>
> 1. (153, 228) Under `## The seven files`, the description of `map.md`'s `## Notes` no longer states that `map.md`'s `## Notes` holds the declared label vocabulary or the bar's commands. Before this work it says "The manager also maintains two things here: the declared label vocabulary, and the bar's commands once they have been discovered for this repo." Wherever the file says which file holds either, it names `map-manager-only.md` for the declared label vocabulary and `map-implementation-rules.md` for the bar's commands. The rest of that description of `## Notes` keeps its meaning, except as clause 2 states.
> 2. (228) No statement in the file requires the effort's ground rules, or its declaration of which sources are authoritative, which are evidence only, and which hold statements known to be false, to sit in `map.md`'s `## Notes` specifically. Each such statement either names the map as a whole, or says plainly that the item lives in `map.md`'s `## Notes` unless the effort holds it in a sibling file of the map.
> 3. (146) Every rule in the file written against "the map's `## Notes`" states which file's `## Notes` it governs. In particular, the 500-byte target for an item under `## Writing the map` and the numbered check under `## Mechanical checks` that reports an item over that target each name the file they apply to.
> 4. (206, 228) No sentence in `## Labels` states or implies that the labels a node may use are declared in `map.md`'s `## Notes` or in any section of `map.md`. Before this work its first bullet reads "A node uses only labels declared in the map's `## Notes`." The section names `map-manager-only.md` as where a declared label vocabulary lives. The rule that a node may use only a declared label stays in force and is not weakened.
> 5. (206) `## Labels`'s other statements are unchanged: "A label names the family or part a node belongs to, for example `CLASS` rather than `CLASS-1`. Labels are optional, and a node may carry several.", "A label is only a filter. Order comes from `Blocked by:` edges and never from a label.", "A node's identity is its `NN` and never a label.", and "An effort that declares no vocabulary has no labels on any node."
> 6. (195) The sentence under `## Writing the map` beginning "Every note, standing preference and fog item" names, for each kind of item it lists, the file of the map that holds that kind, and where two kinds live in different files it says so. Before this work that sentence places all three kinds in `map.md`, while the file's own `## The seven files` places the fog, `## Not yet specified`, in `map-manager-only.md`.
> 7. (195) The opening sentence of `### Change the map`, which before this work reads "Use this when a note, standing preference or fog item in `map.md` no longer says what holds.", names the file that holds each kind of item being changed. Where that depends on the kind, it says so.
> 8. (308) Two statements no longer disagree about how often `map.md` is read: the fenced block under `## The seven files`, which before this work describes `map.md` as "Read once per session.", and the sentence under `## Writing the map` "Every worker reads all of `map.md` once per node, so its size is a cost paid once per node." Which of them changes is the worker's choice.
>
> **Where the never-delete rule reaches**
>
> 9. (233) The file states this test in these words: *"text is rule-stating if an agent could act differently because of it today; it is record-stating if it only tells you what was already decided or done."*
> 10. (233) The file states that what a text is settles that a superseded version of it must never be left readable as though it still binds, and that where the superseded text goes is a second and separate question.
> 11. (233) The file states that where superseded text goes is settled by whether the file holding it already archives its own subject. A node file does, holding every superseded thing about its one node, so its superseded text stays in it. `map.md`, and every sibling of it that states rules that currently bind, does not, so its superseded text is appended verbatim to `map-history.md`.
> 12. (233) The file states four things about an implementation node's acceptance condition:
>     - it is rule-stating while its node is live;
>     - a superseded clause of one stays in the node file and is never appended to `map-history.md`;
>     - such a clause is marked superseded where the clause itself stands, rather than only recorded elsewhere in the node file;
>     - the reason is that the checker is handed the condition as text and does not read the node.
> 13. (233) Before this work, two statements disagree. The paragraph after the one opening "No edit deletes." says "Inside the graph's files, what happens to superseded text depends on the text's job, whichever file holds it." `## Writing the map` says "The graph's other files record what happened: `decisions.md`, `flags.md`, the node files, and `map-history.md`, which holds superseded text only. Superseded text in those files stays where it is." The second sorts by file what the first says is sorted by text. After this work the file does not both say the cut follows the text and sort the node files onto the record side because they are node files.
> 14. (233) The file still describes `map-history.md` as holding superseded text only and as never being rewritten.
> 15. (201) The paragraph stating that no edit to a graph file deletes also states, in its own text, that the rule does not reach removal performed by an act that is invoked and whose declared purpose is removal. It gives the reason as a property: the rule guards against deletion that is unannounced, and being invoked for that purpose is the announcement.
> 16. (201) That statement says what such an act leaves behind in place of what it removed: an entry naming what was removed and recording that the text remains recoverable from the effort's version control history. It states this as a property and names no command and no tool.
> 17. (201) The numbered check under `## Mechanical checks` requiring that every flag entry on a node has a matching line in `flags.md` states two things: a settled flag whose index line has been removed is not a mismatch, and an outstanding flag missing its index line still is one.
> 17a. *(node 148, by way of node 329's remainder R1.1)* *(node 148)* The sentence beginning "A path may say where:" states that such a path is written relative to the repository root, and states the reason: an absolute path names a machine, and the worker and the checker that read the condition may not be on it. The addition is at most two sentences. `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/` returns nothing after the work.
> 17b. *(node 43, by way of node 329's remainder R1.2)* *(node 43)* The sentence "Such a demand goes in the handover's `INVALIDATIONS` part, which names which resolved node the work contradicts and how." is reworded so the part covers any resolved node whose answer the work changes what it says. It names a rename, an extension, a narrowing and a contradiction. "A demand about the record as a whole belongs on the handover and in no condition, whatever its wording." is unchanged.
>
> **What does not change**
>
> 18. (233, 195) The numbered steps of `### Change the map` are unchanged in content, count and order.
> 19. (201, 233, 146) The numbered list under `## Mechanical checks` keeps its existing items, in their order and with their numbers. The only checks whose text changes are the one clause 17 names and the one clause 3 names. The work may add at most one new item, after the existing ones, stating that a superseded clause of an acceptance condition is marked where it stands.
> 20. (201, 195, 206) No procedure under `## Procedures` is reworded except as clause 7 states, and no section changes other than those clauses 1 to 17b name.
> 21. (228, 201, 233) The file names no file of an effort's directory other than the seven listed under `## The seven files`. Every markdown link in the file outside a fenced code block resolves to a path that exists, and the work adds no link to a path that does not exist.
> 22. (206) The file names no plugin, requires no skill to be invocable, and assumes no particular repository, machine or toolchain.
> 23. The working tree meets the bar.

*The manager's note, 2026-09-26:* [node 339](339-tie-graph-conventions-mds-mechanical-checks-to-the-writes-that.md)'s worker proposes, under its `NEW NODES`, a clause for this node: "Where the work adds a check, the act whose write can make the check false names it: in an existing check step, in a new step, or in the check's own text. This stays consistent with `### Who runs a check, and when`." It reports that this node's clause 20 forbids rewording any procedure except as its clause 7 states, so naming the new check in an existing check step would conflict. That goes to the human before this node is claimed.

## Answer

graph-conventions.md now places label vocabulary and fog in map-manager-only.md, and says map.md is read once per node. It gives the rule/record test, and says where superseded text goes turns on whether its file archives its own subject.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `968b1ec`. The node the worker surfaced is [node 343](343-say-in-the-five-worker-contracts-that-the-ground-rules-may-sit-in-a-sibling.md); its replacement phrase for node 56 is filed on node 56.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Say in graph-conventions.md which file of the map holds what, and where the never-delete rule reaches

ANSWER:
`.claude/skills/expedition/graph-conventions.md` was edited plainly, and no other file changed. Clause by clause:

- **The never-delete paragraph (clauses 15, 16).** The "No edit deletes." paragraph now says, in its own text, that the rule does not reach a removal made by an act that is invoked and whose declared purpose is removal. It gives the reason: the rule guards against deletion that is unannounced, and being invoked for that purpose is the announcement. It also says what such an act leaves in place of what it removed: an entry naming what was removed and recording that the text remains recoverable from the effort's version control history. No command and no tool is named. The text was put in the same paragraph, not a new one, because clause 15 says "the paragraph stating that no edit ... deletes also states, in its own text".
- **The old "depends on the text's job" paragraph was replaced by three paragraphs (clauses 9 to 14).**
  - The first gives the rule-stating/record-stating test in the exact words clause 9 requires. It says that what a text is settles that a superseded version must never be left readable as though it still binds, and that where the text goes is a second and separate question.
  - The second says where superseded text goes, settled by whether the file holding it already archives its own subject. A node file does, so its superseded text stays in it, marked where it stands. `map.md` and every sibling that states rules that currently bind do not, so their superseded text is appended verbatim to `map-history.md`. Record text such as a line in `decisions.md` or an entry in `flags.md` is marked superseded in place. `map-history.md` still holds superseded text only and is never rewritten.
  - The third says four things about an acceptance condition: it is rule-stating while its node is live; a superseded clause stays in the node file and is never appended to `map-history.md`; the clause is marked where it stands; and the reason is that the checker gets the condition as text and does not read the node.
- **`## Writing the map`, first paragraph (clause 13).** The sentences that put "the node files" on the record side by file ("The graph's other files record what happened: ... Superseded text in those files stays where it is.") were removed. In their place, the paragraph says that none of the map files archives its own subject, so their superseded text goes to `map-history.md`, as the opening paragraphs state.
- **`## The seven files` (clauses 1, 2, 8).**
  - The fenced block's `map.md` row now reads "Every worker reads it once per node." instead of "Read once per session." That matches `## Writing the map`, `map.md`'s own header and the glossary fix at node 224.
  - A sentence after the `map-manager-only.md` section list says that file holds the declared label vocabulary, where the effort declares one.
  - In the `## Notes` bullet, "The manager also maintains two things here: ..." was removed. The two optional blocks (ground rules, and the declaration of which sources are authoritative) now "live here unless the effort holds it in a sibling file of the map". The rest keeps its meaning. `map-implementation-rules.md` was already named for the bar's commands.
- **`## Writing the map`, further paragraphs (clauses 3, 6).**
  - The "Every note, standing preference and fog item" sentence now places notes and standing preferences in `map.md`'s `## Notes` and fog items in `map-manager-only.md`'s `## Not yet specified`.
  - The 500-byte target now names "the `## Notes` of `map.md`, and of any sibling of it that has one".
- **`### ## Acceptance condition` (clauses 17a, 17b).**
  - After "A path may say where: ...", one added sentence says such a path is written relative to the repository root, because an absolute path names a machine and the worker and checker may not be on it.
  - The `INVALIDATIONS` sentence now reads "which names every resolved node whose answer the work changes, and how it changes what that answer says: a rename, an extension, a narrowing or a contradiction." The "A demand about the record as a whole ..." sentence is unchanged.
- **`## Labels` (clauses 4, 5).** The first bullet now reads "A node uses only labels declared in the effort's label vocabulary, which `map-manager-only.md` holds." The other statements are byte-identical.
- **`### Change the map` (clauses 7, 18).** The opening now reads "a note or standing preference in `map.md`, or a fog item in `map-manager-only.md`". The numbered steps are unchanged.
- **`## Mechanical checks` (clauses 3, 17, 19).**
  - Check 6 gained two sentences: a settled flag whose index line has been removed is not a mismatch, and an outstanding flag missing its index line still is one.
  - Check 10 names the same two files as the target.
  - No other check changed, and no check was added. So the amendment's clause about naming an added check in an act is satisfied without any change, and no procedure's check step was reworded.

Where the node-339 quotes had moved: all of the condition's "before this work" quotes still matched `5c629f4` word for word. Only their positions had shifted.

INDEX LINE:    graph-conventions.md now places label vocabulary and fog in map-manager-only.md, and says map.md is read once per node. It gives the rule/record test, and says where superseded text goes turns on whether its file archives its own subject.

FLAGS:
- ASSUMPTION: The 500-byte target, and check 10, now name "the `## Notes` of `map.md`, and of any sibling of it that has one". I did not narrow them to `map.md`, because "the map's `## Notes`" already reached both files literally: the map includes its siblings, and `map-manager-only.md` has a `## Notes`. Clause 3 asks only that the file be named, so I kept the rule's current reach. Index: The 500-byte Notes target was named as covering map.md and any sibling with a Notes section, which keeps its existing reach rather than narrowing it to map.md.
- ASSUMPTION: For clause 8, the fenced block was changed to "Every worker reads it once per node", and the `## Writing the map` sentence was kept. That matches map.md's own header and the glossary fix at node 224. Index: The seven-files block now says every worker reads map.md once per node, aligning it with Writing the map, rather than the reverse.
- ASSUMPTION: Clause 19 allows one new check for a superseded condition clause being marked where it stands. I added none. Deciding by reading the files alone that a clause is superseded but unmarked is not mechanical, and ground rule 4 prefers the simpler text. So the amendment's clause, about naming an added check in an act, applies to nothing. Index: No mechanical check was added for marking superseded condition clauses in place, since it is not mechanically decidable; the amendment's check-naming clause is therefore vacuous.
- ASSUMPTION: The acceptance-condition paragraph (clause 12) sits among the opening never-delete paragraphs, not under `### ## Acceptance condition`. Clause 20 allows no section changes beyond those clauses 1 to 17b name, and clause 12 names no section. Index: The rule that superseded acceptance-condition clauses are marked in place was placed with the never-delete paragraphs, not the Acceptance condition subsection.

NEW NODES:
- Name: Say in the five worker contracts that the ground rules may sit in a sibling file of the map
  Kind: implementation
  Question: Each of the five worker contracts says "The map's `## Notes` may declare the effort's ground rules. It may also declare, by path or glob, which sources ...". `graph-conventions.md` now says those blocks live in `map.md`'s `## Notes` unless the effort holds them in a sibling file of the map, and this effort holds its ground rules in `map-implementation-rules.md`. Should the contracts say the same?
  Blockers: 338 (the graph-conventions wording lands first)
  Acceptance condition: In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`, the sentence beginning "The map's `## Notes` may declare the effort's ground rules." no longer requires the ground rules, or the declaration of which sources are authoritative, which are evidence only and which hold statements known to be false, to sit in `map.md`'s `## Notes`. It names the map as a whole, or says the blocks sit in `map.md`'s `## Notes` unless the effort holds them in a sibling file of the map. The rest of each contract's paragraph keeps its meaning. No other file changes. The files are shipped, so they are edited plainly. (Under map.md's grouping rule, this could instead join an open node against those five contracts, if one exists.)

INVALIDATIONS:
- Node 189 ("Where the never-delete rule stops") and node 194 ("Ship where the never-delete rule stops"): narrowed. Both say the cut follows the text's job and not the file, and that rule-stating text is replaced, not struck. The shipped file now says a text's kind settles only that its superseded version must never read as binding. Where the text goes follows whether the file archives its own subject. So a superseded clause of a live acceptance condition, which is rule-stating, is marked in place in its node file and not banked. This is node 199's answer, carried in. The map record repeats the old wording in two places: `map.md`'s never-delete preference ("Text whose job is to state a rule that currently binds is not struck in place") and `map-implementation-rules.md`'s paragraph "Which case a piece of text is in follows the text's own job and not the file it sits in". They now disagree with the shipped file on acceptance conditions.
- Node 139: extended. Its 500-byte target, "each item in the map's `## Notes`", now explicitly covers `map.md`'s and any sibling's `## Notes`.
- Node 70 ("Pruning a long-running effort's map"): extended. Its invoked cleanup act is now exempted from never-delete in the shipped text, which also says what it must leave behind.
- Nodes 13/59: the seven-files block's "Read once per session" for `map.md` is renamed to once per node, consistent with node 224.

CONDITIONS:
I searched the `## Acceptance condition` sections of all 87 open or claimed nodes, except this one, for: "once per session", "map's `## Notes`", "maintains two things", "which resolved node the work contradicts", "A path may say where", "other files record what happened", "text's job", "standing preference and fog item", "graph-conventions" and "label vocabulary". Matches: 56, 44, 337, 97, 109, 137, 190, 230, 284, 327, 340, 41, 80. I read only the matching passages.
- Node 56 (open), clause 4, says ground rules are "declared in its map's `## Notes`". That is now wrong for an effort holding them in a sibling. Replacement for that phrase: "declared in its map". The word "map" is fixed by the glossary, whose map entry covers `map.md` and its siblings, and by `graph-conventions.md`'s "`map-manager-only.md` and `map-implementation-rules.md` are part of the map" (shipped, `5c629f4`).
- Node 44 ("A path may say where the work must land"): still true, and it simply lacks the relative-path sentence. No replacement.
- Node 80 quotes `graph-conventions.md` wording that was already stale before this work. That is not caused by this work. No replacement.
- The other matches only name the file or the label vocabulary as a concept. No clause of theirs is made wrong.

MISSING FROM MAP: map.md does not say which file of the map holds a `## Notes` section, or whether the 500-byte target was meant for `map-manager-only.md`'s `## Notes` too. I got the fact that it has one from a heading grep of `map-manager-only.md`. I went on with an ASSUMPTION flag.

GATE PAYLOAD:
- Checker findings: none yet (no checker run).
- Bar: I confirmed against the repo that the worktree root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, with no manifest, build, tests, formatter or CI. That matches `map-implementation-rules.md`. The bar is therefore its non-command half. Wrap width is 104, as before. The only line over 104 is the pre-existing 105-character line in the node-file fenced block. `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/` returns nothing (exit 1).
- A note for the checker on clause 21: the only `](...)` forms outside fenced blocks are in `## Reading the graph` rule 3's examples (links to `95-...`, `103-...`, `139-...`). They sit inside double-backtick code spans, so they are code, not links. Node 339 added them, and this work did not touch them.
- Paths touched: `.claude/skills/expedition/graph-conventions.md` (in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/338-g1`). Nothing else.
- Proposed commit message:
  Say in graph-conventions.md which map file holds what, and where never-delete reaches

  Name map-manager-only.md for the label vocabulary and fog, and
  map-implementation-rules.md for the bar's commands. Let the ground
  rules and the source declaration sit in a sibling of the map. Say
  map.md is read once per node. State the rule/record test, and say
  where superseded text goes by whether its file archives its own
  subject. Mark superseded condition clauses in place. Exempt invoked
  removal acts. Write condition paths relative to the repo root, and
  widen what INVALIDATIONS names.

  Node: graph-workflow/338

RETROSPECTIVE
1. What I had to hunt for: which file of the map the 500-byte target meant. The node 146 question in its file, and node 139's condition, left it open. I found that `map-manager-only.md` has a `## Notes` through a heading grep. I also had to confirm that the node-339 quotes in the condition still matched, which meant reading the whole target file. They all did.
2. What arrived that this node did not need: most of `map.md` (about 40KB). Only the never-delete preference, the seven-files line and the header lines bore on this node. From `map-implementation-rules.md`, only the bar paragraph and the writing rules applied. The review-route history and the record-as-work paragraph did not. The contract's sections on raising, flags and correction rounds were not used this time.
3. What would have made this easier: the condition could have said which file the 500-byte target covers, since node 146's own question found two `## Notes`. The spawn could have listed the open nodes' ids, to save the status scan for the CONDITIONS search. The condition could also have pointed to where decisions.md's 189/194/199 lines are, for the INVALIDATIONS pass.
4. What was stale, wrong or contradictory:
   - Before this work, `map.md`'s never-delete preference and `map-implementation-rules.md` ("follows the text's own job and not the file it sits in") both disagree with node 199's answer, which this work ships.
   - The five worker contracts still place ground rules in "the map's `## Notes`", while this effort keeps them in `map-implementation-rules.md` (reported as a new node).
   - Node 80's condition quotes `graph-conventions.md` wording that no longer exists.
   - `map.md`'s `## Notes` paragraph beginning "This `## Notes` section also carries two optional blocks" says the ground-rules block lives in map.md, but its own next paragraph says the block moved to `map-implementation-rules.md`.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 336's check.*

> PASS
>
> Node 338, "Say in graph-conventions.md which file of the map holds what, and where the never-delete rule reaches". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/338-g1`, on base 5c629f4. `git status --short` shows one path, `.claude/skills/expedition/graph-conventions.md` (59 lines added, 35 removed). For the searches below I unwrapped the finished file into paragraphs with awk and ran `grep -noE` over the result. This PASS covers every part except the one under NOT COVERED.
>
> - **Scope:** met. The worktree status shows only this file changed: nothing under `.scratch/`, and no node file, decisions.md or flags.md. Superseded wording was removed plainly, with no strikethrough and nothing moved to a history file. The main tree's record is under NOT COVERED.
> - **1:** met. The sentence "The manager also maintains two things here: …" is gone from the `map.md` `## Notes` bullet. A grep for `vocabulary` and `bar's commands` finds that the file names a holder only as `map-manager-only.md` for the label vocabulary (the new sentence under `## The seven files`, and `## Labels`) and `map-implementation-rules.md` for the bar's commands. The rest of the bullet keeps its meaning.
> - **2:** met. The only statement about the ground rules and the source-declaration block now says "Each lives here unless the effort holds it in a sibling file of the map." A grep for `ground rules|authoritative` finds no other statement.
> - **3:** met. A grep for `` `## Notes` `` returns four hits:
>   - the `map.md` sections list, which is under `map.md`;
>   - `## Writing the map`, which names "`map.md`'s `## Notes`";
>   - the 500-byte target, which now reads "the `## Notes` of `map.md`, and of any sibling of it that has one";
>   - check 10, which uses the same wording.
>
>   Nothing still says "the map's `## Notes`".
> - **4, 5:** met. The first bullet of `## Labels` now reads "A node uses only labels declared in the effort's label vocabulary, which `map-manager-only.md` holds." The rule itself is unchanged. The diff shows the section's other four statements untouched.
> - **6:** met. The sentence now reads "Every note and standing preference in `map.md`'s `## Notes`, and every fog item in `map-manager-only.md`'s `## Not yet specified`, is a current statement". It names a separate file for each.
> - **7:** met. The opening of `### Change the map` now reads "a note or standing preference in `map.md`, or a fog item in `map-manager-only.md`".
> - **8:** met. The fenced block now reads "Every worker reads it once per node", which agrees with `## Writing the map`. A grep for `once per (session|node)` has no "session" hit.
> - **9:** met. The test appears word for word (unwrapped paragraph 13).
> - **10, 11:** met. The new paragraphs cover both points:
>   - what a text is settles that a superseded version must never read as binding, and where the text goes is a separate question;
>   - where it goes is settled by whether the file archives its own subject. A node file keeps its superseded text. `map.md` and its rule-stating siblings do not, so their superseded text goes to `map-history.md`.
> - **12:** met. The acceptance-condition paragraph states all four points: the condition is rule-stating while its node is live, a superseded clause stays in the node file, it is marked where the clause stands, and the reason is that the checker is handed the condition as text.
> - **13:** met. `## Writing the map` no longer lists the node files as record files. It now says the map files do not archive their subject. A grep for `records? what happened` returns only the opening paragraph's decisions.md and flags.md example.
> - **14:** met. "`map-history.md` holds superseded text only, and is never rewritten." is present.
> - **15, 16:** met. These are added inside the "No edit deletes." paragraph:
>   - the exception for an act that is invoked with removal as its declared purpose;
>   - the reason, that the rule guards against unannounced deletion and being invoked is the announcement;
>   - the entry left behind, which names what was removed and says it is recoverable from version control history.
>
>   No command or tool is named.
> - **17:** met. Check 6 gains "A settled flag whose index line has been removed is not a mismatch. An outstanding flag missing its index line still is one."
> - **17a:** met. One sentence is added: paths are relative to the repository root, because an absolute path names a machine the worker and checker may not be on. `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/` returns nothing (exit 1).
> - **17b:** met. The `INVALIDATIONS` sentence now covers "every resolved node whose answer the work changes, and how it changes what that answer says: a rename, an extension, a narrowing or a contradiction". The "A demand about the record as a whole…" sentence is unchanged.
> - **18:** met. The diff of `### Change the map` touches only the opening paragraph. Steps 1–3 are unchanged.
> - **19:** met. In the checks list only checks 6 and 10 differ. The numbering and order are unchanged, and no check was added.
> - **Amendment clause:** met, with nothing to do: no check was added.
> - **20:** met. Every hunk falls in the places clauses 1–17b name:
>   - the opening paragraphs;
>   - `## The seven files`, including the `map.md` sections list;
>   - `## Writing the map`;
>   - the `## Acceptance condition` subsection;
>   - `## Labels`;
>   - the opening of `### Change the map`;
>   - checks 6 and 10.
>
>   No other procedure is touched.
> - **21:** met. Listing every `*.md` name in the file finds, from an effort's directory, only the seven files (`nodes/NN-<name>.md` and `nodes/MM-<name>.md` stand for `nodes/`). The other names are shipped or repo files (`SKILL.md`, `CONTEXT.md`, `wayfinder-divergences.md`) or examples. Outside fenced blocks, the only `[..](..)` text is the three `Blocked by:` examples under `## Reading the graph`. They sit inside inline code spans, so they are code and not markdown links. That section predates this work, and the work adds no link.
> - **22:** met. A grep for `plugin|mattpocock` finds nothing. The added text names no tool, repository, machine or toolchain; "version control history" is stated as a property.
> - **23:** met. See the bar below.
>
> **The bar:** the repo has no build, tests, formatter or CI, so there are no commands to run. `git diff --check` is clean (exit 0). `awk 'length>105'` over the file prints nothing, so the file's wrap width holds.
>
> **Standards:** I read only the standards in map-implementation-rules.md, as in my earlier checks. The ones that bore on this work:
> - **`CONTEXT.md` `_Avoid_` lines:** checked by hand on the added text. Nothing found. The work removed one use of "session".
> - **The five writing rules:** citations are by heading, prohibitions stand beside their positive form, and there is no added bold.
> - **`/writing-for-agents`:** nothing found.
> - **The ground rules:** nothing assumes a repo, a machine or a toolchain, and nothing addresses the human.
>
> `/coding-principles` and `/naming` did not bear on this work, since it is prose with no new names. graph-conventions.md is the work itself, so I held its additions against the condition and against no element the work introduced. No reviewing skill is named, so I ran none. The condition says it came from no search, so there was no command to re-run.
>
> NOT COVERED:
> - "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*

## Interview

### The manager's raise, 2026-09-26

*The manager's own raise:* whether to add node 339's proposed clause to this node and widen clause 20 so the new check may be named in an existing check step (the manager's recommendation), or add it without widening, so the check names its act in its own text.

The human, `verbatim`: *"ok"* — taking the manager's recommendation: *"add G2's clause and widen G1's clause 20 so the new check can be named in an existing check step"*.

## Amendment, 2026-09-26 (from node 339, by the human's answer)

*The added clause was written by [node 339](339-tie-graph-conventions-mds-mechanical-checks-to-the-writes-that.md)'s worker under its `NEW NODES`, and is pasted as it wrote it. The widening of clause 20 is the manager's wording of the option the human took.*

- **A new clause, after clause 19.** "Where the work adds a check, the act whose write can make the check false names it: in an existing check step, in a new step, or in the check's own text. This stays consistent with `### Who runs a check, and when`."
- **Clause 20, widened.** Besides what clause 7 states, a procedure's existing check step may be reworded to name the check this work adds, and in no other way.

## Flags

`338.1` **· settled** `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* The widening of clause 20 is the manager's wording of the option the human took.

`338.2` **· settled** `ASSUMPTION` — The 500-byte target, and check 10, now name "the `## Notes` of `map.md`, and of any sibling of it that has one". I did not narrow them to `map.md`, because "the map's `## Notes`" already reached both files literally: the map includes its siblings, and `map-manager-only.md` has a `## Notes`. Clause 3 asks only that the file be named, so I kept the rule's current reach.

`338.3` **· settled** `ASSUMPTION` — For clause 8, the fenced block was changed to "Every worker reads it once per node", and the `## Writing the map` sentence was kept. That matches map.md's own header and the glossary fix at node 224.

`338.4` **· settled** `ASSUMPTION` — Clause 19 allows one new check for a superseded condition clause being marked where it stands. I added none. Deciding by reading the files alone that a clause is superseded but unmarked is not mechanical, and ground rule 4 prefers the simpler text. So the amendment's clause, about naming an added check in an act, applies to nothing.

`338.5` **· settled** `ASSUMPTION` — The acceptance-condition paragraph (clause 12) sits among the opening never-delete paragraphs, not under `### ## Acceptance condition`. Clause 20 allows no section changes beyond those clauses 1 to 17b name, and clause 12 names no section.
