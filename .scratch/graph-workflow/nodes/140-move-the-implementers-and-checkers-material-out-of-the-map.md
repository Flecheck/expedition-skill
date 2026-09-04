# Move the implementer's and checker's material out of the map

Type: implementation
Status: open

Blocked by: 139 landed — see the completed condition below

## Question

*Surfaced by [`map.md` has grown back most of what node 59's restructure
saved](136-the-map-has-grown-back-what-node-59-saved.md)'s worker, and pasted as it wrote it.*

> Move the landing policy, the worktree lifecycle, the code-slot count and the bar's commands — 4,358 bytes named by
> seven and eleven retrospectives respectively as read-and-unused — out of the file every worker reads, into one
> sibling the implementation and checker spawns point at, which is the single-source shape the direction in node B
> asks for.

**Blockers, in the worker's words:** *"**B**, whose answer decides whether this node exists at all."* That is [node
138](138-where-the-rules-a-checker-is-held-to-live.md).

## Acceptance condition — written in part, deliberately. ~~Live~~ **superseded below**

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

## Acceptance condition — completed, and superseding the partial one above

*Written by [node 138](138-where-the-rules-a-checker-is-held-to-live.md)'s worker, which held the decision the
partial condition was waiting on. Pasted as it wrote it, and not the manager's.* **The partial text above stands
where it is under the never-delete rule and is no longer this node's condition.**

**Its author's own account of why it may replace rather than append**, in its words:

> Node 140's author wrote its condition in part and refused to name a destination the human had not chosen; the human
> has now chosen it, that author is gone, and this node holds the decision, so the completion is written here as the
> node will hold it. It replaces the partial text rather than being appended to it, and the clause list and byte
> figures below are measured against the post-139 tree rather than the one its author saw.

**Blockers, in its words:** *"node 139 landing, since two of the clauses below are stated against the tree it
produces."* Node 139 landed as commit `4e38c11`.

> The work is `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/` and the file
> `/home/mathieu/projects/graph-agent/.claude/skills/expedition/graph-conventions.md`. Editing `map.md` is what this
> node is for: its subject is the map itself rather than a report of progress on other work. The worker may edit the
> files named here; it may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> The before-state is the working tree at claim time and is recoverable with `git diff`. For scale only, and not to
> be relied on: when this condition was written `map.md` was 31,481 bytes and held three `##` headings — `##
> Destination`, `## Notes`, `## Decisions so far` — and `map-manager-only.md` sat beside it holding the material only
> the manager acts on.
>
> Done means every one of the following is true of the finished tree.
>
> 1. A new file sits beside `map.md` in the same directory, holding the rules an implementation worker works to and a
>    checker holds work against. Its own first sentence names those two as its readers and says that it is part of
>    the map, so that a rule written in it binds this effort exactly as a rule written in `map.md` does. Neither its
>    filename nor the name it gives itself contains the word `provenance` or the word `criteria`: this effort's
>    glossary refuses both by name.
> 2. The new file's headings do not include `## Notes`. A size target and a mechanical check in
>    `graph-conventions.md` are written against *the map's `## Notes`*, which already resolves to two sections; a
>    third is not this node's to create.
> 3. Four bodies of material are in the new file and are no longer in `map.md`: the paragraph beginning `**Landing
>    policy**`; the paragraph beginning `**How many implementation workers run at once`; the paragraph beginning
>    `**What that supersedes**`; and the paragraph beginning `**The bar's commands for this repo`.
> 4. One further body is in the new file and is no longer in `map-manager-only.md`: the paragraph beginning `**The
>    review route for this repo, discovered on first use**`.
> 5. That review-route paragraph is unchanged in wording. In particular the sentence naming `this map's standing
>    preferences, ground rules and four standing rules` is left exactly as it stands: making that reference resolve
>    for a reader who does not read `map.md` is not this node's work.
> 6. `map-manager-only.md`'s own description of what it holds no longer names the review route.
> 7. For the new file `map.md` holds a pointer of at most three lines: a markdown link to it, and one sentence saying
>    who reads it and what it holds. `map.md` restates none of the material moved.
> 8. Nothing was deleted, summarised, paraphrased or shortened by the move. For every line `map.md` or
>    `map-manager-only.md` loses, that line's text appears in the new file. Compare after unwrapping both sides; a
>    difference confined to a line's leading markdown (list marker, heading marks, opening emphasis) does not count.
> 9. `map.md` is at least 3,900 bytes smaller than its before-state.
> 10. `map.md` holds exactly these `##` headings and no other at `##` level: `## Destination`, `## Notes`, `##
>     Decisions so far`.
> 11. The block in `map.md`'s `## Notes` beginning with the line `**Ground rules for this effort.**` and the numbered
>     rules under it, and the block beginning `**Four standing rules for writing anything in this effort**` and the
>     numbered rules under it, are byte-identical to their before-state and remain in `map.md`. Both are copied into
>     other agents' instructions or held against every deliverable, so neither may be reworded, renumbered or
>     reordered, and neither moves in this node.
> 12. `graph-conventions.md` names the correct number of files where it lists the graph's files, and describes the
>     new file's role in one sentence. It changes in no other respect.
> 13. No file under any of `/home/mathieu/projects/graph-agent/.claude/skills/expedition-checker/`,
>     `.../expedition-grilling/`, `.../expedition-implementation/`, `.../expedition-precondition/`,
>     `.../expedition-prototype/`, `.../expedition-research/` is modified.
> 14. Every markdown link in `map.md`, in `map-manager-only.md` and in the new file resolves to a path that exists.

***The manager's note.*** **Its clause 9's floor of 3,900 bytes is the worker's own number and is flagged as such** at
`138.6`, derived from node 139's headroom against a measured 4,376 bytes of movable material. **The manager has
neither set it nor checked it**, and records that node 139's floor was met in bytes and mis-reported by the manager
in characters, so a reader comparing the two numbers should hold them in the same unit.

**Its clause 12 will collide with [node 142](142-bring-graph-conventions-map-shape-into-line.md) and [node
146](146-graph-conventions-map-rules-name-two-notes-sections.md)**, which both edit `graph-conventions.md`. Node 142
is blocked on this node precisely so the shape is corrected once; node 146 is not, and with a code slot of one all
three serialise.
