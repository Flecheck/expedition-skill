# Which harness route creates an implementation node's worktree

Type: grilling
Status: claimed

Blocked by: none

## Question

*Minted by the manager on the human's standing instruction. The question below is the manager's own.*

The human has directed that a worktree be created by the harness rather than by hand. **The instruction is settled and
is in the map**; what it does not settle is which harness route carries it, and the two are not interchangeable.

**Their words**, `verbatim`:

> when you use worktrees, you should use the EnterWorktree skill instead of creating worktrees by hand - that way you
> don't have all these worktree management issues afterwards

**Why a route still has to be chosen.** `EnterWorktree` switches **the calling session** into the worktree. The
manager is the one party that must stay in the main tree: it owns the graph, and every node file, `decisions.md` and
`flags.md` write it makes is to the main checkout. The parties that need to be *in* the worktree are the **worker**
that writes the code and then the **checker** that reads it — two different agents, across a span that outlives
both, because the tree must survive until the human's gate.

**What each route costs, as far as the manager can state it without deciding:**

- **The manager enters the worktree** — matches the instruction's named tool literally, and puts the manager where
  the diff is. Against it: the manager would be writing the graph from inside a worktree, and the graph is the main
  tree's.
- **The worker is spawned with harness worktree isolation** — puts the harness-managed tree around the party that
  actually writes, and the checker is pointed at the path afterwards. Against it: it is not the tool the human named,
  and the manager has not established that such a tree survives the worker's exit in the way the gate needs.

**What this node decides:** which route the effort uses, and consequently what the map's landing policy says the
manager does when an implementation node starts.

## The manager's note at filing

*Not a change to anything above.*

**The instruction itself is not in question and is already in force**, written into `map.md` beside the landing policy
under [Rules added to one effort's map, and what makes them legitimate](93-effort-scoped-custom-rules.md). This node
is the fit, not the direction.

**What produced it**, recorded because it is the evidence either route has to beat: the manager created node 147's
worktree with `git worktree add` and then could not remove it. The sandbox bind-mounts `.git/config` read-only and
makes `.git/worktrees/<name>` its own mountpoint, so both `git worktree remove` and `git worktree prune` returned
`EBUSY`. The entry stayed in `git worktree list` as `prunable`, and **this effort discovers a code slot's occupancy
by counting live worktrees**, so a stale entry reads as an occupied slot. It was cleared only by re-running the prune
outside the sandbox.
