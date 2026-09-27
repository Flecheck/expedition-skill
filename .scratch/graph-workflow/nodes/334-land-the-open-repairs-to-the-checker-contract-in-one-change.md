# Land the open repairs to the checker contract in one change

Type: implementation
Status: resolved
Supersedes: 151, 173, 164
Blocked by: none

## Question

Open nodes 151, 173 and 164 each change `.claude/skills/expedition-checker/SKILL.md` and each forbids other changes to it. Make all their live changes in one node.

*Proposed by [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s worker and filed by the manager, on the human's "ok" to node 329's merge and its conflicts' recommendations.*

## Acceptance condition

*Written by node 329's worker.*

The work is `.claude/skills/expedition-checker/SKILL.md`, path relative to the repository root. The worker may edit that file and no other, and writes no file under `.scratch/`. Done means every one of the following is true of the finished tree.

**A. A method section** *(node 151)*
A1. The file contains a section headed exactly `## How you check`, placed after the section headed `## Hard rules` and before the section headed `## What you hand back`.
A2. That section's body, from its heading to the next line beginning `## `, is at most 2,000 bytes.
A3. It states that the checker splits the acceptance condition into its parts before it reads the work, because its `PASS` owes one line per part.
A4. It states that three things are kept separate and are never merged with or ranked against one another: the acceptance condition, the bar, and the standards the checker reads for itself from `map-implementation-rules.md`. Passing on one of the three never excuses or masks failing on another.
A5. It states that the standards report under the bar, so work that breaches a standard is `FAIL: the bar` and never `FAIL: acceptance condition`.
A6. It states that the checker establishes each part of the condition by a search it can name, and hands that search back, rather than by reading the work through.
A7. It states that the checker says plainly what it did not check.
A8. It states that an effort's own rules may add method specific to that effort on top of this section, and that this section's demands still hold where they do.
A9. The section contains no instruction to search for, look for, discover or otherwise go and find the standards the checker holds work against.
A10. Where the section refers to a shape the file defines elsewhere, it uses the file's own name for it (`PASS`, `FAIL: acceptance condition`, `FAIL: the bar`, `NOT COVERED`) and defines no second version of any of them.
A11. Nothing added to the file names a skill or a plugin, requires anything to be invocable, or assumes a particular repository, machine or toolchain.

**B. The bar's commands** *(node 173)*
B1. The file nowhere states or implies that the checker's spawn may carry the bar's commands. The item in the list of givens that begins `The bar:` today reads "The bar: either its commands for this repo, or the properties alone." and contains "Where you are given the properties and no commands, discover the commands from the repo." After the work it offers no choice between being given commands and being given the properties, and the file holds no sentence conditioned on the checker having been given properties and no commands.
B2. That item states the bar's properties in full: the work builds, it warns about nothing, it is formatted, the tests relevant to it pass, and whatever else the repo itself demands is satisfied. It also states that the checker discovers the commands from the repo itself.
B3. The item says that a repo which states its own commands to an agent typically states them in its own agent-instruction file. That file is named by role and position only, and no particular filename for it appears anywhere in the finished file.
B4. The item keeps its statement that a repo with no build, no tests and no formatter meets the bar on its remaining half, which is "the complete bar for such a repo".
B5. The sentence introducing the givens today reads "You are given six things. The spawn carries the first five, and you read the sixth for yourself from one file this contract names." After the work, the count it states is arithmetically correct for the items the list holds, and it splits them correctly between those that arrive in the spawn and those the checker reads for itself.
B6. The sentence "The implementer works from the same file, so the two of you hold the work to one set of standards." is unchanged. No other sentence claims that the checker and the implementer take the bar's commands from the same place.

**C. Record material in the standards file** *(node 164)*
C1. Under `## The standards you hold the work against`, the file keeps its statement "The file is in the same directory as the record you are blind to, and it may itself hold record material, such as how the work lands, what the effort has decided, or links onward to the rest of the record. Read only the standards in it, and open no other file in the effort's directory." It also states, under the same heading, that the checker says in its outcome that it read only the standards in that file.
C2. The statement beginning "A ground rule is a standing constraint on the effort that is true of any node's work" is unchanged in what it requires.
C3. The statement "Leave the record unread, and do not go looking for it.", with its one exception for `map-implementation-rules.md`, is unchanged in what it requires.

**D. What else may change** *(the union of the fences of 151, 173 and 164)*
D1. Nothing outside the following is deleted or reworded: the new `## How you check` section; the given-list item beginning `The bar:`; the sentence introducing the givens; the sentence C1 adds; and any one sentence elsewhere stating A5's routing, which may be removed as a duplicate of the new section.
D2. No other file is modified.
D3. The working tree meets the bar.

## Answer

The checker contract gains a 1,208-byte `## How you check` section. Its bar given now states properties with commands discovered from the repo, and it says it read only the standards.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `3975732`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Land the open repairs to the checker contract in one change

ANSWER:        `.claude/skills/expedition-checker/SKILL.md` now carries the live changes of superseded nodes 151, 173 and 164. There are three edits and nothing else.

                **A (node 151): a new `## How you check` section.** It sits directly before `## What you hand back`, after `## The standards you hold the work against` and that section's three subsections. The method uses the standards and ends in the shapes the next section defines, so it goes between them. It has six short paragraphs and is 1,208 bytes, heading included, against the 2,000-byte cap. In order, the paragraphs say:
                - split the condition into parts before reading the work, because `PASS` owes one line per part;
                - keep three things separate and never merge or rank them: the condition, the bar, and the standards read from `map-implementation-rules.md`. Passing on one never excuses or masks failing another;
                - the standards report under the bar. A breach is `FAIL: the bar` and never `FAIL: acceptance condition`;
                - establish each part by a search you can name, and hand the search back on the part's line, rather than by reading the work through;
                - say plainly what you did not check, and why. A part of the condition you could not establish, where the rest stands, goes under `NOT COVERED:`. This condition matches the existing `NOT COVERED` section, which already routes the whole-condition case to a raise;
                - an effort's own rules may add method on top of this section. Where they do, every demand of this section still holds.
                The section names no skill or plugin and gives no instruction to find the standards. It uses only the file's own shape names. No existing sentence stated A5's routing (`grep -n -E "FAIL|bar carries|under the bar"`), so nothing was removed as a duplicate. "A standard the bar carries", under `### Where the work moved one of them`, states no routing and was left alone.

                **B (node 173): the given `The bar:`.** It now reads "The bar: its properties, which are that …" and lists all five properties. It says to discover the commands that check them "from the repo itself". It adds that a repo that states its own commands to an agent typically does so "in its agent-instruction file, at the repo's root". The file is named by role and position, and no filename such as CLAUDE.md or AGENTS.md appears anywhere in the file. The item keeps "the complete bar for such a repo". The choice between being given commands and being given properties is gone, and so is the sentence conditioned on having properties and no commands. **The sentence introducing the givens is unchanged, and is correct as it stands.** Six items are listed. The spawn carries items 1 to 5, including the bar as its properties, which is exactly what the manager contract's `## The checker` says the spawn carries ("The bar, as its properties. The spawn says nothing more about the bar."). The checker reads the sixth, the standards, for itself. The discovered commands are part of item 2 and are not a separate given. B6's sentence "The implementer works from the same file …" is unchanged, and no sentence claims the two agents take the bar's commands from the same place.

                **C (node 164):** one sentence is added under `## The standards you hold the work against`, straight after "…open no other file in the effort's directory.": "Say in your outcome that you read only the standards in it." The C2 and C3 statements are untouched.

                **D:** the word diff (`git diff --word-diff=plain`) shows changes only in item 2, the one C1 sentence, and the new section. The line width stays at the file's existing 106 or less. The only longer lines are in the table that was already there.

INDEX LINE:    The checker contract gains a 1,208-byte `## How you check` section. Its bar given now states properties with commands discovered from the repo, and it says it read only the standards.

FLAGS:         ASSUMPTION: I left the sentence introducing the givens ("You are given six things. The spawn carries the first five…") unchanged. B5 asks only that its count and split be correct after the work, and they are. The manager contract's `## The checker` has the spawn carry the bar as its properties, so item 2 still arrives in the spawn. The commands the checker discovers are part of that item, not a seventh given. Nobody asked the human. I read the manager contract, the condition and the checker file, and decided alone.
                Index: I left the checker's givens count ("six, the spawn carries the first five") unchanged, because the spawn still carries the bar as its properties.

                ASSUMPTION: I placed `## How you check` directly before `## What you hand back`, after the standards section and its subsections, rather than directly after `## Hard rules`. A1 allows either. The method uses the standards and leads into the outcome shapes. I decided this alone, with no exchange with the human.
                Index: I placed the checker's `## How you check` directly before `## What you hand back`, which A1 allows, because the method uses the standards and ends in the outcome shapes.

NEW NODES:     none

INVALIDATIONS: none. Consistent with node 145 (four moves in ~15 lines: this is six paragraphs, ~17 lines) and node 167 (commands discovered, spawn does not carry them).

GATE PAYLOAD:  Checker findings: none yet; this is before the first check.
                The bar: I found no build, test or format commands. The repo root holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`. There is no manifest, no task runner, no CI and no agent-instruction file. `.gitignore` ignores `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/`, and invokes nothing. This matches the record in `map-implementation-rules.md`, so there is no difference to report. The non-command half was held as that file states:
                - `CONTEXT.md` `_Avoid_` lines: no refused word is used for its concept in the added text;
                - the five writing rules: each prohibition stands beside a positive, nothing is bolded, and nothing is cited by line number;
                - ground rules 1 to 5: nothing assumes a repo, machine or toolchain, and no skill is named;
                - `/writing-for-agents`: I loaded it for reading only and skipped none of it, since nothing in it conflicted with the hard rules.
                Paths touched: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/334-checker-merge/.claude/skills/expedition-checker/SKILL.md`. Nothing else is modified, uncommitted, on branch `worktree-334-checker-merge`.
                Proposed commit message:
                  Give the checker contract a How you check section and discover the bar's commands

                  Add a method section: split the condition into parts, keep the condition,
                  the bar and the standards separate, report standards under the bar,
                  establish each part by a named search, and say what was not checked. The
                  bar given now states its properties and has the checker discover the
                  commands from the repo, with no route for the spawn to carry them. The
                  checker says in its outcome that it read only the standards in the rules
                  file.

                  Node: graph-workflow/334

Note for the manager, not a finding: the file still says "A standard the bar carries" under `### Where the work moved one of them`, and A4 now says the standards are kept separate from the bar. I read the two as consistent, since A5 has the standards report under the bar, and the sentence is outside D1's fence. A checker might still ask about it.

RETROSPECTIVE
1. What I had to hunt for: whether the checker's spawn still carries the bar's properties. B5 turns on that. I found it in `.claude/skills/expedition/SKILL.md` under `## The checker`, after first looking in the checker file and node 173. I also read node 173 for what B5 intended, because the merged condition does not say whether the bar counts as a spawn given.
2. What arrived that this node did not need: most of `map.md`, including the concurrency, retrospective, worktree, token and naming bullets. Only its `## Notes` rule about related defects and the pointer to the rules file bore on this node. Of `map-implementation-rules.md`, the history, supersession and record-as-work paragraphs bore on nothing here. I needed only its bar paragraph, the ground rules and the writing rules. `decisions.md` needed one grep, and one hit (node 167) bore on the work.
3. What would have made this easier: one line in the spawn or the condition saying that the manager contract has the spawn carry the bar as its properties, so the reader knows whether item 2 counts as a spawn given. A clause D1 could also name "the sentence C1 adds" by its position, as B does for the item.
4. What was stale, wrong or contradictory: nothing stale. One small gap: the manager contract's list of what the checker receives omits "the name of the work", while the checker's givens list it as item 4, carried by the spawn. This was already there and is outside this node's fence. It may belong to an open node against the manager contract, if one exists.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 333's first check.*

> Node 334, "Land the open repairs to the checker contract in one change"
>
> PASS
> - A1: `grep -n '^## '` lists `## How you check` at line 170. It comes after `## Hard rules` (line 70) and before `## What you hand back` (line 192), and the heading text is exact.
> - A2: I counted the section body with awk, from its heading to the next `## ` line. It is 1,208 bytes with the heading and 1,191 bytes without it, both under 2,000.
> - A3: I read the section. Its first paragraph says to split the condition into parts before reading the work, "because your `PASS` owes one line per part".
> - A4: I read the section. It names the three things (the condition, the bar, and the standards "you read for yourself from `map-implementation-rules.md`") and says to hold the work against each on its own. It says "Never merge them, and never rank one against another. Passing on one of the three never excuses or masks a failure on another."
> - A5: The section says "The standards report under the bar", and says to report a breach as `FAIL: the bar` and never as `FAIL: acceptance condition`.
> - A6: The section says to establish each part "by a search you can name", to hand that search back on the part's line, and to search "rather than reading the work through".
> - A7: The section says "Say plainly what you did not check, and why."
> - A8: The section's last paragraph says an effort's own rules may add method, and "Every demand of this section still holds."
> - A9: The section's only reference to the standards points at `map-implementation-rules.md` as the place they are read from. It holds no instruction to search for or find them.
> - A10: The section uses `PASS`, `FAIL: the bar`, `FAIL: acceptance condition` and `NOT COVERED:` by the file's own names, and defines none of them again.
> - A11: I searched the added lines of the diff for skill, plugin, invocable, and tool or command names, and found none. The one filename in the new text is `map-implementation-rules.md`, which the contract already names. The new text names the agent-instruction file only by its role and position.
> - B1: `grep -n -i command` over the whole file finds no sentence that depends on having been given the properties without the commands, and no sentence saying the spawn may carry commands. The rest of its hits are about extents and recorded searches. Item 2 now reads "The bar: its properties, …" and offers no choice.
> - B2: Item 2 lists all five properties. It says "Discover the commands that check these properties from the repo itself."
> - B3: Item 2 says "typically states them in its agent-instruction file, at the repo's root". A grep of the whole file for CLAUDE.md, AGENTS.md, README, GEMINI, .cursorrules and copilot returns nothing.
> - B4: Unwrapped, item 2 keeps "meets the bar on its remaining half, which is the complete bar for such a repo."
> - B5: The introducing sentence is unchanged, and it is still correct. The list holds six items. Items 1 to 5 arrive in the spawn, and item 2's properties are among them. Item 6, the standards, is read from the file the contract names. The bar's commands are not an item of the list.
> - B6: `grep -n -i 'same file\|same place\|implementer'` shows the sentence "The implementer works from the same file…" unchanged. No other hit says the checker and the implementer take commands from the same place.
> - C1: The quoted sentences are unchanged. Directly after them, under the same heading, the work adds "Say in your outcome that you read only the standards in it."
> - C2 and C3: The diff has no hunk touching either statement.
> - D1: The diff has four hunks: item 2, the C1 addition, the new section, and nothing else. The introducing sentence was not changed, which D1 allows. The optional removal of a duplicated routing sentence was not taken.
> - D2: `git status --short --untracked-files=all` in the worktree lists only `.claude/skills/expedition-checker/SKILL.md`. Nothing under `.scratch/` changed.
> - D3: See the bar below.
>
> The bar: the repo has no build, no tests, no formatter and no CI. The worktree root holds only `CONTEXT.md` and `.claude/`, with no manifest or task runner. So the bar here is its remaining half, the standards. `git diff --check` printed nothing and exited 0.
>
> Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`. It is unchanged since `084aae9`, the base of this branch. The standards are `/coding-principles`, `/naming`, the `_Avoid_` lines in `CONTEXT.md`, `graph-conventions.md`, `/writing-for-agents`, the five ground rules and the five standing rules for writing. The ones that bore on this work:
> - the ground rules: nothing added assumes a repo, a machine or a toolchain, and nothing addresses the human;
> - the writing rules: each prohibition sits beside its positive, and nothing new is bolded;
> - `/writing-for-agents`, which I read and applied myself;
> - the `_Avoid_` lines, checked by hand: no refused word is used for its refused concept.
>
> The work does edit a copy of the checker contract, but the standards file is not among the changed paths, so no standard moved. The rules name no reviewing skill, so I ran none. I read the changed path as the work under check.
>
> QUESTIONS:
> - Where does a standards breach send the work? Clause A5 routes a breach of a standard to `FAIL: the bar`. Clause D1 forbids rewording the existing sentence under `### FAIL`, "An unmet condition sends the work back for changes to the feature, and an unmet bar sends it back for changes to the build."
>   - Complying with both leaves the file saying that a prose-standard breach, such as one of the writing rules, sends the work back "for changes to the build". That is not what such a repair is.
>   - The wording and the fence are the condition's own, so they were not the worker's to depart from. This does not affect the `PASS`.
>   - Form: any sentence in the file that says what a bar failure sends back, in terms that cover only build or command failures.
>   - Extent: `grep -n 'changes to the build' .claude/skills/expedition-checker/SKILL.md` returns one hit, line 290. I found no other statement of this form while reading the file, but the instance may not be the only one.
>
> I am ready for node 333's re-check.

*The manager's note:* the checker's question is [node 329](329-group-the-open-nodes-against-the-worker-contracts.md)'s conflict 4, on which the human took option (a), "Leave that sentence fenced and unchanged", with their "ok". It goes to the human at this node's gate.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*

## Flags

`334.1` **· settled** `ASSUMPTION` — I left the sentence introducing the givens ("You are given six things. The spawn carries the first five…") unchanged. B5 asks only that its count and split be correct after the work, and they are. The manager contract's `## The checker` has the spawn carry the bar as its properties, so item 2 still arrives in the spawn. The commands the checker discovers are part of that item, not a seventh given. Nobody asked the human. I read the manager contract, the condition and the checker file, and decided alone.

`334.2` **· settled** `ASSUMPTION` — I placed `## How you check` directly before `## What you hand back`, after the standards section and its subsections, rather than directly after `## Hard rules`. A1 allows either. The method uses the standards and leads into the outcome shapes. I decided this alone, with no exchange with the human.
