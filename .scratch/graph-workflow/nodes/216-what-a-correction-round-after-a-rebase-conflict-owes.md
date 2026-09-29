# What a correction round after a rebase conflict owes — a re-check, a second gate, or neither

Type: grilling
Status: resolved

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

`216.1` `MANAGER-WRONG` **· settled** — **The manager filed this node saying the policy was silent, and it was not.** This node's
question section states that *"the policy's silence means the manager decides"*, and the manager decided route 3 at
node 200's landing on that basis. **Node 115's answer already covers the case node 200 hit** — a conflict in
never-delete text, which the manager resolves by keeping both sides, and *"the work does not return to the checker or
the gate, nothing having been authored"*. The manager reached the same destination by its own judgement without
knowing the rule existed, so the outcome was right and the reasoning was invented. What made it invisible is real
and is not the manager's: node 115's answer has never been carried into the map, and the node that carries it, node
160, is open and blocked on node 144. **The node's subject survives** — node 115 states no destination for the
genuine-contradiction case, and node 68 contradicts node 115 for a post-rebase bar failure — but its premise that the
record was silent is wrong, and it was the manager's premise rather than a worker's.

## Annotation: a measured fact the record did not have, arriving during node 198's landing

*Filed by the manager from its own landing of [node
198](198-two-files-describe-the-rules-file-by-contents-node-188-removes.md). It bears on this node's `Q3.`, which
is still unanswered, and it is recorded here rather than acted on.*

**What the record says about a sandboxed merge failure**, in `map-manager-only.md`'s landing section: *"`HEAD` does
not move and nothing is lost — the commit stays on its branch and the merge succeeds on a retry outside the
sandbox."* **Both halves of that are true and the sentence is still incomplete.**

**What was measured at node 198's landing.** `git merge --ff-only` inside the sandbox printed `Updating
8eaa7fa..b4595b3` and then `error: unable to unlink old '.claude/skills/expedition/graph-conventions.md':
Read-only file system`. `HEAD` did not move, as recorded. **But the merge had already written the other file**: the
main tree was left with `.scratch/graph-workflow/map.md` modified, and the retry outside the sandbox then refused
with *"Your local changes to the following files would be overwritten by merge"*. So the documented retry **does not
work on its own** where the branch touches more than one file and only one of them is under a read-only mount.

**What made it safe to repair rather than a loss.** The manager established that the dirt was **byte-identical to
what the branch carried** — `git diff <branch> -- .scratch/graph-workflow/map.md` returned nothing — so discarding
it with `git checkout --` lost nothing that the merge would not immediately restore, which it then did, verified by
the same diff returning nothing afterwards. **Had the diff been non-empty the repair would not have been the
manager's to make**, and that is the branch this node's `Q3.` is about.

**Why this is evidence for `Q3.` rather than a new question.** `Q3.` asks whether a failure that produces no
conflict sits outside the correction-round rule as plumbing the manager repairs. This is a second instance of that
shape — an environment refusal, no content in dispute, a total undo available — **and it is the first one where the
undo required the manager to verify content-identity before acting.** The worker's own caveat on recommending
`Q3.` was exactly that: *"this route is only as safe as the repair being exactly the prescribed one."* **Here the
prescribed repair did not cover the case**, and the manager improvised one it could verify.

### The human's answer to attempt 1

**Their words, `verbatim`.**

> 216: Q1 ok Q2 don't give the diff, If I want the diff, I can get it. On another notes, the current diff command is not useful, I am using vscode, not looking at the diff in the terminal, it can be removed. Q3 ok

**Q1 — `ok`, taking the worker's recommendation**, quoted as the worker wrote it:

> Yes. It generalises the split already recorded at node 115 rather than inventing one, and it supplies the one
> thing "a round returns to whoever raised it" cannot: an integration failure is raised by the *manager*, and the
> manager cannot be the return address for authored content, being barred from reading code to produce a note.

**Q2 — `don't give the diff`. This is a DIVERGENCE from the worker's recommendation**, and is marked as one so that
the worker does not read a bare answer as agreement. **The worker recommended the opposite**, in its own words:

> Yes, extend it, and with the command rather than the claim; the report awaits no answer. A bare *"I verified it"*
> is exactly the unfalsifiable manager judgement this node exists to remove.

**The human's ground, `verbatim`:** *"If I want the diff, I can get it."* So the duty the worker proposed —
that the manager show the evidence as a runnable command when it lands on an approval already given — **is
refused**, and what remains owed at a landing is whatever Q1's answer requires and no diff.

**Q3 — `ok`, taking the worker's recommendation**, quoted as the worker wrote it:

> Yes, outside it. An environment refusal changes no byte of anybody's work, both `--abort` and the prescribed
> repair are total undos, and node 143 established that repair as a measured single pass after four failed
> attempts.

*The worker's caveat on Q3 travelled with that recommendation and the answer does not address it:* **"that repair
runs `reset --hard` and `clean` over a branch holding approved-but-unmerged work, so this route is only as safe as
the repair being exactly the prescribed one."** The manager hit exactly that limit at node 198's landing, recorded
in the annotation above, where the prescribed repair did not cover the case and the manager improvised one it could
verify. **That is unanswered and the manager has not treated Q3's `ok` as covering it.**

### The steering that arrived alongside, and which is not an answer to this node

**Their words, `verbatim`:** *"On another notes, the current diff command is not useful, I am using vscode, not
looking at the diff in the terminal, it can be removed."*

**This reverses a rule of their own** — the landing policy's *"the gate payload names the worktree's path and the
command that shows its diff"*, given after a gate reached them with neither. It is recorded as standing steering in
`map.md` and carried into the two files that state it by [node
231](231-a-gate-payload-stops-carrying-a-diff-command.md). **The worktree's path survives; the command goes.** The
manager has already stopped emitting it.

## Answer

*Pasted as the worker wrote it.*

### The rule: one test, applied once, at the approval

After the human approves an implementation node at its gate, everything between that approval and the merge is
governed by a single test: **did anybody author content after the approval?**

- **Nothing authored** — the approval stands. The manager re-runs the bar on the rebased result and merges. No
  re-check, no return to the human. What reaches them is the landing report, which awaits no answer.
- **Something authored** — the work returns to the **checker**, which re-runs the bar in full and re-checks the
  acceptance condition only where the worker reports that its change touched something the condition names — the
  existing shipped test, unchanged — and then to the **human** for another approval.

The human's word, `verbatim`: *"Q1 ok"*, taking the recommendation as written.

### What the test decides, case by case

| what happened after the approval | authored? | where it goes |
| --- | --- | --- |
| a conflict in text held under the never-delete rule, the manager keeping both sides | no | the manager lands it — node 115's first branch, unchanged |
| the same hunks re-applying at a different offset — node 200's case | no | the manager lands it |
| a conflict anywhere else, product code included, the branch's own worker resolving it | yes | the checker, then the gate — node 115's second branch, unchanged |
| two sides that genuinely contradict: `git rebase --abort`, correction round | yes | the checker, then the gate — **node 115 left this destination unstated, and this is what fills it** |
| a post-rebase bar failure | yes | the checker, then the gate |
| a rebase that fails without conflicting | not in this vocabulary at all — see below | the manager repairs, retries, lands |

### Why the manager cannot be the return address for authored content

The record's general rule is that **a round returns to whoever raised it**: a checker `FAIL` goes back to the
checker, a gate `correct` goes back to the gate and not the checker. That rule holds because the raiser can judge
the fix. An integration failure is raised by the **manager**, which can judge neither — it is barred from reading
code to produce a note, which is the ground node 115's own worker gave for refusing to make the manager the
resolver of a code conflict. So the general rule does not reach this case, and the authored test governs instead.

### What this supersedes

Node 68's *"**A post-rebase bar failure takes a correction round** — no new status, no new gate outcome"* is
superseded in its second clause only. A bar failure is fixed by somebody authoring something, and content that did
not exist when the human approved is not covered by that approval. **"No new status" stands**: the node does not
change state, and it is the same node throughout.

The landing policy's *"A post-rebase bar failure likewise takes a correction round, and the work does not land"* is
incomplete rather than wrong: the work does land, after the round, the re-check and a second approval.

### What an approval covers, stated because this node's question assumed otherwise

This node offered a route resting on *"the human's word being about the content"*. **It is not.** The recorded
scopes of an approval are three: it is the only thing that permits a code commit; it settles that node's flags; and
it covers the payload it answers. The test above therefore does not rest on approval attaching to bytes — it rests
on the opposite. Approval covers what was in front of them, and content authored afterwards was not.

### The price, measured rather than assumed

Coming back to the human is **not a second gate**. Nothing shipped says a node has one gate *raise*: the manager
contract mandates re-raising uncapped, nodes 143 and 200 each ran two raises with two checker runs, and node 22
calls six of them *"six rounds at one gate"*. Node 108 settles that a gate *"re-enters the queue when it is next
raised"* and that a live re-check occupies the human's channel not at all. **So the cost of the authored branch is a
held code slot, not the human's attention** — which is what makes it affordable, and it is cheaper than this node's
own question assumed.

### The manager shows no diff, and the landing report carries no proof

**`DIVERGENCE`.** The recommendation was that the manager prove, with a command, that what landed equals what was
approved. The human refused it, `verbatim`: *"don't give the diff, If I want the diff, I can get it."*

So at a landing on an approval already given, the manager owes what the test above requires and nothing more: it
says what happened and that the work landed. It does not prove the content unchanged, and node 71's duty to disclose
a skipped re-check **does not extend past the approval**.

**What the refusal does not reach is the manager's own verification.** The question was about *showing*, not about
*doing*, and the test above cannot be applied without it: deciding whether anything was authored is a fact the
manager must establish before it chooses a branch. It establishes it and does not display it.

**This answer assumes no diff command anywhere.** The same reply removes the gate payload's diff command as standing
steering — their words, `verbatim`: *"the current diff command is not useful, I am using vscode, not looking at the
diff in the terminal, it can be removed"* — carried by a separate node. The worktree's path survives; the command
does not. Nothing above depends on one.

### A rebase that fails without conflicting is not a correction round at all

Their word, `verbatim`: *"Q3 ok"*. A rebase failure that produces **no conflict** — a sandbox refusal, an
environment error, a dirty tree left behind by a previous failed attempt — sits outside the correction-round rule
entirely. The manager repairs, retries and reports. No round, no re-check, no return to the human. Nothing was
authored and the worker has nothing to correct; reading *"the rebase failed"* as the trigger would spend a whole
worker on a filesystem mount.

**The licence is narrower than that sentence sounds, and the boundary is the repair.** It covers a failure whose
repair the record already prescribes — node 143's single pass of `reset --hard` to the branch's own commit, `clean`
the record directory, then rebase. **Where the manager must improvise a repair, the failure is outside the
prescribed set**, because an improvisation is the manager deciding on its own how to restore work the human approved
and which has not landed — the shape of judgement this node exists to take away from it. Such a case is **named in
the landing report as an improvisation** and **minted as a node**, so the prescribed set grows rather than the
improvisation repeating silently. It is not proof and it is not a diff; it is one line saying the record did not
cover this.

This boundary was tested for real while this node was being answered, and the licence's limit is therefore measured
rather than predicted: landing node 198, a sandboxed `git merge --ff-only` printed `Updating <a>..<b>`, failed on a
read-only mount **having already written one of the changed files**, and left the tree partially updated so that the
documented retry outside the sandbox refused with *"Your local changes would be overwritten by merge"*. The manager
improvised, and the human's `ok` was given without that case in front of them.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.

`216.2` **· settled** — *The manager's entry, 2026-09-29:* this flag's entry above is in a form the marker position does not fit, so its settling is recorded here. Settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4.

`216.3` **· settled** — *The manager's entry, 2026-09-29:* this flag's entry above is in a form the marker position does not fit, so its settling is recorded here. Settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4.

`216.4` **· settled** — *The manager's entry, 2026-09-29:* this flag's entry above is in a form the marker position does not fit, so its settling is recorded here. Settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4.

`216.5` **· settled** — *The manager's entry, 2026-09-29:* this flag's entry above is in a form the marker position does not fit, so its settling is recorded here. Settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4.

`216.6` **· settled** — *The manager's entry, 2026-09-29:* this flag's entry above is in a form the marker position does not fit, so its settling is recorded here. Settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4.
