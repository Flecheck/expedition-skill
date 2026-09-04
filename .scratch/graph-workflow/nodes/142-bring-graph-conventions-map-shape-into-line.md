# Bring `graph-conventions.md`'s map shape into line with the split map

Type: implementation
Status: open

Blocked by: 140

## Question

*Surfaced by [Move the manager's material out of the map](139-move-the-managers-material-out-of-the-map.md)'s worker,
and pasted as it wrote it.*

> `graph-conventions.md` now lists six graph files including `map-manager-only.md`, but three of its statements still
> place the fog and out-of-scope inside `map.md`: the sentence *"`map.md` has five sections, in this order:"* with its
> bullets for `## Not yet specified` and `## Out of scope`, the `Resolve` procedure's step 5 (*"`map.md`: remove that
> item from `## Not yet specified`"*), and the `Rule out of scope` procedure's step 2 (*"`map.md`: append one line to
> `## Out of scope`"*). Node 139's clause 11 forbade touching them. It waits on node 140 because node 140's own
> condition reuses node 139's clauses 1 to 8 and 12 to 13 only — so nothing raises the file count from six to seven
> when the second sibling lands either, and the shape should be corrected once rather than twice.

## Acceptance condition

*Written by node 139's worker. Pasted as it wrote it, and not the manager's.*

> The work is the file `.claude/skills/expedition/graph-conventions.md`. It is
> written against whatever `.scratch/graph-workflow/` holds at claim time, because
> which sections have moved out of `map.md` is not fixed until node 140 lands. Done means every one of the following
> is true of the finished tree.
>
> 1. The sentence in `graph-conventions.md` beginning `` `map.md` has ``, and the bulleted list under it, name every
>    `##` heading that `.scratch/graph-workflow/map.md` actually holds, and name no
>    heading it does not hold. The count stated in that sentence equals the number of bullets under it.
> 2. Every `##` heading that has moved out of `map.md` into another file in that directory is described in
>    `graph-conventions.md` under that other file rather than under `map.md`, and its one-line description says the
>    same thing it said before the move.
> 3. The `### Resolve` procedure's step that removes a resolved fog item names the file that actually holds `## Not
>    yet specified`.
> 4. The `### Rule out of scope` procedure's step that appends the out-of-scope line names the file that actually
>    holds `## Out of scope`.
> 5. The heading that opens the graph's file list states the number of entries the list holds, and the list holds one
>    entry for each file present in `.scratch/graph-workflow/` plus one entry
>    standing for the per-node files under `nodes/`.
> 6. No file under `.scratch/graph-workflow/` is modified, and no file under any of
>    `.claude/skills/expedition-checker/`, `.../expedition-grilling/`,
>    `.../expedition-implementation/`, `.../expedition-precondition/`, `.../expedition-prototype/`,
>    `.../expedition-research/` is modified.
> 7. `graph-conventions.md` changes in no respect other than clauses 1 to 5.

## The manager's note at filing

*Not a change to anything above.*

**This node exists because a condition fenced its own worker out of a defect that condition created**, which is flag
`139.1`. Node 139's clause 11 required `graph-conventions.md` to name the correct file count while forbidding any
other change, and raising the count is exactly what made three other passages of the same file false. Its worker read
the fence as binding, said so, and reported this node rather than reading the fence generously. **The manager takes
no view on which reading was right and records that both were available.**

**Its condition is the first on this graph written entirely against the tree at claim time rather than against any
state its author could see.** Every clause reads a fact off `.scratch/graph-workflow/` when the work runs, because
node 140 has not landed and the shape is not yet fixed. Under [node 94](94-condition-scope-as-a-predicate.md)'s
rungs it is a predicate with a domain and no recorded return, which is legitimate and which its checker cannot
compare against anything — there is nothing to re-run.

**Why it is blocked on [node 140](140-move-the-implementers-and-checkers-material-out-of-the-map.md) rather than
merely sequenced after it.** Node 140 adds a seventh file and moves more sections out of `map.md`. Doing this node
first would correct the shape to a state node 140 immediately invalidates, which is the double work its author named.
