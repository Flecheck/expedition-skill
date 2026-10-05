# State the sweep as a whole-graph run of the mechanical checks

Type: implementation
Status: claimed
Blocked by: none

## Question

Carry node 389's answer into the shipped files. The manager's contract says what the sweep is and who runs it, and graph-conventions.md makes the sweep the one exception to its rule that no separately spawned agent runs a check.

*Reported by [node 389](389-how-the-sweep-runs-now-that-the-cascades-machinery-is-gone.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. Note for the manager's slot filter: node 388 (claimed) edits both files in other sections, and node 317 (open, no condition) concerns the flags bullet of the same `## Closing an effort` section."*

## Acceptance condition

*Authored by node 389's worker and filed by the manager.*

> The work is these two paths, and no other file may be edited. These are files the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file.
>   `.claude/skills/expedition/SKILL.md`
>   `.claude/skills/expedition/graph-conventions.md`
>
> The scope came from no search: these two places are the work, not instances of a defect.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `.claude/skills/expedition/SKILL.md`, the section `## Closing an effort` ends with its bulleted list, whose last bullet is "- What the sweep found, and every sweep round." Immediately after that list, still inside the section, there is a new paragraph with exactly these words: "The sweep is a run of every check under `## Mechanical checks` in `graph-conventions.md` over the whole graph. Give the run to one read-only agent, which reports only the failures. Each failure becomes a node. When the frontier empties again, the sweep runs again." Line wrapping may differ, but the words may not. Nothing else in the file changes.
> 2. In `.claude/skills/expedition/graph-conventions.md`, under `### Who runs a check, and when`, these two sentences: "No schedule, no periodic pass and no separately spawned agent runs any of them. One run is not tied to an act: a run of every check over the whole graph, which remains available at an empty frontier." are replaced by exactly: "No schedule, no periodic pass and no separately spawned agent runs any of them, with one exception. The sweep runs every check over the whole graph at an empty frontier, and `## Closing an effort` in `SKILL.md` says who runs it." Line wrapping may differ, but the words may not. Nothing else in the file changes.
> 3. No file under `.scratch/` changes.
> 4. The tree meets the bar.
