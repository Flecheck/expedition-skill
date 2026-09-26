# The five worker contracts route a scope raise to the human where the manager may answer it

Type: implementation
Status: superseded
Superseded by: 311

Blocked by: none

## Question

*Surfaced by [node 95](95-carry-the-widening-rule-into-the-shipped-files.md)'s worker, and pasted as it wrote it.*

> Each of the five worker contracts ends its section on reporting an implementation node with *"A condition its
> worker judges wrong is not that worker's to fix: it stops that node and goes to the human, so what you write
> loosely here is paid for there."* **Re-derived on 2026-09-20**: `grep -rn "not that worker's to fix" .claude/`
> returns exactly `expedition-grilling`, `expedition-implementation`, `expedition-precondition`,
> `expedition-prototype` and `expedition-research`, and nothing else. [Node 94](94-condition-scope-as-a-predicate.md)
> reported this as node 95's scope short by five files; node 95 has resolved, so widening it is no longer available
> and the repair needs its own node. **The repair is narrower than node 94 states**: node 252 leaves the mid-node
> case exactly where that sentence puts it, so what is short is the **scope** case alone — a raise whose whole
> content is that the condition's file list is too short is answered by the manager widening it under node 82, at
> the raise, without a human turn, which is what happened at node 58's second amendment.

**Blockers, in the worker's words:** *"none. **Collides with [node 109](109-a-conditions-extent-rule.md)**, whose
clause 6 edits the same section of the same five files and whose clause 7 forbids other changes of meaning there;
the two want ordering rather than merging."*

## Acceptance condition

*Written by node 95's worker. Pasted as it wrote it, and not the manager's.*

> 1. In each of the five files `.claude/skills/expedition-grilling/SKILL.md`,
>    `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`,
>    `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-research/SKILL.md`, the sentence
>    *"A condition its worker judges wrong is not that worker's to fix: it stops that node and goes to the human, so
>    what you write loosely here is paid for there."* states in addition that where what is wrong is only that the
>    condition's list of places is shorter than the defect it describes, the manager may extend that list itself and
>    the node carries on — so the raise is still made and does not always cost a human turn.
> 2. Each file keeps its own voice and its own surrounding wording; the five are not unified onto one sentence.
> 3. Nothing else in any of the five files changes meaning. In particular each still states that the condition is
>    not its worker's to rewrite, that a worker judging it wrong raises rather than deciding, and that what the
>    reporting worker writes loosely is paid for by a later worker.
> 4. `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`,
>    `.claude/skills/expedition-checker/SKILL.md` and `CONTEXT.md` are not changed, and no file under `.scratch/` is
>    changed.
> 5. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is the repair [node 94](94-condition-scope-as-a-predicate.md) named and the manager never made.** Node 94
measured the five-file shortfall; the manager recorded it as owed on node 95 three separate times and did not
perform it, most recently declining to amend node 95's scope because node 82's guard 1 requires re-running the
search. **Node 95's worker ran that search** — `grep -rn "not that worker's to fix" .claude/`, exactly five hits —
so the count is now re-derived rather than trusted, and **the guard is satisfied for whoever claims this.**

**The worker narrowed the repair and its ground is the interesting part.** Node 94 read the five-contract sentence
as the worker's half of the whole party distinction; node 252, which resolved after node 94, leaves the mid-node
case exactly where that sentence puts it. **So the sentence is correct for the case it describes**, and what is
short is only the scope case. That narrowing is recorded as an invalidation on node 95.

**The collision with node 109 is the claiming worker's to respect and the manager's to sequence.** Two workers must
not hold those five files at once.

## Amendment, 2026-09-24

*Written by [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker and filed by the manager, after that node's work landed as commit `4068519`. Every word of each replacement is fixed by that commit: it quotes the research contract's after-text. The minting author's condition above is left as it was, and these replacements take the place of the clauses they name.*

Node 290's worker searched every open node's `## Acceptance condition` for quoted spans of the research contract's before-text, for mentions of the file, and for each piece of wording its rewrite removed or replaced. The full list of handles is on node 290 under `### Re-pointing duty` and `### Correction round 1`.

- **Clause 1.** The quoted sentence is gone. Replacement: "the passage *"The worker that claims the node may not fix a condition it judges wrong. That node stops instead, and the condition goes to the human. So any loose wording you write here can stop that node."* states in addition …", with the rest of the clause unchanged.
- **Clause 3.** Replace "that what the reporting worker writes loosely is paid for by a later worker" with "that loose wording by the reporting worker can stop the node it reports".

*Not filed, and the manager's own note:* node 290's worker also reported that **clause 2**, which says the five files are "not unified onto one sentence", already contradicted node 50 before its work, and now contradicts the byte-for-byte copying of the shared sections as well. It left that demand to the manager or the human. Changing it needs a judgement nobody has made, so it goes to the human before this node is claimed.

## Flags

`279.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `4068519`.

## Superseded, 2026-09-26

*The manager's note.* Made unnecessary, on node 329's worker's recommendation taken by the human's "ok": its demand, that the manager may extend a short scope on a held node with no human turn, contradicts nodes 82 and [311](311-may-the-human-amend-a-held-nodes-condition-of-their-own-accord.md), where a held node's condition changes only by the human's answer; its clause 2 contradicts the byte-identical shared sections of the worker contracts.
