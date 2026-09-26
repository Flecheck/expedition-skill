# The trigger for topping up the human-facing nodes is a node finishing, and nothing states it

Type: implementation
Status: superseded
Superseded by: 100

Blocked by: none

## Question

*The human's, given as a correction to the manager mid-session. Their words are below and the framing around them is
the manager's, marked as the manager's.*

**The human's words, `verbatim`:**

> Also for the grilling, you should have started the new ones once the old ones finished, not waited for all gates to
> be finished. What I expect:
> - A node completes
> - You look at what should be started to replace it
> - You start it
> - You continue what you where doing

**And, on making it permanent, `verbatim`:**

> we need to make it permanant, I don't know if you made a node yet

**What the record already holds, and what it does not.** [`map.md`](../map.md) states the rule for this effort, in
the human's own earlier words: *"the rule is that when a node finishes, you start a new one (or new ones) to get
back to the current amount (2 by default by the user can ask for more)"*, fixed at [node
100](100-the-manager-starts-the-next-node-rather-than-proposing-it.md). **The shipped manager contract states
nothing of it** — `grep` over `.claude/skills/expedition/SKILL.md` for the top-up finds the words `frontier` and
`claim` defined in the glossary and no rule about returning to the target at all.

**What the human's correction adds to what `map.md` already says**, and it is the part that was missing rather than
merely unshipped:

1. **The trigger is a node finishing** — not a gate closing, not a batch of nodes closing together, and not the
   manager being asked.
2. **The top-up is interleaved rather than deferred.** Their four steps put *"you continue what you where doing"*
   last: the manager tops up inside whatever it was already doing and returns to it, rather than waiting for a
   quiet moment.

**Why this node exists rather than a line in the map.** The manager had stated the corrected rule in conversation
and written it nowhere, which the human caught: *"I don't know if you made a node yet"*. The manager had not.

## What this node has to reach

**Two files at least, and which of them is not settled here.**

- `map.md`'s existing statement, which is true but silent on the trigger and on the interleaving.
- The shipped manager contract, `.claude/skills/expedition/SKILL.md`, which says nothing at all. Whether it should
  is the standing default's question — a rule reaches a shipped file only where the human says so — and the human's
  words *"we need to make it permanant"* do not obviously answer it.

## The manager's note at filing

*Not a change to anything above.*

**This node has no acceptance condition and the manager has not written one.** Authoring one is not the manager's,
and no agent minted this node — it comes from the human directly. That gap is [node
55](55-who-writes-a-condition-with-no-spawning-node.md)'s standing question, which is open, and this node is a live
instance of it rather than a new problem.

**The manager applied the correction immediately and separately from this node.** It does not wait on this node to
land, and this node is about the record rather than about the manager's conduct from here.

**The manager's own account of how it failed, filed because the human asked for the rule and not for the excuse.**
It treated a returned payload as a node finishing on one reading and as not finishing on another, and it waited for
a lull instead of topping up in the moment. Both grilling slots sat at target only because the human asked twice.

## Flag `192.1` — the manager's own, against itself

*Filed by the manager. Outstanding, and not about this node's subject except that this node exists to make the rule
permanent.*

**The manager ran one grilling node against a recorded target of two, for most of a session.** The map states the
target and the rule that maintains it in the human's own words — *"by default 2 grilling nodes at once, and the rule
is that when a node finishes, you start a new one (or new ones) to get back to the current amount"* — and adds
explicitly that **a live question does not block a start**. The manager nevertheless ran a single grilling node at a
time, treating the one-question rule as though it capped the number of running nodes, which the same bullet
forbids.

**Caught by the human**, `verbatim`: *"only one grilling slot ?"*. **This is the third top-up failure of this
effort**, after the one that minted this node and one during the shipping backlog.

## Superseded, 2026-09-26

*The manager's note.* Made unnecessary by [node 100](100-the-manager-starts-the-next-node-rather-than-proposing-it.md)'s landed work (`47703bb`): `### Picking the next node` already says "When a node finishes, pick the next one, spawn its worker" and "When a node finishes, start enough work to bring every count back up". Node 330's worker recommended superseding it and the human took that with their "ok".
