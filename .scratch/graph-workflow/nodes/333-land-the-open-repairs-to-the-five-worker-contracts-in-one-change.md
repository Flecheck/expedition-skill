# Land the open repairs to the five worker contracts in one change

Type: implementation
Status: resolved
Supersedes: 326, 155, 303, 60, 148, 43, 57, 81, 331
Blocked by: none

## Question

Open nodes 326, 155, 303 and 60, and the worker-contract parts of 148, 43 and 57, each change a few lines of the five worker contracts and each forbids any other change, so none can run beside another. Make all of their changes in one node.

*Proposed by [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker and filed by the manager, on the human's "ok" to node 329's merge and its conflicts' recommendations.* *The manager's note:* under option 7(a), the `graph-conventions.md` parts of 148 and 43 go to the manager-contract merge and the `CONTEXT.md` part of 57 to [node 335](335-qualify-the-glossarys-research-entry-for-the-research-raise.md); option O1–O3 is therefore not used and is left out below. Option O4 (node 81's entry 3) was taken and is clause J. [Node 331](331-give-each-question-in-a-multi-question-payload-a-context-line.md) is folded in as clause K, on the manager's proposal; the manager widened clause I1's two "B to H" to "B to H, J and K" so the fence covers them.

## Acceptance condition

*Written by node 329's worker, with clause J from its option O4 and clause K from node 259's worker. Assembled by the manager as noted above.*

The work is these five files, paths relative to the repository root. "The five files" below means them.
- `.claude/skills/expedition-grilling/SKILL.md`
- `.claude/skills/expedition-implementation/SKILL.md`
- `.claude/skills/expedition-precondition/SKILL.md`
- `.claude/skills/expedition-prototype/SKILL.md`
- `.claude/skills/expedition-research/SKILL.md`

Done means every one of the following is true of the finished tree. Each clause is tagged with the node it came from.

**A. The shared sections**
A1. *(node 329)* Before this work, the sections headed `## When you raise a flag` and `## When a node you report is an implementation node` are the same text in all five files. The only difference is that the research file has no blank line after the last one. After the work they are still the same text in all five, and every change clauses B and C make inside them is made identically in each.

**B. Who writes a condition** *(node 326)*
B1. The first sentence under `## When a node you report is an implementation node` today reads: "An `implementation` node can be claimed only once it carries an **acceptance condition**: what done means for that node, written by the node that spawned it, before any work on it starts." After the work, it no longer says without qualification that the condition is written by the node that spawned it. It says the condition is written before any work on the node starts, by the agent that created the node, or by the manager where the manager created it.
B2. The next sentence, "When you report one, your node is the one that spawned it, so write its condition in the `NEW NODES` block as the node will hold it.", is unchanged.

**C. Relative paths** *(node 148)*
C1. The bullet in that section beginning "A path may say where, because the checker has the repo" states that such a path is written relative to the repository root. It also states the reason: an absolute path names a machine, and the worker and the checker that read the condition may not be on it. The addition is at most two sentences.
C2. The rule is stated in words and never by showing an absolute path as an example. `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/` returned 0 occurrences when this condition was written, and returns nothing after the work.

**D. Searching the record** *(node 155)*
D1. Each file's `## What you read` section opens "Read each of the following. Do not trust any summary of them." and then gives a bulleted list of pointers. In the research file the list is followed by "You may read outside the working directory." and then "Leave `flags.md` unread. It is not yours.". In the other four, the `flags.md` line follows the list directly. Each file gains one passage inside `## What you read`, placed after the bulleted list, stating all four of the following:
  a. the bulleted pointer list is what the worker reads whole, and the rest of the effort's record is searched rather than read;
  b. a worker that needs a fact it cannot place searches the record for it before opening any file whole, and a file of the record that is not on the pointer list is opened because a search led to it;
  c. the search is narrowed before anything is read: establish which files match, narrow the phrase, then read what matched. The reason is that a broad term can return more text than the file it was meant to spare;
  d. this governs facts held in the record and never the rules the worker is held to. Those arrive in the spawn and in the files the pointer list names, and a worker never goes looking for a standard it is to be judged against.
D2. The passage names a property and never a command. It contains no occurrence of `grep`, `rg`, `ripgrep`, `ls`, `find`, `awk`, `sed` or any other executable name, names no tool as required, and describes searching as something the worker's environment provides.
D3. Nothing is removed from any of the five pointer lists, and no existing bullet is reworded. Each file keeps "- `decisions.md` — the sections the spawn names" byte-identical, and that index remains a file the worker reads whole.
D4. "Leave `flags.md` unread. It is not yours." is unchanged in each file. The added passage neither licenses searching `flags.md` nor mentions it.
D5. `.claude/skills/expedition-checker/SKILL.md` tells its own reader to search the work under review. The added passage does not duplicate, restate or contradict that instruction. Where it needs to relate the two, it cites that file by path instead of repeating what it says.
D6. The added passage is at most 1,200 bytes in each file. The five may share wording verbatim.

**E. The search for conditions the worker's own work makes wrong** *(node 303; wording from `.claude/skills/expedition/SKILL.md`, `### Changing one after it is written`)*
E1. Each file states, addressed to its worker and in its own text rather than as a pointer to another file, all of the following:
  - before handing back, the worker searches the open nodes' `## Acceptance condition` sections for what its own work fixes: each word it refuses, each path it changes or moves something out of, and each phrase it supersedes;
  - it reads only what matches;
  - the search covers every open node's condition, claimed or not;
  - it names on its handover what it searched for.
E2. Each file also states that where the worker's work establishes a fact that makes a clause of an unclaimed node's condition wrong, the worker writes the replacement as text on its handover. Every word of the replacement must already be fixed by a resolved node, by work landed in the tree, by the glossary or by the shipped files, and the replacement names which of those fixed it.
E3. *(node 329)* Each file says which part of its handover carries what E1 and E2 produce. It may be an existing part or a new one. Where it is a new part, clause G7 applies to it.

**F. Widening `INVALIDATIONS`** *(node 43)*
F1. Each file's handover block has one line of the form `INVALIDATIONS: <which resolved node your ... contradicts, and how>`. Today it reads "your answer contradicts" in grilling and prototype, "your facts contradict" in research, and "your work contradicts" in precondition and implementation. After the work, each line asks for any resolved node whose answer this work changes what it says, not only one it contradicts. It names four kinds inline: a rename, an extension, a narrowing and a contradiction. Each file keeps its own noun (`answer`, `facts`, `work`).
F2. Each file states, in prose near that line, that an outright contradiction is the minority case and a renamed term or a narrowed rule the ordinary one.
F3. Each file still carries "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them." unchanged. The shared-section bullet "Put a demand about the record as a whole, such as that the work contradicts no decision or that everything in it traces back to one, on `INVALIDATIONS` and in no condition. No copy can repair such a demand." is also unchanged.

**G. What the map did not say** *(node 60)*
G1. Each file's handover gains one part labelled `MISSING FROM MAP:`, listed among the parts its handover block names.
G2. Each file says in its own voice what goes there: anything about the effort the worker needed that `map.md` did not tell it, and where it got that instead or how it went on without it.
G3. Each file says this part never blocks. The worker does not wait for an answer, and nothing in its handover depends on one.
G4. Each file says `none` is written there in full when the worker has nothing for it.
G5. Where a file describes a route for something its worker cannot go on without (the question shape, or the raise), it says this part is not that route.
G6. `MISSING FROM MAP` appears in the five files and in no other file under `.claude/`.
G7. *(nodes 60 and 329)* Every statement a file makes about how many parts its handover has matches the parts its handover block lists after the work. Today those statements are "Hand back all five parts every time." (grilling, precondition, prototype), "Hand back one handover with all five parts, every time." (research) and "Write all six parts of the handover every time" (implementation).

**H. A research worker's raise** *(node 57)*
H1. The research file gives its worker a raise on the same threshold and in the same terms as `.claude/skills/expedition-precondition/SKILL.md` states under `## When the premise is broken`. Those terms are:
  - raise if any one of three triggers holds:
    - "the broken thing is not yours to change: a resolved node your node depends on, or the size of your own node" (test: "is the broken thing mine to fix?");
    - "the decision affects more than this node" (test: "if I pick wrong, what else has to change?");
    - "you cannot choose alone, because the choice is genuinely open and you hold no recommendation you believe" (test: "can I state a `RECOMMENDED` I believe?");
  - to raise, hand back the question shape about the broken premise, then stop and wait;
  - the human answers either Continue (resume the work) or Stop (you are finished: write nothing more, and hand nothing more back);
  - where no trigger holds, decide the matter yourself, continue, and hand back one `ASSUMPTION` flag.

  Where that wording depends on something untrue of a research node, the research file says the true thing instead, and the handover reports the difference.
H2. The research file's hard rule 3 today reads "Do your work without the human. You have no way to reach the human, and nothing you hand back waits on them." It is no longer stated as written. Its replacement keeps what is still true, that a research node's ordinary work never involves the human and nothing it hands back waits on them, and states the exception H1 creates.
H3. The raise is not a new kind of return. It reuses the question shape the precondition file uses, with the fields `NODE`, `ABOUT`, `SO FAR`, `ASK`, `RECOMMENDED` and `ALTERNATIVES`.
H4. *(node 329)* The research file no longer says anything the raise makes false. Today it says "The manager spawned you and is waiting for one handover.", "A research node never involves the human." and "Hand back one handover with all five parts, every time."

**I. What else may change**
I1. *(the union of the fences of 326, 155, 148, 43, 57 and 60)* No text in the five files is deleted, shortened or reworded except where clauses B to H, J and K demand it. No hard rule is reworded except the research file's hard rule 3 (H2). No heading, bullet, hard rule or clause is renumbered. Text may be added only where clauses B to H, J and K demand it.
I2. No file other than the five changes. In particular `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md` and `CONTEXT.md` are unchanged, and no file under `.scratch/` changes.
I3. The working tree meets the bar.

**J. The prototype contract's code slot line** *(node 81, entry 3; the worker's option O4)*
J1. In the prototype file's `## Words used exactly`, the line "- **code slot** — the right to modify product code, held by one worker at a time. It is never yours." no longer says "held by one worker at a time". It says that one worker holds one slot, and that how many slots an effort runs is that effort's own setting. It keeps "It is never yours." and stays a single line in that list's form. Hard rule 1's sentence "You do not hold the code slot." is unchanged.

**K. A context line for each question** *(node 331, from node 259; the whole of node 331's condition, as its worker wrote it)*
In `.claude/skills/expedition-grilling/SKILL.md`, under the heading `### question — you need the human`:
1. In the fenced block that shows the shape for more than one question, each of the two example questions (Q1 and Q2) has a line beginning `CONTEXT:`, with the field name padded to the same column as the other field names. The line is placed after that question's `Q<n>. <short title>` line and before its `ASK:` line. Its placeholder says that the line holds why this one question is asked, and that the line is left out when the question needs none.
2. The fenced block that shows the shape for one question contains no `CONTEXT:` line and is otherwise unchanged.
3. The prose of that section states each of the following:
   a. In both shapes, `ASK` holds only the question, in a sentence or two.
   b. `CONTEXT` belongs to the multi-question shape only. It holds why its question is asked, and it is left out when there is nothing of that kind to say.
   c. A finding that explains why the recommendation is recommended goes in that question's `RECOMMENDED`, after the recommendation itself.
   d. A fact that more than one question in the payload rests on goes in `SO FAR`.
4. The sentence that lists what each question in the multi-question shape carries (today: a number, a short title, its own recommendation, and the alternatives it sets aside) also names the optional context line.
5. ~~No other part of the file changes what it requires, and no other file under `.claude/` is changed.~~ *The manager's note: this fence of node 331's own is replaced by clause I, the fence over the union, as node 329's worker did for every replaced node's fence.*

## Answer

The five worker contracts gain the record search, the open-condition search in a new `CONDITIONS` part, a widened `INVALIDATIONS`, `MISSING FROM MAP`, relative paths, a research raise, and grilling's `CONTEXT` line.

*The manager's note:* the worker's answer is under `## Handover, attempt 1` and its correction round. The checker failed run 1 on clause D4 and passed run 2. The human approved. The work landed as commit `5acd220`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Land the open repairs to the five worker contracts in one change

ANSWER:
All of clauses A to K are made in the worktree `.scratch/graph-workflow/worktrees/333-worker-contracts-merge`, uncommitted, in the five files `.claude/skills/expedition-{grilling,implementation,precondition,prototype,research}/SKILL.md`. No other file changed. All five files keep their 105-column wrap.

- **A, B, C: the shared sections.** One script made the same edit in all five files, and all five still agree once trailing blank lines are stripped. The research file still ends with no blank line.
  - B: the first sentence of `## When a node you report is an implementation node` now says the condition is "written before any work on it starts, by the agent that created the node, or by the manager where the manager created it". The next sentence is word for word the same and has only been rewrapped.
  - C: the path bullet gained one sentence: "Write the path relative to the repository root, because an absolute path names a machine, and the worker and the checker that read the condition may not be on it." It shows no example path. The C2 search returns nothing.
- **D: searching the record.** One passage of 779 bytes, the same in all five files, goes directly after the bulleted list in `## What you read`. In research it sits before "You may read outside the working directory." It states (a) to (d) and names no command. The checker contract is not mentioned, because nothing needs relating to it. The list, the `decisions.md` bullet and the `flags.md` line are unchanged.
- **E: the condition search.** Each file gets a paragraph after its handover block, in its own text. It says to search the open nodes' `## Acceptance condition` sections for each word the work refuses, each path it changes or moves something out of, and each phrase it supersedes. It covers every open node, claimed or not, and says to read only what matches. It then covers the replacement text, the four sources a replacement's words may come from, and naming those sources.
  - E3: what this search produces goes in a **new** handover part, `CONDITIONS:`. It sits after `INVALIDATIONS`, and its placeholder asks for what was searched and each replacement clause with what fixed its words.
- **F: INVALIDATIONS.** The line now reads `<which resolved node your {answer|facts|work} changes, and how: a rename, an extension, a narrowing or a contradiction of what it says>`, and each file keeps its own noun. A new sentence under the block says an outright contradiction is the minority case and a renamed term or a narrowed rule the ordinary one. Both F3 sentences are unchanged.
- **G: MISSING FROM MAP.** A new part `MISSING FROM MAP:` goes after `CONDITIONS`. In implementation it sits before `GATE PAYLOAD`. A paragraph says:
  - what goes there;
  - `none` is written in full when there is nothing for it;
  - it never blocks;
  - it is not the route for something the worker cannot go on without. That route is named per file: the question shape for grilling, prototype and precondition (by their headings), `### The raise` for implementation, and `## When the premise is broken` for research.
  - G6: the label appears in these five files and nowhere else under `.claude/`.
  - G7: the part counts now read "all seven parts" (grilling, precondition, prototype, research) and "all eight parts" (implementation). Like the old "five" and "six", the count leaves out the `HANDOVER:` name line.
- **H: the research raise.** A new section `## When the premise is broken` sits between `## How you research` and `## What you hand back`. It has:
  - the precondition file's three-trigger table, word for word;
  - "To raise, end your turn and make your entire final output the question shape below, about the broken premise instead of a fact. Then stop and wait.";
  - a question shape with NODE / ABOUT / SO FAR / ASK / RECOMMENDED / ALTERNATIVES;
  - the Continue and Stop answers, word for word;
  - the ASSUMPTION-flag fallback, word for word.

  Other research text changed to match:
  - Hard rule 3 now reads: "Do your ordinary work without the human, and hand back nothing that waits on them. The one exception is a raise under `## When the premise is broken`. It is your only way to reach the human, and it stops your work until they answer."
  - H4, first statement: the intro now says the manager is waiting "for one handover, or for a raise where your premise is broken".
  - H4, second statement: "A research node's ordinary work never involves the human, and you raise only when your premise is broken."
  - H4, third statement: "When you have finished, hand back one handover with all seven parts."

  Where the precondition wording is untrue of research, the research file says the true thing instead. These are the differences:
  - The shape sits inside the raise section rather than under `## What you hand back`, which in research holds only the handover.
  - "instead of a step of the work" becomes "instead of a fact".
  - "end your turn and make your entire final output" is taken from precondition's hard rule 4, because research has no rule about putting a question.
  - ABOUT reads "what fact this node establishes, and why it is being established now" instead of "what this node unblocks".
  - SO FAR reads "what you established" instead of "what you have already done".
  - ASK is "<one question>", with no checklist option, because a research node reserves no step for a person.
  - Precondition's sentence that the flag settles at the close report was not carried over. H1 does not list it, and I1 fences extra text.
- **J: the code slot line.** The prototype line now reads "the right to modify product code, held by one worker. Each effort sets how many code slots it runs. It is never yours." This follows the implementation contract's wording. Hard rule 1 is unchanged.
- **K: the grilling context line.** Both example questions in the multi-question shape gain `CONTEXT:       <why this one question is asked; leave the line out when the question needs none>`, padded to column 16. The one-question shape is unchanged. The "Number each question" sentence now names "an optional context line". One paragraph after the block states 3a to 3d.
- **The bar.** The repo has no build, no tests, no formatter and no CI: there is no manifest, and `.gitignore` invokes nothing. That matches the rules file's record, and I found no difference from it. `git diff --check` is clean. The prose was held against `/writing-for-agents` and `CONTEXT.md`'s `_Avoid_` lines, and "return" was replaced by "match" in the search passage for that reason.
- **Condition search run on this work.** I searched the open and claimed nodes' conditions for "five parts", "six parts", "contradicts, and how", "one worker at a time", "node that spawned it", "never involves the human", "MISSING FROM MAP", "INVALIDATIONS" and "without the human". Nothing outside node 333 is made wrong except where noted under NEW NODES:
  - Node 332's code-slot clause removes the same phrase from the glossary, so the two agree.
  - Node 338's clause 17b widens INVALIDATIONS in the same direction.
  - Node 335 already covers the glossary's research entry.

INDEX LINE:    The five worker contracts gain the record search, the open-condition search in a new `CONDITIONS` part, a widened `INVALIDATIONS`, `MISSING FROM MAP`, relative paths, a research raise, and grilling's `CONTEXT` line.

FLAGS:
- ASSUMPTION: E3 is carried by a new `CONDITIONS` part rather than by `INVALIDATIONS`. `INVALIDATIONS` is about resolved nodes, and F1 fixes its placeholder to that. The manager also files a condition amendment differently from a cascade over resolved nodes. Putting both in one part would make the manager split them apart. The cost is one more part in every handover.
  Index: The open-condition search and its replacement clauses are handed back in a new `CONDITIONS` handover part rather than folded into `INVALIDATIONS`.
- ASSUMPTION: `MISSING FROM MAP:` is longer than the 15-column field padding of the handover blocks. I left every existing line's padding untouched rather than re-pad the whole block, which I1 would have read as a rewording. The new label takes one space, and its continuation line is indented under its own value, as the park shape does.
  Index: `MISSING FROM MAP:` overruns the handover blocks' field padding, and the existing lines were left un-padded rather than realigned.
- ASSUMPTION: For G7, the part counts leave out the `HANDOVER:` name line, as the existing "five" and "six" did. So they read seven for four kinds and eight for implementation.
  Index: Handover part counts keep excluding the name line: seven parts for four worker kinds, eight for implementation.
- ASSUMPTION: For D2, I read "executable name" as the name of a command. The passage also avoids ordinary words that are common command names, "find", "which" and "more", wherever that was possible.
  Index: The record-search passage avoids even ordinary words that are common command names, such as "find", "which" and "more".
- ASSUMPTION: For J1, I read "a single line in that list's form" as one list entry. The entry wraps at 105 columns like its neighbours, because no wording that says both things fits in one physical line.
  Index: The prototype code-slot entry is one list entry wrapped to two lines, since no wording saying both things fits in one.
- ASSUMPTION: For D1, "after the bulleted list" is read as directly after it. In research the passage therefore precedes "You may read outside the working directory."
  Index: In the research contract the record-search passage sits directly after the list, before the read-outside-the-directory line.

NEW NODES: none. Found defects go to existing nodes or to the manager:
1. `.claude/skills/expedition/SKILL.md`, the bullet beginning "A handover has five parts every time", becomes stale once this lands: it lists five parts plus a sixth. This file was off limits under I2. Proposed clause for node 336 or 337, both open and unclaimed. I cannot tell which is the related one, so the manager places it. The clause can only be filed after node 333 lands, because until then its words are fixed only by this work:
   "(node 333) The bullet in `.claude/skills/expedition/SKILL.md` beginning 'A handover has five parts every time' lists the parts the worker contracts' handover blocks list: the answer, the index line, the flags, the nodes surfaced, which resolved node the work changes (`INVALIDATIONS`), the open conditions searched and any replacement clauses (`CONDITIONS`), and what `map.md` did not say (`MISSING FROM MAP`). That is seven parts, and it says an implementation worker returns an eighth, the gate payload."
2. The `**Handover**:` entry in `CONTEXT.md` lists five things and will be stale too. Node 332 is claimed, so its condition stays as written. The manager should place this, perhaps in node 56 or a later glossary node.
3. The map's retrospective bullet says the retrospective is the "sixth" or "seventh" handover part. It will now be the eighth (four kinds) and the ninth (implementation). That is the manager's record.
4. Node 37, a grilling node, has a `## Question` that quotes the old `INVALIDATIONS` line. It is question text, not a condition, so no amendment is owed, but the quote will be out of date.
5. Observation: the glossary defines "the record" narrowly, as answers, statuses, index lines and flags. The D passage, following its clause, uses "the effort's record" in `map.md`'s wider sense, meaning the effort's files. That conflicts with the glossary.

INVALIDATIONS: Read from `decisions.md` index lines only, so confidence is moderate.
- Node 35 (A worker's handover carries no acceptance condition for the node it mints) is narrowed. Its "the node that spawned it" is now "the agent that created the node, or the manager where the manager created it".
- Node 22 (Write the worker contract skills: "each carrying ... every return variant") is extended. The research contract now has a raise as a second way to hand back, and every handover gains two parts.

GATE PAYLOAD:
- Checker findings: none yet. The checker has not run.
- Paths touched, all in the worktree:
  - `.claude/skills/expedition-grilling/SKILL.md`
  - `.claude/skills/expedition-implementation/SKILL.md`
  - `.claude/skills/expedition-precondition/SKILL.md`
  - `.claude/skills/expedition-prototype/SKILL.md`
  - `.claude/skills/expedition-research/SKILL.md`
  - A scratch copy of the shared sections, written under `$TMPDIR` for comparison only. It is outside the repo.
- Proposed commit message:

  Land the open repairs to the five worker contracts

  Each worker contract now searches the record before reading files whole, runs the open-condition search and hands it back in a new CONDITIONS part, widens INVALIDATIONS to renames, extensions and narrowings, and adds MISSING FROM MAP. The shared sections say who writes a condition and that condition paths are repo-relative. Research gains a premise raise, prototype's code-slot line drops "one at a time", and grilling's multi-question shape gains a CONTEXT line.

  Node: graph-workflow/333

Skipped from a method skill: nothing. `/writing-for-agents` was read as a standard and has no conflicting part here.

RETROSPECTIVE
1. What I had to hunt for:
   - Which open node owns the manager contract's "A handover has five parts" bullet. I looked at 338 (graph-conventions only), then 336 and 337, and could not tell which fits.
   - Whether the glossary refuses "return" (yes, for the handover concept).
   - How the existing part counts treat the name line (they leave it out), which I inferred from the blocks.
2. What arrived that this node did not need:
   - Most of `map.md`: the standing preferences on payload timing, diff commands, resume, token priority and the worktree route. Only the Notes line on grouping mattered.
   - Most of the rules file's history paragraphs. Only the bar's commands, the ground rules and the five writing rules were used.
   - In `decisions.md` only about five lines bore on this work. A narrower search did the job without reading the file whole.
3. What would have made this easier:
   - A spawn line saying which open node owns `expedition/SKILL.md`'s handover-parts bullet, or that none does.
   - A line in the node file saying which handover parts the manager contract enumerates. G's knock-on effect on the manager contract and the glossary is predictable from the condition, so node 329 could have filed it together with the other clauses.
   - The condition could say whether E3 prefers an existing part. The choice changes every future handover.
4. What was stale, wrong or contradictory:
   - The map's retrospective bullet ("sixth"/"seventh") becomes wrong with this work.
   - The glossary's narrow "record" conflicts with D's wide "the effort's record", which `map.md`'s never-delete bullet also uses.
   - The research contract's Words entry "worker — ... no contact with the human" now sits a little awkwardly beside the raise. The implementation contract has the same wording beside its own raise, so I left it under I1.
   - D2's "any other executable name" cannot be met literally, because many ordinary English words are also command names.

## Review

### Checker run 1 — `FAIL: acceptance condition`

*The checker's own text, pasted, 2026-09-26. A fresh checker, spawned for this node rather than resumed, because the checker used so far carried close to 500k tokens.*

> FAIL: acceptance condition
>
> ### Finding 1: the added search passage licenses searching `flags.md` (clause D4)
>
> - **Instances.** The added passage in `## What you read` of all five files opens: "Read everything the list above names in full, and search the rest of the effort's record instead of reading it." It goes on: "Open a file of the record that is not on the list above only because a search led you to it."
>   - `flags.md` is not on any of the five pointer lists. The glossary counts it as part of the record: `CONTEXT.md`, entry **Manager**, says "The record is every answer, status, index line and flag". So "the rest of the effort's record" includes `flags.md`, and nothing in the passage carves it out.
>   - The passage also sets searching against reading ("search ... instead of reading it"). That lets the unchanged line after it, "Leave `flags.md` unread. It is not yours.", be read as forbidding reading `flags.md` but not searching it.
>   - Read literally, then, the passage tells the worker to search `flags.md`, to read whatever matches there, and to open the file once a search leads to it. D4 requires that the passage "neither licenses searching `flags.md` nor mentions it".
>   - Sites: grilling line 44, implementation line 54, precondition line 47, prototype line 45, research line 35, all under `.claude/skills/expedition-<kind>/SKILL.md` in the worktree. Found by reading the passage against `CONTEXT.md`'s definition of the record.
>   - The condition can be met: the passage can limit its scope without naming the file, for example to the record apart from any file this section tells you to leave unread.
> - **Form.** Wording in the added passage that directs or permits searching, reading matches in, or opening any record file that is not on the pointer list, with no exception for the file the section leaves unread.
> - **Extent.** `grep -rn "search the rest of the effort's record" .claude/skills/` lists exactly the five passage sites above, all in text the worker may edit. The passage is byte-identical in all five files, so one repair applies to all five.
>
> ### Clauses established (everything except D4 above, and the part not covered below)
>
> - **A1.** I pulled out the two shared sections from base `64db5aa` and from the work, and compared them by md5 and diff. After the work, grilling, implementation, precondition and prototype are identical. Research differs only by the missing trailing blank line, which was already the case in the base.
> - **B1 and B2.** The first sentence now reads "written before any work on it starts, by the agent that created the node, or by the manager where the manager created it" in all five files. The words of B2's sentence are unchanged; the lines are only rewrapped.
> - **C1.** One sentence was added to the "A path may say where" bullet in all five files, and it gives the reason.
> - **C2.** I ran the recorded command `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/` in the worktree. It returned nothing (exit 1), which matches the recorded 0 occurrences.
> - **D1 a to d.** Each point is present in the passage, which sits after the bulleted list. In research it sits before "You may read outside the working directory."
> - **D2.** I searched the passage for the whole words grep, rg, ripgrep, ls, find, awk, sed, cat, head, tail and git, and found none. It says "Your environment provides the search, and no particular tool is required."
> - **D3.** No pointer bullet was changed. "- `decisions.md` — the sections the spawn names" occurs once in each file.
> - **D4.** "Leave `flags.md` unread. It is not yours." occurs once in each file, and the passage does not mention `flags.md`. The licence part of D4 is failed above.
> - **D5.** The passage says nothing about the checker and restates nothing the checker contract says.
> - **D6.** The passage is 777 bytes in each file.
> - **E1 to E3.** Each file has its own paragraph covering the searched sections, what is searched for, "read only what matches", "claimed or not", naming what was searched, and the replacement with what fixed its words. All of it goes to a new `CONDITIONS:` part, which G7 covers.
> - **F1 and F2.** Each `INVALIDATIONS` line now asks which resolved node the work changes, names the four kinds, and keeps its own noun (answer, facts, work). The sentence about the minority case follows each block.
> - **F3.** Both sentences are unchanged. I found the NEW NODES sentence once per file, and the shared-sections comparison covers the record-as-a-whole bullet.
> - **G1 to G5.** Each file has a `MISSING FROM MAP:` part and a paragraph saying what goes there, that it never blocks, and that `none` is written in full. The paragraph names the route it is not: the question shape in grilling, prototype and precondition, and the raise in implementation and research.
> - **G6.** `grep -rln 'MISSING FROM MAP' .claude/` returns only the five files.
> - **G7.** I counted the fields in each handover block, excluding the `HANDOVER:` header line, as the base counts did. That gives 7 in grilling, precondition, prototype and research, and 8 in implementation, which matches the text's "seven" and "eight". No other statement of a part count appears in the five files.
> - **H1 and H3.** The research file's new `## When the premise is broken` section is checked against the precondition file:
>   - The trigger table is copied from the precondition file word for word.
>   - The raise uses the question shape with NODE, ABOUT, SO FAR, ASK, RECOMMENDED and ALTERNATIVES. The shape is given inline, because research has no question shape under `## What you hand back`.
>   - The section gives Continue and Stop in the precondition terms, and the `ASSUMPTION` fallback when no trigger holds.
>   - Two adaptations are made in the file: "instead of a fact", and the shape given in the section itself.
> - **H2.** Hard rule 3 has been replaced. It keeps that ordinary work involves no human and that nothing handed back waits on them, and it states the raise as the exception.
> - **H4.** The three quoted statements have been rewritten. The research glossary still says a worker has "no contact with the human". I do not count that as made false: the implementation file has a raise and uses the same wording.
> - **I1.** I read the whole diff. Every change traces to clauses B to H, J or K. No heading, bullet or hard rule was renumbered.
> - **I2.** `git status` in the worktree shows only the five files, with nothing untracked.
> - **J1.** The line now reads "- **code slot** — the right to modify product code, held by one worker. Each effort sets how many code slots it runs. It is never yours." Hard rule 1's sentence "You do not hold the code slot." is unchanged.
> - **K1 to K4.** The `CONTEXT:` lines are in Q1 and Q2 after the title line and before `ASK:`, and their values start in the same column (16) as the other fields. The single-question block is not touched. The new prose paragraph covers a to d. The listing sentence now names "an optional context line".
>
> NOT COVERED:
> - H1, "and the handover reports the difference". That report is the worker's handover to the manager, which is outside the paths I was given.
>
> **Bar.** The repo has no build, tests, formatter or CI: the worktree root holds only `CONTEXT.md`, with no manifest or task runner. So the bar is its non-command half.
> - `git diff --check` printed nothing (exit 0).
> - The only lines over the files' usual width are the two research table rows. They are copied from the precondition file, where the same rows already exist.
>
> **Standards.** I read `.scratch/graph-workflow/map-implementation-rules.md`, and read only its standards. They are `/coding-principles`, `/naming`, the `_Avoid_` lines in `CONTEXT.md`, `graph-conventions.md`, `/writing-for-agents`, the five ground rules and the five standing rules for writing.
> - Those that bore on this work were the ground rules, the writing rules, `/writing-for-agents` and the `_Avoid_` lines.
> - On the `_Avoid_` lines, I checked the distinctive refused words by hand. The added text has no refused word used for its refused concept. "refuses" and "payload" appear in wording the condition dictates, and in senses other than the refused ones.
> - No reviewing skill is named for this repo, so I ran none. I read the `/writing-for-agents` standard myself and ran no part of it in another agent.
> - The work changes no standard.
> - The work is `.claude/` files, not the effort's own record, so the rules file's rule about record paths did not apply.

## Handover, attempt 1, correction round 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted; its first line, "HANDOVER:      Land the open repairs to the five worker contracts in one change", precedes it.*

CORRECTION ROUND 1: I fixed the checker's one D4 finding by rewording the search passage, and changed nothing else. The fix did not touch any text clause D5 or D6 is about, beyond keeping the passage well under 1,200 bytes.

ANSWER:
Clauses A to K are made in the worktree `.scratch/graph-workflow/worktrees/333-worker-contracts-merge`, uncommitted. The work is in the five files `.claude/skills/expedition-{grilling,implementation,precondition,prototype,research}/SKILL.md`, and no other file changed. All five files keep their 105-column wrap.

- **A, B and C: the shared sections.** One script made the same edit in all five files, and the sections still match once trailing blank lines are stripped. The research file still ends with no blank line.
  - **B:** The first sentence of `## When a node you report is an implementation node` now says the condition is "written before any work on it starts, by the agent that created the node, or by the manager where the manager created it". The next sentence is unchanged and only rewrapped.
  - **C:** The path bullet gains one sentence: "Write the path relative to the repository root, because an absolute path names a machine, and the worker and the checker that read the condition may not be on it." It shows no example path, and the C2 search returns nothing.
- **D: searching the record.** One passage, the same in all five files, sits directly after the bulleted list in `## What you read`. In research it comes before "You may read outside the working directory." It is 840 bytes and reads:
  "Read everything the list above names in full. Search the rest of the effort's record instead of reading it, leaving out any file this section tells you to leave unread. Where you need a fact you cannot place, search for it in that way before you open any file whole. Open a file of the record that is not on the list above only because such a search led you to it. Narrow a search before you read its results: establish the files that match, narrow the phrase, then read what matched. A broad term can match a longer text than the file it was meant to spare. Your environment provides the search, and no particular tool is required. This governs the facts the record holds, and never the rules you are held to. Those arrive in the spawn and in the files the list above names, and you never go looking for a standard you are judged against."
  - What it may search excludes the file the section leaves unread, without naming `flags.md`. Nothing in it licenses searching that file (D4).
  - It names no command and does not mention the checker contract.
  - The pointer lists, the `decisions.md` bullet and the `flags.md` line are unchanged.
- **E: the condition search.** Each file has a paragraph after its handover block, in its own text. It says to search the open nodes' `## Acceptance condition` sections for each word the work refuses, each path it changes or moves something out of, and each phrase it supersedes. The search covers every open node's condition, claimed or not, and the worker reads only what matches. The paragraph also covers writing replacement text, with its four permitted sources, and naming what was searched for.
  - **E3:** What this produces is carried by a new part, `CONDITIONS:`, placed after `INVALIDATIONS`.
- **F: widening `INVALIDATIONS`.** The line now reads `<which resolved node your {answer|facts|work} changes, and how: a rename, an extension, a narrowing or a contradiction of what it says>`. Each file keeps its own noun.
  - A sentence under the block says an outright contradiction is the minority case, and a renamed term or a narrowed rule the ordinary one.
  - Both sentences F3 protects are unchanged.
- **G: `MISSING FROM MAP`.** The new part sits after `CONDITIONS`, and in implementation before `GATE PAYLOAD`. A paragraph says:
  - what goes in it;
  - that `none` is written there in full when there is nothing for it;
  - that it never blocks;
  - that it is not the route for something the worker cannot go on without. That route is the question shape (grilling, prototype, precondition), `### The raise` (implementation), or `## When the premise is broken` (research).
  - **G6:** The label appears only in these five files under `.claude/`.
  - **G7:** The count statements now read "all seven parts" (grilling, precondition, prototype, research) and "all eight parts" (implementation). The count leaves out the `HANDOVER:` name line, as the old counts did.
- **H: the research raise.** A new section, `## When the premise is broken`, sits between `## How you research` and `## What you hand back`. It has:
  - the precondition file's three-trigger table, word for word;
  - "To raise, end your turn and make your entire final output the question shape below, about the broken premise instead of a fact. Then stop and wait.";
  - a NODE / ABOUT / SO FAR / ASK / RECOMMENDED / ALTERNATIVES shape;
  - the Continue and Stop answers, word for word;
  - the fallback of deciding the matter yourself and handing back one `ASSUMPTION` flag, word for word.

  The rest of the research file changes to match:
  - **Hard rule 3** now reads: "Do your ordinary work without the human, and hand back nothing that waits on them. The one exception is a raise under `## When the premise is broken`. It is your only way to reach the human, and it stops your work until they answer."
  - **H4:** The intro says the manager is waiting "for one handover, or for a raise where your premise is broken". The node-kind line says "A research node's ordinary work never involves the human, and you raise only when your premise is broken". The handover line says "When you have finished, hand back one handover with all seven parts."

  Differences from the precondition wording, each replacing something untrue of a research node:
  - The question shape sits in the raise section, because research's `## What you hand back` holds only the handover.
  - "instead of a step of the work" becomes "instead of a fact".
  - "end your turn and make your entire final output" is taken from precondition's hard rule 4.
  - ABOUT reads "what fact this node establishes, and why it is being established now".
  - SO FAR reads "what you established".
  - ASK has no checklist option, because a research node reserves no step for a person.
  - Precondition's sentence about when the flag settles is not carried over. H1 does not list it, and clause I1 fences it out.
- **J: the prototype code slot line.** It now reads "the right to modify product code, held by one worker. Each effort sets how many code slots it runs. It is never yours." Hard rule 1 is unchanged.
- **K: grilling's context line.** Both example questions in the multi-question shape gain `CONTEXT:       <why this one question is asked; leave the line out when the question needs none>`, padded to column 16.
  - The one-question shape is unchanged.
  - The sentence beginning "Number each question" now names "an optional context line".
  - One new paragraph states 3a to 3d.
- **The bar.** The repo has no build, no tests, no formatter and no CI. `.gitignore` invokes nothing. This matches the rules file's record, with no difference to report. `git diff --check` is clean. The prose was held against `/writing-for-agents` and `CONTEXT.md`'s `_Avoid_` lines.
- **The condition search run on this work.** I searched open and claimed nodes' conditions for: "five parts", "six parts", "contradicts, and how", "one worker at a time", "node that spawned it", "never involves the human", "MISSING FROM MAP", "INVALIDATIONS" and "without the human". Nothing outside node 333 is made wrong, apart from the defects listed under NEW NODES.
  - Node 332's code-slot clause agrees with J.
  - Node 338's clause 17b widens `INVALIDATIONS` the same way F does.
  - Node 335 covers the glossary's research entry.

INDEX LINE:    The five worker contracts gain the record search, the open-condition search in a new `CONDITIONS` part, a widened `INVALIDATIONS`, `MISSING FROM MAP`, relative paths, a research raise, and grilling's `CONTEXT` line.

FLAGS:
- ASSUMPTION: **E3.** The condition search is carried by a new `CONDITIONS` part rather than by `INVALIDATIONS`. `INVALIDATIONS` concerns resolved nodes, and F1 fixes its placeholder to that. An amendment to a condition is also filed differently from a cascade over resolved nodes. The cost is one more part in every handover.
  Index: The open-condition search and its replacement clauses are handed back in a new `CONDITIONS` handover part rather than folded into `INVALIDATIONS`.
- ASSUMPTION: **Padding.** `MISSING FROM MAP:` is longer than the handover blocks' 15-column field padding. The existing lines were left un-padded rather than realigned, because under I1 a realignment would count as rewording. The new part's continuation line is aligned under its own value, as in the park shape.
  Index: `MISSING FROM MAP:` overruns the handover blocks' field padding, and the existing lines were left un-padded rather than realigned.
- ASSUMPTION: **Part counts.** They leave out the `HANDOVER:` name line, as the old "five" and "six" did.
  Index: Handover part counts keep excluding the name line: seven parts for four worker kinds, eight for implementation.
- ASSUMPTION: **Command names (D2).** I read "executable name" as a command name. The passage also avoids ordinary words that are also common command names, "find", "which" and "more", wherever that was possible.
  Index: The record-search passage avoids even ordinary words that are common command names, such as "find", "which" and "more".
- ASSUMPTION: **The code slot line (J1).** I read "a single line in that list's form" as one list entry. It wraps to two lines like its neighbours, because no wording that says both things fits in 105 columns.
  Index: The prototype code-slot entry is one list entry wrapped to two lines, since no wording saying both things fits in one.
- ASSUMPTION: **Passage placement (D1).** I read "after the bulleted list" as directly after it. In research, the passage therefore comes before the line allowing reads outside the working directory.
  Index: In the research contract the record-search passage sits directly after the list, before the read-outside-the-directory line.
- ASSUMPTION: **Excluding `flags.md` (D4, correction round 1).** The passage has to exclude `flags.md` from what may be searched without naming it. I did that by pointing at the section's own instruction: "leaving out any file this section tells you to leave unread". This follows the checker's suggestion. I also changed "search the record for it" to "search for it in that way", so the later sentences cannot be read as reaching the whole record.
  Index: The record-search passage excludes, without naming it, any file its section says to leave unread, which keeps `flags.md` out of its licence.

NEW NODES: none. Defects this work creates in files I was not allowed to touch:
1. **The manager contract.** In `.claude/skills/expedition/SKILL.md`, the bullet "A handover has five parts every time" goes stale once this work lands. The proposed clause below is for node 336 or node 337, both open and unclaimed; the manager chooses which. It can be filed only after 333 lands:
   "(node 333) The bullet in `.claude/skills/expedition/SKILL.md` beginning 'A handover has five parts every time' lists the parts the worker contracts' handover blocks list: the answer, the index line, the flags, the nodes surfaced, which resolved node the work changes (`INVALIDATIONS`), the open conditions searched and any replacement clauses (`CONDITIONS`), and what `map.md` did not say (`MISSING FROM MAP`). That is seven parts, and it says an implementation worker returns an eighth, the gate payload."
2. **The glossary.** The `**Handover**:` entry in `CONTEXT.md` lists five things. Node 332 is claimed, so the manager needs to place this.
3. **The map.** The retrospective bullet in `map.md` counts the retrospective as the sixth or seventh part. It becomes the eighth, or the ninth on an implementation node.
4. **Node 37.** Its `## Question` quotes the old `INVALIDATIONS` line. It is question text, so no amendment is owed.
5. **"The record".** The glossary defines the record narrowly, as every answer, status, index line and flag. Clause D uses "the effort's record" in `map.md`'s wider sense, meaning the effort's files. The checker's finding rested on the glossary's definition, which includes flags, and that is why the passage now excludes the unread file.

INVALIDATIONS: These come from `decisions.md` index lines only, so confidence is moderate.
- Node 35 is narrowed: "the node that spawned it" becomes "the agent that created the node, or the manager where the manager created it".
- Node 22 is extended: the research contract gains the raise as a second way to hand back, and every handover gains two parts.

GATE PAYLOAD:
- **Checker Finding 1 (D4: the passage licensed searching `flags.md`).**
  - The second sentence now reads "Search the rest of the effort's record instead of reading it, leaving out any file this section tells you to leave unread."
  - "search the record for it" became "search for it in that way".
  - "only because a search led you to it" became "only because such a search led you to it".
  - The passage is still the same in all five files, and still mentions neither `flags.md` nor the checker. It grew from 779 to 840 bytes.
  - Nothing else changed.
- **Paths touched, all in the worktree:**
  - `.claude/skills/expedition-grilling/SKILL.md`
  - `.claude/skills/expedition-implementation/SKILL.md`
  - `.claude/skills/expedition-precondition/SKILL.md`
  - `.claude/skills/expedition-prototype/SKILL.md`
  - `.claude/skills/expedition-research/SKILL.md`
  - A scratch comparison file under `$TMPDIR`, outside the repo.
- **Proposed commit message:**

  Land the open repairs to the five worker contracts

  Each worker contract now searches the record before reading files whole, runs the open-condition search and hands it back in a new CONDITIONS part, widens INVALIDATIONS to renames, extensions and narrowings, and adds MISSING FROM MAP. The shared sections say who writes a condition and that condition paths are repo-relative. Research gains a premise raise, prototype's code-slot line drops "one at a time", and grilling's multi-question shape gains a CONTEXT line.

  Node: graph-workflow/333

RETROSPECTIVE (new this round only): What was contradictory is the one new item.
- The checker read "record" using the glossary's definition, which includes flags. I had written the passage using the map's wider sense of the effort's files.
- Neither reading makes the D4 exclusion automatic, and D1's own wording, "the rest of the effort's record", creates the gap.
- Either of two things would have prevented the round: an explicit carve-out in D1, or a note that the glossary counts flags as record.

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-09-26, after correction round 1. The same checker as run 1, resumed.*

> Node 333, re-check after correction round 1
>
> PASS
>
> What changed: I diffed the whole of `git diff` against the diff I read last round. The only content that moved is the added search passage in `## What you read`, the same in each of the five files; every other difference is a hunk line number shifting by one. That matches the worker's statement, and I found no change it does not mention. `git status --short --untracked-files=all` still lists only the five files.
>
> - D4, last round's Finding 1, now met: The passage now says "Search the rest of the effort's record instead of reading it, leaving out any file this section tells you to leave unread." In all five files, "Leave `flags.md` unread. It is not yours." sits inside `## What you read`: an awk extract of that section finds it exactly once in each. The exclusion therefore covers `flags.md`. "search for it in that way" and "such a search" point back to that narrowed search, so nothing in the passage licenses searching `flags.md` any longer. A whole-word search of the unwrapped passage finds no "flags" or "flags.md".
> - D1 a to d: re-read against the new text. (a) The list is read in full, and the rest of the record is searched instead. (b) The worker searches "in that way" before it opens any file whole, and opens a file that is not on the list only "because such a search led you to it". (c) and (d) are unchanged.
> - D2: a whole-word search of the unwrapped passage for grep, rg, ripgrep, ls, find, awk, sed, cat, head, tail and git finds nothing. The passage still says "Your environment provides the search, and no particular tool is required."
> - D5: the same search finds no "checker" in the passage, and it neither restates nor contradicts the checker contract.
> - D6: the passage is 840 bytes in each file, counting its lines with their newlines and excluding the blank line after it. The five copies have the same md5, so they are byte-identical.
> - D3 and I1: the change sits wholly inside the added passage. No pointer-list bullet and no existing text moved.
> - C2: I re-ran the recorded command, `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/`. It returned nothing (exit 1), which matches the recorded return of 0 occurrences.
> - G6: `grep -rln 'MISSING FROM MAP' .claude/` still returns only the five files.
> - Everything else I established last round is untouched by the change and stands: A1, B1, B2, C1, D1 as a whole, E1 to E3, F1 to F3, G1 to G7, H1 to H4, I2, J1, and K1 to K4. The two shared sections are outside `## What you read`, so A1 still holds.
>
> NOT COVERED:
> - H1, "and the handover reports the difference": the worker's handover is outside the paths I was given, so this PASS does not cover that part.
>
> The bar: I re-ran it in full. The repo has no build, no tests, no formatter and no CI, so only its remaining half, the standards, applies. `git diff --check` printed nothing (exit 0).
>
> Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`. It has not changed since commit 084aae9. The standards that bore on this work are the five ground rules, the five standing rules for writing, `/writing-for-agents`, and the `_Avoid_` lines of `CONTEXT.md`. I held the passage against them by hand and found no breach. The first sentence was split, and each sentence now carries one idea. The standards file is not among the changed paths, so no standard moved. The rules name no reviewing skill, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve, you can start a fresh checker"*

## Flags

`333.1` **· settled** `ASSUMPTION` — **E3.** The condition search is carried by a new `CONDITIONS` part rather than by `INVALIDATIONS`. `INVALIDATIONS` concerns resolved nodes, and F1 fixes its placeholder to that. An amendment to a condition is also filed differently from a cascade over resolved nodes. The cost is one more part in every handover.

`333.2` **· settled** `ASSUMPTION` — **Padding.** `MISSING FROM MAP:` is longer than the handover blocks' 15-column field padding. The existing lines were left un-padded rather than realigned, because under I1 a realignment would count as rewording. The new part's continuation line is aligned under its own value, as in the park shape.

`333.3` **· settled** `ASSUMPTION` — **Part counts.** They leave out the `HANDOVER:` name line, as the old "five" and "six" did.

`333.4` **· settled** `ASSUMPTION` — **Command names (D2).** I read "executable name" as a command name. The passage also avoids ordinary words that are also common command names, "find", "which" and "more", wherever that was possible.

`333.5` **· settled** `ASSUMPTION` — **The code slot line (J1).** I read "a single line in that list's form" as one list entry. It wraps to two lines like its neighbours, because no wording that says both things fits in 105 columns.

`333.6` **· settled** `ASSUMPTION` — **Passage placement (D1).** I read "after the bulleted list" as directly after it. In research, the passage therefore comes before the line allowing reads outside the working directory.

`333.7` **· settled** `ASSUMPTION` — **Excluding `flags.md` (D4, correction round 1).** The passage has to exclude `flags.md` from what may be searched without naming it. I did that by pointing at the section's own instruction: "leaving out any file this section tells you to leave unread". This follows the checker's suggestion. I also changed "search the record for it" to "search for it in that way", so the later sentences cannot be read as reaching the whole record.
