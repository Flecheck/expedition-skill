# Carry the method-skill deletion into the four worker contracts

Type: implementation
Status: claimed

Blocked by: none

## Question

*Surfaced by [Whether the contracts' instruction to invoke a method skill is doing any
work](113-whether-the-method-skill-instruction-does-any-work.md)'s worker, and pasted as it wrote it.*

> Make the four contracts state their discipline unconditionally and name no method skill.

**Blockers, in the worker's words:** *"none; composes with node 126 in either order."*

## Acceptance condition

*Written by node 113's worker. Pasted as it wrote it, and not the manager's.*

> All four of the following files, and nothing else, are changed:
> `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-implementation/SKILL.md`,
> `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`.
>
> 1. In each of the four, the sentence instructing the worker to invoke a method skill is gone. Those sentences are,
>    one per file: *"Invoke `/grilling` and `/domain-modeling` if they are present."*; *"Invoke `/coding-principles`
>    and `/naming` if they are present."*; *"Invoke `/research` if it is present."*; *"Invoke `/prototype` if it is
>    present."*
> 2. In each of the four, the sentence making the discipline conditional on the skill's absence is gone. Those
>    sentences are: *"Where they are not present, this is the whole of the discipline:"* (grilling); *"Where they are
>    not present, the bar and the acceptance condition are what bind you."* (implementation); *"Where it is not
>    present, rules 4 to 6 above are the whole of the discipline."* (research); *"Where it is not present, this is
>    the whole of the discipline:"* (prototype). Where the surrounding text needs a lead-in so the list or clause
>    still reads, it is written unconditionally — stating that this is the discipline, not that it is the discipline
>    in some circumstance.
> 3. No file among the four contains the string `/grilling`, `/domain-modeling`, `/coding-principles`, `/naming`,
>    `/research`, `/prototype`, `mattpocock`, or any other name of an external skill, in any sentence telling the
>    worker to invoke, consult, load or read one.
> 4. The paragraph beginning *"Where a method skill's instructions and this contract's hard rules conflict, the hard
>    rules govern."* is **retained unchanged** in all four files, including its list of three colliding instructions
>    and its instruction to leave the conflicting part unrun and report it.
> 5. `.claude/skills/expedition-grilling/SKILL.md` states both of the following in its own text, as items in its
>    discipline: that the worker works the decisions in dependency order, a decision branching into the decisions
>    that hang off it, so that a question whose answer depends on one not yet asked waits for it; and that finding
>    facts is the worker's own job and never the human's, so where a question needs a fact from the tree or the
>    environment the worker reads it or dispatches a subagent for it, and does not hold up its other questions while
>    that search runs. Neither item uses the word "frontier". Where the file already states an item in its own text,
>    that item counts as met and is not duplicated.
> 6. Nothing in any of the four files makes any part of its discipline conditional on any skill being present or
>    absent.
> 7. No file outside the four listed above is changed.
>
> Held against the bar.

## The manager's note at filing

*Not a change to anything above.*

**This condition names its scope as four files and quotes the exact sentence to remove from each**, which is [node
94](94-condition-scope-as-a-predicate.md)'s rung 3 case — a scope not derived from a search — even though clause 3 is
a whole-file predicate over those same four. The manager has **not** amended it and reads clause 3's domain as the
four named files rather than the tree, which is what makes it well-formed; **that reading is the manager's** and is
correctable.

**One collision the manager sequences rather than the worker.** [Node
126](126-carry-question-batching-into-the-grilling-contract.md) edits the same grilling contract, and its clause 9
already forbids the construction clause 2 here removes. The surfacing worker judged that they *"compose in either
order"*. With a code slot of one they serialise, and whichever runs second reads a file the other moved.
