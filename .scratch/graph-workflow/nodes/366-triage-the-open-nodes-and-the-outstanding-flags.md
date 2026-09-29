# Triage the open nodes and the outstanding flags

Type: grilling
Status: claimed
Blocked by: none

## Question

On 2026-09-28 the graph holds 60 open nodes, 13 of the 32 open implementation nodes with no usable acceptance condition, and 252 outstanding flags, none reviewed. Much of the open work fixes this effort's own record, and landed work has made some of it moot (nodes 236 and 186 were closed with no edit). Which open nodes are dropped or superseded, which flags are settled in batches, and in what form, if any, does a triage step belong in the shipped skill?

*Filed by the manager from its own retrospective, 2026-09-28. The human's words on it, `verbatim`: "we can do a triage, I don't know if it should be added to the skill also in some form".*

## Interview

#### Questions 1 to 5, relayed 2026-09-29

*Pasted as the worker handed it back.*

```
NODE:          Triage the open nodes and the outstanding flags (366)
ABOUT:         Decides which of the 60 open nodes to drop or merge, how to settle the 251 outstanding flags in batches, and whether a triage step ships in the skill. It is being decided now because much of the open work is stale and four claims in two days stopped on raises for that reason.
SO FAR:        I checked every open node against the current working tree, not against what the record says. Four read-only helper agents did this, each quoting the current text as evidence. Findings:
               - 10 nodes are moot: later work already fixed the thing they target.
               - About 13 are live but low value. They mostly concern this effort's own record or this machine's sandbox, or the human already marked them low priority.
               - About 30 are live, and I recommend keeping them. The live ones that bear most on the skill working elsewhere are 34, 66, 67, 85, 365, 363, 214, 172 and 317.
               - Six live implementation nodes have conditions that quote moved text: 80, 88, 149, 219, 220 and 284. None is claimed, so the manager may amend their conditions without asking the human first (map rule). I have not asked about them.
               - Node 221's premise is wrong. The ten "lost" retrospectives survive in the worker transcripts under ~/.claude/projects/.../subagents/.
               - Flags: 251 outstanding, 225 of them ASSUMPTION. 192 sit on 61 resolved nodes, 45 on 25 superseded nodes, and 14 on 8 open or claimed nodes. The last group are condition-amendment flags that settle at those nodes' own gates.
               - Under the standing rule, a node's flags settle at its gate or node closing report, on the human's next word. The resolved-node flags are outstanding only because the two "Settle a flag" writes were never made. They are not outstanding because the human never saw them.

Q1. Close the moot nodes
ASK:           May these 10 nodes be closed as superseded by the work that made them unnecessary, with no edit?
RECOMMENDED:   Yes. In each case the tree already shows the fix:
               - 152: node 265 replaced the paragraph it would move.
               - 159: the .gitignore comment already points at the right file (node 249).
               - 237: both passages now name one path (node 265).
               - 254: same clause and same fix as 276, which has the complete condition.
               - 51: node 113 removed every plugin skill name from the contracts.
               - 77: worktrees give every worker a consistent snapshot (SKILL.md, "Picking the next node").
               - 121: no respawn cap exists any more; the rule is now resume wherever possible.
               - 154: the Lang path now exists on this machine.
               - 157: the manager banks work now; a worker never needs to commit.
               - 282: the Edit denial no longer reproduces (about 78 of 79 recent worktree edits succeeded).
ALTERNATIVES:  Name any of these to keep open.
               Re-check each one in its own attempt: this costs a spawn per node for the same answer.

---

Q2. Drop the low-value nodes
CONTEXT:       You said the small improvements may have to stop at some point. These are the smallest.
ASK:           May these 13 nodes be ruled out of scope, each with its reason as its line in the out-of-scope list?
RECOMMENDED:   Yes:
               - 62: moving the AFK passes to the workflow runtime is speculative, with no measured failure behind it.
               - 63: wording of this effort's own out-of-scope line.
               - 83: periodic open-ended review, which you marked low priority.
               - 84: the glossary headword check pays off mostly on this self-hosting effort.
               - 104: one `recovered/` file from node 46, whose use is finished.
               - 125: the checker re-running a baseline would only improve diagnosis.
               - 180: the read-only overlay is now predictable from the sandbox settings.
               - 182: the shadow instrument was never shipped, and node 345 already cut the map.
               - 251: sandbox needs already measured piecemeal by later landings.
               - 232: the shipped graph-conventions.md already states the two never-delete tests in full.
               - 88: the check that produced the false failure no longer exists.
               - 65: frontier.sh now ships as the cheap route to the graph state.
               - 221: old retrospectives, recoverable from the transcripts but of little use now.
ALTERNATIVES:  Name any of these to keep open.
               Keep them all open: they stay in the frontier, and each costs a spawn when picked.

---

Q3. Merge overlapping nodes
ASK:           May these open nodes be merged, so the smaller one's clauses join the larger one's condition and the smaller one is superseded?
RECOMMENDED:   Yes. Each pair edits the same passage for the same concern, which is your standing rule for grouping nodes by file:
               - 271 into 190: same bar paragraph of map-implementation-rules.md; 271's clause 1 is already done.
               - 208 into 214: a condition quoting a refused word is one case of a condition contradicting a standard.
               - 89's remaining clause (cleaning up after a superseded node) into 363: same landing-policy bullet; 89's lifecycle question is already answered as per-effort.
               - 170 and 41 together: both edit the closed list of flag markers.
               Also, node 80 shrinks to its one live clause, the reject-as-forward-revert line in map-manager-only.md.
ALTERNATIVES:  Keep them separate and only sequence them: each file then takes two edits and two checks.

---

Q4. Settle the flags in batches
ASK:           May the 237 outstanding flags on resolved and superseded nodes be marked settled in one batch, leaving the 14 on open or claimed nodes to settle at their own gates?
RECOMMENDED:   Yes. Your standing instruction already settles a node's flags when you approve its end or speak after its node closing report. These nodes all closed before you spoke again, so this batch only makes the writes that were owed. On superseded nodes, the work the flags judged was replaced.
ALTERNATIVES:  Settle only the ASSUMPTION flags now, and first see the 24 non-ASSUMPTION flags as a short list: 19 MANAGER-WRONG, 3 CONDITION-WRONG, 2 SPAWN-WRONG.
               Review them node by node: 86 nodes, many payloads.

---

Q5. Whether triage ships in the skill
ASK:           Should a triage step ship in the skill, and in what form?
RECOMMENDED:   A short skill you invoke, like expedition-cleanup and expedition-standing-yes. It would do what this node did:
               - check each open node against the current tree;
               - propose, in one numbered batch, which nodes are moot, which are dropped and which merge, each with a one-line reason;
               - propose settling the flags whose settling moment has already passed.
               The manager's contract forbids it to drop a node or settle a flag on its own judgement, so an invoked act is where that authority comes from. It pairs with node 365's check before a claim, which is the per-node counterpart.
ALTERNATIVES:  Fold it into node 365's question only: that catches stale nodes one at a time, never the backlog as a whole.
               Make it a third operation of expedition-cleanup: that skill's job is to remove record, while triage changes node statuses.
               Ship nothing and keep it as this effort's practice: the next effort in another repo meets the same backlog with no route.
```
