# The glossary's `Flag` entry names one case of a flag reaching the closing report, and the manager contract names two

Type: implementation
Status: superseded
Superseded by: 309
Blocked by: 302, 309, 317

## Question

*Surfaced by [node 302](302-rewrite-the-glossary.md)'s worker, and filed by the manager as it wrote it.*

`CONTEXT.md`'s `Flag` entry says a flag goes into the closing report "only where the human never spoke again". `expedition/SKILL.md` says "Flags reach the closing report in two cases only": the first is a flag raised before this settling rule existed, on a node already resolved, and the second is a flag whose pick report the human never answered. Should the glossary carry both cases?

*The manager's note:* the worker gave 302 as the only blocker. The manager added [node 309](309-drop-the-closing-reports-case-for-flags-raised-before-settle-at-close.md), which asks whether to drop the first of the two cases, and [node 317](317-which-outstanding-flags-reach-the-closing-report.md), which asks which outstanding flags reach the closing report at all. Either answer can change which cases this node's condition should carry, so the condition may need amending once they resolve.

## Acceptance condition

*Written by node 302's worker. Pasted as it wrote it, and not the manager's.*

1. In `CONTEXT.md`, or at the path the glossary has moved to, the `**Flag**:` entry's sentence "A flag goes into the closing report only where the human never spoke again." is replaced by a statement that a flag goes into the closing report in two cases only. The first case is a flag on a node already resolved, raised before flags were settled at a node's gate or at the report that closes the node. The second is a flag whose closing moment the human never answered, because they never spoke again. Where the file no longer uses the term `pick report`, the statement uses the file's term for the same report.
2. The entry's other sentences and its `_Avoid_` line are unchanged. No other entry in the file changes, and no entry is added or removed.
3. No other path changes.
4. The working tree meets the bar.

*The manager's note, 2026-09-26:* [node 309](309-drop-the-closing-reports-case-for-flags-raised-before-settle-at-close.md)'s worker reports, under its `INVALIDATIONS`, that this node's premise no longer holds once 309 lands: the manager contract will name one case, which is what `CONTEXT.md`'s `**Flag**:` entry already says, and item 1 of this condition would put the dropped case back into a shipped file. The worker says the condition needs amending, or the node can be closed as already satisfied, and that node 317 may bear on it too. This goes to the human at node 309's gate.

## Interview

### The manager's raise, 2026-09-26

*The manager's own raise, sent after node 309's gate.* Node 309 has landed (`c52c03e`), so the manager contract and the glossary now both name one case. Should this node be superseded by node 309, which made it unnecessary, or kept with its condition rewritten? The manager recommended superseding it. Node 317, which may still change which flags reach the closing report, would then have to keep the glossary's `**Flag**:` entry in line itself.

The human, `verbatim`: *"ok for superseded"* — taking the option the manager offered: *"Should this node be superseded by node 309, which made it unnecessary"*.

## Superseded, 2026-09-26

*The manager's note.* [Node 309](309-drop-the-closing-reports-case-for-flags-raised-before-settle-at-close.md)'s landing as `c52c03e` makes this node unnecessary: the manager contract's `## Flags` now names one case of a flag reaching the closing report, which is the one case `CONTEXT.md`'s `**Flag**:` entry already names. The question and acceptance condition above are superseded as a whole. Whatever node 317 decides about which flags reach the closing report, its own work keeps the glossary's `**Flag**:` entry in line.
