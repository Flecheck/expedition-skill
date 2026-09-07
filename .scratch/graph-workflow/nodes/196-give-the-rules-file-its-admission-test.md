# Give `map-implementation-rules.md` its admission test

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [`map-implementation-rules.md` carries accounts of what happened, not only the rules its title
names](191-the-rules-file-carries-accounts-rather-than-rules.md)'s worker, and pasted as it wrote it.*

> The file has no test for what it admits, so accounts of what happened accumulate in it beside the rules its title
> names — the human's own words on reading it: *"I am confused, why is there in map implementation rules stuff that
> are not rules?"*. Node 191 settled the test and the clause that makes it applicable. Write both into the file's
> opening, and apply them to nothing.

**Blockers, in the worker's words:** *"none."*

**Its sequencing note, in the same worker's words and marked by it as not an edge:**

> six nodes are open or claimed on this file (149, 160, 184, 186, 188, 190) and the manager picks nodes whose paths
> are disjoint, so this must not hold a worktree over that file concurrently with another. It touches only the
> file's opening, which no queued node's condition reaches.

## Acceptance condition

*Written by node 191's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited. The worker may
> not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
>
> 1. That file's opening — the text before its first `##` heading — carries a statement, under a bold lead-in of its
>    own, of what the file admits. That statement says all three of these in its own text: (a) a line belongs in the
>    file only where an implementation node's worker or its checker would do something differently for having read
>    it while working a node; (b) how a rule was learned is not that, naming at least attempt counts, what a run
>    cost, who was wrong, what the file said before, and a manager correcting itself; and (c) such material belongs
>    in `map-history.md`, the markdown link the line already carries to the node that shaped it standing in its
>    place.
> 2. The same statement carries, in its own text, the distinction that decides the hard case: a **trigger** is part
>    of a rule and stays, a **history** is not — a trigger being an error string, a symptom, or the condition under
>    which a rule fires, which is how the rule's reader knows it applies.
> 3. The same statement says who applies the test: whoever is already editing a passage applies it to that passage,
>    and no sweep of the file is owed or licensed by it.
> 4. That statement is at most 1,000 bytes.
> 5. **This node writes the test and applies it to nothing.** Every paragraph of the file under `## Landing an
>    implementation node's work` and under `## What the work is held against`, and both blocks of numbered rules —
>    the five ground rules and the four standing rules for writing — are byte-identical to what they were in the
>    worker's tree before this work.
> 6. The new statement does not contradict the file's existing statement that the account behind a line in it is in
>    `map-history.md`.
> 7. This work supersedes nothing: no text is removed from the file, and no strike markers are added.
> 8. Every markdown link in the file resolves to a path that exists.
> 9. No file outside `.scratch/graph-workflow/` is modified.
> 10. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Clause 5 is what makes this node cheap and what makes it safe to run against a congested file.** It writes the
standard and repairs nothing, so it collides with no queued condition's subject; the repairs ride the nodes already
queued on the paragraphs that need them — [node 190](190-the-rules-file-states-one-list-twice.md) for the
review-route paragraph the human selected, and [node
188](188-move-the-landing-section-out-of-the-workers-file.md) for the landing section's narratives.

**Its shipped counterpart is [node 197](197-ship-what-a-file-of-the-map-admits.md)**, which the human directed in
their own words at node 191's interview and which is blocked on node 194.
