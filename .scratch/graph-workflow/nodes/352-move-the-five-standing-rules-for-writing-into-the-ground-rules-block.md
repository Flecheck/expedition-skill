# Move the five standing rules for writing into `map.md`'s ground-rules block

Type: implementation
Status: claimed
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

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

````
HANDOVER:      Move the five standing rules for writing into `map.md`'s ground-rules block

ANSWER:        The five standing rules for writing now sit in `map.md`'s `## Notes`, inside the block that begins "**Ground rules for this effort.**". They form a second numbered list, placed after ground rules 1 to 5 and before the paragraph that begins "Every rule above". The list has its own bold lead-in, "**This effort's standing rules for writing**", which says the rules are held against every prose deliverable and links node 53 for the first four and node 289 for the fifth. The five rules were moved word for word, keeping their order and bolding. Ground rules 1 to 5 were not changed.

               **The paragraph after the lists** was rewritten to cover both lists. It now says that every rule above, in both lists, is "a standing constraint true of any node's work, rather than an account of what happened", and that this is node 42's test for what may travel to a blind checker. It no longer says that the rules are drawn from a standing preference, because that is not true of the rules for writing. It keeps the sentence saying the block is appended to like any other part of the map. Because the manager already copies this block into every checker spawn as text, checkers keep receiving the rules for writing. No shipped file changes.

               **`map.md`'s one-line pointer**, which said the rules were in `map-implementation-rules.md`, was removed.

               **In `map-implementation-rules.md`**, the "**Five standing rules for writing anything in this effort**" paragraph and its list were removed. Its "rules of writing versus rules of scope" contrast was not carried over, following node 349's flag. The file names the rules in three places, and each now says that `map.md`'s `## Notes` holds them inside the ground-rules block and that a checker receives them as text in its spawn:
               - the bar paragraph's list of standards;
               - the review route's list of standards;
               - the review route's sentence on the two blocks that pass node 42's test.

               **In `map-history.md`**, one new section was appended after node 160's block: "Superseded from `map.md` and `map-implementation-rules.md` at node 352 — the five standing rules for writing placed in the rules file". It has six subsections, each naming the section its text came from, and each holds a removed or replaced text word for word. None of the removed text contained struck-through text. The file only gained text.

               Rule 5 still says "a term defined in `CONTEXT.md`", as the condition requires. The rules file's two paragraphs also still name `CONTEXT.md`. The manager updates these mentions after landing.

INDEX LINE:    The five standing rules for writing now stand as a second numbered list inside `map.md`'s ground-rules block; the rules file points there, and the displaced texts are in `map-history.md`.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: - Node 144 moved the rules for writing into the rules file. This work reverses that for the rules for writing only (the ground rules had already moved back at node 348).
               - Node 289 is only narrowed: its fifth rule now lives in `map.md` rather than the rules file, with the same wording.
               - Node 349's answer is carried out, and nothing in it is contradicted.

CONDITIONS:    I searched every open or claimed node's `## Acceptance condition` and `## Question` for these phrases: "rules for writing", "rules of writing", "rules of scope", "this file holds below", "held below in this file", "writing, which". Matches outside nodes 349 and 352:
               - **Node 190 (open, unclaimed).** Its clause 1 says "five standing rules for writing, stated as held in this file". Its clause 4 says "No numbered rule in the file's block of five standing rules for writing is reworded". This work makes both false. Node 349's worker already wrote replacements for both, and the manager has filed them on node 190 at "Node 190 (open, unclaimed). Clause 1, as amended by node 348…". Their wording ("held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn") matches the text this work puts in `map-implementation-rules.md` word for word. So once this node lands, those replacements are fixed by landed work. I write no new replacements. Node 190's note that quotes the heading "**Five standing rules for writing anything in this effort**" as being "in the tree" is no longer true after this work.
               - **Node 284 (open)**, clause 4, says "this effort's ground rules and four standing rules for writing". **Node 80 (open)** says "`map.md`'s own standing preferences, ground rules and four standing rules of writing". Neither names where the rules are held, so this work does not change them. Their "four" was already out of date before this node, and the manager's own notes on node 284 already record that.
               - No open node's question changes.

MISSING FROM MAP: none

GATE PAYLOAD:  No checker findings yet.
               Paths touched (all inside the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/352-writing-rules`):
               - `.scratch/graph-workflow/map.md`
               - `.scratch/graph-workflow/map-implementation-rules.md`
               - `.scratch/graph-workflow/map-history.md`
               The bar: I checked the repo and it has no manifest, no build, no tests, no formatter and no CI. The root holds only `.claude`, `.scratch`, `CONTEXT.md`, `CONTEXT-MAP.md` and `.gitignore`. That matches the rules file's record, so the bar is met on its non-command half.
               Checks I ran:
               - The committed `map-history.md` is an exact prefix of the new file, so nothing in it was lost.
               - A script confirmed that every sentence removed from `map.md` or `map-implementation-rules.md` appears word for word in the new text or in `map-history.md`.
               - Every relative markdown link in the three files resolves to a path that exists.
               - I re-ran the condition's scope grep. It gives 1 match in `map.md` (the new lead-in), 2 in `map-implementation-rules.md` (the bar and review route paragraphs), and none in `map-manager-only.md`, `.claude/skills` or `CONTEXT.md`.
               Proposed commit message:
                 Move the five standing rules for writing into map.md's ground-rules block

                 The rules bind prose every worker writes, so they now sit in the one
                 map file every worker reads, inside the block the manager copies into
                 every checker spawn. The rules file points there, and the displaced
                 texts are appended verbatim to map-history.md.

                 Node: graph-workflow/352

RETROSPECTIVE
1. What I had to hunt for: very little. The main thing was finding the exact end of the paragraph just before the rules block in the rules file. My first edit used the wrong anchor and failed. I also had to confirm the order of sections at the end of `map-history.md` so I appended after node 160's block.
2. What arrived that this node did not need: the contract's long section on writing a new node's condition, since I reported no new node. Most of node 349's interview, since its handover and the acceptance condition were enough.
3. What would have made this easier: nothing much. The condition gave the rules word for word and named every paragraph by its opening phrase, which made this work mechanical. It would help if the spawn said that node 349's replacement text for node 190 is already filed on node 190. That would have saved me checking whether `CONDITIONS` owed new text.
4. What was stale, wrong or contradictory: nothing in the three files. After this work, node 190's note saying the "Five standing rules…" heading is "in the tree" is no longer true. Nodes 284 and 80 still say "four standing rules", which was out of date before this node and is already noted on node 284.
````

## Flags

none

*The manager's note, 2026-09-27:* node 56 landed (`9a87ac0`) and moved the glossary to `.claude/skills/expedition/glossary.md`. Rule 5's text in this condition still says "a term defined in `CONTEXT.md`", and the rules file's two paragraphs this node touches still name `CONTEXT.md`. The root `CONTEXT.md` is now a superseded pointer, so every such mention still resolves. The manager updates those mentions itself once this node lands, rather than amending this condition.
