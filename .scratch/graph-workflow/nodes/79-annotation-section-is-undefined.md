# The node format has no section for a manager-filed annotation

Type: implementation
Status: open

## Question

`graph-conventions.md` fixes six sections on a node file — `## Question`, `## Acceptance condition`, `## Answer`,
`## Flags`, `## Review`, `## Interview` — and states that *"Sections appear in that order and only when they have
content."*

**The manager has written roughly forty `## Annotation:` sections onto this graph's nodes, several of them above
`## Answer`, and the document names none of it.**

That is the channel [Cascade pass mechanics](15-cascade-pass-mechanics.md) measured as carrying **fifteen of
eighteen propagations onto resolved nodes** — so it is the graph's busiest write and its least documented.

Reported by node 75's worker as item 175 of §Q2, which wrote the acceptance condition below.

**Blockers: none.** It edits `.claude/skills/expedition/graph-conventions.md` and so contends for the code slot with
[Say who writes a condition when no node spawned the node](55-who-writes-a-condition-with-no-spawning-node.md),
[State in a shipped file that a hard rule binds by being read](73-a-hard-rule-binds-by-being-read.md), and any other
node editing that file.

## Acceptance condition

*Written by node 75's worker.*

`.claude/skills/expedition/graph-conventions.md` gains, in the section that documents a node file's sections, a
statement of a seventh section that a node may carry: an **annotation**, written by the manager onto a node whose
answer a later node has changed the meaning of. Done means all of the following.

1. That section states that an annotation records what a later piece of work changed about this node's answer, that
   its text is the reporting agent's own words where a reporting agent supplied them, and that it is added rather
   than replacing anything the node already holds.
2. It states where an annotation sits relative to the six sections already listed, so that the file's existing rule
   — that a node's sections appear in a stated order and only when they have content — is true of a node carrying
   one. Whether the annotation is one section or several, and where in the order it falls, is the author's to
   choose and to state.
3. It states that an annotation may carry a heading naming what it records, and gives the form of that heading.
4. It states that an annotation is the manager's to write and never a worker's, consistent with that document's
   existing statement that the manager is the graph's only writer.
5. Whatever that file already fixes about a node file is still present afterwards and has lost nothing it required:
   the mandatory fields, the rule that fields live in the header block and nowhere else, the six section names, and
   the statement that sections appear in a stated order and only when they have content.
6. No file under `.claude/skills/expedition-checker/`, `expedition-grilling/`, `expedition-implementation/`,
   `expedition-precondition/`, `expedition-prototype/` or `expedition-research/` is changed: `git diff` over those
   six directories comes back empty.
7. No file under `.scratch/` is changed, and no file outside `.claude/skills/expedition/` is changed.
8. The existing headings of `.claude/skills/expedition/graph-conventions.md`, listed by `grep -n '^#\{1,6\} '`, are
   all still present afterwards and in the same order, with the new material added rather than replacing any of
   them.
9. The working tree meets the bar.

### What the author of this condition could not settle

> Whether an annotation is properly a **section** of the node file or a marked append inside `## Answer`. Clause 2
> states the property — the file's own ordering rule must come out true — and leaves the form to the worker,
> because choosing between the two is a decision this node's author was not in a position to make.
