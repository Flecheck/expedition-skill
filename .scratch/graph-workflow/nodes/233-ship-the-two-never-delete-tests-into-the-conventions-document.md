# Ship the two never-delete tests and the acceptance condition's place into the conventions document

Type: implementation
Status: open

Blocked by: none

## Question

*Specified by [node 199](199-is-an-acceptance-condition-a-rule-or-a-record.md)'s worker after the human answered
`Q3.` — that this ships — and pasted as that worker wrote it.*

> The shipped `graph-conventions.md` says the never-delete cut follows the text and then sorts the node files onto
> the record side by file, and never mentions an acceptance condition. Carry both tests, the archive property and
> the marking rule into it, and leave its two statements agreeing.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 199's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. The worker may not
> mark this node, resolve it, or write a line in `.scratch/graph-workflow/decisions.md` or
> `.scratch/graph-workflow/flags.md`. This is a file the workflow ships, so it is edited plainly: superseded wording
> is removed rather than struck, and nothing is moved to any history file.
>
> **The file today carries two statements that do not agree, and the work must leave them agreeing.** Under its
> `**No edit deletes.**` heading: *"**Inside the graph's files the rule cuts by what a piece of text is, not by
> which file holds it.**"* Under `## Writing the map`: *"The graph's remaining files record what happened and their
> superseded text stays where it is: `decisions.md`, `flags.md`, the node files, and `map-history.md`, which holds
> superseded text only."* The second sorts by file what the first says is sorted by text.
>
> Done means all of the following are true of the finished tree.
>
> 1. The file states this test in these words: *"text is rule-stating if an agent could act differently because of
>    it today; it is record-stating if it only tells you what was already decided or done."*
> 2. The file states that what a text **is** settles that a superseded version of it must never be left readable as
>    though it still binds, and that **where** the superseded text goes is a second and separate question.
> 3. The file states that where superseded text goes is settled by whether the file holding it already archives its
>    own subject: a node file does, holding every superseded thing about its one node, so its superseded text stays
>    in it; `map.md` and every sibling of it that states rules that currently bind do not, so theirs is appended
>    verbatim to `map-history.md`.
> 4. The file states that an implementation node's acceptance condition is rule-stating while its node is live, that
>    a superseded clause of one stays in the node file and is never appended to `map-history.md`, and that such a
>    clause is marked superseded **where the clause itself stands** rather than only recorded elsewhere in the node
>    file — giving as the reason that the checker is handed the condition as text and does not read the node.
> 5. The two statements quoted in the scope paragraph above no longer disagree: whichever wording survives, the file
>    does not both say the cut follows the text and sort the node files onto the record side by their being node
>    files.
> 6. The file still describes `map-history.md` as holding superseded text only and as never being rewritten.
> 7. The `### Change the map` procedure's numbered steps are unchanged in content, count and order. The numbered
>    list under `## Mechanical checks` is unchanged in content and order, except that the work **may** add at most
>    one new item, stating that a superseded clause of an acceptance condition is marked where it stands.
> 8. The work adds no markdown link whose path does not exist.
> 9. No file outside `.claude/skills/expedition/` is modified, and within it only `graph-conventions.md`.

## The manager's note at filing

*Not a change to anything above.*

**This node and [node 232](232-state-the-two-never-delete-tests-in-the-map.md) are disjoint and may run together**,
their author having said so: different files, different readers. **Neither blocks the other and the manager has
written no edge.**

**Three other open nodes also edit `graph-conventions.md`** — [node
222](222-the-conventions-file-says-a-worker-reads-the-whole-map.md), [node
228](228-graph-conventions-says-map-notes-holds-three-things-kept-elsewhere.md) and whatever picks up node 216's
gate-resolution finding. **Two workers must not hold that file at once**, so the manager sequences them; no blocking
edge is written, neither node needing what the other produces.

**Its clause 7 is the unusual one and its author knew it**: it freezes the `### Change the map` procedure and the
mechanical-checks list, then permits exactly one new check. That is a condition anticipating that its own subject
might want a check without letting the worker decide to add several.
