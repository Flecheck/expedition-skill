# The rules file states one list of standards twice

Type: implementation
Status: claimed
Supersedes: 271

Blocked by: 184, 348, 349, 352, 354

## Question

*Surfaced by [The bar's project criteria and the review route's standards are still two different lists](184-the-bar-and-the-standards-are-two-different-lists.md)'s worker, and pasted as it wrote it.*

> `map-implementation-rules.md`'s `## What the work is held against` holds two enumerations that, after node 184, name
> the same standards — the bar paragraph's non-command half and the review route's *"standards to hold work against"*.
> Two copies of one list drift, and this one has now been reconciled by hand twice: node 169 struck `map.md`'s
> standing preferences from the bar's copy, and node 184 added `graph-conventions.md` and `/writing-for-agents` to it.
> Both were repairs to a divergence that the duplication itself produced. Should the section state the standards once,
> in a block both paragraphs point at, leaving each paragraph to carry only what is particular to its own reader?

**Blockers, in the worker's words:** *"184."*

## Acceptance condition

*Written by node 184's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited. The worker may
> not mark this node, resolve it, or write a line in `decisions.md` or `flags.md`.
>
> Done means all of the following are true of the finished tree.
> 1. The section `## What the work is held against` states the standards an implementation node's work is held against
>    **once**, as a single enumeration under its own bold lead-in, naming at least: the human's global coding
>    principles (`/coding-principles`) and `/naming`; `CONTEXT.md`'s `_Avoid_` lines; this effort's ground rules and
>    its four standing rules for writing; `graph-conventions.md`; and `/writing-for-agents`.
> 2. The paragraph beginning `**The bar's commands for this repo, discovered on first use**` and the paragraph
>    beginning `**The review route for this repo, discovered on first use**` each point at that single enumeration
>    rather than restating it, and each retains what is particular to its own reader — for the bar paragraph, that
>    this repo has no build, no tests, no formatter and no CI, and that the node's acceptance condition binds too; for
>    the review route, that no reviewing skill is named for this repo and that `CONTEXT.md`'s refused words return
>    false positives when used as a grep list.
> 3. ~~Nothing is deleted: every superseded enumeration remains in the file, marked struck, and the replacement is
>    added around it.~~
>
>    **Amended, and the amendment is the manager's, carrying a decision the human settled after this clause was
>    written. It is replaced rather than supplemented.** The superseded enumerations are **removed** from this file
>    and appended **verbatim** to `map-history.md` under the heading mirroring the section they came from,
>    struck-through text staying struck through; the file is left stating the current enumeration only. This is the
>    rule [node 189](189-where-the-never-delete-rule-stops.md) settled at the human's word — an enumeration of the
>    standards work is held against **is** a rule statement, and a superseded rule statement is replaced rather than
>    struck. Their words, `verbatim`: *"I don't think there should a be a never delete rule on the rules. They can
>    change."*
>
>    **Two strikes already standing in the bar paragraph are within this clause's reach**, node 158's on the ignore
>    file and node 169's on the standing preferences. Node 184's correction round was scoped away from them by the
>    manager and left them in place; under this amended clause they move.
> 4. No numbered rule in the file's two blocks — the five ground rules, and the four standing rules for writing — is
>    reworded, renumbered or reordered.
> 5. Every markdown link in the file resolves to a path that exists.
> 6. No file outside `.scratch/graph-workflow/` is modified.

## The manager's note at filing

*Not a change to anything above.*

**Its author is the node that ended the chain 144 → 169 → 184**, and it says so: its own condition fenced off no
paragraph, so it could touch both and did, and *"complying with my condition produced no fourth node of that kind"*.
**This node is therefore not a fifth link** — it is not a defect created by a narrow condition, but the duplication
that produced two of the three links in the first place.

**Five nodes now queue on `map-implementation-rules.md`** — this one, [node
186](186-an-implementation-worker-tests-its-worktree.md), [node
188](188-move-the-landing-section-out-of-the-workers-file.md), [node
149](149-state-the-prose-standards-demands-in-the-rules-file.md) and [node
160](160-carry-the-integration-conflict-rule-into-the-map.md). **Node 188 moves the section this one does not touch**,
so the two are disjoint in fact though not by any written edge. The manager holds that ordering.

## The manager's note, 2026-09-23

*The manager's own note, not an amendment.* This node's `## Acceptance condition` quotes the words "four standing rules for writing". Since [node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md), `map-implementation-rules.md` holds five standing rules for writing and says "five" where it said "four". Found by the manager's search of the open conditions for "four standing rules". The clause must be re-pointed before this node is claimed.

## Amendment, 2026-09-27 (from node 168)

*Written by [node 168](168-where-a-non-implementation-worker-gets-the-ground-rules.md)'s worker under its `CONDITIONS`, and filed by the manager. The heading it quotes, "**Five standing rules for writing anything in this effort**", is in the tree (node 289). The clause becomes binding once [node 348](348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md) moves the ground-rules block out of this file; this node is not to be claimed before 348 lands.*

- **Clause 4.** Read: "4. No numbered rule in the file's block of five standing rules for writing is reworded, renumbered or reordered."

## Amendment, 2026-09-27 (from node 348)

*Written by [node 348](348-keep-the-ground-rules-in-map-md-and-strike-the-sibling-file-allowance.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it.*

- **Clause 1.** Replacement for its clause 1 phrase "this effort's ground rules and its four standing rules for writing":
  "this effort's ground rules, stated as held in `map.md`'s `## Notes` and received by a checker as text in its spawn; this effort's five standing rules for writing, stated as held in this file"
  Its words are fixed by node 289 (resolved; "five", with the heading "Five standing rules for writing anything in this effort" in the tree) and by this node's work once landed ("held in `map.md`'s `## Notes`", "a checker receives as text in its spawn", now in `map-implementation-rules.md` and `map.md`). Without it, node 190's merge of the two lists could drop what clause 6 here put in.

## Amendment, 2026-09-27 (from node 349)

*Written by [node 349](349-whether-the-five-standing-rules-for-writing-reach-other-workers.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it. It replaces clause 1's phrase as amended by node 348, and clause 4 as amended by node 168.*

- Node 190 (open, unclaimed). Clause 1, as amended by node 348, contains the phrase "this effort's five standing rules for writing, stated as held in this file". Replacement: "this effort's five standing rules for writing, stated as held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn". Clause 4, as amended by node 168, reads "No numbered rule in the file's block of five standing rules for writing is reworded, renumbered or reordered". Replacement: "4. The file states neither the five ground rules nor the five standing rules for writing as a numbered list. Where it names them, it names `map.md`'s `## Notes` as holding them." Both replacements are fixed by this node, once resolved, and by the new implementation node above, once landed. Node 190 must not be claimed before that node lands.

## Amendment, 2026-09-27 (from node 56)

*Written by [node 56](56-ship-the-glossary-into-the-skill-set.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it.*

- Node 190 (open, unclaimed): clause 1 "`CONTEXT.md`'s `_Avoid_` lines" should read "`.claude/skills/expedition/glossary.md`'s `_Avoid_` lines". Clause 2 "that `CONTEXT.md`'s refused words return false positives" should read "that `.claude/skills/expedition/glossary.md`'s refused words return false positives". The path is fixed by this node's work in the tree, the human's 2026-09-25 choice of name.

## Amendment, 2026-09-28 (from node 354)

*Written by [node 354](354-add-the-sixth-standing-rule-for-writing.md)'s worker under its `CONDITIONS`, and filed by the manager. Pasted as it wrote it. It binds once node 354 lands.*

- Node 190 (open, unclaimed). Node 349's amendment of its clause 1 contains the phrase "this effort's five standing rules for writing, stated as held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn". Replacement: "this effort's six standing rules for writing, stated as held in `map.md`'s `## Notes` inside the ground-rules block and received by a checker as text in its spawn". Node 349's amendment of its clause 4 reads "4. The file states neither the five ground rules nor the five standing rules for writing as a numbered list. Where it names them, it names `map.md`'s `## Notes` as holding them." Replacement: "4. The file states neither the five ground rules nor the six standing rules for writing as a numbered list. Where it names them, it names `map.md`'s `## Notes` as holding them." In both, "six" is fixed by this node's work landed in the tree: `map.md`'s list ends at rule 6, and `map-implementation-rules.md` says "six standing rules for writing". There are still five ground rules in `map.md`. Node 190's original clauses 1 and 4, which say "four", were already replaced by earlier amendments.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      The rules file states one list of standards twice (node 190)

ANSWER:        `map-implementation-rules.md`'s `## What the work is held against` now states the standards once. The section opens with a lead-in in bold, **The standards an implementation node's work is held against.**, followed by one bulleted list: `/coding-principles` and `/naming`; `.claude/skills/expedition/glossary.md`'s `_Avoid_` lines; this effort's ground rules (held in `map.md`'s `## Notes`, received by a checker as text in its spawn); its six standing rules for writing (held in `map.md`'s `## Notes` inside the ground-rules block, received by a checker as text in its spawn); `graph-conventions.md`; and `/writing-for-agents`. The paragraph saying that `map.md`'s standing preferences are not among the standards (node 42's test) now follows the list, because it applies to both readers. It used to sit in the review route.
                The bar paragraph and the review route paragraph still begin with their bold lead-ins and both point at "the standards listed at the head of this section". The bar paragraph keeps: no build, no tests, no formatter, no CI; that the node's acceptance condition binds too; and the "complete bar rather than a deficient one" statement. The review route keeps: no reviewing skill is named; the `glossary.md` trap with false positives; the note on `where`; and the phrases "on the same ground as the bar's commands above" and "the human's standing direction below", so the file's *Nothing below was reworded* paragraph stays accurate.
                The ignore-file sentence (node 271's clauses) is now one sentence with no struck-through text: "`graph-agent` has **no build, no tests, no formatter and no CI** — no manifest, no task runner, nothing to invoke; the one ignore file, `.gitignore`, ignores `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/` and invokes nothing, so the bar's command half is empty, and under the *"if relevant"* clause that is a **complete** bar rather than a deficient one." I opened `.gitignore` at the worktree root. Its patterns are exactly `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/`, and the rest is comments. `.gitignore` was not edited.
                Decisions inside the work that a later reader would otherwise have to work out again:
                (a) The file's own *What this file admits* rule says whoever edits a passage applies the history test to it. Under that rule I left these accounts out of the rewritten paragraphs: "the second added at node 158"; "whose absence here node 297's worker reported"; "Corrected at node 114's check, having claimed no ignore file…"; "the same shape the dogfood target has, one step thinner"; "Two checker runs spent their largest single cost finding this…"; and the sentence on the two enumerations being one set.
                (b) Node 169's strike on the standing preferences, which clause 3 names, was no longer in the tree at 6259c2c1. The only strike left in the file was node 158's on the ignore file, and it moved.
                (c) Once that strike moved, the opening sentence "**The struck rule statements below predate this and are not licence to add another.**" in *How a rule in this file is superseded* became false. I removed it and banked it.
                (d) All three superseded texts were appended verbatim to `map-history.md` under a new heading at its end: "## Superseded from `map-implementation-rules.md` at node 190 — the standards stated twice, and the struck ignore-file wording". It has three `###` subsections and shows both old paragraphs whole. The file now contains no `~~`.
                Clause 4, as amended by node 354, held before the work started and still holds, as the manager anticipated. The file states neither list of rules as a numbered list, and where it names them it names `map.md`'s `## Notes` as holding them.
                Clause 5: every relative link in the rules file and in the new history entry resolves. I checked each one with a script.
                Clause 6: only the two files under `.scratch/graph-workflow/` were modified.

INDEX LINE:    The rules file's `## What the work is held against` now lists the standards once, under its own lead-in, and both paragraphs point at it. The struck ignore-file wording and the duplicate lists moved to `map-history.md`.

FLAGS:         ASSUMPTION: The condition's opening says "The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited". Clause 3 as amended, and node 271's clauses added from node 366, both require appending to `map-history.md`. I read the later amendments, which carry the human's decisions at nodes 189 and 366, as overriding that opening sentence, and I edited `map-history.md`. I did not raise this as a contradiction. Index: Node 190 edited `map-history.md` despite its condition's opening "no other file may be edited", reading the later amendments that require the move to `map-history.md` as overriding it.
                ASSUMPTION: Removing node 158's strike made the opening sentence "The struck rule statements below predate this and are not licence to add another." false, so I removed it and banked it verbatim in `map-history.md`. It sits outside the two paragraphs the condition names. Index: Node 190 removed the rules file's sentence about struck rule statements below, since none remained, and banked it in `map-history.md`.
                ASSUMPTION: Under the rules file's own *What this file admits* rule, the rewritten bar and review-route paragraphs leave out their accounts of how they were learned (node 158/297/114 corrections, the dogfood comparison, the checker-cost sentence). The full old text is banked verbatim. Index: Node 190 left the bar and review-route paragraphs' accounts of how they were learned out of the rewrite, under the file's own admission test, and banked the old paragraphs whole.

NEW NODES:     none

INVALIDATIONS: Node 184 (resolved). Its answer that "the two enumerations are one list" is extended: the list is now stated once, and the bar paragraph's own copy of it no longer exists. Node 271 (superseded into this node): its defect is fixed. Node 189: applied, not changed.

CONDITIONS:    Searched every node not resolved, superseded or out-of-scope (status open or claimed), in both `## Acceptance condition` and `## Question`, for: "struck rule statements", "two enumerations", "standards to hold work against", "non-command half", "ignores `.worktrees", "Two checker runs", "one step thinner", "review route", "bar paragraph", "bar's commands for this repo", "What the work is held against". The only open node that matched was 205 (open, unclaimed). Its clause 3 says the bar paragraph's "enumeration of that non-command half is unchanged", and that paragraph no longer holds an enumeration. Replacement for node 205's clause 3: "3. That paragraph keeps its statement that the bar here is entirely its non-command half and that this is a complete bar rather than a deficient one, and its pointer to the standards listed at the head of that section, together with the node's acceptance condition, is unchanged." Fixed by this node's work once it lands ("the standards listed at the head of this section" is in the tree). Node 205's clause 2 ("one ignore file, which invokes nothing") still holds. Its clause 4 (strike in place, never delete) still collides with node 189's rule, which the manager has already noted. No open node's question is changed.

MISSING FROM MAP: none. map.md does not say that the rules file's own opening rules (*What this file admits*, *How a rule in this file is superseded*) bind the worker who edits that file. I took them as binding because the file states the standards.

GATE PAYLOAD:  No checker findings yet.
                Paths touched (both in /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/190-standards-once):
                  .scratch/graph-workflow/map-implementation-rules.md
                  .scratch/graph-workflow/map-history.md (appended only, at the end; expect it to meet node 80's append at integration)
                The bar: the repo root holds `.claude`, `CONTEXT.md`, `CONTEXT-MAP.md`, `.gitignore` and `.scratch`. It has no manifest, task runner, tests, formatter or CI, so the recorded "no commands" matches the repo and the bar is its non-command half. Note that `CONTEXT-MAP.md` exists at the root and no record names it. It is not a build file.
                Proposed commit message:
                  State the implementation standards once in the rules file

                  The bar paragraph and the review route now point at one list
                  under its own lead-in. The ignore-file sentence names .gitignore's
                  three patterns without struck text, and the superseded paragraphs
                  move verbatim to map-history.md.

                  Node: graph-workflow/190

RETROSPECTIVE:
1. What I had to hunt for: the state of node 169's strike, which clause 3 names but which was already gone; whether open node conditions quote the paragraphs (only node 205 does); the history-entry format, which I copied from node 354's entry.
2. What arrived that this node did not need: most of the 1112-line map-history.md (only the tail format mattered), and the long worktree paragraph in map.md.
3. What would have made this easier: a consolidated, amended acceptance condition on the node. I had to fold six amendments, two of them nested replacements of earlier replacements, plus an opening sentence that the later amendments contradict.
4. What was stale, wrong or contradictory: the condition's "no other file may be edited" against amended clause 3 and node 271's clauses requiring `map-history.md`; clause 3's "two strikes already standing", of which only one still stood; the manager's 2026-09-23 note about "four" and "five", superseded by later amendments; and node 205's clause 3, which this work makes wrong (replacement given above).
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the condition and all six amendments reached it as a verbatim copy in `$TMPDIR/c190.md`.*

> PASS
>
> Node: 190, "The rules file states one list twice". Worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/190-standards-once, base 6259c2c1. The work is the uncommitted diff to .scratch/graph-workflow/map-implementation-rules.md and .scratch/graph-workflow/map-history.md. I read both changed paths as the work under check, under that file's rule on record files handed over as the work. I read nothing else in the effort's directory, except the standards in map-implementation-rules.md.
>
> Condition as amended. I applied 348 then 349 then 354 to clause 1, 349 then 354 to clause 4, 56 to the glossary paths, and replaced clause 3 by its own amendment. Node 366's three clauses are added. All searches ran over the unwrapped text.
>
> - Preamble scope. `git status --short --untracked-files=all` shows only the two paths. Editing map-history.md is required by clause 3 and node 366. Neither decisions.md nor flags.md nor any node file is touched.
> - Clause 1. `## What the work is held against` now opens with the bold lead-in "**The standards an implementation node's work is held against.**" followed by one 6-item bullet list. The list names `/coding-principles` and `/naming`; `.claude/skills/expedition/glossary.md`'s `_Avoid_` lines; the ground rules "which map.md holds in its ## Notes and which a checker receives as text in its spawn"; "six standing rules for writing, which map.md's ## Notes holds inside the ground-rules block and which a checker receives as text in its spawn"; graph-conventions.md; and /writing-for-agents. Established by a python regex over the unwrapped file for each standard's name. Every occurrence falls in that list, except the standing-preferences paragraph, which names the two blocks and is no list of standards. "Once" therefore holds.
> - Clause 2. The bar paragraph says "the standards listed at the head of this section". It keeps "no build, no tests, no formatter and no CI" and that the "node's acceptance condition ... binds too". The review route says "A checker holds the finished work against the standards listed at the head of this section". It keeps "No reviewing skill is named for this repo" and the `.claude/skills/expedition/glossary.md` false-positives trap. Established by reading the unwrapped lines from the same search.
> - Clause 3 (amended). Base lines 39 and 41, the two old paragraphs, appear verbatim in map-history.md (`grep -qxF` on each base line: yes, yes). The ~~ignores `.worktrees/`~~ strike is kept inside the moved text. The removed opening sentence "The struck rule statements below predate this..." is appended verbatim too (`grep -c -F`: 1). Each sits under a `### From ...` heading inside a new `## Superseded from map-implementation-rules.md at node 190` section, matching the pattern of the earlier history entries. `grep -n '~~'` on the new rules file: no hits. Node 158's strike moved. Base line 39 holds no node-169 strike, so nothing else was left to move.
> - Clause 4 (354's wording). `grep -nE '^\s*[0-9]+\.'` on the new file: no hits. Every mention of the ground rules or the standing rules for writing names map.md's `## Notes` (same mention search as clause 1).
> - Clause 5. A python check resolved every relative markdown link against the file's directory: map-implementation-rules.md, 35 links, 0 unresolved. Also map-history.md, 431 links, 0 unresolved.
> - Clause 6. Nothing outside .scratch/graph-workflow/ is modified (git status above).
> - Node 366, clause a. The ignore-file sentence now reads "ignores `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/`". That matches all three patterns in the worktree's .gitignore (cat .gitignore). It contains no `~~`. The replaced text is appended verbatim under a mirroring heading (the line-39 check).
> - Node 366, clause b. The same sentence keeps "no build, no tests, no formatter and no CI", "invokes nothing", and "the bar's command half is empty, and under the "if relevant" clause that is a **complete** bar rather than a deficient one".
> - Node 366, clause c. `git diff --name-only 6259c2c1 -- .gitignore` is empty.
> - Node 366, clause d ("Scope came from no search"). There is no recorded command to re-run.
>
> NOT COVERED:
> - From node 366: "which the worker verifies by opening `.gitignore` and quotes in its handover". The handover is outside what I was given. This PASS does not cover that part.
>
> The bar:
> - Commands: none to run. The worktree root holds only .claude, CONTEXT.md, CONTEXT-MAP.md, .gitignore and .scratch. There is no manifest, no task runner and no .github. The rules file states the repo has no build, no tests, no formatter and no CI. So there was nothing to build, warn, format or test. The command half is empty, and the bar is its standards half.
> - Standards: I read only the standards in map-implementation-rules.md. All six bore on this work: /coding-principles with /naming, the glossary's `_Avoid_` lines, the ground rules, the six standing rules for writing, graph-conventions.md and /writing-for-agents. The ground rules and the six standing rules I held as received in the spawn text.
> - The work moved the standard: I settled what moved first. The set of standards in the two old lists, plus the acceptance condition the bar added, is identical to the set in the new list plus the bar paragraph. Only the wording around them changed, so the check was unaffected.
> - No reviewing skill is named, so I ran none and held the work by hand.
> - Glossary check: I compared the new text by hand against the glossary's `_Avoid_` lines. "CI", "complete" and "review route" occur, but in senses the condition itself demands or the file already uses. No line numbers are cited (writing rule 4). The list cites the nodes that shaped it (writing rule 2).
>
> QUESTIONS:
> - Standing rule for writing 5 says "Bold a term only where it is defined." The new bar paragraph keeps the bolded term "**node's acceptance condition**" from the replaced text. The paragraph split out of the review route keeps "**ground rules**" and "**six standing rules for writing**", both unchanged from the base. The work also adds the new bolded sentence "**A checker holds the finished work against the standards listed at the head of this section**", which is a sentence rather than a term. I did not treat any of these as a breach. Every bolded term is carried verbatim from the base, and the condition itself asks for a bold lead-in, which shows the file's own bold-lead-sentence convention. Does rule 5 bind bold that is carried verbatim into a rewritten paragraph, or bold used on a whole sentence for emphasis? This is about the bar paragraph and the review route in map-implementation-rules.md. To list the candidates: `git -C <worktree> diff -U0 -- .scratch/graph-workflow/map-implementation-rules.md | grep '^+[^+]' | grep -oE '\*\*[^*]+\*\*'`. It returns 13 spans: the 12 base spans that remain after the move plus the new review-route sentence.
>
> I wrote nothing in the repo. The temporary directories I used are removed.

*The manager's note:* the NOT COVERED item is established from the worker's handover, which quotes `.gitignore`'s patterns ("Its patterns are exactly `.worktrees/`, `.claude/worktrees/` and `.scratch/graph-workflow/worktrees/`"). The checker handed back a question beside its outcome, so the standing yes does not cover this gate; it goes to the human.

### Gate — approve, 2026-10-02

The manager put the gate to the human with checker run 1's question on writing rule 5 and flags 190.1 to 190.8, recommending approval as is: rule 5 binds what a work writes, the carried bold is earlier text, and the new bold sentence follows the file's bold lead-sentence convention that clause 1 asks for. The alternative offered was one correction round removing the bold from the one new sentence. The human, `verbatim`: *"ok"*. The manager had said "ok for recommended" would mean approval as is. Flags 190.1 to 190.8 settle at this gate.

## Flags

`190.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 168's replacement for clause 4 was filed on this open, unclaimed node, and the node was made to wait on node 348.

`190.2` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 348 above.* Node 348's replacement for clause 1 was filed on this open, unclaimed node without asking the human first.

*The manager's note, 2026-09-27:* edge to [node 349](349-whether-the-five-standing-rules-for-writing-reach-other-workers.md) added. Node 349's worker found that clause 4, and node 348's amendment to clause 1, both assume the five standing rules for writing stay in the rules file. Node 349's question is whether they move, so this node waits on it.

`190.3` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 349 above.* Node 349's replacements for clauses 1 and 4 were filed on this open, unclaimed node without asking the human first, and the node was made to wait on [node 352](352-move-the-five-standing-rules-for-writing-into-the-ground-rules-block.md).

`190.4` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 56 above.* Node 56's replacement naming `.claude/skills/expedition/glossary.md` in place of `CONTEXT.md` was filed on this open, unclaimed node without asking the human first.

*The manager's note, 2026-09-27:* edge to [node 354](354-add-the-sixth-standing-rule-for-writing.md) added. [Node 253](253-a-shipped-file-points-at-a-sibling-rather-than-restating-it.md)'s worker reports that once node 354 lands, the "five standing rules for writing" in clause 1 (as amended by node 348) and clause 4 becomes wrong, and that the replacement is owed then, since "six" is fixed by no landed work yet.

`190.5` `ASSUMPTION` — *The manager's own entry, carrying the amendment from node 354 above.* Node 354's replacement of "five" (or "four") with "six" standing rules for writing was filed on this open, unclaimed node without asking the human first.

`190.6` `ASSUMPTION` — *The worker's own text.* The condition's opening says "The work is `.scratch/graph-workflow/map-implementation-rules.md`, and no other file may be edited". Clause 3 as amended, and node 271's clauses added from node 366, both require appending to `map-history.md`. I read the later amendments, which carry the human's decisions at nodes 189 and 366, as overriding that opening sentence, and I edited `map-history.md`. I did not raise this as a contradiction.

`190.7` `ASSUMPTION` — *The worker's own text.* Removing node 158's strike made the opening sentence "The struck rule statements below predate this and are not licence to add another." false, so I removed it and banked it verbatim in `map-history.md`. It sits outside the two paragraphs the condition names.

`190.8` `ASSUMPTION` — *The worker's own text.* Under the rules file's own *What this file admits* rule, the rewritten bar and review-route paragraphs leave out their accounts of how they were learned (node 158/297/114 corrections, the dogfood comparison, the checker-cost sentence). The full old text is banked verbatim.

## Amendment, 2026-09-29 (from node 366)

*Written by [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s worker and filed by the manager, under the human's answer to node 366's Q3 (`verbatim`: *"ok"*). The worker's own text, pasted:*

Block 2 (defect joined to open node 190, from node 271). Clauses to add to 190's acceptance condition:
  - In `.scratch/graph-workflow/map-implementation-rules.md`, the sentence of the bar paragraph that states which patterns the repository's ignore file ignores is replaced by its current form, with no struck-through text in it. It names every pattern that `.gitignore` at the repository root then holds, which the worker verifies by opening `.gitignore` and quotes in its handover. The text it replaces is appended verbatim to `.scratch/graph-workflow/map-history.md` under a heading mirroring the section it came from, with struck-through text staying struck through.
  - The same sentence still says that this repo has no build, no tests, no formatter and no CI, that `.gitignore` invokes nothing, and that the bar's command half being empty is a complete bar rather than a deficient one.
  - `.gitignore` is not edited.
  - Scope came from no search: the sentence named is the place of the work.
