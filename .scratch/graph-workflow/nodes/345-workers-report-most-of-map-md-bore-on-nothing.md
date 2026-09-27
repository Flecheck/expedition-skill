# Workers report that most of `map.md` bore on nothing their node needed

Type: grilling
Status: resolved
Blocked by: none
Supersedes: 246

## Answer

The map's bloat is fixed in what it holds: the shipped no-sweep clause is relaxed, then the manager moves manager-only and implementation-only items and each item's account out of `map.md` in one pass.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The node the worker surfaced is [node 346](346-allow-a-sweep-of-a-map-file-in-graph-conventions-md.md); once it lands the manager makes the pass itself, folding in nodes 80 and 256. Flags 345.1 and 345.2 settle at the node closing report.

## Question

Every worker reads all of `map.md` (about 42 KB) once per node, and one after another reports in its retrospective that almost none of it bore on its node. What should change so that a worker reads what its node needs: a smaller `map.md`, more of it moved into siblings read by one kind of reader, a lighter read for some nodes, or something else?

*Minted by the manager under the human's standing rule that a second report of the same retrospective item gets a node. On 2026-09-27 alone the item was reported by the workers of nodes 337, 340, 342, 327, 202, 137 and 344. Node 344's worker, on a two-file term swap: "nearly all of `map.md` (about 42 KB), which the contract makes me read in full. None of it bore on a two-file term swap." Node 327's worker: "nearly all of `map.md` (about 58KB read whole). Only the `## Notes` bullet on grouping by file (the node-327 bullet) bore on this node." Node 137's worker: "Most of `map.md` (about 41 KB), read whole because the contract requires it: the worktree route, token and credit strategy, the retrospective rule's history." The human's own ask that opened this session's work also said the skills feel long and could be compacted. Related, resolved: [node 139](139-move-the-managers-material-out-of-the-map.md) moved the manager's material out and set a soft size target per item; open: [node 256](256-collapse-the-two-map-notes-the-priority-list-subsumes.md) and [node 182](182-whether-map-sections-are-priced-by-the-shadow-instrument.md).*

## Interview

### Attempt 1

#### Question 1, relayed 2026-09-27

*The worker's payload, pasted as handed back.*

```
NODE:          345, Workers report that most of `map.md` bore on nothing their node needed
ABOUT:         Every worker reads all of `map.md` (42,098 bytes) on every node, and seven workers today said almost none of it applied to their node. This node decides where the fix goes: in what the map holds, or in what a worker has to read.
SO FAR:        I read the map, node 136 (which set the map's admission test), node 139, nodes 256 and 182, the part of `graph-conventions.md` on writing the map, and the manager's spawn section. What I found:
               - The rule already exists and the map breaks it. Node 136 settled that `map.md` holds only what *every* worker can act on, and that material for one kind of reader goes to a sibling file. `graph-conventions.md` ships this as "each file of the map declares its reader".
               - I measured the `## Notes` items. About 16.6 KB of them only change what the manager does: one question at a time and the two-grilling target (2,071 bytes), payload release (738), the gate diff command (1,072), never idle (1,296), the last line of a report (707), flags settle at close (1,721), the retrospective rule (4,001, the largest item, which the spawn carries anyway), token priority (1,141), the standing yes (687), resume (1,774), the spent moved-standard licence (808), and the never-ask-which pointer (597). The worktree paragraph (1,687) matters only to implementation nodes. Together that is about 18 KB, over 40% of the file.
               - Items are also long. Most are between 1 and 4 KB against the 500-byte soft target, because they carry the story of how the rule was learned, which the conventions say belongs in `map-history.md`.
               - Why the map doesn't shrink: the admission test is applied only by "whoever is already editing a passage", and a sweep of the file is "neither owed nor permitted". That no-sweep clause was a side-effect named by node 191's worker. You didn't object to it, but it isn't in your words. Since nobody edits old items, they never get moved out. Also, the manager writes new standing rules (such as today's standing yes) into `map.md` even when they are manager-only.
               - Changing the reading side instead runs into the contracts: a worker "never goes looking for a standard it is judged against". Rules have to arrive in the files it is told to read. If `map.md` were made search-only, any rule in it that binds a worker would become one it may never see.
               I settled nothing on my own authority yet.
ASK:           Should the fix be to what `map.md` holds, with a one-time pass that applies the existing "who reads this" test to the whole file, rather than to what a worker is required to read?
RECOMMENDED:   Fix what the map holds. Do it with one pass now, as an implementation node: move the manager-only items verbatim to `map-manager-only.md`, move the worktree paragraph to `map-implementation-rules.md`, and move each remaining item's account to `map-history.md`, bringing items toward 500 bytes. Nothing is deleted, and each file keeps a one-line pointer. It rests on three things. The test is already settled (node 136), so this is enforcement, not a new rule. What goes wrong today is that nothing ever applies the test to items nobody is editing. And the reading-side options conflict with "rules arrive in what you read". On my rough count `map.md` would end up at about 15 to 20 KB, well under half its size. Details come in later questions: whether the no-sweep clause is lifted for good or only for this one pass, and whether the manager checks an item's reader each time it writes one.
ALTERNATIVES:  - Lighten the reading requirement: workers read the Destination and search `## Notes` instead of reading it whole. This is cheaper at once, but a worker can miss a rule that binds it, which the contracts forbid.
               - A lighter read for some kinds of node, for example a small term-swap implementation node reading only the rules file. This saves on small nodes only, and adds a per-kind exception to every contract.
               - Wait for node 182's per-section shadow measurement before moving anything. This is better evidence, but it is blocked on runs the manager has not done, while seven reports a day show the same thing.
               - Both: sweep the map and also make `map.md` search-only. This saves the most, but has the same missed-rule problem as the first alternative.
```

#### The human's answer to question 1, 2026-09-27

The human, `verbatim`: *"ok for recommended"*. The recommendation it takes, the worker's: "Fix what the map holds. Do it with one pass now, as an implementation node: move the manager-only items verbatim to `map-manager-only.md`, move the worktree paragraph to `map-implementation-rules.md`, and move each remaining item's account to `map-history.md`, bringing items toward 500 bytes. Nothing is deleted, and each file keeps a one-line pointer."

#### Question 2, relayed 2026-09-27

*The worker's payload, pasted as handed back.*

```
NODE:          345, Workers report that most of `map.md` bore on nothing their node needed
ABOUT:         This node decides how to stop every worker paying for all of `map.md` (42,098 bytes) when most of it bears on nothing their node needs. Where the fix goes is settled. One point about how it is carried out is left.
SO FAR:        Your answer to Q1, verbatim: "ok for recommended". So the fix is to what `map.md` holds, by one pass that applies the existing "who reads this" test to the whole file:
               - manager-only items move verbatim to `map-manager-only.md`
               - the worktree paragraph moves to `map-implementation-rules.md`
               - each remaining item's account of how its rule was learned moves to `map-history.md`, bringing items toward the 500-byte target
               - nothing is deleted, and each file keeps a one-line pointer.
               One correction to my recommendation, settled on my own authority because the shipped contract decides it. I had said "as an implementation node". But `.claude/skills/expedition/SKILL.md`, `## Writing the graph`, states that a change confined to the graph's files, meaning the map, its siblings, the history file, the indexes and the node files, is the manager's own. It is made with no node, no acceptance condition, no worker, no checker and no gate. So the manager makes the pass itself. I will hand this back as an ASSUMPTION flag.
               One thing I also settled myself: no new rule is needed for the manager's future writes to the map. `graph-conventions.md` already applies the reader test to "whoever is already editing a passage", and that includes the manager writing a new item. New manager-only items landing in `map.md` is a failure to follow that rule, not a missing rule. This will also be an ASSUMPTION flag.
               What is left: the shipped `graph-conventions.md` (`## Writing the map`) says of the reader test "The test requires no sweep of a file, and permits none." The pass you approved is exactly such a sweep, so as things stand it breaks a shipped rule. That "permits none" clause came from node 191's worker as a side-effect you did not object to. It is not in your words.

Q2. Whether the no-sweep clause changes for good, or this effort gets a one-time exception
ASK:           Should the shipped rule change so that a sweep of a map file is not owed but is allowed, or should this effort's map record a one-time exception for this pass and leave the shipped rule as it is?
RECOMMENDED:   Change the shipped rule. A small node edits `.claude/skills/expedition/graph-conventions.md` so the sentence says a sweep is not owed, and drops "and permits none". The manager makes the pass once that lands. The ground is that the ban is the reason the map never shrinks. Items nobody edits never meet the test, which is why the map has regrown after nodes 59, 136 and 139. Any effort that runs long will hit the same wall, so a one-off exception would only postpone the next one. The edit is one clause in one file.
ALTERNATIVES:  - One-time exception: a note in this effort's `map.md` licenses this single pass, and the shipped rule stays. It is faster, since there is no node, but the next effort hits the same wall.
               - A permanent lift with a trigger: a sweep is allowed only when retrospectives report a file mostly unused twice. It is more precise, but the rule that mints a node on a second report already brings the question up, and this adds a mechanism for no gain.
               - Keep the ban and do no pass: the map shrinks only as items happen to be edited. This contradicts your answer to Q1.
```

#### The human's answer to question 2, 2026-09-27

The human, `verbatim`: *"ok for recommended"*. The recommendation it takes, the worker's: "Change the shipped rule. A small node edits `.claude/skills/expedition/graph-conventions.md` so the sentence says a sweep is not owed, and drops "and permits none". The manager makes the pass once that lands."

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      345, Workers report that most of `map.md` bore on nothing their node needed

ANSWER:        **The fix is to what `map.md` holds, not to what a worker is required to read. It is carried out by one pass over the whole file, which the shipped rules are changed to allow.**

               **Why the map holds what nobody reads.** The rule was never missing. [Node 136](136-the-map-has-grown-back-what-node-59-saved.md) settled that `map.md` holds only what *every* worker can act on, and `graph-conventions.md` ships the test as "each file of the map declares its reader". Measured on 2026-09-27, `map.md` is 42,098 bytes. About 16.6 KB of its `## Notes` change only what the manager does: one question at a time and the two-grilling target, payload release, the gate diff command, never idle, the last line of a report, flags settling at close, the retrospective rule (4,001 bytes, the largest item, and carried by the spawn anyway), token priority, the standing yes, resume, the spent moved-standard licence, and the never-ask-which pointer. The worktree paragraph (1,687 bytes) matters only to implementation nodes. Most items also run to 1 to 4 KB against the 500-byte soft target, because they carry the account of how the rule was learned. What keeps the map from shrinking is the clause "The test requires no sweep of a file, and permits none". Under it the test reaches only a passage someone is already editing, so old items never meet it. That clause came from node 191's worker as a consequence the human did not contradict. It was never in the human's words.

               **Why the reading side was not changed.** Every worker contract says a worker never goes looking for a standard it is judged against, so rules must arrive in the files it is told to read. Making `map.md` search-only, or exempting some kinds of node from it, would let a worker miss a rule that binds it. The human's word on Q1, verbatim: "ok for recommended".

               **What is settled:**
               1. **The shipped no-sweep clause changes.** In `.claude/skills/expedition/graph-conventions.md`, `## Writing the map`, a sweep of a map file becomes not owed but allowed: "and permits none" goes. The duplicate statement in `map-implementation-rules.md` ("no sweep of the file is owed or licensed by it") is brought into line in the same node. The human's word on Q2, verbatim: "ok for recommended".
               2. **Once that lands, the manager makes one pass over `map.md`**, as its own change to the graph's files, with no node:
                  - each `## Notes` item whose only reader is the manager moves verbatim to `map-manager-only.md`'s `## Notes`
                  - the worktree paragraph moves verbatim to `map-implementation-rules.md`
                  - each remaining item's account moves verbatim to `map-history.md` under the `Change the map` procedure, bringing items toward 500 bytes
                  - `map.md` keeps a one-line pointer to each sibling. Nothing is deleted.
                  A rough estimate puts `map.md` at 15 to 20 KB afterwards.
               3. **No new rule governs later writes to the map.** The shipped test already binds whoever edits a passage, the manager writing a new item included.

INDEX LINE:    The map's bloat is fixed in what it holds: the shipped no-sweep clause is relaxed, then the manager moves manager-only and implementation-only items and each item's account out of `map.md` in one pass.

FLAGS:         ASSUMPTION: The recommendation the human approved said the pass would be "an implementation node". Under `.claude/skills/expedition/SKILL.md`'s `## Writing the graph`, a change confined to the graph's files is the manager's own, with no node, condition, checker or gate, so the answer makes it the manager's. The substance approved, meaning what moves where and that nothing is deleted, is unchanged. The manager relayed that fact as its own note, and the human's reply did not address it.
               Index: Node 345's map pass was reassigned from an implementation node to the manager's own change, because the shipped file test makes a graph-files-only change the manager's.

               ASSUMPTION: No new rule was asked for about the manager's future writes to `map.md`. `graph-conventions.md` already applies the reader test to whoever edits a passage, a new item included, so a manager-only item written into `map.md` is non-compliance and not a gap.
               Index: Node 345 added no rule for the manager's map writes, holding that the shipped reader test already binds a new item's writer.

NEW NODES:     **Allow a sweep of a map file, in `graph-conventions.md`**
               Kind: implementation.
               Question: The shipped reader test forbids a sweep of a map file, so items nobody edits never meet it and the map regrows. Relax that to "not owed, but allowed".
               Blockers: none.
               Acceptance condition:
               > The work edits `.claude/skills/expedition/graph-conventions.md` and
               > `.scratch/graph-workflow/map-implementation-rules.md`, and, where the latter's superseded text must be kept,
               > `.scratch/graph-workflow/map-history.md`. No other file changes. Done means all of the following hold.
               >
               > 1. In `.claude/skills/expedition/graph-conventions.md`, under `## Writing the map`, the sentence "The test
               >    requires no sweep of a file, and permits none." is replaced by a statement that no sweep of a file is
               >    owed and that one is allowed. The sentence before it ("Whoever is already editing a passage applies that
               >    test to that passage.") is unchanged. No other sentence of the file changes.
               > 2. In `.scratch/graph-workflow/map-implementation-rules.md`, the clause "no sweep of the file is owed or
               >    licensed by it" is replaced so that the file says no sweep is owed and one is allowed, and no longer says
               >    one is not licensed. The superseded sentence, as it stood before this work, appears verbatim in
               >    `.scratch/graph-workflow/map-history.md` under a heading mirroring the section it came from.
               > 3. No file in `.claude/` or `CONTEXT.md` still states that a sweep of a map file is forbidden or not
               >    licensed. Check it with a case-insensitive search for "sweep" across those paths.
               > 4. The bar applies as it does to any implementation node.
               Then, once it lands, the manager makes the pass described in this node's answer, point 2, as its own change with no node.

INVALIDATIONS: [Node 191](191-the-rules-file-carries-accounts-rather-than-rules.md) and [node 197](197-ship-what-a-file-of-the-map-admits.md): narrowed. Their "never as a sweep" / "no sweep … owed or licensed" consequence keeps "not owed" and loses "not licensed". The rest of each (the admission test, trigger against history, the move to `map-history.md`) stands.
               [Node 136](136-the-map-has-grown-back-what-node-59-saved.md): extended, not contradicted. Its test "what every worker can act on" is kept and is now enforced by a pass rather than left to passages being edited.

CONDITIONS:    I searched every open and claimed node's `## Acceptance condition` for "permits none", "sweep", "no sweep", "graph-conventions.md" and "Writing the map".
               - [Node 230](230-point-map-manager-only-at-the-admission-test-that-binds-it.md), clause 3, forbids restating "that no sweep is owed". That is still true after this answer, so no replacement is needed.
               - No other matching clause is made wrong, and I write no replacements.
               Two open nodes are affected by the pass. The pass is not landed yet, so I write no replacement for either:
               - [Node 256](256-collapse-the-two-map-notes-the-priority-list-subsumes.md) names two `map.md` `## Notes` items (never idle, payload goes over) that the pass moves to `map-manager-only.md`. Once the pass lands, its clause 1's path `.scratch/graph-workflow/map.md` becomes wrong.
               - [Node 80](80-map-items-nodes-64-and-68-left-stale.md) edits `map.md` items the pass also rewrites.
               Both are confined to the graph's files, so under the file test in `.claude/skills/expedition/SKILL.md` they fall to the manager too. The manager may fold them into the pass instead of fixing their paths.

MISSING FROM MAP: none. The facts I needed about the map (reader test, size target, siblings, the no-sweep clause) are in `graph-conventions.md`, node 136 and node 191. I found them by search from the manager's pointers.

RETROSPECTIVE:
1. **What I had to hunt for:**
   - Where the no-sweep clause came from, and whether it was the human's. Found in node 191's `## Answer` and the manager's note around line 113, after searching "sweep" across nodes 191 and 197.
   - That `map-implementation-rules.md` states the clause a second time. Found by a "sweep" search across the map's siblings.
   - The per-item byte sizes. I computed them with a script, since the record holds no current count.
2. **What arrived that this node did not need:**
   - Very little of `map.md` bore on the node as work, but here the map was the node's subject, so reading it whole was the work itself.
   - Node 136's full file came back through one broad `sed` (51 KB). I needed only its `## Answer`. Listing the headings first would have spared it.
3. **What would have made this easier:**
   - A spawn note that the map pass is the manager's own under the file test. It arrived as a correction, and my first recommendation named the wrong route.
   - A current per-item size report of `map.md`. Mechanical check 10 in `graph-conventions.md` would produce one, if its output were kept somewhere a worker could read.
4. **What was stale, wrong or contradictory:**
   - `map.md`'s first line says whether the split is right is "settled by measurement", and points at node 60, which is superseded.
   - Node 182's question cites `map.md` at 31,058 bytes. It is now 42,098.
   - Node 80's condition quotes an "in-place update never deletes" wording that `map.md` no longer carries.
   - `graph-conventions.md` and `map-implementation-rules.md` both state the no-sweep clause, which is why the new node edits both.

## Flags

`345.1` `ASSUMPTION` **· settled** — The recommendation the human approved said the pass would be "an implementation node". Under `.claude/skills/expedition/SKILL.md`'s `## Writing the graph`, a change confined to the graph's files is the manager's own, with no node, condition, checker or gate, so the answer makes it the manager's. The substance approved, meaning what moves where and that nothing is deleted, is unchanged. The manager relayed that fact as its own note, and the human's reply did not address it. — Node 345's map pass was reassigned from an implementation node to the manager's own change, because the shipped file test makes a graph-files-only change the manager's.

`345.2` `ASSUMPTION` **· settled** — No new rule was asked for about the manager's future writes to `map.md`. `graph-conventions.md` already applies the reader test to whoever edits a passage, a new item included, so a manager-only item written into `map.md` is non-compliance and not a gap. — Node 345 added no rule for the manager's map writes, holding that the shipped reader test already binds a new item's writer.

*The manager's note, 2026-09-27:* flags 345.1 and 345.2 settle at the node closing report that closes this node.

## Annotation: the pass carried out, 2026-09-27

*The manager's own change to the map, made by an agent acting as its hands (not a node), after [node 346](346-allow-a-sweep-of-a-map-file-in-graph-conventions-md.md) landed as `477d350`. The agent's report, pasted as it handed it back. The manager accepts its reading of check 11 for moves between map files, on the node 139 and 140 precedent, and does not duplicate the moved bodies into `map-history.md`.*

**The map pass is done: `map.md` went from 42,098 to 21,910 bytes.** Nothing is committed and I wrote nothing outside the four map files.

**State after your usage-limit message.** Before touching anything I copied the four files as they stood to `$TMPDIR/p345/`. All my edits then came from one script (`$TMPDIR/p345/pass.py`), and that script ran once and to completion before the limit hit. The copies are still the originals (their sizes match the first measurement), so nothing was moved twice or left half-moved. Every result below compares that snapshot with the files on disk. The `map-implementation-rules.md` change the harness showed you is my own insert.

## Sizes (bytes, before → after)
| File | Before | After |
|---|---|---|
| `map.md` | 42,098 | 21,910 |
| `map-manager-only.md` | 32,264 | 49,630 |
| `map-implementation-rules.md` | 13,182 | 15,104 |
| `map-history.md` | 156,293 | 170,953 |

## Moved whole, byte for byte
**To the end of `map-manager-only.md`'s `## Notes`**, in `map.md` order, after a new italic lead-in. These 12 items went:
1. One question at a time, and the grilling target.
2. A payload goes over when ready (reworded afterwards, see node 256 below).
3. A gate payload carries no diff command.
4. The manager never idles (reworded afterwards, see node 256 below).
5. Every report ends with the line saying what is expected.
6. Approving a node's end settles its flags.
7. The retrospective rule.
8. Token-use priority.
9. The standing yes.
10. Resume wherever possible.
11. The moved-standard licence is spent.
12. The never-ask-which pointer.

**To `map-implementation-rules.md`**, just before `## What the work is held against`, with an italic lead-in: the worktree paragraph ("An implementation node's worktree is made with plain git…").

## Shortened in `map.md`
Each item's full old text was appended verbatim to `map-history.md`, under a new section "Superseded from `map.md`'s `## Notes` at node 345…", one `### From *Notes* — …` subheading per item. Each replacement keeps the human's quoted words and the citations, and ends with a link to `map-history.md`.
- **No dependency on `mattpocock-skills`** (1,573 → 1,489): I dropped "the two open questions", "the manager has changed neither" and "whose first question was already in front of the human when this arrived". Node 113 is now resolved, so "open" was stale.
- **A checker's rules are given, not found** (1,668 → 1,329): the stale "What it reaches… / What it does not settle…" became a pointer. It says the rules live in `map-implementation-rules.md`, settled at node 138 and carried out at node 140.
- **Grouping by file** (1,402 → 1,329): I dropped the account of the circumstances of 2026-09-26.
- **A human decision may be proposed for change** (1,307 → 881): the account of what it corrected went out; node 189 stays cited.
- **A condition forcing a contradiction is a raise** (1,506 → 981): the quotes from node 200's worker and checker went out.
- **The `/expedition` name and vocabulary** (2,181 → 1,405): the struck-through text and the story of the node-29 count went out.

**New one-line pointer**, in place of the worktree paragraph: the manager-only standing preferences are in `map-manager-only.md`'s `## Notes`, and the worktree route is in `map-implementation-rules.md`, both moved by node 345. The header's existing pointer lines were left as they were.

## Left in `map.md` because I was unsure of the reader
- "The human is the scarce resource": partly about the manager's own context budget.
- "Most of the context lives in the workers": it governs design choices about the spawn and the handover, which workers make on this effort.
- "A standing rule binds this effort only once it is written here": `map-manager-only.md`'s header quotes it as a `map.md` item. Its last sentence tells workers that every line binds them.
- "Nodes are grouped by file, and a related defect goes into a node that already exists": node 327's worker said this item bore on its node.
- The optional-blocks and source-declaration item: its last sentence is the manager's act of copying the block into a checker's spawn, but the declaration itself is kept.

I also left some over-target items unshortened because they are all current statement rather than account: node files are written for agents, never-delete, Claude tokens, the graph is seven files, and the optional blocks.

## Nodes 80 and 256 (neither marked resolved)
- **Node 256:** both of its items now live in `map-manager-only.md`, so its clause 1 path (`map.md`) is wrong. I carried out its substance there as a reword under the Change the map rules. Each item now names `SKILL.md`'s `## The order you act in` as where the order of acts is stated. Each keeps its `verbatim` human quotes. The payload item keeps "the trigger is the payload being ready, not the human answering", and both cite node 256.
  - Clause 2 holds: the full old text of both items is in the new history section.
  - Wrinkle: the never-idles item grew from 1,296 to 1,368 bytes. I added the pointer and the node-256 citation and dropped only the node-16 filing phrase.
  - The "a live question does not block a start" clause is in the one-question item, which I moved unchanged.
- **Node 80:**
  - Clause 1 was already met by earlier nodes: the never-delete item no longer says `map.md`'s superseded text stays in place. I did not touch that item.
  - Clause 2, a reword, is done: "worktrees" is gone from the firstmate list in the fog item. The old item is in the history under "Superseded from `map-manager-only.md`'s `## Not yet specified` at node 80".
  - Clause 3 is not done. Re-describing the async-landing seam and the price of a reject against today's landing lifecycle is new analysis, not a move or a reword.
  - Its condition still names only `map.md` and `map-history.md` as files it may change, although both fog items sit in `map-manager-only.md`.

## Checks
- **Check 11, first half:** `cmp -n 156293 <snapshot history> map-history.md` passes. The old history is a byte-exact prefix of the new one.
- **Check 11, second half:** I line-diffed each map file against its snapshot and searched each removed non-blank line.
  - `map.md`: 53 removed lines. 27 appear in the appended history, the 26 moved-item lines appear only in text added to a sibling map file, and 0 are nowhere.
  - `map-manager-only.md`: 1 removed line (the fog item), which is in the appended history.
  - `map-implementation-rules.md`: 0 removed lines.
- **Where check 11 fails as written:** read literally ("every passage the change removed from a map file appears … inside the text appended to `map-history.md`"), it fails on those 26 moved lines. I followed the precedent of nodes 139 and 140, whose history sections say moved bodies "are not quoted here: they stand verbatim in" the sibling. The check's wording does not provide for a move between map files. You decide whether to duplicate the ~18 KB into history.
- **Check 10** (size report; it never fails), bytes as raw / excluding `*"…"*` quotes:
  - `map.md`, 14 items over 500: node files for agents 1231/1078, never-delete 1864/1778, mattpocock 1489, checker rules 1329/871, standing rule binds 949/804, grouping 1329/1116, proposed change 881/618, contradiction raise 981/894, unseen repos 531, Claude tokens 1138/1038, seven files 971, vocabulary 1405, optional blocks 1085. The new pointer is 346.
  - `map-manager-only.md` `## Notes`: most of the moved items are over, the retrospective rule largest at 4001.
  - `map-implementation-rules.md` has no `## Notes`.
- There are no new double blank lines. The one in `map-manager-only.md` was already there.

## What looked wrong
- `map.md`'s header cites superseded node 60 ("settled by measurement").
- The moved diff-command item cites node 231, which is superseded by 336, and says "until that lands".
- The moved last-line item cites node 96, which is superseded by 336.
- The grouping item says "shipping that rule is node 327", which is resolved.
- `map-implementation-rules.md` says "Everything remaining in this file is held against a worker's work". The worktree paragraph is closer to instructions for the worker than a standard, so this is a mild tension.
- Header line 5's list of what `map-manager-only.md` holds is incomplete, and was even before this pass. I left it, since the new pointer covers the gap.

## RETROSPECTIVE
1. **What I had to hunt for:**
   - Whether a move between map files owes a copy in history. The answer was only in the precedent sections for nodes 139 and 140 in `map-history.md`.
   - Where the priority list node 256 points at: `SKILL.md` `## The order you act in`. The word "priority" does not appear there.
   - The statuses of the cited nodes.
   - Whether node 80's fog items still exist, and where.
2. **What arrived that this work did not need:** node 345's full interview payloads, when the `## Answer` and the handover were enough. Also the first full `cat` of `map.md`, which was cut off and had to be re-read.
3. **What would have made this easier:**
   - A line in check 11 on moves between map files.
   - A shipped item-splitting script for check 10.
   - Node 256's condition re-pointed after node 255 resolved.
4. **What was stale, wrong or contradictory:**
   - Check 11's literal wording against the node 139/140 precedent.
   - Node 80's allowed-file scope against where its items now are.
   - Node 256's path.
   - The stale node citations listed under "What looked wrong".
