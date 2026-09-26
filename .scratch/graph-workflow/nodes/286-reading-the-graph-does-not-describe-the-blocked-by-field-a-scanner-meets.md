# `Reading the graph` does not describe the `Blocked by:` field a scanner will meet

Type: implementation
Status: superseded
Superseded by: 339

Blocked by: none

## Question

*Surfaced by [node 273](273-a-script-that-answers-what-can-be-started.md)'s worker, and pasted as it wrote it.*

> `graph-conventions.md` states `Blocked by:` as `NN, NN`, but the never-delete rule makes the field hold
> struck-through numbers, markdown links, prose and commit hashes in code spans. `## Reading the graph` carries two
> scan rules for exactly this class of hazard and is missing the one that bites hardest.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 273's worker. Pasted as it wrote it, and not the manager's.*

> `.claude/skills/expedition/graph-conventions.md`, under its existing `## Reading the graph` heading, carries a
> third numbered rule alongside the two it already holds (*"Read fields only from the header block"* and *"Skip
> fenced code blocks"*).
>
> The new rule states that the `Blocked by:` field is written under the never-delete discipline, so a blocker that
> has been satisfied is **struck through in place rather than removed**, and the field may also hold markdown links
> to node files, explanatory prose, and commit hashes inside code spans. It then states the rule a scanner follows:
> **take a node number from that field only where the number lies outside every backtick-delimited code span,
> outside every `~~...~~` strikethrough, and outside the parenthesised target of every markdown link.**
>
> It gives **at least three** short quoted examples of forms the field actually takes, each paired with what a
> scanner must take from it. **At least one example must be a struck-through blocker from which nothing is taken**,
> and **at least one must be a form whose code span holds digits that must not be read as a node number.**
>
> `## Edges` is left unchanged: the canonical form `Blocked by: NN, NN` that it states stays as it is, and the wider
> set of forms a scanner will actually meet is stated only in `## Reading the graph`.
>
> No file other than `graph-conventions.md` changes.

## The manager's note at filing

*Not a change to anything above.*

**The measurement behind this is its author's and is worth keeping**: **thirty-two open nodes' `Blocked by:` fields
do not look like the canonical form** the document states. The manager's own bookkeeping is a large part of why —
every satisfied blocker this session was struck in place with a prose clause and a commit hash beside it, which is
what the never-delete rule asks for and what a scanner then has to survive.

**Its author built a scanner against the live corpus before writing this**, so the three-clause rule and its
examples are drawn from forms that actually occur rather than from forms imagined. **The four worked examples in
[node 285](285-ship-the-frontier-script-and-say-what-it-cannot-answer.md)'s condition are the same measurement from
the other side**, and whoever claims either node should read both — one states the rule, the other tests it.

**`## Edges` staying unchanged is the deliberate half.** The canonical form is what a *writer* follows; the wider
set is what a *reader* meets. Conflating them would make the format's statement of itself untrue.

**Sequencing, which is the manager's.** `graph-conventions.md` is the most contended file on this effort — one
worker measured **nineteen** open nodes editing it and another **twenty-seven** conditions naming it, and several
demand it change in no other respect. **Two workers must not hold it at once.**

## Superseded, 2026-09-26

*The manager's note.* Replaced by [node 339](339-tie-graph-conventions-mds-mechanical-checks-to-the-writes-that.md), the merge [node 330](330-group-the-open-nodes-against-the-manager-contract.md)'s worker proposed, on the human's "ok". This node's demands are carried there, tagged with this node's number; the question and acceptance condition above are superseded as a whole.
