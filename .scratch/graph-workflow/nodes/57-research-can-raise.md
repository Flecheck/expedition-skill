# Give a research node the cannot-proceed raise

Type: implementation
Status: open

## Question

A `research` worker that can do nothing has no channel. [When an AFK worker cannot
proceed](23-worker-cannot-proceed.md) built the cannot-proceed raise and gave it to the implementer, the checker
and — at that node's gate — the `precondition` kind. **`research` was excluded deliberately.** Give it the
channel.

**The human's instruction, `verbatim`:** *"I think a research node should be able to raise when it can do
nothing."*

**This reverses the human's own earlier decision rather than filling a gap they had not considered.** At node
23's gate they said *"I guess precondition could raise, as it is more reseach that is supposed to be fully
autonomous"* — extending the channel one kind and naming `research` as the kind meant to need nobody. That node
records the exclusion as resting *"on the human's own reasoning rather than on the glossary's"*, and
[`CONTEXT.md`](../../../CONTEXT.md) says a research node *"never involves the human"*. Both are superseded, and
saying so is part of the work.

**What made the case concrete.** [Review every shipped file against
`/writing-great-skills`](47-review-shipped-skills.md)'s worker met a real blocker — its own contract told it to
invoke `/research`, which instructs it to write a file its hard rule 1 forbids outright — and had nowhere to put
it. Its words, on flag `47.1`: *"A research node has no raise channel, so a flag was the only outlet."* A flag
waits for the closing report; the worker resolved the conflict itself and carried on. **[Re-review the shipped
files against `/writing-for-agents`](54-review-against-writing-for-agents.md)'s worker then hit the identical
blocker and did the same.** Two workers, one session, no channel.

Reported by the human's steering during [What the token findings change in the workflow and its
skills](53-what-token-findings-change.md)'s interview, and **not** part of that node's subject.

## Acceptance condition

*Written by the manager, for a node the manager minted from the human's steering.* Marked as the manager's own
under [Who writes the acceptance condition for an implementation node the manager mints
itself](39-condition-for-a-manager-minted-node.md), whose constraint 1 confines it to what is already fixed.
**Everything below is fixed by a resolved node or by a shipped file; where the form is not fixed, this condition
states the property and leaves the form to the worker.**

1. `.claude/skills/expedition-research/SKILL.md` gives its worker the cannot-proceed raise, on the **same
   threshold and in the same terms** as `.claude/skills/expedition-precondition/SKILL.md` already states it.
   Where the precondition contract's wording depends on something untrue of a research node, the research
   contract says the true thing instead and the difference is reported; where it does not, the two agree.
2. That contract's hard rule 3, which today reads *"You have no way to reach the human, and nothing you hand
   back waits on them"*, is no longer true as written and is no longer stated as written. What replaces it keeps
   the part that is still true — that a research node's **ordinary** work never involves the human and nothing
   it hands back waits on them — and states the exception this node creates.
3. The raise is **not** a fourth return variant. It reuses the question shape [Subagent context
   contract](12-subagent-context-contract.md) fixed and node 23 reused, which is what made the channel cheap for
   every kind that already has it.
4. Nothing about the other five contracts changes: not the checker's, and not the four that already carry the
   channel or state they do not need it.
5. `CONTEXT.md`'s `research` entry no longer says a research node *"never involves the human"* without
   qualification. Its `_Avoid_` line is unchanged and no other entry is edited.
6. The working tree meets the bar.

### Two things the manager owes whoever claims this

*Not changes to the condition above.*

**Clause 5 collides with a file that is moving.** [Ship the glossary inside the skill directory and make it
state its own completeness](56-ship-the-glossary-into-the-skill-set.md) moves `CONTEXT.md` into
`.claude/skills/expedition/` and rewrites its head. Clause 5 names no path, so it survives the move — but the
two nodes are **not concurrently claimable**, both editing the glossary, and whichever lands second inherits a
file the other moved. Neither blocks the other.

**This node is not token-use work**, and the human's standing instruction is *"only run stuff about lowering
token use for now"*. It is recorded and deliberately **not started**. It is also not urgent in the way it looks:
both workers that hit the blocker resolved it themselves and reported it, so the channel's absence has cost two
flags and no wrong result.

## Amendment, 2026-09-24

*Written by [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s worker and filed by the manager, after that node's work landed as commit `4068519`. Every word of each replacement is fixed by that commit: it quotes the research contract's after-text. The minting author's condition above is left as it was, and these replacements take the place of the clauses they name.*

Node 290's worker searched every open node's `## Acceptance condition` for quoted spans of the research contract's before-text, for mentions of the file, and for each piece of wording its rewrite removed or replaced. The full list of handles is on node 290 under `### Re-pointing duty` and `### Correction round 1`.

- **Clause 2.** Replace "which today reads *"You have no way to reach the human, and nothing you hand back waits on them"*" with "which today reads *"Do your work without the human. You have no way to reach the human, and nothing you hand back waits on them."*". The rest of the clause is unchanged.

## Flags

`57.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 290](290-rewrite-the-research-contract-as-the-pilot.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `4068519`.
