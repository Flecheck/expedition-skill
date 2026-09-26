# Keep one re-pointing search script for the rewrite nodes

Type: precondition
Status: resolved
Blocked by: none

## Question

Every rewrite node of the plain-English pass ([node 289](289-a-plain-english-and-compaction-pass-over-the-shipped-files.md)) owes a re-pointing search over the open and claimed nodes' acceptance conditions, and a check of which headings of its file other files cite. Nodes 297, 299, 300 and 295 each wrote their own script for it under `/tmp/claude-1000/`. Put one maintained script at a stable path in the record, so a rewrite worker runs it instead of writing one, and so a spawn can name the nodes that quote the file and the headings clause 5 protects.

## Promoted from

*The manager's note.* Promoted on the second report of the same retrospective item, as the effort's standing instruction requires. The two reports, the workers' own words:

- Node 297, retrospective (3): "a maintained re-pointing script at a stable path, shared by every rewrite node; nodes 299, 300 and 297 each wrote their own".
- Node 295, retrospective (3): "A list of the heading texts protected in this file, and of the open nodes that quote it, precomputed in the spawn (this node's list: 151, 164, 173)." and "A shared, maintained search script in the record rather than per-node copies under /tmp."

Existing copies to start from: `/tmp/claude-1000/n297/search.py` and `/tmp/claude-1000/n295/search.py`.

No acceptance condition is written; this is a precondition, and what must be true when it is done is stated in `## Question`.

## Further reports

*The manager's note.* Later workers reported more on the same item, in their own words:

- Node 298, retrospective (3): "A script that skips the ruled-out examples in the common clauses of 291–302, which match in every search." and "A note that a numbered list's positions are cited by other conditions (96, 280, 161)."
- Node 294, retrospective (4): "`/tmp/claude-1000/n295/search.py` stops collecting at any `## The manager…` heading, so it misses every `## Amendment` filed after a manager's note. That affects nodes 148, 155, 279, 109, 111 and 61." Its own copy, which collects amendment sections, is `/tmp/claude-1000/n294/search2.py`.
- Node 293, retrospective (3): "One shared search script with the node number as an argument (node 313), and a shared phrases file holding the handles common to the five contracts."
- Node 304, retrospective (3): "293's search script only catches `## Amendment` headings. The effort has two `### Amendment` headings, so the shared script should accept any heading level."
- Node 301, retrospective (1) and (3): "Node 293's script needed `TMPDIR`, the input file names and the self-exclusion adapted before it would run." and "A generic version of the search script that takes the before and after files as arguments."

## Answer

One maintained search script now sits at `.scratch/graph-workflow/scripts/search-conditions.py`. It takes a node number, the before-text and the after-text (a file or REV:PATH each), and reports open conditions made wrong and headings clause 5 protects.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. A precondition has no gate. Its flags settle at the report that closes it.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted. The worker was sent one correction mid-node: node 301's worktree had been removed on landing, so it should read the after-text from commit `02bdd3b`.*

HANDOVER:      Keep one re-pointing search script for the rewrite nodes

ANSWER:
One maintained script now sits at `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/scripts/search-conditions.py`. It is the only file in the new directory `.scratch/graph-workflow/scripts/`, and it is untracked and not committed. It replaces the per-node copies under `/tmp/claude-1000/n29x/`.

How to run it, from the repo root:
`python3 .scratch/graph-workflow/scripts/search-conditions.py NODE BEFORE AFTER [--path PATH] [--phrases FILE] [--skip FILE] [--ngram N]`

- NODE is the caller's node number. That node's file is left out of the search. The match is on the number, so `07-` matches 7.
- BEFORE and AFTER are each either a file or `REV:PATH`. A `REV:PATH` is read with `git show` in the main repo.
- The rewritten file's repo-relative path is needed to leave it out of the heading check. The script takes it from `--path`, else from whichever argument is `REV:PATH`, else from the AFTER file's position in its git tree. If none of these gives it, the script exits with an error.
- `--skip FILE`: every line of FILE is dropped from every condition before the search. On a rewrite node, pass the node's own file. That drops the COMMON CLAUSES block, which is identical line for line across the rewrite nodes and whose ruled-out examples otherwise match in every search.
- `--phrases FILE`: one phrase per line.
- `--ngram N`: word n-gram length, 6 by default.

What it collects: every section whose heading starts with `Acceptance condition` or `Amendment`, at any heading level, wherever it sits in the file. A section runs to the next heading at its level or above. Headings inside code fences are ignored. It takes these sections from every node whose first `Status:` line, before the first `##` section, reads `open` or `claimed`.

What it prints, to stdout only:
1. The conditions searched: a count and the node numbers.
2. Quoted spans of the before-text that a condition quotes, each marked GONE (the after-text lacks it) or KEPT. A quote is a span of at least 12 characters in backticks, in single-asterisk italics, or in straight or curly double quotes. Bold does not count as a quote.
3. Word n-gram runs a condition shares with the before-text, each marked GONE or KEPT.
4. Phrase hits per node, when `--phrases` is given.
5. For each before-text heading outside fences, which other files of clause 5's list hold its exact text. Each heading is marked `free`, `PROTECTED, kept` or `PROTECTED, NOT IN AFTER-TEXT`. The clause-5 list is hard-coded in the script as `HEADING_CITING_FILES`. Those files are read as they stand in the main tree, not at a revision. A missing list file is printed as `MISSING FILE`.

Text is compared after lower-casing and dropping markdown and punctuation, as whole words, so line wrapping and emphasis do not matter. The script writes no file, needs no environment variable (it was run with TMPDIR unset), and finds the record and the repo from its own location. The usage note is its docstring, which `--help` prints.

Command for node 302's spawn:
`python3 .scratch/graph-workflow/scripts/search-conditions.py 302 "$(git -C <worktree> merge-base HEAD master):CONTEXT.md" <worktree>/CONTEXT.md --skip .scratch/graph-workflow/nodes/302-rewrite-the-glossary.md`

Demonstration run on node 301's stop skill, before-text `ede2c76`, after-text `02bdd3b`, with `--skip` set to node 301's file:
- It searched 86 conditions.
- Quotes: one hit, node 137, `closing report`, KEPT.
- N-grams: runs in nodes 105, 118, 120, 127, 202 and 314, none gone.
- Headings: all six are `free`, cited by no other clause-5 file. I confirmed this by grep.
- A test phrases file (`closing report`, and others) hit nodes 41, 106, 118, 137 and 309.
- Result: node 301's stop-skill rewrite makes no open condition wrong.

The script was also run on node 292's precondition rewrite (`e64b3de` to `ede2c76`). There it marks eight headings as `PROTECTED, kept`, with the files citing each, so the protected branch works too. Collection was checked on nodes 148 and 155, whose amendments sit after other sections, and on nodes 58 and 103, whose amendments are `###` headings. It was also checked on a synthetic file with a nested `###` amendment and a fenced heading.

Effect of the worktree removal: none on the result. The first run read the worktree's after-text, before the correction arrived. That file had 567 words, the same as `02bdd3b`'s. That run's output matched the final one, except for one false quote hit ("That section", node 287). It came from bold being read as italics and was fixed before the final run. The worktree was only read, never written. To answer the correction, AFTER was given the same file-or-`REV:PATH` form as BEFORE.

INDEX LINE:    One maintained search script now sits at `.scratch/graph-workflow/scripts/search-conditions.py`. It takes a node number, the before-text and the after-text (a file or REV:PATH each), and reports open conditions made wrong and headings clause 5 protects.

FLAGS:
- ASSUMPTION: I added a `scripts/` subdirectory to the record for the script, instead of putting it beside `map.md`, so the graph files stay apart from tooling. Index: "The re-pointing search script was put in a new `.scratch/graph-workflow/scripts/` directory, apart from the graph files."
- ASSUMPTION: skipping the COMMON CLAUSES is opt-in (`--skip <own node file>`) and not the default. Always dropping lines a node shares with other conditions would hide a real hit wherever two conditions quote the same sentence on identical lines. Index: "The script drops common rewrite clauses only when passed `--skip`, so shared lines are never hidden by default."
- ASSUMPTION: text in bold is not counted as a quote, and the heading check reads the clause-5 files from the main tree as it stands. The list is copied into the script, so it must be edited by hand if clause 5's list changes. Index: "The search script treats no bold as a quote and holds clause 5's file list as a hard-coded copy."

NEW NODES:     none

INVALIDATIONS: none

RETROSPECTIVE:
(1) What I had to hunt for:
- Where the duty's search wording lives. It is at the end of `### Changing one after it is written` (lines 415–420 of `.claude/skills/expedition/SKILL.md`), not in the section's opening lines where I read first.
- That clause 5 of node 302 is the heading list, not the search duty. The spawn's "the rewrite nodes' own form of it is in … clause 5" pairs the two, but clause 5 is only the heading rule. The duty itself is stated only in the manager contract.
- Which rewrite nodes are still open. Only 301 (claimed) and 302 were, and that decided how much the common-clause skip matters.
(2) What arrived that this node did not need: nearly all of `map.md`. Of it, I used only the never-delete scope and the graph-file list, to decide where a script may sit. The other candidate copies (`n294/search2.py`, `n295`, `n297`) added only confirmation that they were narrower versions of `n293`'s. Naming one best copy plus the list of defects would have been enough.
(3) What would have made it easier: the spawn saying which rewrite nodes are still open, and that the common clauses are identical line for line across them. A line in the node file on what "the directory it is told to use" means would also have helped: the spawn requires it, but no argument for it was specified, and I read it as permission to write nothing.
(4) Stale, wrong or contradictory:
- The spawn and the node file point at the worktree for node 301, which was removed mid-node.
- Node 313's `## Promoted from` names only the `n297` and `n295` copies as starting points. The spawn names `n293` as the most recent.
- Node 13's template line `Status: open | claimed | …` inside a fence would be read as a status by the old copies' `re.search`. It is harmless there only because node 13's real status line comes first.
- Node 301's file still reads `Status: claimed` after its landing at `02bdd3b`.

## Flags

`313.1` **· settled** `ASSUMPTION` — I added a `scripts/` subdirectory to the record for the script, instead of putting it beside `map.md`, so the graph files stay apart from tooling.

`313.2` **· settled** `ASSUMPTION` — skipping the COMMON CLAUSES is opt-in (`--skip <own node file>`) and not the default. Always dropping lines a node shares with other conditions would hide a real hit wherever two conditions quote the same sentence on identical lines.

`313.3` **· settled** `ASSUMPTION` — text in bold is not counted as a quote, and the heading check reads the clause-5 files from the main tree as it stands. The list is copied into the script, so it must be edited by hand if clause 5's list changes.

*The manager's note, 2026-09-26:* [node 319](319-carry-the-one-case-the-manager-renders-a-reply-into-the-manager-contract.md)'s worker reported a defect in the script, in its own words: "`search-conditions.py` reports GONE n-gram runs even when before and after are the same file. It seems to join 6-grams that sit in different places in the before-text, here the heading "What is in front of the human, and when" and the sentence "one question in front of the human at a time", into a run the text never holds in one piece. Every rewrite of SKILL.md will see these two false GONE lines." Node 302's worker reported that the script misses conditions whose demand is a property rather than a quote (node 247's "appears only in"), and asked for a refused-word check and a property-demand grep. First reports; no node minted.

*The manager's note, 2026-09-26:* [node 324](324-make-the-search-scripts-output-show-what-is-gone.md) changed the script's output. Its worker reports that this node's answer describes the old output on these points: "GONE/KEPT marks, `PROTECTED, NOT IN AFTER-TEXT`, "Look first at the lines marked GONE", and runs merged from any overlapping 6-grams". The current output is described under node 324's `## Answer` and in the script's `--help`.
