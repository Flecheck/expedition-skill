# State where the never-delete rule stops, in this effort's map

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [Where the never-delete rule stops](189-where-the-never-delete-rule-stops.md)'s worker, and pasted as
it wrote it.*

> `map.md`'s standing preference beginning *"An in-place update never deletes"* says *"when any file in the graph is
> edited — a node or this map —"*, which has twice been read as an exhaustive list, and it says nothing about the
> rule stopping at a rule statement. Both boundaries are now settled and neither is written anywhere a worker meets
> them. Write them into the map, and into the rules file that node 144 made stand alone for a reader who does not
> read `map.md`.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 189's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-implementation-rules.md`, plus
> `.scratch/graph-workflow/map-history.md` where clause 2 requires text to be moved into it. No other file may be
> edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
>
> 1. `map.md`'s standing preference beginning `**An in-place update never deletes.**` states all four of the
>    following in its own text:
>    a. the rule governs the effort's own record files — `map.md` and its siblings, `decisions.md`, `flags.md`, and
>       the files under `nodes/` — and reaches no file the workflow ships and no product code the effort changes;
>    b. within those files it reaches text whose job is to record what happened — a node's `## Answer`, a line in
>       `decisions.md`, an entry in `flags.md` — which is marked superseded in place and never removed;
>    c. text whose job is to state a rule that currently binds is **not** struck in place: when it is superseded it
>       is **replaced** by its current form, and its existing text is appended **verbatim** to `map-history.md`
>       under the heading mirroring the section it came from, struck-through text staying struck through;
>    d. the ground for (c), quoting the human `verbatim`: *"I don't think there should a be a never delete rule on
>       the rules. They can change."*
> 2. The full text that standing preference carried before this work is appended verbatim to `map-history.md`, under
>    the heading mirroring the `map.md` section it came from.
> 3. `map-implementation-rules.md` states in its own text that a superseded rule in that file is replaced by its
>    current form and its superseded text appended verbatim to `map-history.md`, so a reader of that file who has
>    not read `map.md` can edit it correctly.
> 4. No numbered rule in `map-implementation-rules.md`'s two blocks — the five ground rules, and the four standing
>    rules for writing — is reworded, renumbered or reordered.
> 5. No text already present in `map-history.md` is altered or removed.
> 6. Every markdown link in the two edited files resolves to a path that exists.
> 7. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**Its author split this from its sibling deliberately**, in its words: *"The map statement and the shipped statement
are separate because they have different readers, different files and different blockers — the shipped one cannot
start yet and the map one should not wait for it."* The shipped half is [node
194](194-ship-where-the-never-delete-rule-stops.md).

**This node's own condition is the first written under the rule it states.** Clause 1 replaces a standing
preference rather than striking it, and clause 2 sends the old text to `map-history.md` — which is the procedure
`map.md` has always used and which node 189 established was never carried into its siblings.
