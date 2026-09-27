# Keep the ground rules in `map.md` and strike the sibling-file allowance

Type: implementation
Status: resolved
Blocked by: none

## Question

Where an effort's ground rules and source-standing declaration sit only in `map.md`'s `## Notes`, what must change in the shipped files and in this effort's map?

*Reported by [node 168](168-where-a-non-implementation-worker-gets-the-ground-rules.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's blockers note:* "none. It edits `map-implementation-rules.md`, as does open node 190 ("The rules file states one list twice"). The two touch different passages, but whichever lands second works on the other's text."

## Acceptance condition

*Authored by node 168's worker and filed by the manager.*

> The work is these six shipped files: `.claude/skills/expedition/graph-conventions.md`, `.claude/skills/expedition-grilling/SKILL.md`, `.claude/skills/expedition-research/SKILL.md`, `.claude/skills/expedition-prototype/SKILL.md`, `.claude/skills/expedition-precondition/SKILL.md` and `.claude/skills/expedition-implementation/SKILL.md`. It is also three files of this effort's map: `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-implementation-rules.md` and `.scratch/graph-workflow/map-history.md`. No other file changes. The shipped files are edited plainly, with no strike-through or history note.
>
> Scope: the six shipped files are exactly what `grep -rln "sibling file of the map" .claude CONTEXT.md` returned over the working tree when this condition was written. An instance the same command finds outside that list is reported in the handover and not edited.
>
> Done means all of the following are true of the finished tree.
> 1. In `graph-conventions.md`, the `## Notes` bullet under the description of `map.md`'s three sections no longer contains "unless the effort holds it in a sibling file of the map". The bullet says that the two optional blocks, the effort's ground rules and the declaration of which sources are authoritative, which are evidence only and which hold statements known to be false, live in `map.md`'s `## Notes` and in no sibling file of the map. The rest of the bullet keeps its meaning.
> 2. In each of the five worker contracts, the paragraph beginning "The map may declare the effort's ground rules." no longer contains "unless the effort holds it in a sibling file of the map". It says each declaration sits in `map.md`'s `## Notes`. The rest of each paragraph keeps its meaning, including the research contract's closing sentence "A source marked as evidence stays evidence, whatever it says."
> 3. After the edit, `grep -rn "sibling file of the map" .claude CONTEXT.md` returns no line that places the ground rules or the source declaration in a sibling file.
> 4. In `.scratch/graph-workflow/map-implementation-rules.md`, the block that runs from the line `**Ground rules for this effort.**` through the paragraph beginning "Every rule above is drawn from a standing preference" is no longer present. That is the lead-in line, five numbered rules and one paragraph.
> 5. In `.scratch/graph-workflow/map.md`'s `## Notes`, the block removed under clause 4 stands in the place of the paragraph beginning "**Ground rules for this effort, now in". It is byte-identical to the block as committed at `HEAD` in `map-implementation-rules.md`, and nothing in it is reworded, renumbered or reordered. That pointer paragraph is no longer in `map.md`.
> 6. In `.scratch/graph-workflow/map-implementation-rules.md`, no sentence says that file holds the effort's ground rules. The list of standards that work is held against still names this effort's ground rules, and says that `map.md` holds them. It also says that a checker receives them as text in its spawn. The five standing rules for writing stay in that file unchanged.
> 7. The pointer paragraph removed from `map.md` under clause 5, and the text of each sentence of `map-implementation-rules.md` replaced under clause 6, are appended verbatim to `.scratch/graph-workflow/map-history.md`. Each goes under a heading that names the file and section it came from. The block moved under clauses 4 and 5 is moved, not superseded, so it is not appended.
> 8. Every markdown link in `map.md` and `map-implementation-rules.md` resolves to a path that exists.
> 9. The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.

## Answer

Ground rules and the source declaration sit only in `map.md`'s `## Notes`. The sibling-file allowance is struck from six shipped files, and this effort's block moved back from the rules file unchanged.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `12e916e`. Flags 348.1 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Keep the ground rules in `map.md` and strike the sibling-file allowance

ANSWER:        The effort's ground rules and its source-standing declaration are now stated to sit only in `map.md`'s `## Notes`. The shipped allowance "unless the effort holds it in a sibling file of the map" is struck from all six files that carried it, and this effort's ground-rules block has moved back into `map.md`.
- **Shipped files (worktree `worktree-348-ground`, based on `4b538be`).** In `.claude/skills/expedition/graph-conventions.md`, the `## Notes` bullet now reads "Each lives here and in no sibling file of the map". The rest of the bullet is unchanged in meaning, and it keeps its 105-column wrap. In the grilling, research, prototype, precondition and implementation contracts, the sentence now reads "Each declaration sits in `map.md`'s `## Notes`." and the paragraph is rewrapped. The four plain contracts' paragraphs are byte-identical to each other (same md5). The research paragraph is the same text plus its closing sentence "A source marked as evidence stays evidence, whatever it says.", which is unchanged and now shares a line with the sentence before it.
- **The block moved.** The block runs from `**Ground rules for this effort.**` through the paragraph "Every rule above is drawn from a standing preference…". It is removed from `map-implementation-rules.md` and stands in `map.md`'s `## Notes` in place of the old pointer paragraph ("**Ground rules for this effort, now in [map-implementation-rules.md]…**"), which is gone. Before the move I checked the block in the main checkout's uncommitted `map-implementation-rules.md` against the copy committed at `HEAD` (last touched in `084aae9`). The two are byte-identical (cmp), so the block moved is both. The block now in `map.md` is byte-identical to `HEAD`'s copy. `map.md`'s preceding sentence, "The manager copies the block below as text into every checker spawn", is now literally true again.
- **`map.md`, one further change.** The next paragraph said the five standing rules for writing are in `map-implementation-rules.md` "too". The "too" leaned on the removed pointer, so I dropped it (flag 348.1).
- **`map-implementation-rules.md`, four sentences replaced under the `Change the map` procedure.** These are the sentences that said the file holds the ground rules:
  - The bar's list of its non-command half now names "this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn" and "this effort's five standing rules for writing, which this file holds below". Its standing-preferences exclusion is split into a sentence of its own.
  - The review route's "standards to hold work against" says the same of both blocks and cites node 348.
  - The node-42 sentence now reads "the **ground rules**, held in `map.md`, and the **five standing rules for writing**, held below in this file, are the two blocks that pass it". Its account clause ("the struck wording named the preferences alongside them — a defect from node 42 onward…") is dropped under the file's admission test. That clause would also have dangled once the struck wording left the file.
  - The writing-rules lead-in now says "where this effort's ground rules, held in [`map.md`](map.md)'s `## Notes`, are rules of scope".
  - The five standing rules for writing are untouched.
- **`map-history.md`, appended only** (the prefix is byte-identical to before). One new section, "Superseded from `map.md` and `map-implementation-rules.md` at node 348 — the ground rules placed in the rules file", with one `###` subheading per text, each naming its file and section. The texts are the removed pointer paragraph, the "too" paragraph and the four replaced sentences, all verbatim with strikes kept. The moved block is not appended.
- **Checks.** Every markdown link in `map.md` and `map-implementation-rules.md` resolves. `grep -rn "sibling file of the map" .claude CONTEXT.md` over the worktree returns one line, graph-conventions.md:84 ("and in no sibling file of the map"), and that line denies the placement. Running `grep -rln` with the same pattern before the edit returned exactly the six listed files, so nothing outside them was reported.

INDEX LINE:    Ground rules and the source declaration sit only in `map.md`'s `## Notes`. The sibling-file allowance is struck from six shipped files, and this effort's block moved back from the rules file unchanged.

FLAGS:         ASSUMPTION: In `map.md`'s `## Notes` I dropped the word "too" from the paragraph "**The five standing rules for writing anything in this effort are in [map-implementation-rules.md]…** too". That word leaned on the pointer paragraph clause 5 removes, and left in place it implied the ground rules were in that file as well. The condition does not name this edit, but it limits files and not passages. Its old text is appended to `map-history.md` under its own subheading. What I did: I replaced the one word and appended the prior paragraph verbatim.
Index sentence: Node 348 dropped a "too" from `map.md`'s pointer to the five writing rules, since it implied the ground rules still sat in the rules file.

NEW NODES:     none

INVALIDATIONS: Node 343 ("Say in the five worker contracts that the ground rules may sit in a sibling file of the map") is contradicted: the allowance it added to the five contracts is struck. Node 338 ("Say in graph-conventions.md which file of the map…") is narrowed: its "unless the effort holds it in a sibling file of the map" clause in the `## Notes` bullet is struck, and the rest of the bullet stands. Node 144 ("Make the rules file stand alone") is contradicted in part: its move of the ground rules out of `map.md` into `map-implementation-rules.md` is reversed, though the rules file still stands alone for the five writing rules and the standards list. Node 138 and node 140 ("where the rules a checker is held to live" and the move that carried it out) are narrowed: the ground rules are no longer among what `map-implementation-rules.md` holds, and they reach a checker as text in its spawn. Node 168 is carried out, not changed.

CONDITIONS:    Searched every open or claimed node's `## Acceptance condition` for "sibling file", "map-implementation-rules.md", "Ground rules for this effort", "ground rules", "holds below", "held below", "rules of scope" and "Every rule above is drawn". Nodes 152, 159, 160, 186, 205, 211 and 271 match only on the path, for passages I did not touch (landing policy, worktrees comment, gitignore, commands and so on), so no replacement is needed. Nodes 41 and 80 place the ground rules in `map.md`, which is now true again. Node 56's hits concern a glossary entry, not a location.
Node 190 (open, unclaimed, blocked on this node): its amended clause 4, filed from node 168, now applies, since the block has left the file. Replacement for its clause 1 phrase "this effort's ground rules and its four standing rules for writing":
"this effort's ground rules, stated as held in `map.md`'s `## Notes` and received by a checker as text in its spawn; this effort's five standing rules for writing, stated as held in this file"
Its words are fixed by node 289 (resolved; "five", with the heading "Five standing rules for writing anything in this effort" in the tree) and by this node's work once landed ("held in `map.md`'s `## Notes`", "a checker receives as text in its spawn", now in `map-implementation-rules.md` and `map.md`). Without it, node 190's merge of the two lists could drop what clause 6 here put in.
Seen but not mine: "four standing rules for writing" is stale since node 289 in node 190 clause 1, node 284 clause 4 and node 80. I wrote no replacement except the 190 one above.

MISSING FROM MAP: none

GATE PAYLOAD:  The checker has not run yet, so nothing it found has been fixed.
Paths touched, in two places:
- Worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/348-ground`, branch `worktree-348-ground`, uncommitted:
  - `.claude/skills/expedition/graph-conventions.md`
  - `.claude/skills/expedition-grilling/SKILL.md`
  - `.claude/skills/expedition-research/SKILL.md`
  - `.claude/skills/expedition-prototype/SKILL.md`
  - `.claude/skills/expedition-precondition/SKILL.md`
  - `.claude/skills/expedition-implementation/SKILL.md`
- Main checkout `/home/mathieu/projects/graph-agent`, uncommitted, on top of the record's existing uncommitted changes:
  - `.scratch/graph-workflow/map.md`
  - `.scratch/graph-workflow/map-implementation-rules.md`
  - `.scratch/graph-workflow/map-history.md` (appended only)

The bar: the repo has no build, tests, formatter or CI. I found no manifest or task runner, which matches the rules file's record. So the bar is its non-command half. Each file keeps its wrap width: 105 columns for the shipped prose, and unwrapped lines in the record files.

Proposed commit message:
```
Keep the ground rules in map.md and strike the sibling-file allowance

The effort's ground rules and source declaration sit only in map.md's
## Notes, which every worker reads. Strike "unless the effort holds it
in a sibling file of the map" from graph-conventions.md and the five
worker contracts, and move this effort's ground-rules block back from
map-implementation-rules.md into map.md unchanged.

Node: graph-workflow/348
```

RETROSPECTIVE
1. What I had to hunt for: the `map-history.md` heading convention, which I took from its tail; which nodes introduced the sibling allowance (343 and 338, found via `git log -S`) for INVALIDATIONS; and where node 168's replacement for node 190 was filed (a separate `## Amendment` section, not inside the condition block).
2. What arrived that this node did not need: the note on the 42 KB to 22 KB map rewrite. The quotes the condition relies on all still matched: the pointer paragraph, the block and the "sibling file" sentences.
3. What would have made this easier: the condition naming which sentences of `map-implementation-rules.md` say the file holds the ground rules. Clause 6 says "no sentence", and I found four, spread over three paragraphs. It would also help if clause 6 said whether "the list of standards" means one enumeration or both. There are two until node 190 lands, and I updated both.
4. What was stale, wrong or contradictory: the spawn gave map.md as 22 KB, and it is 21,910 bytes, so that was right. Clause 5's "as committed at HEAD" caused no conflict, since the uncommitted and HEAD copies of the block are identical. Stale elsewhere: "four standing rules for writing" in the conditions of nodes 190, 284 and 80. There is also a latent snag: node 190's condition says the file's "two blocks", and after this node the file holds one.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 339's check; the condition reached it as a verbatim copy in `$TMPDIR/c348.md`.*

> PASS
>
> Node 348, "Keep the ground rules in `map.md` and strike the sibling-file allowance". The work sits in two places:
> - six shipped files, uncommitted in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/348-ground` on base 4b538be;
> - `map.md`, `map-implementation-rules.md` and `map-history.md` in the main checkout. In `map-history.md`, only the block headed "Superseded from `map.md` and `map-implementation-rules.md` at node 348" is this work. The record files' HEAD content is 084aae9.
>
> I read the whole condition in `/tmp/claude-1000/c348.md`. Following the rules file, I read the changed parts of the record files as the work.
>
> **Settled first: a standard moved.** The work moves the ground-rules block, which is one of my standards, out of `map-implementation-rules.md` and into `map.md`.
> - I extracted the block from `git show HEAD:.scratch/graph-workflow/map-implementation-rules.md`: the `**Ground rules for this effort.**` line through the "Every rule above is drawn from a standing preference" paragraph, 9 lines.
> - `cmp` against `map.md` lines 60–68 reports the two byte-identical. So no element the ground rules require or refuse has moved.
> - The same five rules also reached me as text in the spawn, and I held the work against them.
> - The rest of `map-implementation-rules.md`'s standards still stand. Only the sentences saying where the ground rules live were reworded, and the five standing rules for writing are unchanged.
>
> **Parts of the condition**
>
> - **Scope: the nine files and no other, with the shipped files edited plainly.** Met.
>   - The worktree shows exactly the six shipped files. None carries strike-through or a history note.
>   - In the main checkout, the hunks named below are this work. The other uncommitted record changes belong to the map pass and to nodes 346 and 347, which I cannot attribute beyond what the spawn says.
> - **The recorded search.** Met. `git grep -l "sibling file of the map" HEAD -- .claude CONTEXT.md` returns exactly the six files the condition lists.
> - **Clause 1.** Met. The `## Notes` bullet in `graph-conventions.md` now reads "Each lives here and in no sibling file of the map." The two blocks are named after it, and nothing else in the bullet changed apart from rewrapping.
> - **Clause 2.** Met in all five contracts. Each now reads "Each declaration sits in `map.md`'s `## Notes`. Absent any declaration, every source you are pointed at is authoritative." The research contract still ends "A source marked as evidence stays evidence, whatever it says."
> - **Clause 3.** Met. `grep -rn "sibling file of the map" .claude CONTEXT.md` returns only graph-conventions line 84, "and in no sibling file of the map". That line places nothing in a sibling file.
> - **Clause 4.** Met. `map-implementation-rules.md` no longer contains the block: a grep for "Ground rules for this effort" returns 0 and one for "Every rule above is drawn" returns nothing.
> - **Clause 5.** Met.
>   - The block sits in `map.md` at lines 60–68, byte-identical to HEAD as shown above.
>   - It stands where HEAD had the pointer (HEAD line 107), between the "This `## Notes` section also carries two optional blocks…" paragraph and the "five standing rules" pointer, the same neighbours as at HEAD.
>   - The pointer "**Ground rules for this effort, now in …**" is gone from `map.md`.
> - **Clause 6.** Met.
>   - After joining each paragraph onto one line, every mention of ground rules in `map-implementation-rules.md` says `map.md` holds them. No sentence says this file holds them.
>   - The bar's list and the review route both read "this effort's ground rules, which [`map.md`](map.md) holds in its `## Notes` and which a checker receives as text in its spawn".
>   - The five numbered writing rules are not in the diff. Only the lead-in's closing sentence changed, to "where this effort's ground rules, held in [`map.md`](map.md)'s `## Notes`, are rules of scope".
> - **Clause 7.** Met.
>   - The node-348 block appends the `map.md` pointer paragraph and the four replaced sentences of `map-implementation-rules.md`. Each is under a heading naming its file and section.
>   - It also appends the "five standing rules" pointer from `map.md`, whose "too" was dropped. That is one more superseded map sentence, correctly kept.
>   - Each of the six quoted lines is a verbatim substring of the HEAD version of its source file (`grep -F`, 6 of 6 OK). Strike-through text is kept.
>   - The moved block itself is not appended.
>   - `map-history.md`'s diff removes 0 lines.
> - **Clause 8.** Met. Every `](path)` target outside fenced blocks in `map.md` and `map-implementation-rules.md` exists relative to `.scratch/graph-workflow/`. The check printed no missing target.
> - **Clause 9.** See NOT COVERED.
>
> **The bar**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean in the worktree (exit 0) and on the three record files (exit 0).
> - The shipped files keep their wrap width.
>
> **Standards.** I read only the standards in `map-implementation-rules.md`, together with the ground rules, which the spawn and `map.md` carry byte-identically.
> - These bore on the work, and I found nothing against them:
>   - `graph-conventions.md`'s `### Change the map`: verbatim history under mirroring headings, and new statements citing node 348 by link.
>   - The ground rules: each worker contract still stands alone, and nothing assumes a toolchain.
>   - `CONTEXT.md` `_Avoid_` lines.
>   - The writing rules.
>   - `/writing-for-agents`.
> - `/coding-principles` and `/naming` did not bear on the work.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Clause 9, "The worker does not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`." The main checkout's record carries other uncommitted changes that I cannot attribute, and `decisions.md` and `flags.md` are record I was not handed. The files handed to me as the work contain no such write.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`348.1` `ASSUMPTION` **· settled** — In `map.md`'s `## Notes` I dropped the word "too" from the paragraph "**The five standing rules for writing anything in this effort are in [map-implementation-rules.md]…** too". That word leaned on the pointer paragraph clause 5 removes, and left in place it implied the ground rules were in that file as well. The condition does not name this edit, but it limits files and not passages. Its old text is appended to `map-history.md` under its own subheading. What I did: I replaced the one word and appended the prior paragraph verbatim. — Node 348 dropped a "too" from `map.md`'s pointer to the five writing rules, since it implied the ground rules still sat in the rules file.

*The manager's note, 2026-09-27:* the checker left clause 9 not covered. The manager establishes it from its own filing: the only line in `flags.md` written for this node is the `348.1` index line, which the manager wrote when it filed this node's handover (the `190.1` line mentions this node but comes from node 168). `decisions.md` has no line for this node yet, and the node's status was set by the manager.

*The manager's note, 2026-09-27:* flags 348.1 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
