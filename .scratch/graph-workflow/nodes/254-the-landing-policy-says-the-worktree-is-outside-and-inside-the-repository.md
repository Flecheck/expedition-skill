# The landing policy says the worker's worktree is outside the repository and also inside it

Type: implementation
Status: open

Blocked by: none

## Question

*Surfaced by [node 249](249-gitignores-two-comments-point-at-files-that-moved.md)'s worker, and pasted as it wrote
it.*

> `map-manager-only.md`'s landing-policy paragraph opens by placing the worktree "**inside** the repository and
> ignored there", and then, five sentences later, justifies the gate payload naming the worktree's path with
> "because an implementation node's work is uncommitted in a checkout outside the repository and `git diff` where
> the human is standing does not show it". Inside and outside cannot both hold. The justification is the older of
> the two — it predates the human's instruction that moved the worktree inside — and the rule it justifies is still
> correct for a different reason: a harness worktree under `.claude/worktrees/` is ignored, so it is invisible to
> `git status` and to `git diff` in the main tree whether or not it is inside the repository. Which does the
> paragraph state, and does the stale clause go under the supersession route? Found while confirming this node's
> first pointer against the file it names; it is not a consequence of node 249's work.

**Blockers, in the worker's words:** *"none, but it overlaps two open nodes and the manager should sequence rather
than parallelise. It is **the same paragraph** as [node
237](237-the-landing-policy-and-the-worktree-bullets-name-two-paths.md)'s subject — that node has the path
contradiction in the paragraph's first sentence and this one has the inside/outside contradiction in a later
sentence — so the two are candidates to merge, and node 237's own unclaimability (its author could not establish
whether nodes 152 and 144 quote that paragraph's exact phrases) reaches this node identically. Separately, [node
231](231-a-gate-payload-stops-carrying-a-diff-command.md) is already editing the *end* of the same sentence,
removing the diff command from the gate payload; whichever of the two lands second meets the other's edit."*

## Acceptance condition

**None. The surfacing worker wrote none, said so, and said why** — pasted as it wrote it, and **not supplied by the
manager**:

> **None, and this is what is missing and why.** The repair cannot be specified until it is known whether `placed at
> `.worktrees/NN-<name>/` **inside** the repository` and the clause `uncommitted in a checkout outside the
> repository` are among the exact phrases that open node 152's and open node 144's acceptance conditions quote — the
> stated reason node 150's material was added *beside* the landing policy rather than rewritten into it. That is
> exactly the fact node 237's author named and could not establish, and it was not established here either: those
> two conditions are on nodes this worker was not given and did not read, and this node's own condition confined the
> work to `.gitignore`. Where no open condition quotes the clause, the condition is the straightforward one: replace
> `uncommitted in a checkout outside the repository` with wording that states why the work is invisible to the
> human's `git diff` without asserting the worktree is outside the repository, bank the replaced text verbatim to
> `map-history.md` under the heading mirroring the section it came from, touch no other file, write nothing in
> `decisions.md` or `flags.md`, leave every markdown link resolving, and meet the bar. Where an open condition does
> quote it, the node needs a different shape and the fork is the human's. **The manager should decide whether to
> file this at all or to fold it into node 237**, which holds the identical fork over the identical paragraph.

**This node may not be claimed until it carries a complete condition**, and the manager has not written one. Under
the manager's contract, authoring a condition for a node an agent minted is not the manager's; where that agent
wrote none, the manager says so to the human, and this is that.

## The manager's note at filing

*Not a change to anything above.*

**The manager filed this rather than folding it into [node 237](237-the-landing-policy-and-the-worktree-bullets-name-two-paths.md), and that choice is the human's to reverse in one line.** Its reason: the two nodes name different sentences, node 237 is unclaimable for a reason this node inherits rather than causes, and merging two unclaimable nodes produces one unclaimable node rather than a claimable one. Filing it separately keeps the second contradiction from being lost inside the first.

**The same fork blocks both nodes, and nobody has established it**: whether nodes 152's and 144's acceptance
conditions quote that paragraph's exact phrases. Two workers have now named that fact and stopped. It is one
`grep` by a party permitted to read those two conditions — and it is the same shape as [node
252](252-may-an-unclaimed-nodes-acceptance-condition-be-amended.md)'s subject, an unclaimed node's condition
governing whether other work can proceed.
