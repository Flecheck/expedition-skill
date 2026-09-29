# Carry the plain-git worktree route into the map

Type: implementation
Status: resolved
Supersedes: 250, 261, 262

Blocked by: none

## Question

*Surfaced by [node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md)'s worker, and pasted as it
wrote it.*

> `map.md`'s standing instruction says a worktree is created by the harness and never by hand, and
> `map-manager-only.md`'s `How the worktree is made` states the `EnterWorktree`-then-reset route in full. Node 265
> reversed both, on the human's own word. Replace that text with the route now in force, banking what it replaces.

**Blockers, in the worker's words:** *"none. **But it must not be claimed while another worker holds `map.md` or
`map-manager-only.md`.** Two open nodes edit the same material and both are premised on the route this node removes
— [node 261](261-a-worker-can-land-at-the-repository-root-where-enterworktree-is-refused.md), whose question no
longer has a referent, and [node 262](262-three-statements-name-a-different-first-act-for-a-worker.md), whose first
target sentence will now never exist. Whoever sequences should run this node before either, or instead of them."*

## Acceptance condition

*Written by node 265's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map.md`, `.scratch/graph-workflow/map-manager-only.md` and
> `.scratch/graph-workflow/map-history.md`, and no other file may be edited. The worker may not mark this node,
> resolve it, or write a line in `decisions.md` or `flags.md`. Done means every one of the following is true of the
> finished tree.
>
> 1. Neither `map.md` nor `map-manager-only.md` states any longer, as a rule that binds, that an implementation
>    node's worktree is created by calling the `EnterWorktree` tool; that a worktree is created by the agent harness
>    rather than by hand; that a worker calls `EnterWorktree` or `ExitWorktree` to reach or leave its worktree; or
>    that the manager checks the base the worktree landed on and `git reset --hard`es it to the manager's `HEAD`.
> 2. `map-manager-only.md` states, in its own text, all of the following about the route that replaces it:
>    - the manager creates each implementation node's worktree from the main tree with a plain `git worktree add`
>      command placing it at `.scratch/graph-workflow/worktrees/<NN>-<name>` on a branch `worktree-<NN>-<name>`,
>      where `<NN>` is the node's id;
>    - that command lands the worktree on the manager's current `HEAD` by git's own default, so no base reset is
>      performed and no `worktree.baseRef` setting is relied on;
>    - no step of the route needs a harness tool call or a sandbox override, by the manager or by the worker;
>    - a worker writes its worktree by absolute path, calls no tool to reach it, and owes no cleanup;
>    - the worktree is removed with `git worktree remove --force <path>` followed by `git branch -D
>      worktree-<NN>-<name>`.
> 3. `map-manager-only.md` states the route's one failure mode and the check that catches it: that the route works
>    because `.scratch/graph-workflow` is inside the manager's sandbox writable region; that this has not always been
>    so; that the manager runs `test -w .scratch/graph-workflow` before creating a worktree; and that where it fails
>    the worktree can be neither created nor written, which is **raised to the human** rather than worked around, no
>    tool call being able to widen the region for that path.
> 4. Every new statement added by clauses 2 and 3 cites the node that shaped it by markdown link, and none of them
>    recounts how many attempts a decision took, what an earlier attempt cost, or who was wrong.
> 5. Every piece of text in either file that this work displaces and whose job is to state a rule that currently
>    binds is **replaced** rather than struck in place, and its existing wording is appended **verbatim** to
>    `map-history.md` under a heading mirroring the section it came from, with any struck-through text staying struck
>    through. Text whose job is to record what happened is left where it is and marked rather than removed.
>    `map-history.md` gains text and loses none.
> 6. The `## Landing an implementation node's work` heading in `map-manager-only.md` is still present, and the quoted
>    phrase `How the worktree is made` still occurs in that file — two pointers in the repository's `.gitignore` cite
>    them.
> 7. No file under `.claude/skills/` is changed, `.gitignore` is not edited, and no file outside the three named
>    above is modified.
> 8. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**Sequencing, which is the manager's and not this node's.** [Node
260](260-never-ask-which-is-stated-for-nodes-not-for-what-waits.md) holds `map.md` and `map-history.md` in a
worktree at a gate. **This node cannot be claimed until that lands or is refused.** The worker's own blocker note
says the same thing from its side.

**[Node 250](250-state-how-an-implementation-worker-reaches-its-worktree.md)'s parked branch also holds
`map-manager-only.md`**, committed at `bd93fb8` and not merged. Its content is the worker's half of the route this
node removes. **Whoever claims this node works from `master`, not from that branch**, and the parked branch's fate
is the manager's and the human's rather than this node's.

**Clause 6 is load-bearing and easy to break**: `.gitignore`'s two comments cite that heading and that quoted
phrase, and repairing them was node 249's whole subject. Removing the route's text while keeping the phrase that
names it is the narrow path.

## What the work states

*The worker's `ANSWER`, pasted as it wrote it.*

> **The `EnterWorktree`-then-reset route is out of the map, and the plain-git route settled at [node
> 265](265-should-the-worktree-route-drop-enterworktree-for-git.md) is in its place.** Three files changed and no
> others: `map.md`, `map-manager-only.md`, `map-history.md`.
>
> ### What each file now holds
>
> - **`map.md`** — its standing preference *"A worktree is created by the harness, never by hand"* is **replaced** by
>   one paragraph carrying the half of the route every worker can act on: the manager makes the tree with `git
>   worktree add` at `.scratch/graph-workflow/worktrees/<NN>-<name>` on branch `worktree-<NN>-<name>`; **a worker
>   writes that tree by absolute path, calls no tool to reach or leave it, and owes no cleanup**; no step needs a
>   harness tool call or a sandbox override. It points at `map-manager-only.md` for the whole route and at
>   `map-history.md` for what it replaced. It is a 1-line-for-1-line swap.
> - **`map-manager-only.md`** — `How the worktree is made` is rewritten as six bullets: **Create**, **Base**, **no
>   harness tool call and no sandbox override**, **the worker's absolute path**, **Remove**, and **the route's one
>   failure mode**, with the surviving commit-trailer bullet kept in place between them. Each new bullet cites node
>   265 by markdown link. The landing policy's opening clause now names the manager and plain git, and the new path.
> - **`map-history.md`** — gains two sections and loses nothing (110 lines added, 0 removed). Every displaced passage
>   is reproduced **byte-identical to the text it had at `HEAD`**, verified programmatically rather than by eye.
>
> ### The sort clause 5 demanded, and how each passage was classified
>
> `map-manager-only.md`'s worktree material is ~76 lines interleaving two kinds of text. The classification is the
> work, and it went this way:
>
> **Replaced and banked verbatim — job is to state a rule:** the landing policy's *"created by the harness rather
> than by hand … placed at `.worktrees/NN-<name>/`"* clause; the section's opening paragraph; the route bullet;
> *what the reset costs in practice*; *the manager needs `EnterWorktree` for neither the base check nor the reset*;
> *the manager verifies the base at every spawn*; and the ground clause of the correction-round bullet.
>
> **Left where they are and marked — job is to record what happened:** the *One sandbox restriction bites this
> lifecycle* bullet and its three sub-bullets. Nothing was removed from them. A marking sentence was added above
> them saying that they are measurements, that two operations they name — a reset, and an *entered* worktree — are
> steps of no route any longer, and that the merge step they also name is still in the landing policy and what bites
> it is unchanged.
>
> **Kept untouched because they still bind:** the commit-trailer bullet, and the failed-rebase bullet, which is
> about the rebase in the landing policy and not about how the worktree is made.
>
> **The hard call was *what the reset costs in practice*.** It carries three sentences of the human's own words in a
> blockquote, which reads like a record of what happened. Its job is not that: the bullet states what the manager
> does about the reset in three cases, and every case is premised on a reset step this route no longer has. It was
> classified rule-stating, replaced, and banked with the human's words intact inside the banked copy.
>
> ### The contradiction node 265 reported is gone as a by-product
>
> Node 265's invalidation 11 — *"`map-manager-only.md` contradicts itself on `worktree.baseRef`"* — was carried by
> two of the bullets replaced here. Both halves are banked and neither is live. The file now says only that **no
> `worktree.baseRef` setting is relied on**, the command landing on `HEAD` by git's own default.
>
> ### Clause 6, which was the narrow path
>
> `## Landing an implementation node's work` is present exactly once and unchanged. The quoted phrase `How the
> worktree is made` occurs **three** times in `map-manager-only.md`, and `map.md`'s pointer is a fourth in the other
> file. The route's text is gone; the phrase that names it stayed. Three `.gitignore` pointers now cite it: the two
> node 249 repaired, and the third node 269 landed at `7aa89cb` while this node was running.
>
> ### The route was used to document itself
>
> This node's own worktree was made by the route it writes down: `test -w .scratch/graph-workflow`, then `git
> worktree add -b …`. It landed on the manager's `HEAD` with no reset. The worker called no tool, disabled no
> sandbox, wrote every file by absolute path, and owed no cleanup. **Nothing in the route needed testing because
> everything in it had already run.**

**The index line the worker wrote**, held here until the node resolves:

> `map.md` and `map-manager-only.md` now state the plain-git worktree route from node 265; the
> `EnterWorktree`-then-reset text is banked verbatim in `map-history.md`.

## Flags

`268.1` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> Two passages that clause 1 does not literally name were amended anyway, because removing the route made them
> false. The first is the landing policy's path, `.worktrees/NN-<name>/`: clause 1 names *"created by the harness
> rather than by hand"* in that sentence but not the path, and leaving the old path live would have made the file
> contradict the new path clause 2 requires it to state. The second is the correction-round bullet, whose ground was
> *"never re-spawns it with isolation, a second isolated spawn creating a second empty tree at a fresh base"* — no
> spawn creates a tree under this route, so the ground was replaced with the one that now holds. Both were banked
> verbatim under clause 5 exactly as the passages clause 1 does name. **I did not raise, because neither changes
> what the condition demands and both are the condition's own consequence rather than a decision reaching past this
> node.**

`268.2` `ASSUMPTION` **· settled** — *The worker's own text, pasted.*

> The bullet *"What the reset costs in practice, settled by the human"* was replaced and banked rather than marked
> in place, although it carries three sentences of the human's verbatim words. Clause 5 sorts by the text's job, and
> this bullet's job is to state what the manager does in each of three cases — every one premised on a reset step
> the route no longer has — rather than to record what happened. **The same test sent the opposite way on the *One
> sandbox restriction* bullet**, whose job is to record measurements: it stayed, lost nothing, and gained a marking
> sentence. The human's words survive verbatim in the banked copy either way; what differs is whether a reader of
> the live file still meets them.

## Invalidations

*The worker's own text, pasted.*

> 1. **[Node 152](152-where-the-harness-worktree-instruction-lives.md)** — node 265's invalidation 8 predicted this
>    and it is now true. Its condition quotes phrases from `How the worktree is made` that no longer exist in that
>    section. The section's live phrases are now `Create`, `Base`, `Remove`, `The commit trailer …`, and `The
>    route's one failure mode, and the read-only command that catches it`; its lead-in phrase `How the worktree is
>    made` is unchanged. Any repair must quote the section's form as it now stands. Bookkeeping, and the manager's.
> 2. **[Node 261](261-a-worker-can-land-at-the-repository-root-where-enterworktree-is-refused.md)** — already
>    dissolved by node 265. This work removes the last text in the map its question rested on.
> 3. **[Node 262](262-three-statements-name-a-different-first-act-for-a-worker.md)** — `map.md`'s standing
>    instruction was one of the statements its question set against each other, and it is gone. What `map.md` now
>    says about a worker's first act is that there is none.
> 4. **[Node 150](150-which-harness-route-creates-a-worktree.md)'s `decisions.md` line** — still live, still the line
>    a later worker greps for `worktree`. Named by node 265 and untouched here; clause 7 forbade this node to edit
>    `decisions.md`.
> 5. **`map-implementation-rules.md`'s `.gitignore` inventory** — stale as of node 269's landing at `7aa89cb`. Not
>    editable from this node under clause 7.

## Retrospective

*The worker's own text, pasted.*

> **1. What I had to hunt for.** **Nothing important, and that is worth recording.** The spawn named node 265's
> `## Answer` as the source for clauses 2 and 3, and it was. It named the two files as targets, the map-history
> pattern at nodes 244 and 260, and the parked branch to ignore. I opened eight files total and re-opened none.
> **Compare node 265's own retrospective, which reported three hunts. The difference is that this node's spawn named
> the single source for the substance instead of the topic.** The one thing I derived rather than read: the exact
> line boundaries of the seven passages to bank. There is no way to get that but to read the section and count, and
> it is where most of the node's effort went. **A record whose rule-stating bullets were separated from its
> measurement bullets by anything — a sub-heading, an ordering convention — would have made the sort mechanical
> instead of a judgement over 76 interleaved lines.**
>
> **2. What arrived in my context that this node did not need.** **`map-implementation-rules.md` whole, 74 lines.**
> The spawn told me its review-route paragraph is written for the checker and that three workers had reported
> reading it for nothing — and it was right, but I read the file anyway because I needed its bar paragraph and its
> four standing writing rules, and they sit either side of the review route. **This is the fourth report and the
> spawn is now pre-emptively apologising for it**, which is evidence the fix is a file change rather than a spawn
> sentence. **`map.md` whole, 115 lines, and this time it was a deliverable** — so unlike the six workers before me
> I paid for it legitimately; but the arrangement node 250's worker proposed would have let me find the one
> paragraph I had to replace by heading instead of by reading to line 94. **`map-history.md`'s 585 lines were read
> as headings only**, on the spawn's instruction, and that was exactly right — I needed the shape of a banked block
> and two examples, and got both for ~40 lines of output. **That instruction is the single cheapest thing in the
> spawn and it should be standard for any node that appends to that file.**
>
> **3. What would have made this node easier.** **In the record — and this is the one that matters.**
> `map-manager-only.md` interleaves rule and measurement inside a single section with no marker of which is which,
> and clause 5 makes that distinction decide every edit. **The file already knows the distinction exists**:
> `map-implementation-rules.md` states it as *trigger against history*, and `map.md`'s never-delete preference
> states it as *states a rule* against *records what happened*. **Neither file marks which of its own passages is
> which.** A convention as small as measurements living in their own sub-bullet under the rule they ground would
> have turned this node's central judgement into a read. **In the spawn.** The warning that clause 5 cuts against
> clause 1 was the most useful sentence I received, and the correction the manager filed against itself — *"I had
> reasoned from one handle where there were two"* — was the second, because it told me to test the shape of my own
> answer rather than the manager's account of it. I did, twice, and both times programmatically. **A spawn that says
> *test my shape claims* gets a worker that verifies instead of inspecting.** **In the node file.** Nothing.
>
> **4. What I read that was stale, wrong, or contradicted something else.** **`map-manager-only.md`'s landing policy
> still says an implementation node's work is *"uncommitted in a checkout outside the repository"*.** False since
> node 68 and doubly false now. **It is the stated ground for a rule that still binds, which is the worst place for
> a false clause to sit.** **`map-implementation-rules.md` says `.gitignore` ignores two patterns; it carries
> three** since node 269 landed mid-node. **`map-manager-only.md`'s self-contradiction on `worktree.baseRef`** —
> reported on node 243's retrospective and never minted. **It is gone**, both halves having been inside bullets this
> work replaced. **Worth the manager knowing that a finding reported twice and never minted was discharged by
> accident.** **Node 265's `## Interview` holds two full payloads, the first of which recommends the opposite of
> what landed**, at roughly 90 lines before the `## Answer`. **This is the third report this effort of a
> multiply-superseded node file needing a `## Current answer` pointer at its top.**

## The manager's disposal of the retrospective's record items

*Not the worker's text.*

- **The landing policy's "outside the repository" clause** → **minted as [node
  276](276-the-landing-policy-says-the-work-sits-outside-the-repository.md)**, carrying the worker's own condition,
  **with its own note that folding it into [node 231](231-a-gate-payload-stops-carrying-a-diff-command.md) is likely
  cheaper**, that being the same sentence node 231 rewrites. **The fold is the human's call and is named for them.**
- **`map-implementation-rules.md`'s `.gitignore` inventory** → **already minted as [node
  271](271-the-rules-files-account-of-gitignore-names-two-patterns-where-there-are-three.md)**, from node 269's
  worker. **Three agents have now found this independently** — node 269's worker, its checker, and this worker — and
  the manager has minted it once.
- **A finding reported twice and never minted, discharged by accident** — the `worktree.baseRef` self-contradiction
  → **nothing owed, and the worker is right that the manager should know.** It is the clearest available evidence
  that *named for the human* without a node is a channel that loses things.
- **A `## Current answer` pointer at the top of a multiply-superseded node file, third report** → **not minted**, it
  being a `Change the map` on the node-file format, which is node 13's. **Named for the human, third report.**
- **`map-manager-only.md` not marking which of its passages state rules and which record measurements** → **not
  minted, and this is the strongest-argued item any retrospective has produced this session.** Two files already
  state the distinction as a rule; neither marks its own text by it. It is adjacent to node 246 but is not the same
  claim. **Named for the human.**
- **Reading `map-history.md` as headings only** → **nothing owed; the manager will put it in every spawn that
  appends to that file.**

## Review

### Run 1 — `PASS`

*The checker's own text, pasted. It was spawned by the manager, was given the acceptance condition as extracted
text, the bar as properties, the three changed paths and the tree holding them, the record-as-work rule, and this
effort's ground rules and four standing rules for writing copied as text. It was given nothing from this node or
from the effort's record. It was told clause 5's sort was where the work is, that the verbatim half was to be
established programmatically against `git show db81330:` rather than by reading, and that clause 4's second half is
a second sort on the new text.*

> **PASS**
>
> **Reaching the tree.** By absolute path and `git -C` only. No harness tool call, no sandbox override, no refused
> read. `git status --porcelain` returned exactly the three named paths; `--untracked-files=all` adds nothing. I read
> the three changed paths **as the work under check** under the implementation-rules rule for record files, and
> derived no statement of intent from them.
>
> **Clause 1 — the four old rules no longer bind. Met.** I unwrapped both files into paragraphs and searched the
> unbroken text for `EnterWorktree`, `ExitWorktree`, `.claude/worktrees`, `.worktrees`, `CLAUDE_BASE`, `baseRef`, `by
> hand`, `isolation`. In `map.md` the only surviving `EnterWorktree` is inside node 265's title as a citation. In
> `map-manager-only.md` the survivors are node-265 citations (3×), one `no worktree.baseRef setting is relied on` (a
> negation of the old rule), and the sandbox measurement sub-bullets — explicitly marked as naming *"steps of no
> route any longer"*. No binding statement of the old route remains.
>
> **Clause 2 — the replacing route stated. Met, all five items**, in the `How the worktree is made` bullets: create
> from the main tree with `git worktree add -b worktree-<NN>-<name> .scratch/graph-workflow/worktrees/<NN>-<name>`,
> `<NN>` the node's id; lands on the manager's current `HEAD` by git's default, so no base reset and no
> `worktree.baseRef` reliance; no harness tool call or sandbox override by manager or worker; the worker writes by
> absolute path, calls no tool, owes no cleanup; removal by `git worktree remove --force <path>` then `git branch -D
> worktree-<NN>-<name>`.
>
> **Clause 3 — the failure mode and its check. Met**, in one bullet: works because `.scratch/graph-workflow` is
> inside the manager's sandbox writable region; that this has not always been so; `test -w .scratch/graph-workflow`
> run before creating a worktree; where it fails the worktree can be neither created nor written, raised to the human
> rather than worked around, no tool call able to widen the region for that path.
>
> **Clause 4 — citation, and no attempt-counts/costs/blame. Met.** Every one of the six new bullets, and the
> section's new opening, carries a markdown link to node 265. I extracted the added lines and read them for the three
> prohibited forms; none appears. **The closest call** is the failure-mode bullet's *"in one session the manager's
> own shell could not append to `flags.md` in that directory while it could write the node files one level below"* —
> it is neither an attempt count, nor a cost, nor who was wrong; **it is the symptom establishing the trigger clause
> 3 itself demands** (*"that this has not always been so"*), which the trigger-versus-history test keeps in place.
>
> **Clause 5 — the sort, and verbatim banking. Met, and established programmatically rather than by reading.**
>
> - **Nothing lost from `map-history.md`:** the base file is a byte-exact *prefix* of the new one (131,965 of
>   141,318 bytes; 110 lines appended, 0 removed).
> - **Verbatim:** I parsed the appended section into its **eight banked passages**, stripped the blockquote prefix
>   where used, and tested each as a contiguous substring of `git show db81330:<path>`. **All eight are
>   byte-identical** — seven against the base `map-manager-only.md`, one against the base `map.md`.
> - **Nothing displaced went unbanked:** of the 48 removed lines in `map-manager-only.md` and the 1 in `map.md`, all
>   but one appear verbatim in the appended text. The exception is the single long landing-policy line; I showed by
>   character-level comparison that the new line equals `prefix + new clause + suffix` with the identical 140-char
>   prefix and 2,051-char suffix, **so everything deleted from that line lies inside the banked clause.**
> - **The sort itself:** the passages banked are the route-stating ones — the landing-policy clause, the section
>   opening, the `EnterWorktree` route bullet, the reset's cost, the base-check bullets, the correction-round bullet
>   — each states a rule that bound. The passages left in place and marked are the sandbox-restriction bullet and its
>   three measurement sub-bullets, whose job is to record what was measured; they carry a new marking note citing
>   node 265. **I found nothing banked whose job was to record, and nothing left behind that stated a rule the new
>   route displaces.**
> - No `~~` struck text was displaced, so that sub-clause is vacuous. Headings mirror the source and match the
>   file's own established convention.
>
> **Clause 6 — the two `.gitignore` pointers still resolve. Met.** `## Landing an implementation node's work` is
> present, and `How the worktree is made` occurs three times in `map-manager-only.md`.
>
> **Clause 7 — scope. Met.** `git diff --name-only` returns the three paths; `git diff --name-only -- .claude/skills/
> .gitignore` returns nothing. No node status line, no `decisions.md`, no `flags.md` among the work.
>
> **Clause 8 — the bar. Met.** Discovered from the repo rather than taken from any account: the worktree root holds
> only `CONTEXT.md`, `.gitignore`, `.claude/` and `.scratch/` — no manifest of any kind and no `.github/`. No build,
> no tests, no formatter, no CI, so the command half is empty and complete. On the non-command half:
> **`/writing-for-agents`** — the negative framings (`no base reset`, `calls no tool`, `owes no cleanup`) are each
> paired with the positive statement the standard asks for, and their wording is the acceptance condition's own; no
> finding. **`graph-conventions.md`'s `## Writing the map`** — the verbatim-move, heading-mirroring and
> current-statement rules all hold; `map.md`'s new note is 1,072 bytes against the 500-byte target, **down from
> ~1,800**, and the section states the target is never a rule that forces text out. **`CONTEXT.md`'s `_Avoid_`
> lines** — scanned the 150 added lines, reading the ordinary-English third by hand per the measured trap; one hit,
> `On reject`, is pre-existing text this work provably did not displace and names the human's own act. **The four
> standing rules and five ground rules** — each new item states its current form and cites its node, the section
> stays navigable by heading, no line-number citations, nothing assumes a toolchain. **`/coding-principles` and
> `/naming`** — read; no code, and the only names introduced are the path and branch patterns the condition
> dictates.
>
> **Reviewing skill:** none named for this repo, so I ran none and spawned no agent; **no part of any skill ran in an
> agent handed less than I was.**
>
> **Formatting:** no trailing whitespace in any added line; all three files end in a newline; the new bullets wrap at
> the file's existing width.
>
> **Link resolution:** every markdown link in the added text resolves inside the worktree, **with one exception** —
> `nodes/268-…md`, which exists in the main tree but not at base `db81330`. That is the effort's own stated practice
> (graph files are committed periodically rather than per node), **not a defect of this work.**
>
> No questions, and nothing left uncovered.

**The manager's disposal of run 1.** *Not the checker's text.*

- **`PASS` on both halves, first run, no repair owed**, on a node whose central demand was a judgement over 76
  interleaved lines. **Both parties verified the banking programmatically and independently** — the worker against
  `git show HEAD:`, the checker against `git show db81330:` — and both got byte-identical on all eight passages.
- **The checker's one proactive finding is the character-level proof about the long landing-policy line.** Nothing
  asked for it; a line-level diff cannot distinguish *replaced a clause* from *rewrote the line*, and it closed that
  gap by comparing the 140-character prefix and 2,051-character suffix.
- **It also declined a finding and named the test it declined it under** — the failure-mode bullet's *"in one
  session the manager's own shell could not append to `flags.md`"*, which is the symptom clause 3 demands rather
  than a cost. A neighbouring node was failed on that exact standard, so the distinction is live rather than
  theoretical.
- **The dangling `nodes/268-…md` link is [node 266](266-a-worker-cannot-see-the-record-the-manager-has-not-committed.md)'s
  subject exactly**, met for the second time and by a blind reader this time. The checker reached the right
  conclusion — not a defect of this work — from the file's own practice rather than from being told.

### Gate — `approve`

**The human's answer**, `verbatim`: *"approve gate"*

No divergence: the payload carried a `PASS` and no recommendation against landing.

**Landed under the effort's landing policy.** One path-limited commit of the three record files in the node's
worktree; **rebased** from `db81330` onto `7aa89cb`, which node 269 had landed meanwhile, with no conflict; the
bar's command half empty, so nothing to re-run; `git merge --ff-only` onto `master`, **which succeeded inside the
sandbox** — the range touches no file under `.claude/skills/`. **Commit `8933f1d`**, carrying the trailer
`Node: graph-workflow/268`.

### The `EBUSY` failure reproduced at this landing, and the cause is now measured

***The manager's record, and it corrects something the manager told the human twice.***

**`git worktree remove` failed**, `verbatim`: `error: failed to delete
'.git/worktrees/268-plain-git-route-into-map': Device or resource busy`. The working directory was removed; the
**admin directory under `.git/worktrees/` was not**, leaving the entry `prunable`, the branch undeletable (*"cannot
delete branch … used by worktree at …"*), and `git worktree list` showing a tree that no longer exists. **That is
exactly the stale-entry-reading-as-an-occupied-slot failure the human's original never-by-hand instruction was
built on.** `git worktree prune` failed the same way.

**The cause is the sandbox, not git and not the route.** `/proc/mounts` carries, for **every live worktree
including plain-git ones**, two bind mounts:

```
/home/mathieu/projects/graph-agent/.git/worktrees/<name>            rw
/home/mathieu/projects/graph-agent/.git/worktrees/<name>/commondir  ro
```

**A mount point cannot be unlinked**, so any removal attempted inside the sandbox fails on that directory. **`git
worktree prune` with the sandbox off succeeded immediately**, pruning the entry and freeing the branch, which was
then deleted.

**What this corrects.** [Node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md)'s worker reported the
failure had *"not reproduced three times"* and the manager repeated a version of that to the human twice, the second
time as *"four times"*. **It reproduces.** What node 265's worker measured was a worktree it created **and removed
within its own session**, which never acquired the mounts; and node 269's removal succeeded for a reason **not
established**. So the correct statement is narrower than either: *the mounts exist for every worktree the sandbox
knows about, and a removal inside the sandbox fails on them.*

**What this does not change.** The route itself stands: creation, writing and the whole of a worker's life in the
tree ran sandboxed and unrefused, across four nodes. **What changes is the removal step**, which now needs the
sandbox off — a cost the old route paid at a different step, the reset.

**Filed as flag `268.3`, and the repair is a node** rather than a manager note, because
[map-manager-only.md](../map-manager-only.md)'s `How the worktree is made` was written by this very node and now
states a removal step that does not work as written.

*The manager's note, 2026-09-29:* this node's outstanding flags are settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4 (`verbatim`: *"ok"*): the node had closed, and only the two writes of `### Settle a flag` were owed.

`268.3` **· settled** — *The manager's entry, 2026-09-29:* this flag's entry above is in a form the marker position does not fit, so its settling is recorded here. Settled in the batch the human approved at [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s Q4.
