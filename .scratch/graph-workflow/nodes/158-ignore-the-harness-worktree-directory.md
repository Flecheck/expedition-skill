# Ignore the harness's worktree directory

Type: implementation
Status: claimed

Blocked by: none

## Question

*Surfaced by [Which harness route creates an implementation node's
worktree](150-which-harness-route-creates-a-worktree.md)'s worker, and pasted as it wrote it.*

> The repository's `.gitignore` ignores `.worktrees/`, the path the landing policy used when the manager created
> worktrees by hand. The harness creates them at `.claude/worktrees/` instead, which no rule covers, so a live
> worktree appears as untracked in the main tree's `git status`, is traversed by repo-wide searches, and has been
> observed duplicating this workflow's own skill files into the manager's context.

**Blockers, in the worker's words:** *"none."*

## Acceptance condition

*Written by node 150's worker. Pasted as it wrote it, and not the manager's.*

> After the work, the file `.gitignore` at the repository root contains an entry that causes git to ignore the
> directory `.claude/worktrees/`, immediately preceded by a comment stating that this directory holds the git
> worktrees the agent harness creates for implementation workers, and that it is ignored so those worktrees are never
> committed. The file's existing entry ignoring `.worktrees/` is still present, and the existing comment lines above
> it are still present and unaltered. Running `git status --porcelain` from the repository root produces no line
> whose path begins with `.claude/worktrees`. No file other than `.gitignore` is changed anywhere in the repository.
> The working tree meets the bar.

## The manager's note at filing

*Not a change to anything above.*

**The pollution is confirmed in the manager's own context**, not only in `git status`: the harness surfaced all seven
`expedition*` skills a second time, scoped to `.claude/worktrees/agent-ac549d7fb8ff2bf22/`, in the manager's skill
list. Every agent spawned while a worktree is live pays for that.

**The manager did not make this one-line change itself**, though it could have and was tempted to. Having already
acted once today on its own authority in breach of its contract — flag `140.8` — it minted the node instead.

**Flag `68.2` bears on it and stays open**: it recorded that an ignore rule could not be assumed for a repository the
workflow does not own. This node's condition is scoped to this repository only and asserts nothing about any other.

## Flags

*Each entry is the worker's own prose, pasted. The manager added the id and the marker and nothing else.*

`158.1` `ASSUMPTION` — **The comment says more than the condition demands.** The condition demands the comment state
two things: that the directory holds the harness's worktrees for implementation workers, and that it is ignored so
they are never committed. Both are stated in the first two lines. I added two more — that `.worktrees/` above is the
path the landing policy used when the manager made worktrees by hand, and a pointer to
`map-implementation-rules.md`'s "How the worktree is made". My ground: a reader meeting two near-identical worktree
entries with no stated relationship has to go and derive which is live, and that derivation is what the third line
spends four words preventing. The condition does not forbid extra content and nothing added contradicts it, but the
choice was mine.

`158.2` `ASSUMPTION` — **The stale pointer frozen by my own condition was surfaced as a node rather than raised.**
The existing comment I am required to leave unaltered ends "See `.scratch/graph-workflow/map.md`, the landing
policy", and the landing policy moved out of `map.md` to `map-implementation-rules.md` at node 140. That pointer is
therefore stale, and my condition forbids me to fix it. This is arguably raise trigger 1 — a broken thing that is not
mine to change. I decided against a raise on two grounds: the pointer still *resolves*, since `map.md` carries an
explicit forwarding line naming `map-implementation-rules.md` and the landing policy among its contents, so it costs
a reader one extra hop rather than failing; and a raise would spend the human's single live question on a one-hop
pointer when the node route carries it for nothing. Reported under NODES SURFACED instead. If the human would rather
I had raised, this is the judgement to revisit.

## The manager's note after the handover

*Not a change to anything above.*

**This node verified the one step of the worktree route that was still unmeasured.** Its first reported facts were
its own `pwd` — the worktree the spawn named — and its `HEAD`, `6795ca9`, the manager's `HEAD` at spawn. **So a
worker spawned while the manager is inside a worktree does inherit it.** Flag `150.3` is unchanged, its subject being
the other direction — pointing a *replacement* at a surviving worktree when resume is unavailable.

**Its invalidation is against the map and is the manager's to carry.** `map-implementation-rules.md`'s bar paragraph
says *"the one ignore file, `.gitignore`, ignores `.worktrees/` and invokes nothing"*, which this work makes
incomplete in the same way node 114's check once found it. **The load-bearing half — *and invokes nothing* — still
holds**, so the bar itself does not move. The manager has not amended the sentence while this node is claimed and its
own condition forbids it to touch that file; the amendment is made when this node lands.

**Its retrospective found a live contradiction the manager confirms**: `map.md`'s ground rule 5 still locates the
prose standard by plugin name, while `decisions.md` records [node
132](132-does-the-plugin-direction-reach-the-efforts-own-bar.md) as having settled that it states its demands in the
rules file instead. The repair is [node 149](149-state-the-prose-standards-demands-in-the-rules-file.md), which is
blocked on node 144 and has not landed. **Nothing in either file says a settled decision is not yet carried out**,
and the worker's point stands: a worker cannot tell a not-yet-landed decision from a broken one.
