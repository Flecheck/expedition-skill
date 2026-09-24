# Four worker contracts say `map.md` holds the fog

Type: implementation
Status: open
Blocked by: 290, 291, 292, 293

## Question

The shipped `graph-conventions.md` puts `## Not yet specified — the fog` in `map-manager-only.md`, which no worker reads. The `## What you read` bullet in the grilling, precondition, prototype and research contracts still reads "`map.md` — the destination, the standing preferences, the fog".

*Reported by [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker, whose note for the manager reads: "Node 155's clause 3 ("no existing bullet is reworded") would collide with this if 155 is claimed afterwards. Re-point one of the two."*

## Acceptance condition

*Authored by node 290's worker and filed by the manager.*

1. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-research/SKILL.md`, the `## What you read` bullet naming `map.md` names the destination and the standing preferences, and does not name the fog.
2. Enumerator: `grep -rln "the standing preferences, the fog" .claude/` returned exactly those four paths at `e5c03a5`, and after the work it returns nothing.
3. Nothing else in the four files changes, and no other file changes.
4. The tree meets the bar.
