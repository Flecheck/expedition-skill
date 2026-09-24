# The manager contract's `implementation` entry says the node ends at a gate

Type: implementation
Status: superseded
Blocked by: 296, 297, 298
Superseded by: 296

## Question

Node 242 removed "the node ends at the gate" from `CONTEXT.md`'s `implementation` entry. `.claude/skills/expedition/SKILL.md`'s `## Words used exactly` entry still says "The node ends at a gate." That contradicts the glossary, and also that file's own `## The gate`, where the node resolves after the commit. Carry node 242's replacement into the manager contract.

*Reported by [node 296](296-rewrite-the-manager-contract-part-1.md)'s worker. Its blockers as handed back: "296 (it rewrites the text this node edits). Under node 289's freeze, it is claimed only once the manager-contract rewrites 296–298 have landed."*

## Acceptance condition

*Authored by node 296's worker and filed by the manager.*

1. In `.claude/skills/expedition/SKILL.md`, the `## Words used exactly` entry for `implementation` no longer states that the node ends at a gate. It states instead that the gate is the last point at which the human can act on the node, and that the gate is neither where the node ends nor where it resolves: after approval the manager commits the work and lands it, and the node resolves after that.
2. No other sentence in that file states that an implementation node ends or resolves at its gate.
3. No other path changes.
4. The working tree meets the bar.

## The manager's note, 2026-09-24

*The manager's own note.* Node 296's worker withdrew this node at its correction round 5: the `implementation` entry no longer exists once the term list points at `CONTEXT.md`. If node 296 lands with that change, this node is superseded as made unnecessary by it.

## Superseded, 2026-09-24

*The manager's note.* Made unnecessary by [node 296](296-rewrite-the-manager-contract-part-1.md)'s landing as `6745f37`: the manager contract's `implementation` entry no longer exists, and the file takes `CONTEXT.md`'s corrected definition.
