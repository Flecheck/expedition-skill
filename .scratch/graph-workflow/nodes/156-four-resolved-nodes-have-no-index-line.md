# Four resolved nodes have no line in the effort's index of decisions

Type: implementation
Status: claimed

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

## Interview

#### Raise 1, relayed 2026-10-02

*Pasted as the worker handed it back.*

```
NODE:          Four resolved nodes have no index line (node 156)
ABOUT:         This node appends index lines to `.scratch/graph-workflow/decisions.md` for resolved nodes that have none. The work is written and sits uncommitted in the worktree. I am raising before handover because the acceptance condition and a rule the checker holds the work to contradict each other.
SO FAR:        I read the implementation contract, the node file, map.md, map-implementation-rules.md, derivations.md entries (c) and (e), the head and tail of decisions.md, and the `## Answer` sections of nodes 103, 114, 116 and 133.

               Re-derivation for clause 5. I read Status the way derivations.md (c) does: header block only (above the first `##`), fenced blocks skipped, first `Status:` line counts, and the value must equal `resolved` exactly. Counts at 4ed809c59: 273 resolved, 70 superseded, 17 open, 13 out-of-scope, 4 claimed. Two checks over the 273 resolved nodes each missed exactly 103, 114, 116 and 133: whether the node's path appears on any `- ` entry line, and whether it is the lead link of an entry. As a cross-check, I took every node with a `Status: resolved` line anywhere in its text (`grep -lx`, which includes body lines such as node 13's format spec) and tested whether its path appears anywhere in decisions.md. That check missed the same four. So the complete set is still these four. There are no others to append and no shortfall to report, and the manager's claim checks out.

               The work (uncommitted, in `.scratch/graph-workflow/worktrees/156-index-lines`): I appended four lines, and nothing else, to the end of `.scratch/graph-workflow/decisions.md` in order 103, 114, 116, 133. Each line takes the existing form: `- [<node's own H1 title>](nodes/<file>) — <one sentence>`. Each sentence comes from that node's `## Answer`, restates no reasoning, quotes no figure, and runs 25 to 29 words. `git diff --stat` shows 1 file, 4 insertions, 0 deletions. After the append, every resolved node is named by an entry under both readings. One detail: node 116's sentence describes the section the Answer says it added. That section is no longer in the current checker contract (it was changed later), and I wrote the line from the Answer as clause 3 requires. The repo has no build, tests or formatter (I checked the repo; this matches the rules file).

               The contradiction. Clause 1 of the acceptance condition requires appending four entries to `decisions.md`, and clause 6 makes that file the only one changed. But `map-implementation-rules.md`, in its paragraph beginning "An implementation node's work on this effort may be the effort's own record", says: "A change to the node's own status line, to `decisions.md`, or to `flags.md` is bookkeeping reserved to the manager: where one appears among the work the checker's outcome is `FAIL` on the acceptance condition, and that holds whether or not the acceptance condition itself excluded those paths." The checker reads that file and nothing else for its standards. So the only work this condition allows is work the rules file tells the checker to FAIL. Hard rule 1 of the contract allows a worker to write a graph file where its node's own work is a change to that file. The rules file makes no such exception. map.md's standing instruction from node 200's gate makes this a raise and not a flag.
ASK:           Should the checker treat the append to `decisions.md` as this node's work rather than as reserved bookkeeping, so the work as it stands can go to check and the gate?
RECOMMENDED:   Yes. Keep the work as it stands and tell the checker in its spawn that this node's acceptance condition makes `decisions.md` the work itself, under contract hard rule 1. Then file a small node to add that exception to the rules-file sentence. My grounds: the rule exists to stop a worker recording its own node on the graph, and none of these lines is about node 156. The four lines are what the condition demands. Contract hard rule 1 already allows a graph-file change where it is the node's own work.
ALTERNATIVES:  - The manager writes the four lines as ordinary resolution bookkeeping, and this node resolves with no worker diff. The lines I drafted, shown in the diff, can be pasted as they are.
               - Amend the rules-file sentence first to exempt a node whose condition names `decisions.md` as its work, then run the check.
               - Let the checker FAIL and have the human overrule it at the gate. This is the worst option: it spends a check run on a known outcome.

RETROSPECTIVE
1. What I had to hunt for: nothing about the derivation itself, because derivations.md (c) gave the header-block reading directly. The contradiction only came to light because I read the rules file whole. Neither the spawn nor the node mentions it.
2. What arrived that this node did not need: most of map.md (the destination, the Lang and multi-repo notes, the naming history) and most of the rules file (the worktree route, the trigger file, the review route).
3. What would have made this easier: the spawn saying whether this node is exempt from the rule reserving `decisions.md` to the manager. The manager's note says "the contract allows for such a node", but the rules file the checker follows says the opposite.
4. What was stale, wrong or contradictory: the contradiction raised above. A minor stale point: the rules file's review-route paragraph and node 114's Answer still call the glossary `CONTEXT.md` at the repo root, whereas map.md says it moved to `.claude/skills/expedition/glossary.md`. Node 114's index line names `CONTEXT.md` because that is what the node changed at the time.

Paths touched: .scratch/graph-workflow/worktrees/156-index-lines/.scratch/graph-workflow/decisions.md (4 lines appended, uncommitted).
```

*The manager's note:* the manager's spawn said hard rule 1 of the contract allows this node to write `decisions.md`, without checking the rules-file sentence the checker follows. The worker's raise is right that the two disagree.
