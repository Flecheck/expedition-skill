# Move the manager's material out of the map, and give each item a soft size target

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [`map.md` has grown back most of what node 59's restructure
saved](136-the-map-has-grown-back-what-node-59-saved.md)'s worker, and pasted as it wrote it.*

> Carry out the part of node 136's answer that nothing else waits on — the material only the manager acts on leaves
> the file every worker reads, and the soft target lands in the shipped conventions document. 13,261 bytes of the
> 42,566 every worker pays on every node, established by eleven independent retrospectives naming these very sections
> as read-and-unused.

**Blockers, in the worker's words:** *"none. It touches `map.md`, one new sibling, and `graph-conventions.md`, and no
worker contract, so it contends with no other node for the code slot on those files."*

## Acceptance condition

*Written by node 136's worker. Pasted as it wrote it, and not the manager's.*

> The work is the directory `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/` and the file
> `/home/mathieu/projects/graph-agent/.claude/skills/expedition/graph-conventions.md`. Editing `map.md` is what this
> node is for: its subject is the map itself rather than a report of progress on other work. The worker may edit the
> files named here; it may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> The before-state is the working tree at claim time and is recoverable with `git diff`. For scale only, and not to
> be relied on: when this condition was written `map.md` was 42,566 bytes across 107 lines and held five `##`
> headings — `## Destination`, `## Notes`, `## Decisions so far`, `## Not yet specified`, `## Out of scope`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. `map.md`'s opening sentence says that every worker reads the whole file cold once per node, and that it
>    therefore holds only what **every** worker can act on. The word *every* qualifies *worker* in the second half of
>    that claim.
> 2. A new file sits beside `map.md` in the same directory, holding material only the manager acts on. Its own first
>    sentence names the manager as its reader and says that it is part of the map. Neither its filename nor the name
>    it gives itself contains the word `provenance`: this effort's glossary refuses that word by name.
> 3. Five bodies of material are in that new file and are no longer in `map.md`: the paragraph beginning `**The
>    review route for this repo, discovered on first use**`; the paragraph beginning `**The dogfood target is`; the
>    paragraph beginning `**Label vocabulary for this effort`; the whole `## Not yet specified` section; and the
>    whole `## Out of scope` section.
> 4. For that new file `map.md` holds a pointer of at most three lines: a markdown link to it, and one sentence
>    saying who reads it and what it holds. `map.md` restates none of the material moved.
> 5. Nothing was deleted, summarised, paraphrased or shortened by the move. For every line `map.md` loses, that
>    line's text appears in the new file or in `map-history.md`. Compare after unwrapping both sides; a difference
>    confined to a line's leading markdown (list marker, heading marks, opening emphasis) does not count.
> 6. `map.md` holds exactly these `##` headings and no other at `##` level: `## Destination`, `## Notes`, `##
>    Decisions so far`.
> 7. `map.md` is at least 12,000 bytes smaller than its before-state.
> 8. The block in `## Notes` beginning with the line `**Ground rules for this effort.**`, and the five numbered rules
>    under it, are byte-identical to their before-state. That block is copied verbatim into other agents'
>    instructions, so it may not be reworded, renumbered or reordered.
> 9. `graph-conventions.md`'s `## Writing the map` section states a **target** of 500 bytes for each item in the
>    map's `## Notes`, excluding any quotation of the human's own words, and says in its own voice that this is a
>    target the writer aims at and never a rule that forces text out — an item that needs more exceeds it and says
>    why. Nothing in the file makes exceeding it a failure of anything.
> 10. `graph-conventions.md`'s numbered `## Mechanical checks` list gains one check that reports every item in the
>     map's `## Notes` exceeding that target, and that check's own text says it reports and never fails.
> 11. `graph-conventions.md` names the correct number of files where it lists the graph's files, and describes the
>     new file's role in one sentence. It changes in no respect other than clauses 9, 10 and this one.
> 12. No file under any of `/home/mathieu/projects/graph-agent/.claude/skills/expedition-checker/`,
>     `.../expedition-grilling/`, `.../expedition-implementation/`, `.../expedition-precondition/`,
>     `.../expedition-prototype/`, `.../expedition-research/` is modified.
> 13. Every markdown link in `map.md` and in the new file resolves to a path that exists.

## The manager's note at filing

*Not a change to anything above.*

**This is the first implementation node on this graph whose product is a graph file rather than a shipped file**, and
its condition says so in its own first paragraph. Two consequences the manager holds and has not resolved: the
**landing policy** — a worktree, a path-limited commit, a gate — is written for `.claude/` work and this node's paths
are `.scratch/`, which the manager has been committing separately all along; and the **never-delete rule** governs
`map.md`, which is why clause 5 demands that every lost line reappear in the sibling or in `map-history.md` rather
than allowing a trim.

**The condition forbids its worker to mark the node, resolve it, or write in `decisions.md` or `flags.md`.** That is
the write rules restated by a worker inside a condition, which no condition on this graph has done before. It is
correct, and it is recorded here because it is unusual rather than because it is wrong.

**Clause 7 is a byte threshold, which is a mechanical check the manager could not have written**: [node
94](94-condition-scope-as-a-predicate.md)'s rungs ask for an enumerator, and a size floor is one that needs no
domain.
