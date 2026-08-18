# Whether a flag is checked before the human settles it

Type: grilling
Status: open

## Question

A flag is an agent's record of a judgement it made on its own. Today it goes from the agent that raised it
straight to the human, who is the only reader it ever gets. **Should something check it first, and what
exactly would that something be checking?**

The direction is already the human's, given at [Carry the recorded deltas into the shipped skill
files](26-carry-deltas-into-shipped-files.md)'s gate, `verbatim`:

> For the flags, could we give a summarized version of the flags, with explict instruction to check if they
> are valid. It would be good to have a first check before the human check it. Maybe by simplifing the flag,
> only giving what was done and not the reason ?

So this node is not *whether* — it is *what*, *who*, and *when*.

### The gap, measured

**Forty-nine flags exist and not one has ever been read by anything but the agent that raised it and the
human.** Twenty-two are settled, twenty-seven outstanding. Five were filed by the manager about its own
conduct, which means the party being judged and the party writing the judgement were the same, with no step
in between.

### The manager argued against this and was wrong

Worth recording, because the reason it was wrong is the design point. The manager's position was **no**, on
three grounds: the checker's rule 2 bars a finding that touches neither the acceptance condition nor the
bar; a flag is part of the record, which the checker may not read; and blindness had just bought an
*independent* rediscovery of the same ground on node 26.

The human's refinement — **give what was done and not the reason** — dissolves the second and third at once.
Stripped of its reason, a flag is not the worker's reasoning; it is a *claim about the work*, which is
precisely the kind of thing a checker already checks. What survives is a boundary rather than an objection:

- **Is the claim true of the work?** Checkable, and squarely in remit.
- **Was the call right?** Not checkable, rests on the record, and is the human's alone. Rule 2 bars it.

A flag that is **false** — where the work does not do what the flag says — is a defect nothing detects
today, and the human would settle it on a false premise. That is the concrete harm, and it is what the first
check is for.

### Evidence, from running it once on node 26

The pass was run as a **declared extension** of the checker's contract, after its outcome had already been
given so that nothing it concluded could reach the verdict. Three things came out of it before the results
even arrived:

1. **Some flags make no claim about the work at all.** Two of node 26's seven — one recording how the
   manager assembled a spawn, one recording how the node's scope was set — have no truth-condition in the
   working tree. Nothing a checker reads could confirm or refute them. So a flag-checking step covers
   **some** flags and the design has to say which, or the checker is handed things it cannot answer.
2. **Withholding the reason has a cost as well as a benefit, and it was paid immediately.** On run 2 the
   checker raised a question about the glossary's closing-report clause being narrower than the document's.
   It was not narrower; the author had chosen one phrase deliberately to cover both cohorts, and that
   intent was in the record and withheld. So the checker spent a question on a non-issue — the exact
   failure mode *only what was done, not the reason* invites. The same run's other question was a **real**
   trace failure the manager confirmed. One of two, on the first outing.
3. **Ordering does the work that argument could not.** Running the pass *after* the outcome makes the
   contamination objection vanish without a rule: the verdict is already fixed and cannot be revised by
   what the flag pass finds. Whether that ordering is essential or incidental is for this node.
4. **Sometimes the check already covers the flag, and no pass is needed.** Node 26's flag `26.9` claimed one
   `_Avoid_` clause had been re-grounded and that nothing else about it moved. Run 3 established exactly that
   while measuring the bar — before any flag was put to it, and without being asked. So the flag pass is
   **sometimes redundant**, and whether it is depends on which condition the flag's claim happens to sit
   under. A design that always runs it pays for that; one that never runs it misses the flags no condition
   reaches.

### The same flag travels two ways, and the design must hold both

Minutes after instructing that a flag be **stripped** for the checker, the human instructed that it be
**expanded** for themselves, `verbatim`:

> Also for flags, when asking the user, please explain in more detail what was done and why and the context.
> Idealy I don't have to go into the files to find out what happened and how to respond

So one flag has **three** forms and the manager writes two of them: its capped line in
[flags.md](../flags.md), a **stripped** claim for the checker with the reason deliberately withheld, and an
**expanded** payload for the human carrying exactly the reason the checker was denied. The two are not a
compromise between each other — they are opposites, and each is right for its reader. A checker given the
reason accepts the justification instead of checking the claim; a human denied it cannot answer without
opening files.

That is a constraint on this node's answer rather than a decision inside it: **any design here that
describes only one direction will collide with the other.** It also puts both new forms in the manager's
hands, which is where the scribe rule bites — the manager is not supposed to re-author what a worker wrote,
and both of these are re-authorings of a worker's flag for a specific reader. Recorded as an annotation on
[Human review of landed code](20-human-code-review.md), whose gate payload the expanded form belongs to.

### What the answer has to decide

- **Who.** The checker is the obvious actor and may be the wrong one — it is blind by design, and a flag's
  truth-condition sometimes sits outside the work. A separate reader with a narrower remit is the
  alternative.
- **When.** Before the outcome, after it, or as its own step. The node-26 run used *after*, deliberately.
- **What "valid" means.** The proposal here is *true of the work*, and that reading needs to be written
  down, because *valid* will otherwise be read as *reasonable* by whoever implements it.
- **Who strips the flag.** Someone has to write the what-was-done version. The manager holds both halves
  and is the obvious author — which makes it the manager summarising a worker's claim so a third party can
  check it, and the scribe rule says the manager does not re-author what a worker wrote.
- **What a false flag does.** It is not a `FAIL` — the acceptance condition is met either way. Whether it
  blocks the gate, reaches the human as a marked warning, or goes back to the worker is undecided.
- **Whether this is a contract change at all.** It was run once as a declared extension, which is
  [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md)'s open
  question. If a spawn may not extend a contract, this has to land *in* the checker's contract instead.

Feeds `expedition-checker/SKILL.md` and the **manager's own skill**, which is where flag-gathering lives.
Sits directly beside [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md),
whose answer decides how this one may be delivered.
