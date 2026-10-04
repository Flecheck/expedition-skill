# Whether the worktree lifecycle is worth putting behind a script

Type: grilling
Status: claimed

Blocked by: none

## Question

*Surfaced by [node 265](265-should-the-worktree-route-drop-enterworktree-for-git.md)'s worker, and pasted as it
wrote it. **The question inside it is the human's own**, given alongside node 265's and deliberately held back from
that payload because its answer depended on node 265's.*

> The human's own, `verbatim`: *"We can maybe create a script to do to simplify the work"*. Node 265 settled which
> route a script would automate and did not settle whether to build one. The lifecycle is now four plain git
> commands — create, the `test -w` check, remove, delete branch — with no harness tool in the path, so a script can
> carry the whole of it for the first time. What a script would have to be worth: it would be the first executable
> artifact this effort ships, it would need to work on a repository this machine has never seen under ground rule 1,
> and the alternative is four commands written in the map.

**Blockers, in the worker's words:** *"none. Node 265 has settled what it depended on."*

## The manager's note at filing

*Not a change to anything above.*

**The manager has now run the new route once, by hand, and offers that as material rather than as a position.**
Creating [node 269](269-ignore-the-new-worktree-path.md)'s worktree was four things in one command line: the `test
-w` check, `git worktree add -b`, and two reads confirming the tree landed on `HEAD`. It needed no reset and no
sandbox override, and it is the first worktree this effort ever made without a harness tool.

**What the manager does not know and will not guess**: whether four commands run twice per node is friction worth an
artifact, or whether the friction the human was reacting to was the *old* route's reset and override — both of which
node 265 removed without any script at all.

**Ground rule 1 is the sharp edge here and it is not a formality.** *"Nothing in the shipped files may assume this
repo, this machine, or a toolchain."* A script is a toolchain assumption in a way four documented commands are not,
and this effort has never shipped an executable. Whoever works this should treat that rule as the question rather
than as an obstacle to route around.
