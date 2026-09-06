# Move the landing section out of the file an implementation worker reads

Type: implementation
Status: open

Blocked by: none

## Question

*Minted by the manager under the map's rule that a standing retrospective item reported a second time becomes a node.
**This is its sixth report**, and the manager missed the first five.*

`map-implementation-rules.md`'s opening paragraph declares its readers to be **an implementation node's worker and its
checker**, and says it exists so that *"no other worker pays to read it"*. Roughly 125 of its ~185 lines are
`## Landing an implementation node's work` — worktree creation, base checks, rebase forensics, sandbox mounts, merge
and cleanup. **None of it is anything a worker or a checker does.** It is the manager's lifecycle material, and
[node 139](139-move-the-managers-material-out-of-the-map.md) built `map-manager-only.md` for exactly this class.

**The reports, all in workers' own words:**

- [node 144](144-make-the-rules-file-stand-alone.md): *"it is the manager's material sitting in the worker's file, and
  it survived node 140's move because node 140 moved by source rather than by reader."*
- [node 163](163-a-condition-demands-facts-the-checker-does-not-read.md): *"a spawn pointer to `## What the work is
  held against` would have avoided it."*
- [node 167](167-the-checkers-bar-commands-route.md): *"Roughly sixty lines of git diagnostics bearing on nothing a
  grilling worker does."*
- [node 171](171-carry-the-record-node-reading-rule-into-the-rules-file.md): *"nothing in this file says which
  paragraphs a checker holds work against and which are the manager's lifecycle instructions."*
- [node 126](126-carry-question-batching-into-the-grilling-contract.md): *"My spawn warned me and I still took it
  whole, because `Read` on a file is whole-file: **the warning cannot fix this, and the arrangement can.**"*
- [node 177](177-carry-question-batching-into-the-glossarys-grilling-entry.md): *"on the same counting this is at
  least the fourth. The fix has not changed."*

**What is open** is only the shape of the move, the destination being named by the reports themselves.

## Acceptance condition

*The manager's own. Marked as the manager's, and read back against the two rules that bind every condition before this
node may be claimed: it is self-contained text, and it quantifies over no part of the record — every demand below
names a file, a heading or a string.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md` and
> `.scratch/graph-workflow/map-manager-only.md`. No other file may be edited. The worker may not mark this node,
> resolve it, or write a line in `decisions.md` or in `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The whole of the section headed `## Landing an implementation node's work`, from that heading to the line before
>    the next `##` heading, is in `map-manager-only.md` and no longer in `map-implementation-rules.md`. Its text is
>    byte-identical to what `map-implementation-rules.md` held: no paragraph, bullet or struck passage is reworded,
>    renumbered, reordered or unstruck.
> 2. `map-implementation-rules.md` holds, in place of that section, a pointer of at most three lines naming
>    `map-manager-only.md`, saying that it holds how an implementation node's work is landed, and saying that landing
>    is the manager's and bears on neither a worker nor a checker. It restates no part of the moved section.
> 3. `map-implementation-rules.md`'s opening paragraph states that everything remaining in the file is held against a
>    worker's work, so that a reader who has read the file has read only what binds them.
> 4. No text is deleted from either file: the moved section is deleted from its origin only in the sense that it is
>    present, byte-identical, in its destination.
> 5. Nothing under the heading `## What the work is held against` changes, and no numbered rule in either of the two
>    blocks that heading holds — the five ground rules, and the four standing rules for writing — is reworded,
>    renumbered or reordered.
> 6. Every markdown link in both files resolves to a path that exists. Links inside the moved section resolve from
>    its new location.
> 7. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**The condition above is the manager's own**, this node having been minted by the manager rather than by an agent.
What it demands is a byte-identical move plus a pointer; it decides nothing that is open, and it deliberately does
**not** say where in `map-manager-only.md` the section goes, that being the worker's to place.

**The manager's own conduct is part of the subject.** The map's rule is that the second report of a standing item
mints a node. Six reports arrived and the manager minted nothing until now, which is the same failure [node
183](183-nothing-measures-the-record-about-itself.md) records against four reports of a different item. **Two
independent standing items have now each been missed five or more times**, which is evidence about the rule rather
than about either item.
