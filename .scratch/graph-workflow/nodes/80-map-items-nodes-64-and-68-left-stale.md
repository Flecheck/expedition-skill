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
