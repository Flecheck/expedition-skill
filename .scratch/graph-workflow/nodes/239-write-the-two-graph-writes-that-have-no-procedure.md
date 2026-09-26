# Write the two graph writes that have no procedure

Type: implementation
Status: superseded
Superseded by: 339

Blocked by: none

## Question

*Surfaced by [node 213](213-nothing-triggers-the-ten-mechanical-checks.md)'s worker, and pasted as it wrote
it. **Its acceptance condition below is that worker's own**, written in the same handover.*

**2. Write the two graph writes that have no procedure**
Kind: implementation
Blockers: none
Question: `## Procedures` says each of its entries lists every file that changes, and two of the
graph's most frequent writes have no entry — appending a checker's run to a node's `## Review`, and
appending a relayed question or a human answer to a node's `## Interview`. Checks 8 and 9 hang off
exactly those two writes and so have no act to attach to. Write both procedures.

Acceptance condition:

&gt; The work is one edited file, `.claude/skills/expedition/graph-conventions.md`, and no other file may
&gt; be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
&gt; `flags.md`.
&gt;
&gt; That file holds a section headed `## Procedures` whose opening line reads *"Each lists every file that
&gt; changes, in order"*, containing eight subsections: `### Claim`, `### Resolve`, `### Supersede`,
&gt; `### Rule out of scope`, `### Park`, `### Raise a flag`, `### Settle a flag` and `### Change the map`.
&gt; The same file describes the shape of a node's `## Review` section and of its `## Interview` section
&gt; under their own headings, and no subsection of `## Procedures` covers the write into either.
&gt;
&gt; Done means every one of the following is true of the finished tree.
&gt;
&gt; 1. `## Procedures` gains exactly two new subsections and no others: one for appending a checker's run
&gt;    to a node's `## Review` section, and one for appending a relayed question or a human answer to a
&gt;    node's `## Interview` section. Each is a numbered list naming every file that changes, in order, in
&gt;    the form the eight existing subsections use.
&gt; 2. The `## Review` subsection ends with a numbered step naming check 9 in that file's `## Mechanical
&gt;    checks` list; the `## Interview` subsection ends with a numbered step naming check 8. Each says the
&gt;    party performing the act runs the named check itself, over the material that act touched.
&gt; 3. Neither new subsection restates the shape of `## Review` or of `## Interview`. Where a shape is
&gt;    needed, the subsection cites the section of the same file that holds it, by that section's heading.
&gt; 4. No existing subsection under `## Procedures` is reworded, renumbered or removed, and no item in the
&gt;    numbered list under `## Mechanical checks` is added, removed or changed.
&gt; 5. No file other than `.claude/skills/expedition/graph-conventions.md` is modified, and no file under
&gt;    `.scratch/` is modified.
&gt; 6. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node was specified in a handover the manager left unfiled for a session**, and is minted late for that
reason rather than any other — flag `213.4` records the delay against the manager. Nothing in the text above
was re-authored on the way here; it is the worker's own, recovered verbatim from the session record.

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 339](339-tie-graph-conventions-mds-mechanical-checks-to-the-writes-that.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
