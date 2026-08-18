# What keeps the shipped files consistent when a decision changes a term

Type: grilling
Status: open

## Question

A resolved node changes a word or a rule. Which shipped files have to move, and what makes sure every one
of them does?

Nothing answers this today. The workflow has a list of decisions owed to **one** file and no list at all of
the files a decision might be owed to.

### It has failed three times, each time one level further out

1. **[map.md](../map.md)'s delta list tracked `graph-conventions.md` alone.** Eight deltas accumulated
   against it correctly. Then [What is recorded when the human takes an option as
   offered](25-recording-an-option-taken.md) invalidated one sentence in **two of the six worker
   contracts**, and the list had nowhere to put it — which is why [Carry the recorded deltas into the
   shipped skill files](26-carry-deltas-into-shipped-files.md) was minted as a node instead of a tenth line
   on the list. The map recorded the lesson at the time: *"A delta list works until a delta lands on a file
   the list does not track."*
2. **That node's acceptance condition named three files** — the document and the two contracts — written by
   a worker that had just done the analysis and by the manager adding a fifth condition on top.
3. **The checker found a fourth.** Blind, tracing condition 4, it reported that
   [`CONTEXT.md`](../../../CONTEXT.md) had become the stale side: its *Acceptance condition* and *Flag*
   entries still described a worker flagging a wrong condition, where the fifth delta had made that a
   **raise**. `graph-conventions.md` declares the glossary authoritative for the terms it uses, so the
   shipped document was pointing at a file that contradicted it. The human put it in scope with one word,
   `fix`.

Three for three, and the general conclusion was never drawn — only the miniature version of it, once, about
one list.

### Why the obvious answer is not obviously right

*"Keep a list of the shipped files"* is the first thing anyone reaches for, and it is what just failed three
times — each failure being a list that was correct about the files it knew. A list is only as good as
whoever remembers to extend it when a file joins the set, and the file that joins is exactly the one nobody
was thinking about.

What the answer has to decide, then, is whether the mechanism is a **list**, a **check**, or a **procedure**:

- A **list** in `map.md` or the conventions document, naming the product files — cheap, and has failed.
- A **mechanical check**, joining a decision to the files that must carry it. The eight existing checks are
  all decidable without judgement; this one may not be, which is the boundary [Graph file
  format](13-graph-file-format.md) drew between a script's work and the cascade's.
- A **procedure** at resolution: the node that changes a term names the files it invalidates. This is
  nearly free, since a handover already reports `INVALIDATIONS` — but `INVALIDATIONS` is defined over
  **resolved nodes**, not over product files, and no worker has ever reported one.
- Or the **cascade** ([Cascade pass mechanics](15-cascade-pass-mechanics.md)) already owns this and only
  ever gets described over graph edges. If a cascade scans code for decisions that have moved, a shipped
  prose file is code.

### Two things the answer must not miss

**The glossary does not travel.** `CONTEXT.md` sits at the repo root, not under `.claude/skills/`, so
copying the expedition skills to another repository carries none of it — while `graph-conventions.md`
declares it authoritative for every term. That is the same defect as the *"invoke if present"* patch on
method skills, recorded in [map.md](../map.md)'s fog under *how the workflow reaches a repository that is
not this one*, and this node is where it becomes concrete rather than adjacent.

**The failure was found by the party with the least context.** Not by the manager holding the delta list,
not by the worker that had just read every delta — by a **blind checker** tracing a condition that told it
to account for every changed line. Whatever the mechanism turns out to be, that is a datum about where this
class of miss is visible from.

Feeds the **manager's own skill**, and possibly the cascade.
