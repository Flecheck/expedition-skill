# The `recovered/` directory is a sixth file kind the graph's conventions do not define

Type: grilling
Status: open

## Question

*Surfaced by [What the manager reports to the human, in one place](46-what-the-manager-reports.md)'s worker, and
pasted as it wrote it.*

> `graph-conventions.md` fixes an effort's files at five, and `map.md` restates the count. The manager created a
> sixth kind under `recovered/` to carry a dead attempt's work into its replacement's spawn rather than through its
> own context, and named the deviation rather than hiding it. May an effort hold recovered material at all? If so,
> what is it, where does it live, who may write it, when is it deleted or promoted onto a node, and does the five-file
> count become six? If not, what carries a dead attempt's product to its replacement instead — the manager's context,
> an annotation on the node, or nothing?

**Blockers, in the worker's words:** *"none."*

## The manager's note at filing

*Not a change to anything above.*

**The deviation is the manager's own**, and this node exists because the worker that inherited the file reported it
rather than because the manager promoted its own shortcut. The instance: attempt 1 on node 46 died having spent
roughly 485k tokens scanning nodes 01–60, and its scan was written to
`.scratch/graph-workflow/recovered/46-scan-nodes-01-60.md` so attempt 2 could verify it instead of re-running it.
Attempt 2 did verify it, by twenty-two spot-checks, and reported the result — so the mechanism has one recorded use
and it worked.
