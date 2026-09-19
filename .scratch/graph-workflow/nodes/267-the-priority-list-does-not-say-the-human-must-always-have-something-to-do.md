# The priority list does not say the human must always have something to do

Type: implementation
Status: open

Blocked by: none

## Question

*The human's own, `verbatim`, on 2026-09-19, given while pointing at the line `Giving a question to the human` in
`.claude/rules/expedition-triggers.md`:*

> give the gate, I shouldn't have to ask you, maybe the priority list should be improved a bit, ex: when waiting,
> always end with what the humain is supposed to do (-> nothing to do when there is a question -> ask a question)
> and maybe add the fact that the human should always have something to do to "Giving a question to the human"

**The failure that produced it, and it is the manager's.** The manager held [node
260](260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md)'s gate assembled, resumed a worker, and **ended
its turn with the human idle and the gate unsent**. It then did the same again on the next turn. Each step obeyed
the priority list as written — a resume outranks a question — and the list says nothing about the state the turn
must end in, so nothing caught it.

**Why the existing text does not already cover it.** The rules file's third bullet says *"if the human has nothing
to do and there is a question/gate, give it to him"*, which is a **trigger** and fires on a moment. The priority
list is an **ordering over acts** and fires every turn. The manager followed the ordering, never re-checked the
trigger, and the two never met. The human's proposal is to close that by making the ordering itself terminate in a
check rather than in an act.

## Acceptance condition

***Written by the manager.*** This node was minted by the manager from the human's direction, and there is no agent
whose condition it would displace. It is the manager's own failure being repaired, which is worth a reader knowing.

Done when all five hold.

**1.** `.claude/skills/expedition/SKILL.md`'s section `## The order you act in` states that the ordering terminates
in a check on the state the turn ends in, not merely in the act `Waiting`: **before the manager stops, the human has
something to do, or there is provably nothing for them to have.** Where they have nothing and anything is waiting,
the waiting thing is sent before the turn ends.

**2.** That same section's item `Giving a question to the human` carries the standing reason the human gave for it,
in whatever words fit the file: **the human should always have something to do.** It is stated as the ground of that
item rather than as a sixth item.

**3.** The statement in clause 1 says what *provably nothing* means, so it cannot be satisfied by inattention: the
queue is empty — no gate assembled, no worker blocked on a raise, no manager's raise, no relayed question — and
every agent in flight is still working. **Waiting is the state after that check, never instead of it.**

**4.** `.claude/rules/expedition-triggers.md`'s `## Priority` list carries the same two additions, in the file's own
terse register, and its `Waiting` item no longer reads as a bare act. Nothing else in that file changes by this
node's hand.

**5.** No other file is changed. Nothing is written in `decisions.md` or `flags.md`. Every markdown link resolves.
The bar applies.

## The manager's note at filing

*Not a change to anything above.*

**The human's parenthesis is the mechanism and the condition keeps it**: *"(-> nothing to do when there is a
question -> ask a question)"*. It is a check with a consequence, not a preference, and the condition's clause 1 is
that sentence turned into a rule.

**This is the second node in a day repairing the same shape of defect** — [node
260](260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md) found that four sentences implying a rule do not
make a prohibition, and this finds that an ordering over acts does not make a duty about the state you stop in.
**Both were caught by the human rather than by the manager**, and in both cases the manager had read the text it was
breaking.

**Sequencing, which is the manager's.** This edits `SKILL.md`'s `## The order you act in`, which [node
255](255-ship-the-priority-list-into-the-managers-contract.md) landed at `4598672`, and the same file's neighbours
are edited by node 258 and by node 260's gated work. **Two workers must not hold `SKILL.md` at once.**
