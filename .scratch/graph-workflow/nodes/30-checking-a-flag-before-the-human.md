# Whether a flag is checked before the human settles it

Type: grilling
Status: resolved

## Answer

The implementation checker checks each flag's index sentence, after its outcome, only for truth about the work. A false flag returns as a question, which takes the gate out of a standing yes.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. It surfaced [node 379](379-ship-the-checkers-check-of-a-nodes-flags.md), which ships the answer. Its `INVALIDATIONS` narrow node 26 and extend node 42; the manager notes them here and edits neither. Flags 30.1, 30.2, 30.3, 30.4 settle at the node closing report.

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

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      Whether a flag is checked before the human settles it (node 30)
ANSWER:        **The implementation node's checker makes the first check, in the same run as its outcome. It checks the flags the node holds at its gate, and it checks only whether each one is true of the work.** The human answered "yes" to the recommended package, and the five parts below are that package.

               (a) **Who.** The checker of an implementation node. Nothing else checks flags. The manager is not independent of the flags, since it holds their reasons and files flags about its own conduct. A separate pass would cost an extra spawn and a contract of its own.
               (b) **Scope.** The flags the node holds when its check runs. Flags on grilling, research, prototype and precondition nodes stay unchecked: they record judgements about decisions, and nothing in a working tree makes them true or false.
               (c) **What the checker receives.** The flag's sentence from `flags.md`, as the raising agent wrote it, with the flag's id and without the link to its node. Nobody rewrites it, so the manager re-authors nothing. That settles, for the checker's direction, the manager contract's open question about checking flags. The scribe-rule conflict over the fuller form put to the human stays open. Nobody strips the reason, so the checker is told to judge only whether what the flag says was done is true of the work, and never whether the call was right. That is what "valid" means here.
               (d) **When.** The checker reaches its `PASS` or `FAIL` first and checks the flags afterwards. Nothing it finds about a flag changes the outcome.
               (e) **What a false flag does.** For each flag the checker establishes one of three things: it is true, it is false, or it makes no claim about the work. Only a false flag is reported. It goes under `QUESTIONS:` beside the outcome, with the search that showed it false. This uses rules already shipped. A question a checker hands back is never covered by a standing yes, so the gate goes to the human. A checker's question is something it found, so the worker fixes the work or the flag, or says in `GATE PAYLOAD` why it believes the finding false, under node 34's rule.

               **Delivery.** `expedition-checker/SKILL.md` gains the flags as a seventh given and a short section on checking them. The closing sentence of its givens ("The six givens above are everything you are given") is restated as what it protects, the unread record. That carries out node 28's flag `28.3`. `expedition/SKILL.md` gains the flags in the checker's spawn and loses item 2 of `## What nothing here settles`. Both changes are kept small, because the human wants the skills compacted. The work is the new implementation node below.
INDEX LINE:    The implementation checker checks each flag's index sentence, after its outcome, only for truth about the work. A false flag returns as a question, which takes the gate out of a standing yes.
FLAGS:         ASSUMPTION: The checker gets each flag's `flags.md` sentence with the flag's id and without the link to the node. The link would point a blind checker at the record, and the id lets the manager match a question back to its flag. Index: The checker gets a flag's index sentence with its id but not its node link, because the link would lead it into the record it is kept blind to.
               ASSUMPTION: The manager hands the node's flags on every run of the check, re-checks included, because a correction round can change a flag or add one. Index: Flags are handed to the checker on every run, re-checks included, because a correction round can change or add a flag.
               ASSUMPTION: Removing item 2 of the manager contract's `## What nothing here settles` renumbers the items after it. I searched the shipped files with `grep -rn -E 'item [0-9]'` and found no citation of those items by number. Index: Removing the settled item from the manager's list of unsettled duties renumbers the rest, and no shipped file cites them by number.
               ASSUMPTION: The implementation contract does not change. Its rule to fix what the checker found, or say why a finding is false, already covers a question about a false flag, because the checker contract counts questions handed back beside an outcome among what it found. Index: The implementation contract is unchanged, because its existing rule for checker findings already covers a flag the checker reports as false.
NEW NODES:     Name: Ship the checker's check of a node's flags
               Kind: implementation
               Question: Carry node 30's answer into the checker contract and the manager contract.
               Blockers: none
               Acceptance condition:
               > The work is `.claude/skills/expedition-checker/SKILL.md` and `.claude/skills/expedition/SKILL.md`, and no other file may be edited. These are files the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file. The worker may not mark this node, resolve it, or write a line in any index file.
               >
               > Done means all of the following are true of the finished tree.
               >
               > In `.claude/skills/expedition-checker/SKILL.md`:
               >
               > 1. Under `## What you are given`, the numbered list gains a seventh item: the flags the work's node holds, each as one sentence with its id, given as text by the spawn. The item says that a flag is a judgement another agent recorded about this work, and that this given is absent where the node holds no flags. The sentence introducing the list states the new count, and states correctly which givens the spawn carries and which one the checker reads for itself.
               > 2. The paragraph beginning "The six givens above are everything you are given" no longer says "six". It states its closure as protection of the record: the record stays unread, and a flag given under item 7 is a claim about the work, not part of the record. The paragraph's other sentences keep their words. That includes "The one exception is `map-implementation-rules.md`, and only for the standards in it." and "A path you were given as the work is the work wherever it sits, and you read it."
               > 3. A section headed `### The flags, after your outcome` is added under `## What you hand back`. It states all of the following:
               >    (a) Check the flags only after reaching your `PASS` or `FAIL`, and change no outcome because of them.
               >    (b) For each flag, establish one of three things: what it says was done is true of the work, it is false, or it makes no claim the work can make true or false.
               >    (c) Judge only whether what the flag says was done is true of the work, never whether the judgement was right, and ignore any reason the flag gives.
               >    (d) Report a false flag, and only a false flag, under `QUESTIONS:`, naming the flag's id and the search that showed it false.
               > 4. In `### Questions, alongside a \`PASS\` or a \`FAIL\``, the sentence that counts the kinds of question states the new count, and a false flag is described there as one kind. The section points at `### The flags, after your outcome` rather than restating it.
               > 5. No heading of the file is renamed. No sentence outside clauses 1 to 4 changes in content. The table under `### When what you check against is itself the problem` is not changed by this work.
               >
               > In `.claude/skills/expedition/SKILL.md`:
               >
               > 6. In `## The checker`, the list after "The checker receives the following:" gains one item: on the check of an implementation node, every run, the flags the node holds, each as its sentence from `flags.md` with its id and without the link to its node.
               > 7. The sentence "The checker receives nothing from the effort's own record, so its spawn never points it at the node file." is changed so that it makes the flag sentences of clause 6 its only exception, and it still says that the spawn never points the checker at the node file.
               > 8. In `## What nothing here settles`, the item beginning "Does anything check a flag before the human settles it?" is removed, and the items after it are renumbered in their existing order. The bullet "The scribe rule against the fuller form of a flag." under `## Conflicts this contract leaves open` is not changed.
               >
               > Both files:
               >
               > 9. Compared with the commit the work starts from, `.claude/skills/expedition-checker/SKILL.md` grows by no more than 15 lines, and `.claude/skills/expedition/SKILL.md` does not grow. Line counts are those printed by `wc -l`.
               > 10. Every markdown link in both files resolves to a path that exists.
               > 11. The working tree meets the bar.
               >
               > Scope: the places named are the work, not instances of a defect. One search was run to find the count words a seventh given would make wrong: `grep -n -w -i 'six\|five' .claude/skills/expedition-checker/SKILL.md` returned two lines, "You are given six things. The spawn carries the first five, and you read the sixth for yourself from one" and "The six givens above are everything you are given.", which clauses 1 and 2 cover. A count word that this search reaches outside those two lines is reported, not edited.
INVALIDATIONS: Node 26: narrowed. Its trial ran the flag check as a separate pass, after the outcome, on flags the manager stripped to what was done. The standing form is the same checker run, after the outcome, on the flag's `flags.md` sentence unchanged, with the checker told to ignore any reason it gives. The human's tentative "only giving what was done and not the reason" now means the checker ignores the reason; nobody removes it from the text.
               Node 28: no change. Its flag `28.3`, restating "That is everything" as what it protects, is carried out by clause 2 of the new node.
               Node 42: extended. Besides ground rules, one other kind of text now travels to the blind checker: a flag's index sentence, given as a claim about the work. It is not a ground rule and is not tested as one.
               Node 34: no change. Its rule is reused for a false flag.
CONDITIONS:    I listed open and claimed nodes with `grep -l -E '^Status: (open|claimed)'` (22 nodes). In their files I searched for "six givens", "everything you are given", "six things", "Does anything check a flag", "What nothing here settles", "The checker receives", "nothing from the effort", "What you are given", "check a flag", "flag pass" and `expedition-checker/SKILL.md`. Apart from node 30 itself, only two matched, both on `expedition-checker/SKILL.md`. Node 214 changes the table under `### When what you check against is itself the problem`, and its clause 3 forbids other sentences changing to carry its own clauses, so the two do not conflict. Clause 5 of the new node leaves that table alone. Node 41 states the checker file is not changed by its work, which is also no conflict. The open implementation nodes on `expedition/SKILL.md` are nodes 317 and 87. Neither condition matched `## What nothing here settles`, `## The checker` or item numbering. No replacement clause is owed, and no open node's question changes.
MISSING FROM MAP: The map does not say that a standing yes is in force or that it changes where flags reach the human. That came from the manager's notes and `expedition-standing-yes/SKILL.md`. I re-derived the size of flags.md (737 settled lines, 18 outstanding) with grep, rather than relying on node 30's stale "forty-nine".

RETROSPECTIVE:
1. What I had to hunt for: how the standing yes treats a checker's question, which is the rule that made (e) cost almost nothing to ship, found in `expedition-standing-yes/SKILL.md` under "What a standing yes never covers". Whether a checker's question counts as something the worker must answer ("What every finding carries" in the checker contract). The trial run's details in node 26. And the manager contract's own checker spawn list, which needed the exception to "receives nothing from the effort's own record". Node 30 did not mention that list.
2. What arrived that this node did not need: most of map.md (the heterogeneous-model note, the never-delete boundaries, the glossary counts), and the decisions-index line for node 366 beyond its batch figure.
3. What would have made this easier: the node naming the exact sections its answer changes (checker `## What you are given` and `### Questions…`, manager `## The checker` and `## What nothing here settles`). It would also help if a mid-attempt resume like this one said which files had changed since the payload. The manager did say so, and that saved a re-search.
4. What was stale, wrong or contradictory: node 30's "forty-nine flags" (the tree now holds 755 lines in flags.md). The node predates the standing yes, so its idea of where the human sees flags is out of date. The manager contract says the checker "receives nothing from the effort's own record", which this answer has to change. The node's framing that both new forms are the manager's to write no longer holds for the checker's direction: under this answer nobody writes the checker's form.
`````

## Flags

`30.1` `ASSUMPTION` **· settled** — The checker gets each flag's flags.md sentence with its id and without the node link. *(The worker's full text is under its handover's `FLAGS`.)*

`30.2` `ASSUMPTION` **· settled** — Flags are handed on every run of the check, re-checks included. *(The worker's full text is under its handover's `FLAGS`.)*

`30.3` `ASSUMPTION` **· settled** — Removing item 2 of the manager contract's What nothing here settles renumbers the rest; no shipped file cites them by number. *(The worker's full text is under its handover's `FLAGS`.)*

`30.4` `ASSUMPTION` **· settled** — The implementation contract does not change. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-02:* flags 30.1, 30.2, 30.3, 30.4 settle at the node closing report that closes this node.
