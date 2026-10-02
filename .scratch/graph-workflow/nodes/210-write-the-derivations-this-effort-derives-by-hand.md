# Write the derivations this effort has been deriving by hand

Type: implementation
Status: claimed

Blocked by: none

## Question

*Surfaced by [Nothing measures the record about itself](183-nothing-measures-the-record-about-itself.md)'s
worker, and pasted as it wrote it.*

> Write, once, the derivations this effort has re-derived by hand across eight sessions, so
>   that no party needing a number about the record invents the command again. The fog item
>   *"Extraction of a graph tool"* in `map-manager-only.md` is specified in everything but its trigger;
>   this node is that trigger, scoped to the derivations already paid for rather than to a general tool.
>   Nothing is stored: each derivation reads the tree or its version history and returns a current value.

**Blockers, in the worker's words:** none.

## Acceptance condition

*Written by node 183's worker. Pasted as it wrote it, and not the manager's.*

  The work is one new file, `.scratch/graph-workflow/derivations.md`, and one added line in
  `.scratch/graph-workflow/map.md`.

  Done means every one of the following is true of the finished tree.

  1. `.scratch/graph-workflow/derivations.md` exists and contains, as its own named entry, each of
     these nine derivations. Every entry states in one line the question it answers, and then gives the
     means of answering it against the tree at
     `.scratch/graph-workflow/`:
     (a) the byte size of any named file in that directory at any past date;
     (b) the count of node files over time;
     (c) the current count of node files by `Status:` value;
     (d) the current count of node files by `Type:` value;
     (e) the list of nodes whose status is `open` or `claimed`, by file name;
     (f) the count of entries in `flags.md` by checked and unchecked state;
     (g) the total byte size of struck-through text across the directory, and its share of the whole;
     (h) the byte size of each item under `## Notes` in `map.md`, with the items exceeding 500 bytes
         listed, counting each item's own prose and not any quotation of the human's own words;
     (i) the total and mean byte size of the node files.
  2. Entries (c), (d) and (h) each state, in their own text, that a node file's fields are read only
     from the header block above the first `##` heading and that fenced code blocks are skipped, and
     each is written so that it obeys this. A scan that counts a `Status:` or `Type:` line appearing in
     a node's prose body fails this clause.
  3. Each of the nine, run against the tree as the file gives it, returns a value equal to the value
     obtained by measuring the tree directly for that same quantity at the same moment. **No expected
     numeric result is written in the file for any of the nine**, and the file contains no table,
     series or list of recorded measurements.
  4. `derivations.md` states, in its own voice, that it holds no numbers, that a value is obtained by
     running a derivation at the moment the value is wanted, and that a number found written elsewhere
     in the record is a historical statement rather than the current state.
  5. `derivations.md` is not presented as one of the graph's files: it is not added to the list of files
     in the sentence beginning *"The graph is"* in `.scratch/graph-workflow/map.md`, that sentence's
     stated count is left unchanged, and no file under `.claude/` is modified.
  6. `.scratch/graph-workflow/map.md` gains exactly one new line, under `## Notes`, which names
     `derivations.md` by path, says in one sentence that a fact about the record is derived rather than
     stored, and says that a number a worker receives from anywhere is to be re-derived before it is
     relied on. Nothing else in `map.md` changes.
  7. Nothing under `.scratch/graph-workflow/nodes/`, and no other file in
     `.scratch/graph-workflow/`, is modified.
  8. The tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is the trigger the fog item was waiting for**, and the manager records that the narrowing came from the
worker rather than from the human's `ok`: the fog asked for *"extraction of a graph tool"*, and what is minted is
the derivations already paid for by hand. `map-manager-only.md`'s fog item has been narrowed to match in the same
turn.

**Its clause 5 keeps a shipped file out of this effort's practice.** `map.md` says *"The graph is seven files"* and
the shipped `graph-conventions.md` heads a section *"## The seven files"*, so an eighth graph file would drag a
shipped file's structure behind an artifact binding this effort alone — the coupling flag `140.4` recorded and
nothing enforces. That is flag `183.4`, and the manager notes the human may still read a new file in the effort's
directory as an eighth file whatever it is called.

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Write the derivations this effort has been deriving by hand

ANSWER:        The work adds one new file, `.scratch/graph-workflow/derivations.md`, and one new line in `.scratch/graph-workflow/map.md`.

`derivations.md` opens by saying that it holds no numbers, that a value is obtained by running a derivation at the moment the value is wanted, and that a number written anywhere else in the record is a historical statement. It then has nine named entries, `## (a)` to `## (i)`. Each entry gives its question on one line, then its definitions, then one POSIX `sh` block. Nothing in the file is an expected result.

Calls a later reader would otherwise have to re-derive:
- **Where the blocks run.** Every block runs from `.scratch/graph-workflow/` under `sh`. It uses only sh, awk, find, wc, sort, grep and git.
- **Bytes, not characters.** `LC_ALL=C` is set wherever awk measures a length, because a UTF-8 locale makes awk count characters.
- **`worktrees/` is left out.** It holds full checkouts of the repository and is not part of the record.
- **(a)** uses `git rev-list -1 --before="$day 23:59:59" HEAD` and then `git cat-file -s rev:./file`. It fails loudly when there is no commit before the date or the file did not exist. `git show | wc -c` would have printed 0 instead.
- **(b)** gives one line per day on which the node files changed: the count in that day's last commit. It counts `nodes/` and also `issues/`, which was the directory's name before a rename.
- **(c), (d) and (e)** read fields the way `frontier.sh` does. Only the header block above the first `##` counts, fenced code blocks are skipped, and the first occurrence wins. A file with no such field is counted under `(none)`, so the counts always add up to the number of node files. This matters in practice: node 13 has a second `Status:` line in its body, inside the file-format spec.
- **(f)** counts lines beginning `- [ ] ` or `- [x] ` outside fences. The `Format:` block holds an example unchecked entry, so it must be skipped.
- **(g)** defines a strike as the text between `~~` and the next `~~` within one block. A block ends at a blank line, at a heading (a heading is its own block) or where a new list item starts. The markers are not counted. Fences are skipped, and a `~` inside a code span is masked. Every file under the directory except `worktrees/` is included.
- **(h)** defines an item as a paragraph or list item under `## Notes`. Each `*"…"*` span is removed whole; that is how `map.md` quotes the human's words. Line breaks inside an item count and the final one does not. Items over 500 bytes are listed a second time.
- **(i)** is the total from `cat nodes/[0-9]*-*.md | wc -c`, and the mean computed in awk.

The new line in `map.md` is a list item placed at the end of the standing-preferences list. It names `.scratch/graph-workflow/derivations.md`, says a fact about the record is derived rather than stored, says the file is not one of the graph's files, and says a number received from anywhere is re-derived before it is relied on.

Every block was run against the worktree and matched an independent measurement:
- (c), (d), (g) and (h) were re-measured with Python regex scans. The first awk version of (g) disagreed by 68 bytes because it skipped strikes in headings; it was fixed and now matches exactly.
- (f) was checked with grep minus the one fenced example.
- (i) was checked with `wc`.
- (a) was checked with `git show | wc -c`.
- (a)'s failure paths were checked: they exit with 1 and 128.

INDEX LINE:    `derivations.md` holds nine runnable derivations of facts about the record and no values; map.md gains one Notes line saying facts are derived, and received numbers re-derived.

FLAGS:
ASSUMPTION: Clause 2 requires entry (h) to state the node-header rule, but (h) reads `map.md` and no node file. The entry states the rule as it applies to any derivation reading a node file, and says (h) itself reads none. It obeys the part that does apply: it skips fenced code blocks. The clause holds for (h) with nothing to apply it to, so it is not incoherent, and I did not raise.
  Index: Entry (h) states the node-header-block rule clause 2 demands though it reads no node file, and applies only the fence-skipping half.
ASSUMPTION: The condition leaves several measured quantities undefined, so `derivations.md` defines them in its text:
  - struck-through text: per-block, markers excluded, headings included, code spans masked;
  - the human's quotation in `map.md`: the `*"…"*` span, which covers all 11 such spans under `## Notes`, every one of them the human's;
  - a Notes item: a paragraph or a list item;
  - "the directory": every file except `worktrees/`, non-markdown files included;
  - the node-count series: one line per day, counting `issues/` before the rename.
  Index: derivations.md defines the condition's undefined measures itself — strike blocks, human quotations as `*"…"*` spans, Notes items, the directory less worktrees.
ASSUMPTION: The new `map.md` line is a list item appended to the standing-preferences list, so that the diff is exactly one added line. A free-standing paragraph would also need a blank line, which makes two.
  Index: map.md's derivations line is a list item ending the standing-preferences list, so the diff adds exactly one line.

NEW NODES:     none

INVALIDATIONS: none. The work extends node 183's answer by carrying it out, and contradicts nothing.

CONDITIONS:    I searched the `## Question` and `## Acceptance condition` text of every open and claimed node (status read from the header) for: derivation, re-deriv, "derive", "seven files", "The graph is", non-authoritative, "recorded measurement".
- Node 220 (open) adds one entry to `derivations.md` "alongside the entries already" there, and leaves existing entries unchanged. This work creates that file with the entries `(a)`–`(i)`, so node 220's precondition is now met. No clause needs replacing.
- Node 211 (open) asks that the party receiving a number re-derive it. The new `map.md` line states that for this effort. 211's question is about what a handed-on number must carry, which this does not answer, so it is unchanged.
- Node 209 mentions "what derives numbers about the record" only as a contrast. No change.

MISSING FROM MAP: none. I needed two facts that are not in `map.md`: that node files lived under `issues/` before `nodes/`, which `git log --summary` showed, and that `worktrees/` sits inside the record directory, which `ls` and `.gitignore` showed. Both are facts about the tree rather than about the effort.

GATE PAYLOAD:  No checker findings yet.

Bar: the repo has no build, tests, formatter or CI (the root holds only `.claude/`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch/`), which matches `map-implementation-rules.md`. So the bar is its non-command half, and every derivation block was executed.

Paths touched:
- `.scratch/graph-workflow/derivations.md` (new)
- `.scratch/graph-workflow/map.md` (+1 line)

Proposed commit message:
```
Write the derivations of facts about the record

Add .scratch/graph-workflow/derivations.md, nine runnable derivations of facts
about the effort's record that hold no values, and one map.md Notes line saying
a fact about the record is derived rather than stored.

Node: graph-workflow/210
```

RETROSPECTIVE
1. What I had to hunt for: the `issues/` to `nodes/` rename, which matters for (b); that `worktrees/` sits inside the measured directory, which matters for (g); that node 13 holds a second `Status:` line in its body; that flags.md's `Format:` block holds an example unchecked entry; and the convention that the human's words appear as `*"…"*`. I also found that `close` is an awk builtin, so it cannot be used as a variable name.
2. What arrived that this node did not need: the note that node 190 is claimed, and the note that the fog item was gone. `frontier.sh` was useful.
3. What would have made this easier: the condition defining its own measures, especially what counts as struck text and as a Notes item, and saying whether "the directory" includes `worktrees/` and non-markdown files.
4. What was stale, wrong or contradictory: clause 2 applies the node-header rule to (h), which reads no node file. The node's Question still names the fog item in `map-manager-only.md`, which is no longer there, as the manager noted.
````

## Flags

`210.1` `ASSUMPTION` — *The worker's own text.* Clause 2 requires entry (h) to state the node-header rule, but (h) reads `map.md` and no node file. The entry states the rule as it applies to any derivation reading a node file, and says (h) itself reads none. It obeys the part that does apply: it skips fenced code blocks. The clause holds for (h) with nothing to apply it to, so it is not incoherent, and I did not raise.

`210.2` `ASSUMPTION` — *The worker's own text.* The condition leaves several measured quantities undefined, so `derivations.md` defines them in its text: - struck-through text: per-block, markers excluded, headings included, code spans masked; - the human's quotation in `map.md`: the `*"…"*` span, which covers all 11 such spans under `## Notes`, every one of them the human's; - a Notes item: a paragraph or a list item; - "the directory": every file except `worktrees/`, non-markdown files included; - the node-count series: one line per day, counting `issues/` before the rename.

`210.3` `ASSUMPTION` — *The worker's own text.* The new `map.md` line is a list item appended to the standing-preferences list, so that the diff is exactly one added line. A free-standing paragraph would also need a blank line, which makes two.
