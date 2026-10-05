# Begin an implementation node's question with what the work makes possible and for whom

Type: implementation
Status: claimed
Blocked by: none

## Question

Make the author of an implementation node begin its `## Question` with one or two sentences saying what the work makes possible and for whom. The worker that claims the node then has the work's purpose without reading the long node that decided it. The sentence goes into the five worker contracts' shared section on reporting an implementation node, and into the manager contract's `## Acceptance conditions`. Reported by node 384, which took this from the "What to build" part of mattpocock's `/to-tickets`.

*Reported by [node 384](384-what-to-spec-and-to-tickets-put-in-a-ticket-that-our-conditions-lack.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none. Node 382 is open and has exactly the same six files as its work: the five worker contracts and `.claude/skills/expedition/SKILL.md`. Its concern is different, a search of resolved nodes before handing back, so this is not a join under the same-file, same-concern rule. Two consequences for the manager. With one code slot, the two nodes cannot run at once. If the manager merges them under the map's group-by-file preference, node 382's clause 3 ("no other sentence changes"), clause 5 ("nothing outside the change in clause 4 changes", "does not grow") and this node's clause 4 conflict, and go to the human. The two nodes' anchor sentences do not overlap, so either can land first unchanged."*

## Acceptance condition

*Authored by node 384's worker and filed by the manager.*

> The work is these six files, and no other file may be edited:
>   `.claude/skills/expedition-grilling/SKILL.md`
>   `.claude/skills/expedition-research/SKILL.md`
>   `.claude/skills/expedition-prototype/SKILL.md`
>   `.claude/skills/expedition-precondition/SKILL.md`
>   `.claude/skills/expedition-implementation/SKILL.md`
>   `.claude/skills/expedition/SKILL.md`
> These are files the workflow ships, so nothing is struck through and nothing is moved to any history file.
>
> Scope: the named places are the work, not instances of a defect, so the scope came from no search. On 2026-10-04, `grep -c 'No other kind of node carries a' .claude/skills/expedition-{grilling,research,prototype,precondition,implementation}/SKILL.md` returned 1 for each of the five files, and `grep -c 'Where you minted the node, you write the condition.' .claude/skills/expedition/SKILL.md` returned 1. These locate the anchors. They do not bound a scope.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In each of the five worker contracts, under the heading `## When a node you report is an implementation node`, a new paragraph sits immediately after the paragraph that ends "No other kind of node carries a condition." and before the paragraph beginning "If you genuinely cannot say what done means". The new paragraph is exactly: "Begin the node's question with one or two sentences that say what the work makes possible and for whom. The worker that claims the node then knows what the work is for without reading the node that spawned it." Line wrapping may differ. The words may not.
> 2. The paragraph added in clause 1 is byte-identical across the five worker contracts, line wrapping included.
> 3. In `.claude/skills/expedition/SKILL.md`, under `## Acceptance conditions`, the sentence "You also begin its question with one or two sentences that say what the work makes possible and for whom." sits immediately after the sentence "Where you minted the node, you write the condition." and before the sentence beginning "Where a condition carries none of the three things". Re-wrapping that paragraph's lines is permitted. Its other words may not change.
> 4. Apart from clauses 1 and 3, no sentence in the six files changes. In particular, every heading is unchanged, including `### The four constraints on a condition you write yourself`, and the handover block's line beginning `NEW NODES:` is unchanged in each worker contract.
> 5. No file under `.scratch/` changes. `.claude/skills/expedition-checker/SKILL.md`, `.claude/skills/expedition-cascade/SKILL.md`, `.claude/skills/expedition/graph-conventions.md` and `.claude/skills/expedition/glossary.md` do not change.
> 6. The tree meets the bar.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-05.*

`````
HANDOVER:      Begin an implementation node's question with what the work makes possible and for whom

ANSWER:        The author of an implementation node now begins the node's `## Question` with one or two sentences saying what the work makes possible and for whom. The rule is in two places. (1) In each of the five worker contracts (`.claude/skills/expedition-{grilling,research,prototype,precondition,implementation}/SKILL.md`), under `## When a node you report is an implementation node`, a new paragraph sits between the paragraph ending "No other kind of node carries a condition." and the paragraph beginning "If you genuinely cannot say what done means". It reads: "Begin the node's question with one or two sentences that say what the work makes possible and for whom. The worker that claims the node then knows what the work is for without reading the node that spawned it." It is wrapped at the files' 108-column width, and its last line holds the single word "it.". The paragraph is byte-identical in all five files. The whole section is still identical across the five, except for the research file's existing missing trailing blank line, which was already there. (2) In `.claude/skills/expedition/SKILL.md`, under `## Acceptance conditions`, the sentence "You also begin its question with one or two sentences that say what the work makes possible and for whom." now follows "Where you minted the node, you write the condition." The only other change to that paragraph is that its lines were re-wrapped. Following node 384's flag 384.1, the cascade contract was left alone. No other sentence or heading changed. That includes `### The four constraints on a condition you write yourself` and every `NEW NODES:` handover line.

INDEX LINE:    The five worker contracts and the manager's `## Acceptance conditions` now require an implementation node's question to begin with one or two sentences on what the work makes possible and for whom.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: Node 384 is extended, not contradicted: this work ships its "Intent (Q2): taken" answer. Node 50 (shared blocks stay duplicated) and nodes 329/333 (the shared sections are byte-identical across the five contracts) still hold, because the new paragraph is duplicated byte-identically. No other resolved node's `## Answer` or `## Acceptance condition` that matched the search is changed by this work. Node 312's citation of "Where you minted the node, you write the condition." still matches that sentence word for word.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open and claimed node (13, derived 2026-10-05, for scale only), and the `## Answer`/`## Acceptance condition` sections of the resolved nodes. The searches were for these phrases: "No other kind of node carries a", "Where you minted the node", "When a node you report is an implementation node", "## Acceptance conditions", "makes possible", "What to build", "If you genuinely cannot say", plus the six paths. Among open nodes, the phrase searches matched only node 386 itself. The path search hit node 388, which deletes the research contract and edits the precondition contract and `expedition/SKILL.md`. Node 388's clauses anchor on `## Spawning a worker`, `## Hard rules` and the precondition kind paragraph, none of which this work touches. So its condition stays correct, and its stated blocker on 386 is discharged. The path search also hit node 41, whose file list already carries the manager's note about research's deletion. This work does not change that list. Open node 32 cites line numbers in those contracts. Those line numbers were already stale, and this work shifts them by 4 more lines further down the file. I made no replacement clauses, and this work changes no open node's question.

MISSING FROM MAP: none

GATE PAYLOAD:  The checker has not run yet, so there are no findings. Bar: I looked at the repo root. It has no `CLAUDE.md`/`AGENTS.md`, no manifest and no formatter, which agrees with `map-implementation-rules.md`'s record that the command half of the bar is empty. The new prose was checked by hand against the standing rules for writing (plain English, one idea per sentence, no new bold). No new line exceeds 108 columns. The only longer lines in these files are tables that were already there. Paths touched (in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/386-intent-line): `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`, `.claude/skills/expedition/SKILL.md`. Nothing under `.scratch/` changed in that tree. No method skill was invoked.
Proposed commit message:
  Begin an implementation node's question with what the work makes possible

  The five worker contracts' section on reporting an implementation node, and
  the manager's `## Acceptance conditions`, now ask the node's author to open
  its question with one or two sentences on what the work makes possible and
  for whom, so the claiming worker knows the purpose without reading the
  node that spawned it.

  Node: graph-workflow/386

RETROSPECTIVE
1. What I had to hunt for: almost nothing. The anchors were quoted exactly in the condition, and the grep confirmed them. The derivation (j) block had to be pulled out of `derivations.md` with awk before it could run. The entry gives no ready-to-run command, and I looked there first.
2. What arrived in my context that this node did not need:
   - `map-read-whole-for-a-few-items`: carried by 7 earlier retrospectives (nodes 135, 178, 205, 220, 284, 382, 387). For this node `map.md` was about 40KB together with the rules file, and the only things I acted on were ground rules and writing rule 5. A verbatim-insertion node with a self-contained condition needed neither the map's history-laden preferences nor the worktree/record-as-work paragraphs.
   - `rules-file-read-whole-for-one-section`: carried by 5 earlier retrospectives (nodes 178, 220, 382, 387; 382 holds two). Only the bar's-commands paragraph and the standards list bore on this work.
3. What would have made this node easier: the spawn could say "byte-identical section across five contracts, research lacks a trailing blank line" up front, which is the one fact that matters when verifying clause 2. It also arrived through node 329's text in the search. A runnable script file for derivation (j) would remove the extraction step.
4. What I read that was stale, wrong, or contradictory: open node 32 cites line numbers in the five contracts that have long been stale, and this work shifts them again. Otherwise nothing.
   - `stale-number-in-the-record`: carried by 6 earlier retrospectives (nodes 178, 212, 220, 382, 385). The instance this time is node 32's line-number citations.
`````
