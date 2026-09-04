# Make the rules file stand alone for a reader that does not read `map.md`

Type: implementation
Status: open

Blocked by: 140, 143

## Question

*Surfaced by [Where the rules a checker is held to live](138-where-the-rules-a-checker-is-held-to-live.md)'s worker,
and pasted as it wrote it.*

> The standards list names *"this map's standing preferences, ground rules and four standing rules"*, which resolve
> to nothing for a checker that reads the rules file and not the map. Two of the three can move; the third cannot and
> has been unsafe as a checker standard since node 42 fixed the test for what may reach a blind checker.

## Acceptance condition

*Written by node 138's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/`. The worker may edit `map.md` and the
> sibling file holding the implementer's and checker's rules, and no other file; it may not mark this node, resolve
> it, or write a line in `decisions.md` or `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The block beginning with the line `**Ground rules for this effort.**` and the numbered rules under it, and the
>    block beginning `**Four standing rules for writing anything in this effort**` and the numbered rules under it,
>    are in the rules file and no longer in `map.md`. Their text is byte-identical to what `map.md` held: no rule is
>    reworded, renumbered or reordered.
> 2. For each of the two, `map.md` holds a pointer of at most two lines naming the rules file and saying what it
>    holds. `map.md` restates neither block.
> 3. The sentence in the rules file naming `this map's standing preferences, ground rules and four standing rules` as
>    standards is replaced by a statement that resolves inside the rules file itself: it names the two blocks now
>    held there, and it states that the map's standing preferences as a whole are not among the standards work is
>    held against.
> 4. That statement gives the reason in one sentence: a standing preference may be an account of what happened or a
>    steer about what gets worked, and only a standing constraint true of any node's work may be held against a piece
>    of work by a reader blind to the record.
> 5. No other paragraph of the rules file changes, and no heading named `## Notes` is added to it.
> 6. Every markdown link in `map.md` and in the rules file resolves to a path that exists.
> 7. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**Its clause 1 moves the ground-rules block out of `map.md`, which [node
139](139-move-the-managers-material-out-of-the-map.md)'s clause 8 held byte-identical *inside* `map.md`, and which
[node 140](140-move-the-implementers-and-checkers-material-out-of-the-map.md)'s clause 11 holds there too.** Those
are not in conflict: each condition binds its own node's finished tree, and this node runs after both. The manager
records it because a reader meeting the three clauses together will otherwise think one contradicts another.

**Its subject is a defect that predates the split.** In its author's words, the reference to the standing preferences
*"has been wrong as a checker standard since node 42 fixed that test"*, and the move exposes it rather than creating
it. That is [flag `138.4`](138-where-the-rules-a-checker-is-held-to-live.md).

**Why it waits on [node 143](143-rules-arrive-by-the-spawn-never-by-a-search.md) as well as node 140.** Node 143
rewrites what the checker's contract says it is given; this node rewrites what the given itself contains. Doing this
first would edit a standard the contract still describes as discovered.
