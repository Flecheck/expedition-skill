# The landing policy says an implementation node's work sits outside the repository

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 268](268-carry-the-plain-git-worktree-route-into-the-map.md)'s worker, and pasted as it wrote
it.*

> `map-manager-only.md`'s landing policy paragraph states, as the ground for the gate payload naming the worktree's
> path, *"because an implementation node's work is uncommitted in a checkout **outside** the repository and `git
> diff` where the human is standing does not show it"*. The checkout has been **inside** the repository since node
> 68, and under node 265's route it is inside the record directory itself. The clause is false and it is the stated
> reason for a rule that still binds.

**Blockers, in the worker's words:** *"none, but it sits in the same sentence [node
231](231-a-gate-payload-stops-carrying-a-diff-command.md) will rewrite when it removes the diff command from the
gate payload. **Folding this into node 231 is likely cheaper than running it alone**, and that is the manager's call
rather than this node's."*

## Acceptance condition

*Written by node 268's worker. Pasted as it wrote it, and not the manager's.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, and no
> other file may be edited. The worker may not mark this node, resolve it, or write a line in `decisions.md` or
> `flags.md`. Done means all of the following are true of the finished tree.
>
> 1. The `## Landing an implementation node's work` section of `map-manager-only.md` no longer states, as the ground
>    for any rule, that an implementation node's work is uncommitted in a checkout outside the repository.
> 2. The rule that sentence grounds — that the gate payload names the worktree's path — is still stated, and the
>    replacement ground says instead that the work is uncommitted, so it appears in no commit the human can read,
>    and that the path is how the work is found at all.
> 3. The replacement cites by markdown link the node that placed the worktree inside the repository, [Run an
>    implementation node's work in a worktree](68-implementation-in-a-worktree.md).
> 4. The displaced wording is appended verbatim to `map-history.md` under a heading mirroring the section it came
>    from, with any struck-through text staying struck through; `map-history.md` gains text and loses none.
> 5. The `## Landing an implementation node's work` heading is still present and the quoted phrase `How the worktree
>    is made` still occurs in `map-manager-only.md` — three pointers in the repository's `.gitignore` cite them.
> 6. No file outside the two named above is modified, `.gitignore` is not edited, and no file under
>    `.claude/skills/` is changed.
> 7. The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**This node was filed rather than folded into [node 231](231-a-gate-payload-stops-carrying-a-diff-command.md), and
its author said the fold is likely cheaper.** The manager filed it separately for one reason and states it so the
human can reverse it in a line: **folding would widen an open node's subject, which is not the manager's to do.**
Node 231's subject is removing the diff command from the gate payload; this is a false ground clause in the same
sentence. They are two repairs that collide rather than one repair.

**The fold is the human's call**, and the manager's own view is that the author is probably right about the cost —
whichever of the two lands second meets the other's edit in the same sentence, which is exactly the collision node
249's worker flagged about this paragraph months of nodes ago.

**This is the third defect found in that one paragraph.** [Node
237](237-the-landing-policy-and-the-worktree-bullets-name-two-paths.md) holds a path contradiction in its first
sentence; [node 254](254-the-landing-policy-says-the-worktree-is-outside-and-inside-the-repository.md) holds the
inside/outside contradiction and **carries no acceptance condition**, its surfacing worker having written none and
said why. **This node is the first of the three with a complete, satisfiable condition**, its author having been
inside the file with the route in hand. **Whether it supersedes node 254 outright is the human's**, and the manager
has not done it: node 254 names the same clause, and under node 264's widened rule a node made unnecessary by
another may now be superseded — but node 254's own question is broader than this condition, and the manager will not
narrow somebody else's question by retiring it.
