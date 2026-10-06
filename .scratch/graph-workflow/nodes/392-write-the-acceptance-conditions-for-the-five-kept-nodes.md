# Write the acceptance conditions for the five nodes kept at the 2026-10-06 triage

Type: precondition
Status: resolved
Blocked by: none

## Answer

Acceptance conditions written for nodes 40, 185, 214 and 317, plus node 41's amendment adding `PERMISSION` and relocating its clause 5 to SKILL.md, all checked against the files on 2026-10-06.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced no node. Its conditions and node 41's amendment are filed on those nodes, with each one's opening sentence at the head of its question. Flags 392.1, 392.2, 392.3 settle at the node closing report.

## Question

Workers can start nodes 40, 41, 185, 214 and 317 once each has an acceptance condition that holds against the current shipped files. The triage the human invoked on 2026-10-06 kept these five nodes. Four of them now carry the human's decision under their `## Interview`, and node 41 carries node 170's merged question. None has a condition it can be started on: 40, 185, 214 and 317 have none, and node 41 needs an amendment clause for the `PERMISSION` marker.

*Minted by the manager after the triage. The manager may not author a condition for a node an agent minted, and these five were minted by agents or by the human's direction.*

## What must be true when it is done

*Written by the manager, and marked as the manager's.*

- For each of nodes 40, 185, 214 and 317, the handover carries an acceptance condition the manager can file under that node's `## Acceptance condition` unchanged. For node 41, it carries the amendment clause or clauses to file under a new `## Amendment` on that node.
- Each condition carries out the human's recorded decision on its node, and holds against the current shipped files.
- Node 40 has no human decision. Its condition states the property the triage found missing: the full account of a flag, which `graph-conventions.md`'s `### Raise a flag` places in the round that raised it, has a route from the worker to where it is filed, or that requirement is reconciled with `### ## Review`'s closed list of entries. It leaves the form open, so the implementing worker raises a genuine fork.
- **What later nodes depend on:** all five nodes are blocked by this one, and each starts once its condition is filed.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Write the acceptance conditions for the five nodes kept at the 2026-10-06 triage

ANSWER:

Conditions and amendments for nodes 40, 41, 185, 214 and 317, written against the shipped files as they stand on 2026-10-06 (master at `b8068ebdf`). Each subsection can be filed as written. Each one opens with a sentence the manager can file at the head of that node's `## Question`, saying what the work makes possible and for whom. No file in the repo was written.

Facts these conditions rest on, each checked against the files on 2026-10-06:

- `.claude/skills/expedition/graph-conventions.md`, under `### Raise a flag`, now reads "Where a node has no round at all, as with an AFK `precondition` node, the `## Flags` entry carries that account itself." Node 40's question still quotes the older "a `research` node, an AFK `precondition` node" and still says "five contracts". There are four worker contracts: grilling, prototype, precondition and implementation.
- The description of `## Review` under `## The node file` in graph-conventions.md lists three kinds of entry "and nothing else". None of the three is a flag's account.
- The four worker contracts have byte-identical sections in three places, checked by md5:
  - `## When you raise a flag`
  - `## When a node you report is an implementation node`
  - the paragraph beginning "Read everything the list above names in full."
- Each of the four contracts' `## What you read` lists "`decisions.md` — the sections the spawn names". `grep -rn "sections the spawn names" .claude/` finds that phrase in those four files and nowhere else.
- Node 214's 2026-10-04 replacement clause 2 matches the checker contract's text exactly. That covers the sentence "Three kinds of question reach the human this way, and none of them stops your check.", the paragraph beginning "The third is a false flag", and the paragraph beginning "Hand each question back under your outcome". Clause 1's table is under `### When what you check against is itself the problem`.
- Node 41's clause 7, as amended 2026-10-05, names four files and is current. graph-conventions.md's marker list reads "There are three markers:", followed by `ASSUMPTION`, `CONDITION-WRONG` and `DELEGATED`.
- Node 41's clause 5 overlaps text already shipped in `.claude/skills/expedition/SKILL.md` under `### Two things that travel in a spawn and are not yours`, which says: "A direction from the human, carried in their words and marked as theirs. Where the thing blocking a node is not owned by the effort's own repository, such a direction is the only way the node can proceed."
  - Node 312 (commit `e64b3de`) split the rules between the two files. In its decisions line: "file format and procedures there, manager choices here". So graph-conventions.md keeps rules about the graph's files, and SKILL.md keeps rules about the manager's choices.
  - Writing rule 6 in map.md tells a shipped file to point at a sibling's heading rather than restate it.
  - Clause 5 as written would therefore restate SKILL.md text in graph-conventions.md. Its replacement is below.
- Node 41's clauses 4 and 6 also ask graph-conventions.md to state what are manager choices under node 312's split. Unlike clause 5, they restate no shipped text, so they break no written standard and are not amended here. See flag 392.1.
- SKILL.md `## Flags` reads "Flags reach the effort closing report in one case only: a flag whose node closing report the human never answered, because they never spoke again." `## Closing an effort` lists "Every outstanding flag, taken from the unchecked lines of the effort's index of flags and never reconstructed by you." The glossary's `**Flag**:` entry, in `.claude/skills/expedition/glossary.md`, names no case of a flag reaching the effort closing report.
- One observation, not acted on. The glossary's `**Flag**:` entry, and graph-conventions.md's description of `flags.md`, call a flag "a judgement that an agent made on its own". A `PERMISSION` flag records a grant the human made, so that wording will fit it as badly as it already fits `CONDITION-WRONG`. Changing it is not part of the human's decision ("One list grows by one entry, and nothing else moves"), so no clause asks for it.

### Node 40: acceptance condition

**Opening sentence for the question:** This work lets the human see what the worker actually did, in the worker's own words, when they come back to a flag on a node that had an interview or a review. It does this by giving that account a route from the worker to the place where it is filed.

**Acceptance condition**

Done when all of the following hold. In this condition, a *round* is an `## Interview` attempt or a round in `## Review` on a node file. A flag's *account* is the full account of what produced the flag. For a flag from a worker's own unprompted judgement, the account is what the worker actually did, told in the worker's words.

1. `.claude/skills/expedition/graph-conventions.md` states, for every node, which section of the node file holds a flag's account. Before this work, that statement is this paragraph under `### Raise a flag`: "The round that raised the flag, an `## Interview` attempt or a round in `## Review`, says what produced it. For a flag from a worker's own unprompted judgement, what produced it is what the worker actually did, told in the worker's words. A one-line summary is enough under `## Flags`. The round needs the full account. Where a node has no round at all, as with an AFK `precondition` node, the `## Flags` entry carries that account itself." The work may change where the statement places the account. After the work, the statement still places the account in some section of the node file, on every kind of node.
2. Every section that clause 1's statement names as holding the account admits it in graph-conventions.md's own description of that section, under `## The node file`. Where the statement names `## Review`, that section's description lists the account among the kinds of entry it holds. Before this work, that description lists three kinds of entry "and nothing else": a checker run, a correction round, and the gate's outcome. Where the statement names `## Interview`, that section's description lists the account among what an attempt's block holds.
3. Each of these four files states in which part of which of its hand-back shapes its worker hands back the account, for every section where clause 1's statement places the account on that worker's kind of node:
   - `.claude/skills/expedition-grilling/SKILL.md`
   - `.claude/skills/expedition-prototype/SKILL.md`
   - `.claude/skills/expedition-precondition/SKILL.md`
   - `.claude/skills/expedition-implementation/SKILL.md`
4. The account may travel inside a part whose other text is filed under a different section of the node file. An example is the `FLAGS` part, whose prose is filed under `## Flags`. In that case, `.claude/skills/expedition/SKILL.md` or `.claude/skills/expedition/graph-conventions.md` states that the account is filed under the section clause 1's statement names.
5. Where each of the four files in clause 3 states where the account is held, that statement agrees with clause 1's statement. Before this work, the four files' statement is this paragraph of `## When you raise a flag`: "The round that created the flag, an `## Interview` attempt or a `## Review` round, holds the account of what produced the flag. If your node holds no round at all, meaning no exchange with the human and no gate, your `## Flags` entry holds that account instead: what you actually did, in your words."
6. The sections headed `## When you raise a flag` and `## When a node you report is an implementation node` are byte-identical across the four files of clause 3 before this work, and are byte-identical across them after it.
7. This condition fixes no form. Any of the following meets it, provided clauses 1 to 6 hold:
   - the account travels as a new part of a hand-back shape;
   - the account travels as a further element of an existing part, such as `FLAGS`;
   - the account travels inside text a shape already carries, such as a question's `SO FAR` or a correction round's report of what changed;
   - clause 1's statement moves the account to a section that an existing route already reaches.
8. The working tree meets the bar.

Scope: the scope came from no search, because the named places are the work rather than instances of a defect.

### Node 41: amendment, to file under a new `## Amendment` on the node

*Written by node 392's worker. The words are fixed by four sources:*
- *the condition's own clauses 1 and 5, written by node 19's worker;*
- *the human's 2026-10-06 answer on this node, which takes the recommendation to "add `PERMISSION` as a marker beside `FRICTION`, defined in one line: \"a permission the human granted for one attempt, past a contract clause that blocked the node\". It's settled like any flag. One list grows by one entry, and nothing else moves.";*
- *node 312's landed split (commit `e64b3de`): rules about the graph's files go in graph-conventions.md, and rules about the manager's choices go in SKILL.md;*
- *the shipped text of `.claude/skills/expedition/SKILL.md` under `### Two things that travel in a spawn and are not yours`.*

**Opening sentence for the question:** This work lets an agent on any effort record a defect it noticed in the expedition workflow itself. It also lets the manager record a permission the human granted past a blocking contract clause. Each gets a flag marker that says what it is.

- **A replacement for clause 1.** Read clause 1 as: "1. `.claude/skills/expedition/graph-conventions.md`, where it lists the markers a node's `## Flags` entry may carry, lists two markers alongside `ASSUMPTION`, `CONDITION-WRONG` and `DELEGATED`, and states that the list holds five markers. One is named `FRICTION`, and its stated meaning is: a defect the agent noticed in the expedition workflow itself while using it, rather than a judgement about the work in front of it. The other is named `PERMISSION`, and its stated meaning is: a permission the human granted for one attempt, past a contract clause that blocked the node."
- **A replacement for clause 5.** Read clause 5 as: "5. `.claude/skills/expedition/SKILL.md`, under `### Two things that travel in a spawn and are not yours`, states three things: that where friction blocks a node, the way past it is an instruction from the human carried into the spawn as their own words; that where the same instruction is needed more than once, it is written into that effort's ground rules in `map.md`'s `## Notes`; and that the manager may not invent such an instruction on its own authority. Text already under that heading counts toward any of the three. `.claude/skills/expedition/graph-conventions.md` gains none of the three statements."
- **An added clause.** "11. `PERMISSION` is added to the marker list named in clause 1, and to no other file's list of markers. No sentence about how a `PERMISSION` flag settles is added anywhere. It settles under the same rules as every other flag."
- Scope of the three clauses: the scope came from no search, because the named places are the work rather than instances of a defect.

### Node 185: acceptance condition

**Opening sentence for the question:** This work lets every worker find the decisions that bear on its node without reading the whole index of decisions. It works on any effort, with or without a label vocabulary.

**Acceptance condition**

Done when all of the following hold.

1. Each of the following four files, under `## What you read`, no longer lists `decisions.md` among the things read in full:
   - `.claude/skills/expedition-grilling/SKILL.md`
   - `.claude/skills/expedition-prototype/SKILL.md`
   - `.claude/skills/expedition-precondition/SKILL.md`
   - `.claude/skills/expedition-implementation/SKILL.md`

   Before this work, each file lists it as "`decisions.md` — the sections the spawn names".
2. Each of those four files, under `## What you read`, states the following: the worker searches `decisions.md` for its node's terms and paths, and for any node numbers the spawn names; and the worker reads only the lines that match.
3. The text that states clause 2's search is byte-identical across the four files.
4. The paragraph beginning "Read everything the list above names in full." is byte-identical across the four files after this work, as it is before.
5. `.claude/skills/expedition/SKILL.md`, under `## Spawning a worker`, states that a spawn may name the node numbers whose lines in the effort's index of decisions the manager already knows bear on the node. It does not present that index as something the worker reads in full. This condition demands nothing of that section's sentence "Where the effort has a label vocabulary, scope that index by label.": it may stay, change or go.
6. The phrase "the sections the spawn names" appears in no file under `.claude/`.
7. The working tree meets the bar.

Scope: on 2026-10-06, `grep -rn "sections the spawn names" .claude/` was run over the working tree. It returned one line in each of the four files of clause 1, each the list item "`decisions.md` — the sections the spawn names" under `## What you read`, and nothing else. `.claude/skills/expedition/SKILL.md` is named because it is part of the work, not because the search found it. Any instance the search reaches outside these five files is reported and not edited.

### Node 214: acceptance condition

**Opening sentence for the question:** This work lets the human hear before the work is finished, by way of a raise, when an implementation worker's acceptance condition cannot be honoured together with another clause or with a standard. Without it, the human meets the collision at the gate.

**Acceptance condition**

Done when all of the following hold.

1. `.claude/skills/expedition-implementation/SKILL.md`, in the section `## The acceptance condition`, tells the worker what to do in this case: where a clause of its acceptance condition cannot hold together with another clause of the condition, or with a standard its work is held against, its premise is broken, and it raises under trigger 1 of `## Flag, or raise` before it finishes the work. This sentence meets the clause word for word: "When a clause of your condition cannot hold together with another clause or with a standard you are held against, your premise is broken: raise under trigger 1 before you finish." Other wording meets it where it states every element of that sentence.
2. In `.claude/skills/expedition-checker/SKILL.md`, the table under `### When what you check against is itself the problem` gains one row, word for word. Its first cell is "two parts of the condition cannot both hold on one reading of them, and every part holds on another". Its second cell is "your outcome under the reading on which every part holds, and a question". The table's other rows keep their words, though the work for the rest of this node's condition may change them.
3. In the same file, under `### Questions, alongside a \`PASS\` or a \`FAIL\``, the sentence "Three kinds of question reach the human this way, and none of them stops your check." becomes "Four kinds of question reach the human this way, and none of them stops your check." One paragraph is added after the paragraph that begins "The third is a false flag" and before the paragraph that begins "Hand each question back under your outcome". The paragraph is, word for word: "The fourth is two parts of the condition that cannot both hold on one reading of their words, where every part holds on another reading. Check the work under the reading on which every part holds. Taking that reading is not a repair of the condition. In the question, name the reading you took, the reading you set aside, and each part the work would fail under the reading you set aside. Where no reading lets every part hold, the condition is self-contradicting, so raise."
4. No other sentence of `.claude/skills/expedition-checker/SKILL.md` changes to carry clauses 2 and 3, and no heading of the file is renamed.
5. Apart from the row clause 2 adds and the sentence and paragraph clause 3 changes and adds, `.claude/skills/expedition-checker/SKILL.md` is unchanged by this work. In particular, the section `### raise — nothing left to check against` keeps its words.
6. The working tree meets the bar.

Scope: the scope came from no search, because the named places are the work rather than instances of a defect.

### Node 317: acceptance condition

**Opening sentence for the question:** This work lets the human see every flag still outstanding when an effort closes. It also lets the manager build the effort closing report from one rule about flags, instead of two that disagree.

**Acceptance condition**

Done when all of the following hold.

1. `.claude/skills/expedition/SKILL.md`, under `## Flags`, no longer holds the sentence "Flags reach the effort closing report in one case only: a flag whose node closing report the human never answered, because they never spoke again." In its place, the section states that every outstanding flag reaches the effort closing report. It may say this in its own words, or by naming the bullet under `## Closing an effort` that lists what that report carries.
2. The bullet under `## Closing an effort` in the same file, "Every outstanding flag, taken from the unchecked lines of the effort's index of flags and never reconstructed by you.", keeps its words.
3. No sentence of any file under `.claude/` says that flags reach the effort closing report in one case only, or in any set of cases narrower than every outstanding flag. This includes the `**Flag**:` entry of `.claude/skills/expedition/glossary.md`.
4. The working tree meets the bar.

Scope: on 2026-10-06, `grep -rn -i "closing report" .claude/ | grep -i flag` was run over the working tree. It returned these places:
- `.claude/skills/expedition/SKILL.md`, four lines under `## Flags` ("node's flags settle at its node closing report too", "The node closing report awaits no answer", "Flags reach the effort closing report in one case only", and "A node closing report for a node holding flags carries every one of those flags");
- `.claude/skills/expedition-standing-yes/SKILL.md`, its heading `## Flags, and the node closing report`;
- `.claude/skills/expedition-cleanup/SKILL.md`, "The effort closing report is built from its lines";
- `.claude/skills/expedition-precondition/SKILL.md`, "The flag settles at the node closing report".

Only the "one case only" sentence states a case narrower than every outstanding flag. Any instance the search reaches outside `.claude/skills/expedition/SKILL.md` that does so is reported and not edited.

### Read-back against the five points

Each condition and amendment clause above was checked against the five points:
- every path is relative to the repo root;
- no demand points at a node, an interview or a human choice;
- every quoted passage is copied in;
- no demand is about the record as a whole;
- each states exactly one of the three scope forms. Node 185's enumerator and node 317's enumerator ran over the working tree. The other conditions came from no search.

INDEX LINE:    Acceptance conditions written for nodes 40, 185, 214 and 317, plus node 41's amendment adding `PERMISSION` and relocating its clause 5 to SKILL.md, all checked against the files on 2026-10-06.

FLAGS:

- ASSUMPTION (392.1) — *Prose for the node:* Node 41's clause 5 asked graph-conventions.md to state that a human's instruction carried into a spawn is the way past blocking friction. SKILL.md's `### Two things that travel in a spawn and are not yours` already says most of this. Node 312's landed split puts the manager's choices in SKILL.md, and writing rule 6 forbids restating a sibling's text. So I wrote a replacement clause 5 that places the statement under that SKILL.md heading, and gives graph-conventions.md none of it. Clauses 4 and 6 also describe manager choices, which node 312's split would put in SKILL.md. They restate no shipped text, though, so no written standard is broken and I left them as they are. If the manager prefers, clause 5 can be left as written too, at the risk that the implementing worker meets the restating rule and raises. *Index sentence:* Node 41's clause 5 was relocated from graph-conventions.md to SKILL.md's spawn section, where its text mostly already stands; clauses 4 and 6 were left in graph-conventions.md.
- ASSUMPTION (392.2) — *Prose for the node:* Node 214's condition accepts the human-approved sentence word for word, or any wording that states each of its elements. It does not demand the exact words, because a checker holding the exact sentence against writing rule 5 could fail work the worker was not free to reword. Node 208's case, where a condition quotes a word the glossary refuses, gets no separate clause. It falls under the general sentence wherever the glossary's refusals are among the standards the work is held against, as they are on this effort. *Index sentence:* Node 214's condition accepts the approved sentence or any equivalent wording, and covers node 208's refused-word case through the general rule rather than a clause of its own.
- ASSUMPTION (392.3) — *Prose for the node:* The human's decision on node 185 does not say whether the manager contract keeps "Where the effort has a label vocabulary, scope that index by label." So the condition says it demands nothing of that sentence, and the implementing worker decides. *Index sentence:* Node 185's condition leaves open whether the manager contract keeps scoping the decisions index by label.

NEW NODES:     none

INVALIDATIONS: none. No file in the tree changed.

CONDITIONS:

- **What I searched.** Every open node's conditions and questions (40, 41, 185, 214, 317 and this node) for:
  - "sections the spawn names"
  - "one case only"
  - "three markers"
  - "round that raised the flag"
  - "Raise a flag"
  - "When you raise a flag"
  - "What you read"
  - "Two things that travel"
  - "PERMISSION"
  - "FRICTION"
  - "Questions, alongside"

  Each match is on the node whose own subject it is. No other open node exists.
- **Replacements for an unclaimed node's condition:** node 41's clauses 1 and 5, and its added clause 11, are under ANSWER, each naming what fixed its words.
- **Questions this work changes:**
  - Node 40: the quote of `### Raise a flag` is stale ("a `research` node, an AFK `precondition` node" now reads "as with an AFK `precondition` node"), and "five contracts" is now four. The condition quotes the current text.
  - Node 41: "the same five worker contracts as open nodes 32, 38 and 40" is stale. There are four contracts, and of those three nodes only node 40 is still open.
  - Node 214: its title says "in both workers' contracts", but under the human's 2026-10-06 answer the raise applies to the implementer only.
  - Node 185: its open alternatives are answered by the human's decision.
  - All five nodes gain the opening sentence given under ANSWER.

MISSING FROM MAP:
- The split between graph-conventions.md (files and procedures) and SKILL.md (manager choices) is not stated in map.md. I found it in decisions.md, at node 312's line.
- The practice that a condition editing the four worker contracts keeps their shared sections byte-identical is not in the map. It arrived in the spawn's manager notes.

RETROSPECTIVE

1. **What I had to hunt for.** Which file node 41's clauses 4 to 6 belong in now. I looked first in graph-conventions.md and SKILL.md themselves. I found the rule in decisions.md's line for node 312, and then in node 312's condition.
   - `condition-cites-moved-paragraph` — carried by 1 earlier retrospective (node 284). Node 41's clauses predate node 312's split and target the file that rules no longer belong in.
2. **What arrived that this node did not need.**
   - `map-read-whole-for-a-few-items` — carried by 12 earlier retrospectives (nodes 135, 178, 205, 220, 284, 382, 386, 387, 388, 389, 390, 391). From map.md I used only writing rules 5 and 6, the related-defect preference and the dated-number rule.
   - `rules-file-read-whole-for-one-section` — carried by 9 earlier retrospectives (nodes 178, 220, 382, 386, 387, 388, 390, 391; one file holds two). From map-implementation-rules.md I used the standards list and the paragraph on dated numbers in a condition.
   - Searching decisions.md by node number, as the spawn asked, worked well. It is direct evidence for node 185's decision.
3. **What would have made this node easier.**
   - `node-history-read-to-reach-current-condition` — new name. Node 41's file holds notes about a glossary obligation and CONTEXT.md that later notes reverse. I had to read the whole chain to reach the condition as it now stands. One current-state line per node, under its condition, would have avoided that.
4. **What I read that was stale, wrong or contradictory.**
   - `question-quotes-superseded-text` — new name. Node 40's question quotes graph-conventions.md text that node 388 has since changed, and says "five contracts". Node 41's question names five contracts and nodes 32 and 38 as open.
   - `stale-number-in-the-record` — carried by 9 earlier retrospectives (nodes 178, 212, 220, 382, 385, 386, 388, 391; one file holds two). Node 185's question carries "111 lines", "80,400 bytes" and "roughly seventeen prior reports" with no re-derivation note.
`````

## Flags

`392.1` `ASSUMPTION` **· settled** — Node 41's clause 5 was relocated to SKILL.md; clauses 4 and 6 stay in graph-conventions.md. *(The worker's full text is under its handover's `FLAGS`.)*

`392.2` `ASSUMPTION` **· settled** — Node 214's condition accepts the approved sentence or equivalent wording, and covers node 208's case by the general rule. *(The worker's full text is under its handover's `FLAGS`.)*

`392.3` `ASSUMPTION` **· settled** — Node 185's condition leaves the label-scoping sentence open. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-06:* flags 392.1, 392.2, 392.3 settle at the node closing report that closes this node.
