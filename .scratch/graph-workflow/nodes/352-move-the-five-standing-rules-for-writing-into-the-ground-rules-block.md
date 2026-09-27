# Move the five standing rules for writing into `map.md`'s ground-rules block

Type: implementation
Status: open
Blocked by: none

## Question

Carry out node 349's answer: move the five standing rules for writing from `map-implementation-rules.md` into the "Ground rules for this effort" block in `map.md`.

*Reported by [node 349](349-whether-the-five-standing-rules-for-writing-reach-other-workers.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 349's worker and filed by the manager.*

> The work is `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-implementation-rules.md` and `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
> 1. In `map.md`'s `## Notes`, the block that begins with the bold line "**Ground rules for this effort.**" holds, after its numbered rules 1 to 5 and before the paragraph that begins "Every rule above", a second numbered list under its own bold lead-in that names it as this effort's standing rules for writing. The list holds these five rules, each word-for-word as below, in this order and with this bolding:
>    1. **Compress the prose that explains why; never compress the shapes.**
>    2. **An item states its current form and cites the nodes that shaped it; it does not restate what they hold.**
>    3. **A long answer is navigable by heading**, so a reader following a link for one fact reads one section.
>    4. **Cite a file by heading or by a quoted phrase, never by line number.** Append-in-place shifts every line below the append, so a line number decays without anything reporting it.
>    5. **Write plain English.** State a rule as what to do; use a prohibition only where the rule cannot be said as what to do, and then beside the positive. Bold a term only where it is defined. Say any idea that is not a term defined in `CONTEXT.md` in plain words, with no figure of speech and no coined phrase. Make statements directly rather than as slogan-shaped contrasts. Write every sentence grammatically, with one clear referent for each pronoun. Put one idea in each sentence.
>    The lead-in says the rules are held against every prose deliverable, and links the nodes that fixed them: `nodes/53-what-token-findings-change.md` for the first four and `nodes/289-a-plain-english-and-compaction-pass-over-the-shipped-files.md` for the fifth. Ground rules 1 to 5 are not reworded, renumbered or reordered.
> 2. The paragraph in that block that begins "Every rule above" still follows both lists, and it is true of both. It states that every rule in both lists is a standing constraint true of any node's work, rather than an account of what happened. It does not state that the five rules for writing are drawn from a standing preference.
> 3. No sentence in `map.md` says that the five standing rules for writing are held in `map-implementation-rules.md`.
> 4. `map-implementation-rules.md` no longer holds the paragraph that begins "**Five standing rules for writing anything in this effort**" or its numbered list. Wherever the file names the five standing rules for writing, in the paragraph that begins "**The bar's commands for this repo, discovered on first use**" and in the paragraph that begins "**The review route for this repo, discovered on first use**", it says that `map.md`'s `## Notes` holds them inside the ground-rules block, and that a checker receives them as text in its spawn with the ground rules. No sentence in the file says the file holds them.
> 5. Every text this work removes from `map.md` or `map-implementation-rules.md` is appended verbatim to `map-history.md`, under a heading that mirrors the section it came from, with struck-through text staying struck through. `map-history.md` gains text and loses none.
> 6. Every markdown link in the three files resolves to a path that exists.
>
> Scope search: `grep -rn -c "rules for writing" .scratch/graph-workflow/map.md .scratch/graph-workflow/map-implementation-rules.md .scratch/graph-workflow/map-manager-only.md .claude/skills CONTEXT.md`, run over the working tree on 2026-09-27, returned 1 match in `map.md` (the pointer paragraph) and 3 in `map-implementation-rules.md` (the bar paragraph, the review route paragraph twice counted as one line, and the block's lead-in), and none elsewhere. An instance the search reaches outside the three files named above is reported and not edited.

*The manager's note, 2026-09-27:* node 56 landed (`9a87ac0`) and moved the glossary to `.claude/skills/expedition/glossary.md`. Rule 5's text in this condition still says "a term defined in `CONTEXT.md`", and the rules file's two paragraphs this node touches still name `CONTEXT.md`. The root `CONTEXT.md` is now a superseded pointer, so every such mention still resolves. The manager updates those mentions itself once this node lands, rather than amending this condition.
