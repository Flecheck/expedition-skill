# Say what a `## Review` entry records for a correction round the manager starts at integration

Type: implementation
Status: resolved
Supersedes: 89
Blocked by: none

## Answer

graph-conventions.md's `## Review` item 2 now records the conflicted files' paths for a manager-started integration round; SKILL.md cleans up a superseded unlanded implementation node in a reject's order.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `4bce1411`. Flag 89.1, carried here from node 89, settles at the node closing report. The worker reports that the glossary's Reject entry says "deletes its branch", a git-specific term outside this node's scope.

## Question

`graph-conventions.md`'s `## Review` section, item 2, says each correction round is recorded "with the human's words and what the worker changed". A round the manager starts when integrating the work conflicts has no human's words. What does its entry record instead?

*Reported by [node 363](363-carry-node-162s-integration-answer-into-the-shipped-files.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none".*

## Acceptance condition

*Authored by node 363's worker and filed by the manager. The worker's words: "the wording of what is recorded is this worker's proposal and nothing resolved fixes it; the human may choose otherwise".*

> 1. `.claude/skills/expedition/graph-conventions.md`, in the numbered list under the `## Review` section, item 2 (beginning "Each correction round, numbered, with the human's words and what the worker changed."): it now also says that for a round the manager starts when integrating the node's work conflicts, the entry records the paths of the conflicted files in place of the human's words. The item's second sentence, about how the human's words are recorded, is unchanged.
> 2. ~~No other sentence of any file under `.claude/skills/` changes, and no file under `.scratch/` changes.~~ *Superseded 2026-09-29 by node 366's replacement; see `## Amendment, 2026-09-29 (from node 366)`.*
> 3. Scope: this came from no search, because the place is the work.

## Amendment, 2026-09-29 (from node 366)

*Written by [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s worker and filed by the manager, under the human's answer to node 366's Q3 (`verbatim`: *"ok"*). The worker's own text, pasted:*

Block 4 (defect joined to open node 371, from node 89, clauses originally from node 275). Clauses to add to 371's acceptance condition:
  - `.claude/skills/expedition/SKILL.md` also states what happens to the working state of an implementation node that is superseded while its work has not landed. The graph is edited first. After that, the node's tree, and anything else that holds its unlanded work, is removed, in the same order the file gives for a reject. The file states this as properties rather than as commands of any one version-control tool, and names no command that a repository without that tool could not run.
  - The line in `.claude/skills/expedition/SKILL.md` that reads "reject: edit the graph first, and clean the working state after." still states the reject outcome in the same order: the graph first, the working state after.
  - Scope came from no search: the file named is the place of the work, not an instance of a defect.
  Replacement for 371's clause 2: "No other sentence of any file under `.claude/skills/` changes, except the sentences of `.claude/skills/expedition/SKILL.md` that the clauses carried from node 89 require, and no file under `.scratch/` changes."

## Flags carried here

*The manager's note, 2026-09-29:* flag 89.1, on [node 89](89-carry-worktree-lifecycle-into-managers-contract.md), judges the clauses this node took from node 89 ("Node 275's clean-up clauses were filed on this open, unclaimed node without asking the human first"). It stays outstanding on node 89 and settles at this node's gate.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Say what a `## Review` entry records for a correction round the manager starts at integration
ANSWER:        Two edits in the shipped files, both left uncommitted in worktree `.scratch/graph-workflow/worktrees/371-review-entry`.
               (1) `.claude/skills/expedition/graph-conventions.md`, `### `## Review``, numbered item 2. One sentence is appended after the item's existing two sentences, which are byte-identical: "For a round the manager starts when integrating the node's work conflicts, the entry records the paths of the conflicted files in place of the human's words."
               (2) `.claude/skills/expedition/SKILL.md`, `## The gate` > `### Three outcomes, and no fourth`. A new paragraph is placed after the paragraph that ends "...takes as the human's approval." and before `### What reject means`: "An implementation node superseded before its work has landed is cleaned up in the same order as a reject. Edit the graph first. Then remove the node's working tree, and anything else that holds that work."
               Calls a later reader would otherwise have to re-derive:
               - The supersession paragraph sits beside the paragraph that already fixes "the graph before the cleanup", so "the same order as a reject" points at text right above it.
               - It is stated as properties ("working tree", "anything else that holds that work") and names no branch and no git command, following ground rule 1. The glossary's **Reject** entry still says "deletes its branch". That entry is outside this node's clause 2 and was left as it is.
               - The line "- reject: edit the graph first, and clean the working state after." is unchanged.
               - The new paragraph is not under `## The order you act in` or `## What is in front of the human, and when`, so `.claude/rules/expedition-triggers.md` needs no matching edit. That file has no mention of reject, supersession or cleanup.
               - Salvage (the glossary's entry for work saved from a stopped attempt) is not mentioned. The clauses moved here from node 89 ask only for the order of the cleanup.
INDEX LINE:    graph-conventions.md's `## Review` item 2 now records the conflicted files' paths for a manager-started integration round; SKILL.md cleans up a superseded unlanded implementation node in a reject's order.
FLAGS:         none
NEW NODES:     none
INVALIDATIONS: Node 363 is extended. It shipped the integration-started correction round, and this work says what that round's `## Review` entry records. Node 275 / node 89: this work carries out the "cleaned up like a reject's" ruling in SKILL.md, in tool-neutral words. It contradicts neither node. Its words are narrower than node 275's index line, which names a "worktree and branch": the shipped text says "working tree, and anything else that holds that work".
CONDITIONS:    Searched every open node's (claimed or not) `## Question`, `## Acceptance condition` and `## Amendment` sections for: "human's words", "## Review", "correction round", "conflicted file", "reject: edit", "working state", superseded near tree/worktree/branch/landed, "clean"/"cleanup", "Three outcomes", "What reject means". I also checked nodes 270, 276 and 284 for "supersed" and "remov". The matches were in nodes 190, 375, 370, 40, 78, 80 and 85, and in nodes 270, 276 and 284. None of them is made wrong by this work and no question changes. Node 40's clause about the round that raised a flag still holds. Node 370 edits other sections of SKILL.md (`## Words used exactly`) and the glossary, so the two meet only at integration. No replacement clauses.
MISSING FROM MAP: none
GATE PAYLOAD:  Checker findings: none yet (first run).
               Bar: the repo has no build, no tests, no formatter and no CI. The root holds only `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, and has no `.github`. That matches the record in `map-implementation-rules.md`, so the bar is its non-command half.
               Paths touched: .claude/skills/expedition/graph-conventions.md, .claude/skills/expedition/SKILL.md (both inside the worktree).
               Flag 89.1 (the clauses moved here from node 89 without asking the human first) settles at this gate. The added SKILL.md paragraph is what those clauses produced.
               Proposed commit message:
                 Say what a Review entry records for an integration round, and how a superseded node is cleaned up

                 graph-conventions.md's `## Review` item 2: for a correction round the manager starts when
                 integration conflicts, the entry records the conflicted files' paths in place of the
                 human's words. SKILL.md: an implementation node superseded before its work lands is
                 cleaned up in a reject's order, graph first, then its working tree and anything else
                 holding that work.

                 Node: graph-workflow/371

RETROSPECTIVE
1. What I had to hunt for: where in SKILL.md the supersession cleanup belongs. SKILL.md has no section on superseding a node; the only text on order is the "graph before the cleanup" paragraph under `### Three outcomes, and no fourth`, which I found by grep. Node 89's line in decisions.md does not exist (it was superseded), so the only index line for it is node 275's.
2. What arrived that this node did not need: most of map.md, and the worktree paragraph in map-implementation-rules.md. The manager's notes on node 370 were useful only as a check that the two nodes edit different sections.
3. What would have made it easier: the spawn or the amendment naming the section of SKILL.md where the supersession paragraph should go.
4. Stale, wrong or contradictory: the glossary's **Reject** entry says the manager "deletes its branch". That is a git-specific term, it sits against ground rule 1, and it is worded differently from SKILL.md's tool-neutral "clean the working state". It is outside this node's scope (clause 2) and was not edited. The spawn said to read decisions.md's line for node 89, but decisions.md has no line for it.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition and its amendment reached it as a verbatim copy in `$TMPDIR/c371.md`.*

> PASS
>
> Node 371, "Say what a `## Review` entry records for a correction round the manager starts at integration". Worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/371-review-entry, base 2fd65cdb, uncommitted. Changed paths: .claude/skills/expedition/graph-conventions.md and .claude/skills/expedition/SKILL.md.
>
> Acceptance condition, one line per part. The condition is the original clauses 1 and 3, the struck clause 2 replaced by the amendment's replacement, and the three clauses the amendment adds.
> - Clause 1 (graph-conventions.md, `## Review`, item 2): met. `git -C <wt> diff --word-diff=plain -U0` shows that item 2 gained only "For a round the manager starts when integrating the node's work conflicts, the entry records the paths of the conflicted files in place of the human's words." The second sentence, "The human's words are recorded as `### The human's words` in `SKILL.md` says.", is unchanged word for word. Only its line break moved.
> - Clause 2, as replaced by the amendment: met. `git -C <wt> status --short --untracked-files=all` and `--ignored` list only the two modified files, so nothing under `.scratch/` changed. The word-diff shows exactly two insertions and no removed or altered words. One insertion is the clause 1 sentence. The other is the new SKILL.md paragraph that the amendment's clauses require. No other sentence under `.claude/skills/` changed.
> - Clause 3 (scope came from no search): this states how the scope was got and makes no demand on the work. There was no recorded command to run.
> - Amendment clause 1 (SKILL.md states what happens to a superseded implementation node whose work has not landed): met. A paragraph was added under `### Three outcomes, and no fourth`: "An implementation node superseded before its work has landed is cleaned up in the same order as a reject. Edit the graph first. Then remove the node's working tree, and anything else that holds that work." Found by word-diff. It puts the graph edit first, then removal of the tree and anything else holding the work, and ties the order to the reject's. It is stated as properties. It names no version-control command, which I confirmed by reading the 3 added lines.
> - Amendment clause 2 (the reject line is intact): met. `grep -n "reject: edit the graph first"` returns "- reject: edit the graph first, and clean the working state after." at the same line both in the worktree and in `git show 2fd65cdb:.claude/skills/expedition/SKILL.md`.
> - Amendment clause 3 (scope came from no search): no demand on the work, and no recorded command.
>
> The bar:
> - Commands: the repo has no build, no tests, no formatter and no CI, as map-implementation-rules.md records. There is no agent-instruction file at the repo root. So the bar is its non-command half.
> - Whitespace: `git diff --check` printed nothing (rc=0).
> - Line lengths: the added lines are 97, 100, 5, 99, 101 and 30 characters, consistent with how the files are wrapped.
>
> Standards:
> - I read only the standards in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md: `/coding-principles`, `/naming`, glossary.md's `_Avoid_` lines, the ground rules and the six writing rules (received as text), graph-conventions.md, `/writing-for-agents`, the rule on edits to the trigger file, and the rule on record files as work.
> - Bore on this work:
>   - Glossary `_Avoid_` lines. Checked by hand: the new text uses "supersede", "correction round", "reject", "landed" and "integrating ... conflicts", which match the glossary's own wording, and none of the refused words.
>   - Ground rule 1: no tool command is assumed.
>   - Ground rule 3: nothing addresses the human.
>   - Writing rules 5 and 6: one idea per sentence, plain words, and "that work" has a single referent. The reject order is pointed at in the same section rather than restated.
>   - graph-conventions.md: the new text agrees with the glossary's "Correction round" entry, which names the manager integrating conflicting work.
>   - `/writing-for-agents`: held by hand, not invoked.
> - Did not apply:
>   - Trigger-file rule: the SKILL.md edit sits under `## The gate`, not under `## The order you act in` or `## What is in front of the human, and when`, so `.claude/rules/expedition-triggers.md` was not owed an edit.
>   - Record-file rule: none of the changed paths are record files.
> - No standard was moved by the work. No reviewing skill is named for this repo, and I ran none.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and left no part of the condition uncovered. This settles no flag; flag 89.1, carried here from node 89, settles at the node closing report.
