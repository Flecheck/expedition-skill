# Ship the checker's check of a node's flags

Type: implementation
Status: open
Blocked by: none

## Question

Carry node 30's answer into the checker contract and the manager contract.

*Reported by [node 30](30-checking-a-flag-before-the-human.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none"*

## Acceptance condition

*Authored by node 30's worker and filed by the manager.*

> The work is `.claude/skills/expedition-checker/SKILL.md` and `.claude/skills/expedition/SKILL.md`, and no other file may be edited. These are files the workflow ships, so superseded wording is removed rather than struck, and nothing is moved to any history file. The worker may not mark this node, resolve it, or write a line in any index file.
>
> Done means all of the following are true of the finished tree.
>
> In `.claude/skills/expedition-checker/SKILL.md`:
>
> 1. Under `## What you are given`, the numbered list gains a seventh item: the flags the work's node holds, each as one sentence with its id, given as text by the spawn. The item says that a flag is a judgement another agent recorded about this work, and that this given is absent where the node holds no flags. The sentence introducing the list states the new count, and states correctly which givens the spawn carries and which one the checker reads for itself.
> 2. The paragraph beginning "The six givens above are everything you are given" no longer says "six". It states its closure as protection of the record: the record stays unread, and a flag given under item 7 is a claim about the work, not part of the record. The paragraph's other sentences keep their words. That includes "The one exception is `map-implementation-rules.md`, and only for the standards in it." and "A path you were given as the work is the work wherever it sits, and you read it."
> 3. A section headed `### The flags, after your outcome` is added under `## What you hand back`. It states all of the following:
>    (a) Check the flags only after reaching your `PASS` or `FAIL`, and change no outcome because of them.
>    (b) For each flag, establish one of three things: what it says was done is true of the work, it is false, or it makes no claim the work can make true or false.
>    (c) Judge only whether what the flag says was done is true of the work, never whether the judgement was right, and ignore any reason the flag gives.
>    (d) Report a false flag, and only a false flag, under `QUESTIONS:`, naming the flag's id and the search that showed it false.
> 4. In `### Questions, alongside a \`PASS\` or a \`FAIL\``, the sentence that counts the kinds of question states the new count, and a false flag is described there as one kind. The section points at `### The flags, after your outcome` rather than restating it.
> 5. No heading of the file is renamed. No sentence outside clauses 1 to 4 changes in content. The table under `### When what you check against is itself the problem` is not changed by this work.
>
> In `.claude/skills/expedition/SKILL.md`:
>
> 6. In `## The checker`, the list after "The checker receives the following:" gains one item: on the check of an implementation node, every run, the flags the node holds, each as its sentence from `flags.md` with its id and without the link to its node.
> 7. The sentence "The checker receives nothing from the effort's own record, so its spawn never points it at the node file." is changed so that it makes the flag sentences of clause 6 its only exception, and it still says that the spawn never points the checker at the node file.
> 8. In `## What nothing here settles`, the item beginning "Does anything check a flag before the human settles it?" is removed, and the items after it are renumbered in their existing order. The bullet "The scribe rule against the fuller form of a flag." under `## Conflicts this contract leaves open` is not changed.
>
> Both files:
>
> 9. Compared with the commit the work starts from, `.claude/skills/expedition-checker/SKILL.md` grows by no more than 15 lines, and `.claude/skills/expedition/SKILL.md` does not grow. Line counts are those printed by `wc -l`.
> 10. Every markdown link in both files resolves to a path that exists.
> 11. The working tree meets the bar.
>
> Scope: the places named are the work, not instances of a defect. One search was run to find the count words a seventh given would make wrong: `grep -n -w -i 'six\|five' .claude/skills/expedition-checker/SKILL.md` returned two lines, "You are given six things. The spawn carries the first five, and you read the sixth for yourself from one" and "The six givens above are everything you are given.", which clauses 1 and 2 cover. A count word that this search reaches outside those two lines is reported, not edited.
