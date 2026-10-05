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

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-05.*

`````
HANDOVER:      State the sweep as a whole-graph run of the mechanical checks

ANSWER:        Node 389's answer is now in the two shipped files. In `.claude/skills/expedition/SKILL.md`, a new paragraph sits at the end of `## Closing an effort`, directly after the bullet "- What the sweep found, and every sweep round.". It reads: "The sweep is a run of every check under `## Mechanical checks` in `graph-conventions.md` over the whole graph. Give the run to one read-only agent, which reports only the failures. Each failure becomes a node. When the frontier empties again, the sweep runs again." In `.claude/skills/expedition/graph-conventions.md`, under `### Who runs a check, and when`, the two sentences "No schedule, no periodic pass and no separately spawned agent runs any of them. One run is not tied to an act: a run of every check over the whole graph, which remains available at an empty frontier." were replaced by "No schedule, no periodic pass and no separately spawned agent runs any of them, with one exception. The sweep runs every check over the whole graph at an empty frontier, and `## Closing an effort` in `SKILL.md` says who runs it." Both use the acceptance condition's words exactly. The lines are wrapped to the files' existing width of about 105 columns, and nothing else in either file changed. Nothing else needed a decision. `.claude/rules/expedition-triggers.md` was left alone: the edit is not in `## The order you act in` or `## What is in front of the human, and when`, and a search of `.claude/rules/` finds no mention of the sweep. The glossary's `Sweep` entry still defines the sweep as the same work as a cascade. Node 388's clause (e) rewrites that entry, and node 389's settled flag 389.2 covers it, so this node leaves the glossary unedited, as its condition requires.

INDEX LINE:    SKILL.md's closing section now says the sweep is one read-only agent running every mechanical check over the whole graph, and graph-conventions.md makes it the one exception.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none beyond what node 389 already reported (nodes 10 and 15). This node only puts 389's answer into the files. Node 13 (resolved) calls its invariant list "the sweep's mechanical half". That still holds, and the sweep is now made of that half alone, which is the narrowing 389 recorded against node 10.

CONDITIONS:    The open and claimed nodes were searched for "separately spawned", "not tied to an act", "remains available", "Who runs a check", "Closing an effort", "sweep", "empty frontier" and "whole graph". Matches were in node 317 (open), on the flags bullet of `## Closing an effort`, and node 388 (claimed), on glossary clause (e) for `Sweep`. Neither condition is made wrong: node 317 is about a different bullet, and node 388 edits other sections. Node 13 (resolved) matched on "sweep" and is covered under INVALIDATIONS. No replacement clauses.

MISSING FROM MAP: none

GATE PAYLOAD:  No checker findings yet. Paths touched: `.claude/skills/expedition/SKILL.md`, `.claude/skills/expedition/graph-conventions.md`, both uncommitted in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/390-sweep. Nothing under `.scratch/` changed (`git status` shows only those two files). Bar: the repo states no build, test or format commands. Its root holds `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md` (a superseded pointer to the glossary), `.gitignore` and `.scratch`, with no manifest and no CLAUDE.md or AGENTS.md. That matches map-implementation-rules.md's record, so the bar is the standards plus the condition. None of the new lines is longer than the existing wrap width. Skipped method-skill parts: none were invoked.
Proposed commit message:
  State the sweep as a whole-graph run of the mechanical checks

  SKILL.md's closing section says the sweep runs every mechanical check
  over the whole graph with one read-only agent, and graph-conventions.md
  makes it the one exception to its rule that no separately spawned agent
  runs a check.

  Node: graph-workflow/390

RETROSPECTIVE
1. What I had to hunt for: nothing much. The spawn and the node gave both exact replacements. The only check was that the "## Mechanical checks" heading exists in graph-conventions.md, which a grep in the worktree confirmed. To confirm the glossary's stale `Sweep` entry was already handled, I searched node 389's file and found flag 389.2.
2. What arrived that the node did not need:
   - `map-read-whole-for-a-few-items`: 10 earlier retrospectives carry it (nodes 135, 178, 205, 220, 284, 382, 386, 387, 388, 389), derived 2026-10-05 by derivations.md entry (j); the count is for scale only. About 40KB of map.md was read whole, and the only thing that bore on this node was that the repo has no build commands, which sits in the rules file.
   - `rules-file-read-whole-for-one-section`: 7 earlier retrospectives carry it (nodes 178, 220, 382, 386, 387, 388), derived 2026-10-05; the count is for scale only. Only the bar's commands paragraph and the standards list mattered.
   The handover's search of open conditions and questions costs little here. For a node whose condition is given verbatim and complete, it is the only part of the record the work needed.
3. What would have made it easier: for a pure carriage node whose condition holds verbatim text, a spawn that skips the whole-map read. Otherwise nothing: the condition was exact and self-contained.
4. Stale, wrong or contradictory: the glossary's `Sweep` entry ("the same work as a cascade") contradicts the new SKILL.md paragraph until node 388 lands. This is already known (flag 389.2), so no new name is minted. The manager's note about node 388 checked out: 388 is claimed, and its condition touches other sections.
`````
