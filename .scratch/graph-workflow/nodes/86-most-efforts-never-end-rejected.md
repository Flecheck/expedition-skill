# The human rejects *most efforts never end*

Type: grilling
Status: resolved

## Question

[Done-ness and termination](10-done-ness.md) resolved with the finding **"Most efforts never terminate at all, and
that is a legitimate steady state."** The human has now rejected it. Their words, `verbatim`, given at [Write the
first version of the manager's skill](76-write-the-manager-skill.md)'s interview: *"For close 36, I disagree that
most efforts never end."*

**This is the cascade's own case** — a settled decision contradicted after other decisions were built on it — and
this node exists because the claim is load-bearing in eight places rather than one.

### Where the claim lives, gathered rather than assumed

- **[Done-ness and termination](10-done-ness.md)**, which made the finding, and its one-line entry in
  [decisions.md](../decisions.md), which states it as the node's own.
- **`CONTEXT.md`'s `Closed` entry**, in the **product tree**: *"Most efforts are never closed, and that is a
  legitimate steady state."* This is the only instance that ships.
- **[Git and code-landing policy](11-git-and-code-landing.md)** — *"Most efforts never terminate…, so an effort
  branch has no merge point."* The claim is the **reason** the landing policy has no effort branch. This is the
  instance with the most weight on it.
- **[Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md)** — *"The twenty have
  exactly one route to the human: the closing report. Most efforts are never closed."*
- **[Workflow self-improvement during use](19-workflow-self-improvement.md)**, twice — a `FRICTION` flag is raised
  where noticed *"because most efforts never close and the closing report would then never…"*.
- **Duty 142 of [Gather the manager's accumulated duties](75-gather-the-managers-duties.md)**, which carried it into
  the manager's contract as a thing the file must state.

### What the answer has to settle, and it is not one question

**1. What replaces the claim.** *Most efforts never end* is a prediction about how efforts behave. Rejecting it
leaves three possibilities and the human's one line does not choose between them: that most efforts **do** end;
that the proportion is unknown and the workflow should not assume either way; or that the claim was never a
prediction to make in a design and should simply not be stated. **The third is the cheapest and nothing in the
record rules it out** — no effort has ever terminated under this workflow, so the original finding was itself
unmeasured.

**2. Whether the things built on it survive.** Each of the three reasoning sites has to be re-read against whatever
replaces the claim, and they do not all fail together:

- **The landing policy** is the sharp one. If efforts do end, an effort branch has a merge point after all, and
  *"a branch that never merges either forks the repo indefinitely or has to be merged back continuously"* stops
  being decisive. The conclusion may still hold on its other grounds; that has to be checked rather than assumed.
- **The two flag-routing sites** say a `FRICTION` flag must not wait for the closing report. If efforts end, the
  report is reachable and the argument weakens — but *"raised where noticed"* has independent grounds, so this
  probably survives.
- **`CONTEXT.md`'s entry** is the only one in the product tree, so it is the only one a repository that never sees
  this graph would read. It says the same thing and nothing else supports it there.

**3. What the surviving sentence should be.** `## Closing an effort` in the manager's contract now reads *"A
frontier that never empties is a legitimate steady state rather than a stalled one"* and makes no claim about how
often that happens. **That may be the right form everywhere**: it states what the manager must not treat as
failure, which is the operative half, without predicting frequency. If so, this node's answer is mostly a
find-and-replace with a shape already chosen.

### What is already done, and is not this node's

The manager's contract no longer makes the claim: clause 36's demand was amended away by the human at node 76's
interview, and the file was told not to state it in any wording. **`CONTEXT.md` was deliberately left alone** —
clause 42 forbids editing an existing entry and the manager declined to license a departure for something reaching
past that node.

## Where it came from

The human's own words at node 76's interview, in answer to a manager's raise about two clause-mandated statements
their edit had removed. The other of the two was settled there; this one was not, because it rejects a claim rather
than trimming a sentence.

## The manager's note on why this is the recommended next pick

*Filed at the handover to a fresh manager, because [map.md](../map.md)'s `Resume and recovery` fog item records
that **why the manager chose the nodes it chose** is exactly what a session does not leave behind. Not binding on
whoever picks next — a manager picks for itself.*

**Three grounds, in order of weight.**

1. **It is the only open node that contradicts a *resolved* one.** Every other open node adds something missing;
   this one says something already settled and cited is wrong. [Revision semantics](06-revision-semantics.md)
   treats that as the case the graph is least able to leave alone, and nothing else on the frontier is in that
   class.
2. **One instance of it ships.** `CONTEXT.md`'s **Closed** entry states the rejected claim to every reader of the
   skill set, including repositories that never see this graph. The other seven instances are in the record and
   cost nothing until read; that one is in the product.
3. **It is cheap and it unblocks reasoning elsewhere.** The likely answer — that the claim was never one a design
   should make, no effort having ever terminated under this workflow — is a find-and-replace with a shape already
   chosen, *"a frontier that never empties is a legitimate steady state"*, which states the operative half without
   predicting frequency. Until it is settled, [Git and code-landing policy](11-git-and-code-landing.md)'s reason
   for having no effort branch rests on a claim the human has rejected.

**What argues against taking it first.** It is a grilling node and therefore spends the human, who is the scarce
resource; three implementation nodes on the frontier spend nobody. And [The manager's cascade duties are in
neither contract](87-managers-cascade-duties-have-no-contract.md) and [Carry the worktree lifecycle into the manager's contract](89-carry-worktree-lifecycle-into-managers-contract.md) both carry conditions written only in part, so each already owes the human a question before
it can be claimed — bundling those two questions with this one is the cheaper use of a single human turn than
taking this node alone.

## Interview

### Attempt 1 — what replaces the rejected frequency claim

**Q1, from the worker.** *"You rejected 'most efforts never end'. What stands in its place — should the workflow
simply never make a claim about how often efforts end, and state only the conditional that an effort which never
ends is a legitimate steady state rather than a stalled one?"* Its recommendation, in its words: *"Yes — make no
frequency claim anywhere, in any wording."* Its three alternatives were to assert the opposite, to assert that the
proportion is unknown, and to confine the claim to open-ended efforts.

**A1, from the human**, `verbatim`: *"Yes for no frequency. I expect it to be more rare in practice that it doesn't
ends. If it is a very long running effort it will be talked about during the start of the effort I expect"*

**The option taken**, quoted from the worker, which wrote it: *"Yes — make no frequency claim anywhere, in any
wording."* Not a divergence — the answer takes the recommendation.

**Two things in the answer beyond the option**, relayed to the worker rather than read by the manager. The human's
own expectation is that an effort failing to end is **rare**, which is the reverse of node 10's rejected claim and
is stated as their expectation rather than as a claim for the files. And they expect a very long running effort to
be *"talked about during the start of the effort"* — which bears on node 10's ruling that the destination decides
whether an effort can terminate, and was not something the question asked about.

## Answer

*Written by the node's worker and pasted as it wrote it.*

**The workflow makes no claim about how often efforts end, in any wording.** The human's words, `verbatim`, at this
node's interview: *"Yes for no frequency. I expect it to be more rare in practice that it doesn't ends. If it is a
very long running effort it will be talked about during the start of the effort I expect"* — taken against the
recommendation *"Yes — make no frequency claim anywhere, in any wording."* No `DIVERGENCE`.

What replaces *most efforts never terminate* is not the opposite claim. It is the conditional that was underneath it
all along: **an effort whose frontier never empties is in a legitimate steady state rather than a stalled one, and
the workflow must not treat it as a defect.** That is the operative half — it says what the manager may not read as
failure — and it says nothing about frequency. The shape was already chosen and already ships in the manager's
contract, which the human amended at [Write the first version of the manager's skill](76-write-the-manager-skill.md):
*"A frontier that never empties is a legitimate steady state rather than a stalled one."*

### Why the claim was never one to make

Four grounds, and none of them is that the opposite is true.

1. **[Done-ness and termination](10-done-ness.md)'s own answer already holds the right structure without it.** Under
   `### Three kinds of effort, one mechanism` it separates bounded delivery efforts (*"They empty, terminate, and get
   closed"*), open-ended ones, and this map, and rules that **the destination decides whether an effort can
   terminate.** The frequency headline sits on top of a taxonomy that already handles both cases and needs nothing
   from it.
2. **The human's own words in that same node supplied the terminating case**, `verbatim`: *"I will most likely test
   the workflow on some other projects also (not on this machine, for my work), which will finish."* [map.md](../map.md)
   carries it as *"those are the efforts that will actually terminate, since Lang's will not."* The record already
   held their statement that work efforts end; only the proportion was ever asserted.
3. **The proportion was never measured.** No effort has ever terminated under this workflow, and exactly one has ever
   existed. The original finding was a prediction from a sample of one.
4. **At six of the eight sites the word carries no load**, the sentence around it already being conditional.
   [Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md) already says *"on efforts
   like it that route may never open"*; [Workflow self-improvement during use](19-workflow-self-improvement.md)
   already says *"because a foreign effort may never close"* three lines after stating the frequency form, which is
   the same node arguing its point both ways.

### The human expects the reverse, and the files still state neither

Their expectation is that failing to end is **rare** — the reverse of the rejected claim. It is recorded as their
expectation and is **not** a claim the files make. Making it would be the same defect in the other direction, and it
carries a worse failure mode than the one being removed: a manager that reads a non-empty frontier as a stalled
effort. What their expectation does establish is that the never-ending case is real and must still be handled, which
is what keeps the two flag-routing sites standing below.

### The landing policy stands, and its first ground is repaired differently than offered

[Git and code-landing policy](11-git-and-code-landing.md)'s `### No branch policy, and no push` gives three reasons
for having no effort-wide branch and calls the frequency one *"the decisive one"*. **The conclusion holds. The
decisive ground does not, and what replaces it is not what was put to the human.**

The repair offered at the interview was that the workflow cannot know, when it would open the branch, whether or when
the effort ends. **The human's own answer falsified that in the same breath** — *"If it is a very long running effort
it will be talked about during the start of the effort"* means the length of an effort is established at charting
time, so the workflow can know.

The ground that survives is about the **interval**, not the existence, of the merge point. Even for an effort known
to terminate, an effort branch's merge point sits at close, months away, while the human reviews *partially and
continuously* and hand-commits the graph files while work is in flight — both this node's own findings. So such a
branch must be merged back continuously, and node 11's own next clause is the conclusion: *"at which point it was
never a branch."* That clause never depended on frequency.

**And the second ground is untouched and sufficient alone**: *"The human owns branch choice. Lang is developed on
`main` with no local branches; a work repo that requires a branch gets one before the workflow starts."* The human's
new material **strengthens** it rather than weakening it — if whether an effort is long-running is discussed at its
start, that discussion is exactly where a human decides whether to cut a branch for it, and it is still not the
workflow's act.

**One thing the record must not lose:** that whole section has already been overtaken by [Run an implementation
node's work in a worktree](68-implementation-in-a-worktree.md). The workflow now does create and delete per-node
branches and does rewrite history by rebasing. Only the **effort-wide** branch is refused, and that refusal is what
this node preserves.

### The two flag-routing sites stand unchanged

Both argue that a flag must not wait for the closing report because the report may never fire. That is a
**possibility** argument, and the human's answer grants the possibility while calling it rare. A route that exists
for a case that occurs rarely is still required to exist. Node 19's deeper ground is not about closing at all — a
friction node on a foreign graph *"can never be resolved there, the fix landing in `graph-agent` by node 11's
policy"* — and is untouched.

### The disposition at each site is annotation, not replacement

**This node's fix is not a find-and-replace.** Five of the eight sites are graph files, and the standing rule that an
in-place update never deletes means superseded text is marked and left where it is, with new text added around it.
Nor is any node superseded: one sentence of an answer is being corrected, not an answer replaced, which is the case
[Revision semantics](06-revision-semantics.md) and node 11 both already handle by annotation. The per-site
disposition is on `INVALIDATIONS`.

Only `CONTEXT.md`'s **Closed** entry is a true edit, being a shipped file, and it is an implementation node behind a
gate rather than a cascade write.

**One occurrence that is not a site and must not be repaired:** node 76's clause 36 records what that clause demanded
before the human amended it away, and its `## Interview` records the rejection beside it. It is a record of the
correction, not an instance of the error.

### What the worker returned as `INVALIDATIONS`

*Pasted as it wrote it. The manager files these; this node mints no work for them.*

Eight sites. **None is superseded and none is rewritten** — the disposition is an annotation at each, per flag `86.1`.

1. **[Done-ness and termination](10-done-ness.md)** — its `## Answer` opens *"the fact that reframes this node is
   that most efforts will never be done at all."* Contradicted. Annotate: the frequency is withdrawn and the node's
   `### Three kinds of effort, one mechanism` is what its answer now rests on, unchanged. Its bullet *"A
   never-emptying frontier is a legitimate steady state, not a stalled one"* is already the surviving form and needs
   nothing.
2. **[decisions.md](../decisions.md)**, node 10's entry — its final sentence states the claim. Append-only, so it is
   struck in place with a parenthetical pointing here, the precedent being node 13's entry, which carries `~~four
   files~~ **five files**` plus a parenthetical.
3. **`CONTEXT.md`'s `Closed` entry** — contradicted, and the only instance in the product tree. Repaired by new node
   1 above and by nothing else; not a cascade write.
4. **[Git and code-landing policy](11-git-and-code-landing.md)**, `### No branch policy, and no push`, first bullet —
   *"**Most efforts never terminate** …, so an effort branch has no merge point"*, called the decisive reason. **The
   conclusion is not contradicted; its stated reason is.** Annotate with the surviving ground: an effort branch's
   merge point, where one exists, sits at close while the human reviews partially and continuously, so it must be
   merged back continuously — *"at which point it was never a branch"*, that node's own clause, which never depended
   on frequency. Its second reason, the human owning branch choice, is untouched and sufficient alone. The annotation
   sits alongside the node's existing one recording that node 68 replaced this section's conclusion.
5. **[Whether flags.md survives the settle-at-close practice](27-does-flags-file-survive.md)**, `### The residual` —
   *"Most efforts are never closed"*. Annotate: the frequency is withdrawn, the conclusion stands, and the sentence's
   own next clause already carries the surviving form.
6. **[Workflow self-improvement during use](19-workflow-self-improvement.md)**, first instance — *"because most
   efforts never close and the closing report would then never fire"*. Annotate: the conclusion stands; that same
   node's *"because a foreign effort may never close"* is the form it now rests on.
7. **[Workflow self-improvement during use](19-workflow-self-improvement.md)**, second instance — the alternative set
   aside as *"legitimate under [Done-ness]'s *most efforts never close*"*. Annotate: the citation is withdrawn. The
   alternative was set aside on other grounds and stays set aside.
8. **Duty 142 of [Gather the manager's accumulated duties](75-gather-the-managers-duties.md)** — *"Most efforts never
   terminate, and a never-emptying frontier is a legitimate steady state rather than a stalled one."* Annotate: the
   first half is withdrawn, the second half and the duty it states — *"The workflow must be useful continuously
   rather than only at the end"* — stand. The manager's shipped contract already carries only the surviving half.

**A ninth occurrence that is not an invalidation.** Node 76's clause 36 text and its `## Interview` record the demand
and the human's rejection of it. Repairing it would delete the record of the correction.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`86.1` **· settled** `ASSUMPTION` — **Chose annotation over supersession at all five graph-file sites, on my own authority.**
[Revision semantics](06-revision-semantics.md)'s letter says a node that is *"started or resolved"* is superseded,
which read against this node would supersede [Done-ness and termination](10-done-ness.md) and four others. I read the
practice on disk instead: node 06 itself carries `## Annotation: the inbound-edge repointing is the manager's step`,
filed from a worker's `INVALIDATIONS` entry, and node 11 carries three, one of which says outright that it *"corrects
this answer rather than superseding it"*. Supersession preserves work when an answer is replaced; here one sentence
of an answer is wrong and the rest of it is what carries this node's own reasoning, so superseding would retire five
correct answers to fix one sentence. The risk I am accepting: the shipped manager's contract lists as unsettled
*"Where does an annotation onto an already-resolved node belong? … the graph's own file format defines no such
section — neither its name, nor its place in the order, nor its form"*, so I am prescribing eight annotations in a
form nothing defines. I followed the form already on disk, `## Annotation: <what it says>`.

`86.2` **· settled** `ASSUMPTION` — **Made `CONTEXT.md`'s repair a new implementation node rather than a fourth entry on [Bring the
glossary's code-slot and reject entries up to the worktree lifecycle](81-glossary-code-slot-and-reject.md)'s
condition.** Node 81 is open, unclaimed, and already edits `CONTEXT.md`, so folding this in would cost no node. I did
not, because that node's own record is the argument against it: its condition was amended once by the manager, that
amendment is flag `81.1`, and it produced [How a condition's scope is
amended](82-amending-a-condition-whose-scope-was-too-narrow.md) precisely so the shape would not repeat. Doing it
again to save a node would be the third instance of the thing being fixed. The cost accepted: two nodes edit one
file. They touch disjoint entries and neither can run while the other holds the slot, so nothing collides.

`86.3` **· settled** `ASSUMPTION` — **Delivered a different repair to the landing policy's first ground than the one the human
assented to.** They were offered *"the workflow cannot name an effort branch's merge point at the time it would open
one"* and their answer's second half falsified it — if a long-running effort is talked about at the start, the
workflow can know. I did not go back with a second question, because the conclusion they endorsed is unchanged and
the ground I substituted is node 11's own next clause rather than new reasoning of mine. What is at risk is that they
endorsed a sentence that is now not the sentence in the answer.

## Annotation: the retrospective, and the manager's note on filing this node

*Filed by the manager. Not a change to the answer above.*

### The retrospective

*Effort-scoped, at the human's standing instruction. The worker's own text, pasted; the worker was not asked what it
cost and did not estimate it.*

**What I had to hunt for.**

- *That node 68 had already superseded the site this node calls its most load-bearing one.* Node 86 quotes node 11's
  *"an effort branch has no merge point"* bullet as live and never mentions that node 11's whole `### No branch
  policy, and no push` conclusion — *"The workflow never creates, switches or deletes a branch"* — has since been
  reversed. I found it in node 11's own third annotation, at the very end of the file, only because I read the file
  whole. I looked first at the quoted bullet, which reads as current. Had I stopped there I would have handed back an
  answer reasoning about a policy that no longer exists.
- *Whether the fix is a replacement or an annotation.* Node 86 says the answer is *"mostly a find-and-replace"*. That
  is forbidden at five of the eight sites by the effort's own never-delete rule. I looked first at node 06, whose
  letter says a resolved node is superseded — which points at a third, also-wrong answer. The practice that is
  actually correct is visible only as precedent, in node 06's own `## Annotation:` section and node 11's three.
- *Whether the manager's contract has a charting step*, needed to know whether the human's second remark surfaced a
  node or duplicated one. No pointer covers it; I grepped the shipped file's headings and read its nine unsettled
  duties.
- *The eight sites.* One `grep` over the repo found all of them plus two false positives. Node 86's enumeration was
  accurate, so this was confirmation rather than discovery, and it was cheap enough to be worth running anyway.

**What I read and did not use.** `map.md`, of which I used four paragraphs — never-delete, the landing policy, the
line about work projects being the efforts that terminate, and the ground rules. `CONTEXT.md`, of which I used one
entry of fifty-one. `graph-conventions.md`, from which I used nothing; its one hit on my grep was about node kinds
that never end in front of the human, an unrelated sense of the phrase. Node 81, which I read whole to settle
mint-versus-amend and used only the shape of.

**What would have made this node easier.**

- *In the node file:* say that node 68 superseded node 11's branch policy. Whoever wrote node 86 had node 11 open to
  quote from it, and the omission points the worker at a live-looking dead section.
- *In the node file:* do not name a disposition the effort's own rules forbid. *"Mostly a find-and-replace"* had to be
  undone before the work could start, and a worker that trusted it would have proposed deleting text from five node
  files.
- *In the node file:* give the eight sites as file-plus-quoted-phrase pairs. Half are given as node names alone, so
  each cost a read to locate — and standing rule 4 already requires citation by quoted phrase, so the node was asking
  for less than the effort's own rule.
- *In the spawn:* the manager's note that point 2 was the sharpest site was correct and useful, and it was the reason
  I read node 11 to the end rather than skimming to the quoted bullet.
- *In the contract:* nothing blocked me. The `## When you raise a flag` split between node prose and index sentence,
  and the rule that a node with a round carries its account in the round, were both unambiguous.

**What I read that was stale, wrong, or contradicted something else.**

- *Three sources give three different answers on correcting a resolved node.* Node 06's letter says supersede; node
  06's and node 11's own annotations say correct-in-place; the shipped manager's contract says the annotation's
  *"name, place in the order, and form"* are undefined. I picked the practice over the letter and flagged it, but this
  is a rule with no single statement anywhere.
- *The shipped set is internally inconsistent right now.* The manager's `SKILL.md` carries the corrected sentence
  while `CONTEXT.md` — the file that same skill set declares authoritative — still states the rejected claim. That is
  what this node exists to fix, but it means the glossary currently contradicts the contract that cites it as
  authoritative.
- *Node 19 states its point both ways within twenty-two lines*, once as a frequency and once as a possibility. Not
  stale so much as self-refuting, and it turned out to be the single best piece of evidence that the frequency was
  never carrying the argument.
- *Node 86's manager note argues for the answer that was reached*, on grounds that overlap mine. I treated it as one
  party's reading per the spawn's instruction and built the case from node 10 and the human's own prior words instead;
  I record it only because a worker that leaned on it would have inherited its silence about node 68.

### The manager's note

**The retrospective's second and third hunt items are findings against the previous manager's own note on this node**
— that note said the answer was *"mostly a find-and-replace with a shape already chosen"*, which the effort's
never-delete rule forbids at five of the eight sites, and it quoted node 11's branch bullet without saying node 68
had already reversed that section's conclusion. Both are recorded here and neither is repaired in the note above,
which stays as written under the never-delete rule.

**Flag `86.3` is the one to read at settlement.** The human assented to a repair of the landing policy's first ground
and the answer carries a different one, because their own second sentence falsified the version they were shown. The
worker judged that the conclusion was unchanged and did not re-ask. That judgement is theirs to confirm or reverse.
