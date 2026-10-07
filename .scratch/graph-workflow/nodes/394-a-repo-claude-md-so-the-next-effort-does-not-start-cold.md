# A repo `CLAUDE.md` so the next effort in this repo does not start cold

Type: implementation
Status: claimed
Blocked by: none

## Question

This work lets every agent that starts in this repository, on any later effort, learn at once what the repository is, what its work is held to, and how its worktrees are made, without reading this effort's map. That map and its rules file belong to `.scratch/graph-workflow/`, and they stop binding when this effort closes.

*Minted by the manager from the human's request, 2026-10-07, `verbatim`:* *"Can you create a CLAUDE.md withe the information in map-implementation-rules.md and other usefull information so that next effort in this repo doesn't start from scratch"*

*The manager then proposed a scope. It listed what the file would hold: what the repo is, the bar, the standards, the ground rules and writing rules, the worktree route, the trigger file, two traps, and pointers. It listed what stays out: landing and bookkeeping, and the "why". It would be short, around a page, pointing at files instead of restating them. The message ended "Please answer: \"ok for recommended\" mints the node with that scope, or tell me what to add or drop." The human's answer, `verbatim`, 2026-10-07:* *"ok"*

## Acceptance condition

*Written by the manager, who minted the node.*

> The work is one new file, `CLAUDE.md`, at the repository root. No other file may be edited.
>
> Scope: the file is new and the named place is the work, so the scope came from no search.
>
> Done when all of the following hold.
>
> 1. `CLAUDE.md` exists at the repository root, and `git status` shows it as the only change.
> 2. It says what the repository is: the `/expedition` workflow's skill files under `.claude/skills/`, the auto-loaded `.claude/rules/expedition-triggers.md`, and per-effort records under `.scratch/<effort>/`. It says an effort's map is the file `map.md` in that effort's directory.
> 3. It states the bar for this repository. The repository has no build, no tests, no formatter and no CI. So the bar is the standards in clause 4 plus the node's acceptance condition. It states this as the repository's own statement of its commands.
> 4. It lists the standards that work in this repository is held to: `/coding-principles` and `/naming`; the `_Avoid_` lines of `.claude/skills/expedition/glossary.md`; `.claude/skills/expedition/graph-conventions.md`; and `/writing-for-agents`.
> 5. It states, as rules for the files under `.claude/skills/`, the content of the five ground rules and the six standing rules for writing held in `.scratch/graph-workflow/map.md`'s `## Notes`, in the blocks headed "Ground rules for this effort." and "This effort's standing rules for writing". It may reword them so that they read as repository rules rather than this effort's. It keeps every demand they make, drops their node citations, and adds no new demand.
> 6. It states the worktree route an implementation node uses here:
>    - the worktree is made with plain `git worktree add` at `.scratch/<effort>/worktrees/<NN>-<name>` on a branch `worktree-<NN>-<name>`;
>    - that path is ignored by `.gitignore`;
>    - a worker writes the tree by absolute path and owes no cleanup;
>    - the fast-forward merge into the main checkout and the worktree's removal run with the sandbox off.
>
>    It may point at an effort's `map-manager-only.md` for the full steps, rather than restating them.
> 7. It states that whoever edits, in `.claude/skills/expedition/SKILL.md`, the governing statement of a duty copied into `.claude/rules/expedition-triggers.md`, or of the priority that orders them, edits that file in the same change or says plainly why not.
> 8. It states the two traps:
>    - many refused words in the glossary's `_Avoid_` lines are ordinary English refused only for one concept, so a grep for them gives false positives, and the distinctive refusals are checked by hand;
>    - a number about an effort's record that is handed to another agent, or written into a condition, carries the date it was derived and says it is for scale only.
> 9. It says nothing is ever pushed without the human's word.
> 10. It holds no account of how any rule was learned, no node citation, and no rule that binds only `.scratch/graph-workflow/`'s effort, such as its landing steps, its record bookkeeping, its slot counts or its standing yes.
> 11. It is at most 900 words as counted by `wc -w CLAUDE.md`. It points at a file by path or heading wherever the reader can read that file, rather than restating it.
> 12. The working tree meets the bar.
