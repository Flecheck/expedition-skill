# `.gitignore`'s two comments point at files that no longer hold what they name

Type: implementation
Status: resolved
Supersedes: 159

Blocked by: none

## Question

*Surfaced by [node 244](244-map-says-the-worktree-route-question-is-open.md)'s worker, and pasted as it wrote it.*

> `.gitignore`'s first block says *"See .scratch/graph-workflow/map.md, the landing policy"* and its second says
> *"See .scratch/graph-workflow/map-implementation-rules.md, \"How the worktree is made\""*. Neither resolves: the
> landing policy left `map.md` at node 140 and the rules file at node 188, and *"How the worktree is made"* sits in
> `map-manager-only.md`. Both comments were written at node 158, before those moves. A reader following either lands
> in a file that does not hold the text it was sent for. Found while confirming the bar's commands against the repo;
> it is not a consequence of node 244's work.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 244's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.gitignore` at the repository root, and no other file may be edited. The worker may not mark this
> node, resolve it, or write a line in `decisions.md` or `flags.md`. Done means every one of the following is true
> of the finished tree.
>
> 1. `.gitignore` contains neither the string `See .scratch/graph-workflow/map.md, the landing policy` nor the
>    string `See .scratch/graph-workflow/map-implementation-rules.md, "How the worktree is made"`.
> 2. Each of the file's two comment blocks — the one above `.worktrees/` and the one above `.claude/worktrees/` —
>    carries a pointer naming a file that exists and that contains, at the time of this work, the text the pointer
>    sends its reader to; the worker confirms this by opening each named file and finding the named heading or
>    quoted phrase in it, and reports in its handover which file and which heading it found for each.
> 3. A pointer cites its target by heading or by a quoted phrase and never by line number.
> 4. Both ignore patterns `.worktrees/` and `.claude/worktrees/` are still present and unchanged.
> 5. No line of `.gitignore` is deleted other than the two pointer sentences named in (1), and no comment loses
>    information other than the stale location it names.
> 6. No file other than `.gitignore` is modified.
> 7. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This is the second node against the same two comments.** [Node
227](227-gitignore-cites-a-quoted-phrase-that-resolves-to-nothing.md) is open and was minted for the second comment
alone, found independently by node 235's worker. **The manager has not merged them and has written no edge**, the
two conditions being differently scoped — node 227's covers one comment, this one covers both and adds the duty to
confirm each pointer against the file it names. Whichever is claimed first makes the other's work smaller or empty;
that is the manager's sequencing to hold, and a worker claiming either should be told the other exists.

## Flags

`249.1` **· settled** `ASSUMPTION` — The first block's pointer cites the markdown heading `## Landing an implementation node's
work` rather than the bold phrase `Landing policy` that the superseded pointer's wording ("the landing policy") was
closer to. Both strings exist in `map-manager-only.md` and both satisfy the condition's clause 3, which requires a
heading or a quoted phrase; the condition does not choose between them. The heading was picked because it is a real
markdown heading — so an anchor link, a `grep '^##'` and an outline view all find it, where the bold lead-in is
found only by full-text search — and because it names the whole section rather than one paragraph inside it. The
second block keeps the quoted-phrase form it already had, "How the worktree is made", there being no heading over
that material.

## Annotation: what this worker measured about writing a worktree without entering it

*Filed by the manager from the worker's own gate payload, in its words. Not part of this node's work, and recorded
here because [node 250](250-state-how-an-implementation-worker-reaches-its-worktree.md) is arguing about exactly
this and this is a second, independent measurement.*

> **Working directory, reported because the spawn asked.** The spawn was right and the sibling's case did not
> repeat: this worker launched at `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/nodes`, inside the
> repository and not at its root, on branch `master`. `EnterWorktree` with the worktree's absolute path succeeded
> and moved the session to the worktree, `HEAD` at `f22dd5c`, matching the base the manager named, with a clean
> tree.
>
> **The write-without-entering measurement the effort is arguing about: the worktree was already writable before
> `EnterWorktree`.** From the launch directory, `touch <worktree>/.probe-249` succeeded and the probe file was
> removed again. This is a `Bash` write to an absolute path; it is not a measurement of the `Edit` or `Write` tools,
> which were only used after entering. Note that this worktree's path was **not** in the sandbox write-allowlist
> printed in this worker's own system prompt (which named the `229`, `188`, `250`, `166` and `agent-ad9a496d`
> worktrees but not `249`), so **the allowlist as printed does not predict the result.** `EnterWorktree` was called
> anyway, as instructed. `ExitWorktree` was not called.

**The manager's own note beside it:** this is the second worker to report writing a worktree it had not entered, and
the first to report that the printed allowlist did not predict it. Node 250's worker reported the same from the
repository root. Both bear on node 250's raise and neither is the manager's to settle.

## Retrospective

*This effort's own standing instruction, carried in the spawn and shipped nowhere. Pasted as the worker wrote it.*

1. **What I had to hunt for.** Only one thing, and it took two reads. The *current* home of both pointer targets: `map.md`'s line 5 names `map-manager-only.md` as holding the landing policy and its line 94 names it for the worktree route, so the answer was in the first mandatory read — but line 7, three lines earlier, says the landing policy "left that file at node 188" while talking about `map-implementation-rules.md`, which states where it left *from* and not where it went. I read line 7 first and had to keep going. Everything else was where the node file said. The `decisions.md` grep on `worktree` (the spawn's declared subject) returned thirteen lines and contributed nothing the map had not already said.

2. **What arrived that this node did not need.** Three specific things.
   - **`map.md` read whole for four lines.** Of ~110 lines I acted on four. The rest is standing preferences about question batching, flag settlement, payload timing, resume policy, the never-delete rule, the plugin dependency and the checker's rule sources — none of which bears on editing two comments in `.gitignore`. I am not claiming they should not have been read: the never-delete rule in particular is what stopped me wondering whether to delete rather than replace a pointer. The arrangement that would have helped is narrower: **a line in `map.md` saying where each of the three split-out files' major sections now live** — one pointer table rather than three paragraphs each stating one half of one move.
   - **`map-manager-only.md` opened whole, 177 lines, for two headings.** I needed to confirm two strings exist. What came with them was the entire landing lifecycle, the sandbox measurements, the frontier order, the fog and the out-of-scope section. A `grep` for the two strings would have confirmed clause 2 at a fraction of the cost — and in fact the `grep` is what produced the final confirmation, run *after* the full read. The one thing the full read bought that the grep would not have is the inside/outside contradiction reported above, which is a real return but an accidental one.
   - **The retrospective's four questions arrived twice**, once in the spawn at length and once in `map.md`, which also carries the superseded two-question form struck through and the two manager duties that come with them. The spawn already carries the live form; `map.md`'s copy is what a worker does not need to read.

3. **What would have made this easier.** Two things, both cheap.
   - **The node file could have named the two current homes.** The question states where each pointer's target *left from* but the condition deliberately makes the worker find and confirm them, which is right — the confirmation duty is the point of this node. What was missing is nothing; this node was well specified. The spawn's warning that `map.md` moved two commits ago was the single most useful sentence in it.
   - **The spawn's instruction to confirm the pointers by opening the files collides quietly with `map.md`'s statement that `map-manager-only.md` is "a part of this map that no worker reads".** A worker that takes that statement as a prohibition cannot discharge clause 2, since that file is the only one holding either target. It is not a real contradiction — the statement describes what the split is for, not a rule — but I spent a moment deciding that. A word in `map.md` saying the manager-only file is not *forbidden* to a worker, merely not on its read list, would close it.

4. **What was stale, wrong, or contradictory.**
   - **The two `.gitignore` comments**, which is the node's own subject, and both were as described.
   - **`map-manager-only.md`'s landing-policy paragraph contradicts itself** on inside/outside the repository — reported as a new node above — **and on the worktree's path**, which is already node 237's. Two contradictions in one paragraph, and neither is marked.
   - **`map.md`'s gate-payload preference (the diff command goes) and `map-manager-only.md`'s landing policy (the gate payload names the command that shows its diff) state opposite rules**, the first saying the second is reversed and that node 231 will carry it. `map.md` says the manager stops emitting the command "until that lands", so this is a known in-flight difference rather than an unmarked one — but the landing-policy paragraph carries no marker, and a manager reading only `map-manager-only.md` would follow the reversed rule.
   - **Line numbers decay, demonstrated by this very change.** `git check-ignore -v` reported `.claude/worktrees/x` matching `.gitignore:10` in the main tree and `.gitignore:11` in the worktree, because the first comment grew by one line. That is standing rule 4's stated reason, observed live.

## The manager's disposal of the retrospective's record items

*Not the worker's text. Each item naming the record, and what the manager did with it.*

- **The landing policy's inside/outside contradiction** → minted as [node 254](254-the-landing-policy-says-the-worktree-is-outside-and-inside-the-repository.md), **carrying no acceptance condition**, the worker having written none and said why. The manager has not supplied one and has said so to the human.
- **The landing policy carrying no marker against `map.md`'s reversal of the diff-command rule** → **not minted.** [Node 231](231-a-gate-payload-stops-carrying-a-diff-command.md) is open and is the carriage; what this worker adds is that the *unmarked* paragraph misleads a manager reading only that file, which is a fact for whoever claims node 231 rather than a second node. Recorded here.
- **`map.md` stating where each split-out section left from rather than where it went** → **not minted.** It is the same item as [node 246](246-map-notes-mixes-what-a-worker-acts-on-with-what-a-manager-acts-on.md)'s at a different angle, and the manager cannot tell whether a pointer table is that node's business or its own; merging it in would widen an open node's subject, which is not the manager's to do. Named here as a candidate.
- **`map.md`'s "no worker reads `map-manager-only.md`" reading as a prohibition** → **not minted, and it is the one the manager thinks most likely to bite again.** Two agents have now had to decide whether they were permitted to open that file: this worker, and [node 243](243-a-worker-cannot-enter-its-worktree-by-the-route-the-spawn-names.md)'s, which flagged the same read as `243.3`. That is the effort's repeat threshold met, and the manager has not minted it because the repair is one word in `map.md`, a file that has just landed a change and that three open nodes edit. **Named for the human.**
- **The retrospective's four questions arriving twice** → **not minted.** The spawn's copy is the live one and `map.md`'s is the superseded form beside it; removing the duplicate is a `Change the map` on a paragraph the human's own standing instruction owns, and the manager does not edit that on its own judgement.
- **Line numbers decaying, observed live** → **nothing owed.** It is standing rule 4's own stated ground, confirmed rather than discovered.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text, the bar as properties, the changed path, the record-as-work rule, and this effort's ground rules and four
standing rules for writing copied as text, and was given nothing from this node or from the effort's record. It was
told clause 2 was the one needing work from it, and that the worker's report was not its evidence.*

PASS

**Working directory:** the worktree, entered by `EnterWorktree` with that absolute path, from
`.scratch/graph-workflow/nodes`; `pwd` after entry confirms it. Branch
`worktree-249-gitignore-comments-point-at-moved-files`, `HEAD` `f22dd5c`.

**Standards.** Read `map-implementation-rules.md` and nothing else in the effort's directory for standards. Standards named there: `/coding-principles`, `/naming`, `CONTEXT.md`'s `_Avoid_` lines, the effort's ground rules and four standing rules for writing, `graph-conventions.md`, `/writing-for-agents`. It states plainly that **no reviewing skill is named for this repo and a checker does not go looking for one**, so I invoked none and left none unrun by choice. Of those standards, the one that bore on this work is standing rule 4 (cite by heading or quoted phrase, never by line number); `CONTEXT.md`'s `_Avoid_` lines and `/writing-for-agents` I checked against the added text and neither bites. The rules file's rule at "An implementation node's work on this effort may be the effort's own record" required me to say so: **I read the changed paths I was given as the work under check.** Here the single changed path is `.gitignore`, not a record file, so that rule's `FAIL` trigger does not fire. No standard moved under this check.

The condition records no enumerator command, so there was none to re-run.

**Acceptance condition, clause by clause.**

1. Met. Unwrapped `.gitignore` into one unbroken line and grepped both forbidden strings: `0` hits each. The diff shows both old pointer sentences removed.
2. Met, established against the files as they now stand rather than from the handover. Both comments now name `.scratch/graph-workflow/map-manager-only.md`, which exists at that path relative to the repository root where `.gitignore` sits. Searching that file's unwrapped text: `Landing an implementation node's work` occurs once, as a `##` heading whose body opens `**Landing policy**, which binds this map too…` — the landing material the first comment sends its reader to. `How the worktree is made` occurs once, as the bolded lead-in followed by the bullets describing the `EnterWorktree`-then-reset route — the content the second comment sends its reader to. It is a bolded section lead-in rather than a `#`-prefixed heading, which clause 3 permits since it is cited as a quoted phrase. The main checkout's copy of `map-manager-only.md` is identical (unmodified against the same `f22dd5c`) and carries both, so the pointers resolve for a reader standing at the repository root as well.
3. Met. Both pointers cite by quoted phrase; a grep for any line-number form over `.gitignore` returns nothing.
4. Met. `.worktrees/` and `.claude/worktrees/` appear in the diff as unchanged context lines.
5. Met. The diff is 2 deletions, 3 insertions, and the deletions are exactly the two pointer-bearing comment lines. Comparing unwrapped old against unwrapped new, the only text that left is the stale location — `map.md, the landing policy` and `map-implementation-rules.md` — and `committed.` from the first deleted line is carried into its replacement. The second comment's retained sentence `The entry above is the path the landing policy used when the manager created worktrees by hand.` is intact. The reflow of the first comment onto two lines moves no words.
6. Met. `git status --porcelain` in the worktree returns exactly ` M .gitignore`; `--untracked-files=all` adds nothing; `git diff --stat HEAD` reports `.gitignore | 5 +++--` and no other path. No node file, `decisions.md` or `flags.md` is among the changed paths. (The main checkout has unrelated modifications under `.scratch/`, but it is a different working tree at the same commit and is not the work under check.)
7. Met — see the bar below.

**The bar.** Discovered from the repository itself rather than assumed: the root holds only `.claude/`, `CONTEXT.md`, `.gitignore` and `.scratch/`. There is no manifest, no task runner, no `Makefile`/`justfile`, no `.github/` and no CI configuration; the one ignore file invokes nothing. So this repo has no build, no tests and no formatter, and the bar's command half is vacuously satisfied — a complete bar, not a deficient one, which is also what the rules file records from its own first discovery. On its non-command half: the change introduces no refused vocabulary, cites by quoted phrase as standing rule 4 demands, adds no assumption about this repo, machine or toolchain, addresses no human, and the file is clean (no trailing whitespace, terminating newline present).

**No questions, and no part of the condition left uncovered.**

### Gate — `approve`

**The human's answer**, `verbatim`: *"approve"*

Landed under the effort's landing policy: one path-limited commit of `.gitignore` in the node's worktree, no rebase
needed (the worktree's base and the manager's `HEAD` were both `f22dd5c`), the bar's command half empty so nothing
to re-run, `git merge --ff-only` onto `master`, worktree removed and branch deleted. Commit `19df459`, carrying the
trailer `Node: graph-workflow/249`.

**The one flag this node held is settled by this approval.**

**Two more landing measurements for [node 251](251-the-managers-own-session-cannot-write-parts-of-the-record.md).**
The path-limited commit succeeded sandboxed. `git merge --ff-only` failed sandboxed with `unable to unlink old
'.gitignore': Read-only file system` and **failed atomically**, `HEAD` not moving; it succeeded with the sandbox
off. That is the third landing in a row where the commit is sandbox-clean and the merge is not, and the third where
the merge's failure is atomic. **The pattern is now three for three and the cause is constant**: the merge writes
paths outside the manager's writable region, and which paths those are has varied — `.scratch/graph-workflow/`,
`.claude/skills/`, and now the repository root.
