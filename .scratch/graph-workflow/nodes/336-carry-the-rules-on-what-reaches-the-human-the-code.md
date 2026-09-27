# Carry the rules on what reaches the human, the code-slot count and the gate's pointer to the work into the manager contract

Type: implementation
Status: resolved
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

## Answer

The manager contract now keeps one thing awaiting the human, not one question. It frees the channel on reply, ends every report with a what-is-expected line, leaves the code-slot count to the human, and drops the diff command.

*The manager's note:* the worker's answer is under `## Handover, attempt 1` and its two correction rounds. The checker failed runs 1 and 2 on the record edit's citation and passed run 3. The human approved. The contract landed as commit `5c12368`; the manager carried the `map-manager-only.md` sentence and the `map-history.md` section into the main record. The node the worker surfaced was folded into node 335.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Carry the rules on what reaches the human, the code-slot count and the gate's pointer to the work into the manager contract

ANSWER:        The manager contract, `.claude/skills/expedition/SKILL.md`, now carries the changes of superseded nodes 96, 118, 127, 161 and 231, plus node 333's amendment. It is edited plainly, with nothing struck through.
               - **One thing, not one question (127, 118).** The opening of `## What is in front of the human, and when` now says: at most one thing awaiting the human's reply is in front of them, and exactly one whenever something is waiting. Nothing displaces a live one. A payload relayed from one worker may carry several of that worker's questions and still counts as one thing. A new paragraph says the manager never combines questions from different nodes into one payload, and never divides one payload's reply between two workers. A payload's reply goes back unaltered to the one worker it came from. The contract's opening job statement also said "keep exactly one question in front of the human". It now says "keep one thing awaiting the human's reply in front of them whenever something is waiting", so the file does not contradict itself (flag 1).
               - **The channel (118).** A new paragraph says a question occupies the human's channel only while it awaits their answer, so the channel is free from the moment the manager records the reply. Three consequences are listed: a gate answered with a correction frees the channel for the correction round and any re-check; anything that awaits no answer (a pick report, an agent-died notice, the closing report) frees it the instant it is sent; a node waiting at its gate, a running worker or a check in flight does not occupy it. It adds: send a question that is already waiting, and never make one up to give the human something to do.
               - **The waiting line's reason (127).** The bullet that says every relayed question names whatever else is waiting now gives its reason: a thing named in that line but not asked cannot be answered by accident. It gives no attributability reason.
               - **The last line of a report (96, 118).** A new subsection, `### The last line of a report`, sits at the end of the in-front-of-the-human section, before `### Picking the next node`. It says:
                 - every report ends with one short line naming what is expected of the human, and that line is the last thing in the report;
                 - the reason is that the human can read the last line alone and know what to act on;
                 - the line names the act or choice being asked for, in whatever words fit the case;
                 - it says what is expected at the moment it is written and promises nothing about when the next waiting thing is sent;
                 - a nothing-is-expected line is written only when nothing is waiting;
                 - the line is added to whatever else a report or payload must carry and replaces none of it.
               - **The code-slot count (161).** The code-slot bullet under `### Picking the next node` now says:
                 - raising the count buys parallel implementation at the price of conflicts to resolve when the work is integrated;
                 - the human sets the number;
                 - the manager never raises it on its own judgement, and never treats the current value as a ceiling it must justify leaving;
                 - the manager names this trade when the human moves the count.
                 A new paragraph after the two counts says every worker reads a consistent snapshot: an implementation worker its own working tree, every other worker the main checkout. So no worker reads a file while it is being changed, and snapshots that differ are reconciled at integration. The old item 5 of `## What nothing here settles` (a file being changed by the code-slot holder) is removed with its two sentences, and items 6 to 8 become 5 to 7. The file names no branch, worktree, rebase or merge command. It states no count of that list anywhere.
               - **The gate's pointer to the work (231).** The payload bullet now reads "Where the work is: the path of the working tree that holds it. A gate that describes a change and points at nothing has not been presented." In the `## What is never yours` table, the row "rendering a diff into the conversation" now says "say where the work is". No sentence asks for a diff command.
               - **Handover parts (333 amendment).** The `## Words used exactly` bullet now reads "A handover has seven parts every time". It lists the answer, the index line, the flags, the nodes surfaced, `INVALIDATIONS`, `CONDITIONS` and `MISSING FROM MAP`, and says an implementation worker returns an eighth, the gate payload.
               - **Record files (clauses 17 and 18).** In `.scratch/graph-workflow/map-manager-only.md`, under `## Landing an implementation node's work`, the bold lead now reads "**The gate payload names the worktree's path**". The ground after it ("because an implementation node's work is uncommitted…") is unchanged, and nothing else in that file changed. The old sentence is appended verbatim to `.scratch/graph-workflow/map-history.md` under a new section, `## Superseded from `map-manager-only.md` at node 336 — the gate payload's command that shows the diff`, with a sub-heading `### From *Landing an implementation node's work* — the gate payload's sentence`.
               - **Unchanged:** the two tiers and the three fixed kinds in tier 1; arrival order; the "Three things never enter the queue:" list; everything under `## The order you act in`; and the item "What must your report to the human contain?". No section was removed.

INDEX LINE:    The manager contract now keeps one thing awaiting the human, not one question. It frees the channel on reply, ends every report with a what-is-expected line, leaves the code-slot count to the human, and drops the diff command.

FLAGS:         ASSUMPTION: The contract's opening job statement said "keep exactly one question in front of the human". That sentence is outside the section clauses 1 and 2 name. I changed it to "keep one thing awaiting the human's reply in front of them whenever something is waiting", because leaving it would contradict clause 1's rule in the same file. Clause 22 allows a meaning change of the kind clauses 1 to 16 state, and this is clause 1's.
               Index: Node 336 also reworded the manager contract's opening job statement from "one question" to "one thing awaiting the human's reply", to match its new one-thing rule.
               ASSUMPTION: The condition names no place for three pieces of text, so I placed them myself. The last-line rule (clauses 7 and 8) is a new subsection, `### The last line of a report`, at the end of `## What is in front of the human, and when`. The consistent-snapshot text (clause 12) is a paragraph under `### Picking the next node`, after the two counts, because it replaces a question about work that runs in parallel. The channel paragraph (clauses 5 and 6) comes straight after the one-thing rule.
               Index: Node 336 placed the last-line rule in a new subsection of the manager contract's in-front-of-the-human section, and the consistent-snapshot rule under Picking the next node.
               ASSUMPTION: The amendment names its bullet by the phrase it begins with, "A handover has five parts every time". The same amendment makes that bullet say seven parts, so it now begins "A handover has seven parts every time". I took the old phrase as the bullet's identity before this work.
               Index: Node 336 rewrote the manager contract's "A handover has five parts" bullet to say seven, plus the gate payload as an eighth, as node 333's amendment required.

NEW NODES:     Name: The glossary's Handover entry lists five parts where the contracts list seven
               Kind: implementation
               Question: `CONTEXT.md`'s `**Handover**:` entry says a handover is "its node's answer written as the node will hold it, the index line, its flags, the new nodes it found, and the nodes it invalidated". Since commit `5acd220` the worker contracts and now the manager contract list two more parts, `CONDITIONS` and `MISSING FROM MAP`. Bring the entry into line.
               Blockers: none
               Acceptance condition: The work is `CONTEXT.md`. No other file changes. The `**Handover**:` entry lists what a worker returns as seven parts: its node's answer written as the node will hold it, the index line, its flags, the new nodes it found, which resolved node its work changes, the open conditions it searched and any replacement clauses it wrote, and what `map.md` did not tell it. It says an implementation worker returns an eighth part, the gate payload. The entry's last sentence, "The manager files it unaltered.", and its `_Avoid_` line are unchanged. The working tree meets the bar.
               (Under the standing rule that a related defect joins a node that already exists, the manager may fold this into an open, unclaimed glossary node instead of minting it. I found none open while searching, but did not look beyond the conditions search below.)

INVALIDATIONS: - Node 16, "What the manager works on next, and how the human redirects it" ("one live question with two tiers behind it"): narrowed in wording. What is live is now one *thing* awaiting reply, which may be a multi-question payload from one worker. The tiers are unchanged.
               - Node 298, "Rewrite the manager contract part 3": extended. Its section gains three paragraphs and a subsection, and loses one item of `## What nothing here settles`.
               - `map.md`'s `## Notes`, for the manager's own bookkeeping (a record file, not a resolved node):
                 - The bullet beginning "**A gate payload does not carry a command that prints a diff.**" says carrying the rule into the landing policy and the shipped manager contract "is node 231; until that lands…". It is now carried, by node 336.
                 - The bullet beginning "**Every report the manager puts in front of the human ends with one short line…**" says it is "Being shipped by node 96". It is now shipped, by node 336.
                 - The bullet stating "**exactly one question is in front of the human**" is now narrower than the shipped rule, which counts one thing.
               - `CONTEXT.md`'s Handover entry is stale against the manager contract (see NEW NODES).

CONDITIONS:    I ran `.scratch/graph-workflow/scripts/search-conditions.py 336` over both changed rule files, from `5acd220:` to the worktree copy, with node 336's own file skipped. The files were `.claude/skills/expedition/SKILL.md` and `.scratch/graph-workflow/map-manager-only.md`. I added a phrase list: "exactly one question", "command that shows", "diff command", "five parts", "a sixth", "What nothing here settles", "being changed by whoever holds the code slot", "code slots", "git -C", "What is in front of the human", "last line", "Picking the next node", "The payload", "what command shows it". 46 open or claimed conditions were searched, and both runs report `# Gone items: 0`.
               Phrase hits, read in full:
               - Node 337 clause 13 and 14: the numbering of `## What nothing here settles`, relative to when that work starts. Clause 27: the one-at-a-time rule is "unchanged" by that work, also relative to its start. Still correct once this lands.
               - Node 124: `### Picking the next node` and the sentence "You then stop or redirect what you started.", which this work leaves untouched.
               - Node 285: adds to `### Picking the next node`, which still exists.
               - Node 256: "The payload" in unrelated prose.
               No clause of an unclaimed node is made wrong, so I write no replacement.

MISSING FROM MAP: none. `map.md` said everything the node needed. The one thing I took from elsewhere was the existing form of a `map-history.md` superseded section, which I copied from its node 277 and node 281 sections.

GATE PAYLOAD:  Checker findings: none yet; the checker has not run.
               Bar: I confirmed it against the repo. The worktree holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`: no manifest, no build, no tests, no formatter, no CI. That matches `map-implementation-rules.md`'s record, including its three `.gitignore` patterns. So the bar is its non-command half. `git diff --check` is clean. New lines in `SKILL.md` keep the file's existing wrap of about 104 columns. The only longer lines are the pre-existing table rows and the frontmatter.
               Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/336-m1`, branch `worktree-336-m1`, uncommitted):
               - `.claude/skills/expedition/SKILL.md`
               - `.scratch/graph-workflow/map-manager-only.md`: one change only. In `## Landing an implementation node's work`, the bold lead `**The gate payload names the worktree's path and the command that shows its diff**, because` became `**The gate payload names the worktree's path**, because`.
               - `.scratch/graph-workflow/map-history.md`: one new section appended at the end of the file: `## Superseded from `map-manager-only.md` at node 336 — the gate payload's command that shows the diff`. It has an italic moved-verbatim note linking nodes 336, 231 and 189, then `### From *Landing an implementation node's work* — the gate payload's sentence`, then `*Replaced, and it stood as:*`, then the old sentence verbatim. The old sentence runs from "**The gate payload names the worktree's path and the command that shows its diff**, because" to "*"what are the changes ? I don't see them in git ?"*.". The worktree copy does not have the node-333 section the main tree has at its end. Append my section after that one when carrying it across.
               Proposed commit message:
                 Carry the one-thing rule, the report's last line, the code-slot trade and the diff-free gate pointer into the manager contract

                 Node: graph-workflow/336

RETROSPECTIVE:
1. What I had to hunt for. Three things.
   - The exact form a `map-history.md` superseded section takes. I found it by reading that file's tail, the node 277 and 281 sections. Its top rule text says only "under the heading mirroring the section", not the italic-note plus `### From …` sub-heading form.
   - Node 231's exact title, for the link. My first guess from its slug was wrong, and I read its first line.
   - Whether `SKILL.md` anywhere states how many items `## What nothing here settles` holds (clause 14). Grep showed it does not.
2. What arrived that this node did not need.
   - `map.md` as a whole. Only the diff-command bullet, the last-line bullet and the one-question bullet bore on the node, and those only for INVALIDATIONS.
   - The full grep of `decisions.md` for "report" and "gate payload". It returned about 40 lines, of which none changed the work. A narrower phrase ("one question", "diff") would have done.
   - The search script's KEPT and n-gram-run output, which I filtered away.
3. What would have made this easier.
   - The condition names places for most clauses, but not for 7, 8 and 12. One line naming where the last-line rule and the snapshot text go would have removed two assumptions.
   - The amendment names its bullet by a phrase that its own change destroys. A clause identifying the bullet by section plus "the handover bullet" would be sturdier.
   - The spawn's note on how to carry the history edit across helped.
4. What was stale, wrong or contradictory.
   - `CONTEXT.md`'s Handover entry still lists five parts (see NEW NODES).
   - `map.md`'s bullets still say node 231 and node 96 have not shipped, and its standing preference still says "exactly one question".
   - The contract's opening job statement said "exactly one question" and would have contradicted clause 1 had the condition's fence been read narrowly.
   - Clause 5's third consequence, "a node waiting at its gate … does not occupy the channel", reads oddly beside a gate that has been sent and awaits approval. I read "waiting at its gate" as queued and not yet sent, and wrote the clause as given.

## Review

### Checker run 1 — `FAIL: the bar`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 339's check.*

> FAIL: the bar
>
> Node 336, "Carry the rules on what reaches the human, the code-slot count and the gate's pointer to the work into the manager contract". The work is `git -C /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/336-m1 diff`, uncommitted on 5acd220. Following the rule in map-implementation-rules.md, I read the changed paths, including the two `.scratch/` record files, as the work under check. The acceptance condition is met in every part I could establish. The one failure is against a standard.
>
> ### Finding 1 (the bar: graph-conventions.md `### Change the map`, step 2, and writing rule 2)
>
> - **Instances:** The work replaced the gate-payload sentence in `.scratch/graph-workflow/map-manager-only.md` under `## Landing an implementation node's work`. The new sentence starts "**The gate payload names the worktree's path**" and cites no node that shaped the change: neither node 231 nor node 336. The paragraph's existing citations are nodes 11 and 68, and they predate the change. The `### Change the map` procedure in `.claude/skills/expedition/graph-conventions.md` says step 2 must "replace the item with its new current statement, citing by markdown link the nodes that shaped it". Writing rule 2 in map-implementation-rules.md says the same: "An item states its current form and cites the nodes that shaped it." Only the new `map-history.md` entry links nodes 231 and 336. The same file has precedent: nodes 265 and 277 are linked there for their own changes. Found by `grep -o 'nodes/2[0-9][0-9]-[a-z-]*\.md' .scratch/graph-workflow/map-manager-only.md | sort -u`, which returns 265, 277, 289 and 290, with no 231 and no 336.
> - **Form:** a map-file item this work replaced under `Change the map`, whose new statement carries no markdown link to the node or nodes that shaped the replacement.
> - **Extent:** `git -C <worktree> diff .scratch/graph-workflow/map-manager-only.md | grep '^+' | grep -cE 'nodes/(231|336)-'`. It prints 0 now, and the diff has exactly one `+` line. Clause 17 allows the fix inside the replaced sentence, because it requires the rest of the sentence to keep its meaning and adding a citation leaves it unchanged. A citation added outside that sentence would breach "Nothing else in that file changes".
>
> ### Acceptance condition: all met, apart from the part under NOT COVERED
>
> - **Scope:** met. `git status --short` shows exactly SKILL.md, map-manager-only.md and map-history.md. The diff contains no node file, no decisions.md and no flags.md, so the rules file's bookkeeping rule is not triggered. SKILL.md is edited plainly: superseded wording is removed and nothing is struck through.
> - **Searches:** for the searches below, I unwrapped SKILL.md into unbroken paragraphs with an awk command and ran `grep -noiE` over the result.
> - **1:** met. `## What is in front of the human, and when` now opens "At most one thing awaiting the human's reply … exactly one whenever something is waiting. Nothing displaces a live question or any other live thing." It adds that a payload carrying several of one worker's questions counts as one thing.
> - **2:** met. The phrases "exactly one question" and "one question in front" are gone from that section. The one remaining hit, "the one question in front of the human", sits in the table under `## What is never yours`, in a scope rule outside this section and unchanged.
> - **3:** met. The section says "Never combine questions from different nodes into one payload, and never divide one payload's reply between two workers", and the one-worker sentence follows.
> - **4:** met. The line rule is kept, with the added reason "A thing named in that line but not asked cannot be answered by accident." A grep for `attributab` finds nothing.
> - **5, 6:** met. The channel paragraph gives all three consequences as bullets. The next line reads "Send the human a question that is already waiting. Never make one up …"
> - **7, 8, 9:** met. A new `### The last line of a report` covers the last line and its reason, that the line is short, "in whatever words fit the case", that it holds "at the moment you write it" and promises nothing, and the only-when-nothing-is-waiting rule. It ends "added to whatever else … and replaces none of it." Every `-` line in the diff falls under clauses 1–16 or the amendment.
> - **10:** met. The code-slot bullet covers the trade, that the human sets the number, the two things the manager never does, and naming the trade when the count moves.
> - **11:** met. The item is removed along with its two sentences, and the list now runs 1–7 with no gap, which I read directly. Item 1, "What must your report to the human contain?", still stands.
> - **12:** met. A new paragraph under `### Picking the next node` says "Every worker reads a consistent snapshot … reconciled when the work is integrated, not while they are read."
> - **13:** met. `\b(git|branch|worktree|rebase|merge)\b` finds nothing in SKILL.md.
> - **14:** met, because there is nothing to disagree. `nothing here settles|[0-9]+ (items|questions)|(six|seven|eight) (items|questions)` finds no item count, and the section heading is the only hit.
> - **15, 16:** met. The payload bullet now reads "Where the work is: the path of the working tree that holds it. A gate that describes a change and points at nothing has not been presented." The table cell reads "say where the work is". `command` gets three hits, all about the bar's commands, and none asks for a diff command. "Keep two things out of the payload: the diff, and the acceptance condition." is present once.
> - **17:** met. `git diff --word-diff` on map-manager-only.md shows the only change as `[-path and the command that shows its diff**,-]{+path**,+}`. The ground is unchanged and no other line differs.
> - **18:** met. The removed sentence, extracted from HEAD with `grep -o`, is found verbatim in the new map-history.md (`grep -cF` prints 1). The HEAD content is a byte-exact prefix of the new file (`head -c N | cmp` passes), so the file gained text and lost none. The heading reads "### From *Landing an implementation node's work* — the gate payload's sentence", under a `## Superseded from map-manager-only.md at node 336` heading in the file's existing style. The sentence has no struck-through text.
> - **19, 20, 21:** met. The tier text, the "Three things never enter the queue:" list and all of `## The order you act in` are unchanged: no diff hunk touches them. "Nothing displaces a live question" is kept inside a widened sentence.
> - **22:** met. Comparing the old and new heading lists shows one addition, `### The last line of a report`, and no removal.
> - **Amendment:** met. The bullet now reads "A handover has seven parts every time" and lists all seven, with the `INVALIDATIONS`, `CONDITIONS` and `MISSING FROM MAP` names, plus "an eighth, the gate payload". The parts match the handover labels in the worker contracts: ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, CONDITIONS and MISSING FROM MAP. No other count of five or six parts remains.
> - **23:** fails, per Finding 1.
>
> ### The bar
>
> The repo has no build, tests, formatter or CI, so there were no commands to run.
> - `git diff --check`: clean, exit 0.
> - `awk 'length>105'` on SKILL.md: hits only lines 3 (frontmatter) and 52–56 (table rows). None of those lines is in the diff; the table row the work changed is short.
>
> ### Standards
>
> I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md` and opened no other file in the effort's directory apart from the two changed paths handed to me as the work.
> - **Bore on the work:**
>   - graph-conventions.md `### Change the map`: breached, Finding 1.
>   - The five writing rules. Rule 2 is breached, Finding 1. Rule 5 holds: each added prohibition stands beside its positive.
>   - `CONTEXT.md` `_Avoid_` lines: checked by hand on the added text, nothing found.
>   - The ground rules: nothing in SKILL.md assumes a repo or a toolchain, and nothing directs an agent to the human.
>   - `/writing-for-agents`: read, nothing found beyond the above.
>   - The record-file rule: applied.
> - **Did not bear on the work:** `/coding-principles` (the work has no code). `/naming` bore only on the new heading, and I found nothing.
> - No reviewing skill is named, so I ran none. The work changes no standard I hold it against.
>
> The condition says its scope came from no search, so there was no command to re-run.
>
> NOT COVERED:
> - "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

## Handover, attempt 1, correction round 1

*The manager's note, 2026-09-26:* the worker handed back its whole handover again. Its ANSWER, INDEX LINE, FLAGS, NEW NODES, INVALIDATIONS, CONDITIONS and MISSING FROM MAP repeat the first handover with rewording only, apart from the record-files bullet, which now says the sentence cites nodes 231 and 336. Its gate payload and retrospective are pasted as it wrote them.

GATE PAYLOAD:  Checker finding 1 (the bar: `### Change the map` step 2 and writing rule 2, missing citation):
               - What I changed: in `.scratch/graph-workflow/map-manager-only.md`, inside the replaced sentence only, the text after the bold lead now reads: `**The gate payload names the worktree's path**, the command that shows its diff having been dropped at [node 231](nodes/231-a-gate-payload-stops-carrying-a-diff-command.md) and carried here by [node 336](nodes/336-carry-the-rules-on-what-reaches-the-human-the-code.md), because …`.
               - The rest of the sentence and its ground are unchanged, and nothing else in the file changed.
               - The checker's extent command, `git diff map-manager-only.md | grep '^+' | grep -cE 'nodes/(231|336)-'`, now prints 1, and the diff still has one `+` line in that file.
               - No other file was touched in this round.
               Bar: I confirmed it against the repo. The worktree holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`: no manifest, no build, no tests, no formatter, no CI. That matches `map-implementation-rules.md`'s record. `git diff --check` is clean.
               Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/336-m1`, branch `worktree-336-m1`, uncommitted):
               - `.claude/skills/expedition/SKILL.md`
               - `.scratch/graph-workflow/map-manager-only.md`. One sentence changed, in `## Landing an implementation node's work`. The old bold lead `**The gate payload names the worktree's path and the command that shows its diff**, because` became `**The gate payload names the worktree's path**, the command that shows its diff having been dropped at [node 231](nodes/231-a-gate-payload-stops-carrying-a-diff-command.md) and carried here by [node 336](nodes/336-carry-the-rules-on-what-reaches-the-human-the-code.md), because`.
               - `.scratch/graph-workflow/map-history.md`. One new section is appended at the end of the file: `## Superseded from `map-manager-only.md` at node 336 — the gate payload's command that shows the diff`. It has an italic moved-verbatim note linking nodes 336, 231 and 189, then `### From *Landing an implementation node's work* — the gate payload's sentence`, then `*Replaced, and it stood as:*`, then the old sentence verbatim. The old sentence runs from "**The gate payload names the worktree's path and the command that shows its diff**, because" to "*"what are the changes ? I don't see them in git ?"*.". The worktree copy lacks the node-333 section the main tree has at its end. Append my section after that one when carrying it across.
               Proposed commit message:
                 Carry the one-thing rule, the report's last line, the code-slot trade and the diff-free gate pointer into the manager contract

                 Node: graph-workflow/336

RETROSPECTIVE (correction round 1, new items only):
1. What I had to hunt for: nothing new.
2. What arrived that this node did not need: nothing new.
3. What would have made this easier: condition clause 17 says the rest of the sentence keeps its meaning and nothing else in the file changes. It does not mention that `Change the map` step 2 also wants a citation to the shaping node. One line in the condition, or in the spawn's note on the record-file edit, would have prevented this round.
4. What was stale, wrong or contradictory: nothing new.


### Checker run 2 — `FAIL: the bar`

*The checker's own text, pasted, 2026-09-26, after correction round 1.*

> FAIL: the bar
>
> This is a re-check of node 336 after correction round 1: the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/336-m1`, uncommitted on 5acd220. As before, I read the two `.scratch/` record files handed to me as the work under check.
>
> ### What changed since my last outcome, and how I established it
>
> - `git status --short` still shows exactly the three paths, and `git diff --stat` is identical to last round (77/17/2).
> - The modification times are: SKILL.md 22:50:19, map-history.md 22:50:51, map-manager-only.md 22:55:32. So only map-manager-only.md was touched after the other two.
> - `git diff --word-diff=plain` on map-manager-only.md shows the whole change against HEAD. It is still one changed line, with `[-path and-]{+path**,+}` and `[-diff**,-]{+diff having been dropped at [node 231](nodes/231-a-gate-payload-stops-carrying-a-diff-command.md) and carried here by [node 336](nodes/336-carry-the-rules-on-what-reaches-the-human-the-code.md),+}`. Nothing else in the file differs. This matches the worker's statement.
> - Both link targets resolve to files under `.scratch/graph-workflow/nodes/`.
>
> ### Re-established parts of the condition
>
> - **17:** met. The sentence still requires the gate payload to name the worktree's path. It no longer requires a diff command; it mentions the command only as dropped. The ground after "because" is unchanged, and no other line in the file changed.
> - **18:** met. map-history.md still starts with the whole of its HEAD content byte for byte (`head -c N | cmp` passes), and the verbatim entry from last round is unchanged.
> - **Scope:** met. Still only the three paths, and still no node, decisions.md or flags.md write.
> - **Everything else:** SKILL.md was not touched this round, so every other clause and the amendment stand as I established them last round.
>
> ### Finding 1 (last round): its demand is met
>
> The replaced item now cites nodes 231 and 336 by markdown link. The form of that citation introduced Finding 2.
>
> ### Finding 2 (new, the bar: graph-conventions.md `## Writing the map`)
>
> - **Instances:** the phrase added in map-manager-only.md, `## Landing an implementation node's work`: "the command that shows its diff having been dropped at [node 231](…) and carried here by [node 336](…)". It tells what the file used to require and how the requirement was removed. That is an account of how the rule was learned.
>   - `## Writing the map` says: "How a rule was learned fails the test: how many attempts it took and what they cost, who was wrong, and what the file said before. Move that material to `map-history.md`, and leave in its place the markdown link to the node that shaped the line." It also says an item "cites by markdown link the nodes that shaped it, without restating what those nodes hold."
>   - map-history.md already holds this account in its node-336 entry, so the map file repeats it.
>   - I found it by reading the word-diff above.
> - **Form:** text added by this work to a map file that states what the file said before, or how or where a rule changed, rather than the current rule plus a bare markdown link to the node that shaped it.
> - **Extent:** `git -C <worktree> diff .scratch/graph-workflow/map-manager-only.md | grep '^+[^+]' | grep -oE 'having been dropped[^,]*,'`. It returns exactly the one instance.
> - **Repair and limits:** a fix that satisfies Finding 1, Finding 2 and clause 17 is a bare citation inside the sentence, with no account of the dropped command. Clause 17 still binds: the rest of the sentence and its ground keep their meaning, and nothing else in the file changes.
>
> ### The bar, re-run in full
>
> - The repo has no build, tests, formatter or CI, so there were no commands to run.
> - `git diff --check`: clean, exit 0.
> - Standards, re-read from map-implementation-rules.md (only its standards) together with graph-conventions.md `## Writing the map` and `### Change the map`, `CONTEXT.md` `_Avoid_` and the ground rules:
>   - Finding 2 is the only breach.
>   - The standard that Finding 1 held the work against is now met on citation.
>   - Nothing else in the changed sentence bears on any standard.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

## Handover, attempt 1, correction round 2

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

GATE PAYLOAD (correction round 2):
               Checker finding 2 (the bar, graph-conventions.md `## Writing the map`: the citation told the story of how the rule changed):
               - What I changed: in `.scratch/graph-workflow/map-manager-only.md`, inside the replaced sentence only, I removed the account "the command that shows its diff having been dropped at … and carried here by …" and put bare citations in its place. The sentence now reads `**The gate payload names the worktree's path** ([node 231](nodes/231-a-gate-payload-stops-carrying-a-diff-command.md), [node 336](nodes/336-carry-the-rules-on-what-reaches-the-human-the-code.md)), because …`.
               - The ground after "because" is unchanged, and nothing else in the file changed.
               - The checker's extent command (`grep -oE 'having been dropped[^,]*,'` on the diff's `+` lines) now returns nothing.
               - Finding 1 still holds as fixed: `grep -cE 'nodes/(231|336)-'` on those `+` lines prints 1.
               - No other file was touched this round. `git diff --check` is clean.
               Checker finding 1 (from round 1): still met, by the same bare citation above.
               Bar: unchanged from before. There is no build, no tests, no formatter and no CI, so the bar is its non-command half.
               Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/336-m1`, uncommitted):
               - `.claude/skills/expedition/SKILL.md`
               - `.scratch/graph-workflow/map-manager-only.md`. The single changed sentence, in `## Landing an implementation node's work`, went from `**The gate payload names the worktree's path and the command that shows its diff**, because` to `**The gate payload names the worktree's path** ([node 231](nodes/231-a-gate-payload-stops-carrying-a-diff-command.md), [node 336](nodes/336-carry-the-rules-on-what-reaches-the-human-the-code.md)), because`.
               - `.scratch/graph-workflow/map-history.md`: the appended node-336 section is unchanged since round 1.
               Proposed commit message:
                 Carry the one-thing rule, the report's last line, the code-slot trade and the diff-free gate pointer into the manager contract

                 Node: graph-workflow/336

The rest of the handover stands unchanged.


### Checker run 3 — `PASS`

*The checker's own text, pasted, 2026-09-26, after correction round 2.*

> PASS
>
> Re-check of node 336 after correction round 2. The worktree is `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/336-m1`, uncommitted on 5acd220. As before, I read the changed `.scratch/` record files as the work under check. This PASS covers every part of the condition except the one named under NOT COVERED.
>
> What changed since my last outcome, and how I established it:
> - `git status --short` shows the same three paths. `git diff --stat` is unchanged (77/17/2).
> - The md5 checksums of the SKILL.md diff (2462a963…) and the map-history.md diff (4c980aa8…) are identical to the last round. Their modification times (22:50:19 and 22:50:51) are also unchanged.
> - Only map-manager-only.md was touched, at 22:57:23. Its word-diff against HEAD is now the single change `[-path and the command that shows its diff**,-]{+path** ([node 231](nodes/231-a-gate-payload-stops-carrying-a-diff-command.md), [node 336](nodes/336-carry-the-rules-on-what-reaches-the-human-the-code.md)),+}`. It is still one changed line. This matches what the worker said it did.
>
> Finding 2 (last round) is resolved. The added text is two bare markdown links to the nodes that shaped the sentence, with no account of what the file said before. I ran `git diff … map-manager-only.md | grep '^+[^+]' | grep -oE '.{40}(having been dropped|dropped|used to).{40}'`. Its one hit is "used to assume", in text unchanged since HEAD (it is present in `git show HEAD:`). Finding 1's demand for a citation is still met.
>
> Parts of the condition:
> - Scope: met. Only SKILL.md, map-manager-only.md and map-history.md changed. The diff has no node file, decisions.md or flags.md. SKILL.md is edited plainly.
> - Clauses 1–16, 19–22 and the amendment: met. SKILL.md's diff is byte-identical to the one I established them on in my first check (same md5). There I established each one by grep over SKILL.md unwrapped into paragraphs and by comparing the old and new headings:
>   - clause 1: the one-thing rule, with the payload counting as one thing;
>   - clause 2: no "exactly one question" left in the section;
>   - clause 3: the never-combine and never-divide rule;
>   - clause 4: the named-line reason, with no "attributable";
>   - clauses 5 and 6: the channel rule with its three consequences, and the rule against making up a question;
>   - clauses 7–9: `### The last line of a report`, which adds to what a report carries and removes nothing;
>   - clause 10: the code-slot trade, which the human sets;
>   - clause 11: the item removed and the list renumbered 1–7;
>   - clause 12: the consistent-snapshot paragraph;
>   - clause 13: `\b(git|branch|worktree|rebase|merge)\b` finds nothing;
>   - clause 14: no count of items anywhere;
>   - clauses 15 and 16: no diff command in the file, and "Keep two things out of the payload…" still present;
>   - clauses 19–21: none of their text is touched by any diff hunk, and item 1 still stands;
>   - clause 22: the only heading change is one added heading;
>   - amendment: seven parts plus an eighth, matching the worker contracts' handover labels.
> - Clause 17: met. The sentence still requires the gate payload to name the worktree's path. It no longer mentions or requires a diff command. The ground after "because" is unchanged, and no other line of the file differs.
> - Clause 18: met. The map-history.md diff is unchanged. The replaced sentence appears there word for word (`grep -cF` = 1, established in my first check). The file's HEAD content is still a byte-exact prefix of its current content.
> - Clause 23 (the bar): met, see below.
>
> The bar:
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check`: clean, exit 0.
> - Standards: I read only the standards in map-implementation-rules.md, plus graph-conventions.md `## Writing the map` and `### Change the map`, the `CONTEXT.md` `_Avoid_` lines, `/writing-for-agents`, the ground rules and the five writing rules.
>   - The changed sentence now meets `Change the map` step 2 (cite by markdown link the nodes that shaped it) and `## Writing the map` (no account of what the file said before).
>   - Nothing else bears on the change.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The worktree diff contains no such write. What the main tree's record holds is outside what I was given.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*

## Amendment, 2026-09-26 (from node 333)

*Written by [node 333](333-land-the-open-repairs-to-the-five-worker-contracts-in-one-change.md)'s worker, which proposed it for node 336 or 337 and left the choice to the manager, and filed by the manager after that node's work landed as commit `5acd220`, which fixes every word of it. The manager placed it here, under the human's standing instruction that a related defect goes into a node that already exists and that a node not yet started may be updated.*

- **A new clause.** "(node 333) The bullet in `.claude/skills/expedition/SKILL.md` beginning 'A handover has five parts every time' lists the parts the worker contracts' handover blocks list: the answer, the index line, the flags, the nodes surfaced, which resolved node the work changes (`INVALIDATIONS`), the open conditions searched and any replacement clauses (`CONDITIONS`), and what `map.md` did not say (`MISSING FROM MAP`). That is seven parts, and it says an implementation worker returns an eighth, the gate payload."
- **The fence.** Wherever this condition limits what may change in `SKILL.md`, that bullet is added to what may change.

## Flags

`336.1` **· settled** `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 333's clause was placed on this node rather than node 337, and the fence was widened to let it in.

`336.2` **· settled** `ASSUMPTION` — The contract's opening job statement said "keep exactly one question in front of the human". That sentence is outside the section clauses 1 and 2 name. I changed it to "keep one thing awaiting the human's reply in front of them whenever something is waiting", because leaving it would contradict clause 1's rule in the same file. Clause 22 allows a meaning change of the kind clauses 1 to 16 state, and this is clause 1's.

`336.3` **· settled** `ASSUMPTION` — The condition names no place for three pieces of text, so I placed them myself. The last-line rule (clauses 7 and 8) is a new subsection, `### The last line of a report`, at the end of `## What is in front of the human, and when`. The consistent-snapshot text (clause 12) is a paragraph under `### Picking the next node`, after the two counts, because it replaces a question about work that runs in parallel. The channel paragraph (clauses 5 and 6) comes straight after the one-thing rule.

`336.4` **· settled** `ASSUMPTION` — The amendment names its bullet by the phrase it begins with, "A handover has five parts every time". The same amendment makes that bullet say seven parts, so it now begins "A handover has seven parts every time". I took the old phrase as the bullet's identity before this work.
