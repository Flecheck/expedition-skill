# Move the implementer's and checker's material out of the map

Type: implementation
Status: open

Blocked by: 138

## Question

*Surfaced by [`map.md` has grown back most of what node 59's restructure
saved](136-the-map-has-grown-back-what-node-59-saved.md)'s worker, and pasted as it wrote it.*

> Move the landing policy, the worktree lifecycle, the code-slot count and the bar's commands — 4,358 bytes named by
> seven and eleven retrospectives respectively as read-and-unused — out of the file every worker reads, into one
> sibling the implementation and checker spawns point at, which is the single-source shape the direction in node B
> asks for.

**Blockers, in the worker's words:** *"**B**, whose answer decides whether this node exists at all."* That is [node
138](138-where-the-rules-a-checker-is-held-to-live.md).

## Acceptance condition — written in part, deliberately

*Written by node 136's worker. Pasted as it wrote it, and not the manager's.*

> **written in part, and what is missing is named rather than left out.** The shape is node A's clauses 1 to 8 and 12
> to 13 with the five moved bodies replaced by four — the paragraph beginning `**Landing policy**`, the paragraph
> beginning `**How many implementation workers run at once`, the paragraph beginning `**What that supersedes**`, and
> the paragraph beginning `**The bar's commands for this repo`. **What cannot be written until node B answers is the
> destination**, which is the whole of what this node does: whether that material may sit in a sibling at all, and
> whether the file it goes to is the same one node A creates or a second one for the implementer and checker. A
> condition naming a destination the human has not chosen would send its worker at the wrong file, so the byte figure
> and the clause list are stated and the destination is left for the manager to put to them.

*"Node A"* is [node 139](139-move-the-managers-material-out-of-the-map.md).

## The manager's note at filing

*Not a change to anything above.*

**This node is not startable and its condition says why.** Under [node 95](95-acceptance-condition-readiness.md)'s
readiness floor an implementation node is startable when its condition can be written in full; this one cannot be,
and its author said so rather than inventing the missing clause. **The manager has written nothing into it.**

**What completes it is one answer from node 138** — whether the human's *"at the map level"* permits a sibling, and
if so whether the implementer's and checker's material shares node 139's new file or gets its own. Once that lands,
the condition's remaining clauses are mechanical from the shape already given.
