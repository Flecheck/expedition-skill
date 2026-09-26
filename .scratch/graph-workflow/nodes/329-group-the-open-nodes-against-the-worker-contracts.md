# Group the open nodes against the worker contracts

Type: precondition
Status: resolved
Blocked by: none

## Question

Most open implementation nodes change a few lines of one file each, and their conditions forbid touching anything else, so two nodes on the same file cannot be worked together. The human asked for them to be grouped by file. Which open nodes change the five worker contracts `.claude/skills/expedition-{grilling,implementation,precondition,prototype,research}/SKILL.md` and the checker contract `.claude/skills/expedition-checker/SKILL.md`, and what merged node or nodes should replace them?

*Minted by the manager on the human's "You can do the groups", recorded in the map under `## Notes`.*

## What must be true when this is done

- Every open or unclaimed implementation node whose condition changes the five worker contracts `.claude/skills/expedition-{grilling,implementation,precondition,prototype,research}/SKILL.md` and the checker contract `.claude/skills/expedition-checker/SKILL.md` is listed, with the node number, its name and the part of the file it changes. A node that also changes files outside this group is listed and marked as crossing groups.
- For each proposed merged node: its name, the nodes it replaces, and an acceptance condition that carries each replaced node's demands with the node each came from. Where a replaced node's clause fences its own node ("no other entry changes"), the merged condition fences the union instead. Where a demand is already met by the file as it stands, or is stale, that is said and the demand is left out, with the reason.
- Every conflict is listed: between two replaced nodes' demands, or between a demand and the file as it stands. Each conflict says which nodes and which words, and offers the options. These go to the human.
- Nodes left out of any merge are listed, with the reason.

**Later nodes depend on:** the merged nodes' conditions, which the manager files as new nodes once the human approves the supersessions.

## Answer

Worker and checker contract nodes grouped. W merges 326, 155, 303, 60 and parts of 148, 43, 57; C merges 151, 173, 164. Eleven conflicts go to the human.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, and the human's decision under `## Interview`. On the human's "ok": W is [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md), with node 81's entry 3 and node 331 folded in; C is [node 334](334-land-the-open-repairs-to-the-checker-contract-in-one-change.md); R2 is [node 335](335-qualify-the-glossarys-research-entry-for-the-research-raise.md). R1 goes to the manager-contract merge of node 330. Nodes 72 and 279 are superseded by 143 and 311.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Group the open nodes against the worker contracts

ANSWER:
Searched at master `c3ecda3`. I read the Type and Status lines of every node file, grepped every open or claimed implementation node for the six contract paths and for the contracts' section names, and read each hit in full against the files on disk. Where a node has amendments, the latest one is the one I checked against.

**1. Open implementation nodes that change the six files**

Group: `.claude/skills/expedition-{grilling,implementation,precondition,prototype,research}/SKILL.md` and `.claude/skills/expedition-checker/SKILL.md`. X means the node also changes files outside this group.

| node | name | part of the file it changes | crosses? | disposition |
|---|---|---|---|---|
| 326 | Say who writes a condition in the five contracts' reporting sections | shared section `## When a node you report is an implementation node`, first sentence | no | merged into W |
| 155 | Carry the search-the-record instruction into the five worker contracts | `## What you read`, a new passage after the pointer list | no | merged into W |
| 303 | The worker contracts do not state the search-the-open-conditions duty | handover instructions. It has no condition; this node drafts one | no | merged into W |
| 60 | A worker reports what the map did not tell it | handover block, a new `MISSING FROM MAP:` part and the part counts | no | merged into W |
| 148 | Nothing stops the next acceptance condition being written with an absolute path | shared section, the bullet `A path may say where, because the checker has the repo` | X: one sentence in `graph-conventions.md` `### Acceptance condition` (trivially small) | contract part merged into W; the rest goes to remainder R1 |
| 43 | Widen the invalidation channel from contradiction to change | handover block, the `INVALIDATIONS:` line and prose near it | X: one sentence in `graph-conventions.md` (trivially small) | contract part merged into W; the rest goes to R1 |
| 57 | Give a research node the cannot-proceed raise | research contract: hard rule 3, a new raise, `## What you hand back` | X: one sentence of `CONTEXT.md`'s `research` entry (trivially small) | contract part merged into W; the rest goes to R2 |
| 151 | Write the checker contract's `## How you check` section | checker, a new section | no | merged into C |
| 173 | Stop the checker's spawn carrying the bar's commands | checker, the given `The bar:` and the count of the givens | no | merged into C |
| 164 | What a standards path may hold | checker, `## The standards you hold the work against` | no | the part still live goes into C (see conflict 2) |
| 109 | Carry node 94's extent rule into the seven shipped files | shared section: a fifth point, a residual clause, the read-back count | X: `graph-conventions.md` `### Acceptance condition` clauses 1–4 in full, and `expedition/SKILL.md` `## Acceptance conditions`. Not trivially small | not merged |
| 327 | A related defect joins an open node instead of becoming a new one | the new-nodes instructions in the five contracts | X: `expedition/SKILL.md` and `graph-conventions.md`, two substantive clauses | not merged |
| 41 | Ship the FRICTION flag and the self-edit disclosure duty | markers list and `FLAGS:` line in all five | X: `graph-conventions.md` clauses 1–6; also blocked by open node 56 | not merged |
| 61 | Collapse the manager's discipline onto the leading word `scribe` | words list, opening paragraph and handover paragraph in all five | X: `CONTEXT.md` | not merged (conflict 8) |
| 81 | Bring the glossary's code-slot and reject entries up to the worktree lifecycle | prototype `## Words used exactly`, the `code slot` line | X: `CONTEXT.md`, two entries; the glossary is its main part | not merged; optional split (option O4) |
| 137 | Rename the two reports and repair the `_Avoid_` line | precondition `## When the premise is broken`, its last sentence | X: `CONTEXT.md`, `expedition/SKILL.md`, `graph-conventions.md` | not merged |
| 279 | The five worker contracts route a scope raise to the human | shared section, its last paragraph | no | not merged (conflict 1) |
| 32 | Narrow the flags.md clause in the worker contracts | `## What you read`, the `flags.md` line in all five | no | not merged: no condition |
| 40 | Nothing carries a flag's account of what produced it out of a worker | the `FLAGS:` part and the shared flag section | maybe `graph-conventions.md` | not merged: no condition |
| 214 | A condition that cannot be honoured with a standard is a raise | implementation `## Flag, or raise`, and the checker's raise grounds | no | not merged: no condition |
| 72 | The checker is given the review route instead of finding it | checker, the standards section | no | not merged: no condition, and its premise is stale |
| 208, 209 | A condition quoting a refused word traps its worker; A byte-identity clause is discharged by diff | may land in the shared section; which file is not decided | unknown | not merged: no condition |

These mention the six files but are not in this group:
- **44** creates a new `.claude/skills/expedition-cascade/SKILL.md` and changes none of the six.
- **73** changes `graph-conventions.md` only, and its condition requires the six contract directories to stay unchanged.
- **134** and **56** change `CONTEXT.md` only (the glossary group). Node 134 names the six contracts only inside an enumerator.

**2. Facts on disk at `c3ecda3` that the merged conditions rest on**
- The sections `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical in all five worker contracts. The one difference is that the research file ends after the last section with no trailing blank line.
- All five `## What you read` sections open "Read each of the following. Do not trust any summary of them."
- All five carry "- `decisions.md` — the sections the spawn names" and "Leave `flags.md` unread. It is not yours."
- In the research file, "You may read outside the working directory." sits between the pointer list and the `flags.md` line.
- `grep -rln "self-contained" --include="*.md" .claude/ CONTEXT.md` returns 7 paths, as node 109 records.
- `grep -rlnE "against (those four|the four points above)" --include="*.md" .claude/` returns the 5 worker contracts.
- `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/` returns 0.
- `grep -rn "not that worker's to fix" .claude/` returns 0. Node 279's original quote is gone, and its amendment re-points it.
- `MISSING FROM MAP` and `FRICTION` occur nowhere under `.claude/`.
- The manager contract's `## The checker` already says the checker gets "The bar, as its properties. The spawn says nothing more about the bar." So node 173 brings the checker contract into line with the manager contract.

**3. Demands left out because they are already met or stale**
- **173 clause 6 is met.** The sentence already reads "The implementer works from the same file, so the two of you hold the work to one set of standards." C keeps that sentence unchanged instead.
- **164:**
  - Clause 1 is stale. It assumes a standards path handed to the checker, and since node 143 there is no such path: the checker reads one fixed file. It also conflicts with the file as it stands (conflict 2).
  - The first half of clause 2 is met ("Read only the standards in it, and open no other file in the effort's directory").
  - Clause 3's "the two routes by which they reach it" is stale, because there is one route.
  - Clauses 6 and 7 are carried by C's clause A11.
- **151 clause 4's "the standards the spawn gives the checker" is stale.** The file says "Nobody hands them to you. You read them yourself". C re-points it to the standards the checker reads from `map-implementation-rules.md` (conflict 3).
- **The bar restatements are dropped:** 148 clause 7 and 109 clause 9. The bar reaches the checker by its own route, and 148's version still counts the map's standing preferences, which nodes 169 and 184 struck.
- **155's `Read each of these` alternative is dropped as vacuous.** All five files now open with the other form.
- **148's alternative bullet form is dropped.** All five now use `A path may say where, because the checker has the repo`, so the `a **path** may say where` form is gone.

**4. Conflicts for the human** (options; recommendation first)
1. **279 against the manager contract and node 311.** 279 wants the five contracts to say the manager may extend a short scope at the raise, on a held node, with no human turn. The manager contract says the amendments by the fact-establishing party and by the manager "apply only to a node nobody holds yet", and that where a worker holds the node "the human answers". Nodes 82 and 311 fixed this. Separately, 279's clause 2 ("the five are not unified onto one sentence") contradicts the byte-identical shared section.
   - (a) Supersede 279 with no replacement. **Recommended.**
   - (b) Keep it, and change the manager contract too. That crosses into group 330.
2. **164 clause 1 against the checker file.** The file says the standards file "may itself hold record material, such as how the work lands, what the effort has decided, or links onward to the rest of the record". Clause 1 wants the file to state that a standards path holds the standards and not the record.
   - (a) Carry only the unmet half of clause 2 (the checker says in its outcome that it read only the standards) and clauses 4–5 into C. **Recommended; this is how C is written.**
   - (b) Supersede 164 entirely as met by nodes 143 and 295.
   - (c) Rewrite clause 1 for the fixed file. That needs a judgement nobody has made.
3. **151 clause 4's stale "the standards the spawn gives the checker".**
   - (a) Accept C's re-point to "the standards the checker reads for itself from `map-implementation-rules.md`". **Recommended.**
   - (b) Put the wording to the human.
4. **151 clause 5 against the file's `### FAIL`.** Clause 5 routes a standards breach to `FAIL: the bar`, while `### FAIL` says "an unmet bar sends it back for changes to the build". A prose-standard breach is not a build change.
   - (a) Leave that sentence fenced and unchanged. **Recommended.**
   - (b) Let C reword that one sentence.
5. **57 names only hard rule 3.** The research file also says "The manager spawned you and is waiting for one handover.", "A research node never involves the human." and "Hand back one handover with all five parts, every time." The raise makes all three false.
   - (a) Make fixing them a demand. **Recommended; this is W's clause H4, which no replaced node wrote.**
   - (b) Only permit it.
6. **303 had no condition, and its question ("which contracts, in what words") is open.**
   - (a) All five contracts. Use the manager contract's wording, and include the duty to write the replacement for an unclaimed node's clause, because a search duty with no stated use is incoherent. **Recommended; this is W's clause E.**
   - (b) The implementation contract only.
   - (c) The search duty without the replacement duty.
7. **Small other-file parts of 43, 148 and 57.**
   - (a) Split them off. The `graph-conventions.md` sentences go to remainder R1, for group 330's merged node. The `CONTEXT.md` sentence goes to R2, for group 328's. This keeps W off files the other two groups hold, so the three merged nodes can run in parallel. **Recommended.** Cost: a short window in which the glossary still says a research node "is worked without the human" while the research contract has a raise.
   - (b) Take them whole into W, using option O1–O3 below.
8. **61.** Its preamble is false in three ways:
   - The manager contract uses `scribe` about ten times.
   - `CONTEXT.md` now has a `Scribe` entry.
   - The research contract's opening never spelled the idea out.

   Its definition, "authors nothing of its own onto it", also contradicts the glossary's `Scribe` entry ("Anything of its own goes beside that text, as its own marked note") and the manager contract, where the manager writes the condition for a node it mints.
   - (a) Supersede 61 with no replacement. The idea sits at two short sites per file, so the saving is small. **Recommended.**
   - (b) Re-draft its definition by copying the glossary's `Scribe` entry and add it to W.
   - (c) Keep it as it is.
9. **109 crosses groups with a substantial other-file part.**
   - (a) Keep it whole and run it after W. **Recommended.** W changes neither its enumerator returns nor the counts it corrects.
   - (b) Split it: clause 6 goes to W, clauses 1–5 to group 330.
10. **327 crosses groups.** Its clause 1 (workers propose an amendment to a related open node) contradicts the manager contract as it stands until its clauses 2–3 land. The manager contract says an amendment cannot carry "A new demand, at any place" and that "A defect the condition does not describe. That takes a new node, whatever file the defect is in."
    - (a) Keep 327 whole, as its own node or in group 330's merge. **Recommended.**
    - (b) Split it. That opens a window where the worker and manager contracts disagree.
11. **81 and 137.** 81's prototype part is one line and is independent. 137's precondition sentence needs the term "node closing report", which only 137's glossary part defines.
    - For 81: (a) split its entry 3 into W with option O4 (**recommended**), or (b) leave 81 whole in group 328.
    - For 137: keep it whole, outside W. **Recommended.**

**5. Nodes left out of any merge, and why**
- **Crossing groups:** 109, 327, 41 (also blocked by open node 56), 81, 137.
- **Conflicts:** 279 and 61.
- **No acceptance condition:**
  - 32: open fork between a pointer the spawn names and the worker's own judgement.
  - 40: form undecided. The shared flag section already says where the account lives when there is no round.
  - 214: map `## Notes` names it as the carrier of the raise rule, but nobody has written its condition.
  - 72: premise stale. The checker is no longer told to find its standards; it reads `map-implementation-rules.md` and runs a reviewing skill "only where the standards name one". Recommend superseding it as done by node 143.
  - 208 and 209: target file undecided.

  Any of these can join W or C through node 327's related-defect route once it has a condition.
- **Sequencing, not edges:** W's fence and C's fence mean 109, 327, 41, 61, 81 and 137 cannot run beside W. 214 cannot run beside W or C.

**6. A record fact the manager needs when W lands**
The map's retrospective bullet counts the retrospective as the "sixth" part on four kinds and the "seventh" on implementation. W adds `MISSING FROM MAP:`, and may add a search part under clause E3. After that, those counts in `map.md` are wrong.

INDEX LINE:    Worker and checker contract nodes grouped. W merges 326, 155, 303, 60 and parts of 148, 43, 57; C merges 151, 173, 164. Eleven conflicts go to the human.

FLAGS:
ASSUMPTION — The checker contract gets its own merged node (C) instead of sharing W. Nodes 155 (clause 5), 43 (clause 5), 41 (clause 8) and 57 (clause 4) each require the checker to stay unchanged, and the checker has a different reader. What I did: grouped the three checker nodes separately and fenced the checker out of W.
Index: The checker contract's open nodes were merged into a node of their own, because four worker-contract conditions require the checker to stay unchanged.

ASSUMPTION — W's condition has four clauses that no replaced node wrote. A1 says the two shared sections stay identical (the manager's note, and node 50). E is 303's condition in full, since 303 had none. G7 says the part counts must match. H4 makes the research contract's opening and handover section true once it has a raise. Each is marked "(node 329)" in the condition so the human can strike it.
Index: Node 329 added four clauses of its own to the merged worker-contract condition, each marked, including all of node 303's missing condition.

ASSUMPTION — I re-pointed stale quotes to the current text where the file fixes the wording: 151 clause 4, and the single form now used by 148 and 155. I dropped the bar restatements in 109 and 148 because the bar reaches the checker by its own route.
Index: Stale quotes in the merged conditions were re-pointed to the text on disk at c3ecda3, and bar restatements were dropped.

NEW NODES:

--- W ---
Name: Land the open repairs to the five worker contracts in one change
Kind: implementation
Replaces: 326, 155, 303, 60, and the worker-contract parts of 148, 43 and 57. If the human takes option 7(a), their other-file parts become R1 and R2 below. With option O4, it also replaces 81's entry 3.
Question: Open nodes 326, 155, 303 and 60, and the worker-contract parts of 148, 43 and 57, each change a few lines of the five worker contracts and each forbids any other change, so none can run beside another. Make all of their changes in one node.
Blockers: none. Its sources' blockers are resolved: 290–294 for 303, and none for the others.
Acceptance condition:

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
I1. *(the union of the fences of 326, 155, 148, 43, 57 and 60)* No text in the five files is deleted, shortened or reworded except where clauses B to H demand it. No hard rule is reworded except the research file's hard rule 3 (H2). No heading, bullet, hard rule or clause is renumbered. Text may be added only where clauses B to H demand it.
I2. No file other than the five changes. In particular `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md` and `CONTEXT.md` are unchanged, and no file under `.scratch/` changes.
I3. The working tree meets the bar.

*Option O1–O3, used only if the human takes 7(b):* add R1's clauses R1.1–R1.2 and R2's clause R2.1 below to W. In I2, remove `graph-conventions.md` and `CONTEXT.md` from the unchanged list, and add "In `graph-conventions.md` only the two sentences R1.1–R1.2 name change; in `CONTEXT.md` only the `research` entry's sentence R2.1 names changes."
*Option O4, used only if the human takes 11 (split 81):* add this clause *(node 81, entry 3)*. In the prototype file's `## Words used exactly`, the line "- **code slot** — the right to modify product code, held by one worker at a time. It is never yours." no longer says "held by one worker at a time". It says that one worker holds one slot, and that how many slots an effort runs is that effort's own setting. It keeps "It is never yours." and stays a single line in that list's form. Hard rule 1's sentence "You do not hold the code slot." is unchanged.

--- C ---
Name: Land the open repairs to the checker contract in one change
Kind: implementation
Replaces: 151, 173, 164
Question: Open nodes 151, 173 and 164 each change `.claude/skills/expedition-checker/SKILL.md` and each forbids other changes to it. Make all their live changes in one node.
Blockers: none (node 143, which 151 and 164 waited on, is resolved).
Acceptance condition:

The work is `.claude/skills/expedition-checker/SKILL.md`, path relative to the repository root. The worker may edit that file and no other, and writes no file under `.scratch/`. Done means every one of the following is true of the finished tree.

**A. A method section** *(node 151)*
A1. The file contains a section headed exactly `## How you check`, placed after the section headed `## Hard rules` and before the section headed `## What you hand back`.
A2. That section's body, from its heading to the next line beginning `## `, is at most 2,000 bytes.
A3. It states that the checker splits the acceptance condition into its parts before it reads the work, because its `PASS` owes one line per part.
A4. It states that three things are kept separate and are never merged with or ranked against one another: the acceptance condition, the bar, and the standards the checker reads for itself from `map-implementation-rules.md`. Passing on one of the three never excuses or masks failing on another.
A5. It states that the standards report under the bar, so work that breaches a standard is `FAIL: the bar` and never `FAIL: acceptance condition`.
A6. It states that the checker establishes each part of the condition by a search it can name, and hands that search back, rather than by reading the work through.
A7. It states that the checker says plainly what it did not check.
A8. It states that an effort's own rules may add method specific to that effort on top of this section, and that this section's demands still hold where they do.
A9. The section contains no instruction to search for, look for, discover or otherwise go and find the standards the checker holds work against.
A10. Where the section refers to a shape the file defines elsewhere, it uses the file's own name for it (`PASS`, `FAIL: acceptance condition`, `FAIL: the bar`, `NOT COVERED`) and defines no second version of any of them.
A11. Nothing added to the file names a skill or a plugin, requires anything to be invocable, or assumes a particular repository, machine or toolchain.

**B. The bar's commands** *(node 173)*
B1. The file nowhere states or implies that the checker's spawn may carry the bar's commands. The item in the list of givens that begins `The bar:` today reads "The bar: either its commands for this repo, or the properties alone." and contains "Where you are given the properties and no commands, discover the commands from the repo." After the work it offers no choice between being given commands and being given the properties, and the file holds no sentence conditioned on the checker having been given properties and no commands.
B2. That item states the bar's properties in full: the work builds, it warns about nothing, it is formatted, the tests relevant to it pass, and whatever else the repo itself demands is satisfied. It also states that the checker discovers the commands from the repo itself.
B3. The item says that a repo which states its own commands to an agent typically states them in its own agent-instruction file. That file is named by role and position only, and no particular filename for it appears anywhere in the finished file.
B4. The item keeps its statement that a repo with no build, no tests and no formatter meets the bar on its remaining half, which is "the complete bar for such a repo".
B5. The sentence introducing the givens today reads "You are given six things. The spawn carries the first five, and you read the sixth for yourself from one file this contract names." After the work, the count it states is arithmetically correct for the items the list holds, and it splits them correctly between those that arrive in the spawn and those the checker reads for itself.
B6. The sentence "The implementer works from the same file, so the two of you hold the work to one set of standards." is unchanged. No other sentence claims that the checker and the implementer take the bar's commands from the same place.

**C. Record material in the standards file** *(node 164)*
C1. Under `## The standards you hold the work against`, the file keeps its statement "The file is in the same directory as the record you are blind to, and it may itself hold record material, such as how the work lands, what the effort has decided, or links onward to the rest of the record. Read only the standards in it, and open no other file in the effort's directory." It also states, under the same heading, that the checker says in its outcome that it read only the standards in that file.
C2. The statement beginning "A ground rule is a standing constraint on the effort that is true of any node's work" is unchanged in what it requires.
C3. The statement "Leave the record unread, and do not go looking for it.", with its one exception for `map-implementation-rules.md`, is unchanged in what it requires.

**D. What else may change** *(the union of the fences of 151, 173 and 164)*
D1. Nothing outside the following is deleted or reworded: the new `## How you check` section; the given-list item beginning `The bar:`; the sentence introducing the givens; the sentence C1 adds; and any one sentence elsewhere stating A5's routing, which may be removed as a duplicate of the new section.
D2. No other file is modified.
D3. The working tree meets the bar.

--- R1 (only under option 7(a); for group 330's merged node to absorb, or to file alone) ---
Name: Carry the path-form and widened-INVALIDATIONS rules into graph-conventions
Kind: implementation
Replaces: the `graph-conventions.md` parts of 148 and 43
Question: Nodes 148 and 43 each change one sentence of `.claude/skills/expedition/graph-conventions.md`'s `### Acceptance condition`. Their worker-contract parts went to W.
Blockers: none
Acceptance condition:
The work is `.claude/skills/expedition/graph-conventions.md`, path relative to the repository root.
R1.1 *(node 148)* The sentence beginning "A path may say where:" states that such a path is written relative to the repository root, and states the reason: an absolute path names a machine, and the worker and the checker that read the condition may not be on it. The addition is at most two sentences. `grep -rn -oE '/(home|Users)/[A-Za-z0-9_.-]+/' .claude/skills/` returns nothing after the work.
R1.2 *(node 43)* The sentence "Such a demand goes in the handover's `INVALIDATIONS` part, which names which resolved node the work contradicts and how." is reworded so the part covers any resolved node whose answer the work changes what it says. It names a rename, an extension, a narrowing and a contradiction. "A demand about the record as a whole belongs on the handover and in no condition, whatever its wording." is unchanged.
R1.3 Nothing else in the file changes, and no other file changes. The working tree meets the bar.

--- R2 (only under option 7(a); for group 328's merged node to absorb, or to file alone) ---
Name: Qualify the glossary's research entry for the research raise
Kind: implementation
Replaces: the `CONTEXT.md` part of 57
Question: Once the research contract has a raise, the glossary's `research` entry is false where it says the node is worked without the human.
Blockers: none. Best landed with or after W.
Acceptance condition:
R2.1 *(node 57)* In `CONTEXT.md` at the repository root, the `research` entry no longer says without qualification that a research node is worked without the human, which it states today as "It is worked without the human." It says a research node's ordinary work is done without the human, and that its worker may raise where the node's premise is broken. The entry has no `_Avoid_` line, and gains none.
R2.2 No other entry is edited, and no other file changes. The working tree meets the bar.

INVALIDATIONS: none. Separately, node 279's demand contradicts resolved nodes 82 and 311 as the manager contract carries them (conflict 1). And once W lands, the map's "sixth"/"seventh" retrospective part counts are wrong (ANSWER section 6).

RETROSPECTIVE
1. What I had to hunt for:
   - Which open implementation nodes touch the six files. No index maps nodes to files, so I scanned every node file's Type and Status lines and grepped for paths and section names. Six nodes name the contracts only as "the five contracts" and had no path to find them by.
   - Which sections count as shared. I diffed the contracts; node 290's condition names them.
   - Whether node 279's route still exists. Found in the manager contract's `### Changing one after it is written` and in decisions lines 74, 159 and 193.
   - Whether 57's "cannot-proceed raise" is precondition's `## When the premise is broken`. Found in node 23's first line.
2. What arrived that this node did not need:
   - Most of `map.md`. I used only the grouping bullet, the retrospective bullet and the never-delete bullet; the rest, about 28 KB, bore on nothing.
   - In `decisions.md` I used about 8 of 208 lines, found by grep.
   - The amendment histories on 109, 148 and 155, each of five near-identical blocks. Only the last block mattered. A "current effective text" line per condition would have spared reading the rest.
3. What would have made this easier:
   - A file-to-node index in the record, or a `Touches:` header line on each implementation node.
   - A spawn listing the candidate node numbers, found by the same grep I ran.
   - For amended conditions, the manager filing the consolidated current condition beside the amendment log.
4. What was stale, wrong or contradictory:
   - 279: its ground contradicts the manager contract and node 311, and its clause 2 contradicts the shared sections.
   - 164: clauses 1 and 3 assume a handed path that no longer exists.
   - 151 clause 4: "standards the spawn gives" is stale.
   - 61: its preamble is false and its definition contradicts the glossary.
   - 72: its premise is stale.
   - 148 clause 7 and 109 clause 9 restate an outdated bar.
   - 40's premise is partly overtaken by the shared flag section.
   - 173 clause 6 is already met.
   - The map's retrospective part counts will go stale when W lands.

## Flags

`329.1` **· settled** `ASSUMPTION` — The checker contract gets its own merged node (C) instead of sharing W. Nodes 155 (clause 5), 43 (clause 5), 41 (clause 8) and 57 (clause 4) each require the checker to stay unchanged, and the checker has a different reader. What I did: grouped the three checker nodes separately and fenced the checker out of W.

`329.2` **· settled** `ASSUMPTION` — W's condition has four clauses that no replaced node wrote. A1 says the two shared sections stay identical (the manager's note, and node 50). E is 303's condition in full, since 303 had none. G7 says the part counts must match. H4 makes the research contract's opening and handover section true once it has a raise. Each is marked "(node 329)" in the condition so the human can strike it.

`329.3` **· settled** `ASSUMPTION` — I re-pointed stale quotes to the current text where the file fixes the wording: 151 clause 4, and the single form now used by 148 and 155. I dropped the bar restatements in 109 and 148 because the bar reaches the checker by its own route.

## Interview

### The manager's raise, 2026-09-26

*The manager's own raise, sent after node 328's decision:* whether to file the merged nodes W and C, superseding the nodes they replace, taking the worker's recommended option on each of its eleven conflicts, superseding node 72 as done by node 143 as the worker recommends, and folding [node 331](331-give-each-question-in-a-multi-question-payload-a-context-line.md) (the `CONTEXT` line from node 259) into W, which is the manager's own proposal.

The human, `verbatim`: *"ok"* — taking the whole proposal as the manager put it.
