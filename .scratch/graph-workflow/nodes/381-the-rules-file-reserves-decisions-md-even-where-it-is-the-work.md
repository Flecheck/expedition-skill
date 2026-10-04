# The rules file reserves `decisions.md` to the manager even where a node's own work is that file

Type: implementation
Status: open
Blocked by: none

## Question

In `map-implementation-rules.md`, the paragraph on an implementation node's work being the effort's own record calls any change to `decisions.md` or `flags.md` in the work "bookkeeping reserved to the manager" and makes the checker FAIL it. The implementation contract's hard rule 1 allows a worker to write a graph file where its node's own work is a change to that file. Node 156's condition demanded exactly that, and node 156 had to raise. The rules file should state that exception.

*Reported by [node 156](156-four-resolved-nodes-have-no-index-line.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none". Its words on why it is not joined to an existing node: "Node 205 targets the same file but a different concern, the bar-commands paragraph. Its clause 5 forbids touching any other paragraph, so it cannot take this one."*

## Acceptance condition

*Authored by node 156's worker and filed by the manager.*

> 1. In `.scratch/graph-workflow/map-implementation-rules.md`, in the paragraph beginning "**An implementation node's work on this effort may be the effort's own record**", the sentence that today reads "**A change to the node's own status line, to `decisions.md`, or to `flags.md` is bookkeeping reserved to the manager**: where one appears among the work the checker's outcome is `FAIL` on the acceptance condition, and that holds whether or not the acceptance condition itself excluded those paths." is replaced. The replacement states both of the following in its own words:
>    (a) a change to the node's own status line is bookkeeping reserved to the manager in every case, and where one appears among the work the checker's outcome is `FAIL` on the acceptance condition;
>    (b) a change to `decisions.md` or `flags.md` is bookkeeping reserved to the manager, with the same `FAIL`, except where the node's acceptance condition requires a change to that file, in which case that change is the work and is checked against the condition like any other work.
> 2. The paragraph's other sentences keep their words.
> 3. The paragraph as it stood before the change is appended **verbatim** to `.scratch/graph-workflow/map-history.md`, at the end of that file, under a new `##` heading of the form "Superseded from `map-implementation-rules.md` at node NN — <what was superseded>", where NN is this node's number. Nothing already in `map-history.md` is edited or removed.
> 4. No file other than these two is modified. No other paragraph of `map-implementation-rules.md` is modified.
> 5. Scope came from no search: the named sentence is the work, not an instance of a defect. A search of `.claude/skills` for "bookkeeping reserved" returned nothing at 4ed809c59. Any other statement of the same rule that the work finds is reported and not edited.
>
> The work is also held against the bar.
