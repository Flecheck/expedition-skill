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

## Interview

### Attempt 1 — the questions put to the human

*Pasted as the worker wrote them, in its own order and its own words. It re-issued the payload after a sweep, and
this is the re-issued version. **No answer has arrived**; the payload is banked here so that a death leaves the
worker's work on disk rather than losing it.*

**ABOUT:** This decides where an implementation node's work goes when something fails *after* you have already
approved it at its gate: back to the checker, back to you for another approval, or neither. It is being decided now
because the landing policy names the failure and not the destination, so the manager has been choosing — and what it
chooses is how much of your own approval gets re-spent.

**SO FAR:** I read the node file, `map.md`, the landing policy (now in `map-manager-only.md`, moved byte-identical
by node 188), `decisions.md`, resolved nodes 11, 20, 68, 71, 108, 115, 143, 176 and 200, open nodes 34, 160, 162 and
209, and the three shipped contracts plus `CONTEXT.md`.

**The record is not silent here. It is doubly-spoken, and five things already bear on it.**

1. **A round returns to whoever raised it.** The shipped lifecycle: a checker `FAIL` sends the work back to the
   checker and you never see it; a `correct` at your gate sends it back to your gate and *not* to the checker.
   Uncapped either way.

2. **Whether the checker re-runs already has a test you chose**, shipped verbatim: *"The bar is re-checked every
   correction round. The acceptance condition is re-checked only where the worker reports that its correction
   touched something the condition names"* — the trigger on the worker "because the worker is the party that knows."

3. **Node 115 already replaced the very sentence my node quotes**, and neither I nor the manager knew it. It splits
   a rebase conflict by *what conflicted*: a conflict in never-delete text (the map, node files) the manager
   resolves by keeping both sides, and *"the work does not return to the checker or the gate, nothing having been
   authored"*; any other conflict the branch's own worker resolves, and *"the resolution is new work, so it returns
   to the checker and to the gate"*; and two sides that genuinely contradict abort into a correction round, with
   **no destination stated**. Node 176 reaches the same place independently. **Node 200's own conflict was the first
   of those three** — the manager and the node had both appended to the same record file — so a rule already existed
   and it said *land it*. Nobody applied it because node 115's answer has never been written into the map: the node
   that carries it there, **node 160, is open and blocked on node 144**. Its own worker recorded that you *"settled
   that conflicts are resolved at integration and named no resolver"* — the three-way split is that worker's
   derivation, not your words.

4. **Node 68 says the opposite for one case:** a post-rebase bar failure *"takes a correction round — no new status,
   no new gate outcome."* A bar failure means somebody authors a fix, and node 115 says authored content returns to
   the gate. Both cannot hold.

5. **Two corrections to my node's own framing**, which I found rather than assumed.
   - **A second gate is not an extra gate.** Nothing shipped says a node has one gate *raise*; the manager contract
     mandates re-raising uncapped, node 143 and node 200 each ran two raises with two checker runs, and node 22
     calls six of them *"six rounds at one gate"*. Node 108, which you resolved, says a gate *"re-enters the queue
     when it is next raised"* and that a live re-check occupies your channel not at all. **So the price of coming
     back to you is a held code slot, not your attention** — much cheaper than my node assumed.
   - **Route 2's stated ground does not exist in the record.** My node justifies it by *"the human's word being
     about the content"*. Nothing shipped or recorded says approval attaches to content. The two recorded scopes are
     *"the only thing that permits a code commit"* and *"the human's approval of a node's end is that node's
     settlement"*, plus the repeated rule that an `approve` covers only the payload it answers.

So the three routes are not three candidates for one rule. **Two of them each already win in their own case, and
what is missing is the test that says which.**

Settled on my own authority: that node 115's answer is a decision in force even though the map has not caught up;
and that **whether any of this reaches the shipped skill files is not mine** — node 162 already holds that,
including whether the contracts' definition of a correction round, today *"one cycle of the human saying what is
wrong and you fixing it"*, widens to a round the integration triggers rather than you.

**Q1. Whether your approval survives what nobody authored**

**ASK:** After you approve a node at its gate, should the single test be **whether anybody authored content
afterwards**? Nothing authored — your approval stands: the manager re-runs the bar and lands, with no re-check and
no return to you. Something authored — the work goes back to the checker (re-running the acceptance condition only
where the worker says its fix touched something the condition names, your existing test unchanged) and then back to
you for another approval. This would supersede node 68's *"no new gate outcome"* for a post-rebase bar failure.

**RECOMMENDED:** Yes. It generalises the split already recorded at node 115 rather than inventing one, and it
supplies the one thing "a round returns to whoever raised it" cannot: an integration failure is raised by the
*manager*, and the manager cannot be the return address for authored content, being barred from reading code to
produce a note — the same ground node 115's worker gave for refusing to make the manager the resolver of a code
conflict. It also prices correctly now that a re-raise is known to cost a code slot rather than your channel. And it
settles the distinction my node calls the sharp one by keying on *was anything authored* rather than on *is the
content identical*: node 200's re-application lands on the original approval, while a rebase onto a base that moved
the passage under the work comes back to you.

**ALTERNATIVES:**
- Always come back to you (route 1) — safest; it charges you for bytes you have already seen in the case the record
  says is the common one, and node 115 already refused it for throughput.
- Never come back; checker plus bar suffice (route 2) — set aside: the checker holds the condition, not your
  judgement, and its stated ground turns out not to be in the record.
- Neither, always (route 3, what the manager did at node 200) — set aside: right where nothing was authored, and it
  makes the manager sole judge of authored content where something was.
- Keep node 68 and narrow node 115 instead, so no post-approval event ever returns to you — set aside: it makes your
  approval cover content that did not exist when you gave it.

**Q2. What the manager must show when it lands on the approval you already gave**

**ASK:** In the branch where the manager lands without coming back to you, must it **show the evidence** — the diff
of the rebased result against what you approved, named in the landing report as a command you can run — or is its
own assertion that it verified them identical enough? Your existing duty on this fires one step earlier: *"Where the
manager skipped a re-check, the payload says so rather than leaving it to be inferred"*, which at node 71 the
manager honoured in the gate payload **before** you approved. This asks whether that duty extends past the approval,
into the landing report, and whether it now needs proof rather than a statement.

**RECOMMENDED:** Yes, extend it, and with the command rather than the claim; the report awaits no answer. A bare *"I
verified it"* is exactly the unfalsifiable manager judgement this node exists to remove, and the record already
prefers the mechanical form — node 209 was minted on the finding that *"a condition demanding byte-identity is
discharged by diff, not by reading"*, three workers having already proved identity by `cmp` instead of reading. The
gate payload is already required to name the command that shows a diff, so this is a shape you already receive.

**ALTERNATIVES:**
- The assertion is enough — set aside: cheap for the manager, unfalsifiable for you.
- Show the diff and wait for a word before merging — set aside: that is a return to you under another name, which
  Q1's nothing-authored branch exists to avoid.
- Have the checker confirm identity — set aside: it spends a checker run on what one `git diff` settles, and the
  checker holds the condition rather than the bytes you approved.
- Leave it at node 71's precedent, disclosure before the approval only — set aside: in this case the event that
  needs disclosing has not happened yet when you approve.

**Q3. A rebase that fails without conflicting**

**ASK:** The policy's sentence is about a rebase *conflict*. Landing node 188, the rebase failed for something that
was not a conflict at all: the sandbox refused to unlink a file under `.claude/skills/`, git reported only `could
not detach HEAD`, and the failed attempt left a partial checkout that made the tree dirty. The manager ran the
repair the record already prescribes from node 143 — `reset --hard` to the branch's own commit, `clean` the record
directory, then rebase, sandbox off — the rebase then succeeded with no conflict, and the work landed. Should a
rebase failure that produces **no conflict** sit outside this policy's correction-round sentence entirely, as
plumbing the manager repairs, retries and reports, with no round, no re-check and no return to you?

**RECOMMENDED:** Yes, outside it. An environment refusal changes no byte of anybody's work, both `--abort` and the
prescribed repair are total undos, and node 143 established that repair as a measured single pass after four failed
attempts. Reading "the rebase failed" as the trigger would spend a whole worker on a filesystem mount, and the
worker would have nothing to correct. One thing I want stated alongside the yes rather than hidden by it: **that
repair runs `reset --hard` and `clean` over a branch holding approved-but-unmerged work**, so this route is only as
safe as the repair being exactly the prescribed one — I would not extend the licence to a repair the manager
improvises, and Q2's evidence is what makes it checkable after the fact.

**ALTERNATIVES:**
- Read "the rebase failed" as the trigger and take a correction round — set aside: a worker's cost for a mount
  option, with nothing for it to fix.
- Have the manager raise it to you each time — set aside: it is a known, measured, prescribed repair; raising it
  turns a solved problem into a queue entry.
- Draw no distinction and leave the manager to judge case by case — set aside: that is exactly the silence this node
  exists to end.

### The manager's note beside this attempt

*Not part of what the worker wrote, and not an answer to any of it.*

**Its Q3 is about an event the manager caused an hour ago and told this worker about**, so the manager is a party to
that question and states its own conduct rather than a view: it ran the node-143 repair, disclosed the failure and
the override at the landing, and did not take a correction round. **Its finding at point 3 is more serious than the
question it was minted for** — node 115's answer already settles the case node 200 hit, and the manager applied its
own judgement to a question the record had answered, because the node carrying that answer into the map is open and
blocked. That is a `MANAGER-WRONG` flag, and it is filed below rather than left inside the payload.

## Flags

`216.1` `MANAGER-WRONG` — **The manager filed this node saying the policy was silent, and it was not.** This node's
question section states that *"the policy's silence means the manager decides"*, and the manager decided route 3 at
node 200's landing on that basis. **Node 115's answer already covers the case node 200 hit** — a conflict in
never-delete text, which the manager resolves by keeping both sides, and *"the work does not return to the checker or
the gate, nothing having been authored"*. The manager reached the same destination by its own judgement without
knowing the rule existed, so the outcome was right and the reasoning was invented. What made it invisible is real
and is not the manager's: node 115's answer has never been carried into the map, and the node that carries it, node
160, is open and blocked on node 144. **The node's subject survives** — node 115 states no destination for the
genuine-contradiction case, and node 68 contradicts node 115 for a post-rebase bar failure — but its premise that the
record was silent is wrong, and it was the manager's premise rather than a worker's.
