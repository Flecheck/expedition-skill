# File a retrospective where the worker put it, and fold the bullet's duplicated sentences

Type: implementation
Status: resolved
Blocked by: none

## Question

A worker reading the map's retrospective bullet learns where the manager files its retrospective and how to find existing item names, each stated once. The bullet in `map-manager-only.md` says a retrospective "is written under the heading `## Retrospective` and under no other heading". Since node 340, the manager has left most retrospectives inside the pasted handover or question payload, because copying one out under its own heading re-files a worker's text. About 132 node files hold a retrospective inside a paste, and about 66 have a `## Retrospective` heading (counted 2026-10-05, for scale only). Derivations.md entry (j) reads both. Node 387's checker also found two pairs of sentences in the same bullet that say the same thing twice. Node 387's condition froze them, and the human agreed to fold them later.

*Minted by the manager from the manager's own question to the human, 2026-10-05. The question ended: "Please answer: \"ok for recommended\" mints that node, or say you'd rather keep the rule." The recommendation was: "change the rule to match the practice. A retrospective stays where the worker put it, at the end of the pasted handover or question payload. I'd mint one small implementation node on `map-manager-only.md` that rewrites that sentence and folds node 387's two duplicated pairs."*

*The human's answer, `verbatim`, 2026-10-05:* *"ok"*

## Acceptance condition

*Written by the manager, who minted the node.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The bullet in question is the one line of `map-manager-only.md` beginning `- **Every worker returns a retrospective as the last handover part, on this effort only**`. In what follows, "the bullet" means that line.
>
> Scope: the named places are the work, not instances of a defect, so the scope came from no search.
>
> Done means every one of the following is true of the finished tree.
>
> 1. These two sentences of the bullet are removed: "It states how many earlier retrospectives carry that name, and lists their node ids." and "It finds the existing names by searching the retrospective sections of the files under `.scratch/graph-workflow/nodes/`, whatever heading each section was filed under, and not from memory or from any list held elsewhere."
> 2. The sentence "The worker obtains the existing names, with their counts and node files, by running the entry headed `## (j) Item names carried by the retrospectives` in [derivations.md](derivations.md)." becomes exactly: "The worker obtains the existing names, with their counts and node files, by running the entry headed `## (j) Item names carried by the retrospectives` in [derivations.md](derivations.md), and not from memory or from any list held elsewhere."
> 3. These five consecutive sentences of the bullet are removed: "The manager writes it into the node file in the same edit that writes that node's answer, its flags and its line in `decisions.md`.", "It is written last in the file, so the mandatory section order is untouched.", "It is written under the heading `## Retrospective` and under no other heading.", "It is not an annotation, since `graph-conventions.md` defines an annotation as what a later piece of work changed about a node's answer." and the sentence beginning "It is a section the shipped node-file format does not list". In their place there are exactly these sentences: "The manager files it where the worker put it, as the last part of the handover or question payload that the manager pastes onto the node. It stays inside that paste rather than being copied out under a heading of its own. A retrospective filed under a `## Retrospective` heading before 2026-10-05 stays where it is. This filing was settled at [node 391](nodes/391-file-a-retrospective-where-the-worker-put-it.md)."
> 4. No other sentence of the bullet changes, and no other line of `map-manager-only.md` changes.
> 5. The text removed by clauses 1 to 3 is appended verbatim to `.scratch/graph-workflow/map-history.md` under a heading that names `map-manager-only.md`'s retrospective bullet and node 391, in the form of that file's most recent entries. `map-history.md` gains text and loses none.
> 6. Nothing is written in `decisions.md` or `flags.md`, and no node's status line is touched.
> 7. The tree meets the bar.

## Answer

map-manager-only.md's retrospective bullet now files a retrospective inside the pasted handover or question payload, not under `## Retrospective`, and states once how a worker finds existing names.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `4d84523aa`. Flags 391.1, 391.2 settle at the node closing report.

## Handover, attempt 1

*Pasted as the worker handed it back, 2026-10-05.*

`````
HANDOVER:      File a retrospective where the worker put it, and fold the bullet's duplicated sentences

ANSWER:        In `.scratch/graph-workflow/map-manager-only.md`, the retrospective bullet (the line beginning `- **Every worker returns a retrospective as the last handover part, on this effort only**`) now says that the manager files a retrospective where the worker put it. That place is the last part of the handover or question payload the manager pastes onto the node, and the retrospective is not copied out under a heading of its own. A retrospective filed under `## Retrospective` before 2026-10-05 stays where it is. These four sentences replace the five sentences that had the manager write a `## Retrospective` section last in the node file, in the resolving edit, as a section not listed in the node-file format and not an annotation. The bullet also no longer says the same thing twice about how a worker finds existing names. The two older sentences ("It states how many earlier retrospectives carry that name…" and "It finds the existing names by searching the retrospective sections…") are removed. Their one clause the newer text lacked, "and not from memory or from any list held elsewhere", is added to the end of the sentence that points at derivations.md entry (j). No other sentence or line of the file changed; the line-level diff is 1 line changed. Under the `Change the map` procedure, the removed and replaced text is appended verbatim to `.scratch/graph-workflow/map-history.md`, following the form of the node 219/284/135 entries. The new entry is a `## Superseded from `map-manager-only.md` at node 391 — …` heading, then an italic account, then three `###` subsections, each with a `*Replaced/Removed, and it/they stood as:*` line. The subsections hold the two removed duplicate sentences, the entry-(j) sentence as it stood before the clause was added, and the five filing sentences. map-history.md gains 22 lines and loses none.

INDEX LINE:    map-manager-only.md's retrospective bullet now files a retrospective inside the pasted handover or question payload, not under `## Retrospective`, and states once how a worker finds existing names.

FLAGS:         ASSUMPTION: Clause 5 asks for "the text removed by clauses 1 to 3". Clause 2 removes no whole sentence; it extends one. I still appended that sentence's prior form to map-history.md, as its own `###` subsection, because the `Change the map` procedure sends every replaced rule text there. Nothing in clause 5 forbids the extra text, since map-history.md only gains. Index: Node 391 appended to map-history.md the pre-change form of the entry-(j) sentence that clause 2 extended, as well as the sentences clauses 1 and 3 removed.
               ASSUMPTION: Clause 4 freezes two sentences that the new filing sentences have now partly outdated, and I left both untouched. The first is "The name, the ranking and the filing in the resolving edit were settled at [node 212](…)", which still names "the filing in the resolving edit", although the sentence stating that filing is gone. The second is "The superseded wording is in [map-history.md](map-history.md).", which now directly follows "This filing was settled at node 391." That placement happens to read correctly, since 391's superseded wording is in map-history.md. Whether the manager still pastes the handover in the resolving edit is not stated anywhere now. A later small fold could reword the node-212 sentence. Index: Node 391 left the bullet's sentence citing node 212 for "the filing in the resolving edit" unchanged under clause 4, though the filing sentence it refers to was replaced.

NEW NODES:     none

INVALIDATIONS: - Node 212 (narrowing): its answer had the manager write the retrospective in the edit that resolves the node, under `## Retrospective` only. The heading part is superseded. The retrospective now stays inside the pasted handover or question payload. Whether that paste happens in the resolving edit is no longer stated by the bullet.
               - Node 219 (contradiction of its filing sentence): the sentences it wrote ("written last in the file", "under the heading `## Retrospective` and under no other heading", "in the same edit…") are replaced. Its naming sentence on searching retrospective sections "whatever heading" is removed as a duplicate. Entry (j), which reads both sections and pasted `RETROSPECTIVE` parts, now carries that job alone.
               - Node 340 (narrowing): the human's "ok for A" (2026-09-27) allowed `## Retrospective` as a section the node-file format does not list. That allowance is no longer stated in the bullet. It survives only for retrospectives filed under that heading before 2026-10-05.
               - Node 387 (extension): its checker's question on the two duplicated pairs is answered by this fold.

CONDITIONS:    I searched every node file for: "under no other heading", "`## Retrospective`", "searching the retrospective sections", "in the same edit that writes", and "written last in the file". The search covered the `## Acceptance condition` and `## Question` sections of the 12 open or claimed nodes (counted 2026-10-05, for scale only), and the resolved nodes' answers and conditions. No open or claimed node other than 391 matched. Resolved matches: 212, 219, 220, 221, 340, 387, and incidental mentions in 58, 71, 91, 94, 136 and 284. Node 221's condition requires ten files to carry `## Retrospective`. That stays true, because pre-2026-10-05 filings stay where they are. I wrote no replacement clauses, and no open node's question changes.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched (worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/391-retro-filing):
               - .scratch/graph-workflow/map-manager-only.md
               - .scratch/graph-workflow/map-history.md
               Bar: the repo root holds only .claude, CONTEXT-MAP.md, CONTEXT.md, .gitignore and .scratch, with no manifest and no CLAUDE.md/AGENTS.md. It states no build, test or format commands, so the record in map-implementation-rules.md (empty command half) stands unconfirmed as written, and the bar is its non-command half. No method skill was invoked, so none was skipped. Edits were made by an exact-match Python replacement, which asserted each target occurred exactly once in the bullet.
               Manager's-notes check: `grep -l '^RETROSPECTIVE'` over nodes/ returned 133, not about 132, and `grep -l '^## Retrospective'` returned 66 (both 2026-10-05, for scale only). The latest map-history.md entries are indeed from nodes 284 and 135, and I followed their form.
               Proposed commit message:
               ```
               File a retrospective where the worker put it, and fold the retrospective bullet's duplicated sentences

               map-manager-only.md's retrospective bullet now has the manager leave a
               retrospective inside the pasted handover or question payload instead of
               copying it out under `## Retrospective`, and states once how a worker
               finds existing item names. The replaced text is appended verbatim to
               map-history.md.

               Node: graph-workflow/391
               ```

RETROSPECTIVE
1. What I had to hunt for:
   - `history-entry-shape-by-example` — 2 earlier retrospectives carry it: 135, 284. map-history.md's entry form exists only as examples, so I read lines 1140–1251 to copy the shape. The spawn pointed me at it, so it cost little.
   - The extraction of entry (j)'s script: derivations.md does not say the block's relative glob must run from `.scratch/graph-workflow/`. My first run from the repo root failed with "cannot open file nodes/[0-9]*-*.md". New name: `derivation-run-directory-unstated` — 0 earlier retrospectives carry it.
2. What arrived that the node did not need:
   - `map-read-whole-for-a-few-items` — 11 earlier retrospectives carry it: 135, 178, 205, 220, 284, 382, 386, 387, 388, 389, 390. None of map.md's standing preferences bore on this edit except the never-delete/Change-the-map item and rule 5 (plain English).
   - `rules-file-read-whole-for-one-section` — 8 earlier retrospectives carry it: 178, 220, 382, 386, 387, 388, 390 (8 retrospectives over 7 files). Only the bar paragraph and the record-work paragraph bore on the work.
   - The contract's long `NEW NODES` and condition-writing guidance did not apply to a node whose condition already fixes every word.
3. What would have made it easier: the condition was exact and quoted every sentence, which made the edit mechanical. A one-line note in the condition on whether clause 2's old sentence counts as "removed text" would have spared the first ASSUMPTION.
4. Stale, wrong, or contradictory:
   - `stale-number-in-the-record` — 8 earlier retrospectives carry it: 178, 212, 220, 382, 385, 386, 388 (8 retrospectives over 7 files). The manager's "about 132" is now 133. It was correctly marked for scale only.
   - The frozen sentence citing node 212 for "the filing in the resolving edit" now refers to a sentence that no longer exists (see the FLAGS entry).
`````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-05. A fresh checker; the condition and the node's two flags reached it as text in `$TMPDIR/check391.md`.*

> PASS
>
> I treated the changed paths I was given as the work, as `map-implementation-rules.md` requires. Both are record files. I took no statement of intent from them. In `.scratch/graph-workflow/map-implementation-rules.md` I read only the standards, and I opened no other file in the effort's directory.
>
> Method: I extracted HEAD versions of both files with `git show HEAD:<path>` into a temporary directory. A Python script then compared each file as unwrapped lines with the worktree copy. It found the bullet as the single line starting with `- **Every worker returns a retrospective as the last handover part, on this effort only**`. Each of the old and new files has exactly one such line.
>
> - Clause 1: both sentences each occur once in the old bullet. The script removes them with `str.replace`. They are absent from the new bullet, as the exact-equality check below shows.
> - Clause 2: the old entry-(j) sentence occurs once in the old bullet. The script replaces it with the clause's exact extended sentence, and the new bullet equals the expected text.
> - Clause 3: the script took the span from "The manager writes it into the node file" up to " The superseded wording is in [map-history.md](map-history.md). The name, the ranking". That span is exactly the five named sentences, the last being the one beginning "It is a section the shipped node-file format does not list". It replaced that span with the clause's four sentences, verbatim.
> - Clause 4: applying clauses 1 to 3 to the old bullet gives a string exactly equal to the new bullet, which returned True. All lines of `map-manager-only.md` other than the bullet are identical: old and new are both 272 lines, and the prefix and suffix lists are equal.
> - Clause 5: the HEAD version of `map-history.md` is an exact prefix of the new file, which returned True, so the file loses no text. Every removed or replaced text from clauses 1 to 3 appears verbatim in the appended text. That includes the pre-change entry-(j) sentence and all five filing sentences.
>   - The new heading is "## Superseded from `map-manager-only.md` at node 391 — the retrospective bullet's filing sentences and its two duplicated sentences on existing names". It names the file, the retrospective bullet and node 391.
>   - The entry follows the form of the latest entries, matched against the node 219, 276, 381 and 135 entries:
>     - an italic "*Replaced under the `Change the map` procedure at [...]*" paragraph ending "The rest of the bullet is unchanged and is not reproduced here.";
>     - "### From `map-manager-only.md`'s `## Notes` — ..." subheadings;
>     - each subheading followed by "*Replaced/Removed, and it stood as:*" and the verbatim text.
> - Clause 6: `git status --porcelain --untracked-files=all` in the worktree lists only the two work files. So `decisions.md`, `flags.md` and every node file, status lines included, are untouched.
> - Clause 7: see the bar below.
>
> Bar:
> - The repo root has no `CLAUDE.md`, no `AGENTS.md` and no manifest. It holds only `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`. The rules file's own record agrees: no build, no tests, no formatter. So I ran no commands, and the bar is its non-command half alone.
> - Standards read:
>   - `/coding-principles` and `/naming`
>   - the glossary's `_Avoid_` lines
>   - the ground rules
>   - the six standing rules for writing
>   - `graph-conventions.md`
>   - `/writing-for-agents`
> - The ones that bore on this work were the `_Avoid_` lines and the writing rules. They apply to the new prose: the dictated replacement sentences and the worker's italic summary paragraph in `map-history.md`. I checked the `_Avoid_` words by hand, following the rules file's warning that grepping for them gives false positives.
> - I found no breach. "handover or question payload" uses "payload", which the glossary refuses for a handover. The phrase is the condition's own dictated wording, and read as "a handover, or a question payload" it uses the glossary's sense of a payload carrying questions. So it is not a finding.
> - The map-history entry is a record of what happened, which is what that file is for.
> - I ran no reviewing skill, because the standards name none.
> - `.gitignore` excludes the worktree, so I checked the diff with git inside the worktree.
>
> Flags:
> - 391.1: true. The pre-change entry-(j) sentence is present verbatim in the appended `map-history.md` text, alongside the sentences clauses 1 and 3 removed.
> - 391.2: true. The sentence "The name, the ranking and the filing in the resolving edit were settled at [node 212](...)" is unchanged in the new bullet, which the exact-equality check established.
>
> No questions. Nothing not covered. I wrote no files apart from the temporary directory under $TMPDIR, which I have removed.

### Gate — approve, `standing yes`, 2026-10-05

Taken under the standing yes recorded in `map-manager-only.md`, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, found both flags true, and covered every clause. This settles none of the node's flags; they settle at the node closing report.

## Flags

`391.1` `ASSUMPTION` **· settled** — map-history.md also gets the pre-change form of the sentence clause 2 extended. *(The worker's full text is under its handover's `FLAGS`.)*

`391.2` `ASSUMPTION` **· settled** — the frozen sentence citing node 212 for "the filing in the resolving edit" was left unchanged. *(The worker's full text is under its handover's `FLAGS`.)*

*The manager's note, 2026-10-05:* flags 391.1, 391.2 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
