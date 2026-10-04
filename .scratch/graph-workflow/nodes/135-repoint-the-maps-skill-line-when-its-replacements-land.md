# Repoint the map's `## Notes` skill line when its two replacements land

Type: precondition
Status: open

Blocked by: 126, 383

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
