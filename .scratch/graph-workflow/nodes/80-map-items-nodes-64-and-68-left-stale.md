# Update the map items that nodes 64 and 68 left stale

Type: implementation
Status: resolved

## Answer

The async-landing item in map-manager-only.md now prices the flip against today's four landing steps: the gate points at a merged commit, reject needs a revert, and SKILL.md's approval-before-commit order breaks.

*The manager's note:* the worker's answer is under `## Handover, attempt 1`, under the replacement condition of `## Amendment, 2026-09-29 (from node 366)`. The checker passed it on run 1. The gate was taken under the human's standing yes (see `## Review`). The work landed as commit `766efd77`. Flags 80.1, 80.2 settle at the node closing report.

## Question

Three items in `map.md` describe a workflow that no longer exists — one says the map's superseded text stays in
place, one lists worktrees as an unadopted upgrade, and one prices a reject as a forward revert. **Each is falsified
by a node that has already resolved.**

Reported by [Carry the worktree lifecycle into the shipped files](74-carry-the-worktree-lifecycle.md)'s worker as
flag `74.2`, which wrote the acceptance condition below.

**The first is the sharpest, and it has already cost something.** The standing preference *"An in-place update never
deletes"* still tells its reader that `map.md`'s superseded text stays where it is, which [Say in the conventions
document how the map and its history are written](64-conventions-say-how-the-map-is-written.md) falsified. **Node
74's own acceptance condition inherited that staleness** — its clause quoted the map faithfully and was contradicted
by the shipped standard — which cost a manager's raise and a human licence. Node 74's checker met the same
contradiction and recorded that *"a future worker meets the contradiction cold."*

### The licence this node needs before it can be claimed

**It writes `map.md`, which the implementation contract's hard rule 1 forbids.** That is the same collision nodes 59
and 74 met, and it needs the human's licence carried into the spawn in their own words. **The manager may not grant
it.** The permanent fix is [Qualify the graph-file ban in the worker contracts](58-qualify-the-graph-file-ban.md),
still open — **this is the third node to pay a human round trip for a distinction the human has already drawn
twice.**

**Blockers: none**, but it contends for the code slot with any other node editing `map.md`.

## Acceptance condition

*Superseded whole 2026-09-29 by node 366's replacement; see `## Amendment, 2026-09-29 (from node 366)`.*

*Written by node 74's worker.*

`.scratch/graph-workflow/map.md` is edited, together with `.scratch/graph-workflow/map-history.md` where the map's
own conventions require superseded text to be moved there. No other file changes.

Three items in `map.md` are brought to what holds now.

**1. The standing preference beginning "An in-place update never deletes."** It currently reads: *"When any file in
the graph is edited — a node or this map — superseded text is marked as superseded and left where it is, and new
text is added around it. Information leaves a file only when it is clearly wrong or the human asks for it gone.
Quiet deletion is most damaging and least visible in the map itself."* Its second clause is false for `map.md`.
`.claude/skills/expedition/graph-conventions.md`, under its heading `## Writing the map`, states instead: *"So the
map is rewritten as it changes rather than grown by appending: the superseded text moves out, and what replaces it
stands alone."* and *"This deletes nothing. Text moved to `map-history.md` is moved verbatim — never summarised,
paraphrased or shortened — and text already struck through moves struck through. The never-delete rule is satisfied
by the move rather than exempted from it."* The rewritten preference states that a node file's superseded text is
marked in place, and that `map.md`'s moves verbatim to `map-history.md`. It no longer tells its reader that
`map.md`'s superseded text stays where it is.

**2. The fog item beginning "Whether the Claude Code subagent runtime proves too simple."** Its first sentence names
*"the upgrade path to a firstmate shape — real sessions, worktrees, file mailboxes — if it does."* Worktrees are no
longer an unadopted upgrade: `map.md`'s own landing policy has every implementation node's worker working in a git
worktree the manager creates for that node. The item no longer lists worktrees among what a move to a firstmate
shape would buy.

**3. The fog item beginning "When to flip landing to asynchronous."** It currently says: *"The seam is one step —
the manager committing before the gate rather than after — but one gate outcome does not survive it: **reject**
becomes a forward revert rather than a cleaned tree, so the cheapest of the three becomes the most expensive and the
only one that marks history."* Under the landing policy `map.md` now carries, a reject removes the node's worktree
and deletes its branch rather than cleaning a tree, and landing is four steps — a path-limited commit, a rebase onto
the branch the manager thread is on, a re-run of the bar's commands on the rebased result, and `git merge --ff-only`
— rather than one. The item describes the seam and the repriced reject against that lifecycle.

Those three items are the only things that change in `map.md`. The landing-policy paragraphs are left exactly as
they stand.

The standing bar applies: the working tree builds, warns about nothing, is formatted, and passes the tests relevant
to the change. This repository has no build, no tests and no formatter, which is a complete bar on its remaining
half and not a deficient one — so what remains is `/coding-principles` and `/naming`, the `_Avoid_` lines of the
glossary the shipped files declare authoritative, and `map.md`'s own standing preferences, ground rules and four
standing rules of writing.

## Annotation: this node's condition went stale while nothing pointed at it

*Filed by the manager from [node 193](193-state-where-the-never-delete-rule-stops-in-the-map.md)'s handover, and
pasted as that worker wrote it. This node is open and unclaimed; the annotation records the finding rather than
amending the condition.*

> **Node 80 — an open implementation node whose clause 1 is this exact preference, and my work discharges it in
> substance while falsifying it in form.** Nothing links node 80 to nodes 189, 193 or 194; I found it by grepping
> the old wording. Three things, and none of them mine to fix:
>
> - **Its clause 1 is now stale in its quotation and superseded in its framing.** It says *"It currently reads:"*
>   and quotes the text I replaced, so that quotation is no longer of anything in the tree. It then demands the
>   rewritten preference *"states that a node file's superseded text is marked in place, and that `map.md`'s moves
>   verbatim to `map-history.md`"* — a **file-based** cut, which node 189 superseded with a **text-job** cut. Its
>   last demand, *"It no longer tells its reader that `map.md`'s superseded text stays where it is"*, is satisfied.
> - **Its clauses 2 and 3 are unworkable as written, for a reason predating me.** Both name fog items and its
>   condition permits editing only `map.md` and `map-history.md`; node 139 moved the fog to `map-manager-only.md`,
>   where I verified both items still stand with the quoted sentences intact. This is not caused by my work and is
>   worth the manager's attention with it.

***The manager's note.*** **The manager has amended nothing here.** Node 193's work is at its gate and not landed,
so clause 1's quotation is still true of the tree until it lands; amending a condition before the change that
falsifies it has landed would be the manager guessing at a gate's outcome. **What is owed once node 193 lands** is
that this node be looked at rather than picked up as written — its clause 1 discharged in substance, and its
clauses 2 and 3 broken since node 139 by a scope that no longer contains the files they name.

**Why nothing caught it.** Three nodes — 189, 193 and 194 — went past this preference without anyone noticing an
open node held a condition quoting it. **What found it was a `grep` for the old wording, run by a worker on its own
initiative because nothing told it to.** Its retrospective says the fix is an edge: *"An open node whose clause 1 is
the item another node was minted to rewrite should carry an edge to it."* The manager records that as a finding
against its own bookkeeping and not against any worker.

## Amendment, 2026-09-24

*Written by [node 299](299-rewrite-graph-conventions-part-1.md)'s worker and filed by the manager, after that node's work landed as commit `0d406b7`. Every word of the replacement is fixed by that commit: it quotes `graph-conventions.md`'s after-text. The minting author's condition above is left as it was. The replacement takes the place of the clause it names. Node 299's worker searched every open node's `## Acceptance condition` for quoted spans of its before-range, matched literally and normalised with each condition joined into one string, and for each phrase its rewrite removed or replaced. The full list of handles is on node 299 under `### Re-pointing duty` and correction rounds 1 to 3.*

- **Item 1.** Replace the first quote with *"So a map file is rewritten as it changes, rather than grown by appending. The text that replaces an item stands alone."*. That quote had already stopped matching the before-text, which said "So a map file", not "So the map". Replace the second with *"Moving the superseded text out deletes nothing. Text moved to `map-history.md` is moved verbatim, without summarising, paraphrasing or shortening it. Text already struck through moves struck through."*

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      Update the map items that nodes 64 and 68 left stale

ANSWER:        The work follows the condition in `## Amendment, 2026-09-29 (from node 366)`, Block 6. In `.scratch/graph-workflow/map-manager-only.md`, under `## Not yet specified`, the item beginning "When to flip landing to asynchronous" had one sentence replaced: "The seam is one step — … only one that marks history." That sentence described a landing policy with no worktree. The new sentences describe the flip against the policy as it stands in this tree under `## Landing an implementation node's work`:
- Today the manager lands work only after approval, in four steps: a path-limited commit, a rebase onto the manager thread's branch, a re-run of the bar's commands, and `git merge --ff-only` run with the sandbox off (node 369). The flip moves those four steps to before the gate, so the human reviews work that has already merged.
- The gate payload would then point at the merged commit. The worktree's uncommitted changes it names today would be gone.
- A reject today removes the worktree and deletes its branch, leaving nothing on the manager thread's branch. After the flip it needs a revert commit on that branch, which makes it the costliest gate outcome.
- An implementation node superseded after its work has merged costs the same. SKILL.md, as changed by node 371, cleans such a node up in a reject's order.
- The flip also breaks the order `.claude/skills/expedition/SKILL.md` fixes ("approval before any commit"). So it changes the shipped manager contract, not only this effort's landing policy.
The item's title, its "What is unspecified…" sentence, its trigger sentence and its "Shaped by" citations are unchanged. The replaced sentence is appended verbatim to the end of `.scratch/graph-workflow/map-history.md` under the new heading `## Superseded from `map-manager-only.md` at node 80 — the asynchronous-landing item's seam and reject`, with the sub-heading `### From `## Not yet specified` — the item beginning "When to flip landing to asynchronous"`, in the same shape as node 336's entry. Calls a later reader would otherwise re-derive:
- Only the stale sentence was replaced, not the whole item. So only that sentence is banked.
- "Forward revert" and "cleaned tree" no longer appear. A revert commit is still named, because under any policy that merges before the gate, that is what a reject costs.
- The old claim "the only one that marks history" was dropped. After the flip an approval also leaves a commit, so the claim would be untrue.

INDEX LINE:    The async-landing item in map-manager-only.md now prices the flip against today's four landing steps: the gate points at a merged commit, reject needs a revert, and SKILL.md's approval-before-commit order breaks.

FLAGS:         ASSUMPTION: The condition names only the seam and the cost of a reject. I added two consequences that follow directly from the current policy: the gate payload can no longer point at uncommitted changes, and SKILL.md's fixed order "approval before any commit" breaks. I also added the case of a node superseded after its work has merged. I judged these to be part of "describing the seam" against the policy as it stands, not new items. I did not say what the flip does to a correction round, because the policy gives no ground for it. Index: Node 80's rewrite of the async-landing item names the broken approval-before-commit order in SKILL.md and the superseded-node case, beyond what its condition listed.

NEW NODES:     none

INVALIDATIONS: none. Node 11's settled "seam is a single step" framing was already history text. The current form of the item now states the seam differently. That is an extension of the account, not a change to a resolved answer.

CONDITIONS:    Searched the 30 open or claimed node files for "forward revert", "flip landing", "seam is one step", "cleaned tree" and "asynchronous". Only node 80 matched. No replacement clauses and no changed questions.

MISSING FROM MAP: none. map.md points to map-manager-only.md and map-history.md. I found how a superseded node is cleaned up (node 371) by searching decisions.md and then SKILL.md's "Three outcomes, and no fourth".

GATE PAYLOAD:  No checker findings yet. Bar: the repo has no build, test or formatter (confirmed: no manifest. map-implementation-rules.md records the same). So the bar is the standards half alone. I checked the new words against the glossary's `_Avoid_` lines: none apply ("landing commit" and "bookkeeping commit" are not used). Paths touched, in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/80-fog-item:
- .scratch/graph-workflow/map-manager-only.md (1 line changed: the one item)
- .scratch/graph-workflow/map-history.md (10 lines appended, none removed)
Proposed commit message:
  Re-describe the async-landing seam against today's landing lifecycle

  The fog item in map-manager-only.md priced the flip against a landing
  policy with no worktree. It now names the four landing steps, the gate
  pointing at a merged commit, reject needing a revert, and the shipped
  approval-before-commit order the flip would break. The replaced
  sentence is banked verbatim in map-history.md.

  Node: graph-workflow/80

RETROSPECTIVE:
1. What I had to hunt for: where node 371's superseded-node cleanup lives. The manager's notes named it, but neither map file cites node 371. I found it through decisions.md and then SKILL.md. I also had to look up the exact heading shape of map-history.md entries for map-manager-only.md, using node 336's entry as the model.
2. What arrived that this node did not need: node 160's decisions line and the note about node 376. The whole map.md read was also mostly unneeded for a one-item edit to a manager-only file.
3. What would have made this easier: a condition that quoted the exact sentence to replace, and named the map-history.md heading convention to use.
4. What was stale, wrong or contradictory: the node's `## Question` still describes three map.md items and a licence to edit map.md. Both are moot, because the amendment replaced the condition whole. The node's `## Annotation` and the 2026-09-24 amendment are likewise about clauses that no longer exist. Nothing in the files I edited was contradictory.
````

## Review

### Checker run 1 — `PASS`

*The checker's own text, pasted, 2026-10-02. A fresh checker; the replacement condition reached it as a verbatim copy in `$TMPDIR/c80.md`.*

> PASS
>
> Scope: I read the two changed paths, `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, as the work under check, following the rule in map-implementation-rules.md that an implementation node's work may be the effort's own record. I took no statement of intent from them. I unwrapped all text before searching it. Worktree: /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/80-fog-item. Base commit: 4d1e6b34.
>
> Condition, part by part:
> - Preamble (the work is these two files and no others are edited): `git -C <wt> status --short` and `git diff --numstat` show only these two paths. map-history.md is +10/-0 and map-manager-only.md is +1/-1. Neither the node status line, `decisions.md` nor `flags.md` is touched.
> - Part 1 (the item no longer says the seam is one step or that reject becomes a forward revert rather than a cleaned tree, and describes the seam and reject cost against the landing policy):
>   - Running `grep -c 'seam is one step\|forward revert\|cleaned tree'` over the item's line in the worktree returns 0.
>   - The new text names `## Landing an implementation node's work`. It lists the four steps on approval: a path-limited commit, a rebase onto the branch the manager thread is on, a re-run of the bar's commands, and `git merge --ff-only`.
>   - It states the reject today: the worktree is removed and its branch deleted. It states the reject after the flip: a revert commit, so reject becomes the costliest outcome.
>   - I checked these against that section's text in the same file, extracted with awk between `## Landing an implementation node's work` and the next `## `. They agree, including "with the sandbox off".
>   - The item also claims that `.claude/skills/expedition/SKILL.md` fixes "approval before any commit". That phrase is in SKILL.md under `### Three outcomes, and no fourth`.
> - Part 2 (the replaced text is appended verbatim under a heading mirroring the section it came from, and map-history.md loses nothing):
>   - I extracted the removed sentence from `git show 4d1e6b34:.scratch/graph-workflow/map-manager-only.md` with `grep -o 'The seam is one step.*marks history\.'`. `grep -Fxc` of it in the worktree's map-history.md returns 1, so it is byte-identical.
>   - It sits under `## Superseded from map-manager-only.md at node 80 …` / `### From ## Not yet specified — the item beginning "When to flip landing to asynchronous"`. That matches the heading pattern of the earlier entries in the file (`grep -n '^## \|^### '`).
>   - `git diff -U0 | grep -c '^-[^-]'` returns 0, so nothing was removed.
>   - The links in the intro resolve to node files that exist: nodes/80-… and nodes/366-….
> - Part 3 (no other item of map-manager-only.md changes): the diff of that file is one hunk changing one line, the "When to flip" bullet. Its opening "What is unspecified…" and "Shaped by…" text is unchanged; I compared it against the base.
> - Part 4 (scope came from no search): the condition records no command, so there was nothing to run.
>
> The bar:
> - The repo has no build, tests, formatter or CI. `git ls-files` finds no manifest, runner or lint config, as map-implementation-rules.md's `## What the work is held against` states. So the bar is the standards half alone.
> - `git diff --check` printed nothing (rc=0).
>
> Standards: I read only the standards in `.scratch/graph-workflow/map-implementation-rules.md` (`## What the work is held against` and the record-as-work rule). The work did not change that file. The standards that bore on this work:
> - The ground rules and the six standing rules for writing from the spawn. The new text cites by heading and not by line number. It has no bold except defined terms (it actually drops the old bold), puts one idea in each sentence, and has clear referents. The item states its current form and cites the nodes that shaped it.
> - `glossary.md`'s `_Avoid_` lines, checked by hand. "review", "reject" and "gate payload" are each used for the concept the glossary assigns them.
> - `graph-conventions.md`'s rule that superseded map text is appended verbatim to `map-history.md` under a heading mirroring the section. This is met.
> - `/coding-principles`, `/naming` and `/writing-for-agents` bore on nothing beyond the above, since the work is prose only.
>
> No reviewing skill is named for this repo, so I ran none.
>
> A note that is not a finding: the item's sentence "An implementation node superseded after its work has merged costs the same, because it is cleaned up in a reject's order" goes beyond SKILL.md's rule. That rule covers a node superseded "before its work has landed". The sentence reads as a projection of the rule onto the after-flip case. The condition neither asks for nor forbids this.

### Gate — approve, `standing yes`, 2026-10-02

Taken under the standing yes recorded in `map-manager-only.md` on 2026-09-27, scope text *"Approve all gates automatically"*. What was taken: the checker's run 1 outcome, `PASS`. No exclusion applies: the checker handed back no question and no raise, and its closing note is marked by it as not a finding. This settles none of the node's flags; they settle at the node closing report.

## Flags

`80.1` `ASSUMPTION` **· settled** — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

*The manager's note, 2026-09-27:* node 345's map pass carried out this node's clause 2 ("worktrees" is gone from the firstmate list in the fog item, old text in `map-history.md`) and found clause 1 already met. Clause 3, re-describing the async-landing seam and the price of a reject against today's landing lifecycle, is new analysis and stays open. The fog items sit in `map-manager-only.md`, which this node's condition does not name.

`80.2` `ASSUMPTION` **· settled** — *The worker's own text.* The condition names only the seam and the cost of a reject. I added two consequences that follow directly from the current policy: the gate payload can no longer point at uncommitted changes, and SKILL.md's fixed order "approval before any commit" breaks. I also added the case of a node superseded after its work has merged. I judged these to be part of "describing the seam" against the policy as it stands, not new items. I did not say what the flip does to a correction round, because the policy gives no ground for it.

## Amendment, 2026-09-29 (from node 366)

*Written by [node 366](366-triage-the-open-nodes-and-the-outstanding-flags.md)'s worker and filed by the manager, under the human's answer to node 366's Q3 (`verbatim`: *"ok"*). The worker's own text, pasted:*

Block 6 (node 80's condition, replaced whole, since it is unclaimed):
  > The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, and no other file is edited.
  > 1. The item under `## Not yet specified` beginning "When to flip landing to asynchronous" no longer says that the seam is one step, and no longer says that reject becomes a forward revert rather than a cleaned tree. It describes the seam and what a reject costs against the landing policy that the same file's `## Landing an implementation node's work` states: on approval, a path-limited commit, a rebase onto the branch the manager thread is on, a re-run of the bar's commands, and `git merge --ff-only`; on reject, the worktree is removed and its branch deleted.
  > 2. The item's replaced text is appended verbatim to `map-history.md` under a heading mirroring the section it came from. `map-history.md` gains text and loses none.
  > 3. No other item of `map-manager-only.md` changes.
  > 4. Scope came from no search: the item named is the place of the work.

*The manager's note, 2026-10-02:* flags 80.1, 80.2 settle at the node closing report that closes this node, which names its gate as taken under the standing yes.
