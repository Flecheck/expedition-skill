# What a worker does when a file it must read is held by the code slot

Type: grilling
Status: open

## Question

The code slot is separate from the interview slots, so a non-code worker runs alongside an implementation node.
**Nothing says what that worker does when a file it must read is being edited by the slot's occupant.**

[Cascade pass mechanics](15-cascade-pass-mechanics.md) makes only the *per-candidate cascade agent* wait on an
occupied slot, and says nothing about a grilling, research or precondition worker. [What the manager works on
next](16-human-steering.md) separates interview slots from the code slot and does not reach this.

**The live instance:** [Gather the manager's accumulated duties into one enumerated
list](75-gather-the-managers-duties.md) was spawned while [Carry the worktree lifecycle into the shipped
files](74-carry-the-worktree-lifecycle.md) was editing `map.md`, and **the manager's own remedy — telling the worker
to read that file from a named commit with `git show` and to say that it did — appears in no node and in no shipped
file.**

## What has to be decided

1. Does a worker **wait**, read a **pinned revision**, or **report what it could not read**?
2. If a pinned revision, **who names it**, and what does the worker owe the record about having read one?
3. Does the answer differ between a file being edited and a file whose editor **may not land** — a node that could
   be rejected, whose edits then never existed?

**Blockers: none.** It lands on the five worker contracts and on the manager's own skill, which are the live
territory of several open nodes, so it must be **sequenced** against them rather than run beside them.

Reported by node 75's worker, in the answer that gathered the manager's duties — item 179 of §Q2, *practice the
manager adopted on its own authority*.
