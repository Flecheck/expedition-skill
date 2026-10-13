---
name: expedition-cleanup
description: Clean up an expedition's record. The human invokes it in an expedition's manager thread to remove record that a finished part of the effort no longer needs, by its one operation, region cleanup. The manager also reads it to propose a region cleanup when the human says a deliverable's pull request has merged, or when the manager has merged a deliverable locally.
---

# Cleaning up the record

You are the manager of an expedition, and the human has invoked this skill. It removes record that a
finished part of the effort no longer needs.

## The rule this skill is an exception to

The opening paragraph of `graph-conventions.md`, which begins "No edit deletes.", states the
never-delete rule and the exception this skill falls under. In place of what you remove, leave the
entry that paragraph describes.

Remove only text that the effort's version control history already holds, so the entry's claim is true.

## One operation

This skill has one operation, **region cleanup**. The human invokes it. The one region cleanup you
propose without an invocation is the one under `### A merged deliverable as the region`.

Region cleanup is the whole of what this skill does. It removes no text because the text is old, because
its file has grown long, or because the text is marked superseded.

## Region cleanup

A **region** is a part of the effort's subject matter whose work is finished. The human names the
region in their own words. Never judge on your own that a region is finished.

1. Read the human's naming and propose the set of nodes you take it to mean. Where the effort's nodes
   carry `Labels:`, you may use them to propose the set faster. Labels are never required, and most
   efforts declare few or none.
2. The set must meet three conditions, and you remove nothing from a set that fails any of them:
   - every node in the set is `resolved`;
   - nothing outside the set refers to any node in it, whether a remaining node or a part of another
     file of the record that this operation does not remove;
   - the human has confirmed the set.
   Where one of the first two fails, say which node fails it and why, and propose an amended set.
3. Find the outstanding flags the set's nodes hold, by searching their `## Flags` entries for those not
   marked settled. No outstanding flag stops the removal. Removing a node removes its flags. An
   outstanding `FRICTION` flag raised on an effort whose product is not the expedition skill files
   would otherwise have reached the effort closing report. List each such flag, with its id and the
   first sentence of its entry, in the set you put to the human in step 4.
4. Put the set in front of the human for confirmation or amendment. Remove nothing before they confirm
   it.
5. Remove the region from every file of the effort's record, and not from the node files alone. That
   covers each node file in the set, and the part of each other file attributable to the region, such
   as the set's lines in `decisions.md`.
6. In `decisions.md`, where the region's lines stood, write one entry. It names the region as the human
   named it, lists the ids of the nodes removed, and records that the removed text remains recoverable
   from the effort's version control history.

What this removes is each node's account of what happened. Text stating a rule that currently binds is
never removed by this operation. Such text is held in the map's files, which are the effort's rule
files, rather than on a node. So it is never in a region to begin with.

### A merged deliverable as the region

An effort may declare deliverables, each one listed under `## Deliverables` in its
`map-manager-only.md`. Propose a region cleanup whose region is a deliverable at either of two
moments:

- when the human says the deliverable's pull request has merged;
- right after you have merged the deliverable locally.

The merge names the region, so you propose the cleanup without the human invoking this skill.

The proposed set holds:

- every node whose `Deliverable:` field names that deliverable, and whose every named deliverable has
  merged;
- each resolved node that blocks at least one node, and whose every dependent is in the set. A
  node's dependents are the nodes that list it in `Blocked by:`. Apply this item again until it adds
  no node.

A node that also names a deliverable not yet merged stays out of the set. The merged deliverable then
keeps its entry and its local branch, as the passage below beginning "A deliverable that a remaining
node still names" says.

Steps 2 to 6 above apply to that set unchanged: the three conditions, the outstanding flags, the
human's confirmation, and the removal.

Once the record is cleaned, take each deliverable that has merged, by either route, and that no
remaining node names. A deliverable has merged when the human has said its pull request merged, or
when you have merged it locally. For each such deliverable:

1. Remove its entry from `## Deliverables`, by the steps of `### Change the map` in
   `graph-conventions.md`.
2. Delete its local branch. Leave its remote branch as it is, because the human's host owns it. A
   deliverable that landed locally has no remote branch.

A deliverable that a remaining node still names keeps its entry and its branch, until a later cleanup
removes that node.

## Reporting

Report to the human what the operation removed: the region, the node ids, and the ids of the
outstanding flags removed with those nodes. For a merged deliverable, also report whether its entry
and its local branch were removed, and, where they were kept, which remaining node names it.
