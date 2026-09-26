# Four worker contracts say `map.md` holds the fog

Type: implementation
Status: resolved
Blocked by: 290, 291, 292, 293

## Question

The shipped `graph-conventions.md` puts `## Not yet specified — the fog` in `map-manager-only.md`, which no worker reads. The `## What you read` bullet in the grilling, precondition, prototype and research contracts still reads "`map.md` — the destination, the standing preferences, the fog".

*Reported by [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker, whose note for the manager reads: "Node 155's clause 3 ("no existing bullet is reworded") would collide with this if 155 is claimed afterwards. Re-point one of the two."*

## Acceptance condition

*Authored by node 290's worker and filed by the manager.*

1. In each of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-research/SKILL.md`, the `## What you read` bullet naming `map.md` names the destination and the standing preferences, and does not name the fog.
2. Enumerator: `grep -rln "the standing preferences, the fog" .claude/` returned exactly those four paths at `e5c03a5`, and after the work it returns nothing.
3. Nothing else in the four files changes, and no other file changes.
4. The tree meets the bar.

## Answer

The grilling, precondition, prototype and research contracts' `map.md` bullet now names only the destination and the standing preferences, as the implementation contract's does; the fog is in `map-manager-only.md`.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `ec3c772`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted.*

HANDOVER:      Four worker contracts say `map.md` holds the fog

ANSWER:        In the `## What you read` section of `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md` and `.claude/skills/expedition-research/SKILL.md`, the bullet "`map.md` — the destination, the standing preferences, the fog" now reads "`map.md` — the destination and the standing preferences". The fog is in `map-manager-only.md`, which no worker reads, so the bullet no longer names it. The new text is byte-identical to the same bullet in `.claude/skills/expedition-implementation/SKILL.md`, so all five worker contracts now describe `map.md` the same way. No other line in the four files changed.
                The enumerator `grep -rln "the standing preferences, the fog" .claude/` returned exactly the four paths at `e5c03a5` (checked with `git grep` at that commit) and at the base `6d26be1`. After the change it returns nothing (exit 1).
                The bar: the repo has no build, no tests, no formatter and no CI. The worktree root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`, and `.gitignore` invokes nothing. This matches the record in `map-implementation-rules.md`. `git diff --check` is clean. The new bullet is a plain noun phrase, so it meets standing writing rule 5.
                Re-pointing search: no open or claimed node other than 304 quotes the bullet or the phrase in its `## Acceptance condition` or in any `## Amendment` or `### Amendment` section. No replacement clause or supersession is owed.

INDEX LINE:    The grilling, precondition, prototype and research contracts' `map.md` bullet now names only the destination and the standing preferences, as the implementation contract's does; the fog is in `map-manager-only.md`.

FLAGS:         none

NEW NODES:     none. The related defect in `graph-conventions.md`, which still says "Every note, standing preference and fog item in `map.md`", is already node 195 ("graph-conventions still puts the fog…"), which is open.

INVALIDATIONS: none

GATE PAYLOAD:  Checker findings: none yet.
                Paths touched, all in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/304-map-md-holds-the-fog`, uncommitted, one line each:
                  .claude/skills/expedition-grilling/SKILL.md
                  .claude/skills/expedition-precondition/SKILL.md
                  .claude/skills/expedition-prototype/SKILL.md
                  .claude/skills/expedition-research/SKILL.md
                Proposed commit message:
                  Stop four worker contracts saying `map.md` holds the fog

                  The fog lives in map-manager-only.md, which no worker reads. The grilling,
                  precondition, prototype and research contracts' `map.md` bullet now matches
                  the implementation contract's.

                  Node: graph-workflow/304

RE-POINTING SEARCH (the addition your spawn asked for)
- Method: I copied node 293's script to `$TMPDIR/n304/search.py`, which excludes 304 instead of 293. Its `before.md` is the research contract at `6d26be1` and its `after.md` is my edited version. It collects every `## Acceptance condition` and `## Amendment…` section, wherever it sits, of every node with Status `open` or `claimed`. That is 87 nodes with sections, from the 140 open and 2 claimed nodes other than 304.
- Phrases searched in `phrases` mode: the full bullet; "the standing preferences, the fog"; "standing preferences, the fog"; "the destination, the standing preferences". Result: no hits.
- `quotes` and `ngram` modes, filtered for "fog" or "standing pref": no hits.
- Extra check: 293's script only matches `## ` headings, and two nodes use `### Amendment`. I re-ran a scan that accepts any heading level and looks for "fog", "standing preferences" or "What you read". The hits are 111, 148, 155, 190, 195 and 80. None of them quotes the bullet. They mention standing preferences in other senses, fog items in `map.md` or `graph-conventions.md`, or, in 155's case, the `## What you read` opener and the decisions bullet, which this node leaves alone.
- Handles searched (open/claimed with at least one such section): 101, 105, 106, 109, 111, 118, 120, 124, 127, 134, 137, 146, 148, 149, 151, 152, 153, 155, 156, 159, 160, 161, 164, 173, 186, 190, 195, 201, 202, 205, 206, 208, 209, 210, 211, 214, 219, 220, 221, 226, 228, 230, 231, 232, 233, 234, 236, 237, 247, 254, 256, 258, 271, 276, 278, 279, 280, 284, 285, 286, 287, 288, 301, 302, 307, 309, 314, 318, 41, 43, 44, 49, 56, 57, 60, 61, 73, 79, 80, 81, 87, 88, 89, 90, 92, 96, 97.
- A whole-directory grep for the phrase also hits 114, 215, 224, 291, 292, 293, 296 and 53. All of them are resolved, so they are out of scope.
- Node 155's clause 3: I read it the same way you do. It governs only node 155's own diff and does not bind this node.

RETROSPECTIVE
1. What I had to hunt for: (a) Whether `e5c03a5`, named in clause 2, is an ancestor of the base `6d26be1`. I checked with `git merge-base --is-ancestor` and it is. (b) Which wording to use. I found it in the implementation contract's own `## What you read` bullet, which I had already read as my contract. (c) The bar's commands. The rules file had them, and I confirmed them with `ls -a` of the worktree and `.gitignore`. (d) Whether any open node already covered `graph-conventions.md`'s "fog item in `map.md`" sentences. The search itself surfaced node 195. I had first looked at `graph-conventions.md` directly.
2. What arrived that I did not need: most of `map-implementation-rules.md`, meaning the review-route and record-as-work paragraphs, and the whole `map.md` grep. Only the bar paragraph and writing rule 5 mattered. A spawn that pastes the bar's current commands and rule 5 inline for a four-line mechanical edit would have avoided the reads. Your spawn mostly did this already.
3. What would have made it easier: a spawn or node note naming the target wording. For example: "use the implementation contract's bullet, `map.md` — the destination and the standing preferences". Also, 293's search script only catches `## Amendment` headings. The effort has two `### Amendment` headings, so the shared script should accept any heading level.
4. Stale, wrong or contradictory: `graph-conventions.md` says under its file-layout section that the fog is in `map-manager-only.md`. The same file, under `## Writing the map`, says "Every note, standing preference and fog item in `map.md`", and the "Use this when a note, standing preference or fog item in `map.md`" passage says the same. That contradiction is already node 195. Clause 2 of node 304 names `e5c03a5` while the spawn names `6d26be1` as the base. Both are correct, but the mismatch cost a check.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-25. The checker was resumed from node 293's check.*

> PASS
>
> Node 304, "Four worker contracts say `map.md` holds the fog", meets all four parts of its acceptance condition, and the bar holds. The work is one identical one-line edit in each of the four named files, nothing else changed, and the condition's recorded search matches both of its recorded returns.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/304-map-md-holds-the-fog`, on branch `worktree-304-map-md-holds-the-fog`, based on `6d26be1`. I read the changed paths only as the work. No list of rule changes was asked for this node, so none is given.
>
> **Part by part**
> 1. **The `map.md` bullet no longer names the fog: met.** In each of `expedition-grilling`, `expedition-precondition`, `expedition-prototype` and `expedition-research`, `SKILL.md`, the `## What you read` bullet changed:
>    - Before: "`map.md` — the destination, the standing preferences, the fog"
>    - After: "`map.md` — the destination and the standing preferences"
>
>    I also searched each file unwrapped for "fog", and no occurrence remains in any of the four.
> 2. **The recorded search: met.** I ran it as written.
>    - `grep -rln "the standing preferences, the fog" .claude/` in the worktree now returns nothing, with exit status 1. That matches the recorded return after the work.
>    - `git grep -l "the standing preferences, the fog" e5c03a5 -- .claude/` returns exactly the four named paths. That matches the recorded return at `e5c03a5`.
>    - At the branch base `6d26be1` it also returns exactly those four paths.
> 3. **Nothing else changes: met.**
>    - `git status --porcelain --untracked-files=all` shows only the four named files modified, with no untracked files.
>    - `git diff --numstat` shows exactly 1 line removed and 1 added in each file, and the full diff is that one bullet in each.
>    - The edited bullet is outside the shared sections `## When you raise a flag` and `## When a node you report is an implementation node`. Those sections remain identical across the four files.
> 4. **The tree meets the bar: met**, as below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English). The new wording is plain, and it matches the implementation contract's own bullet, "`map.md` — the destination and the standing preferences".
>   - `CONTEXT.md`'s `_Avoid_` lines: no refused word is introduced.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-25

The human, `verbatim`: *"approve"*
