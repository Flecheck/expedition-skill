# Where the never-delete rule stops

Type: grilling
Status: resolved

Blocked by: none

## Question

*Surfaced by [Carry intra-node question batching into the glossary's grilling entry](177-carry-question-batching-into-the-glossarys-grilling-entry.md)'s worker, and pasted as it wrote it.*

> **In the record: state where the never-delete rule stops.** It is the one rule I had to settle by inference, it
> applies to every edit of every shipped file, and it will be re-derived by every worker who edits one. One clause in
> the standing preference — *graph files, not shipped files* — closes it permanently.

**Its full account, in the same worker's words:**

> Whether the never-delete rule reaches a shipped file governs the shape of every edit to `CONTEXT.md` and nothing
> states it. `map.md`'s standing preference says *"when any file in the graph is edited"* and then names *"a node or
> this map"* — which is where I looked first, and it does not answer whether a shipped file counts. I settled it from
> precedent instead: node 133 deleting plainly from a shipped contract at `4000830`, and node 126's own landed change
> deleting the same sentence. **Two node files read to establish a rule that could be one clause in `map.md`.**

## The manager's note at filing

*Not a change to anything above.*

**This is [flag `177.3`](177-carry-question-batching-into-the-glossarys-grilling-entry.md)'s subject.** The flag
records that the worker deleted rather than struck, on inference; this node is where the inference is confirmed or
overturned by the party that can.

**Three landed commits already assume the answer.** Node 133 (`4000830`), node 126 (`8cc9b79`) and node 177's
uncommitted work all delete plainly from shipped files. **So the question is not open in practice and is open in the
record** — which is the shape that produces a worker re-deriving it each time.

**Why this is the human's and not the manager's.** The never-delete rule is a standing preference of theirs, and its
scope is theirs to state; the manager writing *graph files, not shipped files* into the map would be settling a
question about the human's own rule on its own judgement.

## Banked before this node was started

*Written at the moment the human spoke, before any worker held this node. Their words are `verbatim` and everything
around them is the manager's.*

> I don't think there should a be a never delete rule on the rules. They can change.

**They said it while reading [`map-implementation-rules.md`](../map-implementation-rules.md)** at node 184's gate,
having asked why that file carries accounts of what happened rather than rules — the subject of [node
191](191-the-rules-file-carries-accounts-rather-than-rules.md), minted the same minute.

**It cuts along a different axis from the one this node asks about.** This node asks whether the rule reaches a
**shipped** file, a question about a file's *location*. Their answer is about a **rule statement**, a question about
what a piece of text *is* — and a rule statement can sit in a graph file, which is exactly where the one they were
reading sits. So the two cuts cross rather than nest, and a worker on this node has both to place.

**What the manager has already done with it, so that it is not discovered later as a silent act.** It amended clause
2 of [node 184](184-the-bar-and-the-standards-are-two-different-lists.md)'s live acceptance condition, which
imposed strike-in-place on that same file, and recorded the judgement that their words reach that clause as flag
`184.3`. **Nothing in `map.md` was changed**: the standing preference itself stands unedited, because its scope is
what this node settles.

**One thing the manager notes and does not settle**, its own and marked as such: the standing preference already
carries an escape clause — *"Information leaves a file only when it is clearly wrong or the human asks for it
gone."* Whether what they said is that clause being invoked as a standing direction, or a narrowing of the rule
itself, changes what gets written and is not the manager's to pick.

## Interview

### Attempt 1

**The worker's payload carried three questions**, numbered `Q1`, `Q2` and `Q3` under the batching rule [node
126](126-carry-question-batching-into-the-grilling-contract.md) landed as `8cc9b79`.

**What the worker settled without asking, and the manager records rather than asserts.** The question this node was
minted for — whether the rule reaches a **shipped** file — it closed from the record alone, finding the answer in
three independent places and calling it a finding rather than a judgement. In its words: the rule's own text says
*"when any file **in the graph** is edited"* and the phrase after it is an illustration two workers read as an
exhaustive list; `graph-conventions.md` already states it flatly and correctly; and at [node
42](42-checker-spawn-carries-ground-rules.md) a sixth ground rule saying exactly this was offered and struck as
`REDUNDANT` on the recorded ground that the rule is already scoped to graph files. **So flag
[`177.3`](177-carry-question-batching-into-the-glossarys-grilling-entry.md)'s inference was right and the three
commits that deleted plainly from shipped files were all correct.**

**One thing it settled on its own authority and offered for overturning**, in its words: *"your words are a
narrowing of the rule rather than the rule's existing escape clause being invoked once. Ground: if 'superseded'
counted as 'clearly wrong', every strike-through in this record would qualify and the rule would be empty."* The
human did not overturn it.

**The human's reply, `verbatim`.**

> Q1 ok Q2 ok Q3 ok

**The three options it takes**, each quoted from the worker's own payload and attributed to the worker.

> **Q1 RECOMMENDED:** It moves. … *"what that protects is the reader of a rules file, who must never meet a rule
> that no longer binds. A move satisfies that completely and loses nothing. It also needs no new machinery: `map.md`
> itself already works exactly this way — its superseded items are moved out to `map-history.md`, not struck in
> place — and the rules file only differs because it was bulk-moved out of `map.md` in one piece and the
> strike-in-place habit rode along with the text."*

> **Q2 RECOMMENDED:** The text, not the file. *"Text that states a live rule … is replaced when it changes. Text
> whose job is to record what happened — a node's answer, a line in the decisions index, a flag — keeps
> strike-in-place and is never replaced. … your reason is a property of rules rather than of files, and rule
> statements move between files constantly here."*

> **Q3 RECOMMENDED:** It ships. *"Shipping the flat rule without the boundary will reproduce, on every future
> effort, the exact defect this node exists to close. I am recommending against your map's own default here, which
> is why I am asking rather than assuming."*

***The manager's note on Q3.*** **Not a divergence from the worker, and a departure from the map's standing
default.** The worker said in as many words that it was recommending against that default; the human took the
recommendation, so the default is overridden here by their own word rather than by anyone's inference. The manager
records that the default itself is untouched and that this is one answer against it, not its repeal.

***The manager's note on Q1, which the manager had flagged as bearing on work already done.*** It had told the
human that its amendment to [node 184](184-the-bar-and-the-standards-are-two-different-lists.md)'s condition took
Q1's *plain deletion* alternative rather than its recommendation, and that a `Q1 it moves` answer would leave that
work as the one piece not following the rule. **That turns out not to bite, and node 184's checker established why
before the answer arrived**: everything node 184's correction round removed was text that work had itself written
in an unlanded, uncommitted state, and *"nothing that ever landed was deleted, so there was nothing to bank in
`map-history.md`."*

## Answer

*Pasted as the worker wrote it.*

> The never-delete rule stops in two places, and the two cuts compose rather than compete. The first is about
> **where a file sits**; the second, settled here for the first time, is about **what a piece of text is**.
>
> **First cut — the rule reaches the graph's own files and nothing else.** It governs `map.md` and its siblings,
> `decisions.md`, `flags.md`, and the files under `nodes/`. It has never reached a file the workflow ships, and it
> does not reach product code. **This was already true and already the human's, in three places, none of which is
> where a worker looks**, which is why two workers re-derived it from commits instead:
>
> - the preference's own words in `map.md` say *"when any file **in the graph** is edited"*, and the phrase that
>   follows it — *"a node or this map"* — is an illustration that has twice been read as an exhaustive list;
> - the shipped `graph-conventions.md` already states it correctly and flatly: *"**No edit deletes.** When any
>   **graph file** changes…"*;
> - at [node 42](42-checker-spawn-carries-ground-rules.md) a sixth ground rule saying in as many words that the
>   shipped skill files are not the map and may be modified was **struck as redundant**, on the recorded ground that
>   the preference is already scoped to files in the graph.
>
> So the three landed commits that delete plainly from shipped files — node 133's `4000830`, node 126's `8cc9b79`,
> and node 177's work — were all correct, and **flag `177.3`'s inference is confirmed rather than overturned.** This
> half was settled from the record and never put to the human.
>
> **Second cut — inside the graph's files, the rule reaches what records what happened and not what states a rule.**
> The human's words, `verbatim`, said while reading [`map-implementation-rules.md`](../map-implementation-rules.md)
> at node 184's gate:
>
> > I don't think there should a be a never delete rule on the rules. They can change.
>
> - **Text that records what happened is struck in place and never removed.** A node's `## Answer`, a line in
>   `decisions.md`, an entry in `flags.md`, an `## Interview` attempt, a `## Review` round. This is the rule exactly
>   as it always was.
> - **Text whose job is to state a rule that currently binds is replaced by its current form.** The ground rules,
>   the four standing rules for writing, `map.md`'s standing preferences, the landing policy's operative
>   instructions. **It is replaced and not struck**, so a reader of a working file never meets a rule that no longer
>   binds — which is the whole of what *"They can change"* protects.
> - **Nothing is lost when it is replaced.** The superseded text is appended **verbatim** to `map-history.md` under
>   the heading mirroring the section it came from, struck-through text staying struck through. This is the existing
>   `### Change the map` procedure and needs no new machinery: **`map.md` has always worked this way.**
>   `map-implementation-rules.md` differs only because [node
>   140](140-move-the-implementers-and-checkers-material-out-of-the-map.md) bulk-moved it out of `map.md` in one
>   piece and the strike-in-place habit rode along with the text.
>
> **The carve-out follows the text, not the file.** A file-scoped exemption would break the moment a rule statement
> moved file, which has happened four times on this effort (nodes 59, 139, 140, 144). It is also the cut [node
> 42](42-checker-spawn-carries-ground-rules.md) already owns — *"a standing constraint true of any node's work,
> rather than an account of what happened"* — so this reuses a test the human has already accepted rather than
> inventing one.
>
> **The boundary ships.** It goes into `graph-conventions.md`, which is the file that states *"no edit deletes"* for
> every effort and which already carries the map-to-history move as shipped mechanism. This departs from `map.md`'s
> standing default that a rule reaches a shipped file only where the human says so — they were asked, and they said
> so. The ground: a workflow that ships the flat rule without its boundary reproduces, on every future effort, the
> defect this node exists to close.
>
> **Two boundaries this answer does not cross.** `map-history.md`'s own contents are outside it — that file is the
> record, its text is never replaced, and what may be pruned from it is [node 70](70-pruning-a-long-running-map.md)'s.
> And whether relocating an *account* out of a working file is a worker's judgement or needs declaring is [node
> 191](191-the-rules-file-carries-accounts-rather-than-rules.md)'s remaining mechanism question, which this answer
> supplies the rule for and does not perform.

**What the worker reported its work invalidates**, pasted as it wrote it:

> **[Node 64](64-conventions-say-how-the-map-is-written.md)** — one sentence of what it landed is now false. Its
> `## Writing the map` section produced the shipped claim that `map.md` *"is the one file whose superseded text is
> also moved rather than left in place"*, written when the graph had five files and `map.md` had no sibling holding
> rules. It now has two, and their superseded rule statements move the same way. **The rest of node 64 stands** —
> the current-statement/account split, the verbatim-move property, and the `### Change the map` procedure are all
> what this answer builds on rather than displaces.
>
> **Not invalidated, and worth saying so.** Flag `177.3` is **confirmed**: its inference that the rule stops at
> shipped files was correct, and this answer supplies from the record the statement it had to build from two
> commits. And node 184's amendment, which took plain deletion where this answer says move, turns out not to
> diverge — its checker established that everything that round removed was text the same unlanded work had itself
> written, so nothing that ever landed was deleted and there was nothing to bank.

## Flags

*All three are the worker's own text, pasted. The ids and links are the manager's bookkeeping and nothing else.*

`189.1` **· settled** `ASSUMPTION` — **I settled the question this node was minted for rather than asking it.** The
node holds that the rule's scope is the human's to state and not the manager's. I judged that they had already
stated it: `map.md`'s preference is scoped by its own words to files *in the graph*, the shipped conventions file
says *"any graph file"* outright, and at node 42 a proposed ground rule saying the shipped files may be modified was
struck as **redundant** — a decline on the ground that it was already true, not that it was false. So reporting it
is a finding and not a substitution of my judgement for theirs, and their time went to the part the record could not
answer. The one thing I could not pin: the attribution of node 42's quoted sentence is ambiguous in
`map-history.md` between the manager offering and the human declining, so I rested this on the **decline and its
recorded ground** rather than on the quote.

`189.2` **· settled** `ASSUMPTION` — **I read the human's words as narrowing the rule rather than invoking its
escape clause, and did not ask which.** The preference already says *"Information leaves a file only when it is
clearly wrong or the human asks for it gone."* Ground for reading it as a narrowing: if *superseded* counted as
*clearly wrong*, every strike-through in this record would qualify and the rule would be empty; and an ask under the
escape clause names specific information, where theirs names a class of text and gives a reason of principle. It was
offered to them as an explicit alternative under Q1 — *one-off, settling node 184 and writing nothing standing* —
and they took the recommendation instead, so the reading stood without being overturned rather than being confirmed
in as many words.

`189.3` **· settled** `ASSUMPTION` — **I placed `map-history.md` on the record side of the cut and kept this answer
off it.** A worker reading *"text that states a rule is replaced"* could start replacing rule text inside
`map-history.md`, which would destroy the destination the same answer sends text to. So the cut is drawn by a text's
**job in the file it sits in**: `map-history.md` holds only superseded text by construction, so nothing in it states
a rule that currently binds and nothing in it is ever replaced. What may leave that file at all is node 70's,
untouched here.

***The manager's note.*** **All three are settled by the human's answer at this node's own interview**, that being
the first human moment this node's close reached.

## Annotation: this node misattributed the rule, and the human corrected it

*Filed by the manager against itself, after this node resolved.*

**The human's words, `verbatim`:**

> I wasn't the one making the no delete rule, it was done by you but it's not a bad idea, which is why I approved it.

**What this node said, and it is the manager's own text:** *"The never-delete rule is a standing preference of
theirs, and its scope is theirs to state; the manager writing `graph files, not shipped files` into the map would
be settling a question about the human's own rule on its own judgement."* **That premise is wrong.** The rule is
the workflow's own, approved by the human rather than authored by them.

**The map's text is the evidence and the manager should have read it before asserting.** Every other standing
preference in [`map.md`](../map.md)'s list carries the human's words marked `verbatim`; the bullet beginning
`**An in-place update never deletes.**` carries none and cites no node. The one place
[`map-history.md`](../map-history.md) records them speaking near it is a **sixth ground rule offered by the manager
and declined by them** — a decision about the rule's *scope*, which is what made it look like the rule's origin.

**What survives the correction and what does not.** The node's *finding* stands untouched: the rule's location
boundary was already stated in three places, and the text-job boundary is what the human settled here. What does
not stand is the ground this node gave for asking them at all. **Asking was still right** — they approve and
overturn this workflow's rules, and they did both here — but the reason recorded was the wrong one.

**Where else it propagated.** [Node 70](70-pruning-a-long-running-map.md)'s payload put it to them as *"your oldest
standing rule on this effort"*, and the manager relayed that wording without catching it. That worker is live and
has been told.
