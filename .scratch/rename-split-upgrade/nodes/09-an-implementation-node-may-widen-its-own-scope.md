# May an implementation node's worker or checker widen the node's scope, with a reason

Type: grilling
Status: resolved

## Question

*Written by the manager.* This lets an implementation node fix what its own work makes wrong, so that it does not land leaving files stale. Today a node's acceptance condition lists the files it may change, and a place found outside that list is reported and not edited. Node 05 landed four shipped files stale that way. The human said, at node 05's gate, `verbatim`: *"right now the rules seems to somewhat prevent having a implementation node scope increase when the checker or the worker finds issues. I feel like the work itself should be more important than having an explicit list of files to change. Maybe the worker/checker can increase the scope by giving a reason if it finds something when implementing the node ?"* Should a worker or a checker be able to widen an implementation node's scope while the node is worked, and if so, on what grounds, who decides, and how is the widening recorded and checked?

## Answer

**An implementation node's worker may edit places outside its condition's list of files, on its own authority, on three grounds, recording each with a flag.** The checker cannot edit anything. It widens a node's scope by reporting a finding, and the worker carries out the edit.

The human's words, `verbatim`:
- On payload 1: *"for (a) grounds, it works for this which is a skill but for code I feel like there is more. otherwise seems ok"*
- On payload 2: *"seems ok. For the enabling change, if too big, I would prefer to pause the current node, create a node for the enabling change, do it and then continue the node. For a preexisting defect, fixing it in another node is good (we might want grilling is the defect is complex for example). One other change I am thinking of that I don't know if already accounted for is if you need to change the signature of a function/struct you will then need to update all callers for example."*

### The three grounds

Each ground adds places, never a requirement. A widened edit writes nothing that a resolved node, the shipped files, the condition or the work's own change has not already fixed. A repair that needs a judgement nobody has made is still a raise. The grounds hold for every repository, whether its product is code or skill files.

1. **A place the node's own change makes wrong.** Examples are a stale count, a pointer to something the work moved, and a statement the work now contradicts. In code, this includes every caller of a function or type whose signature the work changed, along with tests, documentation and configuration that describe what changed. This ground has no size limit, because these places are the work's own consequences, and the node must not land leaving them wrong. This answers the human's question about a changed signature: yes, it is covered.
2. **A further instance of the defect the condition already describes.** This is the closed effort's node 82 test (widen to more places, write no new requirement), now used by the worker while it works and not only by the manager before the claim.
3. **An enabling change.** This is a change the work cannot meet its condition or the bar without, in a place the condition did not foresee. Examples are a refactor of a function the feature must extend, a fix to called code that makes the work's own tests fail, a new test file, and a dependency version the feature needs. The test of its reason is: would the work meet its condition or the bar without it?

### Who decides, and how it is recorded

The worker decides, either while working or while fixing a checker finding, with no raise and no wait. For each widened place the worker does two things:
- It hands back one `ASSUMPTION` flag naming the place and the reason, and the ground the reason rests on.
- It lists the place among the paths touched in `GATE PAYLOAD`.

The condition's text is not amended, so it stays its author's words. The flags reach the checker on every run, and reach the human at the gate. The human's approval of the node settles them.

### How the checker treats it

- The checker reports a place the work made wrong as an ordinary finding, whether the place is inside or outside the list. It no longer handles such a place only as a question.
- An edit outside the list passes when a flag names that place and gives a reason on one of the three grounds, and the reason holds.
- An edit outside the list with no such flag, or with a reason that does not hold, stays a `FAIL` on the acceptance condition.

### An enabling change too big to make inside the node

The worker judges whether an enabling change is too big, and puts it to the human by raising under trigger 1, the size of its own node. The raise proposes the enabling node: its name, its question and its acceptance condition. The human may answer by pausing the node, which works as follows:
1. The manager mints the enabling node from the raise and adds it to the paused node's `Blocked by:`.
2. The paused node stays `claimed`. It keeps its worktree, with its work left in place, and its worker waits.
3. While the node is blocked, its worktree does not count against the effort's code slots, so the enabling node can start even with one slot.
4. When the enabling node lands, the manager brings the paused worktree onto the commit where it landed, keeping the paused work. A conflict goes to the paused worker, who fixes it in place and runs no git command.
5. The manager then resumes the paused worker with "continue". Where it cannot be resumed, a replacement attempt takes the node under the existing rules.

### What stays a new node

A defect the work comes across that none of the three grounds covers is reported on `NEW NODES`, as a new node of whatever kind fits. It is a grilling node where deciding the fix needs the human, for example when the defect is complex. Where it shares a file and a concern with an open node, it joins that node under the existing related-defect rule.

### What this does not change

- An edit inside a file the condition lists, beyond the condition's literal clauses, stays as it is today: allowed, and flagged. Flags 10.2 and 11.2 are this case.
- The manager's own widening before the claim (`### Changing one after it is written`) is unchanged.

The rule ships through the implementation node reported in `NEW NODES`.

**MISSING FROM MAP, as the worker wrote it:** Whether this effort declares deliverables, and which one, if any, the new shipping node names. `map.md` does not say, and that is in `map-manager-only.md`, which I did not read. I left the node's `Deliverable:` to the manager.

*Manager's note:* this effort declares no deliverables, so node 14 carries no `Deliverable:` field.

## Flags

`09.1` `ASSUMPTION` **· settled** — (callers of a changed signature): The human asked whether updating every caller of a function or type whose signature the work changed is covered. I placed it under ground 1, a place the node's own change makes wrong, with no size limit. Those callers are the work's own consequence, and the human's aim is that a node never lands leaving places wrong. Where the signature change is itself an enabling change outside the list, it falls under ground 3, and its callers then fall under ground 1. Where the whole of it is too big, the pause applies.

`09.2` `ASSUMPTION` **· settled** — (who judges "too big"): The human said an enabling change that is "too big" should pause the node, but did not say who judges. I gave the judgement to the worker, exercised by raising under trigger 1 (the size of its own node). The human therefore decides every pause at the raise. I also had the raise propose the enabling node's name, question and acceptance condition. The worker is waiting, not handing over, and the rule that the agent which mints a node writes its condition still has to be met.

`09.3` `ASSUMPTION` **· settled** — (how a pause works): The human said "pause the current node, create a node for the enabling change, do it and then continue the node". I settled the mechanics as follows. The paused node stays claimed, with its worktree and worker, and the enabling node is added to its `Blocked by:`. After the enabling node lands, the manager brings the paused worktree onto the landed commit, keeping the paused work. A conflict goes to the paused worker to fix in place, and the worker is then resumed with "continue". A paused worker that cannot be resumed is replaced under the existing rules. The node keeps its claim, so the work is not lost.

`09.4` `ASSUMPTION` **· settled** — (a paused node frees its code slot): The glossary counts one code slot per live worktree. A paused node keeps its worktree, so with one slot the enabling node could never start. I made a paused node's worktree not count against the code slots while the node is blocked.

`09.5` `ASSUMPTION` **· settled** — (grounds hold for every repository): The human raised ground 3 for code ("for code I feel like there is more"). I made all three grounds hold for every repository. An enabling change can occur in a skill repository too, and one rule is shorter than a rule per kind of repository.

`09.6` `ASSUMPTION` **· settled** — (edits inside a listed file are unchanged): Flags 10.2 and 11.2 record edits beyond the literal clauses but inside files the condition lists. This answer concerns places outside the list, so I left that case as it is today: allowed, and flagged.

## Interview

### Attempt 1 — agent `ad30b74c58949d68d`

**Relayed question, payload 1, as the worker wrote it:**

NODE:          May an implementation node's worker or checker widen the node's scope, with a reason (node 09)
ABOUT:         Decides whether an implementation node's worker may edit files outside its condition's list when the node's own work makes them wrong, and if so on what grounds, who decides, and how the edit is recorded and checked. It comes from your remark at node 05's gate, where the node would have landed four shipped files stale.
SO FAR:        What I read: the node file, the map, node 05's `## Review` and its amendment 1, the scope rules in `## Acceptance conditions` / `### Changing one after it is written` of `expedition/SKILL.md`, the scope paragraphs of `## Acceptance condition` in `graph-conventions.md`, and the scope parts of the implementation and checker contracts. I also read the closed effort's nodes 82 and 94 as evidence only, for why the rule exists.
               How things work today:
               (1) Each condition lists the files the work may change. Any other place found to need a change is "reported and not edited": the worker has a duty to report it and no permission to edit it.
               (2) The checker fails any edit outside the list. When it sees a stale file outside the list, it can only ask a question. That is what happened at node 05: in runs 1 and 2 it reported adoption.md, wayfinder-divergences.md and expedition-standing-yes as stale and out of scope.
               (3) Nobody may amend the condition of a node a worker already holds except the human. At node 05 that is why it took a correction round plus a manager-written amendment that you then took.
               Why the fence exists (closed-effort nodes 82 and 94): it stops a worker drifting into unrelated work. It also keeps any agent from inventing a new requirement that the blind checker would then judge against. Node 82 already lets the manager widen an unclaimed node's scope with no human turn, on one test: the widening adds places and writes no requirement that was not already fixed.
               Nodes affected: node 07 (claimed) and node 10 (open) both carry today's "reported and not edited" clause.

ASK:           Should the worker of an implementation node be allowed, on its own authority and with a stated reason, to edit places outside its condition's list, under the rule recommended below?

RECOMMENDED:   Yes. The rule has four parts. It reuses node 82's test ("adds places, never a requirement") and moves the decision from the manager before the claim to the worker during the work.
               (a) The grounds. There are exactly two:
                   - A place that this node's own change makes wrong: a stale count, a pointer to something the work moved, or a statement the work now contradicts. This covers all four of node 05's files.
                   - A further instance of the very defect the condition already describes.
                   Both bring a place into line with something already fixed. A different defect that the work merely comes across still becomes a new node through `NEW NODES`. A repair that needs a judgement nobody has made is still a raise.
               (b) Who decides. The worker decides, either while working or while fixing a checker finding, with no raise and no wait. You see every widening at the gate, and your approval settles it.
               (c) How it is recorded. Each widened file gets one flag stating the file and the reason. Flags already reach both the checker and you at the gate, so no new channel is needed. The condition's text is not amended, so it stays its author's words. The file is also listed in `GATE PAYLOAD` with the paths touched.
               (d) How it is checked. The checker reports a place the work made wrong as an ordinary finding, inside or outside the list, rather than as a question. The worker then fixes it by widening. An edit outside the list passes when a flag gives a reason and that reason holds: the work made the place wrong, or it is another instance of the condition's defect. An edit outside the list with no reason, or with a reason that does not hold, stays a FAIL on the acceptance condition.
               Why this design: it fixes what you disliked, stale files that the node itself introduced, without a correction round or a human turn in the middle of the work. It keeps the one thing the fence protects, which is that no agent invents a new demand. The checker is read-only and cannot edit, so a checker "widens" by finding, and the worker carries the widening out. The shipped files would then need a follow-up implementation node to state this rule. Once the rule is settled, I will write that node and its condition, and say what to do about node 10's clause.

ALTERNATIVES:  - Wider grounds: the worker may fix any defect it finds while working, with a reason. This is closest to "the work itself should be more important", but it lets a commit grow into unrelated work that no condition describes.
               - The worker raises each widening and you approve it before the edit. This is safer, but it costs a human turn in the middle of the work every time. That is the friction you named.
               - The manager approves each widening in the middle of the work. This conflicts with the rule that the manager never authors the standard the work is judged against, and it still interrupts the work.
               - A separate flag marker such as `WIDENED` instead of an ordinary `ASSUMPTION` flag. This is clearer at the gate, but it means changes to the glossary and the contracts for a marker that does the same job.
               - Keep today's rule and rely on correction rounds plus amendments, as at node 05. This works, but it costs a human round each time and lands stale files whenever nobody catches them.

**The human's answer to payload 1, `verbatim`:**

> for (a) grounds, it works for this which is a skill but for code I feel like there is more. otherwise seems ok

Parts (b), (c) and (d) take the worker's `RECOMMENDED`. On (a), the human's reply takes the recommended grounds for skill files and says that for code there are more grounds, without naming them.

**Relayed question, payload 2, as the worker wrote it:**

NODE:          May an implementation node's worker or checker widen the node's scope, with a reason (node 09)
ABOUT:         Decides when an implementation node's worker may edit places outside its condition's list. Payload 1 settled who decides, how it is recorded and how it is checked. What is left is the grounds for a repository whose product is code.
SO FAR:        Your reply to payload 1 was "for (a) grounds, it works for this which is a skill but for code I feel like there is more. otherwise seems ok". I read it as settling the following:
               - (b) The worker decides on its own authority, with no raise and no wait, and your gate approval settles each widening.
               - (c) Each widened file gets one flag giving the file and the reason, and is listed in `GATE PAYLOAD`. The condition's text is not amended.
               - (d) The checker reports a place the work made wrong as an ordinary finding, wherever it is. An edit outside the list passes when a flag gives a reason and the reason holds. An edit outside the list with no reason, or with a reason that does not hold, fails the acceptance condition.
               The two grounds already proposed stand for every repository:
               1. A place the node's own change makes wrong.
               2. A further instance of the defect the condition already describes.
               In code, ground 1 already reaches a lot: callers broken by a changed signature, tests that assert the old behaviour, and documentation, configuration or build files that describe what changed. Node 10's flag 10.2 is a nearby case that is not this rule's. That worker edited beyond its clauses, but only inside files its condition lists, and today's rules already allow that with a flag.
               What code adds beyond the two grounds is two kinds of change:
               - An enabling change: a change the work cannot meet its condition or the bar without, made in a file the condition did not foresee. Examples are refactoring a function the feature has to extend, fixing a bug in code the work calls that makes its own tests fail, adding a test file, or raising a dependency's version the feature needs.
               - A defect found in passing: a real bug or smell the worker notices in nearby code that the work does not need fixed.

ASK:           For code, should a third ground be added: an enabling change, meaning a change the work cannot meet its condition or the bar without, with the flag's reason naming what the work needed? And should a defect the worker merely finds in passing stay a new node?

RECOMMENDED:   Yes to both. Add enabling changes as ground 3, and keep a defect found in passing as a new node reported through `NEW NODES`.
               An enabling change is still decided by the work itself. The checker can test its reason by asking whether the work would meet its condition or the bar without the change. That keeps (d)'s check real.
               A defect found in passing has no such test. Allowing it would let any commit grow without limit, and its fix would ship unreviewed inside another node's change. Your own example from the effort's start points the same way. The bug found during benchmarking became its own piece of work, and the deliverables of destination 2 now give such a fix its own branch.
               The limit "the repair writes no requirement nobody has fixed" still holds for all three grounds. An enabling change that needs a design decision, such as choosing a new interface or a new dependency where several would do, is still a raise.

ALTERNATIVES:  - Also allow a defect found in passing when it is small and in a file the work already changes. This is closer to "the work itself matters more than the list", but "small" is a judgement the checker cannot test, so in practice it becomes any fix.
               - Allow any fix the worker can give a reason for. This is the widest option, but it removes the fence that keeps a node's commit about one thing.
               - No third ground. Treat enabling changes as raises, as today. This is safe, but it stops the work in the middle each time a refactor or a test file is needed. That is the friction you named.
               - Let the effort's map declare extra grounds per repository. This is flexible, but it adds a field for a need not yet seen twice.

**The human's answer to payload 2, `verbatim`:**

> seems ok. For the enabling change, if too big, I would prefer to pause the current node, create a node for the enabling change, do it and then continue the node. For a preexisting defect, fixing it in another node is good (we might want grilling is the defect is complex for example). One other change I am thinking of that I don't know if already accounted for is if you need to change the signature of a function/struct you will then need to update all callers for example.

The reply takes the worker's `RECOMMENDED`: *"Yes to both. Add enabling changes as ground 3, and keep a defect found in passing as a new node reported through `NEW NODES`."*, with two additions of the human's: a too-big enabling change pauses the node for a node of its own, and a complex pre-existing defect may take a grilling node. It also asks whether updating callers after a signature change is covered.

## Annotation: node 14 ships this answer with narrowings and extensions

As the worker of [node 14](14-ship-the-rule-for-widening-scope.md) reported it: Node 09 (resolved): no contradiction. Its answer is shipped with these narrowings and extensions: the checker contract's no-new-requirement wording (14.5); the flag index sentence must carry place, reason and ground (14.6); a standing yes on a pause RECOMMENDED reads as a pause (14.2); the enabling node's Deliverable field follows the existing rule (14.4).
