# Say who writes a condition when no node spawned the node

Type: implementation
Status: superseded
Superseded by: 318

## Question

Two shipped files fix an acceptance condition as *"written by the node that spawned it"* —
`.claude/skills/expedition/graph-conventions.md` and [`CONTEXT.md`](../../../CONTEXT.md) — and an implementation
node the manager minted itself has no spawning node, so it cannot satisfy either. This node carries the rule
and its four constraints into those two files.

**The five worker contracts carry the same phrase and are not in scope**: in each, the phrase is followed by an
instruction assigning the condition to the reporting worker, which is correct and is a different case.

Reported by [Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md)'s worker, which wrote the acceptance condition below.

**Sequencing, not a blocker**, in that worker's words: *"`graph-conventions.md` is the live territory of
[Nothing checks that a part a checker left uncovered was ever established](45-nothing-checks-an-uncovered-part.md),
which holds the code slot. The landing policy forbids a second commit against one **node**, not one **file**, so
these may run in either order but not concurrently. Nothing in the condition below quotes that file's current
wording as the thing to be changed, for exactly that reason."* Node 45 has since resolved and landed as commit
`5a4ae83`, so the constraint now reads against whatever else holds the slot.

## Acceptance condition

1. **`.claude/skills/expedition/graph-conventions.md`, in the section that documents a node's
   `## Acceptance condition`, states who writes one for an implementation node that no other node spawned** —
   a node the manager created itself, whether from the human's steering, from its own reading of the graph, or
   as the replacement for a node being retired — **and states that it is the manager.** After this work, no
   sentence anywhere in that file states or implies that every acceptance condition has a spawning node behind
   it; wherever the phrase *"written by the node that spawned it"* or any equivalent appears there, it no longer
   stands unqualified.

2. **That same section states these four constraints on a condition the manager writes**, in the document's own
   voice and in whatever order suits it:

   - it may demand only what a resolved node, the node's own `## Question`, or the state of the files already
     fixes; anything the manager would otherwise have to decide is not written into the condition — the manager
     states the property and leaves the form to the worker, or raises the question to the human;
   - before the node is claimed, the manager reads the condition back against that document's own rule that a
     condition is self-contained text and its own rule that no condition may quantify over the record, and
     records that reading on the node;
   - the condition is marked on the node as the manager's own;
   - where the manager cannot write the condition in full, it writes the part it can, says plainly what is
     missing and why, never omits it in silence, and puts what is missing to the human; the node is not claimed
     until the condition is complete.

3. **`CONTEXT.md`'s `Acceptance condition` glossary entry no longer says a condition is written by the node
   that spawned it without qualification**, and says who writes one when no node spawned the node. Its
   `_Avoid_` line is unchanged, and no other glossary entry is edited.

4. **The five worker contracts are not changed by this work** —
   `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`,
   `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`,
   `.claude/skills/expedition-research/SKILL.md`. Each already follows the phrase with an instruction assigning
   a reported node's condition to the reporting worker, which is correct.
   `.claude/skills/expedition-checker/SKILL.md` is not changed either: a checker mints no nodes.

5. **Whatever that file already fixes about acceptance conditions is still present after this work and has lost
   nothing it required**: that a condition exists before any work starts; that its worker may not rewrite it
   and raises instead where it judges the condition wrong; that a condition is self-contained text whose reader
   never goes elsewhere to learn what it demands, permitting a path to say where and forbidding the demand
   itself to sit outside the text; that material held elsewhere is copied in, with the bar the one exemption;
   that no condition may quantify over the record, that duty being owed on a worker's `INVALIDATIONS` instead;
   and that a condition which points anyway is handed to the checker unrepaired. Its mechanical check that every
   `implementation` node has an `## Acceptance condition` before it is `claimed` is also still present.

6. **No file outside `.claude/skills/expedition/` and `CONTEXT.md` is changed by this work.**

7. **The working tree meets the bar.**

### One thing the manager owes whoever claims this

*Not a change to the condition above.* **Clause 3 edits `CONTEXT.md`, which [What keeps the shipped files
consistent when a decision changes a term](29-shipped-file-consistency.md) has just decided to move** into
`.claude/skills/expedition/CONTEXT.md`, with a completeness paragraph at its top and a forward pointer left at
the repo root — the human assenting to all three parts of that proposal. Clause 3 says *"`CONTEXT.md`'s
`Acceptance condition` glossary entry"* and names no path, so it survives the move; but **whichever of the two
nodes lands second inherits a file the other one moved or rewrote**, and clause 6's *"no file outside
`.claude/skills/expedition/` and `CONTEXT.md`"* reads differently once the glossary lives inside that directory.
Neither is blocked on the other and the two are not concurrently claimable, both editing the glossary.

## The human's decision, 2026-09-25

*The manager's question, proposing what node 312's worker proposed under its `RE-POINTING SEARCH:`:* "Do you agree to supersede node 55 with a smaller node covering those two parts, or keep node 55 as it is?" The two parts were `CONTEXT.md`'s entry saying a condition is "written by the node that spawned it", and the template code block in `graph-conventions.md` saying the same.

The human, `verbatim`: *"ok for supersede"*

## Superseded, 2026-09-25

*The manager's note.* Clauses 1, 2 and 5 are made unnecessary by [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s landing as `e64b3de`: under the split the human approved, who writes a manager-minted condition and the four constraints live in `expedition/SKILL.md`'s `## Acceptance conditions`, not in `graph-conventions.md`. The two parts still live are carried by [node 318](318-say-who-writes-a-condition-in-the-glossary-and-the-node-template.md).
