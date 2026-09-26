# Widen the invalidation channel from contradiction to change

Type: implementation
Status: superseded
Superseded by: 333, 338

## Question

Every worker contract asks for *which resolved node your work contradicts*, and the traffic that part has to
carry is mostly renames, extensions and narrowings — measured at fifteen of eighteen propagations onto
resolved nodes arriving through the manager's reading instead. Reword the part, in the six shipped files that
carry the wording, so its scope is any resolved node whose answer the work changes what it says.

Reported by [Cascade pass mechanics](15-cascade-pass-mechanics.md)'s worker, which wrote the acceptance
condition below. It is part 1 of that node's answer, and the part the human endorsed first.

**Blockers: none. Sequencing only** — `graph-conventions.md` is live territory for [Record a checker's
not-covered part on `## Review`](38-recording-a-not-covered-part.md) and the five contracts for
[Checking a flag before the human sees it](30-checking-a-flag-before-the-human.md), [Narrow the flags.md
clause in the worker contracts](32-narrow-flags-file-clause.md) and [Nothing tells a worker to hold its work
against the record](37-invalidations-is-not-a-check.md), and the code slot is exclusive, so this runs alone
rather than beside any of them.

## Acceptance condition

Six files change, and no other file in the repository changes:

- `.claude/skills/expedition-grilling/SKILL.md`
- `.claude/skills/expedition-research/SKILL.md`
- `.claude/skills/expedition-prototype/SKILL.md`
- `.claude/skills/expedition-precondition/SKILL.md`
- `.claude/skills/expedition-implementation/SKILL.md`
- `.claude/skills/expedition/graph-conventions.md`

1. Each of the five `SKILL.md` files carries one line inside its handover block of the form
   `INVALIDATIONS: <which resolved node your ... contradicts, and how>`. The noun differs per file and
   the current text is: `your answer contradicts` in the grilling and prototype files, `your facts
   contradict` in the research file, and `your work contradicts` in the precondition and implementation
   files. After the change, each of those five lines asks for any resolved node whose answer this work
   **changes what it says** — not only one it contradicts — and names four kinds inline so that a worker
   reading only that line knows the scope: a **rename**, an **extension**, a **narrowing**, and a
   **contradiction**. Each file keeps its own noun (`answer`, `facts`, `work`) rather than the five being
   unified onto one.
2. Each of the five files states, in prose near that line, that an outright contradiction is the minority
   case and a renamed term or a narrowed rule is the ordinary one, so its reader does not treat the part
   as reserved for conflict.
3. `.claude/skills/expedition/graph-conventions.md` carries one sentence describing the same part, whose
   current text is: `` `INVALIDATIONS` — which resolved node its work contradicts, and how — answered by
   the party that built the work and may read the record to see what it touches. `` That sentence is
   reworded to the same widened scope and names the same four kinds.
4. Nothing else in any of the six files changes meaning. Specifically, all five `SKILL.md` files still
   carry the sentence ``Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them.``
   unchanged, and all six files still carry, unchanged, the rule that a demand quantifying over the whole
   record — that the work contradicts no decision, that everything in it traces back to one — belongs on
   the handover's invalidation part and in no acceptance condition.
5. `.claude/skills/expedition-checker/SKILL.md` does not change. The checker returns no invalidation part
   and must not gain one.
6. No file under `.scratch/` changes.
7. The tree meets the bar.

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Clause 3.** Replace the quoted "current text" with: `` Every worker returns `INVALIDATIONS` on its handover instead, naming which resolved node its work contradicts and how. `` It is one sentence again, so "That sentence is reworded" stays as the condition has it. Clause 4 still holds: the file says "A demand about the record as a whole belongs on the handover and in no condition, whatever its wording."

## Flags

`43.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

## Amendment, 2026-09-25 (from node 312)

*Written by [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s worker and filed by the manager, after that node's work landed as commit `e64b3de`. Every word of the replacement is fixed by that commit: it quotes the after-text of `expedition/SKILL.md` and `expedition/graph-conventions.md`. The minting author's condition and any earlier amendment above are left as they were. Node 312's worker's search is on node 312 under `RE-POINTING SEARCH:`.*

- **Clause 3**, as amended by node 299. Replace the quoted current text with: `` Such a demand goes in the handover's `INVALIDATIONS` part, which names which resolved node the work contradicts and how. `` It is still one sentence, so "That sentence is reworded" stays. Clause 4 still holds: `graph-conventions.md` still says "A demand about the record as a whole belongs on the handover and in no condition, whatever its wording."

`43.2` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `e64b3de`.

## Superseded, 2026-09-26

*The manager's note.* Its worker-contract part is replaced by [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md), the merge [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole. Its `graph-conventions.md` sentence is held on node 329 as its remainder R1, for the manager-contract merge of [node 330](330-group-the-open-nodes-against-the-manager-contract.md) to absorb; the manager adds the replacement there when that merge is filed.

## Superseded, 2026-09-26

*The manager's note.* Its `graph-conventions.md` sentence, held on node 329 as remainder R1, is now carried by [node 338](338-say-in-graph-conventions-md-which-file-of-the-map.md) as clause 17a or 17b, on the human's "ok" to node 330's merge.
