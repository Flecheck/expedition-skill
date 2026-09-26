# Group the open nodes against the glossary

Type: precondition
Status: resolved
Blocked by: none

## Question

Most open implementation nodes change a few lines of one file each, and their conditions forbid touching anything else, so two nodes on the same file cannot be worked together. The human asked for them to be grouped by file. Which open nodes change `CONTEXT.md` (the glossary), and what merged node or nodes should replace them?

*Minted by the manager on the human's "You can do the groups", recorded in the map under `## Notes`.*

## What must be true when this is done

- Every open or unclaimed implementation node whose condition changes `CONTEXT.md` (the glossary) is listed, with the node number, its name and the part of the file it changes. A node that also changes files outside this group is listed and marked as crossing groups.
- For each proposed merged node: its name, the nodes it replaces, and an acceptance condition that carries each replaced node's demands with the node each came from. Where a replaced node's clause fences its own node ("no other entry changes"), the merged condition fences the union instead. Where a demand is already met by the file as it stands, or is stale, that is said and the demand is left out, with the reason.
- Every conflict is listed: between two replaced nodes' demands, or between a demand and the file as it stands. Each conflict says which nodes and which words, and offers the options. These go to the human.
- Nodes left out of any merge are listed, with the reason.

**Later nodes depend on:** the merged nodes' conditions, which the manager files as new nodes once the human approves the supersessions.

## Answer

Four glossary-only open nodes (90, 92, 134, 247) merge into one; nine that also change another group's files are listed as crossing, and eight conflicts go to the human.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, and the human's decision under `## Interview`. On the human's "ok", the merged node is [node 332](332-repair-the-glossarys-code-slot-reject-kinds-grilling-and-closed-text.md), carrying C1(a) and C2(a); nodes 90, 92, 134 and 247 are superseded by it, and node 61 by node 76 (C7). The other outcomes are noted on nodes 81, 111, 56, 137, 120 and 258.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Group the open nodes against the glossary

ANSWER:

Read at HEAD `64db5aa`. `CONTEXT.md` was last changed at `3529bec` and has 51 term entries and 41 `_Avoid_` lines. Node 106's work is not in the main tree yet. Following the manager, its text is treated as the file's state for the **Closing report** entry.

**1. Every open implementation node whose condition changes `CONTEXT.md`**

Glossary only. These are merged:
- **90** "Bring the glossary's `Closed` entry off the rejected frequency claim". Changes the third sentence of **Closed** (`## Closing an effort`).
- **92** "`CONTEXT.md`'s Code slot entry contradicts the map on both of its claims". Changes the **Code slot** definition (`## Working a node`).
- **134** "Repair the two `CONTEXT.md` defects node 113 found". Changes the opening paragraph of `## The five kinds of node` and the **grilling** definition. Its blocker, 133, is resolved.
- **247** "Write the glossary's starting-an-effort entries". Adds a new section `## Starting an effort` with two entries.

Crossing groups. Listed only, not merged:
- **81** "Bring the glossary's code-slot and reject entries up to the worktree lifecycle". Changes **Code slot** and **Reject**. Its entry 3 also changes `expedition-prototype/SKILL.md`'s `code slot` line, which is in node 329's group. See conflict C1.
- **137** "Rename the two reports and repair the `_Avoid_` line that reserved the word". Changes these parts of the glossary: renames **Closing report**, adds a node closing report entry under `## Talking to the human`, changes the `_Avoid_` line of **Handover**, and replaces `pick report` in **Flag** (line 186) and **Raise** (line 228). It also changes `expedition/SKILL.md`, `graph-conventions.md` (node 330's group) and `expedition-precondition/SKILL.md` (node 329's group). It conflicts with node 106 (C6).
- **57** "Give a research node the cannot-proceed raise". Changes the **research** entry. It also changes the research contract (329).
- **61** "Collapse the manager's discipline onto the leading word `scribe`". Adds a `scribe` entry. It also changes five worker contracts (329). Stale: the file already has a **Scribe** entry (C7).
- **120** "Carry the resume rule into the shipped files". Changes the **Attempt** entry. It also changes `expedition/SKILL.md`, `graph-conventions.md` and any other shipped file (330).
- **258** "The manager's contract contradicts itself on whether a dead worker is resumed or replaced". Changes the **Attempt** entry. It also changes `expedition/SKILL.md` (330).
- **124** "Give the manager's contract a procedure for stopping a running worker". Its clauses 6 and 9 add or amend entries for the words used for a stop. It also changes `expedition/SKILL.md` and `graph-conventions.md` (330). It is blocked by 120.
- **109** "Carry the extent rule into the shipped files". Changes `CONTEXT.md` only if a term moves (clause 8). It also changes seven contract and convention files. It is blocked by 95 and 103.
- **41** "Ship the FRICTION flag and the self-edit disclosure duty". Its condition never names `CONTEXT.md`. Under node 29's mechanism, though, its worker owes a `FRICTION` entry by way of the bar. It also changes `graph-conventions.md` and five contracts. It is blocked by 56.

**2. The merged node**

"Repair the glossary's code-slot, kinds-of-node, grilling and closed text, and add its starting-an-effort section". It replaces 90, 92, 134 and 247. Its condition is given in full under NEW NODES. It changes no entry that node 106 or any crossing node changes, except **Code slot**, which node 81 also changes (C1). Sequencing: claim it after 106 lands and before 56.

Demands already met or stale, and left out:
- **134, filed condition clause 2, first half**: that grilling no longer says "one question at a time", and that several questions go in one payload with only independent ones sharing it. Met: the current entry says this ("Its worker may put several of its questions in one payload. Only questions that are independent of each other share a payload."), carried by node 177. Only the "held for a later one" half is carried forward.
- **134, filed condition clause 3**: "Superseded text is marked as superseded and left in place rather than deleted". Stale. The map's never-delete rule, bounded at node 189, "reaches no file the workflow ships". Node 134's second condition does not demand it either.
- **134, second condition clause 1**: its quote "Each names what its worker does, and three of them name a skill the worker invokes." Stale since node 302. The current text, "Each kind names what its worker does. Three of the kinds name a skill the worker invokes.", is quoted in its place. The claim is still false. The six-contract scan for `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`, `/research`, `/prototype` and `mattpocock` returns nothing at `64db5aa`.
- **90, 247 and 81**: each allows for the file having moved to `.claude/skills/expedition/CONTEXT.md`. Stale: node 56 now moves it to `.claude/skills/expedition/glossary.md`, and 56 goes last. The merged condition names the root `CONTEXT.md` only.
- **247, fixed baselines 51 → 53 and 41 → 43**: carried as "raises each by exactly two", because node 137 or another node may change the count first.
- **247 clause 1 "no existing entry's text changes", 90 "no other entry changes", 92 clause 3, 134 clause 4 and "nothing else changes"**: each fences its own node. They are replaced by one fence over the union.
- **247 clause 8** (the `Expedition` entry is byte-identical): kept explicitly. The union fence also implies it.
- **92**: its four clauses stand. The current text still says "held by one worker at a time" and "Occupancy is discovered from the working tree rather than recorded". `map-manager-only.md` says occupancy comes "from counting" the live worktrees.
- **90**: stands. The sentence "Most efforts are never closed, and that is a legitimate steady state." is still present. Conflict C2 affects its replacement.

**3. Conflicts, for the human**

**C1. Node 81 crosses groups, and it changes the same Code slot entry as 92.**
Its entry 1 asks for the same thing as node 92, plus: "which may be more than one", and "Both sentences are false". The second sentence includes "so a dying worker leaves nothing behind to clean up", which is false now that a worktree is left behind. Its entry 2 changes **Reject**. Its entry 3 changes the prototype contract, which currently reads "the right to modify product code, held by one worker at a time. It is never yours."
- (a) *Recommended.* Split 81. Its entries 1 and 2 join the merged node, entry 3 joins node 329's merge, and 81 is superseded by both. Add these to the merged condition:
  - In clause 1: "It also states that the number of slots may be more than one. The current second sentence's claim that a dying worker leaves nothing behind to clean up does not survive." *(81, entry 1)*
  - A new clause: "**Reject** (`## Landing code`) currently contains the sentences 'On a reject the node does not resolve, and the working tree is cleaned. What is kept is the discovery.' After the work, the entry no longer says the working tree is cleaned. It says that on a reject the manager removes that node's worktree and deletes its branch, and that where the human asks for the work to be kept, it is committed onto that branch before the directory is removed. It still says that the node does not resolve and that what is kept is the discovery. 'The human's finding at the gate that implementing the node revealed that its code should not exist.', 'A reject is not a verdict on quality: a node whose code is merely wrong takes a correction round.', 'The word is the human's alone; the checker's outcomes are `PASS` and `FAIL`.' and `_Avoid_: refuse, discard, abandon (which names losing the code, not learning why)` are left exactly as they stand." *(81, entry 2, as amended from node 302)*
  - Add the Reject definition to the list of lines the fence allows to change.
  - The keep-the-non-resolution-and-discovery half is my reading. Node 81 calls both sentences false without saying which half survives, and node 81's own `_Avoid_` parenthetical ("learning why") depends on the discovery being kept.
  - For node 329: "`.claude/skills/expedition-prototype/SKILL.md`, `## Words used exactly`: the line `- **code slot** — the right to modify product code, held by one worker at a time. It is never yours.` no longer says 'at a time'. It says one worker holds one slot and that how many slots an effort runs is that effort's own setting. It keeps 'It is never yours.', and stays one line with no `_Avoid_` line. Hard rule 1's sentence 'You do not hold the code slot.' is left exactly as it stands." *(81, entry 3, as amended from node 293)*
- (b) Keep 81 whole and outside the merge. The merged node still changes Code slot for 92, so 81's entry 1 is met by the time 81 is worked. 81 then covers Reject and the prototype line alone.
- (c) Supersede 92 by 81 instead, and drop the Code slot clause from the merge.

**C2. Node 90's replacement vs the Destination entry (node 91).**
Node 90 (written at node 86) asks for an unconditional statement: "an effort whose frontier never empties is in a legitimate steady state rather than a stalled one, and is not to be treated as a defect". The current **Destination** entry, from node 91's later decision, makes this depend on the effort's expectation: "Where the effort is not expected to reach it, that line tells a manager that a frontier that is not empty is the effort's steady state and not a defect." Carried as written, 90 erases the difference node 91 drew for an effort that is expected to end.
- (a) *Recommended.* Amend the clause to: "that an effort whose destination says it is not expected to end, and whose frontier never empties, is in a legitimate steady state rather than a stalled one, and is not to be treated as a defect".
- (b) Keep 90 as written. The merged condition currently carries this.
- (c) Replace the sentence with nothing, since Destination already says it.

**C3. The Code slot demand introduces "worktree" into the shipped files.**
`grep -rn worktree .claude/skills` finds only `expedition-stop/SKILL.md`. The manager contract says nothing about how occupancy is found, and node 89 (330's group) is where the lifecycle goes. Both 81 and 92 require "counting the live worktrees". This contradicts nothing, but the glossary would be the first shipped file to state it.
- (a) *Recommended.* Keep it as 81 and 92 wrote it.
- (b) Word it without the word worktree: "counting the separate working trees the manager has made, one per claimed implementation node".

**C4. Node 247 vs node 111 (330's group) on `charting`.**
Node 247's clause 9 allows `charting` in the glossary only in an `_Avoid_` line, refusing it. Node 111's clause 2 requires its new `SKILL.md` section to name "**charting** … and **adoption**". Node 302's worker reported this, and node 111's note says whoever claims it checks.
- (a) *Recommended.* Amend 111 to refuse `charting`, following node 112's decision.
- (b) Allow `charting` in `SKILL.md`, which contradicts the glossary it points at.

**C5. Node 56 (goes last) vs the merge and the other nodes.**
- Node 56's clause 1 demands exactly **51** term entries. After the merged node it will be 53, and 54 if 137's new entry lands. Its "at least 40" `_Avoid_` lines still hold. Clause 1 needs amending before 56 is claimed.
- Node 56's manager note says "exactly **50**". This is stale and was already reported by node 302.
- These conditions name the root `CONTEXT.md` literally, so they would miss the file if they landed after the move: 137 (scope list, and the enumerators `grep ... .claude/ CONTEXT.md` in clauses 6 and 7), 120 clause 4, 258 clause 2, 124 clauses 6 and 9, 57 clause 5 (no path, so it survives), 61 (scope and clause 1), and 109 (clause 8 and its enumerator).
- The fallback path in 81, 90 and 247, `.claude/skills/expedition/CONTEXT.md`, is stale against the chosen name `glossary.md`.
- 56's clause 3 makes an entry owed for every term a change coins. This bites 41 (`FRICTION`) and 124 (the words for a stop).

**C6. Node 137 vs node 106.**
Already known to the manager. Node 137's clause 1 defines the effort closing report as "what was decided, what landed, and every flag still outstanding", and clause 2 says the renamed entry's meaning is unchanged. Against 106's text ("What the manager hands the human once the frontier empties. It covers only what the human has not already seen. It carries what landed, the supersession chains, the state of the bar, every flag still outstanding, what the sweep found, and every sweep round."), clause 1 would put back the three-item list. Options: amend 137's clause 1 to quote 106's six items, or drop the definition from clause 1 and keep only the rename.

**C7. Node 61 vs the file.**
Its clause 1 asks for a `scribe` entry saying the manager "authors nothing of its own onto" the graph. The existing **Scribe** entry says "Anything of its own goes beside that text, as its own marked note." Its preamble ("appears nowhere in `CONTEXT.md`") is stale, as the manager's notes of 2026-09-24 already record. Options: supersede 61 as largely done, or amend clause 1 to match the existing entry.

**C8. Node 120 vs node 258 vs node 123, on the Attempt entry.**
Both 120 and 258 rewrite **Attempt** ("A node lasts longer than any of its attempts: a worker that dies is replaced, and the replacement is a new attempt.") to "resumed where the harness allows and replaced only where it does not". Node 123 decided that where a resume fails because the human stopped the agent, the fallback is a question to the human, not a replacement. "Replaced only where it does not" is an unconditional fallback. Node 120's clause 4 also asks for superseded wording to be left in place, which is stale for the same reason as 134's clause 3. Options: merge 120's and 258's Attempt clauses in whichever group takes them, worded so that the user-stopped case goes to the human, or leave them to node 330's grouping.

**4. Nodes left out of any merge**
- **56**: on the manager's instruction. It goes last, on its own (see C5).
- **106**: on the manager's instruction. Its work is waiting at its gate.
- **81, 137, 57, 61, 120, 258, 124, 109, 41**: they cross groups (section 1).
- **317** "Which outstanding flags reach the closing report": the manager's note says its work keeps **Flag** in line, but it has no acceptance condition yet, and it also changes `expedition/SKILL.md`.
- **208** and **170**: no acceptance condition. 170 may not touch the glossary at all.
- **101, 148, 190, 279, 284, 287**: name `CONTEXT.md` only as a standard or as a file they must not change.
- **80, 87, 111, 156, 192, 221, 326**: mention it in passing. 111 is in C4.
- Open grilling nodes whose answers may later change the glossary (e.g. 84, 130) are outside this node's scope, which is implementation nodes.

INDEX LINE:    Four glossary-only open nodes (90, 92, 134, 247) merge into one; nine that also change another group's files are listed as crossing, and eight conflicts go to the human.

FLAGS:
ASSUMPTION: I kept node 81 out of the merge because its entry 3 changes the prototype contract, which is node 329's file, even though the manager listed it with the glossary nodes. I offered the split as the recommended option (C1), with the clause text ready to insert. For the part of 81 that would go into the merge, I wrote that the Reject rewrite keeps "the node does not resolve" and "what is kept is the discovery", because 81 calls both sentences false without saying which half survives. No round took place. What I did: I read the node files, `CONTEXT.md`, the map, the glossary lines of `decisions.md`, `map-manager-only.md`'s landing section and the six contracts, and checked each quoted phrase against the file at `64db5aa`.
  Index: Node 81 was listed as crossing groups rather than merged, because it also edits the prototype contract; splitting it was offered to the human.
ASSUMPTION: Of node 134's grilling demand, I carried only the missing half: a dependent question is held for a later payload, as the grilling contract says. I judged the rest met by the current entry. I dropped its clause saying superseded text is marked and left in place, because the never-delete rule does not reach shipped files. I dropped the moved-file path in 90, 247 and 81, relying on node 56 landing last.
  Index: The merged glossary condition leaves out node 134's never-delete clause as stale, and names the root `CONTEXT.md` only, on the ground that node 56 lands last.

NEW NODES:

**Name:** Repair the glossary's code-slot, kinds-of-node, grilling and closed text, and add its starting-an-effort section
**Kind:** implementation
**Question:** Four open nodes each change a few lines of `CONTEXT.md`: 90 (the Closed entry), 92 (the Code slot entry), 134 (the kinds-of-node paragraph and the grilling entry) and 247 (a new starting-an-effort section). Do all four in one piece of work. Supersedes 90, 92, 134 and 247.
**Blockers:** none. Sequencing, not an edge: claim it after node 106 lands and before node 56.
**Acceptance condition:**

> **Which file.** Exactly one file changes: `CONTEXT.md` at the repository root. No other file changes, and no file under `.scratch/` changes. Where this work finds something outside that file that needs changing, it reports it in the handover and does not edit it. *(90, 92, 134, 247)*
>
> **Baselines, to be re-run and reported.**
> - At commit `64db5aa`, `grep -c '^\*\*.*\*\*:$' CONTEXT.md` returns 51 and `grep -c '^_Avoid_' CONTEXT.md` returns 41. This work raises each count by exactly two. Where either count has moved before the work starts, report the starting count. *(247)*
> - At that commit, `grep -rn -i "chart" .claude/skills/ CONTEXT.md` returns nothing. *(247)*
>
> 1. **Code slot.** The entry headed `**Code slot**:` under `## Working a node` currently reads: "The right to modify product code, held by one worker at a time. Occupancy is discovered from the working tree rather than recorded, so a dying worker leaves nothing behind to clean up."
>    - After the work it no longer says the right is held "by one worker at a time", and no longer says occupancy is discovered from the working tree.
>    - It states that how many code slots an effort runs is that effort's own setting, one worker to a slot.
>    - It states that a slot's occupancy is discovered by counting the live worktrees, one per claimed implementation node, rather than by inspecting the working tree for uncommitted changes.
>    - Its `_Avoid_` line, "write lock, code lock — there is no lock", is left exactly as it stands. *(92)*
> 2. **The kinds of node.** Under `## The five kinds of node`, the paragraph before the first entry reads: "Each kind names what its worker does. Three of the kinds name a skill the worker invokes."
>    - After the work, nothing in that paragraph claims that any number of the kinds names a skill the worker invokes. Whatever replaces the second sentence, if anything, is true of the shipped contracts as they stand when the work is done.
>    - That state is tested by a scan of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-checker/SKILL.md` for the strings `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`, `/research`, `/prototype` and `mattpocock`. It returned nothing at `64db5aa`. Re-run it and report what it returns.
>    - The paragraph's first sentence is left as it stands. *(134, both conditions)*
> 3. **grilling.** The entry headed `**grilling**:` currently reads: "A decision only the human can make, reached by interviewing them. Its worker may put several of its questions in one payload. Only questions that are independent of each other share a payload."
>    - Its definition may be reworded. After the work it states all four of these:
>      - a decision only the human can make, reached by interviewing them;
>      - its worker may put several of its own questions in one payload;
>      - two questions share a payload only where neither's answer depends on the other's;
>      - a question whose answer depends on another question in that payload is held for a later payload.
>    - It does not say the human is interviewed one question at a time.
>    - Its `_Avoid_` line, "decision, question, interview", is left exactly as it stands. *(134, both conditions)*
> 4. **Closed.** The entry headed `**Closed**:` under `## Closing an effort` currently reads: "The human's declaration that an effort is over. Only the human closes one; the manager reports that the conditions hold and nothing more. Most efforts are never closed, and that is a legitimate steady state."
>    - Its third sentence is replaced. The replacement makes no claim, in any wording, about how often efforts are closed: not that most are, not that most are not, and not that the proportion is unknown.
>    - In its place, it states that an effort whose frontier never empties is in a legitimate steady state rather than a stalled one, and is not to be treated as a defect.
>    - The first two sentences and the `_Avoid_` line, "done, finished, complete", are left exactly as they stand. *(90)*
> 5. **A new section.** The file gains one new section headed `## Starting an effort`, placed immediately before the existing section headed `## Closing an effort`. No other section moves. *(247)*
> 6. That section holds exactly two term entries and nothing else. Each is written in the same shape as the entries already in the file: a line holding only the headword in bold followed by a colon, then the definition, then a line beginning `_Avoid_:`. *(247)*
> 7. **Starting an effort.** The first entry's headword is `Starting an effort`. Its definition states all of the following:
>    - it is the act that creates an effort;
>    - the manager performs it, and it happens before the graph exists;
>    - it produces the effort's files and its first nodes;
>    - it has two inputs, a conversation with the human or a directory of work that already exists, and the input is the only thing the two ways of starting differ in. *(247)*
> 8. That entry's `_Avoid_` line refuses `charting`, `kickoff`, `onboarding`, `bootstrap`, `setup` and `init`. Against `charting` it gives a reason with both of these halves:
>    - this workflow's cartographic metaphor stops at the map, and every act beneath it is described plainly;
>    - the act the word names is what the file's existing `Expedition` entry says the workflow's ancestor does, "works out what the work is", rather than anything this workflow performs. *(247)*
> 9. **Adoption.** The second entry's headword is `Adoption`. Its definition states all of the following:
>    - it is starting an effort from a directory of work that already exists;
>    - it is a way of starting an effort, not a kind of node;
>    - it carries steps the other input does not, naming at least these five: taking the effort's name from the directory that already exists; resolving any reserved graph name the directory already uses for something else; deriving the map from the record the effort already wrote, rather than from a conversation; declaring the label vocabulary from the foreign label families; and minting the bulk import as `precondition` nodes. *(247)*
> 10. That entry's `_Avoid_` line refuses `migration`, `import`, `onboarding` and `port`. Against `migration` it gives the reason that the word names moving data rather than taking on an effort. Against `import` it gives the reason that importing is one step inside adoption rather than the act itself. *(247)*
> 11. No entry anywhere in the file gives a name to the way of starting whose input is a conversation. That way is referred to by its input, and never by a word of its own, in the new section and everywhere else in the file. *(247)*
> 12. The word `charting` appears in the file in exactly one place, the `_Avoid_` line of clause 8. No other form of the word *chart* appears anywhere in the file. *(247)*
> 13. **Nothing else changes.** Only these may change: the definition lines of **Code slot** (clause 1), the paragraph under `## The five kinds of node` (clause 2), the definition lines of **grilling** (clause 3) and the third sentence of **Closed** (clause 4). The only addition is the new section (clauses 5 to 12). Every other line is byte-identical to the file as it stood when the work was claimed. In particular:
>     - the `Expedition` entry is unchanged;
>     - no entry is removed and no `_Avoid_` line is removed or changed;
>     - no section other than the new one is added or moved.
>
>     *(90, 92 clause 3, 134, 247 clauses 1 and 8)*
> 14. The work leaves the tree meeting the bar. *(90, 92, 134, 247)*

*Carried by node 328. If the human takes C1(a) or C2(a) under node 328's `## Answer`, the manager amends this condition before filing it. C1(a) inserts the text given there and widens clause 13's list to include the Reject definition. C2(a) replaces clause 4's second bullet.*

INVALIDATIONS: none. No resolved node is contradicted. Open nodes whose conditions are stale or in conflict are listed in C1 to C8 of the answer.

RETROSPECTIVE

1. **What I had to hunt for.**
   - Which open implementation nodes change the glossary. I looped over every node's `Type:` and `Status:`, then grepped for `CONTEXT.md|glossary` and read every hit. About half the hits only mention the file.
   - Whether 81's Reject demand still holds. I found the reject steps in `map-manager-only.md`'s landing policy after first looking in `expedition/SKILL.md`, which only says "clean the working state after".
   - That no shipped contract says "worktree" (C3). A grep found it.
   - Whether 133, 255, 177, 112 and 123 are resolved. I read each node's `Status:` line one by one.
2. **What arrived that this node did not need.**
   - Most of `map.md`. Only two bullets bore on this node: "Nodes are grouped by file" and the paragraph about `CONTEXT.md` and node 56. Everything on retrospectives, worktrees, the landing policy and token priority did not.
   - The long flag and amendment histories on nodes 81 and 137. Each amendment restates its provenance at length, and I needed only the replacement bullets.
   - The git status in my spawn context, which was unused.
   - A list of node ids with their `Type:`, `Status:` and a "files it changes" field would have replaced most of my reading.
3. **What would have made this easier.**
   - A per-node "files changed" line in the node header, or a generated index of files per open node. Grouping by file is exactly the question it would answer.
   - Condition texts shown with their amendments applied. For every node I had to fold 2 to 4 amendment blocks into the original clauses by hand to learn what is currently demanded.
   - The spawn could have said that node 81 also touches the prototype contract, since the manager listed it among the glossary nodes.
4. **What was stale, wrong or contradictory.**
   - Node 56's manager note ("exactly **50**") and its clause 1 count, which the merge will move.
   - The moved-file path `.claude/skills/expedition/CONTEXT.md` in 81, 90 and 247, which is now `glossary.md`.
   - The never-delete clauses in 134, 120 and 124, which conflict with node 189's bound.
   - Node 134's second condition's quote of the kinds-of-node sentence, which predates node 302.
   - Node 61's premise, since a Scribe entry already exists.
   - Node 90 against the Destination entry (C2).
   - Node 111's `charting` against node 112 and node 247 (C4).
   - Node 137's clause 1 against node 106 (C6).
   - The gitStatus snapshot said HEAD was `c3ecda3`, but HEAD is `64db5aa`. `CONTEXT.md` did not change between them.

*The manager's note:* node 106 landed as `64db5aa` while this worker ran, so where it says 106 is "not in the main tree yet", 106's text is now the file's state, as it assumed.

## Flags

`328.1` **· settled** `ASSUMPTION` — I kept node 81 out of the merge because its entry 3 changes the prototype contract, which is node 329's file, even though the manager listed it with the glossary nodes. I offered the split as the recommended option (C1), with the clause text ready to insert. For the part of 81 that would go into the merge, I wrote that the Reject rewrite keeps "the node does not resolve" and "what is kept is the discovery", because 81 calls both sentences false without saying which half survives. No round took place. What I did: I read the node files, `CONTEXT.md`, the map, the glossary lines of `decisions.md`, `map-manager-only.md`'s landing section and the six contracts, and checked each quoted phrase against the file at `64db5aa`.

`328.2` **· settled** `ASSUMPTION` — Of node 134's grilling demand, I carried only the missing half: a dependent question is held for a later payload, as the grilling contract says. I judged the rest met by the current entry. I dropped its clause saying superseded text is marked and left in place, because the never-delete rule does not reach shipped files. I dropped the moved-file path in 90, 247 and 81, relying on node 56 landing last.

## Interview

### The manager's raise, 2026-09-26

*The manager's own raise:* "Do you approve replacing 90, 92, 134 and 247 with the merged node, taking the recommendations above for C1–C5 and C8, and my picks for C6 and C7? Or tell me which ones to change." The manager's picks, where the worker gave no recommendation: C6, amend 137 to quote node 106's six items; C7, supersede 61.

The human, `verbatim`: *"ok"* — taking the whole proposal as the manager put it.
