# Make the check-reading rules match the record as it is written

Type: implementation
Status: open
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
