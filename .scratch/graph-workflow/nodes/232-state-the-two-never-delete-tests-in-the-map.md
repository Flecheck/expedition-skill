# State the two never-delete tests, and the acceptance condition's place, in this effort's map

Type: implementation
Status: open

Blocked by: none

## Question

*Specified by [node 199](199-is-an-acceptance-condition-a-rule-or-a-record.md)'s worker after the human answered
all four of its questions, and pasted as that worker wrote it.*

> `map.md`'s never-delete preference states one test and one destination, and says nothing about an acceptance
> condition. Carry in the two-test structure, the node-file archive property, and the marking rule.

**Blockers, in the worker's words:** *"none."*

**Its author on why this is two nodes rather than one**, pasted: *"Same split node 189's answer took a week ago —
node 193 for `map.md`, node 194 for the shipped `graph-conventions.md` — on the same ground: different files,
different readers, and the shipped one carries a contradiction to dispose of while the map one is an append.
Neither blocks the other; they touch disjoint files and the manager may run them together."*

## Acceptance condition

*Written by node 199's worker. Pasted as it wrote it, and not the manager's.*

> The work is `map.md` and `map-history.md` under `.scratch/graph-workflow/`, and no other file may be edited. The
> worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`, and may not edit any
> clause of any node's acceptance condition.
>
> `map.md`'s standing preference beginning `**An in-place update never deletes.**` states a rule that currently
> binds, so it is changed by **replacement**: its superseded wording is removed from `map.md` and appended
> **verbatim** to `map-history.md` under a heading mirroring `## Notes`, struck-through text staying struck through.
> `map-history.md` is appended to and never rewritten. This is why both files are in scope.
>
> Done means all of the following are true of the finished tree.
>
> 1. That preference states this test in these words: *"text is rule-stating if an agent could act differently
>    because of it today; it is record-stating if it only tells you what was already decided or done."*
> 2. It states that deciding a text is rule-stating settles that a superseded version of it must never be left
>    readable as though it still binds, and does not by itself settle where the superseded text goes.
> 3. It states that where superseded text goes is settled by a second question — whether the file holding it already
>    archives its own subject. It names the node files under `nodes/` as files that do, on the ground that a node
>    file already holds every superseded thing about its one node and is the only place that node's history is
>    looked for; and it names `map.md` and every sibling of it that states rules that currently bind as files that
>    do not.
> 4. It states that an implementation node's acceptance condition is rule-stating while its node is live, and that a
>    superseded clause of one is therefore marked superseded in place inside the node file, never removed from it,
>    and never appended to `map-history.md`.
> 5. It states that such a clause is marked **where the clause itself stands**, so a reader of the condition alone
>    sees which clauses bind, and that recording the change only elsewhere in the node file does not satisfy this.
> 6. Nothing the work adds states that a superseded rule statement in `map.md`, or in a sibling of it that states
>    rules that currently bind, is marked in place rather than replaced.
> 7. `map-history.md` holds the preference's superseded wording verbatim, and no text was removed from
>    `map-history.md`.
> 8. The work adds no markdown link whose path does not exist.
> 9. No file outside `.scratch/graph-workflow/` is modified, and within it only `map.md` and `map-history.md`.

## The manager's note at filing

*Not a change to anything above.*

**Its clause 6 is the one that looks like belt-and-braces and is not.** The answer this node carries says a
condition is *rule-stating* and yet *marked in place* — which is exactly the pair a reader could over-generalise
into "rule statements are marked in place", reversing the rule for `map.md` itself. Clause 6 forbids the work from
saying that.

**Flag `199.1` bears on whoever claims this**, and its author said so: the two-test structure is the worker's own
composition from two separately approved answers, and *"whoever carries this into `graph-conventions.md` writes
that structure, so it is worth their eye before it ships."* That applies to this node too.
