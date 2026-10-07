# Which outstanding flags reach the closing report

Type: implementation
Status: claimed
Blocked by: 392

## Question

This work lets the human see every flag still outstanding when an effort closes. It also lets the manager build the effort closing report from one rule about flags, instead of two that disagree.

*The opening sentence above was written by [node 392](392-write-the-acceptance-conditions-for-the-five-kept-nodes.md)'s worker and filed by the manager on 2026-10-06.*

*Minted by the manager from an observation of [node 312](312-cut-the-rules-both-the-manager-contract-and-graph-conventions-state.md)'s checker, which it gave as not a finding. The checker's own words:* "`SKILL.md` now holds both "Flags reach the closing report in two cases only" and, under `## Closing an effort`, "Every outstanding flag". An outstanding flag on a node not yet closed fits neither of the two cases. Before, the two statements sat in different files."

The two statements in `.claude/skills/expedition/SKILL.md` disagree about an outstanding flag on a node that is not yet closed when the effort closes. Which of them is meant, and how should the other be worded? [Node 309](309-drop-the-closing-reports-case-for-flags-raised-before-settle-at-close.md) already changes the first statement's list of cases.

*Manager's note: minted by the manager. No acceptance condition is written yet. It depends on the answer to the question.*

*The manager's note, 2026-09-26:* node 309 landed as `c52c03e`, so `## Flags` now reads "Flags reach the closing report in one case only: a flag whose pick report the human never answered, because they never spoke again." [Node 320](320-the-glossarys-flag-entry-names-one-case-of-a-flag-reaching-the-closing-report.md) was superseded by 309 on the human's "ok for superseded", on the understanding that this node's work keeps `CONTEXT.md`'s `**Flag**:` entry in line with whatever it decides. The condition written for this node carries that entry.

*The manager's note, 2026-10-06:* kept at the triage the human invoked and approved (`verbatim` *"ok"*). A read-only agent checked it against the current files and found it still live; it has no acceptance condition yet.

## Acceptance condition

*Authored by [node 392](392-write-the-acceptance-conditions-for-the-five-kept-nodes.md)'s worker, from the human's 2026-10-06 decision where the node has one, and filed by the manager.*

> Done when all of the following hold.
>
> 1. `.claude/skills/expedition/SKILL.md`, under `## Flags`, no longer holds the sentence "Flags reach the effort closing report in one case only: a flag whose node closing report the human never answered, because they never spoke again." In its place, the section states that every outstanding flag reaches the effort closing report. It may say this in its own words, or by naming the bullet under `## Closing an effort` that lists what that report carries.
> 2. The bullet under `## Closing an effort` in the same file, "Every outstanding flag, taken from the unchecked lines of the effort's index of flags and never reconstructed by you.", keeps its words.
> 3. No sentence of any file under `.claude/` says that flags reach the effort closing report in one case only, or in any set of cases narrower than every outstanding flag. This includes the `**Flag**:` entry of `.claude/skills/expedition/glossary.md`.
> 4. The working tree meets the bar.
>
> Scope: on 2026-10-06, `grep -rn -i "closing report" .claude/ | grep -i flag` was run over the working tree. It returned these places:
> - `.claude/skills/expedition/SKILL.md`, four lines under `## Flags` ("node's flags settle at its node closing report too", "The node closing report awaits no answer", "Flags reach the effort closing report in one case only", and "A node closing report for a node holding flags carries every one of those flags");
> - `.claude/skills/expedition-standing-yes/SKILL.md`, its heading `## Flags, and the node closing report`;
> - `.claude/skills/expedition-cleanup/SKILL.md`, "The effort closing report is built from its lines";
> - `.claude/skills/expedition-precondition/SKILL.md`, "The flag settles at the node closing report".
>
> Only the "one case only" sentence states a case narrower than every outstanding flag. Any instance the search reaches outside `.claude/skills/expedition/SKILL.md` that does so is reported and not edited.

## Interview

#### The human's answer, 2026-10-06

*The manager put the node's question directly, after the 2026-10-06 triage kept the node. The manager's message, as sent:* "Two sentences in the manager contract disagree: `## Flags`: \"Flags reach the effort closing report in one case only: a flag whose node closing report the human never answered.\" `## Closing an effort`: the report carries \"every outstanding flag, taken from the unchecked lines of the effort's index of flags\". [...] My recommendation: every outstanding flag reaches the closing report, and the `## Flags` sentence is reworded to say so. [...] Please answer node 317. \"ok for recommended\" takes \"every outstanding flag\"."

`verbatim`: *"ok"*

*The manager's note:* the reply takes the recommendation: every outstanding flag reaches the effort closing report, and the `## Flags` sentence is reworded to say so. The condition is still to be written.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-06.*

`````
HANDOVER:      Which outstanding flags reach the closing report
ANSWER:        Every outstanding flag reaches the effort closing report. The answer is the human's, given on 2026-10-06. In `.claude/skills/expedition/SKILL.md`, under `## Flags`, the sentence "Flags reach the effort closing report in one case only: a flag whose node closing report the human never answered, because they never spoke again." is replaced by: "Every outstanding flag reaches the effort closing report, whatever the state of its node. The list under `## Closing an effort` gives what that report carries." The bullet under `## Closing an effort`, "Every outstanding flag, taken from the unchecked lines of the effort's index of flags and never reconstructed by you.", is unchanged, so the two statements now agree.
               Calls a later reader would otherwise have to re-derive:
               (1) The rule is restated in `## Flags` and not only pointed at. `graph-conventions.md`'s `### Settle a flag` says "`## Flags` in `SKILL.md` says when a node's flags settle, and which flags reach the effort closing report". A pointer-only paragraph would leave that citation pointing at a section that does not state the rule.
               (2) The phrase is "whatever the state of its node" and not "whether or not its node has closed". The glossary's **Resolve** entry lists `close` in its `_Avoid_` line for a node, and **Closed** is defined for an effort only.
               (3) The glossary's `**Flag**:` entry already names no case of a flag reaching the effort closing report, so it needed no edit. The scope search found no other sentence under `.claude/` that is narrower than every outstanding flag. A broader search for "one case", "cases only", "reach.*closing" and "outstanding flag" found none either. `expedition-triage`'s "for this one case" is about settling, not about reaching the report.
INDEX LINE:    `SKILL.md`'s `## Flags` now says every outstanding flag reaches the effort closing report, whatever its node's state, which matches `## Closing an effort`; the one-case sentence is gone.
FLAGS:         ASSUMPTION: I did not reduce `## Flags` to a pure pointer at `## Closing an effort`. I restated the rule in one sentence and added a pointer after it. The reason is that `graph-conventions.md`'s `### Settle a flag` cites `## Flags` as the place that says "which flags reach the effort closing report". This node held no exchange with the human beyond the 2026-10-06 answer recorded under `## Interview`. What I did: I edited one paragraph of SKILL.md and checked the glossary and the other `.claude/` files by search.
               Index sentence: `## Flags` in the manager contract restates "every outstanding flag reaches the effort closing report" instead of only pointing at `## Closing an effort`, because `graph-conventions.md` cites `## Flags` for that rule.
NEW NODES:     none
INVALIDATIONS: - Node 309 (resolved): its answer, that `## Flags` states one case only (an unanswered pick report), is contradicted. That sentence is gone, and every outstanding flag now reaches the report.
               - Node 370 (resolved): its answer describes `## Flags` as giving "the one case in which flags reach the effort closing report". That description no longer holds. `## Flags` now names every outstanding flag.
               - Nodes 46, 102 and 103 (resolved): their answers say flags reach the closing report where the human never speaks again. My work extends that rule: it remains true, but it is no longer the whole of the rule.
               - Node 364 (resolved): its condition kept "Flags reach the effort closing report" unchanged and deferred to this node. Nothing is contradicted, but the text it protected no longer exists.
CONDITIONS:    I searched the open nodes (13, 185, 214, 40, 41) for: "one case only", "in one case", "reach(es) the (effort) closing report", "closing report", "outstanding flag", "under `## Flags`" and "## Closing an effort". The only match bearing on this work is node 41's "outstanding — left unchecked, meaning carried, and re-surfaced in the effort closing report", and it agrees with my work. No replacement clause is needed and no open node's question changes. The resolved nodes' `## Answer` and `## Acceptance condition` sections were searched for the same phrases, with the results listed under INVALIDATIONS.
MISSING FROM MAP: none
GATE PAYLOAD:  The checker has not run yet, so there are no findings.
               The bar: the repo root holds no CLAUDE.md, no AGENTS.md and no manifest, which confirms `map-implementation-rules.md`'s record that there is no build, no tests, no formatter and no CI. The bar is therefore the standards plus the acceptance condition. The line wraps at the file's existing width.
               One note on the condition: its scope lists "A node closing report for a node holding flags carries every one of those flags" among four lines under `## Flags`. That line actually sits under `## What is in front of the human, and when`. This is harmless and has no effect on any clause.
               Paths touched: .claude/skills/expedition/SKILL.md, the only file, in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/317-closing-flags. The change is left uncommitted.
               Proposed commit message:
                 Every outstanding flag reaches the effort closing report

                 The manager contract's `## Flags` named one case only, which
                 disagreed with `## Closing an effort`'s "Every outstanding flag".
                 `## Flags` now states the same rule and points at that list.

                 Node: graph-workflow/317

RETROSPECTIVE
1. What I had to hunt for: whether "close" may be used of a node. I found it in the glossary's **Resolve** `_Avoid_` line and its **Closed** entry, after I had first written "whether or not its node has closed". I also had to establish that `graph-conventions.md` cites `## Flags` for this rule, which I found by a broad grep over `.claude/`.
   - `glossary-refusal-found-after-writing`: new name, carried by 0 earlier retrospectives. A refused word is caught only by a lookup after it is written, because nothing at the point of writing names the refusals that bear on the section being edited.
2. What arrived that the node did not need: most of `map.md` (the destination, the v2 and Lang notes, the graph-file history) and nearly all of `map-implementation-rules.md` (worktree mechanics, record-as-work, the triggers file). This node needed only the writing rules, the glossary and the bar's paragraph.
   - `map-read-whole-for-a-few-items`: carried by 13 earlier retrospectives (nodes 135, 178, 205, 220, 284, 382, 386, 387, 388, 389, 390, 391, 392).
   - `rules-file-read-whole-for-one-section`: carried by 10 earlier retrospectives across 9 node files (nodes 178, 220, 382, 386, 387, 388, 390, 391, 392).
3. What would have made this node easier: a spawn note that `graph-conventions.md`'s `### Settle a flag` cites `## Flags` for this rule. That citation decides whether a pointer-only rewrite is acceptable.
4. What was stale, wrong or contradictory:
   - `question-quotes-superseded-text`: carried by 1 earlier retrospective (node 392). The node's `## Question` quotes "two cases only", "pick report" and `CONTEXT.md`'s `**Flag**:` entry. All three are superseded: the entry now lives in `glossary.md`, and the condition handles that correctly.
   - `condition-scope-misplaces-a-match`: new name, carried by 0 earlier retrospectives. The condition's scope puts the line "A node closing report for a node holding flags carries…" under `## Flags`, but it sits under `## What is in front of the human, and when`.
`````

## Flags

`317.1` `ASSUMPTION` — `## Flags` restates the rule rather than only pointing at `## Closing an effort`. *(The worker's full text is under its handover's `FLAGS`.)*

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-06. A fresh checker; the condition reached it as a verbatim copy in `$TMPDIR/check317.md`. The node's one flag, 317.1, reached it as text.*

> PASS
>
> Work checked: uncommitted change in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/317-closing-flags. `git status --porcelain --ignored` shows only ` M .claude/skills/expedition/SKILL.md`. The diff replaces one paragraph under `## Flags` and nothing else.
>
> Acceptance condition, one line per part:
> 1. Met. I printed `## Flags` with `awk '/^## Flags/{f=1} /^## Acceptance conditions/{f=0} f'`. The sentence "Flags reach the effort closing report in one case only…" is gone. In its place are "Every outstanding flag reaches the effort closing report, whatever the state of its node." and "The list under `## Closing an effort` gives what that report carries." A grep for "one case only" or "in one case" over the worktree's `.claude/` returns nothing.
> 2. Met. Under `## Closing an effort` (awk extract), the bullet "Every outstanding flag, taken from the unchecked lines of the effort's index of flags and never reconstructed by you." is unchanged, and the diff does not touch it.
> 3. Met. I unwrapped every `.claude/` file containing "effort closing report" (perl join of single newlines) and extracted every sentence containing that phrase. None restricts which flags reach the report to fewer than every outstanding flag. The glossary `**Flag**:` entry, from `grep -A6 '^\*\*Flag\*\*'`, says nothing about the effort closing report. graph-conventions.md says "`## Flags` in `SKILL.md` says when a node's flags settle, and which flags reach the effort closing report", which is still true. A grep for "never answered", "spoke again" and "speaks again" finds only SKILL.md "Where the human never speaks again, nothing settles, and those flags stay outstanding.", which is consistent with the new rule.
> 4. Met, see the bar below.
>
> Bar: the repo root holds .claude, CONTEXT-MAP.md, CONTEXT.md and .gitignore. It has no CLAUDE.md, AGENTS.md or manifest, and the repo states no build, test or formatter commands, so there was nothing to run. The bar is therefore its non-command half, which is the standards. Standards: I read only the standards in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/map-implementation-rules.md (`## What the work is held against`) and opened no other file in the effort's directory. These bore on the work: the glossary `_Avoid_` lines (none of the new text's words is refused for its concept, checked with grep against the `_Avoid_` lines), the ground rules, the six writing rules (plain English, one idea per sentence, a heading cited rather than restated), graph-conventions.md (its pointer at `## Flags` stays accurate) and /writing-for-agents (short and direct). /coding-principles and /naming do not apply to this prose change. No reviewing skill is named, so I ran none. Under the rules-file provision on record files, the changed path is a shipped file and not a record file, so that rule did not come into play.
>
> Recorded search: I ran `grep -rn -i "closing report" .claude/ | grep -i flag` as written over the worktree. It returned 7 lines: standing-yes:76 heading, SKILL.md 363, 366, 371 and 574, cleanup:59, and precondition:107. These are the same places and phrases the condition records, except that the "one case only" line is now line 371, "Every outstanding flag reaches…". That replacement is the work itself.
>
> QUESTIONS:
> - The condition's scope list misdescribes one line. It places SKILL.md's "A node closing report for a node holding flags carries every one of those flags" among "four lines under `## Flags`", but that line (now 574) sits under `## What is in front of the human, and when`, both in the work and at base 431b7c45b. I checked this with an awk that prints the nearest preceding `## ` heading for line 574 in each file. The command's return matches the record. Only the condition's heading attribution is wrong. Form: a line the scope list attributes to a heading it does not sit under. Extent: the four SKILL.md lines in the scope list, which is the whole set of heading attributions the list makes. Not a FAIL, because the work did not need that line.
>
> Flags: 317.1 is true of the work. `## Flags` both states the rule in its own words and points at `## Closing an effort`.
>
> No temporary files remain. The one I wrote under $TMPDIR is removed.

*The manager's note:* the checker handed back a question beside its outcome, so the standing yes does not cover this gate. It goes to the human.


### Gate — approve, 2026-10-07

`verbatim`: *"ok"*

*The manager's note:* the manager's message ended "Please approve node 317, or tell me what to change.", and recommended approving. The checker's question on the scope note's heading attribution is answered by the approval: a slip in the record, with no effect on the work.
