# Pruning a long-running effort's map

Type: grilling
Status: open

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
