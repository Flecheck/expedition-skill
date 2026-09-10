# Whether `map-manager-only.md` gets an admission test, now that it holds the landing section's history

Type: grilling
Status: claimed

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
