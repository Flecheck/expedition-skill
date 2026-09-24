# Ignore the new worktree path

Type: implementation
Status: resolved

Blocked by: none

## Question

*Surfaced by [node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md)'s worker, and pasted as it
wrote it.*

> Worktrees now live at `.scratch/graph-workflow/worktrees/`, which is inside a tracked directory and is not ignored
> — confirmed by `git check-ignore -v .scratch/graph-workflow/worktrees/x` exiting 1. Left as is, every
> implementation node puts a second copy of the whole record where `git status` and every repo-wide search will find
> it.

**Blockers, in the worker's words:** *"none. It can run alongside node 1, editing a different file."* — *"node 1"*
being [node 268](268-carry-the-plain-git-worktree-route-into-the-map.md), the other node that handover surfaced.

## Acceptance condition

*Written by node 265's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.gitignore` at the repository root, and no other file may be edited. The worker may not mark this
> node, resolve it, or write a line in `decisions.md` or `flags.md`. Done means every one of the following is true of
> the finished tree.
>
> 1. `git check-ignore -v .scratch/graph-workflow/worktrees/probe` exits 0 and names `.gitignore` as the source of
>    the match; the worker runs this command and reports its output in its handover.
> 2. The new pattern carries a comment block stating what the directory holds — one git worktree per claimed
>    implementation node, created with plain `git worktree add`, placed inside the repository so that a review can
>    see the diff — and citing `.scratch/graph-workflow/map-manager-only.md` together with the quoted phrase `How the
>    worktree is made` as where the route is stated. The worker confirms that pointer by opening that file and
>    finding that phrase, and reports in its handover that it did.
> 3. No pointer in `.gitignore` cites a target by line number.
> 4. The patterns `.worktrees/` and `.claude/worktrees/` are both still present and unchanged, and neither of their
>    comment blocks loses information.
> 5. No file other than `.gitignore` is modified.
> 6. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node is urgent in a way its author could not know.** It was minted *after* the manager had already begun
using the new route. **This node's own worktree is the first ever made by it**, and it sits at
`.scratch/graph-workflow/worktrees/269-ignore-the-new-worktree-path` — untracked and unignored, which is precisely
the pollution the condition describes. **The worker will see its own worktree in `git status` while working**, which
is evidence rather than a problem.

**Clause 2's pointer is one clause 6 of [node
268](268-carry-the-plain-git-worktree-route-into-the-map.md) is required to preserve.** Node 268 rewrites the
section this node's comment cites, and its own condition holds the quoted phrase `How the worktree is made` in place
for exactly this reason. The two nodes are safe to run together on that account, and they touch different files.

**The two existing patterns clause 4 protects were last repaired at [node
249](249-gitignores-two-comments-point-at-files-that-moved.md)**, whose whole subject was those comments pointing at
files that had moved. Losing information from them would undo landed work.

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> `.gitignore` at the repository root gains one pattern, `.scratch/graph-workflow/worktrees/`, appended below the
> two existing worktree patterns with a comment block of its own. Neither existing pattern nor either existing
> comment was touched.
>
> The added block reads:
>
> ```
> # The current path. It holds one git worktree per claimed implementation node,
> # created with plain `git worktree add` rather than by the harness, and placed
> # inside the repository so that a review can see the diff. Ignored so those
> # worktrees are never committed. The two entries above are the paths used by the
> # earlier routes.
> # See .scratch/graph-workflow/map-manager-only.md, "How the worktree is made".
> .scratch/graph-workflow/worktrees/
> ```
>
> **The measurements the condition demands, as the commands printed them.** Clause 1, run in the node's worktree
> after the edit:
>
> ```
> $ git check-ignore -v .scratch/graph-workflow/worktrees/probe
> .gitignore:19:.scratch/graph-workflow/worktrees/	.scratch/graph-workflow/worktrees/probe
> exit=0
> ```
>
> `.gitignore` is named as the source of the match and the exit status is 0. Clause 2's pointer was confirmed by
> opening `map-manager-only.md` and finding the phrase `How the worktree is made` in it, **in the live record and in
> the worktree's own copy alike** — both hold it, so the citation resolves whichever copy a reader opens. Clause 4
> was measured rather than asserted: after the edit `git check-ignore -v .worktrees/x .claude/worktrees/x` still
> reports both patterns at their own lines, and **both comment blocks are byte-identical to what node 249 left**.
> Clause 5 is `git status --porcelain` returning exactly ` M .gitignore`.
>
> **Three calls inside the work.** The new block was **appended** rather than placed above the two older patterns:
> clause 4 protects those comments, and the second of them says *"The entry above is the path the landing policy used
> when the manager created worktrees by hand"* — a sentence that points upward and would have been falsified by
> reordering. **The new comment carries one line the condition did not ask for**, *"The two entries above are the
> paths used by the earlier routes"*, because after this change three patterns sit in the file and nothing else says
> which one is live; it adds information to the file and removes none from either protected block. And **the new
> block cites the same quoted phrase the `.claude/worktrees/` block already cites**, which clause 2 requires; the two
> pointers now name one target, which is what node 268's clause 6 holds in place.
>
> **The route this worktree was made by.** This node's worktree is the first ever made by the plain `git worktree
> add` route, and it behaved. Every write and every command went to the tree by absolute path; no harness tool was
> called, no sandbox override was needed, and nothing was refused. The record directory does appear twice, as the
> spawn warned — the copy at the worktree's own root is the one edited.
>
> **The bar.** Confirmed against the repo rather than the record: the worktree root holds no manifest, no task
> runner, no CI directory, and one ignore file, `.gitignore`, which invokes nothing. No build, no tests, no
> formatter. The bar's command half is empty and therefore complete, and the record in `map-implementation-rules.md`
> agrees with what the repo says.

**The index line the worker wrote**, held here until the node resolves:

> `.gitignore` gains `.scratch/graph-workflow/worktrees/` with a comment naming the plain-`git worktree add` route
> and citing `map-manager-only.md`'s `How the worktree is made`; the two older patterns are untouched.

## Flags

`269.1` `ASSUMPTION` — *The worker's own text, pasted.*

> The condition fixes what the new comment must say but not where the pattern goes or how the now-three patterns
> relate to each other. I appended below the two existing entries and added one sentence marking the new path as the
> current one and the two above it as earlier routes. Ground: clause 4 forbids losing information from the protected
> comments, and the `.claude/worktrees/` comment contains an upward reference (*"The entry above…"*) that reordering
> would falsify; meanwhile a file listing three worktree paths with no indication which is live is a trap for the
> next reader. Adding a sentence satisfies both. **If the human would rather the file not editorialise about entries
> the condition told me to leave alone, that sentence is the one to cut**, and nothing else in the block depends on
> it.

## Invalidations

*The worker's own text, pasted.*

> `map-implementation-rules.md`'s bar section holds the statement that `.gitignore` *"ignores `.worktrees/` and
> `.claude/worktrees/`, the second added at node 158"*. That statement was an exhaustive account of the file and
> stops being one when this work lands — three patterns, two named. It is the record of node 158's edit rather than
> node 158's own answer, and the repair is the node surfaced above.
>
> Nothing else. In particular, node 150 — which settled `EnterWorktree` as the route — is contradicted by the new
> comment's text, but it was already contradicted by the human's decision at node 265 before this node was minted,
> and node 268 carries that reversal into the map. **This work records the consequence; it does not create it.**

## Retrospective

*The worker's own text, pasted.*

> 1. **What I had to hunt for.** Almost nothing, and the spawn is why. The one real hunt was whether the
>    record-repair I wanted to surface was already node 268's: I found it by opening node 268's file and reading its
>    clause 7, which names the three files it may edit. I looked there first and it answered. The bar's commands took
>    one `ls` at the worktree root. Clause 2's phrase took one grep.
> 2. **What arrived that this node did not need.** Most of `map.md`. This node edits one file by adding six comment
>    lines and one pattern; what bore on it was the retrospective's four questions and nothing else. The question
>    queue, the payload-release trigger, the code-slot and grilling counts, the token scarcity and
>    heterogeneous-harness material, the glossary's entry counts, the moved-standard licence, the flags-settle-at-
>    close rule — none of it could change a character of the work. **The four standing writing rules do bind me and
>    they are not in `map.md` at all**; `map.md` only points at them. So the whole-file read bought one bullet.
>    `map-implementation-rules.md`'s review-route paragraph is written for the checker and I acted on none of it —
>    the spawn said so in advance and I read it anyway, because the contract says read the file. **The spawn reports
>    two workers have already said this; I am the third.** From the contract, the raise procedure, the
>    correction-round section and the replacement-attempt section bore on nothing, which is the ordinary cost of a
>    contract that must cover every path. **The arrangement that would fix both:** give `map.md`'s retrospective
>    bullet its own heading so a spawn can point at it by name instead of a worker reading the file to find it, and
>    put a first line on the review-route paragraph saying *the checker acts on this and the implementer does not* —
>    three workers have now paid for a paragraph that could exempt itself in eight words.
> 3. **What would have made this node easier.** Little. The spawn pre-empted every stale source before I reached it,
>    named the route, and told me which file not to grep — the `decisions.md` warning in particular saved a read that
>    would have been actively misleading. The one gap is in the **record**: nothing at `map-implementation-rules.md`'s
>    bar sentence says it is an enumeration that goes stale when `.gitignore` changes, so the only thing connecting
>    my edit to that sentence was my having read it for the bar minutes earlier. A node that edited `.gitignore`
>    without needing the bar's commands would have missed it entirely. **That is the second drift of that same
>    sentence.**
> 4. **What I read that was stale, wrong, or contradicted something else.** Three things, two of them already known.
>    `map.md`'s standing instruction *"A worktree is created by the harness, never by hand"* is reversed and is node
>    268's. `map-manager-only.md`'s `How the worktree is made` states the `EnterWorktree`-then-reset route in full
>    and is the same node's; I opened that file only for clause 2's phrase and did not read the section, as
>    instructed. The third is not yet anyone's and is the node I surfaced.

## The manager's disposal of the retrospective's record items

*Not the worker's text.*

- **`map-implementation-rules.md`'s enumeration of `.gitignore`** → **minted as [node
  271](271-the-rules-files-account-of-gitignore-names-two-patterns-where-there-are-three.md)**, carrying the
  worker's own question and condition.
- **The review-route paragraph read for nothing, now by three workers in three consecutive nodes** → **still not
  minted, and the manager is naming the cost rather than repeating the referral.** The worker's fix is eight words —
  a first line saying the checker acts on it and the implementer does not — and it is a smaller thing than [node
  246](246-map-notes-mixes-what-a-worker-acts-on-with-what-a-manager-acts-on.md)'s subject, which is why folding it
  there keeps failing. **Named for the human, third report.**
- **`map.md`'s retrospective bullet having no heading a spawn can point at** → **not minted**, and it is the same
  shape: every worker reads the whole file to find one bullet. Recorded as a candidate.
- **The spawn pre-empting stale sources, and the `decisions.md` warning in particular** → **nothing owed.** Recorded
  because it is the first spawn on this effort a worker has reported as having cost it nothing to read.

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text, the bar as properties, the one changed path and the tree holding it, the record-as-work rule, and this
effort's ground rules and four standing rules for writing copied as text. It was given nothing from this node or
from the effort's record. It was told clause 1's command was to be run rather than accepted, that clause 4's
"loses information" needed a comparison against the base rather than a reading for plausibility, and that
`map-manager-only.md` is stale on the worktree route.*

> **PASS**
>
> **I read the changed paths as the work under the implementation-rules file's record rule.** The single changed
> path is `.gitignore` at the repository root — not a record file. No node status line, no `decisions.md` line, no
> `flags.md` line appears among the work: `git status --porcelain=v1 --untracked-files=all --ignored=matching` in the
> worktree returns exactly ` M .gitignore` and nothing else.
>
> I reached the tree by absolute path and `git -C`. **I called no harness tool, did not use `EnterWorktree`, and did
> not disable the sandbox. No read was refused.**
>
> **1 — Met.** I ran it myself rather than accepting any report:
>
> ```
> .gitignore:19:.scratch/graph-workflow/worktrees/	.scratch/graph-workflow/worktrees/probe
> exit=0
> ```
>
> The source named is `.gitignore`. I confirmed no other exclude source could have produced it: `core.excludesFile`
> is unset and the common git dir's `info/exclude` holds no live patterns.
>
> **2 — Met.** The added block carries all three facts the clause enumerates. Its pointer reads `# See
> .scratch/graph-workflow/map-manager-only.md, "How the worktree is made".` I resolved that pointer myself, grepping
> unwrapped text so a wrapped phrase could not hide: the phrase occurs in the live `map-manager-only.md` **and** in
> the worktree's own copy, so the pointer resolves whichever copy a reader lands on. I opened that file only to
> resolve this pointer and read nothing else in it.
>
> **3 — Met.** All three pointers in the file cite by quoted phrase. A scan of the whole file for line-number forms
> returns nothing.
>
> **4 — Met, established against the base commit rather than by reading for plausibility.** The base `.gitignore`
> (602 bytes, from `git show 0402ab1:.gitignore`) is an **exact byte prefix** of the working file — `cmp` against
> `head -c 602 .gitignore` is silent. The diff is 8 insertions and 0 deletions. **Nothing inside either protected
> block moved, so neither can have lost information**; I also compared both blocks unwrapped, in case of a reflow,
> and they are identical word for word.
>
> **5 — Met.** Status returns only ` M .gitignore`. I ran it with `--ignored` deliberately: **the new pattern could
> in principle have hidden a stray file, and it hides none.** `git ls-files .scratch/graph-workflow/worktrees/`
> returns 0 tracked paths, so the new pattern shadows no tracked file either.
>
> **6 — The bar. Met.** Discovered from the repo rather than taken from any account: the repository root holds only
> `.claude/`, `CONTEXT.md`, `.gitignore`, `.scratch/` and `.worktrees/`. No manifest, no task runner, no CI
> directory, no formatter or linter config. No build, no tests, no formatter, no CI to invoke — a complete bar, not a
> deficient one. `map-implementation-rules.md` states in as many words that no reviewing skill is named for this repo
> and that a checker does not go looking for one, **so I ran none — no skill parts run, none left unrun.**
>
> Which bore on this work: **standing rule 4** (cite by heading or quoted phrase) is the one that bites and clause 3
> covers it; **rule 1**'s shapes are stated in full and the why compressed to one clause. **`CONTEXT.md`'s `_Avoid_`
> lines**, checked by hand per the measured trap: the one refused word appearing is **`review`** — refused under
> **Gate** as *"review (that is what the human does at the gate)"*. **The usage here *is* the human's review at the
> gate**, the licensed sense; it is the wording the acceptance condition itself dictates, and the pre-existing first
> block already uses it that way. **Not a finding.** `/coding-principles`, `/naming` and `graph-conventions.md` are
> effectively silent on a six-line comment block introducing no identifier and no new term. **Ground rules** 1 and 3
> are not reached — `.gitignore` invokes nothing and addresses nobody.
>
> ```
> NOT COVERED:
> - "the worker runs this command and reports its output in its handover" (clause 1) — I established the
>   command's behaviour myself and it is met. Whether the worker reported that output IN ITS HANDOVER is
>   held in material I was not given; I hold no handover.
> - "The worker confirms that pointer by opening that file and finding that phrase, and reports in its
>   handover that it did" (clause 2) — I confirmed the pointer resolves, so the substance stands. Whether
>   the worker did so and SAID SO in its handover is likewise outside what I was given.
> ```
>
> My `PASS` covers the state of the finished tree, which is the whole of clauses 1–6 as observable in it. **It does
> not cover what the handover says. Only whoever holds that handover can settle those two sub-parts.**
>
> **QUESTION.** The condition forbids editing any file but `.gitignore`, and complying leaves one statement in the
> repo inaccurate. `map-implementation-rules.md` records that *"the one ignore file, `.gitignore`, ignores
> `.worktrees/` and `.claude/worktrees/`, the second added at node 158"*. After this work `.gitignore` ignores three
> paths, so that enumeration no longer lists what the file holds. **The worker could not have fixed it without
> breaching clause 5, so this is not its defect and I am not failing the work for it** — the wording is the
> condition's own and was not the worker's to depart from. Flagging it so somebody who may edit that file decides
> whether it wants the third entry appended.

**The manager's settlement of the two `NOT COVERED` sub-parts.** *Not the checker's text. The manager holds the
handover the checker was correctly denied, and both are satisfied in it.*

- **Clause 1's reporting half is met.** The handover carries the command and its output under `**The measurements
  the condition demands, as the commands printed them.**`, quoted as a shell transcript with the exit status —
  `.gitignore:19:.scratch/graph-workflow/worktrees/` and `exit=0`, which is byte-for-byte what the checker's own
  independent run printed.
- **Clause 2's reporting half is met.** The handover states *"Clause 2's pointer was confirmed by opening
  `map-manager-only.md` and finding the phrase … in the live record and in the worktree's own copy alike"*, which is
  the same two-copy finding the checker reached separately.
- **Neither was taken on trust.** The checker ran clause 1's command itself and resolved clause 2's pointer itself;
  what the manager settles is only whether the handover *said* so, which is the one thing a blind reader cannot see.

**The manager's disposal of the checker's question.** Already minted, before the check returned, as [node
271](271-the-rules-files-account-of-gitignore-names-two-patterns-where-there-are-three.md) — its author being this
node's own worker, which reported the same drift in its `INVALIDATIONS`. **Two agents found it independently**, one
holding the handover and one blind to it, which is the strongest evidence available that it is real.

~~**The gate is assembled and queued**, the manager's own raise about where the acceptance-condition rule ships being
live in front of the human.~~ Raised once that raise and node 264's question had both been answered.

### Gate — `approve`

**The human's answer**, `verbatim`: *"approve"*

No divergence: the payload carried a `PASS` and no recommendation against landing.

**Landed under the effort's landing policy, and the whole cycle ran inside the sandbox.** One path-limited commit of
`.gitignore` in the node's worktree; **rebased** from `0402ab1` onto `db81330`, which node 260 had landed meanwhile,
with no conflict; the bar's command half empty, so nothing to re-run; `git merge --ff-only` onto `master`; worktree
removed and branch deleted. **Commit `7aa89cb`**, carrying the trailer `Node: graph-workflow/269`.

**No sandbox override was needed at any step** — commit, rebase, merge, `worktree remove`, `branch -d`. Every
landing before this one needed the sandbox off for the merge, because the range crossed `.claude/skills/`; this
range is one file that does not. **It is also the first landing whose worktree was both created and removed by plain
git**, and neither command was refused.

**Verified after landing rather than assumed**: `git check-ignore -v .scratch/graph-workflow/worktrees/probe` on
`master` returns `.gitignore:19:.scratch/graph-workflow/worktrees/` with exit 0, and `git worktree list` shows node
268's live worktree sitting under the now-ignored path.
