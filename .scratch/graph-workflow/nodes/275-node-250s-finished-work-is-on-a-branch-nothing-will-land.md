# Node 250's finished work is committed to a branch that nothing will land

Type: grilling
Status: resolved

Blocked by: none

## Answer

Nothing from node 250's branch lands and the branch is deleted, the remote copy by the human; a superseded implementation node's leftover worktree and branch are cleaned up like a reject's, shipped via node 89.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. Its clean-up clauses are filed on [node 89](89-carry-worktree-lifecycle-into-managers-contract.md) as an amendment. The local branch is deleted by the manager; the copy on `origin` is the human's to delete. Flags 275.1 and 275.2 settle at the node closing report.

## Question

*Surfaced by [node 264](264-no-status-for-a-node-whose-work-no-longer-needs-a-node.md)'s worker, and pasted as it
wrote it.*

> Node 250's work is finished, passed its checker and is committed to `worktree-250-worker-reaches-its-worktree`,
> which is not on `master`. Node 265 replaced the route that work documents and node 268 is writing the replacement
> text now, so nothing will ever merge that branch. The node itself is superseded under node 264. What happens to
> the branch and its worktree — deleted outright, or read by node 268's worker first for anything worth carrying
> across?
>
> **It also sets a precedent the record has no slot for.** `SKILL.md`'s reject taxonomy sends a rejected node to
> exactly one of three places — beyond the destination, asked the wrong question, or something upstream is wrong —
> and node 250 is none of the three. **The work was right when it was written and the world changed under it before
> it landed.** What this decides is what happens the next time that occurs, which on a long-running effort it will.

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**One half of the question has been overtaken since it was written, and the manager is saying so rather than letting
a worker discover it.** Node 268's worker has **finished**. It did not read node 250's branch — its spawn told it to
work from `master` and ignore that branch entirely, which was the manager's instruction and is the reason the
*"read it first for anything worth carrying across"* option was never taken. So that option is now *re-read it
retrospectively and carry anything missed into a follow-up*, which is a different and more expensive thing than the
question assumes.

**What the branch actually holds**, so nobody has to go and look to decide: commit `bd93fb8`, a single file
`map-manager-only.md`, 45 insertions and 0 deletions, adding a section `How the worker reaches it` stating the
worker's half of the `EnterWorktree` route. **Two blind checkers passed its bar and failed it on its acceptance
condition**, the condition having been measured false in three of its six clauses; the manager later amended those
clauses under node 252's rule, so the text and its condition now agree. **None of that changes that the route it
documents no longer exists.**

**The part the manager thinks outlasts the branch** is not the text but two measurements inside it, which are cited
as evidence in node 265's resolved answer and survive whatever happens here: that permission to write a worktree
precedes the `EnterWorktree` call, and that a worker's writable region holds every live worktree rather than its
own. **Those are safe in node 265 and in node 250's own file under never-delete.** What is at risk is only the
branch.

**The precedent half is the larger question and the manager holds no position on it.** It has now happened once,
visibly, within a single day. Whether that makes it worth a rule or is the sort of thing a long effort simply eats
is exactly what this node decides.

## Interview

### Attempt 1

#### Questions 1 to 3, relayed 2026-09-27

*The worker's payload, pasted as handed back.*

```
NODE:          Node 250's finished work is committed to a branch that nothing will land (node 275)
ABOUT:         Node 250 was finished, checked and committed to `worktree-250-worker-reaches-its-worktree`, but it has since been superseded because the route it documents no longer exists. This node decides three things: whether anything on that branch should still land, what happens to the branch, and whether the next "work was right, the world changed before it landed" case needs a rule.
SO FAR:        I read the node, map.md, the decisions.md lines for 250/264/265/268, node 264's answer, node 250's file (searched), the shipped SKILL.md and graph-conventions.md, and the git state.
               - **What is on the branch.** One commit, `bd93fb8`, dated 2026-09-19. It adds 45 lines to `map-manager-only.md` under the heading "How the worker reaches it", covering the worker's side of the `EnterWorktree` route. Node 265 replaced that route with plain `git worktree add` under `.scratch/graph-workflow/worktrees/`, and node 268 has already written the new route into the map from `master`.
               - **The worktree is already gone.** `git worktree list` shows only the main tree and 348's worktree.
               - **What is left is two refs.** One is the local branch. The other is **`origin/worktree-250-worker-reaches-its-worktree` on the remote**: its reflog says "update by push", and the branch config has a `vscode-merge-base` entry, so it looks like you pushed it from VS Code. The landing policy says the manager never pushes, so deleting the remote copy is your action, not the manager's.
               - **The two measurements in it are already safe.** They are "permission to write the worktree comes before the `EnterWorktree` call" and "a worker's writable region holds every live worktree, not just its own". Node 250's own file (lines ~164, 277-288, 426-463) and node 265's answer both hold them, and both are protected by never-delete. So deleting the branch loses nothing the record doesn't already have.
               - **The precedent half is mostly answered already.** Node 264's rule is now shipped. `graph-conventions.md` `### Supersede` reads: "Use this when another node replaces the node, or when another node's answer or landed work means the node no longer needs doing". So "the world changed under it" already has a place: `superseded`. It is not a fourth reject destination.
               - **What still has no rule is the leftover worktree and branch.** For a reject, `SKILL.md` says "reject: edit the graph first, and clean the working state after". For a superseded implementation node that holds unlanded work, nothing says what happens to its worktree and branch.

Q1. Is anything on the branch still worth landing
CONTEXT:       Your note named this as the sharpest question: whether the branch holds anything worth landing, or only raises the question of what to do with the branch.
ASK:           Should any of node 250's text, or a fact in it, be carried onto `master` by a new node, or should nothing from it land?
RECOMMENDED:   Land nothing. Almost every bullet describes the `EnterWorktree` call, which node 265 removed. Only one point still holds under the plain-git route, and it holds more obviously now: nothing stops one implementation worker writing into the other slot's worktree, and the only thing keeping them apart is the spawn naming one tree. It changes nothing the manager does, though. The manager already picks nodes whose paths don't overlap (map-manager-only.md, the code-slot paragraph). Adding a second reason to the same practice is machinery the "short, simple" preference argues against. I would record the point in this node's answer and stop there.
ALTERNATIVES:  A small implementation node adds "write isolation" as a second reason for the disjoint-paths practice in map-manager-only.md's code-slot paragraph, written from master.
               Have a worker reread the whole branch against master and carry over anything node 268 missed. This costs more, and node 268 has already landed the replacement text.

---

Q2. What happens to the branch
ASK:           Should the branch be deleted, both locally and on `origin`, and if so, who deletes the remote copy?
RECOMMENDED:   Delete both. The manager runs `git branch -D worktree-250-worker-reaches-its-worktree` locally. You run `git push origin --delete worktree-250-worker-reaches-its-worktree` yourself, because the manager never pushes. This rests on the facts in SO FAR: the record already holds the text and the measurements, never-delete covers the record and not git refs, and the worktree is already gone.
ALTERNATIVES:  Keep the branch, or a tag at `bd93fb8`, as an archive. That leaves a stray ref pointing at a route that no longer exists.
               Delete only the local branch and leave the remote copy as it is.

---

Q3. A rule for the next time a superseded node holds unlanded work
CONTEXT:       As shown in SO FAR, the status side of the precedent is already shipped. What remains is cleaning up the leftover working state.
ASK:           Should a superseded implementation node's worktree and branch be cleaned up the same way as a rejected node's, and should that rule go only in this effort's map or in the shipped files?
RECOMMENDED:   Yes, and ship it. Extend the one line in `SKILL.md` under `### Three outcomes, and no fourth` so the same order applies to supersession: edit the graph first, then remove the node's worktree and branch. The case is not specific to this effort. Any long effort whose work sits at a gate while the ground shifts will hit it, and the reject line already states exactly this order. The change is one clause in one shipped file, done as an implementation node. The map's rules only let a rule reach a shipped file when you say so, which is why I'm asking.
ALTERNATIVES:  The same one clause, but only in this effort's landing policy (map-manager-only.md). The next effort starts without it.
               No rule. The manager handles each case as it comes, as happened here. It has happened once, and the cost this time was one stray branch.
```

#### The human's answer to questions 1 to 3, 2026-09-27

The human, `verbatim`: *"ok for recommanded, it was kept because at the time we didn't know if it would be useful later"*. It takes the worker's recommendation on all three: Q1 "Land nothing."; Q2 "Delete both. The manager runs `git branch -D worktree-250-worker-reaches-its-worktree` locally. You run `git push origin --delete worktree-250-worker-reaches-its-worktree` yourself, because the manager never pushes."; Q3 "Yes, and ship it. Extend the one line in `SKILL.md` under `### Three outcomes, and no fourth` so the same order applies to supersession: edit the graph first, then remove the node's worktree and branch."

## Handover, attempt 1

*Pasted as the worker handed it back.*

```
HANDOVER:      Node 250's finished work is committed to a branch that nothing will land (node 275)

ANSWER:
**Nothing from node 250's branch lands. The branch is deleted, locally and on `origin`. A superseded implementation node's leftover working state gets the same clean-up as a rejected node's, and that rule is shipped.** The human's words, `verbatim`: *"ok for recommanded, it was kept because at the time we didn't know if it would be useful later"*. This is a bare assent, and it settles all three recommendations in the payload. It is not a divergence. The second half of the reply gives the reason the branch was kept: at the time, nobody knew whether it would be needed later. Now that is known, and the answer is no.

**What the branch held, and why none of it lands.** It holds one commit, `bd93fb8` (2026-09-19): 45 lines added to `map-manager-only.md` under the heading "How the worker reaches it", describing the worker's side of the `EnterWorktree` route. [Node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md) replaced that route with plain `git worktree add`, and [node 268](268-carry-the-plain-git-worktree-route-into-the-map.md) wrote the new route into the map from `master`. Almost every bullet in the commit describes a call that no longer exists. One point still holds, and it holds more obviously under the plain-git route: nothing stops one implementation worker from writing into the other slot's worktree, and the spawn naming one tree is the only separation. It changes nothing the manager does, because the manager already picks nodes whose paths don't overlap. So it is recorded here and lands nowhere. The two measurements the commit carried stay in node 250's own file and in node 265's answer, both under never-delete. Those measurements are that write permission comes before the `EnterWorktree` call, and that a worker's writable region holds every live worktree.

**The branch.** The worktree was already gone: `git worktree list` showed only the main tree and node 348's worktree. Two refs remain.
- The **local branch** `worktree-250-worker-reaches-its-worktree`. The manager deletes it with `git branch -D worktree-250-worker-reaches-its-worktree`.
- **`origin/worktree-250-worker-reaches-its-worktree`**. Its reflog reads "update by push" and the branch config carries a `vscode-merge-base` entry, so it was pushed from outside the workflow. The landing policy never lets the manager push, so the human deletes it: `git push origin --delete worktree-250-worker-reaches-its-worktree`.

Never-delete covers the effort's record and not git refs, and the record already holds everything the commit said. Deleting the branch loses nothing.

**The precedent.** The question said the record had no slot for "the work was right when it was written and the world changed under it before it landed". Most of that slot now exists. [Node 264](264-no-status-for-a-node-whose-work-no-longer-needs-a-node.md)'s rule has shipped: `graph-conventions.md` `### Supersede` reads *"Use this when another node replaces the node, or when another node's answer or landed work means the node no longer needs doing"*. So such a node is `superseded`, and not a fourth reject destination. What was missing was only what happens to its unlanded working state. For a reject, `SKILL.md` already says *"reject: edit the graph first, and clean the working state after"*. For a superseded implementation node holding unlanded work, the same order now applies, **and the rule is shipped rather than kept in this effort's map**: edit the graph first, then remove the node's worktree and branch. The case is not specific to this effort. Any long effort whose work waits at a gate while the ground shifts will meet it. The change goes into the shipped manager contract through [node 89](89-carry-worktree-lifecycle-into-managers-contract.md). That node already covers what happens to a worker's tree on each gate outcome in the same file, so the rule joins it rather than becoming a new node.

INDEX LINE:    Nothing from node 250's branch lands and the branch is deleted, the remote copy by the human; a superseded implementation node's leftover worktree and branch are cleaned up like a reject's, shipped via node 89.

FLAGS:
ASSUMPTION — Joined the clean-up rule to node 89 instead of reporting a new node. The contract says a defect in the same file and on the same concern as an open implementation node joins that node. Node 89 is open and unclaimed, and its condition already requires `.claude/skills/expedition/SKILL.md` to state what happens to a worker's tree on each gate outcome, with no other file under `.claude/skills/` changed. Supersession is not a gate outcome, so the added clause describes a fourth situation rather than a fourth outcome, and it does not strain `### Three outcomes, and no fourth`. The cost: node 89's condition is still incomplete (it waits on whether the workflow ships the worktree mechanism or only permits it), so the rule ships no sooner than node 89 does. If the manager wants it sooner, the clauses below can be filed on their own as a new implementation node, unchanged.
  Index: The clean-up rule for a superseded node's worktree and branch was joined to open node 89 rather than filed as a new node, so it ships only when node 89 does.
ASSUMPTION — Assigned deletion of the remote copy to the human. The landing policy ([node 11](11-git-and-code-landing.md): "no branches, no push") never lets the manager push, and deleting a remote branch is a push. The reflog also shows the copy was pushed from outside the workflow.
  Index: The remote copy of node 250's branch is the human's to delete, because deleting it is a push and the manager never pushes.

NEW NODES:
Joins open node 89, "Carry the worktree lifecycle into the manager's contract" (implementation, open, unclaimed). Clauses to add to its acceptance condition:
> - `.claude/skills/expedition/SKILL.md` also states what happens to the working state of an implementation node that is superseded while its work is not landed. The graph is edited first, and after that the node's tree, and anything else that holds its unlanded work, is removed, in the same order the file gives for a reject. The file states this as properties rather than as commands of any one version-control tool, and names no command that a repository without that tool could not run.
> - The line in `.claude/skills/expedition/SKILL.md` that reads "reject: edit the graph first, and clean the working state after." still states the reject outcome with the same order: the graph first, the working state after.
> - Scope came from no search: the file named is the place of the work, not an instance of a defect.

INVALIDATIONS:
Node 264: an extension. Its answer says *"What is not settled here is the branch, which is reported as a node."* This node settles the branch: it is deleted and nothing from it lands. It also adds the clean-up rule for a superseded node's working state, which node 264's widened `superseded` did not state. Nothing node 264 says is contradicted.
Node 250: none. Its text stands, and nothing in it becomes false because the branch is deleted.

CONDITIONS:
Searched the `## Acceptance condition` sections of every open or claimed node (73 files) for `working state`, `three outcomes`, `reject:`, `no fourth`, `clean the` and `worktree-250`. Nothing matched. Searched the same sections for the path `expedition/SKILL.md`. Two matched: node 89 (the defect above joins it) and node 350 (the open-question search paragraph, which this work does not touch). No replacement clauses.

MISSING FROM MAP: The map does not say that a node's branch can also exist on `origin`, or who removes a remote ref. I found the remote copy in `git branch -a` and its reflog, and the manager's no-push rule in decisions.md (node 11). The landing policy's *Remove* bullet covers only the local worktree and branch.

RETROSPECTIVE
1. What I had to hunt for: whether node 264's widened `superseded` rule had actually shipped (it had, in `graph-conventions.md` `### Supersede`), which reduced the precedent half to leftover clean-up. Also whether node 250's measurements survive outside the branch; searching node 250's file confirmed they do. And the fact that the branch exists on `origin`, which neither the node nor the spawn mentioned.
2. What arrived that this node did not need: nothing significant. Most of map.md's standing preferences had no bearing on this node.
3. What would have made this easier: the node's filing note saying that node 264's rule had already shipped the status side of the precedent, and the spawn mentioning the remote copy. Either would have saved one search round.
4. What was stale, wrong or contradictory: the node's `## Question` presents the precedent as having "no slot". That was already out of date when I was spawned, since node 264's shipped trigger covers it. Node 89's condition is still incomplete and waits on a question ("ships or merely permits the worktree mechanism") that the landed plain-git route in `map-manager-only.md` may effectively have answered for this effort. The manager may want to revisit it before the joined clauses can ship.
```

## Flags

`275.1` `ASSUMPTION` **· settled** — Joined the clean-up rule to node 89 instead of reporting a new node. *(The worker's full text is under its handover's `FLAGS`.)*

`275.2` `ASSUMPTION` **· settled** — Assigned deletion of the remote copy to the human. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-27:* flags 275.1 and 275.2 settle at the node closing report that closes this node.
