# Whether a flag is checked before the human settles it

Type: grilling
Status: claimed

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
- ~~**Whether this is a contract change at all.** It was run once as a declared extension, which is
  [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md)'s open
  question. If a spawn may not extend a contract, this has to land *in* the checker's contract instead.~~
  **Decided by that node, and it is a contract change.** The pass was lawful **as it happened**, under route
  2 — the human's own direction, which the spawn may carry — so nothing about the one run needs excusing. But
  a direction that should bind later workers becomes a contract edit, which is [Off-contract subagent
  output](17-off-contract-output.md)'s existing sentence. This is a standing practice rather than a one-off,
  so **it lands in `expedition-checker/SKILL.md`**. This node is not blocked on any further permission, and
  it needs no licence.

  One thing node 28 hands this node rather than deciding for it: the checker contract's *"That is
  everything"* — the sentence the pass contradicted — is **load-bearing but mis-grounded**. It sits directly
  above the blindfold clause it protects (*"There is a record behind this work… You do not read it"*), so the
  closure guards the blindfold rather than being an arbitrary absolutism. The pass contradicted its
  **letter** while respecting what it guards, the flags having reached the checker stripped of their reason —
  claims about the work rather than record. **The repair is to state the closure as what it guards rather
  than to remove it, and it is one clause in the file this node's answer lands in.** Recorded as flag `28.3`,
  decided by that node's worker alone.

Feeds `expedition-checker/SKILL.md` and the **manager's own skill**, which is where flag-gathering lives.
Sits directly beside [Whether a spawn may override a shipped worker contract](28-spawn-overriding-a-contract.md),
whose answer decides how this one may be delivered.

## Interview

#### Question 1, relayed 2026-10-02

*Pasted as the worker handed it back.*

```
NODE:          Whether a flag is checked before the human settles it (node 30)
ABOUT:         This node decides what checks a flag against the work before the human settles it, when that happens, and what a false flag causes. Your direction at node 26's gate settled that a check happens ("It would be good to have a first check before the human check it. Maybe by simplifing the flag, only giving what was done and not the reason ?"). The answer is due now because node 28 ruled that this practice goes into expedition-checker/SKILL.md, and the manager contract still lists it as open: "Does anything check a flag before the human settles it? Nothing does."
SO FAR:        I read my node, map.md, the decisions-index lines for nodes 26, 34, 366 and 372, the node-26 account of the one trial run, and the relevant sections of the checker, manager, implementation, standing-yes and triage skills.
               - Today, nothing but the agent that raised a flag and the human ever reads it. There are 737 settled lines and 18 outstanding in flags.md (I counted with grep; the figures are not stored anywhere). Under your standing yes, gates auto-approve on a checker PASS. Most flags now reach you only as a line or two in the node closing report, and they settle on whatever you say next. Node 366 settled 237 in one batch, and the triage skill from node 372 proposes batch settling. So an unchecked flag that is false (the work does not do what the flag says) gets settled on a false premise, and nothing would ever catch it. Since the standing yes, that risk has gone up, not down.
               - The trial on node 26 checked five of seven flags. It ran as a separate pass after the checker's outcome. It took 51 seconds and one tool call, and all five came back true. Two flags were left out because they made no claim the working tree could confirm or refute. Holding back the reason cost one wasted question. One flag (26.9) was already covered by the normal check.
               - What already exists and can be reused: the standing yes never covers "a checker's raise, which includes a question a checker hands back beside its outcome". So if a false flag comes back as a question beside the outcome, the gate goes to you with no new standing-yes text. Node 34 already covers a worker disputing a checker finding: the worker gives its reason in GATE PAYLOAD and you settle it at the gate.
               - Only implementation nodes have a checker and a working tree. Flags on grilling or research nodes are judgements about decisions, and nothing in the tree can make them true or false.
               - What I settled myself: "valid" means "true of the work", and never "the call was reasonable". The checker's rule 2 and node 26's own framing already fix that reading, so I am not asking about it.
ASK:           Should the first check be the checker, in the same run, under the design below?
RECOMMENDED:   Yes, as one package:
               (a) Who: the implementation node's checker. Nothing else checks flags.
               (b) Scope: only the flags on the node at its gate. Flags on other kinds of node stay unchecked, because nothing in the tree can make them true or false.
               (c) What it receives: the manager passes each flag's flags.md sentence unchanged, as a seventh given. That sentence is the raising agent's own text, written "for a reader who has not read your node", so nobody re-writes it. That also removes the manager's open scribe-rule conflict for this direction. Since nobody strips the reason, the checker is told to judge only whether what the flag says was done is true of the work, and never whether the call was right.
               (d) When: the checker reaches its PASS or FAIL first and checks the flags afterwards, so they cannot change the outcome.
               (e) Result: for each flag, true, false, or no claim about the work. Only a false flag is reported, as a question beside the outcome with the search that showed it. That takes the gate out of the standing yes through the existing rule, and the worker answers it as it answers any finding (node 34).
               Why the checker: it already has the work open, its searches are reproducible, and the trial cost under a minute. The manager knows the reasons and files flags about its own conduct, so it is not an independent check. A separate pass costs an extra spawn and its own contract.
               Size: about 10 lines in the checker contract, as one given plus one short section. That includes rewording the "six givens above are everything you are given" closing sentence so that it states what it protects, the record being kept unread, as node 28 asked. The manager contract gets about 2 lines in the gate-payload list and loses its open item 2, so the manager contract shrinks.
ALTERNATIVES:  Manager checks flags while assembling the payload: no extra cost, but it is not independent, and it knows the reasons the check is meant to set aside.
               A separate flag-check spawn after the outcome, as in the trial: the cleanest ordering, but an extra spawn per gate and its own instructions to ship.
               The manager strips each flag to "what was done" before handing it over: your original suggestion. It costs a manager re-write per flag and keeps the scribe-rule conflict, and in the trial withholding the reason cost a wasted question.
               A false flag forces a correction round (treated like a FAIL): more machinery, and the condition is met either way.
               A false flag is only marked as a warning in the closing report: cheapest, but under the standing yes the work would be committed before you see it.
               Ship nothing and rely on triage: the trial shows false flags are possible, and batch settling is exactly where nobody would notice them.

RETROSPECTIVE (interim, so far in this attempt):
1. Hunted for: what currently happens to a checker question under the standing yes (found in expedition-standing-yes "What a standing yes never covers"), and the trial run's details (node 26, around "Five of the seven flags").
2. Arrived but not needed: most of map.md (ground rules, the heterogeneous-model note).
3. Would have helped: the node naming the current skill sections it would change (checker "## What you are given", manager item 2 under "What nothing here settles").
4. Stale: the node's "forty-nine flags" count, now 755 lines in flags.md. The node also predates the standing yes, which changes where flags reach the human.
```

#### The human's answer to question 1, 2026-10-02

`verbatim`: *"yes"*

The manager had put the question as "Should the checker do the first check, in the same run, under this design?", closing with "Please answer: "ok for recommended", or name an alternative." The reply "yes" answers that question and names no alternative, so it takes the worker's `RECOMMENDED`, the package (a) to (e).
