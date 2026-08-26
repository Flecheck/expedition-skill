# Bring the glossary's code-slot and reject entries up to the worktree lifecycle

Type: implementation
Status: open

## Question

`CONTEXT.md` is the glossary the shipped files declare authoritative, and **two of its entries state as definitions
things the worktree lifecycle has made false** — including *both* sentences of **Code slot**, which is the term
[Carry the worktree lifecycle into the shipped files](74-carry-the-worktree-lifecycle.md) rewrote the implementation
contract around.

Reported by node 74's worker as flag `74.2`, which wrote the acceptance condition below. **Its condition forbade
touching `CONTEXT.md`**, so the defect was created and reported in the same node.

### The checker found one instance the worker did not, and supplied the extent

Node 74's blind checker independently reported the same gap and enumerated it completely. Its words:

> `map.md`'s `## Notes` calls that glossary a precondition for writing anything and says *"the glossary is
> authoritative"*, **so the authoritative source now states the superseded rule.**

**Extent, as it gave it:** a paragraph-level unwrapped scan over every `.md` under `.claude/skills/` plus
`CONTEXT.md` — *"the complete set of shipped prose in this repo"* — matching
`/code slot|one worker at a time|working tree is cleaned|worktree/i`. **Four entries in two files are every
instance.**

**The one the worker missed:** `.claude/skills/expedition-prototype/SKILL.md`'s own `code slot` glossary entry still
reads *"held by one worker at a time."* **The condition below does not reach it**, having been written before the
check ran — see the manager's note.

**Blockers: none.** It edits `CONTEXT.md`, which [Ship the glossary inside the skill directory and make it state its
own completeness](56-ship-the-glossary-into-the-skill-set.md) is moving; the condition already handles either
location.

## Acceptance condition

*Written by node 74's worker.*

`CONTEXT.md` at the repository root is edited, and nothing else is. Where that file has already moved to
`.claude/skills/expedition/CONTEXT.md`, the file at its new path is the one edited and the entries named below
resolve to it.

Two entries are brought to what holds now.

**1. `**Code slot**`.** It currently reads: *"The right to modify product code, held by one worker at a time.
Occupancy is discovered from the working tree rather than recorded, so a dying worker leaves nothing behind to clean
up."* Both sentences are false. The rewritten entry states that one worker holds one slot and that how many slots
exist is a setting of the effort, which may be more than one; and that a slot's occupancy is discovered by counting
the live worktrees, one per claimed implementation node, rather than by inspecting the working tree for uncommitted
changes. Its `_Avoid_` line, *"write lock, code lock — there is no lock"*, is left exactly as it stands.

**2. `**Reject**`.** Its clause *"so the node does not resolve, the working tree is cleaned, and what survives is
the discovery"* is false. On a reject the manager removes that node's worktree and deletes its branch; where the
human asks for the work to be kept, it is committed onto that branch before the directory is removed. The rewritten
clause says that, and the rest of the entry — including *"Not a verdict on quality — a node whose code is merely
wrong takes a correction round"*, *"The word is the human's alone; the checker's outcomes are `PASS` and `FAIL`"*,
and its `_Avoid_` line — is left exactly as it stands.

No other entry changes, and no entry is added or removed.

The standing bar applies: the working tree builds, warns about nothing, is formatted, and passes the tests relevant
to the change. This repository has no build, no tests and no formatter, which is a complete bar on its remaining
half and not a deficient one — so what remains is `/coding-principles` and `/naming`, and the glossary's own form: a
bolded term, a definition, and an `_Avoid_` line listing the synonyms it refuses.

### What the minting worker deliberately left out, in its own words

> The **Salvage** entry is stale too — it describes *"a path-limited diff the manager writes without reading it,
> kept out of the product tree"*, which assumes a shared working tree. But **no resolved node settles what salvage
> becomes when a stopped attempt's work already sits alone on its own branch.** That is a question for the human
> rather than work for this node, and it is left out of the condition deliberately.

[When an AFK worker cannot proceed](23-worker-cannot-proceed.md) carries the annotation for that, filed at [Gather
the manager's accumulated duties into one enumerated list](75-gather-the-managers-duties.md)'s resolution, where a
second worker reached the same conclusion independently.

### The manager's note at filing, not a change to the condition

**The condition says *"`CONTEXT.md` … is edited, and nothing else is"*, and node 74's checker found a fourth
instance outside it**: `.claude/skills/expedition-prototype/SKILL.md`'s `code slot` glossary entry, still reading
*"held by one worker at a time."* **Read literally, this condition forbids fixing it.**

The manager did not amend the condition — that text is the minting worker's. Two routes are open and the choice is
not the manager's: whoever claims this node **raises** on the ground that the condition's scope was written before
the full extent was known, or the fourth instance becomes its own node. **Recorded here so the audit at claim time
meets it rather than has to find it**, and noted as the second time in this effort a condition's scope was fixed
before a checker enumerated the defect it addresses.
