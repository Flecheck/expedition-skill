# Remove graph-conventions.md's limit on the human amending a held node's condition

Type: implementation
Status: resolved
Blocked by: none

## Question

*Surfaced by [node 311](311-may-the-human-amend-a-held-nodes-condition-of-their-own-accord.md)'s worker, and filed by the manager as it wrote it.*

Carry node 311's answer into the shipped files: the human may change any acceptance condition at any time, and an amended condition on a held node reaches its worker and any live checker.

*The worker's note on blockers:* "none. It edits the same two files as two other nodes, in different sections. Node 318 (open) edits `graph-conventions.md`'s node-file template code block under `## The node file`. Node 319 (claimed) edits `graph-conventions.md` `### Recording the human's words` and `SKILL.md` `### The human's words`. This node touches only `graph-conventions.md` `### \`## Acceptance condition\`` and `SKILL.md` `## The checker`, and reads `SKILL.md` `### Changing one after it is written`."

## Acceptance condition

*Written by node 311's worker. Pasted as it wrote it, and not the manager's.*

1. In `.claude/skills/expedition/graph-conventions.md`, under the heading `### \`## Acceptance condition\``, the two sentences "The human changes only a condition on a node nobody holds yet." and "A condition under a live worker reaches the human by that worker's raise, and by no other route." are removed. Nothing is written in their place that says or implies that the human may change only a condition on a node nobody holds yet, or that a held node's condition reaches the human only by its worker's raise. The sentence before them, "`## Acceptance conditions` in `SKILL.md` says who writes it and who may change it after it is written.", stays as it is. `grep -niE "nobody holds|no other route|live worker" .claude/skills/expedition/graph-conventions.md` returns nothing.
2. In `.claude/skills/expedition/SKILL.md`, under the heading `## The checker`, the two sentences "Where the human amends a condition while a check is live, tell the checker. The amended text is then the whole condition." are replaced where they stand. The replacement, addressed to the manager as *you* like the rest of the file, says three things. Where the human amends the condition of a node a worker already holds, you pass the amended text to that worker. Where a check is also live, you pass it to the checker too. The amended text is then the whole condition. The replacement is stated once, and the rule is not restated anywhere else in the file.
3. In `.claude/skills/expedition/SKILL.md`, under `### Changing one after it is written`, the sentences "The amendments in this section, by the party that established a fact and by you, apply only to a node nobody holds yet." and "The human may also amend a condition of their own accord at any time." are unchanged.
4. No other text in either file changes, no heading in either file changes, and no other path changes.

## Answer

graph-conventions.md no longer limits the human to amending unheld conditions; SKILL.md's checker section now has the manager pass a held node's amended condition to its worker and any live checker.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `f630aa3`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Remove graph-conventions.md's limit on the human amending a held node's condition

ANSWER:
The limit on the human is gone from `graph-conventions.md`, and `SKILL.md` now names the worker as well as the checker as the ones who receive an amended condition.

- `.claude/skills/expedition/graph-conventions.md`, `### \`## Acceptance condition\``: I removed two sentences, "The human changes only a condition on a node nobody holds yet." and "A condition under a live worker reaches the human by that worker's raise, and by no other route." Nothing replaces them. The paragraph now ends on the pointer sentence, "`## Acceptance conditions` in `SKILL.md` says who writes it and who may change it after it is written.", which is unchanged apart from where its line breaks. This follows node 312's split: rules about who may change a condition live in `SKILL.md`, and `graph-conventions.md` points to them.
- `.claude/skills/expedition/SKILL.md`, `## The checker`: I replaced "Where the human amends a condition while a check is live, tell the checker. The amended text is then the whole condition." where it stood with: "Where the human amends the condition of a node a worker already holds, you pass the amended text to that worker. Where a check is also live, you pass the amended text to the checker too. The amended text is then the whole condition."
- In the second sentence I repeated "the amended text" instead of writing "it", so that the sentence has only one possible referent. I wrote "you pass" explicitly instead of a bare imperative, because the condition asks for the text to be addressed to the manager as *you*.
- `### Changing one after it is written` is unchanged. It still limits the party and the manager to nodes nobody holds, and still says "The human may also amend a condition of their own accord at any time." The rule is stated once, in `## The checker`. I grepped `SKILL.md` for "amend" and found no other statement of it.

INDEX LINE:    graph-conventions.md no longer limits the human to amending unheld conditions; SKILL.md's checker section now has the manager pass a held node's amended condition to its worker and any live checker.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none. This carries out node 311's answer. Node 311 already recorded how this contradicts part of node 95's landed work (flag 95.3's boundary applied to the human).

GATE PAYLOAD:
Checker findings: none yet.
Paths touched, both in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/321-human-amends-held-condition`, uncommitted:
- `.claude/skills/expedition/graph-conventions.md`
- `.claude/skills/expedition/SKILL.md`
`git diff --stat` shows 2 files, 4 insertions and 5 deletions. No heading changed.

The bar: the repo has no build, tests, formatter or CI. I found none, which matches `map-implementation-rules.md`, so the bar is its non-command half only. Checks I ran:
- `grep -niE "nobody holds|no other route|live worker" .claude/skills/expedition/graph-conventions.md` in the worktree returns nothing (exit 1).
- The new lines are 104 characters or fewer, which matches the neighbouring wrap width.

Re-pointing search, commands run from the repo root:
- `python3 .scratch/graph-workflow/scripts/search-conditions.py 321 f403975:.claude/skills/expedition/SKILL.md .scratch/graph-workflow/worktrees/321-human-amends-held-condition/.claude/skills/expedition/SKILL.md`. It searched 88 conditions. The only GONE results were the two known false n-gram runs ("is in front of the human at a time", "what is in front of the human at"). No quoted span is GONE.
- `python3 .scratch/graph-workflow/scripts/search-conditions.py 321 f403975:.claude/skills/expedition/graph-conventions.md .scratch/graph-workflow/worktrees/321-human-amends-held-condition/.claude/skills/expedition/graph-conventions.md`. It searched 88 conditions and reported no GONE result.
- To catch conditions whose demand is a property, I grepped every open or claimed node file for `nobody holds|no other route|live worker|tell the checker|check is live|amends a condition|whole condition|worker's raise|amend.*held|held node`. Three nodes matched, all unrelated:
  - 323: "an older blocked worker's raise", in the tier 1 order text.
  - 309: its own clause heading "The whole condition".
  - 81: a quote about the code slot being "held".
- No open condition quotes the removed text, so I propose no replacement clauses and no supersessions.

Proposed commit message:
```
Let the human amend a held node's condition, and pass it to the worker

graph-conventions.md no longer limits the human to conditions on nodes
nobody holds, and no longer says a held condition reaches the human only
by its worker's raise. SKILL.md's checker section now has the manager
pass the amended text to the worker holding the node, and to a live
checker too.

Node: graph-workflow/321
```

RETROSPECTIVE:
(1) What I had to hunt for: nothing of substance. The node file quotes the exact sentences and headings. The one extra search was the property grep of open conditions. I built its pattern from the removed sentences myself, and then had to check what each of the three hits meant. The `ugrep` complexity error on a `.{0,160}` context pattern cost one retry.
(2) What arrived that this node did not need:
- Node 311's whole file, including its interview and retrospective. Only its `## Answer` and its flag 311.1, which gives the placement reason, bore on the work.
- The search script's full output, 37 KB for two runs, of which only the GONE lines mattered.
- A `--gone-only` flag on the script, or a spawn that says "grep the output for GONE", would have avoided reading the rest.
(3) What would have made it easier: nothing much. The condition was precise enough to act on directly. A ready-made list of grep terms for the property search, taken from the removed sentences, would have saved composing one.
(4) Stale, wrong or contradicting: nothing found. Clause 1 says the pointer sentence "stays as it is". Removing the next sentences changes only where its line breaks, not its words. I read that as consistent with the clause.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 302's check.*

> PASS
>
> Node 321, "Remove graph-conventions.md's limit on the human amending a held node's condition", meets all four parts of its acceptance condition, and the bar holds. The work is one sentence group removed from `graph-conventions.md` and one replaced in `SKILL.md`, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/321-human-amends-held-condition`, on branch `worktree-321-human-amends-held-condition`, based on `f403975`. I read the changed paths only as the work. No list of rule changes was asked for this node, so none is given.
>
> **Part by part**
> 1. **`graph-conventions.md`, under `### `## Acceptance condition``: met.**
>    - The two sentences are removed: "The human changes only a condition on a node nobody holds yet." and "A condition under a live worker reaches the human by that worker's raise, and by no other route."
>    - Nothing is written in their place.
>    - The sentence before them stays as it was: "`## Acceptance conditions` in `SKILL.md` says who writes it and who may change it after it is written."
>    - I ran the recorded command as written: `grep -niE "nobody holds|no other route|live worker" .claude/skills/expedition/graph-conventions.md` returns nothing, with exit status 1. That matches the condition.
>    - No other sentence in the file says or implies either limit. I searched unwrapped for amend, "who may change" and raise. The only hits are the pointer sentence above and the unrelated `CONDITION-WRONG` and checker-raise lines.
> 2. **`SKILL.md`, under `## The checker`: met.**
>    - The two sentences "Where the human amends a condition while a check is live, tell the checker. The amended text is then the whole condition." are replaced where they stood.
>    - The replacement is addressed to the manager as *you*: "Where the human amends the condition of a node a worker already holds, you pass the amended text to that worker. Where a check is also live, you pass the amended text to the checker too. The amended text is then the whole condition." It says all three required things.
>    - It is stated once. I searched `SKILL.md` unwrapped for "amend", and every other hit is part of the unchanged `### Changing one after it is written` rules. None of those restates passing the amended text to the worker or the checker.
> 3. **`SKILL.md`, under `### Changing one after it is written`: met.** Both sentences are present, unchanged and under that heading:
>    - "The amendments in this section, by the party that established a fact and by you, apply only to a node nobody holds yet."
>    - "The human may also amend a condition of their own accord at any time."
> 4. **No other text, heading or path changes: met.**
>    - `git diff` touches only the two passages above. That is 4 insertions and 5 deletions in total.
>    - The headings in both files are identical to the before-text.
>    - `git status --porcelain --untracked-files=all` shows only the two named files modified.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the replacement is plain and states its rule positively.
>   - `CONTEXT.md`'s `_Avoid_` lines: no refused word is introduced.
>   - `graph-conventions.md`, which is itself part of the work.
>   - All five ground rules, which are met. The replacement routes the amended text through the manager.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*
