# Can a deliverable land by merging into the main branch locally, instead of by push and pull request

Type: grilling
Status: resolved
Labels: SPLIT

## Question

*Written by the manager.* This lets a human who works alone on a repository use deliverables without pushing branches or opening pull requests. Node 02 decided that a deliverable lands by a push on the human's yes and a pull request the human opens, and that its cleanup starts when the human says the pull request merged. The human then said, `verbatim`: *"Also I would guess that in this repo, I would not push the branch and make a pull request but direclty merge to master as I am the only one. But I guess most of the time it would be push of the branch and then a pull request"*. Should a deliverable, or an effort, be able to land by merging its branch into the main branch locally, and if so, how is that chosen and what replaces the push, the pull request and the merge report that starts cleanup?

## Answer

A deliverable can land in one of two ways. It can be pushed and become a pull request, as [node 02](02-several-deliverables-in-one-effort.md) designed. Or it can be merged locally into a branch of the repository, with no push and no pull request. The human chose this for a repository they work on alone. The decisions below are the human's answers to Q1, Q2 and Q3. The points marked as assumptions are the worker's, and each is flagged.

**How the landing is chosen (Q1).** The human said, verbatim: *"Q1 ok but if nothing is said, by default push upstream"*. The choice is made per deliverable, and it is written in the deliverable's map entry as a third form of base: `base: local <branch>`, for example `base: local master`. A deliverable with that base lands by being merged into that local branch. It is never pushed, and it has no pull request. The effort's landing policy in `map-manager-only.md` may say which form of base a new deliverable takes by default. Where the policy says nothing, a new deliverable takes the upstream form and lands by push and pull request. The manager does not ask the human. This departs from the recommendation, which had the manager ask.
- A deliverable whose base is another deliverable lands the way that deliverable lands. When that base deliverable has merged locally, the dependent's base becomes the local branch it merged into, and the dependent is rebased onto that branch (assumption).
- A local deliverable's branch is created from the current tip of its local branch, even where the main checkout has that branch checked out. Node 02 forbade cutting from the main checkout only because the main checkout's graph commits would reach a pull request. A local merge brings them back to a branch that already holds them (assumption).
- The local branch may be any local branch. In the human's case it is `master`, which is the branch the main checkout has checked out (assumption).

**The merge needs the human's yes (Q2).** The human said: *"Q2 ok"*, accepting the recommendation. The manager merges a local deliverable only on the human's yes to that merge. It offers the merge when every implementation node naming the deliverable has resolved, and also whenever the human asks. The offer is the manager's own raise, as the push offer is. Every merge needs its own yes. A standing yes whose scope covers a merge counts as the human's yes to it, as it does for a push.

**How it is merged (Q3).** The human said, verbatim: *"Q3 ok, but it could be overridden if the user wants merges or squash commits"*.
- By default the manager rebases the deliverable's branch onto the local branch's current tip, then moves the local branch to the deliverable's tip by fast-forward only. History stays linear, and each node commit keeps its `Node:` trailer.
- A rebase that conflicts becomes an implementation node of the deliverable, and the branch is left as it was before the rebase. This is node 02's rule for a stacked deliverable's rebase.
- The effort's landing policy may name a merge commit or a squash in place of the default, and the human may name either in their yes to one merge (assumption on where the override is stated).
- A squash commit carries the `Node:` trailer of every commit it replaces, because that trailer joins git history to the graph (assumption).

**Cleanup.** The manager does the local merge itself, so it knows the deliverable has merged without being told. Right after the merge, it proposes the region cleanup of that deliverable under `expedition-cleanup`, with that skill's safeguards unchanged (assumption). After the cleanup it deletes the deliverable's local branch. There is no remote branch. Node 06's rule still applies: a node that lists several deliverables enters the region only when every deliverable it lists has merged, by either route.

**Not decided here.** This node does not decide whether this effort's own landing policy names `local master` as its default. The human's words ("in this repo, I would not push the branch… but direclty merge to master") point that way, but they gave no instruction to change the map.

This extends [node 02](02-several-deliverables-in-one-effort.md) and narrows its reason for never cutting a deliverable's branch from the main checkout. It extends what [node 05](05-ship-deliverables.md) shipped and what [node 07](07-ship-expedition-upgrade.md) ships. The shipped files change through the implementation node this node mints.

**MISSING FROM MAP, as the worker wrote it:** The map does not say how this effort's own work lands. I took it from `map-manager-only.md` `## Landing an implementation node's work`, which a search for the human's quoted words led me to. Node 05 had landed (commit `7a86d138e0`) during my attempt, so the scope searches ran over the landed tree, not node 05's worktree. Otherwise none.

## Flags

`08.1` `ASSUMPTION` **· settled** — (stacked on a local deliverable): A deliverable whose base is another deliverable lands the way that deliverable lands. When a local base deliverable merges, the dependent's base becomes `local <branch>`, the branch the base merged into, and the dependent is rebased onto it. This mirrors node 02's rule for a base whose pull request merged upstream. The human was not asked, because nothing else follows from the human's answers.

`08.2` `ASSUMPTION` **· settled** — (cutting a local deliverable's branch from the main checkout's branch): Node 02 created a deliverable's branch "never from the main checkout", because graph commits would reach the pull request. A local deliverable has no pull request, and its merge returns to a branch that already holds those commits. So its branch is cut from its local branch's tip even where the main checkout has that branch checked out. Likewise, node 03's check that a promoted branch holds no commit of the effort's record applies only to a deliverable that lands by pull request. The check that the main checkout does not have the promoted branch checked out still applies to every deliverable.

`08.3` `ASSUMPTION` **· settled** — (where the merge method is overridden): The human said the default rebase and fast-forward "could be overridden if the user wants merges or squash commits", without saying where. I settled that the effort's landing policy may name a merge commit or a squash for the effort, and that the human may name either in their yes to one merge.

`08.4` `ASSUMPTION` **· settled** — (squash keeps every trailer): A squash would lose each node commit's `Node:` trailer, which joins git history to the graph. I settled that a squash commit carries the trailer of every commit it replaces.

`08.5` `ASSUMPTION` **· settled** — (cleanup after a local merge): Node 02 starts cleanup when the human says the pull request merged, because the manager cannot see the host. For a local merge the manager made the merge itself, so it proposes the region cleanup right after the merge, without waiting to be told.

`08.6` `ASSUMPTION` **· settled** — (any local branch): The human's case is `master`, the main checkout's branch. I let `base: local <branch>` name any local branch, because nothing in the mechanism depends on which one it is.

## Interview

### Attempt 1 — agent `a708bf305fbc51c49`

**Relayed question, payload 1, as the worker wrote it:**

NODE:          08 — Can a deliverable land by merging into the main branch locally, instead of by push and pull request
ABOUT:         Node 02's deliverable design only lands a piece of work by push and pull request. You said that in this repo you would rather merge straight into master, since you work alone. This node decides whether a deliverable can land that way, how that is chosen, and what replaces the push, the pull request, and "you tell the manager the PR merged".
SO FAR:        I read the node, the map, node 02's answer, and node 05's uncommitted draft of `## Deliverables` in the shipped `SKILL.md` (read only).
               How deliverables work today (node 02, being shipped by node 05):
               - The map lists each deliverable with its name, its branch, and its base. The base is either `upstream <branch>`, the branch its PR targets, or another deliverable it is stacked on.
               - Each node's worktree is cut from the deliverable's branch. On approval the deliverable branch fast-forwards to the node's commit. The main checkout never gets the code until the PR merges upstream.
               - The branch is cut from its base and never from the main checkout, because master holds the graph commits and they would leak into the PR.
               - The manager offers a push when all of the deliverable's nodes have resolved. Each push needs your yes. You open the PR.
               - When you say the PR merged, the manager proposes a region cleanup of that deliverable and deletes its local branch.
               An effort with no deliverables already lands locally. Each node fast-forwards into master as soon as it is approved. So the only thing a local-merge deliverable adds is grouping: a piece's nodes collect on their own branch, the piece reaches master in one step when it is whole, and that step triggers its cleanup. The leak concern above goes away for a local merge, because the graph commits are already on master. I settled nothing on my own authority yet. Once this question is answered, a second payload will ask whether the merge needs your yes, and whether it is a rebase plus fast-forward or a merge commit.
ASK:           Should a deliverable be able to land by being merged locally into the main checkout's branch, and if so, is that chosen per deliverable or once for the whole effort?
RECOMMENDED:   Yes, chosen per deliverable, written as a third form of the entry's base: `base: local <branch>`, for example `base: local master`. The base already says where a deliverable's code ends up, so this adds no new field, and a stacked deliverable can still sit on a local one. The effort's landing policy in `map-manager-only.md` may say which form a new deliverable takes by default. That way this repo says "local master" once, and a work repo says "upstream main". Where the policy says nothing, the manager asks you when it declares the deliverable. The choice fits your words "in this repo… but most of the time push and PR", and an effort with mixed deliverables still works.
ALTERNATIVES:  - Yes, but once for the whole effort, in its landing policy, with no per-deliverable choice. This is simpler, but one effort can't mix a local piece with a PR piece.
               - No. A solo human just declares no deliverables and lands each node into master directly, as today. This loses the grouping: half a piece reaches master, and there is no per-piece cleanup trigger.
               - Yes, with a separate `lands:` field on the entry beside the base. This states the same thing twice, because the base already names the target branch.

**The human's answer to payload 1, `verbatim`:**

> Q1 ok but if nothing is said, by default push upstream

Q1 takes the worker's `RECOMMENDED`: *"Yes, chosen per deliverable, written as a third form of the entry's base: `base: local <branch>`"*, with a change. `DIVERGENCE` on one part: the worker recommended *"Where the policy says nothing, the manager asks you when it declares the deliverable."* The human's default where nothing is said is push upstream.

**Relayed question, payload 2, as the worker wrote it:**

NODE:          08 — Can a deliverable land by merging into the main branch locally, instead of by push and pull request
ABOUT:         Whether a deliverable can land by a local merge into the main checkout's branch instead of a push and a pull request, and what replaces the push, the PR and the "PR merged" report. This payload settles how that local merge happens.
SO FAR:        Settled by your answer to Q1, verbatim: "Q1 ok but if nothing is said, by default push upstream".
               - A deliverable's map entry may take a third form of base, `base: local <branch>`, for example `base: local master`. A deliverable with that base lands by being merged locally into that branch, and it is never pushed.
               - The effort's landing policy in `map-manager-only.md` may say which form a new deliverable takes by default. Where it says nothing, a new deliverable takes the upstream form and lands by push and pull request, as node 02 designed. The manager does not ask.
               What I will settle on my own authority and flag as assumptions, unless you object:
               - The manager does the local merge itself, so it knows the merge happened. It proposes the deliverable's region cleanup right after the merge, with no "you tell me it merged" step. After the cleanup it deletes the deliverable's branch, and there is no remote branch to leave alone.
               - A deliverable stacked on a local deliverable gets the local branch as its base after the merge, and is rebased onto it, just as a stacked deliverable gets the upstream branch after a PR merges.
               - The branch of a local deliverable may be cut from the main checkout's branch. Node 02 forbade that only because master's graph commits would leak into a PR, and for a local merge they are already on master.
               One fact both questions rest on: the main checkout's branch gains graph commits all the time. So by the time a deliverable is finished, master has moved past the point the deliverable's branch was cut from.

Q2. Does the local merge need your yes
ASK:           When every implementation node of a local deliverable has resolved, does the manager merge it into master only on your yes, or merge it by itself?
RECOMMENDED:   It merges only on your yes, offered at the moment a push would be offered: when every implementation node naming the deliverable has resolved, and whenever you ask for it. A standing yes may cover it, as it covers a push. The merge is the point where the piece reaches master as a whole, and only you know whether the piece is finished. All of its nodes having resolved does not mean you have no more work to add to it. It also keeps both kinds of deliverable the same: one yes at the end, either to the push or to the merge.
ALTERNATIVES:  - Merge by itself as soon as every implementation node has resolved. Each node's code was already approved at its gate, but a piece you meant to grow would land half-finished.
               - Merge only when you ask, with no offer. This saves the interruption, but a finished piece can sit unmerged with nobody noticing.

---

Q3. How the deliverable's branch is merged into master
ASK:           Is the local merge a rebase of the deliverable's branch onto master's current tip followed by a fast-forward, or a merge commit?
RECOMMENDED:   Rebase onto master's tip, then fast-forward master, which keeps history linear. This matches the effort's existing landing policy, which only fast-forwards the main checkout. It also matches node 02's rule that a node's commit is put on a moved branch's new tip before a fast-forward. Each node commit keeps its `Node:` trailer through the rebase. A conflict becomes an implementation node of the deliverable, and the branch is left as it was before the rebase, as node 02 rules for a stacked deliverable's rebase.
ALTERNATIVES:  - A merge commit (`--no-ff`). The deliverable's commits stay exactly as approved, and history shows the piece as one group. History stops being linear, and a conflict has to be resolved inside the merge commit.
               - Squash the deliverable into one commit on master. Each node's `Node:` trailer is lost, and that trailer is what joins git history to the graph.

**The human's answer to payload 2, `verbatim`:**

> Q2 ok Q3 ok, but it could be overridden if the user wants merges or squash commits

Q2 takes the worker's `RECOMMENDED`: *"It merges only on your yes, offered at the moment a push would be offered"*. Q3 takes the worker's `RECOMMENDED`: *"Rebase onto master's tip, then fast-forward master, which keeps history linear."*, with the human's addition that the human may override it with a merge commit or a squash.
