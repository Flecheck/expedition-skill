# Carry the rules on what reaches the human, the code-slot count and the gate's pointer to the work into the manager contract

Type: implementation
Status: open
Supersedes: 96, 118, 127, 161, 231
Blocked by: none

## Question

Nodes 96, 118, 127, 161 and 231 each change a few lines of the manager contract's rules on what is in front of the human, how a report ends, how many implementation nodes run, and what a gate payload points at. Make all their changes in one piece of work.

*Proposed by [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker and filed by the manager, on the human's "ok" to node 330's merge and its conflicts' recommendations. The worker wrote each condition to the recommended option of every conflict.*

*The worker's blockers:* none

## Acceptance condition

*Written by node 330's worker.*

> The work is `.claude/skills/expedition/SKILL.md`, plus `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md` for clauses 17 and 18 only. No other file changes. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`. The places named below are the work itself rather than instances of a defect spread across the tree, so this scope came from no search. `SKILL.md` is a file the workflow ships, so it is edited plainly: superseded wording is removed, and nothing in it is struck through or moved to a history file.
>
> Done means every one of the following is true of the finished tree. Each clause names, in brackets, the node its demand comes from.
>
> **What is in front of the human.** These clauses apply to the section headed `## What is in front of the human, and when`, unless a clause names another place.
>
> 1. (127, 118) The section states that at most one thing awaiting the human's reply is in front of them, and exactly one whenever something is waiting, and that nothing displaces a live one. Where that thing is a payload relayed from a worker, it may carry more than one question from that one worker and still counts as one thing.
> 2. (127) The section no longer states that exactly one *question* is in front of the human. Before this work it opens "Keep exactly one question in front of the human at a time."
> 3. (127) The file states that the manager never combines questions from different nodes into one payload, and never divides one payload's reply between two workers. A payload comes from one worker, and its reply goes back to that one worker unaltered.
> 4. (127) The rule that every relayed question names, in one line, whatever else is waiting, by node name and kind only and never restating another question or its options, is kept. The section gives as that rule's reason that a thing named in that line but not asked cannot be answered by accident. It does not justify the rule on the ground that it keeps a terse reply attributable to exactly one thing.
> 5. (118) The file states that a question occupies the human's channel only while it awaits their answer, so the channel is free from the moment the manager records their reply. It states three consequences by name:
>    - a gate answered with a correction leaves the channel free for the whole of the correction round and any re-check that follows;
>    - anything the manager sends that awaits no answer, such as the report of a pick, a notice that an agent died, or the closing report, leaves the channel free the instant it is sent;
>    - a node waiting at its gate, a worker running, or a check in flight does not occupy the channel at all.
> 6. (118) The file states that the manager sends a question that is already waiting, and never makes one up to give the human something to do.
>
> **The last line of a report**
>
> 7. (96) The file states that every report the manager puts in front of the human ends with one short line naming what is expected of them, and that this line is the last thing in the report. It states the reason: the human can look at the last line alone and know what they must act on. It states that the line names the act or the choice being asked for and is short. It prescribes no fixed set of wordings.
> 8. (118) The file states that this line says what is expected of the human at the moment it is written, and promises nothing about when the manager will next send what is waiting. It also states that a line saying nothing is expected of them is written only when nothing is waiting.
> 9. (96) Every existing statement of what a report or a payload that reaches the human must carry still holds. The new rule adds a closing line and removes nothing any section requires.
>
> **The code-slot count**
>
> 10. (161) The bullet under `### Picking the next node` beginning "How many implementation nodes run at once." states that raising the count buys parallel implementation at the price of conflicts to resolve when the work is integrated, and that the human sets the number. It states that the manager neither raises the count on its own judgement nor treats the effort's current value as a ceiling it must justify leaving. It states that the manager names this trade when the human moves the count.
> 11. (161) Under `## What nothing here settles`, the item reading "What does a worker do when a file it must read is being changed by whoever holds the code slot?" is removed, together with the two sentences after it ("Nothing says. Work that is not code runs beside an implementation node by design, including where the two touch the same file."). The items after it are renumbered so the list runs from 1 with no gap and no repeat.
> 12. (161) Text elsewhere in the file states what replaces that item. Every worker reads a consistent snapshot, an implementation worker its own working tree and every other worker the main checkout, so no worker reads a file while it is being changed. Two snapshots that differ are reconciled when the work is integrated, not while it is read.
> 13. (161) `SKILL.md` names no branch, worktree, rebase or merge command, and describes no git lifecycle.
> 14. (161) Wherever `SKILL.md` states how many items `## What nothing here settles` holds, the count agrees with the items present.
>
> **The gate payload's pointer to the work**
>
> 15. (231) Under `### The payload`, the bullet that before this work reads "Where the work is, and the command that shows its diff. A gate that describes a change and points at nothing has not been presented." still requires the payload to say where the work is, by the path of the working tree that holds it. It still says that a gate which describes a change and points at nothing has not been presented. Neither that bullet nor any other sentence of `SKILL.md` asks for a command that shows the diff.
> 16. (231) In the table under `## What is never yours`, the row whose first cell is "rendering a diff into the conversation" keeps that first cell. Its second cell, which before this work reads "say where the work is and what command shows it", says where the work is and names no command. The sentence "Keep two things out of the payload: the diff, and the acceptance condition." still stands.
> 17. (231) In `.scratch/graph-workflow/map-manager-only.md`, under `## Landing an implementation node's work`, the sentence that before this work begins "**The gate payload names the worktree's path and the command that shows its diff**" no longer requires the command that shows the diff, and still requires the gate payload to name the worktree's path. The rest of that sentence, including the ground it gives, keeps its meaning. Nothing else in that file changes.
> 18. (231) The rule text that clause 17 replaces is appended verbatim to `.scratch/graph-workflow/map-history.md`, under a heading mirroring the section it came from, with struck-through text staying struck through. `map-history.md` gains text and loses none.
>
> **What does not change**
>
> 19. (118, 127) These keep their meaning:
>     - that nothing displaces a live question;
>     - the two tiers, tier 1's three fixed kinds, and that only the human can add a fourth kind;
>     - that things within a tier are taken in the order they arrived;
>     - the list beginning "Three things never enter the queue:", together with the three things it lists, neither extended nor renumbered.
> 20. (118) The statements under `## The order you act in` keep their meaning, in particular "The human should always have something to do", "A turn that ends with the human idle while something waits is your defect", and the check at item 5 that is run before the manager writes that nothing is expected of the human.
> 21. (96) Under `## What nothing here settles`, the item asking "What must your report to the human contain?" still stands as an unsettled question. The only item this work removes from that list is the one clause 11 removes.
> 22. (96, 118, 127, 161) No section of `SKILL.md` is removed, and no rule in it changes its meaning other than as clauses 1 to 16 state.
> 23. The working tree meets the bar.
