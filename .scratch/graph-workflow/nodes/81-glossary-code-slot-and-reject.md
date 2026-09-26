# Bring the glossary's code-slot and reject entries up to the worktree lifecycle

Type: implementation
Status: superseded
Superseded by: 332, 333

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

*Written by node 74's worker, and **amended once by the manager on the human's instruction** — the amendment is
recorded below the condition, and entry 3 is the whole of it.*

`CONTEXT.md` at the repository root and `.claude/skills/expedition-prototype/SKILL.md` are edited, and nothing else
is. Where `CONTEXT.md` has already moved to `.claude/skills/expedition/CONTEXT.md`, the file at its new path is the
one edited and the entries named below resolve to it.

Three entries are brought to what holds now.

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

**3. `code slot`, in `.claude/skills/expedition-prototype/SKILL.md`'s `## Words used exactly`.** *This entry is the
manager's amendment and not the minting worker's text.* It currently reads: *"the right to modify product code, held
by one worker at a time. Never yours."* Its first clause is false for the same reason entry 1's first sentence is.
The rewritten entry says what [Carry the worktree lifecycle into the shipped files](74-carry-the-worktree-lifecycle.md)
has already shipped in the implementation contract — that one worker holds one slot, and that how many slots an
effort runs is that effort's own setting — and keeps *"Never yours"*, which is still true of a prototype worker and
is what the entry is there to say. It stays a single line in that list's own form, which carries no `_Avoid_` line.
Nothing else in that file changes: its hard rule 1, *"You do not hold the code slot"*, is true under the lifecycle
and is left exactly as it stands.

No other entry changes in either file, and no entry is added or removed.

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

### The amendment, and the human's word that licensed it

**What was wrong.** As filed, the condition said *"`CONTEXT.md` … is edited, and nothing else is"*, and node 74's
checker had found a fourth instance outside that scope: `.claude/skills/expedition-prototype/SKILL.md`'s `code slot`
glossary entry, still reading *"held by one worker at a time."* **Read literally, the condition forbade fixing it.**
The manager filed the problem rather than repairing it, on the ground that the text was the minting worker's, and put
two routes to the human: whoever claims the node raises, or the fourth instance becomes its own node.

**What the human said**, `verbatim`: *"For 81, fix it"*. Neither route — a third, which is the amendment above.

**What the manager did under that word.** Widened the scope sentence to name both files, and added entry 3. Entry 3
demands only what a resolved node already fixed: node 74's shipped wording in the implementation contract, copied
across rather than composed here, which is why the amendment decides nothing. The node was **unclaimed** when this
was written, so no worker had read the earlier text and no checker had been handed it.

**What it departs from.** [Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md) gives the manager the pen only for nodes it minted itself, and
says of the worker-minted case that *"the manager authoring one remains explicitly wrong"*. This is that case: node
81 was minted by node 74's worker as flag `74.2`, and its condition is that worker's. Flag `81.1` carries the
departure; the permanent fix is [How a condition's scope is amended once the extent turns out wider than it was
written for](82-amending-a-condition-whose-scope-was-too-narrow.md).

**Why a permanent fix and not just this repair.** The same shape has now run twice in a row, and this node is the
second instance rather than the first. Node 74's condition named two files; the defect the worktree lifecycle
created spanned four, which is flag `74.2` in as many words — *"both being outside the two files its condition
named"* — and it is the reason this node exists at all. Then this node's own condition named one file and the same
checker's enumeration reached two. **A condition's scope is written before anything enumerates the defect, and the
enumeration arrives from the check**, which is after every route for changing the scope has closed. Both instances
ended at the human for a decision neither needed.

## Flags

`81.1` `ASSUMPTION` — **The manager amended a condition written by another node's worker.** Licensed by the human in
one line, *"For 81, fix it"*, for this node only. The departure is from node 39's rule that a worker-minted node's
condition stays the minting worker's; the amendment's content decides nothing, being node 74's already-shipped
wording copied across, so what is at risk is the precedent rather than this node's standard. The alternative on the
record and not taken: the fourth instance becomes its own node, which costs a node and a worker and leaves node 81's
scope honest. Recorded under [Whether a spawn may override a shipped worker
contract](28-spawn-overriding-a-contract.md)'s shape — a licence for one attempt, flagged, plus a node for the
permanent fix. *Filed as `ASSUMPTION` because the three kinds `flags.md` declares — `ASSUMPTION`,
`CONDITION-WRONG`, `DELEGATED` — have no word for a departure the human licensed, and inventing a fourth here would
be a second departure to cover the first.*

## Amendment, 2026-09-25 (from node 293)

*Written by [node 293](293-rewrite-the-prototype-contract.md)'s worker and filed by the manager, after that node's work landed as commit `6d26be1`. Every word of the replacement is fixed by that commit: it quotes `expedition-prototype/SKILL.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 293's worker's search is on node 293 under `RE-POINTING SEARCH`.*

- **Entry 3.** Three replacements:
  - "It currently reads: *"the right to modify product code, held by one worker at a time. Never yours."*" becomes "It currently reads: *"the right to modify product code, held by one worker at a time. It is never yours."*"
  - "and keeps *"Never yours"*" becomes "and keeps *"It is never yours"*"
  - "its hard rule 1, *"You do not hold the code slot"*, is true under the lifecycle and is left exactly as it stands" becomes "its hard rule 1's sentence *"You do not hold the code slot."*, which is true under the lifecycle, is left exactly as it stands"

*The manager's note:* the worker reported that the sentence *"You do not hold the code slot."* is byte-identical in the after-text, and that the rest of hard rule 1 now reads "Put everything you build in `prototypes/NN-<name>/`. Keep all of it out of the product tree, and make none of it product code."

`81.2` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 293](293-rewrite-the-prototype-contract.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `6d26be1`.

## Amendment, 2026-09-26 (from node 302)

*Written by [node 302](302-rewrite-the-glossary.md)'s worker and filed by the manager, after that node's work landed as commit `de347dc`. Every word of the replacement is fixed by that commit: it quotes `CONTEXT.md`'s after-text. The minting author's condition and the earlier amendments above are left as they were. Node 302's worker's search is on node 302 under `RE-POINTING SEARCH`.*

- **Entry 2 (`Reject`).** Three replacements:
  - "Its clause *"so the node does not resolve, the working tree is cleaned, and what survives is the discovery"* is false." becomes "Its sentences *"On a reject the node does not resolve, and the working tree is cleaned. What is kept is the discovery."* are false."
  - "The rewritten clause says that" becomes "The rewritten sentences say that".
  - "*"Not a verdict on quality — a node whose code is merely wrong takes a correction round"*" becomes "*"A reject is not a verdict on quality: a node whose code is merely wrong takes a correction round."*"

*The manager's note:* the worker reported that the quoted *"The word is the human's alone; the checker's outcomes are `PASS` and `FAIL`"*, the `Code slot` entry, and both `_Avoid_` lines are byte-identical, so entries 1 and 3 need nothing.

`81.3` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 302](302-rewrite-the-glossary.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `de347dc`.

*The manager's note, 2026-09-26:* the human's "ok" to [node 328](328-group-the-open-nodes-against-the-glossary.md)'s C1(a) splits this node: its entries 1 and 2 are carried by [node 332](332-repair-the-glossarys-code-slot-reject-kinds-grilling-and-closed-text.md), and its entry 3 (the prototype contract's `code slot` line) goes to the worker-contracts merge proposed by [node 329](329-group-the-open-nodes-against-the-worker-contracts.md), which is still before the human. This node is superseded by both once that merge is filed.

## Superseded, 2026-09-26

*The manager's note.* Its entries 1 and 2 are replaced by [node 332](332-repair-the-glossarys-code-slot-reject-kinds-grilling-and-closed-text.md) (node 328's C1(a)), and its entry 3 by [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md) (node 329's option O4), both on the human's "ok".
