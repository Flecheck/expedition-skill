# Bring the glossary's `Closed` entry off the rejected frequency claim

Type: implementation
Status: open

## Question

*Surfaced by [The human rejects *most efforts never end*](86-most-efforts-never-end-rejected.md)'s worker, and pasted
as it wrote it.*

> `CONTEXT.md`'s `Closed` entry states *"Most efforts are never closed, and that is a legitimate steady state"* — the
> claim the human rejected — and it is the only instance in the product tree, read by every reader of the skill set
> including repositories that never see this graph. Every other instance is in the record and is repaired by
> annotation.

**Blockers, in the worker's words:** *"none. It edits `CONTEXT.md`, which [Ship the glossary inside the skill
directory](56-ship-the-glossary-into-the-skill-set.md) is moving, and the condition handles either location. [Bring
the glossary's code-slot and reject entries up to the worktree lifecycle](81-glossary-code-slot-and-reject.md) edits
the same file at disjoint entries; either order works and neither blocks the other."*

## Acceptance condition

*Written by node 86's worker. Pasted as it wrote it, and not the manager's.*

> `CONTEXT.md` at the repository root is edited, and no other file is. Where `CONTEXT.md` has already moved to
> `.claude/skills/expedition/CONTEXT.md`, the file at its new path is the one edited.
>
> One entry changes. Under `## Closing an effort`, the entry `**Closed**` currently reads:
>
> > The human's declaration that an effort is over. Only the human closes one; the manager reports that the
> > conditions hold and nothing more. Most efforts are never closed, and that is a legitimate steady state.
> > `_Avoid_`: done, finished, complete
>
> Its third sentence — *"Most efforts are never closed, and that is a legitimate steady state."* — is false and is
> replaced. **The replacement makes no claim, in any wording, about how often efforts are closed: neither that most
> are, nor that most are not, nor that the proportion is unknown.** In its place it states the conditional: that an
> effort whose frontier never empties is in a legitimate steady state rather than a stalled one, and is not to be
> treated as a defect.
>
> The entry's first two sentences and its `_Avoid_` line are left exactly as they stand. No other entry in the file
> changes, and no entry is added or removed. The glossary's form is kept — a bolded term, a definition, and an
> `_Avoid_` line listing the synonyms the term refuses.
>
> The standing bar applies: the working tree builds, warns about nothing, is formatted, and passes the tests relevant
> to the change. This repository has no build, no tests and no formatter, which is a complete bar on its remaining
> half rather than a deficient one — so what remains is `/coding-principles`, `/naming`, and the glossary's own form
> above.

## The manager's note at filing

*Not a change to anything above.*

**Why this is a node rather than a fourth entry on [node 81](81-glossary-code-slot-and-reject.md)'s condition** is
flag `86.1`'s companion, flag `86.2`, in the worker's own words: node 81's condition was already amended once by a
manager, that amendment is flag `81.1`, and it produced [How a condition's scope is
amended](82-amending-a-condition-whose-scope-was-too-narrow.md) so the shape would not repeat.

**Node 86's answer names this as the only site of the rejected claim that is a true edit.** Its other seven sites are
graph files repaired by annotation under the never-delete rule; this one ships.
