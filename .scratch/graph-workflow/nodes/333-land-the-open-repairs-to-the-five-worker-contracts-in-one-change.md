# Land the open repairs to the five worker contracts in one change

Type: implementation
Status: claimed
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
