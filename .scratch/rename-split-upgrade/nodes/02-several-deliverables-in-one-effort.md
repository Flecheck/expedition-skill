# How one effort holds several mostly independent deliverables, each its own branch and pull request

Type: grilling
Status: resolved
Labels: SPLIT

## Question

The human works on several things at once in one repository: slightly related, mostly independent. In
their example, a feature led to benchmarking, the benchmarks led to an optimisation, the optimisation
needed a package upgrade that had recently been unblocked, and the benchmarks and optimisation turned
up bugs that needed a fix. They split that work by hand, and some conversations outgrew a 1M-token
context and had to be compacted, losing information. They want one expedition to hold all of it. Each
piece is worked in its own worktree and lands on its own branch as its own pull request. When a piece
is finished, the graph is cleaned of what that piece no longer needs.

What does the workflow need for this? Settle at least the following. What a deliverable is in the
graph, and how a node is tied to one. How a deliverable's branch and worktree relate to the per-node
worktrees the workflow uses today, and to the effort's landing policy, which today fast-forwards each
node into the main checkout. Who pushes and who opens a pull request, given that nothing is pushed
without the human's word. What happens when one deliverable needs another's work before that work has
merged. What "cleanup the graph when each part is finished" means, and how it relates to the existing
`expedition-cleanup` skill's region cleanup.

## Answer

An effort can hold several **deliverables**. A deliverable is one piece of work that lands on its own branch and becomes its own pull request. The mechanism is opt-in: an effort that declares no deliverables lands exactly as it does today. The decisions below are the human's answers to questions Q1 to Q6, with Q3 departing from the recommendation. The settled points marked as assumptions are the worker's, and each is flagged.

**What a deliverable is in the graph (Q1).** `map-manager-only.md` keeps a list of the deliverables currently in progress. Each entry gives:
- the deliverable's name;
- its branch;
- its base, which is either the upstream branch its pull request targets or the name of another deliverable it is stacked on.
The manager adds an entry when the human brings a new piece of work. The entry is removed when that deliverable is cleaned up, so the list holds only the work in progress, however long the effort runs. Each implementation node carries exactly one header field, `Deliverable: <name>`, naming an entry on that list. Only implementation nodes carry the field, because only they produce commits (assumption). A grilling node may serve several deliverables. Labels keep their current meaning as an optional filter, and they never decide where code lands.

**Branches, worktrees and landing (Q2).** Each implementation node keeps its own worktree on its own branch. The worktree is cut from the tip of the node's deliverable branch, not from the main checkout. On approval the manager makes the usual path-limited code commit, carrying the node trailer, on the node's branch. It then moves the deliverable branch forward to that commit, by fast-forward only, and removes the node's worktree and branch. Where the deliverable branch has moved since the node's worktree was cut, the node's commit is put on top of the branch's new tip before the fast-forward. A conflict there starts a correction round that names the conflicted paths (assumption). The deliverable branch has no worktree of its own. The gate, the checker and the counting of code slots by live worktrees are unchanged. A deliverable's branch is created when the deliverable is declared, from its base. It is never created from the main checkout, whose graph commits would otherwise reach the pull request. The main checkout never receives deliverable code. That code reaches it only through the upstream merge of the pull request.

**Push and pull request (Q3).** The human said, verbatim: *"I would say for now push when I approve the push I create the pull request. It's a bit hard since the environement here and at my work is quite a bit different"*. The manager pushes a deliverable's branch only on the human's yes to that push. The human creates the pull request. The manager offers the push when every implementation node tied to the deliverable has resolved, and also whenever the human asks (assumption). Every push needs its own yes, including a push that overwrites the remote branch after a rebase (assumption). A standing yes may cover pushes, as it covers any other item in its scope.

**One deliverable needing another's unmerged work (Q4).** The deliverable that needs the work is stacked on the other one. Its entry names the other deliverable as its base, and its branch is cut from that deliverable's branch. A node may be blocked, by an ordinary graph edge, on a node of its own deliverable or of that deliverable's base. A node may not be blocked on a node of any other deliverable. When the base deliverable gains commits the dependent one needs, the manager rebases the dependent branch onto the base deliverable's branch. When the base deliverable merges upstream, the dependent's base becomes the upstream branch, and the manager rebases onto that. A rebase that conflicts becomes an implementation node in the dependent deliverable.

**Cleanup of a finished deliverable (Q5).** The manager never learns by itself that a pull request merged. It learns this when the human says so (assumption). When the human says a deliverable's pull request has merged, the manager proposes a region cleanup under `expedition-cleanup`, with the deliverable as the region. The proposed set holds:
- the nodes tied to the deliverable;
- each resolved node whose every dependent is in the set.
The skill's existing safeguards apply unchanged:
- every node in the set is resolved;
- nothing outside the set refers to a node in it;
- outstanding flags go to the human first;
- the human confirms the set.
When the record is cleaned, the manager removes the deliverable's entry from the list and deletes its local branch. The remote branch is left to the human's host. A node that something outside the set still refers to stays in the graph.

**Name (Q6).** The concept is called *deliverable*, and the node field is `Deliverable:`. Handover's `_Avoid_` line keeps refusing "deliverable" as a word for a handover, because the word now names this concept.

**An effort with no planned end.** The human may run one effort indefinitely and add small tasks to it as they come. This needs no new mechanism (assumption). Such an effort states a lasting purpose as its destination, and its map's existing line says it is not expected to reach that destination.

**git-branchless.** The human asked whether git-branchless would simplify this. The shipped files neither need nor name it. Every step above is plain git, and ground rule 1 forbids assuming a tool. git-branchless runs alongside plain git, so a human who uses it can keep using it on these branches. An effort's own landing policy in its map may name it where the human wants it used (assumption).

**MISSING FROM MAP, as the worker wrote it:** The map does not say what this effort's own landing looks like next to a deliverable. I took it from `map-manager-only.md`'s `## Landing an implementation node's work`, which the contract does not list for a worker. A worker on node 02 or 03 needs that policy as the baseline to change. I went on by reading it. Otherwise none.

## Flags

`02.1` `ASSUMPTION` **· settled** — (opt-in): An effort that declares no deliverables lands exactly as today, so existing efforts and their landing policies are untouched. I settled this because nothing in the human's request asks to change the single-branch case.

`02.2` `ASSUMPTION` **· settled** — (field only on implementation nodes): Only implementation nodes carry `Deliverable:`, because only they produce commits, and a grilling node may serve several deliverables.

`02.3` `ASSUMPTION` **· settled** — (when the push is offered): The manager offers a deliverable's push when every implementation node tied to it has resolved, and also whenever the human asks. Every push needs its own yes, including a push that overwrites the remote branch after a rebase. The human's Q3 answer fixed who pushes and who opens the pull request, but not when the push is offered.

`02.4` `ASSUMPTION` **· settled** — (merge known only from the human): The manager does not watch the host for merges. Because the human creates and merges pull requests in environments that differ, a merge is known only when the human reports it.

`02.5` `ASSUMPTION` **· settled** — (landing onto a moved deliverable branch): Where a deliverable branch has moved since a node's worktree was cut, the node's commit is put on its new tip before the fast-forward, and a conflict starts a correction round naming the conflicted paths. This follows the existing rule for integration conflicts.

`02.6` `ASSUMPTION` **· settled** — (an effort with no planned end): The human's possible use of one indefinite effort is served by the existing "not expected to reach its destination" line, so no new term or mechanism is added.

`02.7` `ASSUMPTION` **· settled** — (git-branchless): The human asked whether git-branchless helps, and added that the skill should not depend on it. The shipped files neither name nor need it. An effort's own landing policy may name it where the human wants it used.

## Interview

### Attempt 1 — agent `a49a720ff5476d15d`

**Relayed question, payload 1, as the worker wrote it:**

NODE:          How one effort holds several mostly independent deliverables, each its own branch and pull request

ABOUT:         This node decides how one expedition can hold several separate pieces of work, each landing on its own branch as its own pull request. The work in your example was a feature, benchmarks, an optimisation, a package upgrade and a bug fix. Node 03 (upgrading a conversation into an expedition) builds on this answer.

SO FAR:        I read the node, the map, the shipped landing rules (`SKILL.md` `### Three outcomes, and no fourth`, `graph-conventions.md` `## The seven files`), the glossary, `expedition-cleanup`, and this effort's own landing policy in `map-manager-only.md`. The facts these questions rest on:
               - The shipped files fix only the order of landing: approval comes before any commit, and the graph is edited before cleanup. Each effort's map states its own landing policy. Today that policy is one worktree per implementation node, on its own branch. On approval the manager makes one path-limited commit there, fast-forwards the main checkout to it, and removes the worktree and the branch.
               - The code-slot count is found by counting live worktrees, with one worktree per claimed implementation node.
               - Labels already exist. They are optional, a node can carry several, and a label is "only a filter".
               - The glossary refuses "deliverable" as a word for a worker's handover. Choosing a name for the new concept is a later question.
               - On this machine the main checkout carries the record's "Graph state" commits, which have not been pushed. A branch cut from the main checkout would carry those commits into a pull request.
               I settled two things myself, so you can correct either one now:
               - An effort that declares no deliverables lands exactly as it does today. The new mechanism is opt-in.
               - Only implementation nodes are tied to a deliverable, because only they produce commits. A grilling node may serve several deliverables.
               Three more questions come in later messages, once these are answered. The first is what happens when one deliverable needs another's work that has not merged yet. The second is what "clean up the graph when a part is finished" does. The third is what the concept is called.

Q1. What a deliverable is in the graph
ASK:           How is a deliverable represented, and how is a node tied to one?
RECOMMENDED:   The effort's map declares a list of deliverables in `map-manager-only.md`, beside the landing policy. Each entry gives a name, the deliverable's branch, and the upstream branch its pull request targets. Each implementation node carries exactly one new header field that names its deliverable. The field takes one value, so a commit can never be unclear about which branch it goes to. Labels keep their current meaning as an optional filter, and they never decide where code lands.
ALTERNATIVES:  Reuse labels as deliverables. This is simpler, but labels are optional and a node can carry several, so the label would quietly start to decide where code lands.
               One effort per deliverable. This is what you do by hand today, and you asked to get away from it.
               An umbrella node per deliverable. A node is sized to one agent's work, so this does not fit.

---

Q2. How a deliverable's branch relates to the per-node worktrees and to landing
ASK:           Where does a node's work land when the node belongs to a deliverable?
RECOMMENDED:   Keep one worktree per node, but cut it from the tip of the node's deliverable branch instead of from the main checkout. On approval the manager makes the same path-limited commit, then fast-forwards the deliverable branch to it. Today it would fast-forward the main checkout. Then the manager removes the node's worktree.
               The deliverable branch needs no worktree of its own. It is a branch that only ever moves forward, so the gate, the checker and the slot counting stay as they are.
               The deliverable branch is created when the deliverable is declared, from the upstream branch its pull request targets. Creating it from the main checkout would carry graph commits into the pull request.
               The main checkout never receives deliverable code. That code reaches it the usual way, once the pull request merges upstream.
ALTERNATIVES:  One long-lived worktree per deliverable, with nodes worked directly in it. This allows only one node at a time per deliverable, and it breaks the rule that each claimed node has its own worktree.
               Land into the main checkout as today, and build each deliverable's branch afterwards by cherry-picking commits by their node trailer. This is fragile, and it puts every deliverable's code into the main checkout together.

---

Q3. Who pushes and who opens the pull request
ASK:           When a deliverable's branch is ready, who pushes it and opens its pull request?
RECOMMENDED:   The manager does both, and only on your explicit yes for that one deliverable. When every implementation node tied to a deliverable has resolved, the manager asks you whether to push its branch and open its pull request. On yes, it pushes and opens the pull request with whatever tool it finds for the repository's host. Where it finds none, it pushes and gives you the branch name.
               A later push to the same branch, for example after you review the pull request, needs a fresh yes. A standing yes can cover these pushes if you give one. This keeps "nothing is pushed without the human's word" while sparing you the mechanics.
ALTERNATIVES:  You always push and open pull requests yourself, and the manager only tells you that the branch is ready.
               The manager pushes at every node approval, so the pull request grows as the work does. Each approval at the gate would then also mean "push", which changes what approval means.

**The human's words bearing on this node, `verbatim`, sent while payload 1 was queued and before it was relayed:**

> Also for Destination 2, I am not sure yet but I might want it to be my main way of working and continue indefinity on it for all small tasks, as I have new things to do I add then and when they are merged I cleanup the graph.

*Manager's note:* not an answer to payload 1, which the human has not seen. Passed to the worker so it can say whether its payload changes before it is relayed.

**Relayed question, payload 1 revised, as the worker wrote it. It replaces payload 1 above, which was never relayed:**

I revised the payload because of your note. A deliverable is now something that can be added to a long-running effort and removed from it again, so Q1 says a deliverable's entry is removed at cleanup and adds an option that the human's note rules out. SO FAR now carries the human's words on destination 2 and lists one more later question. Q2 and Q3 are unchanged.

NODE:          How one effort holds several mostly independent deliverables, each its own branch and pull request

ABOUT:         This node decides how one expedition can hold several separate pieces of work, each landing on its own branch as its own pull request. The work in your example was a feature, benchmarks, an optimisation, a package upgrade and a bug fix. Node 03 (upgrading a conversation into an expedition) builds on this answer.

SO FAR:        I read the node, the map, the shipped landing rules (`SKILL.md` `### Three outcomes, and no fourth`, `graph-conventions.md` `## The seven files`), the glossary, `expedition-cleanup`, and this effort's own landing policy in `map-manager-only.md`.
               You said you might make this your main way of working. That would be one effort that runs with no planned end, where you add new pieces of work as they come and clean each one out of the graph once it has merged. I designed for that case, and it also covers an effort that does end.
               The facts these questions rest on:
               - The shipped files fix only the order of landing: approval comes before any commit, and the graph is edited before cleanup. Each effort's map states its own landing policy. Today that policy is one worktree per implementation node, on its own branch. On approval the manager makes one path-limited commit there, fast-forwards the main checkout to it, and removes the worktree and the branch.
               - The code-slot count is found by counting live worktrees, with one worktree per claimed implementation node.
               - Labels already exist. They are optional, a node can carry several, and a label is "only a filter".
               - The glossary refuses "deliverable" as a word for a worker's handover. Choosing a name for the new concept is a later question.
               - On this machine the main checkout carries the record's "Graph state" commits, which have not been pushed. A branch cut from the main checkout would carry those commits into a pull request.
               - The map already has a way to say that an effort is not expected to reach its destination. For such an effort, a frontier that never empties is normal and is not a defect.
               I settled two things myself, so you can correct either one now:
               - An effort that declares no deliverables lands exactly as it does today. The new mechanism is opt-in.
               - Only implementation nodes are tied to a deliverable, because only they produce commits. A grilling node may serve several deliverables.
               Four more questions come in later messages, once these are answered. The first is what happens when one deliverable needs another's work that has not merged yet. The second is what "clean up the graph when a part is finished" does, which matters more now that cleanup would happen again and again. The third is how a long-running effort of this kind says it has no planned end. The fourth is what the concept is called.

Q1. What a deliverable is in the graph
ASK:           How is a deliverable represented, and how is a node tied to one?
RECOMMENDED:   The effort's map keeps a list of deliverables in `map-manager-only.md`, beside the landing policy. Each entry gives a name, the deliverable's branch, and the upstream branch its pull request targets. The manager adds an entry whenever you bring a new piece of work, and the entry is removed when that deliverable is cleaned up. So the list holds only the work that is currently in progress, however long the effort runs.
               Each implementation node carries exactly one new header field that names its deliverable. The field takes one value, so a commit can never be unclear about which branch it goes to. Labels keep their current meaning as an optional filter, and they never decide where code lands.
ALTERNATIVES:  Reuse labels as deliverables. This is simpler, but labels are optional and a node can carry several, so the label would quietly start to decide where code lands.
               One effort per deliverable. This is what you do by hand today, and you asked to get away from it.
               An umbrella node per deliverable. A node is sized to one agent's work, so this does not fit.
               A new effort for each batch of work, with no list kept in the map. This goes against your wish to keep one effort running indefinitely.

---

Q2. How a deliverable's branch relates to the per-node worktrees and to landing
ASK:           Where does a node's work land when the node belongs to a deliverable?
RECOMMENDED:   Keep one worktree per node, but cut it from the tip of the node's deliverable branch instead of from the main checkout. On approval the manager makes the same path-limited commit, then fast-forwards the deliverable branch to it. Today it would fast-forward the main checkout. Then the manager removes the node's worktree.
               The deliverable branch needs no worktree of its own. It is a branch that only ever moves forward, so the gate, the checker and the slot counting stay as they are.
               The deliverable branch is created when the deliverable is declared, from the upstream branch its pull request targets. Creating it from the main checkout would carry graph commits into the pull request.
               The main checkout never receives deliverable code. That code reaches it the usual way, once the pull request merges upstream.
ALTERNATIVES:  One long-lived worktree per deliverable, with nodes worked directly in it. This allows only one node at a time per deliverable, and it breaks the rule that each claimed node has its own worktree.
               Land into the main checkout as today, and build each deliverable's branch afterwards by cherry-picking commits by their node trailer. This is fragile, and it puts every deliverable's code into the main checkout together.

---

Q3. Who pushes and who opens the pull request
ASK:           When a deliverable's branch is ready, who pushes it and opens its pull request?
RECOMMENDED:   The manager does both, and only on your explicit yes for that one deliverable. When every implementation node tied to a deliverable has resolved, the manager asks you whether to push its branch and open its pull request. On yes, it pushes and opens the pull request with whatever tool it finds for the repository's host. Where it finds none, it pushes and gives you the branch name.
               A later push to the same branch, for example after you review the pull request, needs a fresh yes. A standing yes can cover these pushes if you give one. This keeps "nothing is pushed without the human's word" while sparing you the mechanics.
ALTERNATIVES:  You always push and open pull requests yourself, and the manager only tells you that the branch is ready.
               The manager pushes at every node approval, so the pull request grows as the work does. Each approval at the gate would then also mean "push", which changes what approval means.

**The human's answer to payload 1 revised, `verbatim`:**

> Q1 ok Q2 ok Q3 I would say for now push when I approve the push I create the pull request. It's a bit hard since the environement here and at my work is quite a bit different

Q1 takes the worker's `RECOMMENDED`: *"The effort's map keeps a list of deliverables in `map-manager-only.md`, beside the landing policy."* Q2 takes the worker's `RECOMMENDED`: *"Keep one worktree per node, but cut it from the tip of the node's deliverable branch instead of from the main checkout."*

`DIVERGENCE` on Q3: the worker recommended *"The manager does both, and only on your explicit yes for that one deliverable."* The human's answer has the push happen on their approval, and has the human create the pull request.

**Relayed question, payload 2, as the worker wrote it:**

NODE:          How one effort holds several mostly independent deliverables, each its own branch and pull request

ABOUT:         This node decides how one expedition can hold several separate pieces of work, each landing on its own branch as its own pull request. It may become the long-running effort you described for all your small tasks. Node 03 (upgrading a conversation into an expedition) builds on this answer.

SO FAR:        Your answers to the last message are settled as follows:
               - (Q1) The map keeps a list of the deliverables currently in progress. Each entry gives a name, the deliverable's branch, and the upstream branch it targets. Each implementation node names its one deliverable in a new header field.
               - (Q2) Each node gets its own worktree, cut from its deliverable's branch. On approval the deliverable branch is fast-forwarded to the node's commit. The main checkout never receives deliverable code.
               - (Q3) The manager pushes a deliverable's branch only when you approve that push, and you create the pull request yourself. This is the arrangement "for now", given how different your two environments are.
               I settled three more things myself, so you can correct any of them now:
               - The manager offers the push when every implementation node tied to a deliverable has resolved, and also whenever you ask for it. Every push needs its own yes, including a push that has to overwrite the remote branch because the branch was rebased.
               - Running one effort indefinitely needs no new mechanism. The map can already say that an effort is not expected to reach its destination, and the workflow then treats a frontier that never empties as normal. An effort run that way states a lasting purpose as its destination and says it does not expect to reach it.
               - The manager never learns by itself that a pull request has merged, because you create the pull requests and merge them on your host. It learns this only when you tell it.

Q4. One deliverable needs another's work before that work has merged
CONTEXT:       In your example, the optimisation needed the package upgrade. If those are two deliverables, the optimisation's nodes need code that sits on the upgrade's branch and has not yet merged upstream.
ASK:           What happens when a deliverable needs another deliverable's work that has not merged yet?
RECOMMENDED:   The deliverable that needs the work is stacked on the other one. Its entry in the map names the other deliverable as its base, instead of the upstream branch, and its branch is cut from the other deliverable's branch.
               A node in the dependent deliverable may then be blocked, by an ordinary graph edge, on a node in its base deliverable. A node in any other deliverable may not.
               When the base deliverable gains commits that the dependent one needs, the manager rebases the dependent branch onto it. When the base deliverable merges upstream, the dependent's base becomes the upstream branch again, and the manager rebases onto that. A rebase that conflicts becomes an implementation node in the dependent deliverable.
               This keeps work moving while the base deliverable is still being reviewed. It also matches how pull requests are commonly stacked, and you would open the dependent pull request against the base deliverable's branch.
ALTERNATIVES:  The dependent work waits until the base deliverable merges upstream. This is simpler, but it stalls the work for as long as the review takes, and the graph has no edge that can wait on a merge on your host.
               The two are merged into one deliverable and land as one pull request. This is simple, but it gives up the separate pull requests you asked for.

---

Q5. What cleaning up a finished deliverable does
ASK:           When a deliverable is finished, what does cleaning up the graph do, and what starts it?
RECOMMENDED:   It starts when you tell the manager that a deliverable's pull request has merged. The manager then proposes a region cleanup, using the `expedition-cleanup` skill's existing region cleanup, with the deliverable as the region.
               The proposed set holds the nodes tied to that deliverable. It also holds each resolved node whose every dependent is in the set, which brings in the decisions that served only that deliverable.
               The skill's existing safeguards still apply. Every node in the set must be resolved. Nothing outside the set may refer to a node in it. Outstanding flags go to you first. You confirm the set.
               When the record is cleaned, the manager also removes the deliverable's entry from the map and deletes its local branch. The remote branch is left to your host.
               A node that another node still refers to stays in the graph. That way a decision that later work relies on is not removed.
ALTERNATIVES:  You invoke `/expedition-cleanup` yourself each time and name the region, exactly as today. Nothing changes, but you would have to remember to do it after every merge.
               The manager cleans up without asking you to confirm the set. The skill forbids this today, and a decision that later work relies on could be removed.
               The cleanup starts when the last node of the deliverable lands, rather than when the pull request merges. Your review of the pull request could still send the work back.

---

Q6. What the concept is called
ASK:           What is a deliverable called in the skill files? Its name also becomes the name of the new header field on a node.
RECOMMENDED:   "deliverable", with a node field written `Deliverable: <name>`. The word means one piece of work that is handed over, which here is one branch and one pull request, and it is the word you and this node already use.
               The glossary refuses "deliverable" today, but only as a word for a worker's handover. That refusal stays, and it becomes stronger, because the word now names something else.
               "branch" and "pull request" are words that git and your host already own, so those words stay with them.
ALTERNATIVES:  "piece" or "part", your own words in the request. They are vague in a sentence such as "the node's part".
               "strand" or "track". Both are made-up figures of speech, which the writing rules refuse.
               "feature". Too narrow, because a bug fix or a package upgrade is not a feature.

**The human's answer to payload 2, `verbatim`:**

> Q4 ok , I also tend to use git branchless that might simplify things ? But also the skill should probably not depend on it. I would guess for you it's not really needed anyway Q5 ok Q6 ok

Q4 takes the worker's `RECOMMENDED`: *"The deliverable that needs the work is stacked on the other one."* Q5 takes the worker's `RECOMMENDED`: *"It starts when you tell the manager that a deliverable's pull request has merged. The manager then proposes a region cleanup"*. Q6 takes the worker's `RECOMMENDED`: *""deliverable", with a node field written `Deliverable: <name>`."*

## Annotation: node 03 extends the branch-creation rule for an upgrade

As the worker of [node 03](03-upgrade-a-conversation-into-an-expedition.md) reported it: Node 02 is extended, not contradicted. Its answer says a deliverable's branch "is created when the deliverable is declared, from its base". For an upgrade, the human added that a branch which already exists can be promoted to a deliverable, so a deliverable declared by an upgrade may take an existing branch rather than a new one. The new node's clause 5 states this as a change made only for the upgrade's case.

## Annotation: node 05 narrows and extends this answer as it ships it

As the worker of [node 05](05-ship-deliverables.md) reported it: Node 02 (resolved) is extended and narrowed, not contradicted:
- its cleanup set ("each resolved node whose every dependent is in the set") is narrowed to nodes with at least one dependent, and applied repeatedly;
- "the manager removes the deliverable's entry ... and deletes its local branch" is narrowed to the point when no remaining node names the deliverable;
- the blocking limit is narrowed to nodes that name a deliverable;
- it is extended: the push offer is the manager's own raise, a standing yes covers a push as a stated exception to `expedition-standing-yes`, entry changes and removals go through `### Change the map`, and a conflicting rebase is left undone.

*Manager's note:* the stated exception became a fourth kind of item in `expedition-standing-yes` in node 05's correction round 1.

## Annotation: node 06 lets every node kind carry `Deliverable:`

As the worker of [node 06](06-which-checkout-a-non-implementation-worker-reads.md) reported it: Node 02 (resolved): narrowed and partly contradicted. Its answer says "Only implementation nodes carry the field", and assumption 02.2 says the same "because only they produce commits, and a grilling node may serve several deliverables". The human's Q1 answer lets every node kind carry `Deliverable:`, with zero, one or several names on a non-implementation node. The implementation node's single value stands.

## Annotation: node 08 adds the local merge

As the worker of [node 08](08-a-deliverable-that-lands-by-merging-locally.md) reported it: Node 02: an extension and a narrowing. Node 02 says a deliverable "lands on its own branch and becomes its own pull request". It may now instead be merged locally, on a third form of base, `local <branch>`. Node 02's reason for never creating a deliverable's branch from the main checkout now applies only to a deliverable that lands by pull request. Cleanup starting "when the human says the pull request merged" now covers only that route. A local merge starts cleanup at once.

## Annotation: node 15 narrows the cleanup safeguard on flags

As the worker of [node 15](15-whether-flags-md-is-dropped.md) reported it: 02: a narrowing. Its `## Answer` lists "outstanding flags go to the human first" among the region cleanup safeguards. Now only an outstanding `FRICTION` flag on an effort whose product is not the expedition skill files is shown to the human, in the confirmation, and other outstanding flags are listed by id in the report.
