# The priority list does not say the human must always have something to do

Type: implementation
Status: resolved

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

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> The ordering in `SKILL.md`'s `## The order you act in` now ends in a check on the state the turn ends in, and
> `expedition-triggers.md`'s `## Priority` carries the same two changes word for word. The list is still five items.
>
> **Item 4** now reads *"Giving a question to the human — **the human should always have something to do**, and this
> is the item that keeps that true."* The human's reason is the ground of the item, not a sixth item.
>
> **Item 5** is no longer the act `Waiting`: *"**Before you stop, a check rather than an act**: the human has
> something to do, or provably nothing is waiting — no gate assembled and unsent, no worker blocked on a raise, no
> raise of your own, no relayed question — and nothing an agent handed back is still unfiled. Where the check fails,
> send what this order gives you and stop after that. Waiting is the state you are in once it passes, never
> something you do instead of it."*
>
> **The diagnosis, because a fifth statement of the same shape would have failed the same way.** `SKILL.md` already
> said one question is in front of the human, that arrival order decides, and that the manager never asks which
> waiting thing to take — **and the manager read all three and still stopped with the human idle.** What none of them
> reaches is that **stopping is not an act the manager performs**: it is what happens when it emits nothing more, so
> **no ordering over acts can catch it.** The section now says so in as many words and names the exact failure — a
> turn that resumes and ends with a gate sitting unsent.
>
> **`Provably nothing` is a list you run and can say you ran, not a belief.** The four things item 5 names are the
> *whole membership of the pending queue* under `## What is in front of the human, and when`, whose membership that
> section already declares fixed and closed. **So the enumeration is not a new list invented here; it is the existing
> queue.** One loophole is closed by name: a gate whose check will not pass is still a gate and still waiting.
>
> **What counts as the human having something to do is bounded, because the observed failure was the manager feeling
> discharged by having spoken.** Only something they must act on counts. A pick report, a death notice and the
> closing report await no answer and pass nothing — node 108 settled that.
>
> **The fifth test is deliberately not a liveness check.** The condition's *"every agent in flight is still
> working"* ships as the phrase, immediately rendered as *what has come back that you have not filed, relayed or
> acted on*, and closed with *"never whether each agent is alive"*. **A literal liveness reading would demand a
> resume attempt against every agent before every stop, which contradicts the contract's own rule that death is
> discovered only by a resume that fails.**
>
> **The check terminates in an utterance, which is the human's own mechanism.** Their words were *"when waiting,
> always end with what the humain is supposed to do"*. The section closes with *"the last line of what you send says
> what they are to act on"*, and *"Where you are about to write that nothing is expected of them, run the list."*
> **Writing the sentence is what forces the check; a rule you can satisfy by believing something is the shape that
> already failed four times.** The charge is stated too: *"A turn that ends with the human idle while something waits
> is a defect of yours"*, and *"them asking for work you were already holding is that defect observed."*
>
> **The two lists are still one copy, verified.** Normalising list marker and wrapping, the two diff identical.
> Nothing else in the rules file changed.
>
> **One overlap the manager must sequence, and it is larger than this node's own.** **[Node
> 118](118-offer-a-written-question-the-moment-the-channel-is-free.md) (open, unclaimed) already carries most of
> this rule** and has since before node 267 was minted. Its clause 2 demands the shipped file state that *"whenever
> none is in front of them and a written question is waiting, the manager offers it at once, in the same act"* and
> that *"an idle channel with a written question waiting is a defect"*; its clause 4 demands that *"nothing is
> expected of you" is truthful only when nothing is waiting*. **Both come from node 108, resolved. So the rule the
> human asked for here was settled and waiting to ship, and the repeated failure is at least as much an unshipped
> settled answer as a gap in the ordering.** This node's work sits in a different section and states a stopping
> check rather than an offering duty, so the two compose — but when 118 is claimed, its clauses 2 and 4 will partly
> restate what is now in `## The order you act in`, and **its condition wants re-reading against the landed text
> first.**

**The index line the worker wrote**, held here until the node resolves:

> The manager's act ordering now terminates in a check on the state its turn ends in, with the pending queue
> enumerated so *provably nothing* is a list run rather than a belief held.

## Flags

*All three are the worker's own text, pasted.*

`267.1` `ASSUMPTION` — The condition's clause 3 says *"every agent in flight is still working"*. Taken literally
that is a liveness check, and the same contract states that death is discovered only by a resume that fails — so a
literal reading would oblige the manager to attempt a resume against every running agent before every stop. I
shipped the condition's phrase and immediately rendered it as *what an agent handed back that you have not filed,
relayed or acted on*, closing with *"never whether each agent is alive"*. **The operational content is the same and
the cost is not.**

`267.2` `ASSUMPTION` — Clause 4 asks for the two additions *"in the file's own terse register"*, which reads as
licence to word the rules file's copy differently. **I kept them word for word identical instead.** Node 255
established that the rules file is a copy of the skill's governing statement, and that file's own closing section
says so, so divergence would have broken a property a resolved node set and the file advertises — **and the
compaction-survival copy is exactly where the enumeration must survive.**

`267.3` `ASSUMPTION` — The closing sentence — *"the last line of what you send says what they are to act on"* — is
the shipping of a rule that **open node 96** owns. I wrote it anyway: it is the human's own mechanism in this node's
question, and **without it the check has no moment at which it fires**, leaving a fifth statement of a state the
manager is supposed to believe. It is scoped to the check rather than stated as a general duty on every report, so
node 96's rule is not pre-empted, only anticipated at one site.

## Invalidations

*The worker's text:* `none`. Node 108 is carried out rather than contradicted; node 255's word-for-word-copy
property is preserved and re-verified; node 105's demand that `## What is in front of the human, and when` be
unchanged in meaning is met, that section being cited and not edited.

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.** **The worktree** — the spawn's path did not exist; `git worktree list` found the
> real, doubled one. One wasted round, and it is now a node. **Second, node 118. Nothing pointed at it**; the handle
> search over open conditions found it, and **it is the single most consequential fact about this node.** The
> manager's notes named the four already-failed sentences but **not the settled node whose shipping would have
> supplied the rule.** Third, whether the two priority lists were meant to stay identical — that lives only inside
> node 255's `## Review` prose, not in either shipped file nor in the map.
>
> **2. What arrived that this node did not need.** `map.md` is ~115 lines and about six bore on this work; **nine
> workers have now said so.** `map-implementation-rules.md`'s review-route paragraph is the checker's and the spawn
> said so — **six workers have reported reading it for nothing, and it is still in the file a worker must read
> whole.** In my own contract, `## When a node you report is an implementation node` earned its place only because I
> reported one; `## If you are a replacement attempt` did not. **From the spawn: the warning that `Edit` is refused
> inside a worktree was worth its line and saved a round.**
>
> **3. What would have made this easier.** **One line in the spawn naming node 118 as prior art.** The manager holds
> the graph and this node's whole difficulty was that a settled answer had not shipped — **that is exactly the
> context a spawn is for, and it is inside the cap since the manager already holds it.** Second: the spawn named
> `## What is in front of the human, and when` as a deliverable, which the condition does not; the condition wins,
> but resolving the discrepancy cost a pass. Third: `map-implementation-rules.md` could hoist its worker-relevant
> material above the checker's review-route paragraph.
>
> **4. What was stale, wrong, or contradicted something else.** The spawn's worktree path, wrong. The stated
> worktree route in `map.md` and `map-manager-only.md`, contradicted by both live worktrees — now a node. Nothing
> else read contradicted anything.

## The manager's disposal

*Not the worker's text.*

- **Node 118 existing and unshipped is the finding, and it is the manager's failure rather than the record's.** The
  manager minted this node from the human's direction without checking whether the rule was already settled. **Node
  108 resolved it; node 118 holds the shipping and is open and unclaimed.** Filed as flag `267.4` below.
- **Its surfaced node duplicates [node 284](284-the-worktree-create-command-names-a-relative-path.md)**, minted an
  hour earlier from node 281's worker. **Two workers found it independently.** The manager has **not** merged the
  conditions: this one adds two demands node 284's lacks — that `map.md`'s paragraph state the same path, and that
  `git check-ignore` report `.gitignore` **and not** `.git/info/exclude` — and those are recorded on node 284 for
  whoever claims it rather than folded in silently.
- **The spawn naming a section the condition does not** → the manager's, and it cost a pass. Named.
- **`map.md`'s `## Notes`, tenth report; the review-route paragraph, seventh** → node 246 holds the first; the
  second is still unheld and the manager has now named it seven times.

`267.4` `MANAGER-WRONG` — ***Filed by the manager against itself.*** **It minted this node from the human's
direction without establishing whether the rule was already settled.** It was: [node
108](108-what-leaves-the-channel-free.md) resolved it, and [node
118](118-offer-a-written-question-the-moment-the-channel-is-free.md) has held the shipping, open and unclaimed,
since before node 267 existed. **So the failure the human corrected four times was an unshipped settled answer, and
the manager built a second route to it rather than shipping the first.** The worker found node 118 by the node-263
search duty, not from anything the manager gave it — **and the manager holds the graph, which is exactly the context
a spawn exists to carry.**

## Review

### Run 1 — `PASS`, all five clauses, no questions

*The checker's own text, pasted. Spawned by the manager, given the condition as extracted text, the bar as
properties, the two changed paths at the doubled worktree path, the record-as-work rule, and this effort's standing
rules. Given nothing from this node or the effort's record. **It was told to establish what the file says about
clause 3's last phrase rather than assume either reading.***

> **PASS**
>
> **No standard moved under the check.** Neither changed path holds a standard; `graph-conventions.md` sits beside
> one of them and is unchanged. **Settled before checking anything else.**
>
> **Read as the work under the implementation-rules rule.** **No node status line, no `decisions.md` line and no
> `flags.md` line appears among the work** — `git status --porcelain --untracked-files=all` returns exactly the two
> shipped files.
>
> **How I established "nothing else moved."** For each file I unwrapped `git show 0e82353:<path>` and the
> working-tree version into one-word-per-line streams and diffed those. **In both files the only changes are the
> replacement of priority items 4 and 5, plus — in `SKILL.md` alone — a contiguous pure insertion of the new `###`
> section. Not one other word moved in either file. That is a positive finding, not the absence of diff lines.**
>
> **1 — Met.** Item 5 now reads *"**Before you stop, a check rather than an act**: the human has something to do, or
> provably nothing is waiting…"* The send-before-ending half is *"Where the check fails, send what this order gives
> you and stop after that,"* reinforced by *"where it does not come back empty, you have your next act instead of an
> ending."*
>
> **2 — Met.** Inline, as item 4's ground. **The list still has five items; the reason is not a sixth.**
>
> **3 — Met.** Item 5's enumeration is a **1:1 match** with the condition's four. **I verified the closure claim the
> prose makes**: `## What is in front of the human, and when` holds tier 1 at exactly three with membership declared
> fixed, plus tier 2's relayed question. **Four, and the file's claim is true.**
>
> **4 — Met.** The rules file carries both additions verbatim and the bare `"Waiting, and only where nothing above
> is available."` is gone. **Verbatim copying is that file's own declared register** — it says of itself it holds *"a
> copy of the priority"* — and the two items were already word-identical across the files before this change.
>
> **5 — Met.** Exactly two files. **Both contain zero markdown links** (counted over unwrapped text), so link
> resolution holds vacuously; the one reference the new text makes is a heading citation in a code span, and that
> heading exists in the same file.
>
> **On clause 3's last phrase, which you asked me to establish rather than assume.** The shipped list renders it as
> *"nothing an agent handed back is still unfiled."* **The condition's own phrase does appear verbatim in the file**,
> in bold, naming that test — *"The fifth test stands outside that queue — **every agent in flight is still
> working**: anything an agent handed back that you have not filed, relayed or acted on puts item 1 or item 3 in
> reach… What you check there is what has come back, never whether each agent is alive."*
>
> **I judge this the clause, not a departure, and the deciding evidence is elsewhere in the same file.** `## When an
> agent dies or is stopped` states *"**Death is discovered only by a resume that fails.** You cannot read a running
> agent's transcript or inspect a dead one."* **Liveness is therefore not observable to a manager at all — so a test
> phrased as liveness is precisely one that could only be satisfied by inattention, which is the failure clause 3
> exists to close.** The rendering converts the clause's fifth test into the one fact a manager can actually run, and
> it fails the check in exactly the case where stopping would be the defect. **The residual case — an agent dead
> having handed nothing back — is not lost, it is routed by item 2, the failed resume being the detector. Nothing
> the manager could have delivered is given up.**
>
> **The bar.** Discovered from the repo: `git ls-files` returns no manifest of any kind and no `.github/`. **No
> build, no tests, no formatter, no CI, nothing to invoke** — a complete bar rather than a deficient one. **Ground
> rules** 1–4 all hold. **Four standing rules** — the five-element shape is stated uncompressed while the reasoning
> is compressed into the subsection; the explanation took its own `###` heading rather than swelling the parent; the
> one citation is by heading. **`CONTEXT.md`'s `_Avoid_` lines** checked by hand per the rules file's own measured
> warning: `gate`, `worker blocked on a raise`, `raise`, `relayed question`, `pick report`, `closing report` all
> match `CONTEXT.md`'s own vocabulary; `item` and `queue` are used in the non-refused senses.
>
> **No questions to hand back, and no part of the condition left uncovered.**

**The manager's disposal of run 1.** *Not the checker's text.*

- **`PASS` on all five, first run, no repair owed, and no questions** — the first check on this effort in some days
  to return nothing at all to carry.
- **It vindicated flag `267.1` and did so on evidence the worker did not cite.** The worker rendered *"every agent
  in flight is still working"* as a test on unfiled returns and flagged the departure. **The checker established it
  is not a departure**, from a sentence in the same file the worker never quoted: *"Death is discovered only by a
  resume that fails."* If liveness is unobservable, a liveness test **could only ever be satisfied by inattention** —
  which is the exact failure clause 3 was written to close. **So the literal reading would have defeated the
  clause.**
- **It checked a claim the shipped text makes about itself** rather than taking it — that the four enumerated items
  are the whole pending queue — by going to the section that declares that membership and counting. **The file's
  claim is true.**
- **The gate is assembled and queued.** [Node 283](283-what-makes-a-change-to-a-record-file-a-node-rather-than-bookkeeping.md)'s
  question is live in front of the human, and [node 281](281-map-repeats-the-false-no-override-claim-about-the-worktree-route.md)'s
  gate is ahead of this one by arrival.

### Gate — `approve`

**The human's answer**, `verbatim`: *"2 approve"* — the second of four given in one message.

No divergence: the payload carried a `PASS` on all five clauses, no questions, and no recommendation against
landing.

**Landed under the effort's landing policy.** One path-limited commit of the two shipped files; rebased with no
conflict; the bar's command half empty; `git merge --ff-only`; worktree removed and branch deleted **with the
sandbox off**. **Commit `e5c03a5`**, trailer `Node: graph-workflow/267`.

**What the approval does not settle.** [Node 118](118-offer-a-written-question-the-moment-the-channel-is-free.md)
still holds node 108's unshipped answer, open and unclaimed, and its clauses 2 and 4 now partly restate what this
node landed. **Its condition wants re-reading against the landed text before anyone claims it**, which is this
node's worker's own warning and is not discharged by the gate. Flag `267.4` records that the manager built this
second route without checking for the first.
