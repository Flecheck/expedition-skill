# Group the open nodes against the manager contract

Type: precondition
Status: resolved
Blocked by: none

## Question

Most open implementation nodes change a few lines of one file each, and their conditions forbid touching anything else, so two nodes on the same file cannot be worked together. The human asked for them to be grouped by file. Which open nodes change `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md` and `.claude/rules/expedition-triggers.md`, and what merged node or nodes should replace them?

*Minted by the manager on the human's "You can do the groups", recorded in the map under `## Notes`.*

## What must be true when this is done

- Every open or unclaimed implementation node whose condition changes `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md` and `.claude/rules/expedition-triggers.md` is listed, with the node number, its name and the part of the file it changes. A node that also changes files outside this group is listed and marked as crossing groups.
- For each proposed merged node: its name, the nodes it replaces, and an acceptance condition that carries each replaced node's demands with the node each came from. Where a replaced node's clause fences its own node ("no other entry changes"), the merged condition fences the union instead. Where a demand is already met by the file as it stands, or is stale, that is said and the demand is left out, with the reason.
- Every conflict is listed: between two replaced nodes' demands, or between a demand and the file as it stands. Each conflict says which nodes and which words, and offers the options. These go to the human.
- Nodes left out of any merge are listed, with the reason.

**Later nodes depend on:** the merged nodes' conditions, which the manager files as new nodes once the human approves the supersessions.

## Answer

Node 330 found 45 open nodes on the manager contract and graph-conventions: five merged nodes replace 26, ten cross groups, nine stay out, twelve conflicts.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, and the human's decision under `## Interview`. On the human's "ok": M1 to G3 are nodes 336 to 340, with node 329's remainder R1 folded into G1 (338) and M2 (337) blocked by G2 (339); node 192 is superseded by node 100; nodes 120, 124 and 258 merge into node 124, whose condition [node 341](341-draft-one-condition-for-nodes-120-124-and-258.md) drafts.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Group the open nodes against the manager contract

ANSWER:

Read at commit `c3ecda3`: `.claude/skills/expedition/SKILL.md` (617 lines, 15 `## ` headings), `.claude/skills/expedition/graph-conventions.md` (422 lines), `.claude/rules/expedition-triggers.md` (38 lines). I checked every open or claimed `implementation` node, 100 of them. For each, I read its `## Acceptance condition`, its amendments and annotations, and, where it has no condition, its `## Question`. I grepped them for the three paths, for "manager's contract", "manager contract" and "conventions document", and for bare `SKILL.md`. I read the node's words "changes A, B and C" as "changes any of them".

**The triggers file.** No open node changes `.claude/rules/expedition-triggers.md`. Node 226 names it, but that node's work is limited to `.scratch/`, and its clause 5 requires the triggers file to stay byte-identical.

**1. Nodes that change only files in this group (26 merged, 9 left out)**

| node | name | part of the file it changes | goes to |
|---|---|---|---|
| 96 | Every manager report ends with one line saying what is expected of the human | SKILL.md: the last line of a report (`## The order you act in` holds today's partial statement); `## What nothing here settles` item 1 fenced | M1 |
| 118 | Carry the channel-free rule and the manager's duty to fill a gap into the manager's contract | SKILL.md `## What is in front of the human, and when`, `## The order you act in` | M1 |
| 127 | Say in the manager's contract that one payload may carry several of one worker's questions | SKILL.md `## What is in front of the human, and when` | M1 |
| 161 | The slot count ships as a dial with its price stated | SKILL.md `### Picking the next node` code-slot bullet; `## What nothing here settles` item 5 | M1 |
| 231 | A gate payload stops carrying a command that prints a diff | SKILL.md `### The payload` bullet and the `## What is never yours` diff row; also the record file `map-manager-only.md` landing policy. Has no condition. | M1 |
| 101 | Carry the home of an effort's standing rules into the manager's contract | SKILL.md `### Standing steering, and standing instructions of one effort` | M2 |
| 105 | `revision` is a defined term with no conduct behind it… | SKILL.md, whichever section covers supersession | M2 |
| 111 | Write the starting-an-effort section and its procedure | SKILL.md new `## Starting an effort`; graph-conventions new `### Start an effort` under `## Procedures`, and the `## Destination` line under `## The seven files` | M2 |
| 278 | The manager contract's table of what is never the manager's still states the amendment rule as absolute | SKILL.md `## What is never yours`, the condition row | M2 |
| 280 | The manager contract's open question 5 and the search duty… | SKILL.md `## What nothing here settles` item 4 | M2 |
| 287 | Ship the record-file test into the manager's contract and repair the procedures sentence | SKILL.md `## Writing the graph`; graph-conventions `### Change the map` | M2 |
| 146 | `graph-conventions.md`'s rules for the map now resolve to more than one `## Notes` | GC `## Writing the map` 500-byte target; check 10 | G1 |
| 153 | `graph-conventions.md` still says `map.md`'s `## Notes` holds the label vocabulary and the bar's commands | GC `## The seven files`, the `## Notes` line | G1 |
| 195 | `graph-conventions.md` still puts the fog in `map.md`… | GC `## Writing the map`; the opening sentence of `### Change the map`; the opening never-delete paragraphs | G1 |
| 201 | Ship the cleanup exemption and the flag check | GC opening never-delete paragraph; check 6 | G1 |
| 206 | `graph-conventions.md`'s `## Labels` section still names `map.md`'s `## Notes`… | GC `## Labels` | G1 |
| 228 | `graph-conventions.md` says `map.md`'s `## Notes` holds three things this effort's map keeps elsewhere | GC `## The seven files` `## Notes` line; `## Labels` | G1 |
| 233 | Ship the two never-delete tests and the acceptance condition's place into the conventions document | GC opening paragraphs; `## Writing the map`; optionally one new check | G1 |
| 308 | `graph-conventions.md`'s seven-files block says `map.md` is read once per session | GC `## The seven files` fence. Has no condition. | G1 |
| 49 | Co-locate the scan rules with the mechanical checks | GC `## Mechanical checks` | G2 |
| 238 | Add each check to the procedure whose writes can make it false | GC every `### ` procedure, `## Adding a node`, `## Mechanical checks` (check 5) | G2 |
| 239 | Write the two graph writes that have no procedure | GC `## Procedures` (two new procedures) | G2 |
| 286 | `Reading the graph` does not describe the `Blocked by:` field a scanner will meet | GC `## Reading the graph` | G2 |
| 288 | Nothing mechanically verifies the never-delete bank… | GC `## Mechanical checks` (one new check); `### Change the map` | G2 |
| 73 | A hard rule binds by being read | GC, one new section | G3 |
| 79 | The annotation section is undefined | GC `## The node file` | G3 |
| 285 | Ship the frontier script and say what it cannot answer | a new `.claude/skills/expedition/scripts/frontier.sh`; SKILL.md `### Picking the next node` | left out |
| 317 | Which outstanding flags reach the closing report | SKILL.md `## Flags` / `## Closing an effort`; `CONTEXT.md` `Flag`. Has no condition. | left out |
| 185 | A spawn points at the decisions index without naming which sections bear on the node | SKILL.md `## Spawning a worker`. Has no condition. | left out |
| 192 | The trigger for topping up the human-facing nodes is a node finishing… | SKILL.md `### Picking the next node`. Has no condition. | left out |
| 170 | A licence the human granted has no flag marker… | GC `### `## Flags`` markers. Has no condition. | left out |
| 87 | The manager's cascade duties are in neither contract | SKILL.md or a cascade file. Condition incomplete. | left out |
| 89 | Carry the worktree lifecycle into the manager's contract | SKILL.md. Condition incomplete. | left out |
| 97 | Write the adoption procedure | a new `.claude/skills/expedition/adoption.md`; an optional pointer in SKILL.md | left out |
| 40 | Nothing carries a flag's account of what produced it out of a worker | mainly the five worker contracts; GC only if the answer lands there. Has no condition. | left out |

**2. Nodes that cross groups (10), not merged**

- **109**, "Carry node 94's extent rule into the seven shipped files…". It changes SKILL.md `## Acceptance conditions` (the manager's duties plus a one-sentence pointer), GC `### `## Acceptance condition`` (the extent rule, clauses 1 to 4), and the reporting sections of the five worker contracts (clause 6). Both parts are substantial. Its blockers 95 and 103 are resolved, so it is startable.
- **120**, "Carry the resume rule into the shipped files". It changes SKILL.md `## When an agent dies or is stopped`, GC `### `## Interview`` (dead-attempt marking), the `CONTEXT.md` `Attempt` entry, and any other file under `.claude/skills/`. Its clause 1 (the three-state table, and replacement as the fallback) and clause 3 (the file no longer says a human-stopped agent cannot be resumed) are contradicted by node 122's annotation, by node 123's decision (a user-stopped agent leads to a question to the human, not a replacement) and by node 124's condition, which the human approved (items 6 and 7, four outcomes). Its clause 4 asks for strike-in-place in `CONTEXT.md`, a shipped file (see C2).
- **124**, "Give the manager's contract a procedure for stopping a running worker". It carries the 12-item condition from its 2026-09-26 amendment. It changes SKILL.md (a new stop procedure, the dies-or-stopped section, and the "stop or redirect what you started" sentence in `### Picking the next node`), GC `### `## Interview`` (the heading of an attempt recorded as final), `CONTEXT.md` (the stop words), and other `.claude/skills/` files. It is blocked by 120. Its clause 9 asks for strike-in-place in `CONTEXT.md` (see C2).
- **258**, "The manager's contract contradicts itself on whether a dead worker is resumed or replaced". It changes SKILL.md `## Words used exactly` ("A worker is resumed in place rather than replaced.") and the `CONTEXT.md` `Attempt` entry. That is the same entry as 120's clause 4, which 120's clause 6 already reaches. Its "replaced only where it does not" contradicts node 123's decision for the user-stopped case. Its blocker 255 is resolved.
  *Option for the human:* merge 120, 124 and 258 into one crossing node. They share one SKILL.md section, one GC section and one `CONTEXT.md` entry, and 124 is blocked by 120. Its condition would be 124's approved condition, plus 120's clauses 1 (without the three-state table and the unconditional replacement fallback), 2, 5, 6 and 7, plus 258's clause 1, with strike-in-place dropped. I recommend this, but I have not written that condition, because merging a crossing node was outside my remit. Node 121 (open grilling, "What the two-respawn cap becomes") bears on the same section's "After two replacements" paragraph.
- **327**, "A related defect joins an open node instead of becoming a new one". It changes the five worker contracts (clause 1), SKILL.md (clauses 2 and 3) and GC (clause 4). Both parts are substantial.
- **137**, "Rename the two reports and repair the `_Avoid_` line". It changes `CONTEXT.md`, SKILL.md (all 12 "pick report" occurrences), GC and the precondition contract. Node 328 is handling it. Its recorded count of 3 "pick report" in GC is stale: there are 0 now. The M1 and M2 conditions below avoid quoting "pick report", so they survive the rename in either order.
- **148**, "Nothing stops a condition being written with an absolute path". It changes the five worker contracts and one GC sentence ("A path may say where"). **The GC part is trivially small.** Its home is node 329's group; the human chooses.
- **43**, "Widen the invalidation channel from contradiction to change". It changes the five worker contracts and one GC sentence ("Such a demand goes in the handover's `INVALIDATIONS` part…"). **The GC part is trivially small.** Its home is node 329's group; the human chooses.
- **41**, "Ship the FRICTION flag…". It changes GC (the markers list, the `flags.md` line form, `### Settle a flag`, and three new statements) and the five worker contracts (the marker list and the `FLAGS:` line). It is blocked by 56. Its clause 5 places ground rules in "`map.md`'s `## Notes`", which G1's clause 2 makes generic.
- **56**, "Ship the glossary inside the skill directory…". It moves `CONTEXT.md` (node 328's group) and repoints GC's glossary path (clause 6). **The GC part is trivially small.** Its condition does not reach SKILL.md, which names "the glossary, `CONTEXT.md`" in its opening and in `## Words used exactly`. That is a gap for node 328 or the human.

**3. The merged nodes** (conditions in NEW NODES)

- **M1** replaces 96, 118, 127, 161 and 231. It covers SKILL.md: what is in front of the human, the last line of a report, the code-slot count, and the gate payload's pointer to the work. Under C10's recommended option it also changes one sentence of `map-manager-only.md`, banking the old text in `map-history.md`.
- **M2** replaces 101, 105, 111, 278, 280 and 287. It covers SKILL.md: the record-file test, the home of a standing rule, the second supersession, the condition row of the table, open question 4, and `## Starting an effort`. It also makes three small GC changes: who runs `### Change the map`, `### Start an effort`, and the `## Destination` line.
- **G1** replaces 146, 153, 195, 201, 206, 228, 233 and 308. It covers GC: which file of the map holds what, and where the never-delete rule reaches.
- **G2** replaces 49, 238, 239, 286 and 288. It covers GC: procedures, mechanical checks and scan rules.
- **G3** replaces 73 and 79. It covers GC: the annotation section, and what a hard rule is.

None has a blocker in the graph. M1 and M2 share SKILL.md. M2, G1, G2 and G3 share `graph-conventions.md`. So none of them may run at the same time as another that shares its file, or as the crossing nodes 109, 120, 124, 258, 327, 137 or 285. M1's landing-policy sentence is also the subject of the record nodes 276 and 254. Where C11(a) is taken, G2 lands before M2.

**4. Demands left out because they are already met or stale**

- 118 clause 2 (send a waiting question at once, and an idle human with a question waiting is a defect) is met by `## The order you act in`: "Do every act below that you can do, in the order given, all in one turn", item 4, the item 5 check, and "A turn that ends with the human idle while something waits is your defect". M1 clause 20 keeps it as a fence. Its "at most one question" half is reconciled in C1.
- 118 clause 3 (a ceiling the effort may set) is left out under C1's recommended option.
- 195 clause 3 (the never-delete paragraphs say which files move their superseded text out) is met by node 194's landed text: "Text that states a rule that currently binds is replaced by its current form … `map.md` is written this way, and so is every sibling of it that states rules that currently bind." G1's 233 clauses reword those paragraphs anyway.
- The numbered-steps half of 195 clause 2 is met: step 2 already reads "`map.md`, or the sibling the item came from". Only the opening sentence is carried.
- 101's "No text is deleted… marked as superseded and left where it is" is stale against GC's opening ("Edit … every file the effort ships, plainly"). It is left out under C2.
- 73 clause 4 is left out under C8.
- 192, whole: met by `### Picking the next node` ("When a node finishes, pick the next one, spawn its worker…"; "When a node finishes, start enough work to bring every count back up"), by the same-turn order, and by the triggers file's first bullet. It is a candidate for supersession as made unnecessary by landed work.
- Quotes the rewrite made stale are re-pointed to the current text:
  - 238 and 239's `## Procedures` opening line. It is now "Each procedure lists every file it changes, in the order the changes are made."
  - 79 clause 4's "that document's existing statement that the manager is the graph's only writer". Since node 312, that statement is in SKILL.md `## Writing the graph`.
  - 111 clause 10's `## The five files`. The heading is now `## The seven files`.
  - 111's "eight procedures" becomes "the procedures already there", because G2 adds two.
  - 111's heading counts are dropped.
  - 238 clause 2's "all ten" becomes "all the checks", because G2 adds one.
  - 96 clause 6's "eight … not reduced to seven" is replaced by the fence union below.

**5. Conflicts for the human.** The conditions in NEW NODES are written to each RECOMMENDED option. The alternative clause text is given so that another choice can be pasted in.

- **C1. What is in front of the human (118 against 127).**
  - 118 clause 2 asks for "at most one question is in front of the human at a time". 118 clause 3 asks that "the ceiling … is a number the effort may set … The text reads correctly if the number is not one."
  - 127 clause 1 asks for "exactly one thing awaiting their reply … it may carry more than one question from that one worker and still counts as one". 127 clause 2 forbids saying exactly one *question*.
  - The file says "Keep exactly one question in front of the human at a time". The map's rule, in the human's words, is one question at a time.
  - (a) RECOMMENDED: at most one thing, and exactly one whenever something waits; a payload of one worker's questions counts as one; drop 118 clause 3. Grounds: node 117 resolved batching inside one node, which is what 118 clause 3 hedged against, and the human's rule is one.
  - (b) Keep 118 clause 3. M1 clause 1 then reads: "…at most the effort's number of things awaiting their reply, one unless the effort's map sets another, and never fewer than that number while things are waiting; the text reads correctly if the number is not one…"
- **C2. Strike-in-place in a shipped file.**
  - 101 asks: "No text is deleted from the file. Where a sentence … is superseded … it is marked as superseded and left where it is". 120 clause 4 and 124 clause 9 ask the same for `CONTEXT.md`.
  - GC's opening says: "The never-delete rule covers only the graph's own files … Edit … every file the effort ships, plainly: remove superseded wording".
  - (a) RECOMMENDED: drop the demand and edit plainly (rule from nodes 189 and 194).
  - (b) Keep it for 101's section only, adding to M2: "No text is deleted from that section; a superseded sentence in it is marked as superseded and left where it is."
- **C3. No section of SKILL.md covers "revision and supersession"**, which 105 asks for ("sit in whichever existing section of that file covers revision and supersession"). The nearest are `### What reject means` and the final paragraph of `## When an agent dies or is stopped`.
  - (a) RECOMMENDED: the worker picks an existing section whose subject includes superseding a node and names it in its handover (M2 clause 10).
  - (b) Name `### What reject means`.
  - (c) Allow a new subsection under `## Writing the graph`.
- **C4. "charting" (111 against node 112).**
  - 111 clause 2 asks that the section "names both: **charting** … and **adoption**".
  - Node 112, resolved, decided that "`charting` is refused and the conversation input is never named". Node 247's condition ships that refusal into the glossary's `_Avoid_` line.
  - (a) RECOMMENDED: name that way by its input only, and never use the word `charting` (M2 clause 16).
  - (b) Keep the word.
- **C5. "Five files" against `## The seven files` (111).**
  - 111 clause 2 says "the effort's five files". 111 clause 8 lists "`map.md`, then `map-history.md`, `decisions.md`, `flags.md`, and the `nodes/` directory". GC now lists seven, adding `map-manager-only.md` and `map-implementation-rules.md`.
  - (a) RECOMMENDED: the procedure creates every file listed under `## The seven files`, `map.md` first and the first node files last, with the order of the rest left to the worker (M2 clause 22).
  - (b) Keep the five, and do not create the two siblings at start. M2 clause 22 then reads: "…in order: `map.md`, then `map-history.md`, `decisions.md`, `flags.md`, and the `nodes/` directory, and then the effort's first node files by the steps under `## Adding a node`." M2 clause 16 then says "the effort's files".
- **C6. Name the sibling, or stay generic (153 and 206 against 228).**
  - 153 wants the file to name "the file in `.scratch/graph-workflow/` that actually holds it". 206 clause 2 wants `## Labels` to name `map-manager-only.md`.
  - 228 clause 1 wants each such statement to "name the map as a whole or say plainly that the item lives in `## Notes` unless the effort has moved it to a sibling". Its own question calls the shipped file generic.
  - Today the file contradicts itself. `## The seven files` says "`map-implementation-rules.md` holds the bar's commands", while the `## Notes` line says map.md's Notes holds them.
  - (a) RECOMMENDED: name `map-manager-only.md` for the label vocabulary and `map-implementation-rules.md` for the bar's commands, since the seven-files layout is the workflow's own. 228's generic wording then applies only to the ground rules and the sources declaration (G1 clauses 1, 2 and 4).
  - (b) Use 228's generic wording for all four. G1 clause 1's naming sentence and clause 4's second sentence are then replaced by: "Each such statement names the map as a whole, or says the item lives in `map.md`'s `## Notes` unless the effort holds it in a sibling file of the map."
- **C7. 228 clause 3, "The file names no file outside the seven it lists".**
  - This is false of the file today, which names `SKILL.md`, `CONTEXT.md` and `wayfinder-divergences.md`. It would also bar 73 clause 4.
  - (a) RECOMMENDED: narrow it to "no file of an effort's directory other than the seven" (G1 clause 21).
  - (b) Drop it.
- **C8. 73 clause 4, "It cites `nodes/69-explicit-subagent-definitions.md` by name".**
  - It conflicts with ground rule 1 in `map-implementation-rules.md`: "Nothing in the shipped files may assume this repo". A shipped `graph-conventions.md` in another repo has no node 69.
  - (a) RECOMMENDED: drop it.
  - (b) Keep it, adding to G3: "It cites `nodes/69-explicit-subagent-definitions.md` by name as where the distinction was established."
- **C9. Where an amendment marks the old clause (233 against the file and the record).**
  - 233 clause 4 asks that a superseded clause of a condition be "marked superseded where the clause itself stands". Node 199, resolved, fixed this.
  - SKILL.md `### Changing one after it is written` item 3 says an amendment "is kept apart from the minting author's text, and never merged into it". Every amendment on the record leaves the minting condition "as it was".
  - (a) RECOMMENDED: keep 233 clause 4. A mark is not a merge, and the amendment's text still sits apart. Afterwards the manager's filing practice marks the replaced clause in place.
  - (b) Drop 233 clause 4's "where the clause itself stands" half.
- **C10. The landing-policy half of 231.** `map-manager-only.md` says "**The gate payload names the worktree's path and the command that shows its diff**". Record nodes 276 and 254 edit the same sentence.
  - (a) RECOMMENDED: M1 also makes that record edit (M1 clauses 17 and 18). Node 283, resolved: "a record edit rides the shipped node that would otherwise contradict it".
  - (b) M1 changes SKILL.md only; delete M1 clauses 17 and 18 and drop both `.scratch` paths from M1's scope. The landing-policy half is then added to node 276's condition.
- **C11. `### Start an effort` gets no check step.** Node 213, resolved, says "each procedure gains a final step naming the checks its writes can falsify", and G2 carries this for the existing procedures. M2's new `### Start an effort` is not required to have one.
  - (a) RECOMMENDED: G2 lands first, and M2 gains: "`### Start an effort` ends with a numbered step naming, by number, the checks under `## Mechanical checks` that its writes can make false, and stating that the party performing the act runs them itself at that act."
  - (b) Leave it for a later node.
- **C12. 79 against SKILL.md's open question 6.** Once G3 ships the annotation section, SKILL.md `## What nothing here settles` item 6 ("Where does an annotation onto an already-resolved node belong? … defines no section for them") is false.
  - (a) RECOMMENDED: G3 also removes that item from SKILL.md, or points it at the new section, and renumbers the list. G3 then gains: "In `.claude/skills/expedition/SKILL.md`, the item under `## What nothing here settles` asking where an annotation onto an already-resolved node belongs is removed, the list is renumbered to run from 1 with no gap, and nothing else in that file changes."
  - (b) Leave it for a later node.

**6. Conflicts between fences, resolved by the union rule without a choice**

- 96 clause 6 ("the eight duties … are not reduced to seven"), 105 ("the list … is not reduced"), 280 clause 2 ("none is removed") and 161 clause 2 (remove item 5). M1 removes exactly that one item and keeps item 1 as an open question. M2 measures item numbers as they stand when its work starts.
- 238 clause 5 ("exactly ten items … No check is added"), 239 clause 4, 49 clause 3 and 201 clause 4 ("the list's count and order are unchanged"), against 238 clause 4 (check 5 reworded), 201 clause 3 (check 6), 146 (check 10), 288 (one new check) and 233 clause 7 (at most one optional new check). Items 1 to 10 keep their numbers, and new checks are appended.
- 278 clause 2 ("No other row's second cell changes") against 231's change to the diff row. The two sit in different merged nodes, and each fences only its own work.
- 233 clause 7 ("`### Change the map` … numbered steps are unchanged") against 238(h) and 288 clause 4 (G2 adds a step) and 287 clause 5 (M2). They sit in different merged nodes; G1 changes only the opening sentence.

**7. Resulting facts later nodes depend on**

- Where each item lives in this effort's map: the label vocabulary is in `map-manager-only.md` `## Notes` ("Label vocabulary for this effort: none declared"). The bar's commands and the ground rules are in `map-implementation-rules.md` `## What the work is held against`. The fog is in `map-manager-only.md` `## Not yet specified`.
- The 111 enumerator `grep -rln -i "starting an effort\|start an effort\|charting\|adoption" .claude/skills CONTEXT.md` still returns no files at `c3ecda3`.

INDEX LINE:    Node 330 found 45 open nodes on the manager contract and graph-conventions: five merged nodes replace 26, ten cross groups, nine stay out, twelve conflicts.

FLAGS:
ASSUMPTION — I split the group into five merged nodes by section: two on `SKILL.md` and three on `graph-conventions.md`. The alternative was one node per file, which would carry about 45 clauses for `SKILL.md` and about 50 for `graph-conventions.md`. I judged that too much for one worker session and one checker run. Nodes 111 and 287 each change both files. I put each of them whole into the `SKILL.md` node M2 rather than splitting one node's demands across two merged nodes, so that the two halves of each rule land together. No round took place on this node. What I did was read the three files at `c3ecda3`, check every open implementation node against them, and read the `decisions.md` lines the spawn named.
  Index sentence: At node 330 the manager-contract group was split into five merged nodes by section, and nodes 111 and 287, which change both files, were kept whole inside one.
ASSUMPTION — I left some demands out of the merged conditions, judging by reading the file at `c3ecda3` that they are already met: 118 clause 2, the numbered-steps half of 195 clause 2, 195 clause 3, and all of node 192. I also re-pointed quotes in 79, 96, 111, 238 and 239 that the plain-English rewrite had made stale. The checker reads only the merged conditions. So if one of these judgements is wrong, the demand is lost with nothing reporting it. Each is listed with its reason in this node's answer.
  Index sentence: At node 330 five replaced nodes' demands were judged already met at c3ecda3 and left out of the merged conditions, and five nodes' stale quotes were re-pointed to the current text.
ASSUMPTION — Nodes 231 and 308 had no acceptance condition. I wrote their demands into M1 and G1 myself. 231's demands come from its question and the human's words quoted there: the path stays and the diff command goes, in both the shipped contract and the landing policy. 308's demand is only that the fence and the prose agree about how often `map.md` is read, and the worker chooses the wording.
  Index sentence: At node 330 the demands of nodes 231 and 308, which had no condition, were written by the grouping worker from their questions into merged nodes M1 and G1.

NEW NODES:

--- M1 ---
Name: Carry the rules on what reaches the human, the code-slot count and the gate's pointer to the work into the manager contract
Kind: implementation
Supersedes: 96, 118, 127, 161, 231
Blockers: none
Question: Nodes 96, 118, 127, 161 and 231 each change a few lines of the manager contract's rules on what is in front of the human, how a report ends, how many implementation nodes run, and what a gate payload points at. Make all their changes in one piece of work.
Acceptance condition:

> The work is `.claude/skills/expedition/SKILL.md`, plus `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md` for clauses 17 and 18 only. No other file changes. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. The places named below are the work itself rather than instances of a defect spread across the tree, so this scope came from no search. `SKILL.md` is a file the workflow ships, so it is edited plainly: superseded wording is removed, and nothing in it is struck through or moved to a history file.
>
> Done means every one of the following is true of the finished tree. Each clause names, in brackets, the node its demand comes from.
>
> **What is in front of the human.** These clauses apply to the section headed `## What is in front of the human, and when`, unless a clause names another place.
>
> 1. (127, 118) The section states that at most one thing awaiting the human's reply is in front of them, and exactly one whenever something is waiting, and that nothing displaces a live one. Where that thing is a payload relayed from a worker, it may carry more than one question from that one worker and still counts as one thing.
> 2. (127) The section no longer states that exactly one *question* is in front of the human. Before this work it opens "Keep exactly one question in front of the human at a time."
> 3. (127) The file states that the manager never combines questions from different nodes into one payload, and never divides one payload's reply between two workers. A payload comes from one worker, and its reply goes back to that one worker unaltered.
> 4. (127) The rule that every relayed question names, in one line, whatever else is waiting, by node name and kind only and never restating another question or its options, is kept. The section gives as that rule's reason that a thing named in that line but not asked cannot be answered by accident. It does not justify the rule on the ground that it keeps a terse reply attributable to exactly one thing.
> 5. (118) The file states that a question occupies the human's channel only while it awaits their answer, so the channel is free from the moment the manager records their reply. It states three consequences by name:
>    - a gate answered with a correction leaves the channel free for the whole of the correction round and any re-check that follows;
>    - anything the manager sends that awaits no answer, such as the report of a pick, a notice that an agent died, or the closing report, leaves the channel free the instant it is sent;
>    - a node waiting at its gate, a worker running, or a check in flight does not occupy the channel at all.
> 6. (118) The file states that the manager sends a question that is already waiting, and never makes one up to give the human something to do.
>
> **The last line of a report**
>
> 7. (96) The file states that every report the manager puts in front of the human ends with one short line naming what is expected of them, and that this line is the last thing in the report. It states the reason: the human can look at the last line alone and know what they must act on. It states that the line names the act or the choice being asked for and is short. It prescribes no fixed set of wordings.
> 8. (118) The file states that this line says what is expected of the human at the moment it is written, and promises nothing about when the manager will next send what is waiting. It also states that a line saying nothing is expected of them is written only when nothing is waiting.
> 9. (96) Every existing statement of what a report or a payload that reaches the human must carry still holds. The new rule adds a closing line and removes nothing any section requires.
>
> **The code-slot count**
>
> 10. (161) The bullet under `### Picking the next node` beginning "How many implementation nodes run at once." states that raising the count buys parallel implementation at the price of conflicts to resolve when the work is integrated, and that the human sets the number. It states that the manager neither raises the count on its own judgement nor treats the effort's current value as a ceiling it must justify leaving. It states that the manager names this trade when the human moves the count.
> 11. (161) Under `## What nothing here settles`, the item reading "What does a worker do when a file it must read is being changed by whoever holds the code slot?" is removed, together with the two sentences after it ("Nothing says. Work that is not code runs beside an implementation node by design, including where the two touch the same file."). The items after it are renumbered so the list runs from 1 with no gap and no repeat.
> 12. (161) Text elsewhere in the file states what replaces that item. Every worker reads a consistent snapshot, an implementation worker its own working tree and every other worker the main checkout, so no worker reads a file while it is being changed. Two snapshots that differ are reconciled when the work is integrated, not while it is read.
> 13. (161) `SKILL.md` names no branch, worktree, rebase or merge command, and describes no git lifecycle.
> 14. (161) Wherever `SKILL.md` states how many items `## What nothing here settles` holds, the count agrees with the items present.
>
> **The gate payload's pointer to the work**
>
> 15. (231) Under `### The payload`, the bullet that before this work reads "Where the work is, and the command that shows its diff. A gate that describes a change and points at nothing has not been presented." still requires the payload to say where the work is, by the path of the working tree that holds it. It still says that a gate which describes a change and points at nothing has not been presented. Neither that bullet nor any other sentence of `SKILL.md` asks for a command that shows the diff.
> 16. (231) In the table under `## What is never yours`, the row whose first cell is "rendering a diff into the conversation" keeps that first cell. Its second cell, which before this work reads "say where the work is and what command shows it", says where the work is and names no command. The sentence "Keep two things out of the payload: the diff, and the acceptance condition." still stands.
> 17. (231) In `.scratch/graph-workflow/map-manager-only.md`, under `## Landing an implementation node's work`, the sentence that before this work begins "**The gate payload names the worktree's path and the command that shows its diff**" no longer requires the command that shows the diff, and still requires the gate payload to name the worktree's path. The rest of that sentence, including the ground it gives, keeps its meaning. Nothing else in that file changes.
> 18. (231) The rule text that clause 17 replaces is appended verbatim to `.scratch/graph-workflow/map-history.md`, under a heading mirroring the section it came from, with struck-through text staying struck through. `map-history.md` gains text and loses none.
>
> **What does not change**
>
> 19. (118, 127) These keep their meaning:
>     - that nothing displaces a live question;
>     - the two tiers, tier 1's three fixed kinds, and that only the human can add a fourth kind;
>     - that things within a tier are taken in the order they arrived;
>     - the list beginning "Three things never enter the queue:", together with the three things it lists, neither extended nor renumbered.
> 20. (118) The statements under `## The order you act in` keep their meaning, in particular "The human should always have something to do", "A turn that ends with the human idle while something waits is your defect", and the check at item 5 that is run before the manager writes that nothing is expected of the human.
> 21. (96) Under `## What nothing here settles`, the item asking "What must your report to the human contain?" still stands as an unsettled question. The only item this work removes from that list is the one clause 11 removes.
> 22. (96, 118, 127, 161) No section of `SKILL.md` is removed, and no rule in it changes its meaning other than as clauses 1 to 16 state.
> 23. The working tree meets the bar.

--- M2 ---
Name: Carry the record-file test, the home of a standing rule, the second supersession and starting an effort into the manager contract
Kind: implementation
Supersedes: 101, 105, 111, 278, 280, 287
Blockers: none
Question: Nodes 101, 105, 111, 278, 280 and 287 each add or repair a few statements in the manager contract's sections on writing the graph, standing rules, what is never the manager's, its open questions and starting an effort, with small matching changes in `graph-conventions.md`. Make all their changes in one piece of work.
Acceptance condition:

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

--- G1 ---
Name: Say in graph-conventions.md which file of the map holds what, and where the never-delete rule reaches
Kind: implementation
Supersedes: 146, 153, 195, 201, 206, 228, 233, 308
Blockers: none
Question: Nodes 146, 153, 195, 201, 206, 228, 233 and 308 each correct a few lines of `graph-conventions.md` about which file of a split map holds what, and about where the never-delete rule applies. Make all their changes in one piece of work.
Acceptance condition:

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
>
> **What does not change**
>
> 18. (233, 195) The numbered steps of `### Change the map` are unchanged in content, count and order.
> 19. (201, 233, 146) The numbered list under `## Mechanical checks` keeps its existing items, in their order and with their numbers. The only checks whose text changes are the one clause 17 names and the one clause 3 names. The work may add at most one new item, after the existing ones, stating that a superseded clause of an acceptance condition is marked where it stands.
> 20. (201, 195, 206) No procedure under `## Procedures` is reworded except as clause 7 states, and no section changes other than those clauses 1 to 17 name.
> 21. (228, 201, 233) The file names no file of an effort's directory other than the seven listed under `## The seven files`. Every markdown link in the file outside a fenced code block resolves to a path that exists, and the work adds no link to a path that does not exist.
> 22. (206) The file names no plugin, requires no skill to be invocable, and assumes no particular repository, machine or toolchain.
> 23. The working tree meets the bar.

--- G2 ---
Name: Tie graph-conventions.md's mechanical checks to the writes that can make them false
Kind: implementation
Supersedes: 49, 238, 239, 286, 288
Blockers: none
Question: Nodes 49, 238, 239, 286 and 288 each change `graph-conventions.md`'s procedures, mechanical checks and scan rules: which act runs each check, two writes with no procedure, a check on the history bank, the rules a check needs, and how to read a `Blocked by:` field. Make all their changes in one piece of work.
Acceptance condition:

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

--- G3 ---
Name: Add the annotation section and what a hard rule is to graph-conventions.md
Kind: implementation
Supersedes: 73, 79
Blockers: none
Question: Nodes 73 and 79 each add one passage to `graph-conventions.md`: 73 what kind of thing a hard rule in a worker contract is, and 79 a section for the annotation the manager writes onto a node whose answer a later node changed. Make both in one piece of work.
Acceptance condition:

> The work is `.claude/skills/expedition/graph-conventions.md`. No file outside `.claude/skills/expedition/` changes. No file under `.claude/skills/expedition-checker/`, `expedition-grilling/`, `expedition-implementation/`, `expedition-precondition/`, `expedition-prototype/` or `expedition-research/` changes, so `git diff` over those six directories comes back empty. No file under `.scratch/` changes. The file is one the workflow ships, so it is edited plainly. The places named below are the work itself, so this scope came from no search.
>
> Done means every one of the following is true of the finished tree. Each clause names, in brackets, the node its demand comes from.
>
> 1. (79) The section that documents a node file's sections, `## The node file`, gains a statement of one more kind of section a node may carry: an annotation, written by the manager onto a node whose answer a later node has changed the meaning of. It states three things:
>    - an annotation records what a later piece of work changed about this node's answer;
>    - its text is the reporting agent's own words where a reporting agent supplied them;
>    - it is added rather than replacing anything the node already holds.
> 2. (79) It states where an annotation sits relative to the six sections already listed there (`## Question`, `## Acceptance condition`, `## Answer`, `## Flags`, `## Review`, `## Interview`). So the file's rule that sections appear in the order shown, and only when they have content, is true of a node carrying one. Whether the annotation is one section or several, and where in the order it falls, is the worker's to choose and to state.
> 3. (79) It states that an annotation may carry a heading naming what it records, and gives the form of that heading.
> 4. (79) It states that an annotation is the manager's to write and never a worker's. This is consistent with `SKILL.md`'s `## Writing the graph`, which makes the manager the only writer of the graph's record.
> 5. (79) Whatever the file already fixes about a node file is still present afterwards and has lost nothing it required: the mandatory fields, the rule that fields live in the header block and nowhere else, the six section names, and the statement that sections appear in the order shown and only when they have content.
> 6. (73) The file gains one new section, under a heading of the worker's choosing and at most 200 words long, holding all three of the following:
>    - It states that a hard rule in a worker contract binds by being read by the agent the contract was given to, and that no mechanism in the shipped workflow enforces one.
>    - It states the distinction in both directions. A contract says what a worker **may** do, and what a worker **can** do is a property of the harness that ran it. A clause of the first kind survives a change of harness, and one of the second kind does not.
>    - It states the consequence for anyone writing or editing a contract. A rule that would be false on a harness unable to enforce it does not belong in a shipped file. The remedy for a rule agents read down is a better-written rule or a granted exception, never an assumed capability.
> 7. (73, 79) The file's existing headings, listed by `grep -n '^#\{1,6\} '`, are all still present afterwards and in the same order, with the new material added rather than replacing any of them. No existing text is deleted or reworded, except where clause 2 needs the statement of section order to include the annotation.
> 8. The working tree meets the bar.

INVALIDATIONS: No resolved node is contradicted. The recommended options follow resolved nodes: 112 for C4, 117 for C1, 189 and 194 for C2, 199 for C9, 213 for C11 and 283 for C10.
- Superseding the 26 nodes that M1, M2, G1, G2 and G3 replace makes their conditions void once the human approves.
- Open nodes affected outside this group:
  - Node 276, and node 254, edit the same `map-manager-only.md` sentence as M1 clause 17, so they must not run at the same time as M1.
  - Node 137's renaming of "pick report" and node 106's gate on `CONTEXT.md` do not touch these conditions' words.
  - Node 56's condition does not reach SKILL.md's two mentions of "the glossary, `CONTEXT.md`".
  - Node 41 clause 5's "`map.md`'s `## Notes`" for ground rules becomes stale once G1 lands.
  - Node 120's clauses 1 and 3 are contradicted by node 124's approved condition and node 123's decision, as already annotated on node 120.

RETROSPECTIVE:

1. **What I had to hunt for.** Which nodes touch the three files, because no field records a node's files. I grepped every open node's condition for paths and for "manager's contract". Nodes with no condition (185, 192, 170, 231, 308, 317, 40, 87, 89) needed their question read to know their file. For every quoted sentence I checked the current text against the file to find stale quotes. I also had to find where this effort's label vocabulary, bar's commands and fog now live, and which resolved decisions (112, 117, 189, 199, 213, 283) settle each conflict. Node 276 sharing 231's sentence surfaced only by chance.
2. **What arrived that this node did not need.** Almost all of `map.md`'s `## Notes`; only the grouping bullet and the diff-command bullet bore on the work. Of the `decisions.md` lines the spawn named, the plain-English rewrite lines were not needed. Much of each node file was also unused: long manager notes about sequencing a congested file, and accounts of how each defect was found.
3. **What would have made this easier.** A list or script giving each open implementation node's scope sentence, or the files its condition names. The other two groups' file lists stated in the spawn, so "crosses groups" is decidable at once; I inferred them. A node file saying "changes any of" rather than "changes A, B and C". Conditions quoting current text with the commit they quote.
4. **What was stale, wrong or contradictory.**
   - The spawn named node 95 as touching these files; it is resolved.
   - 238 and 239 quote a `## Procedures` opening line that no longer exists.
   - 111 has "five files", "fourteen headings" and "charting", all stale or refused.
   - 101, 120 and 124 ask for strike-in-place in shipped files.
   - 228 clause 3 is false of the file today.
   - 73 clause 4 conflicts with ground rule 1.
   - 79 clause 4 points at a statement that moved to `SKILL.md`.
   - 137's GC count of 3 "pick report" is now 0.
   - 49's inventory predates check 9.
   - 106's gate reverts part of 137's clause 1.
   - `SKILL.md`'s open questions 5 (by 161) and 6 (by 79) are answered or about to be.
   - `graph-conventions.md` contradicts itself on where the bar's commands live.
   - The `## Question` of this node says "changes `SKILL.md`, `graph-conventions.md` and `expedition-triggers.md`", which read literally means all three at once. I read it as any of them.

## Interview

### The manager's raise, 2026-09-26

*The manager's own raise, sent after node 329's decision:* whether to file the five merged nodes M1, M2, G1, G2 and G3, superseding the 26 nodes they replace, taking the worker's recommended option on each of C1 to C12; whether to merge nodes 120, 124 and 258 into one node as the worker recommends, its condition to be written by a worker; whether to supersede node 192 as done; and the manager's own proposal to fold node 329's remainder R1 (the `graph-conventions.md` sentences of nodes 148 and 43) into G1.

The human, `verbatim`: *"ok"* — taking the whole proposal as the manager put it.

## Flags

`330.1` **· settled** `ASSUMPTION` — I split the group into five merged nodes by section: two on `SKILL.md` and three on `graph-conventions.md`. The alternative was one node per file, which would carry about 45 clauses for `SKILL.md` and about 50 for `graph-conventions.md`. I judged that too much for one worker session and one checker run. Nodes 111 and 287 each change both files. I put each of them whole into the `SKILL.md` node M2 rather than splitting one node's demands across two merged nodes, so that the two halves of each rule land together. No round took place on this node. What I did was read the three files at `c3ecda3`, check every open implementation node against them, and read the `decisions.md` lines the spawn named.

`330.2` **· settled** `ASSUMPTION` — I left some demands out of the merged conditions, judging by reading the file at `c3ecda3` that they are already met: 118 clause 2, the numbered-steps half of 195 clause 2, 195 clause 3, and all of node 192. I also re-pointed quotes in 79, 96, 111, 238 and 239 that the plain-English rewrite had made stale. The checker reads only the merged conditions. So if one of these judgements is wrong, the demand is lost with nothing reporting it. Each is listed with its reason in this node's answer.

`330.3` **· settled** `ASSUMPTION` — Nodes 231 and 308 had no acceptance condition. I wrote their demands into M1 and G1 myself. 231's demands come from its question and the human's words quoted there: the path stays and the diff command goes, in both the shipped contract and the landing policy. 308's demand is only that the fence and the prose agree about how often `map.md` is read, and the worker chooses the wording.

*The manager's note, 2026-09-26:* [node 341](341-draft-one-condition-for-nodes-120-124-and-258.md)'s worker reports, under its `INVALIDATIONS`, that this answer's entry for node 258 is false: "That is the same entry as 120's clause 4, which 120's clause 6 already reaches." Clause 6 reaches only files under `.claude/skills/`, and `CONTEXT.md` is at the repository root. The recipe node 341 was minted with rested on it; that worker carried the Attempt-entry clauses anyway and put the choice to the human as its K1.
