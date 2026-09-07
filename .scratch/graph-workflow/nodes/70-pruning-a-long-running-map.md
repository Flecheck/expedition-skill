# Pruning a long-running effort's map

Type: grilling
Status: claimed

## Question

[Restructure `map.md` to what every worker needs](59-restructure-the-map.md) moved the map's append history into
`map-history.md` and cut every worker's map read by 71%. **It fixed the file workers read and created a file that
grows without bound.** `map-history.md` is already 87,768 bytes at 67 nodes; the dogfood target is 179.

### The human's instruction, `verbatim`

> *"We should add a node for cleanup of old data in the map for long running efforts"*

### Why node 59 does not already answer this, and why the answer cannot simply be "move it again"

Node 59 worked because there were **two readers with different needs** — a worker who must act, and a reader who
wants the account — so the split fell on a real seam. There is no third reader behind `map-history.md`. Anything
moved out of it is moved out of the effort's working files entirely, and that is a different act with a different
rule governing it.

**The rule is the never-delete preference**, and it is the oldest standing constraint in this effort: *when any file
in the graph is edited, nothing is deleted; the old text is marked in place and the new text is added around it.*
Node 59 satisfied it by moving text **verbatim** — the discharge was that all 106 before-state lines still existed
somewhere a reader could reach. **Pruning cannot make that claim**, so this node has to confront the rule rather
than route around it.

### The observation that probably decides it, offered as the manager's own and not as a finding

**Every graph file is committed, so nothing in them has ever been deletable in the sense the rule fears.** The
human commits the tracker periodically — `7d29001 periodic save of map` landed during node 59's run — so the
account of any line is in git whether or not it is in a working file. If the never-delete rule exists to keep the
record recoverable, **git already discharges it**, and the rule's real subject is what a *reader* meets in a file
rather than what exists at all.

If that reading holds, pruning is not deletion but **a change of where history is looked up**, and the question
becomes which material earns its place in a working file versus in `git log`. If it does not hold — because the rule
is also about not making a reader run git to understand a line — then pruning needs a destination and this is a
much larger node.

## What has to be decided

1. **What "old" means.** Node count, age, or the state of the thing described. The strongest candidate is
   **discharge**: an account of a preference that has since been superseded, or a fog item long since spent, has a
   different claim on a working file than a live item's history does. Node 59 already met this — it moved two
   **spent** fog items and flagged the judgement as `59.2`.
2. **Whether the never-delete rule reaches a file's own history file at all**, or is scoped to what a reader meets
   in `map.md` and the node files. Node 59's own fog item on this was narrowed to *"a node file's reader, not this
   map's"*, so the scope is already known to be narrower than it was written.
3. **Where pruned material goes**, if anywhere: git alone, a dated file, or out.
4. **Who runs it and when.** A sweep at close is the obvious hook and the wrong one for a *long-running* effort,
   which is the case the human named. A periodic manager pass is the alternative, and the manager is the party with
   the least context to spare.
5. **Whether the node files need the same treatment.** They are the larger corpus and nothing has measured them —
   this node should measure before assuming the map is where the growth is. Node 13's split was justified on a
   growth rate that turned out to be wrong, which is the cautionary case and is annotated there.

## What is already known, and worth not re-deriving

- **The growth is words per item, not items.** Measured at node 53 and annotated on [Graph file
  format](13-graph-file-format.md): `map.md` reached 92,113 characters while `decisions.md` stayed at one capped
  line per node. **A cap per item is what has actually held**, twice — `decisions.md`'s and node 59's 900-character
  fog items — and neither needed pruning to stay small.
- **That suggests the cheaper answer may not be pruning at all**, but a cap on `map-history.md`'s entries of the
  kind that has already worked twice in this effort. The human asked for cleanup; the manager notes the alternative
  because the two have very different costs and only one of them touches the never-delete rule.

## Where it came from

The human's own instruction, unprompted, alongside [Run an implementation node's work in a
worktree](68-implementation-in-a-worktree.md) and [Whether the workflow ships explicit subagent
definitions](69-explicit-subagent-definitions.md).

## Interview

### Attempt 1

**The worker's first payload carried two questions**, `Q1` and `Q2`, under the batching rule node 126 landed. Its
`SO FAR` reported measurements against this node's own premise, which the manager relayed in full.

**The human's first reply, `verbatim`.**

> I wasn't the one making the no delete rule, it was done by you but it's not a bad idea, which is why I approved it. It seems to be causing some issues ? With line count ? What do you think about it. For the action of doing the cleanup I would see like the stop skill, a cleanup skill. For the cleanup skill, it is designed to delete things so it should be fine.

***The manager's note.*** **Not an answer to either question**, and the manager did not read *"it's not a bad
idea"* as taking `Q1`. It carried three things: a **correction of attribution** — the never-delete rule is the
workflow's own and not the human's, recorded as an annotation on [node
189](189-where-the-never-delete-rule-stops.md); **a question back** to the manager about line count, which the
manager answered from measurements already in the record; and **a mechanism neither question offered**, cleanup as
an invoked skill on the model of [node 166](166-ship-an-expedition-stop-skill.md)'s stop skill.

**The worker withdrew `Q1` rather than re-asking it**, in its words: *"I put Q1 to you as 'your oldest standing
rule'. That was wrong and you were right to say so. I have now checked it myself: twelve of the standing
preferences in `map.md` carry your words marked `verbatim`, and the never-delete bullet carries none and cites no
node. It is the workflow's own rule. I withdraw Q1 — not because you refused it, but because it was built on that
premise."*

**It answered the human's question back with a measurement**, in its words: *"**No, and the number is not close.**
I measured every struck-through passage in the entire record: **6,252 bytes out of 3,600,256 — 0.17%.** In `map.md`
itself it is 1.13%. Across all 193 node files, 0.07%."*

**The human's second reply, `verbatim`.**

> Q3 ok. Q2. I see the cleanup more as a logical cleanup than just a text cleanup. In the idea, either the user choose or the skill finds part of the graph that is considered "done" and then if the effort needs to work on it again it is like the work that was already done was already shipped. For example in Lang, if after a while, the parser is considered done, we can remove the completed issues regarding the parser and if we later need to modify the parser we look at the code instead of looking at all the previous issues. The main source of truth at this point would be the code and documentation instead of using the map. In this idea then all files can be cleanup.

**What `Q3 ok` takes**, quoted from the worker's own re-asked payload and attributed to the worker:

> **RECOMMENDED:** It ships. *"Without it, every future effort's cleanup skill contradicts the rule stated two files
> away, and the manager or a worker re-derives the exemption each time. That is the identical defect node 189 was
> minted for."*

***The manager's note on `Q3`.*** **Not a divergence**, and it takes neither alternative — neither *stays in this
effort's map only*, nor *ships written as a property of the cleanup skill rather than as an exemption to the
never-delete rule*. **It is the second time in this session the human has shipped a boundary against the map's own
standing default** that a rule reaches a shipped file only where they say so, the first being node 189's `Q3`.

***The manager's note on `Q2`.*** **A reframing, not a choice among the three offered**, and it went back to the
worker rather than being read as taking any of them. **All three of the worker's candidates were classes of
text** — struck-through passages, spent fog, settled flag entries. **The human's unit is a subject area of the work
whose output has shipped**, and it cuts across every file at once: their words, *"either the user choose or the
skill finds part of the graph that is considered 'done'"*, and *"In this idea then all files can be cleanup."*
**It also asserts something about what the record is for**, which no question put to them: *"The main source of
truth at this point would be the code and documentation instead of using the map."* `Q2` stays unsettled and its
number is fixed.
