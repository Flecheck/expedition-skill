# Map: what only the manager acts on

No worker reads this file.

## Notes

- **Label vocabulary.** `RENAME` for the repository's rename, `SPLIT` for several deliverables in one
  effort, `UPGRADE` for turning a conversation into an expedition.
- **Counts.** Two nodes that need the human run at once. Two code slots, set by the human, `verbatim`:
  *"You can run 2 code slot, I think it should be the default."* The human sets both, and may move
  either. Two is now the shipped default, from [node 16](nodes/16-two-code-slots-by-default.md).

## Landing an implementation node's work

The landing policy is the one the root `CLAUDE.md` states under `## The worktree of an implementation
node`: a worktree made with plain `git worktree add` at
`.scratch/rename-split-upgrade/worktrees/<NN>-<name>`, on a branch `worktree-<NN>-<name>`, created from
the repository root with `git -C <repo root>`. On approval the manager makes one path-limited code
commit on that branch carrying the node trailer, fast-forwards the main checkout to it, and removes the
worktree and the branch. The merge and the removal run with the sandbox off. On a reject or a
supersession before landing, the graph is edited first and the worktree and branch are removed after.
Where integrating conflicts, the manager starts a correction round naming the conflicted paths.
Nothing is pushed without the human's word.

The human, on how this repository lands work, `verbatim`: *"Also I would guess that in this repo, I would not push the branch and make a pull request but direclty merge to master as I am the only one. But I guess most of the time it would be push of the branch and then a pull request"*. A deliverable can land that way, by a local base, from [node 08](nodes/08-a-deliverable-that-lands-by-merging-locally.md).

## Not yet specified

## Out of scope
