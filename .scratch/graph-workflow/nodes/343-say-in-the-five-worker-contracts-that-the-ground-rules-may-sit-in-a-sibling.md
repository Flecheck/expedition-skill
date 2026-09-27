# Say in the five worker contracts that the ground rules may sit in a sibling file of the map

Type: implementation
Status: resolved
Blocked by: none

## Question

Each of the five worker contracts says "The map's `## Notes` may declare the effort's ground rules. It may also declare, by path or glob, which sources ...". `graph-conventions.md` now says those blocks live in `map.md`'s `## Notes` unless the effort holds them in a sibling file of the map, and this effort holds its ground rules in `map-implementation-rules.md`. Should the contracts say the same?

*Reported by [node 338](338-say-in-graph-conventions-md-which-file-of-the-map.md)'s worker, which gave node 338 as its blocker; node 338 has landed (`968b1ec`).*

## Acceptance condition

*Authored by node 338's worker and filed by the manager.*

In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`, the sentence beginning "The map's `## Notes` may declare the effort's ground rules." no longer requires the ground rules, or the declaration of which sources are authoritative, which are evidence only and which hold statements known to be false, to sit in `map.md`'s `## Notes`. It names the map as a whole, or says the blocks sit in `map.md`'s `## Notes` unless the effort holds them in a sibling file of the map. The rest of each contract's paragraph keeps its meaning. No other file changes. The files are shipped, so they are edited plainly.

## Answer

The five worker contracts now say the map declares the ground rules and source authority, in `map.md`'s `## Notes` unless the effort keeps them in a sibling file of the map.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `688aa50`. The worker's retrospective notes a possible gap: only the implementation contract names a sibling rules file in its reading list. This is its first report, so no node is minted.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Say in the five worker contracts that the ground rules may sit in a sibling file of the map
ANSWER:        In all five worker contracts (grilling, research, prototype, precondition, implementation), the paragraph under `## What you read` that opened "The map's `## Notes` may declare the effort's ground rules." now reads, word for word the same in all five:

               "The map may declare the effort's ground rules. It may also declare, by path or glob, which sources are authoritative, which are evidence only, and which hold statements known to be false. Follow both. Each declaration sits in `map.md`'s `## Notes` unless the effort holds it in a sibling file of the map. Absent any declaration, every source you are pointed at is authoritative."

               The research contract keeps its extra closing sentence, "A source marked as evidence stays evidence, whatever it says." That tail was rewrapped so it fills to the file's 105-column width. Choices made: the subject is now "the map", meaning the whole map. The location rule is a separate sentence that copies graph-conventions.md's own clause, "unless the effort holds it in a sibling file of the map", so the two files agree word for word. That sentence comes after "Follow both." so that "both" still points only at the two declarations. The grilling contract's next paragraph, "The map's `## Notes` may also declare the effort's own domain vocabulary.", was left alone. It is about the vocabulary, not the ground rules, and it still reads correctly after the new text.
INDEX LINE:    The five worker contracts now say the map declares the ground rules and source authority, in `map.md`'s `## Notes` unless the effort keeps them in a sibling file of the map.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: none. This carries graph-conventions.md's wording from node 338 into the contracts. It narrows no resolved node.
CONDITIONS:    I searched the open and claimed nodes' `## Acceptance condition` sections for "may declare the effort's ground rules", "map's `## Notes` may" and "sibling file of the map". Only node 343's own file matched. No replacements.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none yet (no checker run). Paths touched, all in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/343-contracts:
               - .claude/skills/expedition-grilling/SKILL.md
               - .claude/skills/expedition-research/SKILL.md
               - .claude/skills/expedition-prototype/SKILL.md
               - .claude/skills/expedition-precondition/SKILL.md
               - .claude/skills/expedition-implementation/SKILL.md
               Bar: I checked the repo again and it still has no build, no tests, no formatter and no CI, which matches the rules file. So the bar is only its non-command half: the ground rules, the five writing rules, CONTEXT.md's `_Avoid_` lines, graph-conventions.md and /writing-for-agents. The new lines are at most 105 columns, the width these files already use; the only longer lines were already in the files. No method skill used, nothing skipped.
               Proposed commit message:
                 Say in the five worker contracts that the ground rules may sit in a sibling file of the map

                 Node: graph-workflow/343

RETROSPECTIVE
1. What I had to hunt for: nothing much. The graph-conventions.md wording is in its `## Notes` bullet, and I found it with one grep for "sibling file".
2. What arrived that this node did not need: the decisions.md reading. The condition is self-contained, and no decision line changed what I wrote. The map's rules file mattered only for the column width and the finding that the repo has no commands.
3. What would have made this easier: quoting the exact graph-conventions.md clause in the spawn or in the condition would have saved a lookup. It was small anyway.
4. Stale, wrong or contradictory: nothing contradicts this change. Worth knowing: .claude/skills/expedition/SKILL.md at line 31 says "The effort's ground rules ... live in it" (the map). That still holds, because a sibling file is part of the map. I did not touch it, because node 337 owns that file. Also, only the implementation contract names a sibling file (map-implementation-rules.md) in its reading list. A worker of another kind whose effort keeps its ground rules in a sibling file relies on the record-search rule, or on the spawn, to find it. That is a possible gap but not this node's scope.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 335's check.*

> PASS
>
> Node 343, "Say in the five worker contracts that the ground rules may sit in a sibling file of the map". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/343-contracts`, on base b4970ed. I established each part from `git diff` and `git status --short`.
>
> - **Scope, "No other file changes":** met. `git status --short` shows exactly the five contracts: grilling, research, prototype, precondition and implementation `SKILL.md`. The diff has one hunk per file, each confined to the paragraph named.
> - **Shipped files edited plainly:** met. The old sentence was removed outright, with no strikethrough and nothing moved to a history file.
> - **The sentence no longer ties the two blocks to `map.md`'s `## Notes`:** met in all five files. Each diff removes "The map's `## Notes` may declare the effort's ground rules." and adds "The map may declare the effort's ground rules." Both blocks are covered: the ground rules, and the declaration of authoritative, evidence-only and known-false sources.
> - **Names the map as a whole, or adds the sibling qualification:** met in all five files, which do both. Each adds "Each declaration sits in `map.md`'s `## Notes` unless the effort holds it in a sibling file of the map."
> - **The rest of each paragraph keeps its meaning:** met. "It may also declare, by path or glob, …", "Follow both." and "Absent any declaration, every source you are pointed at is authoritative." are unchanged in all five. The research contract still ends "A source marked as evidence stays evidence, whatever it says."; only the line wrapping changed there, and the words are the same.
>
> **The bar:**
> - The repo has no build, tests, formatter or CI. The standards file says so, and the repo root holds no manifest.
> - `git diff --check`: clean, exit 0.
> - `awk 'length>105'` over the contracts: no added line exceeds 105. Every hit is on a line the diff does not touch (tables, a long frontmatter line, and so on).
>
> **Standards:** as before, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
> - Bore on this work:
>   - `CONTEXT.md` `_Avoid_` lines, checked by hand on the added sentence: nothing found.
>   - The five writing rules: one idea per sentence, "Each declaration" has one clear referent, and no bold was added.
>   - `/writing-for-agents`: nothing found.
>   - The ground rules: each contract still stands alone, and nothing assumes a repo, machine or toolchain or addresses the human. Ground rule 2 is satisfied because the sentence refers to a file, not to an invocable skill.
> - Did not bear: `/coding-principles` and `/naming`, since the work is prose and names nothing new.
> - No reviewing skill is named, so I ran none. The work changes no standard I hold it against.
>
> The condition records no search command, so there was nothing to re-run.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this, but the rules file makes it a bookkeeping rule. The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*
