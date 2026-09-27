# Add the annotation section and what a hard rule is to graph-conventions.md

Type: implementation
Status: resolved
Supersedes: 73, 79
Blocked by: none

## Question

Nodes 73 and 79 each add one passage to `graph-conventions.md`: 73 what kind of thing a hard rule in a worker contract is, and 79 a section for the annotation the manager writes onto a node whose answer a later node changed. Make both in one piece of work.

*Proposed by [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker and filed by the manager, on the human's "ok" to node 330's merge and its conflicts' recommendations. The worker wrote each condition to the recommended option of every conflict.*

*The worker's blockers:* none

## Acceptance condition

*Written by node 330's worker.*

> The work is `.claude/skills/expedition/graph-conventions.md`. No file outside `.claude/skills/expedition/` changes. No file under `.claude/skills/expedition-checker/`, `expedition-grilling/`, `expedition-implementation/`, `expedition-precondition/`, `expedition-prototype/` or `expedition-research/` changes, so `git diff` over those six directories comes back empty. No file under `.scratch/` changes. The file is one the workflow ships, so it is edited plainly. The places named below are the work itself, so this scope came from no search.
>
> Done means every one of the following is true of the finished tree. Each clause names, in brackets, the node its demand comes from.
>
> 1. (79) The section that documents a node file's sections, `## The node file`, gains a statement of one more kind of section a node may carry: an annotation, written by the manager onto a node whose answer a later node has changed the meaning of. It states three things:
>    - an annotation records what a later piece of work changed about this node's answer;
>    - its text is the reporting agent's own words where a reporting agent supplied them;
>    - it is added rather than replacing anything the node already holds.
> 2. (79) It states where an annotation sits relative to the six sections already listed there (`## Question`, `## Acceptance condition`, `## Answer`, `## Flags`, `## Review`, `## Interview`). So the file's rule that sections appear in the order shown, and only when they have content, is true of a node carrying one. Whether the annotation is one section or several, and where in the order it falls, is the worker's to choose and to state.
> 3. (79) It states that an annotation may carry a heading naming what it records, and gives the form of that heading.
> 4. (79) It states that an annotation is the manager's to write and never a worker's. This is consistent with `SKILL.md`'s `## Writing the graph`, which makes the manager the only writer of the graph's record.
> 5. (79) Whatever the file already fixes about a node file is still present afterwards and has lost nothing it required: the mandatory fields, the rule that fields live in the header block and nowhere else, the six section names, and the statement that sections appear in the order shown and only when they have content.
> 6. (73) The file gains one new section, under a heading of the worker's choosing and at most 200 words long, holding all three of the following:
>    - It states that a hard rule in a worker contract binds by being read by the agent the contract was given to, and that no mechanism in the shipped workflow enforces one.
>    - It states the distinction in both directions. A contract says what a worker **may** do, and what a worker **can** do is a property of the harness that ran it. A clause of the first kind survives a change of harness, and one of the second kind does not.
>    - It states the consequence for anyone writing or editing a contract. A rule that would be false on a harness unable to enforce it does not belong in a shipped file. The remedy for a rule agents read down is a better-written rule or a granted exception, never an assumed capability.
> 7. (73, 79) The file's existing headings, listed by `grep -n '^#\{1,6\} '`, are all still present afterwards and in the same order, with the new material added rather than replacing any of them. No existing text is deleted or reworded, except where clause 2 needs the statement of section order to include the annotation.
> 8. The working tree meets the bar.

## Answer

graph-conventions.md now defines the annotation: manager-written, added never replacing, last in the file, one section each, headed `## Annotation[: what it records]`. It also says a hard rule binds only by being read.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`. The checker passed it on run 1; the work was then carried onto `d3b1a14` with its lines unchanged. The human approved. The work landed as commit `ac10e70`. Flags 340.1 and 340.2 are settled at this gate. The worker's INVALIDATIONS raises `map.md`'s retrospective line, which calls `## Retrospective` an annotation; that goes to the human.

## Handover, attempt 1

*Filed by the manager as handed back, 2026-09-27. The worker's own text, pasted.*

HANDOVER:      Add the annotation section and what a hard rule is to graph-conventions.md

ANSWER:        `.claude/skills/expedition/graph-conventions.md` now documents the annotation and says what a hard rule in a worker contract is. One stale item is also removed from `SKILL.md`.

- **Annotation (from node 79).**
  - Under `## The node file`, the block of section headings gains a seventh line after `## Interview`: `## Annotation <- written by the manager; one section per annotation, in the order written`. The statement "Sections appear in the order shown, and only when they have content." is kept word for word and is now true of a node carrying annotations.
  - A new subsection, ``### `## Annotation` ``, sits after ``### `## Interview` `` and before `## Statuses`. It states:
    - an annotation records what a later piece of work changed about this node's answer, and the manager writes one onto a node whose answer a later node has changed the meaning of;
    - it is the manager's to write and never a worker's, because `SKILL.md`'s `## Writing the graph` makes the manager the only writer of the record. A worker reports the change in its handover.
    - its text is the reporting agent's own words where that agent supplied them, pasted as `### You write as a scribe` says, with the manager's additions standing beside them as its own marked note;
    - it is added to the node and replaces nothing the node holds;
    - each annotation is its own section, after every other section, in the order written;
    - the heading is `## Annotation`, and it may name what it records after a colon: `## Annotation: <what this annotation records>`.
  - Calls made:
    - Several sections, not one.
    - Placed last, so an annotation is always added at the end of the file and never inserted.
    - Heading form taken from existing practice on this graph (about 40 `## Annotation: …` headings).
    - No procedure was added for writing an annotation. The condition asks for none, so node 339's check-step rule is not engaged.
- **Hard rule (from node 73).** A new last section, `## What a hard rule in a worker contract is`, 167 words including the heading. It states:
  - a hard rule binds by being read by the agent the contract was given to, and nothing in the shipped workflow enforces one;
  - a contract says what a worker may do, and what a worker can do is a property of the harness that ran it. A may-clause survives a change of harness and a can-clause does not.
  - so a rule that would be false on a harness unable to enforce it does not belong in a shipped file. Where agents keep reading a rule as demanding less than it says, the remedy is a better-written rule or an exception granted to that rule, and never an assumed capability.
  - "may" and "can" are left unbolded. Writing rule 5 allows bold only where a term is defined.
- **`SKILL.md`.** Item 5 of `## What nothing here settles` ("Where does an annotation onto an already-resolved node belong? … no name, no place in the order, and no form.") is removed, because this work settles all three. Items 6 and 7 become 5 and 6. Nothing cites those items by number.
- Nothing existing in `graph-conventions.md` is deleted or reworded. Its headings are all present in the same order, checked with `grep -n '^#\{1,6\} '`. The new lines are the block line, ``### `## Annotation` ``, the fenced heading example, and `## What a hard rule in a worker contract is`.

INDEX LINE:    graph-conventions.md now defines the annotation: manager-written, added never replacing, last in the file, one section each, headed `## Annotation[: what it records]`. It also says a hard rule binds only by being read.

FLAGS:         ASSUMPTION: I removed item 5 from `SKILL.md`'s `## What nothing here settles` and renumbered the two items after it. The condition names only `graph-conventions.md` as the work, but after this change that item would state something false in a shipped file. The condition's scope allows any change inside `.claude/skills/expedition/`. The edit is away from the places node 124 is changing.
Index: node 340 removed `SKILL.md`'s open question about where an annotation belongs, since graph-conventions.md now answers it.

ASSUMPTION: Annotations go after every other section, one section each, in the order written, headed `## Annotation` with an optional `: <what it records>`. The condition left this choice to the worker. I followed the graph's existing majority practice, with one change: annotations are always last. Some past annotations sit above `## Answer` and stay as written.
Index: node 340 put annotations last in a node file, one section each, under `## Annotation[: …]`, following existing practice.

NEW NODES:     none

INVALIDATIONS: - `.claude/skills/expedition/SKILL.md`, `## What nothing here settles`, item 5: settled, and removed by this work.
- `map.md`'s retrospective standing preference says the manager files a retrospective "as a `## Retrospective` annotation on the node, which keeps the mandatory section order untouched". The shipped form of an annotation heading is now `## Annotation[: …]`, and `## Retrospective` does not match it. A retrospective also does not fit the new definition of an annotation (what a later piece of work changed about this node's answer). So either that line narrows to calling the retrospective a section of its own rather than an annotation, or its heading becomes `## Annotation: the retrospective`, which is already used 3 times. This is the manager's call, as a change to the map.
- Existing annotations placed above `## Answer` on older nodes are record text and stay as written. They now depart from the stated position. No repair is owed under never-delete.

CONDITIONS:    I searched every open or claimed node's `## Acceptance condition` for: annotat, "nothing here settles", "six sections", "seventh section", "hard rule", "binds by being read", `## Retrospective`.
- 160: mentions its own `## Annotation` sections only. Unaffected.
- 219 (unclaimed) requires the retrospective to be written last and "under the heading `## Retrospective` and under no other heading".
- 221 (unclaimed), clause 1, requires ten files to carry "a section headed exactly `## Retrospective`, positioned last".
- Neither clause is made false by a fact this work establishes, because a retrospective is not an annotation under the new definition. Both still write a section missing from the node file's list of sections, and that was already true before this work. So I write no replacement. Once this lands, and only if the manager resolves the map tension above by calling retrospectives annotations, each of those clauses would read `## Annotation: the retrospective` in place of `## Retrospective`. That form would be fixed by this node's landed work in `graph-conventions.md`.
- 220 lists existing retrospective headings "as of 2026-09-09". Unaffected.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet (no checker run).
Paths touched (worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/340-g3`):
- `.claude/skills/expedition/graph-conventions.md`
- `.claude/skills/expedition/SKILL.md`
Bar: the repo has no build, tests, formatter or CI. This matches `map-implementation-rules.md`, confirmed by the repo having no manifest or task runner. So the bar is its half without commands.
- Wrap width kept at 104 characters. The only 105-character line is the existing `## Acceptance condition` line in the block.
- Checked against `CONTEXT.md`'s `_Avoid_` lines by hand.
- `git diff` over the six worker/checker contract directories is empty.
Proposed commit message:
Add the annotation section and what a hard rule is to graph-conventions.md

Node: graph-workflow/340

RETROSPECTIVE
1. What I had to hunt for: the heading form annotations actually use. I found it with `grep -h '^## ' nodes/*.md | sort | uniq -c` (`## Annotation` / `## Annotation: …`). I also had to find whether any shipped file already mentioned annotations, which turned up `SKILL.md`'s `## What nothing here settles` item 5. Neither the condition nor the spawn names that item. Its removal is the obvious consequence of this node.
2. What arrived that this node did not need: nearly all of `map.md` (worktree mechanics, concurrency counts, the moved-standard licence), since this node needed only the scope and writing rules. Also the long review-route and record-as-work paragraphs of the rules file. The spawn's notes on nodes 336 to 338 were not needed: none of their quotes appear in my condition. The note on 339 was useful context but was not engaged, because no procedure was added.
3. What would have made this easier: a line in the node or spawn saying "`SKILL.md` `## What nothing here settles` item 5 asks this exact question". The spawn's "SKILL.md where your condition names it" hints at it, but the condition names `SKILL.md` only as a consistency reference. Also a note on the map's `## Retrospective` annotation line, which now conflicts with the chosen heading form.
4. What was stale, wrong or contradictory: `map.md`'s retrospective line calls `## Retrospective` an annotation, while the graph also uses `## Annotation: the retrospective` for the same thing. Nodes 219 and 221 fix `## Retrospective`. One of my own search commands (a shell pipeline over open nodes) hung in the background, and I killed it with pkill. I redid the search in Python. No files were affected.

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-09-27. The checker was resumed from node 124's check.*

> PASS
>
> This is the check of node 340, "Add the annotation section and what a hard rule is to graph-conventions.md". The work is the uncommitted diff in `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/340-g3`, on base 3c25240. It changes `.claude/skills/expedition/graph-conventions.md` (+38, -0) and `.claude/skills/expedition/SKILL.md` (+2, -4).
>
> - **Scope:** met.
>   - `git status --short` shows only the two files, both inside `.claude/skills/expedition/`. So no file outside that directory changes, and nothing under `.scratch/` changes.
>   - `git diff HEAD --` over the six named contract directories returns 0 bytes.
>   - graph-conventions.md is edited plainly: only additions, with nothing struck through.
>   - The SKILL.md change removes item 5 of `## What nothing here settles`, "Where does an annotation onto an already-resolved node belong? … the graph's file format defines no section for them". It renumbers items 6–7 to 5–6.
>   - The condition's fence is "No file outside `.claude/skills/expedition/` changes", and SKILL.md is inside it, so I read the change as permitted. It removes a statement this work makes false: graph-conventions.md now defines that section.
>   - `grep -rnoiE 'nothing here settles[^.]*[0-9]|annotation' SKILL.md` finds no item count and no other mention of annotations left behind.
> - **1:** met. A new subsection, `` ### `## Annotation` ``, sits inside `## The node file`, after `` ### `## Interview` `` and before `## Statuses`. It states all three things:
>   - "An annotation records what a later piece of work changed about this node's answer." The manager writes one "onto a node whose answer a later node has changed the meaning of".
>   - "Where a reporting agent supplied the text, the annotation is that agent's own words".
>   - "An annotation is added to the node. It replaces nothing the node already holds."
> - **2:** met.
>   - "Each annotation is its own section. Annotations come after every other section, in the order they were written".
>   - The node-file block gains the line `## Annotation <- written by the manager; one section per annotation, in the order written` after `## Interview`.
>   - So "Sections appear in the order shown, and only when they have content." holds for a node carrying annotations, and that sentence is unchanged.
> - **3:** met. "The heading is `## Annotation`, and it may name what the annotation records after a colon", with the fenced form `## Annotation: <what this annotation records>`.
> - **4:** met. "An annotation is the manager's to write and never a worker's, because `## Writing the graph` in `SKILL.md` makes the manager the only writer of the graph's record."
> - **5:** met. `git diff --numstat` on graph-conventions.md shows 38 lines added and 0 removed. The mandatory fields, the header-block rule, the six section names and the order sentence are therefore all intact.
> - **6:** met.
>   - The new section `## What a hard rule in a worker contract is` is 157 words (`awk` over the section, piped to `wc -w`), within the 200-word limit.
>   - It says a hard rule "binds by being read by the agent the contract was given to. No mechanism in the shipped workflow enforces one."
>   - It gives the may/can distinction in both directions: a contract says what a worker may do, and what it can do is a property of the harness. A "may" clause survives a change of harness and a "can" clause does not.
>   - It gives the consequence: "A rule that would be false on a harness unable to enforce it does not belong in a shipped file." The remedy for a rule agents read as demanding less is "a better-written rule or an exception granted to that rule, and never an assumed capability."
> - **7:** met.
>   - I compared `grep '^#\{1,6\} '` at HEAD with the working file using `diff`. Every existing heading is present and in order, and the diff shows only additions: the new subsection heading, the new section heading, and two heading-shaped lines inside fenced code blocks.
>   - No existing text in graph-conventions.md is deleted or reworded, since the diff removes 0 lines.
> - **8:** met. See the bar below.
>
> **The bar:**
> - The repo has no build, tests, formatter or CI, so there are no commands to run.
> - `git diff --check`: clean, exit 0.
> - No added line exceeds the file's wrap width.
>
> **Standards:** as in my earlier checks, I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md`.
> - Bore on the work:
>   - The `CONTEXT.md` `_Avoid_` lines, checked by hand against the added text. Nothing found.
>   - The five writing rules. Citations are by heading, there is no added bold, each sentence carries one idea, and "never an assumed capability" stands beside its positive.
>   - `/writing-for-agents`. Nothing found.
>   - The ground rules. The hard-rule section assumes no harness and names no tool, and nothing addresses the human.
> - Did not bear: `/coding-principles` and `/naming`, because the work is prose and the new headings are descriptive.
> - No reviewing skill is named, so I ran none. graph-conventions.md is part of the work, and the change adds to it without moving any element I hold the work against.
>
> The condition records no search command, so there was nothing to re-run.
>
> NOT COVERED:
> - Whether the worker marked the node or wrote to `decisions.md` or `flags.md`. The condition does not demand this; the rules file makes it a bookkeeping rule. The worktree diff contains no such write, and what the main tree's record holds is outside what I was given.

### Carried onto master `d3b1a14`, 2026-09-27

*The manager resumed the worker after node 124 landed, because the passed diff no longer applied. The worker's own report, pasted:*

Node 340 is now carried onto the new master, and none of my text changed.

- **New base:** `d3b1a14`. Branch `worktree-340-g3` was moved with `git rebase master` after I saved the diff to `$TMPDIR/340.diff` and reset the tree. I did not use `git stash`.
- **Resolution:** on the new master, `git apply --3way` applied both files cleanly, so there was nothing to resolve by hand. I then ran `git reset -q` so the change sits unstaged in the working tree, and it is not committed.
- **My text:** unchanged. The added and removed lines of the new diff are identical to the diff the checker passed; I compared them with `diff`.
- **Node 124's text:** kept exactly as landed. ``### `## Annotation` `` now sits right after node 124's three new bullets at the end of ``### `## Interview` ``, before `## Statuses`.
- **Headings:** every heading on master is still present in the same order. The only additions are the four lines from before: the `## Annotation` line in the block of section headings, ``### `## Annotation` ``, the fenced example `## Annotation: <what this annotation records>`, and `## What a hard rule in a worker contract is`.
- **`SKILL.md`:** node 124 did not touch `## What nothing here settles`, so removing item 5 and renumbering the next two still applies as passed. The "item 5" mentions near lines 87 and 91 point to a different list, `## The order you act in`, and are unaffected.

`git diff --stat`:
```
 .claude/skills/expedition/SKILL.md             |  6 ++--
 .claude/skills/expedition/graph-conventions.md | 38 ++++++++++++++++++++++++++
 2 files changed, 40 insertions(+), 4 deletions(-)
```

`git diff --check`: no output, exit 0.

*The manager's note:* no re-check was run. The worker reports the added and removed lines are identical to the diff the checker passed; the human is told this at the gate.

### Gate — approve, 2026-09-27

The human, `verbatim`: *"approve"*

## Flags

`340.1` `ASSUMPTION` **· settled** — I removed item 5 from `SKILL.md`'s `## What nothing here settles` and renumbered the two items after it. The condition names only `graph-conventions.md` as the work, but after this change that item would state something false in a shipped file. The condition's scope allows any change inside `.claude/skills/expedition/`. The edit is away from the places node 124 is changing. — node 340 removed `SKILL.md`'s open question about where an annotation belongs, since graph-conventions.md now answers it.

`340.2` `ASSUMPTION` **· settled** — Annotations go after every other section, one section each, in the order written, headed `## Annotation` with an optional `: <what it records>`. The condition left this choice to the worker. I followed the graph's existing majority practice, with one change: annotations are always last. Some past annotations sit above `## Answer` and stay as written. — node 340 put annotations last in a node file, one section each, under `## Annotation[: …]`, following existing practice.
