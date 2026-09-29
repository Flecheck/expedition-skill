# Carry node 162's integration answer into the shipped files

Type: implementation
Status: claimed
Blocked by: none

## Question

Carry node 162's answer into the shipped files. Each landing policy must state what happens when integration conflicts, and a correction round may be started by the manager at integration.

*Reported by [node 162](162-how-much-of-the-integration-rule-ships.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 162's worker and filed by the manager.*

> 1. `.claude/skills/expedition/graph-conventions.md`: the bullet that begins `` - `## Landing an implementation node's work` — the landing policy: `` also says that the policy covers what happens when integrating a node's work conflicts. It becomes: "where a node's worker works, what one path-limited commit of that node's paths takes, what happens to the worker's tree on each of the gate's three outcomes, and what happens when integrating the node's work conflicts." The bullet's closing sentence, "Landing is the manager's, so neither a worker nor its checker reads this section.", is unchanged. No other sentence of the file changes, and the file names no version-control command it did not name before.
> 2. `.claude/skills/expedition-implementation/SKILL.md`, under `## Words used exactly`: the entry `- **correction round** — one cycle of the human saying what is wrong and you fixing it.` becomes `- **correction round** — one cycle of being told what is wrong, by the human at the gate or by the manager when integrating your work conflicts, and you fixing it.`
> 3. The same file, in the code block under `## After the code is written`: the line `→ approve → the manager commits; your node resolves` becomes a branch saying, in these words: `→ approve → the manager lands your work; where integrating it conflicts, you may be resumed to fix the conflicted files in place, running no git command, and the checker and the gate run again`. It may wrap over indented continuation lines inside the block. The `correct` and `reject` lines are unchanged.
> 4. The same file, near the top: the sentence `You hold a code slot from your first edit until the human has approved your work.` becomes `You hold a code slot from your first edit until your work has landed or been rejected.`
> 5. The same file, under the `In a correction round:` list: the bullet beginning `You receive the human's words exactly as they said them.` keeps its existing text and gains one sentence, `In a round the manager starts when integrating your work conflicts, you receive the conflicted files instead, and you fix them in place.`
> 6. `.claude/skills/expedition/glossary.md`, entry `**Correction round**:`: its first sentence, `One cycle of the human saying what is wrong and the worker fixing it, while the node stays claimed.`, becomes `One cycle of being told what is wrong, by the human at the gate or by the manager when integrating the work conflicts, and the worker fixing it, while the node stays claimed.` The entry's other sentences and its `_Avoid_` line are unchanged.
> 7. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
> 8. Scope. The command `grep -rn -E 'saying what is wrong|your node resolves|until the human has approved your work|You receive the human.s words exactly' .claude/skills/`, run over the working tree before this node, returned exactly five lines: `expedition-implementation/SKILL.md` for the code-slot sentence, the correction-round entry, the approve line and the correction-round bullet, and `glossary.md` for the `Correction round` entry. Clauses 2 to 6 cover all five. The `graph-conventions.md` clause came from no search, because the place is the work. After the work, the same command returns no line saying that only the human starts a correction round or that the node resolves at approval. An instance the command reaches outside this list is reported and not edited.

## Handover, attempt 1

*The worker's own text, pasted, 2026-09-29.*

````
HANDOVER:      Carry node 162's integration answer into the shipped files

ANSWER:        The shipped files now carry node 162's answer. Every landing policy covers what happens when integrating a node's work conflicts, and a correction round can be started by the manager at integration, not only by the human at the gate. There are six edits, each worded exactly as its clause gives it.
               - `.claude/skills/expedition/graph-conventions.md`, the `## Landing an implementation node's work` bullet: it now lists "…on each of the gate's three outcomes, and what happens when integrating the node's work conflicts." The closing sentence is unchanged and no version-control command was added. The paragraph was re-wrapped only inside that bullet.
               - `.claude/skills/expedition-implementation/SKILL.md` has four edits:
                 - The code-slot sentence now reads "until your work has landed or been rejected". The next sentence was re-wrapped by one word.
                 - The `correction round` entry under `## Words used exactly` now takes the new wording. It wraps with the list's two-space indent.
                 - In the `## After the code is written` diagram, the approve line reads "→ approve → the manager lands your work; where integrating it conflicts, you may be resumed to fix the conflicted files in place, running no git command, and the checker and the gate run again". It wraps over two indented continuation lines lined up under the text after `approve →`. The `correct` and `reject` lines are unchanged.
                 - The first bullet of `In a correction round:` keeps its text and gains the sentence "In a round the manager starts when integrating your work conflicts, you receive the conflicted files instead, and you fix them in place."
               - `.claude/skills/expedition/glossary.md`, `**Correction round**:`: the first sentence is replaced as clause 6 words it. It wraps over two lines with no indent, as the glossary's other entries do. The other sentence and the `_Avoid_` line are unchanged.
               Clause 8's search, re-run over the worktree before the edit, returned the five listed lines. After the edit it returns one line: `expedition-implementation/SKILL.md`, the "You receive the human's words exactly…" bullet. Clause 5 requires that bullet's text to stay. The line does not say that only the human starts a round, and the added sentence on the bullet's continuation line says the manager may start one. So the clause-8 post-condition holds. No instance outside the list was reached.

INDEX LINE:    The implementation contract, glossary and graph-conventions now say that a correction round may be started by the manager when integration conflicts, and that the code slot is held until landing or reject.

FLAGS:         none

NEW NODES:     Name: Say what a `## Review` entry records for a correction round the manager starts at integration
               Kind: implementation
               Question: `graph-conventions.md`'s `## Review` section, item 2, says each correction round is recorded "with the human's words and what the worker changed". A round the manager starts when integrating the work conflicts has no human's words. What does its entry record instead?
               Blockers: none
               Acceptance condition (the wording of what is recorded is this worker's proposal and nothing resolved fixes it; the human may choose otherwise):
               > 1. `.claude/skills/expedition/graph-conventions.md`, in the numbered list under the `## Review` section, item 2 (beginning "Each correction round, numbered, with the human's words and what the worker changed."): it now also says that for a round the manager starts when integrating the node's work conflicts, the entry records the paths of the conflicted files in place of the human's words. The item's second sentence, about how the human's words are recorded, is unchanged.
               > 2. No other sentence of any file under `.claude/skills/` changes, and no file under `.scratch/` changes.
               > 3. Scope: this came from no search, because the place is the work.
               It was not joined to an open node. The one open condition that names `## Review` in this file is node 368's, and it concerns pointers in `### Recording the human's words`, which is a different concern.

INVALIDATIONS: Node 162 is extended, not contradicted: its answer now stands in the shipped files. Node 11's index line ("the manager commits one path-limited commit per implementation node, after the human approves it") and node 68's ("a conflict aborts into a correction round") have already been narrowed by node 160. This work makes the implementation contract agree with node 160, and it contradicts no resolved node.

CONDITIONS:    Searched for: "saying what is wrong", "node resolves", "approved your work", "correction round", "commits; your", "human's words exactly", "Landing an implementation node's work", "three outcomes" and "code slot from". I searched the `## Acceptance condition` and `## Question` sections of all 64 open or claimed nodes.
               - Node 34 (open, grilling): its question quotes the old diagram line `→ approve → the manager commits; your node resolves` under "What is shipped today". That quotation is now stale. Node 162's worker predicted this and the manager noted it on node 34 on 2026-09-28. The question itself is unchanged in substance, and only the quoted line needs updating to the new approve branch.
               - Node 370 (open): it shares `glossary.md` with this node but not the `Correction round` entry. No clause changes.
               - Nodes 209 and 276 match `## Landing an implementation node's work` only as the heading in `map-manager-only.md`, which this work does not touch. No change.
               - The other matches (190, 219, 65, 51, 40, 85, 78, 84) use "correction round" or "node resolves" in their ordinary sense, and nothing in them is made wrong.
               No replacement clauses are written.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet (no checker has run).
               Paths touched:
                 .claude/skills/expedition-implementation/SKILL.md
                 .claude/skills/expedition/glossary.md
                 .claude/skills/expedition/graph-conventions.md
               Bar: the repo has no build, tests, formatter or CI. The worktree root holds only `.claude/`, `CONTEXT.md`, `CONTEXT-MAP.md`, `.gitignore` and `.scratch/`, with no manifest and no command file. This matches `map-implementation-rules.md`'s record, with no difference to report. The bar is therefore its non-command half: the standards, the ground rules, the six writing rules, the `_Avoid_` lines, `graph-conventions.md` and the acceptance condition. No refused word was introduced.
               Proposed commit message:
                 Carry node 162's integration answer into the shipped files

                 The implementation contract, the glossary's Correction round entry and
                 graph-conventions.md's landing-policy bullet now say that a correction
                 round may be started by the manager when integration conflicts, that
                 the worker then fixes the conflicted files in place, and that the code
                 slot is held until the work lands or is rejected.

                 Node: graph-workflow/363

RETROSPECTIVE
1. What I had to hunt for: nothing for the work itself, because the condition quoted every before and after text. I searched the open nodes for the CONDITIONS part, and I checked whether any open node already covered `## Review` item 2, which produced the NEW NODES entry.
2. What arrived that this node did not need: nearly all of `decisions.md`, about 80KB. Only node 162's and node 360's lines mattered. Most of `map.md` and `map-implementation-rules.md` bore on nothing here either, beyond the bar paragraph and the writing rules.
3. What would have made this easier: a spawn naming only the `decisions.md` lines that bear on the node, which the contract already allows ("the sections the spawn names"). The spawn said "the index of decisions" without naming sections, so I read all of it.
4. What was stale, wrong or contradictory: clause 8 says "after the work, the same command returns no line saying that only the human starts…". Clause 5 requires the bullet to keep its text, so the command still returns that bullet's first line. The clause holds only because it is worded as "no line saying…" rather than "no line". I report the wording but do not dispute the clause. Separately, `graph-conventions.md`'s `## Review` item 2 still assumes every correction round has human's words; it is reported under NEW NODES.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-29. A fresh checker, under the human's ruling that a checker is resumed within its own node only; the condition reached it as a verbatim copy in `$TMPDIR/c363.md`.*

> PASS
>
> Node 363, "Carry node 162's integration answer into the shipped files". Worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/363-integration, uncommitted diff against 77c5b60.
>
> Method: I flattened each changed file into one line (`tr '\n' ' ' | tr -s ' '`) and ran `grep -cF` for each exact target string the condition dictates. I read the diff to confirm that nothing else moved. I read the three changed paths as the work under check.
>
> Condition, one line per clause:
> 1. graph-conventions.md, Landing bullet. `grep -cF` on the flattened file for the whole new bullet, from "- `## Landing an implementation node's work` — the landing policy: where a node's worker works, ..." through "...and what happens when integrating the node's work conflicts. Landing is the manager's, so neither a worker nor its checker reads this section." returned 1. The diff's only hunk in this file is that bullet, rewrapped. The diff adds no version-control command.
> 2. The correction round entry in the implementation SKILL.md. `grep -cF` for the exact new entry returned 1, and the old entry is gone per the diff.
> 3. The approve line. `grep -cF` for "→ approve → the manager lands your work; where integrating it conflicts, you may be resumed to fix the conflicted files in place, running no git command, and the checker and the gate run again" returned 1. It wraps over indented continuation lines inside the block. `grep -cF` for the unwrapped "→ correct → ..." and "→ reject → ..." lines each returned 1, and the diff leaves them untouched.
> 4. The code-slot sentence. `grep -cF` for "You hold a code slot from your first edit until your work has landed or been rejected." returned 1. Its paragraph was rewrapped, and a flat comparison shows no other word moved.
> 5. The correction-round bullet. `grep -cF` for the old text plus "In a round the manager starts when integrating your work conflicts, you receive the conflicted files instead, and you fix them in place." returned 1.
> 6. The glossary Correction round entry. `grep -cF` for the new first sentence, followed by the unchanged "The number of rounds has no limit. A correction round is not a revision, and it is not a check. _Avoid_: review round, iteration, revision", returned 1.
> 7. No other file changed. `git status --short --ignored --untracked-files=all` in the worktree lists only the three modified paths, excluding the ignored worktrees directory. `git diff --stat 77c5b60` shows 3 files, 14 insertions and 9 deletions. Nothing under `.scratch/` changed, and none of the manager's bookkeeping files is among the work.
> 8. Scope search. I ran the command as written. At 77c5b60, via `git grep` with the same regex over `.claude/skills/`, it returns exactly the five recorded lines: SKILL.md lines 16, 36, 178 and 193, and glossary.md line 339. That matches the recorded return. On the working tree it returns one line, expedition-implementation/SKILL.md:196, "- You receive the human's words exactly as they said them...". Clause 5 requires that bullet to keep this text. Unwrapped, the bullet now also covers the round the manager starts, so it does not say that only the human starts a correction round. No line says the node resolves at approval. The command reaches no instance outside the list.
>
> The bar:
> - Commands: the repo has no build, no tests, no formatter and no CI. map-implementation-rules.md records this, and the worktree root holds no manifest or agent-instruction file. So the bar is its non-command half.
> - `git diff --check` printed nothing, so there are no whitespace errors.
> - Line widths of the added lines stay within each file's existing width (at most about 104 characters on added lines).
>
> Standards: I read only the standards in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md. They are:
> - `/coding-principles` and `/naming`
> - glossary.md's `_Avoid_` lines
> - the ground rules and the six standing rules for writing, as I was given them
> - graph-conventions.md
> - `/writing-for-agents`
> - the rule for record paths as work
>
> That file names no reviewing skill, so I invoked none and held the work against these standards by hand.
>
> The ones that bore on this work:
> - `_Avoid_` lines. No refused term is introduced: "landing commit" is not used, and "rejected" is the human's gate outcome, which the Checker entry's `_Avoid_` reserves to the human.
> - Ground rule 3. Nothing tells an agent to address the human.
> - Ground rule 1. No repo, machine or toolchain is assumed. "running no git command" is a prohibition dictated by the condition.
> - Writing rules 5 and 6 and `/writing-for-agents`. All added text is the condition's dictated wording, and there is no line-number citation.
>
> `/coding-principles` and `/naming` do not bear, since the change is prose only. I found no breach.
>
> Not checked: nothing in the condition was left uncovered.

### Gate — approve, `standing yes`, 2026-09-29

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and left no part of the condition uncovered. The node raised no flags.
