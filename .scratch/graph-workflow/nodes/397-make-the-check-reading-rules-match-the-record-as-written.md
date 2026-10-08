# Make the check-reading rules match the record as it is written

Type: implementation
Status: claimed
Blocked by: none

## Question

This work lets the sweep's mechanical checks report real defects instead of hundreds of false ones, for anyone running them on any effort. The first sweep ([node 396](396-sweep-round-1.md)) found 387 settled flags written as `` `NN.k` `ASSUMPTION` **· settled** ``, a form the reading rule does not count as settled, though it is the form the manager has filed every flag in. It also found three rule gaps that make checks 3, 7 and 9 fire on records that are not defects.

*Minted by the manager from the human's `verbatim` "ok", 2026-10-08, to part 1 of the manager's proposal recorded on node 396.*

## Acceptance condition

*Written by the manager, who minted the node.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. It is a file the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file.
>
> Scope: the named places are the work, so the scope came from no search.
>
> Done when all of the following hold.
>
> 1. The settled form shown under `## The node file` puts the marker `**· settled**` directly after the flag's kind marker: `` `NN.k` `ASSUMPTION` **· settled** — … ``.
> 2. Under `### How a check reads the files`, the rule on when a flag counts as settled accepts the marker `**· settled**` in either of two positions: directly after the kind marker, or directly after the id. It still says that the bare word `settled` in an entry's prose does not settle it.
> 3. Check 3 under `## Mechanical checks`, or a rule under `### How a check reads the files`, states that a number for which no node file has ever existed is a skipped number, not a gap that indicates reuse, and that check 3 does not fail on it.
> 4. Check 7, or a rule under `### How a check reads the files`, states that a heading that begins `## Acceptance condition` and continues with further words counts as the node's `## Acceptance condition`.
> 5. Check 9, or a rule under `### How a check reads the files`, states that a `NOT COVERED:` label inside a blockquote is quoted text, and that check 9 does not read it as a label.
> 6. No other sentence of the file changes, and no heading is renamed.
> 7. The working tree meets the bar.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-08.*

`````
HANDOVER:      Make the check-reading rules match the record as it is written

ANSWER:        `.claude/skills/expedition/graph-conventions.md` was edited in two places, and no other file was touched.
- Under `## The node file`, in `### ## Flags`, the settled form now reads `` `NN.k` `ASSUMPTION` **· settled** — <the judgement, in the worker's own prose> ``. The marker comes after the kind marker. This is the form the manager has filed flags in.
- Under `### How a check reads the files`, the settled-flag bullet was replaced. It now says a flag counts as settled only where `**· settled**` stands directly after the entry's kind marker (the shown form) or directly after its id. The second position keeps the manager's later settle entries valid, such as node 213's `` `213.1` **· settled** — … ``. The bullet still says that the bare word `settled` in an entry's prose does not settle it.
- Three bullets were added after it:
  - A number for which no node file has ever existed is a skipped number. It is not a gap that indicates a reused number, and check 3 does not fail on it.
  - A heading that begins `## Acceptance condition` and continues with further words counts as the node's `## Acceptance condition`.
  - A `NOT COVERED:` label inside a blockquote is quoted text, and check 9 does not read it as a label.
- The three gap rules went in as reading rules rather than as edits to the checks' own sentences. That meets clause 6: checks 3, 7 and 9 are unchanged, and no heading was renamed. Rules under `### How a check reads the files` bind every check, so the acceptance-condition heading rule is not limited to check 7.

INDEX LINE:    graph-conventions.md's settled form puts `**· settled**` after the kind marker, the reading rule accepts either position, and three reading rules clear checks 3, 7 and 9's false failures.

FLAGS:
- ASSUMPTION: The skipped-number rule says "a number for which no node file has ever existed", which is the wording clause 3 requires. `## Mechanical checks` opens with "Each of these is decidable by reading the files". Whether a file ever existed cannot be read from the current files. Node 396's sweep established it from git history. I wrote the rule as the condition demands and did not say how a reader establishes "ever existed", because naming git would assume a toolchain (ground rule 1). A later node may want to say that the reader uses whatever history the repo keeps, or that the manager records a skipped number where it happens. Index sentence: graph-conventions.md's skipped-number rule for check 3 depends on file history that the current files do not show, and how a reader establishes it is left unstated.

NEW NODES:     none

INVALIDATIONS: Node 339 (resolved) recorded reading rule g as "`**· settled**` counts only in the marker position, directly after its id". This work widens that rule: two positions are accepted, and the shown form puts the marker after the kind marker. Node 339 also listed seven reading rules under `### How a check reads the files`. There are now ten (an extension). Node 330's quoted draft clause g has the same older wording, and that is a record of the draft, not a contradiction.

CONDITIONS:    I searched the open nodes' (only 398 besides this one) `## Acceptance condition` and `## Question` for `marker position`, `**· settled**`, `settled`, `check 3`, `check 7`, `check 9`, `NOT COVERED`, `187`, `skipped` and `graph-conventions`. Node 398's condition edits only record files, and none of its clauses is affected. I searched resolved nodes for `marker position`, `gap that indicates` and `skipped number`. The matches that bear on this work are nodes 339 and 330 (see INVALIDATIONS). Node 372's matches are retrospective prose about older entry forms and are unaffected. Node 213's matches are settle entries that stay valid under the id position. I could not narrow a search for `` **· settled** `ASSUMPTION` `` (the old shown form) or `· settled` usefully, because they match hundreds of flag entries, so I did not read those results. No replacement clauses.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet.
- Path touched: .claude/skills/expedition/graph-conventions.md (only this file; uncommitted in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/397-reading-rules).
- The bar: the repo's root `CLAUDE.md` `## Commands` says there is no build, test, formatter or CI. This agrees with the copy in `map-implementation-rules.md`, so the bar is the standards and the condition. No command was run.
- A grep of `.claude/` and `CLAUDE.md` found no other shipped file that shows the settled form or "marker position". No other shipped file is left in the older form. The effort's record keeps 387 entries (counted 2026-10-07, for scale only, not authoritative), and these entries now match the shipped form rather than contradicting it.
- Proposed commit message:
  graph-conventions: settled form and check-reading rules match the record

  The shown settled form puts **· settled** after the kind marker, and the reading rule accepts it there or after the id. New reading rules: a never-created number is skipped, not reused (check 3); a suffixed `## Acceptance condition` heading counts (check 7); a blockquoted `NOT COVERED:` label is quoted text (check 9).

  Node: graph-workflow/397

RETROSPECTIVE
1. What I had to hunt for: what the three gaps actually looked like, so the rules would fit them (for example, node 140's `## Acceptance condition — written in part…` headings and the `> NOT COVERED:` blockquotes). I found these in node 396's report under `### Check 7` and `### Check 9`, by grep. The condition was self-contained enough to write the rules without them, so this was only a confirmation.
2. What arrived that the node did not need: all of `map.md` (about 80 lines of standing preferences and history pointers) and all of `map-implementation-rules.md` (the worktree, trigger-file and record-as-work paragraphs). This node needed only the bar paragraph and the standards list. A broad grep of `decisions.md` on `graph-conventions` also returned about 30 index lines, none of which bore on the work.
   - `map-read-whole-for-a-few-items`: carried by 21 earlier retrospectives (nodes 135, 178, 185, 205, 214, 220, 284, 317, 382, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 40, 41).
   - `rules-file-read-whole-for-one-section`: carried by 17 earlier retrospectives (nodes 178, 185, 214, 220, 317, 382, 386, 387, 388, 390, 391, 392, 393, 395, 40, 41; the derivation lists 16 files for 17 retrospectives).
3. What would have made this easier: the contract's search of resolved nodes for "each phrase it supersedes" breaks down when the superseded phrase is the settled marker itself, which appears in hundreds of flag entries. A note in the spawn that the marker is unsearchable would have saved an attempt.
   - `record-is-not-mechanically-scannable`: carried by 7 earlier retrospectives (nodes 178, 212, 220, 382, 385, 387, 395).
4. What was stale, wrong or contradicted: `## Mechanical checks` says every check is "decidable by reading the files", while the skipped-number rule that clause 3 required depends on file history (see the ASSUMPTION flag). The manager's notes checked out: node 398 edits only record files, and the settled form is as stated.
   - `unestablished-inference`: carried by 2 earlier retrospectives (nodes 385, 389). The fit is loose: the check's decidability claim does not hold for this one rule.
`````

## Flags

`397.1` `ASSUMPTION` — The skipped-number rule leaves unstated how a reader establishes that no file ever existed. *(The worker's full text is under its handover's `FLAGS`.)*
