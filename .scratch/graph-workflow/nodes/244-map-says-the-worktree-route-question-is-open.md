# `map.md` says the worktree-route question is open, names two routes, and states a constraint the landed practice contradicts

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 241](241-two-record-defects-needing-a-decision-before-repair.md)'s worker, and pasted as it wrote
it.*

> `map.md`'s paragraph beginning `**A worktree is created by the harness, never by hand.**` ends with a sentence
> that is wrong three times over, and it is live rule-stating text that every worker reads cold. It says the route
> question *"is open and is [node 150]"* — node 150 is resolved. It offers *"the manager entering, or an isolated
> worker"* as the two candidates — the route in force is a third, the human's own, and the isolated-worker route it
> would send a reader toward is the one that was superseded. And it states that *"the manager must stay in the main
> tree to own the graph"* — the landed practice has the manager enter the worktree transiently to create it and
> bring it to the right base, and return. A worker reading `map.md` cold today is told a settled thing is unsettled
> and pointed at a losing option.
>
> **Interaction the worker must know about, stated rather than left to be discovered:** [Where the harness-worktree
> standing instruction lives](152-where-the-harness-worktree-instruction-lives.md) is open and its condition
> requires this same paragraph to move *byte-identical* into another file. That condition is already annotated on
> its own node as unsatisfiable as written, node 188 having moved its destination section to a third file. This node
> makes it no more unsatisfiable than it already is, but the two must not be worked concurrently.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 241's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map.md` and `.scratch/graph-workflow/map-history.md`, and no
> other file may be edited. The worker may not mark this node, resolve it, or write a line in
> `decisions.md` or `flags.md`.
>
> Done means every one of the following is true of the finished tree.
>
> 1. In `.scratch/graph-workflow/map.md`, the paragraph beginning `**A worktree is created by the
>    harness, never by hand.**` contains none of the phrases `is open and is`, `the manager entering, or
>    an isolated worker`, or `the manager must stay in the main tree`, and describes the choice of
>    harness route nowhere as open, unsettled, or undecided by the manager.
> 2. That paragraph states, in wording the worker chooses, the route in force: the manager calls
>    `EnterWorktree` with a name tied to the node, checks the base the worktree landed on, and
>    `git reset --hard`es it to the manager's own `HEAD` before any worker reads the tree. It states that
>    the manager works from the main tree and enters the worktree only to create it and bring it to that
>    base.
> 3. That paragraph names `map-manager-only.md` as where that route is stated in full, by a markdown
>    link, and restates no more of the route than clause 2 requires — no sandbox measurement, no branch
>    or path naming, no account of what was measured.
> 4. The paragraph's first sentence, beginning `**A worktree is created by the harness, never by hand.**`
>    and ending with the closing quotation mark of the human's quoted instruction *"…that way you don't
>    have all these worktree management issues afterwards"*, is byte-identical to what it was before this
>    work.
> 5. Every sentence of that paragraph which this work removes or rewords is appended **verbatim** to
>    `.scratch/graph-workflow/map-history.md`, under a new `##` heading naming `map.md` and the section
>    the text came from, in the form the headings already in that file take. Any struck-through text
>    stays struck through. No character of the appended text differs from what `map.md` held.
> 6. Nothing else in `map.md` changes: no other paragraph gains, loses or reorders text, and the file
>    holds exactly the `##` headings `## Destination`, `## Notes` and `## Decisions so far`.
> 7. Nothing already in `map-history.md` is edited, reordered or removed; the append is the only change
>    to it.
> 8. Every markdown link in the edited paragraph resolves to a file that exists.
> 9. No file other than the two named above is modified.
> 10. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node and [node 243](243-a-worker-cannot-enter-its-worktree-by-the-route-the-spawn-names.md) touch the same
subject from opposite ends.** Node 243 asks how a *worker* reaches the worktree the manager made, which is undecided;
this node repairs `map.md`'s account of how the *manager* makes it, which is settled. Neither blocks the other, and
this node's clause 2 restates only what node 150 already settled.

**The manager has written no blocking edge to [node
152](152-where-the-harness-worktree-instruction-lives.md)**, following the surfacing worker's own account that the
two must not be worked concurrently rather than in a fixed order. The manager holds that sequencing.

## Flags

`244.1` **· settled** `ASSUMPTION` — Clause 3 of the acceptance condition forbids the paragraph to restate "no sandbox
measurement", and the paragraph already contained one that this work did not introduce — the `EBUSY` account of why
`git worktree remove` and `git worktree prune` fail on a hand-made worktree. I read clause 3's ban as scoped to the
restatement of the route, its three items being exactly what `map-manager-only.md`'s route bullet holds beyond
clause 2, and left the `EBUSY` sentence untouched. Node 191's admission test, which binds whoever edits a passage,
points the same way: an error string and a symptom are a trigger and a trigger stays. The alternative was to remove
and bank it under clause 5, which clause 5 permits but no clause requires; I judged the removal unwarranted and a
loss of the ground for the rule the paragraph states. Not raised, because the condition is satisfiable under either
reading and I hold a recommendation I believe.

`244.2` **· settled** `ASSUMPTION` — ***Filed by the manager***, this being a departure the worker reported in its gate payload
rather than as a flag of its own. Its words, `verbatim`: *"`graph-conventions.md`'s `Change the map` says to append
the account first and replace the item second, so a run that dies leaves the text banked. I did the two in the
opposite order. Both landed and the finished tree is identical to the one the stated order produces."* The manager's
own note beside it: the procedure's stated ground is what a dying run leaves behind, so the risk was taken and did
not fire rather than being absent.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text, the bar as properties, the changed paths, the record-as-work rule, and this effort's ground rules and four
standing rules for writing copied as text, and was given nothing from this node or from the effort's record.*

PASS

**I read the changed paths as the work under check**, per the implementation-rules file's rule that an implementation node's work on this effort may be the effort's own record: I held `map.md` and `map-history.md` against the acceptance condition and the standards exactly as I would hold product code, and derived no statement of intent from their content — the acceptance condition was my only statement of intent.

**Standards I read, and which bore.** I read `map-implementation-rules.md` and nothing else in the effort's directory beyond the work. Standards it names: `/coding-principles`, `/naming`, `CONTEXT.md`'s `_Avoid_` lines, this effort's ground rules and its four standing rules for writing, `graph-conventions.md`, `/writing-for-agents`. Bore on this work: `/writing-for-agents`, the four standing rules for writing, `graph-conventions.md`'s `## Writing the map` and `### Change the map`, `CONTEXT.md`'s `_Avoid_` lines, ground rules 3-5. Did not bite: `/coding-principles`, `/naming` (no code, no new identifier), ground rules 1-2 (nothing shipped). **No reviewing skill is named for this repo**, so I ran none and went looking for none; I invoked `/writing-for-agents` directly and held the prose against it by hand — no part of it was delegated to an agent, so the blindness question did not arise.

**No standard moved under this check.** I settled that first: the changed paths are `map.md` and `map-history.md`; the standards live in `map-implementation-rules.md`, `CONTEXT.md`, `graph-conventions.md` and the two skills, none of which changed (`git diff --name-only 23eb355` returns exactly the two work paths). `map.md`'s standing preferences are explicitly not among the standards, so the edited paragraph is work and not a standard.

The acceptance condition records no enumerator command, so there was none to run.

**How I established each part** (all comparisons made on unwrapped text; both files are one-line-per-paragraph, so the paragraph diffs are whole-item):

1. Extracted the paragraph from the new `map.md` and searched the unwrapped text: `is open and is`, `the manager entering, or an isolated worker`, `the manager must stay in the main tree` — all absent. `open`, `unsettled`, `undecided`, `not settled`, `has decided none` — all absent from the paragraph. It now opens the sentence with `**The route is settled, and it is the human's own:**`.
2. The new sentence states each element: `EnterWorktree` with a name tied to the node; checks the base the worktree landed on; `git reset --hard`es it to the manager's own `HEAD` before any worker reads the tree; the manager works from the main tree and enters the worktree only to create it and bring it to that base. All five present.
3. `[map-manager-only.md](map-manager-only.md)` is the markdown link, introduced as "The route is stated in full in". The new text adds no sandbox measurement, no branch name, no path, no account of what was measured — only the settled-ness, the route steps clause 2 demands, and the node-150 citation. **The reading I took, stated so the manager can see it:** clause 3 caps what the paragraph *restates of the route*. The paragraph still carries its pre-existing sentence beginning `**What went wrong is measured rather than argued:**`, which holds a sandbox measurement (`.git/config` read-only, `EBUSY`) — that sentence is the ground for "by the harness, never by hand", not a statement of which harness route is in force, and it is byte-unchanged by this work. On the wider reading (no sandbox measurement anywhere in the paragraph) clause 3 would not be met and clause 5 would also bite, since that sentence was not appended to history. I took the narrower reading because clause 1 enumerates the exact phrases that must go and every one is from the closing sentence, and because clauses 4-6 are built for a minimal edit.
4. Byte-compared old and new paragraph: common prefix is 898 bytes; the human's quoted instruction closes at offset 345, and `old[:345] == new[:345]` exactly. Nothing before the changed sentence moved.
5. The removed sentence is 522 bytes; the blockquote line appended to `map-history.md`, with its `> ` marker stripped, is 522 bytes and compares byte-identical. No strike-through was present, so none to preserve. The heading names `map.md` and `## Notes`, and matches the form already in the file. I confirmed the paragraph does sit under `## Notes` in `map.md`.
6. The diff for `map.md` is one line changed, zero other hunks. `map.md`'s `##` headings are exactly `## Destination`, `## Notes`, `## Decisions so far`.
7. `map-history.md`'s new content starts with the old content byte-for-byte (`new.startswith(old)` is true); 1610 bytes appended, zero deleted.
8. The three links in the edited paragraph — `nodes/93-effort-scoped-custom-rules.md`, `map-manager-only.md`, `nodes/150-which-harness-route-creates-a-worktree.md` — all resolve to existing files. (The two links in the appended history block also resolve.)
9. `git status --porcelain` in the worktree returns exactly the two files, modified, with nothing untracked. `decisions.md`, `flags.md` and any node file are unmodified there, and no node status line was touched. Bound on this: I establish it over the worktree I was given. The manager's main tree carries its own unrelated modifications, which are outside the paths I was given and which nothing I can read attributes to this work.
10. The bar — see below.

**The bar.** Discovered from the repository rather than assumed: the root holds only `.claude`, `CONTEXT.md`, `.gitignore` and `.scratch`. No manifest, no task runner, no `.github`, no formatter config; `.gitignore` invokes nothing. So the bar's command half is empty — a complete bar, not a deficient one — and the bar is its non-command half.

- `git diff --check` → no whitespace errors; both files end in a newline.
- `/writing-for-agents`: the replacement is positive ("The route is settled") rather than a prohibition, carries no no-op, and moves the account out of the working file and behind the heading in `map-history.md`, which is the disclosure move the standard wants. The bounded restatement plus the link to `map-manager-only.md` is a cache of an expensive lookup, not duplication of a cheap one.
- Four standing rules for writing: why is compressed and the shape (the route's steps) is not; the item states its current form and cites node 150 by markdown link; the history entry is navigable by its own `##` heading; every citation is by heading or quoted phrase, and no line number appears anywhere in either change.
- Ground rules: nothing in the change addresses the human (rule 3); the prose is short and reversible (rule 4); rule 5 discharged above. Rules 1-2 concern shipped files and this is not one.
- `CONTEXT.md`'s `_Avoid_` lines, checked by hand rather than by grep per the rules file's measured trap: the only refused word appearing is `question`, in the history block's "it called the route question open" — which the rules file names explicitly as one of the ordinary-English false positives. Nothing else on the lists appears.
- `graph-conventions.md`'s `### Change the map` is followed exactly: verbatim append to `map-history.md` under a heading mirroring the map section, then replacement in `map.md` citing the shaping node by markdown link.

**Reported, not a finding** — `graph-conventions.md`'s mechanical check 10 reports and never fails: the edited `## Notes` item is **1285 bytes** of its own prose, excluding the human's quoted words (1463 total), up from **1244** before this change, against the 500-byte target. Twelve items in `## Notes` are currently over the target. The convention states in as many words that an item over it is a number to look at and not a defect, so I record the number and raise nothing on it.

**What this run handed back alongside its outcome.** No question. **No part of the condition was left uncovered.** Its clause-3 reading is the same one the worker took at flag `244.1`, reached independently and from the other side.

## Retrospective

*This effort's own standing instruction, carried in the spawn and shipped nowhere. Pasted as the worker wrote it.*

1. **What I had to hunt for.** The heading form `map-history.md` uses for a single superseded item: I looked first at that file's own `## How to read it` preamble, which states the mirroring rule but gives no shape for a one-item bank, and found the form by `grep '^## '` over the file. Second, whether node 244's own file exists in the worktree — it does not, the worktree being cut at a commit older than the node, so a markdown link to it would dangle. I discovered that only after drafting the link, by listing `nodes/`. Nothing in the spawn, the node file or the record says a worker's worktree predates its own node file; that is a general fact about every worker on this effort and it is written nowhere.

2. **What arrived and bore on nothing.** Three whole-file reads for a fraction each. `CONTEXT.md`: I went for the `_Avoid_` lines and took all 51 entries; the refusals I actually needed were four, and a gathered refusal list — or the rules file naming the distinctive ones it already says are checked by hand — would have replaced the read. `decisions.md`, read whole at 152 lines: I used three lines about node 150's supersession, and `map.md` had already told me node 150 was resolved, so the file confirmed rather than informed. `map-manager-only.md`, read whole at 176 lines: I needed one bullet, *"How the worktree is made"*, and the spawn could have named that heading. In `map.md` itself — a mandatory whole-file read — the items on retrospectives, flag settlement, question batching, resumed attempts, payload timing and token priority bore on nothing in this node; that is the file's design rather than a defect, but it is where most of my read went. From the spawn, nothing was waste: the `EnterWorktree` warning stopped me spending three calls on a refusal I would have earned, and the manager's note on the base check firing twice this session is what let me judge clause 2's wording true rather than assume it.

3. **What would have made this node easier.** In the spawn: name `map-manager-only.md`'s *"How the worktree is made"* bullet as where the route in force is stated, since clause 3 requires pointing at that file and clause 2 requires restating its first two facts — I had to read the file whole to find them. Also say that the worktree's `nodes/` directory sits at the base commit and therefore lacks this node's own file. In the node file: clause 3's *"no sandbox measurement"* does not say whose scope it has, and it reads as reaching the whole paragraph while meaning the route restatement; one clause of scope there would have removed the flag below. In the record: `map-history.md` states how to read it but not how to write one entry, and every worker that banks a passage re-derives the heading form by grep.

4. **What was stale, wrong, or contradictory.** The paragraph this node repaired, as diagnosed. `.gitignore`'s two pointers, reported as a new node above. And one apparent contradiction that is not one: the condition's clause 2 requires the paragraph to say the manager *enters* the worktree to bring it to its base, while `map-manager-only.md` records, measured, that *"the manager needs `EnterWorktree` for neither the base check nor the reset"* and *"the manager's own session never has to leave the main tree"*. Both hold — calling `EnterWorktree` is itself the entry, and the check and the reset can then be run on the tree from outside it — so I wrote the sentence to be true under both readings rather than raise. A reader meeting clause 2 alone would not know that.

I have no view of my own token usage and estimate none. On node 212's duty to name and count a standing item: **whole-file reads for one fact** is the item I would name — three of them this node, `CONTEXT.md`, `decisions.md` and `map-manager-only.md` — but I hold no earlier retrospective and so cannot count its repeats; the manager has the count.

## The manager's disposal of the retrospective's record items

*Not the worker's text. Each item naming the record, and what the manager did with it.*

- **`.gitignore`'s two stale pointers** → minted as [node 249](249-gitignores-two-comments-point-at-files-that-moved.md), carrying this worker's own acceptance condition. **Not a duplicate mint in the manager's judgement**, though [node 227](227-gitignore-cites-a-quoted-phrase-that-resolves-to-nothing.md) already covers one of the two comments; both nodes' manager notes now name the other.
- **A worker's worktree predating its own node file** → **not minted, and this is why**: the fix is a sentence in the manager's spawn, which the manager has changed in its own conduct and which reaches no file. It is recorded here because the next worker to bank a link to its own node will meet it.
- **`map-history.md` stating how to read it but not how to write one entry** → **not minted.** Two workers have now re-derived the heading form by grep, which under this effort's own repeat rule is the threshold — but the manager cannot tell from what it holds whether the second instance is the same item or a different one, and minting on a miscount is the failure flag `160.2` already records against it. Named here as a candidate rather than settled.
- **`CONTEXT.md` read whole for four refusals, and `decisions.md` read whole for three lines** → **not minted.** [Node 165](165-measure-whether-a-fed-file-earns-its-place.md) is open and exists to measure exactly this; these are two more data for it. The manager has added nothing to that node.
- **`map.md` read whole with most of `## Notes` bearing on nothing** → **already minted**, as [node 246](246-map-notes-mixes-what-a-worker-acts-on-with-what-a-manager-acts-on.md). This is the **sixth** report of the item.
- **The worker's count question — "the manager has the count"** → answered here rather than left: on *whole-file reads for one fact*, this session alone holds four reports, from nodes 112, 235, 241 and 244. It is the most-reported item the effort has.

### Gate — `approve`

**The human's answer**, `verbatim`: *"approve"*

Landed under the effort's landing policy: one path-limited commit of `.scratch/graph-workflow/map.md` and
`map-history.md` in the node's worktree, no rebase needed (the worktree's base and the manager's `HEAD` were both
`23eb355`), the bar's command half empty so nothing to re-run, `git merge --ff-only` onto `master`, worktree removed
and branch deleted. Commit `b988d01`, carrying the trailer `Node: graph-workflow/244`.

**The two flags this node held are settled by this approval**, under the human's standing instruction that approving
a node's end settles its flags.

**Three measurements the landing produced, banked here because [node
251](251-the-managers-own-session-cannot-write-parts-of-the-record.md) is the node that owns them.** The manager ran
each step sandboxed first rather than assuming.

1. **The path-limited commit inside the worktree succeeded sandboxed.** No override was needed.
2. **`git merge --ff-only` in the main tree failed sandboxed**, with `unable to unlink old
   '.scratch/graph-workflow/map-history.md': Read-only file system` and the same for `map.md`. **It failed
   atomically** — `HEAD` did not move, no `MERGE_HEAD` was written, and nothing partial was left behind. It
   succeeded with the sandbox off. The cause is the one node 243's worker measured: the writable region is
   `.scratch/graph-workflow/nodes`, and these two files sit outside it.
3. **`git worktree remove` failed sandboxed** and then failed again unsandboxed, reporting *"contains modified or
   untracked files"*. The tree's `git status` showed exactly one entry, `` D .claude/rules/expedition-triggers.md``
   — **a sandbox overlay artifact rather than a deletion by anyone**: `.claude/rules/` does not exist inside a
   harness worktree at all, while the main tree's copy is present, unmodified and committed at 1,190 bytes. The
   manager verified that before using `--force`. **A worker never sees `.claude/rules/`**, which is consistent with
   that file being the manager's alone, and is worth knowing for any node whose condition quantifies over the tree.
