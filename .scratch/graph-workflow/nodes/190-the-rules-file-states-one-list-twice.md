# The rules file states one list of standards twice

Type: implementation
Status: open

Blocked by: 184

## Question

*Surfaced by [The bar's project criteria and the review route's standards are still two different lists](184-the-bar-and-the-standards-are-two-different-lists.md)'s worker, and pasted as it wrote it.*

> `map-implementation-rules.md`'s `## What the work is held against` holds two enumerations that, after node 184, name
> the same standards — the bar paragraph's non-command half and the review route's *"standards to hold work against"*.
> Two copies of one list drift, and this one has now been reconciled by hand twice: node 169 struck `map.md`'s
> standing preferences from the bar's copy, and node 184 added `graph-conventions.md` and `/writing-for-agents` to it.
> Both were repairs to a divergence that the duplication itself produced. Should the section state the standards once,
> in a block both paragraphs point at, leaving each paragraph to carry only what is particular to its own reader?

**Blockers, in the worker's words:** *"184."*

## Acceptance condition

*Written by node 184's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited. The worker may
> not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
> 1. The section `## What the work is held against` states the standards an implementation node's work is held against
>    **once**, as a single enumeration under its own bold lead-in, naming at least: the human's global coding
>    principles (`/coding-principles`) and `/naming`; `CONTEXT.md`'s `_Avoid_` lines; this effort's ground rules and
>    its four standing rules for writing; `graph-conventions.md`; and `/writing-for-agents`.
> 2. The paragraph beginning `**The bar's commands for this repo, discovered on first use**` and the paragraph
>    beginning `**The review route for this repo, discovered on first use**` each point at that single enumeration
>    rather than restating it, and each retains what is particular to its own reader — for the bar paragraph, that
>    this repo has no build, no tests, no formatter and no CI, and that the node's acceptance condition binds too; for
>    the review route, that no reviewing skill is named for this repo and that `CONTEXT.md`'s refused words return
>    false positives when used as a grep list.
> 3. ~~Nothing is deleted: every superseded enumeration remains in the file, marked struck, and the replacement is
>    added around it.~~
>
>    **Amended, and the amendment is the manager's, carrying a decision the human settled after this clause was
>    written. It is replaced rather than supplemented.** The superseded enumerations are **removed** from this file
>    and appended **verbatim** to `map-history.md` under the heading mirroring the section they came from,
>    struck-through text staying struck through; the file is left stating the current enumeration only. This is the
>    rule [node 189](189-where-the-never-delete-rule-stops.md) settled at the human's word — an enumeration of the
>    standards work is held against **is** a rule statement, and a superseded rule statement is replaced rather than
>    struck. Their words, `verbatim`: *"I don't think there should a be a never delete rule on the rules. They can
>    change."*
>
>    **Two strikes already standing in the bar paragraph are within this clause's reach**, node 158's on the ignore
>    file and node 169's on the standing preferences. Node 184's correction round was scoped away from them by the
>    manager and left them in place; under this amended clause they move.
> 4. No numbered rule in the file's two blocks — the five ground rules, and the four standing rules for writing — is
>    reworded, renumbered or reordered.
> 5. Every markdown link in the file resolves to a path that exists.
> 6. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**Its author is the node that ended the chain 144 → 169 → 184**, and it says so: its own condition fenced off no
paragraph, so it could touch both and did, and *"complying with my condition produced no fourth node of that kind"*.
**This node is therefore not a fifth link** — it is not a defect created by a narrow condition, but the duplication
that produced two of the three links in the first place.

**Five nodes now queue on `map-implementation-rules.md`** — this one, [node
186](186-an-implementation-worker-tests-its-worktree.md), [node
188](188-move-the-landing-section-out-of-the-workers-file.md), [node
149](149-state-the-prose-standards-demands-in-the-rules-file.md) and [node
160](160-carry-the-integration-conflict-rule-into-the-map.md). **Node 188 moves the section this one does not touch**,
so the two are disjoint in fact though not by any written edge. The manager holds that ordering.
