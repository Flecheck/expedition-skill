# Ship where the never-delete rule stops, in the conventions document

Type: implementation
Status: open

Blocked by: 142

## Question

*Surfaced by [Where the never-delete rule stops](189-where-the-never-delete-rule-stops.md)'s worker, and pasted as
it wrote it.*

> The shipped `graph-conventions.md` states *"No edit deletes"* for every effort and scopes it correctly to graph
> files, but says nothing about the rule stopping at a rule statement, and asserts that `map.md` is *"the one file
> whose superseded text is also moved rather than left in place"* — which its siblings that state current rules now
> contradict. Carry both boundaries into the shipped statement.

**Blockers, in the worker's words:** *"142."*

**Its sequencing note, in the same worker's words and marked by it as not part of the condition:**

> node 142 is claimed and running on this file under a condition forbidding changes beyond its own five clauses, and
> nodes 146 and 153 are also open on it. This node runs after 142 lands, and the manager sequences it against 146
> and 153 rather than running them in parallel worktrees over one file.

## Acceptance condition

*Written by node 189's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. The worker may not
> mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. This is a file the workflow ships, so
> it is edited plainly: superseded wording is removed rather than struck, and nothing is moved to any history file.
>
> Done means all of the following are true of the finished tree.
>
> 1. The paragraph beginning `**No edit deletes.**` states in its own text that the rule reaches the graph's own
>    files and nothing outside them — neither the product the effort changes nor any file the effort ships.
> 2. That paragraph, or one adjacent to it under the same heading, states that within the graph's files the rule
>    distinguishes two kinds of text: text that records what happened — a node's `## Answer`, a line in
>    `decisions.md`, an entry in `flags.md` — is marked superseded in place and never removed; and text whose job is
>    to state a rule that currently binds is instead replaced by its current form, its superseded text appended
>    verbatim to `map-history.md`.
> 3. The sentence `**map.md** is the one file whose superseded text is also *moved* rather than left in place` no
>    longer claims `map.md` is the only such file, and the `## Writing the map` section and the `### Change the map`
>    procedure both apply to `map.md` and to those of its siblings that state current rules, rather than to `map.md`
>    alone.
> 4. No procedure in the file other than `### Change the map` is reworded, and the numbered list under
>    `## Mechanical checks` is unchanged in content, count and order.
> 5. Every markdown link in the file resolves to a path that exists.
> 6. No file outside `.claude/skills/expedition/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**This is the node that carries the human's `Q3` answer**, given at node 189's interview against that node's
worker's own recommendation and against `map.md`'s standing default that a rule reaches a shipped file only where
they say so. Their word, `verbatim`: *"Q1 ok Q2 ok Q3 ok"*.

**Its clause 3 repairs what node 189 reported as an invalidation** of [node
64](64-conventions-say-how-the-map-is-written.md) — the shipped claim that `map.md` is the one file whose superseded
text moves, true when the graph had five files and false since node 140 created two siblings that hold rules.

**The manager has added the `Blocked by: 142` edge**, which the worker named in its own text as a blocker and as a
sequencing note. Nodes 146 and 153 are also open on that file and hold no edge to this one; the manager sequences
them rather than running them together.
