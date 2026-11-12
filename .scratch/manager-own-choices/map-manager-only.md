# Map: what only the manager acts on

No worker reads this file.

## Notes

- **Label vocabulary.** This effort declares none.
- **Counts.** Two nodes that need the human run at once. Two code slots. These are the shipped
  defaults. The human sets both, and may move either.
- **Standing yes 1, for commits on the deliverable branches.** The human, `verbatim`, 2026-11-12:
  *"Would you normally ask for my approval before delivering? If yes, standing yes for commits on
  feature branches dedicated to deliverables, in the current effort."* Its scope text: "commits on
  feature branches dedicated to deliverables, in the current effort". It covers the gate of an
  implementation node that names a deliverable, taken on the checker's `PASS`, under the skill
  `expedition-standing-yes`. The human then clarified, `verbatim`: *"by "before delivering" I meant
  "before merging the branch of the deliverable into HEAD""*. A deliverable reaches `master` only
  through its pull request after a push on the human's yes, or through a local merge on the human's
  yes, so the standing yes's condition holds.
- **Standing yes 2, for pushing feature branches.** The human, `verbatim`, 2026-11-12: *"standing yes
  for pushing feature branches"*. Its scope text: "pushing feature branches". It covers a push of a
  deliverable's branch, under the skill `expedition-standing-yes`.
- **The main checkout is the human's.** The human, `verbatim`, 2026-11-12, after the manager switched it back to `master`: *"the switch was not an accident, I was reviewing the PR"*. Leave the main checkout's branch as the human set it. Where a deliverable branch the human has checked out must move, move it inside that checkout by fast-forward, so its files follow.
- **Node 05 waits for Flecheck.** [Node 05](nodes/05-whether-to-port-three-lost-graph-workflow-rules.md)
  is to be "handled by flecheck", in the human's words recorded on it. Start it only once the human
  says Flecheck is there to answer it.

## Landing an implementation node's work

The landing policy is the one the root `CLAUDE.md` states under `## The worktree of an implementation
node`: a worktree made with plain `git worktree add` at
`.scratch/manager-own-choices/worktrees/<NN>-<name>`, on a branch `worktree-<NN>-<name>`, created from
the repository root with `git -C <repo root>`. On approval the manager makes one path-limited code
commit on that branch carrying the node trailer, fast-forwards the main checkout's `master` to it, and
removes the worktree and the branch. The merge and the removal run with the sandbox off. On a reject or
a supersession before landing, the graph is edited first and the worktree and branch are removed after.
Where integrating conflicts, the manager starts a correction round naming the conflicted paths. The
effort declares the deliverables under `## Deliverables` below, at the human's word, and an implementation node that names one lands as `## Deliverables` in the manager contract says. Nothing is pushed without the human's word.

## Deliverables

The human, `verbatim`, 2026-11-12: *"ah, then yes to 1 and 2. That lands as a separate deliverable.
decide yourself on flag at the gate is its own deliverable.
And the manager self-decisions is its own deliverable too."*

- own-choices · branch `own-choices` · base: upstream `master`
- you-decide-on-a-flag · branch `you-decide-on-a-flag` · base: deliverable own-choices
- explain-a-relayed-question · branch `explain-a-relayed-question` · base: upstream `master`

`own-choices` holds [node 07](nodes/07-write-the-rule-for-what-the-manager-settles-on-its-own.md) and [node 08](nodes/08-add-the-amendment-flag-marker.md). `you-decide-on-a-flag` holds [node 06](nodes/06-write-the-you-decide-rule-for-a-flag.md). It is based on `own-choices` because node 06 is blocked on node 08. `explain-a-relayed-question` holds the work of [node 03](nodes/03-the-managers-explanation-of-a-relayed-question.md). The upstream base is the default, because the landing policy names none.

The human, `verbatim`, 2026-11-12: *"push them and open PRs, referring to #1 on them."* All three branches were pushed that day, and the manager opened their pull requests: `own-choices` as #2 against `master`, `you-decide-on-a-flag` as #3 against `own-choices`, and `explain-a-relayed-question` as #4 against `master`. Propose a region cleanup for each when the human says it has merged.

The human, `verbatim`, 2026-11-12: *"you may ship own-choices, then rebase you-decide-on-a-flag, force-push it then ship it too. (Squash-and-merge, with deletion of the corresponding remote feature branches by github, in such a way that they can be restored - I assume the CLI allows this?)"* The manager squash-merged #2 as `33f1d64` and, after rebasing `you-decide-on-a-flag` onto it as `88432da` and force-pushing, #3 as `d534d1a`. Both remote branches are deleted and restorable from their pull requests. The main checkout's `master` is at `d534d1a`. [Node 10](nodes/10-explain-only-from-what-the-manager-already-holds.md) adds a commit to `explain-a-relayed-question` (#4). The human said, `verbatim`: *"yes push"*. The manager pushed it as `4fca813`. A local test merge onto `master` at `d534d1a` succeeds with no conflict. [Node 11](nodes/11-explain-in-own-words-without-inventing.md) and [node 12](nodes/12-explain-rule-says-only-what-not-to-do.md) then added two more commits, pushed under standing yes 2, ending at `48104f3`. The human, `verbatim`: *"Okay good, please squash and merge it and delete the branch like the others, and then commit all the scratch files after your work, adding a "resolves #1" comment in the commit message so that also resolves #1, and push it"*. The manager squash-merged #4 as `3eb54c2`, its remote branch deleted and restorable from #4. All three deliverables have merged. ~~Their local branches remain until a region cleanup removes them.~~ The human, `verbatim`: *"cleanup the branches that were merged - we have them on github anyway"*. The manager checked that each branch's tree matched its squash commit, then deleted the local branches `own-choices`, `you-decide-on-a-flag` and `explain-a-relayed-question` and their config entries.

## Not yet specified

- Example 8 of [issue-1.md](issue-1.md): agents working in a sibling worktree never load the scoped
  `AGENTS.md` and `CLAUDE.md` files that govern the code they edit. The human is trying a fix in a host
  project's own instructions first. Whether the skill needs a change waits on that trial.

## Out of scope
