# The landing policy and the worktree bullets name two different worktree paths

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 229](229-bank-the-landing-sections-accounts-out-of-map-manager-only.md)'s worker, and pasted as
it wrote it. Found outside its own fourteen spans and left there.*

> The landing policy paragraph says the worker's worktree is `placed at \`.worktrees/NN-<name>/\` **inside** the
> repository`, while the bullet six paragraphs down says `The path is \`.claude/worktrees/<name>/\` and the branch
> \`worktree-<name>\``. The second is what the harness actually does and what `.gitignore`'s second entry was added
> for at node 158; the first is the hand-rolled path the route abandoned. Both currently read as binding. Which path
> does the landing policy state, and does the stale one go under the supersession route?

**Blockers, in the worker's words:** *"none."*

**Its author's note for whoever specifies this, pasted:** *"node 152's and node 144's acceptance conditions quote
that paragraph's exact phrases, which is the stated reason node 150's material was added beside the landing policy
rather than rewritten into it — so an edit to that paragraph has to be checked against those two open conditions
first."*

## Acceptance condition

**None, and its author deliberately wrote none.** Pasted as it wrote it:

> Not written, and this is what is missing and why. The work turns on whether the phrase `placed at
> \`.worktrees/NN-<name>/\` **inside** the repository` is one of the exact phrases open node 152's or open node
> 144's acceptance condition quotes. I did not settle that — both conditions are on nodes I was not given and did
> not read, and my own node forbade me to widen past its fourteen spans to find out. Where the phrase is quoted by
> an open condition, the repair is not a free edit and the node needs a different shape; where it is not, the
> condition is the straightforward one: replace the stale path with `.claude/worktrees/<name>/`, bank the replaced
> text verbatim to `map-history.md`, touch no other file, write nothing in `decisions.md` or `flags.md`, leave every
> markdown link resolving, and meet the bar. **That fork is what should go to the human before this node is
> claimed.**

## The manager's note at filing

*Not a change to anything above.*

**Its author named the one fact that decides the node's shape and said it could not establish it.** The manager can,
and has not — establishing it means reading two open conditions, which costs nothing, but **the fork its author
named is the human's** rather than something the manager should pre-empt by settling the fact and then writing the
condition it implies. **This node is therefore unclaimable until the fork is put to the human**, and the manager has
written no acceptance condition, which is the same refusal it makes wherever a condition's author wrote none.

**What the manager can say from its own session without reading anything.** Every worktree it has created today sat
at `.claude/worktrees/<name>/`, created by `EnterWorktree`, with the branch `worktree-<name>` — five of them. **The
`.worktrees/NN-<name>/` path has not been used once.** So the stale statement is stale in fact as well as by
record, and the only open question is the one its author named: whether an open condition quotes it.
