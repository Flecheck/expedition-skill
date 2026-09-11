# Whether `map-manager-only.md` gets an admission test, now that it holds the landing section's history

Type: grilling
Status: resolved

Blocked by: 188

## Question

*Surfaced by [node 188](188-move-the-landing-section-out-of-the-workers-file.md)'s worker, and pasted as it wrote
it. Its blocker is node 188, which is resolved, so the edge is satisfied and this node is on the frontier.*

> `map-implementation-rules.md` has an admission test — a line earns its place only where its declared reader would
> act differently for having read it, with a trigger staying and a history going to `map-history.md` (nodes 191,
> 196, and shipped by node 197 for every file of a map). `map-manager-only.md` has never had one applied, and node
> 188 just doubled it by moving in the effort's largest single account-bearing block: four failed rebase attempts
> with two wrong diagnoses, three superseded sandbox accounts, two struck worktree routes, and a struck code-slot
> count. The human has twice asked why history sits in that material. Node 191 settled that **no sweep is owed or
> licensed** — only whoever is already editing a passage applies the test — so nothing will ever reach this by
> accident, and node 188's own condition demanded a byte-identical move and so could not touch it. Two things are
> open and neither is the manager's to settle: whether `map-manager-only.md` states an admission test of its own for
> its one reader, and whether node 191's supersession route is run once over the landing section to bank its history
> in `map-history.md` — which would be the sweep node 191 refused, and is therefore the human's call rather than a
> worker's.

**Blockers, in the worker's words:** *"188."*

## Acceptance condition

**None, and none is owed.** This is a grilling node: what done means is the human's answer.

## The manager's note at filing

*Not a change to anything above.*

**This is the human's own question arriving as a node rather than as a remark.** They asked it twice — first
`verbatim` as *"why is there in map implementation rules stuff that are not rules ?"*, which the manager routed to
[node 200](200-collapse-the-rules-files-two-map-history-statements.md) on their word, and again on being handed node
188's gate. Node 188 answered neither asking: it moved the block without touching a byte of it, so the history the
human noticed is now in a different file, with the same standing and one reader instead of three.

**Why it is grilling rather than implementation.** Node 191 settled that no sweep is owed and none is licensed, so
running the admission test over the moved section is not work any worker may take on its own, and the manager
writing a condition for it would be the manager licensing the sweep node 191 refused. **Both halves are the
human's**: whether the file states a test at all, and whether this one section's history is banked now.

## Interview

### Attempt 1 — the questions put to the human

*Pasted as the worker wrote them, in its own order and its own words. **No answer has arrived**; the payload is
banked here so that a death leaves the worker's work on disk rather than losing it.*

**ABOUT:** You have twice asked why a rules file holds material that is not rules. This decides the two things that
were left open on that: whether `map-manager-only.md` says in its own text what it admits, and whether the history
now sitting in it gets banked once rather than waiting for someone to edit each paragraph.

**SO FAR:** What I read: your node; `map.md`; `map-manager-only.md` and `map-implementation-rules.md` whole; the
`decisions.md` lines for nodes 139, 189, 191, 193, 196, 197, 200; nodes 191, 196, 197 and 152 in full; the shipped
`graph-conventions.md`; and I measured the landing section itself.

**Three facts that changed the shape of this since your node was written.**

**(1) The admission test already binds `map-manager-only.md`, in shipped text, and it names your case explicitly.**
Node 197 has landed. `graph-conventions.md`'s `## Writing the map` now says: *"Each file of the map declares who
reads it, and a line belongs in that file only where the reader it declares — **one kind of worker, or the manager
alone** — would do something differently for having read it while working a node. **How a rule was learned is not
that**: how many attempts it took and what they cost, who was wrong, what the file said before. That material goes
to `map-history.md` … **A trigger is part of a rule and stays; a history is not** … Whoever is already editing a
passage applies the test to that passage: no sweep of a file is owed or licensed by it."* `map-manager-only.md`'s
own first sentence is *"The manager is this file's reader"*, and the manager's contract says to read
`graph-conventions.md` before touching an effort's files — so the test attaches with no word added. That was the
deliberate design: node 191's flag `191.2` chose the shipped general form *instead of* writing a test into
`map-manager-only.md`, and said in as many words that the file *"gets no admission test until the shipped node
lands"*. It has landed.

**(2) So what is missing is not the standard — it is the clean-up, and node 191's stated reason for refusing a sweep
does not hold for this section.** Node 191 refused a sweep on a checkable claim: *"the six nodes queued on this file
are how the file converges."* For `map-implementation-rules.md` that was true. For the landing section it is not. Of
the open nodes on it, node 152 touches one paragraph (and is itself unsatisfiable as written since node 188 moved
the section out from under it), node 160 adds a rule, node 180 will rewrite the sandbox bullets — and the biggest
accounts, including the exact material you pointed at, sit in passages **no open node touches**.

**(3) Measured, so you are not deciding on my adjectives.** The landing section is **16,569 bytes / 128 lines — 49%
of the 34,160-byte file**. It holds **9 struck-through regions, 1,535 bytes**, and **only 2 of the 9 exist anywhere
else** (the code-slot count at one, and *"No branch is ever created or switched"*, both banked in `map-history.md`)
— the other **7 are struck in place with no copy anywhere**, so removing them without banking them first would be a
deletion. Beyond the strikes: 3 *"Superseded"* passages, 8 *"measured"* narratives, *"the manager corrected it
within the hour"*, *"after four failed attempts and two wrong diagnoses"*, and *"it took three rounds of experiment
to state correctly. Two earlier accounts of it in this file were wrong."* My classification puts **~7,010 bytes —
42% of the section — in paragraphs that are wholly or mostly account**; keeping every trigger node 191 protects (the
error strings `could not detach HEAD`, `Could not reset index file to revision`, `unable to unlink old …`,
`Read-only file system`, the `git checkout --detach` instruction, the `/proc/mounts` command) nets roughly **5-6 KB
out, leaving the section around 10-11 KB**.

What I settled on my own authority: that node 197's landed text reaches this file without needing your say-so (I
verified the shipped wording rather than taking node 197's word for it), and that these two questions are
independent — the shipped test binds whichever way Q1 goes, so Q2 does not wait on it.

**Q1. Does the file say anything itself about what it admits**

**ASK:** `map-implementation-rules.md` opens with its own admission test in its own words; `map-manager-only.md`
opens with nothing of the kind, even though the shipped test now covers it. Do you want (a) nothing added, the
shipped test being in force already, (b) one pointer sentence in the opening saying the file's contents are held to
what `graph-conventions.md`'s `## Writing the map` admits, or (c) the test restated locally in full, the way node
196 wrote it into the rules file?

**RECOMMENDED:** **(b), one pointer sentence, ~130 bytes.** It rests on three things. The asymmetry in (a) is a real
cost, not a cosmetic one: a reader comparing the two siblings sees one declaring a test and one declaring none, and
reads the silence as *this file is not under a test* — which is the misreading your original question came from. (c)
is the option I would refuse: node 196 wrote the test locally into the rules file, its own worker reported the
duplication that created, and node 200 then spent a whole node collapsing it — a third statement of one discipline
in this effort's record buys the same defect again. And the pointer is the form this effort has already sanctioned:
node 197's own condition allowed the conventions document's gloss *"at most one clause pointing at `## Writing the
map`"* and nothing else, and your standing rule 2 for writing is exactly this — an item states its current form and
cites what shaped it rather than restating it.

**ALTERNATIVES:** (a) Nothing added — cheapest and defensible, since the test genuinely binds; the price is that the
file reads as untested to anyone comparing it with its sibling.
(c) The test restated in full locally — makes the file stand alone for a reader who reads neither the conventions
document nor `map.md`; buys back the duplication node 200 was minted to remove.

**Q2. Whether the landing section's history is banked once, now**

**ASK:** Node 191 settled that no sweep of a map file is owed and none is licensed, and node 188 moved this section
byte-identical under a condition that forbade touching it — so nothing will reach this material by accident. Do you
license one bounded exception: a single implementation node that runs node 189's supersession route over the landing
section of `map-manager-only.md` and nothing else?

**RECOMMENDED:** **Yes, run it once, scoped to that one section.** The node would bank the 7 unbanked struck regions
and the account-only paragraphs **verbatim** into `map-history.md` under a heading naming the section, keep every
trigger and every operative instruction, and change **no rule that currently binds**. Three grounds. First, node
191's refusal rested on convergence-by-queue, and I checked it: it does not reach the passages carrying the largest
accounts, including the four-failed-rebases narrative you were reading — so this is the rule's own mechanism missing
this section rather than you overriding a rule that is working. Second, the section is 49% of a file whose only
reader is the manager, and the manager's context is this effort's measured scarcity (`map.md` records a
100k-per-node budget against ~200k actual). Third, nothing else is owed you here: you have asked twice and node 188
answered neither asking, because it was forbidden from touching a byte.

**ALTERNATIVES:** Leave it, and let the standing rule reach each passage whenever 152, 160 or 180 edits it — no
exception licensed; the material you pointed at stays indefinitely, since no open node touches it.
Bank only the 7 unbanked struck regions and leave the unstruck accounts — no judgement calls at all, roughly a third
of the saving, and it misses the four-failed-rebases narrative, which is not struck.
Widen it to the whole of `map-manager-only.md`, or to every sibling — that is the sweep node 191 refused, at full
size and with no bound on it.
Fold it into node 152, which needs a fresh acceptance condition anyway and touches the same section — one node
cheaper, but it makes that node's condition carry a demand its subject never weighed, which is the exact failure
flag `191.4` names.

### The human's answer to attempt 1

**Their words, `verbatim`.**

> Q1 ok Q2 ok

**Both take the worker's recommendation**, and each recommendation is quoted here as **the worker wrote it**, not as
the manager renders it.

**Q1 — the worker's recommendation, taken:**

> **(b), one pointer sentence, ~130 bytes.** It rests on three things. The asymmetry in (a) is a real cost, not a
> cosmetic one: a reader comparing the two siblings sees one declaring a test and one declaring none, and reads the
> silence as *this file is not under a test* — which is the misreading your original question came from. (c) is the
> option I would refuse: node 196 wrote the test locally into the rules file, its own worker reported the
> duplication that created, and node 200 then spent a whole node collapsing it — a third statement of one discipline
> in this effort's record buys the same defect again. And the pointer is the form this effort has already
> sanctioned: node 197's own condition allowed the conventions document's gloss *"at most one clause pointing at
> `## Writing the map`"* and nothing else, and your standing rule 2 for writing is exactly this — an item states its
> current form and cites what shaped it rather than restating it.

**Q2 — the worker's recommendation, taken:**

> **Yes, run it once, scoped to that one section.** The node would bank the 7 unbanked struck regions and the
> account-only paragraphs **verbatim** into `map-history.md` under a heading naming the section, keep every trigger
> and every operative instruction, and change **no rule that currently binds**.

**What Q2's answer is, stated plainly because it is unusual.** It is a **licence from the human for a bounded
exception to a rule they have already approved**: [node 191](191-the-rules-file-carries-accounts-rather-than-rules.md)
settled that no sweep of a map file is owed and none is licensed, and this permits exactly one, over
`## Landing an implementation node's work` in `map-manager-only.md` and nothing else. **It does not widen node 191**,
and the manager will say so in whatever node carries the work.

*No divergence: the human took both recommendations as written. Neither answer contradicts anything the worker
advised.*

## Flags

*The worker's own text, pasted. The ids are the manager's bookkeeping and nothing else. **Outstanding** — this is a
grilling node, so its flags reach the human at the pick report that closes it rather than at a gate.*

`225.1` `ASSUMPTION` — **On the one live clause inside a struck bullet.** The bullet the sweep node deletes is
struck in full, but the unstruck sentence after it says *"the commit trailer stays the join key regardless"* — so
the commit trailer `Node: <effort>/<NN>` being the join key is a live fact whose only statement anywhere in the
section sits inside struck text. I decided it survives, and wrote the one-sentence replacement into the acceptance
condition myself rather than leaving the worker to judge it. If the trailer is stated elsewhere in the record, that
replacement is a duplication; if it is not live at all, the sweep node preserves something dead.

`225.2` `ASSUMPTION` — **On the account I kept.** The sentence explaining that the landing policy was added beside
rather than rewritten, *"because node 152 and node 144 hold conditions quoting that paragraph's exact phrases"*, is
an account of how the file came to be arranged and fails the shipped test by its letter. I excluded it from the
removal list because node 152 is open and its condition still quotes that paragraph, so the sentence is what stops a
future editor breaking it. If node 152 is re-conditioned off those phrases, this sentence becomes bankable and
nothing will notice.

`225.3` `ASSUMPTION` — **On the two sub-bullets left byte-identical.** The `**What it hits.**` and `**What it does
not hit, established by experiment rather than inferred.**` sub-bullets carry error strings and measured behaviour
that are the rule, so I left them out of the removal list — but *"established by experiment rather than inferred"*
is history by the test's letter. I traded a few bytes for a bounded edit list with no judgement calls left in it.

`225.4` `ASSUMPTION` — **On where the pointer sentence goes.** I fixed its position in the condition — second
paragraph of the opening, directly below the one declaring the file's reader and necessarily above *"Nothing below
was reworded on the way here"*, which claims a property of everything after it that a new paragraph would falsify.
That is node 196's own placement argument, applied to a different file by me rather than by the human.

## Answer

*Pasted as the worker wrote it.*

**Both halves are settled, and they came apart once the tree was read rather than reasoned about.** The human's
answer, `verbatim`: *"Q1 ok Q2 ok"*, taking both recommendations and neither of the alternatives beside them.

**The first half was already answered by a node that had landed, which is why it is a pointer and not a test.**
`map-manager-only.md` does **not** state an admission test of its own. It does not need one: [node
197](197-ship-what-a-file-of-the-map-admits.md) has landed, and `graph-conventions.md`'s `## Writing the map` now
states the test over *"Each file of the map declares who reads it, and a line belongs in that file only where the
reader it declares — **one kind of worker, or the manager alone** — would do something differently for having read
it while working a node"*, with the trigger-against-history clause and the no-sweep clause beside it.
`map-manager-only.md`'s own first sentence declares its reader, and the manager's contract says to read
`graph-conventions.md` before touching an effort's files, so the test attaches with no word added. That was [node
191](191-the-rules-file-carries-accounts-rather-than-rules.md)'s design, recorded at flag `191.2`: the shipped
general form **instead of** a test written into this file, with the consequence stated there that the file *"gets no
admission test until the shipped node lands"*. It has landed, so the consequence is discharged rather than
outstanding.

**What is added is one pointer sentence and nothing more.** The file opens declaring its reader and says nothing
about what it admits, while its sibling `map-implementation-rules.md` opens with a test in its own words — and a
reader comparing the two reads that silence as *this file is under no test*, which is the misreading the human's
original question came from. A pointer removes the asymmetry and restates nothing. The full restatement was refused
on measured ground rather than on taste: [node 196](196-give-the-rules-file-its-admission-test.md) wrote the test
locally into the rules file, its own worker reported the duplication that created, and [node
200](200-collapse-the-rules-files-two-map-history-statements.md) was then spent collapsing it. A third statement of
one discipline buys that defect a second time.

**The second half is one bounded exception, and node 191's refusal of a sweep stands unchanged.** The human
licensed a single node running node 189's supersession route over `## Landing an implementation node's work` in
`map-manager-only.md` and over nothing else. That is an **exception** to node 191's *"no sweep of a file is owed or
licensed by it"*, not a change to it: node 191's rule binds every other passage of every other file exactly as
before, and nothing here widens it to the rest of this file or to any sibling.

**The exception has a specific ground, and it is a claim of node 191's that stopped being true.** Node 191 refused
the sweep on something checkable: *"the six nodes queued on this file are how the file converges."* For
`map-implementation-rules.md` that held. For this section it does not. Of the open nodes standing on it, node 152
touches one paragraph and is itself unsatisfiable as written since node 188 moved the section out from under it,
node 160 adds a rule, and node 180 will rewrite the sandbox bullets — and the passages carrying the largest
accounts, the four-failed-rebases narrative the human was reading among them, are touched by **none** of them. So
this is the rule's own convergence mechanism failing to reach one section, not the human overriding a rule that is
working.

**Measured, at this node's filing.** The landing section is **16,569 bytes over 128 lines — 49% of the 34,160-byte
file**. It holds **9 struck-through regions totalling 1,535 bytes**, and **only 2 of the 9 exist anywhere else**.
**The other 7 are struck in place with no copy anywhere**, so removing any of them without banking it first would be
a deletion. Paragraphs that are wholly or mostly account come to **~7,010 bytes, 42% of the section**; the fourteen
edits specified come to less than that, because every trigger node 191 protects is kept and one account is kept
deliberately.

**What is kept, and it is the half of node 191's clause that does the work.** Every error string stays — `could not
detach HEAD`, `Could not reset index file`, `unable to unlink old …`, `Read-only file system` — as does the
`git checkout --detach` instruction, the `/proc/mounts` command, every `verbatim` quotation of the human, and every
rule that currently binds. A trigger is part of a rule and stays.

**One account is kept although the test's letter would evict it**, and the reason is a live dependency rather than
sentiment: the sentence *"Added beside the landing policy above rather than rewritten into it, because [node 152]
and [node 144] hold conditions quoting that paragraph's exact phrases"* is how a future editor knows not to reword
that paragraph, and node 152 is still open and still quotes it. **It is a trigger wearing a history's clothes.**

**Two nodes come out of this, and they are sequenced rather than parallel**, both writing `map-manager-only.md`: the
exception node first, the pointer node blocked on it.

**What the worker reported its work invalidates:** `none`, with three near-misses it recorded because each looks like
one — **node 191 is excepted, not contradicted**; **node 191's flag `191.2` is discharged, not falsified**, the
shipped node it waited for having landed; and **node 188 is fulfilled rather than contradicted**, its condition
having demanded a byte-identical move and so being unable to touch the material.

## Retrospective

*Filed by the manager in the same edit that resolves the node. Pasted as the worker wrote it.*

**1. What I had to hunt for.** Three facts, and the expensive one was *whether node 197 had landed*. My node file,
my spawn and the manager's notes all described node 197's shipped statement as a future or as a rule of node 191's —
none said it was live text in `graph-conventions.md` today. I found it by reading node 197's file to the bottom and
then grepping the shipped file to verify the wording rather than trust the node's `## Answer`. **That single fact
inverted Q1**: without it I would have recommended writing a test into the file, which is the option the human would
then have been choosing between under a false premise. Second, *which struck regions are already banked* — nothing
records that, so I diffed the nine against `map-history.md` by substring and found 2 of 9. Third, *whether open
nodes converge on this section* — I had to read node 152 in full and check statuses one by one to establish that
node 191's convergence claim fails here, which is the whole ground the human's Q2 answer rests on. I looked first in
the node file and the spawn for all three; none of them was there.

**2. What arrived in my context that this node did not need.** `map.md` in full, read cold, is the largest item and
about a fifth of it bore. The fourteen other standing preferences bore on nothing I decided. That is the mandatory
read working as designed, so it is not a complaint about `map.md`; it is an argument that **a grilling node whose
subject is one file's contents could be spawned with a named subset**. Second, and this one is avoidable: I read
`map-implementation-rules.md` whole, 12,370 bytes, to learn one thing — the exact wording of the admission test in
its opening. A spawn line quoting that paragraph would have saved the read entirely, and my spawn already quoted
node 188's byte counts, so the shape was there. Third, `decisions.md` I never opened whole; I grepped six node ids
out of it, which is the right access pattern for a 38 KB index and cost almost nothing. Worth saying because the map
lists it as a read-whole file on the human's *"it's small enough"*: **for this node it was not read whole and
nothing was lost.**

**3. What would have made this node easier.** Two things, both in the record rather than in the contract. **The
record does not state which nodes are open on a given passage.** Establishing that node 191's convergence claim
fails for this section — the single load-bearing fact of Q2 — took reading one node in full and statusing thirteen
others. Node files say what they are blocked by; nothing says what they will touch. A one-line `Touches:` on an
implementation node would have answered it in one grep, and it is the same fact a manager needs to sequence two
writers over one file, which this effort's own code-slot bullet already requires it to compute by hand. **And a
shipped node's answer does not say that it shipped.** Node 197 is `Status: resolved` with an approved gate, but
knowing whether its text is *in the shipped file right now* meant opening the shipped file. On an effort whose
subject is the shipped files, that gap is structural: every node that reasons about what the workflow currently says
has to re-verify it the way I did.

**4. What I read that was stale, wrong, or contradicted something else.** One thing, and it is in my own node file:
its `## Question` says `map-manager-only.md` *"has never had one applied"* and lists the two open halves as though
both were live. **The first half was substantially closed by node 197 landing, which happened before this node was
filed.** The node file was pasted from node 188's worker, who wrote it before checking, and the manager's note at
filing repeated the framing rather than testing it. Nothing was wrong to write; it was true when node 191 resolved
and stopped being true when node 197 landed, with no mechanism noticing. That is the same failure mode
`map-manager-only.md`'s own fog item names — *nothing watches a standard that lives outside this repository* — one
step inward, where **the thing unwatched is this effort's own shipped file**.
