# Map: the manager handles its own choices instead of putting them to the human

Every worker reads this whole file once per node. What only the manager acts on is in
[map-manager-only.md](map-manager-only.md). What an implementation node's work is held to is in
[map-implementation-rules.md](map-implementation-rules.md).

## Destination

GitHub issue 1, "Trips on self-written nodes", is fixed in this repository's shipped files. The
manager stops sending the human choices it made itself, such as a condition it wrote and that a check
showed slightly wrong, where fixing that choice changes nothing the human decided. Each of the issue's
proposed changes 1 to 6 has been either landed or ruled out by the human. Example 8 of the issue, about
scoped instruction files that never load, is part of the destination only if the human brings it in
after their trial outside the skill.

The effort is expected to reach this destination.

The human's request, `verbatim`, as it started the effort: *"we'll work on issue 1 on github"*. The
human then weighed holding this work in the closed `graph-workflow` effort, and chose a separate
effort, `verbatim`: *"Yeah, okay, let's move it back to separate effort."*

## Notes

- **Domain.** The product of this effort is the expedition skill files under `.claude/skills/`, and
  `.claude/rules/expedition-triggers.md`. The root `CLAUDE.md` states the rules for writing them, the
  standards they are held to, and the duty to keep the trigger file in step with `SKILL.md`.
- **The issue.** [issue-1.md](issue-1.md) holds the issue's title, body and comment, saved on
  2026-11-11 at `d49b11e`. Read it there. `gh` has no credentials in the sandbox. The comment's
  `A note from the human on how to write the fix` is the human's own steer, given in paraphrase: keep
  the fix to the principle, and list no steps per scenario.
- **Ground rules.** Work in this effort is held to the standards listed under `## Standards` in the
  root `CLAUDE.md`, and to its `## Rules for the files under .claude/skills/`. Nothing is pushed
  without the human's word.
- **Deliverables.** The work lands as three deliverables, each its own branch and pull request:
  `own-choices` ([node 07](nodes/07-write-the-rule-for-what-the-manager-settles-on-its-own.md),
  [node 08](nodes/08-add-the-amendment-flag-marker.md)), `you-decide-on-a-flag`
  ([node 06](nodes/06-write-the-you-decide-rule-for-a-flag.md)), based on `own-choices`, and
  `explain-a-relayed-question` ([node 09](nodes/09-write-the-rule-for-explaining-what-an-agent-wrote.md)). Two
  deliverables that edit the same lines conflict when the second is integrated, so an implementation
  node keeps clear of the lines another deliverable's open node edits.
- **Sources.** The shipped files under `.claude/skills/` and `.claude/rules/`, and the root
  `CLAUDE.md`, are authoritative. [issue-1.md](issue-1.md) is the human's account of what happened on
  another effort and what they propose. Its clause quotes are evidence only, and may have drifted from
  the files. `.scratch/graph-workflow/` and `.scratch/rename-split-upgrade/` are the records of closed
  efforts. They are evidence only, and their rules bind nothing in this effort.

## Decisions so far

See [decisions.md](decisions.md).
