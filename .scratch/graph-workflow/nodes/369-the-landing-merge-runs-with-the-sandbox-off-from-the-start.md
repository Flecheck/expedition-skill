# The landing merge runs with the sandbox off from the start

Type: implementation
Status: claimed
Blocked by: ~~234~~

## Question

Should the landing policy say that `git merge --ff-only` into the main tree always runs with the sandbox off? The sandbox mounts the main checkout's `.claude/skills` read-only, so a merge run inside it can fail after writing part of its result. Every landing merge on 2026-09-28 ran with the sandbox off from the start, and none partially wrote.

*Reported by [node 234](234-a-failed-merge-can-leave-the-tree-partially-updated.md)'s worker under its `NEW NODES`, and filed by the manager. Its words on blockers: "none. It edits `.scratch/graph-workflow/map-manager-only.md`, which node 234 also edits, so the two must not run in the same pair of code slots." The manager made the edge to node 234.*

## Acceptance condition

*Authored by node 234's worker and filed by the manager.*

> The work is `.scratch/graph-workflow/map-manager-only.md` and `.scratch/graph-workflow/map-history.md`. The worker may edit those two files and no other.
> Done means every one of the following is true of the finished tree.
> 1. In `map-manager-only.md`, under the heading `## Landing an implementation node's work`, the paragraph beginning `**Landing policy**` states that the manager runs `git merge --ff-only` with the sandbox off, and states the reason: the sandbox mounts `.claude/skills` in the main checkout read-only, so a merge run inside it can fail after writing some of the changed files.
> 2. Where a sentence stating a rule that currently binds is replaced to meet clause 1, its text before the change is appended, unaltered, to `map-history.md` under a heading naming `map-manager-only.md` and this node, with a subheading naming *Landing an implementation node's work*. It is appended rather than replacing anything.
> 3. The text in the same section that states the repair for a partially written merge (confirm that each dirty file is byte-identical to the branch's version, discard, then re-run the merge outside the sandbox, and stop without discarding where any file differs) is still present, and says it applies where a merge was run inside the sandbox.
> 4. Every markdown link in both files resolves to a path that exists, except a link to a path outside this repository.
> 5. No file outside `.scratch/graph-workflow/` is modified.
> Scope came from no search: the named places are the work.

## Handover, attempt 1

*The worker's own text, pasted, 2026-09-29.*

```
HANDOVER:      369, "The landing merge runs with the sandbox off from the start"

ANSWER:        In `.scratch/graph-workflow/map-manager-only.md`, under `## Landing an implementation node's work`, the `**Landing policy**` paragraph gains four sentences, placed right after "...merges with `git merge --ff-only`, then removes the worktree and deletes the branch." and before "A rebase conflict is resolved, and the rebase is not aborted.":
               "The manager runs `git merge --ff-only` with the sandbox off, on the first attempt as well as on any retry. The reason is that the sandbox mounts `.claude/skills` in the main checkout read-only, so a merge run inside the sandbox can fail after writing some of the changed files. The repair for a merge that was run inside the sandbox is in the bullet *One sandbox restriction bites this lifecycle* below. Settled at [node 369](nodes/369-the-landing-merge-runs-with-the-sandbox-off-from-the-start.md)."
               In the same section, in the sub-bullet "What it hits", two sentences go in right before "The repair for a partially written merge is one pass, in this order.": "The landing policy above has the manager run the merge with the sandbox off. The repair that follows applies where a merge was run inside the sandbox despite that rule." Node 234's repair text (byte-identity first, discard outside the sandbox, re-merge, stop where a file differs) is otherwise unchanged.
               Decisions a later reader would otherwise have to re-derive:
               - Both changes are additions. No sentence stating a binding rule was replaced, so the conditional clause 2 did not trigger and `map-history.md` is untouched. The existing sentence already lists `git merge --ff-only` as a landing step, and the new sentences add to it without contradicting it.
               - "on the first attempt as well as on any retry" carries the node's "from the start". The old practice was to retry outside the sandbox only after a failure inside it.
               - The reason sentence says "inside the sandbox" rather than "inside it", because "it" could also refer to the main checkout.
               - The repair stays in place as the fallback. The sandbox's read-only overlay on `.claude/skills` in the main checkout still exists, and the repair covers a merge that was run inside the sandbox by mistake.
               - "The manager must expect this rather than discover it" and the sub-bullets' lead-in ("what bites it is unchanged") are left as they are. Both are still true: the failure still happens inside the sandbox, and the new rule is how the manager expects it.

INDEX LINE:    The landing policy now has the manager run `git merge --ff-only` with the sandbox off from the first attempt, since the sandbox's read-only `.claude/skills` can partially write a merge; the repair remains the fallback.

FLAGS:         ASSUMPTION: Clause 1 is met by adding sentences to the `**Landing policy**` paragraph, not by rewriting its existing sentence that lists the landing steps. So no binding rule text was replaced, and clause 2 (conditional, "Where a sentence ... is replaced") bound nothing, and `map-history.md` was not touched. Grounds: the existing sentence stays true as written, and adding to it is the smallest change that meets the clause.
               Index sentence: Node 369 met its landing-policy change by adding sentences instead of replacing any, so nothing was banked in map-history.md.

NEW NODES:     none

INVALIDATIONS: Node 234 (a sandbox-failed merge can partially write the tree): narrowed, not contradicted. Its repair is now the fallback for a merge run inside the sandbox against the landing policy, not a step the manager should expect to reach on an ordinary landing. Its text is kept, with the new scoping sentence placed before it. Node 115 / node 160 (the landing policy's rebase-and-merge sequence): extended with how the merge step is run. Their rebase-conflict text is untouched.

CONDITIONS:    Searched every open and claimed node's `## Acceptance condition` and `## Question` for "Landing policy", "sandbox off", "ff-only", "partially written", "What it hits", "One sandbox restriction", "merge --abort" and "sandbox mounts". Matches besides this node: node 152 (condition names the paragraph beginning `**Landing policy**` only as a place in another file; it is already annotated as unsatisfiable because of node 188, and my work does not change that), node 80 (condition lists the four landing steps including `git merge --ff-only`; still accurate, since the step list is unchanged), node 251 (question notes the ff-only merge was run with the sandbox off and not retested; consistent with my work), node 180 (question: does knowing which trees get the read-only overlay make the landing route's "needs the sandbox off" cases predictable in advance). My work partly answers node 180 for the merge: the landing merge now always runs with the sandbox off, so it no longer needs predicting. The rest of node 180's question is untouched, namely which trees carry the mounts and the removal case. No replacement clauses written.

MISSING FROM MAP: none

GATE PAYLOAD:  Checker findings: none yet.
               Paths touched, in worktree `/home/mathieu/projects/graph-agent/.scratch/graph-workflow/worktrees/369-merge-unsandboxed`:
               - `.scratch/graph-workflow/map-manager-only.md` (the only modified file; `git status --porcelain --untracked-files=all` lists nothing else)
               Checks run against the condition:
               - Clause 1: the four sentences are inside the `**Landing policy**` paragraph and state the rule and the reason.
               - Clause 2: no rule sentence was replaced, so nothing is banked.
               - Clause 3: the repair text is present and unchanged, now preceded by "The repair that follows applies where a merge was run inside the sandbox despite that rule."
               - Clause 4: every relative `](...)` target in both files, with any anchor stripped, passes `[ -e ]`. That includes the new link to the node-369 file.
               - Clause 5: only the one file under `.scratch/graph-workflow/` is changed.
               Writing rules: the added text has no bold. The only added diff line containing `**` is the whole `**Landing policy**` paragraph line, whose existing bold spans are unchanged. I re-read each pronoun I added.
               The bar: the repo root holds `.claude`, `CONTEXT.md`, `CONTEXT-MAP.md`, `.gitignore` and `.scratch`. There is no build, test suite, formatter or CI, which matches `map-implementation-rules.md`. There was no command to run, and there is no difference to report.
               On `git merge --abort` (your note): the statement is accurate. A failed `--ff-only` merge writes no `MERGE_HEAD`, and `git merge --abort` then only exits with "There is no merge to abort (MERGE_HEAD missing)" and changes nothing. It belongs, if anywhere, as one clause in the "What it hits" repair, where a manager would reach for it first. My recommendation is to leave it out: under the new rule the repair is a rare fallback, and trying `--abort` fails harmlessly. Not added.
               Proposed commit message:
               Run the landing merge with the sandbox off from the first attempt

               The sandbox mounts .claude/skills in the main checkout read-only, so a
               merge run inside it can fail after writing some of the changed files.
               The landing policy now has the manager run git merge --ff-only with the
               sandbox off on every attempt, and the partial-write repair states that
               it applies only to a merge that was run inside the sandbox.

               Node: graph-workflow/369

RETROSPECTIVE
1. What I had to hunt for: nothing much. I confirmed that the two passages the condition names still matched after node 234 and node 160, and I found the human's question in node 234's gate answer rather than under a heading of its own.
2. What arrived that this node did not need: most of node 234's file (checker runs, both handovers), since only the gate answer and the manager's note bore on this node.
3. What would have made this easier: the spawn pointing at the heading "The human's answer at the gate, 2026-09-29" in node 234, and the condition saying plainly whether adding sentences with no replacement is acceptable for clause 2, which I settled with a flag.
4. What was stale, wrong or contradictory: node 234's "Checker run 1 — FAIL" section holds the wrong checker text. It is the check of node 297 ("Rewrite the manager contract's second part in plain English", worktree 297-rewrite-the-manager-contract-part-2), not of node 234. The record of node 234's first check is therefore missing, and the manager's note under it refers to findings that text does not contain.
```

## Flags

`369.1` `ASSUMPTION` — *The worker's own text.* Clause 1 is met by adding sentences to the `**Landing policy**` paragraph, not by rewriting its existing sentence that lists the landing steps. So no binding rule text was replaced, and clause 2 (conditional, "Where a sentence ... is replaced") bound nothing, and `map-history.md` was not touched. Grounds: the existing sentence stays true as written, and adding to it is the smallest change that meets the clause.
