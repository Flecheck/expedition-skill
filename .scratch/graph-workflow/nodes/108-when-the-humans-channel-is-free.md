# When the human's channel is free, and whether the manager must fill every gap in it

Type: grilling
Status: resolved

## Question

**The human reported this as a defect in the manager's conduct.** Their words, `verbatim`: *"Since the worker for 100
was running, shouldn't you have given me the other question while it runs ?"*

### What happened, recorded by the manager against itself

[The manager starts the next node rather than proposing it and
waiting](100-the-manager-starts-the-next-node-rather-than-proposing-it.md)'s gate was in front of the human. They
replied querying one sentence. The manager wrote their words to disk, passed them to the worker unaltered, and told
them **"Nothing is expected of you right now"** — while [Whether a condition's scope stops being a list of
files](94-condition-scope-as-a-predicate.md)'s question and [Whether charting an effort establishes and records that
it is expected to end](91-charting-records-whether-an-effort-ends.md)'s question both sat written and queued.

**The manager treated the gate as occupying the channel for the whole of its lifetime**, including the stretch where
the worker held the correction round and nothing awaited the human's answer at all. Node 94's question went out only
after the round closed and a re-check was spawned — a whole worker-round later than it could have.

### Why the shipped rule does not settle it

`.claude/skills/expedition/SKILL.md`'s `## What is in front of the human, and when` fixes that exactly one question
is in front of the human and that nothing displaces a live one. **It does not say when a question stops being
live.** Two readings both fit its words:

- a gate occupies the channel from the moment it is raised until the node leaves the gate — the reading the manager
  took, which idles the channel for every correction round and every re-check;
- a question occupies the channel only while it awaits the human's answer, so the moment they reply the channel is
  free and the queue is served — under which the manager owed node 94's question immediately.

**And a second question sits behind that one**: whether the manager must *fill* a gap it finds, or may leave the
channel empty. The effort's never-idle rule is written about **work** — the manager starts nodes rather than
proposing them — and says nothing about the human's channel. The human's own framing here is *"shouldn't you have
given me the other question while it runs"*, which is a duty to fill rather than a permission to.

### What this is not

**It is not the count.** The target of two concurrently running nodes that need the human is settled and in the map.
This is about the single channel those nodes' questions queue for, and it would matter at a target of one or of five.
The human raised the count separately in the same session — *"Why can't I anser the other questions ?"* — and was
offered three ways to change it; that offer is open and is not this node.

## The manager's note at filing

*Not a change to anything above.*

**Filed as grilling rather than implementation, and the manager says why rather than choosing quietly.** Both
readings above are consistent with every shipped sentence, so nothing fixes which is right, and
[Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md)'s constraint 1 confines a manager-written condition to what is
already fixed. Writing one here would be the manager settling a rule about its own conduct.

**Not started, and this is what it is waiting for.** Two nodes that need the human already run — node 94 and node 91
— which is this effort's target, so starting this one would exceed it. It starts the moment one of them closes,
unless the human says otherwise.

**The manager's own conduct is the evidence and is not offered as an argument.** The instance above is recorded
because [Friction from running this map by hand](24-self-hosted-friction.md) makes the manager's own friction the
effort's material, not because it settles which reading is right.

## Annotation: a second instance, and a second cause the first one did not name

*Filed by the manager against itself while this node was claimed and its question queued. **Evidence, not an
argument** — the same standing as the instance in `## Question`.*

**What happened.** The manager sent a pick report closing node 100 and starting node 103. A pick report awaits no
answer, so nothing was in front of the human when it landed. Node 108's question and node 110's question were both
written and queued. The manager ended that report with *"Nothing is expected of you right now — node 108's and node
110's questions are both written and queued, and I will serve them the moment you reply to anything."*

**The human's reply**, `verbatim`: *"I don't understand the "I will serve them the moment you reply to anything ?""*

**The cause, which is not the one the first instance had.** The first instance was a reading of *when a question
stops being live*. This one is a **conflation of two different rules**: [A node's flags arrive after the human moment
that was supposed to settle them](99-flags-arrive-after-the-node-s-human-moment.md) fixes that a **flag's
settlement** rides the human's next word whatever that word is about, and the manager extended that to the **service
of the queue**, which no rule attaches to the human speaking at all. Under the correct reading the queue is served
when nothing awaits the human's answer, and a pick report awaiting no answer leaves the channel free the instant it
is sent.

**So the closing line was false twice over** — *"nothing is expected of you"* was true, but it accompanied two
questions the manager was holding back for no reason, and the sentence that followed named a trigger that does not
exist. [Every manager report ends with one line saying what is expected of the
human](96-every-manager-report-ends-with-what-is-expected.md) is the rule that makes the closing line a check on the
queue rather than decoration; this instance is a case where the line was written and the check was not performed.

**What the manager did on being told:** served node 108's question in the next message.


## Answer

*Written by this node's worker and pasted as it wrote it.*

**One rule with two halves, in the human's own words**, `verbatim`: *"there should be at most one question offered to
the user and if there is none and there is a question waiting from one of the subagents, it should be offered to the
user"*.

### 1. When the channel is free

A question occupies the human's channel **only while it awaits their answer**. Their words, `verbatim`: *"yes, it
frees the moment you reply"*.

So the channel is free from the moment the manager records their reply, whatever becomes of the node afterwards:

- a **gate** answered *correct* frees the channel at that reply. The correction round, the worker's respawn and the
  re-check all run with the channel free, and the gate re-enters the queue when it is next raised;
- anything the manager sends that **awaits no answer** leaves the channel free the instant it is sent — a report of a
  pick, a notice that an agent died, the closing report;
- a node sitting at its gate, a worker running, a check in flight: none of these occupy the channel.

**The channel is held by an unanswered question and by nothing else.**

**The reading this refuses** is the one the manager took: that a gate occupies the channel from the moment it is
raised until the node leaves it. That idles the channel for every correction round and every re-check, and it cost
node 94's question a whole worker-round.

**The ground, kept because the rule is easy to misread back.** The ceiling exists to keep a terse reply attributable
to exactly one thing — its measured cause was two *asked* things at once and a reply that named an option in only one
of them. A question already answered cannot be answered by accident, so nothing the ceiling protects is in play once
the human has replied.

### 2. The floor: the manager owes the gap

Whenever nothing is in front of the human and a written question is waiting, **the manager offers it at once** — in
the same act, not at its next convenient message. **An idle channel with a written question waiting is a defect
chargeable to the manager.**

This half is new. The ceiling was already shipped; the floor was not, and nothing anywhere placed a duty on the
human's channel while the map placed one on the manager's own idleness — an asymmetry running against the map's own
statement that the human is the scarce resource.

Read the two halves together: **the number of questions in front of the human is the smaller of the ceiling and the
number waiting.** Never more, and never fewer.

### 3. The ceiling is a number, and the duty is to top up to it

The ceiling is one unless the effort sets another. **The floor does not depend on its value**: whenever fewer than
the ceiling are in front of the human and something is waiting, the manager tops up at once. It is the shape the map
already uses for how many human-needing nodes run — *"a count is a target to reach rather than a ceiling to stay
under"*.

**Only the number is contingent.** §1's freeing rule and §2's floor hold at any ceiling, which is what lets this
answer survive a node revisiting how many questions reach the human at once.

### 4. The manager forecasts nothing about the queue

Under a duty the answer to *when* is always *at once*, so a sentence naming a future trigger for service is either
redundant or false. Both recorded failures wrote one — *"I will serve them the moment you reply to anything"* named a
trigger no rule creates.

So the line ending every manager report says what is expected of the human **now** and promises nothing about later.
*"Nothing is expected of you"* is a claim about the queue at the moment of writing, and is truthful only when nothing
is waiting. **Staleness needs no separate remedy**: a question arriving after that line is served at once, so the
human's next message from the manager is the question itself.

### 5. Why this rule needed a line to be checked on

Sixteen flags across six closed nodes stood unmarked while a rule declared them settled, because that rule's
performance left no trace. **A duty whose non-performance is invisible is a duty in name.** Tying this one to the
sentence the manager must write in every report is what makes skipping it visible to the human in the place they
already look.

### 6. What this does not decide

- **Tier membership.** The two tiers and tier 1's three fixed members are untouched. The floor says the manager
  serves the queue; the tiers say what it serves first.
- **Whether a pick report joins the shipped list of things that are not claimants.** The shipped file already says a
  pick report *"awaits no answer and takes no place in the queue"*, and §1 makes that mean the channel is free the
  instant it is sent. Whether *"Three things are not claimants at all"* should name it is flag `100.2`, outstanding
  and the human's.
- **How many questions reach the human at once.** §3 makes this answer survive any value.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id, the marker and the state.*

`108.1` `ASSUMPTION` — **The rule is written as a ceiling plus a top-up rather than as the literal number one.** The
human said *"at most one question offered to the user"*, naming the number; I wrote §3 so that only the number moves
if the ceiling is later changed, and so that §1 and §2 stand at any value. Decided because a node on sending
questions in batches is already minted and would revisit exactly that number, and because the map already carries
this shape for its other count — *"a count is a target to reach rather than a ceiling to stay under"*. The human
named a number, not a shape.

`108.2` `ASSUMPTION` — **The manager writes no forecast of when it will serve the queue.** §4 is mine and not the
human's: they stated the duty and said nothing about what the manager may write about it. Derived from the duty
itself — where the answer to *when* is always *at once*, a sentence naming a future trigger is either redundant or
false — and from the two recorded instances, one of which wrote a trigger no rule creates and was queried by the
human for exactly that.

`108.3` `ASSUMPTION` — **A duty to serve the queue is not a duty to keep the human busy.** The manager offers what is
already waiting and never manufactures a question to fill the channel. Decided because what may be started is
already bounded by the effort's two counts, so the queue's contents are governed there and not by the channel;
without the line, a floor on the channel reads as pressure to generate questions.

## Interview

### Attempt 1, round 1

**Asked**, in the worker's words:

> Does a question stop occupying your channel the moment you reply to it — so a gate you have answered with
> *"correct this"* frees the channel immediately and the queue is served while the worker fixes the work — or does a
> gate hold the channel from the moment it is raised until the node finally leaves the gate, correction rounds and
> re-checks included?

**Answered**, `verbatim`:

> yes, it frees the moment you reply

**The option taken**, written by this node's worker and quoted here as it offered it:

> It frees the moment you reply. The channel is occupied only by a question that is actually awaiting your answer.

*Not a divergence: the reply takes the worker's own recommendation, and names it in its own words rather than by
assent alone.*

**The manager's note on what the reply does not reach.** *Not a change to anything above.* This node's `## Question`
holds **two** questions, and the worker's `ASK` put only the first. The second — whether the manager **must** fill a
free channel or merely may — is not answered by this reply, and the worker holds it.

### Attempt 1, round 2

**Asked**, in the worker's words:

> When nothing awaits your answer and a written question is queued, **must** the manager serve it at once — so an
> idle channel with a non-empty queue is a defect chargeable to it — or **may** it hold the channel and serve the
> queue when it next judges the moment right?

**Answered**, `verbatim`:

> for 108, there should be at most one question offered to the user and if there is none and there is a question
> waiting from one of the subagents, it should be offered to the user

**The option taken**, written by this node's worker and quoted here as it offered it:

> A duty, unconditional, discharged in the same act rather than at the manager's next convenient message.

*Not a divergence: the reply takes the worker's own recommendation and states it as a rule in the human's own words
rather than by assent alone.* **Both halves of the rule are in their sentence** — the ceiling (*at most one*) and the
floor (*if there is none and one is waiting, it is offered*) — which is the pairing the worker's question separated
into its two rounds.
## Annotation: a manager's relay line that read as self-contradictory

*Filed by the manager against itself, from the human's own words. **Evidence, not an argument.***

**The manager's line**, in the relay carrying node 110's question: *"Nothing is queued behind it; node 108's worker
holds a second question of its own."*

**The human's words**, `verbatim`: *"'Nothing is queued behind it; node 108's worker holds a second question of its
own' doesn't this means that there is a question queued behind ?"*

**What was true, and what the line got wrong.** At the moment it was written the worker had been resumed and had not
yet produced its second question, so nothing was queued and the first clause held. The second clause named a question
that did not yet exist, in the same breath, which makes the line read as contradicting itself. **The distinction
between a question owed and a question written is one the manager was tracking and the human should not have had to
parse.** By the manager's next message the question existed and was queued, and the manager corrected the line then.

**Why it belongs on this node.** The closing line naming what is expected is the check that makes this node's duty
auditable at no cost — the worker's own recommendation rests on it. This instance is that line being written
**accurately about a state that changed one turn later**, which is a third failure mode beside the two already on
this node: not a wrong reading and not a conflated rule, but a true statement of the queue that stops being true
before the human can act on it.

## Retrospective

*The worker's own text, pasted, handed back as the sixth handover part this effort asks for.*

**1. What I had to hunt for.**

- *Why* the one-question ceiling exists. I looked first in the shipped `SKILL.md`'s `## What is in front of the
  human, and when`, which states the rule and carries no trace of its reason. I found it in node 16's answer §1 and
  its `## Interview` attempt 1: two things were asked at once, the human's reply named an option in only one, and the
  manager had to guess. **That reason is what decided the first question.** A worker asked to interpret a shipped
  rule had to go to the record to find the rule's purpose, which is the read the shipped files exist to spare it.
- Whether any resolved node already fixed that a gate holds the channel for its lifetime. One grep of
  `.claude/skills/` for *"in front of the human"* (three hits), then node 16 and node 23 in full. Nothing does.
- The shipped text as it actually stands now. My spawn and my node file both described node 100 as at its gate; it
  had landed by my third round, and its landed sentence *"the report awaits no answer and takes no place in the queue
  above"* is what my second question turned on. Re-reading the file rather than trusting my first read is what caught
  it.

**2. What I read and did not use.** Node 23 almost entirely — the three triggers, the two answer shapes, salvage, the
checker's third outcome, four annotations; only its pre-emption fragment bore on my node, and node 16 restates that.
Most of node 100: four checker runs, five flags, the condition read-back; two sentences of its landed text were what
I needed. The second half of `map.md` — landing policy, dogfood target, review route, the whole fog section and
out-of-scope. `decisions.md` end to end, to pick which nodes to open; two of eighty were relevant.

**3. What would have made this node easier.**

- **The shipped rule not carrying its own reason** is the single biggest cost, above. One clause of *why* beside the
  ceiling in `SKILL.md` would have removed a node-16 read entirely.
- **The spawn named a section of my node file that is not on disk.** I was told to read `## Annotation: a manager's
  relay line that read as self-contradictory`; the file has no such heading. I worked from the manager's two-sentence
  account in the spawn. A spawn that cites a section should either be sent after it is written or quote it inline.
- **The batching node arrived after both questions were asked.** It changed how I wrote the answer — a ceiling plus a
  top-up rather than the number one. Had it come with the first spawn it would have shaped my second question's
  alternatives too, none of which offered a variant over a changed ceiling.
- **A pointer to node 99.** The second instance's cause is a conflation with it, and I reasoned about that boundary
  from the manager's summary and `decisions.md`'s one line rather than from the node. That was enough to see it did
  not move my answer, and it would not have been enough had it.

**4. What was stale, wrong, or contradicted something else.** My node file's `## The manager's note at filing` says
node 100 is at its gate and that starting this node would exceed the effort's target; both were false by the time I
worked, and the spawn repeated the first. Ordinary for an append-only node file, and still the sort of line a worker
reads as current. The annotation named in the spawn and absent from the file, above. Nothing contradicted anything in
substance — the one thing that looks like a contradiction, the shipped *"Three things are not claimants at all"*
coexisting with two further non-claimants named in the same file, is already flag `100.2` and I left it alone rather
than repairing it.

**The manager's note on the retrospective.** *Not a change to anything above.* Its second point is a **manager
defect, and worse than the worker could see**: the annotation it was told to read was not missing from the file
because the manager had not written it yet — the manager *had* written it, into a **stray file at the effort's root**
created by an append run from the wrong directory. Two node files, this one and [Whether the checker re-runs a
condition's own enumerator](110-does-the-checker-rerun-the-enumerator.md), were silently short a section each for
several turns, and this worker is the only reason it was found. Both files have since been made whole and the strays
removed. **Nothing on this graph would have reported it**, which is the part worth keeping: a node file can lose a
section to a mistyped path and read as complete, and no mechanical check covers that.
