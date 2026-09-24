# Nothing mechanically verifies the never-delete bank once a map change has no checker

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 283](283-what-makes-a-change-to-a-record-file-a-node-rather-than-bookkeeping.md)'s worker, and
pasted as it wrote it.*

> The only mechanical verification the never-delete bank has ever had came from the checkers on record-only
> implementation nodes, which established `map-history.md`'s prior content as a byte-exact prefix of its new self
> and each banked passage as an exact substring of the pre-change file. `graph-conventions.md`'s ten mechanical
> checks cover none of it. **When record edits become the manager's own there is no checker, so the `Change the map`
> procedure's first step becomes something nobody verifies.** Give it a check.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 283's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.claude/skills/expedition/graph-conventions.md`, and no other file may be edited. The worker may not
> mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. Done means all of the following are
> true of the finished tree.
>
> **1.** The `## Mechanical checks` list carries a check covering **both halves** of what a change to a map file
> owes the history file: that the history file's content **before** the change is a **byte-exact prefix** of its
> content **after** the change, so the file gained text and lost none; and that **every passage the change removed
> from a map file appears byte-identically inside the text the change appended to the history file.**
>
> **2.** The check states **how it is decided** — by comparing the two states of the files character by character
> rather than by reading them for sense — so that its reader can run it without inventing a method, and so that it
> remains decidable by reading the files as that list's opening sentence requires of every check.
>
> **3.** The check is stated as **failing** when it does not hold, in the manner of that list's first nine entries,
> and not as a report-only item in the manner of its last.
>
> **4.** `### Change the map` names that check, **by its number**, as what establishes that its first step was
> carried out.
>
> **5.** The file states nowhere how many attempts this took, what it cost, or who was wrong.
>
> **6.** Only the one named path is edited. No node file, no status line, and nothing in `decisions.md` or
> `flags.md`.

## The manager's note at filing

*Not a change to anything above.*

**This is the safeguard node 283's answer names as replacing something it removes**, and its author flagged as
`283.4` that **it was never put to the human** — the session was closing under `/expedition-stop` and the worker was
directed not to open a fresh payload. **It is cheap and reversible and can be struck without disturbing the file
test**, which is the author's own framing and is the honest one.

**The check is not hypothetical and the record holds two worked instances.** Node 281's checker established
`map-history.md`'s base content as a **strict byte prefix** of the new file (+1421 bytes of tail) and the banked
passage as an exact substring of the base; node 268's checker did the same against `git show db81330:`, parsing the
appended block into **eight** passages and testing each. **Those two runs are what the check should be written to
reproduce**, and whoever claims this should read them rather than invent a method.

**Why this matters more than it looks.** The never-delete rule is the one invariant this effort has that nothing
else guards: a lost bank is silent, and the text it loses is the only copy of what a rule used to say. **Mechanical
check 5 would not have caught node 264's five unmarked supersessions either**, its author noted, because the
disagreement was on the superseded side — so this is the second gap found in that list this session.

**Sequencing**: `graph-conventions.md` is the most contended file on this effort, and [node
287](287-ship-the-record-file-test-and-repair-the-procedures-sentence.md) edits it too. **Two workers must not hold
it at once.**
