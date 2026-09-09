# A clause demanding byte-identity is discharged by diff, and says so

Type: implementation
Status: open

Blocked by: none

## Question

*Promoted by the manager from [node 200](200-collapse-the-rules-files-two-map-history-statements.md)'s
retrospective, and pasted as that worker wrote it.*

> `map.md` is a mandatory read and two of its ~50 items bore on the work (the never-delete preference, the
> seven-files line); ~28KB read for two facts. The rules file's `## Landing an implementation node's work` section —
> roughly 10KB of sandbox and rebase measurement — bore on nothing: clause 5 forbade changing it, and `cmp` against
> `HEAD` proved byte-identity without my reading a line of it. **A condition demanding byte-identity is discharged
> by diff, not by reading**, and saying so in the condition would let its worker skip the section outright.

The clause pattern is common on this effort — every recent condition on a congested file carries one — and each
worker decides for itself whether it must read the frozen section to honour the clause. Three of them proved
identity by hash or `cmp` instead; whether that is the practice, and where it is written so the next worker does not
read 10 KB to obey a clause a diff discharges, is this node's question.

## Acceptance condition

**None. Its author reported it as friction in a retrospective rather than minting a node, so no condition came with
it, and the manager did not write one.** Whoever the human sends at it owes the condition.

## The manager's note at filing

*Not a change to anything above.*

**This is the measured half of a claim the effort has otherwise only predicted.** The saving is one worker's read of
a named section — about 10 KB on this node — and it is stated by the worker that paid it rather than projected.
~~The effort's own token rule ranks work by measured saving and refuses predicted saving, which is what makes this
mintable as it stands.~~ **Struck in the turn it was written**: the human corrected that gloss at [node
183](183-nothing-measures-the-record-about-itself.md)'s interview, `verbatim` — *"having real number is better fo
cource but guessing can help"* — so a measured saving is worth more than an estimate and an estimate disqualifies
nothing. What makes this mintable is that the saving is measured, not that measurement was required.

**It is adjacent to [node 183](183-nothing-measures-the-record-about-itself.md) and is not the same item.** Node 183
is deciding what derives numbers about the record; this is about what a condition tells its worker it may skip.
