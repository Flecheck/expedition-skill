# Starting an effort has no section in the manager's contract

Type: grilling
Status: resolved

## Question

*Surfaced by [Adopting an in-flight effort](18-adopting-in-flight-effort.md)'s worker, and pasted as it wrote it.*

> An effort begins in one of two ways — charted from a conversation, or adopted from work that already exists — and
> the manager's shipped contract describes neither. Its headings run from `## Words used exactly` to `## Closing an
> effort` with nothing in front, and `CONTEXT.md`'s fifty entries hold no word for either act. So the parts of
> starting an effort that both ways share — writing the map, fixing the destination, declaring the label vocabulary —
> have nowhere to live, and node 18's answer states them inside adoption for want of anywhere else. What does
> starting an effort consist of, which parts do the two ways share, and does the shared part get a section of its
> own?

**Blockers, in the worker's words:** *"none."*

> **Reported knowing it overlaps [node 91](91-charting-records-whether-an-effort-ends.md), and the manager may prefer
> to widen 91 rather than take this as a second node.** They are not the same question — 91 asks whether charting
> *records that an effort is expected to end*, which presumes the section this one says is missing — but one worker
> could hold both, and 91 is open and unclaimed.

## Answer

*Written by this node's worker on attempt 2, and pasted as it wrote it.*

**Starting an effort gets a place of its own in the shipped files, and it is two writes.** The human, `verbatim`:
*"For 98, ok for recommanded"*, taking the option this node's worker offered at attempt 1 and quoted under
`## Interview`. Not a divergence.

### What starting an effort consists of

An effort begins in one of two ways, and they differ only in their input. **Charting** starts from a conversation
with the human, with nothing on disk before it. **Adoption** starts from a directory of work that already exists.
Both produce the same thing: an effort's five files and its first nodes.

### The six parts the two ways share

1. **The effort's name**, which is its directory's.
2. **The destination** — what reaching the end of the effort looks like.
3. **Whether the effort is expected to reach it** — settled at this moment and written into the map. This part is
   [node 91](91-charting-records-whether-an-effort-ends.md)'s and lands here because this section is where it belongs.
4. **The map's standing preferences**, the effort's **ground rules** where it has any, and its **standing over
   sources** where it has one.
5. **The label vocabulary**, declared or declared absent.
6. **The effort's first nodes.**

Everything else in [Adopting an in-flight effort](18-adopting-in-flight-effort.md)'s seven steps is adoption's own:
taking the name from a directory that already exists rather than choosing one, resolving a reserved graph name the
directory is already using, deriving the map from the foreign record rather than from a conversation, declaring
labels from the foreign families, appending an expedition section to the target's tracker doc, building the
citation-repointing table, and minting the bulk import as `precondition` nodes.

### Where each part lives, and why the split falls there

**A `## Starting an effort` section in the manager's contract**, saying what the act establishes, that it has two
inputs, and that the manager performs it before the graph exists. **A `### Start an effort` procedure in
`graph-conventions.md`**, listing the files the act creates in order. **Adoption's extra steps stay in the separate
`adoption.md`** that [node 97](97-write-the-adoption-procedure.md) will write.

The contract already declares this division in its own opening — *"This contract says what you do; that document
says what the files look like when you have done it"* — and every other act that writes graph files has a procedure
in the conventions document. Measured while writing this answer: `graph-conventions.md` carries **eight** procedures
(`Claim`, `Resolve`, `Supersede`, `Rule out of scope`, `Park`, `Raise a flag`, `Settle a flag`, `Change the map`),
and **starting an effort is the only act that creates all five files and the only one with no procedure**. The split
also keeps the cost right: the contract section is a handful of lines, and the mechanical detail sits in the file
read before touching an effort's files rather than in the entry skill read on every effort.

### The gap is measured, not asserted

`grep -rln -i "starting an effort\|start an effort\|charting\|adoption" .claude/skills CONTEXT.md` returns **no
files**. The shipped set contains no statement of either act. The one adjacent sentence is in
`wayfinder-divergences.md` under `## Not covered here` — *"Importing an effort that is already under way … That is a
separate procedure"* — which points at a procedure rather than stating one.

### What this answer does not disturb

**Node 18's answer is discharged rather than contradicted.** Its `### What this answer depends on and does not
supply` said the shared steps were *"stated here for want of anywhere else, and belong with charting when charting
is written."* This is that anywhere-else.

**Node 97's acceptance condition stands unamended**, on the reading recorded as a flag below.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`98.1` `ASSUMPTION` **settled** — **Node 97's acceptance condition needs no amendment, and the human's approval of this node
disposes of the tension attempt 1 flagged.** Attempt 1 flagged, and the manager passed on without endorsing, that
node 97's condition item 3 would ship the seven shared start-of-effort steps inside `adoption.md`. I read item 3
clause by clause against node 18's seven steps and judge the overlap thin rather than whole. Item 3's spelled-out
content is mostly adoption's **specialisation** of a shared step, not the shared step: *"copied from what the effort
already wrote rather than invented"* is what distinguishes adoption from charting, and *"declaring the label
vocabulary from the foreign label families"* likewise. Only *"writing `map.md`"* and *"creating the remaining graph
files empty"* are purely shared, and adoption.md must state the sequence anyway because the adoption-specific and
shared steps interleave. Against that, [Whether the five contracts' shared blocks stay
duplicated](50-shared-blocks-stay-duplicated.md) is open and the effort currently duplicates 216 lines across five
contracts **deliberately**, so a two-clause overlap is not a defect this effort forbids today. Narrowing a condition
is also not something node 82 licenses — that procedure covers widening, where an amendment adds places and no
demand — so treating this as a defect would have cost a node or a human turn to repair something that is inside the
effort's own tolerance. What I accepted: if node 50 later rules against duplication, adoption.md is one of the places
that has to be re-read.

`98.2` `ASSUMPTION` **settled** — **Left the new section's position in `SKILL.md` as a checkable property rather than fixing its
slot.** The contract's fourteen `##` headings put no act before `## Words used exactly` and end the act sequence at
`## Closing an effort`. The natural slot is directly after `## Words used exactly`, so the act sections run in the
order an effort runs them — but `## What is never yours` and `## Writing the graph` are cross-cutting rules rather
than acts, and putting a single act in front of them is arguable either way. I wrote the condition to demand only
that `## Starting an effort` appear **before** `## Closing an effort` and left the slot to the worker, on the ground
that stating the property and leaving the form is what the contract asks of a condition's author.

## Interview

### Attempt 1, round 1

**Asked**, in the worker's words:

> Does starting an effort get a place of its own in the shipped files — and is it these two writes: a short
> `## Starting an effort` section in the manager's contract saying what the act establishes and that it has two
> inputs, plus a `### Start an effort` procedure in `graph-conventions.md` listing the files it creates in order,
> with adoption's extra steps staying in the separate `adoption.md` node 97 will write?

**Answered**, `verbatim`:

> For 98, ok for recommanded

**The option taken**, written by this node's worker and quoted here as it offered it:

> Yes, and split exactly that way. The contract already declares this division in its own opening — *"This contract
> says what you do; that document says what the files look like when you have done it"* — and every other act that
> writes graph files (add a node, resolve, supersede, park, raise a flag, change the map) already has a numbered
> procedure in the conventions document listing the files it touches. Starting an effort is the only act that creates
> *all five* files and it is the only one with no procedure. The split also keeps the cost right: the contract
> section is a handful of lines about what the manager establishes and who decides it, and the mechanical detail sits
> in the file read before touching an effort's files rather than in the entry skill read on every effort.

*Not a divergence: the reply takes the worker's own recommendation.*

**Attempt 1 died here**, on a session limit reported by the harness — not on anything about this node, and after the
answer above had reached disk. It never asked its second question, which it had said would be [Charting records
whether an effort is expected to end](91-charting-records-whether-an-effort-ends.md)'s. The answer above is **banked**
and travels to attempt 2, which will not put the same question to the human twice. The claim stays with the node, as
a death releases none.

### Attempt 2

Spawned with the banked answer and with node 91, which attempt 1 had judged one question with this node.

## The manager's note at filing

*Not a change to anything above.*

**Filed as its own node rather than folded into node 91**, and the reason is the same one that keeps recurring: node
91 is another agent's node, and widening another party's question to absorb a second one is the shape [How a
condition's scope is amended](82-amending-a-condition-whose-scope-was-too-narrow.md) governs for conditions and
nothing governs for questions. Filing two cheap nodes costs less than deciding that.

**Whoever picks either should almost certainly claim both**, and this note says so rather than the graph enforcing
it: node 91 presumes the section this node says is missing, so answering 91 alone writes a duty into a document that
has nowhere to put it. There is no `Blocked by:` edge between them because neither strictly blocks the other.

**A third node sits beside these two.** [Rules added to one effort's map, and what makes them
legitimate](93-effort-scoped-custom-rules.md) is about what an effort's map may carry that the workflow does not, and
declaring such a rule is plainly an act of starting an effort — but it is a question about the map's contents rather
than about the contract's missing section, so it stays separate.

## Retrospective

*The worker's own text, pasted, handed back as the sixth handover part this effort asks for. It is **one
retrospective across both of its nodes** — this one and [node
91](91-charting-records-whether-an-effort-ends.md) — and is filed here whole rather than split, since splitting it
would be re-authoring. Node 91 carries a pointer to it.*

**What I had to hunt for.**

- *That the node 97 tension is thinner than it was described.* The spawn's manager note, and attempt 1's flag behind
  it, said node 97's condition *"would ship the seven shared start-of-effort steps inside `adoption.md`"*. I looked
  first at node 98's `## Interview` and the manager's note, which is where the characterisation lives. The fact is
  only visible by laying node 97's condition item 3 beside node 18's seven steps clause by clause — most of item 3's
  spelled-out content is adoption's *specialisation* of a shared step, not the shared step. That reading is what
  turned a human turn into a flag.
- *How many procedures `graph-conventions.md` actually has.* The banked option I inherited argues from *"every other
  act … already has a numbered procedure"*, and `decisions.md`'s node 21 line says seven. One `grep -n "^### "` says
  eight. I looked first at the `decisions.md` line, which is stale.
- *The sentence that actually governs node 91.* I looked first at `map.md`'s `## Destination` and `CONTEXT.md`'s
  `Destination` entry, neither of which says anything about terminability. The governing sentence — *"the destination
  decides whether an effort can terminate"* — is six sections into node 10's answer, reachable only by reading that
  node whole.

**What I read and did not use.** Node 46 in full: about ninety duties across nine manager→human forms, of which I
used two facts, and the spawn had already given me both, so the read confirmed rather than informed. Node 50 in full
including three annotations, used for one sentence — that this effort has not decided against duplication.
`graph-conventions.md`'s `## Review` section and its whole `NOT COVERED:` / `OWED` / `ESTABLISHED BY` machinery,
about fifty-five lines, neither of my nodes touching a checker. Node 86's landing-policy sections and its eight-site
invalidation list, of which I used one quoted sentence of the human's. Node 10's bar, sweep and cascade-miss
sections. Node 94 in full, read to write one condition correctly, of which I used `### The three rungs`.

**What would have made this node easier.**

- *In the spawn:* the note characterised node 97's condition rather than quoting it, and the characterisation was an
  overstatement I had to undo before I could judge. Quoting item 3 would have cost the manager one paste. This is the
  note-cap working exactly as designed — the manager holds no more than it holds — so the fix is not more work for it
  but *quote, do not summarise*, which is strictly cheaper.
- *In the node files:* the same sentence about the contract's headings — *"its headings run from `## Words used
  exactly` to `## Closing an effort` with nothing in front"* — appears independently in node 98's question, node 91's
  question, and node 18's answer. Three copies, three things to fix, and all three are slightly misleading about the
  shape: there are fourteen headings, and the fact that matters is that none names an act happening before the graph
  exists.
- *In the contract:* nothing blocked me. The one observation is the flag above — it tells me to invoke two method
  skills if present, they are present, and I did not, as the two grilling workers before me did not.
- *Structurally, and it worked:* holding both nodes together was right and saved a human turn. Node 98's banked
  answer is what let me settle node 91's shape without first asking what starting an effort consists of. A worker
  given node 91 alone would have had to ask that question or guess it.

**What I read that was stale, wrong, or contradicted something else.** Five things, all reported above and none
repaired by me.

- `map.md`'s fog item on the skill-file implementation nodes says *"the manager's own skill has no node yet"*; node
  76 shipped it and `decisions.md` carries the line.
- `decisions.md`'s node 21 line says seven procedures; there are eight.
- `CONTEXT.md`'s `Destination` entry is short by node 91's answer, and no open node reaches it.
- `CONTEXT.md`'s `Closed` entry still states the frequency claim the human rejected, and its `Closing report` entry
  still lists three items where the settled list has six — both already minted as nodes 90 and 106, named here only
  so nobody re-mints them.
- The glossary's own size is given three ways in three places: node 98's question quotes *"fifty entries"*, `map.md`
  says *"50 term entries and 40 `_Avoid_` lines"*, and node 86's retrospective says *"one entry of fifty-one"*.
  Minor, but it is a count nobody re-derives and three files disagree.

**The manager's note on the retrospective.** *Not a change to anything above.* Three of its five staleness reports
are now repaired: `map.md`'s fog item is rewritten and its superseded text moved to `map-history.md`;
`decisions.md`'s *seven* is struck in place and reads eight; and `CONTEXT.md`'s `Destination` entry has a node, [node
114](114-context-destination-entry-omits-the-expectation.md), minted with a manager-written condition because the
worker surfaced it as an invalidation rather than as a node and node 111's own clause 12 could not absorb it. The
glossary's three-way count is carried on [node 112](112-what-the-glossary-calls-starting-an-effort.md), which is the
node that will be in that file. **The one item the manager owes and has not done** is its own: the spawn note that
characterised node 97's condition instead of quoting it. *Quote, do not summarise* is cheaper for the manager as well
as better for the worker, and it joins the promotions the manager owes off retrospectives.
