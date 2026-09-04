# Four resolved nodes have no line in the effort's index of decisions

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [What to do about the record's token cost, given what `qmd` turns out to
be](129-what-to-do-about-the-records-token-cost.md)'s worker, and pasted as it wrote it.*

> Four nodes whose files state `Status: resolved` appear nowhere in `.scratch/graph-workflow/decisions.md` — not as
> an entry and not as a citation inside another entry. Under the human's stated rationale for keeping that file read
> whole, a decision with no line in it is a decision no worker's context is ever fed. Give each one its line.

**Why it is surfaced now, in the worker's words:** *"the shipped conventions already require this (`Every resolved
node has an ## Answer and exactly one line in decisions.md`), so the defect is that nothing runs the check, not that
the rule is missing. It became consequential an hour ago: the human's ground for keeping the index in every worker's
context is that a fed entry is taken into account naturally, and these four are fed to nobody. **All four are nodes
that carried an earlier decision into files**, which suggests the omission is patterned rather than random and worth
looking at as such."*

## Acceptance condition

*Written by node 129's worker. Pasted as it wrote it, and not the manager's.*

> 1. **In `.scratch/graph-workflow/decisions.md`, four entries are appended**, one for each of these nodes, at the
>    end of the list and in ascending numeric order:
>    - `nodes/103-carry-the-pick-report-settling-moment.md` — *Carry the pick-report settling moment into the shipped
>      files and the map*
>    - `nodes/114-context-destination-entry-omits-the-expectation.md` — *`CONTEXT.md`'s `Destination` entry does not
>      say the destination states whether the effort is expected to end*
>    - `nodes/116-carry-the-enumerator-duty-into-the-checker-contract.md` — *Carry the checker's enumerator duty into
>      the checker's contract*
>    - `nodes/133-carry-the-method-skill-deletion-into-the-contracts.md` — *Carry the method-skill deletion into the
>      four worker contracts*
> 2. **Each entry takes the form the file's existing entries take** — a markdown link whose text is the node's own
>    title and whose target is the node's path relative to `.scratch/graph-workflow/`, an em dash, then one sentence
>    of about 25 words saying what the node settled.
> 3. **Each sentence is derived from that node's own `## Answer` section** and states what it settled. It restates no
>    reasoning and quotes no figure from it.
> 4. **Nothing already in the file is edited, reordered, struck through or deleted.** The four entries are appended
>    and are the only change to it.
> 5. **The general property is re-derived at the time of the work rather than taken from this condition**: after the
>    append, every node file under `.scratch/graph-workflow/nodes/` whose text contains a line reading `Status:
>    resolved` is named by at least one entry in `decisions.md`. The four above were the complete set at the time
>    this condition was written; where re-derivation finds others, they are appended on the same terms and reported.
>    Where re-derivation finds fewer, the discrepancy is reported and nothing is removed.
> 6. **No file other than `.scratch/graph-workflow/decisions.md` is modified.**
>
> The work is also held against the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is mechanical check 5 failing, found by counting rather than by running the check.** The conventions state the
rule; nothing enforces it, which is the same shape as the extraction-of-a-graph-tool fog item in
[map-manager-only.md](../map-manager-only.md).

**Clause 5 will find more than four.** Nodes 129, 132, 145 and 147 resolved after this condition was written and were
given their lines by the manager at resolution; the re-derivation the clause demands is what will confirm that. The
manager has not amended the condition, and this note is not part of it.
