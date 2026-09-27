# Differences from a wayfinder tracker

This file is only for a repo whose tracker doc already describes the `/wayfinder` skill's
local-markdown scheme. `graph-conventions.md` holds the conventions. This file holds only how they
differ from that tracker doc, and the block to append to the doc.

## Unchanged

- The effort directory, `.scratch/<effort>/`, and `map.md` as the map.
- One file per node, `NN` numbered from `01`.
- The `Type:`, `Status:` and `Blocked by:` lines in the header.
- Claiming: set `Status: claimed` and save before any work.
- Conversation appended to the bottom of the node file.

Every ticket already written under that doc stays valid.

## Added

- A fifth node type, `implementation`.
- Three more statuses: `open`, `superseded`, `out-of-scope`.
- Two more edge kinds: `Supersedes:` and `Superseded by:`.
- The `Labels:` field.
- The `## Acceptance condition`, `## Flags` and `## Review` sections.

## Changed

Append the block below, which states the five conventions that differ, to the target's tracker doc.
No other part of that doc needs to be rewritten or removed.

```markdown
## Expedition operations

An effort run as an expedition follows `graph-conventions.md`, which extends the wayfinding
operations above. Five differences:

- **Node files live at `.scratch/<effort>/nodes/NN-<name>.md`**, not under `issues/`. An effort's
  nodes never share a directory with this repo's own tickets.
- **The fourth node type is `precondition`**, not `task`. The other four are unchanged, and a
  fifth, `implementation`, is added.
- **Conversation appends under `## Interview`**, not `## Comments`, and each recorded answer is
  marked `verbatim` or `paraphrase`.
- **Resolving appends a capped line to `.scratch/<effort>/decisions.md`**, not to the map body.
- **The frontier is a set, not a queue.** It is every node that is open, unblocked and unclaimed;
  no order is fixed within it, and `Labels:` scopes it to one area.
```

## Not covered here

How to adopt an effort that is already under way is in `adoption.md`. Adoption turns the existing
questions, decisions and prose edges into node files, and appends the block above to the tracker doc.
