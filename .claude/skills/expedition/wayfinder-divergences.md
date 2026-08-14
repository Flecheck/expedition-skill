# Differences from a wayfinder tracker

For a repo whose tracker doc already describes the `/wayfinder` skill's local-markdown scheme. A repo
with no such doc needs nothing from this file.

`graph-conventions.md` holds the conventions themselves. This file holds only where they read
differently from that doc, and the block to append to it.

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

## Read differently

Five things. Append the block below to the target's tracker doc; nothing in that doc has to be
rewritten or removed.

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

Importing an effort that is already under way — its existing questions, decisions and prose edges
becoming node files. That is a separate procedure.
