# Reword `implementer` to "the worker" in the shipped files

Type: implementation
Status: claimed
Blocked by: none

## Question

Carry node 353's answer into the shipped files: the 9 uses of `implementer` become "the worker"/"a worker" (or "the implementation worker" where a sentence needs it), with no glossary headword.

*Reported by [node 353](353-whether-implementer-becomes-a-glossary-headword.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 353's worker and filed by the manager.*

> Done when all of the following hold.
> 1. Running `grep -rn -i "implementer" --exclude-dir=.scratch --exclude-dir=.git .` from the repository root returns nothing. Run over the working tree when this condition was written, it returned exactly these 9 lines, which are the whole scope of the work:
>      `.claude/skills/expedition/glossary.md:134` — "The manager starts it, and the implementer never does, because whoever spawns it"
>      `.claude/skills/expedition/SKILL.md:830` — "3. What does an implementer do with a finding it believes is false? It has no route except fixing it."
>      `.claude/skills/expedition-checker/SKILL.md:79` — "5. Your outcome goes to the manager, which sends it to the implementer."
>      `.claude/skills/expedition-checker/SKILL.md:88` — "The implementer works from the same file, so the two of you"
>      `.claude/skills/expedition-checker/SKILL.md:208` — "over the part of the work the implementer may edit."
>      `.claude/skills/expedition-checker/SKILL.md:209` — "command whose hits are mostly text the implementer may not touch"
>      `.claude/skills/expedition-checker/SKILL.md:210` — "command to text the implementer may edit is part of supplying one."
>      `.claude/skills/expedition-checker/SKILL.md:215` — "The extent lets the implementer repair every instance"
>      `.claude/skills/expedition-checker/SKILL.md:250` — "A `FAIL` sends the work back to an implementer who met the scope as written"
>    An instance the grep reaches outside this list is reported and not edited.
> 2. At each of the 9 sites, the party is now named "the worker" or "a worker", with the article adjusted to the sentence. "The implementation worker" is allowed instead where the sentence would otherwise not say which worker. No other word or coined phrase names this party at these sites.
> 3. Apart from the rename and the article changes it forces, the sentences at these sites say what they said before. No rule is added, removed or narrowed, and lines are re-wrapped only as far as the rename requires.
> 4. `.claude/skills/expedition/glossary.md` gains no headword and no `_Avoid_` line, and its entry and `_Avoid_` counts are unchanged by this work.
> 5. No file other than `.claude/skills/expedition/glossary.md`, `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition-checker/SKILL.md` is changed, and nothing under `.scratch/` is changed.
> 6. The working tree meets the bar.
