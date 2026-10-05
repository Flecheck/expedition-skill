# File a retrospective where the worker put it, and fold the bullet's duplicated sentences

Type: implementation
Status: open
Blocked by: none

## Question

A worker reading the map's retrospective bullet learns where the manager files its retrospective and how to find existing item names, each stated once. The bullet in `map-manager-only.md` says a retrospective "is written under the heading `## Retrospective` and under no other heading". Since node 340, the manager has left most retrospectives inside the pasted handover or question payload, because copying one out under its own heading re-files a worker's text. About 132 node files hold a retrospective inside a paste, and about 66 have a `## Retrospective` heading (counted 2026-10-05, for scale only). Derivations.md entry (j) reads both. Node 387's checker also found two pairs of sentences in the same bullet that say the same thing twice. Node 387's condition froze them, and the human agreed to fold them later.

*Minted by the manager from the manager's own question to the human, 2026-10-05. The question ended: "Please answer: \"ok for recommended\" mints that node, or say you'd rather keep the rule." The recommendation was: "change the rule to match the practice. A retrospective stays where the worker put it, at the end of the pasted handover or question payload. I'd mint one small implementation node on `map-manager-only.md` that rewrites that sentence and folds node 387's two duplicated pairs."*

*The human's answer, `verbatim`, 2026-10-05:* *"ok"*

## Acceptance condition

*Written by the manager, who minted the node.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The bullet in question is the one line of `map-manager-only.md` beginning `- **Every worker returns a retrospective as the last handover part, on this effort only**`. In what follows, "the bullet" means that line.
>
> Scope: the named places are the work, not instances of a defect, so the scope came from no search.
>
> Done means every one of the following is true of the finished tree.
>
> 1. These two sentences of the bullet are removed: "It states how many earlier retrospectives carry that name, and lists their node ids." and "It finds the existing names by searching the retrospective sections of the files under `.scratch/graph-workflow/nodes/`, whatever heading each section was filed under, and not from memory or from any list held elsewhere."
> 2. The sentence "The worker obtains the existing names, with their counts and node files, by running the entry headed `## (j) Item names carried by the retrospectives` in [derivations.md](derivations.md)." becomes exactly: "The worker obtains the existing names, with their counts and node files, by running the entry headed `## (j) Item names carried by the retrospectives` in [derivations.md](derivations.md), and not from memory or from any list held elsewhere."
> 3. These five consecutive sentences of the bullet are removed: "The manager writes it into the node file in the same edit that writes that node's answer, its flags and its line in `decisions.md`.", "It is written last in the file, so the mandatory section order is untouched.", "It is written under the heading `## Retrospective` and under no other heading.", "It is not an annotation, since `graph-conventions.md` defines an annotation as what a later piece of work changed about a node's answer." and the sentence beginning "It is a section the shipped node-file format does not list". In their place there are exactly these sentences: "The manager files it where the worker put it, as the last part of the handover or question payload that the manager pastes onto the node. It stays inside that paste rather than being copied out under a heading of its own. A retrospective filed under a `## Retrospective` heading before 2026-10-05 stays where it is. This filing was settled at [node 391](nodes/391-file-a-retrospective-where-the-worker-put-it.md)."
> 4. No other sentence of the bullet changes, and no other line of `map-manager-only.md` changes.
> 5. The text removed by clauses 1 to 3 is appended verbatim to `.scratch/graph-workflow/map-history.md` under a heading that names `map-manager-only.md`'s retrospective bullet and node 391, in the form of that file's most recent entries. `map-history.md` gains text and loses none.
> 6. Nothing is written in `decisions.md` or `flags.md`, and no node's status line is touched.
> 7. The tree meets the bar.
