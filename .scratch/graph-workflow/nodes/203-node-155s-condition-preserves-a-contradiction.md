# Node 155's condition preserves a contradiction it also creates

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [Pruning a long-running effort's map](70-pruning-a-long-running-map.md)'s worker, and pasted as it
wrote it.*

> Node 155 is open and unclaimed. Its acceptance condition clause 1a requires each worker contract to state that
> *"the bulleted pointer list is what the worker reads whole"*, while clause 3 requires the bullet naming the index
> of decisions to stay **byte-identical**, and that bullet currently reads *"`decisions.md` — the sections the spawn
> names"*. A worker meeting both clauses ships five files that say the index is read whole and read in named
> sections. The human's own ground at node 129 was *"leave decisions in read-whole - it's small enough"*, so the
> bullet is the stale half.

**Blockers, in the worker's words:** *"none — but it must be settled before node 155 is claimed, or landed as an
amendment to it."*

## Acceptance condition

*Written by node 70's worker. Pasted as it wrote it, and not the manager's.*

> The work is node 155's acceptance condition, in
> `.scratch/graph-workflow/nodes/155-carry-the-search-the-record-instruction-into-the-contracts.md`, and no shipped
> file is edited by this node. Done means all of the following are true.
>
> 1. That node's clause 3 no longer requires the bullet naming the effort's index of decisions to be byte-identical,
>    and instead permits exactly one change to it: that the phrase restricting the worker to named sections of that
>    index is replaced by wording stating the file is read whole.
> 2. The rest of clause 3 is unchanged: nothing is removed from any of the five pointer lists, and no other bullet
>    is reworded.
> 3. Clauses 1, 2, 4, 5, 6 and 7 of that condition are unchanged in content, count and order.
> 4. The change is made as a replacement of the superseded wording with its current form, the superseded text
>    appended verbatim to `map-history.md` under a heading naming node 155.
> 5. No file outside the two named above is modified.

## The manager's note at filing

*Not a change to anything above.*

**This node's work is an amendment to another node's acceptance condition, and that is not the manager's to make by
hand here.** Amending a condition is normally the manager's act with the human; this one is large enough to want a
worker and a check, and its author wrote a condition for it rather than handing the manager a sentence. **The
manager records that it took that route and did not shortcut it.**

**Its urgency is a sequencing fact rather than an edge:** node 155 is open and unclaimed, and claiming it before
this lands would ship five contracts contradicting each other. The manager holds that and node 155 stays unclaimed
until this resolves.

**It is the sixth node this session created by a condition fencing a worker out of a defect the condition itself
creates**, and the first found by a worker on an unrelated node reading the record for something else.

## Annotation: this node's own clause 4 is falsified, and the node may no longer be needed at all

*Filed by the manager on 2026-09-19, carrying [node
252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s worker's words rather than the manager's. **It
found this; nobody else had.***

> **This node's clause 4 contradicts [node 199](199-is-an-acceptance-condition-a-rule-or-a-record.md)**, and nothing
> anywhere records it. It demands that node 155's superseded clause be *"appended verbatim to `map-history.md` under
> a heading naming node 155"*; node 199 settled that a condition's superseded clause is *"marked superseded in place,
> inside its node file, and is never removed from it and never appended to `map-history.md`."* Node 203 is open and
> unclaimed, and node 199 resolved after it was minted.

And, separately, on what this node is now for:

> Two of those four are themselves repair nodes, built to amend somebody else's unclaimed condition: node 203 on
> node 155's, and [node 245](245-node-156s-condition-re-derives-a-weaker-property.md) on node 156's. **Under this
> answer the work each names can be done directly.** Node 203 also prices the instrument it is: **the repair node's
> own condition rotted the same way the condition it was built to repair did**, and nobody had recorded it.

***The manager's own note, beside that text.*** **This node is not stood down and its clause 4 is not amended**,
though under node 252 the pen for the second is the manager's. Standing it down has no status to take —
`out-of-scope` says the work is beyond the destination, which is false, and `superseded` needs the node to hold work
and a replacement to point at, and it has neither. That gap is [node
264](264-no-status-for-a-node-whose-work-no-longer-needs-a-node.md), and **this node and node 245 are its two live
instances**, sitting on the frontier where nobody should take them.
