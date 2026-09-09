# Replace the mint-on-second-report rule in the map's retrospective item

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [The rule that mints a node on a repeated retrospective item has been defeated by its own
test](212-the-mint-on-second-report-rule-is-defeated.md)'s worker, and pasted as it wrote it.*

> The map's retrospective bullet carries three statements this node replaces: that the worker's
>            retrospective names no standing item, that the manager mints a node on the second report of the same
>            standing item, and that the retrospective is filed as an annotation after the node resolves. All
>            three are one bullet and one coherent statement, so they are one edit rather than three — three
>            nodes editing one bullet is node 115's two-writers collision. Nothing ships: the retrospective
>            appears in no file under `.claude/`.

**Blockers, in the worker's words:** none

## Acceptance condition

*Written by node 212's worker. Pasted as it wrote it, and not the manager's.*

> The work is edits to two files, `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-history.md`.
> Nothing else changes.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `.scratch/graph-workflow/map.md`, under `## Notes`, the bullet beginning **"Every worker returns a
>    retrospective as the last handover part, on this effort only"** states all four of the following, and every
>    statement that bullet previously carried which contradicts them is no longer in it:
>
>    (a) **The worker names the item.** For each standing item its retrospective reports, the worker gives that
>        item a short name; it reuses a name an earlier retrospective already carries where one fits and mints a
>        new one where none does; and it states how many earlier retrospectives carry that name, listing the node
>        ids. The bullet says the worker finds the existing names by searching the retrospective sections of the
>        files under `.scratch/graph-workflow/nodes/`, and not from memory or from any list held elsewhere.
>
>    (b) **The word is "name".** That field is called a name throughout the bullet, and the bullet does not call
>        it a label.
>
>    (c) **A count ranks and mints nothing.** The bullet states that a repeated standing item is not minted as a
>        node on reaching any count; that the count ranks that item among what the manager picks next, so
>        repetition orders work rather than triggering it; and that the manager's separate duty to dispose of each
>        item naming the record in the report closing that node — by acting on it, minting a node, or saying why
>        not — is unchanged.
>
>    (d) **Filing is part of resolving.** The bullet states that the worker hands the retrospective back as text
>        and the manager writes it into the node file in the same edit that writes that node's answer, its flags
>        and its line in `decisions.md`, rather than as a later separate act; that it is written last in the file
>        so the mandatory section order is untouched; and that it is written under the heading `## Retrospective`
>        and under no other heading.
>
> 2. Every statement clause 1 replaced is appended verbatim to `.scratch/graph-workflow/map-history.md`, under a
>    heading naming the section of `map.md` it came from, with any struck-through text left struck through.
>    Nothing already in `map-history.md` is changed, reordered or removed.
>
> 3. That bullet still carries, unchanged and character-for-character, the human's quoted instruction beginning
>    **"Could you, for this effort only, ask subagents"**, and the four retrospective questions numbered (1)
>    through (4). Clause 1(a) is stated as a duty covering all four and adds no fifth question.
>
> 4. No file under `.claude/` is modified, and no file in `.scratch/graph-workflow/` other than `map.md` and
>    `map-history.md` is modified.
>
> 5. The tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Three statements, one bullet, one node — and its author gave the reason in the effort's own vocabulary:** *"three
nodes editing one bullet is node 115's two-writers collision."*

**Its clause 3 protects the human's own words** — the quoted instruction that created the retrospective, and the
four questions — character-for-character, and forbids a fifth question. What changes is what the manager does with
the answers, not what a worker is asked.
