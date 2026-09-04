# A "just do it" mode that skips grilling and puts the work up for review

Type: grilling
Status: open

Blocked by: none

## Question

*The human's own idea, `verbatim`. **Minted by the manager from their message and not surfaced by any worker.***

> I also had the idea of a "just do it" mode, where the grilling is skipped, it is implemented and then the user can
> review. For low stakes stuff or if the user wants to work by looking at what it could be. (It can be easier to
> spot issue when it is written than during planning)

**What has to be decided**, written by the manager and confined to what their words already fix:

1. **What the mode is a property of.** Their words leave three readings and do not pick: a property of one **node**,
   set when it is minted; a property of an **effort**, set when it is charted; or a thing the human **says in the
   moment**, which turns the next pick into an implementation node rather than a grilling one.
2. **What replaces the grilling node's output.** A grilling node produces a decision that later nodes are blocked
   on, and an implementation node needs an **acceptance condition written before any work starts** that its own
   worker may not rewrite. Under this mode nobody has decided the thing the condition would state. So: who writes
   the condition, and what does it say? [Who writes the acceptance condition for an implementation node the manager
   mints itself](39-condition-for-a-manager-minted-node.md) already permits the manager to write one under four
   constraints, the first of which confines it to **what is already fixed** — and in this mode, by construction,
   less is fixed.
3. **What the review at the end is.** The effort already has a **gate**: an implementation node's work stops there
   until the human acts, and the outcomes are approve or send back. Their *"then the user can review"* may be that
   gate unchanged, or may be a different act — because a gate sends work back against an acceptance condition, and
   here the thing being judged is partly the decision the grilling would have made.
4. **Whether the flags mechanism already is this mode, partly.** An AFK worker that meets an ambiguity **decides it
   and raises a flag**, and the flag reaches the human at the node's first human moment. That is already
   *decide-then-show*. What this mode adds is skipping the decision **node** rather than the decision, so the
   question is what is left that flags do not already cover.
5. **What makes a thing low stakes**, and whether that is the human's call in the moment or a property anything can
   read. Their words offer *"low stakes stuff"* and a second, different ground — *"if the user wants to work by
   looking at what it could be"* — and the second is not about stakes at all.

**Their stated reason, which is a claim about how review works rather than about the workflow:** *"It can be easier
to spot issue when it is written than during planning."* The manager records it as their ground and has not weighed
it.

## The manager's note at filing

*Not a change to anything above.*

**One thing on the record that bears on this and cuts both ways.** This effort has run **one** node in something like
this shape: [node 114](114-context-destination-entry-omits-the-expectation.md), whose acceptance condition the
manager wrote itself because no worker reached the defect. It landed a `PASS` on its first check with no part
uncovered — **and the manager got the condition's own recorded enumerator wrong on the first attempt**, both returns
false, caught only because another node's worker happened to re-run them. That is one instance of the mode working
and one instance of what it costs, on the same node.

**Also relevant and not yet resolved:** whether the manager may write a condition at all in a case where less is
fixed is flag `94.4`, which is outstanding.
