# Cut the passages where `expedition/SKILL.md` restates itself

Type: implementation
Status: claimed
Blocked by: none

## Question

Can the passages of `.claude/skills/expedition/SKILL.md` that restate a rule the same file states at another heading be cut or turned into pointers to that heading, without losing a rule?

*Reported by [node 362](362-where-expedition-skill-md-restates-itself.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 362's worker and filed by the manager.*

> Scope: the scope came from no search command. The places are a bounding set: node 362's worker read `.claude/skills/expedition/SKILL.md` in full and listed the passages below from that reading. If you find another passage of that file that restates a rule the same file states elsewhere, report it and do not edit it.
>
> All clauses concern `.claude/skills/expedition/SKILL.md`.
>
> 1. `## The gate`: the paragraph beginning "A gate that a standing yes covers" is removed. The last paragraph of `## What is in front of the human, and when`, beginning "An item that a standing yes covers", stays and still names the skill `expedition-standing-yes`.
> 2. `## The order you act in`, item 5, the bullet beginning "Nothing is waiting when there is": it no longer lists the four kinds (gate assembled and unsent, worker blocked on a raise, the manager's own raise, relayed question). It says instead that nothing is waiting when the pending queue under `## What is in front of the human, and when` holds nothing. It still requires saying which of the queue's kinds were checked, and it still says that a gate whose check will not pass is still waiting. `.claude/rules/expedition-triggers.md` is not changed.
> 3. `## The order you act in`, the paragraph after the numbered list: the sentence beginning "So make the last line of what you send" is removed or replaced by a sentence naming `### The last line of a report`. The sentence beginning "A turn that ends with the human idle" stays.
> 4. `## Words used exactly`, the bullet beginning "You own the map.": it no longer states where the ground rules and the standing steering live, and names `### Standing steering, and standing instructions of one effort` for that. Its sentences about where the map records the bar's commands, and about confirming that record against the repo, stay.
> 5. `## What is in front of the human, and when`, the paragraph beginning "A gate waits in arrival order": it no longer restates that a gate is sent after every older thing in tier 1, which the sentence "Within a tier, take things in the order they arrived." already states. It still states that a gate keeps its place in arrival order although it holds a code slot while it waits, and that the manager never moves a gate ahead on its own judgement.
> 6. `## What is in front of the human, and when`: the section states only once that tier 1's membership is fixed and that only the human can add a kind to it. The sentence "Tier 1 keeps its three kinds." is removed. The paragraph beginning "A checker's question never enters the queue" still states that a checker's question never enters the queue and travels inside the gate payload.
> 7. `## What is in front of the human, and when`, the bullet beginning "Settling a flag.": it no longer states when a flag settles. For that it names `## Flags`.
> 8. `### Picking the next node`: the sentence "Those flags settle at the node closing report, so a flag it leaves out is settled without the human seeing it." is removed. The sentence stating that a node closing report carries every flag the node holds, in the fuller form under `### A flag in a payload`, stays.
> 9. `### A flag in a payload`: the sentence "A gate taken under a standing yes settles no flag." is removed. `## Flags` still states that a gate taken under a standing yes is not put to the human and that its node's flags settle at its node closing report.
> 10. `### Standing steering, and standing instructions of one effort`: the section states each of the following once. A standing rule binds an effort only once it is written into that effort's map, and it is written there when the human states it. The next effort starts without it. A rule reaches a shipped skill file only on the human's word, as a node, and never on the manager's own judgement, even where the manager judges the rule to be about the workflow rather than about the effort. Where the human says nothing about a rule's scope, the rule is the effort's alone. The paragraph beginning "The map is a rule's ordinary home" no longer exists as a separate restatement. The section's two bullets, its statement that a standing instruction is recorded as the human's in their words and never presented as a rule of the workflow, and its paragraph beginning "Every worker on an effort is bound" stay.
> 11. `## When an agent dies or is stopped`: the section says only once that whether a resume is possible is found by attempting it and never predicted. The paragraph beginning "Where an attempt's agent carries the mark of a stop from the human's side" no longer restates that such an attempt is not replaced without the human's answer. It still says to keep the node claimed and not to retry the resume, and it still gives the one question with what it names, what would be lost, and its two choices.
> 12. The rule that an attempt recorded as a final stop is never resumed is stated once in the file: either in `## Stopping a running worker` item 5 or in the first paragraph of `## When an agent dies or is stopped`.
> 13. `### Picking the next node`: the sentence "An implementation node is startable when its acceptance condition can be written in full, with nothing in it waiting on an open question." is removed. `### Where you cannot write one in full` still states that the node is not claimed until the condition is complete.
> 14. `### Changing one after it is written`: the sentence "The worker holding the node works to meet the condition as written, and never rewrites it." is removed. The sentence stating that a condition a worker already holds is handed over as written stays.
> 15. For each passage changed under clauses 1 to 14, every statement it no longer holds is still stated at the heading or passage the clause names. No rule is lost.
> 16. These passages are not changed: the bullet of `## Words used exactly` beginning "A dead attempt is resumed", and the paragraph of `## Flags` beginning "Flags reach the effort closing report".
> 17. No heading in `.claude/skills/expedition/SKILL.md` is renamed, added or removed. Every heading a changed passage names exists in the file with exactly the named text.
> 18. No file other than `.claude/skills/expedition/SKILL.md` changes.

*The worker's note for the manager, pasted:* "open node 89 also changes `.claude/skills/expedition/SKILL.md`, and open node 359 cites its headings (this node renames none). Check for overlapping edits before you fill a slot."

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-28. The worker's own text, pasted.*

````
HANDOVER:      Cut the passages where `expedition/SKILL.md` restates itself

ANSWER:

## Answer

`.claude/skills/expedition/SKILL.md` no longer holds the fourteen passages where it restated itself. It went from 9,409 words to 9,070 (`wc -w`), which cuts 339 words. No heading was renamed, added or removed: I diffed the `^#` lines against `HEAD` and they are identical. Every heading a changed passage now names exists with that exact text. No other file changed. Every quoted opening in the condition still matched the file at `53c4be7`, which is byte-identical to master.

Per clause:

1. `## The gate`: the standing-yes paragraph is removed. The standing-yes paragraph at the end of `## What is in front of the human, and when` is untouched.
2. Item 5, second bullet, now reads: "Nothing is waiting when the pending queue under `## What is in front of the human, and when` holds nothing. Say which of its kinds you checked. A gate whose check will not pass is still waiting." I also dropped the claim that all four kinds are "fixed". The queue section fixes only tier 1, so keeping the word would have added a fresh restatement.
3. The "So make the last line…" sentence became "End what you send as `### The last line of a report` says." The "A turn that ends with the human idle" sentence stays.
4. The "You own the map." bullet now names `### Standing steering, and standing instructions of one effort` for which of the human's rules and steering the map holds. Its two sentences on the bar's commands stay. This also removes the old "nowhere else", which contradicted that section.
5. The arrival-order paragraph is now only "Keep a gate at its place in arrival order even though it holds a code slot while it waits. Never move a gate ahead on your own judgement."
6. The tier 1 fact is stated once, where the list is introduced: "Tier 1 holds exactly three kinds of thing. Its membership is fixed, and only the human can add a kind to it:". Two sentences are removed: "Only the human can add a fourth kind to tier 1. Never infer one yourself." and "Tier 1 keeps its three kinds.". The checker-question paragraph keeps "never enters the queue" and "travels inside the gate payload, so it needs no place in tier 1."
7. The "Settling a flag." bullet now reads "Settling a flag. `## Flags` says when it happens."
8. and 9. The two flag-settling sentences are removed. `## Flags` still holds the standing-yes case.
10. `### Standing steering…`: the "ordinary home" paragraph is gone. Also removed from the binding paragraph: "Until it is there, it binds nobody." and "This holds for rules of conduct…". Both repeat that paragraph's own first sentence, whose "whether about what to work on or about how work is done" already covers conduct. The shipped-file paragraph is folded into: "A rule reaches a shipped skill file only on the human's word, and it does so as a node. Never carry one there on your own judgement, even where you judge the rule to be about the workflow rather than about the effort." The scope-silence sentence follows it. "The next effort starts without it." now appears once, in the standing-instruction paragraph. The bullets, the "record it as theirs" sentence and the "Every worker on an effort is bound" paragraph stay.
11. `## When an agent dies or is stopped`: "so test whether a resume is possible, and never predict it" is removed, and "A failed resume starts no agent and costs nothing." stays as the reason. The human-side-stop paragraph drops "do not replace the attempt on your own". It keeps "do not retry the resume", keeping the node claimed, and the one question with its two choices.
12. The final-stop rule now lives only in `## Stopping a running worker` item 5, which is unchanged. I removed "An attempt recorded as a final stop is never resumed." from the first paragraph of `## When an agent dies or is stopped`.
13. and 14. The two sentences are removed. `### Where you cannot write one in full` and "its condition is handed over as written" stay.
16. The dead-attempt bullet and "Flags reach the effort closing report" are unchanged.

Every edited paragraph is rewrapped to the file's 105-column width.

`.claude/rules/expedition-triggers.md` is not changed, because clause 2 forbids it. The map's rules file asks whoever edits the governing statement of the priority to edit that file in the same edit, or say why not. The reason is that the rule itself did not change. The bullet now points at the queue instead of listing its four kinds, and the triggers file's copy of the four kinds still matches the queue section.

INDEX LINE:    `expedition/SKILL.md` cut fourteen self-restatements (339 words, 9,409 to 9,070) into pointers or single statements, headings unchanged, triggers file untouched by condition.

FLAGS:
ASSUMPTION: In clause 10 I also cut two sentences the condition does not name, "Until it is there, it binds nobody." and "This holds for rules of conduct as well as for steering about what gets worked." Both sit in the section clause 10 says must state each thing once, and both restate that same paragraph's first sentence. In clause 2 I dropped the word "fixed" for all four queue kinds, because `## What is in front of the human, and when` fixes only tier 1. In clause 6 I dropped "Never infer one yourself" as covered by "only the human can add a kind to it". I left the rest of the checker-question paragraph ("so it needs no place in tier 1") as it was, since the condition asks only for "Tier 1 keeps its three kinds." to go. I did all this work alone, with no exchange with the human.
Index: node 364's worker also cut two self-restating sentences inside clause 10's section and one "Never infer" sentence in the tier 1 passage, which the condition did not name but whose sections it required to say each rule once.

NEW NODES:     none

INVALIDATIONS: none. No resolved node's answer is contradicted. Node 362's answer measured these passages, and this work carries out its Tier 1 list minus item 4, which is held for node 360.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open or claimed node except 364 for each removed phrase: "Tier 1 keeps", "final stop", "settles no flag", "ordinary home", "nowhere else", "startable when", "never rewrites", "never predict", "every older thing", "fourth kind", "Never infer", "moment that already exists", "last line of what you send", "fixed membership", "binds nobody", "A gate that a standing yes covers", "Nothing is waiting when", "You own the map", "A gate waits in arrival order", "Settling a flag", "rules of conduct", "do not replace the attempt on". I also searched for the path `expedition/SKILL.md`. Findings:
- Node 359's clause 6 names `## Flags` in SKILL.md for the standing-yes flag rule. That heading and its sentence still exist, so no change is needed.
- Node 359's clause 2 names `## When an agent dies or is stopped`, which still exists and still holds the replacement rules.
- Node 157 matched "never rewrites" in a different rule, hard rule 3's "never rewrites history". It is not affected.
- Node 317 concerns `## Flags`' "Flags reach the effort closing report" and `## Closing an effort`, both unchanged.
- Node 89 requires the existing headings to remain. They do.
- Node 34 cites `SKILL.md:830` by line number. Lines have shifted by about 20, but that is a manager's note, not a condition clause.
No replacement clauses. No open node's question is changed.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet (no checker has run).
- Paths touched: `.claude/skills/expedition/SKILL.md` (in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/364-self-restate`, branch `worktree-364-self-restate`, uncommitted).
- The bar: I confirmed against the repo that there is still no manifest, build, tests, formatter or CI (the root holds only `.claude`, `CONTEXT.md`, `CONTEXT-MAP.md`, `.gitignore`, `.scratch`). This matches the rules file. The bar is its non-command half: the glossary's `_Avoid_` lines, where the only hit is "queue", which is refused only for the frontier, while "pending queue" is this file's own term; the ground rules and the rules for writing; and the wrap width, with no prose line over 105 columns. No method skill was invoked, so nothing was skipped.
- Proposed commit message:
  ```
  Cut the passages where expedition/SKILL.md restates itself

  Fourteen passages that restated a rule the same file states at another
  heading are removed or turned into pointers to that heading. The file
  goes from 9,409 to 9,070 words; no heading changes.

  Node: graph-workflow/364
  ```

RETROSPECTIVE
1. What I had to hunt for: nothing much. The only real judgement was clause 12, where item 5 says "not to be resumed" in two forms inside the one item. I kept item 5 and cut the sentence in the other section.
2. What arrived that this node did not need: node 362's Tier 2 section and the manager's note about wrap width. Both were cheap. The condition quoted every opening, so the measurement was mostly confirmation.
3. What would have made this easier: the condition could say whether cutting nearby restatements inside a named section is in scope. Clause 10 says "each once", which implies it is, but clause 6's checker paragraph was left ambiguous.
4. What was stale, wrong or contradictory: nothing stale, since every quoted opening matched. One small inaccuracy: the old item 5 bullet called all four queue kinds a "fixed membership", while the queue section fixes only tier 1. The new text no longer claims it. The triggers file's copy still lists the four kinds, which is consistent but now the only enumeration outside the queue section.
````

## Flags

`364.1` `ASSUMPTION` — In clause 10 I also cut two sentences the condition does not name, "Until it is there, it binds nobody." and "This holds for rules of conduct as well as for steering about what gets worked." Both sit in the section clause 10 says must state each thing once, and both restate that same paragraph's first sentence. In clause 2 I dropped the word "fixed" for all four queue kinds, because `## What is in front of the human, and when` fixes only tier 1. In clause 6 I dropped "Never infer one yourself" as covered by "only the human can add a kind to it". I left the rest of the checker-question paragraph ("so it needs no place in tier 1") as it was, since the condition asks only for "Tier 1 keeps its three kinds." to go. I did all this work alone, with no exchange with the human.
