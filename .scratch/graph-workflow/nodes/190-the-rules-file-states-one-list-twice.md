# The rules file states one list of standards twice

Type: implementation
Status: open

Blocked by: 184, 348, 349, 352, 354

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

## The manager's note, 2026-09-23

*The manager's own note, not an amendment.* This node's `## Acceptance condition` quotes the words "four standing rules for writing". Since [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md), `map-implementation-rules.md` holds five standing rules for writing and says "five" where it said "four". Found by the manager's search of the open conditions for "four standing rules". The clause must be re-pointed before this node is claimed.

## Amendment, 2026-09-27 (from node 168)

*Written by [node 168](168-where-a-non-implementation-worker-gets-the-ground-rules.md)'s worker under its `CONDITIONS`, and filed by the manager. The heading it quotes, "**Five standing rules for writing anything in this effort**", is in the tree (node 289). The clause becomes binding once [node 348](348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md) moves the ground-rules block out of this file; this node is not to be claimed before 348 lands.*

- **Clause 4.** Read: "4. No numbered rule in the file's block of five standing rules for writing is reworded, renumbered or reordered."

## Amendment, 2026-09-27 (from node 348)

*Written by [node 348](348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it.*

- **Clause 1.** Replacement for its clause 1 phrase "this effort's ground rules and its four standing rules for writing":
  "this effort's ground rules, stated as held in `map.md`'s `## Notes` and received by a checker as text in its spawn; this effort's five standing rules for writing, stated as held in this file"
  Its words are fixed by node 289 (resolved; "five", with the heading "Five standing rules for writing anything in this effort" in the tree) and by this node's work once landed ("held in `map.md`'s `## Notes`", "a checker receives as text in its spawn", now in `map-implementation-rules.md` and `map.md`). Without it, node 190's merge of the two lists could drop what clause 6 here put in.

## Amendment, 2026-09-27 (from node 349)

*Written by [node 349](349-whether-the-five-standing-rules-for-writing-reach-other-workers.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it. It replaces clause 1's phrase as amended by node 348, and clause 4 as amended by node 168.*

- Node 190 (open, unclaimed). Clause 1, as amended by node 348, contains the phrase "this effort's five standing rules for writing, stated as held in this file". Replacement: "this effort's five standing rules for writing, stated as held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn". Clause 4, as amended by node 168, reads "No numbered rule in the file's block of five standing rules for writing is reworded, renumbered or reordered". Replacement: "4. The file states neither the five ground rules nor the five standing rules for writing as a numbered list. Where it names them, it names `map.md`'s `## Notes` as holding them." Both replacements are fixed by this node, once resolved, and by the new implementation node above, once landed. Node 190 must not be claimed before that node lands.

## Amendment, 2026-09-27 (from node 56)

*Written by [node 56](56-ship-the-glossary-into-the-skill-set.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it.*

- Node 190 (open, unclaimed): clause 1 "`CONTEXT.md`'s `_Avoid_` lines" should read "`.claude/skills/expedition/glossary.md`'s `_Avoid_` lines". Clause 2 "that `CONTEXT.md`'s refused words return false positives" should read "that `.claude/skills/expedition/glossary.md`'s refused words return false positives". The path is fixed by this node's work in the tree, the human's 2026-09-25 choice of name.

## Flags

`190.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 168's replacement for clause 4 was filed on this open, unclaimed node, and the node was made to wait on node 348.

`190.2` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 348 above.* Node 348's replacement for clause 1 was filed on this open, unclaimed node without asking the human first.

*The manager's note, 2026-09-27:* edge to [node 349](349-whether-the-five-standing-rules-for-writing-reach-other-workers.md) added. Node 349's worker found that clause 4, and node 348's amendment to clause 1, both assume the five standing rules for writing stay in the rules file. Node 349's question is whether they move, so this node waits on it.

`190.3` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 349 above.* Node 349's replacements for clauses 1 and 4 were filed on this open, unclaimed node without asking the human first, and the node was made to wait on [node 352](352-move-the-five-standing-rules-for-writing-into-the-ground-rules-block.md).

`190.4` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 56 above.* Node 56's replacement naming `.claude/skills/expedition/glossary.md` in place of `CONTEXT.md` was filed on this open, unclaimed node without asking the human first.

*The manager's note, 2026-09-27:* edge to [node 354](354-add-the-sixth-standing-rule-for-writing.md) added. [Node 253](253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)'s worker reports that once node 354 lands, the "five standing rules for writing" in clause 1 (as amended by node 348) and clause 4 becomes wrong, and that the replacement is owed then, since "six" is fixed by no landed work yet.
