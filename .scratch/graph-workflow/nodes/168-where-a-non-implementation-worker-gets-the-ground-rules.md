# Where a worker that is not an implementation worker gets this effort's ground rules

Type: grilling
Status: resolved

Blocked by: 144

## Answer

Ground rules and the source-standing declaration sit only in `map.md`'s `## Notes`, which every worker reads; the sibling-file allowance is struck and this effort's block moves back.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The nodes it surfaced are [node 348](348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md) and [node 349](349-whether-the-five-standing-rules-for-writing-reach-other-workers.md); its replacement clause for node 190 is filed there. Flags 168.1 and 168.2 settle at the node closing report.

## Question

*Surfaced by [Make the rules file stand alone for a reader that does not read `map.md`](144-make-the-rules-file-stand-alone.md)'s worker, and pasted as it wrote it.*

> This effort's ground rules have left `map.md`'s `## Notes` for
> `map-implementation-rules.md`, which only an implementation worker and a checker are given. Five
> shipped contracts — research, grilling, prototype, precondition, implementation — and
> `graph-conventions.md` all say the ground rules may be declared in the map's `## Notes`, so on this
> effort those workers now meet a pointer where the block was. Three answers are open and they differ in
> what they ship: leave the block in the map and move only the four standing rules; widen the contracts
> to "the map, or a sibling file the map points at"; or have the manager copy the ground rules into
> every worker's spawn as it already does for a checker. The third makes the map's location question
> moot and matches node 42's existing route, but it changes what every spawn carries, which the human
> settles rather than a worker.

## The manager's note at filing

*Not a change to anything above.*

**The blocker is the manager's bookkeeping**, taken from the `blockers: 144` its author wrote beside the node. It is
an edge on node 144 rather than on node 144's gate: the defect this node names does not exist until node 144's work
lands.

## Interview

### Attempt 1

*The worker stopped once on the session's usage limit and was resumed in place.*

#### Question 1, relayed 2026-09-27

*The worker's payload, pasted as handed back.*

```
NODE:          168, Where a worker that is not an implementation worker gets this effort's ground rules
ABOUT:         This effort's five ground rules are rules of scope that bind every node's work. They sit in `map-implementation-rules.md`, and only the implementation worker and the checker are told to read that file. This node decides how a grilling, research, prototype or precondition worker comes to have those rules. It is being decided now because node 343 has just shipped wording that permits the gap. Node 343's worker reported the same gap independently.
SO FAR:        I read the following. The shipped files: the five worker contracts' `## What you read` sections, `graph-conventions.md`'s `## The seven files` and `## Writing the map`, the manager `SKILL.md`'s `## Spawning a worker` and its checker-spawn givens, and the checker contract's givens. The record: node 168, the map's `## Notes` ground-rules items, `map-implementation-rules.md`'s ground-rules block, node 144's answer, node 343, and node 345's answer.
               What the shipped files say today:
               - All five worker contracts say: "The map may declare the effort's ground rules ... Follow both. Each declaration sits in `map.md`'s `## Notes` unless the effort holds it in a sibling file of the map." (node 343, `688aa50`).
               - Only the implementation contract lists a sibling file in its reading list, and that file is `map-implementation-rules.md`. The other four list only `map.md`, the node file and `decisions.md`.
               - All five contracts also say that the rules a worker is held to "arrive in the spawn and in the files the list above names, and you never go looking for a standard you are judged against". So when a non-implementation worker meets the map's pointer to the rules file, the contract gives no clear leave to follow it.
               - `graph-conventions.md` says "Each file of the map declares its reader: one kind of worker, or the manager alone". It gives `map-implementation-rules.md`'s readers as "that node's worker and its checker, rather than every worker".
               - The manager's spawn carries pointers only, and a grilling spawn adds "nothing extra". The checker alone gets the ground rules copied as text into its spawn (node 42).
               Map facts I rely on:
               - The ground-rules block (five rules plus the node-42 membership test) is in `map-implementation-rules.md` under `## What the work is held against`. Node 144 moved it there verbatim.
               - `map.md` keeps a one-line pointer where the block was.
               - Node 144 moved the block so the rules file would "stand alone for a reader who does not read this map". That reader is the checker, which already gets the ground rules copied into its spawn.
               - Node 345's decided pass moves implementation-only items out of `map.md`. Ground rules bind every worker, so they are not implementation-only.
               - Several of the five rules bind non-implementation work directly. Rule 1 (no repo, machine or toolchain assumptions in shipped files) and rule 3 (the human talks only to the manager) constrain what a grilling or research worker recommends.
               Settled on my own authority:
               - The source-standing declaration (authoritative, evidence only, false) gets the same treatment as the ground rules. The contracts state both in the same sentence, and this effort declares none.
ASK:           How should the shipped files make sure every worker receives the effort's ground rules? One way is a rule about where they may live: in `map.md`, the file every worker reads. The other is a pointer to the holding sibling file, added to the four non-implementation contracts' reading lists.
RECOMMENDED:   Adopt a rule about where they may live. The ground rules, and any source-standing declaration, sit in `map.md`'s `## Notes` and in no sibling, because they bind every worker and `map.md` is the one map file every worker reads. The sibling clause that nodes 338 and 343 added to `graph-conventions.md` and the five contracts would be struck for these two blocks. This effort's block would move back from `map-implementation-rules.md` into `map.md`, and the rules file would name `map.md` in its place.
               It rests on four points:
               (a) It applies the shipped rule that each map file declares its reader. A block every worker needs placed in a file only some workers read breaks that rule, and a pointer only adds one more hop.
               (b) Nobody loses access. The implementation worker already reads `map.md`, and the checker gets the rules as text in its spawn. So node 144's stand-alone reason no longer needs the block to live in the rules file.
               (c) The block is five short rules, about 1 KB, so putting it back costs little against node 345's goal of a smaller `map.md`.
               (d) It changes four shipped files less than a pointer would. It also keeps the "never go looking for a standard" line true without adding an exception.
               This narrows node 144, and nodes 338 and 343 for these two blocks. I would report that in INVALIDATIONS and file an implementation node for the edit.
ALTERNATIVES:  - Pointer in the four reading lists (for example, "the sibling of `map.md` that `map.md` names as holding the ground rules, where there is one"). This keeps node 144's placement, but the four workers then open a file whose declared reader they are not. They also pay for its bar commands and review route, which they never use.
               - The manager copies the ground rules as text into every worker's spawn, as it does for a checker. This makes the file location irrelevant, but it changes what every spawn carries and duplicates what `map.md` would hold. It also breaks the spawn's "points, does not summarise" rule.
               - Change nothing, and let each worker follow the map's pointer on its own judgement. This leaves the contract's "never go looking for a standard" line in conflict with the "sibling file" line.
```

#### The human's answer to question 1, 2026-09-27

The human, `verbatim`: *"ok"*. The manager reads it as taking the recommendation, the one option the question marked recommended: "Adopt a rule about where they may live. The ground rules, and any source-standing declaration, sit in `map.md`'s `## Notes` and in no sibling, because they bind every worker and `map.md` is the one map file every worker reads."

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Where a worker that is not an implementation worker gets this effort's ground rules
ANSWER:        The ground rules sit where every worker reads them. An effort's ground rules, and its declaration of which sources are authoritative, which are evidence only and which hold statements known to be false, sit in `map.md`'s `## Notes` and in no sibling file of the map. They bind every node's work, and `map.md` is the one map file every worker reads. The human took this on a bare "ok" to the recommendation. The manager recorded the reply as taking the recommendation, the only option marked.

               **What changes in the shipped files.** The clause "unless the effort holds it in a sibling file of the map", which nodes 338 and 343 added, is struck for these two blocks. The clause sits in `graph-conventions.md`'s `## Notes` bullet and in the "What you read" paragraph of the five worker contracts. With it gone, the rule a worker reads matches `graph-conventions.md`'s own rule that each map file declares its reader. `map-implementation-rules.md` keeps its declared readers, the implementation worker and the checker.

               **What changes in this effort's map.** The ground-rules block moves verbatim back from `map-implementation-rules.md` into `map.md`'s `## Notes`, where the one-line pointer to it now stands. That is the five numbered rules and the paragraph after them stating the node-42 test. The rules file's list of standards then says where the ground rules are held instead of "this file holds below".

               **Nobody loses access.** The implementation worker already reads `map.md`, and the checker gets the ground rules as text in its spawn (node 42). Node 144 moved the block into the rules file so that file would stand alone for the checker. That reason no longer needs the block to live there.

               **Set aside:**
               - A pointer in the four non-implementation contracts' reading lists. It would send those workers into a file whose declared reader they are not, and one full of bar and review-route material they never use.
               - Copying the ground rules into every worker's spawn. It changes every spawn, and a spawn points rather than summarises.
               - Changing nothing. The contracts' "you never go looking for a standard" line would then stay in conflict with the "sibling file" line.

               **Not settled here:** whether the five standing rules for writing, which are not ground rules and stay in `map-implementation-rules.md`, must reach the workers that are not implementation workers. That is filed as a new node.
INDEX LINE:    Ground rules and the source-standing declaration sit only in `map.md`'s `## Notes`, which every worker reads; the sibling-file allowance is struck and this effort's block moves back.
FLAGS:         ASSUMPTION: The question named the ground rules, and I applied the same answer to the source-standing declaration. Every shipped statement puts the two blocks in one sentence under one rule of placement, and this effort declares no source standing, so nothing in the record moves for it.
                 Index: Node 168 applied the human's ground-rules placement to the source-standing declaration too, since the shipped files state both in one sentence.
               ASSUMPTION: I kept the five standing rules for writing out of this answer and left them in `map-implementation-rules.md`. The rules file itself calls them rules of writing rather than ground rules, and the human's answer covered ground rules only. Whether they reach the other workers is filed as a new node rather than decided here.
                 Index: Node 168 left the five standing rules for writing in the rules file and filed their reach to other workers as a separate grilling node.
NEW NODES:     1. Name: Keep the ground rules in `map.md` and strike the sibling-file allowance
                  Kind: implementation
                  Question: Where an effort's ground rules and source-standing declaration sit only in `map.md`'s `## Notes`, what must change in the shipped files and in this effort's map?
                  Blockers: none. It edits `map-implementation-rules.md`, as does open node 190 ("The rules file states one list twice"). The two touch different passages, but whichever lands second works on the other's text.
                  Acceptance condition:
                  > The work is these six shipped files: `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`. It is also three files of this effort's map: `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-implementation-rules.md` and `.scratch/graph-workflow/map-history.md`. No other file changes. The shipped files are edited plainly, with no strike-through or history note.
                  >
                  > Scope: the six shipped files are exactly what `grep -rln "sibling file of the map" .claude CONTEXT.md` returned over the working tree when this condition was written. An instance the same command finds outside that list is reported in the handover and not edited.
                  >
                  > Done means all of the following are true of the finished tree.
                  > 1. In `graph-conventions.md`, the `## Notes` bullet under the description of `map.md`'s three sections no longer contains "unless the effort holds it in a sibling file of the map". The bullet says that the two optional blocks, the effort's ground rules and the declaration of which sources are authoritative, which are evidence only and which hold statements known to be false, live in `map.md`'s `## Notes` and in no sibling file of the map. The rest of the bullet keeps its meaning.
                  > 2. In each of the five worker contracts, the paragraph beginning "The map may declare the effort's ground rules." no longer contains "unless the effort holds it in a sibling file of the map". It says each declaration sits in `map.md`'s `## Notes`. The rest of each paragraph keeps its meaning, including the research contract's closing sentence "A source marked as evidence stays evidence, whatever it says."
                  > 3. After the edit, `grep -rn "sibling file of the map" .claude CONTEXT.md` returns no line that places the ground rules or the source declaration in a sibling file.
                  > 4. In `.scratch/graph-workflow/map-implementation-rules.md`, the block that runs from the line `**Ground rules for this effort.**` through the paragraph beginning "Every rule above is drawn from a standing preference" is no longer present. That is the lead-in line, five numbered rules and one paragraph.
                  > 5. In `.scratch/graph-workflow/map.md`'s `## Notes`, the block removed under clause 4 stands in the place of the paragraph beginning "**Ground rules for this effort, now in". It is byte-identical to the block as committed at `HEAD` in `map-implementation-rules.md`, and nothing in it is reworded, renumbered or reordered. That pointer paragraph is no longer in `map.md`.
                  > 6. In `.scratch/graph-workflow/map-implementation-rules.md`, no sentence says that file holds the effort's ground rules. The list of standards that work is held against still names this effort's ground rules, and says that `map.md` holds them. It also says that a checker receives them as text in its spawn. The five standing rules for writing stay in that file unchanged.
                  > 7. The pointer paragraph removed from `map.md` under clause 5, and the text of each sentence of `map-implementation-rules.md` replaced under clause 6, are appended verbatim to `.scratch/graph-workflow/map-history.md`. Each goes under a heading that names the file and section it came from. The block moved under clauses 4 and 5 is moved, not superseded, so it is not appended.
                  > 8. Every markdown link in `map.md` and `map-implementation-rules.md` resolves to a path that exists.
                  > 9. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.

               2. Name: Whether the five standing rules for writing reach a worker that is not an implementation worker
                  Kind: grilling
                  Question: This effort's five standing rules for writing are held against every prose deliverable. They sit in `map-implementation-rules.md`, which only an implementation worker and a checker read. Grilling, research, prototype and precondition workers also write prose that the manager pastes onto the graph unaltered. Must those rules reach those workers, and if so, by moving them into `map.md`, by a pointer in those contracts, or by some other route?
                  Blockers: node 1 above. It fixes where the ground rules sit, and this question may follow the same pattern.
INVALIDATIONS: - Node 343: contradicted. It made the five worker contracts allow the ground rules and the source declaration to sit in a sibling file of the map, and this answer strikes that allowance.
               - Node 338 (carrying node 228's clause 2): narrowed. Its clause required that `graph-conventions.md` not require the two blocks to sit in `map.md`'s `## Notes`. For these two blocks the requirement returns, and on a different ground from before: every worker reads `map.md`.
               - Node 144: narrowed. Its move of the ground-rules block into `map-implementation-rules.md` is reversed. Its move of the standing rules for writing, and its making of the standards sentence resolve inside the rules file, stand.
               - Node 12 ("Subagent context contract"): no change. Its placement of the optional blocks in `map.md`'s `## Notes` is what this restores.
CONDITIONS:    I searched every open and claimed node's `## Acceptance condition` for "sibling", "ground rule", "ground-rule", "map-implementation-rules" and "holds below", then read only what matched "sibling", "ground rule" and "holds below". The matches came from nodes 149, 190, 56, 80, 284, 232 and 41.
               - Node 190 (open, unclaimed), clause 4: "No numbered rule in the file's two blocks — the five ground rules, and the four standing rules for writing — is reworded, renumbered or reordered." This becomes wrong once the ground-rules block leaves that file. Replacement: "4. No numbered rule in the file's block of five standing rules for writing is reworded, renumbered or reordered." Fixed by the tree: `map-implementation-rules.md` heads that block "**Five standing rules for writing anything in this effort**", which landed with node 289.
               - Node 190, clause 1: its phrase "this effort's ground rules" still holds, because the list still names them. Its "four standing rules for writing" was already stale from node 289, not from this node, and I wrote no replacement for it.
               - Node 56's glossary clause ("declared in its map's `## Notes`"), node 80's "`map.md`'s own ... ground rules" and node 41's "that effort's ground rules in `map.md`" become correct again. They need no replacement.
               - Nodes 149, 232 and 284 match on general wording about sibling files or the list of standards, and nothing in them conflicts with this answer.
MISSING FROM MAP: none. The manager's note said node 345's pass left the ground-rules block and its pointer in place, and I read their current location directly in `map.md` and `map-implementation-rules.md`.

RETROSPECTIVE
1. What I had to hunt for: why node 144 had moved the block, meaning whose reading it served. It took node 144's answer plus the checker's spawn givens in the manager `SKILL.md` to see that nobody would lose access. I also had to hunt for whether the changes to the map file belong to the implementation node or to the manager. The answer is the manager `SKILL.md` rule that a node whose shipped change would leave the graph's files contradicting it makes the graph change inside that node.
2. What arrived that this node did not need: `map.md` read whole, of which only the two ground-rules items in `## Notes` bore on this node. Also node 345's interview, which I opened only to confirm the pass did not touch ground rules.
3. What would have made this easier: a spawn line saying the checker already gets the ground rules in its spawn, and that node 144 moved the block only for the checker. That is the fact that decides the question. Also, the open-node condition search was slow and broad: 131 open nodes, many mentioning `map-implementation-rules.md` for unrelated reasons. A per-node list of the files each condition touches would narrow it.
4. What was stale, wrong or contradictory: the node's `## Question` text is stale. It says the contracts allow the rules only in the map's `## Notes`, which predates node 343. Node 190's clause 1 still says "four standing rules for writing" where the rules file now holds five (node 289). The shipped contracts contradict themselves: "sits in a sibling file" against "never go looking for a standard you are judged against", which this answer removes.

## Flags

`168.1` `ASSUMPTION` **· settled** — The question named the ground rules, and I applied the same answer to the source-standing declaration. Every shipped statement puts the two blocks in one sentence under one rule of placement, and this effort declares no source standing, so nothing in the record moves for it. — Node 168 applied the human's ground-rules placement to the source-standing declaration too, since the shipped files state both in one sentence.

`168.2` `ASSUMPTION` **· settled** — I kept the five standing rules for writing out of this answer and left them in `map-implementation-rules.md`. The rules file itself calls them rules of writing rather than ground rules, and the human's answer covered ground rules only. Whether they reach the other workers is filed as a new node rather than decided here. — Node 168 left the five standing rules for writing in the rules file and filed their reach to other workers as a separate grilling node.

*The manager's note, 2026-09-27:* flags 168.1 and 168.2 settle at the node closing report that closes this node.
