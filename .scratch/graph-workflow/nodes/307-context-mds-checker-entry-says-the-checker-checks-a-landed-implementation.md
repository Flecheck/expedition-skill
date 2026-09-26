# `CONTEXT.md`'s checker entry says the checker checks a landed implementation

Type: implementation
Status: resolved
Blocked by: 302

## Question

`CONTEXT.md`'s `**Checker**:` entry says the checker "checks a landed implementation … before the human sees it". The checker runs before the gate, and landing comes after approval. The manager contract now takes its definition from this entry. Correct the word.

*Reported by [node 296](296-rewrite-the-manager-contract-part-1.md)'s worker, which gave it no blockers and left its sequencing with node 302, the glossary rewrite, to the manager. The manager has blocked it on node 302 under node 289's freeze on a file being rewritten.*

## Acceptance condition

*Authored by node 296's worker and filed by the manager.*

1. In `CONTEXT.md`, the `**Checker**:` entry no longer says the checker checks a *landed* implementation. It says the checker checks a finished implementation, before the human sees it.
2. No other entry in `CONTEXT.md` changes.
3. No other path changes.
4. The working tree meets the bar.

## Answer

The glossary's checker entry now says the checker checks a finished implementation, not a landed one, because the checker runs before the gate and landing follows approval.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1. The human approved. The work landed as commit `7d6a67f`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      CONTEXT.md's checker entry says the checker checks a landed implementation

ANSWER:        In `CONTEXT.md`, the first line of the `**Checker**:` entry now reads "The second, independent, read-only agent that checks a finished implementation against its acceptance condition and the bar before the human sees it." The only change is that "landed" became "finished". The checker runs before the gate and landing comes after approval, so "landed" named the wrong moment. The line is now 101 characters wide. The file's lines run up to 102, so the entry was not rewrapped. No other entry and no other path changed. The word "finished" appears on the `_Avoid_` line of the `**Closed**:` entry, but that line refuses it only as a word for an effort being over. The glossary already uses "finished" in its ordinary sense elsewhere (its opening line, and the `**Handover**:` entry), so this use does not conflict with it. The repo has no build, tests, formatter or CI, so the bar is its non-command half only. The one-word edit meets it: the sentence is plain English and unchanged in shape.

INDEX LINE:    The glossary's checker entry now says the checker checks a finished implementation, not a landed one, because the checker runs before the gate and landing follows approval.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none. The re-pointing search found no open or claimed condition that quotes the removed text.
  Commands run, from the repo root:
  - `python3 .scratch/graph-workflow/scripts/search-conditions.py 307 a57f9cd:CONTEXT.md .scratch/graph-workflow/worktrees/307-checker-entry-landed/CONTEXT.md`. It searched 85 conditions. Every quoted span was KEPT. In the n-gram report, exactly one run was GONE: node 81's "the word is the human s alone the checker s outcomes are pass and fail and". That run is a script artefact and was not caused by this change. The same run is reported GONE when the script compares `a57f9cd:CONTEXT.md` with itself. It is a merged run that joins text from two entries: the `**Reject**:` entry's "The word is the human's alone; the checker's outcomes are `PASS` and `FAIL`" and the checker entry's "outcomes are `PASS` and `FAIL`, and". The text node 81 actually quotes is byte-identical after the change.
  - A grep of every open or claimed node file for "landed implementation", "checks a landed", "checks a finished", "before the human sees it" and "read-only agent that checks". The only hits were node 307 itself, node 43 (the title of a node link, not the entry's text), and node 13's status-line template, which the regex matched although the node is resolved. No replacement clause is owed.
  - A grep of `.claude/skills` for "landed implementation" and "checks a landed" returned nothing.

GATE PAYLOAD:  No checker findings yet.
  Paths touched: `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/307-checker-entry-landed/CONTEXT.md` (the `**Checker**:` entry, one word). The change is uncommitted.
  Proposed commit message:
    Say the checker checks a finished implementation in the glossary

    The checker runs before the gate, and landing comes after approval,
    so "landed" named the wrong moment.

    Node: graph-workflow/307

RETROSPECTIVE:
1. What I had to hunt for. I checked whether "finished" is a refused word, because the `**Closed**:` entry's `_Avoid_` line lists it. I found that entry by grepping `CONTEXT.md` for `_Avoid_` lines that hold "finished". I also had to work out whether the one GONE line in the search output was mine. I settled it by re-running the script with the same text as before and after. The file's wrap width took an `awk` length count, because "wrap at the file's width" gave no number.
2. What arrived that this node did not need. Almost all of `map-implementation-rules.md`: its history paragraphs, the record-node reading rule, the supersession procedure. So did the long `decisions.md` hits for "checker". For a one-word glossary fix, the spawn could have quoted the five writing rules and the four points of the bar, and skipped both files.
3. What would have made it easier. The spawn could state the file's line width, which is about 100 with a few lines at 102. It could also warn that the search script's n-gram report is already known to show node 81's GONE run on `CONTEXT.md` at `a57f9cd` with no edit at all. The script itself could flag a run that is also GONE when before and after are identical, or it could avoid merging runs across separate matches.
4. What was stale, wrong or contradictory. The search script's n-gram report gives a false GONE for node 81 on an unchanged file. Otherwise nothing: the node file, the spawn and the glossary agreed.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 323's check.*

> PASS
>
> Node 307, "CONTEXT.md's checker entry says the checker checks a landed implementation", meets all four parts of its acceptance condition, and the bar holds. The work is a one-word change in the **Checker** entry, and nothing else changed.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is `CONTEXT.md` in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/307-checker-entry-landed`, on branch `worktree-307-checker-entry-landed`, based on `a57f9cd`. I read the changed path only as the work. No list of rule changes was asked for this node, so none is given.
>
> `CONTEXT.md`'s `_Avoid_` lines are one of the standards this work is held against. The edit does not touch any `_Avoid_` line, so no standard moved.
>
> **Part by part**
> 1. **The Checker entry says "finished", not "landed": met.**
>    - The `**Checker**:` entry changed "checks a landed implementation" to "checks a finished implementation".
>    - It now reads "The second, independent, read-only agent that checks a finished implementation against its acceptance condition and the bar before the human sees it." So it states both required things: a finished implementation, and before the human sees it.
>    - The only "landed" left in the file is in the **Closing report** entry ("what landed"), which is a different entry and correct there.
> 2. **No other entry changes: met.** `git diff` shows exactly one line changed, inside the Checker entry. The rest of that entry, including its `_Avoid_` line, is unchanged.
> 3. **No other path changes: met.** `git status --porcelain --untracked-files=all` shows only `CONTEXT.md` modified.
> 4. **The working tree meets the bar: met**, as below.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): "finished" is plain.
>   - `CONTEXT.md`'s `_Avoid_` lines: none is changed, and no refused word is introduced.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*
