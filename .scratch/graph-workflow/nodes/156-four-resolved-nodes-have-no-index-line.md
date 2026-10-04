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

#### The human's answer to raise 1, 2026-10-04

`verbatim`: *"ok"*

The manager had closed the payload with "Please answer node 156's raise: "ok for recommended", or name an alternative." The reply takes the worker's `RECOMMENDED`: "Yes. Keep the work as it stands and tell the checker in its spawn that this node's acceptance condition makes `decisions.md` the work itself, under contract hard rule 1. Then file a small node to add that exception to the rules-file sentence."

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Four resolved nodes have no index line (node 156)

ANSWER:        `.scratch/graph-workflow/decisions.md` has four new entries appended at its end, in ascending order: nodes 103, 114, 116 and 133. Each uses the file's existing form: a markdown link whose text is the node's own H1 title and whose target is `nodes/<file>`, then an em dash, then one sentence of 25 to 29 words. Each sentence comes from that node's `## Answer`, restates no reasoning and quotes no figure. Nothing already in the file was edited, and no other file changed (1 file, 4 insertions, 0 deletions).

               **How "a node whose status is resolved" was read (clause 5).** I read the status the way `derivations.md` entry (c) does. It comes from the header block above the first `##` heading only. Fenced blocks are skipped, the first `Status:` line counts, and the value must equal `resolved` exactly. At 4ed809c59 that gives 273 resolved nodes (also 70 superseded, 17 open, 13 out-of-scope, 4 claimed). I tested each resolved node two ways: is its path named on any `- ` entry line, and is it the lead link of an entry. Both tests missed exactly 103, 114, 116 and 133. I also ran a looser cross-check: every node with a `Status: resolved` line anywhere in its text (`grep -lx`, which also catches body lines like the one in node 13's format spec), tested for its path anywhere in decisions.md. It missed the same four. So the set was exactly the four the condition names, with none extra and none short. After the append, all of these checks return nothing.

               **Node 116's line** describes the checker-contract section that node's Answer says it added. That section is no longer in the current `.claude/skills/expedition-checker/SKILL.md` because later work changed it. Clause 3 asks for the line to come from the node's own Answer, so it does. **Node 114's line** says `CONTEXT.md`, the file that node changed at the time, and not the glossary's current path.

               **The record-file rule.** The rules file reserves a change to `decisions.md` to the manager. The human settled at raise 1 that this node's condition makes that file its work, under the implementation contract's hard rule 1. The checker's spawn carries that. Writing the exception into the rules file is the new node below.

INDEX LINE:    Four resolved nodes that carried earlier decisions into files (103, 114, 116, 133) now have their decisions.md lines; a header-block status re-derivation found no others.

FLAGS:         none

NEW NODES:     **Name:** The rules file reserves `decisions.md` to the manager even where a node's own work is that file
               **Kind:** implementation
               **Question:** In `map-implementation-rules.md`, the paragraph on an implementation node's work being the effort's own record calls any change to `decisions.md` or `flags.md` in the work "bookkeeping reserved to the manager" and makes the checker FAIL it. The implementation contract's hard rule 1 allows a worker to write a graph file where its node's own work is a change to that file. Node 156's condition demanded exactly that, and node 156 had to raise. The rules file should state that exception.
               **Blockers:** none
               **Acceptance condition:**
               > 1. In `.scratch/graph-workflow/map-implementation-rules.md`, in the paragraph beginning "**An implementation node's work on this effort may be the effort's own record**", the sentence that today reads "**A change to the node's own status line, to `decisions.md`, or to `flags.md` is bookkeeping reserved to the manager**: where one appears among the work the checker's outcome is `FAIL` on the acceptance condition, and that holds whether or not the acceptance condition itself excluded those paths." is replaced. The replacement states both of the following in its own words:
               >    (a) a change to the node's own status line is bookkeeping reserved to the manager in every case, and where one appears among the work the checker's outcome is `FAIL` on the acceptance condition;
               >    (b) a change to `decisions.md` or `flags.md` is bookkeeping reserved to the manager, with the same `FAIL`, except where the node's acceptance condition requires a change to that file, in which case that change is the work and is checked against the condition like any other work.
               > 2. The paragraph's other sentences keep their words.
               > 3. The paragraph as it stood before the change is appended **verbatim** to `.scratch/graph-workflow/map-history.md`, at the end of that file, under a new `##` heading of the form "Superseded from `map-implementation-rules.md` at node NN — <what was superseded>", where NN is this node's number. Nothing already in `map-history.md` is edited or removed.
               > 4. No file other than these two is modified. No other paragraph of `map-implementation-rules.md` is modified.
               > 5. Scope came from no search: the named sentence is the work, not an instance of a defect. A search of `.claude/skills` for "bookkeeping reserved" returned nothing at 4ed809c59. Any other statement of the same rule that the work finds is reported and not edited.
               >
               > The work is also held against the bar.

               Not joined to an existing node: I searched the open and claimed nodes' acceptance conditions for `map-implementation-rules` and "bookkeeping reserved". Node 205 targets the same file but a different concern, the bar-commands paragraph. Its clause 5 forbids touching any other paragraph, so it cannot take this one.

INVALIDATIONS: none. The four entries add lines and change nothing any resolved node says.

CONDITIONS:    I searched every open or claimed node's `## Acceptance condition` and `## Question` for `index line`, `decisions.md`, the four node paths `nodes/(103|114|116|133)-`, and "mechanical check 5". Hits:
               - Node 149 and node 284 name `decisions.md` only as a file their work must not touch. Unaffected.
               - Nodes 185, 37 and 211 discuss `decisions.md` as a whole (its size, how spawns scope it, index lines as a carrier of numbers). This work changes none of their premises: the file grew by four lines.
               - Node 156 is this node.
               I also searched the conditions for `map-implementation-rules` and "bookkeeping reserved" while placing the new node. That found node 205 (different paragraph, unaffected) and node 379 (the checker contract, unaffected).
               I wrote no replacement clauses and changed no node's question.

MISSING FROM MAP: map.md and the spawn did not say that the rules file's reserved-bookkeeping sentence covers `decisions.md`, nor that this node was exempt from it. I found the conflict by reading `map-implementation-rules.md` whole and raised it. The human's answer is recorded on node 156 under `## Interview`, and I checked it there.

GATE PAYLOAD:  No checker findings yet. The checker has not run.
               When it does, its spawn should state the human's answer to raise 1: this node's condition makes `decisions.md` the work itself, under the implementation contract's hard rule 1. That answer is recorded on node 156 under `## Interview`, 2026-10-04.

               Bar: the repo has no build, no tests, no formatter and no CI. I checked the repo; this matches the record in `map-implementation-rules.md`, so the bar is the standards and the condition. No method skill was invoked, so none was skipped. Nothing was committed.

               Paths touched: .scratch/graph-workflow/worktrees/156-index-lines/.scratch/graph-workflow/decisions.md (4 lines appended).

               Proposed commit message:
               ```
               Give four resolved nodes their decisions.md index lines

               Nodes 103, 114, 116 and 133 resolved without a line in the index.
               A header-block re-derivation of resolved status found no others.

               Node: graph-workflow/156
               ```

RETROSPECTIVE
1. What I had to hunt for: nothing about the derivation, because `derivations.md` (c) gave the header-block reading directly. I found the reserved-bookkeeping conflict only by reading the rules file whole. Neither the spawn nor the node mentioned it.
2. What arrived that this node did not need: most of map.md (the destination, the Lang and multi-repo notes, the naming history) and most of the rules file (the worktree route, the trigger file, the review route).
3. What would have made this easier: a spawn that said whether this node was exempt from the rule reserving `decisions.md` to the manager. The new node above makes that unnecessary next time.
4. What was stale, wrong or contradictory:
   - The spawn's note said "the contract allows for such a node", but the rules file the checker follows said the opposite. The human has settled that, and the new node fixes it.
   - Minor and stale: the rules file's review-route paragraph and node 114's Answer still name `CONTEXT.md` as the glossary, which map.md says moved to `.claude/skills/expedition/glossary.md`.
   - Every claim in the resumption message checked out: the `## Interview` record on node 156 holds the raise and the human's verbatim "ok" taking `RECOMMENDED`.
`````

*The manager's note:* the node the worker surfaced is filed as [node 381](381-the-rules-file-reserves-decisions-md-even-where-it-is-the-work.md).
