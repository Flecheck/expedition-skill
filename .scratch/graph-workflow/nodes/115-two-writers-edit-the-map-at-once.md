# Two writers edit the map at once when an implementation node's work is a map change

Type: grilling
Status: open

## Question

*Surfaced by [Carry the pick-report settling moment into the shipped files and the
map](103-carry-the-pick-report-settling-moment.md)'s worker, and pasted as it wrote it.*

> `.scratch/` is tracked, so an implementation node whose own work includes editing `map.md` edits the copy in its
> worktree — which is the last commit's — while the manager goes on editing the live copy in the main checkout,
> uncommitted. At node 103 the two had diverged in four places before the worker began. Two policy lines then pull
> against each other: the landing policy says the graph's files are *not* committed per node but periodically by the
> human, and it also says the manager makes one path-limited commit of that node's paths and merges `--ff-only` —
> which cannot run over a tracked path the main checkout has dirty. So what should happen: does such a node's map
> text travel back as text for the manager to apply, does the manager commit the graph before creating the worktree,
> is the map excluded from the worker's tree entirely, or something else?

**Blockers, in the worker's words:** *"none. Node 103's own map edit is affected and its gate is the first place the
collision bites."*

## The manager's note at filing

*Not a change to anything above.*

**The manager has already acted on this for node 103 alone, and that act is not an answer to this node.** It took the
worker's map and `map-history.md` text out of the worktree, applied it verbatim to the live copies in the main
checkout, and reverted the worktree's `.scratch/` — so node 103's commit carries its four shipped files only. Recorded
as flag `103.5`. **The route it took is the first of the four this question offers**, chosen because it was the only
one that needed no decision the manager is not entitled to make: the two files are the graph's own and the manager is
their only writer, so pasting a worker's text into them is scribe work. It is a one-node disposition and this node
decides the rule.

**One consequence the manager accepted and this node should weigh.** Under that route, **place 5 of node 103's
acceptance condition cannot be established in the tree its checker sees** — and the checker is blind to `.scratch/`
regardless, so it could never have established it. That is a second, sharper form of the collision: a condition may
name a place its own checker is forbidden to look at. Whether an acceptance condition may demand a change to the
effort's record at all is not something the four routes above settle.
