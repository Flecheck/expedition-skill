# The manager contract says three node states show in no file, while the stop skill derives each from the node's file

Type: implementation
Status: resolved
Blocked by: none

## Question

*Surfaced by [node 298](298-rewrite-the-manager-contract-part-3.md)'s worker, and filed by the manager as it wrote it.*

`SKILL.md`'s `### Three states nothing in the files shows` tells the manager to keep track of three states itself, because the files show them only as `claimed` or `open`. `expedition-stop/SKILL.md`'s `## Write no handoff document` says each of the three is derivable from the node's own file. Should the manager contract state the derivations?

## Acceptance condition

*Written by node 298's worker. Pasted as it wrote it, and not the manager's.*

In `.claude/skills/expedition/SKILL.md`, the section headed `### Three states nothing in the files shows` no longer states or implies that the three states cannot be read from the files. It states that each reads as `claimed` or `open` on the node's status line, and that each can be derived from the node's own file, as follows. Waiting at a gate: `claimed`, with a checker's outcome recorded and no gate outcome under it. A worker blocked on a raise: `claimed`, with a question recorded and no answer under it. Banked and waiting: `open`, with a non-empty interview. The section still tells the manager to report the first two without being asked, and the third when the human asks. The heading may be reworded. No other path changes. The working tree meets the bar.

## Answer

The manager contract's three-states section, renamed `### Three states the status line does not show`, now derives each state from the node's own file instead of saying the files cannot show them.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `4cc74de`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted.*

HANDOVER:      The manager contract says three node states show in no file

ANSWER:        The manager contract now states how to derive each of the three states from the node's own file, so it agrees with the stop skill. In `.claude/skills/expedition/SKILL.md`, under `## What is in front of the human, and when`, the section that was headed `### Three states nothing in the files shows` is now headed `### Three states the status line does not show`. The old heading said the files cannot show the three states, so it had to change. The section now says that each state reads as `claimed` or `open` on the node's status line, like any other node, and it tells the manager to derive each state from the node's own file:
                - Waiting at a gate for the human's approval: `claimed`, with a checker's outcome recorded and no gate outcome under it.
                - A worker blocked on a raise: `claimed`, with a question recorded and no answer under it.
                - Banked and waiting, meaning a parked node and its answers: `open`, with a non-empty `## Interview`.
                The instruction "Keep track of each state yourself" is gone, because it implied that the files cannot show the states. The reporting rule is unchanged: report the first two without being asked, and the third when the human asks. The third derivation names the `## Interview` section where the condition says "interview", because that is the section name `graph-conventions.md` gives in `## Statuses`. The first two derivations follow the condition's wording and name no section. No other path changed.

INDEX LINE:    The manager contract's three-states section, renamed `### Three states the status line does not show`, now derives each state from the node's own file instead of saying the files cannot show them.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none. One map passage is out of date and needs a new clause. See RE-POINTING SEARCH below.

GATE PAYLOAD:  Checker findings: none yet, because no checker has run.
               Paths touched: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/314-three-node-states/.claude/skills/expedition/SKILL.md`. Nothing else changed, and the change is uncommitted on `worktree-314-three-node-states`.
               The bar: the repo has no build, no tests, no formatter and no CI. I confirmed this against the repo, and it matches the record in `map-implementation-rules.md`. So the bar is its non-command half only: the project criteria, the ground rules and the five writing rules. I wrote to writing rule 5: no emphasis bold, rules stated as what to do, one idea per sentence.
               Proposed commit message:
                 Derive the three node states from the node's file in the manager contract

                 Node: graph-workflow/314

RE-POINTING SEARCH:
  Scope: the `## Acceptance condition` section, every `## Amendment…` section and every `### Amendment…` section of all 86 open and claimed nodes other than 314. My copy of node 293's script, at `$TMPDIR/n314/search.py` (`/tmp/claude-1000/n314/`), also catches `### Amendment` headings, and a non-amendment `###` heading does not end an acceptance condition. I ran all three modes: quoted spans, 6-word overlaps with the old section, and a phrase list.
  Phrases searched: "Three states nothing in the files shows", "nothing in the files shows", "Three states", "Keep track of each state yourself", "banked and waiting", "waiting at a gate", "blocked on a raise", "Report the first two", "Report the third when the human asks", and the parent heading "What is in front of the human, and when".
  Node results: none need a change.
  - 120 matches "three states", but it means the three states a message to an agent reports, which has nothing to do with this section.
  - 105 and 127 cite the parent heading `## What is in front of the human, and when`, which I did not change. Their demands are about other rules in that section: 105 about the one-question rule, its two tiers and its list of things that are not claimants; 127 about the payload rules. Neither quotes the three-states subsection.
  Shipped files: nothing under `.claude/` or in `CONTEXT.md` cites the old heading. `expedition-stop/SKILL.md` has the derivations but does not cite the heading.
  Map files: one match. `map-manager-only.md`, `## Not yet specified`, the item headed "Resume and recovery", reads: `that the **three states the manager's contract says "nothing in the files shows" are in fact derivable**:`. The contract no longer says this. Proposed replacement clause: `that the **three states the manager's contract then said "nothing in the files shows" are in fact derivable**, which its section `### Three states the status line does not show` now states:`. The passage is a record of a measurement, so under the map's rule for text that records what happened, the manager could instead mark it superseded where it stands.
  Side note, not a finding against this node: that same map passage says the gate derivation is "no `### Gate` entry". `graph-conventions.md` `### `## Review`` records the gate's outcome as an entry in `## Review`, with no `### Gate` heading.

RETROSPECTIVE:
  (1) What I hunted for: two things. First, the section names behind "a checker's outcome", "gate outcome" and "interview". I found them in `graph-conventions.md` under `### `## Review``, `### `## Interview`` and `## Statuses`, after first looking at the stop skill. Second, the trailer's effort name (`graph-workflow`). I found it in `git log`, because neither the contract nor the spawn gives it.
  (2) What I did not need: most of `map-implementation-rules.md`. Only the bar paragraph and writing rule 5 applied. I also read `map.md`'s grep hits only for the worktree paragraph. A spawn that quoted the worktree paragraph and the bar's result ("no commands; non-command half only") would have saved both reads.
  (3) What would have made this easier: the spawn naming the commit trailer's effort name; and the manager's notes saying which of the condition's terms map to which node-file sections, or saying that the condition's wording is enough without them. Node 293's script also needed changing to handle `###` amendments without dropping `###` subsections inside a condition. A shared, fixed copy of the script would save each worker from redoing that.
  (4) What was stale or wrong: `map-manager-only.md`'s "Resume and recovery" item. It quotes the old heading, and its `### Gate` entry does not match `graph-conventions.md` (both covered above).

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 301's check.*

> PASS
>
> Node 314, "The manager contract says three node states show in no file", meets its acceptance condition, and the bar holds. The work is a single rewrite of one section in the manager contract, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `.claude/skills/expedition/SKILL.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/314-three-node-states`, on branch `worktree-314-three-node-states`, based on `ec3c772`. I read the changed path only as the work. No list of rule changes was asked for this node, so none is given.
>
> **Part by part**
> 1. **The section no longer states or implies that the three states cannot be read from the files: met.**
>    - The heading went from `### Three states nothing in the files shows` to `### Three states the status line does not show`. That rewording is allowed, and the new heading makes a claim only about the status line.
>    - The before-text's "Keep track of each state yourself, so that you can report it" is gone. It now reads "Derive each state from the node's own file".
> 2. **Each state reads as `claimed` or `open` on the status line: met.** The section now opens: "A node in each of the three states below reads as `claimed` or `open` on its status line, like any other node."
> 3. **Each state can be derived from the node's own file, as specified: met.**
>    - "Waiting at a gate for the human's approval: `claimed`, with a checker's outcome recorded and no gate outcome under it."
>    - "A worker blocked on a raise: `claimed`, with a question recorded and no answer under it."
>    - "Banked and waiting, meaning a parked node and its answers: `open`, with a non-empty `## Interview`." The condition says "a non-empty interview". An interview is the record kept under the node's `## Interview` section, so this is the same requirement.
> 4. **Reporting duties kept: met.** The section still says "Report the first two without being asked. Report the third when the human asks.", unchanged.
> 5. **No other path changes: met.**
>    - `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition/SKILL.md` modified.
>    - The diff is confined to this section: the heading, the opening sentences and the three bullets.
>    - The old heading text is referenced nowhere else. I searched `.claude/`, `CONTEXT.md`, `.gitignore` and the main tree's map files. Only the new heading remains.
> 6. **The working tree meets the bar: met**, as below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the new text is plain and direct.
>   - `CONTEXT.md`'s `_Avoid_` lines: no refused word is introduced. "Interview", "banked" and "parked" are spelled as `CONTEXT.md` defines them.
>   - The derivations match word for word the ones the stop skill (`.claude/skills/expedition-stop/SKILL.md` at this base) gives for the same three states.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

*The manager's note:* the checker's item 5 says the old heading text remains nowhere in the main tree's map files. The worker's re-pointing search found it quoted in `map-manager-only.md`'s "Resume and recovery" item, as a quotation in lowercase ("nothing in the files shows"). The two do not conflict on the work, which touches only the shipped file. The map passage is the manager's to update at close.

### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*
