# Whether the five standing rules for writing reach a worker that is not an implementation worker

Type: grilling
Status: resolved
Blocked by: 348

## Answer

The five standing rules for writing move verbatim into `map.md`'s ground-rules block, so every worker reads them and checkers keep receiving them as spawn text.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The node it surfaced is [node 352](352-move-the-five-standing-rules-for-writing-into-the-ground-rules-block.md); its replacements for node 190's clauses 1 and 4 are filed there. Flags 349.1 and 349.2 settle at the node closing report.

## Question

This effort's five standing rules for writing are held against every prose deliverable. They sit in `map-implementation-rules.md`, which only an implementation worker and a checker read. Grilling, research, prototype and precondition workers also write prose that the manager pastes onto the graph unaltered. Must those rules reach those workers, and if so, by moving them into `map.md`, by a pointer in those contracts, or by some other route?

*Reported by [node 168](168-where-a-non-implementation-worker-gets-the-ground-rules.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Interview

#### Question 1, relayed 2026-09-27

*Pasted as the worker handed it back.*

```
NODE:          349, Whether the five standing rules for writing reach a worker that is not an implementation worker
ABOUT:         This effort has five standing rules for writing: compress the explanation of why but never the shapes; state an item's current form and cite the nodes behind it; make a long answer navigable by heading; cite by heading or quoted phrase, never by line number; write plain English. `map.md` says they are "held against every prose deliverable", but they sit only in `map-implementation-rules.md`, which only an implementation worker and a checker read. This node decides whether grilling, research, prototype and precondition workers must have them, and by what route. It comes up now because node 348 landed today and put the ground rules back in `map.md` for the same reason, and left these five rules behind.
SO FAR:        I read the following: the grilling contract, `map.md`, `map-implementation-rules.md`, the `decisions.md` lines about the ground rules and the rules file, node 168's interview and handover, node 190's condition, and the checker-spawn section of the manager contract and the checker contract.
               What the files say today:
               - `map.md` ends its `## Notes` with a one-line pointer: the five rules "are in map-implementation-rules.md, held against every prose deliverable".
               - The four non-implementation contracts list only the node file, `map.md` and `decisions.md` as reading. They also say "you never go looking for a standard you are judged against". So a grilling or research worker sees the pointer but may not follow it. The claim that the rules cover every prose deliverable is therefore not true for those four workers.
               - Those workers do write prose that the rules are aimed at. The manager pastes a grilling worker's ANSWER onto the node unaltered, and rules 2 to 4 are about that kind of record text. The human reads the question payloads directly, and rule 5 (plain English) is about exactly that.
               - The checker gets its standards by reading `map-implementation-rules.md` itself. The ground rules are the exception: the manager copies "the block of ground rules" into every checker spawn as text (manager contract, node 42).
               - No shipped file mentions the five rules. They belong to this effort alone, so any answer here changes only this effort's map, unless you say otherwise.
               - The block is 1,412 bytes. `map.md` is 22,838 bytes.
               - Node 190 (open) is NOT independent of this node, which is different from what the manager believed. Two of its clauses assume the five rules stay in the rules file. Clause 4 says: "No numbered rule in the file's block of five standing rules for writing is reworded". Node 348's amendment to clause 1 says: "five standing rules for writing, stated as held in this file". If the block moves, both clauses must be rewritten, and node 190 should not be claimed until this node has resolved.
               Settled on my own authority: I treat "reach" as meaning the worker has the rules in a file its contract tells it to read. Whether anyone checks a grilling worker's prose against them is a separate matter, because no checker looks at non-implementation work.
ASK:           Must the five standing rules for writing reach the grilling, research, prototype and precondition workers, and if so, by which route?
RECOMMENDED:   Yes. Move the five rules verbatim from `map-implementation-rules.md` into `map.md`'s `## Notes`, as a second numbered list inside the "Ground rules for this effort" block. The rules file then says that `map.md` holds them, in the same way it already does for the ground rules. This rests on four points:
               (a) It is the same reasoning you accepted at node 168: a block that binds every worker belongs in the one map file every worker reads.
               (b) Putting the rules inside the ground-rules block means the checker keeps receiving them with no change to any shipped file. The manager already copies that block into every checker spawn as text, and the rules file already says the five rules pass node 42's test for what may be copied there. If they sat in `map.md` as a separate block, the checker would lose them, because it does not read `map.md`.
               (c) Keeping the ground rules as "rules of scope" and these as "rules of writing" does little work. Ground rule 5 (`/writing-for-agents`) is itself a rule of writing.
               (d) The cost is 1.4 KB more in `map.md` for every worker, and the rules file shrinks by the same amount.
               I would file this as one implementation node for the move, plus replacement text for node 190's clauses 1 and 4.
ALTERNATIVES:  - Move the rules to `map.md` as their own block, separate from the ground rules. The checker then loses them unless the manager contract (a shipped file) copies a second block, or the rules file keeps a duplicate that can drift.
               - Keep them in the rules file and add that file to the four contracts' reading lists. You rejected this for the ground rules at node 168: those workers would read the bar commands, the worktree route and the review route, which they never use.
               - Keep a copy in both files. That makes two places to supersede and lets them drift apart.
               - Have the manager copy them into every worker's spawn. This changes every spawn and breaks the rule that a spawn points rather than summarises.
               - Say they bind implementation work only, and narrow `map.md`'s "every prose deliverable" to match. This is the cheapest option, but it leaves the answers pasted onto nodes and the payloads you read outside rules that were written for them.
```

#### The human's answer to question 1, 2026-09-27

The human, `verbatim`: *"ok"*. It takes the worker's recommendation: "Yes. Move the five rules verbatim from `map-implementation-rules.md` into `map.md`'s `## Notes`, as a second numbered list inside the "Ground rules for this effort" block. The rules file then says that `map.md` holds them, in the same way it already does for the ground rules."

## Handover, attempt 1

*Pasted as the worker handed it back.*

````
HANDOVER:      Whether the five standing rules for writing reach a worker that is not an implementation worker
ANSWER:        Yes, they reach every worker. This effort's five standing rules for writing move verbatim from `map-implementation-rules.md` into `map.md`'s `## Notes`. They go in as a second numbered list inside the "Ground rules for this effort" block. The human took this with a bare "ok" to the one recommended option.

               **Why.** The rules bind prose that every worker writes. A grilling worker's ANSWER is pasted onto its node unaltered, which is the record text that rules 2 to 4 are about. The human reads each worker's question payload directly, which is what rule 5 (plain English) is about. Before this node, the four non-implementation contracts listed only the node file, `map.md` and `decisions.md` as reading, and they forbid going looking for a standard. So those workers saw `map.md`'s pointer to the rules and could not follow it, and `map.md`'s claim that the rules were "held against every prose deliverable" was untrue for them. This node applies node 168's reasoning: a block that binds every worker belongs in the one map file every worker reads.

               **Why inside the ground-rules block.** The manager already copies that block into every checker spawn as text (node 42's route in the manager contract), and the rules file already said the five rules pass node 42's test. So the checker keeps receiving them, as text in its spawn rather than from the rules file, and no shipped file changes. As a separate block in `map.md`, the rules would not reach the checker, because the checker does not read `map.md`. The split between "rules of scope" (the ground rules) and "rules of writing" was doing little work, since ground rule 5 (`/writing-for-agents`) is itself a rule of writing.

               **What changes.** In `map.md`: the list joins the ground-rules block, and the one-line pointer to the rules file is replaced. In `map-implementation-rules.md`: the block leaves the file, and its lists of standards say `map.md` holds the rules. Both displaced texts go verbatim to `map-history.md`. The change binds this effort only, because no shipped file mentions these rules.

               **Set aside:**
               - A separate block in `map.md`. The checker would lose the rules unless a shipped file changed or a duplicate were kept.
               - Adding the rules file to the four contracts' reading lists. Node 168 rejected this for the ground rules.
               - A copy in both files. It would drift.
               - Copying the rules into every worker's spawn. A spawn points rather than summarises.
               - Narrowing the rules to implementation work only.
INDEX LINE:    The five standing rules for writing move verbatim into `map.md`'s ground-rules block, so every worker reads them and checkers keep receiving them as spawn text.
FLAGS:         ASSUMPTION: I took "reach" to mean that the worker has the rules in a file its contract tells it to read. It does not mean that anyone checks the worker's prose against them, because no checker looks at non-implementation work. Enforcement for those workers was not asked and stays unaddressed.
                 Index: Node 349 took "reaching a worker" to mean the rules sit in a file it reads, leaving unaddressed that no checker holds non-implementation prose to them.
               ASSUMPTION: I placed the list after ground rule 5 and before the paragraph that states node 42's test, so that it sits inside the block the manager copies. I also required that paragraph to stop claiming that every rule above is drawn from a standing preference, which is not true of the five rules for writing. The rules file's sentence contrasting "rules of writing" with "rules of scope" leaves with the block and is not carried over.
                 Index: Node 349 placed the rules for writing inside the ground-rules block before its node-42 paragraph, and dropped the rules-of-scope versus rules-of-writing contrast.
NEW NODES:     1. Name: Move the five standing rules for writing into `map.md`'s ground-rules block
                  Kind: implementation
                  Question: Carry out node 349's answer: move the five standing rules for writing from `map-implementation-rules.md` into the "Ground rules for this effort" block in `map.md`.
                  Blockers: none
                  Acceptance condition:
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
NEW NODES (cont.): For node 190 (open, unclaimed): add a blocker on the node above, and add the clause replacements given under CONDITIONS.
INVALIDATIONS: - Node 144: narrowed further. Its move of the standing rules for writing into `map-implementation-rules.md` is reversed. The rules now live in `map.md`, like the ground rules node 168 moved back.
               - Node 168: its ASSUMPTION flag 168.2, which left the five rules in the rules file, is superseded by this answer. The answer itself stands.
               - Node 348: narrowed. The rules file's statement that it holds the five rules "below", which 348 left in place, becomes wrong once the move lands.
               - Node 184: renamed location only. Its single list of standards still names the five rules, but the list now says `map.md` holds them.
               - Nodes 53 and 289: unchanged in content. Only where their rules are stated moves.
CONDITIONS:    I searched every open node's `## Acceptance condition`, claimed or not, for "rules for writing", "standing rules", "Ground rules for this effort" and "map-implementation-rules". That matched 190, 284 and 80 on the first two terms, and 152, 159, 160, 186, 205, 211 and 271 on the last. None of the last group says anything about the five rules.
               - Node 190 (open, unclaimed). Clause 1, as amended by node 348, contains the phrase "this effort's five standing rules for writing, stated as held in this file". Replacement: "this effort's five standing rules for writing, stated as held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn". Clause 4, as amended by node 168, reads "No numbered rule in the file's block of five standing rules for writing is reworded, renumbered or reordered". Replacement: "4. The file states neither the five ground rules nor the five standing rules for writing as a numbered list. Where it names them, it names `map.md`'s `## Notes` as holding them." Both replacements are fixed by this node, once resolved, and by the new implementation node above, once landed. Node 190 must not be claimed before that node lands.
               - Node 284 (open) and node 80 (open) name the rules without saying where they live, so this node leaves them correct. Both still say "four standing rules" where there are five since node 289. That was already stale before this node, the manager has already noted it on 284, and I wrote no replacement.
MISSING FROM MAP: Two things. First, `map.md` does not say which paragraphs make up "the block below" that the manager copies into a checker spawn. I inferred it as the numbered rules plus the node-42 paragraph, from node 168's handover. Second, the manager's note said node 190 does not depend on this node. Reading node 190's amendments showed that it does.

Method skill: none invoked, and no part skipped.

RETROSPECTIVE
1. What I had to hunt for: how the checker gets its standards, which is by reading the rules file itself, with only the ground-rules block copied into its spawn. That fact decided the route, and I found it in the checker contract and the manager contract. I also had to hunt for where the copied block ends. I had to open node 190 to find that it depends on this node.
2. What arrived that this node did not need: most of the `decisions.md` lines matching "rules file", such as those about the worktree, landing and `.gitignore`.
3. What would have made this easier: a spawn note that the checker reads `map-implementation-rules.md` itself while the ground rules reach it as spawn text. On the record's side, a stated boundary for "the block" the manager copies. The node's `## Question` could also have named node 190's two dependent clauses.
4. What was stale, wrong or contradictory: the manager's note that node 190 does not depend on this node is wrong, because its clauses 1 and 4 assume the rules stay in the rules file. `map.md` claims the rules are "held against every prose deliverable" while four contracts give no way to read them. Nodes 190, 284 and 80 still say "four standing rules" where there are five. `map.md`'s "Every rule above is drawn from a standing preference" would become false for the new list, which the condition handles.
````

## Flags

`349.1` `ASSUMPTION` **· settled** — I took "reach" to mean that the worker has the rules in a file its contract tells it to read. *(The worker's full text is under its handover's `FLAGS`.)*

`349.2` `ASSUMPTION` **· settled** — I placed the list after ground rule 5 and before the paragraph that states node 42's test. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-09-27:* flags 349.1 and 349.2 settle at the node closing report that closes this node.
