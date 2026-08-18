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
4. No other contract changes, and no decision on any resolved node changes. `CONTEXT.md` is touched only if a
   term genuinely moves, and if it is, the [glossary-does-not-travel problem](29-shipped-file-consistency.md)
   applies and is reported rather than solved here.
5. The bar as [map.md](../map.md) records it for this repo: no build, no tests, no formatter, so the project
   criteria, this map's standing preferences, `CONTEXT.md`'s `_Avoid_` lines, and these conditions are the
   whole of it.

**One warning to whoever spawns this**, learned the hard way on node 26: **that node's acceptance condition
was the first written by the manager rather than by a spawning node or its worker, and it had to be amended
twice** — once for naming a glossary entry that does not exist, once for a clause true only of implementation
nodes. This condition is also manager-written. Read it against the files before trusting it.
