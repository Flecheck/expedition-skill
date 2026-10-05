# Repoint the map's `## Notes` skill line when its two replacements land

Type: precondition
Status: resolved

Blocked by: 126, 383

## Answer

`map.md`'s consult-skills line now names `/repo-docs` in place of `/domain-modeling` and points at the grilling contract's `## How you grill` in place of `/grilling`; old line in map-history.md.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced no node. Its `MISSING FROM MAP` names two gaps: the map does not say where graph-conventions.md lives, and nothing states the shape of a map-history.md entry. Flags 135.1 settle at the node closing report.

## Question

*Surfaced by [Whether the contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md)'s worker, and pasted as it wrote it.*

> `map.md`'s `## Notes` names `/grilling` and `/domain-modeling` as skills every session should consult. That is
> correct today and stops being correct once node 126 has landed the batching rules into the grilling contract and
> node 130 has shipped the docs discipline replacing `/domain-modeling`. Repoint those two entries at the shipped
> text then.

**Blockers, in the worker's words:** *"nodes 126 and 130."*

**Why it is a node, in the worker's words:** *"nothing else watches this, and the human's assent kept the `## Notes`
clause deliberately."*

## What must be true when it is done

*Written by the manager, and marked as the manager's, because a precondition node's spawn owes this and the surfacing
worker stated the trigger rather than the outcome.*

- `map.md`'s `## Notes` no longer points a worker at `/grilling` or `/domain-modeling` for a discipline that by then
  lives in a shipped file, and points at the shipped text instead.
- The other four names on that line are untouched unless something has replaced them too.
- **What later nodes depend on:** nothing depends on this node's result. It exists so that a correct line does not
  silently become wrong; it unblocks no other node.

## The manager's note at filing

*Not a change to anything above.*

**This is the first node on this graph minted against an expiry rather than a defect.** The line it repairs is
**correct today**, and node 113's worker was explicit that this is *"a cascade obligation on two open nodes, not a
defect in what was decided here."* Whether the graph should hold nodes of this shape — work whose premise does not
yet exist — is not settled anywhere, and the manager has not raised it.

*The manager's note, 2026-10-04:* the edge on node 130 was moved to [node 383](383-ship-the-repo-docs-skill.md), which ships `/repo-docs`. Node 130's worker reported under its `CONDITIONS` that this node's trigger is now that node's landing, not node 130's resolution. Node 130 named `/repo-docs` as the text that replaces `/domain-modeling`.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Repoint the map's `## Notes` skill line when its two replacements land
ANSWER:        `map.md`'s `## Notes` line beginning `**Skills every session should consult:**` was replaced under graph-conventions.md's `### Change the map`, in the worktree `.scratch/graph-workflow/worktrees/135-skill-line`, and left uncommitted. Two files changed: `.scratch/graph-workflow/map.md` (the one line) and `.scratch/graph-workflow/map-history.md` (an appended entry).

Before starting, both blockers were checked against the tree at 3706023f3:
- Node 126 is resolved. `.claude/skills/expedition-grilling/SKILL.md` states the batching rules under `## How you grill`: one payload may carry any number of questions, two share a payload only when neither's answer depends on the other's, and each question carries its own recommendation. The word "batch" does not appear in that file.
- Node 383 is resolved, landed as `ffbd4b07b`, and `.claude/skills/repo-docs/SKILL.md` exists.

The new line:
- names `/repo-docs` "by default" in the place `/domain-modeling` held, and links `.claude/skills/repo-docs/SKILL.md`, citing nodes 130 and 383;
- removes `/grilling` from the list of skills to consult. In its place it states that the grilling discipline is `## How you grill` in `.claude/skills/expedition-grilling/SKILL.md`, citing nodes 113 and 126;
- leaves `/naming`, `/coding-principles`, `/prototype` and the glossary sentence byte-unchanged.

The superseded line is appended verbatim to `map-history.md` under `## Superseded from `map.md`'s `## Notes` at node 135 — the skills line naming `/grilling` and `/domain-modeling``, with an italic account.

Checks run by the worker:
- Check 11 passes. The pre-change `map-history.md` is a byte-exact prefix of the new one (cmp), and the removed line appears byte-identically in the appended text (grep -xF).
- Check 4 does not apply, since no `Labels:` line was touched.
- Check 10 reports, without failing, that the item is now 1,044 bytes. It was 527 bytes before, already over the 500-byte target. The increase comes from the four node links and two file links. Sizes measured 2026-10-05; for scale only, re-derive.
- Every link target in the new line exists.

`/prototype` is still a `mattpocock-skills` plugin skill. Nothing has replaced it, so it stays.
INDEX LINE:    `map.md`'s consult-skills line now names `/repo-docs` in place of `/domain-modeling` and points at the grilling contract's `## How you grill` in place of `/grilling`; old line in map-history.md.
FLAGS:         ASSUMPTION — The node said to "point at the shipped text" but not in what form. The worker put `/repo-docs` into the consult list in `/domain-modeling`'s "by default" slot, because it is an invocable skill node 130 named as the replacement. It took `/grilling` out of the list and stated where its discipline now lives (`## How you grill` in the grilling contract) rather than listing that contract as something every session consults, because only a grilling worker reads it and that worker is already told to. The item grew to about 1,044 bytes against the 500-byte soft target (2026-10-05, for scale only). Index sentence: Node 135 slotted `/repo-docs` into `/domain-modeling`'s "by default" place in the map's consult line and replaced `/grilling` with a pointer to the grilling contract's `## How you grill`, not a list entry.
NEW NODES:     none
INVALIDATIONS: Node 113 is narrowed, not contradicted. Its answer says "The skills stay named in `map.md`'s `## Notes`" and "still names the six skills", on the ground that the reconciliation clause of node 48 keeps its subject. The line now names four skills: `/repo-docs`, `/naming`, `/coding-principles` and `/prototype`. The clause still has a subject, so node 48 is not contradicted either.
CONDITIONS:    The worker searched every open or claimed node (16) for `Skills every session`, `domain-modeling` and `` `/grilling` ``, in both `## Acceptance condition` and `## Question`. There were two matches besides node 135 itself.
- Node 149 (open, unclaimed), clause 8, needs the `**The shipped files should not depend on the` bullet to stop claiming that the no-plugin direction reaches the consult-skills line. That clause is still correct and unaffected.
- Node 149, clause 9, needs the consult-skills line to be "byte-identical to what it was before this work", meaning before node 149's own work. That is still satisfiable against the new line, and no replacement is needed.
- The other match was resolved node 13, not an open node.
No open node's question is changed.
MISSING FROM MAP: The map does not say where graph-conventions.md lives. The worker found it at `.claude/skills/expedition/graph-conventions.md` with `find`. The map does not say the shape of a `map-history.md` entry either. The worker copied it from the most recent entries, those of nodes 211 and 284.

RETROSPECTIVE
(1) What I had to hunt for
- `history-entry-shape-by-example`: the shape of a map-history entry (heading, italic account, `### From *Notes*`, "Replaced, and it stood as:") is stated nowhere. I copied it from the entries of nodes 211 and 284. 1 earlier retrospective carries this name: 284.
- `nothing-pointed-me-at-it`: two things nothing pointed me to. First, the path of graph-conventions.md: the spawn named the file but not its directory, and I found it with `find`. Second, where the grilling discipline now lives: I grepped the grilling contract for "batch" first and got no hits, then found it under `## How you grill` through node 126's `## Answer`. 2 earlier retrospectives carry this name: 178, 385.
(2) What arrived that this node did not need
- `map-read-whole-for-a-few-items`: of `map.md` I used the one consult line, the never-delete bullet, the no-plugin bullet and writing rules 2 and 5. 5 earlier retrospectives carry this name: 178, 205, 220, 284, 387.
- The expedition-precondition contract's sections on raising flags and on implementation-node conditions bore on nothing here, but they are short.
(3) What would have made this node easier
- A spawn that names, for a "repoint at shipped text" node, the exact files and headings that hold the shipped text: here `.claude/skills/expedition-grilling/SKILL.md` `## How you grill` and `.claude/skills/repo-docs/SKILL.md`. It should also give graph-conventions.md by full path. Both are already part of the reported items above.
(4) What was stale, wrong or contradictory
- `count-wrong-when-written`: newly minted, 0 earlier retrospectives carry it. Two counts of the consult line were wrong when they were written. Node 135's `## What must be true` says "the other four names on that line", but the line has three other skill names (`/naming`, `/coding-principles`, `/prototype`), or four only if the glossary file is counted. Node 113's answer says `## Notes` "already lists all six" and "still names the six skills", but the line named five; `/research` was never on it.
- Node 149's acceptance condition still names absolute paths `/home/ten/Projects/expedition/...`. This is already flagged as 149.1, so it is not a new item.
`````

## Flags

`135.1` `ASSUMPTION` **· settled** — `/repo-docs` took `/domain-modeling`'s slot; `/grilling` became a pointer, not a list entry. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-05:* flags 135.1 settle at the node closing report that closes this node.
