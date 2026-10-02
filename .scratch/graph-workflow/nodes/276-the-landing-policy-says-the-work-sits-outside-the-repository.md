# The landing policy says an implementation node's work sits outside the repository

Type: implementation
Status: claimed
Supersedes: 254

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

## Handover, attempt 1

*The worker's own text, pasted, 2026-10-02.*

````
HANDOVER:      The landing policy says an implementation node's work sits outside the repository

ANSWER:        In `.scratch/graph-workflow/map-manager-only.md`, under `## Landing an implementation node's work`, the landing policy paragraph had one sentence that grounded the gate-payload rule on a false claim: "because an implementation node's work is uncommitted in a checkout outside the repository and `git diff` where the human is standing does not show it". That sentence is replaced, and the rest of the paragraph is unchanged. The new text keeps the rule (**The gate payload names the worktree's path**) and keeps its citations of nodes 231 and 336. It now gives this ground: the work is uncommitted, so it appears in no commit the human can read, and the path is how the work is found at all. Next comes one sentence saying the worktree is inside the repository. That sentence cites [Run an implementation node's work in a worktree](nodes/68-implementation-in-a-worktree.md) by markdown link and says the worktree is ignored there, so its changes do not show in the human's `git status` or `git diff`. I confirmed the ignore with `git check-ignore`, which matches `.gitignore`'s `.scratch/graph-workflow/worktrees/` line. The human's quoted words ("what are the changes ? I don't see them in git ?") stay as the evidence. The paragraph's first sentence also contains "a worktree outside the repository". That is part of an account of what led to the human's instruction, it grounds no rule, and it was left alone. The displaced sentence was appended verbatim to the end of `.scratch/graph-workflow/map-history.md` under `## Superseded from map-manager-only.md at node 276 — the landing policy's ground for naming the worktree's path` / `### From *Landing an implementation node's work* — the landing policy's sentence on what the gate payload names`. It has no struck-through text. map-history.md only gained text. The section heading is still present, and `How the worktree is made` still occurs 3 times in map-manager-only.md.

INDEX LINE:    The landing policy now says the gate payload names the worktree's path because the work is uncommitted and the path is how it is found, not because it sits outside the repository.

FLAGS:         ASSUMPTION: Clause 3 of the condition writes the node 68 link target as `68-implementation-in-a-worktree.md`, which is relative to `nodes/`. From `map-manager-only.md` that target would not resolve, so I wrote `nodes/68-implementation-in-a-worktree.md` with the condition's link text, the same form the paragraph already uses for node 68 at its end. I made the change by direct edit, with no interview and no gate before this handover. — Index: The node-68 link in the landing policy uses the `nodes/` path that resolves from map-manager-only.md, not the bare filename the condition wrote.

NEW NODES:     none

INVALIDATIONS: none. The edit narrows no resolved node. Node 68's placement inside the repository is now stated where the false clause was.

CONDITIONS:    I searched the `## Acceptance condition` and `## Question` sections of every open and claimed node for "outside the repository", "uncommitted in a checkout", "names the worktree's path", "gate payload", "where the human is standing" and "Landing an implementation node". The only match is this node. Nodes 231, 237 and 254 also name the sentence, and all three are superseded. Node 209's question mentions "The rules file's `## Landing an implementation node's work` section", which this work does not touch, and it needs no change from this node. I wrote no replacement clauses.

MISSING FROM MAP: none. The map-history heading convention was taken from the existing entries in map-history.md.

GATE PAYLOAD:  No checker findings yet. Paths touched: `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`, in worktree /home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/276-landing-ground. Nothing is committed. Bar: the repo has no build, tests, formatter or CI. The root holds only `.claude`, `CONTEXT-MAP.md`, `CONTEXT.md`, `.gitignore` and `.scratch`, which matches what map-implementation-rules.md records, so the bar is its non-command half. `git diff --check` is clean. The manager's note about node 211 holds: my append goes at the very end of map-history.md, after the node 219 entry, so it will meet node 211's append there. Both sides are text held under the never-delete rule, so the merge keeps both. Proposed commit message:
  "Ground the gate payload's worktree path on the work being uncommitted

  The landing policy said the work sits in a checkout outside the repository; it has been inside since node 68. The displaced sentence is banked in map-history.md.

  Node: graph-workflow/276"

RETROSPECTIVE:
1. What I had to hunt for: where node 68 says the worktree moved inside the repository (its section `### 1. The worktree moves inside the repository`), and whether nodes 231 and 254 were still open. Both are superseded.
2. What arrived that this node did not need: most of map.md and map-implementation-rules.md. Of the decisions.md lines for nodes 68 and 265, only node 68's was used.
3. What would have made this easier: a condition that wrote the link target relative to the file being edited (`nodes/68-...`).
4. What was stale, wrong or contradictory: clause 3's link target does not resolve from map-manager-only.md, as flagged above. Node 209's question still calls the landing section part of "the rules file", but it moved to map-manager-only.md at node 188. The manager's notes checked out: the phrase was present, and the second mention of "outside" is in an account.
````

## Flags

`276.1` `ASSUMPTION` — *The worker's own text.* Clause 3 of the condition writes the node 68 link target as `68-implementation-in-a-worktree.md`, which is relative to `nodes/`. From `map-manager-only.md` that target would not resolve, so I wrote `nodes/68-implementation-in-a-worktree.md` with the condition's link text, the same form the paragraph already uses for node 68 at its end. I made the change by direct edit, with no interview and no gate before this handover.
