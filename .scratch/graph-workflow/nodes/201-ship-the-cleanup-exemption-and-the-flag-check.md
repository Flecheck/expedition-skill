# Ship the cleanup exemption and the flag check into the conventions document

Type: implementation
Status: open

Blocked by: none — [node 194](194-ship-where-the-never-delete-rule-stops.md) landed as `02f9e38`

## Question

*Surfaced by [Pruning a long-running effort's map](70-pruning-a-long-running-map.md)'s worker, and pasted as it
wrote it.*

> `graph-conventions.md` states *"No edit deletes"* for every effort and says nothing about an invoked act whose
> declared purpose is removal — which the human has now approved and directed to ship. Its mechanical check joining
> a node's flag entry to the flag index also has to tolerate a settled line that a cleanup has removed. Carry both.

**Blockers, in the worker's words:** *"194 — it rewords the same `**No edit deletes.**` paragraph, and node 194 is
claimed under a condition freezing the mechanical-check list, so these cannot run together."* **That blocker is
discharged**; node 194 landed while this node was being filed.

## Acceptance condition

*Written by node 70's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. This is a file the
> workflow ships, so it is edited plainly: superseded wording is removed rather than struck, and nothing is moved to
> any history file. The worker may not mark this node, resolve it, or write a line in any index file.
>
> Done means all of the following are true of the finished tree.
>
> 1. The paragraph stating that no edit to a graph file deletes also states, in its own text, that the rule does not
>    reach removal performed by an act that is invoked and whose declared purpose is removal — and gives the reason
>    as a property: the rule guards against deletion that is unannounced, and being invoked for that purpose is the
>    announcement.
> 2. That statement says what such an act leaves behind in place of what it removed: an entry naming what was
>    removed and recording that the text remains recoverable from the effort's version control history. It states
>    this as a property and names no command and no tool.
> 3. The numbered mechanical check requiring that every flag entry on a node has a corresponding line in the
>    effort's flag index states that a settled flag whose index line has been removed is not a mismatch, and that an
>    outstanding flag missing its index line still is one.
> 4. No numbered mechanical check other than the one in clause 3 changes in content, and the list's count and order
>    are unchanged.
> 5. No procedure in the file other than the paragraph in clauses 1 and 2 is reworded.
> 6. Every markdown link in the file resolves to a path that exists.
> 7. No file outside `.claude/skills/expedition/` is modified.
> 8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is the file five nodes now queue on**, with [node 197](197-ship-what-a-file-of-the-map-admits.md) claimed
and running on it, and nodes 146, 153 and 195 open. The manager sequences them rather than parallelising worktrees
over one file; that sequencing is not an edge and none of those nodes blocks this one.

**Its clause 2 is what makes the exemption honest rather than a hole.** A removal that leaves an entry naming what
went and where it is recoverable from is the *announcement* the never-delete rule's own harm clause is about —
*"Quiet deletion is most damaging and least visible"*. The human put it as a property of the act rather than of the
text: *"For the cleanup skill, it is designed to delete things so it should be fine."*
