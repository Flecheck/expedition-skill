# Make the search script's output show what is gone

Type: precondition
Status: resolved
Blocked by: none

## Question

The shared re-pointing search script, `.scratch/graph-workflow/scripts/search-conditions.py` (made at [node 313](313-keep-one-re-pointing-search-script-for-the-rewrite-nodes.md)), prints every match, so a worker has to read the whole output to find the few lines that matter, and a search of the output for "GONE" does not prove nothing is gone. Make its output show what is gone at a glance, and fix the reported false results.

## Promoted from

*The manager's note.* Promoted on the second report of the same retrospective item, as the effort's standing instruction requires. The reports, the workers' own words:

- Node 321, retrospective (2): "The search script's full output, 37 KB for two runs, of which only the GONE lines mattered. A `--gone-only` flag on the script, or a spawn that says "grep the output for GONE", would have avoided reading the rest."
- Node 322, retrospective (3) and (4): "The search script could print an explicit "no GONE lines" summary, or tag each gone item with GONE, so that a grep for GONE is conclusive." and "the output has no GONE-tagged data lines when nothing is gone, and only the headers say "GONE"."

- Node 307, retrospective (3) and (4): "The search script's n-gram report gives a false GONE for node 81 on an unchanged file." It is a merged run joining text from the `Reject` and `Checker` entries of `CONTEXT.md`, reported GONE when the script compares `a57f9cd:CONTEXT.md` with itself.

Related first reports, filed on node 313: node 319's worker found two false GONE n-gram runs on every `SKILL.md` change; node 302's worker found the script misses conditions whose demand is a property rather than a quote.

No acceptance condition is written; this is a precondition. What must be true when it is done: every gone item is tagged so that one search of the output finds all of them; the output ends with a count of gone items, which reads zero when nothing is gone; no n-gram run is reported GONE when the before-text and the after-text are the same file, which covers the two runs node 319 reported on `SKILL.md` and the one node 307 reported on `CONTEXT.md`; and the usage note says how to read the output.

## Answer

search-conditions.py now starts every gone item's line with `GONE |` and ends with `# Gone items: N`, and no longer reports false GONE n-gram runs from joining text taken from separate places in the before-text.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. A precondition has no gate. Its flag settles at the report that closes it.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-26. The worker's own text, pasted.*

HANDOVER:      Make the search script's output show what is gone

ANSWER:
I changed `.scratch/graph-workflow/scripts/search-conditions.py` in place. It still takes the same arguments (NODE BEFORE AFTER [--path] [--phrases] [--skip] [--ngram]), prints only to stdout, writes no file and needs no environment variable. I built the change on a copy inside the scripts directory and moved it over the original once, so the script stayed runnable the whole time. The directory is untracked in git, as it was before.

What the output now looks like, which later nodes depend on:
- Every gone item is one line that starts, after its indent, with `GONE |`. There are three forms:
  - `GONE | quote | NN | span`
  - `GONE | n-gram run | NN | run`
  - `GONE | protected heading | text`
  NN is the number of the node whose condition holds the item. A gone line therefore makes sense on its own in grep output, without its `==` group header.
  - The old heading state `PROTECTED, NOT IN AFTER-TEXT` is now `GONE | protected heading`. `free` and `PROTECTED, kept` are unchanged.
- No header uses the word GONE in capitals any more. The report headers now say "each KEPT or gone from the after-text". The per-node n-gram line now reads `== <node> N runs`, without "M gone".
- `grep '^ *GONE |'` on the output lists exactly the gone items. A plain `grep GONE` lists them too, plus any quoted span or heading whose own text contains GONE in capitals.
- The output's last line is always `# Gone items: N (quotes Q, n-gram runs R, protected headings H)`, and it reads `# Gone items: 0 (quotes 0, n-gram runs 0, protected headings 0)` when nothing is gone.
- KEPT lines and free headings are context only.
- The usage note, which `--help` prints, has a new "Reading the output" paragraph saying all of this. It also says that comparing a file with itself reports nothing gone.

Why the n-gram runs were falsely GONE, and the fix:
- The cause: the script merged the 6-grams a condition shares with the before-text whenever they were next to each other in the condition, even when they sat in different places in the before-text. The merged run then appeared in neither text, so it was reported GONE even when a file was compared with itself.
- The fix: a new function, `runs_held_by`, replaces `consecutive_ranges`. It extends a run only while the joined words still appear in one piece in the before-text, and starts a new run where they stop. Every run it reports therefore appears in the before-text. When the after-text is the same file, no run can be gone.
- Real runs are judged exactly as before: a run is GONE when the after-text does not hold it whole.

Test results, run on the installed script:
- `999 f630aa3:.claude/skills/expedition/SKILL.md` against itself: before, two false GONE runs (node 118 "is in front of the human at a time", node 127 "what is in front of the human at"). Now `# Gone items: 0`. Each false run is now two KEPT pieces, for example "is in front of the human" and "in front of the human at a time".
- `999 a57f9cd:CONTEXT.md` against itself: before, one false GONE run (node 81, "the word is the human s alone ... pass and fail and"). Now `# Gone items: 0`, and the run is two KEPT pieces.
- Node 319's real change, `f403975^:.claude/skills/expedition/graph-conventions.md` against `f403975:...`: `# Gone items: 0`. The old script found nothing gone here either, so this pair does not show gone items being reported.
- A pair I constructed to show gone items still being found: `a57f9cd:CONTEXT.md` against a copy in which `## Closing an effort` became `## Ending an effort` and the sentence "A flag goes into the closing report only where the human never spoke again." was replaced. The output was:
  - `GONE | quote | 111 | ## Closing an effort`, twice, because node 111's condition quotes it twice
  - `GONE | n-gram run | 320 | a flag goes into the closing report only where the human never spoke again`
  - `GONE | n-gram run | 320 | a flag goes into the closing report`
  - `GONE | protected heading | Closing an effort`
  - `# Gone items: 5 (quotes 2, n-gram runs 2, protected headings 1)`
  The old script found the same items, plus the false node-81 run.

What this node did not do: node 302's report, that the script misses conditions whose demand is a property rather than a quote (such as node 247's "appears only in"), is not addressed. That was not asked of this node. A gone quote is still counted once for each time a condition quotes it, which is how the old script behaved.

INDEX LINE:    search-conditions.py now starts every gone item's line with `GONE |` and ends with `# Gone items: N`, and no longer reports false GONE n-gram runs from joining text taken from separate places in the before-text.

FLAGS:
ASSUMPTION: I chose the tag format and what counts as a gone item. Gone lines start with `GONE |` and carry their report kind and node number. A protected heading missing from the after-text counts as gone. The final count is broken down by report. Headers no longer use GONE in capitals. Grounds: nodes 321 and 322 asked for a search that proves on its own whether anything is gone, and a missing protected heading is the heading report's version of gone.
Index sentence: The search script's gone tag is a line starting `GONE |` with report kind and node number, a missing protected heading counts as gone, and the final count is broken down by report.

NEW NODES:     none

INVALIDATIONS: Node 313's answer describes the old output: GONE/KEPT marks, `PROTECTED, NOT IN AFTER-TEXT`, "Look first at the lines marked GONE", and runs merged from any overlapping 6-grams. That description is now out of date on those points. Its findings are unaffected, except that a GONE n-gram run reported by the old script may have been a false one.

RETROSPECTIVE:
(1) Hunting: very little. The cause of the false runs was clear from node 313's manager note, which quotes node 319's words, together with reading `report_ngrams`. I confirmed it by running the spawn's test cases. I had to check whether `scripts/` is tracked in git, and it is not. I also had to discover that a copy of the script run from `$TMPDIR` would search the wrong directory, because it finds the record from its own location (`RECORD = parents[1]`). That is why the working copy sat inside the scripts directory.
(2) Unneeded context: the map and decisions index were rightly marked as barely needed, and I did not read them. The git-status snapshot listing dozens of modified node files arrived unasked and was irrelevant.
(3) Easier: the spawn's "real case" example (node 319's change) has nothing gone under either the old or the new script, so it cannot show gone items being reported. A spawn that says so, or names a pair with a known gone item, would save a round of constructing one. The spawn could also say that the script finds the record from its own location, so a copy must sit in the scripts directory.
(4) Stale or contradictory: the spawn implies node 319's change would show gone items; it shows none. Node 313's description of the output format is now out of date, as listed under INVALIDATIONS. Otherwise I found nothing wrong.

## Flags

`324.1` **· settled** `ASSUMPTION` — I chose the tag format and what counts as a gone item. Gone lines start with `GONE |` and carry their report kind and node number. A protected heading missing from the after-text counts as gone. The final count is broken down by report. Headers no longer use GONE in capitals. Grounds: nodes 321 and 322 asked for a search that proves on its own whether anything is gone, and a missing protected heading is the heading report's version of gone.
