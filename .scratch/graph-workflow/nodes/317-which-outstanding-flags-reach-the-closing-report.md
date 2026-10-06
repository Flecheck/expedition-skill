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
