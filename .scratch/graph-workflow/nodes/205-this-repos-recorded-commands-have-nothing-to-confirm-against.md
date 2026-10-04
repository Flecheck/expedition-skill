# Say in the rules file that this repo's recorded bar commands are a copy with nothing to confirm them against

Type: implementation
Status: claimed

Blocked by: none

## Question

*Surfaced by [Which statement of the bar's commands wins where a recorded copy and the repo's own
instructions disagree](174-which-statement-of-the-bars-commands-wins.md)'s worker, and pasted as it wrote it.*

> The rules file's bar paragraph records that this repo has no build, no tests, no
> formatter and no CI, and says it was recorded so no later node re-derives it. Under the rule above,
> a record is confirmed against the repo's own statement before use — and this repo makes no such
> statement, so there is nothing to confirm against and the record stands as it is. Three checkers this
> session spent a look re-verifying the absence from the tree anyway. Say what the record is and what
> confirming it costs here, so the next one does not.

**Blockers, in the worker's words:**

> none. It states this repo's case and is true whether or not the node above has landed;
> landing after it is tidier, so the two wordings agree.

## Acceptance condition

*Written by node 174's worker. Pasted as it wrote it, and not the manager's.*

> The work is the file `.scratch/graph-workflow/map-implementation-rules.md`, relative to the
> repository root. The worker may edit that file and no other.
>
> Done means every one of the following is true of the finished tree.
>
> 1. The paragraph in the section headed `## What the work is held against` that records this repo's
>    bar commands states, in its own words, all three of the following: that what it records is a copy
>    of an earlier discovery rather than the authority for what is run; that where a repo states its
>    own build, test or format commands such a copy is confirmed against that statement before use and
>    the repo's statement wins where the two differ; and that this repo states none of its own, so
>    there is nothing to confirm the record against and it stands as it is.
> 2. That paragraph keeps every factual claim it already makes about this repo: no build, no tests, no
>    formatter and no CI; no manifest and no task runner; and one ignore file, which invokes nothing.
> 3. ~~That paragraph keeps its statement that the bar here is entirely its non-command half and that
>    this is a complete bar rather than a deficient one, and its enumeration of that non-command half
>    is unchanged.~~ *Superseded 2026-10-02 by node 190's replacement; see `## Amendment, 2026-10-02 (from node 190)`. It binds once node 190 lands.*
> 4. Nothing already in that file is deleted. Where the work supersedes text already there, that text
>    is marked as superseded and left where it is, and the new text is added around it.
> 5. No section of that file other than the one named in clause 1 is modified, and within that section
>    no paragraph other than the one named in clause 1 is modified.
> 6. No file other than the one named above is modified.
> 7. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**It states this repo's own case, and [node 204](204-demote-the-recorded-bar-commands-to-a-copy.md) states the rule.** Its author marked it true whether or not 204 has landed and named landing second as tidier rather than necessary, so no edge is written.

**What it buys is measured rather than guessed.** Its author counted three checkers this session that spent a look re-verifying the absence of a build, a test runner and a formatter from this tree — a fourth did so on node 197, after this node was written.

**A collision the manager noticed and did not repair.** Clause 4 says superseded text *"is marked as superseded and left where it is"*, and clause 6 forbids touching any other file. [Node 189](189-where-the-never-delete-rule-stops.md) settled the opposite for exactly this kind of text: a passage stating a rule that currently binds is **replaced** and its old text banked verbatim to `map-history.md` — which clause 6 puts out of reach. The condition was written by node 174's worker, so the manager hands it over as written; where the work turns out to supersede a live rule statement, that goes to the human rather than to a rewrite of the condition.

## Amendment, 2026-10-02 (from node 190)

*Written by [node 190](190-the-rules-file-states-one-list-twice.md)'s worker under its `CONDITIONS`, and filed by the manager under the standing instruction that an open, unclaimed node's condition may be amended where every word of the replacement is already fixed. The worker's words: "Fixed by this node's work once it lands (\"the standards listed at the head of this section\" is in the tree)." It binds once node 190 lands. The worker's own text, pasted:*

- **Clause 3.** "3. That paragraph keeps its statement that the bar here is entirely its non-command half and that this is a complete bar rather than a deficient one, and its pointer to the standards listed at the head of that section, together with the node's acceptance condition, is unchanged."

## Flags

`205.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above.* Node 190's replacement for clause 3 was filed on this open, unclaimed node without asking the human first.
