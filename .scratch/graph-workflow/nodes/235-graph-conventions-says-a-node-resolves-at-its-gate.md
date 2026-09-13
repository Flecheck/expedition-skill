# `graph-conventions.md` says a node resolves at its gate, and it does not

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 216](216-what-a-correction-round-after-a-rebase-conflict-owes.md)'s worker, and pasted as it
wrote it.*

> `.claude/skills/expedition/graph-conventions.md`, on when an owed `NOT COVERED` part is established, says it
> happens *"by the gate at the latest, the node resolving there with nothing after it to establish anything."* The
> node does not resolve there: the landing policy resolves it after the commit, rebase, bar re-run and merge, and
> node 68 already named the consequence — *"the human's approval is no longer the last thing that can fail."* This
> node's answer widens the gap, a second approval now being reachable after the first. **The false clause is the
> reason given for a rule, so a reader who checks the reason finds it does not hold.**

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 216's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`. The worker may edit that file and no other; it may
> not mark this node, resolve it, or write a line in `.scratch/graph-workflow/decisions.md` or
> `.scratch/graph-workflow/flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The clause asserting that the node resolves at its gate, with nothing after it able to establish anything, no
>    longer appears in the file. The surrounding rule — that an owed `NOT COVERED` part is established by the gate
>    at the latest — is unchanged in what it demands.
> 2. Whatever reason stands in its place is true of the lifecycle the file describes: that the gate is the last
>    point at which the human can act on it, rather than the point at which the node resolves.
> 3. No other rule in the file changes what it demands, and no rule is added.
> 4. The file's existing section order and heading names are unchanged.
> 5. Every markdown link in the file resolves to a path that exists, except a link to a path outside this
>    repository, which is out of scope.
> 6. No file outside `.claude/skills/expedition/` is modified.
> 7. The standing quality bar for this repository holds of the finished tree.

## The manager's note at filing

*Not a change to anything above.*

**Two `NOT COVERED` parts were settled after their gate on this effort today**, which is the clause's falsity
demonstrated rather than argued: node 198's two, settled by the manager at its landing, and node 229's one, settled
by the manager at its gate. In all three the establishing happened at or after the moment the clause says nothing
can follow.

**Four open nodes now edit `graph-conventions.md`** — this one, [node
222](222-the-conventions-file-says-a-worker-reads-the-whole-map.md), [node
228](228-graph-conventions-says-map-notes-holds-three-things-kept-elsewhere.md) and [node
233](233-ship-the-two-never-delete-tests-into-the-conventions-document.md). **Two workers must not hold that file at
once.** The manager holds the sequencing and has written no blocking edge, none of the four needing what another
produces.
