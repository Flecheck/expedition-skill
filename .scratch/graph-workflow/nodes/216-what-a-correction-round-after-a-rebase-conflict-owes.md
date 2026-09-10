# What a correction round after a rebase conflict owes — a re-check, a second gate, or neither

Type: grilling
Status: claimed

Blocked by: none

## Question

*Minted by the manager, from a gap it hit while landing [node
200](200-collapse-the-rules-files-two-map-history-statements.md) and could not answer from the record.*

The landing policy says what happens when a rebase conflicts: *"A rebase conflict is resolved by nobody in the
moment: the manager runs `git rebase --abort` and the node takes a correction round with the worker respawned. A
post-rebase bar failure likewise takes a correction round, and the work does not land."*

**It does not say where the correction round returns to.** Three routes are open and the policy names none:

1. **Back to the checker, then to a second gate.** Safest, and it spends the human's attention twice on one
   approval.
2. **Back to the checker, then straight to landing** on the approval already given, the human's word being about
   the content and the content being unchanged.
3. **Neither** — the manager re-runs the bar on the re-applied work, verifies it is content-identical to what was
   approved, and lands it.

**The case that raised it.** Node 200 was approved, its second check passed, and the rebase conflicted only because
the manager had appended to the same file the node held an append to. The correction round re-applies the same two
hunks at a different offset in one file. **Nothing about the content changes**, so route 1 asks the human to
approve the same bytes twice, while route 3 lands work no checker has seen in its final position.

**What makes it more than bookkeeping**: a conflict that is *not* content-identical is possible — a rebase onto a
base that moved the passage under the work — and the answer may differ between the two cases. The policy's silence
means the manager decides, and the manager deciding how much of the human's own gate to re-spend is the wrong party.

## Acceptance condition

**None, and none is owed.** This is a grilling node: what done means is the human's answer.

## The manager's note at filing

*Not a change to anything above.*

**What the manager did in the meantime, so the record shows it was a call and not a rule.** On node 200 it took
**route 3** for a re-application it can verify is content-identical, and it will say so at the landing rather than
raise a second gate. That is the manager's judgement filling a silence, and this node exists so it stops being the
manager's.

**A second thing the manager invented and should not have.** It queued another node's banked questions *behind*
this landing, as though a landing occupied the human's attention. **No rule says that** — the contract's rule is one
**question** at a time, and a landing is not a question. The human corrected it, `verbatim`: *"Don't wait for 200
relanding ? Why are you waiting to give questions ? Is there a rule that is not correct ?"* Nothing in this node
turns on that; it is recorded because the same habit will otherwise idle the one channel the human has.
