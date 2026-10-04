# The rules file reserves `decisions.md` to the manager even where a node's own work is that file

Type: implementation
Status: claimed
Blocked by: none

## Question

In `map-implementation-rules.md`, the paragraph on an implementation node's work being the effort's own record calls any change to `decisions.md` or `flags.md` in the work "bookkeeping reserved to the manager" and makes the checker FAIL it. The implementation contract's hard rule 1 allows a worker to write a graph file where its node's own work is a change to that file. Node 156's condition demanded exactly that, and node 156 had to raise. The rules file should state that exception.

*Reported by [node 156](156-four-resolved-nodes-have-no-index-line.md)'s worker under its `NEW NODES`, and filed by the manager. The worker's words on blockers: "none". Its words on why it is not joined to an existing node: "Node 205 targets the same file but a different concern, the bar-commands paragraph. Its clause 5 forbids touching any other paragraph, so it cannot take this one."*

## Acceptance condition

*Authored by node 156's worker and filed by the manager.*

> 1. In `.scratch/graph-workflow/map-implementation-rules.md`, in the paragraph beginning "**An implementation node's work on this effort may be the effort's own record**", the sentence that today reads "**A change to the node's own status line, to `decisions.md`, or to `flags.md` is bookkeeping reserved to the manager**: where one appears among the work the checker's outcome is `FAIL` on the acceptance condition, and that holds whether or not the acceptance condition itself excluded those paths." is replaced. The replacement states both of the following in its own words:
>    (a) a change to the node's own status line is bookkeeping reserved to the manager in every case, and where one appears among the work the checker's outcome is `FAIL` on the acceptance condition;
>    (b) a change to `decisions.md` or `flags.md` is bookkeeping reserved to the manager, with the same `FAIL`, except where the node's acceptance condition requires a change to that file, in which case that change is the work and is checked against the condition like any other work.
> 2. The paragraph's other sentences keep their words.
> 3. The paragraph as it stood before the change is appended **verbatim** to `.scratch/graph-workflow/map-history.md`, at the end of that file, under a new `##` heading of the form "Superseded from `map-implementation-rules.md` at node NN — <what was superseded>", where NN is this node's number. Nothing already in `map-history.md` is edited or removed.
> 4. No file other than these two is modified. No other paragraph of `map-implementation-rules.md` is modified.
> 5. Scope came from no search: the named sentence is the work, not an instance of a defect. A search of `.claude/skills` for "bookkeeping reserved" returned nothing at 4ed809c59. Any other statement of the same rule that the work finds is reported and not edited.
>
> The work is also held against the bar.

## Handover, attempt 1

*Pasted as the worker handed it back.*

`````
HANDOVER:      The rules file reserves `decisions.md` to the manager even where a node's own work is that file

ANSWER:        In `.scratch/graph-workflow/map-implementation-rules.md`, in the paragraph beginning "**An implementation node's work on this effort may be the effort's own record**" (under `## What the work is held against`), the sentence that reserved every change to the node's own status line, to `decisions.md` or to `flags.md` to the manager has been replaced. The new text, unwrapped, reads:

               "**A change to the node's own status line is bookkeeping reserved to the manager in every case**: where one appears among the work the checker's outcome is `FAIL` on the acceptance condition, and that holds whether or not the acceptance condition itself excluded that path. **A change to `decisions.md` or to `flags.md` is also bookkeeping reserved to the manager, with the same `FAIL`, except where the node's acceptance condition requires a change to that file.** Such a required change is the node's work, and the checker holds it against the acceptance condition like any other work. The exception was added at [node 381](nodes/381-the-rules-file-reserves-decisions-md-even-where-it-is-the-work.md)."

               Decisions a later reader would otherwise have to work out again:
               - The status-line half keeps the old sentence's "whether or not the acceptance condition itself excluded" clause, so the status line stays reserved even where a condition is silent about it.
               - The exception applies file by file. A change to `decisions.md` or `flags.md` goes beyond what the condition requires (for example, a condition that requires `decisions.md` but not `flags.md`) is still reserved and still FAILs.
               - The replacement ends with a citation of this node. Without it, the paragraph's closing attribution to node 163 would read as the source of the exception. The rules file's *What this file admits* allows such a link in place of history.
               - All other sentences of the paragraph keep their words. This was checked by normalizing whitespace and confirming that the old file, with only the old sentence swapped for the new text, equals the new file. Line breaks were changed only inside the replaced sentence. The next original line, "paths as the work under this rule.** This rule stands beside ...", is untouched.
               - The paragraph as it stood before the change is appended verbatim, with its original line wrapping, to the end of `.scratch/graph-workflow/map-history.md`. It sits under "## Superseded from `map-implementation-rules.md` at node 381 — the sentence reserving `decisions.md` and `flags.md` to the manager in every case", in the same shape as the earlier entries: an italic account, a `###` "From `## What the work is held against` — ..." subheading, then "*Replaced, and it stood as:*". A script confirmed that the old file is an exact prefix of the new `map-history.md` and that the new file ends with the old paragraph.
               - No other statement of the same rule exists. I searched line-wrap-insensitively (newlines collapsed) for "bookkeeping reserved", "reserved to the manager" and "reserved bookkeeping" across `.claude/skills/**`, `.claude/rules/*` and the top-level files of `.scratch/graph-workflow/`. Only this paragraph matched. A plain grep for "bookkeeping" in `.claude/skills` and `.claude/rules` found only the general statements that a worker does no graph bookkeeping and that the manager adds a flag's bookkeeping. None is a checker FAIL rule. The checker contract does not mention `decisions.md`, `flags.md` or "status line".

INDEX LINE:    The rules file now lets a node change `decisions.md` or `flags.md` where its acceptance condition requires it, and keeps the node's own status line reserved to the manager.

FLAGS:         ASSUMPTION: The acceptance condition asks for the sentence to be replaced with text stating (a) and (b). I added one more short sentence to that replacement, "The exception was added at [node 381](...)". The rules file cites the node that shaped a rule, and its *What this file admits* names that link as what stands in for history. Without it, the paragraph's closing "Surfaced by node 163 ..." would be the only attribution and would misattribute the exception. If the human wants the replacement to state only (a) and (b), deleting that sentence is the whole fix.
               Index sentence: Node 381's worker added a one-sentence citation of node 381 to the replacement text in the rules file, beyond the (a) and (b) the condition demanded.

NEW NODES:     none

INVALIDATIONS: Node 163's rule, as written into `map-implementation-rules.md`, is narrowed. A change to `decisions.md` or `flags.md` that the node's acceptance condition requires is now the work rather than reserved bookkeeping. The status line stays reserved in every case. This also puts in writing the one-off direction given at node 156's raise (human's verbatim "ok" to the worker's RECOMMENDED), so a checker no longer needs that direction in its spawn. Separately, the paragraph's closing sentence, "This rule ... supersedes no wording in this file", was kept word for word as clause 2 demands, but the paragraph itself has now had a sentence superseded. It reads as true of the rule when it was introduced, and is slightly stale as a description of the paragraph now. Reported, not edited.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` text of every open or claimed node (header-block Status), with newlines collapsed, for "bookkeeping reserved", "reserved to the manager", "reserved bookkeeping", "map-implementation-rules" and "own record". Matches outside node 381: node 149 ("own record" is about the repository's own record of a prose standard, unrelated); node 205 (targets `map-implementation-rules.md`'s bar-commands paragraph, unaffected); node 214 (asks which supersession route retired text took, unaffected); node 284 (a manager's note about a count of rules for writing, unaffected). No clause needs replacing, and no open node's question changes. Merge note: node 205, and any other node that supersedes a rules-file paragraph, will also append to the end of `map-history.md`. Integrating both is a trivial append-order conflict.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none received yet.
               Paths touched, relative to the worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/381-reserved-bookkeeping:
               - .scratch/graph-workflow/map-implementation-rules.md
               - .scratch/graph-workflow/map-history.md
               `git status --short` shows only these two files modified. The work is uncommitted, on branch worktree-381-reserved-bookkeeping.
               Bar: I checked the repo afresh. The root holds `.claude/`, `.scratch/`, `CONTEXT.md`, `CONTEXT-MAP.md`, `.gitignore` and no manifest, task runner, formatter config or CI directory. That matches the record in `map-implementation-rules.md`: no build, no tests, no formatter, so the bar is its non-command half (the standards and the acceptance condition). No difference from the recorded commands to report.
               Proposed commit message:
                 Rules file: a required change to decisions.md or flags.md is the work

                 The record-as-work paragraph in map-implementation-rules.md reserved
                 every change to decisions.md or flags.md to the manager, even where a
                 node's acceptance condition required it. Keep the node's status line
                 reserved in every case, and make a required change to either index
                 the node's work. The superseded paragraph is appended to map-history.md.

                 Node: graph-workflow/381

RETROSPECTIVE:
1. What I had to hunt for: nothing much. The manager's note that the sentence is line-wrapped was correct and saved time. I searched with newlines collapsed from the start. Finding the `##` section the paragraph sits under, for the history subheading, took one scan of the file's headings.
2. What arrived that this node did not need: most of `map.md`, which I read whole as the contract requires. Only its `## Notes` items on the never-delete rule, the rules for writing and the ground rules were relevant. The decisions.md line for node 156 added nothing beyond what the node's own question already said.
3. What would have made this easier: a one-line statement in the condition (or in the rules file's *How a rule in this file is superseded*) of the expected shape of a `map-history.md` entry: the `##` heading, the italic account, the `###` "From ..." subheading, "*Replaced, and it stood as:*". I took the shape from the most recent entries. The condition also does not say whether the verbatim copy should keep the source's line wrapping. I kept it.
4. What was stale, wrong or contradictory: nothing in the spawn. Both of the manager's notes checked out (the line wrapping; node 156's raise and the human's verbatim "ok" under its `## Interview`). One mild tension: the paragraph's closing "supersedes no wording in this file" is now slightly stale, but clause 2 required keeping it word for word (see INVALIDATIONS). The rules file's *What this file admits* tells whoever edits a passage to apply its history test to that passage. I read "passage" as the replaced sentence, so clause 2 governed the paragraph's other sentences, including its historical "Surfaced by node 163 ..." attribution.
`````

## Flags

`381.1` `ASSUMPTION` — Node 381's worker added a one-sentence citation of node 381 to the replacement text in the rules file, beyond the (a) and (b) the condition demanded. *(The worker's full text is under its handover's `FLAGS`.)*
