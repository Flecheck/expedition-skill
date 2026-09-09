# Write the derivations this effort has been deriving by hand

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [Nothing measures the record about itself](183-nothing-measures-the-record-about-itself.md)'s
worker, and pasted as it wrote it.*

> Write, once, the derivations this effort has re-derived by hand across eight sessions, so
>   that no party needing a number about the record invents the command again. The fog item
>   *"Extraction of a graph tool"* in `map-manager-only.md` is specified in everything but its trigger;
>   this node is that trigger, scoped to the derivations already paid for rather than to a general tool.
>   Nothing is stored: each derivation reads the tree or its version history and returns a current value.

**Blockers, in the worker's words:** none.

## Acceptance condition

*Written by node 183's worker. Pasted as it wrote it, and not the manager's.*

  The work is one new file, `.scratch/graph-workflow/derivations.md`, and one added line in
  `.scratch/graph-workflow/map.md`.

  Done means every one of the following is true of the finished tree.

  1. `.scratch/graph-workflow/derivations.md` exists and contains, as its own named entry, each of
     these nine derivations. Every entry states in one line the question it answers, and then gives the
     means of answering it against the tree at
     `.scratch/graph-workflow/`:
     (a) the byte size of any named file in that directory at any past date;
     (b) the count of node files over time;
     (c) the current count of node files by `Status:` value;
     (d) the current count of node files by `Type:` value;
     (e) the list of nodes whose status is `open` or `claimed`, by file name;
     (f) the count of entries in `flags.md` by checked and unchecked state;
     (g) the total byte size of struck-through text across the directory, and its share of the whole;
     (h) the byte size of each item under `## Notes` in `map.md`, with the items exceeding 500 bytes
         listed, counting each item's own prose and not any quotation of the human's own words;
     (i) the total and mean byte size of the node files.
  2. Entries (c), (d) and (h) each state, in their own text, that a node file's fields are read only
     from the header block above the first `##` heading and that fenced code blocks are skipped, and
     each is written so that it obeys this. A scan that counts a `Status:` or `Type:` line appearing in
     a node's prose body fails this clause.
  3. Each of the nine, run against the tree as the file gives it, returns a value equal to the value
     obtained by measuring the tree directly for that same quantity at the same moment. **No expected
     numeric result is written in the file for any of the nine**, and the file contains no table,
     series or list of recorded measurements.
  4. `derivations.md` states, in its own voice, that it holds no numbers, that a value is obtained by
     running a derivation at the moment the value is wanted, and that a number found written elsewhere
     in the record is a historical statement rather than the current state.
  5. `derivations.md` is not presented as one of the graph's files: it is not added to the list of files
     in the sentence beginning *"The graph is"* in `.scratch/graph-workflow/map.md`, that sentence's
     stated count is left unchanged, and no file under `.claude/` is modified.
  6. `.scratch/graph-workflow/map.md` gains exactly one new line, under `## Notes`, which names
     `derivations.md` by path, says in one sentence that a fact about the record is derived rather than
     stored, and says that a number a worker receives from anywhere is to be re-derived before it is
     relied on. Nothing else in `map.md` changes.
  7. Nothing under `.scratch/graph-workflow/nodes/`, and no other file in
     `.scratch/graph-workflow/`, is modified.
  8. The tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is the trigger the fog item was waiting for**, and the manager records that the narrowing came from the
worker rather than from the human's `ok`: the fog asked for *"extraction of a graph tool"*, and what is minted is
the derivations already paid for by hand. `map-manager-only.md`'s fog item has been narrowed to match in the same
turn.

**Its clause 5 keeps a shipped file out of this effort's practice.** `map.md` says *"The graph is seven files"* and
the shipped `graph-conventions.md` heads a section *"## The seven files"*, so an eighth graph file would drag a
shipped file's structure behind an artifact binding this effort alone — the coupling flag `140.4` recorded and
nothing enforces. That is flag `183.4`, and the manager notes the human may still read a new file in the effort's
directory as an eighth file whatever it is called.
