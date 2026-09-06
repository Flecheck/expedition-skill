# The bar's project criteria and the review route's standards are still two different lists

Type: implementation
Status: open

Blocked by: 169

## Question

*Surfaced by [The rules file's bar paragraph still names the map's standing preferences as project criteria](169-rules-file-bar-paragraph-names-the-maps-standing-preferences.md)'s worker, and pasted as it wrote it.*

> `map-implementation-rules.md`'s `## What the work is held against` holds two enumerations of what work is held to,
> and after this node they still differ. The bar paragraph's non-command half reads *"the project criteria (the
> human's global coding principles and `/naming`), [the ground rules and the four standing rules], `CONTEXT.md`'s
> `_Avoid_` lines, and the node's acceptance condition"*. The review-route paragraph's **standards to hold work
> against** reads *"`/coding-principles` and `/naming`; `CONTEXT.md`'s `_Avoid_` lines; [the ground rules and the four
> standing rules]; `graph-conventions.md`; and `/writing-for-agents`"*. So `graph-conventions.md` and
> `/writing-for-agents` are in the checker's list and absent from the implementer's, and `/writing-for-agents` is the
> standard ground rule 5 says every prose deliverable on this effort is held against. The human's standing direction
> at `map.md` is that *"The rules should also be used by the implementer"* — one set of rules, not two — and node 143
> landed the implementer and the checker reading the same file for that reason. Whether the divergence is a defect or
> a deliberate split between *the bar* and *the standards* is what this node settles; I could not repair it, my
> condition's clause 3 forbidding any change to another paragraph of that file.

**Blockers, in the worker's words:** *"169."*

## Acceptance condition

*Written by node 169's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited. The worker may
> not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
> 1. The paragraph beginning `**The bar's commands for this repo, discovered on first use**` and the paragraph
>    beginning `**The review route for this repo, discovered on first use**` no longer disagree about whether
>    `graph-conventions.md` and `/writing-for-agents` are held against an implementation node's work. Either both
>    paragraphs name them, or one paragraph states in its own text that it enumerates something different from the
>    other and says what — for instance that the bar's project criteria are a subset, and which reader each
>    enumeration is for.
> 2. Nothing is deleted: any superseded wording remains in the file, marked struck, and the replacement is added
>    around it.
> 3. No numbered rule in the file's two blocks — the five ground rules, and the four standing rules for writing — is
>    reworded, renumbered or reordered.
> 4. Every markdown link in the file resolves to a path that exists.
> 5. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**Its author found this while forbidden to fix it**, by the same clause that produced this node's own parent: node
144's condition stopped its worker touching the bar paragraph, which became node 169; node 169's condition stops its
worker touching the review-route paragraph, which becomes this. **Three nodes in a chain, each created by the
condition of the last.** The manager records the shape and takes no view on whether the conditions were wrong to be
narrow.
