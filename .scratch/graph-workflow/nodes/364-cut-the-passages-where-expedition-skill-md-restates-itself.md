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
