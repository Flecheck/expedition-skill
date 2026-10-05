# State in the retrospective bullet the form a standing item's name is written in

Type: implementation
Status: claimed
Blocked by: 220

## Question

map-manager-only.md's retrospective bullet has the worker name each standing item it reports, but fixes no written form. Entry (j) of derivations.md finds names in exactly one form, as the human settled at node 220's raise 1 on 2026-10-04. A name written in any other form is invisible to it, and so to the next worker looking for a name to reuse.

*Reported by [node 220](220-derive-how-many-times-each-standing-item-was-reported.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "220 (the entry the bullet points at must have landed)". On joining: "node 284 also edits `map-manager-only.md`, but only its *How the worktree is made* Create bullet, which is a different concern."*

## Acceptance condition

*Authored by node 220's worker and filed by the manager.*

> The work is an edit to one file, `.scratch/graph-workflow/map-manager-only.md`. Nothing else changes.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `.scratch/graph-workflow/map-manager-only.md`, the bullet beginning **"Every worker returns a retrospective as the last handover part, on this effort only"** states that the worker writes each standing item's name as a numbered or bulleted list item of its retrospective, whose text opens with the name in a code span. The name is two or more words of lowercase letters and digits joined by hyphens. The name is followed in that list item by the count of earlier retrospectives carrying it and their node ids.
> 2. That bullet states that the existing names, with their counts and node files, are obtained by running the entry headed `## (j) Item names carried by the retrospectives` in `.scratch/graph-workflow/derivations.md`, and that a name written in any other form is not found by that entry.
> 3. No statement already in that bullet is changed or removed. In particular, the human's quoted instruction beginning *"Could you, for this effort only, ask subagents"* and the four questions numbered (1) to (4) are unchanged character for character.
> 4. No file under `.claude/` is modified, and no file in `.scratch/graph-workflow/` other than `map-manager-only.md` is modified.
> 5. The tree meets the bar.
>
> The scope came from no search: the named bullet is the work, not an instance of a defect.

## Amendment, 2026-10-04 (from node 220, correction round 1)

*Written by [node 220](220-derive-how-many-times-each-standing-item-was-reported.md)'s worker, the author of this node's condition, in its correction-round handover, and filed by the manager before this node is claimed. The worker's words, pasted:*

- "In its clause 1, after "joined by hyphens", add: "The list item may sit inside a blockquote." This keeps it matched to entry (j)."

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      State in the retrospective bullet the form a standing item's name is written in

ANSWER:        In `.scratch/graph-workflow/map-manager-only.md`, the bullet beginning "Every worker returns a retrospective as the last handover part, on this effort only" now says what written form a standing item's name takes. I added seven sentences straight after the existing sentence "It finds the existing names by searching the retrospective sections … and not from memory or from any list held elsewhere." and before "Two duties on the manager". Nothing in the bullet was changed or removed. The text inserted:

               "The worker writes each standing item's name as a numbered or bulleted list item of its retrospective. The text of that list item opens with the name in a code span. The name is two or more words of lowercase letters and digits joined by hyphens. The list item may sit inside a blockquote. In the same list item, the name is followed by the count of earlier retrospectives that carry it and by their node ids. The worker obtains the existing names, with their counts and node files, by running the entry headed `## (j) Item names carried by the retrospectives` in [derivations.md](derivations.md). That entry does not find a name written in any other form. The written form was settled at [node 220](nodes/220-derive-how-many-times-each-standing-item-was-reported.md)."

               Decisions behind it, so a later reader does not have to work them out again:
               - Where it goes. The new sentences sit straight after the existing "finds the existing names by searching" sentence. Read in that order, running entry (j) is how that search is done, and it does not look like a second, competing method. The existing sentence says "retrospective sections … whatever heading", while entry (j) also reads `RETROSPECTIVE` parts pasted from handovers. That sentence is frozen by clause 3, so it stays as it is.
               - The blockquote sentence is the amendment filed by node 220's worker. It matches entry (j)'s own text: "The list item may sit inside a blockquote, behind one or more `>` markers."
               - Who settled the form. I checked node 220's file: the human answered "ok" on the RECOMMENDED of raise 1 on 2026-10-04 (its "#### The human's answer to raise 1, 2026-10-04" and the handover's "What an item name is"). Writing rule 2 asks for a citation, so the bullet cites node 220.
               - I wrote "each standing item's name" in full, not "each name", so the subject matches clause 1 word for word.

INDEX LINE:    map-manager-only.md's retrospective bullet now fixes the written form of a standing item's name, a kebab-case code span opening a list item, and points at derivations.md entry (j).

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none. The bullet's earlier statements stand as they were. Node 212's answer says names are found by searching "the retrospective sections". Node 220 already recorded that narrowing and extension in its own INVALIDATIONS. This node does not change it further.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open and claimed node for: `short name`, `item name`, `standing item`, `retrospective bullet`, `Every worker returns a retrospective`, `(j)`, `map-manager-only`, `name form`, `code span`, `kebab`. Matches outside node 387 itself:
               - node 149 (open): names `map-manager-only.md` only as a file that is not the rules file. My work does not affect it.
               - node 385 (claimed): only a retrospective line, which is not part of its condition or question. My work does not affect it.
               I wrote no replacement clauses, and no open node's question changes.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched: `.scratch/graph-workflow/map-manager-only.md` (one line changed, an insertion within the bullet's paragraph). Nothing under `.claude/` was changed, and no other file in `.scratch/graph-workflow/`.
               Bar: `map-implementation-rules.md` records no build, tests, formatter or CI. I checked the repo again: there is no manifest or task runner, and the only ignore file is `.gitignore`, which runs nothing. The command half of the bar is therefore empty, and the bar is the standards plus the acceptance condition. The record and the repo agree.
               Checks I ran:
               - `git diff --word-diff` shows only inserted text, so clause 3 holds and the quoted human instruction and questions (1) to (4) are untouched.
               - `git status --short` lists only `map-manager-only.md`, so clause 4 holds.
               - Entry (j) of derivations.md, run from `.scratch/graph-workflow/`, works and prints nothing on stderr.
               Skipped from a method skill: none were invoked.
               Proposed commit message:
                 State the written form of a standing item's name in the retrospective bullet

                 map-manager-only.md's retrospective bullet now has the worker write each
                 standing item's name as a list item opening with a kebab-case code span,
                 followed by its count and node ids, and get existing names from
                 derivations.md entry (j), which finds no other form.

                 Node: graph-workflow/387

RETROSPECTIVE
(Counts derived 2026-10-05 by running derivations.md entry (j). Not authoritative, for scale only.)
1. What I had to hunt for: little. I had to confirm that the human settled the one written form at node 220's raise 1. The node question says so, and I checked it by grepping node 220 for "raise 1" and "written form", which found "#### The human's answer to raise 1, 2026-10-04" straight away. To find entry (j) I grepped derivations.md headings and read only that entry.
2. What arrived that this node did not need:
   - `rules-file-read-whole-for-one-section` — 3 earlier retrospectives carry it: 178, 220 (twice). I read map-implementation-rules.md whole for a node whose work is a record file with an empty bar. Only the bar's commands paragraph and the standards list bore on the work. The "record work" paragraph would have mattered only to a checker.
   - `map-read-whole-for-a-few-items` — 3 earlier retrospectives carry it: 178, 220, 284. Of map.md only the six writing rules and the dated-number rule bore on this one-paragraph insertion.
   - map-manager-only.md, the file I edited, was read whole as well, about 270 long lines, to change one bullet. The edit needed only that bullet. A heading per bullet, or a spawn saying "read the bullet, the file is manager-only", would have avoided it.
3. What would have made this node easier: nothing. The spawn quoted the condition with its amendment, gave the bullet's opening words, and checked the facts before I needed them.
4. What was stale, wrong or contradicted something else:
   - `record-is-not-mechanically-scannable` — 3 earlier retrospectives carry it: 178, 212, 220. Node 385 (claimed) has a retrospective that writes "- Standing item `nothing-pointed-me-at-it`. 1 earlier retrospective carries the name: 178." The list item opens with prose, not with the code span, so entry (j) does not count it. Its own text also says kebab-case names are in node 243, and entry (j) finds none there. This is the defect this node fixes, met in a live retrospective. The fix only works from now on.
   - The manager's note was right: the bullet still says "under the heading `## Retrospective` and under no other heading", and "searching the retrospective sections … whatever heading". My insertion does not make this worse. If anything, "The list item may sit inside a blockquote" admits that retrospectives also sit inside pasted handovers.
`````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-05. A fresh checker; the condition and its author's amendment reached it as a verbatim copy in `$TMPDIR/c387.md`. The node holds no flags.*

> PASS
>
> Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/387-name-form (branch worktree-387-name-form). I compared the working tree against HEAD for `.scratch/graph-workflow/map-manager-only.md`. The changed path is a record file. Under the rules file's rule on record files, I read it as the work under check and derived no intent from it. The bullet is one physical line, so no unwrapping was needed. All phrase checks ran in python over that line, taken by `grep '^- \*\*Every worker returns a retrospective as the last handover part, on this effort only\*\*'`. That grep matches exactly 1 line, line 80.
>
> Parts of the acceptance condition. Clause 1 is checked as amended, with "The list item may sit inside a blockquote." inserted after "joined by hyphens".
>
> 1. Clause 1 (numbered or bulleted list item, opening with the name in a code span; two or more lowercase-letter/digit words joined by hyphens; may sit inside a blockquote; followed in that list item by the count of earlier retrospectives carrying it and their node ids). Met. Substring checks on the bullet were all True for "numbered or bulleted list item", "opens with the name in a code span", "two or more words of lowercase letters and digits joined by hyphens", "The list item may sit inside a blockquote" and "count of earlier retrospectives that carry it and by their node ids". The check `"joined by hyphens. The list item may sit inside a blockquote." in bullet` is True, so the amendment sits where it says.
> 2. Clause 2 (names, counts and node files obtained by running entry `## (j) Item names carried by the retrospectives` in derivations.md; a name in any other form is not found by that entry). Met. The bullet contains "by running the entry headed `## (j) Item names carried by the retrospectives` in [derivations.md](derivations.md)" and "That entry does not find a name written in any other form." Both substring checks are True. `test -e .scratch/graph-workflow/derivations.md` succeeds, so the link resolves. I did not open derivations.md, a record file I was not handed, so I did not check that heading (j) exists there. The condition does not demand it.
> 3. Clause 3 (no existing statement changed or removed; the quoted instruction and (1) to (4) unchanged character for character). Met. `git diff --word-diff=porcelain` shows only `+` tokens and no `-` tokens. In python, the new bullet with the inserted passage removed once equals the HEAD bullet exactly (True). The full quoted instruction `*"Could you, for this effort only, ask subagents, ... something else ?)."*` is present in both the old and new bullet (True/True). The 985-character span from "(1) what did you have" through "contradicted something else." in the HEAD bullet appears unchanged in the new bullet (True).
> 4. Clause 4 (nothing under `.claude/` and no other file in `.scratch/graph-workflow/` modified). Met. `git diff --name-only` lists only `.scratch/graph-workflow/map-manager-only.md`. `git diff --name-only -- .claude | wc -l` gives 0. `git status --porcelain --untracked-files=all` shows only ` M .scratch/graph-workflow/map-manager-only.md`, with no untracked files.
> 5. Clause 5 (the tree meets the bar). Met; see below.
>
> The condition records no search ("The scope came from no search"), so there was no recorded command to rerun.
>
> The bar.
> - Commands: the repo root holds no CLAUDE.md or AGENTS.md. It has no manifest, task runner, formatter config or CI (`find` for CLAUDE.md, AGENTS.md, package.json, Makefile, *.toml, .pre-commit*, .editorconfig, .prettierrc*, .markdownlint* and justfile, excluding .git, returned nothing). That matches what the rules file records: no build, no tests, no formatter. So the bar's command half is empty. `git diff --check` reported no whitespace errors, and the file ends in a newline.
> - Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`. They are `/coding-principles` and `/naming`, the glossary's `_Avoid_` lines, the ground rules, the six standing rules for writing, `graph-conventions.md` and `/writing-for-agents`. No reviewing skill is named, and I ran none. Eight standards bore on the work, each held by hand:
>   - Glossary `_Avoid_`: I found no refused word used for its refused concept. "item" means a list item or the existing term "standing item", not a node. "running the entry" means running a command, not an effort or an attempt.
>   - Writing rule 2 and graph-conventions `## Writing the map`: the new text states the current form and cites [node 220] by markdown link, and the link resolves (`ls nodes/220-derive-how-many-times-each-standing-item-was-reported.md`).
>   - Writing rule 4: it cites by heading, with no line numbers.
>   - Writing rule 5: no bold was added, there is one idea per sentence, and each pronoun has one referent. "That entry does not find..." states a fact, not a prohibition.
>   - Writing rule 6: it points at a heading of derivations.md.
>   - Graph-conventions `### Change the map`, check 11: the change removes nothing, so nothing is owed to map-history.md.
>   - Graph-conventions, the 500-byte target: the bullet sits in `## Notes`. The target "reports and never fails" and was already far exceeded before this change, so it is not a defect.
>   - `/writing-for-agents`: covered under the question below.
>
>   `/coding-principles`, `/naming` and the ground rules for shipped files did not bear on the work: this is no code, and the file is not shipped.
> - Rules file: I read the changed path as the work under the rules file's rule on record files. Neither decisions.md nor flags.md nor any status line changed.
>
> QUESTIONS:
> - The bullet now says twice how the worker finds existing names, and the condition is what produced this. Clause 3 forbids changing or removing any statement already in the bullet, so the worker could not merge the old sentences with the new ones. The two pairs:
>   - "It finds the existing names by searching the retrospective sections of the files under `.scratch/graph-workflow/nodes/`, whatever heading each section was filed under, and not from memory or from any list held elsewhere." now sits beside "The worker obtains the existing names, with their counts and node files, by running the entry headed `## (j) ...` in [derivations.md](derivations.md)."
>   - "It states how many earlier retrospectives carry that name, and lists their node ids." now sits beside "In the same list item, the name is followed by the count of earlier retrospectives that carry it and by their node ids."
>
>   `/writing-for-agents` (Pruning: "Keep each meaning in a single source of truth ... Duplication costs maintenance and tokens") counts two statements of one meaning as a defect. A reader could also take the first pair as two different methods. The older one says to search the sections "whatever heading each section was filed under". I cannot tell whether entry (j) covers every heading, because derivations.md is a file I may not read. The wording is the condition's own, so it was not the worker's to change. Should a later change fold the older sentence of each pair into the newer one?
>   - Form: within this one bullet, an older sentence and a sentence added by this work state the same act (how existing names are found, or what follows the name).
>   - Extent: the smallest set is the two pairs above. I computed it by comparing each inserted sentence with the HEAD bullet's sentences about names. The other inserted sentences (list-item form, code span, hyphenated name, blockquote, the "other form" consequence and the node 220 citation) have no counterpart in the HEAD bullet.
>
> The node holds no flags, so I had none to check. I left the tree as I found it. I removed the temporary directory I made under $TMPDIR, and `git status` shows only the work's one modification.

*The manager's note:* the checker handed back a question beside its outcome, so the standing yes does not cover this gate. It goes to the human.

### Gate — approve, 2026-10-05

`verbatim`: *"ok"*

*The manager's note:* the manager's message ended "Please approve node 387, or tell me to send it back for the fold now.", and recommended approving as is, with the fold of the checker's two duplicated pairs left to a later change. The reply takes the approval. The fold is not yet a node.
