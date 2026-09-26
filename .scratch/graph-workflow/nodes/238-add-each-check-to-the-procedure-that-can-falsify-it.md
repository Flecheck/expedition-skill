# Add each check to the procedure whose writes can make it false

Type: implementation
Status: superseded
Superseded by: 339

Blocked by: none

## Question

*Surfaced by [node 213](213-nothing-triggers-the-ten-mechanical-checks.md)'s worker, and pasted as it wrote
it. **Its acceptance condition below is that worker's own**, written in the same handover.*

**1. Add each check to the procedure whose writes can make it false**
Kind: implementation
Blockers: none
Question: The ten mechanical checks in `graph-conventions.md` are the read-back of the procedures in
the same file, filed where no procedure points at them, and nothing has ever run one. Put each check on
the last step of the act that can make it false.

Acceptance condition:

&gt; The work is one edited file, `.claude/skills/expedition/graph-conventions.md`, and no other file may
&gt; be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
&gt; `flags.md`.
&gt;
&gt; That file holds a section headed `## Procedures` whose opening line reads *"Each lists every file that
&gt; changes, in order"*, containing subsections `### Claim`, `### Resolve`, `### Supersede`, `### Rule out
&gt; of scope`, `### Park`, `### Raise a flag`, `### Settle a flag` and `### Change the map`, each a
&gt; numbered list; a separate section headed `## Adding a node`; and a section headed `## Mechanical
&gt; checks` holding a numbered list of ten checks.
&gt;
&gt; Done means every one of the following is true of the finished tree.
&gt;
&gt; 1. Each of the nine sections below ends with one added numbered step — continuing that section's
&gt;    existing numbering where it has one — which names by number the checks it must run, and states that
&gt;    the party performing the act runs them itself, at that act, over the material that act touched. The
&gt;    sections and the numbers each must name:
&gt;    (a) `### Claim` — 7; (b) `### Resolve` — 5 and 9; (c) `### Supersede` — 1 and 2; (d) `### Rule out
&gt;    of scope` — 1; (e) `### Park` — 8; (f) `### Raise a flag` — 6; (g) `### Settle a flag` — 6;
&gt;    (h) `### Change the map` — 4 and 10; (i) `## Adding a node` — 1, 3 and 4.
&gt; 2. The `## Mechanical checks` section states, in wording the implementer chooses, all three of: that
&gt;    every check is run by the party performing the act that can make it false, at that act, over the
&gt;    material that act touched; that no schedule, no periodic pass and no separately spawned agent runs
&gt;    any of them; and that a whole-graph run of all ten remains available at an empty frontier and is the
&gt;    only run not tied to an act.
&gt; 3. That same section states what a failure produces: the party repairs it inside the same act and
&gt;    reports nothing, where what failed is that act's own bookkeeping — a missing index line, a missing
&gt;    edge, a flag left unmarked; and puts it to the human instead where the repair would change something
&gt;    the human decided, would rewrite or remove text already recorded, or would reverse a status. It
&gt;    states that no flag is raised in either case.
&gt; 4. Check 5 in the numbered list is worded so that it is satisfied by a node having exactly one line in
&gt;    `decisions.md` **that is not struck through**, struck-through lines being permitted in any number.
&gt;    Its wording before this work is *"Every `resolved` node has an `## Answer` and exactly one line in
&gt;    `decisions.md`"*, which no node whose earlier line was struck through and replaced can satisfy.
&gt; 5. The numbered list under `## Mechanical checks` still holds exactly ten items, numbered 1 to 10 in
&gt;    order. No check is added and none is removed, and clause 4 is the only change any item's text
&gt;    receives.
&gt; 6. No existing numbered step in any subsection under `## Procedures` is reworded, renumbered or
&gt;    removed, and `## Adding a node`'s existing prose is unchanged apart from the step clause 1 adds.
&gt; 7. No file other than `.claude/skills/expedition/graph-conventions.md` is modified, and no file under
&gt;    `.scratch/` is modified.
&gt; 8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node was specified in a handover the manager left unfiled for a session**, and is minted late for that
reason rather than any other — flag `213.4` records the delay against the manager. Nothing in the text above
was re-authored on the way here; it is the worker's own, recovered verbatim from the session record.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 339](339-tie-graph-conventions-mds-mechanical-checks-to-the-writes-that.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
