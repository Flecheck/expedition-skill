# Nothing tells a worker to hold its work against the record

Type: grilling
Status: claimed

## Question

The record-wide demand has left acceptance conditions, and `INVALIDATIONS` on the handover is now the only
thing carrying it. **Nothing tells a worker to go and look.**

All five worker contracts word it as a report:

```
INVALIDATIONS: <which resolved node your work contradicts, and how>
```

> *"Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them."*

There is no instruction to check, and no statement of how much of the record a worker is expected to read
to answer it. A worker reads its own node, `map.md`, and only the `decisions.md` sections its spawn names —
so it cannot hold its work against the whole record either.

**Is `INVALIDATIONS` a duty to check, or only to report what surfaced while working?** If the former,
against what — and does the spawn have to hand the worker more of the record than it does today?

### Why this exists

Created at [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md)'s gate, reported by that node's own
worker as **the honest cost of the answer it had just shipped**. That node ruled the demand out of
acceptance conditions on the ground that `INVALIDATIONS` already carries it, addressed to a party that can
discharge it. Its worker then said what that leaves, in its own words:

> The duty's new home is checked by nobody: the five contracts ask a worker to *report* `INVALIDATIONS`,
> not to go and look, and nothing says how much of the record a worker is expected to hold its work
> against. That is strictly better than where it was — four independent blind checkers each spent a verdict
> on node 22's condition 3 and each declared it not establishable — but it is not enforcement.

**Nothing checks it in either case, which was also true of the clause it replaces.** So this node is not a
regression opened by node 36; it is the same hole, now in one place instead of two, and visible.

### One fact already established, and it bounds the answer

Node 36's checker went and confirmed the asymmetry the shipped paragraph rests on, rather than taking the
file's word for it: `INVALIDATIONS` is present in all five worker contracts and **absent from the
checker's own**. It also settled how much of the record a worker can reach — all five contracts read
`decisions.md`, which is one capped line per resolved node and therefore **the index of the whole decision
record**; only `flags.md` is withheld, and flags are not decisions.

So a worker can already reach an index of every decision the effort has made. What it cannot reach cheaply
is the reasoning behind any of them, which lives in the node files. Whether the index is enough to answer
`INVALIDATIONS` honestly is the crux: an index is enough to notice a collision and not enough to judge one.

### What the answer touches

The five `.claude/skills/expedition-<type>/SKILL.md` contracts, and possibly
[Subagent context contract](12-subagent-context-contract.md)'s spawn template if the answer is that the
spawn must hand over more of the record.

**Sequencing, not a blocker.** Those five files are also the live territory of [Checking a flag before the
human sees it](30-checking-a-flag-before-the-human.md), [A worker's handover carries no acceptance
condition for the node it mints](35-handover-mints-no-condition.md) and [Narrow the flags.md clause in the
worker contracts](32-narrow-flags-file-clause.md). The landing policy forbids a second commit against one
**node**, not against one **file**, so these may run in any order — but not concurrently, the code slot
being exclusive.

### Adjacent, and not the same question

[Cascade pass mechanics](15-cascade-pass-mechanics.md) owns the pass that propagates a *known* revision
outward, and [What keeps the shipped files consistent when a decision changes a
term](29-shipped-file-consistency.md) owns the same problem for product files. Both are about acting on an
invalidation once someone has found one. This node is about **finding** it, at the one moment a party with
the work in front of it is already being asked.

## Annotation: the same question, with a larger share of the traffic riding on it

Added by [Cascade pass mechanics](15-cascade-pass-mechanics.md)'s worker, in its words:

> [Nothing tells a worker to hold its work against the record](37-invalidations-is-not-a-check.md) keeps
> its whole question and gains a reason it matters more: part 1 now carries eighteen twenty-eighths of this
> effort's propagation traffic on a channel nothing tells a worker to go and look at.

One sequencing fact for whoever claims this node: [Widen the invalidation channel from contradiction to
change](43-widen-the-invalidation-channel.md) rewords the same part in the same five contracts this node's
answer would reach, and the code slot is exclusive, so the two run in some order and never together.

## Interview


#### Question 1, relayed 2026-10-02

*Pasted as the worker handed it back.*

```
NODE:          Nothing tells a worker to hold its work against the record (node 37)
ABOUT:         Each worker's handover has an `INVALIDATIONS` part, which names the resolved nodes the work changes. No contract tells the worker to go and look for those nodes, so the part only reports what the worker happened to notice. This node decides whether the worker must check, and against what. It comes up now because node 36 left the record-wide demand with this part alone, and node 15 later sent most resolved-node propagation through it.

SO FAR:        What I read: my node file, the grilling contract, map.md, decisions.md in full, and nodes 43, 185 and 263. I also searched the five worker contracts, the manager contract and graph-conventions.md.

               Facts I checked:
               - The manager's note is correct. Node 43 ("widen the invalidation channel") is superseded. Its wording landed through node 333 (part F, the five contracts) and node 338 (clause 17b, graph-conventions.md), and both are resolved. All five contracts now read `INVALIDATIONS: <which resolved node your {answer|facts|work} changes, and how: a rename, an extension, a narrowing or a contradiction of what it says>`. The node's sequencing note about 43 no longer applies, and the old line quoted in its question is out of date.
               - The hole is still there. The manager contract's `## What nothing here settles` item 3 says so: "Does anything tell a worker to look at the record when it reports what its work invalidates? Nothing does in general..."
               - One bounded case already has a duty to look. Node 263 made every worker search the open nodes' `## Acceptance condition` and `## Question` sections for the handles its work fixes (each word it refuses, each path it changes, each phrase it supersedes) and read only what matches. That paragraph is the same in all five contracts and opens "Before you write your handover". Node 263 kept resolved nodes out of its scope and left them to this node.
               - The checker contract and the cascade contract have no `INVALIDATIONS` part.

               What I measured: I ran node 263's handle search against resolved nodes instead of open ones. There are 275 resolved nodes.
               - Searching the whole resolved node files (79,605 lines) is too costly. A broad handle such as `map-implementation-rules.md` matches 854 lines.
               - Searching only their `## Answer` and `## Acceptance condition` sections (19,465 lines) costs 4 to 172 matching lines per handle across the eight handles I tried.
               - The index (`decisions.md`, 298 lines) is cheap but misses things. For the handle `expedition-triggers`, the index finds 2 lines (nodes 218 and 226). The section search also finds nodes 255, 260 and 267, which changed that same file.
               - The `## Acceptance condition` sections have to be included. 14 resolved implementation nodes have no `## Answer`, node 218 among them.
               - The node asks whether an index is enough to judge a collision. A section search answers that: what matches is the decision's own text, so the worker can judge from what it has just read.

               What I settled myself: node 43's sequencing note is moot, for the reasons above. I priced the duty with my own measurement, as node 263 did. I treated "what a resolved node says" as its Answer, or its condition where it has no Answer, and left landed code to the cascade under node 15 part 3.

ASK:           Should `INVALIDATIONS` be a duty to search the resolved nodes, rather than a report of whatever the worker happened to see? If so, should it search their answer and condition sections, the index, or something the spawn hands over?

RECOMMENDED:   Yes. Make it the same handle search node 263 shipped for open nodes, pointed at resolved nodes. The spawn hands over nothing more. It ships, as two small changes to existing text and no new section:
               1. In each of the five worker contracts, add one sentence to the "Before you write your handover" paragraph, right after its open-question search: "Search the resolved nodes' `## Answer` and `## Acceptance condition` sections the same way, for the same words, paths and phrases, read only what matches, and report in `INVALIDATIONS` each one your work changes." The `INVALIDATIONS` line and its placeholder stay as they are. The handles are already named in `CONDITIONS`.
               2. Remove item 3 from the manager contract's `## What nothing here settles`, because this answers it.
               The accepted gap is the one node 263 accepted: a resolved node that describes the thing in different words will not match.
               Why: the party that made the change already holds the handles, so the search is close to free in its context. It finds the nodes the index misses (3 of the 5 in the triggers-file test). It costs one sentence per contract and removes one item, which suits your wish for compact skills. Handing more of the record over in the spawn would spend the manager's context, which this effort has measured as what fails first.

ALTERNATIVES:
               - Search the index, then read only the matching nodes: cheapest, but in the triggers test it missed 3 of the 5 nodes that matter.
               - Search the resolved node files whole: complete, but a broad handle matches up to 854 lines.
               - Have the spawn name the resolved nodes that bear on the work (this ties into node 185's scoping question): spends the manager's context and depends on the manager guessing what the work will touch.
               - Keep it a report and say so in the contracts: honest, but leaves node 15's main propagation channel unchecked.
               - Put the duty on the manager when it resolves a node: one party, but node 263 found that repairs stall in the manager's hands.

RETROSPECTIVE:
               1. What I had to hunt for: whether node 43 had landed (its node file, then 333 and 338), the current `INVALIDATIONS` wording, and the fact that 14 resolved implementation nodes have no `## Answer`, which changed the search target.
               2. What arrived that this node did not need: most of decisions.md (about 300 lines; I used about six), the node's "What the answer touches" sequencing over nodes 30, 32 and 35, and the map's worktree and landing items.
               3. What would have made this easier: the node saying it is the manager contract's `## What nothing here settles` item 3, and node 263 being linked from my node file. Node 263 links to node 37, but node 37 does not link back.
               4. What was stale, wrong or contradictory: the node's question quotes the old `INVALIDATIONS` line ("your work contradicts"). Its annotation treats node 43 as open future work, but node 43 is superseded and landed. Node 263's Answer also calls node 43 "open" and says decisions.md is "read whole by every worker", but the contract now reads "the sections the spawn names".
```

#### The human's answer to question 1, 2026-10-04

`verbatim`: *"ok"*

The manager had closed the payload with "Please answer: "ok for recommended", or name an alternative." The reply takes the worker's `RECOMMENDED`: "Yes. Make it the same handle search node 263 shipped for open nodes, pointed at resolved nodes. The spawn hands over nothing more."
