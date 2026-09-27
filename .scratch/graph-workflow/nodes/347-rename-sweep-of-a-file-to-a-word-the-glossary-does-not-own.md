# Rename "sweep of a file" to a word the glossary does not own

Type: implementation
Status: resolved
Blocked by: none

## Question

The glossary's **Sweep** is the whole-graph pass that looks for revisions nobody propagated, and `SKILL.md` says "A sweep runs only on an empty frontier." `graph-conventions.md`'s reader test and `map-implementation-rules.md` also use "sweep" for a pass over one map file under the admission test, so a reader holding the glossary term can read the second use as bound by the first.

*Reported by [node 346](346-allow-a-sweep-of-a-map-file-in-graph-conventions-md.md)'s checker, beside its `PASS`, and minted by the manager on the human's "ok" to the manager's recommendation at that gate.*

## Acceptance condition

*Written by the manager, which minted this node. Every word is fixed by node 346's landed text (`477d350`), the glossary's **Sweep** entry in `CONTEXT.md`, and the checker's recorded search.*

The work edits `.claude/skills/expedition/graph-conventions.md` and `.scratch/graph-workflow/map-implementation-rules.md`, and appends to `.scratch/graph-workflow/map-history.md` where the latter's superseded text must be kept. No other file changes. The scope came from this search, run at `477d350` over the working tree: `grep -rniE 'sweep of (a|the) file' .claude/ CONTEXT.md .scratch/graph-workflow/map-implementation-rules.md`, which returned one line in `graph-conventions.md` ("No sweep of a file is owed under the test, and one is allowed.") and one in `map-implementation-rules.md` ("No sweep of the file is owed, and one is allowed."). An instance the search reaches outside those two files is reported and not edited.

1. In both files, the sentence names a pass over a map file under the admission test by a word other than "sweep", and it still says such a pass is not owed and is allowed.
2. After the work, the search above returns nothing.
3. The glossary's **Sweep** entry and every other use of "sweep" meaning the whole-graph pass are unchanged.
4. The superseded sentence of `map-implementation-rules.md` appears verbatim in `map-history.md` under a heading mirroring the section it came from, and `map-history.md` gains text and loses none.
5. The working tree meets the bar.

## Answer

The pass over one map file under the admission test is now called a pass over the whole file, in graph-conventions.md and map-implementation-rules.md, leaving "sweep" to the glossary's whole-graph pass.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `4b538be`. Flags 347.1 settle at the node closing report.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Rename "sweep of a file" to a word the glossary does not own

ANSWER:        The pass over one map file under the admission test is now called "a pass over a whole file" in `graph-conventions.md` and "a pass over the whole file" in `map-implementation-rules.md`. "Sweep" stays only in its glossary sense, the whole-graph pass that looks for revisions nobody propagated.
               - `.claude/skills/expedition/graph-conventions.md`, `## Writing the map`, reader-test paragraph: "No sweep of a file is owed under the test, and one is allowed." now reads "No pass over a whole file is owed under the test, and one is allowed." The paragraph was re-wrapped at the file's 105-column width. Nothing else in the file changed. The whole-graph use at line 109 ("because the sweep and the effort closing report are built from it") is untouched.
               - `.scratch/graph-workflow/map-implementation-rules.md`, the opening *What this file admits* paragraph: "No sweep of the file is owed, and one is allowed." now reads "No pass over the whole file is owed, and one is allowed." The citation clause right after it, "and the sweep allowed at [node 346]", now reads "and the pass over the whole file allowed at [node 346]". It names the same pass, and leaving it would have kept the double use in the same passage (see the flag). The link target `nodes/346-allow-a-sweep-of-a-map-file-in-graph-conventions-md.md` is a filename and was not changed.
               - `.scratch/graph-workflow/map-history.md`: one section was appended at the end, "Superseded from `map-implementation-rules.md` at node 347 — the sentence that named a pass over the file a sweep", with a subheading "From the file's opening, *What this file admits* — the sentence on who applies the test". Under it the superseded lines are copied verbatim, with their original line breaks. It follows node 346's history entry in form.
               - Why "pass": `CONTEXT.md` defines no term "pass". Its Cascade and Sweep entries use "pass" only as the general word ("A pass that ..."), and no `_Avoid_` line refuses it.
               - Checks: `map-history.md` before the change is a byte-exact prefix of after, and the one removed hunk of the rules file (old lines 12-14) appears byte-identically in the appended text. That is check 11, done by script. Checks 4 and 10 do not apply: no labels were touched and the rules file has no `## Notes`.
               - The condition's search, run with `.claude/` and `CONTEXT.md` taken from the worktree and the rules file from the main checkout, returns nothing (exit 1). Run in the main tree it still hits `.claude/.../graph-conventions.md:122` until this worktree lands.

INDEX LINE:    The pass over one map file under the admission test is now called a pass over the whole file, in graph-conventions.md and map-implementation-rules.md, leaving "sweep" to the glossary's whole-graph pass.

FLAGS:         ASSUMPTION: The word chosen is "pass" ("a pass over a whole file" / "a pass over the whole file"). The glossary defines no term by that word and refuses it nowhere, and its Cascade and Sweep entries use it only as the general word. I also rewrote the next clause in `map-implementation-rules.md`, "and the sweep allowed at [node 346]", to "and the pass over the whole file allowed at [node 346]". The condition's search does not reach that clause. But it names the same pass in the same passage, and clause 3 protects only whole-graph uses of "sweep". The superseded text of both sentences is in `map-history.md`.
               Index: Node 347 chose "pass over the whole file" for the pass over one map file, and also renamed the adjacent "the sweep allowed at node 346" citation clause, which the search did not reach.

NEW NODES:     none — The addition to node 230's condition below goes under CONDITIONS, as the replacement for a clause of an unclaimed node's condition.

INVALIDATIONS: Node 346 (resolved): a rename. Its landed wording "No sweep of a file is owed under the test, and one is allowed." in `graph-conventions.md`, and its answer's "sweep of the file" in `map-implementation-rules.md`, now say "pass over a whole file" / "pass over the whole file". The rule is unchanged: such a pass is not owed and is allowed. Node 191 (resolved): its "no sweep of the file is owed" wording, already superseded at 346, now uses "pass" as well. The rule is unchanged.

CONDITIONS:    I searched every open or claimed node's `## Acceptance condition` for `sweep of`, `no sweep`, `sweep allowed`, `sweep is owed` and `one is allowed`. There were two matches: node 347 itself, and node 230 (open, unclaimed), clause 3. That clause ends "...does not state who applies the test or that no sweep is owed. A paragraph containing any of those is a restatement and fails this clause." Replacement for that last sentence pair: "...does not state who applies the test, that no pass over a whole file is owed, or that one is allowed. A paragraph containing any of those is a restatement and fails this clause." Its words are fixed by the shipped `graph-conventions.md` `## Writing the map` text as this node leaves it ("No pass over a whole file is owed under the test, and one is allowed."), with "one is allowed" from node 346's landed text (`477d350`).

MISSING FROM MAP: none

GATE PAYLOAD:  No checker findings yet.
               Paths touched:
               (1) worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/347-rename`, branch `worktree-347-rename`: `.claude/skills/expedition/graph-conventions.md`, uncommitted.
               (2) main checkout `/home/mathieu/projects/graph-agent`: `.scratch/graph-workflow/map-implementation-rules.md` (3 lines of the opening paragraph) and `.scratch/graph-workflow/map-history.md` (appended section at the end only). Both files also carry earlier uncommitted work from the map pass and node 346, which is not mine.
               Bar: the repo has no manifest, build, tests, formatter or CI. The worktree root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. That matches the rules file's record, so the bar is its non-command half. The wrap widths were kept: 105 in `graph-conventions.md`, about 115 in the rules and history files.
               Proposed commit message:
               Rename "sweep of a file" to a pass over the whole file

               The glossary's Sweep is the whole-graph pass, so the admission test's
               pass over one map file now says "pass" in graph-conventions.md and
               map-implementation-rules.md; the superseded sentence is kept in
               map-history.md.

               Node: graph-workflow/347

RETROSPECTIVE:
1. What I had to hunt for: the byte-exact demand of check 11 (at the end of `## Mechanical checks`, not in `### Change the map`). Node 346's `map-history.md` entry, to copy its heading form. The rules file's real line numbers: an earlier combined dump had shifted them.
2. What arrived that this node did not need: most of `map.md`, including all standing preferences except never-delete. Most of the implementation contract (the raise format, the rules for reporting a new implementation node). Most of the rules file's review-route paragraphs.
3. What would have made this easier: the spawn or condition could have said whether the adjacent clause "the sweep allowed at [node 346]", in the same paragraph but outside the search, should be renamed too. I had to decide that and flag it. It would also have helped to point at node 346's history entry as the model for the heading.
4. What was stale, wrong or contradictory: nothing contradictory. The condition's search is phrased for one tree. Run in the main tree it keeps hitting `.claude/` until the worktree lands, because the shipped file and the record live in different trees for this node. The checker should run it with `.claude/` from the worktree.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 44's check; the condition reached it as a verbatim copy in `$TMPDIR/c347.md`.*

> PASS
>
> This is the check of node 347, "Rename "sweep of a file" to a word the glossary does not own". The work is in two places:
> - `.claude/skills/expedition/graph-conventions.md`, uncommitted in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/347-rename`, on base 477d350;
> - in the main checkout, the opening paragraph of `.scratch/graph-workflow/map-implementation-rules.md`, and in `map-history.md` only the block headed "Superseded from `map-implementation-rules.md` at node 347".
>
> I read the whole condition in `/tmp/claude-1000/c347.md`. Following the rules file, I read the changed parts of the two record files as the work.
>
> **Settled first: the work moved a standard.** `map-implementation-rules.md` is the file I read my standards from, and this work rewords one of its sentences. What that sentence requires and refuses has not moved: no pass is owed, and one is allowed. Only the name "sweep" changed, to "pass over the whole file". The standard therefore stands, and I held the work against it as before.
>
> **Parts of the condition**
>
> - **Scope ("No other file changes").** Met. `git status --short --untracked-files=all` in the worktree shows only `graph-conventions.md`. In the main checkout, the hunk in the rules file's opening paragraph and the node-347 block in `map-history.md` are this work. The other uncommitted record changes there belong to node 346 and a map pass, as the spawn says.
> - **Clause 1.** Met in both files. Both still say no such pass is owed and one is allowed.
>   - `graph-conventions.md` now reads "No pass over a whole file is owed under the test, and one is allowed." `git diff --word-diff` shows `[-sweep of-]{+pass over+} a {+whole+} file`, and everything else in the hunk is rewrapping.
>   - `map-implementation-rules.md` now reads "No pass over the whole file is owed, and one is allowed." Its citation of node 346 now reads "the pass over the whole file allowed at [node 346](…)".
>   - The glossary has entries for **Cascade** and **Sweep** but none for **Pass**, so the new word is not one it owns.
> - **Clause 2.** Met. I ran the recorded search as the spawn describes, over the same trees the worker used: `grep -rniE 'sweep of (a|the) file'` over `.claude/` and `CONTEXT.md` in the worktree, and over `.scratch/graph-workflow/map-implementation-rules.md` in the main checkout. It returns nothing. The condition records one line in each of the two files at 477d350, and those are the two lines this work changed.
> - **Clause 3.** Met. `CONTEXT.md` is unchanged, including its **Sweep** entry. The worktree diff touches only the one sentence in `graph-conventions.md`, so its other uses of "sweep" (such as "the sweep and the effort closing report are built from it") are unchanged. The rules file's hunk touches only this sentence.
> - **Clause 4.** Met.
>   - The superseded sentence appears verbatim, line breaks included, under `### From the file's opening, *What this file admits* — the sentence on who applies the test`. It reads "**Whoever is already editing a passage applies this to that passage**. No sweep of the file is owed, and one is allowed. Settled at [node 191](…), and the sweep allowed at [node 346](…)."
>   - That is exactly the sentence I read in the rules file when I checked node 346. It is uncommitted, so there is no commit to compare against.
>   - `git diff -- map-history.md | grep -c '^-[^-]'` returns 0, so `map-history.md` gains text and loses none.
> - **Clause 5.** Met. See the bar below.
>
> **The bar**
>
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check` is clean in the worktree. It is also clean on the two record files in the main checkout (exit 0).
> - The rewrapped lines keep each file's width.
>
> **Standards.** As in my earlier checks, I read only the standards in `map-implementation-rules.md`.
>
> - These bore on the work:
>   - `graph-conventions.md` `### Change the map`. The superseded text was appended verbatim under a mirroring heading, and the new statement keeps its markdown citations.
>   - `CONTEXT.md` `_Avoid_` lines. "pass" is not refused, and the change removes the clash with the glossary's **Sweep**.
>   - The writing rules.
>   - `/writing-for-agents`.
>   - The ground rules.
> - `/coding-principles` and `/naming` did not bear on the work.
> - No reviewing skill is named, so I ran none.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The main checkout's record carries other uncommitted changes that I cannot attribute. The two files handed to me as the work contain no such write.

### Gate — approve, `standing yes`, 2026-09-27

Taken under the standing yes recorded in `map.md`'s `## Notes` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its one NOT COVERED item is the worker's bookkeeping. This settles none of the node's flags; they settle at the node closing report.

## Flags

`347.1` `ASSUMPTION` **· settled** — The word chosen is "pass" ("a pass over a whole file" / "a pass over the whole file"). The glossary defines no term by that word and refuses it nowhere, and its Cascade and Sweep entries use it only as the general word. I also rewrote the next clause in `map-implementation-rules.md`, "and the sweep allowed at [node 346]", to "and the pass over the whole file allowed at [node 346]". The condition's search does not reach that clause. But it names the same pass in the same passage, and clause 3 protects only whole-graph uses of "sweep". The superseded text of both sentences is in `map-history.md`. — Node 347 chose "pass over the whole file" for the pass over one map file, and also renamed the adjacent "the sweep allowed at node 346" citation clause, which the search did not reach.

*The manager's note, 2026-09-27:* flags 347.1 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
