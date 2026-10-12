---
name: expedition-cleanup
description: Clean up an expedition's record. The human invokes it in an expedition's manager thread to remove record that a finished part of the effort no longer needs, by one of two operations, region cleanup or flag cleanup. The manager also reads it to propose a region cleanup when the human says a deliverable's pull request has merged, or when the manager has merged a deliverable locally.
---

# Cleaning up the record

You are the manager of an expedition, and the human has invoked this skill. It removes record that a
finished part of the effort no longer needs.

## The rule this skill is an exception to

The opening paragraph of `graph-conventions.md`, which begins "No edit deletes.", states the
never-delete rule and the exception this skill falls under. In place of what you remove, leave the
entry that paragraph describes.

Remove only text that the effort's version control history already holds, so the entry's claim is true.

## Two operations

This skill has two operations: **region cleanup** and **flag cleanup**. The human invokes each one
separately, and neither implies the other. Where the invocation does not say which one it is, ask the
human. The one region cleanup you propose without an invocation is the one under
`### A merged deliverable as the region`.

The two operations are the whole of what this skill does. It removes no text because the text is old,
because its file has grown long, or because the text is marked superseded.

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
3. A node in the set that holds an outstanding flag also stops the removal. Put that flag to the human
   first, because removing its line would drop it from the effort closing report.
4. Put the set in front of the human for confirmation or amendment. Remove nothing before they confirm
   it.
5. Remove the region from every file of the effort's record, and not from the node files alone. That
   covers each node file in the set, and the part of each other file attributable to the region, such
   as the set's lines in `decisions.md` and in `flags.md`.
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

## Flag cleanup

`flags.md` holds one line per flag, with its state. The effort closing report is built from its lines
whose flag is not yet settled.

1. Remove from `flags.md` each line whose flag is settled, marked `- [x]`.
2. Leave every line whose flag is outstanding, marked `- [ ]`.
3. Leave every node file unchanged.

Nothing is lost. A flag's prose and its `settled` marking both live on the node that raised it, and this
operation does not modify that node.

## Reporting

Report to the human what each operation removed: for region cleanup the region and the node ids, and
for flag cleanup the ids of the lines removed. For a merged deliverable, also report whether its entry
and its local branch were removed, and, where they were kept, which remaining node names it.
