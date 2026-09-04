# `graph-conventions.md` still says `map.md`'s `## Notes` holds the label vocabulary and the bar's commands

Type: implementation
Status: open

Blocked by: 140

## Question

*Surfaced by [Move the implementer's and checker's material out of the map](140-move-the-implementers-and-checkers-material-out-of-the-map.md)'s worker, and pasted as it wrote it.*

> `graph-conventions.md`'s `## Notes` bullet reads *"Also the two things the manager maintains here: the **declared
> label vocabulary**, and the bar's commands once they have been discovered for this repo."* The label vocabulary
> left `map.md` at node 139 and the bar's commands left at node 140, so both halves are false; the sentence describes
> the map's shape, which is the same defect class node 142 owns.

**Blockers, in the worker's words:** *"node 140 landing. **May instead be folded into node 142**, which is the same
file and already waits on node 140; it is reported separately because node 142's clauses reach headings and procedure
steps and not this bullet's description."*

## Acceptance condition

*Written by node 140's worker. Pasted as it wrote it, and not the manager's.*

> The work is the file `.claude/skills/expedition/graph-conventions.md`. Done means: no sentence in that file states
> that `map.md`'s `## Notes` holds the declared label vocabulary or the bar's commands; where the file says which
> file holds either, it names the file in `.scratch/graph-workflow/` that actually holds it at claim time; the
> bullet's remaining description of `## Notes` is otherwise unchanged; no file outside
> `.claude/skills/expedition/graph-conventions.md` is modified; and the file changes in no other respect.

## The manager's note at filing

*Not a change to anything above.*

**Its author offered a fold into [node 142](142-bring-graph-conventions-map-shape-into-line.md) and the manager has
not taken it.** Both edit one file and both wait on node 140, so they serialise on the code slot regardless; keeping
them apart costs a node file and keeps two conditions each answerable on its own. Whoever works the later of the two
should read the earlier's landed diff first.
