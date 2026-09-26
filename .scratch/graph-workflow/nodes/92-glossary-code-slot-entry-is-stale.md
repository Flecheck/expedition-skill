# `CONTEXT.md`'s Code slot entry contradicts the map on both of its claims

Type: implementation
Status: superseded
Superseded by: 332

## Question

*Surfaced by [Qualify the graph-file ban in the worker contracts](58-qualify-the-graph-file-ban.md)'s worker, and
pasted as it wrote it.*

> The glossary says a code slot is *"held by one worker at a time"* and that *"Occupancy is discovered from the
> working tree rather than recorded"*. Since [Run an implementation node's work in a
> worktree](68-implementation-in-a-worktree.md) the map says how many slots an effort runs is that effort's own
> setting, and that occupancy is discovered by counting the live worktrees rather than by inspecting the working tree
> — the implementation contract already carries the map's version. Found while checking `_Avoid_` lines for this
> node; unrelated to it.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 58's worker. Pasted as it wrote it, and not the manager's.*

> 1. `CONTEXT.md`'s **Code slot** entry states that how many code slots an effort runs is that effort's own setting,
>    one worker to a slot.
> 2. It states that a slot's occupancy is discovered by counting the live worktrees — one per claimed implementation
>    node — rather than by inspecting the working tree for uncommitted changes.
> 3. Its `_Avoid_` line, *"write lock, code lock — there is no lock"*, is unchanged, and no other entry in
>    `CONTEXT.md` changes its meaning.
> 4. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node contends for the code slot with two others that edit the same file** — [Bring the glossary's code-slot and
reject entries up to the worktree lifecycle](81-glossary-code-slot-and-reject.md), whose subject overlaps this one
directly, and [Bring the glossary's `Closed` entry off the rejected frequency
claim](90-glossary-closed-entry-frequency-claim.md). Whoever picks next should read node 81 first and decide whether
these two are one node: node 81 was minted before this defect was found, and its own name claims the code-slot entry.
The manager did not fold them together, because amending another worker's condition is what [How a condition's scope
is amended](82-amending-a-condition-whose-scope-was-too-narrow.md) exists to govern and it is still open.

**It was found by a worker scanning the glossary's `_Avoid_` lines for its own node**, and it is unrelated to that
node. `map.md` records that such a scan is a poor grep target — about a third of the refused words are ordinary
English — so the find was a by-product of a check the map already prices as expensive.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 332](332-repair-the-glossarys-code-slot-reject-kinds-grilling-and-closed-text.md), the merged glossary node [node 328](328-group-the-open-nodes-against-the-glossary.md)'s worker proposed, on the human's "ok". This node's demands are carried there, each tagged with this node's number; the question and acceptance condition above are superseded as a whole.
