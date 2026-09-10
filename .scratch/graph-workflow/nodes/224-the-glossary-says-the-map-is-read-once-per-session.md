# The glossary's `Map` entry says the map is read once per session, where one of its files is read by no worker

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [The manager's contract defines the map as one
file](215-the-managers-contract-defines-the-map-as-one-file.md)'s worker, and pasted as it wrote it.*

> `CONTEXT.md`'s entry for **Map** reads *"The whole effort at low resolution, read once per session: the destination, the standing notes, the fog, and what is out of scope. It indexes decisions and never restates one."* The *"read once per session"* clause attaches a whole-map read to the term, and that is false of a map that is more than one file: the file holding the manager's own material is read by no worker at all, and the file holding an implementation node's rules is read only by that node's worker and its checker. This is the same defect node 215 removed from the manager's contract's `map` entry, and it survives on the very ground node 194 used to narrow the identical claim one file over — that node deliberately made *"Every worker reads `map.md` whole and cold"* precise in `graph-conventions.md` rather than widening it to *"the whole map"*, saying in its answer that *"the sibling holding the manager's material is read by no worker at all, so a widened 'the whole map' would have been false"* — and node 194 never reached `CONTEXT.md`. No open node covers this entry. The condition below deliberately scopes its arithmetic clause to counts the file states of its own contents rather than to every counted list in the file, because that is the cheap half and it is the half a glossary can get wrong; the expensive whole-file form is the standing item this node's own retrospective reports below.

**Blockers, in the worker's words:** none

## Acceptance condition

*Written by node 215's worker. Pasted as it wrote it, and not the manager's.*

> The work is one file, relative to the repository root: `CONTEXT.md`. The worker may edit that one and no other, and may not write any file under `.scratch/`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. That file's entry for the term **Map** no longer states or implies that the map is read once per session, and no longer states or implies that any reader reads the whole of it. Where the entry says what is read once per session, it says that what is read that way is a part of the map rather than the whole of it.
> 2. That entry keeps its statement of what the map is — the whole effort at low resolution, holding the destination, the standing notes, the fog, and what is out of scope — and keeps its statement that it indexes decisions and never restates one.
> 3. The entry names no particular filename. Where it says where the map's material sits, it says so by role and position only.
> 4. That entry's `_Avoid_` line is unchanged, character for character.
> 5. No entry for any term other than **Map** is added, removed or reworded, and no text outside the **Map** entry is deleted or reworded.
> 6. Any count the finished file states of its own contents — of its term entries, of its `_Avoid_` lines, or of anything else it enumerates about itself — is arithmetically correct for the finished file.
> 7. The finished file names no plugin, requires no skill to be invocable, and assumes no particular repository, machine or toolchain.
> 8. No file other than the one named above is modified, and no file under `.scratch/` is modified.
> 9. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Its author's own work is what made this reachable, and its author said why the defect survived so long.** Node
194 met the identical claim one file over and deliberately narrowed *"Every worker reads `map.md` whole and cold"*
rather than widening it to *"the whole map"* — recording that *"the sibling holding the manager's material is read by
no worker at all, so a widened 'the whole map' would have been false"* — and **node 194 never reached
`CONTEXT.md`**.

**Its clause 6 is deliberately narrower than its sibling nodes' arithmetic clauses**, and its author explained the
choice: it scopes the count check to *"counts the file states of its own contents"* rather than to every counted
list in the file, *"because that is the cheap half and it is the half a glossary can get wrong"*. **The expensive
whole-file form is the standing item its own retrospective names** — `nothing indexes counted lists`, which node
204's worker and this node's both paid for by hand.

**It is disjoint from [node 222](222-the-conventions-file-says-a-worker-reads-the-whole-map.md)**, which carries the
same defect in `graph-conventions.md`. Three files stated the map as one thing: the manager's contract, now
repaired; `CONTEXT.md`, this node; and the conventions document, node 222.
