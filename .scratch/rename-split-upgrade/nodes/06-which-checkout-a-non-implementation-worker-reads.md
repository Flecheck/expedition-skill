# Which checkout a non-implementation worker reads in an effort with deliverables

Type: grilling
Status: resolved
Labels: SPLIT

## Question

`SKILL.md` says "every other worker reads the main checkout". With deliverables, the main checkout never receives a deliverable's code until its pull request merges upstream. So a grilling or precondition worker serving a deliverable cannot see that deliverable's landed work. Should such a worker read the deliverable's branch, and how is that given to it without a worktree?

*Manager's note:* minted by the worker of [node 05](05-ship-deliverables.md) on its `NEW NODES` part, with the question as it wrote it.

## Answer

A grilling, precondition or prototype worker reads a deliverable's code at a fixed commit through git, without a checkout. Which deliverables it reads is recorded on the node, in a `Deliverable:` field that any kind of node may now carry.

**Which deliverables a node serves (Q1).** Every kind of node may carry `Deliverable:`. The human said, verbatim: *"Q1 maybe add a Deliverable field with a list in it for relevent deliverable, so we can do 1, 0 or mutliple"*. This went against the recommendation, which was to have the spawn name the deliverables and add no field.
- An implementation node keeps exactly one name, because its commit lands on exactly one branch.
- A grilling, precondition or prototype node lists the deliverables it serves, comma-separated as `Labels:` is.
- A node that serves no deliverable carries no field (assumption).
- A node belongs to every deliverable it lists. This applies to the rule on which nodes may block which (assumption).
- Whoever creates a node sets the field. A worker reporting a node gives the field's value in that node's `NEW NODES` block (assumption).

**How the worker reads the code (Q2).** The human said, verbatim: *"Q2 I feel like a worktree for each deliverable might be good for this but I don't know, it seems that for llms it is quite easy to look at files on a branch without a checkout so do what you think is best. Your recommended seems ok"*.
- For each deliverable a non-implementation node lists, the spawn gives that deliverable's branch and the commit at the branch's tip when the spawn is written.
- The worker reads that deliverable's files at that commit through git, without checking it out. The commit stays fixed for the whole attempt, so the snapshot the worker reads cannot move when another node lands on the branch.
- The worker reads the effort's record, the map and its contract where it reads them today.
- A prototype that needs to build on the code copies the files it needs from that commit into its own artifact directory.
- When a worker writes an acceptance condition for a node that will name a deliverable, it runs the scoping search over that deliverable's code at the commit the spawn gave. Where the spawn gave none, it runs the search at the branch's tip (assumption). That is the tree the checker later searches, since the implementation worktree is cut from that branch.
- No worktree is made for this reading (delegated). The human had considered a worktree per deliverable.
- Triage checks an open node that lists deliverables against each listed deliverable's branch tip, read the same way (assumption).

**Cleanup of a node that lists several deliverables (Q3).** The human said: *"Q3 ok"*, accepting the recommendation. A node enters a merged deliverable's region only when every deliverable it lists has merged. Until then the node stays. The merged deliverable keeps its entry and its local branch, as `### A merged deliverable as the region` already provides for "a deliverable that a remaining node still names".

This narrows assumption 02.2 of [node 02](02-several-deliverables-in-one-effort.md) and extends what [node 05](05-ship-deliverables.md) shipped. The shipped files change through the implementation node this node mints.

## Flags

`06.1` `ASSUMPTION` **· settled** — Zero deliverables means the field is absent. The human asked for a field allowing "1, 0 or mutliple". The node-file conventions already say every optional field appears only when it has a value, so I wrote no empty form.

`06.2` `ASSUMPTION` **· settled** — A node belongs to every deliverable it lists. This applies to the shipped rule "A node may be blocked on a node of its own deliverable, or on a node of its deliverable's base." That rule was written for one deliverable per node. Reading "its own deliverable" as "any deliverable it lists" is the plain extension, and it keeps a node from being blocked on a deliverable it does not serve.

`06.3` `ASSUMPTION` **· settled** — Whoever creates a node sets its `Deliverable:` field, and a worker reporting a node gives the value in its `NEW NODES` block. The human's answer added the field without saying who fills it in. I followed how every other header field of a new node is set.

`06.4` `ASSUMPTION` **· settled** — A worker writing a condition for a node that will name a deliverable runs the scoping search at the commit the spawn gave for that deliverable, or at the branch's tip where the spawn gave none. The contracts say "Run the command over the working tree". For deliverable work, that tree lacks the code the checker later searches in a worktree cut from the deliverable's branch. The branch-tip fallback covers a worker minting a node for a deliverable its spawn did not name.

`06.5` `ASSUMPTION` **· settled** — Triage checks an open node that lists deliverables against each listed deliverable's branch tip. `expedition-triage` checks nodes "against the current working tree". That tree lacks deliverable code, so a node already done on its deliverable's branch would look still needed there. I applied this node's principle to triage, the manager's own check.

`06.6` `DELEGATED` **· settled** — The human said of Q2 "do what you think is best. Your recommended seems ok", after saying a worktree per deliverable "might be good". I kept the route without a worktree: the spawn gives a fixed commit and the worker reads through git. A worktree per deliverable would need creating and removing (in this repository the removal runs with the sandbox off). The manager counts code slots by live worktrees, so it would also miscount such a worktree as a code slot. Reading at a fixed commit gives the same consistent snapshot with nothing to clean up.

## Interview

### Attempt 1 — agent `a80e502000489e69c`

**Relayed question, payload 1, as the worker wrote it:**

NODE:          Which checkout a non-implementation worker reads in an effort with deliverables
ABOUT:         Under deliverables, a deliverable's code never reaches the main checkout until its pull request merges upstream. Grilling, precondition and prototype workers read the main checkout, so they cannot see the code their node is about. This node decides how such a worker gets that code. It is decided now because node 05 is shipping deliverables with the sentence "every other worker reads the main checkout" left unchanged.
SO FAR:        I read the node, the map, node 02's line in decisions.md and parts of node 02's answer, and node 05's uncommitted text in its worktree, which I only read. That text is `## Deliverables` in `SKILL.md`, the deliverable entry and the `Deliverable:` field in `graph-conventions.md`, and `### A merged deliverable as the region` in `expedition-cleanup`. The facts both questions rest on:
               - `SKILL.md` `### ... frontier` (node 05's text) still says: "an implementation worker reads its own working tree, and every other worker reads the main checkout. So no worker reads a file while it is being changed."
               - Node 05's text says "The main checkout never receives the node's code." A deliverable's branch has no worktree of its own. Approval moves the branch forward by fast-forward, so the branch tip moves while other nodes are being worked.
               - Only implementation nodes carry `Deliverable:`, and it takes one value. Node 02 recorded this as assumption 02.2: "only they produce commits, and a grilling node may serve several deliverables."
               - The manager counts code slots by live worktrees (glossary). Any extra worktree would be counted as a code slot.
               - Every contract tells a worker that writes an acceptance condition to run its scoping search "over the working tree". For a node that will name a deliverable, a search run over the main checkout misses that deliverable's code. The checker later runs the same command in a worktree cut from the deliverable's branch, so the two results would differ.
               - The record, the map and the contracts live on the main checkout, so a worker must keep reading those there.
               Settled on my own authority: the snapshot a worker reads is fixed for the whole attempt, which keeps the "consistent snapshot" rule true. When a deliverable is based on another deliverable, reading the dependent's commit is enough, because that commit contains the base's work.

Q1. Who says which deliverables a non-implementation worker reads
CONTEXT:       A non-implementation node does not record which deliverable it serves, and assumption 02.2 says it may serve several.
ASK:           How is it decided which deliverables' code a grilling, precondition or prototype worker reads?
RECOMMENDED:   The manager names them in the spawn, as a judgement made from the node's question and from the nodes it blocks. A spawn may name no deliverable, one, or several, and adds no field. This keeps assumption 02.2 as it is. It also fits a grilling node that exists before any implementation node it will produce. The manager already writes spawn notes from context it holds.
ALTERNATIVES:  Let every kind of node carry `Deliverable:`. This contradicts 02.2, allows only one value, and makes the node part of that deliverable's cleanup region and subject to its blocking rule.
               Derive the deliverables from the implementation nodes the node blocks. This fails for a fresh grilling node, which blocks nothing yet.

---

Q2. How the worker reads a deliverable's code without a worktree
ASK:           How does a worker read a deliverable's code, given that the deliverable's branch has no worktree and its code is not in the main checkout?
RECOMMENDED:   For each deliverable it names, the spawn gives the branch and the commit at the branch's tip at spawn time. The worker reads the code at that commit through git, without checking it out, for example by showing a file or searching at that commit. It reads the record, the map and its contract from the main checkout as before. When the worker writes an acceptance condition for a node that will name a deliverable, it runs the scoping search at that deliverable's commit. A prototype that needs to build on the code copies the files it needs from that commit into its own artifact directory. The fixed commit keeps the snapshot from moving mid-attempt. Nothing new has to be created or cleaned up.
ALTERNATIVES:  The manager adds a detached worktree at the deliverable's tip for the attempt. It costs a creation and a removal per attempt (in this repository the removal needs the sandbox off), and the manager's slot counting would read it as a code slot.
               The spawn names only the branch. The branch moves when a sibling node lands, so one attempt could read two different snapshots.
               Leave it as it is. A worker on deliverable work cannot see the code it is deciding about, and its condition searches cover the wrong tree.

**The human's answer to payload 1, `verbatim`:**

> Q1 maybe add a Deliverable field with a list in it for relevent deliverable, so we can do 1, 0 or mutliple .Q2 I feel like a worktree for each deliverable might be good for this but I don't know, it seems that for llms it is quite easy to look at files on a branch without a checkout so do what you think is best. Your recommended seems ok

`DIVERGENCE` on Q1: the worker recommended *"The manager names them in the spawn, as a judgement made from the node's question and from the nodes it blocks. A spawn may name no deliverable, one, or several, and adds no field."* The human proposes a `Deliverable` field holding a list, so a node can name none, one or several.

Q2 takes the worker's `RECOMMENDED`: *"For each deliverable it names, the spawn gives the branch and the commit at the branch's tip at spawn time."*

**Relayed question, payload 2, as the worker wrote it:**

NODE:          Which checkout a non-implementation worker reads in an effort with deliverables
ABOUT:         This node decides how a grilling, precondition or prototype worker sees a deliverable's code, which never reaches the main checkout before its pull request merges. Your answer to Q1 introduces one new case that needs your call before I can hand the node back.
SO FAR:        Settled by your reply:
               - Q1, in your words: "maybe add a Deliverable field with a list in it for relevent deliverable, so we can do 1, 0 or mutliple". So a grilling, precondition or prototype node may carry `Deliverable:` listing zero, one or several deliverables. An implementation node keeps exactly one, because its commit lands on exactly one branch. This narrows node 02's assumption 02.2, which allowed the field on implementation nodes only.
               - Q2, in your words: "do what you think is best. Your recommended seems ok". So for each deliverable in the node's field, the spawn gives the branch and the commit at its tip at spawn time. The worker reads the code at that commit through git, without a checkout, and runs any condition-scoping search there. It reads the record, the map and its contract from the main checkout. A prototype copies the files it needs from that commit into its own artifact directory. You considered a worktree per deliverable, so I will record a DELEGATED flag noting that I kept the no-worktree route. Two reasons: no creation or removal per attempt, and no miscount of code slots, which the manager counts by live worktrees.
               Settled on my own authority, to be flagged as assumptions:
               - Zero deliverables means the field is absent, as every optional field is.
               - A node counts as belonging to every deliverable it lists. This matters for the blocking rule in node 05's text: "A node may be blocked on a node of its own deliverable, or on a node of its deliverable's base."
               - The manager sets the field when it creates a node. A worker reporting a node proposes the field's value in that node's `NEW NODES` block.
               Node 05 has passed its check with "exactly one name, and only implementation nodes carry the field". So this change lands as a later implementation node, which I will report.

Q3. Cleaning up a node that lists several deliverables
CONTEXT:       Node 05's cleanup rule takes into a merged deliverable's region "every node whose `Deliverable:` field names that deliverable". A grilling node listing A and B would then be removed when A merges, while B, which it still serves, is in progress. Cleanup removes record, which is hard to undo.
ASK:           When one of several deliverables a node lists has merged, what happens to that node at cleanup?
RECOMMENDED:   The node enters a merged deliverable's region only when every deliverable it lists has merged. Until then it stays, and the merged deliverable keeps its entry and its local branch, as node 05's text already does for "a deliverable that a remaining node still names". This needs no new step. Nothing about B's work is removed early.
ALTERNATIVES:  Remove the node at A's merge, like a single-deliverable node. B loses decisions it may still rest on.
               At A's merge, drop A from the node's list and keep the node. This adds an edit to resolved node files to the cleanup steps.

**The human's answer to payload 2, `verbatim`:**

> Q3 ok

Q3 takes the worker's `RECOMMENDED`: *"The node enters a merged deliverable's region only when every deliverable it lists has merged."*

## Annotation: node 08 adds the local merge

As the worker of [node 08](08-a-deliverable-that-lands-by-merging-locally.md) reported it: Node 06: an extension. Its question's premise that a deliverable's code reaches the main checkout only when its pull request merges upstream now also includes the local merge. Its answer is unchanged, and its several-deliverables cleanup rule applies to both routes.
