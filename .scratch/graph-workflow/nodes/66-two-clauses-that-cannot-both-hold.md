# The checker has no form for two clauses of one condition that cannot both hold

Type: grilling
Status: resolved

## Answer

When two condition parts cannot both hold on one reading but can on another, the checker checks under that reading and hands back a question; no raise, and no new verdict.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The human took both recommendations. Its shipped change joins [node 214](214-a-condition-that-contradicts-a-standard-is-a-raise.md) as clauses for that node's future condition. The node raised no flags.

## Question

A checker met two clauses of one acceptance condition that **cannot both be satisfied**, where which one gives way
is a **reading** rather than a fact. Its contract's routing table has no branch for it.

In the checker's own words, from [Restructure `map.md` to what every worker
needs](59-restructure-the-map.md):

> No form for the case I actually hit: two clauses of one condition that cannot both hold, where which one gives
> way is a reading rather than a fact. The routing table has *"you can check it and disagree"*, *"complying is what
> produced the defect"*, *"a part you cannot establish"*, and *"the condition is broken, raise"*. None fits. I took
> the reading that keeps the condition satisfiable and put the alternative in `QUESTIONS`, but the contract did not
> tell me to, **and a checker taking the strict reading would have failed the work for obeying clause 4.**

That last clause is what makes this more than a gap in a table. **The same work passes or fails on which reading
the checker happens to take**, and the contract is silent, so the outcome is set by the checker's disposition
rather than by the work.

**Why *the condition is broken, raise* is the wrong branch, and this is the substance of the decision.** A raise
stops the check. But the condition here was **satisfiable** — the checker found a reading under which every clause
holds, and the work met it. Raising would have spent a gate on a question the check could answer, on an effort where
a check is sometimes *unavailable* and six runs have died. The cheap disposition is what the checker improvised:
**take the satisfiable reading, establish the clauses under it, and hand the alternative back as a question.** The
decision is whether that becomes a fifth branch, and what it must carry so the human can overrule it.

**It is the third return shape improvised at the same place.** [What the checker contract owes to having been run
](31-checker-contract-owes.md) fixed the first two — the reserved clause and the non-blocking `QUESTIONS:` — and
this is the same defect recurring: a checker meeting a case its contract does not name, doing the sensible thing,
and the sensible thing reaching the next checker only if someone writes it down.

## What has to be decided

1. **Whether the satisfiable reading is the mandated default**, or whether the checker must raise and let the human
   choose. The trade is a gate against a wrong-way failure.
2. **What the handover must carry when it takes that route** — at minimum the reading taken, the reading declined,
   and which clauses would be unmet under the declined one, since the checker on node 59 supplied all three
   unprompted and the value was entirely in the third.
3. **Whether the verdict is qualified.** A `PASS` under a reading is not the same object as a `PASS`, and nothing in
   the shipped form distinguishes them.
4. **Who owns the repair afterwards.** The checker said it plainly — *"if the strict one does, it is the condition
   that needs amending rather than the work"* — and an acceptance condition is not the manager's to rewrite
   ([An acceptance condition is self-contained text](33-condition-is-self-contained.md)), so amending one after a
   check has run has no owner.

## Two instances already on the record

- **Node 59's clauses 4 and 9.** Clause 4 required moved history verbatim; the moved text contains a line-number
  citation that clause 9 bans. **Both the worker and the blind checker independently took the same reading** —
  clause 9 governs the pointers the files offer, not a preserved quotation — which is evidence the satisfiable
  reading is discoverable rather than arbitrary. It is flag `59.1` and the checker's first question.
- **Node 45's clauses 1 and 2**, where the manager's own audit recorded that *"if clause 1 is done loosely, clause 2
  is unsatisfiable rather than merely hard."* That one resolved by the ordering being load-bearing rather than by a
  reading, so it is a near miss rather than an instance — worth reading beside this because it shows the shape
  arriving a fourteen nodes earlier without being recognised.

## Interview

#### Questions 1 and 2, relayed 2026-09-29

*Pasted as the worker handed it back.*

```
NODE:          The checker has no form for two clauses of one condition that cannot both hold
ABOUT:         Decides what a checker does when two clauses of one acceptance condition cannot both hold as first read, but every clause holds on another reading. It is being decided now because checkers have met this three times with no rule for it (nodes 59 and 359, plus a near case at 204), and each improvised the same answer.
SO FAR:        I read the node, map.md, the decisions.md lines for 31, 59 and 334, the checker contract as it stands today (after node 334), the `## Review` of nodes 359 and 367, open node 214, and the standing-yes skill.
               - The current checker contract has no route for this case. Its routing table under `### When what you check against is itself the problem` has six rows. The one nearest to this case is "the work complies, and complying is what produces the defect → your outcome, and a question", but here the work cannot comply with both clauses on a strict reading, so that row does not fit. Hard rule 3 ("never check the work against your own repair of one") pulls the other way: a checker could treat choosing a reading as repairing the condition. A raise covers only a condition that is "self-contradicting" on every reading, and that is not this case.
               - Node 359, checker run 1, is a true instance. Clause 11 asked that every removed statement be "still stated at the heading the clause names". Clause 6 names only `## Flags`, and it also requires removing a sentence whose rule is stated elsewhere, at `### Picking the next node`. The checker took the reading under which every clause holds, found the condition met, and put the other reading in `QUESTIONS`. The human approved at the gate ("ok").
               - Node 367, checker run 1, is not an instance of this case. It is the existing "met and still wrong" route: clause 1's "word for word" left a pronoun with an unclear referent under writing rule 5. The existing row already covers it.
               - The shipped standing-yes skill already lists "a question a checker hands back beside its outcome" among the items it does not cover. So a question beside a PASS already brings the gate to the human, and it already marks that PASS as reached under a reading. No new verdict word is needed.
               - Open node 214, "A condition that cannot be honoured with a standard is a raise", covers the neighbouring case, where a clause conflicts with a standard rather than with another clause. It comes from your words at node 200: "If both the checker and implementer knew it, I would have expeted a raise at least." It has no acceptance condition yet. That node's checker also stated what a checker's raise costs: it stops the check and withholds an outcome the checker could give. For a checker, a raise and a question beside the outcome both reach you at the gate. The only difference is whether you also get the outcome.

Q1. The rule for the checker
ASK:           Should the checker contract state that, when two parts of the condition cannot both hold on one reading but every part holds on another, the checker checks under the reading on which every part holds and hands back a question beside its outcome, rather than raising?
RECOMMENDED:   Yes, with this text, about 700 bytes:
               (a) One new table row: "two parts of the condition cannot both hold on one reading of them, and every part holds on another | your outcome under the reading on which every part holds, and a question".
               (b) In `### Questions, alongside a PASS or a FAIL`, "Two kinds" becomes "Three kinds", and this paragraph is added: "The third is two parts of the condition that cannot both hold on one reading of their words, where every part holds on another reading. Check the work under the reading on which every part holds. Taking that reading is not a repair of the condition. In the question, name the reading you took, the reading you set aside, and each part the work would fail under the reading you set aside. Where no reading lets every part hold, the condition is self-contradicting, so raise."
               Why this rests on what already exists:
               - It turns the improvised practice into the rule, so the verdict no longer depends on which reading a checker happens to take.
               - Under the standing yes, the question already stops the gate from being auto-approved, so you still rule on the reading. You also get the outcome that a raise would withhold.
               - The node's decision points 3 and 4 need nothing new. The question is what marks the PASS as reached under a reading. The repair has an owner: your answer at the gate settles the reading. If you choose the reading the checker set aside, the work goes back and you amend the condition, a case the contract already covers under "The human may amend the acceptance condition while your check is live".
ALTERNATIVES:  - Make it a raise: every such case stops the check with no outcome. This matches the direction behind node 214, but it spends a gate the question already brings you and withholds an outcome the checker could give.
               - Leave it unwritten: checkers keep improvising, and a checker that takes the strict reading fails correct work.
               - Also add a qualified verdict word, such as "PASS under a reading": it adds a new shape that the question beside the PASS already stands for.

---

Q2. Where it lands
CONTEXT:       Whatever Q1 decides, the change lands in the same routing table as node 214's change.
ASK:           Should this change join open node 214 as clauses of its future condition, or become its own small implementation node that can land now?
RECOMMENDED:   Join node 214. Both are about a condition that cannot be honoured, in the same table of the same file. One change to the table avoids two edits of it that may disagree, and it follows your standing rule that a related defect goes into an existing node. The cost: this rule then waits until node 214 gets a condition.
ALTERNATIVES:  - A separate implementation node for `.claude/skills/expedition-checker/SKILL.md` only: it can land now, but the table is edited twice.
```

#### The human's answer to questions 1 and 2, 2026-10-02

`verbatim`: *"ok"*

The manager had put the questions with the line "Please answer Q1 and Q2. "ok for recommended" takes both." So the reply takes the worker's `RECOMMENDED` on both: the checker checks under the reading on which every part holds and hands back a question beside its outcome, with the worker's text (a) and (b); and the change joins open node 214.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      The checker has no form for two clauses of one condition that cannot both hold

ANSWER:        The case is two parts of one acceptance condition that cannot both hold on one reading of their words, where every part holds on another reading. The checker does not raise in this case. It checks the work under the reading on which every part holds, gives its outcome on that reading, and hands back a question beside the outcome. The question names the reading taken, the reading set aside, and each part the work would fail under the reading set aside. Where no reading lets every part hold, the condition is self-contradicting, and that remains a raise.

               What carries it, and so needs no new rule:
               - **The verdict is not qualified by a new word.** The question beside the `PASS` is what marks it as reached under a reading. The shipped standing-yes skill already counts "a question a checker hands back beside its outcome" as an item it does not cover, so such a gate still comes to the human.
               - **The human's answer at the gate owns the repair.** It settles the reading, and the manager records it in the node's `## Review`. If the human chooses the reading the checker set aside, the work goes back, and the human may amend the condition. The checker contract's `## When you are handed the same work again` already covers a condition amended while a check is live.

               Why not a raise: for a checker, a raise and a question beside the outcome both bring the item to the human at the gate. The raise also withholds an outcome the checker could give. A checker taking the reading is not repairing the condition, which hard rule 3 forbids, so the shipped text says that explicitly.

               Instances: node 59, clauses 4 and 9 (flag `59.1`), and node 359, checker run 1, clause 11 against clause 6. Node 367's checker run 1 is not an instance. It is the existing route for a condition that is met and still wrong.

               Where it lands: the change goes into open node 214, as clauses of its future acceptance condition, because both changes edit the same routing table in `.claude/skills/expedition-checker/SKILL.md`.

               The human's reply to Q1 and Q2, `verbatim`: *"ok"*. It took the recommendation of both.

INDEX LINE:    When two condition parts cannot both hold on one reading but can on another, the checker checks under that reading and hands back a question; no raise, and no new verdict.

FLAGS:         none

NEW NODES:     None minted. A defect joins open node 214, "A condition that cannot be honoured with a standard is a raise, in both workers' contracts", which is unclaimed and has no acceptance condition yet. These are the clauses to add to its condition once it has one. If node 214 is claimed before they are added, file them as their own implementation node with exactly these clauses.

               Clauses to add:
               1. In `.claude/skills/expedition-checker/SKILL.md`, the table under `### When what you check against is itself the problem` gains one row, word for word. Its first cell is "two parts of the condition cannot both hold on one reading of them, and every part holds on another". Its second cell is "your outcome under the reading on which every part holds, and a question". The table's other rows keep their words, though the work for the rest of this node's condition may change them.
               2. In the same file, under `### Questions, alongside a \`PASS\` or a \`FAIL\``, the sentence "Two kinds of question reach the human this way, and neither stops your check." becomes "Three kinds of question reach the human this way, and none of them stops your check." After the paragraph that begins "The second is a condition that is met and still wrong", and before the paragraph that begins "Hand each question back under your outcome", one paragraph is added, word for word: "The third is two parts of the condition that cannot both hold on one reading of their words, where every part holds on another reading. Check the work under the reading on which every part holds. Taking that reading is not a repair of the condition. In the question, name the reading you took, the reading you set aside, and each part the work would fail under the reading you set aside. Where no reading lets every part hold, the condition is self-contradicting, so raise."
               3. No other sentence of `.claude/skills/expedition-checker/SKILL.md` changes to carry clauses 1 and 2, and no heading of the file is renamed.

               Scope: the scope came from no search, because the named places are the work rather than instances of a defect.

INVALIDATIONS: - Node 31, "What the checker contract owes to having been run", is extended rather than contradicted. The two non-blocking kinds of question it fixed become three, and the routing table gains a row.
               - Hard rule 3 of the checker contract ("never check the work against your own repair of one") is narrowed. Taking the reading on which every part holds is stated not to be a repair.

CONDITIONS:    What I searched:
               - Every open and claimed node's `## Acceptance condition` and `## Question`, for "Two kinds of question", "Questions, alongside", "When what you check against", "routing table", "met and still wrong", "hard rule 3", "own repair of", "cannot both" and "both hold". Apart from node 66 itself, nothing matched.
               - Open nodes whose text names `expedition-checker/SKILL.md`: nodes 30, 34 (claimed) and 41. Their matches concern other sections, and I rewrite no clause of theirs.
               - The shipped files, for "two kinds of question". Only the checker contract's own sentence matched, and clause 2 above rewrites it.

               Open node whose question this changes: node 214. Its question gains the clause-against-clause case beside its clause-against-standard case. The rule for the clause-against-clause case is settled here, so node 214 decides only its own case and the wording that sits with this one in the same table. Its amendment from node 366, about a word the glossary refuses, is untouched.

MISSING FROM MAP: The map does not say that a question a checker hands back beside a `PASS` keeps the gate out of the standing yes. I got it from `.claude/skills/expedition-standing-yes/SKILL.md` and from the manager's notes.

RETROSPECTIVE:
1. What I had to hunt for:
   - The node 359 and 367 reviews, which I found with a path glob.
   - Whether the standing-yes skill already treats a checker's question as uncovered, which I settled with one grep.
   - Open node 214 and its relation to this node. Nothing pointed me to it; a search for "a reading" found it.
2. What arrived that this node did not need:
   - The decisions.md line for node 334. The checker contract on disk carried everything relevant.
   - Most of map.md's `## Notes`, apart from the node-200 standing instruction and the rule on joining a related defect to an existing node.
3. What would have made this easier: a spawn naming node 214 as the neighbouring open node, and stating that the standing-yes skill already treats a checker's question as uncovered.
4. What was stale, wrong or contradictory:
   - The manager's note listed node 367 as a recent instance. It is not one: it is the existing route for a condition that is met and still wrong.
   - The node's quotes of the routing table name four rows, and the table now has six.
   - The node frames decisions 3 and 4 as open, but shipped machinery already answers both.
`````
