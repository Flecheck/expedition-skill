# Update the map items that nodes 64 and 68 left stale

Type: implementation
Status: open

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

## Flags

`80.1` `ASSUMPTION` — *The manager's own entry, carrying the amendment above as the amendment rule requires.* The acceptance condition was amended from [node 299](299-rewrite-graph-conventions-part-1.md)'s re-pointing list, on the ground that every word of the replacement is fixed by commit `0d406b7`.

*The manager's note, 2026-09-27:* node 345's map pass carried out this node's clause 2 ("worktrees" is gone from the firstmate list in the fog item, old text in `map-history.md`) and found clause 1 already met. Clause 3, re-describing the async-landing seam and the price of a reject against today's landing lifecycle, is new analysis and stays open. The fog items sit in `map-manager-only.md`, which this node's condition does not name.
