# Two record defects the first run of the checks found, each needing a decision before it can be repaired

Type: grilling
Status: open

Blocked by: none

## Question

*Surfaced by [node 213](213-nothing-triggers-the-ten-mechanical-checks.md)'s worker, and pasted as it wrote
it. **Its acceptance condition below is that worker's own**, written in the same handover.*

**4. Two record defects the first run of the checks found, each needing a decision before it can be
worked**
Kind: grilling
Blockers: none
Question: Running the mechanical checks for the first time returned two failures whose repair is a
decision rather than work. (a) `nodes/207-the-checkers-raise-branch-fires-on-a-purely-additive-edit.md`
is `Status: superseded` and carries no `Superseded by:`, and no node in the record carries a
`Supersedes:` field — so either a replacement exists and both edges are missing, or the status is wrong.
(b) Node 150 is `resolved` and has three entry lines in `decisions.md`, all struck through and none
live — so either it owes a current line, or a resolved node may legitimately have none. Which is it in
each case?

**Acceptance condition: none, and none is owed** — this is a grilling node.

**What I could not write, and why**, stated rather than left out: I deliberately did not mint these as
implementation nodes. For 207 I do not know whether a replacement node exists, and naming one would be
authoring a supersession. For 150 the text of a replacement index line is a statement of what that node
decided, which is not a worker's to write. Both need the human before either can be work.

## The manager's note at filing

*Not a change to anything above.*

**This node was specified in a handover the manager left unfiled for a session**, and is minted late for that
reason rather than any other — flag `213.4` records the delay against the manager. Nothing in the text above
was re-authored on the way here; it is the worker's own, recovered verbatim from the session record.

## Annotation: one of the two defects is already repaired, the other still stands

*Filed by the manager, from the tree rather than from memory, on the day this node was minted.*

**(a) is discharged.** The condition names
`nodes/207-the-checkers-raise-branch-fires-on-a-purely-additive-edit.md` as `Status: superseded` with no
`Superseded by:` and no node anywhere carrying `Supersedes:`. **Both edges now exist**: node 207 carries
`Superseded by: 178`, and node 178 carries `Supersedes: 207`. The manager wrote both after node 213's worker made
its observation and before this node was minted — the same unfiled-handover delay flag `213.4` records.

**(b) still stands, exactly as described.** [Node 150](150-which-harness-route-creates-a-worktree.md) is
`Status: resolved` and **all three** of its lines in `decisions.md` are struck through, so it has **zero live index
lines**. That is a live failure of mechanical check 5 — *"Every `resolved` node has an `## Answer` and exactly one
line in `decisions.md`"* — and it is the failure this node exists to decide, because the repair is a choice between
unstriking one, writing a fourth, and something else again.

**So this node's subject is now one defect rather than two**, and the manager has neither narrowed its question nor
touched its wording: **the question is its author's**, and whoever answers it should know that half of it has
answered itself.
