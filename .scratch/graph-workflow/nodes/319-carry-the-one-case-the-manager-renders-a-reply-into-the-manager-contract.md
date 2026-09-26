# Carry the one case the manager renders a reply into the manager contract

Type: implementation
Status: resolved
Blocked by: none

## Question

*Surfaced by [node 315](315-the-manager-contract-forbids-rendering-a-reply-while-graph-conventions-permits-a-paraphrase.md)'s worker, and filed by the manager as it wrote it.*

State in the shipped manager files the only case where the manager records a reply in its own words, and remove the contradiction between them.

## Acceptance condition

*Written by node 315's worker. Pasted as it wrote it, and not the manager's.*

1. In `.claude/skills/expedition/SKILL.md`, section `### The human's words`, the sentence "You never render a reply, so its mark never depends on your judgement." no longer appears. In its place, that section states all four of the following, in wording of the worker's choosing:
   (a) The manager records a reply in its own words only when the human's words are no longer in its context to copy, because a compaction or the end of a session lost them before they were written onto the node.
   (b) Such an entry holds what the manager still has. It is marked `paraphrase`, never `verbatim`, and it carries a note of the manager's own saying why it could not paste.
   (c) In every other case the manager pastes the reply as the human wrote it. The existing sentence "Paste the reply as the human wrote it, however terse." may stand as this statement.
   (d) Whether the words are still present to copy is a fact, not a judgement of the manager's, so the mark does not depend on the manager's judgement.
2. In `.claude/skills/expedition/graph-conventions.md`, section `### Recording the human's words`:
   - the sentence "The manager marks an answer `paraphrase` only where it could not avoid rendering the answer in its own words." no longer appears;
   - the section says that SKILL.md's `### The human's words` states when an answer is marked `paraphrase`;
   - the section still names both marks, `verbatim` and `paraphrase`, and still says what `verbatim` means;
   - the section states no condition of its own for when `paraphrase` is used.
3. No sentence in either file still says or implies that the manager never renders a reply, or that it may render one for any reason other than the one in 1(a).
4. The work changes no file other than these two.

## Answer

SKILL.md's `### The human's words` now states the one case the manager records a reply in its own words, marked `paraphrase`; graph-conventions.md points there instead of stating its own condition.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, as changed by correction round 1. The checker passed it on run 2. The human approved. The work landed as commit `f403975`.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-25. The worker's own text, pasted.*

HANDOVER:      Carry the one case the manager renders a reply into the manager contract

ANSWER:        The shipped manager files now state one case in which the manager records a reply in its own words, and the two files no longer contradict each other.

In `.claude/skills/expedition/SKILL.md`, `### The human's words`, the sentence "You never render a reply, so its mark never depends on your judgement." is gone. The paste sentence stays as it was, and a new paragraph follows it:

"Record a reply in your own words only when the human's words are no longer in your context to copy. A compaction of your context, or the end of a management session, can lose the human's words before you have written them onto the node. In that case, write down what you still have. Mark the entry `paraphrase` and never `verbatim`, and add a note of your own that says why you could not paste. Whether the words are still in your context is a fact and not a judgement of yours, so the mark never depends on your judgement."

In `.claude/skills/expedition/graph-conventions.md`, `### Recording the human's words`, the sentence "The manager marks an answer `paraphrase` only where it could not avoid rendering the answer in its own words." is deleted. It had no replacement sentence. Instead, the section's opening sentence already pointed at SKILL.md's `### The human's words`, and it now lists "when it marks an answer `paraphrase`" among the things that section says. The paragraph that names both marks and says what `verbatim` means is unchanged. The section now gives no condition of its own for `paraphrase`.

Calls a later reader would otherwise re-derive:
- "End of a session" became "end of a management session". `CONTEXT.md` lists `session` in the `_Avoid_` lines for effort and attempt. "Management session" is the term the stop skill already uses for the manager's session, so it names a different thing.
- I put the pointer into the existing opening sentence rather than adding a second sentence. The existing sentence already sent the reader to the same SKILL.md section, and two pointers to one section in a short section would repeat each other.
- The scribe section's "a paraphrase silently becoming the permanent record" was left alone. It is about agents' handed-back text, not the human's replies, so it does not imply that the manager never renders a reply (condition point 3).

Bar: the repo has no build, tests, formatter or CI. I checked this against the repo: no manifest, no task runner, and `map-implementation-rules.md` says the same. The bar is therefore its non-command half: standing writing rule 5, `CONTEXT.md`'s `_Avoid_` lines, and `graph-conventions.md`. New lines are wrapped to the file's width.

INDEX LINE:    SKILL.md's `### The human's words` now states the one case the manager records a reply in its own words, marked `paraphrase`; graph-conventions.md points there instead of stating its own condition.

FLAGS:         none

NEW NODES:     none

INVALIDATIONS: none. The `## Answer`s of nodes 296 and 312 quote SKILL.md's old "You never render a reply", and node 300's and node 26's quote graph-conventions.md's "could not avoid" sentence. Those quotes are now out of date. Node 315 already noted this as a later edit to a file, not a contradicted decision.

GATE PAYLOAD:  No checker findings yet.
Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/319-the-one-case-the-manager-renders`, uncommitted):
- `.claude/skills/expedition/SKILL.md`
- `.claude/skills/expedition/graph-conventions.md`
Proposed commit message:
  State the one case the manager records a reply in its own words

  SKILL.md's `### The human's words` replaces "You never render a reply" with the one case: the human's words are no longer in context to copy, so the entry is marked `paraphrase` with a note of why. graph-conventions.md drops its "could not avoid" condition and points to SKILL.md.

  Node: graph-workflow/319

RE-POINTING SEARCH:
Commands, run from `/home/mathieu/projects/graph-agent`:
- `python3 .scratch/graph-workflow/scripts/search-conditions.py 319 4cc74de:.claude/skills/expedition/SKILL.md .scratch/graph-workflow/worktrees/319-the-one-case-the-manager-renders/.claude/skills/expedition/SKILL.md`
- `python3 .scratch/graph-workflow/scripts/search-conditions.py 319 4cc74de:.claude/skills/expedition/graph-conventions.md .scratch/graph-workflow/worktrees/319-the-one-case-the-manager-renders/.claude/skills/expedition/graph-conventions.md`
- A control run with the before-text as the after-text: `python3 .scratch/graph-workflow/scripts/search-conditions.py 319 4cc74de:.claude/skills/expedition/SKILL.md 4cc74de:.claude/skills/expedition/SKILL.md`
- A direct grep of `nodes/` for "never render a reply" and "could not avoid rendering". It found them only in resolved nodes 26, 296, 300, 312 and 315, plus this node.
Result: no open or claimed condition quotes text I removed. No replacement clause and no supersession proposal is owed.
- graph-conventions.md: no GONE entries.
- SKILL.md: two GONE n-gram runs, "is in front of the human at a time" (node 118) and "what is in front of the human at" (node 127). Both are false positives. The control run against the unchanged file reports the same two GONE, and that text is untouched in both versions.

RETROSPECTIVE:
1. Hunted for: very little. I looked for whether "session" is refused in `CONTEXT.md` and found it in the `_Avoid_` lines for Effort and Attempt. Then I looked for the manager's own session term and found "management session" in `.claude/skills/expedition-stop/SKILL.md`. I had checked `CONTEXT.md` and `expedition/SKILL.md` first. I also had to confirm that the two GONE runs were artifacts, which took the control run.
2. Not needed: most of `map-implementation-rules.md`, since only the ground rules and writing rule 5 bore on this node. Also the contract's sections on reporting new implementation nodes and on replacement attempts. The decisions index was not needed: node 315's file carried everything, and the spawn pointed straight at it. No different arrangement is needed, because the spawn was already tight.
3. Easier: the condition could have said whether "end of a session" had to be kept word for word. It collides with `CONTEXT.md`'s refused `session`, and a checker reading the `_Avoid_` lines could flag either choice. A note in the node file on which session is meant would settle it.
4. Stale or wrong: `search-conditions.py` reports GONE n-gram runs even when before and after are the same file. It seems to join 6-grams that sit in different places in the before-text, here the heading "What is in front of the human, and when" and the sentence "one question in front of the human at a time", into a run the text never holds in one piece. Every rewrite of SKILL.md will see these two false GONE lines. Separately, the kept `### The human's words` text still says the human's words "stay banked". That is a figure of speech under writing rule 5. It is outside this node's condition, so I left it.

## Review

### Checker run 1 — `FAIL`, acceptance condition

*The checker's own text, pasted, 2026-09-26. The checker was resumed from node 314's check, stopped on a usage limit mid-check, and was resumed again after the reset.*

> FAIL: acceptance condition
>
> Node 319, "Carry the one case the manager renders a reply into the manager contract", fails on part 3 of its acceptance condition. One sentence the work left untouched still requires the human's words to be recorded verbatim, with no exception. Parts 1, 2 and 4 are met, and the bar holds. The fix is a one-line edit.
>
> My contract is the main-tree checker contract, unchanged since my last check: its last commit is `76e66e3` and it has no uncommitted edits. The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/319-the-one-case-the-manager-renders`, on branch `worktree-319-the-one-case-the-manager-renders`, based on `4cc74de`. I read the changed paths only as the work. No list of rule changes was asked for this node, so none is given.
>
> I was told the worktree had not changed since the usage limit. I checked that myself: `git status` and `git diff --stat` show the same two files and the same 9 insertions and 6 deletions I read before the stop.
>
> **Finding: part 3, a sentence still implying the manager never renders a reply (1 instance)**
> - **Instance:** `.claude/skills/expedition/graph-conventions.md`, section `### `## Review``, item 2 of the three kinds of entry: "Each correction round, numbered, with the human's words verbatim and what the worker changed."
>   - The manager writes a correction round's entry from the human's reply. The sentence requires those words verbatim in every case.
>   - Suppose a compaction or the end of a session loses a correction-round reply before it is written onto the node. The new rule in `SKILL.md` (part 1(a) and (b)) says to record what the manager still has, marked `paraphrase`. This sentence still demands the words verbatim. So it implies the manager never renders that reply, which part 3 rules out.
>   - Wording that defers to `SKILL.md` would meet part 3, for example "with the human's words, recorded as `### The human's words` in `SKILL.md` says".
> - **Form:** a sentence in either file that requires the human's words to be recorded verbatim with no exception, where the manager writes those words from the human's reply rather than pasting text an agent handed back.
> - **Extent (enumerator):** `for f in .claude/skills/expedition/SKILL.md .claude/skills/expedition/graph-conventions.md; do tr '\n' ' ' < $f | tr -s ' ' | grep -o -i -E "[^.]*(verbatim|as (they|the human) (said|wrote)|human's (own )?words|never render)[^.]*\."; done`. I judged each hit by hand.
>   - The review item above is the only instance.
>   - The `### Park` step 2 sentence ("Include every question already answered, with the human's words verbatim and not summarised") is not an instance. There the manager appends the progress the worker hands back, so it pastes an agent's text and does not render a reply.
>   - The `map-history.md` and fog-item "verbatim" sentences concern map text, not replies.
>
> **Part by part**
> 1. **`SKILL.md`, `### The human's words`: met.**
>    - The sentence "You never render a reply, so its mark never depends on your judgement." no longer appears.
>    - (a) "Record a reply in your own words only when the human's words are no longer in your context to copy. A compaction of your context, or the end of a management session, can lose the human's words before you have written them onto the node. In that case, …" This limits rendering to that case.
>    - (b) "write down what you still have. Mark the entry `paraphrase` and never `verbatim`, and add a note of your own that says why you could not paste."
>    - (c) "Paste the reply as the human wrote it, however terse." stands.
>    - (d) "Whether the words are still in your context is a fact and not a judgement of yours, so the mark never depends on your judgement."
> 2. **`graph-conventions.md`, `### Recording the human's words`: met.**
>    - The sentence "The manager marks an answer `paraphrase` only where it could not avoid rendering the answer in its own words." is removed.
>    - The section now says `SKILL.md`'s `### The human's words` states "when it marks an answer `paraphrase`".
>    - It still names both marks: "Every recorded answer carries one of two markers, `verbatim` or `paraphrase`."
>    - It still says what `verbatim` means: "A reply pasted as the human wrote it is marked `verbatim`. That mark says the answer is the human's own words rather than the manager's rendering of them."
>    - It states no condition of its own for `paraphrase`.
> 3. **No sentence says or implies the manager never renders a reply, or renders one for another reason: fails**, on the one instance above.
>    - Nothing in either file gives any other reason to render a reply.
>    - "Never re-author, shorten, re-order, re-render or improve that text" and "re-authoring what an agent wrote" concern text an agent handed back, not the human's replies.
> 4. **No other file changes: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md` modified, with no untracked files.
>
> **The bar**
> - The repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at my last check: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the new text is plain and direct.
>   - `CONTEXT.md`'s `_Avoid_` lines: "Verbatim / paraphrase" are spelled as `CONTEXT.md` defines them. "Session" names a management session, not an effort or an attempt.
>   - `graph-conventions.md`, which is itself part of the work.
>   - All five ground rules, which are met.
> - No reviewing skill is named, so I ran none.

### Correction round 1 — the worker's changes for checker run 1

*The worker's own text, pasted, 2026-09-26.*

CORRECTION ROUND 1, node 319: Carry the one case the manager renders a reply into the manager contract

WHAT I CHANGED: I fixed the checker's one finding, on part 3 of the acceptance condition. The fix is in `.claude/skills/expedition/graph-conventions.md`, section `### `## Review``, item 2 of the three kinds of entry.
- Before: "Each correction round, numbered, with the human's words verbatim and what the worker changed."
- After: "Each correction round, numbered, with the human's words and what the worker changed. The human's words are recorded as `### The human's words` in `SKILL.md` says."

The item no longer asks for the words verbatim with no exception. It now defers to the SKILL.md rule, and that rule includes the one `paraphrase` case. The change touches part 3 of the acceptance condition. Part 4 still holds, because no file other than the two named changed. `SKILL.md` did not change this round. I left the `### Park` step 2 sentence alone, as the checker judged it is not an instance.

RE-POINTING SEARCH: I re-ran it for graph-conventions.md, because the new wording removes the word "verbatim" from item 2. Commands, run from `/home/mathieu/projects/graph-agent`:
- `python3 .scratch/graph-workflow/scripts/search-conditions.py 319 4cc74de:.claude/skills/expedition/graph-conventions.md .scratch/graph-workflow/worktrees/319-the-one-case-the-manager-renders/.claude/skills/expedition/graph-conventions.md`
- `grep -l "human's words verbatim and what" .scratch/graph-workflow/nodes/*.md`

Result: the script reports no GONE entries. The grep finds the old sentence only in resolved nodes 20, 38 and 75, plus this node's own file. No open or claimed condition quotes it, so I owe no replacement clause.

PARTS OF THE HANDOVER THAT DIFFER:
- ANSWER: add this paragraph: "In `graph-conventions.md`'s `### `## Review``, item 2 no longer requires a correction round's human words to be recorded verbatim. It says they are recorded as SKILL.md's `### The human's words` says. That keeps the one `paraphrase` case open for a correction-round reply lost before it was written down."
- INDEX LINE: unchanged.
- FLAGS: none. NEW NODES: none. INVALIDATIONS: none, unchanged.
- GATE PAYLOAD:
  - Checker finding (part 3, the `## Review` item 2 sentence): reworded as above.
  - Paths touched: unchanged, still `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md`.
  - Proposed commit message: the body gains one sentence, "graph-conventions.md's `## Review` item 2 defers to the same rule for correction-round replies." The trailer is still `Node: graph-workflow/319`.

RETROSPECTIVE ADDITION: my first pass searched both files for "render", "paraphrase" and "in its own words". It did not search for "verbatim" used as a requirement, and that is the form the checker found. A spawn note that part 3 covers every sentence requiring the human's words verbatim would have caught this in the first pass.

### Checker run 2 — `PASS`

*The checker's own text, pasted, 2026-09-26.*

> PASS
>
> This is check 2 of node 319, "Carry the one case the manager renders a reply into the manager contract". The part-3 finding from run 1 is fixed, and the correction changes nothing else. The work now meets all four parts of the acceptance condition, and the bar holds.
>
> My contract is the main-tree checker contract, unchanged since run 1: its last commit is `76e66e3` and it has no uncommitted edits. The work is in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/319-the-one-case-the-manager-renders`, based on `4cc74de`. I read the changed paths only as the work. No list of rule changes was asked for this node, so none is given.
>
> **What changed since run 1.** I worked this out from the diff itself, not from the worker's statement. It matches the statement exactly:
> - `.claude/skills/expedition/graph-conventions.md`, section `### `## Review``, item 2 of the three kinds of entry.
>   - Before: "Each correction round, numbered, with the human's words verbatim and what the worker changed."
>   - After: "Each correction round, numbered, with the human's words and what the worker changed. The human's words are recorded as `### The human's words` in `SKILL.md` says."
> - `.claude/skills/expedition/SKILL.md` has exactly the same diff as in run 1.
> - The rest of the `graph-conventions.md` diff is the same as in run 1.
> - `git diff --stat` now shows 11 insertions and 7 deletions, against 9 and 6 in run 1. The difference is this one item.
>
> **Part by part**
> 1. **`SKILL.md`, `### The human's words`: met**, as established in run 1. That file is unchanged since then.
>    - The sentence "You never render a reply…" is gone.
>    - (a) The one case: the words are no longer in context, because a compaction or the end of a session lost them.
>    - (b) What the entry holds: what the manager still has, marked `paraphrase` and never `verbatim`, with its own note saying why it could not paste.
>    - (c) "Paste the reply as the human wrote it, however terse."
>    - (d) "…is a fact and not a judgement of yours, so the mark never depends on your judgement."
> 2. **`graph-conventions.md`, `### Recording the human's words`: met**, as established in run 1. That section is unchanged this round.
>    - The old `paraphrase` sentence is removed.
>    - The section points to `SKILL.md` for "when it marks an answer `paraphrase`".
>    - It still names both marks and still says what `verbatim` means.
>    - It still gives no condition of its own for `paraphrase`.
> 3. **No sentence says or implies the manager never renders a reply, or renders one for another reason: met.**
>    - The run-1 instance now defers to `SKILL.md`'s `### The human's words`, which holds the one exception. It no longer demands the words verbatim in every case.
>    - I re-ran the run-1 enumerator over both files, unwrapped, and read every hit:
>      `for f in .claude/skills/expedition/SKILL.md .claude/skills/expedition/graph-conventions.md; do tr '\n' ' ' < $f | tr -s ' ' | grep -o -i -E "[^.]*(verbatim|as (they|the human) (said|wrote)|human's (own )?words|never render|in (its|your) own words|paraphrase)[^.]*\."; done`
>    - No instance remains. The `### Park` step 2 sentence is still not an instance, as judged in run 1: there the manager pastes the progress the worker hands back. The `map-history.md` and fog-item "verbatim" sentences concern map text, not replies.
>    - Nothing in either file gives any other reason to render a reply.
> 4. **No other file changes: met.** `git status --porcelain --untracked-files=all` shows only `.claude/skills/expedition/SKILL.md` and `.claude/skills/expedition/graph-conventions.md` modified, with no untracked files.
>
> **The bar, re-run in full**
> - The repo has no build, tests, formatter or CI, and `git diff --check` prints nothing.
> - **Standards read:** from `.scratch/graph-workflow/map-implementation-rules.md` in the main tree, in the same state as at run 1: the bar, the review route, the five ground rules and the five standing rules for writing.
> - **Standards that bore on this work:**
>   - Standing rule 5 (plain English): the new sentence is plain.
>   - `CONTEXT.md`'s `_Avoid_` lines: no refused word is introduced.
>   - `graph-conventions.md`, which is itself part of the work.
>   - All five ground rules, which are met.
> - The new sentence's reference to `### The human's words` in `SKILL.md` resolves to that heading.
> - No reviewing skill is named, so I ran none.

### Gate — approve, 2026-09-26

The human, `verbatim`: *"approve"*
