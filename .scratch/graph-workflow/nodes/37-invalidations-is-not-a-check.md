# Nothing tells a worker to hold its work against the record

Type: grilling
Status: resolved

## Answer

`INVALIDATIONS` becomes a duty to search: before handing back, a worker searches resolved nodes' Answer and condition sections for its work's handles; the spawn carries nothing more.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced [node 382](382-ship-the-search-of-resolved-nodes-before-a-handover.md), which ships the answer. Its `INVALIDATIONS` contradict node 337's clause 13, narrow nodes 263 and 75, and extend nodes 36, 15, 350 and 333; the manager notes them here and edits none. Flags 37.1, 37.2, 37.3 settle at the node closing report.

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

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Nothing tells a worker to hold its work against the record

ANSWER:        **`INVALIDATIONS` is a duty to search, not only a report of what surfaced while working.** The human's reply, `verbatim`: *"ok"*. The payload closed with "Please answer: "ok for recommended", or name an alternative.", so the reply takes this node's `RECOMMENDED` whole. There is no divergence.

               ### The duty
               Before handing back, a worker searches the resolved nodes' `## Answer` and `## Acceptance condition` sections. It searches for the same handles it already searches the open nodes for under node 263's rule: each word its work refuses, each path it changes or moves something out of, and each phrase it supersedes. It reads only what matches, and reports in `INVALIDATIONS` each resolved node its work changes. This is node 263's handle search pointed at resolved nodes instead of open ones. It sits in the same hand: the party that holds the fact and the handles already.

               ### Against what, and why those sections
               Measured over the 275 resolved nodes on 2026-10-02:
               - Whole node files are 79,605 lines. A broad handle such as `map-implementation-rules.md` matches 854 of them, which is too costly.
               - The `## Answer` and `## Acceptance condition` sections together are 19,465 lines. Across eight handles tried, they cost 4 to 172 matching lines per handle.
               - The index, `decisions.md` (298 lines), is cheap but misses nodes. For the handle `expedition-triggers` it finds nodes 218 and 226. The section search also finds nodes 255, 260 and 267, which changed the same file.
               - Conditions are included because 14 resolved implementation nodes hold no `## Answer`, node 218 among them.
               The question was whether an index is enough to judge a collision as well as notice one. The section search settles it: what matches is the decision's own text, so the worker judges from what it has just read.

               ### What the spawn carries
               Nothing more. The worker contracts already let a worker search the whole record instead of reading it. Handing more of the record over would spend the manager's context, which this effort has measured as what fails first.

               ### The accepted miss
               A resolved node that describes a thing in different words from the ones the work uses will not match. This is the same miss node 263 accepted for open nodes. Landed code stays with the cascade's per-candidate pass, under node 15's part 3.

               ### Where it ships
               - One sentence is added to the "Before you write your handover" paragraph of the five worker contracts.
               - The manager contract's `## What nothing here settles` loses its item "Does anything tell a worker to look at the record when it reports what its work invalidates?". The item is named by its text, because node 379's pending work renumbers that list.
               - The `INVALIDATIONS` line and its placeholder are unchanged. The handles are already named in `CONDITIONS`.
               The implementation node below carries this.

               ### The sequencing note about node 43 is moot
               Node 43 is superseded. Its wording landed through node 333 (part F, the five contracts) and node 338 (clause 17b, `graph-conventions.md`), and both are resolved. The `INVALIDATIONS` line quoted in this node's `## Question` is the old one.

INDEX LINE:    `INVALIDATIONS` becomes a duty to search: before handing back, a worker searches resolved nodes' Answer and condition sections for its work's handles; the spawn carries nothing more.

FLAGS:
               ASSUMPTION: I treated the annotation's sequencing note about node 43 as moot. Node 43 is `superseded`. Its demands were carried by node 333's part F and node 338's clause 17b, and both are resolved, which I checked on all three node files and in the five contracts' current `INVALIDATIONS` line. No interview was needed for this, and none was held.
               Index: Node 37's note sequencing it against node 43 is moot, node 43 being superseded and landed through nodes 333 and 338.

               ASSUMPTION: The search targets resolved nodes' `## Answer` and `## Acceptance condition` sections. This rests on my own measurement on 2026-10-02 (counts in the answer), not on an established figure. Landed code was left to the cascade's per-candidate pass under node 15's part 3. The human approved the recommendation that carried this choice.
               Index: Node 37's search target, resolved nodes' Answer and condition sections, rests on its worker's own 2026-10-02 measurement of match costs.

               ASSUMPTION: In the sentence the human approved, I changed "report in `INVALIDATIONS` each one your work changes" to "report in `INVALIDATIONS` each resolved node your work changes", so that "one" has a single clear referent under the effort's writing rule 5. The meaning is unchanged.
               Index: Node 37's shipped sentence says "each resolved node" where the approved wording said "each one", to give the pronoun one referent.

NEW NODES:
               name:      Ship the search of resolved nodes before a handover
               kind:      implementation
               question:  Carry node 37's answer into the five worker contracts and the manager contract: a worker searches the resolved nodes' `## Answer` and `## Acceptance condition` sections for its work's handles before handing back, and reports what it changes in `INVALIDATIONS`.
               blockers:  none. Sequencing only, because the code slot is shared: node 379 (at its gate) edits `## What nothing here settles` in `.claude/skills/expedition/SKILL.md`, and node 380 (open) edits a different sentence of the same five worker contracts. Not joined to node 380: it is the same files but a different concern (what a worker checks in its spawn), so this is new work rather than a defect of that node.
               acceptance condition:

> The work is these six files, and no other file may be edited:
>   `.claude/skills/expedition-grilling/SKILL.md`
>   `.claude/skills/expedition-research/SKILL.md`
>   `.claude/skills/expedition-prototype/SKILL.md`
>   `.claude/skills/expedition-precondition/SKILL.md`
>   `.claude/skills/expedition-implementation/SKILL.md`
>   `.claude/skills/expedition/SKILL.md`
> These are files the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file.
>
> Scope came from two searches over the working tree, run on 2026-10-04. `grep -l "^Before you write your handover, search the open nodes'" .claude/skills/*/SKILL.md` returned exactly the five worker contracts listed above. `grep -rln "Does anything tell a worker to look at the record" .claude/` returned exactly `.claude/skills/expedition/SKILL.md`. If either search reaches a file outside this list when the work is done, report it and do not edit it.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In each of the five worker contracts, the paragraph beginning "Before you write your handover, search the open nodes' `## Acceptance condition` sections" gains one sentence. The sentence is placed immediately after the sentence "Search the open nodes' `## Question` sections the same way, for the same words, paths and phrases, in every open node, claimed or not, and read only what matches." and immediately before "Name in `CONDITIONS` what you searched for." The added sentence is exactly: "Search the resolved nodes' `## Answer` and `## Acceptance condition` sections the same way, for the same words, paths and phrases, read only what matches, and report in `INVALIDATIONS` each resolved node your work changes." Line wrapping may differ. The words may not.
> 2. The paragraph named in clause 1 is byte-identical across the five worker contracts after the work, as it was before.
> 3. In each of the five worker contracts, no other sentence changes. In particular, the handover block's line beginning `INVALIDATIONS:`, the sentence "Report `NEW NODES` and `INVALIDATIONS` yourself. Nothing else reports them.", and the sentence beginning "In `INVALIDATIONS`, an outright contradiction is the minority case" are unchanged. Re-wrapping the lines of the paragraph named in clause 1 to fit the added sentence is not a change of sentence.
> 4. In `.claude/skills/expedition/SKILL.md`, under `## What nothing here settles`, the numbered item beginning "Does anything tell a worker to look at the record when it reports what its work invalidates?" is removed with all of its sentences. The items after it are renumbered in their existing order, so the list's numbers run from 1 with no gap. Every other item keeps its words.
> 5. In `.claude/skills/expedition/SKILL.md`, nothing outside the change in clause 4 changes. The file does not grow, counting lines as `wc -l` prints them, compared with the commit the work starts from.
> 6. No file under `.scratch/` changes, and `.claude/skills/expedition-checker/SKILL.md` and `.claude/skills/expedition-cascade/SKILL.md` do not change.
> 7. The tree meets the bar.

INVALIDATIONS: These come from a search of the resolved nodes' `## Answer` and `## Acceptance condition` sections for "INVALIDATIONS", "go and look", "hold its work against", "What nothing here settles" and "Before you write your handover", reading only what matched.
               - Node 337 ("Carry the record-file test, the home of a standing rule, …"): contradiction of its clause 13. That clause requires the item "Does anything tell a worker to look at the record when it reports what its work invalidates?" to still stand as an unsettled question. This answer removes the item, because the general duty now exists.
               - Node 263 ("Nothing tells the party that falsifies an acceptance condition to go and look for it"): extension. Its handle search now also reaches resolved nodes. Narrowing of its section "Node 37 stays separate": that section says node 37's targets are indexed by `decisions.md`, "read whole by every worker". Resolved nodes are now found by searching their sections, not through the index. (Separately, its statement that node 43 is open is stale. Node 43 is superseded.)
               - Node 36 ("The clause that says no resolved node changes cannot be self-contained"): extension. The duty it placed on `INVALIDATIONS`, which its worker called "checked by nobody … ask a worker to *report* … not to go and look", now carries a duty to search.
               - Node 15 ("Cascade pass mechanics"): extension of part 1, where resolved-node targets ride the worker's handover. The worker now searches for them. Its phrase "a channel nothing tells a worker to go and look at" no longer holds.
               - Node 75 ("Gather the manager's accumulated duties"): narrowing of its item 47, "Nothing today tells a worker to *go and look*". That is no longer true for resolved nodes' answer and condition sections.
               - Node 350 ("Carry the open-question search into the shipped contracts") and node 333: extension. The paragraph they shaped gains a third search.

CONDITIONS:    I listed the open and claimed nodes with `grep -l -E '^Status: (open|claimed)' nodes/*.md`, which returned 22 nodes. I searched their files for: "INVALIDATIONS", "Before you write your handover", "Does anything tell a worker", "What nothing here settles", "read only what matches", "go and look", "the same words, paths and phrases", "resolved nodes'", "Name in `CONDITIONS`", and the paths `expedition-grilling/SKILL.md`, `expedition-research/SKILL.md` and `expedition-implementation/SKILL.md`. I read only what matched.
               - Node 379 (claimed, implementation): its clause 8 removes another item from `## What nothing here settles` and renumbers the rest. My answer makes nothing in it wrong. The new node's clause 4 names its item by text so that it holds in either landing order.
               - Node 380 (open, implementation): it edits the same five worker contracts. Its clauses 5 and 6 bound only its own diff, so nothing in it is made wrong. Sequencing only.
               - Nodes 41 and 32 (open, implementation) name the same contract paths but different passages. Nothing is made wrong.
               - The node 13 matches are in annotations, not in its condition or question.
               No replacement clauses are written, and no open node's question changes. Node 185's question (scoping the `decisions.md` pointer) is untouched in its terms. One reason a worker needed the index, finding resolved nodes for `INVALIDATIONS`, now goes through the section search instead.

MISSING FROM MAP: The map does not say which nodes correspond to the items under the manager contract's `## What nothing here settles`. I found that node 37 is item 3 by searching `.claude/skills/expedition/SKILL.md`, and found node 337's clause 13 by searching resolved sections.

RETROSPECTIVE:
               1. What I had to hunt for: node 379's file and worktree, to confirm the renumbering claim (it is true: node 379 is claimed and at its gate, and its clause 8 removes the flag-check item). I also had to hunt for node 337's clause 13, which the handle search found and which no node file links to node 37. And I checked that all five "Before you write your handover" paragraphs are byte-identical (they are, by md5), so the condition could demand one sentence placed identically.
               2. What arrived that this node did not need: nothing in this resume. The resume message was exactly what was needed.
               3. What would have made this easier: node 37's file linking to node 263, and to node 337's clause 13, which kept the item this node removes.
               4. What was stale, wrong or contradictory: everything the resume message claimed checked out (the human's "ok" is on node 37 under `## Interview`, and node 379's pending removal is real). Still stale: node 37's `## Question` quotes the old `INVALIDATIONS` line, its annotation treats node 43 as pending, and node 263's Answer calls node 43 open.
`````

## Flags

`37.1` `ASSUMPTION` **· settled** — The annotation's sequencing note about node 43 is treated as moot, node 43 being superseded and landed through nodes 333 and 338. *(The worker's full text is under its handover's `FLAGS`.)*

`37.2` `ASSUMPTION` **· settled** — The search targets resolved nodes' Answer and condition sections, on the worker's own 2026-10-02 measurement. *(The worker's full text is under its handover's `FLAGS`.)*

`37.3` `ASSUMPTION` **· settled** — The shipped sentence says "each resolved node" where the approved wording said "each one". *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-04:* flags 37.1, 37.2, 37.3 settle at the node closing report that closes this node.
