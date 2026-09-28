# Carry node 162's integration answer into the shipped files

Type: implementation
Status: open
Blocked by: none

## Question

Carry node 162's answer into the shipped files. Each landing policy must state what happens when integration conflicts, and a correction round may be started by the manager at integration.

*Reported by [node 162](162-how-much-of-the-integration-rule-ships.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 162's worker and filed by the manager.*

> 1. `.claude/skills/expedition/graph-conventions.md`: the bullet that begins `` - `## Landing an implementation node's work` — the landing policy: `` also says that the policy covers what happens when integrating a node's work conflicts. It becomes: "where a node's worker works, what one path-limited commit of that node's paths takes, what happens to the worker's tree on each of the gate's three outcomes, and what happens when integrating the node's work conflicts." The bullet's closing sentence, "Landing is the manager's, so neither a worker nor its checker reads this section.", is unchanged. No other sentence of the file changes, and the file names no version-control command it did not name before.
> 2. `.claude/skills/expedition-implementation/SKILL.md`, under `## Words used exactly`: the entry `- **correction round** — one cycle of the human saying what is wrong and you fixing it.` becomes `- **correction round** — one cycle of being told what is wrong, by the human at the gate or by the manager when integrating your work conflicts, and you fixing it.`
> 3. The same file, in the code block under `## After the code is written`: the line `→ approve → the manager commits; your node resolves` becomes a branch saying, in these words: `→ approve → the manager lands your work; where integrating it conflicts, you may be resumed to fix the conflicted files in place, running no git command, and the checker and the gate run again`. It may wrap over indented continuation lines inside the block. The `correct` and `reject` lines are unchanged.
> 4. The same file, near the top: the sentence `You hold a code slot from your first edit until the human has approved your work.` becomes `You hold a code slot from your first edit until your work has landed or been rejected.`
> 5. The same file, under the `In a correction round:` list: the bullet beginning `You receive the human's words exactly as they said them.` keeps its existing text and gains one sentence, `In a round the manager starts when integrating your work conflicts, you receive the conflicted files instead, and you fix them in place.`
> 6. `.claude/skills/expedition/glossary.md`, entry `**Correction round**:`: its first sentence, `One cycle of the human saying what is wrong and the worker fixing it, while the node stays claimed.`, becomes `One cycle of being told what is wrong, by the human at the gate or by the manager when integrating the work conflicts, and the worker fixing it, while the node stays claimed.` The entry's other sentences and its `_Avoid_` line are unchanged.
> 7. No other file under `.claude/skills/` changes, and no file under `.scratch/` changes.
> 8. Scope. The command `grep -rn -E 'saying what is wrong|your node resolves|until the human has approved your work|You receive the human.s words exactly' .claude/skills/`, run over the working tree before this node, returned exactly five lines: `expedition-implementation/SKILL.md` for the code-slot sentence, the correction-round entry, the approve line and the correction-round bullet, and `glossary.md` for the `Correction round` entry. Clauses 2 to 6 cover all five. The `graph-conventions.md` clause came from no search, because the place is the work. After the work, the same command returns no line saying that only the human starts a correction round or that the node resolves at approval. An instance the command reaches outside this list is reported and not edited.
