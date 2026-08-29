# A human edit lands in a worker's tree while the node is claimed

Type: grilling
Status: open

## Question

The implementation contract tells a worker, in as many words: **"The tree your spawn names is yours alone for the
whole of the node, and every file you edit is inside it."** That sentence is now false, and it was made false by the
one party whose right to edit anything is not in question.

**What happened.** While [Write the first version of the manager's skill](76-write-the-manager-skill.md) was claimed
and between two of its correction rounds, the human edited the deliverable in the worker's own worktree. Their
words, `verbatim`: *"I have also made a few changes to the skill"*. The file went 582 lines to 578.

**Nothing about that is wrong.** The human owns the repository, the effort and the deliverable, and reading a draft
and tightening it is the cheapest review there is — cheaper than a correction round, and the reason the worktree was
moved inside the repository in the first place. **The defect is that nothing in the design expects it.**

### What breaks, precisely

**The worker has no reason to look.** It is told the tree is its own, so on being resumed it treats its last version
as the baseline. A worker that does not check reports a diff containing someone else's writing, or silently reverts
it while fixing something adjacent. That exact failure was predicted at [Carry the worktree lifecycle into the
shipped files](74-carry-the-worktree-lifecycle.md), by a worker whose manager had wrongly told it the tree was
clean: *"A worker told its baseline is clean has no reason to check, and the one that does not check reports a diff
containing someone else's writing."* It was a warning about the manager's spawn; it has now arrived from a
direction nobody was watching.

**The checker is told the paths are the work.** It holds the changed paths against the acceptance condition and
attributes everything in them to the worker. It has no way to know a passage is the human's, and no route to treat
it differently if it did — and on a `FAIL` the manager would send the human's own prose back to a worker as a
defect to repair.

**The manager invented its remedy on the spot.** On noticing the file had moved it established mechanically that
every structural clause survived, declined to ask what changed or to guess, and told the worker the human's text was
authoritative, must not be reverted, and that a collision was to be reported rather than resolved. **No node
authorises any of that**, and it is the [Gather the manager's accumulated duties into one enumerated
list](75-gather-the-managers-duties.md) §Q2 class exactly: practice the manager adopted on its own authority.

### What the answer has to fix

- **Whether the worker is told at all**, and if so what it is told. Naming the fact costs one line in a resume; the
  alternative is that the human's edits are invisible to the party most likely to overwrite them.
- **Whether the contract's sentence changes.** *"Yours alone"* is what makes a worker's own `git status` an honest
  account of its work, which several duties rest on. Weakening it to *"yours alone among the agents"* keeps that and
  states the truth; saying nothing leaves a shipped sentence that is false whenever the human uses their own tree.
- **What the checker is told, if anything.** This is the hard half: a checker is blind by design, and *"these three
  paragraphs are the human's"* is an account of what happened, which [The checker's spawn carries the effort's
  ground rules](42-checker-spawn-carries-ground-rules.md) forbids travelling to it. So either the checker checks the
  human's prose as though it were the worker's — which is at least honest, the condition being the standard either
  way — or something changes about what may travel.
- **Whether the manager may ask what changed.** It did not, on the ground that guessing risks undoing the work; but
  a diff would have cost the human nothing to describe and would have removed the guessing entirely.

### What is deliberately not assumed here

That this is a problem to be **prevented**. The likeliest right answer is that it is a feature — the human editing a
draft in place is a review channel the design does not have — and that what is missing is only the bookkeeping
around it. A node that started from *stop the human writing there* would be solving the wrong thing.

## Where it came from

Minted by the manager at node 76's third correction round, from the event itself. Related: [Human review of landed
code](20-human-code-review.md), which settled how the human sees code that has **landed** and says nothing about
code in flight; and [When an AFK worker cannot proceed](23-worker-cannot-proceed.md), whose salvage question is the
same shape one step later.
