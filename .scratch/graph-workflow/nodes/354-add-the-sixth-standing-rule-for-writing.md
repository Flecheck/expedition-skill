# Add the sixth standing rule for writing: point at a heading of a file the reader already reads

Type: implementation
Status: claimed
Blocked by: 352

## Question

Write node 253's rule as the sixth standing rule for writing, in the list that holds the other five.

*Reported by [node 253](253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)'s worker under its `NEW NODES`, and filed by the manager.*

## Acceptance condition

*Authored by node 253's worker and filed by the manager.*

> The work is `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-implementation-rules.md` and `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
> 1. In `map.md`'s `## Notes`, the numbered list of this effort's standing rules for writing, inside the block that begins with the bold line "**Ground rules for this effort.**", ends with a sixth rule, word for word as below. Rules 1 to 5 of that list are not reworded, renumbered or reordered.
>    6. **Point at a heading of another shipped file instead of restating what it holds, where the reader is already told to read that file.** Where the reader is not, restate what the reader needs when the file pointed at is mostly text that reader does not need, so the reader is not sent to read it. A passage that changes a rule for its own case names that rule by heading and states the change in its own words. Rename a heading that another shipped file cites only in the change that updates every citation of it, found by searching the shipped files for the heading's exact text.
> 2. The list's bold lead-in links `nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md` as the node that fixed the sixth rule. Wherever the lead-in gives the number of rules, it says six.
> 3. No sentence in `map.md`, `map-implementation-rules.md` or `map-manager-only.md` gives the number of this effort's standing rules for writing as four or five.
> 4. Every text this work removes from `map.md` or `map-implementation-rules.md` is appended verbatim to `map-history.md`, under a heading that mirrors the section it came from, with struck-through text staying struck through. `map-history.md` gains text and loses none.
> 5. Every markdown link in the three files resolves to a path that exists.
>
> Scope search for clause 3: `grep -rn -i "rules for writing" .scratch/graph-workflow/map.md .scratch/graph-workflow/map-implementation-rules.md .scratch/graph-workflow/map-manager-only.md .claude/skills`. Run over the working tree on 2026-09-27, before node 352 landed, it returned 1 line in `map.md` (the paragraph beginning "The five standing rules for writing anything in this effort") and 3 matches in `map-implementation-rules.md` (the bar paragraph, and the review route paragraph twice). It returned none in `map-manager-only.md` or `.claude/skills`. Node 352 moves these lines, so the worker re-runs the command on the tree it starts from and edits every match in the three editable files. A match the search reaches in any other file is reported, not edited.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-28. The worker's own text, pasted.*

````
HANDOVER:      Add the sixth standing rule for writing: point at a heading of a file the reader already reads

ANSWER:
**Node 253's rule is now the sixth standing rule for writing.** It is in `map.md`'s `## Notes`, in the numbered list inside the ground-rules block, and its wording matches the acceptance condition's rule 6 exactly. Rules 1 to 5 are unchanged.

- **The lead-in** now reads "The first four were fixed by [node 53](…), the fifth by [node 289](…) and the sixth by [node 253](nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)." The lead-in never stated a count, so no number was added to it.
- **`map-implementation-rules.md`** gave the count as "five" in three places: the bar's list of its non-command half, the review route's list of the standards, and the review route's sentence naming the two blocks that pass node 42's test. All three now say "six", and nothing else in those sentences changed.
- **`map-history.md`** has one new section at its end, "Superseded from `map.md` and `map-implementation-rules.md` at node 354 — the standing rules for writing counted as five". It has four subsections, each headed with the file and section the text came from, the same way node 352's section is laid out. They hold the old lead-in paragraph and the three old sentences, copied verbatim. Each sentence is shown without the rest of its paragraph, as node 352's section does. None of the removed text contained struck-through text. Nothing already in `map-history.md` was changed.
- **The scope search was re-run on the tree this node started from (master `2490b5b`, after node 352):** `grep -rn -i "rules for writing" .scratch/graph-workflow/map.md .scratch/graph-workflow/map-implementation-rules.md .scratch/graph-workflow/map-manager-only.md .claude/skills`. It returned 1 line in `map.md` (the lead-in, which gives no count) and 2 lines in `map-implementation-rules.md` (the bar paragraph, and the review-route paragraph with two matches). It found nothing in `map-manager-only.md` or `.claude/skills`, and nothing outside the three editable files. A wider grep over the same three map files for "four/five … rules" and for "writing rules" found nothing else. After the edit, the same command finds only the lead-in and three "six standing rules for writing" matches.
- **Links:** every markdown link in the three files resolves. That is 62 in `map.md`, 39 in `map-implementation-rules.md` and 401 in `map-history.md`, checked by a script that tested each relative target with `os.path.exists`.

INDEX LINE:    Node 253's rule is now the sixth standing rule for writing in map.md's ground-rules block, and every count of those rules in the map now says six.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS:
- Node 352 (resolved), an extension. Its answer puts "the five standing rules for writing" in `map.md`'s ground-rules block. That list now holds six.
- Node 349 (resolved), an extension. It is named for "the five standing rules for writing", and its answer is about moving those five. The list it moved now has a sixth rule.
- Node 289 (resolved), an extension. It fixed the fifth rule and the count "five". The count is now six.

CONDITIONS:    I searched the `## Question`, `## Acceptance condition` and `## Amendment` sections of every node whose status is not resolved, superseded, dropped or closed, claimed nodes included. The terms were: "four/five/six/4/5 (standing) rules", "rules for writing", "writing rules", "sixth rule" and "fifth rule". Matches: 190, 284, and 354 itself.
- Node 190 (open, unclaimed). Node 349's amendment of its clause 1 contains the phrase "this effort's five standing rules for writing, stated as held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn". Replacement: "this effort's six standing rules for writing, stated as held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn". Node 349's amendment of its clause 4 reads "4. The file states neither the five ground rules nor the five standing rules for writing as a numbered list. Where it names them, it names `map.md`'s `## Notes` as holding them." Replacement: "4. The file states neither the five ground rules nor the six standing rules for writing as a numbered list. Where it names them, it names `map.md`'s `## Notes` as holding them." In both, "six" is fixed by this node's work landed in the tree: `map.md`'s list ends at rule 6, and `map-implementation-rules.md` says "six standing rules for writing". There are still five ground rules in `map.md`. Node 190's original clauses 1 and 4, which say "four", were already replaced by earlier amendments.
- Node 284 (open, unclaimed). Clause 4's bar sentence says "this effort's ground rules and four standing rules for writing". The manager's note of 2026-09-23 on that node already records that this is stale. Replacement for that phrase: "this effort's ground rules and six standing rules for writing". It is fixed by the same landed work.
- No open node's question is changed by this work. Node 355's question refers to "node 253's rule", which this work places without renaming it.

MISSING FROM MAP: none

GATE PAYLOAD:
- Checker findings: none yet (no checker has run).
- Paths touched (all in the worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/354-sixth-rule`):
  - `.scratch/graph-workflow/map.md`
  - `.scratch/graph-workflow/map-implementation-rules.md`
  - `.scratch/graph-workflow/map-history.md` (one section appended at the end, for you to integrate at landing alongside node 230's appends)
- The bar: the repo has no build, tests, formatter or CI. The root holds only `.claude`, `.scratch`, `CONTEXT.md`, `CONTEXT-MAP.md` and `.gitignore`, with no manifest and no `.github`. That matches the rules file's record, so only the non-command half applies.
- Skipped method-skill parts: none, because no method skill was used.
- Proposed commit message:
  ```
  Add the sixth standing rule for writing: point at a heading of a file the reader already reads

  map.md's writing-rules list gains node 253's rule as rule 6, and its lead-in
  names node 253. map-implementation-rules.md counts six rules where it said
  five. The superseded lead-in and sentences are in map-history.md.

  Node: graph-workflow/354
  ```

RETROSPECTIVE
1. What I had to hunt for: very little. I had to find how `map-history.md` lays out a replacement that shows single sentences. Node 352's section, the one just before, served as the template. I found node 190's current amended clause wording by searching its amendments.
2. What arrived that this node did not need: most of node 253's `## Answer` region, especially the interview payload. The rule text and the acceptance condition were already on the node file.
3. What would have made this easier: the node file or the spawn could have said that after node 352 the lead-in no longer states any count. Clause 2's "wherever the lead-in gives the number" then applies to nothing, and I had to work that out.
4. What was stale, wrong or contradictory: the condition's recorded search result (1 match in `map.md` "The five standing rules…", 3 in the rules file) was out of date after node 352, as the condition itself warned. The re-run found a lead-in with no count and the same three matches in the rules file. Node 284's clause 4 still says "four" and node 190's amendments say "five". Replacements for both are under CONDITIONS.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 230's check; the condition reached it as a verbatim copy in `$TMPDIR/c354.md`.*

> PASS
>
> This is the check of node 354, "Add the sixth standing rule for writing: point at a heading of a file the reader already reads". The work is the uncommitted diff to three record files, `.scratch/graph-workflow/map.md`, `map-implementation-rules.md` and `map-history.md`. It sits in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/354-sixth-rule`, on base 2490b5b. Under the rules file, I read these record files as the work. I read the whole condition in `/tmp/claude-1000/c354.md`.
>
> **Settled first:** the work adds an element to the writing rules, which are among my standards. Rules 1–5 and the ground rules are unchanged: all are context lines in the diff. I held the work against those. I did not hold the work against the rule it adds.
>
> **Parts of the condition**
>
> - **Scope:** met. `git status --short --untracked-files=all` shows only the three files. No node file, `decisions.md` or `flags.md` changed.
> - **1:** met.
>   - The list inside `map.md`'s ground-rules block now ends with rule 6.
>   - `grep -qxF` matches the whole of that line against the condition's rule 6 text, character for character.
>   - Rules 1–5 are unchanged context lines, in the same order.
> - **2:** met.
>   - The lead-in now reads "The first four were fixed by [node 53](…), the fifth by [node 289](…) and the sixth by [node 253](nodes/253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)."
>   - It gives no total count, so there is no number that would need to say six.
> - **3:** met. I joined each file's wrapped lines into unbroken paragraphs. `grep -noiE '(four|five|4|5) (standing )?(rules|writing rules)'` over `map.md`, `map-implementation-rules.md` and `map-manager-only.md` then finds nothing. The rules file's three counts now read "six standing rules for writing":
>   - the bar paragraph;
>   - the review route;
>   - the node-42 sentence.
> - **4:** met.
>   - The node-354 block in `map-history.md` appends the replaced lead-in and the three replaced rules-file sentences. Each sits under a heading that mirrors the section it came from.
>   - Each of the four quoted lines matches HEAD's `map.md` or `map-implementation-rules.md` exactly under `grep -F`.
>   - The diff of `map-history.md` removes 0 lines.
> - **5:** met. Every `](path)` target outside fenced blocks in the three files exists: relative paths resolved from `.scratch/graph-workflow/`, and the one absolute path, `/home/mathieu/projects/Lang`, checked directly.
> - **Scope search:** I re-ran `grep -rn -i "rules for writing"` over the four paths it names. It returns `map.md` line 68 (the lead-in) and `map-implementation-rules.md` lines 39 and 41, and nothing in `map-manager-only.md` or `.claude/skills`. Every hit is in an editable file and edited, so nothing outside needs reporting.
>
> **The bar**
>
> - The rules file records no build, tests, formatter or CI, and the repo confirms it.
> - `git diff --check` is clean (exit 0).
>
> **Standards.** These bore on the work, and I found nothing against them:
> - the ground rules;
> - writing rules 1–5, including rule 4, since citations are by heading and link;
> - `graph-conventions.md`'s `### Change the map`;
> - the glossary's `_Avoid_` lines;
> - `/writing-for-agents`.
>
> No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - None of the condition's parts is uncovered. The ban on writes to the node, `decisions.md` and `flags.md` is established from the worktree diff.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

none
