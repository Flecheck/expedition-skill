# A human edit lands in a worker's tree while the node is claimed

Type: grilling
Status: claimed

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

## Interview

#### Questions 1 and 2, relayed 2026-10-02

*Pasted as the worker handed it back.*

```
NODE:          A human edit lands in a worker's tree while the node is claimed (node 85)
ABOUT:         The implementation contract says "The tree your spawn names is yours alone for the whole node. Edit only files inside it." That stopped being true at node 76, where you edited the manager's skill inside the worker's worktree between two correction rounds ("I have also made a few changes to the skill"). This node decides how the workflow treats that kind of edit. It is being decided now because the shipped sentence is false whenever you edit a tree that is in flight, and the manager handled the node 76 case with a rule it made up on the spot.
SO FAR:        Read the node, map.md, the grilling contract, and the current shipped text in expedition-implementation, expedition-checker and expedition/SKILL.md. Facts:
               - Work in a worktree stays uncommitted through the checker and through the gate. So git cannot tell your edits from the worker's. `git status` in the worktree lists both as "the work". The worktrees sit inside the repo so that you can review them, which makes editing in place the natural thing to do.
               - The checker is given "the paths that changed, in the working tree holding them", and is held to the acceptance condition alone. Node 42 forbids sending it any account of what happened, and "these lines are the human's" is that kind of account.
               - At node 76 the manager checked mechanically that the structure survived your edit. It did not ask what you changed. It told the worker your text was authoritative, must not be reverted, and that a collision was to be reported. The worker then found that your edit had removed two statements the acceptance condition required, and raised that instead of restoring them. You settled it at the raise: restore one, drop the other from the condition. So "keep the human's text, raise a collision" has been tried once, and it worked.
               - When a correction round comes from you, the worker already receives your words verbatim. A remark like "I changed the skill" made at the gate therefore already reaches the worker. What is missing is any instruction telling the worker what to do with it.
               - This machine's global CLAUDE.md already tells agents not to undo the human's edits. A shipped rule cannot rely on that file, because the workflow will run on other machines.
               Settled on my own authority: this is a review channel to support, not something to prevent, which is the node's own working assumption. Q1 offers prevention as an alternative so that you can overturn this.

Q1. What the workflow does when the human edits a tree in flight
ASK:           Do you accept this package? (a) The contract sentence becomes "The tree your spawn names is yours alone among the agents for the whole node. The human may also edit it. Edit only files inside it." (b) One line in the correction-round section: "Where the human has edited your tree, keep what they wrote. Where it conflicts with the acceptance condition or with a finding, raise it instead of changing it." (c) The checker contract does not change. (d) The manager does not ask you what you changed. It passes what you said to the worker, and the worker reads the tree.
RECOMMENDED:   Accept all four. The package adds about three lines to the shipped files, which fits the compaction goal. Rationale for each part:
               (a) The rule that matters is that no other agent edits the tree, and that rule still holds. "Among the agents" makes the sentence true and keeps it short.
               (b) This is the node 76 practice. It worked, and it turns a silent revert into a question for you.
               (c) Judging your prose against the condition is honest, because the condition is the standard whoever wrote the text. When your text fails the condition, the checker's FAIL reaches the worker, and (b) makes the worker raise it to you instead of rewriting your text. So nothing new has to reach the checker, and node 42's rule stays intact.
               (d) Asking costs you a message every time, and the worker can see the current state of the tree for itself. What it cannot know is that you edited it, and (b) covers that.
ALTERNATIVES:  - Also have the manager ask you, at each resume after you edit, which passages are yours. This is more exact, but it costs you a message each time and adds a duty.
               - Have the manager commit a snapshot at each handover, so that `git diff` shows your edit apart from the worker's. This is exact without asking you, but it breaks the "uncommitted until approval" landing policy and is more machinery.
               - Tell the checker which passages are yours. This contradicts node 42.
               - Prevent it: tell you not to edit trees in flight and to give corrections at the gate instead. This removes the cheapest review channel you have, which is the reason the worktrees were moved inside the repo.
               - Leave the sentence as it is and add nothing. The shipped sentence stays false, and a worker on another machine may revert your edit.

---

Q2. Where the rule lands
CONTEXT:       Map rule: a standing rule reaches a shipped file only where you say so. Otherwise it is this effort's alone.
ASK:           Should the Q1 changes go into the shipped files (the implementation contract, plus the glossary if it restates the sentence), or only into this effort's map?
RECOMMENDED:   Shipped files. The false sentence is itself in a shipped file, and you will edit worktrees on other projects in the same way. The global CLAUDE.md cannot carry the rule there, because a shipped rule cannot assume this machine.
ALTERNATIVES:  - This effort's map only. That fixes nothing in what ships, and the shipped sentence stays false.

RETROSPECTIVE (attempt so far):
1. What I had to hunt for: the current landing facts (uncommitted until the gate, worktrees inside the repo). They are in map-manager-only.md, which a worker has no reason to read. The manager's notes pointed me there. I also had to look up how node 76's raise actually ended, in node 76's `## Interview`.
2. What arrived that this node did not need: the decisions.md lines for 160 and 363. Integration conflicts barely bear on this node.
3. What would have made this easier: a link in the node from the event to node 76's Attempt 1, which shows that "keep it and raise it" was already tested once.
4. What was stale, wrong or contradictory: the node quotes the older wording of the contract sentence ("every file you edit is inside it"). It also assumes a correction round that the manager starts only from the gate. Node 363 added correction rounds started by the manager on integration conflicts, which leaves this node unaffected.
```

#### The human's answer to questions 1 and 2, 2026-10-02

`verbatim`: *"ok"*

The manager had put the questions with the line "Please answer Q1 and Q2. "ok for recommended" takes both." So the reply takes the worker's `RECOMMENDED` on both: the package (a) to (d) is accepted, and it goes into the shipped files.
