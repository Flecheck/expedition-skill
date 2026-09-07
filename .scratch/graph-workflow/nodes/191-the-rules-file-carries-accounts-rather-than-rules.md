# `map-implementation-rules.md` carries accounts of what happened, not only the rules its title names

Type: grilling
Status: resolved

Blocked by: none

## Question

*The human's, raised while reading the file at node 184's gate. Their words are below and the framing around them is
the manager's, marked as the manager's.*

**The human's words, `verbatim`:**

> I am confused, why is there in map implementation rules stuff that are not rules ? Like explaining what it was
> before the file existed and explaining stuff like "discovered on first use** and recorded here so no later checker
> re-derives it, on the same ground as the bar's commands above. Two checker runs spent their largest single cost
> finding this, and one of them nearly reported the prose standard absent". It wasn't introduced by this commit but
> it's not what I expected

**The line they selected** is in the review-route paragraph of
[`map-implementation-rules.md`](../map-implementation-rules.md), and it is not the only one of its kind: the landing
section carries the account of node 143's four failed rebases and two wrong diagnoses, the account of the manager
correcting itself *"within the hour"* on node 169's worktree, and several *"measured at"* narratives.

**The file forbids this in its own second paragraph**, `verbatim`: *"The account behind a line here is in
`map-history.md`, as it is for a line in `map.md`."* And the **four standing rules for writing**, held at the bottom
of that same file and binding on every prose deliverable of this effort, rule 2: *"An item states its current form
and cites the nodes that shaped it; it does not restate what they hold."*

**The selected account is also duplicated.** The same fact — two checker runs spending their largest single cost on
the review route — stands in `map.md`'s standing preference on resuming an agent, where it is the **ground** for the
human's own rule that a checker is resumed rather than respawned. There it is load-bearing. In the rules file it is
evidence quoted a second time beside a rule it is not the ground for.

**How it got there, and why it is structural rather than a slip.** [Node
140](140-move-the-implementers-and-checkers-material-out-of-the-map.md) moved the implementer's and checker's
material out of `map.md` in one **verbatim** bulk move, carrying out [node
138](138-where-the-rules-a-checker-is-held-to-live.md). The file records the property that was chosen: *"Nothing
below was reworded on the way here"* — stated so plainly that it must warn a reader that an *"above"* in this file
may point at a paragraph in `map.md`. A verbatim move deletes nothing, so it needs no exception to the never-delete
rule and no judgement about any single paragraph; that was the point. **The accounts rode along, because judging
them one at a time was exactly the cost the move was designed to avoid.**

**And no sibling inherited an admission test.** [Node 136](136-the-map-has-grown-back-what-node-59-saved.md) bounded
`map.md` with two things: an admission test over its readers — *what **every** worker can act on* — and a soft
target on each item's size. That test is what created these sibling files. **None of them was given a test of its
own.** Measured at this node's filing: `map.md` 29,880 bytes, `map-implementation-rules.md` 25,911,
`map-history.md` 110,986.

## What is open

1. **Does this file get an admission test of its own, and what is it?** Node 136's *"what every worker can act on"*
   does not transfer unchanged, this file having exactly two readers by design. The candidate is *what an
   implementation worker or its checker must act on to work a node* — which would reject every account.
2. ~~**Is relocating an account to `map-history.md` a move under the never-delete rule, or does each one need the
   human's say-so?**~~ **Handed to [node 189](189-where-the-never-delete-rule-stops.md), which already held the
   never-delete rule's scope, and struck here so that two workers do not interview the human on one question.** The
   human has since said, `verbatim`: *"I don't think there should a be a never delete rule on the rules. They can
   change."* Their words are banked on node 189 with the manager's note on what has already been done with them.
   **A worker on this node does not put the never-delete rule's scope to the human** and takes node 189's answer as
   a given once it exists; what stays here is the mechanism question — whether relocating text to `map-history.md`
   paragraph by paragraph, on a worker's judgement, is the same act as node 59's and node 140's declared bulk moves.
3. **Whether the account is sometimes load-bearing and must stay.** The landing section's node 143 narrative ends in
   an operative instruction — *"read `git checkout --detach <target>` rather than the rebase's summary when it fails
   again"* — so a test that rejects accounts wholesale would take that with it.
4. **Whether the same test reaches the other siblings**, `map-manager-only.md` among them, or whether this is one
   file's repair.
5. **Whether this is [node 70](70-pruning-a-long-running-map.md)'s question.** Node 70 is pruning `map-history.md`,
   the destination; this is what should never have reached the working file in the first place. They meet at the
   same rule from opposite sides.

## The manager's note at filing

*Not a change to anything above.*

**The manager has taken no route and repaired nothing.** The file is untouched at this node's filing.

**The manager owns part of this.** It has appended accounts to this file itself over the last several nodes — the
node 175 amendments and the self-correction beside them are the manager's own text, and each is an account of what
happened rather than a statement of current form. The bulk move explains what was inherited; it does not explain
what was added since.

**Node 149 is open on the same file** and states the prose standard's demands in it; whether that node's worker
meets this material is not settled here.

## Interview

### Attempt 1

**The worker's payload carried one question**, having collapsed the node's five open items into a single `ASK` after
the historical reading turned up what it called a decisive fact: that [node
138](138-where-the-rules-a-checker-is-held-to-live.md) foresaw exactly this and said the review route's operative
list should be *"separated from its story"*, and that [node
140](140-move-the-implementers-and-checkers-material-out-of-the-map.md)'s condition then required the paragraph to
move *"unchanged in wording"*, so the story rode along. **Nobody chose to keep it; a condition kept it.**

**The human's reply, `verbatim`.**

> 191 ok, I think it should be in graph conventions also

**The option `ok` takes**, quoted from the worker's own payload and attributed to the worker:

> **RECOMMENDED:** Give the file the test its title implies, as two sentences in its opening:
>
> > **What this file holds.** A line belongs here only where an implementation worker or its checker would do
> > something differently for having read it while working a node. How a rule was learned is not that — attempt
> > counts, what a run cost, who was wrong and for how long, what the file said before, when the manager corrected
> > itself — and it goes to `map-history.md`, the citation the line already carries standing in its place.
>
> Plus one clause that decides the hard case: **a trigger is part of a rule and stays; a history is not.**

***The manager's note.*** **Not a divergence, and it takes none of the five alternatives.** The worker also named
**two consequences it would carry *"unless you say otherwise"*** — that material failing the test is **moved** to
`map-history.md`, and that the test is applied by whichever worker is already editing that paragraph and **never as
a sweep**. The human said nothing otherwise, so both stand as the worker wrote them.

***The manager's note on the second half of the reply.*** **It is an addition rather than an answer, and it reaches
past what the worker asked.** The payload put no question about shipping at all; the human's own words extend the
test to the shipped `graph-conventions.md`. **The manager has not read it as settling how much ships or in what
form** — that went back to the worker, which holds the interview — and records only that the direction is theirs
and that its subject was not in front of them when they gave it.

## Answer

*Pasted as the worker wrote it.*

> **The file gets an admission test of its own, and it is a reader test rather than a ban on narrative.** The
> human's answer, `verbatim`: *"191 ok, I think it should be in graph conventions also"* — taking the recommendation
> put to them and none of the five alternatives offered beside it.
>
> **The test, as it goes into the file's opening:**
>
> > **What this file holds.** A line belongs here only where an implementation worker or its checker would do
> > something differently for having read it while working a node. How a rule was learned is not that — attempt
> > counts, what a run cost, who was wrong and for how long, what the file said before, when the manager corrected
> > itself — and it goes to `map-history.md`, the citation the line already carries standing in its place.
>
> **And the clause that decides whether an account is ever load-bearing — open question 3, and the part everything
> else hung on:** *a trigger is part of a rule and stays; a history is not.* An error string, a symptom, or the
> condition under which a rule fires is how its reader knows the rule applies, so it is the rule rather than an
> account of it. Worked on the two cases that made the question hard:
>
> - The landing section's rebase paragraph **keeps** *"`git rebase` reported only `could not detach HEAD`; the
>   underlying `git checkout --detach` reports the real cause"* and **loses** *"after four failed attempts and two
>   wrong diagnoses"*. The operative instruction a manager acts on — *"read `git checkout --detach <target>` rather
>   than the rebase's summary when it fails again"* — was never at risk, and the wholesale-rejection test that would
>   have taken it is refused.
> - The line the human selected **loses** *"Two checker runs spent their largest single cost finding this, and one
>   of them nearly reported the prose standard absent"*, and the rule beside it does not change.
>
> **Two mechanisms came with the recommendation as consequences, were not contradicted, and stand.** Material that
> fails the test is **moved** to `map-history.md` — whether it may instead be removed plainly is [node
> 189](189-where-the-never-delete-rule-stops.md)'s and is settled there, not here. And the test is applied by
> **whichever worker is already editing that paragraph, never as a sweep**: it binds every write from now, and no
> node exists or is wanted to walk the file repairing paragraphs nobody is otherwise touching. That is the reading
> of the human's *"Let's stop doing wrong things now"* — a standard that stops the accumulation, with the clean-up
> riding work already queued.
>
> **The mechanism reaches both cases the human pointed at, which is checkable rather than hoped for.** The
> review-route story sits in a paragraph [node 190](190-the-rules-file-states-one-list-twice.md) rewrites by its own
> clause 2; the landing section's rebase and *"measured at"* narratives sit in the section [node
> 188](188-move-the-landing-section-out-of-the-workers-file.md) moves. Neither needs a sweep, and the six nodes
> queued on this file are how the file converges.
>
> **Why this was a hole and not a slip, established rather than argued.** [Node
> 138](138-where-the-rules-a-checker-is-held-to-live.md), which decided this file should exist, said in as many
> words that the review route's operative list should be *"separated from its story — the part recording that two
> earlier checkers burned their biggest cost finding these standards"*, and that the story should go to the manager
> or to `map-history.md`. That is the exact sentence the human selected. [Node
> 140](140-move-the-implementers-and-checkers-material-out-of-the-map.md) then carried the move out under an
> acceptance condition demanding that paragraph move *"unchanged in wording"*. **Nobody chose to keep the story; a
> condition kept it** — the same pathology as the chain 144 → 169 → 184, one link earlier and on content rather
> than on scope.
>
> **The test is not new; its scope was.** Node 42's test — *"a standing constraint true of any node's work, rather
> than an account of what happened"* — already stands in this file, and the file says in its own words that it
> bounds one block and not the file: *"That test is what keeps the rest of this file out of the block."* This node
> **does not** widen node 42's test, which was authored for what may travel to a blind checker and would evict the
> manager's landing instructions with it. It states a second test, over the file's two declared readers, in the
> shape [node 136](136-the-map-has-grown-back-what-node-59-saved.md) gave `map.md`.
>
> **It ships, by the human's own unasked addition**, `verbatim`: *"I think it should be in graph conventions also"*.
> No question about shipping was in front of them, so the direction is theirs and its form is this node's. **What
> ships is the discipline's shape and not this effort's wording.** `graph-conventions.md`'s `## Writing the map`
> already says a map file's items are current statements citing the nodes that shaped them, and that the account
> belongs in `map-history.md`; what it does not say is **what a map file admits at all**, nor does it distinguish a
> trigger from a history. Those two are what ship, stated over **the reader each map file declares** rather than
> over `map.md` alone — which is where the sentence attaches to [node
> 194](194-ship-where-the-never-delete-rule-stops.md)'s clause 3, that node already widening `## Writing the map`
> and `### Change the map` from `map.md` to its siblings that state current rules. So the shipped node runs after
> 194 and is blocked on it.
>
> **Open question 4 — whether the test reaches the other siblings — is answered by the shipped form and not by this
> node editing them.** Once the shipped discipline is stated over the reader a map file declares,
> `map-manager-only.md` is reached by it without being named, and so is any later sibling. So this is neither one
> file's repair nor a five-file sweep: the general form ships once and each sibling inherits it.
> `map-manager-only.md` is not edited by any node this answer mints.
>
> **Open question 5 is not node 70's question.** [Node 70](70-pruning-a-long-running-map.md) prunes
> `map-history.md`, the destination, and asks what may leave the record entirely; this asks what may enter the
> working file. Different file, different act, different actor. No edge between them.

**What the worker reported its work invalidates:** `none`, with two near-misses it recorded because each looks like
one. In its words: *"**Node 138 is fulfilled rather than contradicted.** Its recommendation that the review route's
story be separated from its operative list was never carried out — node 140's condition overrode it — and this
answer restores it."* And: *"**Node 42's test is untouched.** This answer states a second test rather than widening
node 42's."*

## Flags

*All four are the worker's own text, pasted. The ids are the manager's bookkeeping and nothing else.*

`191.1` **· settled** `ASSUMPTION` — **On the node 70 boundary.** I settled open question 5 myself rather than
spending a human question on it: node 70 governs what leaves `map-history.md` and this node governs what enters
`map-implementation-rules.md`, so they touch one preference from opposite sides without overlapping in file, act or
actor. I minted no edge between them and reported none. If they are one question, the two conditions below are
written against the wrong boundary.

`191.2` **· settled** `ASSUMPTION` — **On the siblings.** I settled open question 4 myself, and only because the
human's shipping addition made a general answer available: rather than write a test into `map-manager-only.md`, the
shipped discipline is stated over the reader each map file declares, so every sibling inherits it from one
sentence. The human named `graph-conventions.md` and named no sibling, so the reach across siblings is mine. The
consequence is that `map-manager-only.md` gets no admission test until the shipped node lands, and no node edits
it.

`191.3` **· settled** `ASSUMPTION` — **On what *"in graph conventions also"* reaches.** No shipping question was in
front of the human, so I read their addition on two judgements of my own. First, that what ships is the
discipline's **shape** and not this effort's wording — a shipped file names no effort and no node, so the sentence
had to be rewritten over "the reader a map file declares" rather than over an implementation worker and its
checker. Second, that it belongs in `## Writing the map` and not in the `## The seven files` gloss for
`map-implementation-rules.md`; stating it in both is the duplication defect node 190 exists to repair, so the
shipped condition below forbids it.

`191.4` **· settled** `ASSUMPTION` — **On not amending node 194's condition.** The manager offered folding the
shipped half into node 194's open condition instead of minting beside it. I minted beside it. The two subjects
differ — 194 settles how superseded text leaves a map file, this settles what enters one — and node 194's condition
was written by node 189's worker, so adding a demand its author never weighed is the same failure my own finding
names, a condition carrying more than its worker was briefed for. The cost I accepted is a fifth node queued
serially on a congested 26.6 KB file. **This is cheap for the manager to overrule**: if it folds the shipped node's
clauses into 194 instead, nothing in this answer changes.

***The manager's note on `191.4`.*** **The manager has not overruled it.** It offered the fold and the worker
declined it with a reason that names the manager's own recurring failure mode — a condition carrying more than its
author weighed — so the offer is withdrawn rather than pressed. The fifth node is [node
197](197-ship-what-a-file-of-the-map-admits.md).

***The manager's note.*** **All four flags are settled by the human's answer at this node's own interview**, that
being the first human moment this node's close reached.
