# What the checker contract owes to having been run

Type: implementation
Status: open

## Question

`expedition-checker/SKILL.md` was written by the manager at [Write the worker contract
skills](22-worker-contract-skills.md) and had never been run by the agent it was written for. It has now been
run four times on one node, and it did **three things its own text does not describe** — each of them right,
and each invisible to the next checker, which gets the file and not the transcript.

Created at [Carry the recorded deltas into the shipped skill files](26-carry-deltas-into-shipped-files.md)'s
gate, from the human's question on reading the gate payload: *"do you also want to do something also with the
'What the checker did that I'd want kept'"*. The manager had recorded all three on that node as things worth
keeping and had stopped there, which is a record of admiration rather than a change to anything.

### The three

**1. How to check work that edited the checker's own standard.** The bar for this repo includes
[`CONTEXT.md`](../../../CONTEXT.md)'s `_Avoid_` lines, and the work edited one of them — so the standard moved
under the check. Handed a framing and explicit permission to raise, the checker used neither and found the
right thing to measure instead: **a standard has operative content and a rationale.** It counted the forty
`_Avoid_` lines before and after, found one differing line, and compared the *refused set* — `{escalate,
interrupt, ask}` — which was identical. Only the appositive after `ask` had moved. Then it named its own raise
condition:

> What would have changed that: had the edit added or removed a refused word, the operative standard itself
> would have moved and I would have had nothing unmoved to check the rest of the work against — that I would
> have raised rather than resolved.

The next round moved the same clause again, and it applied its own test rather than inheriting its own
conclusion. **Moving a rationale leaves a check intact; moving operative content destroys it.** Nothing in the
contract says this and the contract is what the next checker gets.

**2. What to do when the defect is in the acceptance condition and the work complies with it.** The contract
has two routes for a bad condition and neither fits: `raise` is for a condition that *cannot be checked* —
incoherent, unmeasurable, unobservable — and *"a condition you can check but disagree with is not a raise.
Check it as written."* This condition was checkable, the work complied, **and complying produced a
contradiction between two entries of the shipped glossary.** Failing the work would have been wrong; saying
nothing would have shipped the defect. It did neither: it handed the observation back as a **question**
alongside its `PASS`, noting that the wording was the condition's own and so not the worker's to depart from.
The human took it, the condition was amended, and a real defect in the authoritative file was caught.

That is a third route and the contract sanctions the channel only for something else — *"where a skill you ran
wants to ask the human something."* Whether it is a use of `QUESTIONS:` or a fourth return shape is the one
genuinely open call in this node.

**3. What "the statement of what changed is not evidence" costs when the work was reflowed.** The contract
says comparing modification times against the last outcome *"is enough to find them."* It is not, once a file
is rewrapped: a reflow moves every line of a paragraph. The checker reconstructed the previous version of the
entry from the diff it had read the round before, unwrapped both, and word-diffed them — establishing that the
whole change was one inserted phrase. It also **unwrapped before grepping** to confirm shared wording, noting
that a line-based grep misses a phrase that wraps.

### A fourth, added in place by [Whether a spawn may override a shipped worker
contract](28-spawn-overriding-a-contract.md)

**4. What to do when the acceptance condition itself moves while the check is live.** On that same node,
condition 7 was **amended twice mid-node** and the manager said so in each resume. The contract's *"When you
are handed the same work again"* section is written for a changed **work** against a fixed condition — the
whole design says a condition is written before work starts and is not the worker's to rewrite — so nothing
in it covers this. The checker handled it correctly with no instruction: it re-checked against the amended
text and did not treat its own earlier conclusion as inherited.

Node 28 ruled this **not a departure from the contract but an uncovered case**, which is why it lands here
rather than being licensed. It meets this node's own criterion exactly — real, handled right without
instruction, and invisible to the next checker, which gets the file and not the transcript.

Added in place because this node was unstarted, per [Revision semantics](06-revision-semantics.md).

### A fifth and a sixth, added in place by [An acceptance condition is self-contained
text](33-condition-is-self-contained.md)

**5. The raise for a bad condition does not name the case node 33 routes to it.** The contract opens that
raise for a condition *"incoherent, self-contradicting, unmeasurable, or naming something that cannot be
observed"*. A condition whose **demand is held in material the checker was not given** is none of those on
its face: the thing named can be observed perfectly well, by somebody else. Node 33 shipped the rule that
sends exactly such a condition here — *"raised by the manager where it meets one before the check, or by the
checker on a condition it cannot check"* — so the list now owes it a clause.

What happened instead, for the fourth time: handed node 33's condition 6, whose deliverable lands in a node's
`## Answer` that no checker is given, the checker **neither passed nor failed nor raised it**. It returned
`PASS` and recorded that one clause was outside what it could establish, in its own words:

> Reading it as "in the file" would be checking against my own repair of the condition, which my contract
> forbids. **The manager holds that handover and is the only party that can verify the audit was reported; my
> `PASS` does not cover it.**

That is item 2's third route again, arriving unprompted on a different trigger — and it is now the shape this
node has seen most often. Whether the two cases want one return shape or two is this node's to say.

**6. A blind checker that invokes a reviewing skill loses its blindfold to the sub-agents that skill
spawns.** The contract tells the checker to run a reviewing skill for code standards. Node 33's checker found
one on the machine and **declined to invoke it**, giving the reason:

> because it runs its axes in spawned sub-agents that would be handed none of that and would go looking,
> including into the record

It applied that skill's standards axis by hand instead, and left its spec axis unrun on the ground that the
axis holds work against an originating document — which here is the node file the checker may not read.
Nothing in the contract says any of this. The blindfold is a property of what the checker is *given*, and
delegation hands a fresh agent a fresh set of givens; the contract treats *"invoke a reviewing skill"* as
free.

**A second checker met the same case and answered it differently, and both answers are right.** Added in
place by [The clause that says no resolved node changes cannot be
self-contained](36-resolved-node-clause-cannot-be-self-contained.md). That node's checker found the same
reviewing skill and **invoked its standards axis anyway — with the standards and the smell baseline pasted
into the sub-agent**, so the delegate was handed givens rather than sent looking. It left the same spec
axis unrun, on the same ground and adding one detail the first did not: *its search order points into
`.scratch/`*, which is the record, so the axis would have walked there before reading anything.

So the uncovered case has two correct discharges — **decline to invoke**, and **invoke with the givens
supplied** — and the contract names neither. The second is strictly more useful, since it gets the axis run;
the first is safer where a skill's internals cannot be constrained. That is the distinction condition 8
below has to make, and it is why the honest answer may be a duty to *judge and report* rather than a
prohibition.

## Acceptance condition

1. `expedition-checker/SKILL.md` states the operative-content-versus-rationale test for a standard the work
   itself moved, and the condition under which the checker raises instead of resolving: an added or removed
   refused element leaves nothing unmoved to check against. In the contract's own voice, general over
   standards rather than written about `_Avoid_` lines, since the next repo's bar will not have them.
2. It states the route for a condition that is checkable and complied with, where compliance is what produces
   the defect — distinguished from the existing raise, which is for a condition that cannot be checked at all,
   and from *"a condition you can check but disagree with"*, which stays out of scope. **If the honest answer
   is a fourth return shape rather than a use of `QUESTIONS:`, raise it** rather than deciding it: the three
   return shapes are [Human review of landed code](20-human-code-review.md)'s and [Write the worker contract
   skills](22-worker-contract-skills.md)'s, not this node's.
3. Its *"When you are handed the same work again"* section no longer claims modification times are **enough**
   to find unmentioned changes, and says what to do about a reflow: reconstruct and compare content, not
   lines. Unwrapping before searching is stated wherever the contract tells the checker to search.
4. ~~No other contract changes, and no decision on any resolved node changes. `CONTEXT.md` is touched only if a
   term genuinely moves, and if it is, the [glossary-does-not-travel problem](29-shipped-file-consistency.md)
   applies and is reported rather than solved here.~~

   **Replaced in place**, by [The clause that says no resolved node changes cannot be
   self-contained](36-resolved-node-clause-cannot-be-self-contained.md) at its gate. That node's audit found
   this clause failing the self-containment rule **twice** — once on *"no decision on any resolved node
   changes"*, which node 36 has now ruled out of every acceptance condition because no copy can repair a
   demand that quantifies over the record; once on *"the glossary-does-not-travel problem"*, whose content
   sits only in node 29 and which node 33's rule says to **copy in**. Both repairs are below, and this node
   being open and unstarted, they are made here rather than by a node of their own — the worker that
   reported them said the call was the manager's.

   **No other contract file changes.** `expedition-checker/SKILL.md` is the only one this node's work
   touches; the five `.claude/skills/expedition-<type>/SKILL.md` worker contracts and `CONTEXT.md` stay as
   they are.

   **Where a term does genuinely have to move, `CONTEXT.md` is edited and the move is reported rather than
   propagated.** The reason, copied in rather than pointed at: **nothing checks the shipped files against
   the glossary.** A decision that changes a word leaves every other shipped file still carrying the old
   one, and no mechanical check and no agent's contract looks for it — so a term moving here is a report to
   the human and a `NEW NODES` entry, never a sweep of the other files from inside this node.

   The record-wide demand that used to sit here is now owed on the handover instead, where every worker
   returns `INVALIDATIONS` — which resolved node its work contradicts, and how. Nothing about it is this
   condition's business.
5. The bar as [map.md](../map.md) records it for this repo: no build, no tests, no formatter, so the project
   criteria, this map's standing preferences, `CONTEXT.md`'s `_Avoid_` lines, and these conditions are the
   whole of it.

6. Its *"When you are handed the same work again"* section says what the checker does when **the acceptance
   condition** has changed since its last outcome, distinguished from a changed work: re-check against the
   amended text, and do not inherit a conclusion reached against the old wording. *(Added with the fourth
   case above, by [Whether a spawn may override a shipped worker
   contract](28-spawn-overriding-a-contract.md). **Manager-written**, and so subject to the same warning as
   the rest of this condition — read it against the file before trusting it. Added rather than left to the
   `## Question` alone because flag `26.7` records what a described case with no condition covering it costs:
   one product file in scope and no condition reaching it.)*

7. Its raise for a bad condition covers a condition the checker cannot check **because what the condition
   demands is held in material the checker was not given** — distinguished from the four grounds already
   listed, none of which fit: such a demand is neither incoherent nor self-contradicting nor unmeasurable,
   and what it names is observable by a party that has the material. Where the answer to condition 2 is a
   fourth return shape, this case uses it too, or the contract says why the two differ. *(Added with the
   fifth case above, by [An acceptance condition is self-contained
   text](33-condition-is-self-contained.md). **Manager-written**, and subject to the same warning as the
   rest of this condition.)*

8. It states that a reviewing skill run under this contract must not delegate the check to agents that would
   not be handed the checker's own givens — or, where the contract cannot bind what a skill does internally,
   it says that the checker judges this itself before invoking one and reports which axes it ran and which it
   left. The blindfold is a property of what the checker is given, and the current text treats invoking a
   reviewing skill as free. *(Added with the sixth case above, by the same node, and **manager-written**.
   If the honest answer is that no contract can constrain a third-party skill's internals, say so and write
   the reporting duty alone.)*

**One warning to whoever spawns this**, learned the hard way on node 26: **that node's acceptance condition
was the first written by the manager rather than by a spawning node or its worker, and it had to be amended
twice** — once for naming a glossary entry that does not exist, once for a clause true only of implementation
nodes. This condition is also manager-written. Read it against the files before trusting it.
